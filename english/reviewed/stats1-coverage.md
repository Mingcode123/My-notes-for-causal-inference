# STATS1 comprehensive mathematical and original-ink audit

Scope: all 58 original pages of `Lecture1-10.pdf`, including supplements and personal observations, compared with the English body and tail. Every source page was visually re-inspected. The full reviewed copies are `src/stats1-body.tex` and `src/stats1-tail.tex`; 50 findings are recorded in `stats1-findings.json`. Original black/red/blue ink is independent of editorial classification: purple original-note corrections, orange qualifications; our mistaken prior translator criticism is removed directly and logged only in JSON.

The main reference is Stefan Wager, *STATS 361: Causal Inference*, Spring 2022, https://web.stanford.edu/~swager/stats361.pdf (locally downloaded PDF and text). Mathematical identities were independently derived, rather than accepted solely because they occur in the lecture. In particular, lecture (1.16), (4.6), the convex-uniqueness claim, and Lecture 10 footnote 4 also require correction. NPIV completeness was checked against Newey–Powell (2003), https://doi.org/10.1111/1468-0262.00459; panel-asymptotic context against Arkhangelsky et al. (2021), https://www.aeaweb.org/articles?id=10.1257/aer.20190159. Publisher access to the full BV chain-rule paper was unavailable; the Stieltjes correction is established directly by the displayed integration-by-parts argument and the Cantor-function counterexample.

| Lecture | Source pages | Complete audit coverage |
|---|---|---|
| 1 | 1–3 | SUTVA versus sampling, difference-in-means identification/unbiasedness, balanced allocation and centering, linear and general projection decompositions, CLTs, sandwich covariance, weak variance-reduction inequality, personal prediction interpretation. |
| 2 | 4–10 | Finite-stratum expansion and variance, population/empirical masses, propensity balancing proof and conditioning, stratification consistency, IPW consistency and overlap, potential-outcome model and exact oracle variance, personal comparison. The prior translator's assertion that the c-model coefficients were reversed was checked and rejected: the original is correct. |
| 3 | 11–16 | AIPW algebra and both robustness arguments, regular efficiency bound, split-sample independence, nuisance risk product, every remainder term, variance versus stochastic-order annotation, likelihood score versus influence function, empirical variance and confidence level. |
| 4 | 17–20 | CATE/T-learning regularization concern, Robinson residual identity, corrected sandwich, cross-fitting rates, R-loss excess-risk derivation and identification, RCT nuisance distinction, penalized objective, overlap-weighted constant-coefficient target. |
| 5 | 21–25 | RDD boundary identification, deterministic propensity and rate scope, local-linear objective/kernels, smoothness and Lipschitz definition, Taylor normalization, intercept weights and moment constraints, bias/noise rates, latent-normal running variable and deconvolution expectation. |
| 6 | 26–31 | Conditional Gaussian assumptions, exact conditional variance, symmetric bias class, affine moment constraints, normalized curvature optimization, minimax versus actual MSE, Gaussian bias-aware CI, discrete/multivariate scope, heteroskedastic weighted CLT and residual-variance caution. |
| 7 | 32–37 | IPW Cauchy–Schwarz argument, series/expectation interchange (answering author's red question), logistic calibration KKT and Hessian, existence/uniqueness qualification, arm-specific calibration, Holder/norm definitions, concentration and lasso rates, augmentation decomposition, studentization and sample/population targets. |
| 8 | 38–43 | Panel matrix orientation, constant effects/no dynamics, strict exogeneity, two-period DID and clustered variance, general TWFE closed form, interactive factor model, synthetic-control weights and weighted-DID algebra, factor-balance limitations, conditional exchangeability, unbiasedness constraints and variance criterion, doubly robust constraint combination. |
| 9 | 44–50 | IV conditions and causal graph, structural versus regression interpretation, covariance bias identity, optimal-instrument ratio/estimating equation, square-root-n scaling and optimization direction, conditional-IV target, independent-product variance, scalar estimating-equation variance, first-stage cross-fitting/weak-IV limits, blue example's residual identity, NPIV operator identification and regularization. |
| 10 | 51–58 | Binary Wald/LATE derivation and compliance table, ambiguous ATE label, supply-demand monotonicity/existence and Fubini conditions, threshold orientation and uniform normalization, jump/continuous weights, density versus mass, BV/Stieltjes representation including singular continuous part, multiple-jump typo, distributional derivative question, local-IV chain rule/support. |

## Original page and ink/arrow inventory

1. Black SUTVA supplement, definition arrow retained.
2. Black RCT derivation; blue difference-in-means/fitted-coefficient/slope-uncertainty annotations; arrows retained.
3. Black general OLS and personal representation; red strict-inequality claim; blue prediction interpretation.
4. Black aggregate-variance continuation, linked from p. 5.
5. Black discrete aggregation; red probability weighting, blue grouping/expansion labels; continuation link.
6. Blue/red discrete points and continuous curves reconstructed, downward comparison arrows, blue Lebesgue label; black proof.
7. Black propensity result and sorting; blue similarity and consistency comments; sorting link.
8. Black potential-outcome model, linked to p. 9 variance.
9. Black IPW formulas; blue consistency and rate comments.
10. Black c interpretation; blue variance-comparison arrow.
11. Black AIPW and robustness algebra; blue residual/fairness intuition.
12. Black rearrangement/variance; blue IPW/mean-zero labels and oracle-to-CLT link.
13. Black split estimator/conditions; blue random split, consistency and RMSE observations.
14. Black three-term remainder proof; blue rates and oracle comments retained.
15. Black score/variance definitions, including the original mathematical error.
16. Black variance/CI formulas; blue oracle arrow; normal shaded-area sketch reconstructed.
17. Black CATE and model; blue category/regularization/basis/error annotations; black transformation arrow and red Robinson label.
18. Black residual regression/sandwich; blue preprocessing and omitted-fold comments.
19. Black constant-effect supplement; blue comparison and R-loss continuation link.
20. Black population R-loss; blue baseline analogy, penalty explanation and entire feasible objective/lasso supplement.
21. Black overlap failure/rate discussion; blue eta qualification.
22. Black RDD estimator; blue cutoff-neighborhood intuition; red kernel/side labels linked to terms.
23. Black smoothness/Taylor equations; red expansion/remainder labels.
24. Black intercept weights and rate derivation; red curvature/noise labels and bounding arrow, bandwidth/error comments.
25. Black latent model/deconvolution; blue noise arrow and Gaussian-density formula; red CDF and weighted-effect/bias labels.
26. Black minimax continuation; blue comparison with local-linear estimation.
27. Black Gaussian/bias/MSE derivation; red linear-estimator link/norm/minimax/MSE comments; blue symmetry comment.
28. Black split and weight-profile sketch; red group labels, weight constraints, and arrows.
29. Black optimization; blue dual-problem link.
30. Black interval calculation; blue conditional-design/discrete-support/distance remarks.
31. Black heteroskedastic formulas; blue fitted-mean and residual-inflation arrows.
32. Black balance introduction/IPW bound; black introductory relationship; blue Cauchy–Schwarz and AIPW comments.
33. Black basis/expectation/balance formulas; red basis examples and regularity question; black expectation arrow and red conditioning identity arrow.
34. Black norm supplement, with original erroneous shorthand retained and corrected adjacent.
35. Black calibration equations; blue means/two-model/Holder/personal remarks; red imbalance label; KKT-to-Newton link.
36. Black weight/augmentation formulas; red norm/imbalance/tuning labels, residual-bias bound and error-correction arrow.
37. Black integrated rate/CLT argument; red noise label; blue sample-versus-population caveat.
38. Black panel layout reconstructed and within-unit variance supplement.
39. Black TWFE/DID text; red no-dynamics/effect/exogeneity notes, blue DID link.
40. Black A/B product arrows reconstructed; black clustering postscript.
41. Black interactive panel/weight formulas and block-treatment matrix reconstructed; red group labels, parallel-trend intuition and treated-weight arrow.
42. Black double-robustness supplement; red fixed-effect cancellation explanation.
43. Black exchangeability/weight constraints; red zero-sum cancellation arrow; blue within-stratum variation comment.
44. Black IV checklist; red/black instrument-to-treatment-to-outcome arrows reconstructed, with additional treatment pathway.
45. Black structural/covariance derivation; red OLS label and black structural-model link.
46. Red conditional-IV extension and formula; black independent-product variance identity.
47. Black instrument equations; red optimization/prediction arrows and labels; source n and argmin retained with purple correction.
48. Black estimating-equation supplement.
49. Black first-stage/cross-fitting text; blue overfitting example and equivalence arrow; red mean-square consistency formula.
50. Black NPIV equations; blue warning and regularization/consistency margin.
51. Black compliance table and proof; red monotonicity formula; blue LATE/ATE postscript.
52. Black binary-IV/noncompliance definitions; red actual/assigned-treatment labels.
53. Black market model/proof; red causal chain and Fubini link.
54. Black cutoff jump sketch; red U-strip sketch and effect/density/weight arrows reconstructed.
55. Black threshold model and weighted formula; blue exogeneity/exclusion/relevance and erroneous monotonicity comment; black BV claim.
56. Black distributional-derivative question, expression and Dirac reminder.
57. Black single/multiple-jump cases and covariance proof; original numerator typo restored visibly before correction.
58. Black local-IV derivative formula and complete chain-rule proof.

## Preservation and remaining uncertainty

- Reading order remains main-page first with the corresponding preceding supplement integrated where used; it was not reordered into textbook prose. Author intuition, questions, examples and incorrect original claims remain visible.
- Forty-two explicit note-arrow relationships and seven TikZ drawings supplement mathematical arrows and the panel array. Drawing coordinates are schematic; labels, relationships and original pen colors were restored. Ordinary underlining/stars used only for emphasis were not facsimile-traced.
- Page 41 bottom sentence and page 50 bottom-edge margin are physically clipped. The readable fragments remain; missing words are not invented from the lecture.
- Page 51 blue IATE/ATE label remains uncertain; the unconditional expectation is mathematically an ATE regardless of that label.
- Tiny sketch labels on page 6 are lower-resolution handwriting; arithmetic comparison is represented by its visible outcome pairs (10,5), (8,4), (7,5).
- The page 40/42 short bibliography abbreviations are not assigned an invented exact citation.
- The handwritten notes are mathematical study notes, not a complete list of sufficient assumptions for every theorem. Orange annotations make the material restrictions explicit without pretending the source proved them.
- Root handles merged-PDF compilation, full page layout QA, Markdown conversion, bilingual output, final directory synchronization, and Git operations. These reviewed body files are frozen for that build.
