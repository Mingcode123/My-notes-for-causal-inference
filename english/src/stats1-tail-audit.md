# STATS 361, Lectures 1-10, pages 40-58: tail audit

Every source PDF page 40-58 was visually inspected at 145 dpi. This tail continues the Lecture 8 section from the other translation fragment; it starts with `Interactive panel models`, then contains Lectures 9 and 10. Append `stats1-tail.tex` after the main `stats1-body.tex` (pages 1-39). No overlap or omitted source page occurs at the boundary.

## Reconstructed reading order

41 with 40; 43 with 42; 45 with 44; 47 with 46 and the estimating-equation reminder on 48; 49; 50; 52 with 51; 53; 55 with 54; 57 with 56; 58.

The material on p48 is the general estimating-equation/delta-method explanation for the asymptotic variance on p47, even though it physically faces p49. It is placed with that calculation. Supplementary left pages are integrated after the relevant main statement, never treated as independent chapter openings.

## Page inventory

| Source page | Coverage |
|---|---|
| 40 | Matrix-product diagram and non-synthetic-control alternative using k-means. Integrated with p41. |
| 41 | Interactive factor model, block-treatment matrix, synthetic weights, weighted two-way regression, closed-form effect, consistency statement. All readable formulas and annotations retained; clipped bottom text identified. |
| 42 | Two-way unbiased-weight conditions and combined doubly robust restrictions. Integrated after p43 design argument. |
| 43 | Exchangeability conditional on total treatment count, weighted estimator and full conditional-mean calculation, variance-minimizing weights. All retained. |
| 44 | Three IV conditions and instrument-to-treatment-to-outcome diagram. Integrated into p45. |
| 45 | Lecture 9 structural constant-effect model, endogeneity bias, covariance IV identification and estimator. All retained. |
| 46 | Conditional-IV extension, doubly robust and random-forest remarks; variance of independent product. Integrated with p47. |
| 47 | Optimal instruments, sample ratio, estimating equation, asymptotic variance and conditional-mean instrument. Original rate/optimization discrepancies explicitly retained. |
| 48 | Starred estimating-equation/delta-method variance reminder. Integrated with p47. |
| 49 | First-stage feasibility, overfitting warning and blue example, cross-fitting and MSE consistency. All retained. |
| 50 | Nonparametric IV model, integral equation, cross-fitted loss, basis expansion, regression form, bottom marginal intuition. Last clipped wording identified. |
| 51 | Compliance-type table, monotonicity, LATE derivation and personal note on unobserved never-taker treated outcome. Integrated after p52 setup. |
| 52 | Lecture 10, binary Wald ratio, noncompliance interpretation, IV assumptions. All retained. |
| 53 | Supply/demand setup and assumptions, derivative-weighted IV target, full Fubini derivation. All retained. |
| 54 | Cutoff jump diagram, treatment-effect strip and probability/derivative weighting. Integrated with p55 and described in prose alongside full formulas. |
| 55 | Threshold rule, uniform latent variable, IV conditions, MTE and jump/continuous decomposition, bounded-variation qualification. All retained; convention/representation caveats labeled. |
| 56 | Distributional derivative question and Dirac delta reminder. Integrated with p57 covariance proof. |
| 57 | Single/multiple jumps, compliance strata, continuous cutoff, covariance expansion and Gaussian identity. All retained; source label/formula inconsistencies flagged. |
| 58 | Marginal-treatment-effect derivative ratio and full proof via Fubini/chain rule. All retained. |

## Explicit uncertainties and source discrepancies

- P40 the short literature/page reference is unclear; not replaced by a fabricated bibliography item.
- P41 a final sentence extends below the scanned area. Readable consistency claim is translated; the missing qualification is marked clipped. The red-margin dependence on T0 and n was resolved during independent review.
- P42 a short reference is only partly legible (p67/[2019]); not expanded from outside sources.
- P47 the normal-limit multiplier appears as n rather than sqrt(n), while p48 clearly gives sqrt(n). Both literal usage and the discrepancy are explained. The objective is written argmin of covariance squared / variance although the intended optimum maximizes that ratio; this is recorded explicitly.
- P49 the blue marginal example labels two expressions equivalent without specifying conditions. The translation preserves the warning and the equations, without upgrading that assertion to a proof.
- P50 the introductory text names Z as the linear variable although the displayed equation uses W. The equation-based reading and wording discrepancy are explicit. The last bottom-edge sentence is clipped.
- P51 the marginal IATE label accompanies an expectation, leaving the individual-versus-average distinction imprecise. The ambiguity is retained.
- P53 monotonicity uses an equilibrium-price symbol in the handwriting; the intended relevant-price condition is described and the source notation noted.
- P55 increasing c together with W=1{U>=c(Z)} implies decreasing treatment with instrument. The source also says nondecreasing; that contradiction is flagged. The integral-only representation of a bounded-variation cutoff does not contain jumps; its limits are explicitly noted.
- P57 the source labels the switching stratum compliers despite the preceding increasing-cutoff convention. Labels are preserved with the sign-convention note. A numerator gap looks like z_k-c_-(z_k), whereas the general equation and denominator give c(z_k)-c_-(z_k); the consistent version is displayed and discrepancy recorded.
- All diagrams are reconstructed as equations, a table, or concrete prose about the pictured arrows/weights. No textbook content is substituted for the original intuition.

## Output

`english/src/stats1-tail.tex` is a standalone body fragment using standard LaTeX mathematics and `sourcepages`. Root builds the combined Lectures 1-10 PDF and handles final visual QA, workspace synchronization, and Git operations.

## Independent-review resolutions

- P41 red margin resolved as dependence on T0 and n (not Pi0/Pi1); body corrected.
- P50 retained the legible regularization cost in the bottom annotation; remaining clipped words remain uncertain.
- P53 corrected the parenthetical explanation: ordinary differentiability is not necessary; monotonicity gives a distributional derivative. It is not an explanation of the index i.
