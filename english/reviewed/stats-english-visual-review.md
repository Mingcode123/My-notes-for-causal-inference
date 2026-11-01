# STATS361 English final visual review

Reviewed artifact: repository-root `STATS361-English.pdf`, 76 physical pages, using `tmp/pdfs/reviewed-build/stats-en-final-01.png` through `76.png` and all seven `stats-en-contact-*.jpg` overview sheets. Physical page numbers below count the cover as page 1; printed footer numbers are one lower after the cover.

## Coverage

- Viewed all seven overview sheets, covering all 76 pages.
- Enlarged physical pages 9, 14, 15, 20, 23, 24, 28, 33, 38, 41, 45, 47, 48, 49, 56, 59, 60, 61, 62, 64, 70, 71, 72, 73, 75, and 76.
- Individually viewed all 12 assets, `english/reviewed/assets/STATS361-English-figure-001.png` through `012.png`.
- Focused on arrows, figure labels, dense equations, cross-page review notes, and heading placement.

## Findings requiring a small layout fix

1. **Physical page 64 / footer 63: run-in heading collides with arrow layout.** Near the bottom, “My left-page mnemonic.” runs directly into the red arrow-source text, without a separating space. The arrow is pushed to the far-right edge, while its target (“The three do-calculus rules above.”) wraps onto the next line at the left. Source: `english/reviewed/src/stats2-body.tex`, approximately lines 673–674, `\\paragraph{My left-page mnemonic.}` immediately followed by `\\notearrow{red}`. Use a separate block heading before this arrow.

2. **Physical page 70 / footer 69: the same heading/arrow collision.** At the top, “My intuition about this bound.” runs into “The gap … in the denominator.” The arrow is pushed to the right, and its target (“Closer arms …”) begins on the following line at the left. Source: `english/reviewed/src/stats2-body.tex`, approximately lines 869–870, `\\paragraph{My intuition about this bound.}` followed by the first red arrow. Use the same block-heading fix.

Both were reported to the root agent. No source or PDF was edited by this reviewer.

## Otherwise

- No figure-label overlaps or clipping were found in the 12 standalone figure assets.
- The enlarged dense equations fit the page. No cropped formulas, missing glyphs, or orphaned section headings were observed.
- Arrow labels and targets are clear on the other enlarged pages.
- Physical page 49 has substantial whitespace after the end of the preceding proof, before Lecture 11 starts on page 50. This is a cosmetic chapter-boundary choice, not missing content or an orphaned heading.
- Some review notes continue across pages, including pages 61–62. Their continuation remains readable and correctly colored; this did not require correction.

Status: visual review complete; the two run-in heading/arrow cases need targeted confirmation after the root agent's layout adjustment.


Final integration update: the two run-in headings before annotation arrows were converted to separate block headings in the build pipeline. Physical pages 64 and 70 were re-rendered and visually checked; both arrow columns now display correctly. The IV-list lead-in was also moved immediately before its list in both languages.
