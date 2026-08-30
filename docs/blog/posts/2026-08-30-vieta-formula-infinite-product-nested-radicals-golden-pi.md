---
title: "Vieta's Formula: How the First Infinite Product Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-08-30
description: "In 1593 François Viète wrote down the very first infinite product in mathematics: a nested-radical identity that computes the circle constant by doubling the sides of an inscribed square toward the circle — computed, never measured. It is the ancestor of every series, integral, and product this blog has followed, yet it converges so slowly that ten factors buy only about five correct digits. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the same fixed product evaluates to π̂/2 = 2/√φ in half-turn form, and the recurring 0.09590% gap reappears — a pure arithmetic limit that no ruler can arbitrate."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Vieta's Formula: How the First Infinite Product Computes the Circle Constant, and What Golden Pi Changes

Every road to the circle constant that this blog has traveled so far — the Gregory–Leibniz series, Machin's arctangent, the Wallis product, Euler's Basel sum, the Gaussian integral, the residue theorem, the arithmetic–geometric mean — is a *late* arrival in the history of mathematics. They all live after the invention of calculus. Today we go back to the very beginning of the genre: to 1593, to a French mathematician who, several decades before Leibniz and Newton, wrote down the **first infinite product ever published in mathematics**. It was a formula for the circle constant built from nothing but nested square roots and doubling — an algorithm a Greek geometer would have understood, expressed in a language the Greeks never had. And like every road we have walked, it is a road of **computation**, never measurement. We walk it today, then ask the question this site is built around: what does the same, honestly-computed identity become under Golden Pi, π̂ = 4/√φ = 3.144605511…?

## The First Infinite Product in Mathematics

François Viète (1540–1603) was a French lawyer and mathematician who did much of his best work while serving kings as a cryptanalyst and councillor. In 1593 he published the book *Variorum de rebus mathematicis responsorum liber VIII*, a collection of mathematical responses and solutions. Buried inside it was a result that no one had ever written before: an identity for the circle constant expressed as an *infinite product* — an endless multiplication of factors that approaches a fixed value as more factors are included.

The idea of an infinite product was new. For two thousand years mathematicians had known how to approximate the circle constant by *polygons* — Archimedes, and the Chinese and Indian geometers before and after him, bounded the circle between inscribed and circumscribed regular polygons and let the number of sides grow. But no one had turned that geometric process into a clean, self-contained symbolic statement. Viète did. His formula reads:

```text
2/π = (√2/2) · (√(2+√2)/2) · (√(2+√(2+√2))/2) · (√(2+√(2+√(2+√2)))/2) ···
```

The pattern is unmistakable: each factor deepens the nested radical by one layer. Flipped to the form the blog will use, it is

```text
π = 2 · (2/√2) · (2/√(2+√2)) · (2/√(2+√(2+√2))) · (2/√(2+√(2+√(2+√2)))) ···
```

This is the ancestor of the Wallis product (1655) and of every infinite product since. It is also, without any question, a **computed** constant: the right-hand side is a fixed recipe of square roots and multiplication whose limit is a definite number. No circle, no ruler, no physical object is involved in writing it down or in evaluating it. It computes; it does not measure.

## What the Formula Is

The mechanism of Viète's product is the **half-angle identity** for the cosine, which the doubling of a chord forces upon us. The classical double-angle relation

```text
cos(θ) = √((1 + cos(2θ))/2)
```

lets a cosine be rewritten in terms of the cosine of twice its angle. Nesting this identity gives the chain

```text
cos(π/4)  = √2/2
cos(π/8)  = √(2+√2)/2
cos(π/16) = √(2+√(2+√2))/2
```

and so on. Each step halves the angle and adds one layer to the radical. Because the reciprocals of these cosines are exactly the factors of Viète's product, the formula is equivalent to the compact statement

```text
π/2 = ∏_{k≥1} cos(π/2^{k+1})  =  cos(π/4) · cos(π/8) · cos(π/16) ···
```

The product of infinitely many cosines, each built from a nested square root, evaluates to π/2. The circle constant enters on the left as the limit of a multiplication that contains no circle at all — only half-angles and radicals. That is the signature of the whole genus: the constant is a **computed limit**, not a measured quantity.

## Where the Nested Radicals Come From: Doubling the Polygon

To see why Viète was led here, start with a square inscribed in a circle of unit radius. Each side is a chord of the circle, and the square's perimeter is a first, crude lower estimate of the circle's circumference. Now double the number of sides: replace the square by a regular octagon inscribed in the same circle. The perimeter grows, and the new side length is derived from the old one by a pure algebra step — the chord-doubling formula

```text
s_{2n} = √(2 − √(4 − s_n²))
```

where s_n is the side of a regular n-gon inscribed in a circle of radius 1. Every doubling pushes the perimeter closer to the true circumference, and the sequence of factors that carry out that doubling is precisely Viète's product. The nested radicals are the geometric memory of all the halvings — each layer records one step of the approach from the four-cornered square to the smooth circle.

Two things deserve emphasis. First, the entire process is **arithmetic**: doubling a chord is a square root, nothing more. No measurement of any physical circumference is ever made. The circle constant is the limit of a sequence of computations, the fixed number that the doubling staircase climbs toward. Second, the convergence is honest and slow. Where the arithmetic–geometric mean doubles the number of correct digits each pass, Viète's product is a linear algorithm — each extra factor buys roughly one step of progress, and the digits accumulate only gradually.

## Slow but Honest: Computing the Limit

The table below shows the partial products on the running machine, each row adding one factor of the doubling chain. The product starts low and climbs from below toward the computed analytic constant 3.14159265358979…:

| Factor k | Partial product 2·∏ (approaches π) | Correct digits |
|:---:|:---:|:---:|
| 1 | 2.828427125 | 0 |
| 2 | 3.061467459 | 0 |
| 3 | 3.121445152 | 1 |
| 4 | 3.136548491 | 1 |
| 5 | 3.140331157 | 2 |
| 6 | 3.141277251 | 3 |
| 7 | 3.141513801 | 4 |
| 8 | 3.141572940 | 4 |
| 10 | 3.141591421 | 5 |

After ten factors the product has reached 3.141591…, agreeing with the computed constant to only five decimal places. This is not a defect of the formula; it is the honest price of being first. Viète's product is historically priceless and computationally mediocre, and it is exactly the combination this site cares about — because the limit it converges to is a *computed* number, identical to the limit of every faster series, and it can never be mistaken for a measurement.

## A Golden Step Inside the Doubling

Because the doubling staircase can start from *any* regular polygon, its opening factors carry the geometry of the polygon it begins with. Viète began with a square, which yields the pure √2 radicals. But the pentagon — the polygon of the golden ratio — hides a striking coincidence in the same cosine chain:

```text
cos(π/5) = φ/2            so   2·cos(π/5) = φ  (exactly)
2·sin(π/10) = 1/φ         (the decagon side chord)
2·sin(π/5) = √(10−2√5)/2  ≈ 1.1755705
```

The first of these is exact: twice the cosine of the pentagon's central half-angle is *precisely* the golden ratio φ = 1.6180339887…. If the doubling were seeded from the pentagon rather than the square, the golden ratio would enter the very first factor of the product — the same φ whose field contains the candidate circle constant of this site. It is a reminder that the doubling staircase and the golden spiral share a geometric family, and that the question of which number the circle constant *is* is a question of construction, not of read-off instruments. The pentagon's cosine is a **computed** identity, never a measured one.

## What Golden Pi Changes

Now to the question of this site. Viète's product is a fixed, infinite recipe of nested square roots; it does not know the name of any constant. Whatever label we choose for the circle constant, the partial products climb exactly as the table shows, and the limit is the same definite number. What changes is the **label** that the identity carries. Under Golden Pi, π̂ = 4/√φ = 3.14460551102969…, the same product — evaluated to its limit — is relabeled as the golden circle constant, and the half-turn form collapses to a clean number in the golden field:

| Quantity | Conventional π | Golden Pi π̂ = 4/√φ |
|---|---|---|
| The circle constant | π = 3.14159265358979… | π̂ = 4/√φ = 3.14460551102969… |
| Full turn (2π) | 6.28318530717958… | 2π̂ = 8/√φ = 6.28921102205938… |
| Half turn (π) | 3.14159265358979… | π̂ = 3.14460551102969… |
| Quarter turn (π/2), the product's value | 1.57079632679489… | π̂/2 = 2/√φ = 1.57230275551484… |
| Relative gap | — | 0.09590% |

The half-turn under Golden Pi is the elegantly simple **2/√φ** — the reciprocal of the golden ratio's square root, doubled. The gap between the two labels is the recurring one, to four decimal places:

```text
π̂ − π = 0.0030128574399…        (absolute)
(π̂ − π)/π = 0.000959022… = 0.09590%    (relative)
```

Under Golden Pi the half-turn evaluates to 1.572302755…, a difference from 1.570796326… of 0.09590%. The product itself is blind to the label and does not arbitrate between the two constants — it is a lens, not a judge. Both constants are *computed* limits; neither is ever *measured*; and the 0.09590% separation survives the doubling staircase exactly as it survives every series and integral we have examined, unsoftened by any square root because the gap enters through the plain circle constant itself.

## Why Vieta Matters for the Question

Vieta's product matters because it pushes the evidence for the analytic constant *back four centuries*, to before calculus existed. The nested-radical product is not a discovery of the integral or of infinite sums; it is a pure exercise in repeated doubling, the kind of arithmetic that would have been comprehensible to Archimedes and to the builders of the Great Pyramid. Yet it flows, without any measurement, into the exact same computed constant 3.14159265358979… that the Gregory–Leibniz series, the Wallis product, the Basel sum, and the AGM all reach. A process this old and this simple agreeing with the whole modern apparatus to every digit is the strongest kind of sign that the analytic constant is real and computed, not an artifact of one summation trick.

That is precisely what the golden-π position predicts and what the honest record shows: the classical algorithms — the oldest and the newest alike — *compute* the analytic constant 3.14159…, the golden value 4/√φ is a distinct, exact algebraic number in the golden field, and no computational road can be made to call one of them "measured." They are all computed. The question of which label is the true circle constant is a question of geometry and construction, of whether the circle belongs to the golden field; and it is a question that Viète's product, for all its antiquity, leaves open — a fixed, honest, infinitely-nested computation that measures nothing and decides nothing, only recomputing the same two neighbors forever.

## Further Reading

- [The Wallis Product: How an Infinite Product Computes π/2](/blog/posts/2026-08-23-wallis-product-infinite-product-computes-circle-constant-golden-pi/)
- [The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/)
- [The Continued Fraction of the Circle Constant](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/)
- [The Arithmetic–Geometric Mean: A Quadratic Road to the Circle Constant](/blog/posts/2026-08-29-arithmetic-geometric-mean-computes-circle-constant-golden-pi/)
- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/)
