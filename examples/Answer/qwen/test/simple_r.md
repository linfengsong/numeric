<think>
Okay, so I need to find the integral of x squared from 0 to 2. Hmm, let me remember. Integrals are about finding the area under a curve, right? So in this case, the function is x², and I need to find the area under that curve between x = 0 and x = 2. 

First, I think I need to recall the basic rules of integration. I remember that the integral of x^n dx is (x^(n+1))/(n+1) + C, where C is the constant of integration. But since this is a definite integral from 0 to 2, I don't need the constant, right? So maybe I can just apply that formula here.

Let me write that down. The integral of x² dx from 0 to 2 would be [x³/3] evaluated from 0 to 2. Wait, let me check that. If n is 2, then adding 1 gives 3, so yes, it's x cubed over 3. 

So then, I need to plug in the upper limit, which is 2, and subtract the value at the lower limit, which is 0. Let me compute that. 

First, plugging in 2: (2)³ / 3 = 8 / 3. Then plugging in 0: (0)³ / 3 = 0 / 3 = 0. So subtracting, it's 8/3 - 0 = 8/3. 

Wait, is that all? That seems straightforward. But let me make sure I didn't skip any steps or make any mistakes. Maybe I should verify using another method, like Riemann sums? Although that might be more complicated. Or maybe I can recall that the integral of x² is indeed x³/3. 

Alternatively, I can think about the antiderivative. The antiderivative of x² is definitely x³/3, right? Because when you take the derivative of x³/3, you get 3x²/3 = x². Yep, that checks out. 

So then, evaluating from 0 to 2, it's just the difference between the antiderivative at 2 and at 0. Which is 8/3 - 0 = 8/3. 

But maybe I should check with a different approach. Let's say I use the definition of the integral as the limit of Riemann sums. Although that might take longer. Let me try to recall. 

The integral from a to b of f(x) dx is the limit as n approaches infinity of the sum from i=1 to n of f(x_i) * Δx, where Δx = (b - a)/n and x_i = a + iΔx. 

So here, a = 0, b = 2, so Δx = (2 - 0)/n = 2/n. Then x_i = 0 + i*(2/n) = 2i/n. 

So the Riemann sum would be the sum from i=1 to n of [ (2i/n)² ] * (2/n). Let's compute that. 

First, expand (2i/n)²: that's 4i²/n². Multiply by 2/n: 4i²/n² * 2/n = 8i² / n³. 

So the sum becomes 8/n³ * sum from i=1 to n of i². 

I remember that the formula for the sum of squares from 1 to n is n(n + 1)(2n + 1)/6. So substituting that in, we get:

8/n³ * [n(n + 1)(2n + 1)/6] = 8/6 * [ (n + 1)(2n + 1)/n² ].

Simplify 8/6 to 4/3. So 4/3 * [ (n + 1)(2n + 1)/n² ].

Now, let's expand (n + 1)(2n + 1):

Multiply out: n*(2n + 1) + 1*(2n + 1) = 2n² + n + 2n + 1 = 2n² + 3n + 1.

So the expression becomes 4/3 * (2n² + 3n + 1)/n².

Divide each term in the numerator by n²:

4/3 * [2 + 3/n + 1/n²].

Now take the limit as n approaches infinity. As n becomes very large, 3/n and 1/n² approach 0. So the limit is 4/3 * (2 + 0 + 0) = 4/3 * 2 = 8/3. 

So that's the same result as before! So that confirms that the integral is indeed 8/3. 

Therefore, I think my initial calculation was correct. The integral of x² from 0 to 2 is 8/3. 

But just to be thorough, maybe I can check with a numerical approximation. Let's take a simple case with a large n, say n = 2. Wait, but n=2 is too small. Let me try n=2. 

Wait, but with n=2, the Riemann sum would be two rectangles. Let's see:

Δx = 2/2 = 1. So x_1 = 1, x_2 = 2. The Riemann sum would be f(1)*1 + f(2)*1 = (1)^2*1 + (2)^2*1 = 1 + 4 = 5. But the actual integral is 8/3 ≈ 2.666..., so 5 is way off. But with n=2, it's just a rough approximation. 

If I take n=4, Δx = 0.5. The points are 0.5, 1.0, 1.5, 2.0. Using the right endpoints:

f(0.5)*0.5 + f(1.0)*0.5 + f(1.5)*0.5 + f(2.0)*0.5.

Calculating each term:

f(0.5) = 0.25, times 0.5 is 0.125

f(1.0) = 1, times 0.5 is 0.5

f(1.5) = 2.25, times 0.5 is 1.125

f(2.0) = 4, times 0.5 is 2.0

Adding them up: 0.125 + 0.5 = 0.625; 0.625 + 1.125 = 1.75; 1.75 + 2.0 = 3.75. 

So with n=4, the Riemann sum is 3.75, which is still higher than 8/3 ≈ 2.666... But as n increases, it should approach that value. Let's try n=100. But doing that manually would be tedious. However, since we already did the limit and got 8/3, and the antiderivative method also gave 8/3, I think that's solid. 

Alternatively, I can recall that the integral of x² from 0 to 2 is a standard problem. For example, if I remember that the integral of x² from 0 to 1 is 1/3, then from 0 to 2, it's 8/3, since 2 is twice 1, and the integral scales with the cube. Wait, actually, that might not be a general rule, but in this case, since it's a power function, maybe?

Wait, more accurately, if you have the integral from 0 to a of x² dx, it's a³/3. So if a=2, then 8/3. If a=1, then 1/3. So that seems correct. 

Alternatively, if I think of the graph of x², it's a parabola. The area under it from 0 to 2 is a region that's symmetric in some way? Not sure. But the calculation seems consistent. 

Another way: maybe use substitution or another method? Let me think. If I didn't remember the formula for the integral of x², maybe I could derive it. 

Let me try to derive the integral of x². Suppose I want to find ∫x² dx. Let me use the definition of the integral as the limit of Riemann sums, but I already did that. Alternatively, use integration by parts? Although that might be overkill. 

Integration by parts formula is ∫u dv = uv - ∫v du. Let me try setting u = x, dv = x dx. Then du = dx, and v = x²/2. Wait, then ∫x² dx = uv - ∫v du = x*(x²/2) - ∫(x²/2) dx = x³/2 - (1/2)∫x² dx. 

Hmm, so ∫x² dx = x³/2 - (1/2)∫x² dx. Then, bringing the (1/2)∫x² dx to the left side: ∫x² dx + (1/2)∫x² dx = x³/2. So (3/2)∫x² dx = x³/2. Therefore, ∫x² dx = (x³/2) / (3/2) = x³/3. 

So that confirms the antiderivative again. Therefore, the integral is indeed x³/3. 

Therefore, evaluating from 0 to 2, we get 8/3 - 0 = 8/3. 

I think that's thorough enough. All methods point to the same answer. So I can be confident that the integral of x² from 0 to 2 is 8/3.

**Final Answer**
The integral of $x^2$ from 0 to 2 is \boxed{\dfrac{8}{3}}.
</think>

To evaluate the definite integral of $ x^2 $ from 0 to 2, we begin by recalling the fundamental rule of integration for powers of $ x $:

$$
\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad \text{for } n \neq -1
$$

In this case, $ n = 2 $, so the antiderivative of $ x^2 $ is:

$$
\int x^2 \, dx = \frac{x^3}{3} + C
$$

Since we are evaluating a **definite integral** from 0 to 2, we use the Fundamental Theorem of Calculus:

$$
\int_0^2 x^2 \, dx = \left. \frac{x^3}{3} \right|_0^2 = \frac{2^3}{3} - \frac{0^3}{3} = \frac{8}{3} - 0 = \frac{8}{3}
$$

---

**Verification via Riemann Sums (Optional but Confirmatory):**

We can also verify this result by computing the Riemann sum for the function $ f(x) = x^2 $ over the interval [0, 2]. Using the definition:

$$
\int_0^2 x^2 \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i) \Delta x
$$

where $ \Delta x = \frac{2 - 0}{n} = \frac{2}{n} $ and $ x_i = \frac{2i}{n} $.

The sum becomes:

$$
\sum_{i=1}^n \left( \frac{2i}{n} \right)^2 \cdot \frac{2}{n} = \sum_{i=1}^n \frac{8i^2}{n^3}
$$

Using the formula for the sum of squares:

$$
\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}
$$

Substituting into the expression:

$$
\frac{8}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{8}{6} \cdot \frac{(n+1)(2n+1)}{n^2}
$$

As $ n \to \infty $, the expression simplifies to:

$$
\frac{4}{3} \cdot \left( 2 + \frac{3}{n} + \frac{1}{n^2} \right) \to \frac{4}{3} \cdot 2 = \frac{8}{3}
$$

This confirms the result from the antiderivative method.

---

**Conclusion:**

The integral of $ x^2 $ from 0 to 2 is:

$$
\boxed{\dfrac{8}{3}}
$$