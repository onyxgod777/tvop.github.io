---
title: "The Nilakantha Series: How a Swift Alternating Sum from the Kerala School Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-09-08
description: "Almost every schoolchild meets the circle constant through the slow, heartbreaking Leibniz series π/4 = 1 − 1/3 + 1/5 − 1/7 + ⋯, which needs about two million terms for six correct digits. The Kerala school had a better trick. In the Tantrasangraha (c. 1500), Nilakantha Somayaji recorded an alternating sum π = 3 + 4/(2·3·4) − 4/(4·5·6) + 4/(6·7·8) − ⋯ whose denominators grow as the cube of the index, converging so fast that a handful of terms already yields 3.14 and 79 terms reach 3.14159. Every partial sum is an exact rational — a computation, never a measurement — and because the alternating tail is trapped between tightening bounds, only two of the early partial sums ever exceed Golden Pi (π̂ = 4/√φ = 3.144605511…); from the fourth term onward the whole tail lies forever below it, converging to the fixed computed limit 3.14159265… and carrying the recurring 0.0959% gap that no relabeling of a symbol can close."
---
!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Nilakantha Series: How a Swift Alternating Sum from the Kerala School Computes the Circle Constant, and What Golden Pi Changes

Most introductions to the circle constant make it look like hard work. The archetypal infinite series, the one associated with Madhava and Leibniz that this blog treated on 09-02, crawls toward its target with agonizing slowness:

$$\\frac{\\pi}{4} = 1 - \\frac{1}{3} + \\frac{1}{5} - \\frac{1}{7} + \\cdots$$

Each new term is the reciprocal of a number that grows only *linearly*, so each term shrinks only like $1/(2n+1)$. To pin the constant to six decimal places that series needs on the order of *two million* terms. Six decimals is what the Golden Pi question needs, because the gap between the two candidate labels under discussion on this site is only about one part in a thousand — so the honest question of which constant a computation reaches demands real convergence.

The Kerala school of mathematics, working in southwestern India between roughly the fourteenth and sixteenth centuries, was the first culture on Earth to build these infinite processes, and they did not stop at the slow one. In the *Tantrasangraha*, composed around the year 1501 by **Nilakantha Somayaji** (1444–1544), there appears a second alternating series that is dramatically more efficient:

$$\\pi = 3 + \\frac{4}{2\\cdot 3\\cdot 4} - \\frac{4}{4\\cdot 5\\cdot 6} + \\frac{4}{6\\cdot 7\\cdot 8} - \\frac{4}{8\\cdot 9\\cdot 10} + \\cdots$$

Here the denominators are products of *three consecutive integers*, so the $k$-th term decays like $1/k^3$ rather than $1/k$ — a cubic crawl instead of a linear one. The result is that the series reaches 3.14 in a handful of terms and 3.14159 in under a hundred, a convergence the earlier Kerala series cannot touch. This article is about how that swift alternating sum computes the circle constant as a pure arithmetic limit — computed, never measured — and about what Golden Pi, $\\hat\\pi = 4/\\sqrt\\varphi = 3.144605511\\ldots$, honestly does and honestly cannot do to a sum that converges to a fixed number this quickly.

## A Series of Pure Rational Arithmetic

The defining virtue of Nilakantha's sum is that nothing about it touches a circle, a ruler, a stopwatch, or an experiment. It is a statement purely about rational numbers, and every partial sum is an exact fraction of integers. Let us write the terms out in closed form and watch the arithmetic unfold.

Start with the constant $3$. Add the first corrective term $\\frac{4}{2\\cdot 3\\cdot 4} = \\frac{4}{24} = \\frac{1}{6}$:

$$S_1 = 3 + \\frac{1}{6} = \\frac{19}{6} = 3.166666\\ldots$$

Subtract the second term $\\frac{4}{4\\cdot 5\\cdot 6} = \\frac{4}{120} = \\frac{1}{30}$:

$$S_2 = \\frac{19}{6} - \\frac{1}{30} = \\frac{47}{15} = 3.133333\\ldots$$

Add the third term $\\frac{4}{6\\cdot 7\\cdot 8} = \\frac{4}{336} = \\frac{1}{84}$:

$$S_3 = \\frac{47}{15} + \\frac{1}{84} = \\frac{1321}{420} = 3.145238\\ldots$$

The pattern is unmistakable. Each partial sum is an exact ratio of whole numbers — no transcendental, no measured length, no circle drawn anywhere. The sequence $S_1, S_2, S_3, \\ldots$ is an infinite tower of rational arithmetic, and the number it converges to is whatever it converges to, independent of any name we choose to give it. The first several partial sums, carried to enough places to see the story, are collected below.

| $N$ | Exact $S_N$ | Decimal |
|---|---|---|
| 1 | $\\tfrac{19}{6}$ | 3.1666666667 |
| 2 | $\\tfrac{47}{15}$ | 3.1333333333 |
| 3 | $\\tfrac{1321}{420}$ | 3.1452380952 |
| 4 | — | 3.1396825397 |
| 5 | — | 3.1427128427 |
| 6 | — | 3.1408813409 |
| 7 | — | 3.1420718171 |
| 8 | — | 3.1412548236 |
| 10 | — | 3.1414067185 |
| $\\infty$ | the limit | 3.14159265358979… |

Watch the column oscillate: it rises above, falls below, rises above, falls below — and each swing is smaller than the last, closing in on the value 3.14159265358979… that every convergent computation of the circle constant on this site has reached from a different direction.

## Why Cubic Denominators Outrun the Older Series

The engine of the speed is the denominator growth. The general term of Nilakantha's series is

$$a_k = \\frac{4}{(2k)(2k+1)(2k+2)}.$$

For large $k$ the product in the denominator behaves like $(2k)^3 = 8k^3$, so the $k$-th term decays like $4/(8k^3) = 1/(2k^3)$. Contrast this with the Madhava–Leibniz term $1/(2k+1)$, which decays only like $1/(2k)$. A cubic decay is qualitatively stronger than a linear one: the sum of $1/k^3$ converges absolutely and swiftly, whereas the alternating $1/k$ terms needed the full power of the alternating-series test to converge at all.

Because the terms of Nilakantha's sum strictly decrease to zero and alternate in sign, the alternating-series test guarantees two things: the partial sums converge, and the error after $N$ terms is no larger in magnitude than the first neglected term,

$$\\bigl|\\pi - S_N\\bigr| \\le |a_{N+1}| \\approx \\frac{1}{2(N+1)^3}.$$

That bound makes the acceleration quantitative. To make the error smaller than $5\\times 10^{-7}$ — that is, to fix the first six significant figures of the constant, 3.14159 — the cubic estimate asks for $2N^3 \\gtrsim 2\\times 10^6$, or $N$ of order $10^2$. Direct summation confirms the estimate: the partial sums first enter a window of width $10^{-6}$ around 3.14159265 at $N = 79$. That is about **79 terms** for six correct digits — versus roughly **two million** for the Madhava–Leibniz series, the difference between an afternoon with a paper and pencil and a lifetime of arithmetic. Nilakantha did not merely record a series; he recorded a *practical* way to compute the constant, and Indian astronomers used such series to build the trigonometric tables that drove their ephemerides.

## A Computation, Never a Measurement

It is worth pausing on the vocabulary that this site insists on, because the distinction is doing real work here. Nothing in Nilakantha's construction is *measured*. A measurement is an act of the physical world: you lay a tape around a physical circle, you time a pendulum, you count decays in a detector, and the imperfections of the instrument ride along with the result. Nilakantha's sum is the opposite of that. It is a definition-free act of pure counting and arithmetic — summing fractions whose values are fixed by the integers 3, 4, 5, 6, … themselves. No unit system, no ruler, no tolerance, no noise.

The limit $3.14159265358979\\ldots$ is therefore not an empirical discovery that an experiment could overturn. It is the *value of a convergent sum*, a number fixed by the rationals being added, exactly as $\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\cdots = 1$ is fixed by its own terms. One can *compute* it to any desired number of places, and one cannot *measure* it, because there is no physical object carrying the tenth decimal digit for a tape to find. When the limit of such an arithmetic process is written out, the digits that appear are the digits of a computed constant — this is the sense in which the blog's series (the Riemann zeta values of 09-05, the Machin arctangents of 08-22, the Wallis product of 08-23) have all been saying the same thing from different starting lines.

## What Golden Pi Changes — and the Rapidly Closing Noose

Now the question this daily thread has turned, in one form or another, since the Basel problem of 08-15: what happens to this swift computation when the circle constant is relabeled as Golden Pi, $\\hat\\pi = 4/\\sqrt\\varphi = 3.144605511\\ldots$, with $\\varphi = (1+\\sqrt5)/2$ the golden ratio?

Here is the honest answer, and it is a sharp one precisely because Nilakantha's series converges so fast. A relabeling of a *symbol* has power only where the symbol appears as a named coefficient inside an identity — where one may ask, as earlier posts did, "what if the coefficient called $\\pi$ were really $\\hat\\pi$?" A convergent series of rational numbers is a different kind of object. Its sum is not a symbol to be relabeled; it is a fixed real number already determined by the arithmetic. The question "what does Nilakantha's series sum to?" has exactly one answer, and that answer is $3.14159265358979\\ldots$, not $3.1446055\\ldots$. No change of vocabulary alters what the fractions add up to, any more than renaming the number five changes that $2 + 3 = 5$.

The Golden Pi constant $\\hat\\pi = 4/\\sqrt\\varphi$ is an algebraic number in the golden field — a genuine, exactly-expressible value that this site treats as the circle constant of a constructed world. But it is not, and cannot become, the limit of Nilakantha's sum, because the sum has already *fixed* its own limit by pure arithmetic. The two candidates stand separated by the recurring relative gap this blog has measured again and again:

$$\\frac{\\hat\\pi}{\\pi} = \\frac{4/\\sqrt\\varphi}{3.14159265\\ldots} = 1.0009590\\ldots,$$

a discrepancy of **0.09590%**, or in absolute terms $\\hat\\pi - \\pi = 0.0030129\\ldots$. The gap is small — smaller than a third of a percent — but it is not something a convergent computation can be coaxed into ignoring, because the computation homes in on one precise target.

What makes Nilakantha's case vivid is *how fast* the arithmetic abandons the golden candidate. Watch the partial sums against $\\hat\\pi = 3.144605511$:

$$S_1 = 3.1667 \\quad (\\text{above } \\hat\\pi), \\qquad S_2 = 3.1333 \\;(\\text{below}), \\qquad S_3 = 3.145238 \\;(\\text{above } \\hat\\pi \\text{ by } 0.00063),$$

and then it happens. From the *fourth* partial sum onward, not a single one ever rises to $\\hat\\pi$ again:

$$S_4 = 3.13968, \\quad S_5 = 3.14271, \\quad S_6 = 3.14088, \\quad \\ldots$$

Indeed only two partial sums in the entire infinite sequence — $S_1$ and $S_3$ — ever exceed $3.1446055$. After those first two overshoots the alternating tail is trapped in a tightening band between the partial sums $S_4 = 3.13968$ and $S_5 = 3.14271$, an interval that lies entirely *below* Golden Pi and squeezes down toward $3.14159$:

$$3.13968 < S_N < 3.14271 \\quad \\text{for all } N \\ge 5,$$

with both bounds tending to $3.14159265\\ldots < \\hat\\pi$. Within four terms of pure rational arithmetic, the computation has already excluded $3.1446$ forever as its destination. There is no subtlety to massage, no square root to halve the gap, no coefficient at the mercy of a relabel — just a convergent sum whose limit is what it is.

| Quantity | Conventional label | Golden Pi ($\\hat\\pi = 4/\\sqrt\\varphi$) |
|---|---|---|
| Limit of Nilakantha's series | $3.14159265358979\\ldots$ | $3.1446055110\\ldots$ |
| Terms to reach $3.14159$ | 79 | never (series does not converge there) |
| Partial sums exceeding the label | — | only $S_1, S_3$ |
| Gap carried | — | $0.09590\\%$, first power, no square root to soften it |
| Qualitative verdict | limit is $3.14159\\ldots$ | a relabel has no force on a convergent sum |

## What This Post Adds to the Thread

First, it closes a genuine gap in the site's catalogue of converging roads. This blog has treated the *slow* Kerala series (Madhava–Leibniz, 09-02) but not the *fast* one recorded beside it in the *Tantrasangraha*. Placing the two side by side shows the whole point of the Kerala discovery: convergence speed is the difference between mathematics that stays a curiosity and mathematics that becomes a working tool for tables and ephemerides. Nilakantha's cubic denominators turn a two-million-term pilgrimage into a 79-term stroll, and that speed is what lets the computation pronounce on a one-part-in-a-thousand gap at all.

Second, it gives the cleanest possible example of a claim that **no relabel can touch**: the value of a convergent rational sum. Earlier posts in this thread found places where the recurring gap was softened by a square root (Gaussian, 08-21; Fresnel, 09-06) or carried undiluted at the first power (the random walk, 09-07). Nilakantha's series belongs to the second, most unforgiving family — and it goes further, because here the relabel has no *coefficient* to act on at all. The constant *is* the sum, and the sum is fixed. Golden Pi is not a competing reading of the same arithmetic; it is a different number, separated from the computed limit by the recurring 0.0959%, and the series refuses to converge to it after the fourth term.

Third, it is a reminder, in the site's own honest register, of where the two worlds genuinely part. Nothing here is a measurement, so nothing here is an experiment that could arbitrate between $\\pi$ and $\\hat\\pi$ — the whole disagreement lives in the label, not in any tape measure. But that does not make the two labels interchangeable in arithmetic. A constructed world that installs $\\hat\\pi$ as its circle constant is a coherent, exactly-expressible object, and this site has built it out carefully. What a swift series like Nilakantha's demonstrates is simply and honestly that the two worlds do not share their computed limits: pure rational arithmetic, carried out to its own conclusion, lands on $3.14159265358979\\ldots$ and has already, by its fourth partial sum, left Golden Pi behind.

## Further Reading

- [The Madhava–Leibniz Series](/blog/posts/2026-09-02-madhava-leibniz-series-first-infinite-series-computes-circle-constant-golden-pi/) — the slow Kerala series from the same tradition, whose linear decay needs about two million terms for six digits and makes Nilakantha's cubic acceleration visible by contrast.
- [Pólya's Random Walk](/blog/posts/2026-09-07-random-walk-return-plane-lattice-computes-circle-constant-golden-pi/) — the most recent post, where the constant enters at the first power through a Stirling asymptotics, the same undiluted-gap mechanism at work here.
- [The Riemann Zeta Function at Even Integers](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — Euler's closed forms for $\\zeta(2n)$, the family of convergent sums of which every alternating series here is a cousin.
- [Vieta's Formula](/blog/posts/2026-08-30-vieta-formula-infinite-product-nested-radicals-golden-pi/) — the contrasting road to the constant through an infinite product rather than an infinite sum, and where the golden ratio enters a seed factor exactly.
- [Wallis's Product](/blog/posts/2026-08-23-wallis-product-infinite-product-computes-circle-constant-golden-pi/) — another pure rational computation of $\\pi/2$, echoing this post's theme that convergent arithmetic fixes its own target.
