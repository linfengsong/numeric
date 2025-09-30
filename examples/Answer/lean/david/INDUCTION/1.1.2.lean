-- If $r \neq 1$, show that for any positive integer n,
-- $$a + ar + ar^2 + \ldots + ar^n = \frac{a(r^{n+1}-1)}{r-1}$$

import Mathlib.Tactic

theorem geometric_series_sum (a r : ℚ) (n : ℕ) (h : r ≠ 1) :
    ∑ k ∈ Finset.range (n + 1), a * r ^ k = a * (r ^ (n + 1) - 1) / (r - 1) := by
  induction n with
  | zero =>
    -- Base case: n = 0
    simp [mul_comm]
    <;> field_simp [sub_ne_zero.mpr h, sub_ne_zero.mpr h.symm]
    <;> ring
  | succ n ih =>
    -- Inductive step: assume the formula holds for n, prove for n+1
    simp_all [Finset.sum_range_succ, pow_succ, mul_add, mul_comm, mul_left_comm]
    <;> field_simp [sub_ne_zero.mpr h, sub_ne_zero.mpr h.symm] at *
    <;> ring_nf at *
    <;> linarith
  exact h₁
