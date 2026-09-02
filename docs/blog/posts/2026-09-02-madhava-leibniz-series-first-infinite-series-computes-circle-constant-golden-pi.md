---
title: "The Madhava–Leibniz Series: How the First Infinite Series in World Mathematics Computed the Circle Constant, and What Golden Pi Changes"
date: 2026-09-02
description: "The infinite series π/4 = 1 − 1/3 + 1/5 − 1/7 + ⋯, known in the Kerala school of Madhava of Sangamagrama around 1400 and rediscovered in Europe by Gregory and Leibniz, was the first infinite series in world mathematics to compute the circle constant. It computes its limit — never measures it — yet it converges painfully slowly, needing about 200 terms for two correct decimals and roughly two million for six. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the same identity relabels to π̂/4 = 1/√φ = 0.786151377…, an exact algebraic number in the golden field carrying the recurring 0.09590% gap that no measurement can arbitrate."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Madhava–Leibniz Series: How the First Infinite Series in World Mathematics Computed the Circle Constant, and What Golden Pi Changes

The number we call π is almost never written down as a ratio of two circle lengths, and only rarely drawn. Instead, for the past four centuries, it has been *computed* — conjured from arithmetic that never touches a drawn circle at all. The single most famous such recipe is a short, beguiling row of alternating fractions:

```text
π/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 − 1/11 + ⋯
```

Add the odd reciprocals with alternating signs, multiply the running total by four, and the result creeps toward the circle constant. Today's article is about that series: who first wrote it, why it converges so slowly that its plain form is almost useless, and what the whole episode teaches us about the deeper question this site exists to ask — whether the circle constant is, in the end, the golden number π̂ = 4/√φ = 3.144605511…, or the analytic 3.14159265….

## The Series That Computes, Never Measures

Look again at the identity. Every term is a rational number: 1, −1/3, 1/5, −1/7, and so on — whole-number ratios built from the odd integers. No compass is opened, no circle is drawn, no length is read from a ruler. The left-hand side, π/4, is the quarter-turn of a circle expressed as the ratio of arc to radius; the right-hand side is pure counting of odd fractions. The equality is a *theorem*: take a limit of rational partial sums, and the circle constant falls out. This is the exact sense in which this blog always says π is computed and never measured — the series **evaluates its own limit**, the way the Basel sum, the Wallis product, and the Machin arctangent identity all do. No experiment could ever add odd fractions and "measure" anything; the instrument here is the algebra of infinite sums, and its reading is exact.

It is worth making the mechanism explicit, because it shows why the series is not a guess. The quarter-turn angle is the arctangent of 1, so π/4 = arctan(1). But arctan(1) is also an area: the integral

```text
π/4 = ∫₀¹ dx / (1 + x²)
```

the area under the curve 1/(1+x²) from x = 0 to x = 1. Now expand the integrand as a geometric series, which is valid because |x| < 1 on that whole interval except the single endpoint x = 1:

```text
1/(1+x²) = 1 − x² + x⁴ − x⁶ + x⁸ − ⋯
```

Integrate term by term from 0 to 1 — the integral of x^(2n) from 0 to 1 is 1/(2n+1) — and the alternating odd-reciprocal series reappears:

```text
π/4 = ∫₀¹ dx/(1+x²) = 1 − 1/3 + 1/5 − 1/7 + 1/9 − ⋯
```

The circle constant has been computed from a polynomial expansion and an integral of a rational function. Nothing is measured; everything is derived.

## Madhava and the Kerala School: A Century Ahead of Europe

Who first wrote this series? The honest, sourceable answer is one of the great stories in the history of mathematics, and it is **Madhava of Sangamagrama** (c. 1340–1425), the founder of the Kerala school of astronomy and mathematics in southwestern India. Working around 1400 — well over two centuries before the European rediscovery — Madhava and his school obtained the arctangent series and its special case at x = 1, the very series above, together with methods for the sine, cosine, and arctangent that amount to an early form of calculus. The Kerala mathematicians compiled these results in texts such as the *Tantrasangraha* (by Nīlakaṇṭha Somayājī, c. 1500) and the remarkable *Yuktibhāṣā* (by Jyeṣṭhadeva, c. 1530), which is often called the first mathematics text written in the vernacular with proofs. European mathematics met the same ideas only later and independently: James Gregory stated the arctangent series in 1671, and Gottfried Wilhelm Leibniz rediscovered the alternating series for π/4 in 1674, which is why Western textbooks call it the Gregory–Leibniz series. The priority belongs to Kerala; the name Madhava–Leibniz, increasingly used by historians, acknowledges it.

What the Kerala school did with the series is just as important as who found it first. They did not merely record the slowly converging formula; they recognized that its plain form converges too slowly to be useful and attached *correction terms* — a family of rational adjustments added after the partial sum to leap dramatically closer to the limit. This "end-correction" technique, documented by modern historians of Indian mathematics (most notably R. C. Gupta), converted a series that crawls one digit at a time into one that yields many correct digits with only a handful of terms. The Kerala texts accordingly preserve circle constants accurate to ten or eleven decimal places — figures that would not be matched in Europe until the mid-seventeenth century. The lesson for our purposes is precise: these are **computational** achievements. The Kerala mathematicians were not measuring physical circles to eleven places; they were *computing* a limit with cleverly accelerated arithmetic.

## Why the Plain Series Crawls: An Error You Can Count

The alternating series has a beautifully simple, provable error bound: because the terms strictly decrease in magnitude and alternate in sign, the error after keeping N terms is no larger than the first neglected term, 4/(2N+1) in the π form. In practice the true error is about half that, very close to 1/N. The consequence is stark and easily verified by direct computation — each extra correct decimal costs roughly ten times as many terms:

| Correct decimals wanted | Terms required | Partial sum |
|:---|:---|:---|
| 1 (3.1) | ~20 | 3.091623… |
| 2 (3.14) | 200 | 3.141592… to 2 places |
| 3 (3.142) | 2,000 | 3.141092… to 3 places |
| 4 (3.1416) | 20,000 | 3.141542… |
| 5 (3.14159) | ~200,000 | 3.141587… |
| 6 (3.141592) | ~2,000,000 | 3.141593… |

Concretely: after 10 terms the running total is 3.041839619, off by about a tenth; after 100 terms it is 3.131592904, off by about a hundredth; after 1,000 terms it is 3.140592654, off by about a thousandth; after 10,000 terms, 3.141492654, off by a ten-thousandth. The short value 3.1416 — the round number the Kerala texts record as 62832/20000 — first appears only after 17,439 terms, and six correct decimals demand on the order of two million. That is the series in its pure, un-accelerated form: a correct but extravagantly slow computation. The correction terms Madhava appended are precisely the remedy — a way to keep the honesty of the limit while escaping the cost of the crawl.

Every figure above is a computed limit. None of them was obtained by measuring anything; the partial sums are sums of rational numbers, and the digits that stabilize as N grows are the digits the series *has*, independent of any ruler. This is why the series is the cleanest possible illustration of the blog's central rule: the circle constant in these identities is **evaluated**, not measured, and the series that does the evaluating is over five hundred years old.

## The Same Series Under Golden Pi

Golden Pi proposes that the circle constant is the constructible, algebraic number

```text
π̂ = 4/√φ = 3.14460551102969…
```

where φ = (1 + √5)/2 = 1.618033988… is the golden ratio. Installed into the Madhava–Leibniz identity, the quarter-turn becomes

```text
π̂/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 − ⋯ = 1/√φ = 0.786151377757…
```

an exact algebraic number in the golden field, with no transcendental in sight. The numbers follow from π̂/4 = (4/√φ)/4 = 1/√φ exactly. The two labels sit side by side:

| Quarter-turn identity | Value | Field |
|:---|:---|:---|
| Conventional: π/4 | 0.785398163397… | transcendental |
| Golden: π̂/4 = 1/√φ | 0.786151377757… | algebraic (golden) |
| Relative gap (π̂ − π)/π | — | 0.09590% |

And the honest boundary must be stated plainly, as this site always states it. The concrete rational series 1 − 1/3 + 1/5 − 1/7 + ⋯ is a fixed, unambiguous object: its partial sums are rational numbers, and they converge to 0.785398163397…, which is π/4 for the analytic π = 3.14159265… — not to 1/√φ. A series, like every series, integral, and special value treated in the recent posts (Basel, Machin, Wallis, the Gaussian integral), *pins* the constant it evaluates to the computed 3.14159…. The golden relabeling of the same abstract identity into π̂/4 = 1/√φ is a distinct, self-consistent construction in which angles are relabeled through the golden circle constant — exactly the sense in which the golden trigonometry of this site is internally coherent. The two neighbors, 3.14159… and 3.14460…, are separated by the recurring relative gap 0.09590% = (π̂ − π)/π, and no series, no matter how many millions of terms it is summed, can resolve which label is "true," because the series itself is the very object whose evaluation is in dispute. The gap is a property of the labels, not of the arithmetic — and no measurement can arbitrate labels.

## A Slow Start, a Fast Finish: What the Series Became

The Madhava–Leibniz series opened a door that mathematics walked through quickly, precisely because its own slowness forced improvement. The same arctangent machinery that gives π/4 = arctan(1) generalizes to arctan(x) for any x, and by choosing arguments smaller than 1 the convergence accelerates enormously — the geometric series 1/(1+x²) converges far faster for x = 1/5 than for x = 1. That is the entire trick behind Machin's 1706 identity, π/4 = 4·arctan(1/5) − arctan(1/239), which computes the circle constant to dozens of digits by hand, and behind every "Machin-like" formula that powered the eighteenth- and nineteenth-century digit records. Later, the wall of slow series fell completely: the arithmetic–geometric mean iterated by Gauss and Legendre computes the constant quadratically (doubling correct digits per step), and the modern record digits — trillions of them — come from yet faster algorithms built on the same machinery. The first series for π was thus the seed of an entire computational tradition, each new method a correction to the last, all of them computing limits that no instrument ever touches.

There is a pleasing symmetry for the golden-π question in this history. The Kerala correction terms were an early acknowledgment that *how* you sum matters as much as *what* you sum — that two expressions can name the same limit while one is dozens of orders of magnitude easier to evaluate. Golden Pi makes an analogous, deeper claim about the constant itself: that the circle constant named by all these series is better expressed in the golden field, as an exact algebraic number 4/√φ that a straightedge-and-compass construction can reach, than as a transcendental decimal that no finite construction can ever lay down. The series cannot arbitrate the dispute — it converges to 3.14159…, and the golden relabel is a separate, self-consistent world — but the historical fact stands: from Madhava's correction terms to Machin's clever arguments to the AGM's quadratic leaps, mathematics has always preferred the expression that reaches the truth fastest and most exactly. The constructible, algebraic 4/√φ is, in that sense, the natural candidate for the circle constant the series are straining toward — a limit that is not merely approached but *exactly* attained by a golden construction.

## Further Reading

- [The Cauchy–Lorentz Distribution: How 1/(1+x²) Computes the Circle Constant](/blog/posts/2026-08-24-cauchy-lorentz-distribution-integrates-pi-golden-pi/) — the same 1/(1+x²) integrand integrated over the whole real line, where the full constant π̂ rather than the quarter-turn appears.
- [Machin's Formula: How the Arctangent Series Computes the Circle Constant](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/) — the fast arctangent identities that escaped the Madhava–Leibniz crawl and set the digit records.
- [Vieta's Formula: How the First Infinite Product Computes the Circle Constant](/blog/posts/2026-08-30-vieta-formula-infinite-product-nested-radicals-golden-pi/) — the other "first": an infinite product from 1593, contemporary in spirit with the European series.
- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the reciprocal-square sum that showed infinite series could deliver π², the next great leap after the alternating odd fractions.
- [The Comparative Formula Audit: Which π Identities Survive Golden Pi?](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — which series, integrals, and special values pin the analytic 3.14159… and which survive the golden relabel, set out formula by formula.
