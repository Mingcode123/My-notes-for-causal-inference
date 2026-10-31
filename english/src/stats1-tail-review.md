# Independent fidelity review: STATS 361, source pages 40–58

Reviewed `stats1-tail.tex` against all 19 rendered original pages, including the supplementary left pages. This is a source-fidelity review, not a replacement exposition or verification of the author's mathematical claims. Three corrections are needed; no other material omission or transcription error was found in this pass.

## Required corrections

1. **Page 41, red margin after the closed-form synthetic DID estimator.** The handwriting clearly reads `与 T_0 与 n 有关`: related to / depends on T_0 and n. The current text incorrectly reads the symbols as Pi_0 and Pi_1 and marks them unclear. Replace with: **“The red margin notes that this expression depends on T_0 and n.”** Magnified evidence: `tmp/pdfs/stats1/review-tail-41.png`.

2. **Page 50, blue bottom margin on nonparametric IV.** The visible wording explicitly says `(9.15) 很复杂，用 (9.17) 而付出正则化`: (9.15) is complicated; using (9.17) comes at the cost of regularization. The current “Bottom-margin interpretation” retains the consistency requirement but omits this regularization tradeoff and substitutes an explanatory statement about minimizing the loss for each coefficient. Preserve the author's point with wording such as: **“Consistency for g requires conditions. Equation (9.15) is complicated; using (9.17) comes with a regularization tradeoff.”** The final bottom-edge line is genuinely clipped, so retain the uncertainty statement for that line. Magnified evidence: `tmp/pdfs/stats1/review-tail-50.png`.

3. **Page 53, parenthesis immediately after defining Q_i'(p).** This is a substantive mathematical aside, not an explanation of the index i. The legible beginning/end read `不必微，因为 Q_i(.) 已 [monotonicity arrow]，因此分布导数必存在`: differentiability is unnecessary; Q_i is already monotone, so a distributional derivative exists. Suggested replacement: **“Parenthetical note: ordinary differentiability is not essential; since Q_i is monotone, a distributional derivative exists.”** The shorthand arrow's direction is less clear than the surrounding words; translating it as “monotone” is supported by the preceding explicit demand-curve assumption and avoids silently interpreting the arrow as a direction inconsistent with that assumption. Magnified evidence: `tmp/pdfs/stats1/review-tail-53.png`.

## Complete page inventory and ordering check

| Original page | Review result |
| --- | --- |
| 40 | Matrix/interactive-fixed-effects intuition and clustering postscript retained; correctly attached after main p41. |
| 41 | Main synthetic-control/DID formulas retained; red-margin symbol correction required above. |
| 42 | Doubly robust panel-weight intuition and constraints retained; correctly paired with main p43. |
| 43 | Main weighted estimator and comparison retained. |
| 44 | IV exogeneity, relevance, exclusion explanations retained; attached to p45. |
| 45 | Main IV setup and estimator retained. |
| 46 | Conditional IV, nuisance-learning/double-robustness intuition and independent-product variance retained. |
| 47 | Main asymptotic/optimal-IV expressions retained. Source's questionable n versus square-root-n multiplier and argmin covariance-squared/variance choice are explicitly flagged rather than silently corrected. |
| 48 | Estimating-equation/delta-method supplement retained. |
| 49 | Overfit-instrument/noise example and cross-fitting/MSE-consistency reasoning retained. |
| 50 | Main basis-regression formulas retained; restore author's blue regularization tradeoff above. |
| 51 | Compliance table, Bayes/LATE derivation and personal IATE comment retained; appropriately follows main p52. |
| 52 | Main binary-IV/LATE setup retained. |
| 53 | Supply/demand formulas, causal chain and Fubini derivation retained; replace incorrect reading of distributional-derivative parenthesis above. |
| 54 | Weighted jump/continuous-cutoff illustration and explanatory meaning retained; attached to main p55. |
| 55 | Main threshold model and continuous/jump distinction retained. The source's monotonicity sign inconsistency and absolutely-continuous representation caveat are transparently noted. |
| 56 | Distributional-derivative question and Dirac-delta definition retained; attached to p57. |
| 57 | Jump/continuous weighted representation retained. Source numerator discrepancy is identified in the translator's note. |
| 58 | MTE chain-rule derivation retained. |

No changes were made to `stats1-tail.tex` by the reviewer. The parent agent owns the final corrections and PDF rebuild.

## Resolution

The root editor verified the reported source-reading corrections and applied them to the final LaTeX body before the final build. No reported content fix remains pending.
