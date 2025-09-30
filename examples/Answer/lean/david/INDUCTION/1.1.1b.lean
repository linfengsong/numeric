-- Establish the formulas below by mathematical induction:
--   $1 + 3 + 5 + \ldots + (2n - 1) = n^2$ for all n $\geq{1}$.

import Mathlib.Tactic

theorem sum_of_odd_numbers (n : ℕ) : ∑ k ∈ Finset.range n, (2 * k + 1) = n^2 := by
  induction n with
  | zero => simp
  | succ n ih =>
    cases n with
    | zero => simp
    | succ n =>
      simp_all [Finset.sum_range_succ, Nat.pow_succ, Nat.mul_succ]
      ring_nf at *
