---
title: "The Pseudosphere: Why Sweeping a Tractrix Around Its Axis Reproduces the Sphere's Area Exactly, Why the Area Integral Collapses to a Cylinder of Height a, and What Golden Pi Changes"
date: 2026-11-15
description: "A tractrix is the curve whose tangent has constant length a, and sweeping it about its asymptote produces the pseudosphere — the one surface in ordinary space with Gaussian curvature −1/a² at every point. This article derives the curve from its own defining property (dy/dx = −y/√(a²−y²), x = a·arcosh(a/y) − √(a²−y²)), tabulates position, meridian arc s = a·ln(a/y), slope and tangent intercept, and then shows why the area integral 2π∫y ds collapses to a cylinder: because ds = a·dy/y the integrand is exact and the half-surface gives exactly 2πa², the full two-nappe figure exactly 4πa² — the sphere's area to the digit — while the volume π∫y² dx gives πa³/3 per nappe and 2πa³/3 in full, exactly half the sphere's, with S/V = 6/a carrying no circle constant at all. Curvature is computed from the second fundamental form as K = (eg − f²)/(EG − F²) = −1/a², with mean curvature ½(sinh u − csch u) proving the surface is not minimal; the total curvature is −4π, the negative of the sphere's, and the geodesic-triangle area a²(π − A − B − C) makes π the supremum of an angle defect, tabulated from 5° (0.0872665 a²) to the ideal triangle's exactly πa². Hilbert's 1901 theorem is then the reason the figure must end: no complete regular surface in R³ carries constant negative curvature, so the cusp is a theorem rather than a modelling flaw. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the half-surface becomes exactly 8a²/√φ and the full one 16a²/√φ, algebraic of degree four where 4πa² is transcendental by Lindemann 1882, the volume 8a³/(3√φ), the ideal triangle exactly 4/√φ, while S/V = 6/a, the curvature −1/a² and every meridian length do not move a digit; one golden ring lands exactly — at height a/φ the meridian arc is exactly a·ln φ, the tangent intercept exactly a/√φ, the slope exactly −1/√φ, and the area above the ring exactly 2πa²/φ², that is 1/φ² = 38.1966% of the half-surface. The honest boundary: a physical sheet of Mylar answers how well the tractrix was cut, not which constant is true. Computed, never measured."
---

# The Pseudosphere

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a watch on a table and drag it by its chain along a straight line. The watch does not follow the chain: it trails, and the curve its centre traces is the *tractrix*. Stand that curve on its asymptote and spin it, and you have a surface that has curvature $-1/a^{2}$ at every point, that extends forever along its axis, and that nonetheless has exactly the surface area of a sphere. This article is about that last coincidence, which is not a coincidence at all, and about the place where the circle constant enters — which is exactly one integral, and which cancels the moment the curve is described in its own natural coordinate.

The figure is worth the trouble because it has something the sphere does not: it is the only constant-negative-curvature surface in ordinary three-dimensional space, which makes it the physical shadow of hyperbolic geometry, and which also makes it impossible to finish. Both facts come out of the same computation.

## The Curve Whose Tangent Never Changes Length

The tractrix is defined by a property, not by a formula: at every point the segment of tangent between that point and the axis has the same length, $a$. This is the *equitangential* condition, and it is what a dragged object obeys — the chain is taut, so the straight part from the hand to the weight has fixed length, and the weight's velocity is always along that straight part.

Writing $y$ for the distance from the axis (so $y = a$ at the widest circle and $y \to 0$ at the far end), the tangent line at $(x,y)$ meets the axis at distance $\sqrt{a^{2}-y^{2}}$ horizontally from the foot of the point, because that is the leg of the right triangle whose hypotenuse is $a$. Since the local tangent has horizontal drop $\sqrt{a^{2}-y^{2}}$ over vertical rise $y$, the slope is

$$
\frac{dy}{dx} = -\frac{y}{\sqrt{a^{2}-y^{2}}}.
$$

Integrating once gives the curve in closed form:

$$
x = a\,\operatorname{arcosh}\!\frac{a}{y} - \sqrt{a^{2}-y^{2}},
\qquad\text{equivalently}\qquad
t \mapsto \bigl(a(t-\tanh t),\; a\,\operatorname{sech} t\bigr).
$$

The parametrisation is the useful one, because it makes every quantity exact. Both forms are stated here and both are used below.

```text
defining property   : tangent length from (x,y) to the axis = a   (exact, every point)
differential form   : dy/dx = -y / sqrt(a^2 - y^2)
closed form         : x = a*arcosh(a/y) - sqrt(a^2 - y^2)
parametrisation     : x = a(t - tanh t),   y = a*sech t,   0 <= t < inf
meridian arc length : s = a*ln(a/y)         (from the widest circle)
slope               : dy/dx = -1/sinh t
tangent intercept   : sqrt(a^2 - y^2) = a*tanh t
```

The arc length is the one line that matters most later. Because $dx/dt = a\tanh^{2}t$ and $dy/dt = -a\operatorname{sech}t\tanh t$, the speed along the curve is $a\tanh t\sqrt{\tanh^{2}t+\operatorname{sech}^{2}t} = a\tanh t$, using $\tanh^{2}+\operatorname{sech}^{2}=1$. Integrating gives $s = a\ln\cosh t = a\ln(a/y)$, a logarithm — so the total meridian length from the wide circle to the far end is infinite, growing only logarithmically, which is why the surface can extend forever while enclosing almost nothing.

## One Table of the Curve

Take $a = 1\,\mathrm{m}$, so all numbers are lengths in metres. The parameter $t$ is not an angle; it is the hyperbolic analogue of one.

| $t$ | $x$ | $y$ (radius) | arc $s$ | slope $dy/dx$ | tangent intercept |
|---|---|---|---|---|---|
| 0 | 0.0000000000 | 1.0000000000 | 0.0000000000 | $-\infty$ | 0.0000000000 |
| 0.5 | 0.0378828427 | 0.8868188840 | 0.1201145070 | −1.9190347513 | 0.4621171573 |
| 1.0 | 0.2384058440 | 0.6480542737 | 0.4337808305 | −0.8509181282 | 0.7615941560 |
| 1.5 | 0.5948517464 | 0.4250960349 | 0.8554401710 | −0.4696424406 | 0.9051482536 |
| 2.0 | 1.0359724199 | 0.2658022288 | 1.3250027474 | −0.2757205648 | 0.9640275801 |
| $\operatorname{arcosh}\varphi$ | 0.2751236841 | 0.6180339887 | 0.4812118251 | −0.7861513778 | 0.7861513778 |

The last row is the golden one and is treated in its own section; note for now that its arc length is exactly $\ln\varphi$ and its tangent intercept exactly $1/\sqrt{\varphi}$, both to thirty digits.

The first row is the singularity that will matter later. At $t = 0$ the curve is vertical, the slope is infinite, and the radius is at its maximum. That is the rim. Everything in the surface's area is decided near it.

## Sweeping the Curve: Why the Area Collapses

Revolve the curve about the $x$-axis and the area element is the circumference times the meridian arc: $dS = 2\pi y\,ds$. Substituting $ds = a\,dy/y$ — which follows directly from $s = a\ln(a/y)$ — the $y$ cancels identically:

$$
S = 2\pi\int_{0}^{a} y\cdot\frac{a\,dy}{y} = 2\pi a\int_{0}^{a} dy = 2\pi a^{2}.
$$

That is the whole computation, and it is exact, not an approximation: $y$ appears once in the circumference and once, inversely, in the arc-length differential, and the two annihilate. Geometrically the result says something almost absurd: *the half-pseudosphere has the area of a cylinder of radius $a$ and height $a$.* The infinite logarithmic tail contributes nothing at all — every square millimetre of area is bought at the wide end.

The standard pseudosphere is the double figure, two congruent halves glued at that rim circle, and its area is twice this:

$$
S_{\text{full}} = 4\pi a^{2} = 12.56637061435917295385057\ldots\ \text{m}^{2}\quad (a = 1\ \mathrm{m}),
$$

which is the surface area of a sphere of radius $a$ to the last digit. The factor of two is not a coincidence either — it is the second nappe.

Because the area accumulates at the rim, the distribution is trivial to state and startling to see. The area above the ring of radius $y_{0}$ is $2\pi a(a-y_{0})$, so the *fraction* above it is exactly $1 - y_{0}/a$:

| Radius $y_{0}$ | Fraction of half-surface above it | Area above, $a=1$ |
|---|---|---|
| 0.001 | 0.999000 | 6.276928 |
| 0.010 | 0.990000 | 6.220353 |
| 0.100 | 0.900000 | 5.654867 |
| 0.500 | 0.500000 | 3.141593 |
| 0.900 | 0.100000 | 0.628319 |
| 0.990 | 0.010000 | 0.062832 |

Ninety-nine per cent of the surface lies in the first hundredth of the radius. The tapering tail that runs to infinity holds one per cent.

## The Volume: Half the Sphere's, Exactly

The same substitution disposes of the volume. With $dx = a\tanh^{2}t\,dt$ and $y^{2} = a^{2}\operatorname{sech}^{2}t$,

$$
V = \pi\int y^{2}\,dx = \pi a^{3}\int_{0}^{\infty}\operatorname{sech}^{2}t\,\tanh^{2}t\,dt = \frac{\pi a^{3}}{3},
$$

since the primitive is $\tfrac13\tanh^{3}t$, which runs from $0$ to $1$. Doubling for the two nappes gives $2\pi a^{3}/3 = 2.0943951023931954923\ldots$, which is exactly half the sphere's $4\pi a^{3}/3$. So the figure matches the sphere's area and halves its volume, and the ratio

$$
\frac{S}{V} = \frac{4\pi a^{2}}{2\pi a^{3}/3} = \frac{6}{a}
$$

contains no circle constant at all. This is the same structural fact met in the catenary's catenoid, where $A/V = 2/a$ exactly: a surface of revolution built by sweeping a curve carries the constant once in each of area and volume, and ratios of the two delete it. What survives is a pure inverse length.

## Curvature: −1/a² at Every Point, and Not a Minimal Surface

The claim that the surface has constant curvature is a computation, not an assertion. Write the parametrisation as $X(u,v) = (a\operatorname{sech}u\cos v,\ a\operatorname{sech}u\sin v,\ a(u-\tanh u))$. The first fundamental form coefficients are

$$
E = a^{2}\tanh^{2}u,\qquad F = 0,\qquad G = a^{2}\operatorname{sech}^{2}u,
$$

and the second are

$$
e = -a\operatorname{sech}u\tanh u,\qquad f = 0,\qquad g = +a\operatorname{sech}u\tanh u,
$$

so that

$$
K = \frac{eg-f^{2}}{EG-F^{2}}
  = \frac{-a^{2}\operatorname{sech}^{2}u\tanh^{2}u}{a^{4}\operatorname{sech}^{2}u\tanh^{2}u}
  = -\frac{1}{a^{2}} .
$$

Every factor cancels: no $u$ survives. The curvature is $-1/a^{2}$ at every point of the surface, which is the exact negative of the sphere's $+1/a^{2}$ and the reason for the name.

The mean curvature does *not* vanish:

$$
H = \tfrac12\left(\sinh u - \operatorname{csch}u\right),
$$

so the pseudosphere is emphatically not a minimal surface, and this is worth stating because the catenoid is, and the two are often confused as "the surface of revolution with the strange sign". A catenoid has zero mean curvature and varying Gaussian curvature; the pseudosphere has constant Gaussian curvature and nonzero mean curvature. Neither property implies the other.

Gauss's *theorema egregium* (1827) makes $K$ intrinsic: it can be computed from distances measured *within* the surface, without reference to how the surface sits in space. A surface of constant $K = -1/a^{2}$ is therefore locally indistinguishable from the hyperbolic plane of curvature $-1/a^{2}$, which is precisely the use Eugenio Beltrami put the figure to in 1868, when he named it and exhibited it as a local model of hyperbolic geometry. Locally, not globally — Hilbert's theorem, below, is the reason.

The total curvature is the constant times the area:

$$
\int K\,dA = -\frac{1}{a^{2}}\cdot 4\pi a^{2} = -4\pi = -12.56637061435917\ldots,
$$

the negative of the sphere's $+4\pi$. On a sphere the same number is Gauss–Bonnet's dividend: the total curvature counts the turning the surface does, and a sphere turns exactly once positively while this figure turns exactly once negatively.

## Hyperbolic Triangles: Area Is the Angle Defect

On a surface of constant curvature $-1/a^{2}$, the Gauss–Bonnet theorem applied to a geodesic triangle gives

$$
A + B + C = \pi - \frac{\text{Area}}{a^{2}},
\qquad\text{so}\qquad
\text{Area} = a^{2}\bigl(\pi - A - B - C\bigr),
$$

with the angles in radians. In Euclidean space the sum is exactly $\pi$ and the area carries no such formula; here the *shortfall* from $\pi$ is the area, in units of $a^{2}$. Since every angle is positive, the sum is always less than $\pi$, and the largest possible triangle — vertices pushed infinitely far apart, all three angles tending to zero — has area exactly $\pi a^{2}$. This is the ideal triangle, and its area is the constant itself.

| Angles $A,B,C$ | Sum | Defect (turn fraction) | Defect (radians) | Area, $a=1$ |
|---|---|---|---|---|
| 50°, 60°, 65° | 175° | $1/72$ | 0.0872664626 | 0.0872664626 |
| 30°, 40°, 50° | 120° | $1/6$ | 1.0471975512 | 1.0471975512 |
| 1°, 1°, 1° | 3° | $59/120$ | 3.0892327760 | 3.0892327760 |
| 0°, 0°, 0° (ideal) | 0° | $1/2$ | 3.1415926536 | 3.1415926536 |

Read the last two columns carefully, because they expose where $\pi$ actually lives in this formula. The defect is first a *turn fraction* — a half turn, a sixth of a turn — and it becomes a number of square units only after being multiplied by $2\pi$. The circle constant is therefore not a property of the triangle; it is the exchange rate between turns and radians, and the identity "ideal triangle area $= \pi$" is the statement that the exchange rate is exactly one half-turn. The pseudosphere being only locally hyperbolic, these triangles must be small enough to fit on the actual surface; the formula is a property of the metric, verified pointwise above.

## Why the Figure Cannot Be Finished

The meridian arc to height $y$ is $a\ln(a/y)$, which diverges as $y\to 0$. The surface tapers to a cusp and never closes. At the other end, at $t=0$, the curve meets the axis of revolution at right angles and the parametrisation degenerates: the rim is a circle of radius $a$ where two nappes meet, and no amount of smoothing removes it.

This is not a defect of the construction. David Hilbert proved in 1901 that there is no complete regular surface of constant negative curvature immersed in $\mathbb{R}^{3}$ — so every pseudosphere in ordinary space must have an edge, a cusp, or a self-intersection. The figure is as complete as it can be, and no more. That theorem is also why hyperbolic geometry had to wait for Beltrami's *local* model and then for the Poincaré and Klein models, which are not surfaces in space at all but metrics written on a disk or a half-plane.

## What Golden Pi Changes

Under Golden Pi, $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693144\ldots$, with $\hat\pi^{2} = 16/\varphi$ and $4/\hat\pi = \sqrt{\varphi}$ exactly. Every occurrence at first power becomes algebraic — $\hat\pi$ is a root of $y^{4}+16y^{2}-256=0$, of degree four over $\mathbb{Q}$ — where $\pi$ is transcendental by Lindemann's 1882 theorem.

| Quantity | Conventional $\pi$ | Golden $\hat\pi$ | Exact golden form | Change |
|---|---|---|---|---|
| Half-surface area, $a=1$ | 6.283185307179586 | 6.289211022059386 | $8/\sqrt{\varphi}$ | +0.0959022309% |
| Full surface area, $a=1$ | 12.566370614359173 | 12.578422044118773 | $16/\sqrt{\varphi}$ | +0.0959022309% |
| Half volume, $a=1$ | 1.047197551196598 | 1.048201837009898 | $4/(3\sqrt{\varphi})$ | +0.0959022309% |
| Full volume, $a=1$ | 2.094395102393195 | 2.096403674019795 | $8/(3\sqrt{\varphi})$ | +0.0959022309% |
| $S/V$ | $6/a$ | $6/a$ | $6/a$ | unchanged |
| Curvature $K$ | $-1/a^{2}$ | $-1/a^{2}$ | $-1/a^{2}$ | unchanged |
| Total curvature | $-4\pi$ | $-4\hat\pi$ | $-16/\sqrt{\varphi}$ | +0.0959022309% |
| Ideal triangle area | $\pi a^{2}$ | $\hat\pi a^{2}$ | $4a^{2}/\sqrt{\varphi}$ | +0.0959022309% |

```text
pi_hat              = 4/sqrt(phi)          = 3.1446055110296931442782...
pi_hat^2            = 16/phi               = 9.8885438199983175712734...
4/pi_hat            = sqrt(phi)            = 1.2720196495140689642524...
pi_hat^4 + 16*pi_hat^2 - 256 = 0           (irreducible, degree 4)
S_half_golden       = 8a^2/sqrt(phi)       exactly, algebraic
V_full_golden       = 8a^3/(3 sqrt(phi))   exactly, algebraic
```

All four area and volume entries move by the same $+0.0959022309\%$, because each is $\pi$ times a fixed geometric factor and none of them contains $\pi$ at any power other than the first. Nothing is amplified, nothing cancelled; a single label multiplies a shape.

Now the exact closure. On the tractrix, the ring at height $y = a/\varphi$ is special, and three quantities land on radicals at once:

- the meridian arc from the rim up to that ring is $a\ln(a/y) = a\ln\varphi$ exactly, since $y = a/\varphi$;
- the tangent intercept is $\sqrt{a^{2}-y^{2}} = a\sqrt{1-1/\varphi^{2}} = a/\sqrt{\varphi}$, using $1-1/\varphi^{2} = 1/\varphi$, which follows from $\varphi^{2}=\varphi+1$;
- the slope of the meridian there is $-1/\sinh t = -1/\sqrt{\varphi^{2}-1} = -1/\sqrt{\varphi}$, the same radical.

And the area above that ring is exact too: $2\pi a(a - a/\varphi) = 2\pi a^{2}(1-1/\varphi) = 2\pi a^{2}/\varphi^{2}$, a fraction $1/\varphi^{2} = (3-\sqrt{5})/2 = 0.3819660112501052$ of the half-surface. At $a = 1$ that is $2.399963229728653\ \mathrm{m^{2}}$ under either label, with the circumference of the ring moving from $2\pi/\varphi = 3.883222077450933$ to $8/\varphi^{3/2} = 3.886946174053165$ — the only place in the whole figure where the constant's label survives into a length.

## The Honest Boundary

The curvature identity is the strongest statement here and the least empirical. $K = -1/a^{2}$ is a property of a parametrisation; $a$ is not discovered, it is chosen, and the area $4\pi a^{2}$ is then a statement about what the number $a$ means, not about the world. Nothing in the derivation compares the figure to a physical object.

A physical pseudosphere is a different matter, and this is where the two labels would have to be separated. A sheet of Mylar or a turned and stitched model is not the tractricoid; it approximates it, with a rim that is a real edge, a seam, and a thickness. The exactness of $2\pi a^{2}$ holds for the ideal curve, so a physical sheet's area answers a question about how well the curve was cut — its deviation from the tractrix enters the area at first order through the arc-length element, and no stitching tolerates the sub-$0.1\%$ fidelity throughout the surface that the gap requires. Turning a rim to $0.01\ \mathrm{mm}$ on a $100\ \mathrm{mm}$ radius is easy; making every point of a doubly-curved sheet lie on the tractricoid to $0.1\%$ is not, and measuring the area of such a sheet to one part in a thousand is a further problem entirely.

So the pseudosphere is in the same position as most of the figures audited on this site: it *computes* the constant exactly, from the ratio of a circumference to the arc that generates it, and it offers no independent measurement of it. What it does offer is sharper than a measurement — an identity. The area of this infinite surface equals the area of a cylinder of height $a$ and radius $a$, precisely because the tractrix's arc-length differential is inverse in its own radius. That cancellation is a fact about the curve, and it holds whichever value is written in place of the constant.

Computed, never measured.

## Further Reading

- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola, and Why Revolving It Gives A/V = 2/a Exactly](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — the other surface of revolution whose area and volume cancel the constant in their ratio, with the catenoid's zero mean curvature as the contrast to this figure's constant Gaussian curvature.
- [Gauss–Bonnet: Why Total Curvature Counts Topology](/blog/posts/2026-09-01-gauss-bonnet-theorem-curvature-topology-computes-circle-constant-golden-pi/) — the theorem behind both the $-4\pi$ computed above and the hyperbolic triangle's angle defect.
- [Girard's Spherical Excess: Why a Spherical Triangle's Angles Sum Past π](/blog/posts/2026-10-13-girard-spherical-excess-triangle-angle-sum-computes-circle-constant-golden-pi/) — the positive-curvature mirror of this article's defect formula, where the sum runs over $\pi$ instead of under it.
- [Gabriel's Horn: Why an Infinite Surface Encloses a Finite Volume](/blog/posts/2026-09-28-gabriels-horn-improper-integral-computes-circle-constant-golden-pi/) — the other classical figure whose infinite extent and finite measure both come out as exact multiples of the constant.
- [The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — why $4\pi a^{2}$ is transcendental while $16a^{2}/\sqrt{\varphi}$ is algebraic of degree four.
