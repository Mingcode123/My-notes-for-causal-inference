"""Verify the reviewed outputs without modifying sources. Needs pypdf and pdfplumber."""
from pathlib import Path
import json,re,collections,hashlib,sys
import pdfplumber
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'english/reviewed'
BUILD=ROOT/'tmp/pdfs/reviewed-build'
BOOKS={'STATS361-English':['stats1','stats2'],'STATS361-Chinese':['stats1','stats2'],'Brave-and-True-English':['brave1','brave2'],'Brave-and-True-Chinese':['brave1','brave2']}
if sys.argv[1:]:
 selected=set(sys.argv[1:])
 if not selected <= set(BOOKS):raise SystemExit('Unknown book: '+str(selected-set(BOOKS)))
 BOOKS={k:v for k,v in BOOKS.items() if k in selected}
COLORS={'blue':(36/255,77/255,168/255),'red':(201/255,43/255,50/255),'purple':(122/255,43/255,145/255),'orange':(180/255,90/255,0)}
report={'books':{},'source_scans':{},'checks':{},'limitations':['Scan reading and mathematical review are human/model judgments, not proof that every possible error has been found.','GitHub strips prose CSS colors; the PDF is the color reference.','English layout is reflowed; arrows retain relationships and diagrams are schematic.']}
errors=[]
for stem,keys in BOOKS.items():
 pdf=ROOT/(stem+'.pdf'); tex=ROOT/(stem+'.tex');md=ROOT/(stem+'.md')
 findings=[v for key in keys for v in json.loads((SRC/(key+'-findings.json')).read_text(encoding='utf-8-sig'))]
 ids=[v['id'] for v in findings]
 if len(ids)!=len(set(ids)):errors.append(stem+': duplicate finding ID')
 text=tex.read_text(encoding='utf-8-sig');markdown=md.read_text(encoding='utf-8-sig')
 visible=re.findall(r'\\begin\{reviewnote\}\{([^}]+)\}\{([^}]+)\}',text)
 visible_ids={i for _,i in visible}
 expected={v['id'] for v in findings if v['type']!='transcription'}
 if visible_ids!=expected:errors.append(stem+': review box IDs differ: '+str(visible_ids^expected))
 for v in findings:
  if v['type']=='transcription' and v['id'] in visible_ids:errors.append(v['id']+': direct repair incorrectly annotated')
 for typ,i in visible:
  expectedtype=next(v['type'] for v in findings if v['id']==i)
  if typ!=expectedtype:errors.append(i+': review color category mismatch')
 for token in ['\\notearrow','\\begin{tikzpicture}','\\begin{reviewnote}','\\inkblue','\\inkred','REVIEWPURPLEMARK','INKBLUEMARK']:
  if token in markdown:errors.append(stem+': unresolved Markdown macro '+token)
 images=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',markdown)
 if len(images)!=text.count(r'\begin{tikzpicture}'):errors.append(stem+': Markdown diagram count differs from LaTeX')
 if markdown.count(r'\longrightarrow')<text.count(r'\notearrow{'):errors.append(stem+': Markdown annotation arrow is missing')
 for img in images:
  if not (ROOT/img).is_file():errors.append(stem+': missing diagram '+img)
 pdftext=[];bounds=[];counts=collections.Counter();blank=[]
 with pdfplumber.open(pdf) as doc:
  for n,page in enumerate(doc.pages,1):
   tx=page.extract_text() or '';pdftext.append(tx)
   if len(tx.strip())<15:blank.append(n)
   for c in page.chars:
    if c['text'].strip() and (c['x0']<25 or c['x1']>page.width-25 or c['top']<15 or c['bottom']>page.height-20):
     bounds.append({'page':n,'text':c['text'],'bbox':[round(c[k],1) for k in ['x0','top','x1','bottom']]})
    color=c.get('non_stroking_color')
    if isinstance(color,(list,tuple)) and len(color)==3:
     for k,target in COLORS.items():
      if max(abs(float(a)-b) for a,b in zip(color,target))<.012:counts[k]+=1
  pagecount=len(doc.pages)
 if bounds:errors.append(stem+': text outside safe page bounds')
 if blank:errors.append(stem+': blank/near-blank pages '+str(blank))
 combined='\n'.join(pdftext)
 for i in expected:
  if i not in combined:errors.append(stem+': missing PDF finding '+i)
 if any(counts[c]==0 for c in COLORS):errors.append(stem+': missing expected ink color')
 log=(BUILD/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
 warnings=[line for line in log.splitlines() if any(w in line for w in ['Overfull','Missing character','LaTeX Warning','Package fancyhdr Warning'])]
 if warnings:errors.append(stem+': LaTeX warnings')
 reader=PdfReader(pdf)
 def dests(outline):
  for d in outline:
   if isinstance(d,list):yield from dests(d)
   else:yield d
 outline=list(dests(reader.outline))
 bad=[str(d.get('/Title','')) for d in outline if reader.get_destination_page_number(d) is None]
 if bad:errors.append(stem+': invalid outline destinations')
 report['books'][stem]={'pages':pagecount,'findings':dict(collections.Counter(v['type'] for v in findings)),'review_boxes':len(visible),'arrow_relations':text.count('\\notearrow{'),'markdown_diagrams':len(images),'outline_entries':len(outline),'color_character_counts':dict(counts),'safe_bounds_violations':bounds,'latex_warnings':warnings,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
manifest=json.loads((SRC/'source-manifest.json').read_text(encoding='utf-8'))
for rel,record in manifest['scans'].items():
 p=ROOT/rel;entry=dict(record);entry['present_in_current_tree']=p.exists()
 if p.exists():
  if hashlib.sha256(p.read_bytes()).hexdigest()!=record['sha256']:errors.append('Source scan changed: '+rel)
  if manifest['removed_from_current_tree']:errors.append('Source scan not removed: '+rel)
 elif not manifest['removed_from_current_tree']:errors.append('Unexpected missing scan: '+rel)
 report['source_scans'][rel]=entry
report['source_reference_commit']=manifest['source_commit']
report['scans_removed_as_requested']=manifest['removed_from_current_tree']
# Verify that the two language editions share the same structural and mathematical skeleton.
from build_reviewed import replace_commands
pattern=re.compile(r'\\\[.*?\\\]|\\begin\{(?:align\*?|equation\*?|gather\*?|multline\*?)\}.*?\\end\{(?:align\*?|equation\*?|gather\*?|multline\*?)\}',re.S)
def normalize_math(v):
 v=replace_commands(v,'text',1,lambda a:'')
 v=replace_commands(v,'tag',1,lambda a:r'\tag{'+(','.join(re.findall(r'\d+(?:\.\d+)*',a)) or a)+'}')
 return re.sub(r'\s+','',v)
report['math_comparison']='Display mathematics is compared after removing translated text labels and retaining numeric equation tags.'
report['bilingual_structure']={}
for part in ['stats1-body','stats1-tail','stats2-body','brave1-body','brave2-body']:
 en=(SRC/'src'/(part+'.tex')).read_text(encoding='utf-8-sig')
 zp=SRC/'src'/(part+'-zh.tex')
 if not zp.exists():
  report['bilingual_structure'][part]={'pending':True}
  if len(BOOKS)==4:errors.append('Missing Chinese body '+part)
  continue
 zh=zp.read_text(encoding='utf-8-sig')
 ids=lambda v:re.findall(r'\\begin\{reviewnote\}\{([^}]+)\}\{([^}]+)\}',v)
 arrows=lambda v:re.findall(r'\\notearrow\{([^}]+)\}',v)
 em=[normalize_math(v) for v in pattern.findall(en)];zm=[normalize_math(v) for v in pattern.findall(zh)]
 mismatches=[i+1 for i,(a,b) in enumerate(zip(em,zm)) if a!=b]
 structural=ids(en)==ids(zh) and arrows(en)==arrows(zh) and en.count(r'\begin{tikzpicture}')==zh.count(r'\begin{tikzpicture}')
 report['bilingual_structure'][part]={'review_ids_and_arrow_colors_match':structural,'english_display_math_blocks':len(em),'chinese_display_math_blocks':len(zm),'math_blocks_needing_review':mismatches}
 if len(BOOKS)==4 and (not structural or len(em)!=len(zm) or mismatches):errors.append('Bilingual structure/math mismatch: '+part)

report['checks']={'all_books_checked':len(BOOKS)==4,'source_pages':sum(p['pages'] for p in report['source_scans'].values()),'errors':errors,'passed':not errors}
(SRC/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
if errors:raise SystemExit(1)
