# English edition

Prepared 31 October 2026 from all 143 pages of the four original scan PDFs.

## What was preserved

- Main text, equations and derivations, informal explanations, questions, warnings, and visible marginal additions.
- The meaning of diagrams, expressed as typeset schematic figures, directed edges, tables, or descriptions of axes and curves.
- The author's tentative and unfinished arguments, with their unresolved status retained.
- Source PDF page references, allowing each translated passage to be checked against the manuscript.

Author annotations and translator's notes are explicitly distinguished. Attribution of an annotation to the author means it is visible in the notebook; it does not establish whether it is absent from the underlying textbook. This is a translation, not a mathematical errata edition. Some clipped or ambiguous words remain marked rather than guessed.

## Reading-order audits

Notebook page roles were identified using binding edges, content, arrows, and continuation. There is no global odd/even-page rule.

| Source | Coverage | Audit |
|---|---|---|
| Lecture1-10.pdf | Pages 1-39 | [Main audit](src/stats1-audit.md) |
| Lecture1-10.pdf | Pages 40-58 | [Continuation audit](src/stats1-tail-audit.md) |
| Lecture11-14.pdf | Pages 1-31 | [Audit](src/stats2-audit.md) |
| Chapter1-23.pdf | Pages 1-40 | [Audit](src/brave1-audit.md) |
| Chapter24-25.pdf | Pages 1-14 | [Audit](src/brave2-audit.md) |

Examples of substantive ordering decisions:
- Chapter 13 on scan p17 precedes Chapter 14 on pp16 and18.
- The nonlinear extension on Chapter1-23 p38 precedes its facing-page procedure on p37.
- Lecture1-10 p40 is a left-page supplement to the interactive panel model on p41.
- Chapter24-25 p1 completes the assumptions on p2; p7 supplements p6; p9 follows the relevant lower portion of p10.

The audit files list uncertain readings and original notation discrepancies. These same issues are marked at the relevant points in the English PDFs.

## Files and rebuilding

PDFs are in [output/pdf](../output/pdf). Editable LaTeX fragments and the common preamble are in [src](src). The STATS 361 Lectures 1-10 volume combines the main and continuation fragments.

Install Python 3 and XeLaTeX (TeX Live). Required LaTeX packages are listed in the common preamble; fonts are TeX Gyre Pagella, TeX Gyre Heros, and Latin Modern Mono.

From the repository root:

    python english/build.py

Build a single volume by supplying stats1, stats2, brave1, or brave2:

    python english/build.py brave2

The script runs XeLaTeX three times so contents links and page numbers settle, then writes the four final PDFs. Build intermediates and rendering checks live under tmp/pdfs and are ignored by Git. The original scans are not required to rebuild the already-translated edition.

## Review

Every source scan was inspected visually. Additional independent content review covered the complete Chapters24-25 volume, the complete Lectures1-10 continuation, selected equation-heavy passages, and all identified left-page supplements in Lectures11-14. Review corrected a reversed superefficiency annotation and a group-label ambiguity.

The final checks include PDF rendering, page-layout inspection, source-page inventory coverage, missing-glyph and overflow checks, and exact file-hash comparisons between the working directory and the Git checkout. See [verification.json](verification.json) for final counts and automated checks.

The working-copy/checkout synchronization is performed only at completion. The scanned originals remain unchanged.
