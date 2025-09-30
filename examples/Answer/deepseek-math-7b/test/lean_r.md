### Lean4 Proof
```lean4
theorem imo_1963_p5 : Real.cos (Real.pi / 7) - Real.cos (2 * Real.pi / 7) + Real.cos (3 * Real.pi / 7) = 1 / 2 := by
  have h₁ : Real.cos (Real.pi / 7) - Real.cos (2 * Real.pi / 7) + Real.cos (3 * Real.pi / 7) = 1 / 2 := by
    have h₂ : Real.cos (Real.pi / 7) - Real.cos (2 * Real.pi / 7) + Real.cos (3 * Real.pi / 7) = 1 / 2 := by
      have h₃ : Real.cos (Real.pi / 7) - Real.cos (2 * Real.pi / 7) + Real.cos (3 * Real.pi / 7) = 1 / 2 := by
        -- Use the sum-to-product and product-to-sum identities to simplify the expression.
        have h₄ : Real.cos (Real.pi / 7) - Real.cos (2 * Real.pi / 7) = 2 * Real.sin (3 * Real.pi / 14) * Real.sin (Real.pi / 14) := by
          rw [Real.sin_sub_sin] <;> ring_nf <;>
          norm_num <;>
          ring_nf <;>
          norm_num <;>
          ring_nf <;>
          norm_num
        have h₅ : Real.cos (3 * Real.pi / 7) = Real.cos (3 * Real.pi / 7) := by rfl
        have h₆ : Real.cos (3 * Real.pi / 7) = Real.cos (3 * Real.pi / 7) := by rfl
        have h₇ : Real.cos (3 * Real.pi / 7) = Real.cos (3 * Real.pi / 7) := by rfl
        have h₈ : Real.cos (3 * Real.pi / 7) = Real.cos (3 * Real.pi / 7) := by rfl
        have h₉ : Real.sin (3 * Real.pi / 14) * Real.sin (Real.pi / 14) ≥ 0 := by
          apply mul_nonneg
          exact Real.sin_nonneg_of_mem_Icc ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩
          exact Real.sin_nonneg_of_mem_Icc ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩
        nlinarith [Real.cos_le_one (3 * Real.pi / 7), Real.cos_le_one (2 * Real.pi / 7), Real.cos_le_one (Real.pi / 7),
          Real.sin_sq_add_cos_sq (3 * Real.pi / 14), Real.sin_sq_add_cos_sq (Real.pi / 14),
          Real.sin_sq_add_cos_sq (Real.pi / 7), Real.sin_sq_add_cos_sq (2 * Real.pi / 7)]
      exact h₃
    exact h₂
  exact h₁
```