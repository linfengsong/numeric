-- Establish the formulas below by mathematical induction:
--   $1^2 + 3^2 + 5^2 + \ldots + (2n - 1)^2 = \frac{n(2n-1)(2n+1)}{3}$ for all n $\geq{1}$.

import Mathlib.Tactic

theorem sum_of_odd_squares (n : ℕ) :
  ∑ k ∈ Finset.range n, (2 * k + 1) ^ 2 = n * (2 * n - 1) * (2 * n + 1) / 3 := by
  induction n with
  | zero =>
    -- Base case: n = 0
    simp
  | succ n ih =>
    -- Inductive step: assume the statement holds for n, prove for n+1
    cases n with
    | zero =>
      -- Base case: n = 1
      simp [Finset.sum_range_succ, Nat.mul_div_cancel_left]
    | succ n =>
      -- Inductive step: n = k + 1
      simp_all [Finset.sum_range_succ, Nat.mul_div_cancel_left, Nat.mul_sub_left_distrib,
        Nat.mul_add, Nat.add_mul, Nat.mul_one, Nat.mul_assoc]
      ring_nf at *
      omega
