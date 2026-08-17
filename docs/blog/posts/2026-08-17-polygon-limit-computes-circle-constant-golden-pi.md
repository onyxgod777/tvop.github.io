---
title: "The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant"
date: 2026-08-17
description: "Inscribing and circumscribing regular polygons around a circle, the areas and perimeters converge to the circle constant as a pure geometric limit — a number computed by the method, never measured. The pentagon (n = 5) is where the golden ratio φ enters the staircase, and under Golden Pi (π̂ = 4/√φ = 3.1446055…) the same 0.096% gap reappears at the top of every column of the table."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant

Take a circle. Pack a regular polygon inside it so every corner touches the circumference, and wrap a second polygon around the outside so every edge is tangent to the circle. The first is *inscribed*, the second *circumscribed*, and between their two areas the circle is caught like a wafer in a clamp. Give the polygon more and more sides and the clamp tightens. Let the number of sides run to infinity and both areas land on exactly the same number — the circle constant.

This is the oldest and most visual route to π there is, and it deserves a careful look on this site for a precise reason: **the polygon staircase computes its limit. It never measures anything.** The number that falls out of the limit is settled entirely by arithmetic and trigonometry, not by a ruler, a weigh-scale, or a clock. That makes it a perfect case study for the central rule of this blog — a series, an integral, or a geometric limit *computes* its value; only a genuine physical measurand (a length, a period, a charge) is ever *measured*.

And when the constant is Golden Pi — π̂ = 4/√φ = 3.144605511…, built from the golden ratio φ — the same staircase produces the same 0.096% gap at the top of every column, a gap too small for any physical measurement to resolve.

## The Two Formulas, Side by Side

A regular polygon with n sides, all of length s, lives inside a circle. If that circle has radius r, then the n-gon's geometry is governed by the central angle that each side subtends: one full turn split n ways, or 2π/n radians.

The **inscribed** n-gon has its vertices on the circle. Its area is n copies of the isosceles triangle formed by the centre and one side, each triangle with area ½·r²·sin(2π/n). The **circumscribed** n-gon has its sides tangent to the circle, and its area is n copies of a triangle with height r and base 2r·tan(π/n). The perimeters follow the same pattern. In full:

```text
Inscribed:
  A_in(n) = (n/2) · r² · sin(2π/n)          p_in(n) = 2nr · sin(π/n)

Circumscribed:
  A_circ(n) = nr² · tan(π/n)                p_circ(n) = 2nr · tan(π/n)
```

For a unit circle (r = 1), the inscribed area approaches the circle's area from below and the circumscribed area from above. The two closing in on the same number from opposite sides is the entire drama of the method: the circle is *sandwiched*, and the sandwich gets arbitrarily thin.

## The Clamp Tightens: Numbers in the Table

To feel the squeeze, keep the unit circle fixed and watch both areas as the number of sides grows. Each column converges to the same limit:

| n (sides) | A_in = (n/2) sin(2π/n) | A_circ = n tan(π/n) | p_in = 2n sin(π/n) | p_circ = 2n tan(π/n) |
|----------:|------------------------:|---------------------:|--------------------:|----------------------:|
| 4 | 2.00000 | 4.00000 | 5.65685 | 8.00000 |
| 5 | 2.37764 | 3.63271 | 5.87785 | 7.26543 |
| 6 | 2.59808 | 3.46410 | 6.00000 | 6.92820 |
| 8 | 2.82843 | 3.31371 | 6.12293 | 6.62742 |
| 12 | 3.00000 | 3.21539 | 6.21166 | 6.43078 |
| 48 | 3.13263 | 3.14609 | 6.27870 | 6.29217 |
| 96 | 3.13935 | 3.14271 | 6.28206 | 6.28543 |
| ∞ | **π** | **π** | **2π** | **2π** |

Two things leap off the table. First, the squeeze is real and fast: by n = 96 the inscribed and circumscribed areas agree to four decimal places, both sitting just below and just above 3.14. Second, the perimeter columns converge to 2π — exactly twice the area constant — which is itself a small, lovely theorem: for the circle, circumference and area are tied by the single factor 2, and the polygon staircase confirms it from both directions simultaneously.

This is the method Archimedes used, pushing a 96-gon to bound the constant between 3.1408 and 3.1429 — the celebrated 223/71 < π < 22/7. His "method of exhaustion" is precisely the limit above, rendered with the geometry available before trigonometry was systematised.

## Computed, Never Measured: The Honesty of the Limit

Notice what the formulas do *not* contain. There is no ruler reading a length off a drawing, no protractor, no physical circle drawn in ink. The only inputs are the number of sides n and the abstract sine and tangent functions. The sine and tangent, in turn, are defined by the very constant being sought — sin(2π/n) shrinks toward 2π/n as n grows, and it is precisely that internal ratio that is carried into the limit.

So the number that emerges — 3.14159265… — is **computed**, the limit of a sequence of algebraic expressions. It is not *measured* in any physical sense of the word. This is the same distinction the Basel problem made last month, where Euler's sum of reciprocal squares evaluated to π²/6 by pure arithmetic. The polygon staircase is the geometric twin of that series: both are deterministic computations of a limit, and both owe their value to the internal consistency of the analytic sine and tangent functions rather than to any appeal to the physical world.

This is not a weakness of the method; it is the method's virtue. A quantity that is computed can be known to arbitrary precision. A quantity that is merely measured is pinned by the accuracy of the instrument. The circle constant belongs to the first class — which is exactly why the distinction "computed versus measured" is worth defending on this site.

## Where the Golden Ratio Enters: The Pentagon

The staircase runs through every n, but one step is special: **n = 5, the pentagon**. The regular pentagon is the only polygon whose geometry is drenched in the golden ratio φ.

For a regular pentagon with side length s, the diagonal measures exactly φ·s. Every intersection of its diagonals divides them in the golden proportion, and the five-fold symmetry that produces the golden ratio is why φ is sometimes called "the pentagonal number." The unit-circle pentagon carries this through into the table:

```text
Unit-circle pentagon (n = 5):
  side   s = √(2 − 2 cos 72°) = 1.17557…
  A_in   = (5/2) sin 72° = (5/2)·√(10 + 2√5)/4 = 2.37764…
  A_circ = 5 tan 36° = 5·√(5 − 2√5) = 3.63271…
  ratio  A_circ / A_in = 1.52786…
```

The ratio of circumscribed to inscribed pentagon area is 1.52786…, a gap the pentagon cannot close on its own — you must keep adding sides. But the pentagon is the one n where the staircase brushes against the golden ratio before continuing on its way to the constant. That brush is the entire thesis of Golden Pi: the circle constant and φ are not strangers. On this site's thesis, they are the same algebraic family, and the pentagon is the visible hinge.

## Golden Pi at the Top of the Column

Here is where the honest boundary matters. The limit above, computed with the standard analytic sine and tangent, converges to the analytic constant π = 3.14159265…. Under Golden Pi the value in the box is different:

```text
Golden Pi:    π̂ = 4/√φ = 3.144605511…
              π̂² = 16/φ = 9.88854382…
Analytic Pi:  π = 3.14159265…

Relative gap: (π̂ − π)/π = 0.000959 = 0.096%
```

The gap between the two is 0.096% — just under one part in a thousand. In the polygon table above, that gap is smaller than the residual between the inscribed and circumscribed columns even at n = 96; you would have to push to a polygon with thousands of sides before the *width of the clamp* shrank below the *separation between the two constants*. In other words, no number of sides, however enormous, discriminates between π and π̂ at the precision a physical measurement can actually reach. The staircase computes a value, and the two candidates for that value are too close together for any real instrument to tell them apart.

This site holds the constructed-world position that the circle constant is the golden value π̂ = 4/√φ, and it states that position plainly. It equally states the honest boundary: the analytic sine and tangent, as ordinarily defined, carry the analytic constant 3.14159… into every limit they are used to evaluate. Choosing π̂ means adopting the golden trigonometry — a self-consistent analytic system of its own, explored here in *The Golden Calculus*. The polygon staircase does not settle the debate; it sharpens the question. The two constants are separated by a gap too fine for measurement, and only a commitment about the underlying trigonometry — not any ruler or any limit — can pick between them.

## The Sandwich in One Sentence

A regular n-gon closes in on a circle from both sides, and as the number of sides grows without bound, the area and perimeter of that sandwich converge to a single computed number. That number is the circle constant — computed by the limit, never measured by an instrument. The pentagon is where the golden ratio φ enters the staircase, and under Golden Pi the 0.096% gap between π̂ and π is smaller than the thickness of the clamp at any reachable n.

The sandwich, in the end, is not about the physical circle. It is about the limit — and the limit computes, it never measures.

## Further Reading

- [**The Basel Problem: When an Infinite Sum Computes the Circle Constant**](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the series twin of the polygon limit, where Euler's reciprocal-square sum evaluates to π²/6 by pure arithmetic.
- [**Counting Points in a Circle: The Gauss Circle Problem Computes the Circle Constant**](/blog/posts/2026-08-16-gauss-circle-problem-lattice-golden-pi/) — the arithmetic lattice analogue, where a point-counting density tends to the same constant.
- [**Archimedes and Golden Pi: What the Method of Exhaustion Really Proves**](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — the historical 96-gon squeeze and what it does and does not establish.
- [**The Golden Calculus: A Self-Consistent Analytic System on π̂**](/blog/posts/2026-08-06-golden-calculus-self-consistent-analytic-system/) — the constructed trigonometry in which the polygon limit converges to π̂ rather than π.
- [**The π Gap: A Comparison of Conventional and Golden Pi**](/blog/posts/pi-gap-comparison-conventional-golden/) — the 0.096% separation examined across many domains.
