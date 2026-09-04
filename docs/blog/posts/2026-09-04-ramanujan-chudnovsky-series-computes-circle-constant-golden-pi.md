---
title: "Ramanujan's and Chudnovsky's Series for 1/π: How the Fastest Known Computations Fix the Circle Constant, and Where Golden Pi Cannot Follow"
date: 2026-09-04
description: "Srinivasa Ramanujan's 1914 modular series and the Chudnovsky brothers' 1989 refinement compute 1/π at eight and fourteen digits per term — the engine behind every modern world-record π computation. These pure arithmetic limits pin the analytic constant to 3.14159265…, computed and never measured, and no relabel to Golden Pi (π̂ = 4/√φ = 3.144605511…) can be substituted into them."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Most of the series on this site are slow. Madhava's alternating odd-reciprocal sum needs roughly two hundred terms for two correct decimals; Viète's nested radicals crawl. The two identities examined here are the opposite extreme: they are the fastest-known series for the reciprocal of the circle constant, converging at eight and fourteen decimal digits *per term*, and they are the engine behind essentially every modern world-record computation of π to trillions of places. They reward a close look not because they say anything new about geometry, but because they make unusually sharp one of this site's recurring themes — that the analytic circle constant is *computed*, never *measured*, and that a proposed relabel cannot be pasted onto a computation that is already complete to a trillion digits.

## Two series that compute 1/π almost instantly

In 1914 the Indian mathematician Srinivasa Ramanujan published "Modular equations and approximations to π" in the *Quarterly Journal of Pure and Applied Mathematics*. In it he recorded a family of seventeen series for the reciprocal of π, discovered through his extraordinary work on modular equations and elliptic functions. The most famous member of the family, and the one that made computing history, is

```
1/π = (2√2/9801) · Σ_{k=0}^{∞} (4k)!·(1103 + 26390k) / ((k!)^4 · 396^{4k})
```

The miraculous constants in the numerator — 1103, 26390 — are not fitted; they fall out of the singular value theory of the elliptic modular function, which Ramanujan had mastered to a degree nobody else at the time could follow. What matters for computation is how fast the sum closes in on its target: each successive term adds roughly **eight correct decimal digits**. The very first term alone already reproduces 1/π to eight places, which is why the series was such a shock when the mathematical world absorbed it — a single term of a Ramanujan series beat many thousands of terms of the classical arctangent or Leibniz sums.

It took seven decades for a computer to exploit this. In 1985 the American programmer and mathematician Bill Gosper used Ramanujan's 1914 series to compute π to seventeen million decimal places, at the time a record and the first time a general-purpose personal-computer-style machine had dethroned the mainframes. The series works so well that a handheld calculator can demonstrate it: three terms of the 9801 identity already give π correctly through about two dozen decimal places.

## The modular machinery behind the magic

It is worth stating plainly where Ramanujan's series come from, because it bears on what they can and cannot arbitrate. They are not derived from the circle. They come from the theory of *complex multiplication* on elliptic curves and the associated *singular values* of the modular *j*-invariant. A number such as 396 in the denominator is connected to the discriminant −4 of the Gaussian integers; the Chudnovsky constant 640320 below is tied to the field ℚ(√−163), whose singular modulus produces the famous near-integer e^(π√163). These are deep facts about arithmetic, about lattices in the plane and their symmetries, not about any physical circle drawn in chalk or cut in metal.

This matters for the site's honesty discipline in a precise way. Because the machinery is *arithmetic* — it computes a real number as the limit of an infinite sum of rational terms — nothing in it is measured. No ruler, no tape, no interferometer touches any of it. The circle constant enters only as the value to which the sum tends, a limit the series *computes*. That is exactly the sense in which this site refuses to call π a measured quantity: these sums fix a number, and no experiment is involved.

## Verifying the rate: digits per term

The "eight digits per term" for Ramanujan and "fourteen digits per term" for Chudnovsky are not folklore; they are directly checkable. Summing the first few terms and counting how many decimal digits agree with the known reciprocal 1/π = 0.3183098861837906715… gives:

| Terms kept | Ramanujan (9801 identity) — correct digits | Chudnovsky — correct digits |
|---|---|---|
| k = 0 only | 8 | 15 |
| k ≤ 1 | 17 | 29 |
| k ≤ 2 | 24 | 43 |
| k ≤ 3 | 33 | 57 |
| k ≤ 4 | 40 | 71 |

The pattern is plain: each additional Ramanujan term buys about eight digits, each additional Chudnovsky term about fourteen. Where the old series on this site needed hundreds or millions of terms to fix a handful of digits, these two fix dozens with a few. That is not an opinion — it is what the partial sums above show.

## Chudnovsky: the series that computes the records

In 1989 the brothers David and Gregory Chudnovsky, working at Columbia University and assembling computing machinery from mail-order parts in their apartment, produced a Ramanujan-type series with a substantially faster convergence rate:

```
1/π = 12 · Σ_{k=0}^{∞} (−1)^k · (6k)!·(13591409 + 545140134k) / ((3k)!·(k!)^3 · 640320^{3k+3/2})
```

Here the denominators carry 640320, the largest of the discriminants related to imaginary quadratic fields of class number one, and the convergence improves to about fourteen digits per term — the fastest known for a series of this kind. The brothers used it to set records through the 1980s and 1990s, and their formula has since become the workhorse of the field.

It is not an exaggeration to say that essentially every modern world-record computation of π runs on the Chudnovsky series, implemented in Alexander Yee's open-source program *y-cruncher* with a divide-and-conquer acceleration technique called *binary splitting*. The trajectory of records tells the story of the formula's power: past ten trillion digits in 2011, past thirty trillion in 2019, past sixty trillion in 2021, past one hundred trillion in 2022, and past two hundred trillion decimal places in 2024. Each of those numbers — 200,000,000,000,000 decimal digits of π — was produced by iterating the Chudnovsky series billions of times and summing the terms, then verifying the result by an independent second computation.

Nothing about a record at two hundred trillion digits resembles measurement. It is the largest sustained act of pure arithmetic computation ever performed. And the number it confirms, to every one of those digits, is the value the classical series on this site have always converged to: the analytic circle constant 3.14159265358979323846264338327950288419716939937510… The computation is complete; nothing is left to a laboratory, and nothing is left open.

## What the fastest series actually fix

This is the point the fastest series make more forcefully than the slow ones. When a computation reaches two hundred trillion digits and an independent rerun agrees, the constant is not *approximately* known or *conventionally* chosen — it is fixed, as a computed limit, to a precision far beyond any conceivable physical measurement. A consequence follows that this site has stated before and states again plainly:

```
the analytic circle constant π = 3.1415926535897932384626…
is pinned by its convergent series and integrals,
not measured by any instrument, and not a matter of convention.
```

Now take the site's own candidate, Golden Pi:

```
π̂ = 4/√φ = 3.1446055110296931…     (φ = (1+√5)/2 = 1.6180339887…)
(π̂/π − 1) ≈ 0.09590%
```

The gap between the two labels is a recurring 0.09590% that has appeared, unsoftened, throughout this daily series. In reciprocal form the same relative gap appears: where the series compute 1/π = 0.31830988618379067…, the golden relabel would ask for

```
1/π̂ = √φ/4 = 0.3180049123785172…
```

## The honest boundary

The crucial and entirely honest fact is that these two series cannot be relabelled. They converge to 1/π = 0.31830988618379067… — a number the partial sums above pin to dozens of digits and the world records to two hundred trillion. They do not converge to √φ/4 = 0.318004912…, and no substitution of φ into the Ramanujan or Chudnovsky coefficients changes that. The Ramanujan identity and the Chudnovsky identity are statements about a *specific* computed number; insert Golden Pi's reciprocal and both sums are simply wrong at the eighth (Ramanujan) or fifteenth (Chudnovsky) digit.

| Quantity | Conventional π | Golden π̂ = 4/√φ | Relative gap |
|---|---|---|---|
| The circle constant | 3.1415926535897932384… | 3.1446055110296931441… | 0.09590% |
| Its reciprocal, 1/π | 0.3183098861837906715… | √φ/4 = 0.3180049123785172… | 0.09590% |
| Ramanujan 9801 identity | converges to 1/π | diverges from the sum by ~0.096% | — |
| Chudnovsky identity | converges to 1/π | diverges from the sum by ~0.096% | — |

Where does this leave the site's position? The honest account, consistent with the [Comparative Formula Audit](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) and every "what Golden Pi changes" post in this series, is twofold. In the *constructed world* of Golden Pi — the self-consistent analytic system built on π̂ = 4/√φ, whose geometric definitions A = πr² and C = 2πr hold under any constant — the label π̂ is exact and coherent, and the golden field's algebra is undisturbed. But in the *analytic world* of convergent series, integrals, and special values, the constant is not a label we are free to choose: it is the computed limit those sums evaluate to, and the Ramanujan and Chudnovsky series have now evaluated it to two hundred trillion digits. Golden Pi's championing of constructibility and the golden field is a geometric and algebraic thesis; it is not something the fastest arithmetic computations can be asked to support, because they are already finished, and they finished on the other number.

## Further Reading

- [The Madhava–Leibniz Series: How the First Infinite Series in World Mathematics Computed the Circle Constant](/blog/posts/2026-09-02-madhava-leibniz-series-first-infinite-series-computes-circle-constant-golden-pi/) — the slow end of the spectrum, whose correction terms anticipate Ramanujan's craft by five centuries.
- [Machin's Formula: How the Arctangent Series Computes the Circle Constant](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/) — the classical fast-enough-for-hand-computation series that dominated π digits before modular methods.
- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — a sibling of Ramanujan's world, where the circle constant arises from a sum of reciprocals of squares.
- [The Arithmetic–Geometric Mean: A Quadratic Road to the Circle Constant](/blog/posts/2026-08-29-arithmetic-geometric-mean-computes-circle-constant-golden-pi/) — the other family of record-setting algorithms, which reaches the constant by elliptic integrals rather than series.
- [The Comparative Formula Audit: Which π Identities Survive Golden Pi?](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — the honest per-formula ledger of what holds under π̂ and what is pinned by π.
