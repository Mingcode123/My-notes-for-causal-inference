# Independent mathematical review of selected STATS361 corrections

Reviewed: `stats1-findings.json`, corresponding passages in `src/stats1-body.tex` and `src/stats1-tail.tex`, the original scans, and the local official STATS361 lecture text. This was an independent derivation and read-only review of the existing corrections; no body or findings files were changed by this reviewer.

Result: all seven selected `original` classifications are supported by the handwriting and the mathematics. No correction needs to be withdrawn. Source pages below refer to `note_for_Causal _inference_STATS_361/Lecture1-10.pdf`.

## S1-003 — Misspecified OLS covariance

Source: scan page 3; official lecture equation (1.16).

The source visibly places zero in the intercept–slope covariance blocks. Centering X gives a block-diagonal design moment matrix, but does not generally give a block-diagonal sandwich covariance. Let q=(1,X')', Q=E[qq'], and r=Y-c*-X' beta*. The influence function is Q^-1 q r, so its covariance is Q^-1 E[r^2 qq'] Q^-1. The off-diagonal block depends on E[r^2 X], whereas projection orthogonality only gives E[r X]=0.

This remains a real error under the page's homoskedastic original-noise assumption. For example, take X standard normal, Y=X^2+X^3+epsilon, with independent centered homoskedastic epsilon. Then c*=1, beta*=3, and r=(X^2-1)+(X^3-3X)+epsilon. Here E[X r^2]=12, not zero. The correction's intercept variance and subsequent balanced-trial variance-reduction identity remain valid; they only require the relevant projection orthogonality.

Verdict: correction confirmed; no necessary adjustment.

## S1-014 — Robinson sandwich uses the regression residual

Source: scan page 18; official lecture equation (4.6).

The scan and official lecture both put Var(Ztilde Ytilde) in the middle of the sandwich. With Ytilde=Z' beta+epsilon and Q=E[ZZ'], OLS satisfies

sqrt(n)(beta_hat-beta) = Q^-1 n^-1/2 sum_i Z_i epsilon_i + o_p(1).

Therefore the covariance is Q^-1 E[ZZ' epsilon^2] Q^-1, since E[Z epsilon]=0. Randomness in the estimated Gram matrix cancels the ZZ' beta part of Z Ytilde; retaining Var(Z Ytilde) incorrectly leaves that contribution in the variance.

A simple check: let W be Bernoulli(1/4), Z=W-1/4, Ytilde=Z, and epsilon=0. The through-origin OLS coefficient equals one exactly for every sample, while Var(Z Ytilde)=Var(Z^2)>0. This directly falsifies the original middle term. Under conditional homoskedasticity, the corrected covariance reduces to b^2 Q^-1 as stated.

Verdict: correction confirmed; no necessary adjustment.

## S1-019 — Local-linear weight normalization

Source: scan page 24.

The scan defines the hatted moments as in-band sample averages and then uses an unnormalized sum of gamma_i Y_i. Write N for the number of in-band observations, u_i=Z_i-c, m_1=N^-1 sum u_i and m_2=N^-1 sum u_i^2. The original gamma_i=(m_2-m_1 u_i)/(m_2-m_1^2) sums to N. The corrected weights divide by N and give both sum gamma_i=1 and sum gamma_i u_i=0, provided m_2-m_1^2>0.

Verdict: original omission and proposed correction confirmed.

## S1-026 — Convexity does not ensure uniqueness and attainment

Source: scan page 35; official lecture equation (7.10).

The original explicitly claims a unique solution from the convex objective. The stated Hessian, n^-1 sum_i W_i exp(-X_i theta) X_i'X_i, is positive semidefinite; full treated-covariate span gives positive definiteness at finite theta. Existence of a finite minimizer is an additional question, not a consequence of convexity or strict convexity.

The current correction is valid. An optional precision is useful when an intercept is included: the first-order conditions can be rearranged as sum_treated exp(-X_i theta) X_i = sum_control X_i. Their intercept component fixes the positive exponential weights to sum to the control count. Thus the control-group covariate mean must lie in the appropriate relative interior of the treated convex support for a nondegenerate finite calibration solution. Merely saying that the overall target mean lies inside the treated hull would not be a sufficient existence condition; the existing text does not assert that converse.

Verdict: correction confirmed; optional clarification only.

## S1-036 — IV asymptotic scaling

Source: scan pages 47–48; official lecture equation (9.12).

The main scan on page 47 visibly writes n rather than sqrt(n); the supplementary estimating-equation result uses the conventional scaling. A first-order ratio expansion gives

sqrt(n)(tau_hat_w-tau) = [n^-1/2 sum_i (w(Z_i)-E[w(Z)]) epsilon_i] / Cov(W,w(Z)) + o_p(1)

under the stated centered-error, IID, finite-moment and nonzero-denominator conditions. Independence of epsilon and Z gives the displayed variance product. If errors are not centered, the general expression uses epsilon_i-E[epsilon]; the correction already states centered errors, consistent with the red source annotation.

Verdict: original scaling error and correction confirmed.

## S1-037 — Optimal instrument maximizes the ratio

Source: scan page 47; official lecture equations (9.13)–(9.15).

The scan writes argmin of Cov(W,w(Z))^2/Var(w(Z)), while the asymptotic variance is proportional to the reciprocal of that ratio. The ratio must therefore be maximized. With m(Z)=E[W|Z],

Cov(W,w)^2 = Cov(m,w)^2 <= Var(m) Var(w).

For Var(m)>0 equality is attained by w=a+b m with b nonzero. This also validates the source's prediction intuition. The correction appropriately confines the result to the source's independent-error/homoskedastic-instrument setting rather than claiming a general heteroskedastic optimal-instrument theorem.

Verdict: correction confirmed; no necessary adjustment.

## S1-048 — Stieltjes formulation including singular variation

Source: scan pages 54–57, particularly page 55's bottom representation and page 56's distributional-derivative supplement; official lecture equations (10.7)–(10.11) and footnote 4.

The source says a monotone cutoff can be represented by the integral of an ordinary nonnegative Lebesgue-integrable derivative. This is false for general bounded monotone functions. A right-continuous nondecreasing cutoff has a Stieltjes measure dc, which may contain an absolutely continuous part, jump atoms, and a singular continuous part. Removing jumps alone does not imply absolute continuity.

The proposed comprehensive formula is correct. Put F(u)=integral_0^u tau(v) dv. Under the threshold model W=1{U>=c(Z)}, uniform U, and the source's exogeneity assumptions,

E[W|Z=z]=1-c(z),
E[Y|Z=z]=E[Y(0)]+F(1)-F(c(z)).

For standard Gaussian Z and bounded-variation conditional means, Stieltjes integration by parts gives

Cov(W,Z) = - integral phi(z) dc(z),
Cov(Y,Z) = - integral phi(z) d[F(c(z))].

The two minus signs cancel, giving exactly the ratio in the correction. At a jump z, the numerator measure has mass F(c(z))-F(c(z-))=integral_[c(z-),c(z)] tau(u) du. This preserves the author's strip interpretation. It also avoids interpreting a Dirac mass as an ordinary pointwise function.

A useful explicit condition sentence is: c maps R to [0,1], is right-continuous, nondecreasing and nonconstant; the required outcome moments exist and tau is bounded or appropriately integrable. Since phi is strictly positive, nonconstant c gives integral phi dc>0. The source's relevance condition already supplies the nontriviality, but making the denominator condition explicit improves the new standalone formula. The main STATS1 agent was asked to add these conditions.

### Cantor cutoff counterexample

Let C be the Cantor function on [0,1], extended by zero to z<0 and by one to z>1. Set c=C, let U be uniform and independent of standard Gaussian Z, and choose Y(0)=0 and Y(1)=1. Then tau(u)=1 everywhere. This is a continuous, nondecreasing, nonconstant cutoff with c'(z)=0 Lebesgue-almost everywhere and no jumps.

The original jump-plus-ordinary-derivative representation gives zero in both numerator and denominator. But W is nontrivial, Y=W, and hence the IV covariance ratio is exactly one. The Stieltjes formula correctly gives

[integral phi dC] / [integral phi dC] = 1,

where the positive measure dC is singular continuous. This verifies both the diagnosis and the proposed repair without relying on the official lecture's erroneous general statement.

Verdict: correction and comprehensive Stieltjes formula confirmed; make the stated support, regularity and nonzero-denominator conditions explicit.

## Reference

[Official STATS361 lecture notes](https://web.stanford.edu/~swager/stats361.pdf), checked against the local PDF/text. The reasoning above was independently derived; agreement with the official source was not taken as proof of correctness.
