# Independent review of Brave2 original-note findings

Scope: the seven `original` findings in `brave2-findings.json`. Original scan pages 2, 3, 4, 6, 8, 10, and 13 were visually checked. This is a targeted second review, not another full review of all 14 pages.

## Result

No finding needs to be withdrawn. One qualification is recommended for B2-004.

| Finding | Scan evidence and assessment |
| --- | --- |
| B2-002 | The blue prose on page 2 broadly says all characteristics are controlled. The restriction to additive unit-invariant effects and common time effects is warranted. A generous reading could treat the source as shorthand, but the correction accurately states the mathematical limitation. |
| B2-004 | Both displays omit the grand mean. The zero-based inclusive endpoints conflict with the denominators. The corrected balanced-panel residual is right. Add the slope-invariance caveat below. |
| B2-007 | The page-3 event-study display is introduced through TWFE but omits the common time effect; tail indices are inconsistent. The complete displayed specification is a justified correction. |
| B2-009 | Page-4 sums repeatedly multiply coefficients by the same observation-level treatment indicator and reuse observation indices. Explicit cohort-by-calendar-time indicators repair actual source notation. |
| B2-012 | Strict positivity is visible. Pages 8 and 10 additionally write an individual weight equal to one where a sum-to-one constraint is intended. The closed nonnegative simplex is the appropriate standard constraint. |
| B2-013 | Page 10 really instructs adding a row of ones to the treated pre-period outcome vector. The intercept belongs in the unit-weight design matrix as a column of ones. The separate page-8 time-weight row-vector convention is correctly distinguished. |
| B2-021 | Page 13 labels the finite categorical inverse-probability expression as continuous. The distinction between point probabilities and a continuous conditional density is correct. |

## Recommended addition to B2-004

> Omitting the grand mean shifts each transformed variable by a constant. If the subsequent regression includes an intercept, its slope is unchanged; the expression is nevertheless not the zero-mean fixed-effect residual. Without that intercept, the omission can change the slope.

Reason: the source transformation equals the correct residual minus the grand mean of the variable. OLS with an intercept is invariant to separate constant shifts in the outcome and regressor. Thus this is a projection/centering error, but its consequence for an implemented coefficient depends on the subsequent intercept.

## Primary references consulted

- [The Diff-in-Diff Saga](https://matheusfacure.github.io/python-causality-handbook/24-The-Diff-in-Diff-Saga.html)
- [Synthetic Diff-in-Diff](https://matheusfacure.github.io/python-causality-handbook/25-Synthetic-Diff-in-Diff.html)
- [Debiasing with Propensity Score](https://matheusfacure.github.io/python-causality-handbook/Debiasing-with-Propensity-Score.html)

No Brave2 source or finding was edited by this review. Brave1 reviewed artifacts remain frozen.
