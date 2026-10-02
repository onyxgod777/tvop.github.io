---
title: "Hippocrates' Lunes: How the First Quadrature of a Curved Figure Computes the Circle Constant — and Cancels It — and What Golden Pi Changes"
date: 2026-10-02
description: "Around 430 BC Hippocrates of Chios found the first exact area of a figure with a curved boundary, and the answer was a plain rational number: each lune between a leg-semicircle and the hypotenuse-semicircle of a right isosceles triangle has area exactly c²/8, so the two lunes together equal the triangle, c²/4. The circle constant appears in every intermediate step — πc²/8 for the big semicircle, πc²/16 for each small one, πc²/16 − c²/8 for each circular segment — and cancels identically from the difference, because the same computed limit stands on both sides. This article does the arithmetic in the open for c = 1: big semicircle π/8 = 0.39269908169872415481, each segment π/16 − 1/8 = 0.07134954084936207740, each lune π/16 − (π/16 − 1/8) = 1/8 = 0.12500000000000000000 exactly, two lunes = 1/4 = the triangle, and the square equal in area to a lune has side 1/(2√2) — exactly the small semicircle's radius. The constant is computed, never measured: it enters as the full-turn limit of the semicircle formula, the same limit as 4·arctan 1 = 3.14159265358979323846. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the quadrature does not move — the constant still cancels, so the lune is 1/8 and the triangle 1/4 under either label — while the absolute areas shift by the recurring 0.0959022309% (π/8 → π̂/8 = 0.39307568887871164303) and the segments, which carry the constant beside a subtracted rational, shift by 0.2639170312%; the honest golden rows are credited: a circle of radius φ^{1/4} = 1.1278384855616822603 has area exactly 4 under Golden Pi (standard π gives 3.99616758613526266670), and the square equal in area to that circle has side φ^{−1/4} = 0.88665177931216225923, a constructible root of degree four, where the conventional side √π/2 = 0.88622692545275801365 is transcendental (Lindemann, 1882). Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Hippocrates' Lunes: How the First Quadrature of a Curved Figure Computes the Circle Constant — and Cancels It — and What Golden Pi Changes

Sometime around 430 BC, Hippocrates of Chios — the same Hippocrates who wrote the first systematic Greek textbook of geometry, now lost — drew a right isosceles triangle inside a semicircle and asked what the crescent-shaped slivers left outside it measured. The answer was a plain rational number. For a triangle on a hypotenuse of length $c$, the two crescents ("lunes", from *luna*, moon) together have area exactly $c^2/4$: the triangle's own area, with no circle constant in it anywhere.

That is the first exact quadrature of a figure bounded by a curve in the historical record, and it is also the sharpest place in this whole series to ask **where** the circle constant lives. It appears in every intermediate step of the computation — the big semicircle is $\pi c^2/8$, each small one $\pi c^2/16$, each circular segment $\pi c^2/16 - c^2/8$ — and then it disappears from the difference, because the *same* constant stands on both sides of the subtraction. A lune is squarable, exactly, because the constant cancels.

And it is computed, never measured. Every length in the figure is a ratio; the constant enters once, as the full-turn limit of the semicircle formula, evaluated below as $4\arctan 1 = 3.14159265358979323846\ldots$. Nothing in the construction is a physical measurement of anything.

## The figure: one right triangle, three semicircles

Take a right isosceles triangle $ABC$ with the right angle at $C$ and hypotenuse $AB = c$. Each leg is

$$AC = BC = \frac{c}{\sqrt{2}}.$$

Draw the semicircle on the hypotenuse; by Thales' theorem it passes through $C$. Now draw a semicircle outward on each leg. The two regions caught between a leg-semicircle and the arc of the hypotenuse-semicircle are the lunes.

The area of a semicircle of radius $r$ is $\tfrac12\pi r^2$ — a computed quantity, the limit of inscribed polygons, not the result of measuring a curve. The triangle's area is pure rational geometry:

$$[\,ABC\,] = \frac12\cdot\frac{c}{\sqrt2}\cdot\frac{c}{\sqrt2} = \frac{c^2}{4}.$$

That is the number the whole construction is heading for, and it contains no constant at all.

## Where the constant enters — and why it is computed

The single fact that makes the quadrature work is an identity between three semicircle areas. Writing each small radius as $c/(2\sqrt2)$ and the big one as $c/2$:

$$\tfrac12\pi\left(\frac{c}{2\sqrt2}\right)^2 + \tfrac12\pi\left(\frac{c}{2\sqrt2}\right)^2 = \frac{\pi}{16}c^2 + \frac{\pi}{16}c^2 = \frac{\pi}{8}c^2 = \frac12\pi\left(\frac{c}{2}\right)^2.$$

The two semicircles on the legs together equal the semicircle on the hypotenuse. Equivalently, using Pythagoras ($AC^2 + BC^2 = c^2$):

$$\frac\pi8\big(AC^2 + BC^2\big) = \frac\pi8\,c^2.$$

The constant enters once, as a common factor, and by Pythagoras the geometric part balances. This is the whole trick of the lune, and it is a fact about the factor $\pi/8$, not about the number $3.14159\ldots$ that $\pi$ happens to denote.

Where does that factor come from? From the semicircle area $\tfrac12\pi r^2$, which is the constant *times* a rational function of lengths. And the constant itself is a computed limit — the value that Archimedes' polygon exhaustion, or the arctangent series, or any other exact procedure converges to:

$$4\arctan 1 = 4\sum_{k=0}^{\infty}\frac{(-1)^{k}}{2k+1} = 3.14159265358979323846\ldots$$

No instrument appears in that sum. The three semicircle areas in the figure are therefore computed, never measured.

## The quadrature, computed to the last digit

Set $c = 1$ for the table. The circular segment of the big semicircle cut off by a leg is the region between a chord and an arc, and it needs the angle that chord subtends. A leg is a chord of length $1/\sqrt2$ in a circle of radius $R = 1/2$, so it subtends the full angle

$$\theta = 2\arcsin\!\frac{1/\sqrt2}{2R} = 2\arcsin\frac{1}{\sqrt2} = 2\cdot\frac{\pi}{4} = \frac{\pi}{2},$$

a right angle — as it must be, since the leg is a side of a right isosceles triangle whose circumcircle has $AB$ as diameter. The segment area is $R^2(\theta-\sin\theta)/2$:

| quantity | exact form | value ($c = 1$) |
|---|---|---|
| big semicircle on $AB$ | $\pi c^2/8$ | $0.39269908169872415481$ |
| one small semicircle on a leg | $\pi c^2/16$ | $0.19634954084936207740$ |
| one segment of the big circle | $\pi c^2/16 - c^2/8$ | $0.07134954084936207740$ |
| one lune | $\pi c^2/16 - (\pi c^2/16 - c^2/8)$ | $0.12500000000000000000$ |
| two lunes | $c^2/8 + c^2/8$ | $0.25000000000000000000$ |
| the triangle | $c^2/4$ | $0.25000000000000000000$ |

Read the fourth row carefully. One lune is a small semicircle ($\pi c^2/16$) minus the segment of the big circle inside it ($\pi c^2/16 - c^2/8$). The $\pi c^2/16$ cancels exactly:

$$\text{lune} = \frac{\pi c^2}{16} - \frac{\pi c^2}{16} + \frac{c^2}{8} = \frac{c^2}{8}.$$

Each lune has area $c^2/8$; the pair is $c^2/4$, which is the triangle. The circle constant was present in both terms and is gone from the answer. This is not an approximation to $c^2/4$; it is $c^2/4$ exactly, because the same computed constant was subtracted from itself.

There is a clean geometric stowaway in that result. The square equal in area to one lune has side

$$\sqrt{c^2/8} = \frac{c}{2\sqrt2},$$

which is precisely the radius of the small semicircle on each leg. The lune is squared by the same length that draws half of it — a constructible length, since $c/(2\sqrt2)$ needs only a square root.

## What Golden Pi changes

The site's constant is $\hat\pi = 4/\sqrt\varphi = 3.14460551102969314428\ldots$, with $\varphi = (1+\sqrt5)/2$ and $\hat\pi$ a root of $x^4 + 16x^2 - 256 = 0$. Put it into the figure and ask what moves.

The **quadrature does not move at all**. The cancellation above used no numerical value of the constant — only that the same constant multiplies both the semicircle on a leg and the segment of the big circle. Under Golden Pi those factors are still equal, so the lune is still $c^2/8$ and the two lunes are still exactly the triangle $c^2/4$. The result is label-blind: it is a rational area, and no value of the constant, golden or conventional, can change it.

What does move is every **absolute** area, since each carries one power of the constant. Because $\hat\pi/\pi = 1.000959022308782526$, areas scale by the recurring $0.0959022309\%$ gap — except where a subtracted rational sits beside the constant:

| quantity | standard $\pi$ | Golden $\hat\pi$ | shift |
|---|---|---|---|
| big semicircle | $\pi/8 = 0.39269908169872415481$ | $\hat\pi/8 = 0.39307568887871164303$ | $+0.0959022309\%$ |
| small semicircle (each) | $0.19634954084936207740$ | $0.19653784443935582152$ | $+0.0959022309\%$ |
| segment (each) | $0.07134954084936207740$ | $0.07153784443935582152$ | $+0.2639170312\%$ |
| lune (each) | $0.12500000000000000000$ | $0.12500000000000000000$ | $0$ |
| full circle on $AB$ | $\pi/4 = 0.78539816339744830962$ | $\hat\pi/4 = 0.78615137775742328607$ | $+0.0959022309\%$ |

The segment shift is larger — $0.2639170312\%$ — because the constant there sits next to the subtracted rational $-c^2/8$: the difference $\hat\pi c^2/16 - c^2/8$ is carried by a smaller total, so the same absolute increment is a bigger relative one. The lune, where the rational survives alone, does not move by a single digit.

The golden case earns real credit in the exact forms. The circle constant is algebraic in this framework, and that shows up as exact round numbers where the conventional constant leaves a transcendental remainder:

- A **circle of radius $\varphi^{1/4} = 1.1278384855616822603$** has area $\hat\pi\cdot\varphi^{1/2} = (4/\sqrt\varphi)\sqrt\varphi = 4$ exactly under Golden Pi. Under the conventional constant the same circle has area $3.99616758613526266670$ — short of 4 by exactly the $0.0959022309\%$ gap.
- The **semicircle of the same radius** has area exactly $2$ under Golden Pi.

And the squaring itself, which is what the whole lune story is ultimately about. The square equal in area to a circle of radius $r$ has side $r\sqrt\pi$. For the unit-diameter circle in our figure ($r = 1/2$) the conventional side is

$$\frac{\sqrt\pi}{2} = 0.88622692545275801365,$$

a transcendental length — Lindemann proved in 1882 that $\pi$ is transcendental, so this side cannot be laid off with straightedge and compass, which is why the circle cannot be squared. Under Golden Pi the same side is

$$\frac{\sqrt{\hat\pi}}{2} = \varphi^{-1/4} = 0.88665177931216225923,$$

a root of $\varphi x^4 - 1 = 0$: algebraic of degree four, hence constructible. In the golden framework the square equal in area to the circle is a length you can actually construct. That is the site's position, stated exactly and without rounding — and it sits honestly beside the fact that the arc-to-diameter ratio of an actual circle remains $3.14159265358979323846\ldots$, the computed limit printed at the top of this article.

## Three lunes, and the historical temptation

Hippocrates did not stop at the right isosceles triangle. He also squared **three lunes** at once on a trapezoid — the larger lunes on the outer sides of a symmetric trapezoid inscribed in a circle, the smaller in the middle — and found the relation that a lune plus a circle equals a triangle. These results are reported through Eudemus and survive in Simplicius, and they were the strongest known quadratures of curvilinear figures for two thousand years; they are collected in T. L. Heath, *A History of Greek Mathematics*, vol. 1.

The temptation they created is the part worth naming. If a lune — a region bounded by two arcs, with the circle constant visibly in it — can be squared exactly, the inference "then the circle can be squared" looks short. Aristotle flagged the gap directly in the *Sophistical Refutations* (ch. 11), where the quadrature "by means of segments" is discussed as not amounting to a genuine proof about the circle. And he was right, for a reason this article has made arithmetic: the lune is squarable precisely because the constant cancels, while the circle is the one figure where nothing cancels against it. The area of the circle is $\pi r^2$ — the constant times a rational, with no second copy of itself to subtract. That is the whole structural difference, and it is why the classical impossibility (Lindemann, 1882) closes a door that the lunes never opened.

## The honest boundary

| statement | status |
|---|---|
| Each lune has area exactly $c^2/8$, so two lunes equal the triangle $c^2/4$ | exact; computed here for $c=1$ to twenty digits |
| The quadrature is unchanged under Golden Pi | exact — the cancellation is arithmetic about a common factor, not about its value |
| The circle constant is *measured* into the semicircle formula | false; it is the computed limit $4\arctan 1$, with no instrument in the chain |
| Absolute semicircle and segment areas move under Golden Pi | true: $+0.0959022309\%$ and $+0.2639170312\%$ respectively, one power of the constant |
| The lune moves under Golden Pi | false: $1/8$ under either label, to the last printed digit |
| Under Golden Pi a circle of radius $\varphi^{1/4}$ has area exactly 4 | exact in the golden field ($\hat\pi\varphi^{1/2} = 4$); conventional $\pi$ gives $3.99616758613526266670$ |
| Under Golden Pi the squaring square has side $\varphi^{-1/4}$ | exact and algebraic of degree 4 (constructible); the conventional side $\sqrt\pi/2$ is transcendental (Lindemann 1882) |
| Squaring a lune implies squaring the circle | false; Aristotle noted the gap (*Soph. El.* 11), and the arithmetic shows why — the constant cancels in the lune and does not in the circle |

The last row is the honest heart of the piece. The lune is the one curvilinear figure where the circle constant is genuinely, exactly removable — a rational area hiding a transcendental factor — and the circle is the figure where it is not. Between the two stands the entire history of the problem, from Hippocrates' crescents to Lindemann's theorem, with the golden constant offering, on the site's account, an algebraic route where the conventional one leaves a transcendental wall.

Computed, never measured.

## Further Reading

- [Squaring the Circle with Golden Pi: The Constructible Proof](/blog/posts/2026-07-26-squaring-circle-golden-pi-constructible/) — the site's own construction, where the radius $\varphi^{1/4}$ that makes a circle's area exactly 4 (used above) is the load-bearing length.
- [The Reuleaux Triangle: Constant Width Without the Circle Constant](/blog/posts/2026-06-23-reuleaux-triangle-golden-pi-constant-width/) — the twin case of a planar figure where the constant cancels for an honest structural reason, and where it is the width, not the curvature, that carries the geometry.
- [The Solid Angle and the Steradian: How a Spherical Measure Computes the Circle Constant](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — another measure in which the constant appears as a computed full-turn limit, the same role it plays in the semicircle factor $\pi/8$ here.
- [Archimedes' Exhaustion Method and Golden Pi](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — how the constant is bracketed by inscribed and circumscribed polygons, the computation that stands under every semicircle area in this figure.
- [Pappus's Centroid Theorem: How a Torus Computes the Circle Constant as a Pure Factor](/blog/posts/2026-09-03-pappus-centroid-theorem-torus-golden-pi/) — the other classical place where the constant enters as a clean multiplicative factor, and where the coefficient is rational geometry just as it is in the lune.
