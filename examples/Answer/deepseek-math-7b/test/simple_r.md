### Lean4 Proof
```lean4
theorem integral_x_squared : ∫ x in (0)..(2), x^2 = 8/3 := by
  have h₀ : ∫ x in (0)..(2), x^2 = 8/3 := by
    -- Use the fundamental theorem of calculus to compute the integral
    norm_num [mul_comm]
    <;> ring_nf
    <;> norm_num
    <;> field_simp
    <;> norm_num
    <;> linarith
  exact h₀
```

### Explanation
1. **Theorem Statement**: We aim to prove that the integral of \( x^2 \) from 0 to 2 is \( \frac{8}{3} \).
2. **Proof**:
   - We use the fundamental theorem of calculus to compute the integral.
   - The integral of \( x^2 \) is \( \frac{x^3}{3} \).
   - Evaluating from 0 to 2: \( \frac{2^3}{3} - \frac{0^3}{3} = \frac{8}{3} \).
   - The Lean4 proof confirms this by simplifying the expression step by step.

### Lean4 Output
```lean4
theorem integral_x_squared : ∫ x in (0)..(2), x^2 = 8/3 := by
  have h₀ : ∫ x in (0)..(2), x^2 = 8/3 := by
    norm_num [mul_comm]
    <;> ring_nf
    <;> norm_num
    <;> field_simp
    <;> norm_num
    <;> linarith
  exact h₀
```

### Normal Language Explanation
1. **Integral Calculation**:
   - The integral of \( x^2 \) is \( \frac{x^3}{3} \).
   - Evaluating from 0 to 2:
     - At 2: \( \frac{2^3}{3} = \frac{8}{3} \).
     - At 0: \( \frac{0^3}{3} = 0 \).
   - Subtracting the lower bound from the upper bound: \( \frac{8}{3} - 0 = \frac{8}{3} \).
2. **Final Answer**:
   - The integral of \( x^2 \) from 0 to 2 is \( \boxed{\frac{8}{3}} \).