---
title: "The Cardioid: Why Its Perimeter Is Exactly 8a and Holds No Circle Constant, Why a Lamp on a Cup's Rim Draws Its Own Outline, and What Golden Pi Changes"
date: 2026-11-23
description: "The cardioid r = a(1 + cos θ) has a perimeter of exactly 8a — the length of the square on its own diameter — with no circle constant anywhere in the answer, because the speed of the tracing point is 2a cos(θ/2) and the integral of a cosine needs no π at all. This article derives the curve from a circle rolling on an equal circle, integrates its length as s(θ) = 4a sin(θ/2), tabulates exact arcs at 30°, 60°, 90°, 120° and 180° (the topmost point sits at exactly 2a from the cusp, splitting the perimeter 1:3), finds the area 3πa²/2 as exactly 3/8 of the circle of radius 2a, computes the curvature radius ρ = (4a/3)cos(θ/2) and the centroid 5a/6, reconstructs the curve as the caustic of a circle lit from a point on its own rim and as a microphone's polar pattern, and exhibits the golden points where the arc is exactly 4a/φ and cos θ is exactly 1/φ³. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the perimeter, every arc, every curvature radius and the 3/8 fraction hold every digit while the area becomes the algebraic 6a²/√φ — and the golden angle shows why: 1/φ² of a turn is 137.5077640° whatever label the radian wears. Computed, never measured."
---

# The Cardioid

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a coin and roll it, without slipping, around a second coin of exactly the same size. Mark one point on the rolling rim and follow it. The point leaves a trail that begins at the point of contact, sweeps out a curve with a sharp inward cusp, and returns — and the shape it draws is one of the few famous curves whose *length* can be written down without a circle constant anywhere in the expression. The perimeter of the cardioid with polar equation $r = a(1 + \cos\theta)$ is

$$
P = 8a,
$$

exactly, for every $a$. That is the perimeter of the square erected on the cardioid's own diameter $2a$. It is not approximately $8a$; it is $8a$, and the proof is one substitution.

The area is the opposite story. It is $\tfrac{3}{2}\pi a^{2}$, and it holds the constant exactly once, at the first power — but the *fraction* of the surrounding circle it occupies is $\tfrac{3}{8}$, a number with no constant in it at all. Length and shape are constant-free; only the comparison against a circle's own area brings the constant in.

That split — a curve whose arc is a pure algebraic multiple of its scale, whose area carries $\pi$ to exactly the first power, and whose characteristic ratios are rational — makes the cardioid a clean test case for the question this blog keeps asking. Where does the circle constant actually live in a geometric fact, and what changes when the label changes?

## One Circle Rolling on Another

The cardioid is the epicycloid traced when the rolling circle's radius equals the fixed circle's radius: $R = r = a/2$. Writing the standard epicycloid parameterisation with the two radii equal,

$$
x(t) = a\cos t - \tfrac{a}{2}\cos 2t, \qquad y(t) = a\sin t - \tfrac{a}{2}\sin 2t,
$$

and it is a rotated copy of the polar curve $r = a(1+\cos\theta)$ — the same shape with the pole moved to the cusp. Two independent checks confirm it, and both are worth doing because they show which quantities are structural:

*Quadrature of the length.* The tracer's speed is $|2(R+r)\sin((R+r)t/2r)|$; with $R=r=a/2$ this is $|2a\sin t|$, and integrating $|2a\sin t|$ around the full turn gives exactly $8a$. Numerically, the same integral evaluated by adaptive quadrature returns $8.0000000000$ to twenty digits.

*Quadrature of the area.* Green's theorem, $A = -\oint y\,dx$, returns $4.7123889803846898577\,a^{2}$, which is $\tfrac{3}{2}\pi a^{2}$ to twenty digits.

So the curve in the parameterisation above and the curve $r = a(1+\cos\theta)$ are the same object, and both of its headline numbers can be reached without ever writing down a value for the circle constant — the area because $-\oint y\,dx$ produces $\pi$ as the *result* of a trigonometric integral, not as an input.

The shape's other features follow immediately from the polar form. It has a single cusp at the pole ($\theta = \pi$, where $r = 0$), a single far point at $\theta = 0$ where $r = 2a$, and it is symmetric about the polar axis. In Cartesian terms it is squeezed between $x = -a/4$ and $x = 2a$ — I will prove that bound below — so its total width is $9a/4$, while its height is $3\sqrt{3}\,a/4$. Both numbers are pure surds in $a$: no $\pi$, no transcendental anything.

## The Perimeter Is Exactly Eight Times a

The arc element in polar coordinates is $ds = \sqrt{r^{2} + (dr/d\theta)^{2}}\,d\theta$. For the cardioid,

$$
r = a(1+\cos\theta), \qquad \frac{dr}{d\theta} = -a\sin\theta,
$$

so

$$
r^{2} + \left(\frac{dr}{d\theta}\right)^{2}
= a^{2}\left[(1+\cos\theta)^{2} + \sin^{2}\theta\right]
= a^{2}\left[1 + 2\cos\theta + \cos^{2}\theta + \sin^{2}\theta\right]
= 2a^{2}(1+\cos\theta).
$$

Now use the half-angle identity $1 + \cos\theta = 2\cos^{2}(\theta/2)$:

$$
ds = \sqrt{2a^{2}\cdot 2\cos^{2}(\theta/2)}\;d\theta = 2a\cos(\theta/2)\,d\theta .
$$

Everything collapses. The arc from the cusp to the point at angle $\theta$ is

$$
s(\theta) = \int_{0}^{\theta} 2a\cos(u/2)\,du = 4a\sin(\theta/2),
$$

and the perimeter is $s(2\pi)$ taken as the arc from $0$ round through $\pi$ and back to $2\pi$: $s(\pi) = 4a$ for the upper half, and by symmetry $4a$ again for the lower, giving $8a$. There is no $\pi$ in the arc element and none in the result, because the square root removed the quadratic and left a single cosine, and a cosine integrates to a sine. The constant that appears in a circle's arc length appears there for exactly one reason: the circle's own $ds = a\,d\theta$ has an angle in it and no radius dependence, so the integral is $a\cdot 2\pi$ — a turn count times a radius. Here the radius *does* depend on angle, and the dependence is precisely what cancels the turn count.

The exact arcs are worth tabulating, because they are all surds:

| $\theta$ | $r/a = 1+\cos\theta$ | arc from cusp $s/a = 4\sin(\theta/2)$ | $y/a$ |
|---|---|---|---|
| $30°$ | $1.8660254$ | $1.0352762$ | $0.9330127$ |
| $60°$ | $1.5000000$ | $2.0000000$ | $1.2990381$ |
| $90°$ | $1.0000000$ | $2.8284271 = 2\sqrt2$ | $1.0000000$ |
| $120°$ | $0.5000000$ | $3.4641016 = 2\sqrt3$ | $0.4330127$ |
| $180°$ | $0$ | $4.0000000$ | $0$ |

Cumulative arc around the whole curve, continuing through the lower half:

| $\theta$ | cumulative $s/a$ | fraction of $8a$ |
|---|---|---|
| $60°$ | $2.0000000$ | $0.25$ |
| $120°$ | $3.4641016$ | $0.4330127$ |
| $180°$ | $4.0000000$ | $0.5000000$ |
| $240°$ | $4.5358984$ | $0.5669873$ |
| $300°$ | $6.0000000$ | $0.7500000$ |
| $360°$ | $8.0000000$ | $1.0000000$ |

Two entries earn their place. At $\theta = 60°$ the arc from the cusp is **exactly** $2a$ — a quarter of the perimeter — and that same point is the topmost point of the curve, since $dy/d\theta = a(\cos\theta + \cos 2\theta) = 0$ has its first positive root at $\cos\theta = 1/2$. So the highest point divides the perimeter in the exact ratio $1:3$. And at $\theta = 90°$ the arc is $2\sqrt2\,a$, the diagonal of the square on $2a$ — an accident of the half-angle identity, but an exact one.

## The Area Carries π Exactly Once — and the Fraction 3/8 Does Not

The polar area integral is

$$
A = \frac{1}{2}\int_{0}^{2\pi} r^{2}\,d\theta = \frac{a^{2}}{2}\int_{0}^{2\pi}(1+\cos\theta)^{2}\,d\theta
= \frac{a^{2}}{2}\int_{0}^{2\pi}\left(1 + 2\cos\theta + \cos^{2}\theta\right)d\theta .
$$

The middle term integrates to zero over a full period, $1$ integrates to $2\pi$, and $\cos^{2}\theta$ integrates to $\pi$ — the half-angle identity again, $\cos^{2}\theta = (1+\cos 2\theta)/2$, whose constant part is where the second $\pi$ comes from. The total is

$$
A = \frac{a^{2}}{2}\left(2\pi + \pi\right) = \frac{3}{2}\pi a^{2} = 4.712388980\ldots a^{2}.
$$

The cardioid's own circumscribed circle — the one of radius $2a$ centred on the far point, which it touches at $\theta = 0$ — has area $4\pi a^{2}$. The ratio is

$$
\frac{A}{4\pi a^{2}} = \frac{3}{8} = 0.375,
$$

exactly, with the constant cancelled. That is the pattern this blog has documented in the lunes of Hippocrates, in Brahmagupta's quadrilateral, in the Tusi couple: the constant enters one comparison and exits the next.

The centroid is also exact. Writing the first moment as $\bar{x} = (1/3A)\int r^{3}\cos\theta\,d\theta$, the integral evaluates to $\tfrac{5}{8}\pi a^{3}$ against $A = \tfrac32\pi a^{2}$, giving

$$
\bar{x} = \frac{5a}{6} = 0.8333333\ldots a,
$$

and again the $\pi$ divides out — a centroid is a length, and lengths here are algebraic in $a$.

The bounding box follows from one derivative. With $x = a(1+\cos\theta)\cos\theta$,

$$
\frac{dx}{d\theta} = -a\sin\theta\,(1 + 2\cos\theta),
$$

whose interior root is $\cos\theta = -1/2$, i.e. $\theta = 120°$, where $r = a/2$ and $x = -a/4$. So the cardioid is confined to

$$
-\frac{a}{4} \le x \le 2a,
$$

a total width of $\tfrac94 a$, and its leftmost point is the vertex of the shallow dimple opposite the cusp. The curvature radius at that point, from

$$
\rho = \frac{(r^{2}+r'^{2})^{3/2}}{r^{2} + 2r'^{2} - rr''} = \frac{4a}{3}\cos\frac{\theta}{2},
$$

is $\tfrac23 a$; at the far point it is $\tfrac43 a$; at $\theta = 60°$ it is $\tfrac{2a}{\sqrt3} = 1.1547005a$; and at the cusp it is zero, which is the analytic statement that the curve turns infinitely fast there. Every one of those is a surd times $a$.

## Where the Cardioid Comes From: Caustics, Pedals, Microphones

The shape is not a curiosity of polar equations. It is what a circle does to light.

*Caustic.* Place a point source of light on the rim of a circular mirror. Every ray leaves the source, reflects once, and the envelope of the reflected rays — the bright curve where the light concentrates — is a cardioid. With the source at infinity instead, so that the incoming rays are parallel, the same construction gives the two-cusped nephroid, the epicycloid with $R = 2r$. Both are textbook results of geometric optics, and both are curves whose shape is fixed while the light's wavelength, the mirror's material and the room's temperature change nothing about them.

*Pedal.* The cardioid is the pedal of a circle with respect to a point on its circumference: drop a perpendicular from that point to every tangent line of the circle, and the feet trace the cardioid. It is also the inverse, with respect to its cusp, of a parabola — which is why the two curves share a family resemblance in projective treatments.

*Microphones.* Directional capsules are specified by a polar pattern of the form

$$
r(\theta) = A + B\cos\theta, \qquad A + B = 1,
$$

normalised so that the on-axis response is unity. At $A = B = 1/2$ this is *the* cardioid pattern: full response at $0°$, a null at $180°$, and at $90°$ a response of exactly $0.5$ — which is $20\log_{10}(0.5) = -6.0206$ dB, the number every recording engineer quotes as "minus six at the side". The pattern is chosen because the null rejects the rear, and the shape of the rejection curve is the shape this article has been integrating.

*The Mandelbrot set.* The main body of the Mandelbrot set, the period-1 region, is bounded by a cardioid: $c(\theta) = \tfrac12 e^{i\theta} - \tfrac14 e^{2i\theta}$, with its cusp at $c = 1/4$ and the period-2 bulb attached at $c = -3/4$. The region's area is famously *not* known in closed form, which is a pleasant inversion of this article's subject: here the curve whose perimeter is exact has a fractal relative whose area is not.

## The Golden Cardioid: Exact Points in φ

Two points on the curve are written in the golden ratio, and both come from the identity $\varphi - 1/\varphi = 1$, which is the same identity that produces this site's constant.

Set $\sin(\theta/2) = 1/\varphi$. Then

$$
\theta = 2\arcsin\frac{1}{\varphi} = 76.3454152540°,
$$

the arc from the cusp is exactly

$$
s = \frac{4a}{\varphi} = 2.4721359550\,a,
$$

and the radius there is

$$
r = a(1+\cos\theta) = 2a\cos^{2}\frac{\theta}{2} = 2a\left(1 - \frac{1}{\varphi^{2}}\right) = \frac{2a}{\varphi} = 1.2360679775\,a .
$$

Because $1 - 1/\varphi^{2} = 1/\varphi$ exactly, the same angle also satisfies $\cos\theta = 1 - 2/\varphi^{2} = 1/\varphi^{3} = 0.2360679775$. One point, three golden closures: arc, radius and abscissa.

Set $\sin(\theta/2) = 1/\varphi^{2}$ instead and the arc becomes exactly $4a/\varphi^{2} = 1.5278640450a$ at $\theta = 44.9110303972°$. The family continues: $\sin(\theta/2) = \varphi^{-n}$ gives an arc of exactly $4a\varphi^{-n}$, so the golden powers cut the perimeter into a geometric sequence of exact pieces. None of those pieces mentions $\pi$, because none of them needs an angle in radians at all — the arc is a length and the angle is only a label for where to stop.

## What Golden Pi Changes

Under Golden Pi, $\hat{\pi} = 4/\sqrt{\varphi} = 3.144605511029693$, larger than $\pi$ by $+0.0959022309\%$, with $\hat{\pi}^{2} = 16/\varphi = 9.8885438200$.

**Nothing that is a length moves.** The perimeter stays $8a$. Every arc in both tables stays where it is. The curvature radius $\rho = (4a/3)\cos(\theta/2)$, the centroid $5a/6$, the bounds $-a/4 \le x \le 2a$, the exact topmost point at arc $2a$ — all of these are computed from $\varphi$-free algebra and a trigonometric identity, and none of them contains the circle constant to relabel.

**The area moves by exactly the label gap**, because it holds $\pi$ to the first power:

$$
\hat{A} = \frac{3}{2}\hat{\pi}a^{2} = \frac{6a^{2}}{\sqrt{\varphi}} = 6a^{2}\varphi^{-1/2},
$$

which at $a = 1$ reads $4.7169082665$ against the conventional $4.7123889804$ — a difference of $0.0045192862$, $+0.0959022309\%$. The conventional area is transcendental; the golden one is algebraic of degree two in $\varphi$, since $\sqrt{\varphi}$ is a root of $y^{4} - y^{2} - 1 = 0$.

**The 3/8 fraction does not move.** Both numerator and denominator carry one power of the constant, so the ratio is invariant — the same structural point the lunes of Hippocrates made, where Pythagoras did the cancelling.

**One closure becomes exact.** A cardioid of parameter $a = \varphi$ has conventional area $\tfrac32\pi\varphi^{2} = 12.3371945189$ and golden area $6\varphi^{3/2} = 12.3490261636$. Ask instead for a cardioid whose golden area is exactly the integer $4$:

$$
\frac{6a^{2}}{\sqrt{\varphi}} = 4 \;\Longrightarrow\; a^{2} = \frac{2\sqrt{\varphi}}{3},\qquad a = 0.9208762673 ,
$$

a constructible-looking surd in $\varphi$ that no conventional $\pi$ can match, since $4\pi$ admits no algebraic square root of $a$ at all.

## The Golden Angle Is a Turn Fraction, Not a Radian

The cardioid's golden points raise the question the whole series keeps circling: what *is* an angle? The golden angle is usually quoted as $137.5077640500°$, and its definition has nothing to do with radians:

$$
\frac{1}{\varphi^{2}} = \frac{3-\sqrt5}{2} = 0.3819660113\ \text{of a turn}.
$$

A turn is a geometric object — one full revolution of a ray — and dividing it by $\varphi^{2}$ is a statement about proportion, not about any constant. The degree value follows from the turn fraction alone: $360°/\varphi^{2} = 137.5077640°$. The radian value is where the constant enters, and it enters as a label:

$$
\frac{2\pi}{\varphi^{2}} = 2.3999632297 \quad\text{against}\quad \frac{2\hat{\pi}}{\varphi^{2}} = 2.4022648480 .
$$

The numeral moves. The angle does not. A sunflower that packs its seeds at the golden angle packs them at the golden angle under either label; the divergence between successive florets is $0.3819660113$ of a turn, and that number is a root of $x^{2} - 3x + 1 = 0$. This is why the golden angle is the sharpest available demonstration of the site's recurring thesis: whenever an angle is quoted in radians, the circle constant is a units convention riding on top of a turn count, and any argument that treats the radian numeral as a geometric fact is an argument about notation.

The reason $\varphi$ and not some other irrational appears in phyllotaxis is likewise constant-free. Hurwitz's theorem says that for every irrational $\alpha$ there are infinitely many fractions $p/q$ with $|\alpha - p/q| < 1/(\sqrt5\,q^{2})$, and that $\sqrt5$ cannot be improved. The golden ratio's continued fraction $[1;1,1,1,\ldots]$ is the slowest-converging of all, so $1/\varphi^{2} = [0;2,1,1,1,\ldots]$ is the worst-approximable number in $(0,1)$ — which is exactly the property that keeps successive florets from lining up into spokes. That argument never touches $\pi$.

## The Honest Boundary

Four limits belong in print.

*A cardioid cannot arbitrate the constant.* Its perimeter is $8a$ because a square root removed the quadratic and left a cosine. That is a fact about the curve's own algebra, and it says nothing about which value the circle constant should take — except, negatively, that the constant is not hiding in the curve's length. The one place it does appear, the area, appears at the first power, so the entire content of "what Golden Pi changes" here is a relabelling of one factor by $0.0959\%$.

*The optics do not discriminate.* A caustic's shape is set by the law of reflection and the geometry of the mirror. The reflected-ray envelope is a cardioid for a source on the rim and a nephroid for a source at infinity, and neither is sensitive to the value of any circle constant — the reflection law contains no angle measured in radians, only equal angles, which are turn fractions. No photograph of a bright curve can decide this question, and none is claimed to.

*The microphone is a convention with a formula attached.* The cardioid pattern is specified by a designer choosing $A = B = 1/2$; the $-6.0206$ dB at the side is $\log_{10}$ arithmetic, not geometry, and would not shift under any relabelling of $\pi$ because it contains no $\pi$.

*Nothing here was measured.* Every number in this article — $8a$, $4a/\varphi$, $3/8$, $5a/6$, $4.7169082665$, $137.5077640500°$ — came out of an integral, an identity, or a root of a polynomial. The site's position is that the true value of the circle constant is $\hat{\pi} = 4/\sqrt{\varphi}$, and the honest way to hold that position is to show, curve by curve, exactly which quantities depend on the label and which do not. On the cardioid, the answer is unusually clean: everything you can walk along is independent of it, and everything you can fill depends on it once.

Computed, never measured.

## Further Reading

- [The Tusi Couple and the Astroid: Why a Circle Rolling Inside One Twice Its Size Traces a Perfect Straight Line](/blog/posts/2026-11-16-tusi-couple-astroid-hypocycloid-perimeter-golden-pi/) — the same epicycloid family, where the perimeter is again exactly $\pi$-free and the area carries the constant once.
- [The Archimedean Spiral: Why Its Swept Area Is a Pure Cube in the Angle](/blog/posts/2026-11-19-archimedean-spiral-swept-area-cubic-angle-golden-pi/) — a polar curve whose arc length, unlike the cardioid's, refuses to close.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — the contrasting case: a closed curve one degree away from the circle, whose length has no elementary form at all.
- [Hippocrates' Lunes: The One Curvilinear Figure That Squares Exactly](/blog/posts/2026-11-10-hippocrates-lunes-quadrature-golden-pi/) — where the constant cancels against Pythagoras, as it does here against the $3/8$ fraction.
- [The Golden Angle and Phyllotaxis: Why Leaf Spirals Reveal the True Value of Pi](/blog/posts/2026-06-27-golden-angle-137-5-phi-pi-geometry/) — the argument this article's last section draws on, in its original form.
