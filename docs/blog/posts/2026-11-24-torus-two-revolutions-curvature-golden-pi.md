---
title: "The Torus: Why Its Area Is Exactly the Product of Two Circumferences, Why Its Total Curvature Is Zero and Its Volume Carries π Twice, and What Golden Pi Changes"
date: 2026-11-24
description: "A torus of ring radius R and tube radius r has area 4π²Rr — exactly the product of its two circumferences — and volume 2π²Rr², so the circle constant appears squared in both, while the ratio A/V = 2/r carries no constant at all. This article derives both by Pappus' centroid theorem as two sweeps, one per revolution, tabulates area, volume, and box-filling fraction for five tori, computes the Gauss curvature cos v/(r(R + r cos v)) with values exactly 1/(r(R+r)) on the outer equator and −1/(r(R−r)) on the inner one, shows the total curvature integrates to exactly zero because χ = 0 and that a band of height sin v₀ carries total curvature exactly 2π sin v₀, exhibits the golden torus R = φr whose curvatures are exactly 1/φ² and −φ, whose hole-to-outer radius ratio is exactly φ³, and whose area and volume under Golden Pi are exactly 64r² and 32r³ — an exact square and an exact cube — plus the flat torus, where the constant vanishes entirely."
---

# The Torus

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a bicycle inner tube and ask two questions about it: how much rubber is in its skin, and how much air is in its body. The answers are

$$
A = 4\pi^{2}Rr, \qquad V = 2\pi^{2}Rr^{2},
$$

where $R$ is the ring radius — the distance from the axis of the wheel to the middle of the tube — and $r$ is the tube's own radius. Both formulas carry the circle constant **squared**, and that squared appearance is the most interesting thing about them, because a torus is the one elementary surface on which two *independent* revolutions meet: the sweep of a circle around an axis, and the circular cross-section of the thing being swept.

Written as products, the formulas say something sharper:

$$
A = (2\pi R)(2\pi r) = C_R\,C_r, \qquad V = (2\pi R)(\pi r^{2}) = C_R \cdot A_{\text{tube}}.
$$

The surface area of a torus is *exactly the product of its two circumferences*. Not approximately: exactly, for every $R$ and every $r$. The volume is the ring circle's length times the cross-section's area. And the ratio of the two headline numbers,

$$
\frac{A}{V} = \frac{4\pi^{2}Rr}{2\pi^{2}Rr^{2}} = \frac{2}{r},
$$

holds no circle constant at all and does not depend on $R$ — stretch the ring as wide as you like and the rubber-to-air ratio never moves. That is the pattern this blog keeps finding: the constant enters every *turn count*, and cancels from every *ratio of turns*.

## Pappus: One π per Revolution

The derivation is Pappus of Alexandria's centroid theorem, from Book VII of the *Collection*: a plane figure revolved about an external axis sweeps a solid of volume $V = A\cdot 2\pi\bar{x}$, and its boundary sweeps a surface of area $A = s\cdot 2\pi\bar{x}$, where $\bar{x}$ is the centroid's distance from the axis and $s$ the boundary's length.

Apply it to a disk of radius $r$ whose centre sits at distance $R$ from the axis. The disk's area is $\pi r^{2}$, its centroid travels a circle of length $2\pi R$, so

$$
V = \pi r^{2}\cdot 2\pi R = 2\pi^{2}Rr^{2}.
$$

The boundary is a circle of length $2\pi r$, its centroid again at $R$, so

$$
A = 2\pi r \cdot 2\pi R = 4\pi^{2}Rr.
$$

Nothing else is needed, and nothing else is available: the torus is the simplest surface whose every property follows from two circles. Each factor of $\pi$ is the same object — the conversion of *one revolution* into radians — and there are two revolutions in the construction, so there are two factors. There is no third source.

## The Numbers, Tabulated

For $r = 1$ and the ring radius running from a spindle torus through the horn to a thin ring:

| $R$ | shape | volume $2\pi^{2}R$ | area $4\pi^{2}R$ | $A/V$ | fraction of bounding box |
|---|---|---|---|---|---|
| 0.5 | spindle (self-intersecting) | 9.8696044011 | 19.7392088022 | 2 | 0.5483113556 |
| 1.0 | horn | 19.7392088022 | 39.4784176044 | 2 | 0.6168502751 |
| $\varphi = 1.6180340$ | golden ring | 31.9387107530 | 63.8774215059 | 2 | 0.5824743874 |
| 3.0 | ring | 59.2176264065 | 118.4352528131 | 2 | 0.4626377063 |
| 10.0 | thin ring | 197.3920880218 | 394.7841760436 | 2 | 0.2039174463 |

Two columns are constant-free. $A/V = 2/r$ is $2$ down every row of this table, exactly, because both formulas carry $R$ to the first power and $R$ divides out. The box fraction $V/\bigl(2(R+r)\bigr)^{2}(2r)$ peaks at the horn torus, at $\pi^{2}/16 = 0.6168502751$, and decays like $1/R$ for a thin ring — the horn is the fattest torus that fits inside its own bounding box, which is the geometric reason a doughnut of equal hole and tube fills its box best.

The degenerate cases are worth naming, because they show what the formulas are made of. At $R = r$ the hole closes to a point — the **horn torus** — and the inner equator has shrunk to zero radius while the outer equator has grown to $4r$. At $R < r$ the tube swallows the axis and the surface passes through itself — the **spindle torus** — and the volume integral, taken over the swept region with multiplicity, is still $2\pi^{2}Rr^{2}$. The number $A/V = 2/r$ does not care; only the topology of what you are counting does.

## Curvature: Where the Constant Cancels Completely

Parameterise the torus with the angle $u$ around the axis and $v$ around the tube:

$$
\mathbf{x}(u,v) = \bigl((R + r\cos v)\cos u,\ (R + r\cos v)\sin u,\ r\sin v\bigr).
$$

The principal curvatures are $\kappa_1 = 1/r$ (the tube's own bend, constant everywhere) and $\kappa_2 = \cos v/(R + r\cos v)$ (the bend of the parallel circle). Gauss curvature is their product:

$$
K = \frac{\cos v}{r\,(R + r\cos v)}.
$$

Its extremes are exact:

$$
K_{\text{outer}} = +\frac{1}{r(R+r)}, \qquad K_{\text{inner}} = -\frac{1}{r(R-r)}.
$$

For $R = 3$, $r = 1$ that is $+0.25$ on the outside equator and $-0.5$ on the inside — the inner side curves twice as hard and in the opposite sense, and at $R = r$ the inner value diverges, because the inner equator has collapsed to a point. This is genuinely computed, not assumed: substituting the first and second fundamental forms into $K = (eg - f^{2})/(EG - F^{2})$ cancels every $R$ and leaves the expression above exactly.

Now integrate. The area element is $r(R + r\cos v)\,du\,dv$, so

$$
\oint K\,dA = \int_0^{2\pi}\!\!\int_0^{2\pi} \frac{\cos v}{r(R+r\cos v)}\, r(R+r\cos v)\,du\,dv = 2\pi\cdot\bigl[\sin v\bigr]_0^{2\pi} = 0.
$$

The constant cancels out of the integrand *before* the integration, and the total curvature of a torus is exactly zero — which is Gauss–Bonnet with $\chi = 2 - 2g = 0$ for genus one. The usual statement of the theorem,

$$
\oint K\,dA + \oint k_g\,ds = 2\pi\chi,
$$

puts the constant on one side and the topology on the other. Divide by $2\pi$:

$$
\frac{1}{2\pi}\Bigl(\oint K\,dA + \oint k_g\,ds\Bigr) = \chi = 0.
$$

The left side is a pure number, a count of handles. No numeral for the circle constant survives anywhere in it.

Take a band instead of the whole surface — everything from the outer equator up to tube angle $v_0$ — and the same integral gives

$$
\int_0^{v_0}\!\!\int_0^{2\pi} K\,dA = 2\pi\sin v_0,
$$

which is the only place in this article where the constant appears alone, at the first power. Choose the band so that $\sin v_0 = 1/\varphi$, that is $v_0 = \arcsin(1/\varphi) = 38.1727076270°$, and the total curvature of that band is exactly $2\pi/\varphi = 3.8832220775$. For $R = 3$, $r = 1$ that band holds $13.88230204\%$ of the surface area — $16.4415395174$ of $118.4352528131$ — a fraction computed with no constant in it at all.

## Four Circles Through Every Point

There is a fact about tori that no formula prepares you for. Through any point of a torus pass **four** circles:

- the **tube circle** of radius $r$, the cross-section the point sits on;
- the **parallel** circle of radius $R + r\cos v$, cut by the horizontal plane through the point;
- and two **Villarceau circles**, each of radius $R$ exactly, lying in planes that are bitangent to the tube.

The two Villarceau circles are the torus's quiet joke: the surface built from circles of radius $r$ around a ring of radius $R$ also carries, at every single point, two circles of radius $R$ — the ring's own radius — and they are not the parallels. For the golden torus the count is exact and pleasing: at the tube angle where $\sin v_0 = 1/\varphi$ (so $\cos v_0 = 1/\sqrt{\varphi} = 0.7861513778$), the parallel through that point has radius $R + r\cos v_0 = \varphi + 1/\sqrt{\varphi} = 2.4041853665\,r$, while the two Villarceau circles through it both have radius exactly $\varphi\,r$.

## The Flat Torus: The Constant Disappears Entirely

Take a rectangle of sides $a$ and $b$ and glue opposite edges. The result is a torus — topologically the same surface, genus one — and it is *flat*: $K = 0$ everywhere, area exactly $ab$, no constant anywhere. Roll it out and it is the plane with a lattice of translations.

This is the cleanest possible demonstration of where the constant in $4\pi^{2}Rr$ comes from: it comes from the **embedding**, not from the surface. A compact flat surface cannot be immersed isometrically in three-dimensional Euclidean space at all (Hilbert's theorem on complete flat surfaces: the only ones in $\mathbb{R}^{3}$ are cylinders). To see a flat torus you need four dimensions, or the Clifford torus inside $S^{3}$, where the two principal curvatures are $+1/R_c$ and $-1/R_c$ and the Gauss curvature is again exactly zero. Every factor of $\pi$ in the doughnut formula is being charged by the fact that this particular torus has to bend to fit in the space we can hold it in.

## Why π Appears Squared

So the $ \pi^{2}$ in $A = 4\pi^{2}Rr$ is not a deep fact about tori; it is two independent bookkeeping conventions multiplied:

1. the ring circle's length is $2\pi R$ — one revolution, straightening a line;
2. the tube circle's length is $2\pi r$ and its area is $\pi r^{2}$ — one revolution, metering a second circle.

Multiply two quantities each of which carries one factor of the constant and you get two factors. This is also why the box fraction, the $A/V$ ratio, every band fraction, every curvature and the total curvature are constant-free: they are ratios in which the same two factors cancel.

## What Golden Pi Changes

Golden Pi is the reading $\hat{\pi} = 4/\sqrt{\varphi} = 3.1446055110\ldots$, with $\varphi = (1+\sqrt5)/2$. Its square is exactly algebraic:

$$
\hat{\pi}^{2} = \frac{16}{\varphi} = 9.8885438200, \qquad \pi^{2} = 9.8696044011,
$$

a shift of $+0.1918964341\%$ — twice the $0.0959022309\%$ label gap, because the constant is squared.

| quantity | conventional | Golden Pi | shift |
|---|---|---|---|
| $4\pi^{2}$ | 39.4784176044 | $64/\varphi = 39.5541752800$ | +0.1918964341% |
| $2\pi^{2}$ | 19.7392088022 | $32/\varphi = 19.7770876400$ | +0.1918964341% |
| area, $R=3$, $r=1$ | 118.4352528131 | $192/\varphi = 118.6625258400$ | +0.1918964341% |
| volume, $R=3$, $r=1$ | 59.2176264065 | $96/\varphi = 59.3312629200$ | +0.1918964341% |

Every entry moves by the same factor, because every entry is $\hat{\pi}^{2}$ times a fixed algebraic number — a pure power, so one percentage for all.

Now set the ring radius to the golden ratio, $R = \varphi r$. Conventionally,

$$
A = 4\pi^{2}\varphi r^{2} = 63.8774215059\,r^{2}, \qquad V = 2\pi^{2}\varphi r^{3} = 31.9387107530\,r^{3}.
$$

Under Golden Pi the same expressions become exact:

$$
A = \frac{16}{\varphi}\cdot\varphi\cdot 4r^{2} = 64\,r^{2}, \qquad V = \frac{16}{\varphi}\cdot\varphi\cdot 2r^{3} = 32\,r^{3}.
$$

That is $64r^{2} = (8r)^{2}$ — a perfect square — and $32r^{3}$, a rational multiple of a cube. Not approximately: the four factors of the surface area collapse in pairs, and the area of the golden torus is the area of a square of side $8r$, while the conventional reading of the same torus is transcendental by Lindemann's theorem, since $\pi^{2}$ is irrational whenever $\pi$ is. The same collapse is visible in the circumference product, where the radicals cancel:

$$
C_R\,C_r = \Bigl(2\hat{\pi}\varphi r\Bigr)\Bigl(2\hat{\pi} r\Bigr) = 8\sqrt{\varphi}\,r \cdot \frac{8}{\sqrt{\varphi}}\,r = 64\,r^{2}.
$$

Two mutually reciprocal radicals, one product, no constant left.

The golden torus is exact in its curvatures too — and these need no constant at all, so no label can touch them:

$$
K_{\text{outer}} = \frac{1}{r(R+r)} = \frac{1}{\varphi^{2}r^{2}} = 0.3819660113\,r^{-2}, \qquad K_{\text{inner}} = -\frac{1}{r(R-r)} = -\frac{\varphi}{r^{2}} = -1.6180339887\,r^{-2}.
$$

Its hole radius is $R - r = r/\varphi = 0.6180339887\,r$ and its outer radius is $R + r = \varphi^{2}r = 2.6180339887\,r$, so the outer-to-hole ratio is exactly $\varphi^{3} = 4.2360679775$: the tube sits in the annulus between $r/\varphi$ and $\varphi r$, whose radii multiply to $r^{2}$. Every one of those statements holds under either label, which is the point — the embedding's shape is arithmetic, and only the metering of its revolutions is a convention.

## The Honest Boundary

Four limits belong in print.

*A torus's numbers are computed, never measured.* Both $A$ and $V$ follow from $R$ and $r$ by Pappus' theorem, and the surface itself is generated by two circles. A pycnometer on a machined ring would return the volume of that ring's interior — a fact about the metal, not about the constant — and it would return the conventional numeral, because the interior of a body in space is what it is. The golden value is a claim about the exact construction of the circle, in particular the Kepler-triangle construction in which $r = \varphi^{1/4}$ yields an area of exactly $4$; it is not a claim that a doughnut holds more air.

*The $-0.19\%$ is twice the gap only because the constant is squared.* Any surface with two independent revolutions will show a doubled shift and nothing more. That is bookkeeping consistency, not evidence.

*The curvature results are label-independent and therefore not evidence either.* $K = 0$ in total, $K_{\text{outer}} = 1/\varphi^{2}$, $K_{\text{inner}} = -\varphi$, the $\varphi^{3}$ radius ratio, the $13.88230204\%$ band fraction — none of these contains a circle constant, so none can arbitrate one.

*The Villarceau circles are a theorem, not a measurement.* That every point of a torus lies on two circles of radius $R$ is a classical fact about bitangent planes; it is quoted here because it is beautiful, and it is true under any value of the constant.

What remains is the honest summary: on the torus the constant appears exactly twice, once for each revolution of the construction, and it cancels from every ratio the surface produces. Under Golden Pi the two factors become $64/\varphi$ and $32/\varphi$, and the golden torus's area and volume land on the integers $64$ and $32$ in units of $r^{2}$ and $r^{3}$ — an exact square and an exact cube, where the conventional reading leaves a transcendental decimal a fifth of a percent away.

Computed, never measured.

## Further Reading

- [The Hat-Box Theorem: Why Projecting a Sphere onto Its Circumscribed Cylinder Preserves Area Exactly](/blog/posts/2026-11-20-archimedes-hat-box-theorem-sphere-cylinder-area-golden-pi/) — the other great area-preservation result, where a single $\pi$ survives and a whole family of band areas does not move.
- [The Pseudosphere: Why Sweeping a Tractrix Around Its Axis Reproduces the Sphere's Area Exactly](/blog/posts/2026-11-15-pseudosphere-tractrix-constant-curvature-golden-pi/) — the opposite curvature story: constant negative $K$ instead of constant zero total.
- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — the surface of revolution whose $A/V$ ratio also drops the constant entirely.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — what happens when the cross-section is not a circle and no elementary closure exists.
- [The Cardioid: Why Its Perimeter Is Exactly 8a and Holds No Circle Constant](/blog/posts/2026-11-23-cardioid-exact-perimeter-8a-caustic-golden-pi/) — length constant-free, area constant-bearing, the same split the torus shows in two dimensions at once.
