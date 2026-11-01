# Independent review of STATS 361 Lectures 11–14 corrections

A second reviewer checked all 14 findings classified as original-note errors against the relevant scans (3, 13, 15, 16, 22, 25, 27, 28, 30, 31), the official lecture, and independent derivations. No original-error classification required withdrawal.

One new editorial error was found and corrected before the final merge: S2-012 originally exempted treatment assignment independent of X1. This is insufficient when the policy varies with X1 and the randomization probability is not one half. The condition now requires the policy-matching probability itself to be constant in the history; the 0.2/0.8 counterexample is included. This was a correction to the new explanation, not an additional error attributed to the notebook.

Checks independently confirmed:

- The sequential IPW recursion starts with the empty product gamma0=1; zero would annihilate every weight. The displayed AIPW telescoping identity is consistent with that initialization.
- Next-history arguments use X(t+1) and the actual prior treatment W1, not the mismatched indices in the scan.
- UCB arm counts give an inequality, with regret summed over strictly positive gaps. Initial pulls contribute the sum of gaps, preventing a uniform bound over unrestricted real arm means.
- The proof requires the other deviation direction. For T>=2, the two-sided Gaussian tail 2 Phi(-2 sqrt(log T)) is at most T^-2, so union over K*T arm/sample-size pairs retains probability at least 1-K/T.
- Nested potential outcomes such as Y(0,Z(1)) are expressible in potential-outcome notation; identifying their distribution is a separate question. A structural random variable is not itself a probability distribution.
- Martingale integrability uses an absolute first moment; the note also acknowledges that a finite real expectation can implicitly impose this condition.

The remaining orange qualifications were not all re-audited in this second pass. Primary-reference URLs and detailed corrections remain in stats2-findings.json and the reviewed body.
