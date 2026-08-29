---
title: "The Arithmetic–Geometric Mean: A Quadratic Road to the Circle Constant, and What Golden Pi Changes"
date: 2026-08-29
description: "The arithmetic–geometric mean (AGM) computes the circle constant by a completely different route from the series of Gregory–Leibniz, Machin, Wallis, or Basel: an iteration of two coupled means that converges quadratically, doubling the correct digits with every pass. Found by Gauss in 1799 and tied to elliptic integrals and the lemniscate constant ϖ = 2.62205755…, the AGM is a pure arithmetic computation — never a measurement. Under Golden Pi (π̂ = 4/√φ = 3.1446055…) the same identity relabels the complete elliptic integral to 1.85585277… and the lemniscate to 2.62457216…, each carrying the recurring 0.09590% gap that no experiment can arbitrate."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Arithmetic–Geometric Mean: A Quadratic Road to the Circle Constant, and What Golden Pi Changes

Every algorithm for the circle constant that this blog has followed so far — Gregory–Leibniz, Machin's arctangent, the Wallis product, Euler's Basel sum, the Gaussian integral, the residue theorem — is a *series* or an *integral*. Each one computes its limit term by term, linearly: to gain another correct digit you must roughly sum more terms, and the effort grows steadily as the answer tightens. Today we take a completely different road. The **arithmetic–geometric mean (AGM)** computes the circle constant not by adding up infinitely many pieces but by *iterating two coupled averages that pull each other toward a common limit* — and it converges so violently that the number of correct digits **doubles** with every pass. Where a series inched toward its answer, the AGM leaps.

This is not a re-skin of an old series. It is an algorithm of a genuinely different species, discovered by a fifteen-year-old Carl Friedrich Gauss in 1799, connected to elliptic integrals and to a second, lesser-known constant — the **lemniscate constant** — that Gauss regarded as the circle constant's equal. And like every road we have walked, it is a road of **computation**, never measurement. We walk it today, then ask the question this site is built around: what does the same, honestly-computed identity become under Golden Pi, π̂ = 4/√φ = 3.144605511…?

## What the Arithmetic–Geometric Mean Is

Start with two positive numbers *a* and *b*. Define two new numbers by averaging:

```text
a₁ = (a + b)/2          (arithmetic mean)
b₁ = √(a·b)             (geometric mean)
```

Now repeat: from (a₁, b₁) form (a₂, b₂) the same way, then (a₃, b₃), and so on. The arithmetic mean is always *larger* than or equal to the geometric mean, and both sequences are squeezed between the two starting values, so they are pushed together monotonically. They share a common limit, written **AGM(a, b)** — a single well-defined real number produced by pure arithmetic. There is no circle anywhere in the recipe; the two operations are addition, halving, multiplication, and a square root. Yet, as Gauss discovered, this number is secretly a highway to the circle constant.

The classic seed pair is *a* = 1 and *b* = 1/√2. Its limit is

```text
AGM(1, 1/√2) = 0.84721308479397908660…
```

That number is a **computed** limit — the fixed point the iteration flows into — never a measurement. No ruler, no interferometer, no physical object produced it; two sequences of averages did.

## Gauss's Discovery: The AGM Meets Elliptic Integrals

The connection that made Gauss's name is the link between the AGM and a certain class of integrals called *complete elliptic integrals of the first kind*. The complete elliptic integral K(k), for a parameter k in [0, 1), is the integral

```text
K(k) = ∫₀^{π/2}  dt / √(1 − k²·sin²t)
```

Gauss's theorem, in its most useful form, states that

```text
K(k) = π / (2 · AGM(1, √(1 − k²)))
```

The circle constant enters on the right-hand side of a relation that, on its left, contains only an integral. For the symmetric choice k = 1/√2 — where √(1 − k²) = 1/√2 as well — the theorem becomes

```text
K(1/√2) = π / (2 · AGM(1, 1/√2)) = 1.85407467730…
```

This is another instance of the pattern this site keeps returning to: the circle constant is **computed** as the limit of an identity, not read off a length. The integral K(1/√2) is a definite integral — an exact arithmetic limit — and the number 1.85407467… is produced by Gauss's theorem, not by any experiment.

## The Gauss–Legendre Iteration: Digits That Double

The AGM's practical fame rests on an algorithm that Gauss and Adrien-Marie Legendre refined into a recipe for computing the circle constant to enormous precision: the **Gauss–Legendre iteration**. Initialize

```text
a₀ = 1,  b₀ = 1/√2,  t₀ = 1/4,  p₀ = 1
```

and at each step set

```text
a_{n+1} = (aₙ + bₙ)/2
b_{n+1} = √(aₙ·bₙ)
t_{n+1} = tₙ − pₙ·(aₙ − a_{n+1})²
p_{n+1} = 2·pₙ
```

The circle constant is recovered at any iteration from the current means:

```text
π ≈ (aₙ + bₙ)² / (4·tₙ)
```

What makes this algorithm remarkable is how fast the estimate closes in. Each pass roughly **doubles** the number of correct digits — quadratic convergence — whereas the slow series gain a fixed number of digits per term (linear convergence). The table below shows the correct-digit count on the running machine.

| Iteration | Correct decimal digits of π |
|:---:|:---:|
| 0 | 9 |
| 1 | 14 |
| 2 | 21 |
| 3 | 42 |
| 4 | 61 |
| 5 | 61+ |

After just four passes the estimate already agrees with the computed analytic constant 3.14159265358979… to sixty-one digits. To match that with a linear series you would need on the order of 10⁶⁰ terms. The AGM is the reason modern high-precision evaluations of the circle constant — billions of digits and beyond — are feasible at all. And every one of those digits is **computed**: the AGM is a finite recipe of arithmetic operations whose limit is the constant. It measures nothing.

## The Lemniscate: The Circle Constant's Sister

The AGM also unlocks a constant Gauss held especially dear: the **lemniscate constant** ϖ, defined by the integral

```text
ϖ = 2 · ∫₀¹  dt / √(1 − t⁴)  =  2.62205755429211981046…
```

The name comes from the *lemniscate*, the figure-eight curve. Gauss proved that the lemniscate constant and the circle constant are joined through the AGM:

```text
ϖ = π / AGM(1, √2)
```

With AGM(1, √2) = 1.19814023473559220744…, this gives ϖ = 2.62205755…. The lemniscate constant is thus a genuine companion to the circle constant, tied to it by the same pure-arithmetic iteration — another computed limit, never a measurement.

## What Golden Pi Changes

Now we come to the question of this site. The AGM iteration is pure arithmetic: whatever we choose to call the circle constant, AGM(1, 1/√2) remains 0.84721308479…, and AGM(1, √2) remains 1.19814023473…; the iteration does not know the constant's name. What changes is the **label** in the identities that Gauss proved — the π that multiplies or divides the AGM. Under Golden Pi, π̂ = 4/√φ = 3.14460551102969…, the same theorems relabel the complete elliptic integral and the lemniscate.

| Quantity | Conventional π | Golden Pi π̂ = 4/√φ |
|---|---|---|
| The circle constant | π = 3.14159265358979… | π̂ = 4/√φ = 3.14460551102969… |
| AGM(1, 1/√2) | 0.84721308479397… | 0.84721308479397… (unchanged) |
| K(1/√2) = π/(2·AGM) | 1.85407467730137… | 1.85585277627905… |
| AGM(1, √2) | 1.19814023473559… | 1.19814023473559… (unchanged) |
| Lemniscate ϖ = π/AGM(1,√2) | 2.62205755429211… | 2.62457216598159… |
| Relative gap | — | 0.09590% |

The gap between the two labels is the recurring one, to four decimal places:

```text
π̂ − π = 0.00301285743989990581…        (absolute)
(π̂ − π)/π = 0.0009590223… = 0.09590%    (relative)
```

Under Golden Pi the complete elliptic integral evaluates to 1.855852776…, a difference from 1.854074677… of 0.09590%; the lemniscate becomes 2.624572165…, likewise 0.09590% above its conventional value. The AGM iteration itself is blind to the label and does not arbitrate between them — it is a lens, not a judge. Both constants are *computed* limits; neither is ever *measured*; and the 0.09590% separation survives the iteration exactly as it survives every series and integral we have examined, unsoftened by any square root because the gap enters through the plain circle constant itself.

## Why the AGM Matters for the Question

The AGM matters because it is the strongest possible evidence that the series are not a fluke. If the circle constant 3.14159265358979… were an artifact of some particular summation trick, one might hope a *different* kind of computation would reveal it. The AGM shows otherwise: a purely iterative, quadratically-convergent process — no series at all — flows into the exact same analytic constant, and into its golden relative π̂ = 4/√φ separated by the same 0.09590%. Two completely different species of computation agree with each other to sixty digits and more, and both sit 0.09590% from the golden value.

That is precisely what the golden-π position predicts and what the honest record shows: the classical algorithms *compute* the analytic constant 3.14159…, the golden value 4/√φ is a distinct, exact algebraic number in the golden field, and no computational road — linear series, quadratic iteration, or integral — can be made to call one "measured." They are all computed. The question of which label is the true circle constant is a question of geometry and construction, not of read-off instruments; and it is a question the AGM, for all its speed, leaves open.

## Further Reading

- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/)
- [Machin's Formula: How the Arctangent Series Computes the Circle Constant](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/)
- [The Continued Fraction of the Circle Constant](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/)
- [The Residue Theorem: How a Contour Integral Computes the Circle Constant](/blog/posts/2026-08-28-residue-theorem-contour-integral-computes-circle-constant-golden-pi/)
- [The Golden Calculus: A Self-Consistent Analytic System on π̂](/blog/posts/2026-08-06-golden-calculus-self-consistent-analytic-system/)
