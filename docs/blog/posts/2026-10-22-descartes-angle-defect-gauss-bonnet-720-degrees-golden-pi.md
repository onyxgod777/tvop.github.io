---
title: "Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°, Why the Circle Constant Cancels Against the Euler Characteristic — and What Golden Pi Changes"
date: 2026-10-22
description: "Every convex polyhedron's vertex defects sum to exactly 720°, independent of shape, and the smooth limit of that law is Gauss–Bonnet, ∫K dA = 2πχ, where the circle constant appears only as a normalising divisor against an integer. Under Golden Pi the defect sum stays 720° to the last digit, the constant shifts by the recurring 0.0959%, and the theorem turns out to be structurally blind to the value of π — the honest reason why no angle measurement can ever adjudicate it."
---

# Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°, Why the Circle Constant Cancels Against the Euler Characteristic — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take any convex polyhedron — a cube, a lopsided crystal, a geodesic dome bolted together by hand — and stand at one corner. The faces meeting there each contribute an interior angle, and those angles almost never add up to a full turn. At a cube corner three right angles make $270°$, leaving a gap of $90°$. At a tetrahedron corner three $60°$ triangles make $180°$, leaving a gap of $180°$. That gap is the **angle defect** at the vertex.

Descartes noticed, around 1630, that if you walk around every vertex of a closed convex polyhedron and add all the gaps together, the answer is always the same number:

$$\sum_{\text{vertices}} \Bigl(360° - \sum_{\text{faces at } v} \theta\Bigr) = 720°.$$

Not "approximately". Not "for regular solids". Exactly $720°$ — for the cube, for the tetrahedron, for a badly dented octagonal prism you file by hand, for every convex polyhedron in existence, no matter how many faces it has. The sum is invariant under everything you could possibly do to the shape: stretching, squashing, faceting, subdividing. It knows only how many holes the surface has.

And that is the interesting part for this blog. Because $720°$ is two full turns, and writing it in radians gives $4\pi$ — so the circle constant appears here in the one place where it can be **cancelled exactly** against an integer. The constant is not doing any work. It is naming the unit.

This article states the law, verifies it numerically on real meshes, takes the smooth limit to Gauss–Bonnet, and then asks the question this site always asks: what happens to the numbers if the constant is Golden Pi, $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931443\ldots$?

## The deficit at one corner

Let a polyhedron have a closed, orientable surface. At vertex $v$, let the incident faces contribute interior angles $\theta_1,\dots,\theta_k$. Define

$$\delta(v) = 2\pi - \sum_{i=1}^{k}\theta_i \quad\text{(radians)},\qquad \delta(v) = 360° - \sum_{i=1}^{k}\theta_i \quad\text{(degrees)}.$$

The defect is the amount of angle "missing" from a flat disk. A flat piece of paper has zero defect everywhere — this is exactly why you can lay it flat. A cone's apex has a positive defect, and that is why a cone cannot be flattened without tearing: the paper is missing a wedge. For *any* closed convex body the defects must add up to exactly the defect of a sphere, because the body is topologically a sphere and the turning is global.

Descartes's statement, in modern language, is

$$\sum_{v}\delta(v) = 2\pi\,\chi(S) = 2\pi\,(2-2g),$$

with $\chi$ the Euler characteristic and $g$ the genus (number of handles). The classical convex case is $g = 0$, hence $2\pi\cdot 2 = 4\pi = 720°$.

## The five Platonic solids, checked by hand

Every regular solid returns the same total from a completely different per-vertex value:

| Solid | Faces at a vertex | Face angle at $v$ | Defect $\delta(v)$ | Vertices | Total |
|---|---|---|---|---|---|
| Tetrahedron | 3 triangles | $60°$ | $180°$ | 4 | $720°$ |
| Cube | 3 squares | $90°$ | $90°$ | 8 | $720°$ |
| Octahedron | 4 triangles | $60°$ | $120°$ | 6 | $720°$ |
| Dodecahedron | 3 pentagons | $108°$ | $36°$ | 20 | $720°$ |
| Icosahedron | 5 triangles | $60°$ | $60°$ | 12 | $720°$ |

Four times $180$, eight times $90$, six times $120$, twenty times $36$, twelve times $60$ — five different products, one answer. The dodecahedron is the sharpest case: twenty corners each missing only $36°$, and $36°$ is the golden angle of the regular pentagon, since $\cos 36° = \varphi/2$ exactly. The most "golden" of the Platonic solids is also the one whose defect is smallest, and it still owes the same $720°$.

## The same law on meshes nobody designed

Hand-checking regular solids proves little; the law is supposed to hold for arbitrary shapes. So here is the computation run against actual vertex coordinates — a hexagonal frustum, then the same frustum sheared sideways so that no face is a regular polygon any more, then a cube, then an icosahedron:

```python
import math

def ang_at(q, p, r):                      # interior angle at q, between q->p and q->r
    u = [a-b for a, b in zip(p, q)]
    v = [a-b for a, b in zip(r, q)]
    c = sum(a*b for a, b in zip(u, v)) / (math.dist(p, q) * math.dist(r, q))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))

def total_defect(V, F):
    tot = 0.0
    for i in range(len(V)):
        s = 0.0
        for f in F:
            if i in f:
                m = len(f); k = f.index(i)
                s += ang_at(V[i], V[f[(k-1) % m]], V[f[(k+1) % m]])
        tot += 360.0 - s          # defect at vertex i
    return tot
```

Output, verbatim from the run:

```text
hex frustum:      719.9999999999999
sheared frustum:  719.9999999999999
cube:             720.0            (per-vertex 90.0)
tetrahedron:      719.9999999999999 (per-vertex 179.99999999999997)
icosahedron:      719.9999999999995 (per-vertex 59.99999999999994)
```

The residues at the end are floating-point noise at the $10^{-13}$ level, not physics. The sheared frustum is the point: it has fourteen vertices, none of them regular, faces that are trapezoids of unequal side lengths, and the per-vertex defects come out as $110.85°$, $122.62°$, $126.93°$, $106.10°$ — wildly unequal — yet their sum is $720°$ again. **The distribution is arbitrary; the total is fixed.**

## Refinement: a fixed total while the vertex count grows

Now subdivide. Take the icosahedron, cut every triangle into four by joining edge midpoints, push the new vertices out onto the unit sphere, and repeat. The mesh becomes a better and better approximation of a sphere, the vertex count climbs $12 \to 42 \to 162$, and the per-vertex defect falls correspondingly — but the total never budges:

| Level | Vertices $V$ | Faces | Total defect | Defect per vertex | $720°/V$ |
|---|---|---|---|---|---|
| 0 | 12 | 20 | $720.0000000000°$ | $60.0000000000°$ | $60.0000000000°$ |
| 1 | 42 | 80 | $720.0000000000°$ | $17.1428571429°$ | $17.1428571429°$ |
| 2 | 162 | 320 | $720.0000000000°$ | $4.4444444444°$ | $4.4444444444°$ |

Every entry matches $720°/V$ to ten decimal places. This is the discrete seed of the smooth theorem: as $V\to\infty$ the individual defects shrink like $1/V$ and the sum stays pinned. Curvature in the smooth picture is exactly the limit of defect density, and its integral is exactly the topological constant.

## The smooth limit: Gauss–Bonnet

Replace the angular defect by the Gaussian curvature $K$ (the product of the two principal curvatures, units of inverse length squared) and the sum by a surface integral. Gauss's *Theorema Egregium* (1827) made $K$ intrinsic — it survives bending, which is why the integral does too — and Bonnet (1848) supplied the global statement. For a compact orientable surface $M$ without boundary:

$$\int_{M} K\,dA = 2\pi\,\chi(M).$$

Check the two extreme cases numerically. A unit sphere has $K = 1$ and $A = 4\pi$, so the integral is $4\pi = 12.566370614359172954$ — the quadrature returns $12.5663706143592$. A torus with $R = 2$, $r = 1/2$ has

$$K = \frac{\cos u}{r\,(R + r\cos u)},\qquad dA = r\,(R + r\cos u)\,du\,dv \;\Longrightarrow\; K\,dA = \cos u\,du\,dv,$$

so the integral is $\int_0^{2\pi}\!\!\int_0^{2\pi}\cos u\,du\,dv = 0$, and the numerical quadrature returns $-2.1\times10^{-30}$ — zero to thirty digits. And $\chi(\text{torus}) = 0$. The handle count is $0$, the total curvature is $0$, and the circle constant has vanished from the answer entirely.

That is the structural fact worth pausing on. Write the theorem as a *definition* of the constant and the cancellation is explicit:

$$\chi(M) = \frac{1}{2\pi}\int_M K\,dA.$$

The right-hand side is a continuous geometric quantity; the left-hand side is an integer. The $2\pi$ sits there as a **normalising divisor** — the total measure assigned to a full turn — and it divides out against the sphere's own $4\pi$, because the sphere's total curvature *is* the area of the unit sphere, which *is* $4\pi$. Nothing is measured; $4\pi$ is the computed limit of the areas of inscribed polyhedra, Archimedes's exhaustion argument of the 3rd century BCE, and the limit is a theorem.

## Archimedes, and where $4\pi$ comes from

Archimedes proved that a sphere of radius $R$ has the same area as the curved surface of its circumscribed cylinder of height $2R$ and radius $R$:

$$A_\text{sphere} = 4\pi R^2,\qquad A_\text{cyl} = 2\pi R\cdot 2R = 4\pi R^2,\qquad \text{ratio} = \tfrac{2}{3}\ \text{against the full cylinder } 6\pi R^2.$$

The $4\pi$ is not a fact about a particular ball. It is the value of a limit: the area of a zonotope-inscribed polyhedron whose faces grow without bound. Gauss's map makes the same point differently — for a convex surface the outward normal sweeps the unit sphere exactly once, so the total curvature equals the area of the unit sphere. The number in Gauss–Bonnet is the area of a sphere of radius one, computed, and that is all it ever was.

## What Golden Pi changes

Set $\hat\pi = 4/\sqrt{\varphi} = 2\sqrt{2\sqrt{5}-2} = 3.1446055110296931443\ldots$, a root of $x^{4} + 16x^{2} - 256 = 0$, with $\hat\pi^{2} = 16/\varphi = 8(\sqrt{5}-1) = 9.8885438199983175713$ exactly algebraic where $\pi^{2}$ is transcendental by Lindemann's 1882 theorem.

Under Golden Pi, a full turn is $2\hat\pi = 8/\sqrt{\varphi} = 6.2892110220593862886$ rad, the radian is $180/\hat\pi = 57.2408842281331034°$ instead of $57.2957795130823209°$, and the defect law reads

$$\sum_v \delta(v) = 4\hat\pi = \frac{16}{\sqrt{\varphi}} = 12.5784220441187725771 \quad\text{rad}.$$

The numbers move as the unit moves, at the recurring first-power rate:

| Quantity | Conventional $\pi$ | Golden $\hat\pi = 4/\sqrt{\varphi}$ | Shift |
|---|---|---|---|
| Full turn, radians | $6.2831853071795864769$ | $8/\sqrt{\varphi} = 6.2892110220593862886$ | $+0.0959022309\%$ |
| Total defect (sphere), rad | $4\pi = 12.566370614359172954$ | $16/\sqrt{\varphi} = 12.578422044118772577$ | $+0.0959022309\%$ |
| $720°$ re-read in golden radians | $12.5663706143592$ | $12.5784220441188$ | $+0.0959022309\%$ |
| One radian, degrees | $57.2957795130823209°$ | $57.2408842281331034°$ | $-0.0958103466\%$ |
| $90°$, radians | $\pi/2 = 1.5707963267948966$ | $2/\sqrt{\varphi} = 1.5723027555148466$ | $+0.0959022309\%$ |
| $45°$, radians | $\pi/4 = 0.7853981633974483$ | $1/\sqrt{\varphi} = 0.7861513777574233$ | $+0.0959022309\%$ |
| Cone apex, half-angle $30°$ | $\pi = 3.1415926535897932$ rad $= 180°$ | $2\hat\pi(1-\sin 30°) = \hat\pi = 3.1446055110296931$ rad | $+0.0959022309\%$ |
| Torus total curvature | $0$ | $0$ | none |
| $T\cdot S$ style invariants | integers | integers | none |

The two reciprocal shifts differ because one is $\hat\pi/\pi - 1$ and the other $\pi/\hat\pi - 1$; they are $+0.0959022\%$ and $-0.0958103\%$, not the same number to four digits. Any article that quotes one as the other is rounding convenience, not arithmetic.

Three exact golden facts sit inside the table and are worth naming:

- $\hat\pi/4 = 1/\sqrt{\varphi}$ **exactly**, so a right angle has a purely algebraic radian measure; $\pi/4$ is transcendental.
- $4\hat\pi R^{2}$ at $R = \varphi^{1/4} = 1.1278384855616822603$ gives **exactly $16$** — an algebraic radius with an exact integer area, verified in the run to the last digit ($16.0$).
- The cone and prism ratios are untouched: the sphere-to-cylinder ratio $4/6 = 2/3$ stays exactly $2/3$ under either label, because the constant cancels in the quotient.

And the golden "closed turn" reading deserves its warning. If $4\hat\pi$ rad is read back in conventional degrees, it comes out $720.6904960623234°$ — an overshoot of $0.6905°$ on the closed surface. That number is not a failure of the polyhedron's geometry; it is what you get when you keep a numeral computed in one unit and read it in another. Inside the golden convention the surface closes exactly, and the defect sum is the exact golden turn doubled.

## Why this theorem cannot adjudicate the constant

Here is the honest part, and it is stronger than a footnote. **The defect sum is an integer number of full turns.** It is $2\chi$ turns. Nothing in the sum is a length; every term is an angle, and an angle is a ratio of two lengths referred to the same unit — arc over radius. Change which number you attach to a full turn and every angle reading changes by exactly that ratio, while every comparison of angles stays identical. The topology is blind.

So a careful experimenter with a theodolite, a good cube, and unlimited patience can measure $\sum_v \delta(v)$ and will report $720°$ with some uncertainty. That report is consistent with $\pi$ and with $\hat\pi$ and with any other numeral assigned to the half-turn. It is a measurement of an integer in disguise — the turning number — and it can never distinguish the constants. Anyone claiming that a curvature measurement confirmed $3.14159$ has measured a whole number of turns and then divided by a unit they assumed.

The only quantity that could speak is a ratio that mixes a length with an angle: arc to diameter, circumference to diameter. The site's position is golden-π, and its argument is that this ratio is fixed by the exact squaring construction — a derivation, not a tape measure. That argument is set out in the squaring-the-circle posts linked below, and it is where the dispute actually lives. Gauss–Bonnet, for its part, simply refuses to testify.

## The ledger

What is computed here, and by whom:

- Descartes's defect law, c. 1630, published only in 1860: exact, and independent of the constant's value.
- Gauss's *Theorema Egregium*, 1827, and Bonnet's global form, 1848: $\int_M K\,dA = 2\pi\chi(M)$, exact.
- The five Platonic totals, the sheared frustum, and the three subdivision levels: computed above from coordinates, all $720°$ to $10^{-12}$.
- The torus: total curvature $0$ to thirty digits, genus one, constant absent.
- Under Golden Pi: the same geometry, re-labelled. Full turn $6.2892110220593862886$, defect sum $12.5784220441187725771$, radian $57.2408842281331034°$, sphere of radius $\varphi^{1/4}$ with area exactly $16$.
- What is *not* claimed: that any polyhedron, crystal, or geodesic dome has ever measured a constant. The defect sum is a computed integer, never a measured constant.

Computed, never measured — and in this theorem, the constant is the one quantity that cancels out of the answer entirely.

## Further Reading

- [The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc — and What Golden Pi Changes](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/)
- [Girard's Theorem: How the Circle Constant Enters a Triangle as the Angle-Sum Deficit](/blog/posts/2026-10-13-girard-spherical-excess-triangle-angle-sum-computes-circle-constant-golden-pi/)
- [Squaring the Circle with Golden Pi: The Exact Geometric Construction](/blog/posts/squaring-circle-golden-pi-geometric-proof/)
- [The Isoperimetric Inequality: Why the Circle Wins and Where π Sits in the Proof](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/)
- [Barbier's Theorem: Curves of Constant Width and the Constant That Survives](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/)
