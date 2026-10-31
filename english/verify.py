"""Verify source-page inventories, final PDFs, TeX logs, and TOC targets.
Run after english/build.py. Requires pypdf and pdfplumber.
"""
from pathlib import Path
import hashlib
import json
import re
import pdfplumber
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent.parent
SOURCES=[
("note_for_Causal _inference_STATS_361/Lecture1-10.pdf",58,["stats1-audit.md","stats1-tail-audit.md"]),
("note_for_Causal _inference_STATS_361/Lecture11-14.pdf",31,["stats2-audit.md"]),
("note_for_Causal_Inference_for_The_Brave_and_True/Chapter1-23.pdf",40,["brave1-audit.md"]),
("note_for_Causal_Inference_for_The_Brave_and_True/Chapter24-25.pdf",14,["brave2-audit.md"]),
]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
report={"prepared_date":"2026-10-31","source_pages":0,"english_pages":0,"sources":[],"outputs":[]}
for rel,count,audits in SOURCES:
    path=ROOT/rel
    assert len(PdfReader(path).pages)==count
    covered=set()
    for audit in audits:
        text=(ROOT/"english/src"/audit).read_text(encoding="utf-8-sig")
        covered.update(map(int,re.findall(r"^\|\s*(\d+)\s*\|",text,re.M)))
    assert covered==set(range(1,count+1)),(rel,sorted(set(range(1,count+1))-covered))
    report["source_pages"]+=count
    report["sources"].append({"path":rel,"pages":count,"sha256":sha(path),"audit_page_coverage":"complete"})
outputs=sorted((ROOT/"output/pdf").glob("*-English.pdf"))
assert len(outputs)==4
for path in outputs:
    reader=PdfReader(path)
    problems=[]
    with pdfplumber.open(path) as doc:
        for n,page in enumerate(doc.pages,1):
            assert page.chars,("Empty PDF text",path.name,n)
            for c in page.chars:
                if c["x0"]<35 or c["x1"]>page.width-35 or c["top"]<15 or c["bottom"]>page.height-15:
                    problems.append({"page":n,"character":c["text"]})
    assert not problems,(path.name,problems)
    log=(ROOT/"tmp/pdfs/build"/(path.stem+".log")).read_text(encoding="utf-8",errors="replace")
    warnings=[line for line in log.splitlines() if "Overfull" in line or "Missing character" in line]
    assert not warnings,(path.name,warnings)
    toc=(ROOT/"tmp/pdfs/build"/(path.stem+".toc")).read_text(encoding="utf-8")
    entries=re.findall(r"\}\{(\d+)\}\{([^{}]+)\}",toc)
    assert entries,(path.name,"Missing TOC")
    dests=reader.named_destinations
    for printed,dest in entries:
        assert dest in dests,(path.name,dest)
        # Cover page is not numbered; printed page equals zero-based PDF index.
        assert reader.get_destination_page_number(dests[dest])==int(printed),(path.name,printed,dest)
    report["english_pages"]+=len(reader.pages)
    report["outputs"].append({"path":path.relative_to(ROOT).as_posix(),"pages":len(reader.pages),"sha256":sha(path),"searchable_text":True,"safe_page_bounds":"pass","tex_overflow_and_missing_glyph_check":"pass","toc_entries_verified":len(entries)})
report["limitations"]="Ambiguous/clipped handwriting and source notation discrepancies remain explicitly marked in the translation and source-order audits."
(ROOT/"english/verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
