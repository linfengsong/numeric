<think>
Okay, I need to prove that cos(π/7) - cos(2π/7) + cos(3π/7) equals 1/2 using Lean 4. Let me think about how to approach this.

First, I remember that trigonometric identities can sometimes be tricky, especially with angles like π/7. Maybe there's a clever identity or a way to relate these terms. Alternatively, perhaps using complex numbers or roots of unity could help. Since the problem involves cosines of multiples of π/7, maybe considering the 7th roots of unity?

Let me recall that the sum of certain cosine terms can be related to the real parts of roots of unity. For example, the 7th roots of unity are solutions to z^7 = 1. These roots are e^(2πik/7) for k from 0 to 6. But the angles here are π/7, 2π/7, etc., which are half of the angles in the roots of unity. Hmm, maybe I need to consider some other equation.

Alternatively, I remember that there's a known identity for cos(π/7) - cos(3π/7) + cos(5π/7) = 1/2, but the problem here has different signs. Wait, maybe there's a similar identity. Let me check the exact expression again: cos(π/7) - cos(2π/7) + cos(3π/7). Let me compute the numerical value to see if it's indeed 1/2. Let me calculate each term approximately.

π is approximately 3.1416, so π/7 ≈ 0.4488 radians. cos(π/7) ≈ 0.90097. Then 2π/7 ≈ 0.8976 radians, cos(2π/7) ≈ 0.62349. Then 3π/7 ≈ 1.3464 radians, cos(3π/7) ≈ 0.2225. So the expression is 0.90097 - 0.62349 + 0.2225 ≈ 0.90097 - 0.62349 is 0.27748 + 0.2225 ≈ 0.49998, which is approximately 0.5. So yes, the numerical value checks out. So the problem is to prove that this sum equals 1/2.

Now, how to prove this in Lean? Let me think about possible approaches.

One method might be to use multiple-angle identities or to find a clever algebraic manipulation. Alternatively, using complex exponentials. Let me try the complex exponential approach.

Let me recall that cosθ = (e^(iθ) + e^(-iθ))/2. So maybe I can express each term as such and combine them. Let me try that.

Let me denote θ = π/7. Then the expression becomes cosθ - cos(2θ) + cos(3θ). Let me compute this:

cosθ - cos(2θ) + cos(3θ) = [ (e^(iθ) + e^(-iθ))/2 ] - [ (e^(i2θ) + e^(-i2θ))/2 ] + [ (e^(i3θ) + e^(-i3θ))/2 ].

Combining these terms, we have:

[ e^(iθ) + e^(-iθ) - e^(i2θ) - e^(-i2θ) + e^(i3θ) + e^(-i3θ) ] / 2.

Let me see if this sum can be simplified. Let me note that θ = π/7, so 3θ = 3π/7, and 7θ = π. So e^(i7θ) = e^(iπ) = -1. Also, e^(iθ) is a root of z^7 + 1 = 0? Wait, z^7 = e^(i7θ) = e^(iπ) = -1. So z^7 + 1 = 0. Therefore, the roots of z^7 + 1 = 0 are e^(i(π + 2πk)/7) for k=0,...,6. But maybe that's not directly helpful. Alternatively, perhaps considering the roots of z^7 - 1 = 0, which are the 7th roots of unity. But since θ = π/7, 7θ = π, so e^(i7θ) = e^(iπ) = -1, which is a root of z^2 - 1 = 0. Hmm, maybe I need to relate the sum to some equation.

Alternatively, perhaps I can consider the sum S = cosθ - cos(2θ) + cos(3θ). Let me try to compute S.

Alternatively, maybe using some trigonometric identities. Let me think about summing cosines with different arguments. For example, using sum-to-product formulas.

Alternatively, let me consider that 3θ = π - 4θ, since θ = π/7, so 3θ = 3π/7, and π - 4θ = π - 4π/7 = 3π/7. So cos(3θ) = cos(π - 4θ) = -cos(4θ). So substituting that into the expression:

cosθ - cos(2θ) + cos(3θ) = cosθ - cos(2θ) - cos(4θ).

Hmm, so the expression becomes cosθ - cos2θ - cos4θ. Maybe this is easier to handle. Let me see.

Alternatively, perhaps using the identity for cosA - cosB. Let me recall that cosA - cosB = -2 sin( (A+B)/2 ) sin( (A-B)/2 ). Let me try applying this to cosθ - cos2θ.

So cosθ - cos2θ = -2 sin( (θ + 2θ)/2 ) sin( (θ - 2θ)/2 ) = -2 sin(3θ/2) sin(-θ/2) = 2 sin(3θ/2) sin(θ/2). 

So then the expression becomes 2 sin(3θ/2) sin(θ/2) - cos4θ. Let me compute that. Hmm, not sure if this helps. Maybe I need another approach.

Alternatively, let me consider multiplying both sides by 2 sin(θ/2) to use some identities. Wait, perhaps there's a better way. Let me think about the sum S = cosθ - cos2θ + cos3θ. Let me write down all terms:

S = cos(π/7) - cos(2π/7) + cos(3π/7).

Alternatively, maybe consider adding and subtracting terms to form known identities. For example, I know that the sum of cos(kπ/7) for k=1 to 6 is -1, but that might not be directly helpful. Wait, let me recall that the sum of cos(2πk/n) for k=1 to n-1 is -1. But here, the angles are π/7, 2π/7, etc. Maybe not directly applicable.

Alternatively, perhaps using Chebyshev polynomials or some other method. But I'm not sure. Maybe I need to consider a system of equations.

Alternatively, let me consider the equation that the given expression equals 1/2 and try to square both sides or manipulate it algebraically. But that might get complicated.

Alternatively, let me think about using complex numbers. Let me consider the sum of the real parts of certain complex exponentials.

Let me denote z = e^(iπ/7). Then, since θ = π/7, we have z^7 = e^(iπ) = -1. So z^7 + 1 = 0. Therefore, z^7 = -1. So z^14 = 1, so z is a primitive 14th root of unity? Wait, z^7 = -1, so z^14 = 1. So z is a primitive 14th root of unity. Hmm, but maybe that's complicating things. Let me think.

Alternatively, since z^7 = -1, then z^k for k=0,...,6 would be e^(i(π + 2πk)/7) = e^(iπ(1 + 2k)/7). But maybe that's not helpful. Alternatively, perhaps considering the minimal polynomial of z.

But perhaps I can express the sum S in terms of z. Let me see:

S = Re(z) - Re(z^2) + Re(z^3). Since cos(kθ) is the real part of z^k. So S = Re(z) - Re(z^2) + Re(z^3) = Re(z - z^2 + z^3).

So if I can compute z - z^2 + z^3, then take its real part, and show that it equals 1/2.

But how can I compute this expression? Let me compute z - z^2 + z^3. Since z^7 = -1, perhaps I can find a relation for z^k.

Alternatively, since z^7 = -1, then z^7 + 1 = 0. Let me factor this equation. z^7 + 1 = (z + 1)(z^6 - z^5 + z^4 - z^3 + z^2 - z + 1) = 0. Since z ≠ -1 (because z = e^(iπ/7) ≠ -1), then z satisfies the equation z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0. Let me note that.

So, z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0. Let me rearrange this equation:

z^6 + z^4 + z^2 + 1 = z^5 + z^3 + z.

Hmm, not sure if that helps. Let me think about the expression z - z^2 + z^3. Let me denote this as A = z - z^2 + z^3. Maybe I can find a relation involving A.

Alternatively, let me compute A and then take its real part. But how?

Alternatively, maybe I can find the value of A by using the equation that z satisfies. Let me try to express higher powers of z in terms of lower ones.

Let me note that z^7 = -1. So z^7 = -1, z^8 = -z, z^9 = -z^2, etc. But I'm not sure if that helps directly.

Alternatively, let me compute A = z - z^2 + z^3. Let me multiply both sides by something. Maybe multiply by z^something to get a relation.

Alternatively, let me consider the sum A + something. For example, if I can find another expression involving z that relates to A. Alternatively, think of A as part of a larger sum.

Alternatively, let me compute the sum of all terms from z^k for certain k. For example, since z^7 = -1, then z^k = z^{k mod 7} * (-1)^{floor(k/7)}? Not sure.

Alternatively, maybe consider that the minimal polynomial of z is the 14th cyclotomic polynomial, but that might be too complex for me to handle right now.

Alternatively, perhaps consider that the given expression S is the real part of A = z - z^2 + z^3. Let me compute A and then take its real part. Let me compute A:

A = z - z^2 + z^3. Let me compute A + conjugate(A). Since the real part of A is (A + conjugate(A))/2. But since z is a complex number on the unit circle, its conjugate is 1/z. Because |z| = 1, so conjugate(z) = 1/z. Let me check that: z = e^(iπ/7), so conjugate(z) = e^(-iπ/7) = 1/z, since z * conjugate(z) = |z|^2 = 1. So yes.

So conjugate(A) = conjugate(z) - conjugate(z^2) + conjugate(z^3) = 1/z - 1/z^2 + 1/z^3.

Therefore, the real part of A is (A + conjugate(A))/2 = [z - z^2 + z^3 + 1/z - 1/z^2 + 1/z^3]/2.

Let me compute this expression. Let me denote this as [z + 1/z - z^2 - 1/z^2 + z^3 + 1/z^3]/2.

But z + 1/z = 2 cosθ, where θ = π/7. Similarly for other terms. So:

z + 1/z = 2 cosθ = 2 cos(π/7).

Similarly, z^2 + 1/z^2 = 2 cos(2θ) = 2 cos(2π/7).

Similarly, z^3 + 1/z^3 = 2 cos(3θ) = 2 cos(3π/7).

So substituting into the expression:

[2 cosθ - 2 cos2θ + 2 cos3θ]/2 = cosθ - cos2θ + cos3θ = S.

Wait, but that brings us back to S. So this approach seems circular. Hmm.

But perhaps I can find another relation. Let me think. Since z^7 = -1, then z^7 + 1 = 0. Let me compute A * z^k for some k to find a relation. Alternatively, perhaps express A in terms of the equation z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0.

Let me recall that z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0. Let me rearrange this:

z^6 + z^4 + z^2 + 1 = z^5 + z^3 + z.

Hmm. Let me see if I can express A in terms of this. Let me note that A = z - z^2 + z^3. Let me see if I can relate this to the equation. Let me consider multiplying both sides of the equation by something.

Alternatively, let me compute z^3 - z^2 + z. Let me think of that as A. Let me see if I can find an expression involving A.

Alternatively, maybe consider the sum of A and other similar terms. For example, if I consider other combinations of z^k terms.

Alternatively, let me think about the minimal polynomial of cos(π/7), but that might be complicated.

Alternatively, perhaps consider squaring the expression S. Let me try that. Let me denote S = cosθ - cos2θ + cos3θ, where θ = π/7. Then S = 1/2. Let me square both sides:

S^2 = 1/4.

Expanding the left side:

(cosθ - cos2θ + cos3θ)^2 = cos²θ + cos²2θ + cos²3θ - 2cosθ cos2θ + 2cosθ cos3θ - 2cos2θ cos3θ.

But this seems messy. Maybe there's a better way. Alternatively, perhaps use known values of cosines. But I don't know them off the top of my head.

Alternatively, perhaps consider using the identity for the sum of cosines. Let me think of another approach.

Wait, I remember that there's a known identity for this particular sum. Let me try to recall or derive it. For example, in some trigonometric identities, sums involving cosines of angles that are multiples of π/n can be evaluated using roots of equations. 

Let me consider the equation for the 7th roots of unity. The roots of z^7 - 1 = 0 are e^(2πik/7) for k=0,...,6. However, our angles are π/7, 2π/7, etc., which are half of those angles. So maybe considering the equation for z^14 - 1 = 0, which would have roots e^(πik/7) for k=0,...,13. But I'm not sure.

Alternatively, consider that the minimal polynomial for cos(π/7) is known. Let me recall that cos(π/7) is a root of the equation 8x^3 - 4x^2 - 4x + 1 = 0. But how does that help here?

Alternatively, perhaps I can set up an equation involving S and use the minimal polynomial. But this might be complicated.

Alternatively, let me consider the following approach: Let me denote S = cos(π/7) - cos(2π/7) + cos(3π/7). Let me also compute another similar expression, maybe involving sin terms, and combine them. For example, using the identity that relates sums of cosines and sines.

Alternatively, consider multiplying S by 2 sin(π/7) or some other sine term to use product-to-sum formulas. Let me try that.

Let me multiply S by 2 sin(π/7):

2 sin(π/7) * S = 2 sin(π/7) [cos(π/7) - cos(2π/7) + cos(3π/7)].

Let me compute each term separately.

First term: 2 sin(π/7) cos(π/7) = sin(2π/7) (using the identity 2 sin a cos a = sin 2a).

Second term: -2 sin(π/7) cos(2π/7) = - [sin(3π/7) - sin(π/7)] using the identity 2 sin a cos b = sin(a + b) + sin(a - b). Wait, the identity is 2 sin a cos b = sin(a + b) + sin(a - b). So here, -2 sin a cos b = -sin(a + b) - sin(a - b). Let me check:

Let me compute 2 sin a cos b = sin(a + b) + sin(a - b). So if I have -2 sin a cos b = -sin(a + b) - sin(a - b).

So for the second term, a = π/7, b = 2π/7. Then:

-2 sin(π/7) cos(2π/7) = - [ sin(π/7 + 2π/7) + sin(π/7