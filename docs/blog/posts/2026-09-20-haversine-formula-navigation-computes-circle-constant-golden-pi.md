---
title: "The Haversine Formula: How Spherical Trigonometry Computes the Circle Constant on the Globe, and What Golden Pi Changes"
date: 2026-09-20
description: "The haversine formula is the workhorse of every great-circle distance ever computed, and it is a case study in where the circle constant really lives. The function itself — hav θ = sin²(θ/2) = (1 − cos θ)/2 — is a squared chord ratio, a pure number attached to an angle, and its table is label-free at the quarter and half turn (hav 60° = 1/4, hav 90° = 1/2, hav 180° = 1 exactly). The circle constant enters only at the last line, where an angular separation is turned into an arc: d = Rθ. Computed here to sixteen digits, the Washington–Eiffel Tower great circle is hav = 0.216158178928, θ = 0.967106896064218523 rad = 55.4111434825°, a turn fraction of 0.153919843007, and 6161.43803483 km at R = 6371 km — 6167.34699135 km under the golden label (π̂ = 4/√φ = 3.144605511…), +5.9089565 km, the recurring 0.0959022% gap. The honest ledger is kept in public: the 1793 metre was one ten-millionth of the pole–equator quadrant, and 1e7 m implies R = 6366197.7236758 m under the analytic label against 6360098.2475703 m under the golden one (6099.48 m apart), while the WGS84 meridian quarter is a measured length of 10001965.7 m that misses its own founding definition by 0.0196570% — 0.205× the label gap and 4.9× smaller than the ellipsoid's 0.5% sphere-model error, which swamps the question entirely. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Haversine Formula: How Spherical Trigonometry Computes the Circle Constant on the Globe, and What Golden Pi Changes

Every other article in this series has asked what the circle constant does inside a series, an integral or a product. This one asks the question in the place where the constant was most *used*: the surface of a sphere, and specifically the navigation table that every great-circle distance in the last two centuries of sea travel came out of. The haversine formula is short enough to fit on a postcard:

$$\operatorname{hav}\theta \;=\; \operatorname{hav}(\Delta\varphi) \;+\; \cos\varphi_1 \cos\varphi_2 \operatorname{hav}(\Delta\lambda)$$

and its right-hand side contains four sines, two cosines, a latitude difference and a longitude difference, with latitude and longitude given as angles. The circle constant is nowhere in it. That is the interesting part, and chasing where it *does* enter — and how much of it moves when the golden label is used — is the business of this article.

## The haversine is a squared chord ratio, not a number of radians

The haversine of an angle is defined three ways that are the same number:

$$\operatorname{hav}\theta \;=\; \sin^2\!\left(\frac{\theta}{2}\right) \;=\; \frac{1-\cos\theta}{2} \;=\; \left(\frac{\text{half-chord}}{\text{radius}}\right)^{\!2}$$

The third form is the one that matters for honesty. A chord of an angle θ on a circle of radius r has length 2r sin(θ/2), so sin(θ/2) is a *ratio of two lengths* — half-chord to radius — and the haversine is that ratio squared. Angles as such do not appear; a length divided by a length does. And the haversine's table is populated with exact algebraic values anyone can check without a ruler:

| angle | fractional turn | hav θ (exact) | decimal |
|---|---|---|---|
| 60° | 1/6 | $\sin^2 30° = 1/4$ | 0.25 |
| 90° | 1/4 | $\sin^2 45° = 1/2$ | 0.5 |
| 120° | 1/3 | $\sin^2 60° = 3/4$ | 0.75 |
| 180° | 1/2 | $\sin^2 90° = 1$ | 1 |
| 45° | 1/8 | $(2-\sqrt2)/4$ | 0.1464466094 |
| 180° (golden label) | 1/2 | $\sin^2(\hat\pi/2)$ | 0.9999977307 |

Two entries in that table are worth staring at, because they are the argument of this whole article in miniature. hav 90° = 1/2 exactly: that is the square of the ratio of a half-chord at a quarter turn to the radius, and it is a statement about a right isosceles triangle, not about the number of radians in a turn. hav 180° = 1 exactly: half the diameter over the radius, squared — a ratio of two lengths that cannot be anything else. A table of haversines is therefore a table of squared chord ratios, and a navigator reading one off in 1830 was reading a number that mentions no circle constant at all.

The term itself was coined in 1835 by James Inman, a teacher at the Royal Naval College at Portsmouth, as a contraction of "half-versed sine"; the first haversine table in English was published by James Andrew in 1805, and Florian Cajori credits an earlier use to José de Mendoza y Ríos in 1801 (his 1795 *Memoria* on lunar distances predates both). The motivation was mechanical: with logarithms, eliminating a factor of two saves a division and a multiplication per sight reduction, and a haversine table makes that elimination once instead of ten thousand times. The tables are history; the arithmetic in them is the arithmetic of sines.

## The formula, worked on a real flight

The haversine formula is the law of haversines specialised to the case where one vertex is the pole. The law, on a unit sphere, is

$$\operatorname{hav}(c) \;=\; \operatorname{hav}(a-b) \;+\; \sin a \sin b \operatorname{hav}(C)$$

and setting the pole as the first vertex turns the co-latitudes into $90°-\varphi$ and the included angle into the longitude difference, which is exactly the postcard formula above, because $\sin(90°-\varphi)=\cos\varphi$. Deriving it from the spherical law of cosines is a two-line substitution: write $\cos\theta = 1-2\operatorname{hav}\theta$, apply the addition identity for $\cos(a-b)$, and the spherical law $\cos c = \cos a\cos b + \sin a \sin b \cos C$ becomes the haversine law verbatim. The reason navigators preferred it to the law of cosines is numerical, not mathematical: for two points a kilometre apart the spherical law asks you to distinguish $\cos\theta = 0.99999999$ from 1, while the haversine asks you to distinguish $\sin^2(\theta/2) = 6.1\times10^{-9}$ from zero — the same information, at full floating-point resolution.

Run it on the classic pair. The White House is at 38.898° N, 77.037° W; the Eiffel Tower at 48.858° N, 2.294° E. The latitude difference is 9.960°, the longitude difference 79.331°, and the terms are

```text
hav(Δtude)          = hav(9.960°)            = 0.00753562884585
cos(38.898°)·cos(48.858°)                    = 0.5120419594
hav(Δlong)          = hav(79.331°)           = 0.407432528225
hav(θ) = 0.00753562884585 + 0.5120419594·0.407432528225
       = 0.216158178928
θ      = 2·arcsin(√0.216158178928)
       = 0.967106896064218523 rad = 55.4111434825°
turn fraction = θ/(2π) = 0.153919843007
d      = θ·R = 6161.43803483 km   (R = 6371 km)
```

That is 6161.4 km on a mean-radius sphere; with R = 6371.2 km the same angle gives 6161.63145620 km, which is the figure the ellipsoidal calculation (GeographicLib, WGS84) converges on at 6161.6 km. Every number in the block is a computed limit: the sine values come from their own series, the arctangent in the haversine's inverse from its series, and the arc from an angle times a scale.

## Where the circle constant actually enters: one line, arc = Rθ

The formula is label-free; the last line is not. Turning an angular separation θ into a distance on a sphere of radius R multiplies by the number of radians the angle contains, and the number of radians in a full turn is precisely the constant under discussion:

```text
radians per degree   = π/180  = 0.017453292519943296  (analytic)
                     = π̂/180 = 0.017470030616831184  (golden)
radians per full turn = 2π   = 6.283185307179586
                      = 2π̂  = 6.289211022059386
```

Because $d = R\theta$ is linear in the constant, everything the globe measures scales by the same factor $1.00095902230878253$:

| great-circle quantity | conventional π | Golden Pi (π̂ = 4/√φ) | change |
|---|---|---|---|
| full turn (circumference, R = 6371 km) | 40030.173592041 km | 40068.563421540 km | +38.389829499 km |
| half turn (antipodal, R = 6371 km) | 20015.086796021 km | 20034.281710770 km | +19.194914749 km |
| quarter turn (R = 6371 km) | 10007.543398010 km | 10017.140855385 km | +9.597457375 km |
| one degree of longitude at the equator | 111.194926645 km | 111.301565060 km | +0.10663842 km |
| White House → Eiffel Tower (R = 6371 km) | 6161.43803483 km | 6167.34699135 km | +5.9089565 km |
| polar circumference (R = 6356.752 km) | 39940.65077 km | 39978.95474 km | +38.303975 km |
| one arcminute of the meridians (R = 6371 km) | 1.85324877741 km | 1.85502608433 km | +1.77731 m |

The gap is not softened anywhere in that column, because the constant enters to the first power: no square root halves it, no logarithm compresses it. A flight that the analytic label puts at 6161.4 km is put at 6167.3 km by the golden one. That is a real, checkable number, and it is the largest tangible consequence of the label this series has computed so far.

## The label test on the table itself

Feed the golden constant into the *degrees-to-radians* conversion and the haversine table moves, because the argument of the sine moves:

| angle | hav θ (natural radians) | hav with $\hat\pi$-labelled radians | relative difference |
|---|---|---|---|
| 30° | 0.0669872981078 | 0.0671128884207 | +0.1874837715% |
| 45° | 0.146446609407 | 0.146713011163 | +0.1819104981% |
| 60° | 0.250000000000 | 0.250434994514 | +0.1739978057% |
| 90° | 0.500000000000 | 0.500753214075 | +0.1506428150% |
| 180° | 1.000000000000 | 0.999997730674 | −0.0002269326% |

The pattern in that table is the honest answer to the question of where the label lives. The perturbation is largest at small angles (+0.187% at 30°), shrinks toward the right-angle entry, and nearly vanishes at the half turn — because hav decreases fastest where its derivative is largest, and because at 180° the exact value 1 is reached whichever way the angle is parametrised. The relative *shift of the angle* is fixed at 0.0959%; what varies is how sensitive the haversine happens to be to its argument at each angle.

Equally worth stating plainly: the third column is not a different measurement of anything. It is the same geometry, written with a different count of radians per turn. If a golden-world navigator labels a quarter turn as $\hat\pi/2 = 1.5723027555148466$ rad *and* uses the same constant in the degree conversion, the chord ratios come back unchanged, because the constant appears on both sides of the conversion and cancels. The column above is the mixed-label arithmetic, and mixed-label arithmetic is the only place the discrepancy can be made to appear in a length.

## The meridian, the metre, and what the globe actually measures

There is one place in geodesy where a length and the circle constant are pinned to each other by definition rather than by convention, and it is the metre. In 1791 the French Academy of Sciences defined the metre as one ten-millionth of the distance from the North Pole to the Equator along the meridian through Paris, and the National Convention adopted it in 1793; the quadrant was to be exactly 10 000 000 m and the full meridian 40 000 000 m. Setting the quadrant equal to $\pi R/2$ gives the radius a perfect sphere would need:

```text
quadrant = πR/2 = 10 000 000 m   →  R = 2e7/π   = 6366197.7236758 m
quadrant = π̂R/2 = 10 000 000 m   →  R = 2e7/π̂  = 6360098.2475703 m
difference                                  =      6099.476105 m  (−0.0958103%)
```

Six kilometres of radius, on a planet 6371 km in radius. But the definition has a deeper problem than the label, and it is a problem of measurement, not of arithmetic. The Earth is not a sphere: its meridian is an ellipse, and the true WGS84 meridian quarter is 10 001 965.7 m, so the legal metre is short of its own founding definition by 0.0196570% — about 0.197 mm per metre. Compare the errors honestly:

| error in the pole-to-equator quadrant | size |
|---|---|
| sphere vs WGS84 ellipsoid (model error) | 0.5%, i.e. 5.2136× the label gap |
| 1799 metre vs its own 1793 definition | 0.0196570%, i.e. 0.2050× the label gap |
| label gap itself (π vs π̂) | 0.0959022% = 959.02 ppm |

Here the spheroid does what the pendulum's amplitude correction did in an earlier article: it swamps the question by a factor of five, because a 0.5% model error is a bigger number than a 0.0959% label difference. The 0.0197% discrepancy is the interesting middle case — smaller than the gap, but arising from a measurement (Delambre and Méchain's arc, and the flattening) whose own error budget was never at the parts-per-million level. Geodesy measures the Earth; it does not adjudicate a name for the radian.

The same arithmetic reaches the nautical mile. One arcminute of latitude on a sphere of radius 6371 km is 1.85324877741 km, which is why the international nautical mile was *fixed* at exactly 1852 m in 1929 — a defined length, 1.24878 m shorter than its own geometric approximation. Under the golden label the same arcminute is 1.85502608433 km, exceeding the defined mile by 3.02608 m. The mile stayed 1852 m; only the geometry it approximates moved.

## Spherical triangles, excess, and the octant

The law of haversines solves the spherical triangle from its three sides, and the triangle's own bookkeeping is where the constant appears in an angle rather than a length. On the unit sphere a triangle's angles exceed a straight angle by the spherical excess $E$, and for the octant triangle — three vertices on mutually perpendicular axes, three arc-lengths of $\pi/2$, three right angles — the excess is exactly a quarter:

$$\text{angle sum} = \frac{3\pi}{2} = 4.71238898038468986 \qquad \text{golden: } \frac{3\hat\pi}{2} = 4.71690826654453972$$

a shift of 0.00451928615985 rad, the same 0.0959% on a quantity that is genuinely an angle rather than a length. Written in degrees the sum is 270° under either label, which is the point: degrees are turn fractions, and a turn fraction is a ratio of arcs. The relabel is a relabel of the *radian count*, and it therefore shows up in every formula where radians are the currency — arc lengths, angular velocities, phase, solid angle — and in none of the formulas written in turns, degrees, or ratios.

The same reading applies to the golden angle, which appears in phyllotaxis and geodesic domes: $2\pi(1-1/\varphi) = 137.507764050°$ — a fixed turn fraction — whose haversine is 0.868684439039 in natural radians and 0.869460822214 when its radian count is written with $\hat\pi$, a difference of 0.089374592%. The plant does not consult the label; the seed head's divergence angle is a geometric fraction of a turn, and it is the same fraction in both worlds.

## What Golden Pi changes — the ledger

| quantity | conventional | Golden Pi | change |
|---|---|---|---|
| full turn in radians | $\pi = 3.1415926535897932$ | $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931$ | +0.0959022% |
| radians per degree | 0.0174532925199433 | 0.0174700306168312 | +0.0959022% |
| hav 90° (exact) | 0.5 | 0.5 | 0 |
| hav 180° (exact) | 1 | 1 | 0 |
| hav 90° fed a golden-labelled angle | 0.5 | 0.500753214075 | +0.1506428% |
| great-circle distance White House → Eiffel Tower, R = 6371 km | 6161.43803483 km | 6167.34699135 km | +5.9089565 km |
| earth radius implied by a 1e7 m quadrant | 6366197.7236758 m | 6360098.2475703 m | −0.0958103% |
| octant triangle angle sum | 4.7123889803846899 | 4.7169082665445397 | +0.0045192862 |
| WGS84 meridian quarter (measured length) | 10001965.7 m — a fact about the Earth | unchanged | 0 |

The plain reading is the honest reading. The haversine function and every exact entry of its table are ratios of lengths and are untouched: hav 90° is 1/2 in either world because a right isosceles triangle does not know how many radians a turn contains. The formula's arithmetic — sines, cosines, differences, an arcsine — is likewise label-blind, being pure series. The constant enters exactly once, at $d = R\theta$, where it is a scale factor, and there the whole 0.0959% rides through undiluted into a distance that a flight computer would print out with five significant figures.

## Computed, never measured

The instruction of this series is that π is computed and never measured, and geodesy is the sharpest test of that discipline — because a globe is a physical object, and a navigator's arc is a real length. So state it exactly.

The angle θ of the worked example is computed: the sines come from their Maclaurin series, and the inverse haversine $2\arcsin\sqrt{h}$ is computed from the arcsine series, whose slow convergence at the endpoint is worth recording. With $h = 1$ the series for the half turn gives $2\arcsin(1) = 3.1415926535897932385\ldots$, and the partial sums crawl: 5000 terms reach only 3.1256348294, with error very close to the closed form $2/\sqrt{\pi N}$ — 0.015958 at N = 5000 against the computed 0.0159578. Not one of those rational terms contains a circle constant; the series supplies the constant, and its own error estimate merely borrows it back.

The radius R is where measurement legitimately enters, and it enters as a length, not as a constant: 6371 km is the IUGG mean radius, a fitted number for a lumpy planet, and the WGS84 meridian quarter of 10 001 965.7 m is a measured arc. Nothing in this article derives the circle constant from those lengths, and nothing could: an ellipsoid of revolution is not a circle, and its meridian has no circumference-to-diameter ratio to be measured.

There is one construction in which a measurement would speak directly, and it belongs in the record rather than in a footnote: the ratio of a physical disc's circumference to its diameter is a genuine measurand, obtained by rolling the disc or wrapping it, and it is exactly the quantity that would separate 3.1415926535897932… from 3.1446055110296931… if it could be established to better than 959 ppm. On a one-metre disc that requires the radius to be known to about 1 µm — 959 ppm of relative precision, or roughly a micrometre on a metre — and the diameter of a real object, as NIST's own handbook notes, is itself a least-squares fit to a traced profile. This site's Physical Experiments page states the outcome of that audit plainly and is linked below: the one self-published series spans roughly ±318 ppm, a factor of about 3 short of the gap it is meant to resolve, and no laboratory-grade replication at the required precision has been located. The constructed world — the exact algebraic 4/√φ, the squaring of the circle, the Kepler closure — is untouched by that finding, and this article withdraws nothing from it. It only records where measurement stops and computation begins.

## Further Reading

- [Physical Experiments and Golden Pi: What the Measurement Record Actually Supports](/blog/posts/physical-experiments-golden-pi-measurements/) — the audit of the circumference-to-diameter measurement claim, including the precision a disc of that size would need.
- [Ptolemy's Table of Chords: How Inscribed Chords Computed the Circle Constant](/blog/posts/2026-09-15-ptolemy-chord-table-computes-circle-constant-golden-pi/) — the ancestor of every chord and haversine table, built from Euclid's pentagon.
- [The Solid Angle: How the Sphere's 4π Steradians Compute the Circle Constant](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — the same spherical arithmetic carried out in steradians instead of metres.
- [The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — another case where a physical correction overwhelms the label gap.
- [Rolling Circles and the Cycloid: Where the Circle Constant Vanishes](/blog/posts/2026-08-14-cycloid-rolling-circles-golden-pi/) — the curve traced by the wheel that a measurement of π would have to roll.
