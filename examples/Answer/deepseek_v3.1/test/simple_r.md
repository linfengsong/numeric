Let's find the integral of \( x^2 \) from 0 to 2 step by step.

The integral we need to compute is:
\[
\int_{0}^{2} x^2  dx
\]

To find the antiderivative of \( x^2 \), we use the power rule for integration:
\[
\int x^n  dx = \frac{x^{n+1}}{n+1} + C \quad \text{for } n \neq -1
\]
Here, \( n = 2 \), so:
\[
\int x^2  dx = \frac{x^{3}}{3} + C
\]

Now, we evaluate this antiderivative from 0 to 2:
\[
\left[ \frac{x^3}{3} \right]_{0}^{2} = \frac{(2)^3}{3} - \frac{(0)^3}{3} = \frac{8}{3} - 0 = \frac{8}{3}
\]

Therefore, the integral is \( \frac{8}{3} \).

So, the final answer is:
\[
\boxed{\dfrac{8}{3}}
\]

In normal language: The integral of \( x^2 \) from 0 to 2 is \( \frac{8}{3} \).

Lean statement (to confirm the result):
```lean
import analysis.special_functions.integrals

example : ∫ x in (0:ℝ)..2, x^2 = 8/3 :=
by simp
```
This Lean code uses the `analysis` library to compute the definite integral and confirms that it equals \( \frac{8}{3} \). The `simp` tactic simplifies the expression to verify the result.