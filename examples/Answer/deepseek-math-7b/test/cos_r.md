### Lean4 Proof
```lean4
theorem cos_pi_div_7_minus_cos_2pi_7_plus_cos_3pi_7_eq_half : 
    cos (π / 7) - cos (2 * π / 7) + cos (3 * π / 7) = 1 / 2 := by
  have h₁ : 0 < π / 7 := by linarith [Real.pi_pos]
  have h₂ : 0 < 2 * π / 7 := by linarith [Real.pi_pos]
  have h₃ : 0 < 3 * π / 7 := by linarith [Real.pi_pos]
  have h₄ : cos (π / 7) - cos (2 * π / 7) + cos (3 * π / 7) = 1 / 2 := by
    -- Use the sum-to-product and product-to-sum identities to simplify the expression.
    have h₅ : cos (π / 7) - cos (2 * π / 7) + cos (3 * π / 7) = 1 / 2 := by
      -- Use the sum-to-product and product-to-sum identities to simplify the expression.
      have h₆ : cos (π / 7) - cos (2 * π / 7) = 2 * sin (3 * π / 14) * cos (π / 2) := by
        rw [cos_sub_cos]
        <;> ring_nf
        <;> norm_num
        <;> ring_nf
        <;> norm_num
        <;> ring_nf
        <;> norm_num
      have h₇ : cos (3 * π / 7) = cos (π - 4 * π / 7) := by ring_nf
      rw [h₇] at *
      have h₈ : cos (π - 4 * π / 7) = -cos (4 * π / 7) := by
        rw [cos_pi_sub]
      rw [h₈] at *
      have h₉ : sin (3 * π / 14) > 0 := by
        apply sin_pos_of_pos_of_lt_pi
        linarith [Real.pi_pos]
        linarith [Real.pi_pos]
      have h₁₀ : cos (π / 2) = 0 := by norm_num
      simp_all
      <;> ring_nf
      <;> norm_num
      <;> linarith [Real.pi_pos]
    exact h₅
  exact h₄
```