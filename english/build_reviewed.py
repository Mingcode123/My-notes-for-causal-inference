"""Build the two reviewed books as self-contained LaTeX, Markdown, HTML, and PDF.

Usage: python english/build_reviewed.py [brave|stats] [--pandoc PATH]
Requires XeLaTeX, Poppler (pdftoppm), Pandoc, and Pillow. Source PDFs are never changed.
Markdown keeps editable mathematics and color spans; GitHub removes CSS colors, so
its visible labels and PNG diagrams remain useful. The PDF is the color reference.
"""
from pathlib import Path
import argparse, hashlib, json, re, shutil, subprocess, sys
from PIL import Image, ImageChops
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'english/reviewed'
BUILD=ROOT/'tmp/pdfs/reviewed-build'
PDF=ROOT/'output/pdf'
COLORS={'blue':'#244DA8','red':'#C92B32','black':'#000000','ReviewPurple':'#7A2B91','ReviewOrange':'#B45A00'}
BOOKS={
 'brave': dict(stem='Brave-and-True-Reviewed',title='Causal Inference for the Brave and True',subtitle='Chapters 1--25 and Appendix',short='Brave and True',parts=['brave1-body.tex','brave2-body.tex'],audits=['brave1','brave2'],pages=54),
 'stats': dict(stem='STATS361-Reviewed',title='STATS 361: Causal Inference',subtitle='Lectures 1--14',short='STATS 361',parts=['stats1-body.tex','stats1-tail.tex','stats2-body.tex'],audits=['stats1','stats2'],pages=89)
}
def run(args,cwd=None,stdin=None):
 p=subprocess.run([str(a) for a in args],cwd=cwd,input=stdin,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',errors='replace')
 if p.returncode: raise RuntimeError('Command failed: '+str(args[0])+'\n'+p.stdout[-5000:]+'\n'+p.stderr[-3000:])
 return p.stdout,p.stderr

def tex_compile(path,passes=3):
 for n in range(passes):
  p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',path.name],cwd=path.parent,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',errors='replace')
  (path.parent/(path.stem+f'-run{n+1}.txt')).write_text(p.stdout,encoding='utf-8')
  if p.returncode: raise RuntimeError(p.stdout[-7000:])
 return path.with_suffix('.pdf')

def title_tex(b):
 return r'''\begin{titlepage}\thispagestyle{empty}
\vspace*{14mm}{\small\sffamily MING'S PERSONAL STUDY NOTES\par}\vspace{10mm}
{\Huge\sffamily\bfseries '''+b['title']+r'''\par}\vspace{8mm}
{\LARGE\sffamily '''+b['subtitle']+r'''\par}\vspace{10mm}
{\large Reviewed English edition\par}\vfill
\textbf{Reading this edition}\par
The author's explanations, intuitions, questions, and marginal supplements are preserved alongside the lecture material. Scan references use one-based PDF page numbers. Reading order follows topics and drawn links, including left-page additions to right-page notes. The English layout is reflowed; reconstructed curves are schematic, not numerical data.\par
\textcolor{black}{Black}, \inkred{red}, and \inkblue{blue} reproduce the original pen-color categories. Arrows preserve the relation between an annotation and its target. These colors do not indicate editorial judgments.\par
\textcolor{ReviewPurple}{\textbf{Purple: a mistake present in the original handwritten note.}} The source claim is preserved and the correction is placed beside it.\par
\textcolor{ReviewOrange}{\textbf{Orange: a qualification, missing assumption, unclear reading, or unresolved point.}} This does not necessarily mean the original statement is false.\par
Recognition and translation mistakes are corrected directly; the audit files record them without adding colored error boxes. Editorial comments are separate from the author's voice. The source scans remain unchanged.\par
\textbf{Coverage:} '''+str(b['pages'])+r''' scanned pages, merged by textbook. The companion findings and coverage files document the review and primary references.\par
\vspace{6mm}{\small Prepared 31 October 2026\par}
\end{titlepage}\tableofcontents\clearpage
'''

def brace(text,pos):
 while pos<len(text) and text[pos].isspace():pos+=1
 if pos>=len(text) or text[pos]!='{': raise ValueError('Expected argument near '+text[pos:pos+70])
 depth=1;i=pos+1
 while i<len(text):
  if text[i]=='\\': i+=2;continue
  if text[i]=='{':depth+=1
  elif text[i]=='}':
   depth-=1
   if depth==0:return text[pos+1:i],i+1
  i+=1
 raise ValueError('Unbalanced argument')

def replace_commands(s,name,n,callback):
 pattern=re.compile(r'\\'+re.escape(name)+r'(?![A-Za-z])')
 pieces=[];end=0
 for m in pattern.finditer(s):
  if m.start()<end:continue
  args=[];pos=m.end()
  for _ in range(n):a,pos=brace(s,pos);args.append(a)
  pieces.append(s[end:m.start()]);pieces.append(callback(*args));end=pos
 pieces.append(s[end:]);return ''.join(pieces)

def environments(s,name,n,callback):
 token='\\begin{'+name+'}';ending='\\end{'+name+'}'
 while token in s:
  start=s.index(token);pos=start+len(token);args=[]
  for _ in range(n):a,pos=brace(s,pos);args.append(a)
  end=s.index(ending,pos)
  s=s[:start]+callback(*args,s[pos:end])+s[end+len(ending):]
 return s

def markdown_latex(body,b,assets):
 figs=[]
 def fig(m):
  figs.append(m.group(0));return '\\includegraphics{assets/'+b['stem']+f'-figure-{len(figs):03}.png'+'}'
 s=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',fig,body,flags=re.S)
 s=environments(s,'reviewnote',4,lambda kind,ident,title,source,content:
   '\\begin{quote}\nREVIEW'+('PURPLE' if kind=='original' else 'ORANGE')+'MARK\n\\textbf{'+('Original-note correction' if kind=='original' else 'Qualification / unresolved point')+' ('+ident+'): '+title+'}\\par\n\\textit{Source: '+source+'}\\par\n'+content+'\n\\end{quote}')
 s=environments(s,'inkblock',1,lambda c,content:'\\begin{quote}\nINK'+c.upper()+'MARK\n'+content+'\n\\end{quote}')
 s=replace_commands(s,'notearrow',3,lambda c,a,t:'\\begin{quote}\\textcolor{'+c+'}{'+a+'} \\(\\textcolor{'+c+'}{\\longrightarrow}\\) '+t+'\\end{quote}')
 for c in ('blue','red'):
  s=replace_commands(s,'ink'+c,1,lambda a,c=c:'\\textcolor{'+c+'}{'+a+'}')
 s=replace_commands(s,'sourcepages',1,lambda a:'\\par\\textit{Scan reference: '+a+'}\\par')
 if figs:
  assets.mkdir(parents=True,exist_ok=True)
  figtex=BUILD/(b['stem']+'-figures.tex')
  fhead=r'''\documentclass[tikz,border=4pt,multi=tikzpicture]{standalone}
\usepackage{fontspec}\setmainfont{TeX Gyre Pagella}\setsansfont{TeX Gyre Heros}
\usepackage{amsmath,amssymb,mathtools,bm,xcolor,graphicx,needspace}
\usetikzlibrary{arrows.meta,positioning,calc,decorations.pathreplacing}
'''+(SRC/'macros.tex').read_text(encoding='utf-8-sig')
  figtex.write_text(fhead+'\n\\begin{document}\n'+'\n'.join(figs)+'\n\\end{document}',encoding='utf-8')
  figpdf=tex_compile(figtex,1)
  run(['pdftoppm','-r','180','-png',figpdf,BUILD/(b['stem']+'-fig')])
  outputs=sorted(BUILD.glob(b['stem']+'-fig-*.png'))
  if len(outputs)!=len(figs):raise RuntimeError('Figure page count mismatch')
  for i,p in enumerate(outputs,1):
   im=Image.open(p).convert('RGB')
   # Trim only white outer margins; retain the full source diagram.
   box=ImageChops.difference(im,Image.new('RGB',im.size,'white')).getbbox()
   if box:im=im.crop((max(0,box[0]-6),max(0,box[1]-6),min(im.width,box[2]+6),min(im.height,box[3]+6)))
   im.save(assets/(b['stem']+f'-figure-{i:03}.png'))
 return s,len(figs)

def text_content(x):
 if isinstance(x,list):return ''.join(text_content(y) for y in x)
 if isinstance(x,dict):
  if x.get('t')=='Str':return x['c']
  if x.get('t') in ('Space','SoftBreak','LineBreak'):return ' '
  return text_content(x.get('c',[]))
 return ''

def adjust_ast(x):
 if isinstance(x,list):return [adjust_ast(y) for y in x]
 if not isinstance(x,dict):return x
 x={k:adjust_ast(v) for k,v in x.items()}
 if x.get('t')=='BlockQuote' and x['c']:
  p=x['c'][0]
  if p.get('t') in ('Para','Plain') and p['c'] and p['c'][0].get('t')=='Str':
   marker=p['c'][0]['c'];styles={
    'REVIEWPURPLEMARK':('ReviewPurple','Original-note correction'),
    'REVIEWORANGEMARK':('ReviewOrange','Qualification / unresolved point'),
    'INKBLUEMARK':('blue','Original blue ink'),
    'INKREDMARK':('red','Original red ink'),
    'INKBLACKMARK':('black','Original black ink')}
   if marker in styles:
    c,label=styles[marker];p['c']=p['c'][1:]
    while p['c'] and p['c'][0].get('t') in ('Space','SoftBreak'):p['c'].pop(0)
    if not p['c']:x['c'].pop(0)
    return {'t':'Div','c':[['',['review-note' if marker.startswith('REVIEW') else 'original-ink'],[['style','color: '+COLORS[c]],['data-ink',c],['aria-label',label]]],x['c']]}
 if x.get('t')=='Span':
  attrs=x['c'][0][2]
  for a in attrs:
   if a[0]=='style':
    for color,hexval in COLORS.items():
     if a[1]=='color: '+color:a[1]='color: '+hexval
 if x.get('t')=='RawInline' or x.get('t')=='RawBlock':
  if x['c'][0]=='tex' and x['c'][1].strip() not in ('','\\smallskip','\\medskip','\\clearpage','\\newpage'):
   print('Retained raw TeX:',x['c'][1][:120])
 return x

def build(key,pandoc):
 b=BOOKS[key];print('Building',b['stem'],flush=True)
 body='\n\\clearpage\n'.join((SRC/'src'/f).read_text(encoding='utf-8-sig') for f in b['parts'])
 body=re.sub(r'\\paragraph\{([^{}\n]*)\}\s*(?=\\notearrow)',lambda m:r'\par\Needspace{7\baselineskip}\noindent\textbf{'+m[1]+r'}\par\smallskip'+'\n',body)
 body=body.replace(r'\par\smallskip\textit{',r'\par\nobreak\smallskip\textit{').replace(r'\par\smallskip{\small\textit{',r'\par\nobreak\smallskip{\small\textit{')
 body=re.sub(r'(?m)^(\\(?:sub)?section\{[^\n]+\}\n\\sourcepages\{)',lambda m:r'\Needspace{9\baselineskip}'+'\n'+m[0],body)
 body=body.replace(r'\par\smallskip\textit{Reference:',r'\par\nobreak\smallskip\textit{Reference:').replace(r'\par\smallskip{\small\textit{References:',r'\par\nobreak\smallskip{\small\textit{References:')
 pre=(SRC/'preamble-base.tex').read_text(encoding='utf-8-sig')+(SRC/'macros.tex').read_text(encoding='utf-8-sig')
 if b.get('lang')=='zh':pre=pre.replace('pdflang={en}','pdflang={zh-CN}')
 tex='\\newcommand{\\shorttitle}{'+b['short']+'}\n'+pre+'\n\\hypersetup{pdftitle={'+b['title']+' - Reviewed English notes}}\n\\begin{document}\n'+title_tex(b)+body+'\n\\end{document}\n'
 canonical=SRC/(b['stem']+'.tex');canonical.write_text(tex,encoding='utf-8')
 work=BUILD/canonical.name;work.write_text(tex,encoding='utf-8')
 pdf=tex_compile(work)
 shutil.copy2(pdf,PDF/pdf.name)
 mtex,nfigs=markdown_latex(body,b,SRC/'assets')
 (BUILD/(b['stem']+'-markdown-input.tex')).write_text(mtex,encoding='utf-8')
 asttext,err=run([pandoc,'-f','latex','-t','json'],stdin=mtex)
 (BUILD/(b['stem']+'-pandoc.log')).write_text(err,encoding='utf-8')
 ast=adjust_ast(json.loads(asttext))
 (BUILD/(b['stem']+'-ast.json')).write_text(json.dumps(ast,ensure_ascii=False),encoding='utf-8')
 md,err=run([pandoc,'-f','json','-t','gfm','--wrap=none'],stdin=json.dumps(ast))
 legend='# '+b['title']+'\n\n'+b['subtitle'].replace('--','–')+' · Reviewed English edition\n\n'
 legend+='Original black, red, and blue ink is retained in color spans and diagrams. Purple marks errors in the original note; orange marks qualifications or unresolved readings. Recognition and translation errors are fixed directly. Arrows show the author’s pointing relations in a reflowed English layout.\n\n'
 legend+='**Color rendering:** GitHub strips CSS colors from prose. The labeled review blocks remain readable there; use the [PDF](../../output/pdf/'+b['stem']+'.pdf) or [HTML preview]('+b['stem']+'.html) to see prose colors. Mathematical source remains editable in this Markdown file; diagram PNGs preserve the original arrow colors.\n\n'
 legend+='Source coverage: '+str(b['pages'])+' scanned pages. See the companion findings JSON and coverage Markdown for the audit trail.\n\n---\n\n'
 (SRC/(b['stem']+'.md')).write_text(legend+md,encoding='utf-8')
 # A local HTML preview makes the Markdown's color spans reviewable. Equations use MathJax.
 html,err=run([pandoc,'-f','json','-t','html5','--mathjax','--standalone','--metadata','title='+b['title']],stdin=json.dumps(ast))
 css='<style>body{max-width:960px;margin:3rem auto;padding:0 1.5rem;font:18px/1.6 Georgia,serif}img{max-width:100%;height:auto}.review-note{border-top:1px solid;border-bottom:1px solid;padding:.8em 0;margin:1.2em 0}.original-ink{margin:.6em 0}blockquote{margin-left:1.2em}h1,h2{line-height:1.25}pre{overflow:auto}</style>'
 html=html.replace('</head>',css+'</head>').replace('<body>','<body><p><strong>Color preview of the reviewed Markdown.</strong> Formulas require MathJax network access; the PDF is self-contained.</p>')
 (SRC/(b['stem']+'.html')).write_text(html,encoding='utf-8')
 log=work.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
 warnings=[l for l in log.splitlines() if any(w in l for w in ['Overfull','Missing character','LaTeX Warning','Package fancyhdr Warning'])]
 print(json.dumps({'book':key,'figures':nfigs,'arrows':body.count('\\notearrow'),'warnings':warnings},ensure_ascii=False),flush=True)
 return {'book':key,'figures':nfigs,'arrows':body.count('\\notearrow'),'warnings':warnings,'sha256':hashlib.sha256((PDF/pdf.name).read_bytes()).hexdigest()}

def main():
 p=argparse.ArgumentParser();p.add_argument('books',nargs='*',metavar='BOOK');p.add_argument('--pandoc');a=p.parse_args()
 if any(k not in BOOKS for k in a.books):p.error('BOOK must be brave or stats')
 pandoc=a.pandoc or shutil.which('pandoc')
 if not pandoc:
  found=list((ROOT/'tmp/pandoc').glob('*/pandoc.exe'));pandoc=str(found[0]) if found else None
 if not pandoc:raise SystemExit('Pandoc is required. Supply --pandoc PATH or add it to PATH.')
 BUILD.mkdir(parents=True,exist_ok=True);PDF.mkdir(parents=True,exist_ok=True)
 results=[build(k,pandoc) for k in a.books or BOOKS]
 (SRC/'build-last-run.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
if __name__=='__main__':main()
