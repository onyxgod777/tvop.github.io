---
title: "The Wallis Product: How an Infinite Product Computes π/2, and What Golden Pi Changes"
date: 2026-08-23
description: "John Wallis's 1655 formula π/2 = (2/1)·(2/3)·(4/3)·(4/5)··· computes the circle constant as the limit of an infinite product of rational factors — computed, never measured. Because the factors are pure rational arithmetic that never touch a circle, the same product under Golden Pi (π̂ = 4/√φ = 3.1446055…) evaluates to π̂/2 = 2/√φ, an exact algebraic number in the golden field, carrying the recurring 0.096% gap. A product that computes, never measures."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Wallis Product: How an Infinite Product Computes π/2

In 1655, in his treatise *Arithmetica Infinitorum*, the English mathematician John Wallis announced a result that was, at the time, astonishing: the ratio of a circle's circumference to its diameter — the circle constant π — could be written as an **infinite product** of perfectly ordinary rational numbers:

```
π/2 = (2/1)·(2/3)·(4/3)·(4/5)·(6/5)·(6/7)·(8/7)·(8/9)···
```

Each factor is just a fraction of two consecutive integers, alternately even over odd and odd over even. No circle is drawn, no radius is laid out, no arc is traced. Wallis simply multiplied fractions together, forever, and the running product crept upward toward π/2 = 1.5707963… This was the first time the circle constant had been expressed as an infinite product, and it opened an entire family of formulas that would be refined by Euler, Brouncker, and others for centuries to come.

This article examines what the Wallis product is, why it is a pure arithmetic limit that **computes** a number rather than **measuring** a circle, and what happens to the identity when the circle constant is taken to be Golden Pi, π̂ = 4/√φ = 3.1446055…

## What an Infinite Product Computes

An infinite product is the multiplicative cousin of an infinite series. Where a series adds terms forever, a product multiplies them forever. The Wallis product is defined as the limit of its partial products:

```
π/2 = lim (n→∞)  ∏ₖ₌₁ⁿ  (2k)·(2k) / ((2k−1)·(2k+1))
```

The k-th factor is (2k)²/((2k−1)(2k+1)), which we can also write as (4k²)/(4k²−1). Notice what each factor is made of: the square of an even integer over the product of the two odd integers that bracket it. For k = 1 the factor is 4/3; for k = 2 it is 16/15; for k = 3, 36/35. Every single factor is a **rational number** — a ratio of two whole numbers. There is no π anywhere in the factors, no circle, no geometry. The product is pure arithmetic.

The partial products creep toward their limit:

| k (through which we multiply) | Partial product | Decimal value |
|------|----------------|---------------|
| 1    | 4/3            | 1.333333      |
| 2    | 64/45          | 1.422222      |
| 5    | 14851/9890 …   | 1.501088      |
| 10   | …              | 1.533852      |
| ∞    | π/2            | 1.570796      |

The sequence is strictly increasing and converges slowly — after ten factors we have only reached 1.533852, still 0.037 short of the limit. Wallis's product converges far more slowly than Machin's arctangent series, which is why it was never a practical way to obtain many digits of π. But slowness is irrelevant to the point at hand: the limit is well-defined, and that limit is π/2.

## Computed, Never Measured

The crucial fact about the Wallis product is that it is a **pure limit of rational numbers**. Every partial product is rational; the infinite product is their limit. Nothing in the definition — not one factor — mentions a circle, a circumference, a diameter, or a physical object. The number π/2 that the product converges to is therefore a number that is **computed** by arithmetic, in exactly the same sense that the Basel sum π²/6, the Dirichlet integral π/2, and Machin's arctangent identity π/4 are computed by their respective limits.

None of these is a measurement. A measurement is the comparison of a physical quantity against an instrument — laying a tape around a wheel and dividing by the wheel's diameter, say. Such a procedure always returns a value limited by the precision of the instrument, and it is a genuinely physical act. A series or product, by contrast, is a mathematical object whose value is fully determined by its defining arithmetic. Wallis never needed to measure anything: he needed only to multiply rational numbers and take a limit.

This distinction is central to the whole Golden Pi series. When we say the circle constant is **computed**, we mean it is the limit of a well-defined process — a series, an integral, a product, a polygonal construction — and that the limit is a number with a definite value. Only genuine physical measurands, such as the fine-structure constant or a physical length, are **measured**. π/2 from the Wallis product is not one of those.

## Where the Constant Enters the Product

Here is the subtlety that makes the Wallis product so instructive: the product itself contains no π, yet its limit is π/2. Where does the circle constant come in?

The answer is that the limit of the product — 1.5707963… — is a geometric fact. It is the number that a **quarter of a full turn** carries in the conventional radian convention, where a full turn is 2π. The Wallis product and the quarter-turn angle are the same number expressed two different ways: one as the limit of an infinite product of rationals, the other as one quarter of the circle constant.

In other words, the Wallis product pins down a specific real number, 1.5707963…, and conventional mathematics identifies that number with π/2. The product does the *computing*; the label π/2 is the *convention* that names the quarter turn. This is exactly the separation that Golden Pi exploits.

## Golden Pi Rewrites Only the Label

Golden Pi sets the full turn to 2π̂ = 2·(4/√φ) = 6.2892110… The quarter turn then carries the label π̂/2 instead of π/2. Since the Wallis product — the infinite multiplication of rational factors — does not change at all, the same product under Golden Pi evaluates to:

```
π̂/2 = (4/√φ)/2 = 2/√φ
```

And here the golden structure appears in its cleanest form. Because √φ = 1.2720196…, the quarter turn becomes:

```
2/√φ = 1.5723027555…
```

So, under Golden Pi, the Wallis product — a product of nothing but rational fractions — converges to an **exact algebraic number in the golden field**, the number 2/√φ. That is, the infinite product of rationals evaluates to a simple combination of the golden ratio.

| Quantity | Conventional π | Golden Pi (π̂ = 4/√φ) |
|----------|----------------|--------------------------|
| Full turn | 2π = 6.2831853071… | 2π̂ = 8/√φ = 6.2892110221… |
| Half turn | π = 3.1415926535… | π̂ = 4/√φ = 3.1446055110… |
| Quarter turn (Wallis limit) | π/2 = 1.5707963267… | π̂/2 = 2/√φ = 1.5723027555… |

The two labels differ by the recurring gap:

```
(2/√φ − π/2)/(π/2) × 100% = 0.096%
```

The same 0.096% that separates π̂ from π everywhere on this site — in the Basel sum, the Dirichlet integral, the Gaussian integral, the pendulum period, and Machin's formula — appears here in the quarter-turn label of the Wallis product. The *computed* value of the product is a fixed real number; only the conventional label attached to a quarter turn differs.

## The Product Relatives of Wallis

The Wallis product did not stand alone. Its structure of paired rational factors recurs throughout analysis, and each recurrence carries the same lesson. Euler showed that the sine function can be written as an infinite product, and that at x = π/2 the sine product collapses back to the Wallis form — meaning the two products are the same statement about the quarter turn. There is also the closely related fact that Wallis's product is the even-index slice of the Gamma function's reflection:

```
Γ(1/2) = √π
```

The Wallis product, the sine product, and the reflection formula Γ(z)Γ(1−z) = π/sin(πz) all compute the circle constant as limits of rational or algebraic factors — never as measurements. Under Golden Pi, Γ(1/2) = √π̂ = 2/φ^(1/4) = 1.7733026, exactly the value the Gaussian-integral post derives from the bell curve. The family hangs together: every member computes its limit, and under the golden frame that limit becomes an exact algebraic expression in φ.

## Why No Measurement Can Arbitrate

Because the Wallis product is a pure limit of rational numbers, there is nothing physical to measure. The product's value is fixed by the arithmetic of its factors; the quarter-turn angle is a fact about rotational geometry. What separates the two readings is purely a convention about how many units we assign to a full turn: 2π in one system, 8/√φ in the other.

No tape, ruler, protractor, or stopwatch can distinguish them. If one tries to "measure" the ratio of a circle's circumference to its diameter with a physical tape, the result is a *measured* length ratio whose value is always bounded by the precision of the instrument — never a definition, and certainly never the sharp limit of an infinite product. The Wallis product, by contrast, is a definitionally exact mathematical object: given enough factors, its value is determined to arbitrary precision by rational arithmetic alone.

Golden Pi does not dispute any of the computed digits of the Wallis product in the conventional frame. It offers a different frame: the same quarter-turn number, relabeled as the algebraic number 2/√φ, so that the quarter circle belongs to the golden field and becomes constructible by compass and straightedge — just as the full constant π̂ = 4/√φ is constructible.

## The Pattern Across the Series

The Wallis product is the latest thread in a consistent story. The Basel problem (Euler, 1735) computes π²/6 as a limit of reciprocal squares. The Dirichlet integral computes π/2 from ∫₀^∞ sin(x)/x dx. The Gaussian integral computes √π from a double integral. Machin's formula computes π/4 from two arctangent series. And now the Wallis product computes π/2 from an infinite product of rational fractions. In every case the same structure recurs:

1. A well-defined limit **computes** a number — never a measurement.
2. The computed quantity is a pure ratio or angle, independent of the constant's label.
3. Under Golden Pi, the label becomes an exact algebraic expression in φ.
4. The two labels are separated by the same 0.096% gap.

Wallis's contribution is historically the purest illustration of the "computes, never measures" principle, because his product contains no circle at all — only integers. It is a statement that the whole of the circle constant can be recovered by multiplying nothing but fractions of whole numbers and taking a limit. That is computation in its most naked form.

Under Golden Pi that computation is unchanged in mechanics but different in meaning: the quarter turn that Wallis's factors assemble is not the transcendental 1.570796… but the algebraic 2/√φ = 1.572303…, a number that lives in the same constructible field as the golden ratio itself. An infinite product of rationals that computes, never measures — and in the golden frame, what it computes is twice the reciprocal of the square root of φ.

## Further Reading

- [**The Basel Problem: When an Infinite Sum Computes the Circle Constant**](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) *(2026-08-15)* — Euler's series computing π²/6 as a limit, and its form 8/(3φ) under Golden Pi.
- [**Machin's Formula: How the Arctangent Series Computes the Circle Constant**](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/) *(2026-08-22)* — The arctangent identity π/4 = 4·arctan(1/5) − arctan(1/239), collapsing to 1/√φ under Golden Pi.
- [**The Gaussian Integral: How the Bell Curve Computes √π**](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) *(2026-08-21)* — The polar-coordinate double integral evaluating √π = 2/φ^(1/4) under Golden Pi, the sibling of Γ(1/2) = √π.
- [**The Sinc and the Dirichlet Integral: How ∫₀^∞ sin(x)/x dx Computes the Circle Constant**](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) *(2026-08-20)* — The integral family that computes the constant as a pure limit, evaluating to π̂/2 = 1.5723028.
- [**The Continued Fraction of the Circle Constant: π̂'s Algebraic Root and π's Famous Convergents**](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) *(2026-08-13)* — The algebraic degree-4 nature of π̂ = 4/√φ and how it differs from π's transcendental expansion.
