---
title: "The Ellipse's Perimeter: How the Complete Elliptic Integral of the Second Kind Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-09-12
description: "The ellipse is the one classical curve whose perimeter has no elementary closed form: its length is L = 4a·E(e), where E is the complete elliptic integral of the second kind, an integral whose upper limit is a quarter turn. That quarter turn is where the circle constant enters — computed, never measured — and the value of the integral is the length of a genuine physical arc. For a golden ellipse with semi-axes a and a/√φ, the eccentricity is exactly 1/φ and the full minor axis is exactly π̂/2 = 2/√φ = 1.5723028. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the perimeter relabels to 2π̂a·(1 − S)/AGM(1, k′) with the recurring 0.0959022% gap riding on the prefactor, while a second, equally defensible placement of the constant — relabel the quarter turn inside the integral — shifts the perimeter by only 0.0841186%. The two placements disagree, which is precisely why no ruler settles the matter: Legendre's relation E K′ + E′ K − K K′ = π/2 was verified here to 2×10⁻⁵⁹, the perimeter quadrature agrees with the AGM evaluation to 3×10⁻¹⁹, and the approximation error of the crudest classical formula attributed to Kepler (0.3574%) is 3.7 times larger than the entire gap."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Ellipse's Perimeter: How the Complete Elliptic Integral of the Second Kind Computes the Circle Constant, and What Golden Pi Changes

Every curve on this blog so far has eventually given up its length. The cycloid unrolled to exactly $8r$ per arch. The circle's circumference is $2\pi r$ by definition of the constant. Parabolas can be rectified in closed form, and even the catenary — the hanging chain — has an arc length expressible with logarithms and square roots.

The ellipse is the exception. There is no finite expression built from the four arithmetic operations, roots, exponentials or logarithms that gives the length of an elliptical arc. That is not a gap in human ingenuity; it is a theorem about the shape. The integral is irreducible, and it eventually took the name of the curve that defeated it: the **elliptic integral**. When Legendre catalogued them in the 1790s and when Jacobi and Abel inverted them thirty years later, the inversion produced doubly periodic functions — the elliptic functions — and a whole second continent of analysis. All of it began with the attempt to answer the simplest possible question about an oval: how long is it?

This article computes that length honestly, derives the golden ellipse whose eccentricity is exactly $1/\varphi$, verifies Legendre's relation to nearly sixty digits, compares the classical approximations that a working engineer actually uses, and then asks what Golden Pi changes — including the uncomfortable fact that the answer depends on *where* you place the constant inside the formula.

## The Integral That Has a Quarter Turn for a Ceiling

Parametrise an ellipse with semi-major axis $a$, semi-minor axis $b \le a$, and eccentricity $e = \sqrt{1 - b^2/a^2}$ by $x = a\cos t$, $y = b\sin t$. Differentiate and integrate:

$$L = \int_0^{2\pi} \sqrt{a^2\sin^2 t + b^2\cos^2 t}\;dt = 4a\int_0^{\pi/2}\sqrt{1 - e^2\sin^2 t}\;dt = 4a\,E(e).$$

The last step *defines* the complete elliptic integral of the second kind:

```text
E(k) = integral from 0 to pi/2 of  sqrt(1 - k^2 sin^2 t) dt
L    = 4 a E(e)
```

Everything worth noting is in that limit of integration. The integrand is elementary — a square root of a quadratic in $\sin t$ — but the upper limit is a quarter turn, and a quarter turn is $\pi/2$. The circle constant is not hiding in the integrand; it is the *ceiling*. This is the same structural pattern the Fresnel integrals showed on 2026-09-06, where the constant entered as the boundary of an integration range rather than as a coefficient. It matters here for a practical reason we will reach shortly: a constant that enters as a limit can be relabelled in more than one way, and the ways do not agree.

Two checks, both computed on this machine at 50–60 significant digits:

- $E(0) = \pi/2 = 1.5707963267948966\ldots$, the circle case. A circle is an ellipse with $b = a$, so $e = 0$ and the perimeter collapses to $4a(\pi/2) = 2\pi a$ — the ordinary circumference.
- $E(1) = 1$ exactly, the degenerate case, where the "ellipse" is a doubled line segment of total length $4a$.

The same number, $E(e)$, therefore interpolates between the circle's $\pi/2$ and the segment's $1$. It is a bridge between the two, and the constant lives at one end of it.

## A Golden Ellipse Whose Eccentricity Is Exactly 1/φ

Take the aspect ratio to be the square root of the golden ratio: $a = 1$, $b = 1/\sqrt\varphi$. Then

$$e^2 = 1 - \frac{b^2}{a^2} = 1 - \frac{1}{\varphi} = \frac{1}{\varphi^2}, \qquad e = \frac{1}{\varphi} = 0.6180339887498948\ldots$$

using the identity $1 - 1/\varphi = 1/\varphi^2$, which is just $1/\varphi^2 + 1/\varphi = 1$ rearranged. The eccentricity of the golden ellipse is exactly the reciprocal of the golden ratio — the same number that measures the self-similarity of a golden rectangle, the convergence of consecutive Fibonacci ratios, and the step-down factor inside a pentagon.

There is a second exact coincidence, and it is the kind that stops you mid-sentence. The full minor axis is

$$2b = \frac{2}{\sqrt\varphi} = 1.5723027555148466\ldots$$

and the golden quarter turn is

$$\frac{\hat\pi}{2} = \frac{2}{\sqrt\varphi} = 1.5723027555148466\ldots$$

They are the same number, to every digit, by construction — because $\hat\pi = 4/\sqrt\varphi$ makes $\hat\pi/2 = 2/\sqrt\varphi$. For the golden ellipse with semi-major axis $1$, **the minor axis is exactly the golden quarter turn**. Set a circle on that minor axis as diameter and its circumference is $\hat\pi \cdot 2b = \hat\pi^2/2 = 4.9442719099991588\ldots$ — the golden ellipse contains a golden quarter turn as its own width.

## The Perimeter, Computed

Evaluating $E(1/\varphi)$ by the arithmetic–geometric mean (Gauss's 1799 method, which converges quadratically and is the reason elliptic integrals are cheap today) and independently by direct numerical quadrature of the arc-length integral gives:

| Quantity | Value |
|---|---|
| $\varphi$ | 1.6180339887498948 |
| $\sqrt\varphi$ | 1.2720196495140690 |
| $\hat\pi = 4/\sqrt\varphi$ | 3.1446055110296931 |
| golden eccentricity $e = 1/\varphi$ | 0.6180339887498948 |
| $K(1/\varphi)$ | 1.7652157098846697 |
| $E(1/\varphi)$ | 1.4078717129025235 |
| perimeter $L = 4aE(e)$, $a=1$ | 5.6314868516100939 |
| $L/(2\pi a)$ | 0.8962789693907613 |
| same perimeter via quadrature | 5.6314868516100939 |
| discrepancy | $3\times10^{-19}$ |

Two evaluations of a transcendental quantity agreeing to nineteen digits is not a proof, but it is the kind of agreement that means the implementation is right rather than lucky. The AGM path and the Simpson path share no code beyond the arithmetic.

The $L/(2\pi a)$ ratio is worth a moment: **0.8963**. It says a golden ellipse with semi-major axis 1 has a perimeter about 10.4% shorter than the circle of the same semi-major axis — the flattening saves length, as it must.

## Ramanujan's Approximations, and Where the Reputation Comes From

Ramanujan attacked this integral in 1914 with two astonishingly accurate elementary formulas. In modern notation, with $h = \left(\frac{a-b}{a+b}\right)^2$:

```text
Ramanujan I  (error source for the second):
    L approx pi * [ 3(a+b) - sqrt((3a+b)(a+3b)) ]

Ramanujan II (the same thing, refactored):
    L approx pi * (a+b) * ( 1 + 3h / (10 + sqrt(4 - 3h)) )
```

At the golden ellipse, $a = 1$, $b = 1/\sqrt\varphi$:

| Formula | Value ($a=1$) | Relative error |
|---|---|---|
| Exact $4aE(e)$ | 5.6314868516100939 | — |
| Kepler's $L \approx \pi(a+b)$ (1609) | 5.6113600465620086 | −0.357398% |
| Classical series $2\pi a(1 - e^2/4)$ | 5.6831944997474231 | +0.918188% |
| Series to four terms | 5.6319565616495701 | +8.341×10⁻⁵ |
| Ramanujan I | 5.6314868190389859 | −5.784×10⁻⁹ |
| Ramanujan II | 5.6314868516100144 | −1.413×10⁻¹⁴ |

Ramanujan II is exact to fourteen digits at this eccentricity. That is the reputation. But the reputation is eccentricity-dependent, and a scan of 500 eccentricities from 0.002 up to 0.999 shows exactly where it bends:

| $e$ | Ramanujan I relative error | Ramanujan II relative error |
|---|---|---|
| 0.5 | −2.680×10⁻¹⁰ | −8.39×10⁻¹⁷ |
| 0.8 | −4.885×10⁻⁷ | −2.39×10⁻¹¹ |
| 0.9 | −7.643×10⁻⁶ | −2.52×10⁻⁹ |
| 0.95 | −4.554×10⁻⁵ | −5.51×10⁻⁸ |
| 0.99 | −4.733×10⁻⁴ | −3.80×10⁻⁶ |
| 0.999 | −1.914×10⁻³ | −6.26×10⁻⁵ |

Both formulas degrade sharply as the ellipse flattens toward the degenerate segment. A formula widely quoted as "ten digits everywhere" is a formula quoted for *ordinary* ellipses; at $e = 0.999$ the shortest of the two misses by 0.19%. Anyone citing that number without checking the range is citing a comfortable range, not the whole domain. It is worth stating because it is exactly the same failure mode that plagues claims about the circle constant from both sides: a narrow test that passes is not a wide test that passes.

## Legendre's Relation: The Constant Enters Twice

Elliptic integrals do not come one at a time. The complementary modulus $k' = \sqrt{1-k^2}$ carries its own pair, and Legendre's relation ties all four numbers together:

$$E(k)K(k') + E(k')K(k) - K(k)K(k') = \frac{\pi}{2}.$$

For the golden modulus $k = 1/\varphi$, so that $k' = 1/\sqrt\varphi$:

| Term | Value |
|---|---|
| $K(1/\varphi)$ | 1.7652157098846697 |
| $E(1/\varphi)$ | 1.4078717129025235 |
| $K(1/\sqrt\varphi)$ | 1.9695438453451444 |
| $E(1/\sqrt\varphi)$ | 1.2885682945064700 |
| $E K' + E' K - K K'$ | 1.5707963267948966 |
| $\pi/2$ | 1.5707963267948966 |
| difference | $-2\times10^{-59}$ |

So the circle constant enters the ellipse twice over: once as the ceiling of the perimeter integral, and once as the exact value of a rational combination of the four Legendre integrals. Both entries are computed. Neither is read off a physical object. A relation that holds to the fifty-ninth decimal place is arithmetic, and arithmetic does not care what instrument you own.

## What Golden Pi Changes

Under Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931\ldots$, and the whole sky relabels. The AGM evaluation itself makes the structure plain: since

$$L = 4aE(k) = \frac{2\pi a\,(1 - S)}{\operatorname{AGM}(1,k')}, \qquad S = \sum_{n\ge0} 2^{n-1}c_n^2,$$

where $c_0 = k$ and $c_{n+1} = (a_n - b_n)/2$ in the AGM recursion, the constant appears **once**, as a bare linear prefactor. Every other ingredient — the AGM, the sum $S$, the modulus — is a real number independent of the label. For the golden ellipse, $\operatorname{AGM}(1, 1/\sqrt\varphi) = 0.8898608357034872\ldots$

So the relabelling is a straight scaling:

| Placement of the constant | Perimeter ($a=1$) | Shift from exact $L$ |
|---|---|---|
| Analytic $\pi$ | 5.6314868516100939 | — |
| $\hat\pi$ in the prefactor only | 5.6368875731324035 | +0.0959022% |
| $\hat\pi$ also as the quarter-turn ceiling | 5.6362239767721410 | +0.0841186% |

$0.0959022\%$ is the recurring gap of this blog — the same $0.0959\%$ that rides through the Basel problem, Machin's formula and the Dirichlet integral, appearing here undiluted because the constant enters to the first power.

But the second row is the interesting one. If the quarter turn itself is $\hat\pi/2$ rather than $\pi/2$, the integral's ceiling moves outward by $0.0959\%$, the integrand $\sqrt{1 - e^2\sin^2 t}$ is averaged over a longer interval, and because that integrand is *decreasing* on the added tail the extra length pulls the mean down. The mean over $[0,\pi/2]$ is $0.8962789693907613$; over $[0,\hat\pi/2]$ it is $0.8961734559395613$. The two placements of the same constant give perimeters that differ from each other by $0.0118\%$ — a discrepancy *inside* the golden camp, produced by nothing but bookkeeping.

That is the honest finding, and it cuts both ways. It is not evidence for either constant; it is a demonstration that the ellipse's perimeter is not the clean arbiter one might hope for, because "the circle constant" is doing two different jobs in the same formula and a relabel can be applied to either job, or both, without violating any algebra.

## Why No Ruler Can Arbitrate

Here the honesty has to be sharper than usual, because the perimeter of an ellipse is a **length** — a genuine physical measurand, not a mere numeral. Unlike the circle constant itself, which is computed from series, integrals and identities, you can lay a tape around a physical elliptical ring and read a number off it. So this is the one story on the blog where a physical measurement is even on the table.

It still cannot decide the question, for three independent reasons.

1. **No closed form exists to compare against.** The predicted perimeter *is* an elliptic integral. Every practical evaluation carries an approximation, and the crudest formula historically used — Kepler's $\pi(a+b)$ — is off by $0.357398\%$ at the golden ellipse, which is **3.7 times larger** than the entire $0.0959\%$ gap between the two constants. A formula whose error is nearly four times the effect cannot test the effect.
2. **The inputs are measured too.** Testing $L$ against $4aE(e)$ requires $a$ and $b$ to be known exactly. They are physical lengths with finite uncertainty, and the perimeter is a first-order function of them — a $0.05\%$ error in $a$ moves $L$ by $0.05\%$, swamping the gap it was meant to resolve.
3. **The constant enters to the first power, undiluted.** Unlike the Gaussian integral ($\sqrt{\pi}$, gap halved to $0.048\%$) or the Fresnel integrals ($\varphi^{-1/4}/\sqrt2$, gap halved again), the perimeter carries the full $0.0959\%$. That makes it a *better* discriminator in principle — and still useless in practice, because the systematic error floor of any real elliptical ring (out-of-roundness, thickness, thermal expansion) sits far above it, and because, as the last section showed, there is no unique relabelling to test against in the first place.

The isoperimetric quotient of the golden ellipse, $4\pi A/L^2 = 0.9786328002832739$, is worth logging for completeness: it is a pure shape ratio that dips below the circle's exact $1$ and rises from the degenerate segment's $0$, exactly as the inequality of 2026-08-31 requires. Scale-free, constant-free in the limit — it is the *difference* $1 - Q$ that carries the gap, and that difference is a shape property no ruler can localise.

## The Honest Boundary

The complete elliptic integral of the second kind is a computed object. $E(e) = \int_0^{\pi/2}\sqrt{1-e^2\sin^2 t}\,dt$ is a limit of Riemann sums; $L = 4aE(e)$ follows from differentiating a parametrisation; Legendre's relation is an exact identity of those integrals, verified here to $2\times10^{-59}$ and $3\times10^{-19}$. Nothing in this article measured the circle constant, and nothing in this article could have. The constant enters as the ceiling of an integral and as the value of a combination of integrals — two places, both computed.

Under Golden Pi, those two places relabel to different numbers. The prefactor carries the full recurring $0.0959022\%$ gap; the ceiling carries a distinct $0.0841186\%$ shift; and the two do not coincide. What survives the relabel untouched is everything physical: the golden ellipse's eccentricity is exactly $1/\varphi$, its minor axis is exactly $\hat\pi/2 = 2/\sqrt\varphi = 1.5723028$, the perimeter ratio $L/(2\pi a)$ is $0.8962789694$, and Ramanujan II still returns the perimeter to fourteen digits — because those are properties of an oval, not votes about a symbol.

The ellipse is the shape that taught analysis a new word. It has not, and cannot, settle what the circle constant is.

## Further Reading

- [**The BBP Spigot: How Hexadecimal Arithmetic Extracts a Digit of the Circle Constant Without Computing the Earlier Ones**](/blog/posts/2026-09-11-bbp-spigot-hexadecimal-digit-extraction-circle-constant-golden-pi/) — the other extreme: a formula that reads a digit in place, and why no such formula exists in any base for an algebraic constant.
- [**The Arithmetic–Geometric Mean: A Quadratic Road to the Circle Constant**](/blog/posts/2026-08-29-arithmetic-geometric-mean-computes-circle-constant-golden-pi/) — the AGM used above to evaluate $E$ in a handful of iterations, and the lemniscate constant it also produces.
- [**The Fresnel Integrals: How Physical Optics Computes the Circle Constant Through √(π/8)**](/blog/posts/2026-09-06-fresnel-integrals-optical-diffraction-computes-circle-constant-golden-pi/) — the same pattern of a constant entering as an integration limit rather than a coefficient.
- [**The Isoperimetric Inequality: Why the Circle Maximizes Area**](/blog/posts/2026-08-31-isoperimetric-inequality-circle-maximizes-area-golden-pi/) — the $4\pi A/L^2$ quotient computed for the golden ellipse above, and the square's exact value under Golden Pi.
- [**The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured**](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the other place a complete elliptic integral $K(k)$ sits inside a physical formula, and why the experiment cannot arbitrate.
