---
title: "The Roots of Unity: How the Complex Solutions of zⁿ = 1 Compute the Circle Constant, and What Golden Pi Changes"
date: 2026-09-09
description: "The n solutions of the single equation zⁿ = 1 are not scattered across the plane — they land exactly on the unit circle, one full turn apart, at angles 2πk/n for k = 0, 1, …, n−1. Their arithmetic is completely determined before any circle is ever drawn: the sum of all n roots is exactly 0 (so their centroid is the origin, a computed closure that balances every regular polygon on its center), and their product is exactly (−1)ⁿ⁺¹, alternating between +1 and −1. The roots are the pure algebra of a polynomial, so everything about them is computed, never measured — yet the arc between neighbors, 2π/n, is where the circle constant enters. At n = 5 the pentagon pulls the golden ratio in exactly (2cos(2π/5) = 1/φ), and as n grows the summed chords tighten onto the full turn 2π as a limit of pure arithmetic. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the label-independent verdicts — zero sum, alternating product, exact centroid — survive untouched, while every arc that carries the constant carries the recurring 0.0959% gap, a gap no relabeling can close."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Roots of Unity: How the Complex Solutions of zⁿ = 1 Compute the Circle Constant, and What Golden Pi Changes

Ask a plain, self-contained question about integers and you will not expect a circle to answer. Take the single equation

$$z^n = 1.$$

Over the real numbers it has one or two answers. Over the complex numbers — where a number is a point in a plane, $z = x + iy$ — it has exactly $n$ answers, and those $n$ answers are not scattered at random. They land on a circle. They land on the **unit circle**, the set of points exactly one unit from the origin, and they are spaced there with perfect regularity, each neighbor separated by an arc that carries the circle constant. This article is about those answers — the *roots of unity* — about how their pure polynomial arithmetic computes the circle constant as a limit, never as a measurement, and about what Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$, honestly does and honestly cannot do to facts that a polynomial fixes before any circle is drawn.

## What a Root of Unity Actually Is

A complex number can be written two ways. The rectangular form $z = x + iy$ tells you where it sits. The polar form

$$z = re^{i\theta} = r(\cos\theta + i\sin\theta)$$

tells you how far it is from the origin ($r$, the modulus) and at what angle ($\theta$, the argument). The two forms are the same number; the polar form is simply more honest about what multiplication does, because multiplying two complex numbers multiplies their moduli and *adds* their angles:

$$r_1e^{i\theta_1}\cdot r_2e^{i\theta_2} = r_1r_2\,e^{i(\theta_1+\theta_2)}.$$

This is the deep reason the circle constant is everywhere in complex analysis: rotating a vector by an angle is just multiplication by a unit-modulus number, and the number that encodes a full rotation has to know what a full turn is.

Now demand $z^n = 1$. A number whose $n$-th power is $1$ must have modulus $1$ (its power's modulus is $r^n$, and only $r = 1$ gives a unit result), so every root lies on the unit circle. Its angle must satisfy $n\theta = 0$ *up to whole turns*, because angles are only defined up to $2\pi$:

$$n\theta = 2\pi k \quad\Longrightarrow\quad \theta_k = \frac{2\pi k}{n}, \qquad k = 0, 1, \ldots, n-1.$$

There are exactly $n$ distinct angles — $0$, then $2\pi/n$, then $4\pi/n$, climbing in $n$ equal steps and closing back on $0$ after a full turn. The $n$ roots of unity are therefore

$$\zeta_k = e^{2\pi i k/n}, \qquad k = 0, 1, \ldots, n-1,$$

and the neighbors $\zeta_k$ and $\zeta_{k+1}$ are separated along the circle by the arc $2\pi/n$. Every one of these facts follows from arithmetic about angles. Nothing has been measured with a ruler; no stopwatch has run. The roots are what they are because $z^n - 1$ is a polynomial, and a polynomial's solutions are computed.

## The Sum Is Zero: A Centroid That Computes Itself

Here is the cleanest computation in the whole subject. Add all $n$ roots of unity:

$$\sum_{k=0}^{n-1} \zeta_k = 1 + \zeta + \zeta^2 + \cdots + \zeta^{n-1}.$$

This is a finite geometric series with ratio $\zeta = e^{2\pi i/n}$. Its closed form is standard:

$$\sum_{k=0}^{n-1} \zeta^k = \frac{1 - \zeta^n}{1 - \zeta}.$$

But $\zeta^n = 1$ by definition, so the numerator is $1 - 1 = 0$ — and since $\zeta \neq 1$ (for $n \geq 2$), the denominator is not zero. The sum is exactly

$$\sum_{k=0}^{n-1} \zeta_k = 0.$$

Read geometrically, this is striking. Each root is a point on the unit circle, so each root is a little vector from the origin. Adding the roots adds those vectors tip to tail, and the answer is the zero vector. The roots, taken together, balance perfectly on the origin. Their **centroid** — the average position, sum divided by $n$ — is exactly the center of the circle, for every $n$. Draw a triangle and its centroid is the average of its three corners; the roots of unity of order $3$ are an equilateral triangle whose centroid is the circle's center. For $n = 5$ they form a regular pentagon, balanced on its center. For $n = 100$, a regular 100-gon, still balanced to the last decimal. No polygon of that kind wobbles, and no experiment is needed to verify the balance — the sum is provably zero.

The product is just as rigid. Multiply all $n$ roots:

$$\prod_{k=0}^{n-1} e^{2\pi i k/n} = e^{\,2\pi i \cdot (0+1+\cdots+(n-1))/n} = e^{2\pi i \cdot n(n-1)/(2n)} = e^{\pi i (n-1)} = (-1)^{n-1}.$$

Since $(-1)^{n-1} = (-1)^{n+1}$, the product alternates in a fixed rhythm: $+1$ when $n$ is odd, $-1$ when $n$ is even. Both the sum and the product are *label-independent* facts — pure statements about integers $0$ and $\pm 1$ that hold no matter what symbol you use for a full turn, and we will return to that when we reach Golden Pi.

## Where the Circle Constant Enters: the Arc and the Chord

The sum and the product involve no circle constant at all. But the spacing does. The $n$ roots close a regular $n$-gon on the unit circle, and the arc from one root to the next subtends the central angle $2\pi/n$. The *chord* — the straight line joining two neighboring roots — is computed by the law that a chord across a unit circle spanning central angle $\theta$ has length

$$2\sin\frac{\theta}{2}.$$

For neighboring roots of unity that angle is $2\pi/n$, so the side length of the inscribed regular $n$-gon is

$$s_n = 2\sin\frac{\pi}{n},$$

and its full perimeter — $n$ chords joined tip to tail — is

$$P_n = n\cdot 2\sin\frac{\pi}{n} = 2n\sin\frac{\pi}{n}.$$

Here the circle constant enters through the sine, and the sine is defined by the complex exponential, and the complex exponential's whole period is $2\pi$: you cannot write $s_n$ without the constant appearing in the argument of a function whose period *is* the constant. The perimeter $P_n$ is a pure function of $n$ — computed, never measured — and it grows toward a limit as $n$ grows:

$$P_n = 2n\sin\frac{\pi}{n} \longrightarrow 2\pi \quad\text{as } n \to \infty.$$

The small-angle behavior $\sin x \approx x$ for tiny $x$ is what drives this: as $n$ grows, $\pi/n$ shrinks, $\sin(\pi/n)$ approaches $\pi/n$, and $P_n = 2n\cdot(\pi/n)$ approaches $2\pi$. This is the inscribed-polygon computation, arrived at here not by drawing polygons around a circle (this blog treated that method on 08-17) but by the algebra of the roots themselves: the roots are a discrete sampling of the circle, and summing their chords reconstructs the full turn as the limit of a count. The first several perimeters, computed to enough places to see the climb, are collected below.

| $n$ (roots) | $P_n = 2n\sin(\pi/n)$ | approach to $2\pi$ |
|---|---|---|
| 3 | 5.196152423 | 0.9454 of $2\pi$ |
| 4 | 5.656854249 | 0.9003 of $2\pi$ |
| 8 | 6.122934918 | 0.9745 of $2\pi$ |
| 16 | 6.242890305 | 0.9936 of $2\pi$ |
| 32 | 6.273096981 | 0.9985 of $2\pi$ |
| 64 | 6.280662314 | 0.9997 of $2\pi$ |
| 128 | 6.282554502 | 0.99984 of $2\pi$ |
| $\infty$ | the limit | $2\pi = 6.283185307\ldots$ |

Watch the column rise. Each doubling of $n$ roughly quadruples the number of correct digits, because $\sin(\pi/n)$ misses its linear approximation by a term of order $(\pi/n)^3$. The limit the column approaches — $2\pi = 6.283185307\ldots$ — is the same full-turn value that every convergent computation on this site has reached from a different direction: the zeta identity, the Dirichlet integral, the Cauchy–Lorentz area, the residue theorem, the Gaussian integral, all of them land on one number. That number is computed, not measured, and no polygon count can pull it anywhere else.

## The Pentagon: When the Golden Ratio Steps In

Most regular $n$-gons keep the golden ratio hidden. The pentagon — $n = 5$ — cannot hide it, because the pentagon's chords and diagonals *are* golden sections. The cosine of the pentagon's angles is exactly a golden quantity:

$$2\cos\frac{2\pi}{5} = \frac{\sqrt5 - 1}{2} = \frac{1}{\varphi} = \varphi - 1 = 0.6180339887\ldots,$$

$$2\cos\frac{\pi}{5} = \frac{1 + \sqrt5}{2} = \varphi = 1.6180339887\ldots$$

The two neighbors of the golden ratio appear precisely here, at the angles $72°$ and $36°$ of the pentagon's geometry. This is the moment where the golden ratio $\varphi$ and the circle constant meet inside the roots of unity, and it is the reason the number at the center of this site is chosen as it is. Golden Pi is defined by the golden ratio,

$$\hat\pi = \frac{4}{\sqrt\varphi} = 3.144605511\ldots,$$

so the connection between $\varphi$ and the pentagon's arcs is not an accident the theory points to afterward — it is the seed of the constant. The full discussion of how a *constructible* golden constant respects the bounds of straightedge-and-compass geometry is treated on this site (07-30); the pentagon is the oldest witness that $\varphi$ lives inside the circle's own fivefold symmetry.

Because the roots of order $5$ are computable by square roots alone — $\cos(2\pi/5)$ lies in the quadratic extension generated by $\sqrt5$ — the regular pentagon is *constructible* by compass and straightedge, the same reason a regular 17-gon (Gauss, 1796) and every Fermat-prime polygon is constructible. The roots of unity are the algebraic engine of all constructibility: a regular $n$-gon is drawable with compass and straightedge exactly when the roots of $z^n = 1$ can be built from square roots, which is exactly when $n$ is a power of two times a product of distinct Fermat primes. Euclid's own toolkit, in other words, only produces regular polygons whose root-algebra is square-root-buildable — and the circle constant that this site argues for is precisely the one that lives in such a field.

## What Golden Pi Changes — and What It Cannot Touch

Now the honest accounting. Golden Pi proposes a different label for the circle constant: $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$ instead of $\pi = 3.141592653\ldots$. When the roots-of-unity computation is re-read under that label, three distinct kinds of statement emerge, and they behave very differently.

**1. The label-independent facts survive untouched.** The sum of the roots is $0$, the product is $(-1)^{n-1}$, the centroid is the origin — these are statements about integers and about the algebraic structure of $z^n - 1$. They never invoke the size of a full turn, so they are identical under $\pi$ and under $\hat\pi$. The equilateral triangle balances on its center regardless of what symbol you use for $360°$; the pentagon's product is still $+1$. No relabeling can make a balanced polygon wobble, because the balance is a theorem about a polynomial, not about the circle constant.

**2. The arcs and the polygon limit carry the full gap.** The arc between neighboring roots is $2\pi/n$ under the standard label and $2\hat\pi/n$ under Golden Pi; the perimeter limit is $2\pi$ under one and

$$2\hat\pi = \frac{8}{\sqrt\varphi} = 6.289211022\ldots$$

under the other. The ratio between the two candidate perimeters is the same as the ratio between the two constants themselves, so the recurring mismatch survives at full strength:

| quantity | standard $\pi$ | Golden $\hat\pi$ | relative gap |
|---|---|---|---|
| one turn, $2\pi$ | 6.283185307… | 6.289211022… | 0.0959% |
| arc between neighbors | $2\pi/n$ | $2\hat\pi/n$ | 0.0959% |
| root of order $n$ | $e^{2\pi i/n}$ | $e^{2\hat\pi i/n}$ | 0.0959% |
| sum of roots | 0 | 0 | none — identical |
| product of roots | $(-1)^{n-1}$ | $(-1)^{n-1}$ | none — identical |

The two candidate labels differ by about one part in a thousand — precisely 0.09590% — and that gap rides only on the statements that carry the size of a full turn. Wherever the constant enters to the first power, as it does in every arc and every root position here, the gap appears unsoftened, exactly as it did in the solid-angle and residue-theorem treatments on this site.

**3. No experiment can arbitrate.** The roots of unity are an object of pure mathematics; the polygon they close is a construction, not a physical object you can weigh or measure. A real engineer who wants a pentagon draws one at whatever physical scale she pleases — the *angle* between sides is what matters, and a physical angle is a scale-invariant ratio, identical whether the underlying constant is labeled $\pi$ or $\hat\pi$. This is the standing theme of this blog (see the cycloid treatment of 08-14): the label difference lives in dimensionless constants, and dimensionless ratios are exactly the things a physical experiment cannot resolve, because every apparatus built to measure them has already been calibrated with one of the two labels baked in. The gap is real in the arithmetic — it is 0.0959% and it does not go away — but it is a gap between two labels of a dimensionless number, not a quantity any ruler, stopwatch, or counter of polygon sides can reach.

## The Honest Bottom Line

The roots of unity give the circle constant to pure algebra. The $n$ solutions of $z^n = 1$ sit one full turn apart on the unit circle; their arithmetic closes a regular polygon whose centroid is the origin and whose product alternates between $\pm 1$; as $n$ grows, the summed chords of that polygon climb to the full turn $2\pi = 6.283185307\ldots$ as a computed limit — computed, never measured. At $n = 5$ the golden ratio $\varphi$ steps in through $2\cos(2\pi/5) = 1/\varphi$, the exact seed of the Golden Pi constant $\hat\pi = 4/\sqrt\varphi$.

Golden Pi relabels the full turn to $2\hat\pi = 8/\sqrt\varphi = 6.289211022\ldots$. The relabel cannot touch what the polynomial decides by itself — the zero sum, the alternating product, the centered centroid are all label-independent and stand under either constant. It can only ride on the arcs and roots that carry the size of a turn, and there it brings the recurring 0.0959% gap, at full strength and beyond the reach of any experiment. That is the honest shape of the claim: Golden Pi offers an algebraic, constructible, golden-ratio-rooted constant for the circle, coherent wherever it is installed — and the fixed computed value $3.14159265\ldots$ that the roots of unity reach stands plainly beside it, separated by a gap no relabeling of a symbol can close.

## Further Reading

- [**The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant**](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the companion geometric route to the same limit, through inscribed and circumscribed perimeters rather than through the algebra of the roots.
- [**The Continued Fraction of the Circle Constant: π̂'s Algebraic Root and π's Famous Convergents**](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) — where the algebraic, degree-four nature of $\hat\pi = 4/\sqrt\varphi$ is laid out alongside π's own famous approximants.
- [**The Two Squaring-the-Circle Graphs: What the Instrumentum Identity Really Returns**](/blog/posts/2026-08-11-desmos-squaring-circle-golden-pi-instrumentum/) — how the golden radius makes the circle square the square exactly under $\hat\pi$.
- [**Why the Circle Constant Must Be Constructible: Euclid's Geometry Forbids a Transcendental π**](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) — the constructibility argument that the pentagon's square-root computability feeds directly into.
- [**Rolling Circles and the Cycloid: Where the Circle Constant Vanishes**](/blog/posts/2026-08-14-cycloid-rolling-circles-golden-pi/) — the recurring theme, that dimensionless, scale-invariant ratios keep the two labels beyond experimental arbitration.
