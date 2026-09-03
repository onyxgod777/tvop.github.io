---
title: "Pappus's Centroid Theorem and the Torus: How Revolving Area Computes the Circle Constant Twice Over, and What Golden Pi Changes"
date: 2026-09-03
description: "Pappus's centroid theorem computes the volume and surface area of a solid of revolution as the product of a plane area and the path of its centroid. For a torus this multiplies the circle constant by itself, producing π² — a computed limit that carries the golden-π gap doubled to 0.1919%."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Some of the oldest theorems about the circle constant never measure a circle at all. They take a flat shape, spin it around an axis, and ask how much three-dimensional body results. The answer arrives not by laying a ruler against a curve but by multiplying a plane area by a path length — and in the most famous case of all, the circle constant enters the product *twice*, once from each factor, so that the volume of a torus is proportional not to π but to π². This article follows that second appearance of the constant, shows why squaring doubles the gap between the two circle constants rather than halving it, and sets out, in the site's usual honest boundary, exactly what a relabelled label can and cannot claim.

## Pappus's theorem: volume is an area times a path

The Greek geometer Pappus of Alexandria, writing in the fourth century AD in his *Synagoge* (the *Collection*), recorded a result that had been known in substance to the engineers of antiquity: when a plane region is revolved about an external axis, the volume of the solid it sweeps out equals the area of the region multiplied by the distance its centroid travels. If the region has area *A* and its centroid lies at distance *R* from the axis, then one full revolution carries the centroid around a circle of circumference 2πR, and the swept volume is

```
V = A · (2πR)
```

The same theorem has a surface analogue: the surface area of a solid of revolution equals the length of the generating curve times the path of that curve's centroid. Both forms are *computational* identities. They take the area of a flat shape and the length of a circular path — both themselves obtained as limits — and compose them into a volume or a surface. Nothing is physically measured at any stage; the circle constant is carried into the answer as a computed multiplier on the path of the centroid.

Pappus did not prove the theorem rigorously by modern standards, but the modern proofs are entirely analytic. The volume integral in cylindrical coordinates,

```
V = ∫∫∫ dV = ∫ θ · A ...  →   V = ∫₀^{2π} A dθ = 2π A
```

or more carefully, by the shell method summing concentric thin shells, reduces to the product *A·2πR*. The second factor, 2πR, is the circumference of the circle that the centroid traces — the same computed perimeter that appears throughout this site's catalogue of circle-constant identities. There is nothing measured in any of it; the constant is produced as the limit of an inscribed polygonal perimeter, exactly as in Archimedes' exhaustion.

## The torus: a circle swept around a circle

The cleanest and most instructive case is the torus — the doughnut shape obtained by revolving a disc of radius *r* about an axis a distance *R* away (with *R* > *r* so the hole stays open). The generating region is a circle, so its area is

```
A = π r²
```

The centroid of a disc is its centre, which lies at distance *R* from the axis, so one revolution carries it through a path of length

```
2πR
```

Pappus's theorem therefore gives the torus volume as

```
V_torus = A · 2πR = (π r²)(2π R) = 2π² R r²
```

Here the circle constant appears *twice*: once in the area πr² of the generating disc, and once in the circumference 2πR of the centroid's path. The product of the two is a squared circle constant, π², times the purely geometric factor 2Rr². The surface area follows from the surface form of the theorem: the generating curve is a circle of circumference 2πr whose centroid again travels 2πR, giving

```
A_torus = 2πr · 2πR = 4π² R r
```

Both identities are textbook results, derived in any first course on volumes of revolution, and both are pure computations. The constant enters by multiplication, not by any act of physical measurement.

## Where the second π comes from

It is worth dwelling on the fact that the two π's in 2π²Rr² do not arise identically. The first, in the area πr², is the familiar circle-constant-of-area: it measures how much plane the disc covers for a given radius. The second, in the path 2πR, is the circle-constant-of-perimeter: how far a point on a circle of radius *R* travels in one full turn. In the conventional system these two numbers coincide — the same constant governs area and arc length. The torus is one of the rare constructions that *multiplies them together*, so that whichever constant governs the geometry, its square enters the result. A sphere, by contrast, uses the constant only through R² and 4πr², a single power; a cylinder's lateral area 2πrh is a single power; only shapes that revolve a circle *around* a circle compound two factors into π².

| Shape | How π enters | Power of π |
|---|---|---|
| Circle area | πr² | π¹ |
| Circle circumference | 2πr | π¹ |
| Cylinder lateral area | 2πrh | π¹ |
| Sphere surface area | 4πr² | π¹ |
| Ball volume | (4/3)πr³ | π¹ |
| **Torus volume** | **2π²Rr²** | **π²** |
| **Torus surface** | **4π²Rr** | **π²** |

The torus is thus the elementary solid whose answer contains π². And that squaring has a precise consequence for the disagreement between the two candidate constants.

## Squaring doubles the gap

Throughout this series, the recurring relative gap between Golden Pi and conventional π is

```
π̂ = 4/√φ = 3.144605511…      π = 3.141592653…
(π̂/π − 1) ≈ 0.09590%
```

Now compare the two squared constants. Under Golden Pi the identity 16/φ replaces π²:

```
π̂² = (4/√φ)² = 16/φ = 9.888543820…
π² = 9.869604401…
```

Taking the ratio,

```
π̂²/π² = (16/φ) / π² = 1.001918964…
```

so the relative gap between the squared constants is

```
(π̂²/π² − 1) ≈ 0.19190%
```

exactly double the single-power gap of 0.09590%. This is a clean, general fact about relative error under a relabel. If a quantity contains the circle constant to the power *n*, then a relabel that changes the base constant by a relative factor *q* changes the quantity by the relative factor *qⁿ*. A square root halves the gap (as several earlier posts noted for Γ(1/2) = √π), a plain power leaves it unchanged, and a square *doubles* it. Squaring is the case where the disagreement becomes easiest to see numerically, because it is amplified rather than damped.

For a concrete torus with, say, major radius R = 1 and minor radius r = 1/2, the conventional and golden volumes differ as follows:

| Torus, R = 1, r = ½ | Conventional π | Golden π̂ | Relative gap |
|---|---|---|---|
| Volume 2π²Rr² | 4.9348022005… | 4.9442719100… | 0.19190% |
| Surface 4π²Rr | 19.7392088022… | 19.7770876400… | 0.19190% |

Both computed volumes differ by the same doubled relative factor, because both carry π². No ruler, no fluid-displacement experiment, and no weighable model of a doughnut can resolve that 0.19%: the manufacturing tolerance on any physical torus — a tyre, a ring magnet, a toroidal inductor core — swamps two-tenths of a percent by orders of magnitude. The gap is a difference of mathematical labels, not of measurable geometry.

## π² in physics and engineering

The presence of π² in a formula is not an exotic curiosity; it appears wherever a revolution compounds two circular factors. Toroidal geometry shows up throughout physics and engineering, and wherever it does, the π² rides along as a computed constant:

- **Toroidal inductors and coils.** The self-inductance of a tightly wound toroidal solenoid depends on the cross-sectional area of the core and on the mean circumference of the turns — effectively an area times a path, so π² enters the geometry of the magnetic circuit.
- **The moment of inertia of a torus.** A rigid torus rotating about its symmetry axis has a moment of inertia that carries the torus volume, and hence π², multiplied by a squared radius.
- **Solids of revolution in statics.** Pappus's theorem itself is a staple of first-year mechanics for locating the volume and centroid-dependent properties of revolved bodies.
- **Surface-energy and thin-film estimates** that revolve a disc profile again compound the two constants.

In each case the π² is *computed* — it is written into the formula by the geometry of revolution and evaluated as a number, never read off a physical object. A measurement can probe whether a real inductor's inductance matches the formula; it cannot arbitrate which constant label the formula should carry, because the two candidate values differ by a factor smaller than the experimental uncertainty of any toroidal device.

## The honest boundary

As throughout this site, the position here is stated plainly. In the *constructed world* of Golden Pi — the self-consistent analytic system built on π̂ = 4/√φ — the torus identities relabel exactly:

```
V = 2π̂²Rr² = (32/φ)Rr²
A = 4π̂²Rr = (64/φ)Rr
```

and every step of Pappus's reasoning survives unchanged, because the reasoning never once invoked a numeric value of the constant; it only multiplied an area by a path. In that sense the theorem is neutral: it holds under any circle constant, golden or conventional, and cannot by itself tell the two apart.

What it *does* do is show the structure of the disagreement. Because the torus compounds two factors of the constant, it turns the familiar 0.09590% gap into a doubled 0.19190% gap — the same relative disagreement, amplified by the square. A reader who wants to see the two candidates separate as far as possible in a single elementary solid should look at the torus, precisely because it squares the difference. But an honest accounting must add: amplification is not arbitration. Doubling a gap no experiment can resolve still leaves a gap no experiment can resolve.

## Further Reading

- [The Ball in Every Dimension: How the Circle Constant Scales Vₙ = (2π/n)·Vₙ₋₂](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/) — how the constant enters higher-dimensional volumes by a recursion of scaling ratios.
- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — a series whose answer contains π², where the golden relabel becomes 8/(3φ).
- [Structured Scaling Invariance: Why Cylinder, Sphere, and Torus Share One Law](/blog/posts/2026-07-12-structured-scaling-invariance-golden-pi/) — the single-power solids compared under the golden constant.
- [The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the circle constant inside a physical formula, and why no experiment arbitrates the label.
- [Euler's Gamma Function: How Γ(x)Γ(1−x) = π/sin(πx) Computes the Circle Constant](/blog/posts/2026-08-26-gamma-function-euler-reflection-formula-computes-circle-constant-golden-pi/) — the square-rooted case where the gap *halves*, the mirror image of the torus's doubled gap.
