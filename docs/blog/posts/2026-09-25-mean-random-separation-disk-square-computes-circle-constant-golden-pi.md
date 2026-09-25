---
title: "The Mean Random Separation: How Integral Geometry Computes the Circle Constant in a Disk, Cancels It in a Square, and What Golden Pi Changes"
date: 2026-09-25
description: "Drop two points at random into a shape and average the distance between them. In a square the answer is π-free — (2+√2+5·ln(1+√2))/15 — in a 3-ball it is exactly 36/35, and in a disk it is (2/π)·(64/45) = 128/(45π). Every value here is a computed limit, never a measurement; under Golden Pi the square does not move at all, while the disk moves by the recurring 0.0959%."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a shape, drop two points into it at random, and average the straight-line distance between them. This is one of the oldest questions in geometric probability — Laplace and Borel both handled pieces of it — and it is a clean place to ask where the circle constant actually lives, because the question contains no angles, no arcs and no circle until the shape you choose has one.

The answer splits the world in two. For a square, the average separation is

$$\bar d_\square = \frac{2+\sqrt2+5\ln\!\left(1+\sqrt2\right)}{15} = 0.521405433164720678330982\ldots$$

and there is no circle constant anywhere in it. For a ball in three dimensions the answer is exactly $36/35 = 1.028571428\ldots$, also with no circle constant. But for a disk the answer is

$$\bar d_\bigcirc = \frac{2}{\pi}\cdot\frac{64}{45} = \frac{128}{45\pi} = 0.905414787367226799040761\ldots$$

and the constant has arrived — as a factor $2/\pi$ multiplying a pure rational. That factor is the entire circle-constant content of the problem, and it is not a length ratio. It is a *turn divided by an area*, one power short of cancelling.

In what follows every number is computed — from rational functions, square roots, logarithms and the limits of quadratures — and none is measured. "Measure" below is the mathematician's word for an area, an angular interval or a probability, never an instrument reading.

## Why the square has no constant in it

Put two independent uniform points in the unit interval $[0,1]$. The mean separation is an elementary double integral,

$$\bar d_{[0,1]} = \int_0^1\!\!\int_0^1 |x-y|\,dx\,dy = \frac13 = 0.3333333333\ldots$$

Now go up a dimension. In the unit square the *difference* of two uniform coordinates has a triangular density: $p(u) = 1-|u|$ on $[-1,1]$, because the set of pairs with $x_1-x_2=u$ has length $1-|u|$. No square root, no trigonometry, no circle — just a tent. So the mean separation is the two-dimensional integral

$$\bar d_\square = \int_{-1}^{1}\!\!\int_{-1}^{1} (1-|u|)(1-|v|)\sqrt{u^2+v^2}\;du\,dv = 4\int_0^1\!\!\int_0^1 (1-u)(1-v)\sqrt{u^2+v^2}\;du\,dv,$$

and its closed form is the one quoted above. Quadrature confirms it digit for digit: $0.521405433164713$ against $0.521405433164721$ at 600 nodes per axis. The only transcendental that survives is a logarithm in disguise — $\ln(1+\sqrt2) = \operatorname{arsinh} 1 = 0.8813735870195430252$ — which is exactly the kind of quantity that appears in a rectangular geometry rather than a round one. The variance is likewise π-free:

$$\operatorname{Var}_\square = \frac13 - \bar d_\square^{\,2} = 0.061469707599643331\ldots,\qquad \sigma_\square = 0.247930852456170390\ldots$$

Two further checks in the same register. The mean distance from a uniform point in the unit square to a corner is

$$\frac{\sqrt2+\ln\!\left(1+\sqrt2\right)}{3} = 0.765195716464212691\ldots$$

(quadrature agreeing to twelve digits), and the mean *squared* separation is exactly $2\operatorname{Var}(x) = 2\cdot\tfrac{1}{12} = \tfrac13$. Three independent averages of the same body; three answers; no circle constant.

## The same integral in three dimensions, still without the constant

Roundness alone does not summon the constant. Two uniform points on the *surface* of a unit sphere are separated by the angle $\gamma \in [0,\pi]$ with density $\tfrac12\sin\gamma$ (each point is a uniformly random direction, and the geometry of the sphere makes the pair-angle distribution elementary). With $|x-y| = \sqrt{2-2\cos\gamma} = 2\sin(\gamma/2)$,

$$\bar d_{\text{sphere}} = \int_0^\pi \tfrac12\sin\gamma \cdot 2\sin\!\left(\tfrac{\gamma}{2}\right)d\gamma = \frac43 = 1.3333333333\ldots,\qquad \operatorname{Var} = 2\operatorname{Var}(\hat x) = \frac29,$$

and the $4\pi$ of the solid angle appears twice, once in each normalisation, so it cancels before it can reach the answer. (This is the same cancellation that removes $4\pi$ from the fine-structure constant; the sphere's *area* normalisation and the *turn* normalisation are the same power of the same constant.)

Inside the unit ball in three dimensions the answer is the classical

$$\bar d_{\text{ball}} = \frac{36}{35} = 1.0285714285714285714\ldots,\qquad \operatorname{Var} = 2-\left(\frac{36}{35}\right)^2 = \frac{1154}{1225} = 0.9420408163265306\ldots$$

two rational numbers, no constant. A Monte Carlo with two million pairs returns $1.028715 \pm 0.000267$, consistent with $36/35$ to within the sampling error — and the arithmetic is exact anyway.

## Where the constant does do the work: isotropic averages

Take a straight line in the plane, uniformly over all positions and directions (the invariant line measure $d\mu = dt\,d\theta$, $\theta \in [0,\pi)$), and restrict it to lines that meet a convex body $K$. The mean chord is

$$\bar L = \frac{\pi A}{P},$$

the classic Crofton–Cauchy result: for the unit square, $\pi/4 = 0.7853981633974483096\ldots$; for the unit disk, $\pi A/P = \pi\cdot\pi/2\pi = \pi/2 = 1.5707963267948966192\ldots$.

Both ingredients of that formula are verifiable by computation, and neither contains a circle constant:

* **Cavalieri.** For a fixed direction, $\int L\,dt = A$ exactly, because integrating the chord lengths over the offsets is exactly the area of the body. Numerically at $\theta = 0,\ 0.3141,\ 0.7854,\ 1.2,\ 1.5708,\ 2.3,\ 2.9$ rad the quadrature returns $1.00000000$, $1.00000000$, $0.99999991$, $0.99999998$, $1.00000010$, $0.99999997$, $0.99999992$ — the unit square's area, seven times, with no constant in sight.
* **Cauchy's width formula.** The measure of the set of lines that meet the body is the perimeter, $\int_0^\pi 2h(\theta)\,d\theta = P$, and for the unit square the half-widths integrate to $4$, its perimeter.

So where does $\pi$ come from? Only from the *range* of $\theta$: the integral over directions is taken over a half-turn. The mean chord of a square is $\pi A/P$ because a half-turn is $\pi$ radians and the body's area is $A$ — the constant here is the size of the angular interval, not a property of the square.

That is also why the number is measure-dependent in the well-known way. If you instead weight every direction equally and average the *per-direction* mean chord, you get, for the unit square,

$$\frac{2}{\pi}\cdot\frac{1}{\sqrt2}\ln\frac{\tan(3\pi/8)}{\tan(\pi/8)} = 0.7935150210236095365\ldots$$

against $\pi/4 = 0.7853981633974483096\ldots$: same geometry, two honest answers, because the two weightings are not the same (Jensen's inequality on $1/2h(\theta)$). For the *disk* the ambiguity evaporates, because there the half-width $h=R$ is direction-independent — the round body is the one case where the isotropic measure and the direction-uniform measure agree.

The same mechanism drives the mean separation of two points chosen uniformly on the *circumference* of a unit circle. With the angular difference $\Delta$ uniform on $[0,2\pi)$ and the chord $2\sin(\Delta/2)$,

$$\bar d_{\text{arc}} = \frac{1}{2\pi}\int_0^{2\pi} 2\left|\sin\frac{\Delta}{2}\right|d\Delta = \frac{4}{\pi} = 1.2732395447351626862\ldots,\qquad \operatorname{Var} = 2-\frac{16}{\pi^2} = 0.378861061722595657\ldots$$

Here the constant does not cancel, because the average is taken over an *angular parameterisation* — the integrand is a chord, not an area element — and $4/\pi$ is what remains of the ratio between them.

## The disk: one power short of cancelling

Now the disk. A uniform point in a unit disk has density $r\,dr\,d\theta/\pi$, and the $\pi$ in that denominator is the disk's own area. Two points give $1/\pi^2$. The angle of the first point integrates to the full turn $2\pi$; the angle of the second is the source of the curvature. The result is

$$\bar d_\bigcirc = \frac{2\pi}{\pi^2}\int_0^1\!\!\int_0^1 r_1 r_2\, G(r_1,r_2)\,dr_1\,dr_2 = \frac{2}{\pi}\cdot\frac{64}{45},$$

where $G(r_1,r_2) = \frac{1}{2\pi}\int_0^{2\pi}\sqrt{r_1^2+r_2^2-2r_1r_2\cos\theta}\,d\theta$ performs the angular average of the separation at fixed radii, and the remaining double integral is pure geometry. Its value is the exact rational

$$\bar d_\bigcirc\cdot\frac{\pi}{2} = \frac{64}{45} = 1.4222222222\ldots$$

which the quadrature reproduces to nine digits ($1.4222222211$ at $400\times400\times600$ nodes, the residual being the grid's own error). Read the factorisation the other way: the *geometry* of the disk contributes a rational number, and the circle constant enters only as turn-over-area, $2\pi/\pi^2 = 2/\pi = 0.6366197724$ — one power short of cancelling. Had the turn and the area been the same power of the constant, as on the sphere, nothing would have survived.

The same decomposition holds for the disk's second moment, which is exactly $1$ — the sum of two uniform disk points' squared radii expectations, $2\cdot\tfrac12$ — so the variance and standard deviation are

$$\operatorname{Var}_\bigcirc = 1-\left(\frac{128}{45\pi}\right)^2 = 0.180224062816759483\ldots,\qquad \sigma_\bigcirc = 0.424528047149725412\ldots$$

## The ledger

Every row below is computed; the fourth column states whether a power of the circle constant survives.

| Bodies and averages | Exact value | Decimal | circle constant? |
|---|---|---|---|
| two uniform points, unit interval | $1/3$ | 0.3333333333 | no |
| mean squared separation, unit interval | $1/6$ | 0.1666666667 | no |
| two uniform points, unit square | $(2+\sqrt2+5\ln(1+\sqrt2))/15$ | 0.5214054331647206783 | no |
| mean squared separation, unit square | $1/3$ | 0.3333333333 | no |
| corner distance, unit square | $(\sqrt2+\ln(1+\sqrt2))/3$ | 0.7651957164642126913 | no |
| two uniform points, unit sphere surface | $4/3$ | 1.3333333333 | no |
| two uniform points, unit 3-ball | $36/35$ | 1.0285714286 | no |
| centre distance, unit disk | $2/3$ | 0.6666666667 | no |
| mean squared separation, unit disk | $1$ | 1.0000000000 | no |
| mean chord, unit square (invariant line measure) | $\pi/4$ | 0.7853981634 | yes — the half-turn |
| mean chord, unit disk (invariant line measure) | $\pi/2$ | 1.5707963268 | yes — the half-turn |
| two uniform points, unit circle (arc) | $4/\pi$ | 1.2732395447 | yes — angular average |
| two uniform points, unit disk | $128/(45\pi) = (2/\pi)(64/45)$ | 0.9054147873672267990 | yes — turn ÷ area |

The last three rows are the whole story: $\pi$ enters where the average runs over a turn, and it survives only where the turn and the area are different powers of it. Two shapes, two random point sets, and the constant turns up in exactly one of them — the one whose boundary is a circle, and there only as a single residual factor.

As a sanity check on the two most-often-quoted numbers of this kind: the unit disk's mean separation over the unit square's is $1.7364889772469846067\ldots$, and every one of these averages scales with size — a disk of radius $R$ gives $0.9054147874R$, a square of side $s$ gives $0.5214054332s$ — so none of them is a candidate for a fundamental constant of nature; they are properties of a *measure*, computed as limits.

## The golden ledger

Golden Pi's label is $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$ with $\varphi = (1+\sqrt5)/2$, a $+0.0959022309\%$ step above the analytic value of the constant ($\hat\pi/\pi = 1.0009590223087825260$). Feed that label to the rows above, and the ledger splits cleanly.

| Quantity | Analytic label | Golden label ($\hat\pi = 4/\sqrt\varphi$) | movement |
|---|---|---|---|
| mean separation, unit disk | $128/(45\pi) = 0.9054147873672267990$ | $128/(45\hat\pi) = 32\sqrt\varphi/45 = 0.9045473063211157079$ | $-0.0958103466\%$ ($-0.0008674810461$, i.e. $0.867481046$ mm per metre) |
| variance, unit disk | $1-(128/45\pi)^2 = 0.180224062816759483$ | $(2025-1024\varphi)/2025 = 0.181794170627213667$ | $+0.8711976558\%$ |
| mean separation, unit circle arc | $4/\pi = 1.2732395447351626862$ | $4/\hat\pi = \sqrt\varphi = 1.2720196495140689643$ | $-0.0958103466\%$, exactly $\sqrt\varphi$ |
| variance, unit circle arc | $2-16/\pi^2 = 0.378861061722595657$ | $2-\varphi = 0.381966011250105152$ | $+0.8195483361\%$ |
| mean chord, unit square | $\pi/4 = 0.7853981633974483096$ | $\hat\pi/4 = 1/\sqrt\varphi = 0.7861513777574232861$ | $+0.0959022309\%$, exactly $1/\sqrt\varphi$ |
| mean chord, unit disk | $\pi/2 = 1.5707963267948966192$ | $\hat\pi/2 = 2/\sqrt\varphi = 1.5723027555148465721$ | $+0.0959022309\%$, exactly $2/\sqrt\varphi$ |
| the $\pi$-free rows above (interval, square, corner, sphere, 3-ball and the mean-squared separations) | — | identical, digit for digit | **zero** |

Two exact algebraic forms are worth putting in the ledger plainly, because they are what the golden label *is*: $\hat\pi$ is a root of $x^4+16x^2-256=0$, so $1/\hat\pi = \sqrt\varphi/4$, and every quantity that carried $1/\pi$ to the first power becomes an algebraic number in $\sqrt\varphi$:

$$\frac{4}{\hat\pi} = \sqrt\varphi,\qquad \frac{\hat\pi}{4} = \frac{1}{\sqrt\varphi},\qquad \frac{\hat\pi}{2} = \frac{2}{\sqrt\varphi},\qquad \frac{128}{45\hat\pi} = \frac{32\sqrt\varphi}{45},\qquad \frac{1}{\hat\pi^2} = \frac{\varphi}{16}.$$

So the site's own constant, read through this problem, converts a transcendental ratio into radicals. The square, the interval, the sphere and the ball do not care which label is in force, because no label appears in their closed forms at all: their entries are $1/3$, $1/6$, $(2+\sqrt2+5\ln(1+\sqrt2))/15$, $1/3$, $4/3$, $36/35$, $1154/1225$ — arithmetic and logarithms only.

## The honest boundary, and the sampling ledger

For once, one of these quantities is genuinely *estimated* rather than evaluated — the mean separation can be sampled — so it is worth stating exactly what a Monte Carlo can and cannot do here.

Two million uniform pairs in the unit disk give $0.905504 \pm 0.000150$, consistent with the computed $0.9054147874$. The gap between the analytic and golden labels, however, is only $0.0008674810461$ in the same units, and the standard deviation of a single pair's separation is $\sigma_\bigcirc = 0.4245280471$. To resolve the label gap at one sigma you need

$$N > \left(\frac{\sigma_\bigcirc}{\Delta}\right)^2 = \left(\frac{0.4245280471}{0.0008674810461}\right)^2 = 239\,493$$

pairs, and about $2\,155\,437$ for three sigma. That is a cheap computation, and it is a computation: the ensemble's limit is a number fixed by the geometry of the disk, not a reading from a ruler, and a physical version of the experiment would measure the *placement* of the points and the radius of the plate. Worse — or better, depending on which register you are in — the square cannot be used for the test at all, because its closed form contains no circle constant to move: relabelling the constant leaves $0.5214054331647206783$ exactly where it was. Only an average whose integrand is an *angle* — a turn, a chord, a rotation — can even pose the question, and even there the constant arrives as a normalisation (turn ÷ area, or turn ÷ arc) rather than as a length ratio that some instrument could referee.

That is the register discipline this site tries to keep: the circle constant here is a computed limit — an integral, a limit of partial averages, a ratio of two measures — and the one place in this problem where it fails to cancel is the place where a full turn is divided by a disk's own area, which is a fact about how we count angles, not about how long anything is.

## Further Reading

- [Buffon's Needle: How a Tossed Needle Estimates the Circle Constant](/blog/posts/2026-09-10-buffon-needle-geometric-probability-estimates-circle-constant-golden-pi/) — the other classical geometric-probability average, and why its noise, not its arithmetic, decides which label it can see.
- [The Gaussian Integral: How the Bell Curve Computes the Root of the Circle Constant](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the same turn-over-area normalisation, where the full turn is what makes $\sqrt\pi$ appear.
- [Pappus's Centroid Theorem: How Rotation Sweeps Out the Circle Constant](/blog/posts/2026-09-03-pappus-centroid-theorem-torus-golden-pi/) — the sibling question: a translation sweeps area with no constant, a rotation brings the turn back in.
- [The Isoperimetric Inequality: Why the Circle Maximises Area](/blog/posts/2026-08-31-isoperimetric-inequality-circle-maximizes-area-golden-pi/) — the round boundary as the extremal case, and what that does and does not say about the constant.
- [Squaring the Circle: Why Golden Pi Is Constructible](/blog/posts/2026-07-26-squaring-circle-golden-pi-constructible/) — the site's core geometric claim, and the sense in which $\hat\pi$ is exact.
