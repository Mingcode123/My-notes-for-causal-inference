# Brave and True Chapters 1-23: translation audit

All 40 source pages were visually inspected at 145 dpi. Page 39 was additionally inspected at 220 dpi. The source is `note_for_Causal_Inference_for_The_Brave_and_True/Chapter1-23.pdf`; page numbers below are PDF page numbers (not printed notebook numbers).

## Reading order

The first 36 scans are consecutive content pages; mechanically alternating odd/even pages would be wrong for this file. The chapter numbering establishes one reorder: p.17 (Chapter 13) precedes pp.16 and 18 (Chapter 14). Pages 37-38 are a facing spread: p.38 introduces the unfinished nonlinear extension and p.37 supplies its step-by-step procedure; the translation reads p.38 then p.37. All other content follows the scan sequence, with arrow and margin annotations placed after the proposition they modify.

## Complete page inventory

| PDF page | Content | Disposition |
|---|---|---|
| 1 | Chapters 1-2; ATE/ATT bias decomposition; RCT arrows | Fully translated; blue intuition attached to decomposition |
| 2 | Chapter 3; SE, confidence, p-values | Fully translated; informal statistical wording flagged |
| 3 | Chapter 4; chain, fork, collider; personal confounding/selection diagrams | Graphs transcribed as edges and explanatory text; one clipped phrase flagged |
| 4 | Chapter 5; regression, FWL, OVB | Equations and blue residual intuition preserved |
| 5 | Chapter 6; grouping, dummy regression, IQ interaction | Equations, coefficient interpretations, weighting retained |
| 6 | Chapter 7; controls, SE, participation, selection | Full decompositions and graph edges; edge text uncertainty flagged |
| 7 | Chapter 8; IV covariance derivation, calculus intuition, Wald | All algebra and marginal explanations retained |
| 8 | Chapter 8 continuation; IV conditions, 2SLS, weak IV bias | Author's red 'corrected in 09' note explicitly preserved |
| 9 | Chapter 9; compliance types and four assumptions | Full list, graph, and blue weak-first-stage intuition |
| 10 | Chapter 9; Wald-to-LATE derivation | All steps and red complier qualification preserved |
| 11 | Chapter 10; subclassification, KNN matching | Formulas, weighting comparisons, distance normalization |
| 12 | Chapter 10; matching bias correction, dimensionality | Full correction derivation and counterfactual/factual explanation |
| 13 | Chapter 11; balance identity, IPW, author's intuition | Full proof and all warning/weighting annotations |
| 14 | Chapter 11; propensity matching warnings | Both numbered concerns and author's negative assessment |
| 15 | Chapter 12; doubly robust estimator and two cancellations | Formula plus both algebraic explanations |
| 16 | Chapter 14 opening; panel/FE and DID reminder | Placed after Chapter 13 p.17, before continuation p.18 |
| 17 | Chapter 13; DID contrasts and arrows | Placed before Chapter 14; both failed contrasts and combined estimator |
| 18 | Chapter 14 continuation; residualization, within estimator, limitations | All algebra, reverse-causality margin, time effects and parallel-line sketch description |
| 19 | Chapter 15; synthetic control setup | Unit/time notation and weighted counterfactual |
| 20 | Chapter 15; regression overfitting, convex constraints, V weights | Weight criterion, diagrams described, implementation choices |
| 21 | Chapter 15; optimization and placebo inference | Fit screening, p formula, numerical p and directional ambiguity |
| 22 | Chapter 16; RDD continuity, discontinuity, regression | Full limit derivation and graphs described |
| 23 | Chapter 16; kernel weighting, fuzzy RD | Kernel, Wald ratio, interpretation and sketches |
| 24 | Chapter 16; significance note, McCrary test | All two short notes retained |
| 25 | Chapter 17; prediction, validation, R2, qcut, policy | All content retained |
| 26 | Chapter 18; heterogeneity, CATE, derivative intuition | All formulas and interaction explanation |
| 27 | Chapter 19; comparison models, cumulative elasticity | All model definitions, slope formula, ranking goals |
| 28 | Chapter 19; cumulative gain, slope SE | Both equations and curve description |
| 29 | Chapter 20; CATE, treatment-effect MSE | Definitions, interaction note, source MSE equality flagged |
| 30 | Chapter 20; transformed binary outcome | Complete randomized and propensity-weighted derivations |
| 31 | Chapter 20; continuous transformed outcome, speculative nonlinear proposal | All derivation, problematic denominator and author's unresolved proposal preserved |
| 32 | Chapter 21; S- and T-learners | Both flowcharts expressed stepwise, regularization and sample-size intuition |
| 33 | Chapter 21; X-learner | All four stages, weighting, crossing arrows and red explanation |
| 34 | Chapter 22; FWL and nuisance ML | Full four-step residualization |
| 35 | Chapter 22; DML, author's overfit explanations, cross-fitting, CATE | All steps and annotated reasoning preserved |
| 36 | Chapter 22; R-loss, weighted regression, nonparametric vs nonlinear | Full loss derivation and author interpretation |
| 37 | Facing-left supplement to p.38; five-fold LGBM and counterfactual curve | Moved after p.38 conceptual introduction; complete procedure |
| 38 | Chapter 22 unfinished 'Non-Scientific' extension | Author's unfinished status explicit; formulas, flow, shortcomings |
| 39 | Chapter 23; latent-to-binary simulation and heterogeneity | All equations/values and all three sketches described; income G(20,2) resolved with magnified crop |
| 40 | Chapter 23; two nonlinear price-response curves | Curves, type/price dependence and transformation suggestion retained |

No blank page was omitted; all pages contain substantive writing. Drawings are translated by their directed edges, axes, curve behavior, and explanatory meaning rather than included as unreadable scan crops.

## Source ambiguities retained visibly in the English text

- p.1: ATT-to-ATE arrow without stated additional assumption.
- p.2: informal p-value/confidence definitions, preserved with clearly separated translator clarification.
- p.3: last phrase beside investment mediator graph not fully legible.
- p.4: verbal direction of residual regression conflicts with formula and blue explanation; clarified explicitly.
- p.6: SE-versus-X-variance wording conflicts with formula; small graph variable label and bottom edge words unclear.
- p.8: the author marks conditional independence IV statement as inaccurate and defers correction to Chapter 9; weak-IV SE parenthetical unclear.
- pp.9-10: strict monotonicity written while never/always-takers are permitted; Wald result labeled ATE but conditioned on compliers.
- p.13: potential-outcome independence is visually equated with balancing; additional unconfoundedness requirement clarified.
- p.15: expectation-level DR cancellation written as an observation-level equality; retained as shorthand.
- pp.16-17: conditional outcome means use compressed notation; first-chapter order reversed in scan, corrected by chapter heading evidence.
- p.20: T/N size comparison not securely legible; illustrative weight digits approximate.
- p.21: verbal direction of placebo extremeness conflicts with displayed lower-tail comparison; p=0.0286 denominator unspecified.
- pp.22-23: intercept interpretation assumes centered running variable although equation is not centered; fuzzy monotonicity written strictly.
- p.24: p-value size equated with effect size, flagged as shorthand.
- p.29: independence symbol uses X where surrounding text discusses treatment assignment; CATE MSE and individual-effect MSE equated although they differ by irreducible variance.
- p.31: proposed model argument M(T_i) is inconsistent with stated E[T|X] target; squared individual-residual denominator is unverified. The author's 'no solution yet' and numerical difficulty remain explicit.
- p.38: extension explicitly unfinished; prediction labeled price though the fitted variable is outcome; JS implementation margin unclear.
- p.39: income Gamma parameter resolved as 20 using a magnified crop of the 220 dpi rendering; final baseline-conversion lines contradict each other and are preserved as unresolved.
- p.40: price transformation exponent looks like 4 but is not fully clear.

## Fidelity boundaries

This is an English translation of the handwritten notes, including informal, mistaken, and unfinished thoughts. Translator notes are explicitly labeled. No textbook content was used to replace or fill in the author's original discussion. No external paper claims were added. Mathematical notation is typeset consistently while substantive discrepancies are surfaced rather than silently repaired.
