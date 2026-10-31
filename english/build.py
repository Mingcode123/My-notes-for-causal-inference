"""Build the four English PDFs from their editable LaTeX source.
Requires Python 3 and XeLaTeX (TeX Live with the packages in src/preamble.tex).
Run from any directory: python english/build.py
"""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "english" / "src"
BUILD = ROOT / "tmp" / "pdfs" / "build"
OUT = ROOT / "output" / "pdf"
VOLUMES = [
    ("stats1", "STATS361-Lectures1-10-English", "STATS 361: Causal Inference", "Lectures 1--10", "STATS 361 / Lectures 1--10", ["stats1-body.tex", "stats1-tail.tex"], "Lecture1-10.pdf", 58),
    ("stats2", "STATS361-Lectures11-14-English", "STATS 361: Causal Inference", "Lectures 11--14", "STATS 361 / Lectures 11--14", ["stats2-body.tex"], "Lecture11-14.pdf", 31),
    ("brave1", "Brave-and-True-Chapters1-23-English", "Causal Inference for the Brave and True", "Chapters 1--23", "Brave and True / Chapters 1--23", ["brave1-body.tex"], "Chapter1-23.pdf", 40),
    ("brave2", "Brave-and-True-Chapters24-25-English", "Causal Inference for the Brave and True", "Chapters 24--25 and Appendix", "Brave and True / Chapters 24--25", ["brave2-body.tex"], "Chapter24-25.pdf", 14),
]

def document(title, subtitle, short, bodies, source, pages):
    body = "\n".join((SRC / name).read_text(encoding="utf-8-sig") for name in bodies)
    return (
        "\\newcommand{\\shorttitle}{" + short + "}\n"
        + (SRC / "preamble.tex").read_text(encoding="utf-8-sig")
        + "\\hypersetup{pdftitle={" + title + " - " + subtitle + "}}\n"
        + "\\begin{document}\n\\begin{titlepage}\n\\thispagestyle{empty}\n"
        + "\\vspace*{18mm}\n{\\small\\sffamily\\color{muted}MING'S PERSONAL STUDY NOTES\\par}\n\\vspace{12mm}\n"
        + "{\\Huge\\sffamily\\bfseries\\color{ink}" + title + "\\par}\n\\vspace{7mm}\n"
        + "{\\LARGE\\sffamily " + subtitle + "\\par}\n\\vspace{12mm}\n"
        + "{\\large English translation of the handwritten notebook\\par}\n\\vfill\n"
        + "\\textbf{How to read this edition}\\par\n"
        + "The translation follows the handwritten notes, including explanations, intuitions, questions, derivations, and marginal additions. "
        + "Main pages and their supplements are joined by topic and by the arrows in the scans, rather than by a fixed odd/even page rule.\\par\n"
        + "Scan references use one-based PDF page numbers. Author annotations preserve remarks visible in the notebook; they do not claim independent verification that a remark is absent from the textbook. "
        + "Translator's notes identify uncertain handwriting or apparent source notation issues. They are separate from the author's notes. "
        + "This is a translation, not a replacement textbook or a mathematical errata edition.\\par\n"
        + "\\textbf{Source:} \\texttt{" + source + "}, " + str(pages) + " scanned pages. "
        + "The accompanying source-order audit records page coverage and unresolved readings.\\par\n"
        + "\\vspace{8mm}{\\small\\sffamily Prepared 31 October 2026\\par}\n"
        + "\\end{titlepage}\n\\tableofcontents\n\\clearpage\n"
        + body + "\n\\end{document}\n"
    )

def main():
    exe = shutil.which("xelatex")
    if not exe:
        raise SystemExit("XeLaTeX is required; install TeX Live and add xelatex to PATH.")
    BUILD.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    selected = set(sys.argv[1:])
    for key, stem, title, subtitle, short, bodies, source, pages in VOLUMES:
        if selected and key not in selected:
            continue
        missing = [name for name in bodies if not (SRC / name).exists()]
        if missing:
            raise SystemExit("Missing sources: " + ", ".join(missing))
        tex = BUILD / (stem + ".tex")
        tex.write_text(document(title, subtitle, short, bodies, source, pages), encoding="utf-8")
        for run in range(3):
            result = subprocess.run(
                [exe, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", tex.name],
                cwd=BUILD, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                encoding="utf-8", errors="replace"
            )
            (BUILD / (stem + f"-run{run+1}.txt")).write_text(result.stdout, encoding="utf-8")
            if result.returncode:
                print(result.stdout[-6500:])
                raise SystemExit(result.returncode)
        log = (BUILD / (stem + ".log")).read_text(encoding="utf-8", errors="replace")
        warnings = [line for line in log.splitlines() if any(s in line for s in ["Overfull", "Missing character", "LaTeX Warning", "Package fancyhdr Warning"])]
        shutil.copy2(BUILD / (stem + ".pdf"), OUT / (stem + ".pdf"))
        print(stem + ".pdf")
        for line in warnings:
            print("  " + line)
if __name__ == "__main__":
    main()
