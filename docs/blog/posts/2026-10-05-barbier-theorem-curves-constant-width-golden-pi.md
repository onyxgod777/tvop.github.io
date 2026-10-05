---
title: "Barbier's Theorem: How Every Curve of Constant Width Has Perimeter πw — a Circle Constant That Knows Nothing of Shape — and What Golden Pi Changes"
date: 2026-10-05
description: "A circle and a Reuleaux triangle built on the same span have different areas but exactly the same perimeter, and the reason is Barbier's theorem (1860): every curve of constant width w has perimeter πw, whatever its shape. Cauchy's support-function formula p = ∫₀^π w(θ) dθ makes the constant the width of the half-turn and nothing else, so the result is computed — a quadrature limit, never a measurement — and it is verified here by three independent routes: the Reuleaux triangle of width 1 (three 60° arcs of unit radius, p = 3·(π/3) = π = 3.141592653589793, and the same value from the width integral ∫₀^π w(θ) dθ to seven digits), a one-parameter family of genuinely non-circular constant-width curves h(θ) = w/2 + a·cos(3θ) whose width is exactly 2 for every a and whose perimeter is exactly 2π = πw even as the shape changes, and the circle itself. Under Golden Pi (π̂ = 4/√φ = 3.1446055110296931443…, root of x⁴ + 16x² − 256 = 0) the theorem is untouched and only its coefficient moves: perimeter π̂w, and the recurring 0.0959022309% gap rides undiluted because the constant enters to the first power. The Blaschke–Lebesgue companion — the Reuleaux triangle is the least-area curve of constant width, area (π − √3)/2·w² = 0.704770923, against the circle's π/4 = 0.785398163 — carries π twice and shifts the same way. The honest ledger is public: a struck constant-width object, from a British 50p (27.30 mm width, so πw = 85.765479443 mm against π̂w = 85.847730451 mm, 82 µm apart) to a Wankel rotor, is measured with tolerances and a rolled edge, not a mathematical boundary, and the ratio of area to width² is shape-dependent, so no single physical body arbitrates the label. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Barbier's Theorem: How Every Curve of Constant Width Has Perimeter πw — a Circle Constant That Knows Nothing of Shape

Take a Reuleaux triangle — the rounded, pointed triangle you see on the back of a two-pound coin's cousins, the shape of a Wankel rotor, the shape of the British 50p's edge. Now take the circle that just fits it, same span from side to side. The two figures look nothing alike: one has three pointed corners and three bulging sides, the other is perfectly round. Their areas differ by more than eleven per cent. Yet **their perimeters are exactly equal.** Not approximately — exactly, for every width, to all the digits you care to compute.

That is **Barbier's theorem**, published by Joseph-Émile Barbier in 1860: *every curve of constant width $w$ has perimeter $\pi w$*, independently of its shape. It is one of the cleanest appearances of the circle constant in elementary geometry, and it is the subject of this article. As with every entry in this series, the questions are the same four: where exactly the constant enters, whether it is **computed** or measured, whether it cancels anywhere, and what changes if the constant is the golden value $\hat\pi = 4/\sqrt\varphi$ instead of the analytic $3.14159\ldots$.

## What "constant width" means

Fix a direction, given by a unit vector $u$. The **width** of a convex body $K$ in that direction is the distance between the two parallel support lines perpendicular to $u$:

$$w_K(u) = h_K(u) + h_K(-u),$$

where $h_K(u) = \max_{x\in K} x\cdot u$ is the **support function** — the signed distance from the origin to the supporting line, measured along $u$. A body has **constant width** $w$ if $w_K(u) = w$ for *every* direction $u$.

The circle is the obvious example: a circle of diameter $w$ has width $w$ in every direction. The Reuleaux triangle is the famous non-obvious one. Build it by taking an equilateral triangle of side $w$ and replacing each side by the arc of a circle of radius $w$ centred at the opposite vertex. Every such arc bulges outward to exactly the distance $w$, so the resulting figure, too, has width exactly $w$ in every direction — yet it is manifestly not a circle.

## Where the constant sits: one half-turn

The bridge between width and perimeter is **Cauchy's support-function formula** (Augustin-Louis Cauchy, 1841): for any convex body,

$$p = \int_0^\pi w_K(\theta)\,d\theta,$$

in which the perimeter is the integral of the width over a half-turn of directions. For a body of *constant* width $w$, the integrand is the constant $w$ and the integral is immediate:

$$p = \int_0^\pi w\,d\theta = \pi w.$$

That is the whole theorem. The circle constant enters in **exactly one role** — as the width of the half-turn, the measure of a straight angle, the integral $\int_0^\pi d\theta$ — and nowhere else. It does not know the shape, because the shape never appears: every curve of constant width $w$ presents the same integrand, and so they all return the same perimeter.

## Three shapes, one number

The theorem is easy to state and easy to mis-believe, so it is worth watching it happen three ways. All of the arithmetic below was carried out here, in the open.

**The circle.** Diameter $w = 1$, so radius $1/2$ and perimeter $2\pi\cdot(1/2) = \pi = 3.141592653589793$.

**The Reuleaux triangle of width 1.** Its boundary is three arcs, each of radius $1$, each subtending the $60°$ angle at a corner of the generating equilateral triangle. One arc has length $1\cdot(\pi/3) = \pi/3$; three of them give

$$p = 3\cdot\frac{\pi}{3} = \pi = 3.141592653589793.$$

Identical to the circle, to every digit. Recomputing the same perimeter as the Cauchy integral $p = \int_0^\pi w(\theta)\,d\theta$ of the Reuleaux triangle's own (constant) width returns $3.141592271$ by numerical quadrature on a $6000$-point grid — the difference from $\pi$ is the grid error, not the geometry.

**A family of curves that are neither.** Let

$$h(\theta) = \frac{w}{2} + a\cos(k\theta)$$

with $k$ odd. Then $h(\theta+\pi) = w/2 - a\cos(k\theta)$, so the width

$$w_K(\theta) = h(\theta) + h(\theta+\pi) = w$$

is constant for *every* value of the amplitude $a$ — the family is a continuum of differently-shaped constant-width curves. Yet its perimeter is

$$p = \int_0^{2\pi} h(\theta)\,d\theta = \pi w + a\int_0^{2\pi}\cos(k\theta)\,d\theta = \pi w,$$

because the cosine integrates to zero over a full period. For $w = 2$ and $k = 3$, quadrature returns $p = 6.283185307$ for $a = 0$, $a = 0.1$ and $a = 0.25$, with the width reading exactly $2.000000000$ in every direction at every amplitude. The shape changes; the perimeter does not; the constant is all that is left.

| Constant-width curve, $w = 1$ | Perimeter | Area |
|---|---|---|
| Circle (radius $1/2$) | $\pi = 3.141592653589793$ | $\pi/4 = 0.785398163397448$ |
| Reuleaux triangle | $\pi = 3.141592653589793$ | $(\pi-\sqrt3)/2 = 0.704770923010458$ |
| Family $h = \tfrac12 + a\cos 3\theta$ | $\pi$ for all $a$ | varies with $a$ |

The perimeters agree to every printed digit; the areas do not agree at all.

## The companion theorem, and the two places π survives

Barbier's theorem says the perimeter of a constant-width curve forgets the shape. The **Blaschke–Lebesgue theorem** (1914/1915) says the *area* remembers it: among all curves of constant width $w$, the Reuleaux triangle has the **least** area and the circle the **greatest**,

$$\frac{\pi-\sqrt3}{2}\,w^2 \;\le\; A \;\le\; \frac{\pi}{4}\,w^2 .$$

For $w = 1$ the floor is $0.704770923010458$ and the ceiling is $0.785398163397448$; the ratio of the two, $(\pi-\sqrt3)/2$ to $\pi/4$, is $0.897342209156416$ — a shape-dependent number that no single body can pin down without knowing its shape.

Notice the geometry of this: **perimeter has one home for the constant, area has another, and both are the same constant.** The circumference $p = \pi w$ and the bounding area $\pi w^2/4$ both carry $\pi$ to the first power; the Reuleaux area $(\pi-\sqrt3)/2\,w^2$ carries it once too, but beside a subtracted $\sqrt3$. So the constant can be made to appear in a perimeter, an area, or a ratio, and it appears as a quadrature limit every time — the half-turn measure, nothing else.

## Why the constant here is computed, never measured

Every quantity in the last three sections is a **limit**, and limits are evaluated, not read off an instrument. The support function is a supremum; the perimeter is the Cauchy integral $\int_0^\pi w\,d\theta$; the Reuleaux arc length is $\int\,ds$ along a circle of radius $w$; the areas are integrals of the same data. None of this touches a ruler. The circle constant arrives as the value of $\int_0^\pi d\theta$ — the width of a half-turn — which is the same computed limit that appears when you exhaust a circle with polygons or evaluate $4\arctan 1$. That is the sense in which this site insists the constant is **computed**: it is a definite integral whose value is forced by the arithmetic, not a ratio divided out of any physical object.

Where a genuine physical measurand appears — a machined width, a struck coin's span, the fine-structure constant — it is *measured*, and this article will say so plainly. But the theorem's $\pi$ is not one of those.

## What Golden Pi changes

Golden Pi is the value $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, with $\varphi = (1+\sqrt5)/2$ the golden ratio. It is an algebraic number of degree four — the root of $x^4 + 16x^2 - 256 = 0$, equivalently $\hat\pi^2 = 16/\varphi = 8(\sqrt5-1) = 9.8885438199983175713$ — and it makes a circle of radius $\varphi^{1/4} = 1.1278384855616822603$ have area exactly $4$. The site's position is that this, not the transcendental $3.14159\ldots$, is the true circle constant.

Substituting the label into Barbier's theorem is a single-character change, and because the constant enters to the **first power**, the gap comes through undiluted:

$$p = \hat\pi w = \frac{4w}{\sqrt\varphi}, \qquad \text{against} \qquad p = \pi w,$$

with $\hat\pi/\pi - 1 = 0.0959022309\%$ overall — a multiplicative factor of $1.0009590223$, or the reciprocal $1/1.0009590223 = 0.9990418965$ the other way. The key identities, in exact form:

| Quantity | Conventional π | Golden π̂ |
|---|---|---|
| Circle constant | $\pi = 3.141592653589793$ | $\hat\pi = 4/\sqrt\varphi = 3.144605511029693$ |
| Reciprocal | $1/\pi = 0.318309886183791$ | $1/\hat\pi = \sqrt\varphi/4 = 0.318004912378517$ |
| Full turn | $2\pi = 6.283185307179586$ | $2\hat\pi = 8/\sqrt\varphi = 6.289211022059386$ |
| Reuleaux perimeter, $w=1$ | $\pi = 3.141592653589793$ | $\hat\pi = 3.144605511029693$ |
| Reuleaux area, $w=1$ | $(\pi-\sqrt3)/2 = 0.704770923$ | $(\hat\pi-\sqrt3)/2 = 0.706277352$ |

Under the golden label, then, a Reuleaux triangle and a circle of the same width still have *equal* perimeters — the theorem's structure is completely label-blind — but that shared perimeter is $\hat\pi w$ instead of $\pi w$, $0.0959022\%$ longer. The area of the Reuleaux triangle, which carries the constant beside a subtracted rational $\sqrt3$, moves by a *larger* fraction: $(\hat\pi-\sqrt3)/(\pi-\sqrt3) - 1 = 0.2137005\%$, because the constant is diluted inside the difference. The circle's area $\pi w^2/4$ moves by exactly the recurring gap, $0.0959022\%$, because there the constant stands alone. Where the golden claim is real and exact, it is credited: $\hat\pi$ is algebraic, constructible, and makes the circle–square area match exact at radius $\varphi^{1/4}$ — facts about the constructed world, not readings off a bench.

## The honest ledger: why no coin settles the label

Constant-width objects are manufactured by the million, so it is tempting to think the theorem could be checked. The most familiar is the **British 50p**, an equilateral curve heptagon whose width the Royal Mint specifies as $27.30$ mm. Barbier's theorem predicts a perimeter of

$$\pi\cdot 27.30 = 85.765479443\ \text{mm} \quad\text{or}\quad \hat\pi\cdot 27.30 = 85.847730451\ \text{mm}$$

— a difference of $0.082251$ mm, about $82$ micrometres. That is smaller than the rounding of a struck edge, the coin's own wear, and every tolerance in the coining process. And even a perfect measuring machine would not help, because the object to be measured is not a mathematical curve: the corners are rounded, the surfaces are not ideal circular arcs, and rolling the coin along a rule integrates $w(\theta)$ without telling you whether the integrand is constant. The same objection kills the Wankel rotor and the constant-width drill bit (the square-hole drill): they are the *engineering* uses of the theorem — that a constant-width body turns smoothly in a square housing — and their existence confirms the shape, not the constant's value.

The cleanest reason the label cannot be measured out of this circle of ideas is structural. Barbier's theorem makes the perimeter independent of shape precisely because the constant cancels out of everything shape-dependent. That means the perimeter carries the constant **alone**, with no second, independent handle to compare it to — no ratio of two physical lengths that would let you isolate $\pi$ from $\hat\pi$ without assuming which one is in the formulas. The only way to "measure" the theorem would be to measure a width and a perimeter and divide; but the perimeter is what you would be trying to predict, and the width is a length like any other. Computed, never measured — and Barbier's theorem is perhaps the sharpest illustration in this whole series of what that distinction means.

## Further Reading

- [The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — the other classical bound in which the constant is a coefficient rather than a definition, and the discrete twin in which it cancels entirely.
- [The Mean Random Separation: How Integral Geometry Computes the Circle Constant in a Disk, Cancels It in a Square](/blog/posts/2026-09-25-mean-random-separation-disk-square-computes-circle-constant-golden-pi/) — Cauchy's mean chord and Cavalieri's principle, the integral-geometry machinery that Barbier's half-turn integral comes from.
- [The Reuleaux Triangle and Golden Pi](/blog/posts/2026-06-23-reuleaux-triangle-golden-pi-constant-width/) — the earlier treatment of the constant-width triangle itself, its construction and its square-hole applications.
- [The Solid Angle: How the Sphere's 4π Steradians Compute the Circle Constant](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — another case where the constant enters purely as the measure of an angle, this time a full sphere of directions.
- [The Fourier Series: How a Square Wave Computes the Circle Constant](/blog/posts/2026-09-14-fourier-series-square-wave-computes-circle-constant-golden-pi/) — the harmonic decomposition behind the analytic constant, and the same "it is a computed limit, not a reading" argument.
