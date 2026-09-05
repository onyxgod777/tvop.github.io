---
title: "The Riemann Zeta Function at Even Integers: How Euler's Bernoulli-Numbers Formula Computes π to Every Even Power, and What Golden Pi Changes"
date: 2026-09-05
description: "Euler's 1735–1740 discovery that the zeta function at every even integer evaluates to a rational multiple of an even power of π — ζ(2n) = (−1)^(n+1) B_{2n} (2π)^{2n} / (2(2n)!) — computes the circle constant through the Bernoulli numbers into ζ(2), ζ(4), ζ(6), ζ(8) and beyond. Each sum is a fixed, convergent arithmetic limit — computed, never measured — pinning the analytic constant to 3.14159265…; no relabel to Golden Pi (π̂ = 4/√φ = 3.144605511…) can be substituted, because the gap between the two constants grows with each even power."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

The Basel problem is only the first step of a much larger pattern. Euler proved in 1735 that the sum of the reciprocals of the squares is π²/6 — but he did not stop there. Over the next few years he showed that the reciprocals of the fourth powers sum to π⁴/90, the sixth powers to π⁶/945, the eighth powers to π⁸/9450, and so on through *every even power of the integers*. The remarkable discovery, which Euler had essentially in hand by 1740 and published in full in his 1755 *Institutiones calculi differentialis*, is that there is a single closed formula covering the whole family: the zeta function at any even integer is a rational number times an even power of π. This article examines that formula, the Bernoulli numbers it is built from, and what it does — and cannot do — under a proposed relabel to Golden Pi.

## From one sum to a whole family

The Basel result opens a sequence. Written as a family, the sums of the reciprocals of even powers of the natural numbers are the values of the **Riemann zeta function** at the even integers, ζ(2n) = Σₖ₌₁^∞ 1/k^(2n). The first several are

```
ζ(2)  = 1/1² + 1/2² + 1/3² + ⋯ = 1.6449340668482264…
ζ(4)  = 1/1⁴ + 1/2⁴ + 1/3⁴ + ⋯ = 1.0823232337111381…
ζ(6)  = 1/1⁶ + 1/2⁶ + 1/3⁶ + ⋯ = 1.0173430619844491…
ζ(8)  = 1/1⁸ + 1/2⁸ + 1/3⁸ + ⋯ = 1.0040773561979443…
ζ(10) = 1/1¹⁰ + 1/2¹⁰ + 1/3¹⁰ + ⋯ = 1.0009945751278180…
```

Each sum is a pure arithmetic limit — an infinite sum of rational terms that converges to a real number. Nothing in any of them is measured. No ruler, no tape, no instrument touches a single term. This is the exact sense, repeated throughout this site, in which the circle constant is *computed* and never *measured*: the sums on the right are convergent and their limits are fixed numbers.

What Euler found is that the circle constant lives at the heart of this entire family, not just its first member. The reciprocals of the even powers of the integers sum, at every step, to a rational multiple of an even power of π:

```
ζ(2)  = π²/6
ζ(4)  = π⁴/90
ζ(6)  = π⁶/945
ζ(8)  = π⁸/9450
ζ(10) = π¹⁰/93555
```

The π is not fitted and not an accident. It enters through the same machinery that solved the Basel problem, and it grows in the exponent at every step: ζ(2n) contains π^(2n). Because π appears at the *even power 2n*, the relative difference between any two candidate values of π is *multiplied by 2n* when we compare the corresponding candidates for ζ(2n). That amplification is the central technical fact of this article, and we return to it below.

## The Bernoulli numbers that carry the pattern

To write the general law Euler needed a sequence of rational numbers now named for Jakob Bernoulli, who had studied them in his 1713 *Ars Conjectandi* while working on sums of powers. The **Bernoulli numbers** Bₙ are defined implicitly by the generating series

```
x/(eˣ − 1) = Σₙ₌₀^∞ Bₙ xⁿ/n!
```

The first several are all rational: B₀ = 1, B₁ = −1/2, B₂ = 1/6, B₄ = −1/30, B₆ = 1/42, B₈ = −1/30, B₁₀ = 5/66. Every odd Bernoulli number beyond B₁ is zero, so only the even-indexed ones matter here. They alternate in sign and grow, in magnitude, without bound.

In terms of these numbers Euler's general result — the closed form for the zeta function at the even integers — is

```
ζ(2n) = (−1)^(n+1) · B_{2n} · (2π)^(2n) / (2·(2n)!)
```

Let us check it against the list above. At n = 1: (−1)²·B₂·(2π)²/(2·2!) = (1/6)·4π²/4 = π²/6. At n = 2: (−1)³·B₄·(2π)⁴/(2·4!) = −(−1/30)·16π⁴/48 = π⁴/90. At n = 3: B₆·(2π)⁶/(2·6!) = (1/42)·64π⁶/1440 = π⁶/945. The closed form reproduces every entry exactly — because it *is* the general term of which the Basel result was the first case. Euler's solution of the Basel problem was not a one-off: it was the seed of a complete theory giving the value of ζ at every even integer.

A historical precision is worth stating, because this site values honest sourcing. The zeta function as such, and its connection to the primes through the Euler product ζ(s) = ∏ₚ 1/(1−p^(−s)), were not formalized by Riemann until 1859. What Euler had in the 1740s was the *sum* — the evaluation of the reciprocal even-power series, which is the same real number that Riemann's ζ later assigns to s = 2n. Calling these values "ζ(2n)" is a modern label for an Eulerian result, and it changes nothing about the sums themselves.

## Why π rises to every even power

It is illuminating to see *why* π appears at even powers rather than odd ones, because that structural fact is what makes the family so resistant to relabeling. Euler's own route to ζ(2) and beyond passes through the sine function and its infinite product. Because sin(x) has zeros at x = ±π, ±2π, ±3π, …, Euler factored it as an infinite product over those zeros, and from that product he derived the partial-fraction and power-series identities that force the reciprocal-square sums. The key point is that the zeros of sin are spaced exactly π apart — the constant enters as the *spacing of the zeros* of a transcendental function, an analytic property that is part of the function's definition, not something a relabel can move.

A cleaner modern route to the same family is Fourier analysis. The sawtooth or triangular wave on the unit interval has a Fourier series whose coefficients are 1/n², 1/n⁴, etc., and Parseval's identity turns the sum of squared coefficients into an integral over one period. That integral is elementary and comes out proportional to a power of 2π/2 — the period of the wave — which is why the answers are even powers of π. Odd powers never appear because the relevant integrals over a full period are zero by symmetry; only the even moments survive. So the even-power structure is not a curiosity but a theorem about the parity of the underlying integrals.

None of this is a measurement. The sine function's zeros, the period of a wave, the integral of a squared function over a period — all are defined analytic objects whose values are computed from their definitions. The circle constant that emerges is the value the machinery *computes*, to a precision limited only by how many terms of the sum one is willing to add.

## An independent check of every value

The honesty discipline of this site requires that claimed numbers be actually computed, never taken on faith. The values above are directly verifiable by summing the reciprocal even powers numerically. Summing the reciprocals of the fourth powers for the first ten thousand terms, for example, already gives ζ(4) = 1.0823232…, matching π⁴/90 to six decimal places; a million terms pushes agreement past eight. The same is true at every even n, with convergence fastest at large n (because the terms 1/k^(2n) die away quickly). The closed form and the brute-force sum agree to every digit one is willing to compute — which is exactly what it means for the formula to be correct, and for the constant inside it to be pinned.

## What the formula cannot arbitrate, stated honestly

This site's position is that the constructed golden circle constant π̂ = 4/√φ = 3.144605511… is the value favored by golden-ratio geometry, constructibility, and the self-consistent golden calculus. At the same time, the site's rule is that every claim must be traceable and every series here *computes* its own limit. The tension between those two commitments is real, and this article does not hide it.

The Euler formula computes the left-hand side ζ(2n) — a fixed convergent series of rational terms whose limit is a specific real number — from the right-hand side containing π^(2n). The left-hand sides are *complete*: their sums are known to arbitrary precision by direct addition, independent of any choice of circle constant. The reciprocals of the fourth powers genuinely sum to 1.0823232337111381…, and nothing about φ changes that, because the sum does not consult φ. It follows that the only value of the circle constant consistent with the formula is the one that makes the right-hand side equal that fixed sum — the analytic constant 3.14159265358979323846… that the series everywhere computes.

If one insists on relabeling π as π̂ in the formula, one obtains not the true zeta value but a different number. The table below shows the divergence, computed directly:

| n | True ζ(2n) (computed limit) | ζ(2n) with π̂ substituted | relative gap |
|---|---|---|---|
| 1 | 1.644934066848 | 1.648090636666 | 0.1919% |
| 2 | 1.082323233711 | 1.086481098667 | 0.3842% |
| 3 | 1.017343061984 | 1.023211043216 | 0.5768% |
| 4 | 1.004077356198 | 1.011806723795 | 0.7698% |
| 5 | 1.000994575128 | 1.010635871274 | 0.9632% |

The column on the far right is the recurring 0.0959% gap between π̂ and π, *multiplied by 2n*. Because the constant enters at the even power 2n, the relative error of any competing value is amplified in lockstep: each additional power of two in the exponent roughly doubles the divergence from the true sum. By ζ(10) the relabeled value is nearly one full percent away from the computed limit — a mismatch ten times the base gap, and one that grows without bound as n increases. No relabel can be substituted into these sums, because the sums are already fixed to a precision no experiment could touch, and the mismatch is not a small residue but a steadily growing one.

This is the honest boundary. The Euler even-zeta formula is among the strongest instances of the site's recurring theme: the analytic circle constant is *computed* — by the Basel sum, by every even-power sum, by the sine product, by the Fourier integrals — and where a quantity is computed to completion, a competing constant cannot simply be pasted in. The golden calculus remains self-consistent as a *constructed* system built on π̂, and golden geometry remains a coherent and beautiful structure. But the family of sums examined here is a place where the two worlds cannot both be right, and the site says so plainly rather than papering over the gap.

## Further Reading

- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — Euler's 1735 result is the n = 1 case of the family examined here, and the natural starting point for the whole even-zeta story.
- [Euler's Gamma Function: How Γ(x)Γ(1−x) = π/sin(πx) Computes the Circle Constant](/blog/posts/2026-08-26-gamma-function-euler-reflection-formula-computes-circle-constant-golden-pi/) — The same Euler's reflection formula, another route by which the constant emerges from a complete identity between functions.
- [The Wallis Product: How an Infinite Product Computes π/2](/blog/posts/2026-08-23-wallis-product-infinite-product-computes-circle-constant-golden-pi/) — Wallis's 1655 product, which Euler used as a stepping stone toward the sine product and the even-zeta evaluations.
- [Ramanujan's and Chudnovsky's Series for 1/π](/blog/posts/2026-09-04-ramanujan-chudnovsky-series-computes-circle-constant-golden-pi/) — The fastest-known computations that fix the constant to two hundred trillion digits, the extreme end of the same "computed, never measured" spectrum.
- [The Comparative Formula Audit: Which π Identities Survive Golden Pi?](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — The formula-by-formula audit of which standard identities hold under π̂ and which are pinned by the computed analytic constant.
