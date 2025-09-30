-- Establish the formulas below by mathematical induction:
--   $1 + 2 + 3 + \ldots  + n = \frac{n(n+1)}{2}$ for all n $\geq{1}$.

import Mathlib.Tactic
import Mathlib.Data.Nat.Basic
--import Mathlib.Data.Nat.Arithmetic
--import Mathlib.Algebra.BigOperators.Basic

--open BigOperators

import Mathlib.Data.Nat.Basic
--import Mathlib.Algebra.BigOperators.Basic

open BigOperators Finset

theorem sum_id (n : ℕ) : ∑ i ∈ range (n + 1), i = n * (n + 1) / 2

-- import Mathlib.Tactic


--theorem sum_natural_numbers (n : ℕ) : ∑ i ∈ Finset.range (n + 1), i = n * (n + 1) / 2 := by
--  induction' n with k IH
--  · simp
--  · rw [Finset.sum_range_succ, IH]
--    ring_nf

--theorem sum_formula (n : ℕ) : ∑ i ∈ Finset.range n, (i + 1) = n * (n + 1) / 2 := by
--  induction n with
--  | zero => simp
--  | succ n ih =>
--    cases n with
--    | zero => simp
--    | succ n =>
--      simp_all [Finset.sum_range_succ, Nat.mul_add, Nat.add_mul]
--      ring_nf at *
--      omega
