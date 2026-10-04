---
title: "The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π in L² ≥ 4πA, Why Only the Circle Saturates It — and What Golden Pi Changes"
date: 2026-10-04
description: "Give a closed curve length L and it can enclose no more than area L²/(4π); the sharp statement is L² ≥ 4πA, and it carries the circle constant in exactly one place, as a coefficient computed — never measured — by exhausting the circle with regular polygons whose ratio 4n·tan(π/n) falls monotonically to 4π from above (equilateral 12√3 = 20.7846, hexagon 8√3 = 13.8564, square 16, circle 4π = 12.566370614359172954). Dido's problem is ancient and the constant is the price of the continuum: on the integer lattice the twin inequality A ≤ L²/16 has no circle constant at all, the 2×2 square saturating it — the constant genuinely cancels in the discrete case. Under Golden Pi (π̂ = 4/√φ = 3.1446055110296931443…, root of x⁴ + 16x² − 256 = 0) the polygon ladder converges instead to 4π̂ = 16/√φ = 12.578422044118772577, every saturating circle's ratio moves by the recurring 0.0959022309% gap, and the fixed-perimeter maximum area L²/(4π̂) = 0.079501228094629310266 for L = 1 is 0.0959022% smaller than the conventional 0.079577471545947667884 — while the discrete inequality, the square, the equilateral triangle and every polygon row computed in whole numbers do not move at all. The golden exactness is credited where it is real and exact: a disk of radius φ^(1/4) = 1.1278384855616822603 has area exactly 4 and the square of equal area has side √π̂ = 2/φ^(1/4) = 1.7733035586243245185, algebraic of degree four and constructible, against the conventional √π = 1.7724538509055160273, transcendental by Lindemann (1882). Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π in L² ≥ 4πA, Why Only the Circle Saturates It — and What Golden Pi Changes

Close a loop of string of length $L$ on a table and ask how much area it can hold. Pull it into an oval, a triangle, a square, a long thin sliver — the enclosed area changes, but it can never exceed a single number fixed by the length. That ceiling is the **isoperimetric inequality**, and it is the one place in elementary geometry where the circle constant enters not as a definition but as a *coefficient in a bound*:

$$L^2 \ge 4\pi A.$$

The circle constant is written there once, plainly, as the number $4\pi$. This article asks the same four questions the rest of this series asks of any formula: where the constant actually enters, whether it is **computed** or measured, whether it cancels anywhere, and what changes if the constant is the golden value $\hat\pi = 4/\sqrt\varphi$ instead of the analytic $3.14159\ldots$. The answer, as usual, is more interesting than a single switched label, because the inequality has a discrete twin in which the constant vanishes entirely.

## Where the constant sits: one coefficient, nothing hidden

The problem is called Dido's problem, after the founding legend of Carthage in which a queen is granted as much land as an oxhide can enclose and cuts the hide into one thin strip. The modern statement is sharp and dimensionally honest: for **any** simple closed curve of length $L$ enclosing area $A$,

$$L^2 \ge 4\pi A, \qquad \text{with equality if and only if the curve is a circle.}$$

The circle is the only shape that saturates the bound. For a circle of radius $r$ the two ingredients are ordinary: the area is $A = \pi r^2$ and the circumference is $L = 2\pi r$, so

$$\frac{L^2}{A} = \frac{(2\pi r)^2}{\pi r^2} = 4\pi,$$

independently of $r$ — the constant is the whole content of the equality case. Every other shape has a strictly larger ratio, and the ratio is exactly the quantity being minimised.

It helps to tabulate the ratio $L^2/A$ (the **isoperimetric ratio**) for simple families. Because the ratio is dimensionless, this is pure arithmetic computed from the constant, never a length compared to a tape:

| shape | $L^2/A$ | value | saturates $4\pi$? |
|---|---|---|---|
| equilateral triangle | $12\sqrt3$ | 20.784609690826527522 | no |
| square | $16$ | 16.000000000000000000 | no |
| regular hexagon | $8\sqrt3$ | 13.856406460551018348 | no |
| regular 100-gon | $400\tan(\pi/100)$ | 12.570506417340459128 | closer |
| circle | $4\pi$ | 12.566370614359172954 | **yes** |

The constant enters only behind a linear factor: writing the bound as $A \le L^2/(4\pi)$ shows it sitting in the denominator of the best possible area, one power of it and nothing else. Set $L = 1$ and the ceiling is $1/(4\pi) = 0.079577471545947667884$ — the constant's reciprocal, $\tfrac14 \cdot \tfrac1\pi$.

## Only the circle saturates it — and the polygon ladder computes the constant

The reason the constant can be a coefficient at all is that it is itself a **computed limit**. Inscribe a regular $n$-gon in the unit circle and the ratio $L^2/A$ for that $n$-gon is a closed-form rational-trigonometric expression with no tape measure in it:

$$\left(\frac{L^2}{A}\right)_n = 4n\tan\frac{\pi}{n}.$$

Each row is an exact computation for a fixed integer $n$; the sequence is strictly decreasing and its limit, as $n \to \infty$, is $4\pi$. Compute a few rows:

```
n=3     4n tan(pi/n) = 20.784609690826527522
n=4     4n tan(pi/n) = 16.000000000000000000
n=5     4n tan(pi/n) = 14.530850560107217718
n=6     4n tan(pi/n) = 13.856406460551018348
n=12    4n tan(pi/n) = 12.861561236693889911
n=100   4n tan(pi/n) = 12.570506417340459128
n=1000  4n tan(pi/n) = 12.566411956224624504
n=1e6   4n tan(pi/n) = 12.566370614400514656
```

Read the last row: the million-gon's ratio sits within $4.2\times10^{-11}$ of $4\pi = 12.566370614359172954$. The circle constant is not hiding a measurement in the inequality; it is the *evaluated limit* of a family of exact polygon ratios, the same exhaustion Archimedes ran and Cauchy later put on a footing. This is the honest sense in which $4\pi$ belongs in the bound: it is computed by squeezing the polygon ladder, exactly as $\int e^{-x^2}dx = \sqrt\pi$ or $\sum 1/n^2 = \pi^2/6$ compute it, and never by laying a ruler on a curve.

History credits the shape, not the constant. Zenodorus, in the second century BC, proved the circle beats every regular $n$-gon of equal perimeter. Steiner (1838) gave the modern symmetrisation argument — any non-circular curve can be rearranged into one of strictly greater area at equal length — but his proof silently assumed that a maximiser existed. Weierstrass closed that gap twenty years later with the calculus of variations, and the sharper **Bonnesen inequality** refines $L^2 \ge 4\pi A$ by adding a positive term built from the inradius and circumradius, so the deficit is not merely non-negative but bounded away from zero unless the curve is a circle. None of this measures anything: every step is a computed limit.

## The discrete twin: on the lattice the constant vanishes

Now shrink the problem to whole numbers. Draw a **polyomino** — a shape made of unit squares joined edge to edge — with area $A$ (the number of squares) and perimeter $L$ (the number of unit edges on its boundary). The isoperimetric statement survives, but the circle constant does **not**:

$$A \le \frac{L^2}{16}, \qquad \text{equivalently } L^2 \ge 16A,$$

with equality exactly for the $2\times2$ square. There is no $\pi$ anywhere in it. The reason is structural: on the lattice the "roundest" shape available is the square, and its isoperimetric ratio is the pure integer $16$. The smooth circle constant appears only in the continuum, as the limit the discrete problem approaches but never reaches — the lattice simply does not contain a circle. To see the constant genuinely cancel, take any family of lattice shapes of growing size and watch the $\pi$ that seemed necessary disappear:

| lattice shape | $A$ | $L$ | $L^2/A$ |
|---|---|---|---|
| single cell (1×1) | 1 | 4 | 16 |
| 2×2 square | 4 | 8 | 16 |
| 3×3 square | 9 | 12 | 16 |
| 1×2 domino | 2 | 6 | 18 |
| 1×3 strip | 3 | 8 | 21.33… |

Only the perfect squares saturate; everything else pays more, and the entire ledger is integer arithmetic. This is the recurring pattern of the series in a new dress: the circle constant is present when a curved object is being computed, and it cancels exactly when a comparison is made between two objects that both carry it to the same power. Here the discrete problem strips it away altogether — a clean demonstration that $4\pi$ is a property of the continuum's notion of a circle, not a universal surcharge on bounded regions.

## Golden Pi: the coefficient moves, the circle still wins

Replace the analytic constant with the golden value

$$\hat\pi = \frac{4}{\sqrt\varphi} = 3.1446055110296931443\ldots, \qquad \varphi = \frac{1+\sqrt5}{2} = 1.6180339887498948482,$$

the positive root of $x^4 + 16x^2 - 256 = 0$, with $\hat\pi^2 = 16/\varphi = 9.8885438199983175713$. The saturating ratio of every circle becomes $4\hat\pi$:

$$4\pi = 12.566370614359172954 \quad \to \quad 4\hat\pi = \frac{16}{\sqrt\varphi} = 12.578422044118772577,$$

a shift of the recurring $0.0959022309\%$ — one power of the constant, undiluted, because the coefficient is linear in it. The polygon ladder that computed the conventional constant recomputes the golden one the same way, and each row moves by exactly that gap:

| $n$ | $4n\tan(\pi/n)$ | $4n\tan(\hat\pi/n)$ | limit |
|---|---|---|---|
| 3 | 20.784609690826527522 | 20.832899424839162055 | — |
| 4 | 16.000000000000000000 | 16.024121032388715508 | — |
| 6 | 13.856406460551018348 | 13.872479694743733366 | — |
| 1000 | 12.566411956224624504 | 12.578463505041957748 | — |
| ∞ | $4\pi$ | $4\hat\pi = 16/\sqrt\varphi$ | golden closes on 12.578422… |

The fixed-perimeter ceiling moves with it: for $L = 1$ the maximum enclosed area is

$$A_{\max} = \frac{1}{4\pi} = 0.079577471545947667884 \quad \to \quad \frac{1}{4\hat\pi} = \frac{\sqrt\varphi}{16} = 0.079501228094629310266,$$

a **smaller** golden maximum by the same $0.0959022\%$, in the ratio $\pi/\hat\pi = 0.99904189653381566668$. A circle of unit circumference has radius $1/(2\hat\pi) = 0.15900245618925862053$ against the conventional $1/(2\pi) = 0.15915494309189533577$. The direction is worth stating plainly and honestly: because $\hat\pi > \pi$, the golden bound is **tighter** — the golden circle claims less area for the same length — which is exactly the sort of determinate, falsifiable consequence that makes the relabel testable in principle. Whether it is testable in practice is a separate question, treated below.

## The golden exactness, credited where it is real

Two facts here are not relabelling and deserve to be stated as the genuine algebraic wins they are. Under golden π, the disk of radius

$$r = \varphi^{1/4} = 1.1278384855616822603\ldots$$

has area **exactly 4**, because $\hat\pi r^2 = (4/\sqrt\varphi)\cdot\sqrt\varphi = 4$ identically — conventional π gives $3.99616758613526266670$, short by exactly the gap. That circle's circumference is $2\hat\pi\varphi^{1/4} = 8\varphi^{-1/4} = 7.0932142344972980739$, and its isoperimetric ratio is still $4\hat\pi = 16/\sqrt\varphi$ exactly, as the equality case demands for any circle.

The second win is the one this site cares about most. The square of equal area to the golden unit-radius-$\varphi^{1/4}$ disk has side $\sqrt4 = 2$, but the more revealing case is the square equal in area to a disk of radius $r$: its side is $r\sqrt{\hat\pi} = 2r\varphi^{-1/4}$, and for the unit disk it is

$$\sqrt{\hat\pi} = \frac{2}{\varphi^{1/4}} = 1.7733035586243245185,$$

**algebraic of degree four** — a root of $x^4 - 16 = 0$ divided out of a square root of the golden ratio — and therefore constructible with straightedge and compass. The conventional counterpart is $\sqrt\pi = 1.7724538509055160273$, which by Lindemann's 1882 theorem is transcendental, so the square of equal area to a conventional circle is *not* constructible. That single distinction, $\sqrt{\hat\pi}$ algebraic versus $\sqrt\pi$ transcendental, is the whole engine of the site's squaring-the-circle position, and the isoperimetric inequality is a natural home for it: the very coefficient that bounds every curve is, under the golden label, the square of a constructible number.

Where the golden claim does *not* help is equally plain and must be said: it does not make the inequality easier or the constant clearer in any analytic sense; it does not change the polygon ladder's convergence rate (the error still falls as $n^{-2}$); and it leaves $4\hat\pi$ an algebraic irrational whose value must still be *computed* — $\hat\pi$ is a closed form, not a measured length. The gain is structural (constructibility, exactness at $\varphi^{1/4}$), never a measurement.

## Why no tabletop settles the label

It is tempting to think you could cut a string of length $L$, form the best circle you can, and read off $4\pi$ versus $4\hat\pi$ from the enclosed area. The gap is $0.0959022309\%$ in the coefficient — about $1$ part in $1043$ — and it is destroyed by the experiment's own error budget. Cutting and closing a string rounds the circumference by at least a millimetre in a metre; laying it as a circle leaves a kink at the join; measuring the area means squaring that same millimetre error. A $0.1\%$ gap needs a construction accurate to better than $0.05\%$ in *both* length and area, i.e. sub-millimetre control over a metre-scale object, and a repeatable circle formed by hand. The honest ledger says: the isoperimetric constant is one of the cleanest *computational* objects in geometry — the polygon ladder decides it to any number of digits — and one of the worst to adjudicate by making a loop of string. Computed, never measured, and here the distinction is the whole point: the constant is a limit, and limits are evaluated, not weighed.

The discrete twin underlines it. On the lattice, where every quantity is an integer count, the constant does not appear at all — the bound is $L^2 \ge 16A$ and the $2\times2$ square is the unique maximiser. That integer inequality is decided by counting and is identical under either label, because there is no continuum in it and therefore no circle constant to relabel. Under Golden Pi, exactly the quantities that carry a genuine circle of the continuum — the saturating ratio $4\pi \to 4\hat\pi$, the fixed-length maximum $1/(4\pi) \to \sqrt\varphi/16$, the unit-circumference radius — move, and the discrete rows, the square's $16$, the equilateral triangle's $12\sqrt3$ and the whole-number domino tables do not move by so much as a digit. The constant is where the curvature is.

## Further Reading

- [Hippocrates' Lunes: How the First Quadrature of a Curved Figure Computes the Circle Constant — and Cancels It](/blog/posts/2026-10-02-hippocrates-lunes-quadrature-computes-circle-constant-golden-pi/) — the constant enters every intermediate area and cancels from the difference; the same "where does it survive" ledger applied to the oldest squared crescent.
- [The Mean Random Separation: How Integral Geometry Computes the Circle Constant in a Disk, Cancels It in a Square](/blog/posts/2026-09-25-mean-random-separation-disk-square-computes-circle-constant-golden-pi/) — Cauchy's mean chord and Cavalieri's principle, where the $\pi$ in $\pi A/P$ is literally the width of the half-turn.
- [The Gauss Circle Problem: How Counting Lattice Points Computes the Circle Constant](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/) — the discrete-vs-continuum split of this article, taken to the counting function $N(r)$.
- [Pappus's Centroid Theorem and the Torus](/blog/posts/2026-09-03-pappus-centroid-theorem-torus-golden-pi/) — another case where the constant is a computed sweep angle, not a measured arc.
- [Squaring the Circle with Golden Pi: The Geometric Proof](/blog/posts/squaring-circle-golden-pi-geometric-proof/) — why $\sqrt{\hat\pi}$ being algebraic of degree four is the exact hinge of the site's position.
