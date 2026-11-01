# Independent mathematical review of Brave and True, Chapters 1–23

Reviewed source: `note_for_Causal_Inference_for_The_Brave_and_True/Chapter1-23.pdf`.

Scope: all 17 findings currently classified as `original` in `english/reviewed/brave1-findings.json`, their adjacent mathematical annotations in `english/reviewed/src/brave1-body.tex`, and the relevant handwritten scans. This was an independent, read-only review of the frozen body and findings. No changes to those files were made by this reviewer.

**Conclusion:** the 17 source-error classifications are defensible. Two annotation-wording corrections were necessary: B1-041 misattributed column-vector orientation to the handwriting, and B1-015 described overlap as necessary for a conditional-independence implication that does not itself need overlap. Neither correction changes the classification of the original handwritten error. Both were reported to the root editor; B1-041 was confirmed corrected and the B1-015 correction was accepted.

## Required annotation corrections

### B1-041: source coefficients are row vectors

Source pages: **18 and 34**; explicit coefficient orientation appears on **p. 34**.

The scan says each feature is a column, each observation a row, and the coefficient vectors are **row vectors** (“β1、β2 为行向量”). The previous review annotation and JSON diagnosis incorrectly attributed *column* coefficient vectors to the scan.

The original matrix products are still dimensionally inconsistent. For the scan's convention,
\[
X_j\in\mathbb R^{n\times p_j},\qquad
\widehat\beta_j\in\mathbb R^{1\times p_j},
\]
a conformable fitted column of outcomes is
\[
\widehat Y=X_1\widehat\beta_1^\top+X_2\widehat\beta_2^\top.
\]
Equivalently, explicitly switch to column coefficient vectors and write
\(\widehat Y=X_1\widehat b_1+X_2\widehat b_2\).
For residualization, \(\widehat X_1=P_{X_2}X_1\).
The source's \(\widehat\beta_jX_j\) does not follow its stated layout. The FWL argument itself remains valid.

The correction must distinguish this genuine source error from our erroneous description of what the scan says. The official Chapter 22 prose also calls the coefficients row vectors while displaying the inconsistent product, so it does not justify silently reinterpreting the handwriting as column vectors. [Handbook, Chapter 22](https://matheusfacure.github.io/python-causality-handbook/22-Debiased-Orthogonal-Machine-Learning.html).

### B1-015: separate conditional independence from overlap

Source page: **13**.

The source's equivalence between a balancing identity and ignorability is false, so the original-error classification is correct. However, overlap is not needed for the mathematical implication
\[
(Y(0),Y(1))\perp T\mid X
\quad\Longrightarrow\quad
(Y(0),Y(1))\perp T\mid e(X),
\qquad e(X)=P(T=1\mid X).
\]

Indeed, writing \(U=(Y(0),Y(1))\), for any measurable set \(A\),
\[
\begin{aligned}
E[T\,\mathbf1\{U\in A\}\mid e]
&=E\!\left[E[T\mid U,X]\,\mathbf1\{U\in A\}\mid e\right]\\
&=E[e(X)\mathbf1\{U\in A\}\mid e]\\
&=e\,P(U\in A\mid e).
\end{aligned}
\]
The corresponding relation for \(1-T\) follows too. This proves the binary-treatment conditional independence even at \(e=0\) or \(e=1\), where treatment is conditionally constant.

Correct wording: **conditional exchangeability given \(X\) implies conditional exchangeability given the true propensity score; overlap is additionally required to identify both-arm causal contrasts over the target population.** The true propensity balances \(X\) regardless of whether treatment is causally unconfounded. [Handbook, Chapter 11](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html).

## All 17 classifications

| Finding | Original PDF pages | Independent conclusion |
|---|---:|---|
| B1-007 | 4 | Confirmed. FWL residual treatment comes from regressing \(T\) on \(X\), not covariates on treatment. The author's blue addition already gives the intended direction. With an appropriate intercept and full-rank controls, \(\widetilde T=(I-P_X)T\) and the treatment slope is \(\widetilde T^\top Y/(\widetilde T^\top\widetilde T)\). |
| B1-011 | 8 | Confirmed, with the author's own red correction acknowledged. Potential-outcome exclusion \(Y(t,z)=Y(t)\) is not \(Y\perp Z\mid T\). Conditioning on collider \(T\) can open \(Z\to T\leftarrow W\to Y\), even for a valid instrument. Instrument exogeneity is a separate IV condition. |
| B1-013 | 9, 10, 23 | Confirmed. Population monotonicity permits equality: \(T(1)\ge T(0)\) almost surely, with positive complier probability for the ratio. Strict inequality for everyone excludes the never- and always-takers drawn in the notes. Under the other IV conditions the Wald estimand is LATE, not unrestricted population ATE. The same non-strict ordering is relevant to the fuzzy-RD discussion. |
| B1-015 | 13 | Confirmed source error; annotation wording required the overlap correction above. A balancing identity does not by itself imply potential-outcome ignorability. |
| B1-017 | 15 | Confirmed. \(E[\widehat\mu_1(X_i)]=Y_i\) is not an identity. Doubly robust cancellations are conditional expectation statements. For fixed nuisance functions, a correct outcome regression makes \(E[T\{Y-\mu_1(X)\}/q(X)\mid X]=0\), with valid nonzero denominators; a correct propensity yields the corresponding identity for arbitrary outcome regression. The ATE outcome-model route concerns both arms. |
| B1-021 | 22, 23 | Confirmed. In an uncentered model with \(D=\mathbf1\{R>c\}\), the jump from \(\beta_2D+\beta_3DR\) is \(\beta_2+\beta_3c\). After centering \(r=R-c\), the coefficient on \(D\) is the jump. |
| B1-023 | 24 | Confirmed. A large \(p\)-value is not evidence that the effect magnitude is small. The standard error and effect size jointly determine the test statistic. |
| B1-024 | 25 | Confirmed. For nonconstant outcomes the usual \(1-\mathrm{SSE}/\mathrm{SST}\) includes \(1\). In-sample OLS with an intercept gives \([0,1]\); out-of-sample values can be negative. Constant outcomes require a separate convention. |
| B1-027 | 29 | Confirmed. \((Y(0),Y(1))\perp X\) does not establish comparability of treatment groups. The relevant randomized-assignment statement uses \(T\), or observational identification uses exchangeability conditional on \(X\). |
| B1-028 | 29 | Confirmed. Individual-effect risk equals CATE prediction risk plus \(E[\operatorname{Var}\{Y(1)-Y(0)\mid X\}]\), for a fixed or independently trained prediction. The two risks generally share a minimizer, not the same value. |
| B1-031 | 31 | Confirmed. \(M\) predicts treatment from covariates, so its input is \(X_i\). A single squared treatment residual is not conditional treatment variance. Dividing by it produces an unstable individual ratio, not a generally unbiased CATE target. A residual ratio with squared-residual weights can instead re-express R-loss, retaining the undivided objective at zero residual. The author's tentative/numerical caveat should remain visible. |
| B1-034 | 36 | Confirmed. A flexible R-loss learner \(\tau(X)\) targets a conditional linear projection slope for a nonlinear treatment response, not automatically the derivative at the current treatment. Detailed derivation below. |
| B1-035 | 37; output-label issue on 38 | Confirmed. If training residual is \(T-\widehat m(X)\), prediction must use \(T_{\mathrm{new}}-\widehat m(X)\), not the reverse. The final residual-outcome learner predicts residual sales, not price. |
| B1-037 | 39 | Confirmed. The handwritten unscaled income distribution and zero threshold do not generate the quoted conversion effect. The textbook code uses income multiplied by 100 and threshold \(0.1\); its \(0.39477\) is a simulated sample contrast. The latent-scale population ATE \(1.4\) is correct under the stated shape–scale Gamma convention. Detailed check below. |
| B1-038 | 39 | Confirmed. For a fixed positive latent shift \(\delta\), the conversion effect is \(\Phi(a+\delta-c)-\Phi(a-c)\), which tends to zero at both extremes of \(a\). Low baseline conversion does not universally imply a large effect. The preceding handwritten both-tail saturation intuition is correct. |
| B1-041 | 18, 34 | Confirmed source dimension error, but the review's claim that the scan states column coefficients was itself a transcription/attribution error. Correct as specified above. |
| B1-043 | 29 | Confirmed. The blue word “unrelated” is legible. In a correctly specified exogenous OLS model with full-rank design, an irrelevant covariate does not itself create coefficient bias. Detailed argument below. |

## Focused independent derivations

### B1-034: nonlinear treatment response and R-loss

Let \(m(x)=E[T\mid X=x]\), \(\ell(x)=E[Y\mid X=x]\), and assume finite conditional second moments and \(\operatorname{Var}(T\mid X=x)>0\). At a fixed \(x\), minimize
\[
Q_x(a)=E\!\left[\{Y-\ell(x)-a(T-m(x))\}^2\mid X=x\right].
\]
The first-order condition gives
\[
a^*(x)=
\frac{E[(T-m(x))(Y-\ell(x))\mid X=x]}
     {E[(T-m(x))^2\mid X=x]}
=
\frac{\operatorname{Cov}(T,Y\mid X=x)}
     {\operatorname{Var}(T\mid X=x)}.
\]
If \(E[Y\mid T=t,X=x]=g(x)+\tau(x)t\), this equals \(\tau(x)\), the treatment derivative. For an arbitrary nonlinear response it is a projection coefficient.

The existing annotation's example, \(Y=T^2\), \(T\sim U(0,1)\), correctly gives slope \(1\) while the derivative function is \(2t\). Although they coincide at \(t=1/2\), this coincidence does not identify the derivative function. An optional stronger example is \(Y=T^3\):
\[
a^*=\frac{1/5-(1/2)(1/4)}{1/12}=\frac9{10},
\qquad
\left.\frac{d(t^3)}{dt}\right|_{t=E[T]}=\frac34.
\]
Even the derivative at the mean treatment need not equal the projection slope.

The official Chapter 22 nonlinear code additionally feeds residual treatment into the final learner. This differs from the usual final learner \(\tau(X)\); it does not rescue the general derivative claim. In an intercept-only residualization example with response \(g(t)\), an unrestricted ratio learner at nonzero \(r=t-E[T]\) instead targets
\[
\frac{g(t)-E[g(T)]}{t-E[T]},
\]
a centered ratio rather than \(g'(t)\). Thus the annotation's warning is justified, while its projection formula should be understood as applying to the displayed R-loss with a coefficient depending on \(X\). [Handbook, Chapter 22](https://matheusfacure.github.io/python-causality-handbook/22-Debiased-Orthogonal-Machine-Learning.html), [Nie–Wager, R-learner](https://arxiv.org/abs/1712.04912).

### B1-037: latent and binary conversion effects are different

Use shape–scale notation:
\[
A\sim\Gamma(10,4),\quad I\sim\Gamma(20,2),\quad
L(t)=-4.5+0.001I+t(1+0.01A)+\varepsilon,
\quad\varepsilon\sim N(0,1).
\]
The latent contrast is \(1+0.01A\), hence
\[
E[L(1)-L(0)]=1+0.01(10\cdot4)=1.4.
\]
For the handwritten conversion threshold zero, however, the population contrast is
\[
E\!\left[\Phi(-3.5+0.001I+0.01A)
          -\Phi(-4.5+0.001I)\right].
\]
It is not \(1.4\), nor does the handwritten parameterization yield the quoted \(0.394\).

As an independent numerical diagnostic, 80-node generalized Gauss–Laguerre quadrature, assuming the independent Gamma draws used by the simulation, gave:

| Quantity under the handwritten unscaled DGP | Approximate value |
|---|---:|
| Control conversion probability | 0.0000041014 |
| Treated conversion probability | 0.0012072323 |
| Population conversion ATE | 0.0012031309 |
| Overall conversion with 50% treatment | 0.0006056669 |

These are quadrature evaluations of the displayed expectation, not reproduced Monte Carlo sample results. They strongly separate the written DGP from the reported number.

The official code uses \(100\,\Gamma(20,2)\) for income and a threshold \(0.1\). It reports a simulated difference \(0.3947727\ldots\); this should not be relabeled the exact population ATE. The same quadrature calculation for that code's DGP gives a population conversion contrast about \(0.39921\), which is compatible with a different finite-sample contrast. The review annotation correctly distinguishes the source prose/code mismatch and the scale of the effect. [Handbook, Chapter 23](https://matheusfacure.github.io/python-causality-handbook/23-Challenges-with-Effect-Heterogeneity-and-Nonlinearity.html).

### B1-043: irrelevant covariates and OLS bias

For the interaction design \(Z=[1,T,X,TX]\), assume
\[
Y=Z\beta+\varepsilon,\qquad E[\varepsilon\mid Z]=0,
\]
and \(Z^\top Z\) invertible. Then
\[
E[\widehat\beta\mid Z]
=\beta+(Z^\top Z)^{-1}Z^\top E[\varepsilon\mid Z]
=\beta.
\]
This remains true if \(X\) and its interaction are irrelevant, with their population coefficients equal to zero. Therefore irrelevance alone cannot imply bias in the treatment coefficient or interaction coefficient.

For a concrete counterexample to the handwriting's blanket claim, take independent \(T,X,\varepsilon\), with \(E[\varepsilon]=0\), and \(Y=\beta_0+\beta_1T+\varepsilon\). Adding \(X\) and \(TX\) to an otherwise valid full-rank OLS regression does not generate bias. It can affect precision, and regularized or misspecified procedures require separate analysis. The annotation's exogeneity and rank conditions make its correction mathematically sound. The derivative in the source's interaction model is \(\beta_1+\beta_3X\), so the observation that \(\beta_2\) drops out remains valid. [Handbook, Chapter 5](https://matheusfacure.github.io/python-causality-handbook/05-The-Unreasonable-Effectiveness-of-Linear-Regression.html).

## Remaining qualifications

No further mathematical changes to the 17 original-error annotations are required from this review after the B1-041 and B1-015 wording corrections. B1-011 records a proposition the author already questioned and corrected in red, and B1-031 concerns an explicitly tentative proposed formula; the reviewed text should continue to preserve those statuses. The optional cubic counterexample for B1-034 is explanatory enrichment, not a required repair.
