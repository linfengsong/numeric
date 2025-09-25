<think>
Okay, so I need to prove that cos(π/7) - cos(2π/7) + cos(3π/7) equals 1/2. Hmm, trigonometric identities... Maybe I can use some known formulas or properties of cosine functions. Let me think.

First, I recall that sometimes sums of cosines can be simplified using complex numbers or roots of unity. Since π/7 is involved, maybe there's something with the 7th roots of unity? Let me try to recall. The roots of the equation z^7 = 1 are e^(2πik/7) for k from 0 to 6. But how does that relate to cosines?

Alternatively, maybe I can use some trigonometric identities. Let me write down the expression again:

cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2.

I wonder if there's a way to combine these terms. Let me check if there are known values for these cosines. For example, cos(π/7) is approximately 0.90097, cos(2π/7) ≈ 0.62349, and cos(3π/7) ≈ 0.2225. Let me compute the left-hand side numerically:

0.90097 - 0.62349 + 0.2225 ≈ 0.90097 - 0.62349 = 0.27748 + 0.2225 ≈ 0.49998, which is approximately 0.5. So that checks out numerically. But I need an analytical proof.

Another idea: Maybe using multiple-angle formulas or product-to-sum formulas? Let me try to manipulate the expression.

Alternatively, consider that 3π/7 is π - 4π/7, so cos(3π/7) = cos(π - 4π/7) = -cos(4π/7). Similarly, cos(2π/7) is just cos(2π/7), and cos(π/7) is cos(π/7). So maybe rewrite the expression as:

cos(π/7) - cos(2π/7) - cos(4π/7). Wait, but the original expression is cos(π/7) - cos(2π/7) + cos(3π/7), which is cos(π/7) - cos(2π/7) - cos(4π/7). So maybe this is helpful?

So, the expression becomes cos(π/7) - cos(2π/7) - cos(4π/7). Let me denote this as S = cos(π/7) - cos(2π/7) - cos(4π/7). I need to show that S = 1/2.

Hmm, perhaps there's a way to relate these terms. Let me think about summing them up or using some identity. Alternatively, consider using complex exponentials.

Let me recall that for roots of unity, the sum of all 7th roots of unity is zero. The 7th roots of unity are 1, e^(2πi/7), e^(4πi/7), e^(6πi/7), e^(8πi/7), e^(10πi/7), e^(12πi/7). The sum is zero. So, 1 + e^(2πi/7) + e^(4πi/7) + e^(6πi/7) + e^(8πi/7) + e^(10πi/7) + e^(12πi/7) = 0.

If I take the real parts of both sides, since the imaginary parts would cancel out. The real part of each term is cos(2πk/7) for k from 0 to 6. So:

1 + 2[cos(2π/7) + cos(4π/7) + cos(6π/7)] = 0.

Wait, because cos(2π/7), cos(4π/7), cos(6π/7), cos(8π/7)=cos(2π - 6π/7)=cos(6π/7), cos(10π/7)=cos(2π - 4π/7)=cos(4π/7), cos(12π/7)=cos(2π - 2π/7)=cos(2π/7). So indeed, the sum becomes 1 + 2[cos(2π/7) + cos(4π/7) + cos(6π/7)] = 0. Therefore:

cos(2π/7) + cos(4π/7) + cos(6π/7) = -1/2.

But note that cos(6π/7) = cos(π - π/7) = -cos(π/7). Similarly, cos(4π/7) = cos(π - 3π/7) = -cos(3π/7). So substituting:

cos(2π/7) - cos(3π/7) - cos(π/7) = -1/2.

Rearranging terms:

- [cos(π/7) - cos(2π/7) + cos(3π/7)] = -1/2.

Multiply both sides by -1:

cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2.

Wait, that's exactly the expression we need to prove! So that's the proof? Let me check again.

Starting from the sum of the real parts of the roots of unity:

1 + 2[cos(2π/7) + cos(4π/7) + cos(6π/7)] = 0.

Then, simplifying cos(6π/7) = -cos(π/7), cos(4π/7) = -cos(3π/7), so:

1 + 2[cos(2π/7) - cos(3π/7) - cos(π/7)] = 0.

Therefore:

2[cos(2π/7) - cos(3π/7) - cos(π/7)] = -1.

Divide both sides by 2:

cos(2π/7) - cos(3π/7) - cos(π/7) = -1/2.

Multiply both sides by -1:

cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2.

Yes! That's exactly the expression we wanted to prove. So the key was to use the roots of unity and take real parts. That seems to work. But let me make sure I didn't skip any steps or make any miscalculations.

Let me verify the step where I converted the sum of cos(2πk/7) for k=0 to 6. The roots of unity sum to zero, so their real parts sum to zero. The real parts are 1 + 2[cos(2π/7) + cos(4π/7) + cos(6π/7)] because the terms for k=1,2,3 and k=4,5,6 are conjugates. So yes, that gives 1 + 2[cos(2π/7) + cos(4π/7) + cos(6π/7)] = 0. Then, substituting cos(6π/7) = -cos(π/7) and cos(4π/7) = -cos(3π/7), so that gives 1 + 2[cos(2π/7) - cos(3π/7) - cos(π/7)] = 0. Then solving for the expression gives the desired result.

Alternatively, if I didn't remember the roots of unity approach, maybe there's another way. For example, using trigonometric identities. Let me try that as a check.

Let me denote the expression as S = cos(π/7) - cos(2π/7) + cos(3π/7). Maybe I can square both sides or use some product formulas. Alternatively, consider writing S as the real part of some complex exponential.

Alternatively, consider using multiple-angle identities. For example, since π/7 is involved, maybe using the identity for cos(7θ) = 0 when θ = π/7, but that might get complicated.

Alternatively, consider that 7θ = π, so θ = π/7. Let me recall that cos(7θ) can be expanded using multiple-angle formulas. Let me try that.

Let me recall that cos(7θ) can be expressed as 64cos^7θ - 112cos^5θ + 56cos^3θ - 7cosθ. But since θ = π/7, then cos(7θ) = cos(π) = -1. Therefore:

64cos^7(π/7) - 112cos^5(π/7) + 56cos^3(π/7) - 7cos(π/7) = -1.

But this seems complicated. Maybe not the best approach. However, perhaps if I consider equations involving cos(π/7), cos(2π/7), etc. Maybe there's a system of equations?

Alternatively, let me consider that the minimal polynomial for cos(2π/7) is known. But I might not remember it. Alternatively, maybe using some identities.

Alternatively, consider that the original expression S is equal to 1/2. Let me try to compute S + something or relate it to other expressions.

Wait, but since the roots of unity approach worked, and I verified the steps, maybe that's sufficient. But just to be thorough, let me check again.

Starting with the sum of the real parts:

Sum_{k=0}^6 e^(2πik/7) = 0.

Taking real parts:

Sum_{k=0}^6 cos(2πk/7) = 0.

Which is 1 + cos(2π/7) + cos(4π/7) + cos(6π/7) + cos(8π/7) + cos(10π/7) + cos(12π/7) = 0.

But cos(8π/7) = cos(π + π/7) = -cos(π/7).

Similarly, cos(10π/7) = cos(π + 3π/7) = -cos(3π/7).

cos(12π/7) = cos(2π - 2π/7) = cos(2π/7).

Wait, cos(12π/7) is cos(2π - 2π/7) = cos(2π/7). Similarly, cos(6π/7) = cos(π - π/7) = -cos(π/7).

Similarly, cos(4π/7) = cos(π - 3π/7) = -cos(3π/7).

Therefore, substituting:

1 + cos(2π/7) + (-cos(π/7)) + (-cos(3π/7)) + (-cos(π/7)) + (-cos(3π/7)) + cos(2π/7) = 0.

Let me write that out:

1 + [cos(2π/7) + cos(2π/7)] + [-cos(π/7) - cos(π/7)] + [-cos(3π/7) - cos(3π/7)] = 0.

Which is:

1 + 2cos(2π/7) - 2cos(π/7) - 2cos(3π/7) = 0.

Rearranged:

2cos(2π/7) - 2cos(π/7) - 2cos(3π/7) = -1.

Divide both sides by 2:

cos(2π/7) - cos(π/7) - cos(3π/7) = -1/2.

Multiply both sides by -1:

cos(π/7) + cos(3π/7) - cos(2π/7) = 1/2.

But the original expression is cos(π/7) - cos(2π/7) + cos(3π/7), which is the same as the left-hand side. Therefore, indeed, S = 1/2. So that's the proof.

Therefore, the key idea was to use the fact that the sum of the real parts of the 7th roots of unity is zero, and then express those cosines in terms of cos(π/7), cos(2π/7), etc., leading to the desired equation. That seems solid.

Alternatively, if I didn't think of roots of unity, maybe another approach. Let me think.

Suppose I consider the identity for cos A + cos B + cos C... but I don't know. Alternatively, consider writing cos(π/7) + cos(3π/7) + cos(5π/7) = 1/2. Wait, that's another known identity. Wait, but here we have cos(π/7) - cos(2π/7) + cos(3π/7). Maybe there's a relation between these?

Alternatively, note that cos(5π/7) = cos(π - 2π/7) = -cos(2π/7). So cos(π/7) + cos(3π/7) + cos(5π/7) = cos(π/7) + cos(3π/7) - cos(2π/7) = same as our expression S. Therefore, S = 1/2. So that's another way to state it. Therefore, if I can prove that cos(π/7) + cos(3π/7) + cos(5π/7) = 1/2, then we are done.

But how to prove that?

Alternatively, maybe use the formula for sum of cosines in an arithmetic progression? The formula is:

Sum_{k=0}^{n-1} cos(a + kd) = [sin(n*d/2)/sin(d/2)] * cos(a + (n-1)d/2).

But here, the angles are π/7, 3π/7, 5π/7. So they are in arithmetic progression with difference 2π/7, starting from π/7, with n=3 terms. Let me check:

Sum = cos(π/7) + cos(3π/7) + cos(5π/7).

Using the formula:

n=3, a=π/7, d=2π/7.

Sum = [sin(3*(2π/7)/2)/sin(2π/7/2)] * cos(a + (n-1)d/2)

Compute:

Numerator: sin(3π/7)

Denominator: sin(π/7)

Multiply by cos(a + (n-1)d/2) = cos(π/7 + (2)(2π/7)/2) = cos(π/7 + 2π/7) = cos(3π/7).

Therefore, Sum = [sin(3π/7)/sin(π/7)] * cos(3π/7).

So Sum = [sin(3π/7)cos(3π/7)] / sin(π/7).

Note that sin(3π/7)cos(3π/7) = (1/2) sin(6π/7) = (1/2) sin(π - π/7) = (1/2) sin(π/7).

Therefore, Sum = [ (1/2) sin(π/7) ] / sin(π/7) ) = 1/2. Therefore, Sum = 1/2. Hence, cos(π/7) + cos(3π/7) + cos(5π/7) = 1/2. But since cos(5π/7) = -cos(2π/7), this is equal to cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2. Which is exactly our original expression. Therefore, this is another proof using the formula for the sum of cosines in arithmetic progression.

So that's another way to see it. So whether using roots of unity or using the sum formula, we get the result. Therefore, the identity holds.

Therefore, the answer is 1/2. So the proof is done.

But just to recap, since the problem was to prove that cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2, and through two different methods (roots of unity and sum of arithmetic progression) we arrived at that conclusion. Therefore, the identity is correct.

I think that's thorough enough. I don't see any mistakes in the reasoning, and both methods confirm the result. So I can be confident that the proof is correct.

**Final Answer**
\boxed{\dfrac{1}{2}}
</think>

To prove that:

$$
\cos\left(\frac{\pi}{7}\right) - \cos\left(\frac{2\pi}{7}\right) + \cos\left(\frac{3\pi}{7}\right) = \frac{1}{2}
$$

we can utilize the **roots of unity** and **trigonometric identities**.

---

### Step 1: Use the Roots of Unity

Consider the 7th roots of unity, which are the complex numbers:

$$
z_k = e^{2\pi i k / 7}, \quad \text{for } k = 0, 1, 2, \dots, 6
$$

These satisfy the equation:

$$
z^7 = 1
$$

The sum of all 7th roots of unity is:

$$
\sum_{k=0}^{6} z_k = 0
$$

Taking the real parts of both sides gives:

$$
\sum_{k=0}^{6} \cos\left(\frac{2\pi k}{7}\right) = 0
$$

This simplifies to:

$$
1 + \cos\left(\frac{2\pi}{7}\right) + \cos\left(\frac{4\pi}{7}\right) + \cos\left(\frac{6\pi}{7}\right) + \cos\left(\frac{8\pi}{7}\right) + \cos\left(\frac{10\pi}{7