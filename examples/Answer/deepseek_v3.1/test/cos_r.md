I will prove the identity \(\cos{\frac{\pi}{7}} - \cos{\frac{2\pi}{7}} + \cos{\frac{3\pi}{7}} = \frac{1}{2}\).

**Proof:**

Let \(S = \cos{\frac{\pi}{7}} - \cos{\frac{2\pi}{7}} + \cos{\frac{3\pi}{7}}\).

We use the identity for the sum of cosines in arithmetic progression. Consider the sum:
\[
\sum_{k=1}^{3} \cos\left(\frac{(2k-1)\pi}{7}\right) = \cos\frac{\pi}{7} + \cos\frac{3\pi}{7} + \cos\frac{5\pi}{7}.
\]
But note that \(\cos\frac{5\pi}{7} = -\cos\frac{2\pi}{7}\) (since \(\cos(\pi - x) = -\cos x\)), so:
\[
\cos\frac{\pi}{7} + \cos\frac{3\pi}{7} + \cos\frac{5\pi}{7} = \cos\frac{\pi}{7} + \cos\frac{3\pi}{7} - \cos\frac{2\pi}{7} = S.
\]
Thus, \(S = \sum_{k=1}^{3} \cos\left(\frac{(2k-1)\pi}{7}\right)\).

Now, there is a known formula for the sum of cosines of odd multiples of an angle:
\[
\sum_{k=1}^{n} \cos((2k-1)\theta) = \frac{\sin(2n\theta)}{2\sin\theta}.
\]
Here, \(n=3\) and \(\theta = \frac{\pi}{7}\), so:
\[
S = \frac{\sin(6\pi/7)}{2\sin(\pi/7)}.
\]
But \(\sin(6\pi/7) = \sin(\pi - \pi/7) = \sin(\pi/7)\), so:
\[
S = \frac{\sin(\pi/7)}{2\sin(\pi/7)} = \frac{1}{2}, \quad \text{provided } \sin(\pi/7) \neq 0.
\]
Since \(\sin(\pi/7) \neq 0\), we conclude:
\[
\cos{\frac{\pi}{7}} - \cos{\frac{2\pi}{7}} + \cos{\frac{3\pi}{7}} = \frac{1}{2}.
\]

**Lean Statement:**
```lean
import data.real.basic
import analysis.special_functions.trigonometric.basic

open real

theorem cos_sum_eq_half : cos (π/7) - cos (2*π/7) + cos (3*π/7) = 1/2 :=
begin
  have h1 : cos (5*π/7) = -cos (2*π/7),
  { rw [cos (π - 2*π/7), cos_sub_pi], ring_nf, exact (cos (2*π/7)).symm.neg },  -- Actually: cos(π - x) = -cos x
  have S_eq : cos (π/7) - cos (2*π/7) + cos (3*π/7) = cos (π/7) + cos (3*π/7) + cos (5*π/7),
  { rw [h1], ring },
  have sum_formula : cos (π/7) + cos (3*π/7) + cos (5*π/7) = sin (6*π/7) / (2 * sin (π/7)),
  { -- Use formula for sum of cosines of odd multiples: ∑_{k=1}^n cos((2k-1)θ) = sin(2nθ)/(2 sin θ)
    -- Here n=3, θ=π/7.
    have := sum_cos_odd_mul 3 (π/7),  -- This would be a custom lemma; need to prove or use existing.
    -- Alternatively, derive directly using trigonometric identities.
    sorry  -- Placeholder for the detailed proof in Lean.
  },
  have h2 : sin (6*π/7) = sin (π/7),
  { rw [sin (π - π/7)], exact sin (π/7) },
  rw [h2] at sum_formula,
  have : sin (π/7) ≠ 0 := by apply sin_ne_zero_of_ne_zero; linarith [pi_pos],
  field_simp [this] at sum_formula,
  exact S_eq.trans sum_formula,
end
```

**Note:** The Lean proof above is a sketch. The actual implementation would require proving the sum formula for cosines of odd multiples (which can be done by induction or using complex exponentials) and ensuring all steps are rigorous. The key steps are:
1. Relate the expression to the sum \(\cos(\pi/7) + \cos(3\pi/7) + \cos(5\pi/7)\).
2. Use the identity \(\cos(5\pi/7) = -\cos(2\pi/7)\).
3. Apply the formula \(\sum_{k=1}^n \cos((2k-1)\theta) = \frac{\sin(2n\theta)}{2\sin\theta}\) for \(n=3\), \(\theta=\pi/7\).
4. Simplify using \(\sin(6\pi/7) = \sin(\pi/7)\).

The result is \(\frac{1}{2}\).

**Output in normal language:**
The sum \(\cos(\frac{\pi}{7}) - \cos(\frac{2\pi}{7}) + \cos(\frac{3\pi}{7})\) equals \(\frac{1}{2}\). This is proven by rewriting the expression as the sum of cosines of odd multiples of \(\pi/7\) (namely \(\pi/7, 3\pi/7, 5\pi/7\)), using the identity \(\cos(5\pi/7) = -\cos(2\pi/7)\). Then, applying the formula for the sum of cosines in arithmetic progression gives \(\frac{\sin(6\pi/7)}{2\sin(\pi/7)}\), which simplifies to \(\frac{1}{2}\) because \(\sin(6\pi/7) = \sin(\pi/7)\).