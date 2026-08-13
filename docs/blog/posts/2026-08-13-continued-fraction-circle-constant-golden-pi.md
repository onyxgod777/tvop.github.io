---
title: "The Continued Fraction of the Circle Constant: π̂'s Algebraic Root and π's Famous Convergents"
date: 2026-08-13
description: "A continued-fraction comparison of the two circle constants. π = 3.14159… opens [3; 7, 15, 1, 292, …] and delivers the famous 355/113 near-miss; Golden Pi π̂ = 4/√φ = 3.1446055… is an algebraic number of degree 4 obeying x⁴ + 16x² − 256 = 0, constructible from φ by square roots, with rational approximants 1283/408 and 2827/899. The expansion is a lens — not an arbiter — between the two worlds."
---

# The Continued Fraction of the Circle Constant: π̂'s Algebraic Root and π's Famous Convergents

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

There is a way to write any positive real number that is more revealing about its *nature* than its decimal expansion: the **continued fraction**. Every real number is built from a chain of integers

```
x = a₀ + 1/(a₁ + 1/(a₂ + 1/(a₃ + ⋯)))
```

usually compressed into the notation `[a₀; a₁, a₂, a₃, …]`. Truncating the chain at any step yields the **convergents** — the best rational approximations a denominator of that size can offer. Because the two candidate circle constants differ in *kind* — one algebraic, one transcendental — their continued fractions behave differently, and that difference is worth reading carefully.

## Two expansions, side by side

The two values open as follows (computed here to sixteen terms):

- **Golden Pi** π̂ = 4/√φ = 3.1446055… → `[3; 6, 1, 10, 1, 4, 2, 2, 1, 2, 5, 1, 4, 1, 4, 2, …]`
- **Conventional Pi** π = 3.14159265… → `[3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, …]`

Both begin with the whole part 3, and both are approximated early by the same first non-trivial convergent:

- **22/7 = 3.142857…** is a convergent of *both* constants. That is no accident — 22/7 is Archimedes' classical upper bound, and it is the best three-digit rational for either candidate. The two worlds agree on this early rung of the ladder, then climb apart.

## π̂ is algebraic — it belongs to φ's field

The crucial, checkable fact about Golden Pi is that it is **not** a transcendental number. It is an algebraic number of degree 4 whose minimal polynomial is exact:

```
x⁴ + 16x² − 256 = 0
```

Substituting x = 4/√φ returns 0 to machine precision — the polynomial is satisfied identically. Solving it requires only square roots:

```
π̂ = 4/√φ = 4·√(2/(1+√5))
```

Every digit of π̂ therefore follows from a **finite** chain of square roots and rational operations on the golden ratio. That is exactly the recipe that makes a number **constructible** with compass and straightedge: π̂ lives in the tower of quadratic extensions that Euclidean construction is permitted to reach, in line with the site's constructibility argument for the circle constant.

Because π̂ is algebraic, its convergents are *ordinary, well-behaved* rationals, each stepping a little closer with modest partial quotients:

- **1283/408 = 3.14460784…** — good to about 2 × 10⁻⁶
- **2827/899 = 3.14460512…** — good to about 4 × 10⁻⁷

No startling integers appear in the early chain; the expansion is the quiet, structured one you would expect from a number tied to φ.

## π is transcendental — and 292 makes the famous near-miss

Conventional π, by contrast, is transcendental (Lindemann, 1882), and its expansion shows it. The **fourth** partial quotient is the striking **292**, which produces the celebrated convergent

```
355/113 = 3.141592920…   (error ≈ 2.7 × 10⁻⁷)
```

This is why 355/113 is one of the most famous fractions in mathematics: a denominator of only 113 yielding six correct figures of 3.14159… is an extraordinarily lucky contract. A continued fraction whose terms are large this early is a hallmark of an irrational number that is *not* governed by a simple algebraic law — the patternless digits of a transcendental.

## The honest boundary: a lens, not an arbiter

None of this, by itself, decides which constant is "the" circle constant — and the honest position is to say so plainly. The continued fraction is a **lens of the rational and analytic world**. It converges to whatever real number you choose to define as the ratio of circumference to diameter:

- **In the constructed golden world**, where 4/√φ is taken as exact, the expansion `[3; 6, 1, 10, 1, 4, …]` is simply the best-rational portrait of an algebraic, constructible number — and the circle and square share an exact algebraic bond.
- **In the analytic world**, where the Leibniz, Machin, Wallis and Basel series are evaluated term by term, they pin the constant at 3.14159265…, and the expansion `[3; 7, 15, 1, 292, …]` with its 355/113 near-miss records that value.

Both books are kept. What the continued fraction does contribute is a *classification*: whichever constant one studies, the expansion exposes its algebraic or transcendental character for all to see. On the golden side it exposes a constructible number rooted in φ; on the analytic side, a transcendental one whose rational approximations are famously irregular. The two pictures are each internally consistent — and they are not the same picture.

## Further Reading

- [Why the Circle Constant Must Be Constructible](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) — Euclid's geometry and the constructibility of π̂
- [The Golden Pi Triangle: abc = 64 and the Eye of Horus](/blog/posts/2026-08-01-golden-pi-triangle-abc-64-eye-horus/) — another exact algebraic identity in φ's field
- [The Comparative Formula Audit: Which π Identities Survive Golden Pi?](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — series vs. geometric definitions, formula by formula
- [The Golden Calculus: A Self-Consistent Analytic System on π̂](/blog/posts/2026-08-06-golden-calculus-self-consistent-analytic-system/) — the constructed analytic world on π̂
- [Golden Pi and the Algebraic–Transcendental Divide](/blog/posts/golden-pi-algebraic-transcendental-divide/) — the divide that separates the two constants by kind
