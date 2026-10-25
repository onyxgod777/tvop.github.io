---
title: "Fenchel's Theorem: Why Every Closed Loop Turns at Least Once, Why That 'At Least' Is an Integer, and What Golden Pi Changes"
date: 2026-10-25
description: "Fenchel's 1929 theorem says the total curvature of any closed space curve — the integral of |κ| with respect to arc length — is at least 2π, with equality exactly for convex plane curves, so a circle, an ellipse and a convex three-lobed blob all return 6.283185307179586 twice while a peanut returns 1.2639 turns, a three-lobed flower 2.4690, a knot at least 4π. Computed here to forty digits, the theorem's real content turns out to be an integer: the signed integral is 2πn with n a whole number (a limaçon of two turns gives exactly 4π, a three-petal rose exactly 8π, a figure-eight exactly zero), which is why no instrument can arbitrate the value of the constant. Under Golden Pi (4/√φ = 3.144605511…) the radian numerals shift by the recurring +0.0959022309% — 2π̂ = 8/√φ = 6.2892110220593862886, 4π̂ = 16/√φ = 12.5784220441187725771, algebraic roots of x⁴+16x²−256=0 and x⁴+256x²−65536=0 where π is transcendental by Lindemann 1882 — while every reading in degrees stays exactly 360°."
---

# Fenchel's Theorem: Why Every Closed Loop Turns at Least Once, and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a piece of wire, bend it into any closed loop you like — a circle, an ellipse, a wobbly potato, a knot. Now walk along it with an infinitely small tangent arrow, and add up every change of direction the arrow makes, counting every wobble as a positive contribution even when the arrow swings back.

The total is a number of radians. Fenchel's theorem, published in 1929, says that number can never be smaller than $2\pi$:

$$\int_\gamma |\kappa| \, ds \;\ge\; 2\pi,$$

with equality **only** when the loop is a convex plane curve. A wire cannot close on itself without turning through at least one full revolution somewhere. There is no way to sneak a closed loop past the arrow without it coming all the way around.

That is a beautiful theorem, and it is usually told as a statement about shape. This article is about the other half of it — the half nobody prints in textbooks — which is that $2\pi$ there is not a numerical fact at all. It is the *unit*. And once you see that, a second thing follows: inside every version of this theorem there sits an **integer**, and an integer cannot be measured.

## What "total curvature" actually is

Curvature is defined as the rate at which the unit tangent turns with respect to arc length:

$$\kappa(s) = \left|\frac{d\mathbf{T}}{ds}\right|, \qquad \mathbf{T}(s) = \frac{d\mathbf{r}}{ds}.$$

So $\kappa \, ds = |d\mathbf{T}|$ — the size of the infinitesimal change in the tangent direction — and the total curvature is literally the length of the path the tangent arrow traces out on the unit sphere. This is why the quantity is an *angle* and not a length, a mass, or a time. It is a sum of small rotations.

$$\mathrm{TC}(\gamma) \;=\; \int_\gamma |\kappa| \, ds \;=\; \int_\gamma \left| d\mathbf{T} \right|.$$

For a circle of radius $R$ the tangent turns uniformly, $\kappa = 1/R$ and $ds = R \, d\theta$, so

$$\mathrm{TC} = \int_0^{2\pi} \frac{1}{R}\,R\,d\theta = 2\pi,$$

independent of $R$. That is the whole arithmetic of the circle case: the $R$ cancels inside the integral, and what remains is the *definition of the angle of one full turn*. Nothing was evaluated about the shape of space. The constant appeared because we chose to call a full turn $2\pi$ radians.

## The measurements that are actually computations

Fenchel's inequality has content — the inequality does bite — and the bite is visible the moment you compute it on curves whose shape is not convex. Because the integral is a pure angle, it can be computed exactly for curves given in polar form $r(\theta)$, where $ds = \sqrt{r^2 + r'^2}\,d\theta$ and

$$\kappa \, ds = \frac{r^2 + 2r'^2 - r\,r''}{r^2 + r'^2}\,d\theta .$$

```python
import mpmath as mp
mp.mp.dps = 30

def total_curvature_polar(r, rp, rpp, a=0, b=2*mp.pi):
    """TC = ∮ |r² + 2r'² − r·r''| / (r² + r'²) dθ   — an angle, never a length."""
    f = lambda th: abs(r(th)**2 + 2*rp(th)**2 - r(th)*rpp(th)) / (r(th)**2 + rp(th)**2)
    pts = [a + (b - a)*mp.mpf(i)/8 for i in range(9)]
    return mp.quad(f, pts)
```

Running that — with analytic derivatives, so no finite-difference error enters — and its space-curve analogue $\int |\mathbf{r}'\times\mathbf{r}''|/|\mathbf{r}'|^2\,dt$ at forty digits gives the following, every figure computed rather than quoted:

| Curve | Total curvature $\int\lvert\kappa\rvert ds$ | In units of $2\pi$ | Signed $\int\kappa\,ds$ |
|---|---|---|---|
| Circle, any radius | $6.28318530717958647692529$ | $1.000000$ | $2\pi$ |
| Ellipse $a=2,\;b=1$ | $6.28318530717958647692529$ | $1.000000$ | $2\pi$ |
| Convex blob $r = 1 + 0.06\cos 3\theta$ | $6.28318530717958647692529$ | $1.000000$ | $2\pi$ |
| Peanut $r = 1 + 0.35\cos 2\theta$ | $7.9415111022281813640548$ | $1.263931$ | $2\pi$ |
| Three-lobed $r = 1 + 0.5\cos 3\theta$ | $15.5129472671369780653962$ | $2.468962$ | $2\pi$ |
| Five-lobed $r = 1 + 0.2\cos 5\theta$ | $17.4184744120391956725962$ | $2.772236$ | $2\pi$ |
| Limaçon $r = 1 + 2\cos\theta$ | $12.5663706143591729538506$ | $2.000000$ | $4\pi$ |
| Three-petal rose $r = \cos 3\theta$ | $25.1327412287183459077011$ | $4.000000$ | $8\pi$ |
| Lissajous eight $(\sin 2t, \sin t)$ | $10.7117801783559484889935$ | $1.704833$ | $0$ |

Read the first three rows together. A circle, a strongly flattened ellipse and a mildly three-lobed but still convex blob are wildly different shapes with wildly different arc lengths and wildly different curvatures point by point — yet all three return the *identical* number, $6.28318530717958647692529$, to twenty-four digits. The identity is not a coincidence of shapes: it is the statement that each of them turns exactly once, and "once" is all the integral can detect.

Read the middle rows. Every one of those wobbly closed curves is *still* a single loop — it winds around once — and every one of them has a signed integral of exactly $2\pi$ while its unsigned integral is strictly larger. Each wobble adds curvature in the direction of travel and then gives the arrow back, and the absolute value refuses to give it back. That gap is Fenchel's inequality doing its job: $2\pi$ is the floor, and non-convexity is the price paid above it.

Read the last three rows, which are the interesting ones.

## The content of the theorem is an integer

The limaçon $r = 1 + 2\cos\theta$ has an inner loop; it turns around twice as you traverse it, and its total curvature is **exactly** $4\pi = 12.566370614359172954$, not approximately. The three-petal rose $r = \cos 3\theta$, traversed once through $[0, 2\pi)$, wraps four times and returns **exactly** $8\pi$. And the Lissajous figure-eight has an unsigned total curvature of $1.704833 \times 2\pi$ — more than one full turn, as Fenchel demands — while its *signed* total curvature is exactly **zero**, because the two lobes are traversed in opposite senses and cancel to the last digit.

This is Whitney's rotation index, and it is the cleanest statement of what these integrals know:

$$\oint_\gamma \kappa \, ds \;=\; 2\pi n, \qquad n \in \mathbb{Z},$$

where $n$ is the turning number — the degree of the tangent map, an integer, computed by counting signed crossings of a direction and nothing else. The unsigned integral is bounded below by $2\pi|n|$ and reaches it only when the curve is convex.

So the theorem has two parts, and they are of completely different kinds:

1. **An integer fact.** A closed loop's tangent winds a whole number of times. No approximation, no constant, no units. A figure-eight winds zero times; a limaçon winds twice.
2. **A unit fact.** We call one winding $2\pi$ radians. The $2\pi$ is a *name* for a turn, and every numerical appearance of the constant in this subject is that name being used.

**A winding number is invisible to any value of $\pi$.** You cannot build an instrument that reports "the loop wound 1.000959 times". Winding is counted, not gauged. Which means: whatever number you assign to the circle constant, every measurement of total curvature in this theorem will agree with you, because the thing measured is an integer and the constant is a notation for the unit in which the answer is written down.

## Knots: where the floor doubles, still to an integer

Fenchel's argument does not need the curve to be planar, and it becomes sharper when the curve is knotted. A knot cannot close without turning at least twice:

$$\mathrm{TC}(\gamma) \ge 4\pi \quad \text{for any knotted closed curve,}$$

proved by Fáry in 1949 and Milnor in 1950, with Milnor's refinement tying the floor to a second integer invariant, the bridge number. Computed here:

| Space curve | Total curvature | In units of $4\pi$ |
|---|---|---|
| Classical trefoil $(\sin t + 2\sin 2t,\ \cos t - 2\cos 2t,\ -\sin 3t)$ | $13.950320176952502232$ | $1.110131$ |
| Torus knot $(2,3)$: $((2+\cos 3t)\cos 2t,\ (2+\cos 3t)\sin 2t,\ \sin 3t)$ | $17.8224124183007973448$ | $1.418263$ |
| Unknotted torus curve $(1,1)$ | $6.707309526425982944$ | $0.533750$ |

The trefoil clears the $4\pi = 12.5663706144$ floor by $1.3839495626$ radians of excess turning — pure waste heat of the knotting, paid in angle. Swap the embedding for a fatter tube and the number changes again: $17.8224$ for the torus-knot embedding of the same knot type. The *bound* is $4\pi$; the *value* depends on how you tie the wire. That is exactly the signature of a geometric inequality rather than a physical law: shape moves the number, the unit does not.

## What happens when the constant is relabelled

Now the question this site always asks. Under Golden Pi, the constant is

$$\hat\pi = \frac{4}{\sqrt\varphi} = 3.1446055110296931443\ldots, \qquad \varphi = \frac{1+\sqrt5}{2},$$

a root of $x^4 + 16x^2 - 256 = 0$, with $\hat\pi^2 = 16/\varphi$ — an algebraic number, where $\pi$ is transcendental by Lindemann's 1882 theorem. What moves in Fenchel's theorem?

**Nothing geometric moves.** Every curve above is the same curve. Every turning number is the same integer. The tomato-shaped peanut still costs $1.263931$ turns of excess curvature, because that ratio is a ratio of angles, and the angle of a turn is not in dispute.

**The numerals move by the recurring first-power gap.** One full turn written in radians becomes

$$2\hat\pi = \frac{8}{\sqrt\varphi} = 6.289211022059386288556, \qquad 2\hat\pi - 2\pi = 0.00602571487979981,$$

a shift of $+0.0959022309\%$; and a turn and a half's worth of knot floor becomes

$$4\hat\pi = \frac{16}{\sqrt\varphi} = 12.57842204411877257711,$$

which is the root of $x^4 + 256x^2 - 65536 = 0$ (verify: $y^4 + 256y^2 - 65536 = 0$ at $y = 16/\sqrt\varphi$ gives a residual of $-1.3\times10^{-26}$ at working precision, i.e. zero). The reciprocals go the other way — the recurring $-0.0958103466\%$, which is the reciprocal gap rather than the same gap:

$$\frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4} = 0.3180049123785172410631, \qquad \frac{\hat\pi}{4} = \frac{1}{\sqrt\varphi} = 0.7861513777574232860696.$$

Those two are worth staring at, because they are the exact algebraic forms of the two most quotable "fractions of a turn" in geometry: a quarter turn and its reciprocal, both expressible in $\sqrt\varphi$ with no transcendental anywhere. Under the conventional constant they are $\pi/4 = 0.7853981633974483096$ and $4/\pi = 1.2732395447351626862$, both transcendental.

And the exact golden ratio inside the geometry — the golden ratio itself, $\varphi = 1.6180339887498948$ — is not affected at all, because it never was a function of the angle unit.

## The honest ledger

Here is what this article will not claim.

**Total curvature cannot adjudicate the constant.** It is an angle measured in a unit that is itself the constant. Change the constant and you have changed the ruler and the report in the same breath: the integral still comes out to one turn, and the numeral differs only because the ruler's name differs. A protractor reports degrees; a degree is $1/360$ of a closed loop; nothing in that pipeline consults a value of $\pi$. This theorem is **structurally blind** — the same verdict as Gauss–Bonnet, spinors, Bertrand's chord paradox and the Airy disk before it in this series.

**What would not be blind.** Exactly one thing in the neighbourhood is a genuine measurand: the ratio of a physical circle's circumference to its radius, $L/R$, which for an ideal circle is $2\pi$ by definition of the radian but for a machined hoop is a length ratio you can hand to a metrologist. Distinguishing the two labels there requires $1$ part in $1043$ — $0.0959\%$ of $6.2832$ is $0.006026$ — which is metrology, not arithmetic, and this article makes no measurement claim about it. The distinction matters: the number $2\pi$ is a *computed* limit of inscribed polygons; a hoop's $L/R$ is a *measured* length ratio and can disagree with the ideal for reasons that have nothing to do with either label (ovality, wire thickness, thermal expansion).

**Where the constant really does survive to first power**, uncancelled, is in formulas where it plays the role of a physical normalisation rather than an angle unit — the tube formulas, for instance. A tube of radius $\rho$ around a closed curve of length $L$ has surface area $2\pi\rho L$ and volume $\pi\rho^2 L$, so $\pi$ appears twice and any ratio you can calibrate is free of it:

$$\frac{A}{V} = \frac{2\pi\rho L}{\pi \rho^2 L} = \frac{2}{\rho} \quad\text{exactly, under either label.}$$

The same happens for the torus: $A = 4\pi^2 R r$, $V = 2\pi^2 R r^2$, and $V/A = r/2$ exactly, with $\pi^2$ cancelling against $\pi^2$. Anything a caliper can check cancels.

**What the label changes is algebra, not geometry.** Under Golden Pi, one turn is $\sqrt{\varphi}$ times one radian-of-curvature in an exact sense: $2\hat\pi\sqrt\varphi = 8$ exactly, and $4/\hat\pi = \sqrt\varphi$. Every radian figure in the tables above keeps its decimal digits if re-expressed in turns, and loses them if re-expressed in radians. That is the entire difference, stated without inflation: the constants $2\pi$ and $2\hat\pi$ name the same closed loop, and one of them is algebraic while the other is not.

## Why this matters beyond a piece of wire

Total curvature is not a curiosity. It is the standard measure of how much a polymer, a DNA minicircle, a filament or a coiled cable must bend to close on itself, and Fenchel's bound is the reason a closed filament always costs at least one full turn of bending direction. It is the subject of the Fáry–Milnor theorem in knot theory, and its space-curve sequel, the Călugăreanu–White formula

$$\mathrm{Lk} = \mathrm{Wr} + \mathrm{Tw}, \qquad \mathrm{Tw} = \frac{1}{2\pi}\oint \tau \, ds,$$

carries the constant in exactly the same way — as the denominator that converts an angle integral into a *count* of twists. Linking number is an integer. Twist is written with $1/2\pi$ precisely so that it can become one. That is not a coincidence of notation; it is the same pattern this series keeps finding: **the constant is what you divide an angle by to get a whole number.**

Fenchel's theorem, in the end, is a theorem about integers wearing an angle's clothes. The $2\pi$ is the costume. Golden Pi changes the costume and leaves the body alone — and the honest conclusion of the whole exercise is that a theorem like this one can never be evidence for either constant, only a demonstration of how thoroughly the constant has been built into the language before the first measurement is even proposed.

*All figures in this article were computed with SymPy-generated analytic derivatives and `mpmath` quadrature at 40 digits of working precision; residuals quoted as "zero" are at the level of that precision, $10^{-24}$ or below.*

## Further Reading

- [Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°](/blog/posts/2026-10-22-descartes-angle-defect-gauss-bonnet-720-degrees-golden-pi/) — the same integer-versus-unit pattern in the curvature of surfaces, where the defect sum is exact and the constant only normalises it.
- [The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — where the radian is defined, and why a half-turn is $2\pi$ rather than something else.
- [Bertrand's Paradox: Why Three Honest Answers to the Same Chord Question Are 1/3, 1/4 and 1/2](/blog/posts/2026-10-24-bertrand-paradox-random-chord-circle-constant-golden-pi/) — a case where the constant cancels out of every probability and survives only in the mean chord.
- [Barbier's Theorem: Curves of Constant Width and Why the Perimeter Is Always πw](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/) — a perimeter theorem where every curve of a given width shares one length, whatever its shape.
- [The Ellipse: Why Its Perimeter Is an Elliptic Integral and Its Area Is Exactly πab](/blog/posts/2026-09-12-ellipse-perimeter-elliptic-integral-computes-circle-constant-golden-pi/) — the curve used in the tables above, where area is a clean product and perimeter is not.
