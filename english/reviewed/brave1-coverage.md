# Brave and True Chapters 1–23: comprehensive review coverage

All 40 original scan pages were visually reinspected against the full English body. Every chapter's definitions, displayed formulas, derivations, causal identification claims and personal intuitions were checked. The output is a translation with separate review annotations, not a replacement textbook summary.

## Delivered artifacts

- `src/brave1-body.tex`: full reviewed body, original black/blue/red semantic ink restored; 96 explicit annotation-to-target arrows and 12 TikZ figures.
- `brave1-findings.json`: 43 findings (5 direct transcription fixes, 17 original-note corrections, 21 qualifications).
- Purple review boxes diagnose original-note issues; orange review boxes state conditions or uncertainty. Original red/blue ink is independent of review status. Transcription fixes have JSON records and no colored correction box.

## Reading order

Pages 1–36 are consecutive main notes, not an even/odd-page alternation. Chapter 13 on scan p17 is placed before Chapter 14 on pp16+18. The unfinished main discussion on p38 precedes its facing-page recipe on p37. Chapter 23 follows on pp39–40. All chapter labels and the author's tentative nonlinear ideas are retained.

## Page and ink/arrow inventory

| Scan | Chapter | Mathematical coverage | Original ink restored | Pointing relations / diagrams |
|---|---|---|---|---|
| 1 | 1–2 | ATE/ATT decomposition; randomization | Blue labels, implication chain and independence display; red bias star | Association → ATT → ATE; RCT → independence; eliminate/study links |
| 2 | 3 | SE, tests, confidence levels | Black core; blue interval/difference and sample/threshold labels | SE → variance formula; interval/difference annotations |
| 3 | 4 | D-separation, confounding, bad controls | Black throughout | Three primitive DAGs; X→W2←Y, W2→W1, X→Y; mediator graph |
| 4 | 5 | FWL and OVB identities | Black equations; blue residual/ability explanations; red OVB label | Residualization → T residual; ability → omitted term/coefficient; OVB → extra term |
| 5 | 6 | Dummy interactions and regression weights | Black model; blue coefficient interpretation and weight labels | Binary contrast and interaction-slope links |
| 6 | 7 | Precision controls; participation decomposition | Black main; blue precision/decomposition; red bad-control circles | Three DAGs; participation and selection-bias labels |
| 7 | 8 | Covariance/Wald IV derivation | Black derivation; blue error/reduced-form labels | Z/T/W/Y graph; error information and reduced-form arrows |
| 8 | 8 | 2SLS and weak instruments | Black main; blue first-stage/control commentary; red author correction | Instrument diagram; red correction → conditional independence |
| 9 | 9 | IV assumptions and compliance types | Black assumptions; blue noncompliance intuition; red emphasis | Z→T weakening; exogeneity and exclusion explanations |
| 10 | 9 | Wald/LATE algebra | Black proof; red complier annotation | Strict complier event → compliance |
| 11 | 10 | Subclassification and matching | Black main; blue averaging, distance and match; red KNN/sign labels | Integral average; sign coding; nearest opposite-treatment unit |
| 12 | 10 | Matching bias correction and dimensionality | Black main; blue mean function/counterfactual/correction reasoning; red emphasis | Bias discrepancy → correction; mu0 targets; dimensions → sparse cells |
| 13 | 11 | Balancing and IPW | Black main; blue question mark on personal intuition | Propensity DAG; original double arrow; balancing proof; pseudo-populations |
| 14 | 11 | Propensity-score matching caveats | Black throughout | No separate drawn pointing arrow; connection to p13 retained |
| 15 | 12 | AIPW and both robustness arguments | Black estimator/definitions; blue proof; red cancellation emphasis | Combine regression/IPW; both cancellation routes |
| 16 | 14 | Panel notation and parallel trends | Black core; blue y/X/U interpretation | Repeated person → fixed attributes; known/estimated counterfactual meaning |
| 17 | 13 | Two-period DID | Black equations; blue temporal/spatial counterfactual reasoning | Curved regrouping arrows → treated change minus control change |
| 18 | 14 | FWL, within transformation, FE limits | Black equations; blue limitations/cancellation; blue parallel lines | Ubar=U → remove fixed effect; feature matrix meaning |
| 19 | 15 | Synthetic-control setup | Black core; blue factual/counterfactual/time/OLS explanations | Donor pool; treatment-time effect; weights → regression |
| 20 | 15 | OLS overfit and convex restriction | Black optimization; blue overfit explanation and convex hull | Donor-to-treated extrapolation versus convex hull |
| 21 | 15 | Placebo inference | Black procedure; blue numeric/tail conclusion | Repeat by state; poor prefit → threshold |
| 22 | 16 | Sharp-RD identification and local fit | Black curves/proof; blue local/side annotations; red observed curve | Potential to observed switch; cutoff estimand; side regressions |
| 23 | 16 | RD intercept, kernel, fuzzy IV | Black main; blue weights/WLS; red observed jumps and Wald emphasis | Kernel factors; treatment jump → outcome jump/Wald ratio |
| 24 | 16 | Significance and density test | Black throughout | No separate source arrow |
| 25 | 17 | Prediction/CV/R2 | Black main; blue R2/overfit explanation | Learned expectation; depth → overfit; threshold → decision |
| 26 | 18 | CATE, derivative and interaction | Black equations; blue conditional/personalization labels; red interaction | Condition X → policy; interaction → heterogeneous derivative |
| 27 | 19 | Ranking, cumulative elasticity | Black throughout | Feature matrices; ranked group accumulation → overall effect |
| 28 | 19 | Gain and standard error | Black throughout | Gain sketch versus straight baseline |
| 29 | 20 | ITE/CATE risks and interaction | Black main; blue beta2/irrelevance margin; red risk minimization | CATE → interaction; derivative ignores beta2; loss target |
| 30 | 20 | Binary transformed-outcome proof | Black proof; red expectation emphasis | Conditional expectation expansion → CATE |
| 31 | 20 | Continuous transformation and tentative extension | Black math; red denominator/numerical warning | Demand-price slope; problematic denominator → numerical warning |
| 32 | 21 | S/T learners | Black algorithms/flowchart; blue split-data tension | S/T learner branches and common-X comparisons |
| 33 | 21 | X-learner | Black algorithm/flowchart; red imputation/weight intuition | Crossed counterfactual predictions; propensity → weighted final effect |
| 34 | 22 | FWL and nuisance learning | Black throughout | Residual regression → coefficient; matrix-layout interpretation |
| 35 | 22 | DML and cross-fitting | Black equations; blue overfit intuition; red nuisance roles/R-learner | MY/MT role arrows; overfit → residual effects/variance |
| 36 | 22 | R-loss and nonlinear claim | Black equations; blue predictor/weight/R-loss labels | Nuisance predictions; weighted ratio target; R-loss minimization |
| 37 | 22 supplement | Five-fold nonlinear prediction recipe | Black throughout | Counterfactual Tnew → residual input → add baseline outcome |
| 38 | 22 main | Unfinished nonlinear model | Black throughout | Linear residual equation → nonlinear proposal; two cross-fitted branches → final model |
| 39 | 23 | Latent/conversion DGP and heterogeneity | Black equations/plots; blue income/age/threshold annotations | Income → common additive term; age → segmentation; income → conversion TEH |
| 40 | 23 | Price/type dependence and transformation | Black throughout | Type and price → ranking concern; nonlinear sales curves |

## Key distinctions verified against actual ink

- p3: magnification resolves the collider as W2 and its descendant as W1; the graph is X→W2←Y, W2→W1, X→Y. Investment is written alongside W1.
- p6: the scan says variance (not coefficient bias), and the black prose says inverse relationship. The previous translation's contrary reading was repaired directly.
- p29: the blue note says X is unrelated to the outcome. The prior translation reversed this; the original mathematical assertion is then reviewed separately.
- p37: the source itself reverses the new-treatment residual subtraction; this is retained as source wording and corrected in purple.
- p36: the local-derivative claim is also present in the textbook; the review gives the projection-slope target and a counterexample.
- p39: the G(20,2) scan reading is clear. The textbook code, unlike its displayed prose, multiplies income by 100 and uses conversion threshold 0.1. The quoted conversion effect belongs to that different simulation. The source equation is preserved and the inherited inconsistency explained.

## Remaining uncertainty / intentional limits

- p6: the end of the participant-selection margin is clipped; its visible comparison and full algebra are preserved.
- p8: one short weak-IV standard-error parenthesis is still not fully legible. The main variance/weak-instrument claim is reviewed.
- p20: the exact intended T/N sample-size comparison is uncertain; no inequality has been invented.
- p21: the denominator yielding 0.0286 is absent from the handwritten note. It is not reverse-engineered or silently claimed exact.
- p38: a short implementation abbreviation formerly guessed as JS remains marked unclear; the cross-prediction/averaging idea is preserved.
- p40: the example power transform looks like negative price to the fourth power, but its exponent is not fully certain. The author's proposal is kept tentative.
- Ink restoration is semantic rather than a pixel facsimile. Decorative stars/underlines are represented by their colored labels and connections; source DAG directions, meaningful arrows and curve-color roles are explicitly rebuilt. No uncertain arrow direction was fabricated.

## Primary-source verification and QA

Official handbook chapters were consulted directly. Specialist checks additionally use Imbens–Angrist (LATE), Abadie–Imbens (matching), McCrary (density discontinuity), Chernozhukov et al. (DML), Nie–Wager (R-learner), and Künzel et al. (meta-learners). Full primary URLs are in each finding and compact clickable references in each review box. Textbook claims were not treated as automatically correct.

A temporary standalone XeLaTeX QA build compiled successfully (36 pages before the final small heading keep-together adjustment). The compiler reported no overfull/underfull boxes or missing glyphs. All rendered pages were inspected on contact sheets; figures, original colors and the changed closing pages were additionally viewed at full page size. The parent owns final combined-book pagination and final output PDF verification.
