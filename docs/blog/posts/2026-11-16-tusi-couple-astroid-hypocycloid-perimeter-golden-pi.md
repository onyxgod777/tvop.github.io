---
title: "The Tusi Couple and the Astroid: Why a Circle Rolling Inside One Twice Its Size Traces a Perfect Straight Line, Why Every Hypocycloid's Perimeter Is Exactly π-Free, and What Golden Pi Changes"
date: 2026-11-16
description: "A circle of radius r rolling without slipping inside a fixed circle of radius R = kr traces a hypocycloid, and its tracer's speed is 2(R−r)|sin(kt/2)| — a form containing no circle constant at all, which is why the perimeter is exactly 8(R−r) for every integer k, while the enclosed area is πr²(k−1)(k−2), carrying the constant exactly once. This article derives the parametrisation from the rolling condition, proves the Tusi couple as the degenerate case k = 2 where the tracer's two sinusoidal components cancel to y ≡ 0 exactly and the point slides along a diameter as 2r·cos t, tabulates the whole family from the deltoid (k = 3, P = 16r, A = 2πr², 2/9 of its circumscribed circle) to the astroid (k = 4, P = 6a, A = 3πa²/8, 3/8), shows the covering fraction is the π-free (1−1/k)(1−2/k), and works the astroid in full: curvature radius 3a·sin t·cos t peaking at 3a/2, the figure confined to the annulus [a/2, a], its identity as the envelope of a sliding ladder, and the exact ratio A/P = πa/16. Rational ratios are then closed exactly — k = p/q gives p cusps and a signed area πr²(p−q)(p−2q)/q — which exposes what an irrational ratio does: with R/r = φ the curve never closes, is dense in the annulus whose inner radius is exactly r/φ² and outer exactly rφ, of width exactly 2r/φ, of area exactly 4πr²/φ = 94.427% of the circle it fits inside, with the signed area per Fibonacci winding diverging at exactly −πr²/φ³. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) every area becomes algebraic — 6π̂ = 24/√φ = 18.867633066…, the astroid's A/P = r/√φ, the golden annulus 16r²/φ^{3/2} — while every perimeter, every covering fraction and the entire Tusi cancellation do not move a digit. Computed, never measured."
---

# The Tusi Couple and the Astroid

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a spirograph — the toy with a toothed ring and a smaller toothed wheel inside it — and pin the pen to the wheel's rim. Turn the wheel round the ring once and the pen draws a curve with cusps: sharp points where the line stops, turns, and goes back. Now make the inner wheel exactly half the ring. The cusps vanish, the curve collapses, and the pen slides along a straight line through the centre. A device generating perfect rectilinear motion out of two circular motions is not a toy but a piece of thirteenth-century astronomy, and it is the cleanest place in classical geometry where the circle constant can be watched leaving an equation.

This article follows that constant through the whole family. It enters exactly once — in the area — and it is provably absent from the perimeter, from every ratio of areas, and from the Tusi cancellation itself.

## The Construction

Fix a circle of radius $R$ centred at the origin; roll inside it a circle of radius $r$ without slipping, and track a point on the rolling rim. The centre of the rolling circle travels on a circle of radius $R-r$ at angular rate $\dot t = 1$, so it sits at $\bigl((R-r)\cos t,\,(R-r)\sin t\bigr)$. Rolling without slipping inside means the contact point is instantaneously at rest, which forces the wheel to spin in the opposite sense at rate $-(R-r)/r$ relative to its own centre. Writing $k = R/r$ and $\lambda = k-1 = (R-r)/r$, the tracer is

$$
X(t) = (R-r)\cos t + r\cos(\lambda t), \qquad
Y(t) = (R-r)\sin t - r\sin(\lambda t).
$$

```text
fixed circle radius  R = k r
rolling circle radius r
spoke rate           lambda = (R - r)/r = k - 1
tracer (on the rim)  X = (R-r)cos t + r cos(lambda t)
                     Y = (R-r)sin t - r sin(lambda t)
velocity             V = 2(R-r) sin(k t / 2)      (magnitude, signed by branch)
cusps                t = 2*pi*j/k,  j = 0..k-1   (integer k)
```

Differentiating and collecting terms gives $X' = -(R-r)\bigl[\sin t + \sin\lambda t\bigr]$ and $Y' = (R-r)\bigl[\cos t - \cos\lambda t\bigr]$, so

$$
|V|^{2} = (R-r)^{2}\Bigl[2 - 2\cos\bigl((1+\lambda)t\bigr)\Bigr] = 4(R-r)^{2}\sin^{2}\!\frac{kt}{2},
$$

because $1+\lambda = k$. Every property in this article comes out of that one line, and the line contains no $\pi$. The speed vanishes exactly where $\sin(kt/2) = 0$, that is at $t = 2\pi j/k$: $k$ instants per revolution at which the tracer is momentarily at rest. Those are the cusps. A cusp is not a corner drawn by hand; it is a place where the pen stops.

## The Tusi Couple: The Case $k = 2$

Set $R = 2r$, so $\lambda = 1$. The parametrisation becomes

$$
X = r\cos t + r\cos t = 2r\cos t, \qquad Y = r\sin t - r\sin t = 0,
$$

and the second coordinate is not merely small — it is identically zero, term by term, because the two contributions have equal amplitude and opposite phase. The curve is the segment from $-2r$ to $+2r$, traversed twice per revolution, and the tracer's motion along it is $x = 2r\cos t$: simple harmonic motion at constant angular rate, the exact projection of uniform circular motion onto a diameter.

This is the **Tusi couple** (*zawja*), described by Naṣīr al-Dīn al-Ṭūsī in his *Tadhkira fī ʿilm al-hayʾa* (c. 1260), and associated with the circle of astronomical instruments at Marāgha. Its purpose was kinematic rather than geometric: it produces oscillation along a line from two uniform rotations, which is exactly what a planetary model needs when it wants a body to move back and forth without inventing a reciprocating mechanism. Historians of astronomy have also argued that a closely related pair of circles appears in Copernicus's *De revolutionibus*; the priority question is scholarly, and nothing below depends on it.

The device is the $d = r$ member of a family worth stating, because the family shows how special the straight line is. Put the tracer at distance $d$ from the rolling circle's centre instead of on its rim. Then

$$
X = r\cos t + d\cos t = (r+d)\cos t, \qquad Y = r\sin t - d\sin t = (r-d)\sin t,
$$

an **ellipse** with semi-axes $r+d$ and $|r-d|$. Only $d = r$ collapses the minor axis to zero.

| $d$ (with $r = 1$, $R = 2$) | semi-axes | enclosed area | figure |
|---|---|---|---|
| 0 | 1.000000, 1.000000 | $\pi = 3.141592654$ | the fixed circle itself |
| 0.5 | 1.500000, 0.500000 | $0.75\pi = 2.356194490$ | ellipse |
| 0.75 | 1.750000, 0.250000 | $0.4375\pi = 1.374446786$ | flatter ellipse |
| 1.0 | 2.000000, 0.000000 | $0$ | the diameter |

The areas are $\pi(r^{2}-d^{2})$ in every row — the constant at first power, multiplied by a difference of squares. The straight line is the unique case in which that product is zero.

## Why the Perimeter Carries No $\pi$

The perimeter is $\int|V|\,dt$ over one closure. With $|V| = 2(R-r)|\sin(kt/2)|$ and $k$ an integer, the integrand has $k$ half-periods across $[0, 2\pi]$, and each contributes the same amount:

$$
P = 2(R-r)\int_{0}^{2\pi}\Bigl|\sin\frac{kt}{2}\Bigr|\,dt
  = 2(R-r)\cdot 4 = 8(R-r) = 8r(k-1).
$$

The factor is $4$, an integer, and it appears because the absolute value of a sine over a whole number of lobes integrates to $2/\pi$ times $\pi$ — the $\pi$ in the antiderivative and the $\pi$ in the period cancel identically. That cancellation is the whole content of the result: **the length of a hypocycloid is a rational multiple of the radii, for every integer $k$.**

| $k = R/r$ | cusps | perimeter $P$ (in $r$) | area $A$ | $A/(\pi R^{2})$ | $A/P$ (in $r$) |
|---|---|---|---|---|---|
| 2 | 2 | $8$ | $0$ | $0$ | $0$ |
| 3 | 3 | $16$ | $2\pi = 6.283185307180$ | $2/9 = 0.222222222222$ | $\pi/8 = 0.392699081699$ |
| 4 | 4 | $24$ | $6\pi = 18.849555921539$ | $3/8 = 0.375000000000$ | $\pi/4 = 0.785398163397$ |
| 5 | 5 | $32$ | $12\pi = 37.699111843078$ | $12/25 = 0.480000000000$ | $3\pi/8 = 1.178097245096$ |
| 6 | 6 | $40$ | $20\pi = 62.831853071796$ | $5/9 = 0.555555555556$ | $\pi/2 = 1.570796326795$ |
| 7 | 7 | $48$ | $30\pi = 94.247779607694$ | $30/49 = 0.612244897959$ | $5\pi/8 = 1.963495408494$ |
| 8 | 8 | $56$ | $42\pi = 131.946891450771$ | $21/32 = 0.656250000000$ | $3\pi/4 = 2.356194490192$ |

The perimeter column is arithmetic. The area column is not, and the reason is worth isolating.

## Where the Constant Actually Lives

Green's theorem gives the enclosed area as $A = \tfrac12\oint(X\,dY - Y\,dX)$, and evaluating it on the parametrisation above — the cross terms integrate to zero over a full period, and what survives is a sum of two squares of the radii — returns

$$
A = \pi r^{2}(k-1)(k-2) = \pi R^{2}\Bigl(1-\frac1k\Bigr)\Bigl(1-\frac2k\Bigr).
$$

This is why the table's fourth column is pure rationals: divide the area by $\pi R^{2}$ and the constant is gone, leaving $(k-1)(k-2)/k^{2} = (1-1/k)(1-2/k)$. The figure covers that fraction of the circle whose radius is its own outer reach, and the fraction tends to $1$ as $1 - 3/k + 2/k^{2}$ — the curve becomes the circle, quadratically.

So the constant enters the area exactly once, and it enters for one reason only: converting a squared length into a measure of the plane. For an integer $k$ the area formula is $\pi$ times an integer times $r^{2}$; the perimeter formula is an integer times $r$. A spirograph measures the second and cannot see the first.

## The Astroid in Full

At $k = 4$ the hypocycloid is the **astroid**, and it is the member of the family with its own literature. Since $R = 4r$ and $X = 3r\cos t + r\cos 3t = 4r\cos^{3}t$ (using $\cos 3t = 4\cos^{3}t - 3\cos t$), it has the classical closed form

$$
x = a\cos^{3}t, \qquad y = a\sin^{3}t, \qquad a = R = 4r,
$$

with perimeter $P = 6a$ (the table's $24r$ with $a = 4r$), area $A = 3\pi a^{2}/8$, and a covering fraction $3/8$ of its circumscribed circle — the circle of radius $a$, which it touches at the four cusps $(a,0), (0,a), (-a,0), (0,-a)$.

Three further exact statements follow from the same parametrisation.

**Curvature.** The speed is $3a|\sin t\cos t|$ and the curvature radius is $\rho = 3a\sin t\cos t$, which vanishes at every cusp and peaks at $3a/2$ on the diagonals. For $a = 4$: $\rho = 1.1920159848$ at $t = 0.1$, $2.3365100539$ at $0.2$, $5.0488259088$ at $0.5$, exactly $6.0000000000$ at $t = \pi/4$ — one and a half times $a$, no constant involved.

**Confinement.** The distance from the centre satisfies $a/2 \le \rho \le a$: at $t = \pi/4$ the point is $(\sqrt2, \sqrt2)$, distance $2 = a/2$ for $a = 4$. The astroid is not a curve that wanders; it is trapped in a specific annulus.

**Envelope.** The astroid is the envelope of a ladder of length $a$ sliding with its ends on two perpendicular walls. Every position of the ladder is tangent to the astroid, and the region it sweeps is the astroid's interior — which is why the shape turns up in the sliding-ladder problem rather than in any drawing of a rolling circle.

And the ratio that will matter under Golden Pi: $A/P = (3\pi a^{2}/8)/(6a) = \pi a/16 = \pi r/4$, exactly the area of a quarter of the circle of radius $r$.

## Rational Ratios, and What an Irrational One Does

If $R/r$ is rational, $k = p/q$ in lowest terms, the tracer closes after $t$ has run through $2\pi q$, and the closed curve has $p$ cusps. The perimeter integral must now be taken over the longer interval, but the area has a subtlety: the curve winds round the centre $q$ times, so its *signed* area counts overlap with multiplicity. Direct quadrature confirms

$$
A = \pi r^{2}\,\frac{(p-q)(p-2q)}{q},
\qquad P = 8r\,(p-q)\ \text{(per closure)}.
$$

| $k = p/q$ | cusps | $A/\pi r^{2}$ computed | $(p-q)(p-2q)/q$ |
|---|---|---|---|
| $5/2$ | 5 | $1.500000000000$ | $1.5$ |
| $8/5$ | 8 | $-1.200000000000$ | $-1.2$ |
| $13/8$ | 13 | $-1.875000000000$ | $-1.875$ |
| $21/13$ | 21 | $-3.076923076923$ | $-38/13$ |

The signs are not an error. A ratio below $2$ puts the tracer's path through the centre region, and the winding number then subtracts regions it has already covered. The areas are negative and grow in magnitude with $q$.

Now let $p/q \to \varphi$. The cusp count follows the Fibonacci numbers — $2, 3, 5, 8, 13, 21, \ldots$ — and the quantity $A/(\pi r^{2} q)$ has a limit:

$$
\lim_{k\to\varphi}(k-1)(k-2) = \Bigl(\frac{1}{\varphi}\Bigr)\Bigl(-\frac{1}{\varphi^{2}}\Bigr) = -\frac{1}{\varphi^{3}},
$$

using $\varphi - 1 = 1/\varphi$ and $\varphi - 2 = -1/\varphi^{2}$. So the signed area per winding diverges at exactly $\pi r^{2}/\varphi^{3} = 0.2360679\ldots \pi r^{2}$ per closure — the signature of a curve that never closes and keeps sweeping new territory.

## The Golden Hypocycloid: $R/r = \varphi$

Set $R = \varphi r$. Then $\lambda = \varphi - 1 = 1/\varphi$, the two angular rates are $1$ and $1/\varphi$, and their ratio is $\varphi$ — irrational. The curve never closes. Its radial distance obeys an exact identity obtained by expanding $|X + iY|^{2}$:

$$
|Z(t)|^{2} = r^{2}\Bigl(\frac{1}{\varphi^{2}} + 1 + \frac{2}{\varphi}\cos(\varphi t)\Bigr),
$$

so as $\cos(\varphi t)$ runs over $[-1,1]$ the radius runs over exactly

$$
\frac{r}{\varphi^{2}} \le |Z| \le r\varphi,
$$

with $r/\varphi^{2} = 0.3819660113\,r$ and $\varphi r = 1.6180339887\,r$. Three exact facts follow:

- the annulus has width $r(\varphi - 1/\varphi^{2}) = 2r/\varphi$ exactly;
- the inner and outer radii multiply to $r^{2}$ exactly, and their ratio is $\varphi^{3} = 4.2360679\ldots$;
- the annulus area is $\pi r^{2}(\varphi^{2}-\varphi^{-4}) = 4\pi r^{2}/\varphi = 7.7664441549\,r^{2}$, which is $4/\varphi^{3} = 94.4272\%$ of the circle it sits inside.

Sampled directly from the parametrisation, to twelve digits: $t=0$ gives $1.618033988750$; $t=0.5$, $1.495029292858$; $t=1$, $1.150477623588$; $t=2$, $0.389114697705$; $t=3$, $1.247616601084$; $t=4$, $1.611221367483$; $t=6$, $0.441829629197$; $t=20$, $1.451286056334$. The angle meanwhile keeps turning: at $t=4$ it reads $-137.511366°$, at $t=10$ it has come round to $-26.129114°$ — the same radii visited at new angles.

Because $1$ and $1/\varphi$ are incommensurable, the pair $(t, t/\varphi)$ runs densely through a torus, and the image under $Z$ is dense in the annulus above: every radius in $[\varphi^{-2}, \varphi]$ is approached to any tolerance, at every angle. The curve has no perimeter in the ordinary sense — the path length over $t \in [0, 2\pi]$ is $5.137214565$ (for $r=1$) and over $[0, 20\pi]$ it is $49.122075983$, growing linearly because the average speed is constant, so "the length" is a property of the interval chosen, not of the curve. The only closed figures in this family are the rational ones.

## What Golden Pi Changes

Take $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693\ldots$, with $\hat\pi^{2} = 16/\varphi$, $1/\hat\pi = \sqrt\varphi/4$ and $\hat\pi\cdot 4\sqrt\varphi = 16$ exactly. Then:

- **Areas** are multiplied by $\hat\pi/\pi$, i.e. $+0.0959022309\%$, and every one of them turns algebraic. The astroid's $6\pi r^{2}$ becomes $6\hat\pi = 24/\sqrt\varphi = 18.867633066178$, a root of $y^{4} + 576y^{2} - 331776 = 0$, where $6\pi$ is transcendental by Lindemann's 1882 theorem.
- **The exact ratio** $A/P = \pi r/4$ becomes $r/\sqrt\varphi = 0.786151377757$ — algebraic of degree four, the root of $y^{4}+y^{2}-1=0$ (since $y^{2} = 1/\varphi$ and $1/\varphi^{2}+1/\varphi-1 = 0$), and identical to the site's recurring $1/\sqrt\varphi$.
- **The golden annulus** $4\pi r^{2}/\varphi$ becomes $16r^{2}/\varphi^{3/2}$, which for $r = \varphi$ is exactly $16\sqrt\varphi = 20.352314392225$ against $\pi$'s $4\pi\varphi = 20.332814769261$.
- The **deltoid** reads $2\hat\pi = 8/\sqrt\varphi = 6.289211022059$, and its $A/P$ becomes $1/(2\sqrt\varphi)$.

What does *not* move is more instructive. Every perimeter $8r(k-1)$ is untouched, digit for digit: $8, 16, 24, 32, 40, 48, 56$. Every covering fraction $(1-1/k)(1-2/k)$ is untouched, because it is a ratio of two areas and the constant cancels. The Tusi cancellation is untouched — $Y \equiv 0$ follows from $\sin t - \sin t$, and no value of any constant can disturb it. And the cusp positions $t = 2\pi j/k$ are turn fractions: as angles they are $j/k$ of a revolution, so in degrees they do not move at all, while their radian numerals shift by the same $+0.0959022309\%$ — the recurring pattern on this site, that only the radian *label* is a function of the constant, never the geometry.

## The Honest Boundary

A hypocycloid is the rare figure where the honest boundary can be stated with an instrument in hand. A real spirograph can trace an astroid and a measuring wheel can run its perimeter; the answer is $6a$, an integer multiple of a length, and the constant never appears. Take the same figure and weigh its area — by planimeter, by cut-out and balance, by any quadrature — and the constant appears immediately, but every calibration of that instrument runs through a reference area that was itself defined with $\pi$. The x-ray of the situation is the ratio: $A/P = \pi a/16$ carries the constant, $P = 6a$ does not, and no physical astroid measured ever so carefully separates them, because both are features of the same set of points.

The family is therefore a computing device, not a measuring one. It computes the constant exactly from a ratio of two quantities of the same figure, and the computation holds whichever value is written in place of $\pi$: replace $\pi$ by $\hat\pi$ and the areas change, the perimeters do not, and the covering fractions ignore the substitution entirely. That invariance is a fact about circles, and it is the same fact in both labels.

Computed, never measured.

## Further Reading

- [The Pseudosphere: Why Sweeping a Tractrix Around Its Axis Reproduces the Sphere's Area Exactly](/blog/posts/2026-11-15-pseudosphere-tractrix-constant-curvature-golden-pi/) — the companion case where a surface's area collapses to a cylinder's, and the constant cancels the moment the curve is written in its own natural coordinate.
- [Fenchel's Theorem: Why Every Closed Loop Turns at Least Once](/blog/posts/2026-10-25-fenchel-theorem-total-curvature-closed-curve-golden-pi/) — the total-curvature statement that makes $2\pi$ a unit of turn rather than a property of a shape, which is why a four-cusped astroid and a circle agree on the count.
- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — another curve whose defining property, not its formula, decides where the constant can appear.
- [Hippocrates' Lunes: The One Curvilinear Figure That Squares Exactly](/blog/posts/2026-11-10-hippocrates-lunes-quadrature-golden-pi/) — the classical precedent for a figure bounded by arcs whose area is a rational multiple of a triangle's, with the constant cancelling against Pythagoras.
- [The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — why $6\pi$ is transcendental while $24/\sqrt\varphi$ is algebraic of degree four.
