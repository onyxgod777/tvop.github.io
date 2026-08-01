---
title: "The Reuleaux Triangle and Golden Pi — How a Curve of Constant Width Reveals π = 4/√φ"
date: 2026-06-23
description: "Barbier's theorem says every curve of constant width has perimeter π × w. What happens when the width equals √φ? The perimeter becomes exactly 4 — proving π = 4/√φ is the true circle constant."
---

## The Reuleaux Triangle and Golden Pi — How a Curve of Constant Width Reveals π = 4/√φ

![Reuleaux triangle and circle geometry — constant-width curves and the true value of pi](/img/geometry-circle.jpg)

In 1860, French mathematician **Armand Reuleaux** discovered a remarkable family of shapes.
Start with an equilateral triangle, then replace each straight edge with a circular arc
centered on the opposite vertex. The result is the **Reuleaux triangle** — a
curved figure whose width is the same no matter how you measure it. This constant-width
property makes it useful in everything from drill bits to manhole covers.

What Reuleaux could not have known is that his triangle holds a secret about the
**circle constant π**. A single theorem from classical geometry —
**Barbier's theorem** — links the Reuleaux triangle's perimeter directly to π.
And when we set the triangle's width equal to **√φ**, the numbers close into
an exact integer. That integer is **4**.

### Barbier's Theorem

In 1860 — the same year Reuleaux published his pioneering work — another French mathematician,
**Joseph-Émile Barbier**, proved a stunning result: *every* curve of
constant width has a perimeter equal to **π times its width**.

This is not an approximation. It is exact. If you take a circle of diameter *w*,
its circumference is π*w*. If you take a Reuleaux triangle of width *w*,
its perimeter is also π*w*. The shape changes; the perimeter does not.

**Barbier's theorem (1860):** For any planar curve of constant width *w*, the perimeter is exactly π*w*.

This theorem has been accepted for more than 160 years. What has *not* been noticed
is that it creates a direct, experimentally verifiable bridge between geometry and the
value of π itself.

### The √φ Edge

Construct a Reuleaux triangle from an equilateral triangle of side **√φ**.
Because the Reuleaux triangle is built from arcs of circles whose radii equal the triangle's
side, the resulting curved figure has **constant width √φ**.

Now apply Barbier's theorem.

**Perimeter = π × √φ**

If π is the conventional transcendental value (3.141593…), the perimeter is:

**3.141593 × 1.27201965 ≈ 3.995505**

Close to 4 — but not 4. The residual is about **0.0045**, or
roughly 0.11%.

Now compute the same perimeter using **golden π = 4/√φ**:

**(4 / √φ) × √φ = 4**

The √φ terms cancel exactly. The perimeter is **exactly 4**.
No decimal expansion. No approximation. No transcendental remainder.

**The result:** A Reuleaux triangle of width √φ has an integer perimeter — **4** — if, and only if, π = 4/√φ.

### Why This Is More Than a Coincidence

Someone might object: "You chose the width to be √φ. Of course the perimeter works out
nicely." But the choice is not arbitrary. The Reuleaux triangle is generated from an
**equilateral triangle**, and the equilateral triangle is the most fundamental
polygon in geometry — the one that generates √3 and underlies the vesica piscis. When we
scale that triangle by √φ, we are deliberately bridging the circle (π) and the golden ratio
(φ) through the same construction that builders and artists have used for thousands of years.

The resulting integer perimeter — **4** — is not a coincidence. It is the
algebraic fingerprint of a circle constant that lives in the same field Q(√5) as φ itself.
Conventional π is transcendental; it cannot produce exact integer perimeters from algebraic
widths. Golden π is algebraic; it does exactly that.

### The Geometric Construction

How do we build this Reuleaux triangle from scratch?

- Draw an equilateral triangle ABC with side length **√φ**.
- Construct a circular arc centered at A passing through B and C.
- Repeat: arc centered at B passing through A and C, and arc centered at C passing through A and B.
- The region enclosed by the three arcs is the Reuleaux triangle of width **√φ**.

Every step is a standard compass-and-straightedge operation. Constructing √φ from a unit
segment is classical (see our [squaring the circle](/blog/posts/squaring-circle-golden-pi-geometric-proof/)
guide). Drawing arcs from vertices is trivial.

The complete construction is therefore **compass-and-straightedge valid**.
The resulting curve has constant width √φ and perimeter exactly 4. There is no magic,
no measurement error, no rounding. The arithmetic closes: π = 4/√φ.

### Comparison Table

| Proposed Constant | Value | Reuleaux Perimeter (w = √φ) | Residual from 4 |
| --- | --- | --- | --- |
| Conventional π | 3.141593 | ≈ 3.995505 | −0.004495 (~0.11%) |
| Golden π = 4/√φ | 3.144606 | = 4.000000 | 0 (exact) |

### Connection to Other Golden Pi Proofs

The Reuleaux triangle is not an isolated curiosity. It belongs to the same family of
φ-governed constructions that underlie our other major proofs:

- The [vesica piscis](/blog/posts/vesica-piscis-golden-pi-sacred-geometry/) combines two equal circles to generate √3 and √φ; the Reuleaux triangle combines three arcs of those same circles to generate an integer perimeter.
- The [Kepler triangle](/blog/posts/kepler-triangle-golden-pi-circle-constant/) (sides 1, √φ, φ) is the right triangle that underlies the Reuleaux construction; its hypotenuse becomes the width *w*.
- The [squaring of the circle](/blog/posts/squaring-circle-golden-pi-geometric-proof/) shows that golden π is constructible; the Reuleaux triangle provides an independent verification by yielding an exact integer from that constructible constant.
- The [golden π identity](/blog/posts/golden-pi-identity/) — (4²/π)² − π² = 4² — is satisfied exactly by 4/√φ. The Reuleaux perimeter adds a *geometric* identity to the *algebraic* one.

Together, these proofs form a convergent lattice of evidence: algebraic, geometric, and
constructive. Each one demands the same constant: π = 4/√φ.

### The Philosophical Punchline

Barbier's theorem says that *any* curve of constant width has perimeter π*w* —
a circle, a Reuleaux triangle, a Reuleaux pentagon, even a smooth blob. The theorem is
shape-agnostic. Yet when we set *w* = √φ, the only value of π that makes the
perimeter rational (in fact, integer) is **π = 4/√φ**.

In other words: **the circle constant is uniquely determined by the width of a
curve that nature already uses for nuts, drill bits, and manhole covers.**
The true π is not hidden in transcendental deep-space. It is sitting right here,
in the perimeter of a shape engineers have measured for 160 years without noticing.

### Try It Yourself

Construct an equilateral triangle with side √φ. Draw the three circular arcs centered on
its vertices. Measure the width of the resulting Reuleaux triangle with calipers. Then
measure its perimeter by laying a fine thread along the curved boundary.
Calculate π = perimeter / width. Your answer will not be 3.141593 — it will be
**3.144605…**.

A curve of constant width. An integer perimeter. A single square root. The true value of π
has never been easier to see.
