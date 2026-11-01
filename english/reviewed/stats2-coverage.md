# STATS361 Lecture 11–14: mathematical and source-fidelity coverage

Reviewed output: `src/stats2-body.tex`. Findings: `stats2-findings.json`.
Source: `note_for_Causal _inference_STATS_361/Lecture11-14.pdf`, all 31 pages, visually re-inspected during this review. Reference: the local `tmp/references/stats361-reference.pdf` / `.txt`, Lectures 11–14, with independently checked algebra. Official notes are not treated as infallible: several copied mistakes occur in both versions.

38 findings: 14 original-note corrections, 20 qualifications/unresolved points, and 4 direct transcription/translation fixes. Original-note corrections use purple; qualifications use orange. Transcription corrections are applied directly and appear only in the JSON audit. Original black/red/blue is retained separately. The body contains 30 explicit annotation-arrow pairs and 5 TikZ diagrams, including both d-separation examples, front-door, IV, mediation, and the two qualitative UCB sketches (the path pair and sketch pair each share one TikZ picture).

## Reading order

1; 3 with 2; 5 with 4; 7 with 6; 8; 10 with 9; 11; 12; 13; 14; 15; 16; 17; 19 with 18; 20; 21; 22; 24 with 23; 25; 27 with 26; 28; 29; 31 with 30.

The preceding left-page supplements remain integrated with the corresponding right-page main notes. Arrow source/target relations are made explicit rather than inferred from page parity. Original ink is reconstructed semantically, including the red boxed conditional expectation, classification underbraces, red and blue marginal interpretations and questions, red proof connections, blue backward-regression and known-variance comments, and actual directed graph edges. Page ruling, notebook logos, and incidental pen strokes are not reproduced. Qualitative sketches are labeled as qualitative rather than assigned invented numerical data.

## Page-by-page coverage

| Scan | Checked material | Ink and relation restoration / result |
|---|---|---|
| 1 | Policy, value, optimal class policy, regret, assumptions, deterministic deployment | Black main; red regret-versus-square-loss emphasis; overlap limitation qualified. |
| 2 | IPW ATE expectation conditioning on propensity score | Black supplement to p3; balancing-score argument consistent with unconfoundedness and overlap. |
| 3 | Empirical maximization and fixed-policy IPW unbiasedness | Black derivation; red boxed factor equals one; omitted outcome in original explicitly preserved and corrected. |
| 4 | VC regret bound, bounded outcomes, overlap, superefficiency caveat | Red complexity/optimality/faster-rate commentary retained; minimax versus pointwise targets distinguished. |
| 5 | Baseline decomposition, advantage, IPW score, weighted classification | Red E0 and classification/weight markings; blue surrogate warning; exact loss identity independently derived. |
| 6 | Efficient regret scale and V-star | Black continuation arrow to optimality intuition; red doubt retained; second moment versus fixed-policy score variance clarified. |
| 7 | Oracle and cross-fitted AIPW, nuisance rates, uniform equivalence | Red nuisance-rate commentary; rates checked in L2 with product-rate/overlap/complexity qualifications. |
| 8 | Bayes rule and restricted policy classes | Black; pragmatic reasons retained; arbitrary extra covariates do not automatically preserve ignorability. |
| 9 | Sequential history sketch and complete randomization | Black supplement, explicit history-to-2^T-outcomes arrow; design distinction retained. |
| 10 | Dynamic policies, potential histories, sequential ignorability | Black formulas; red links from second decision to covariates/past treatments; positivity and shorthand qualified. |
| 11 | Treatment-confounder feedback and principal-stratum composition | Black table and comparisons retained; no outcome table available; zero-versus-60 reference discrepancy unresolved rather than falsely declared an OCR mistake. |
| 12 | Filtration, value function, tower identity, invariant transitions | Red overall value/Bellman intuition and transition arrow; Bellman analogy qualified without adding a Markov assumption to original argument. |
| 13 | Change of measure, sequential IPW, gamma recursion | Red factor-cancellation and denominator question; original X_t index, omitted conditioning, gamma0=0, and history argument slips explicitly addressed. |
| 14 | Backward regression | Blue error-propagation to Q-learning arrow; evaluation/optimization distinction qualified. |
| 15 | Sequential AIPW construction | Black iteration arrows and red weight/correction labels; original final claim retained with red underline; telescoping proof and finite-sample conditions supplied separately. |
| 16 | Independent-error SEM, invariance, intervention truncation | Red parent/function interpretation and arrow; blue concrete-distribution interpretation and denominator question; imposed-value typo corrected in purple, continuous support in orange. |
| 17 | Path blocking, d-separation, graph surgery | Actual path diagrams; dashed annotation arrows distinguished from causal arrows; universal path quantifier explicit. |
| 18 | Do-calculus mnemonic | Entire red supplement retained and connected to the rules. |
| 19 | Three rules, Z(W), completeness | Red incoming-arrow interpretation retained; formulas checked; completeness distinguished from failed informal search. |
| 20 | Back-door proof and structural conditional independence | Red step labels and marginal interpretation; blue arrow to (13.10); prior root-node mistranslation and specified/unspecified reversal directly fixed. |
| 21 | Front-door graph and factorization proof | Actual DAG; red rule labels, factor decomposition and replacement arrow; black observational-integration insight linked to P(W). |
| 22 | IV graph, SEM/potential-outcome relation, nested counterfactual | Actual IV and mediation DAGs; red cross-world and Identifiable? comments; random-variable/distribution mismatch and claimed notational limitation corrected, model-relative identification qualified. |
| 23 | K-arm interpretation and common best arm | Black left-page restatement retained. |
| 24 | Arm counts, means, regret, uniform randomized baseline | Black definition arrows; red history/sublinear-regret explanation; blue per-individual expected loss annotation. |
| 25 | UCB construction, known Gaussian variance, gap bound | Blue known-variance arrow; red initialization, one-observation/time, gap and strong/weak-effect intuitions; equality and unbounded-gap worst-case claim corrected. |
| 26 | Bounded Hoeffding, union bound, attempted Gaussian proof | Red boundedness arrow and explicit doubts retained; Gaussian tail calculation resolves the unfinished question in orange. |
| 27 | Adaptive-time reindexing and confidence event | Red range-expansion and equal-distribution links; copied arm-zero slips identified; reward-stream coupling explained. |
| 28 | Pull-count threshold and regret decomposition | Red confidence-to-count arrow and threshold comments, two red qualitative sketches, initialization labels; missing deviation direction corrected. |
| 29 | UCB limitations and Thompson sampling | Red Bayesian heuristic, historical dependence and probability threshold; black causal-inference link; parenthesis partly unclear, tie and cutoff qualifications. |
| 30 | Martingale definition, increments, variance stabilization, CLT and variance consistency | Red conditional-mean and CLT/rate remarks; black denominator-cancellation arrow; absolute integrability corrected; conditional variance of M_t itself verified as valid, not mistakenly flagged. |
| 31 | AVG/IPW/AW estimators and studentized pivot | Red Gaussian-pivot clarification; blanket absence-of-normality corrected; pre-assignment probability and positivity specified. |

## Independent mathematical checks

- Fixed-policy IPW unbiasedness uses conditional expectation and consistency; same-sample maximization does not retain unbiasedness.
- The policy advantage identity and weighted zero-one classification equivalence hold exactly; arbitrary surrogate objectives need separate guarantees.
- V-star is E[(Gamma-star)^2], while a fixed-policy advantage score variance subtracts A(pi)^2.
- Sequential IPW follows a supported change of measure; gamma0 must be one. The sequential AIPW summand telescopes and exposes why correct weights permit arbitrary independently trained outcome models.
- The three do-calculus rules and front-door/back-door manipulations were checked against the graph surgery conditions. The nested potential outcome is expressible in either framework; cross-world identification needs assumptions.
- For Gaussian UCB, the exact standardized tail at 2 sqrt(log T) is at most T^-2 for T>=2 (Mills bound), including both directions. Union over KT pairs gives 1-K/T; both directions are needed for the count proof. T>=K and positive noise variance are implicit in the nontrivial construction; zero-variance problems are degenerate.
- Unbounded arm gaps make a worst case over all Gaussian means infinite because initialization alone incurs sum Delta_k.
- The AW martingale's conditional variance is correct even conditioning on its own past. A sufficient finite-fourth-moment/polynomial exploration regime verifies Lyapunov and residual-variance concentration; it is stated as sufficient, not necessary.

## Remaining uncertainty

- p11: The visible handwritten 0 differs from the official uncentered example's 60. The scan omits the outcome table; unstated centering cannot be ruled out. Unsubscripted W/Y(1)-Y(0) lacks a precise sequence convention.
- p5: The marginal year looks like Wager [2020]; retained with uncertainty. No guessed bibliographic entry added for this scribble.
- p20: A few words of the top red intuition remain unclear, but the mathematical back-door claim and its target are clear.
- p29: Part of the black parenthesis and a small red aside remain unclear. The previous unsupported treatment-amount interpretation was removed; no invented detailed sentence replaces it.
- p15: The final black statement with red underline is terse. The review does not equate its phrase 'unbiased value estimates' with a complete double-robustness theorem.

## References consulted

- [Official STATS361 notes](https://web.stanford.edu/~swager/stats361.pdf), Lectures 11–14; local PDF/text also checked.
- [Athey and Wager, Policy Learning with Observational Data](https://arxiv.org/abs/1702.02896).
- [Jiang and Li, Doubly Robust Off-policy Value Evaluation](https://proceedings.mlr.press/v48/jiang16.html).
- [Imai, Keele and Tingley, A General Approach to Causal Mediation Analysis](https://imai.sites.fas.harvard.edu/research/files/BaronKenny.pdf).
- [Hadad et al., Confidence intervals for policy evaluation in adaptive experiments](https://pmc.ncbi.nlm.nih.gov/articles/PMC8054003/).

## Validation and handoff

The complete fragment compiles under XeLaTeX using the root's shared preamble and macros. Isolated preview: `tmp/review-stats2/preview.pdf`, 27 pages. Final compile has no overfull/underfull box messages or undefined-command errors. Environment nesting and unique IDs checked; no old Translator notes or transcription reviewnote environments remain. The merged book must still be rendered and visually inspected by the root after final pagination. The temporary generation script predates a few final direct layout/notation fixes; the reviewed body and JSON are the authoritative outputs.
