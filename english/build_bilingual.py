"""Build root-level English and Chinese editions. Requires the same tools as build_reviewed.py."""
from pathlib import Path
import argparse,json,shutil,re
import build_reviewed as core
ROOT=core.ROOT
SRC=core.SRC
core.PDF=ROOT
for key in ('brave','stats'):
 core.BOOKS[key]['stem']=core.BOOKS[key]['stem'].replace('-Reviewed','-English')
 z=dict(core.BOOKS[key]);z['parts']=[f.replace('.tex','-zh.tex') for f in z['parts']];z['lang']='zh';z['stem']=z['stem'].replace('-English','-Chinese')
 if key=='brave':z.update(title='因果推断学习笔记：Brave and True',subtitle='第1至25章与附录',short='Brave and True / 中文')
 else:z.update(title='STATS 361：因果推断笔记',subtitle='第1至14讲',short='STATS 361 / 中文')
 core.BOOKS[key+'-zh']=z
old_title=core.title_tex

def title(b):
 if b.get('lang')!='zh':
  return old_title(b).replace('The source scans remain unchanged.','The original scans were unchanged during review and are removed from the current tree after verification at the author\'s request.')
 return r'''\def\ChineseEdition{1}
\renewcommand{\contentsname}{目录}

\fancyhead[R]{\small\sffamily 校订笔记}
\renewcommand{\sourcepages}[1]{\par{\small\sffamily\color{muted}\textbf{原扫描页码：} #1\par}\nobreak\smallskip\nopagebreak[4]}
\begin{titlepage}\thispagestyle{empty}
\vspace*{14mm}{\small\sffamily MING的个人学习笔记\par}\vspace{10mm}
{\Huge\sffamily\bfseries '''+b['title']+r'''\par}\vspace{8mm}
{\LARGE\sffamily '''+b['subtitle']+r'''\par}\vspace{10mm}
{\large 中文校订排印版\par}\vfill
\textbf{阅读说明}\par
保留讲义内容、个人直觉、问题、推导与边栏补充。阅读顺序按主题、左右页接续和原箭头关系整理；来源页码为原扫描PDF中从1开始的页码。中文重新排版，图形保留关系，曲线坐标仅作示意。\par
\textcolor{black}{黑色}、\inkred{红色}、\inkblue{蓝色}对应原笔颜色。箭头连接原批注及其目标，不表示校订判断。\par
\textcolor{ReviewPurple}{\textbf{紫色：原手写笔记本身的错误。}}保留原表述，在旁边给出修正。\par
\textcolor{ReviewOrange}{\textbf{橙色：补充条件、字迹歧义或待确认问题。}}不一定表示原命题错误。\par
识别与翻译错误直接改正，仅在审计记录中说明。中英文版本使用相同校注编号和公式结构，校订说明与作者原批注明确区分。\par
本书合并整理自'''+str(b['pages'])+r'''页扫描。原扫描在核对期间保持不变，完成后按作者要求从当前目录删除；保留来源页码和审计记录以便追溯。\par
\vspace{6mm}{\small 整理于2026年10月31日\par}
\end{titlepage}\tableofcontents\clearpage
'''.replace('#1','#1')
core.title_tex=title
old_markdown=core.markdown_latex

def markdown_latex(body,b,assets):
 s,n=old_markdown(body,b,assets)
 if b.get('lang')=='zh':
  s=s.replace('Original-note correction (','原笔记纠错（').replace('Qualification / unresolved point (','补充条件／待确认（')
  s=re.sub(r'(原笔记纠错|补充条件／待确认)（([BS][12]-[0-9]+)\): ',r'\1（\2）：',s)
  s=s.replace('\\textit{Source: ','\\textit{来源：').replace('\\textit{Scan reference: ','\\textit{原扫描页码：')
 return s,n
core.markdown_latex=markdown_latex

def finish(b):
 stem=b['stem']
 shutil.move(SRC/(stem+'.tex'),ROOT/(stem+'.tex'))
 md=(SRC/(stem+'.md')).read_text(encoding='utf-8')
 md=md.replace('(assets/','(english/reviewed/assets/').replace('../../output/pdf/','').replace(']('+stem+'.html)','](english/reviewed/'+stem+'.html)')
 if b.get('lang')=='zh':
  content=md.split('\n---\n',1)[1]
  md='# '+b['title']+'\n\n'+b['subtitle']+' · 中文校订排印版\n\n黑、红、蓝对应原笔颜色。紫色标注原笔记错误；橙色标注补充条件或待确认问题。识别和翻译错误直接改正。保留原公式、个人直觉与箭头关系。\n\n**颜色显示：** GitHub会去掉正文CSS颜色；完整颜色请看[PDF]('+stem+'.pdf)或[HTML预览](english/reviewed/'+stem+'.html)。公式可直接编辑，图像保留原箭头颜色。中英文使用同一套校注编号。\n\n---\n'+content
 (ROOT/(stem+'.md')).write_text(md,encoding='utf-8');(SRC/(stem+'.md')).unlink()

def main():
 p=argparse.ArgumentParser();p.add_argument('books',nargs='*');p.add_argument('--pandoc');a=p.parse_args()
 selected=a.books or list(core.BOOKS)
 if any(k not in core.BOOKS for k in selected):p.error('Choose brave, stats, brave-zh or stats-zh')
 pandoc=a.pandoc or shutil.which('pandoc')
 if not pandoc:
  found=list((ROOT/'tmp/pandoc').glob('*/pandoc.exe'));pandoc=str(found[0]) if found else None
 if not pandoc:raise SystemExit('Supply --pandoc PATH or add Pandoc to PATH.')
 core.BUILD.mkdir(parents=True,exist_ok=True)
 results=[]
 for k in selected:
  results.append(core.build(k,pandoc));finish(core.BOOKS[k])
 (SRC/'build-last-run.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
if __name__=='__main__':main()
