# Independent content review: STATS 361 Lectures 11-14

Reviewer: separate translation agent. This is a source-fidelity review, not a mathematical verification against the textbook.

## Scope

Compared `stats2-body.tex` with original scans pp. 2-7, 9-10, 18-19, 23-24, 26-28, 30-31. This includes every requested supplementary page (2, 4, 6, 9, 18, 23, 26, 30) and the corresponding main pages. Magnified p.4 and p.6 marginal text for confirmation.

## Required correction

**Source p.4, red bottom margin: the superefficiency observation is reversed.**

The scan reads: `也有超效率，固定 π(x)，观察 n 个时收敛速率，可能会超 sqrt(VC(Π)/n)`.

Current English: `at a fixed policy π(x) and n observations, the convergence rate cannot be faster than ...`.

Suggested replacement: `The author also notes a possible superefficiency caveat: for a fixed policy π(x), the convergence rate with n observations may be faster than sqrt(VC(Π)/n). This is a pointwise observation in the margin, rather than a replacement for the preceding worst-case rate.`

Do not change the main regret bound. The needed change is to retain the author's own exception/intuition instead of reversing it.

## Other checked material

- p.2 IPW analogy: complete algebra retained.
- pp.3/5: indicator cancellation, baseline/effect split, earn/pay intuition and weighted classification preserved.
- p.6: efficiency bound and the red `不太对...` reservation correctly retained as `Not quite right...`.
- pp.9-10: time-history diagram and author's judgment that complete randomization is unreasonable are preserved.
- pp.18-19: all three do-calculus mnemonics and graph-edge conventions are retained.
- pp.23-24: K treatments per individual, only one observed potential outcome, common best arm, and sublinear-regret intuition are preserved.
- pp.26-28: the author's unfinished Hoeffding attempt, concern about unbounded Gaussian outcomes, unknown simplification, union-bound connection, and threshold intuition are preserved. Translator clarification is distinctly labeled.
- pp.30-31: martingale definition, numerator derivation, variance stabilization, slow probability decay, log(T) sampling caveat, and denominator cancellation are preserved.

No additional omissions or mathematical transcription errors found in these sampled pages. No body edits were made by this reviewer.

## Additional spot review: Lectures 1-10

Compared `stats1-body.tex` against pp.20-22 and pp.28-30. The R-loss and lasso formulas; RDD overlap-failure supplement; local-linear objective; signed weight sums and sketch; minimax remainder constraints; bias-aware normal interval; and discrete/multivariate-running-variable annotations are faithfully represented. No required correction found in this sample.

## Resolution

The root editor verified the reported source-reading corrections and applied them to the final LaTeX body before the final build. No reported content fix remains pending.
