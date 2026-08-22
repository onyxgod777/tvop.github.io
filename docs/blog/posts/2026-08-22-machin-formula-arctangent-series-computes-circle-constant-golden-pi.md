---
title: "Machin's Formula: How the Arctangent Series Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-08-22
description: "Machin's 1706 identity π/4 = 4·arctan(1/5) − arctan(1/239) computes the circle constant as the limit of an arctangent series — computed, never measured. Because arctangent values are pure angle sums that do not depend on the circle constant, the same identity under Golden Pi (π̂ = 4/√φ = 3.1446055…) becomes π̂/4 = 1/√φ, an exact algebraic number in the golden field, carrying the recurring 0.096% gap. A series that computes, never measures."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Machin's Formula: How the Arctangent Series Computes the Circle Constant

In 1706, the English mathematician John Machin discovered an identity that, for more than two centuries, was the fastest known way to compute the digits of π by hand:

```
π/4 = 4·arctan(1/5) − arctan(1/239)
```

Machin used it to push π to 100 decimal places — a feat no earlier series had matched. In 1873 William Shanks carried the same family of formulas to 707 digits. And in 1949, when the ENIAC became the first computer to calculate π, it did so using exactly this kind of Machin-type arctangent identity. For the whole arc of that history, from pen-and-ink to vacuum tubes, π was being **computed** — built up digit by digit as the limit of a convergent series — never **measured** against any physical circle.

This article examines what Machin's formula is, why its arctangent terms are pure angle arithmetic that does not depend on the value of the circle constant, and what happens to the identity when the circle constant is taken to be Golden Pi, π̂ = 4/√φ = 3.1446055…

## What the Arctangent Series Actually Computes

The arctangent function is defined — independent of any choice of circle constant — by the integral

```
arctan(x) = ∫₀ˣ  dt/(1 + t²)
```

or, equivalently, by its Taylor series expansion, which converges for |x| ≤ 1:

```
arctan(x) = x − x³/3 + x⁵/5 − x⁷/7 + x⁹/9 − …
```

This series is a pure limit. Each partial sum is a rational number; the infinite sum is their limit. Nothing about the terms — the odd powers of x and the reciprocals of the odd integers — mentions π, a circle, or a circumference. The arctangent of a small rational argument is therefore a number that is fully determined by the arithmetic of the series. It is **computed**, never measured.

Substituting x = 1/5 = 0.2 and x = 1/239 ≈ 0.004184, the series gives:

| Term | Series limit | Decimal value |
|------|--------------|---------------|
| arctan(1/5) | 1/5 − 1/(3·5³) + 1/(5·5⁵) − … | 0.1973955598… |
| arctan(1/239) | 1/239 − 1/(3·239³) + … | 0.0041840760… |

Both of these are geometric angles: arctan(1/5) is the angle whose tangent is 0.2 (about 11.31°), and arctan(1/239) is a much smaller angle (about 0.24°). The arctangent series *computes* those angles as limits. This is the crucial point: **the arctangent values are fixed by the series alone and never change, no matter what constant we later use for the circle.**

## The Geometry of the Identity

Machin's formula is a statement about angles. It says that four copies of the arctan(1/5) angle, minus one copy of the arctan(1/239) angle, combine to exactly a quarter of a full turn:

```
4·(11.31°) − 1·(0.24°) = 45°
```

The identity is a consequence of the tangent addition formula and is exact. It tells us that this particular sum of angles is precisely one eighth of a full circle — a right angle cut in half, the angle of a diagonal across a square.

Now here is where the choice of circle constant matters. A **full turn** is a geometric fact: rotating all the way around returns you to your start. The *number* we assign to a full turn is convention. In the conventional system a full turn is 2π radians, so a quarter turn is π/2 and an eighth of a turn is π/4. Machin's formula, in that convention, reads:

```
4·arctan(1/5) − arctan(1/239) = π/4
```

The left-hand side is a fixed sum of two *computed* angles. The right-hand side is the *label* those angles receive when a full turn is set to 2π. The identity holds — but it holds because both sides are the same eighth of a turn, one expressed as angle arithmetic and the other as a fraction of the chosen full-turn constant.

## Golden Pi Rewrites Only the Label

Golden Pi sets the full turn to 2π̂ = 2·(4/√φ) = 6.2892110… The eighth of a turn then carries the label π̂/4 instead of π/4. Since the left-hand side of Machin's formula — the sum of the two computed arctangents — does not change, the identity under Golden Pi becomes:

```
4·arctan(1/5) − arctan(1/239) = π̂/4
```

And here the golden structure appears. Because π̂ = 4/√φ,

```
π̂/4 = (4/√φ)/4 = 1/√φ
```

So, under Golden Pi, Machin's formula collapses to an exact algebraic number in the golden field:

```
4·arctan(1/5) − arctan(1/239) = 1/√φ = 0.7861513777…
```

The eighth of a turn is the reciprocal of the square root of the golden ratio. This is the same golden square root that appears throughout Golden Pi geometry: it is the side of the golden triangle, the constructible length at the heart of π̂, and — as earlier posts in this series have shown — the scale that governs the squaring-the-circle match.

| Quantity | Conventional π | Golden Pi (π̂ = 4/√φ) |
|----------|----------------|--------------------------|
| Full turn | 2π = 6.2831853071… | 2π̂ = 8/√φ = 6.2892110291… |
| Quarter turn | π/2 = 1.5707963267… | π̂/2 = 2/√φ = 1.5723027545… |
| Eighth of a turn (Machin sum) | π/4 = 0.7853981633… | π̂/4 = 1/√φ = 0.7861513777… |

The two labels differ by the recurring gap:

```
(1/√φ − π/4)/(π/4) × 100% = 0.096%
```

The same 0.096% that separates π̂ from π everywhere on this site — in the Basel sum, the Dirichlet integral, the pendulum period, and the Gaussian integral — appears here in the eighth-of-a-turn label of Machin's formula. The *computed* arctangent angles on the left are identical in both worlds; only the conventional label attached to a quarter turn differs.

## Why No Measurement Can Arbitrate

Because both sides of Machin's formula are pure limits — the arctangent series on the left, the definition of the constant on the right — there is nothing physical to measure. The angles arctan(1/5) and arctan(1/239) are fixed by an integral that involves no circle. The eighth of a turn is a fact about rotational geometry. What separates the two readings is purely a convention about how many units we assign to a full turn: 2π in one system, 8/√φ in the other.

No dial, ruler, or stopwatch can distinguish them. If one tries to "measure" the ratio of a circle's circumference to its diameter with a physical tape, the result is a *measured* length ratio whose value is always limited by the precision of the instrument — never a definition. And the series that Machin used never touches a circle at all. The whole edifice of digits of π, from Shanks's 707 hand-computed figures to the ENIAC's 2,037, is an exercise in evaluating limits. That is computation in the purest sense.

Golden Pi does not dispute any of those computed digits in the conventional frame. What it offers is a *different* frame: the same eighth-of-a-turn angle, relabeled as the algebraic number 1/√φ, so that the quarter circle belongs to the golden field and becomes constructible by compass and straightedge — just as the full constant π̂ = 4/√φ is constructible.

## The Pattern Across the Series

This is the consistent thread of the daily Golden Pi series. The Basel sum (Euler, 1735) computes π²/6 as the limit of a series of reciprocal squares. The Dirichlet integral computes π/2 from ∫₀^∞ sin(x)/x dx. The Gaussian integral computes √π from a double integral. The pendulum formula embeds π as the limit of a complete elliptic integral. And now Machin's formula computes π/4 from two arctangent series. In every case the same structure recurs:

1. A well-defined limit **computes** a number — never a measurement.
2. The computed quantity is a pure ratio or angle, independent of the constant's label.
3. Under Golden Pi, the label becomes an exact algebraic expression in φ.
4. The two labels are separated by the same 0.096% gap.

Machin's contribution is historically the sharpest illustration of the "computes, never measures" principle, because his whole point was speed and precision: pack the digits tightly into the series so that each term adds several correct decimal places. arctan(1/239) is so small that its terms shrink almost immediately, which is why Machin could reach 100 digits in 1706 and why the ENIAC used Machin-type formulas in 1949. It was — and remains — the canonical method of *computing* the circle constant to arbitrary precision.

Under Golden Pi that computation is unchanged in mechanics but different in meaning: the eighth of a turn that Machin's terms assemble is not the transcendental 0.785398… but the algebraic 1/√φ = 0.786151…, a number that lives in the same constructible field as the golden ratio itself. A series that computes, never measures — and in the golden frame, what it computes is a square root of φ.

## Further Reading

- [**The Basel Problem: When an Infinite Sum Computes the Circle Constant**](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) *(2026-08-15)* — Euler's series computing π²/6 as a limit, and its form 8/(3φ) under Golden Pi.
- [**The Sinc and the Dirichlet Integral: How ∫₀^∞ sin(x)/x dx Computes the Circle Constant**](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) *(2026-08-20)* — The integral family that computes the constant as a pure limit.
- [**The Gaussian Integral: How the Bell Curve Computes √π, and What Golden Pi Changes**](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) *(2026-08-21)* — The polar-coordinate double integral that evaluates √π, and its golden form 2/φ^(1/4).
- [**The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant**](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) *(2026-08-17)* — The geometric limit family that converges to the circle constant.
- [**The Golden Calculus and a New Closed Form of Golden Pi**](/blog/posts/golden-calculus-new-closed-form/) *(2026-08-05)* — The algebraic closed forms 4/√φ and 4φ/((φ+1)√(φ−1)) that place π̂ in the golden field.
