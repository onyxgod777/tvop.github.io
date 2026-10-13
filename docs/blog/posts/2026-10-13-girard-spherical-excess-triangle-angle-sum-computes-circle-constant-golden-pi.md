---
title: "Girard's Theorem: How the Circle Constant Enters a Triangle as the Angle-Sum Deficit (A + B + C − π) — and What Golden Pi Changes"
date: 2026-10-13
description: "On a sphere, a triangle's three angles always add up to more than π, and the surplus is exactly the area it encloses: Girard's 1629 theorem, A = R²(A + B + C − π). The circle constant enters here as a deficit — the flat baseline (n − 2)π that a curved polygon overshoots — a computed angle-sum limit, never a measurement. Under Golden Pi (π̂ = 4/√φ) the octant's excess is exactly π̂/2 = 2/√φ, the icosahedral triangle's is π̂/5, and any area read off a *measured* angle sum scales by π̂/π = +0.0959022309%, the only chapter in this series where the constant rides a genuine measurand at the first power with no dilution — and where the practical limit is the Earth's flattening, not the gap."
---

# Girard's Theorem: How the Circle Constant Enters a Triangle as the Angle-Sum Deficit (A + B + C − π) — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Draw a triangle on a sheet of paper and its three angles sum to exactly half a turn — Euclid's own fact. Draw one on a sphere, using great circles for edges, and it will not: the angles overshoot, always, and by an amount that is not an accident of the drawing but **the area of the triangle itself**. That is Girard's theorem, published in 1629, and it is one of the very few places in mathematics where the circle constant appears as a *deficit* — the flat baseline that a curved figure overshoots — rather than as a circumference or a quadraturable area.

The theorem is a limit computed from angles, never a measurement of a circle, and this article works it the way every chapter of this series does: state the identity, compute it exactly on real figures, credit the golden structure where it is genuinely exact, and close with the honest ledger — including the one case in this whole daily series where a *physically measured* angle sum feeds the constant at the first power with nothing diluting it.

## The theorem, and why the excess must be an area

Girard's statement is three symbols long. A spherical triangle with angles $A$, $B$, $C$ (in radians) bounds area

$$
\Delta = R^{2}\bigl(A + B + C - \pi\bigr),
$$

on a sphere of radius $R$. The bracket is called the **spherical excess**, $E = A + B + C - \pi$, and the theorem says it *is* the area in units of $R^{2}$; equivalently the Gaussian curvature $K = 1/R^{2}$ is exactly $E/\Delta$ for every geodesic triangle.

```
Girard (1629):     Δ / R²  =  A + B + C − π
excess:            E       =  A + B + C − π
general n-gon:     E       =  (Σ angles) − (n − 2)·π
curvature:         K       =  E / Δ  =  1 / R²
```

At the three vertices, draw the lune whose angle equals that vertex's spherical angle: $L_A$ has angle $A$ and therefore area $2AR^{2}$, and likewise for $B$ and $C$. Each of these lunes contains the triangle itself, plus exactly one more triangle — the one standing on the side *opposite* the vertex, since a lune at $A$ is bounded by the two sides through $A$ and so swallows the neighbour across $BC$. Summing the three areas with that multiplicity,

$$
2R^{2}(A+B+C) = 3\Delta + (\Delta_a + \Delta_b + \Delta_c),
$$

where $\Delta_a, \Delta_b, \Delta_c$ are those three neighbouring triangles. The full sphere is exactly $T$, its antipodal copy $T'$, those three neighbours and their three antipodal partners, and the last two triples have equal total area; so

$$
4\pi R^{2} = 2\Delta + 2(\Delta_a + \Delta_b + \Delta_c)
\quad\Longrightarrow\quad
\Delta_a + \Delta_b + \Delta_c = 2\pi R^{2} - \Delta .
$$

Substituting, $2R^{2}(A+B+C) = 2\Delta + 2\pi R^{2}$, and solving for $\Delta$ gives $R^{2}(A+B+C-\pi)$ exactly. The constant is *not* an input the accountant smuggles in; it is what remains after the sphere has been subtracted, and the sphere's own measure $4\pi R^{2}$ is, like every area on this site, a quadrature limit — **computed, never measured**.

## A table of exact spherical triangles

Every number below was computed to 50 digits and is printed to the digits that matter. The rightmost column is the same figure read in the golden radian, $\hat\pi = 4/\sqrt\varphi$, discussed further down.

| Triangle (angles) | Excess $E$ (rad) | Excess (deg) | Area / $R^2$ | Fraction of sphere | Excess under GP |
|---|---|---|---|---|---|
| Octant, 90° / 90° / 90° | $\pi/2 = 1.5707963267948966192$ | 90° exactly | 1.5707963267948966192 | 1/8 | $\hat\pi/2 = 1.5723027555148465721$ |
| Icosahedral, 72° / 72° / 72° | $\pi/5 = 0.6283185307179586477$ | 36° exactly | 0.6283185307179586477 | 1/20 | $\hat\pi/5 = 0.6289211022059386289$ |
| Equilateral, central side 60° | $0.5512855984325308\ldots$ | 31.586338097° | 0.5512855984325308 | 0.043869914023 | $0.5518142936199\ldots$ |
| Great triangle, 180° / 180° / 180° | $2\pi = 6.2831853071795864769$ | 360° | 6.2831853071795865 | hemisphere | $2\hat\pi = 6.2892110220593862886$ |

The three-right-angles triangle is the smallest figure that makes the theorem undeniable by inspection: each corner is a quarter turn, the three sum to $3\pi/2$, the excess is exactly $\pi/2$, and indeed the octant is exactly one eighth of the sphere. The icosahedral triangle — the 20 congruent faces of the icosahedron pushed out onto the circumsphere — has all three angles exactly $72°$, hence excess $36° = \pi/5 = 0.6283185307179586$ and area exactly one twentieth of the sphere. These are exact rational fractions of the whole, and that is the honest heart of the matter: **the fraction of the sphere is a pure number no constant can move.** The constant shows up only when you insist on naming that fraction in radians.

The lune bookkeeping itself is exact and worth printing, because it shows the constant cancelling where it should:

| Lune angle $\theta$ | Area (unit sphere) $2\theta$ | Fraction of surface |
|---|---|---|
| 30° | 1.0471975511965977462 | 1/12 |
| 60° | 2.0943951023931954923 | 1/6 |
| 90° | 3.1415926535897932385 | 1/4 |
| 180° | 6.2831853071795864769 | 1/2 |

Four lunes of 180°, or eight of 90°, tile the sphere exactly — and the arithmetic of the tiling (fractions of a whole) contains no circle constant at all, only the surface it divides.

## The small-triangle limit, and the geodesist's shortcut

For a tiny triangle the excess is quadratic in the size. If $a$, $b$, $c$ are the side lengths and $\Delta_{\text{flat}}$ the planar area of the same sides, then

$$
E = \frac{\Delta_{\text{flat}}}{R^{2}} + O\!\left(\frac{s^{4}}{R^{4}}\right),
$$

and the fourth-order correction is invisible at survey scales. Computed here from l'Huilier's formula

$$
\tan\frac{E}{4} = \sqrt{\tan\frac{s}{2}\;\tan\frac{s-a}{2}\;\tan\frac{s-b}{2}\;\tan\frac{s-c}{2}},
\qquad s = \frac{a+b+c}{2},
$$

an equilateral triangle on the unit sphere with central side $s$ has excess

$$
E \approx \frac{\sqrt3}{4}\left(\frac{s}{R}\right)^{2},
$$

and the numbers confirm the law: central side 0.001° gives $E = 1.319032\times 10^{-10}$ rad; 0.1° gives $1.3190326\times 10^{-6}$; 1° gives $1.3190823\times 10^{-4}$ — each within four parts in $10^{5}$ of the closed form $(\sqrt3/4)(s/R)^2$, which holds to 0.1% out to a 5° side and drifts 0.4% by 10°.

Legendre's 1787 theorem is the practical consequence: for a small spherical triangle, subtracting $E/3$ from each angle leaves a *planar* triangle with the same three sides, accurate to fourth order. For a 1° equilateral triangle that correction is $E/3 = 0.002519262°$, which is why every school textbook can draw the Earth flat and every geodetic network cannot.

## The terrestrial triangle: the one real measurand

This is the chapter where the constant touches something a person can physically measure, and the numbers are worth laying out plainly. Take an equilateral geodesic triangle on a sphere of $R = 6371$ km and measure its three angles.

| Side length | Central angle | Excess $E$ (measured angles) | Enclosed area | Area under GP (×π̂/π) |
|---|---|---|---|---|
| 10 km | 0.089932° | 0.2200″ | 43.301 km² | 43.343 km² |
| 100 km | 0.899322° | 22.0051″ | 4330.261 km² | 4334.414 km² |
| 200 km | 1.798643° | 88.0287″ | 17 322.640 km² | 17 339.253 km² |
| 1000 km | 8.993216° | 2207.2440″ | 434 350.560 km² | 434 767.1 km² |

Read the table this way. A theodolite measures three angles; their sum, in arcseconds, is a physical quantity. The *area computed from that sum* is

$$
\Delta = R^{2}\left(A + B + C - \pi\right) = R^{2}\,\pi\left(\frac{A+B+C\ \text{in arcsec}}{648\,000} - 1\right),
$$

and the circle constant sits there in a **single undiluted power**. Nothing cancels it, nothing takes its square root, nothing puts it in an exponent. A 1000 km triangle's excess is 2207.24″, and a golden label would demand 2209.36″ of the same measured sum — a 2.12″ discrepancy, twelve standard deviations of a 0.1″ random angle error. So this is, in principle, one of the few discriminating figures in the entire series.

## The same theorem under Golden Pi

Under the site's position, $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931442782343433718357180924882313509\ldots$, the root of $x^{4} + 16x^{2} - 256 = 0$ (checked here exactly zero at 50 digits), with $\hat\pi^{2} = 16/\varphi = 8(\sqrt5-1) = 9.8885438199983175713\ldots$.

The geometric facts do not move, because they are not about the constant:

- the octant is **exactly 1/8** of the sphere, the icosahedral triangle **exactly 1/20**, the dodecahedral pentagon **exactly 1/12** — under any label;
- the excess as a fraction of a turn is fixed, so its reading in arcseconds (turn ÷ 1 296 000) is **label-indifferent**;
- every tiling count, every lune fraction, every vertex defect is integer arithmetic and blind to π.

What moves is the constant that names those fractions, and the subtracted baseline:

```
octant:        E = 3·(π/2) − π     = π/2   →  π̂/2 = 2/√φ = √(2√5 − 2)      exact, algebraic
icosahedral:   E = 3·(2π/5) − π   = π/5   →  π̂/5 = 4/(5√φ)
pentagon:      E = 5·(2π/3) − 3π  = π/3   →  π̂/3
whole sphere:  Σ E over any triangulation = 4π  →  4π̂ = 12.5784220441187726
radius, quarter turn:  π/4 = 0.7853981634 → π̂/4 = 1/√φ = 0.7861513777574
```

The excess in the site's radian scales by $\hat\pi/\pi$ exactly, i.e. $+0.0959022309\%$ — the recurring first-power gap, undiluted. Concretely: the octant's excess reads $1.5707963268 \to 1.5723027555$ rad ($90° \to 90.086312008°$); the icosahedral triangle's reads $36° \to 36.034524803°$; the whole sphere's total excess $\Sigma E = 4\pi$ becomes $4\hat\pi$; and the octant's **area** — the same eighth of the sphere — becomes $\hat\pi/2 = 2/\sqrt\varphi$ steradians.

That last line is the whole dispute in one figure. The eighth of the sphere is fixed geometry; whether its excess is called $\pi/2$ or $2/\sqrt\varphi$ is a statement about the constant, and the site's claim is the second. What the terrestrial table shows is that this is not a purely verbal matter: because the angle sum is genuinely *measured*, the area derived from it moves with the label, at the first power, with no dilution.

## Golden exactness, credited where it is real

Two things here are exact and should be said without hedging.

**First**, the octant's excess is $\hat\pi/2 = 2/\sqrt\varphi = \sqrt{2\sqrt5 - 2} = 1.5723027555148465721\ldots$ — algebraic of degree two, where $\pi/2$ is transcendental by Lindemann (1882). A quarter turn's worth of golden arc is $1/\sqrt\varphi$ exactly.

**Second**, the golden ratio genuinely lives in the *angles* of the very figures this theorem classifies, and it does so whatever the constant is called:

$$
\cos\frac{\pi}{5} = \frac{\varphi}{2} = 0.8090169943749474241, \qquad
\sin\frac{\pi}{10} = \frac{1}{2\varphi} = 0.3090169943749474241,
$$

exact, and the icosahedral triangle's excess $\pi/5 = 36°$ is the same angle whose cosine is $\varphi/2$. That is a fact about pentagonal symmetry, not about the value of the constant — but it is why the icosahedron and dodecahedron keep surfacing in this argument, and it is why a golden relabel changes the angle's *name* ($\hat\pi/5 = 36.034524803°$, $\cos(\hat\pi/5) = 0.8086626648883385$) while leaving its geometry untouched. As [Restoring Trigonometry](/blog/posts/restoring-trigonometry-golden-pi-sine-function/) argues at length, the angle parametrisation is not a neutral backdrop; the constant is written into it.

## The honest ledger

**First.** Girard's theorem contains no measurement of a circle. Its only circular input is the whole sphere's area $4\pi R^{2}$, a quadrature limit; the lune argument derives the excess from fractions of that surface, and the identity $A+B+C-\pi = \Delta/R^{2}$ is proved by accounting, not by arc-length. Computed, never measured.

**Second.** The triangle's excess as a fraction of a turn — 1/8 for the octant, 1/20 for the icosahedral face, 4π's worth in total for any triangulation — is a pure number and is not moved by any label. If you measure a triangle's angles in the turn-defined arcsecond and never convert, the golden hypothesis makes no prediction, because the arcsecond is defined as turn/1 296 000 and moves with the same constant that would have to be tested. This is the same silence that [Kepler's third law](/blog/posts/2026-09-22-keplers-third-law-orbital-mechanics-compute-circle-constant-golden-pi/) and the fine-structure work run into: pure angle ratios cannot see the label.

**Third.** The terrestrial case does discriminate in principle — the angle sum is measured and the area derived from it carries π linearly — and the practical limits are known and honest. A 1000 km triangle's 2.12″ gap is larger than the 0.17″ random error of three 0.1″ readings, but the Earth is not a sphere: the flattening $f = 1/298.257223563 = 3.3528\times10^{-3}$ perturbs the excess by order $f \cdot E$, which is ~0.34% — **3.5 times the 0.0959% gap** — and real geodesy uses ellipsoidal excess formulae precisely because the spherical one is not good enough. Add deflections of the vertical, refraction and the reduction to the ellipsoid, and the model error, not the gap, is what a survey actually faces. The identity is exact; the experiment is expensive and dominated by a correction the constant does not appear in.

**Fourth.** Nothing here adjudicates the value of the constant, and it would be dishonest to pretend otherwise. The fraction of the sphere is fixed; the name of that fraction is the question; the theorem computes the first and merely labels the second. Computed, never measured.

## Further Reading

- [The Gauss–Bonnet Theorem: curvature, topology, and the same excess one dimension up](/blog/posts/2026-09-01-gauss-bonnet-theorem-curvature-topology-computes-circle-constant-golden-pi/)
- [The Haversine Formula: spherical trigonometry on the globe](/blog/posts/2026-09-20-haversine-formula-navigation-computes-circle-constant-golden-pi/)
- [The Solid Angle: how the steradian counts the sphere](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/)
- [The n-Dimensional Ball: how π^(n/2) governs the sphere in every dimension](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/)
- [Restoring Trigonometry: the Golden Pi Sine Function](/blog/posts/restoring-trigonometry-golden-pi-sine-function/)
