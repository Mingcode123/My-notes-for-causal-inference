# STATS 361, Lectures 11-14: translation audit

All 31 PDF pages were visually inspected at 145 dpi. This is a translation of the handwritten notes, including marginal objections and personal interpretations; it is not a substitute textbook summary. Page references below refer to original PDF pages, not translated output pages.

## Reconstructed reading order

1; 3 with 2; 5 with 4; 7 with 6; 8; 10 with 9; 11; 12; 13; 14; 15; 16; 17; 19 with 18; 20; 21; 22; 24 with 23; 25; 27 with 26 then 28; 29; 31 with 30.

Unlike the other scan files, this file begins with a right-hand main page at PDF page 1. Parity then changes when consecutive main pages were scanned. Content, binding edge, arrows and continuity determine placement; PDF parity alone does not.

## Page inventory

| PDF page | Content and disposition |
|---|---|
| 1 | Lecture 11: policies, value, regret, assumptions, deterministic deployment warning. Translated in full. |
| 2 | Left supplement: unbiasedness derivation for ATE IPW. Integrated after policy-value IPW derivation on p3. |
| 3 | Empirical value maximization and policy IPW proof. All equations retained; missing outcome in initial handwritten expectation flagged. |
| 4 | Left supplement: VC dimension and regret rate. Integrated after p5 classification representation. Red rate annotation preserved. |
| 5 | Value decomposition, advantage, IPW score, weighted classification. Personal earn/pay interpretation and surrogate-loss doubt preserved. |
| 6 | Left supplement: AIPW regret, V-star, Wager 2017, author's objection. Integrated after p7. |
| 7 | Efficient scoring, oracle and feasible cross-fit AIPW, uniform convergence. Translated with equations. |
| 8 | Policy-class restrictions versus Bayes rule; reasons and examples. Translated in full. |
| 9 | Left supplement: longitudinal array intuition and complete randomization assumption rejected as unreasonable. Integrated into p10. |
| 10 | Lecture 12 setup, potential covariates/outcomes, two estimands, sequential ignorability. Translated in full. |
| 11 | Treatment-confounder feedback; two wrong approaches; stable/responder/acute table. Full type-composition argument retained. Unsubscripted W ambiguity flagged. |
| 12 | Filtration, value function, tower law, Bellman analogy, factorization. Equations and red intuition retained. |
| 13 | Change of measure, sequential IPW, recursive weights. Original gamma initial value 0 explicitly retained and inconsistency explained. |
| 14 | Backward regression and error propagation/Q-learning note. Translated in full. |
| 15 | AIPW correction intuition and final estimator. Final unbiasedness sentence retained with conditions-unspecified note. |
| 16 | Lecture 13 SEM definition, intervention, truncated factorization and denominator question. Formula label inconsistency preserved explicitly. |
| 17 | Path blocking/d-separation, graph modification notation. Small graphs reconstructed with arrows; all-path clarification labeled. |
| 18 | Left supplement: red mnemonic for do-calculus. Integrated after p19 rules. |
| 19 | Three do-calculus rules and completeness statement. Translated in full. |
| 20 | Back-door derivation and graphical/potential-outcome intuition. Topmost marginal wording partly unclear and labeled. |
| 21 | Front-door graph and full derivation. All exchange steps and observational-distribution insight retained. |
| 22 | IV graph and limitations; SEM versus potential outcomes; nested counterfactual and author doubts. All retained, distribution/random-variable mismatch flagged. |
| 23 | Left supplement: personal restatement of K-arm experiment and total regret. Integrated into p24. |
| 24 | Lecture 14 setting, empirical arm means, linear versus sublinear regret, exploration/exploitation. Translated in full. |
| 25 | UCB algorithm, normal model, confidence intervals, regret bound and gap intuition. Equality versus bound flagged. Small qualitative sketches described. |
| 26 | Left supplement: Hoeffding inequality, union bound, unsuccessful application and explicit author questions. Integrated within pp27-28 proof. |
| 27 | UCB regret proof, time-change/supremum steps, simultaneous coverage. Full equation chain retained; copied arm index 0 noted. |
| 28 | UCB arm-count bound and regret substitution, handwritten sketches and threshold intuition. Missing opposite-tail condition flagged. |
| 29 | UCB limitations, Thompson sampling, algorithm, prior tuning intuition. One peripheral parenthetical phrase unclear; marked. |
| 30 | Left supplement: martingale definition, adaptively weighted derivation, variance and CLT conditions, denominator cancellation. Integrated after p31. |
| 31 | Inference, average/IPW obstacles, adaptive weighting, pivot, variance estimator and interpretation. Translated in full. |

## Uncertainties and editorial choices

- P1 squared-error loss parenthesis is read as a contrast with regret; no external content added.
- P3 first IPW proof line lacks Y in the scan; translation shows the consistent full equation and explicitly records the omission.
- P5 marginal citation is read as Wager [2020], with the year marked uncertain.
- P6 the author's “not quite right” reservation on the optimality wording is preserved.
- P11 W has no precise subscript in the naive and stratified estimators. No specific treatment target is invented.
- P13 gamma_i0 is visibly written 0. The translation distinguishes literal transcription from the value 1 required by the preceding product. The missing conditioning argument has the author's original question recorded.
- P15 the source's final unbiasedness claim is not presented as a fully specified theorem.
- P16 intervention values alternate between x_j and w_j; a denominator question “1?” is retained.
- P17 the handwritten blocking definition mentions an individual path. The all-path condition for d-separation is a labeled clarification.
- P20 a small top red phrase is partly unclear. Its legible adjustment/back-door content is translated; the uncertainty is declared.
- P22 distribution notation is equated with an outcome-valued function in the source. It is preserved with a note. The author questions identifiability; no cross-world conclusion is silently supplied.
- P25/p27/p28 use equality for a regret upper bound. Both literal source usage and intended inequality are explicitly distinguished.
- P26 the author's attempted Gaussian/Hoeffding derivation is retained as unresolved, including duplicated b notation and concern about unbounded outcomes.
- P27 two arm indices read 0, while the accompanying definition specifies k. The translation uses k and records the discrepancy.
- P28 a two-sided control is needed for a displayed implication while only one side is written. This is labeled as a gap in the notes, not filled in as original work.
- P29 one peripheral parenthetical aside is unclear; no guessed assertion substituted.
- P30 notation is a martingale with conditional variance of M_t given past, equivalently the new increment. The repeated equation number (14.8) is labeled as such.
- P31 the source's categorical statement about nonnormal limits is translated with its unstated-condition limitation explicitly recorded.

## Production

Body fragment: `english/src/stats2-body.tex`. Standard LaTeX with amsmath/amssymb and the parent-provided `sourcepages` macro. No custom graphics dependencies. Small DAGs are faithfully encoded as directed edge equations; the treatment-response diagram is a table. PDF build and visual QA are handled by the parent agent.
