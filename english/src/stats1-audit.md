# STATS 361, Lecture1-10: translation audit (main fragment)

Source: `note_for_Causal _inference_STATS_361/Lecture1-10.pdf` (58 scanned pages).
Translation fragment: `stats1-body.tex`, covering original PDF pages 1-39. Original pages 40-58 are assigned to `stats1-tail.tex` and its separate audit. The split deliberately keeps page 40's left-page supplement with page 41's interactive-panel discussion.

## Method and reading order

Every page in this main fragment was visually inspected at the rendered 145-dpi page resolution. Page parity is **not** a reliable left/right indicator: the scan omits many blank left pages, so multiple right-hand pages can be consecutive. Reading order follows the actual notebook layout, subject headings, continuation text, and arrows. Each logical section identifies its original PDF pages. Main text is followed by its attached left-page clarification; supplement pages are never discarded for being mostly blank.

All substantive equations, prose, marginal comments, and personal interpretations are included. Repeated equations at page tops are carried into the continuous argument rather than duplicated mechanically. Simple visual sketches are translated into explicit descriptions or formulas; they are listed below. No textbook text was substituted for handwriting. Apparent source mathematical errors are identified as translator notes rather than silently removed.

## Page inventory

| PDF page | Type / content | Placement and coverage |
|---|---|---|
| 1 | Left supplement: SUTVA, observed outcome, randomized assignment | Attached to Lecture 1 after its ATE/difference-in-means setup on p2; both numbered SUTVA comments retained. |
| 2 | Main: Lecture 1, RCT regression, ATE, DM and OLS variance | All formulas and error decomposition retained; blue uncertainty annotation included. |
| 3 | Main continuation: nonlinear mean models, population OLS projection, variance comparison, personal fitted-value view | All displayed calculations retained, including the original strict-inequality annotation. |
| 4 | Left continuation: aggregate estimator limit and variance | Inserted immediately after the bottom-of-p5 expansion, following the arrow. |
| 5 | Main: Lecture 2, unconfoundedness, discrete strata, group-wise ATE and aggregation | Full estimator definitions, sample counts, limit, and four-term expansion retained. |
| 6 | Left supplement: discrete/continuous sketches and propensity-score proof | Attached to p7 propensity result. Discrete outcome values and gaps listed; continuous-curves diagram described; integral calculation retained. |
| 7 | Main: continuous X, balancing score, propensity stratification | Personal 'cannot peek' interpretation, algorithm, and blue similarity comment retained. Abbreviated control-group sum expanded explicitly with the same stratum indices. |
| 8 | Left supplement: conditional potential-outcome model for IPW variance | Attached before the p9 variance calculation; original weighting coefficients preserved. |
| 9 | Main: IPW, oracle IPW, overlap/consistency and variance | Full formulas and marginal comments retained. |
| 10 | Main continuation: c(x), aggregation comparison, linear-model comparison | Both personal comparisons retained. |
| 11 | Main: Lecture 3, two ATE representations, AIPW, first half of double robustness | Full estimator and explanation retained; fairness interpretation explicitly marked personal intuition. |
| 12 | Main: other half of double robustness, semiparametric efficiency | Rearrangement, oracle approximation, efficient variance and Cramer-Rao comparison retained. |
| 13 | Main: sample splitting, two-fold cross-fitting, assumptions and rates | Full cross-fit formula, overlap, uniform consistency, product risk and n^-1/4 RMSE comments retained. |
| 14 | Main continuation: oracle-equivalence proof and K-fold formula | Entire three-term remainder decomposition retained; unclear first bound identified. Repeated top-of-page definition incorporated into preceding section. |
| 15 | Left supplement: score and empirical/effective variance definitions | Inserted into p16 confidence-interval section before variance formulas. |
| 16 | Main: oracle and cross-fitted variance estimators, interval | Long summands represented using explicitly defined psi_i, retaining exact components; shaded normal diagram explained as the central coverage region. |
| 17 | Main: Lecture 4, CATE, regularization bias, semiparametric/Robinson model | Personal imbalance-between-two-fits example and all formulas retained. |
| 18 | Main continuation: residual-on-residual regression, variance, cross-fitting | Full oracle and feasible transformations, stated sandwich expression and rate condition retained. |
| 19 | Left supplement: constant-effect residual slope, heterogeneous-effect weighted average, practical use | Attached to p20 R-loss discussion; source equation label 4.5 retained. |
| 20 | Main: general R-loss, oracle/feasible objectives, lasso | Full derivation and all objectives retained; penalty interpretation and CNN margin included. |
| 21 | Left supplement: why IPW fails in RDD, lack of overlap, nonparametric rates | Attached after the p22 RDD setup; personal comparison argument retained. |
| 22 | Main: Lecture 5, cutoff identification, local linear regression, kernels | Main formulas and red kernel/side labels retained. |
| 23 | Main continuation: smoothness, weaker/stronger smoothness observations, Taylor approximation, separate regressions | Entire argument retained, including original Taylor remainder convention. |
| 24 | Main continuation: window-kernel weights, bias/noise split and rates | Full formulas and explanations retained; missing normalization and inconsistent factor 1/2 noted. |
| 25 | Main: noisy running variable and deconvolution estimator | Latent-variable model, CDF/density, normalization, expectation split all retained; apparent missing latent mean noted. |
| 26 | Left continuation: minimax estimator and comparison with local linear | Attached immediately after p27 MSE bound, before derivation on p29. |
| 27 | Main: Lecture 6, linear estimator, conditional normal law, minimax bias bound | All formulas and red norm/MSE comments retained. |
| 28 | Left supplement: positive/negative weight sums and sketch | Attached to p29 weight constraints; original red Y=1/Y=0 labels are acknowledged while W equations retained. Sketch is described with its sign pattern. |
| 29 | Main: deriving minimax weights and constrained optimization | All moment constraints and infinite-dimensional bias constraint retained; dual-problem instruction included. |
| 30 | Main: bias-aware confidence intervals, discrete and multivariate examples | Probability bound, interval, quantile definition, and all personal comments retained. |
| 31 | Main continuation: beyond homoskedasticity | Conditional normal approximation, residual variance estimate and conservative-fit annotation retained. |
| 32 | Main: Lecture 7, review of IPW and Cauchy-Schwarz consistency bound | Three-step argument and blue AIPW comparison retained, despite author labeling review 'not important'. |
| 33 | Main: basis expansion and population/sample balance | Full expectation calculation and personal question on assumptions retained. |
| 34 | Left supplement: norm reminders | Attached to high-dimensional Holder bound on p35; original shortcuts retained with a translator note. |
| 35 | Main: logistic balancing loss, high-dimensional confounding and Holder bound | All equations and personal questions retained; separate propensity-model annotation retained. |
| 36 | Main continuation: balancing optimization, concentration bounds, augmentation and lasso rates | Full criterion and decomposition retained, including red explanation that weights correct coefficient estimation error. |
| 37 | Main continuation: sparse-model synthesis, asymptotic expansion and CLT | All steps, rates, CLT and personal sample-mean-versus-population-mean caveat retained. |
| 38 | Left supplement: panel matrix sketch and robust variance | Attached to p39 panel introduction and two-period DID. Matrix sketch described; entire variance expression retained. |
| 39 | Main: Lecture 8 introduction, constant treatment effects, two-way model, DID | All formulas, limitations, dynamics explanation, parallel-trends comment retained. |
| 40-58 | Tail handoff | Not represented by this fragment. Page 40 belongs to page 41; see stats1-tail.tex and its audit. |

## Ambiguities and source inconsistencies preserved

- p2: The OLS error decomposition and intercept centering implicitly assume centered covariates; the source does not restate this. Balanced-allocation factors of four retained.
- p3: The handwritten 'strictly smaller always' claim conflicts with the displayed squared-norm difference, which permits equality. The simplified projection covariance is retained as a source statement.
- p6: The handwritten balancing-score proof omits conditioning on potential outcomes in the first mixing distribution; its intended result is clear and original integral is preserved.
- pp8-10: The supplied c(x) potential-outcome equations and the c(x)^2 variance formula use inconsistent weights. Both source statements remain, with the discrepancy explained.
- p14: The first remainder bound is written approximately as o_p(1)/n. Whether this is a term bound or a variance bound is unclear; no unsupported correction was made.
- p15: The source calls the ordinary likelihood score derivative an efficient score; the distinction is noted.
- p16: The source says alpha-level but gives a 1-alpha coverage formula; the formula is preserved and clarified.
- p18: The middle factor of the sandwich covariance uses transformed outcome instead of regression residual in the scan; preserved with a note.
- pp23-24: The local-linear weight formula is missing division by the within-bandwidth sample count; the later weight-sum identity requires it. Taylor remainder factor 1/2 is also dropped in the next decomposition. Both are explicitly flagged.
- p25: The source writes Z|U ~ N(0, nu^2), but subsequent formulas require mean U (or a centered noise term). Preserved and explained.
- p28: Red Y=1/Y=0 labels appear over a split that the formulas identify as W=1/W=0.
- p34: The handwritten zero-norm and general p-norm shortcuts are retained; standard definitions are supplied only as translator notes.
- p39: The source says multi-period OLS lacks a closed-form solution. This is preserved with a note distinguishing the simple two-period DID formula from the general OLS matrix solution.

## Authorship separation

Personal intuition, questions, and marginal observations are labeled as such only where their handwritten role is evident. All added mathematical cautions begin 'Translator\'s note'. These are editorial observations, not attributed to the notebook author. No external textbook or web material was incorporated into this fragment.
