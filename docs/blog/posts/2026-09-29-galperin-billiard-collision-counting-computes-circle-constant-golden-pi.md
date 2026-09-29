---
title: "Galperin's Billiard: How Counting Elastic Collisions Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-09-29
description: "A block, a smaller block, and a wall: with a mass ratio of exactly 100^(n−1), the number of perfectly elastic collisions is the first n digits of π — 3, 31, 314, 3141, reproduced here with exact rational arithmetic and zero free parameters. This article follows where the circle constant actually lives in that machine. The masses, velocities and impact times are all rationals; the constant enters only as the half-turn that ends the sweep in velocity space, θ = arctan√(m/M) and N = ⌈π/θ⌉ − 1, so it is computed — an arctangent of a ratio and a sweep ceiling — never measured. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the same machine returns a different integer: 4, 31, 314, 3144, 31446, 314460, 3144605, with the count shortfall equal to the recurring 0.0959022% gap times the count itself (3.012 at a mass ratio of 10⁶, 301.29 at 10¹⁰, 3012.86 at 10¹²). Unlike most settings in this series the label is not free here — the count is a dimensionless integer built from a pure ratio, so the billiard does discriminate in principle — and that is exactly why the honest ledger has to be kept: turning it into a measurement means trusting the elasticity of 3.14 million real impacts, and no apparatus does that."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Galperin's Billiard: How Counting Elastic Collisions Computes the Circle Constant, and What Golden Pi Changes

Every article in this series so far has taken a formula — a series, a product, an integral, a polynomial identity — and asked what the circle constant does inside it. This one takes something stranger: a *machine* whose only output is an integer, and whose integer is the digit string of π. There is no summation, no limit notation, no symbol π anywhere in its input. There is a wall, a small block, a large block, and the rule of perfectly elastic collision. Count the impacts and the count is 3.14159…

The construction is due to G. Galperin, who published it as *Playing Pool with π (The number π from a billiard point of view)* in **Regular and Chaotic Dynamics 8(4), 2003, pp. 375–394**. It is the cleanest case in the whole literature of the question this blog keeps asking: **is the circle constant inside the physics, or is it inside the angle we use to describe the physics?** Here the answer is unusually sharp, because the machine's output is a countable integer and the machine's inputs are ratios of masses — pure numbers with no units and no instrument anywhere.

## The apparatus: one wall, two blocks, no ruler

The setup is one-dimensional and deliberately bare. A wall sits at the origin. A small block of mass $m$ sits between the wall and a large block of mass $M$. The large block moves toward the wall at speed $v$; the small block is at rest. Everything is frictionless, everything is perfectly elastic, and the blocks are treated as point masses — so the small block may touch the wall and be reflected with no loss.

With $M = 1$ and $m = 1$ the run is trivial: the blocks meet, exchange velocities, the small block bounces off the wall, comes back, meets the large block a second time, and both then travel away to the right forever. Three collisions. The integer is $3$.

Scale the large block up and the count grows into a digit string. The rule is: set the mass ratio to exactly

$$M/m = 100^{\,n-1},$$

and the number of collisions before the two blocks separate permanently is the integer formed by the **first $n$ digits of π**. A mass ratio of 1 (that is, $n=1$) gives 3 collisions; 100 gives 31; 10 000 gives 314; 1 000 000 gives 3141. The growth is by a factor of ten per digit, which is why nobody has pushed this very far, and why its interest is structural rather than computational.

## Velocity space turns the impacts into a rotation

The reason the count is a constant-bearing string and not just a big number is that the whole collision sequence is a **rotation**. Energy conservation in a two-body problem with a wall is enough to see it.

Write the velocities in scaled coordinates

$$u_1 = \sqrt{M}\,v_1, \qquad u_2 = \sqrt{m}\,v_2 .$$

The kinetic energy is $E = \tfrac12(u_1^2 + u_2^2)$, so the point $(u_1,u_2)$ is pinned to a **circle** of radius $\sqrt{2E}$ for the entire history: no collision can move it off, because every collision conserves energy. What a collision does is *reflect* the point in one of two lines through the origin:

- the **wall** impact reflects $(u_1,u_2)$ in the line $u_2 = 0$ (the large block is untouched);
- the **block–block** impact reflects it in the line perpendicular to $(\sqrt M, -\sqrt m)$, which is the momentum-conservation direction.

Those two mirror lines meet at the angle

$$\theta = \arctan\sqrt{m/M},$$

and this single angle is the whole content of the machine. Unroll the reflections — the standard trick for a point bouncing inside a wedge — and the zig-zag becomes a straight ray sweeping a wedge of opening angle $\theta$. The ray escapes the wedge once the total swept angle reaches a half-turn. So the number of reflections is the number of whole steps of size $\theta$ that fit into $\pi$:

$$N = \left\lceil \frac{\pi}{\theta} \right\rceil - 1, \qquad \theta = \arctan\sqrt{m/M}.$$

That is the entire theorem. The circle constant enters in exactly one place — as the **ceiling of the sweep**, the half-turn — and nowhere else. Not in the masses, not in the velocities, not in the impact times.

## The count reproduces the digits

The formula is not an approximation. With the mass ratio a power of a hundred, $\pi/\theta$ lands just short of an integer and the ceiling does the digit extraction. Running the dynamics directly — exact rational arithmetic, simultaneous-event handling, no floating point in the collision law — reproduces the published string with **zero free parameters**:

| $n$ | $M/m = 100^{\,n-1}$ | $\theta = \arctan\sqrt{m/M}$ | $\pi/\theta$ | collisions (simulated) | first $n$ digits of π |
|---|---|---|---|---|---|
| 1 | 1 | 0.785398163397448 | 4.000000000 | **3** | 3 |
| 2 | 100 | 0.099668652491162 | 31.523872 | **31** | 31 |
| 3 | 10 000 | 0.009999666686665 | 314.168205 | **314** | 314 |
| 4 | 1 000 000 | 0.000999999666667 | 3141.593701 | **3141** | 3141 |
| 5 | 100 000 000 | 0.000099999999667 | 31415.555258 | 31415 | 31415 |
| 6 | 10 000 000 000 | 0.000009999999999667 | 314159.206441 | 314159 | 314159 |

The rows through $n = 4$ were simulated event by event with `fractions.Fraction` masses and velocities; the larger rows follow from the identical formula. The mechanism is visible in the small case. For $M = m$ the four impacts are:

```text
# n = 1,  M = m = 1,  no free parameters
1  block-block   v1 =  0.000000000   v2 = -1.000000000
2  wall          v1 =  0.000000000   v2 = +1.000000000
3  block-block   v1 =  1.000000000   v2 =  0.000000000   <- both moving right
```

Three impacts, and the machine stops. Note what is *not* there: at no point is any quantity irrational. Every velocity, every impact time, and the mass ratio itself are rationals, all the way through. The only irrational object in the entire run is the half-turn used to decide when the sweep ends.

The $n = 2$ case shows the mechanism at work — mass ratio 100, thirty-one impacts, with the small block's speed climbing as it is repeatedly kicked:

| # | event | $v_1$ | $v_2$ |
|---|---|---|---|
| 1 | block–block | −0.980198 | −1.980198 |
| 2 | wall | −0.980198 | +1.980198 |
| 3 | block–block | −0.921576 | −3.881972 |
| 9 | block–block | −0.543088 | −8.396761 |
| 11 | block–block | −0.366061 | −9.305909 |

The velocity vector never leaves its energy circle: $|u| = \sqrt{M} = 10$ throughout that run, and at $M/m = 10^6$ it reaches $\sqrt M = 1000$, which is why the small block's largest recorded speed there is $999.999683$ — just under the circle's radius, as it must be. The whole history is one point circling a rational radius, ticking off an integer number of reflections.

## The honest ledger: computed, never measured

This blog's standing rule is that the circle constant is **computed or evaluated, never measured** — only genuine physical measurands (the fine-structure constant, a physical length, a ratio of forces) are measured. Galperin's billiard sits on the computed side of that line, and it is worth being precise about why, because the machine *looks* physical.

- The angle $\theta$ is not read off any protractor. It is $\arctan$ of a **pure ratio of masses**, an algebraic input chosen by the designer.
- The count $N$ is not a reading either. Given the inputs, it is the output of integer arithmetic on rationals.
- The half-turn that terminates the sweep is the *only* place the constant appears, and it appears as a **ceiling** — the same role it plays as an integration limit in the ellipse's perimeter, not as a physical quantity anyone gauged.

In other words: the billiard computes π the way a spigot computes digits — from arithmetic alone. And there is a real, verified distinction to keep honest here. In the Kepler's-third-law case this series covered earlier, a genuine measurement ($GM_\odot$, the au, the year) *fixes* the constant and rules the golden label out by about 7 400×. Galperin's billiard is different in kind: because the count is a dimensionless integer built from a dimensionless ratio, the machine **does** discriminate between labels in principle — and that makes the next section a calculation rather than a footnote.

## The golden relabel

Under Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$, with $\varphi = (1+\sqrt5)/2$, the machine is unchanged — same masses, same elasticity, same wall — and only its ceiling moves. Because $\hat\pi^2 = 16/\varphi = 8(\sqrt5-1) = 9.888543820\ldots$ and $\hat\pi = 4/\sqrt\varphi$ are exact in the golden field (and $1/\hat\pi = \sqrt\varphi/4 = 0.3180049123785172\ldots$), the relabelled count is still an integer string, just a different one:

| $n$ | $M/m$ | π-count ⌈π/θ⌉−1 | π̂-count ⌈π̂/θ⌉−1 | difference | difference ÷ count |
|---|---|---|---|---|---|
| 1 | 1 | 3 | **4** | 1 | 0.333 |
| 2 | 100 | 31 | 31 | 0 | 0 |
| 3 | 10 000 | 314 | 314 | 0 | 0 |
| 4 | 1 000 000 | 3141 | **3144** | 3 | 3.01229 |
| 5 | 10⁸ | 31415 | **31446** | 31 | 30.12769 |
| 6 | 10¹⁰ | 314159 | **314460** | 301 | 301.28549 |
| 7 | 10¹² | 3141592 | **3144605** | 3013 | 3012.85681 |

The pattern is exact and worth stating plainly. The count is proportional to the constant, so the golden relabel's shortfall in collisions is precisely

$$\Delta N = N\cdot\frac{\hat\pi-\pi}{\pi} = N \times 0.000959022308782\ldots,$$

the recurring **0.0959022% gap** carried undiluted into a discrete tally, because here the constant enters to the first power with no square root and no dilution. At $n=4$ that is $3141 \times 0.0959022\% = 3.012$ collisions; at $n=6$ it is $301.29$; at $n=7$ it is $3012.86$. The relabelled strings themselves are the digits of the relabelled constant: read off $\hat\pi = 3.144605511\ldots$ and you get 3, 31, 314, 3144, 31446, 314460, 3144605 — the golden machine is a digit extractor for whatever constant you put in its ceiling. Nothing about the masses, the wall, or the elasticity distinguishes the two runs; only the half-turn does.

## What would it take to settle it physically?

This is where the series' honesty rule bites hardest, because the answer is not "nothing".

A real walk-away count at $n = 4$ needs $10^6$ impacts with **perfect elasticity at every single one**. Any dissipation is not a small perturbation to the count; it changes $\theta$, and $\theta$ is the divisor in $N = \lceil \pi/\theta\rceil - 1$. The margin is razor-thin exactly where the digits are: at $n = 4$, $\pi/\theta = 3141.5937$ sits only $0.4063$ of a step below the next integer, so an error of order $1.3\times10^{-4}$ in $\theta$ already flips a count. To reach the six digits at $n = 6$ you must be sure you missed none of $314\,159$ impacts, that the wall is exactly perpendicular, that the blocks never rotate or deform, and that the coefficient of restitution is one to better than a part in $10^{4}$ across three hundred thousand collisions. No bench does that. The billiard is therefore a beautiful **computation** and a hopeless **experiment** — which is precisely the boundary this site keeps drawing, and precisely why the digit string is evidence about arithmetic, not about the world.

There is one more honest asymmetry to note, in the site's favour and against it. In favour: the golden machine's counts are internally consistent, its $\hat\pi$ is algebraic and its digit extraction works exactly as well as the classical one — the relabelled constant is not a broken object, it is a different exact object. Against: the classical machine's output is fixed by the same ceiling that fixes every other computed appearance of the constant in this series — the quarter-turn in the arctangent, the half-turn in the sweep, the sphere's $4\pi$ steradians, the $\pi^4/15$ of the Planck integral — and all of those agree with a single computed value, $3.14159265358979323846\ldots$, at the same time. A relabel must move all of them together, and the count moves with them: 3141 becomes 3144.

Computed, never measured. The blocks are honest, the arithmetic is exact, and the only thing the tally measures is the ceiling we chose to sweep against.

## Further Reading

- [**Gabriel's Horn: How an Improper Integral Computes the Circle Constant Inside a Finite Volume, and What Golden Pi Changes**](/blog/posts/2026-09-28-gabriels-horn-improper-integral-computes-circle-constant-golden-pi/)
- [**The Gauss Circle Problem: How Counting Lattice Points Computes the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/)
- [**Buffon's Needle: How a Tossed Needle Estimates the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-09-10-buffon-needle-geometric-probability-estimates-circle-constant-golden-pi/)
- [**Kepler's Third Law: How the Circle Constant Enters Celestial Mechanics as 4π², and What Golden Pi Changes**](/blog/posts/2026-09-22-keplers-third-law-orbital-mechanics-compute-circle-constant-golden-pi/)
- [**The Roots of Unity: How the Complex Solutions of zⁿ = 1 Compute the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-09-09-roots-of-unity-compute-circle-constant-golden-pi/)
