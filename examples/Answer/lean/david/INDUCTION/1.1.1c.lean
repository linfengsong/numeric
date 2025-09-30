-- Establish the formulas below by mathematical induction:
--   (c) $1 · 2 + 2 · 3 + 3 · 4 + \ldots + n(n + 1) = \frac{n(n+1)(n+2)}{3}$ for all n $\geq{1}$.

import Mathlib.Tactic

theorem sum_product_consecutive (n : ℕ) : ∑ i ∈ Finset.range (n + 1), i * (i + 1) = n * (n + 1) * (n + 2) / 3 := by
  induction n with
  | zero => simp
  | succ n ih =>
    cases n with
    | zero => simp
    | succ n =>
      simp_all [Nat.mul_succ, Nat.succ_eq_add_one, Nat.add_assoc]
      ring_nf
      <;> omega
