---
title: "Ptolemy's Table of Chords: How Inscribed Chords Computed the Circle Constant, and What Golden Pi Changes"
date: 2026-09-15
description: "The Almagest's table of chords turns circle geometry into pure rational arithmetic: a chord is 2sin(θ/2), fixed by geometry and never touching the circle constant, while the constant enters only as the arc the chord spans. Ptolemy's computed value 377/120 = 3.1416667 (3;8;30 in sexagesimal) sits +0.0023559% from the analytic constant and −0.0934567% from Golden Pi (π̂ = 4/√φ = 3.144605511…) — 40.7× closer to the analytic value — and the same rational exhaustion bracket [223/71, 22/7] excludes π̂ by 0.0556299% without a single measurement, while feeding π̂ into the identical algorithm closes the bracket on π̂ instead."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Ptolemy's Table of Chords: How Inscribed Chords Computed the Circle Constant, and What Golden Pi Changes

The previous articles in this series have all followed the same shape. An integral converges, a series sums, a solid angle integrates — and in every case the circle constant arrives as a **computed limit**, never as the output of an instrument. Claudius Ptolemy's *Almagest* (c. 150 CE) is the oldest artifact in that tradition that survives in usable technical detail, and it does something the modern formulas do not: it removes the circle constant from the problem almost entirely.

<div class="gp-live" markdown>
<div class="gp-live__tag">🔬 Live graph · Laws of appearance</div>
<iframe src="https://www.desmos.com/calculator/gzm8tmnjit?embed" width="100%" height="470" style="border:0;border-radius:10px" frameborder="0" loading="lazy" title="What a real disc can resolve" allowfullscreen></iframe>
<p class="gp-live__note"><strong>Measurement feasibility: how far apart the two candidates are in millimetres on a physical disc.</strong> <em>The Goblet of the Truth keeps two bodies of law apart — the laws and recommendations of the primal power (Creation), and the <strong>laws of appearance (nature)</strong> (Ch&nbsp;2 §342), the register governing how a thing manifests and behaves. Geometry answers to that second register, so nothing here asks to be taken on authority: drag the slider, change a value, and the figure answers for itself (Ch&nbsp;22 §35: <em>“the fluidal-powers are truthful effects of natural laws”</em>).</em></p>
</div>

A table of chords is not a table of angles. It is a table of *straight lines* — lengths of the segments joining two points on a circle — and every one of those lengths is fixed by pure geometry, provable by Pythagoras and the pentagon, and computable to any precision with nothing but square roots. The circle constant appears only when you ask what **arc** a chord spans, and that step is a coordinate choice. That separation is the cleanest diagnostic this series has found for sorting what Golden Pi ($\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$) relabels from what it breaks.

## The Chord Function: A Length That Never Mentions the Constant

On a circle of radius $1$, define the chord function

$$\operatorname{crd}(\theta) = 2\sin\frac{\theta}{2},$$

the straight-line distance between two points separated by a central angle $\theta$. The factor of $2$ and the halving of the angle are not decoration: they are what turns an angle into a length. The exact values are the ones every schoolchild can construct with a compass:

| Central angle | Chord (radius 1) | Exact form | Source |
|---|---|---|---|
| $60°$ | $1.0$ | $1$ | hexagon side |
| $90°$ | $1.414213562373095$ | $\sqrt{2}$ | square side |
| $120°$ | $1.732050807568877$ | $\sqrt{3}$ | equilateral triangle |
| $180°$ | $2.0$ | $2$ | diameter |
| $36°$ | $0.618033988749895$ | $1/\varphi$ | decagon side |
| $72°$ | $1.175570504584946$ | $\sqrt{3-\varphi}$ | pentagon side |
| $12°$ | $0.209056926535307$ | — | interpolated |
| $24°$ | $0.415823381635519$ | — | interpolated |

Every entry is a length. Not one of them mentions the circle constant. The hexagon chord is $1$ because six equilateral triangles tile the circle; the decagon chord is $1/\varphi$ because $\varphi = 2\cos(\pi/5)$, a fact about the pentagon that was known to Euclid, not a fact about any constant at all. The supplement identity

$$\operatorname{crd}^2(\theta) + \operatorname{crd}^2(\pi - \theta) = 4$$

holds exactly — evaluated at $18°$ it returns $0.097887\ldots + 3.902113\ldots = 4$ to all forty digits computed here — and it too is a statement about lengths.

This is the first hint of the article's theme. If you want to argue about the circle constant, the chord table is a bad place to do it: the numbers in it are geometric truths that a relabel cannot touch, and they are the raw material from which the constant itself gets computed.

## Ptolemy's Theorem: The Engine That Builds the Table

The table could not be built by compass alone; it needed a recurrence. Ptolemy's theorem supplies it. For any cyclic quadrilateral $ABCD$,

$$AC \cdot BD = AB \cdot CD + BC \cdot AD,$$

the products of the diagonals equal the sum of the products of opposite sides. Choosing the four points to make $AC$ and $BD$ diameters converts this into an addition formula for chords, and choosing $AD$ a diameter converts it into a half-angle recurrence:

$$\operatorname{crd}(\theta/2) = \sqrt{2 - \sqrt{4 - \operatorname{crd}^2(\theta)}}.$$

Both were verified by direct computation for this article. For the four points at $0°$, $40°$, $110°$ and $200°$ on the unit circle, the two sides of Ptolemy's identity agree to all twenty-five printed digits,

$$AC \cdot BD = AB \cdot CD + BC \cdot AD = 3.226829136446394975286794,$$

and the half-angle recurrence, started from the hexagon's exact chord $1$, walks down the table exactly:

```text
Ptolemy's recurrence from crd(60 deg) = 1
step 1 -> crd(30 deg) = 0.5176380902050415247    (exact half-angle check: equal)
step 2 -> crd(15 deg) = 0.2610523844401031831    (equal)
step 3 -> crd(7.5 deg) = 0.13080625846028613363  (equal)
```

Ptolemy took the same staircase and tabulated chords for a radius of 60 sexagesimal parts at half-degree steps, interpolating between the constructible values. The arithmetic is what makes the table historically extraordinary: every value is a **computed** square root or a rational interpolation, and the whole construction contains no physical measurement of a circle anywhere.

## The Golden Chords: Where φ Enters Without Being Invited

The pentagon is where the golden ratio walks into the table on its own. Since $\varphi = 2\cos 36°$, the decagon chord is exactly $1/\varphi$, and the pentagon chord is exactly $\sqrt{3-\varphi} = 1.175570504584946$, whose square is the exact algebraic number $1.381966011250105$. Written as identities in the code block this site uses for its house relations:

```text
phi            = 2 cos(36 deg) = 1.61803398874989484820
crd(36 deg)    = 2 sin(18 deg) = 1/phi  = 0.61803398874989484820
crd(72 deg)    = 2 sin(36 deg) = sqrt(3 - phi) = 1.17557050458494625825
circumference of an inscribed decagon (r = 1) = 10 sin(18 deg) = 3.09016994374947
```

That last line deserves a second look, because it is the whole tension of this article in one number: the inscribed decagon's perimeter divided by the diameter is $10\sin 18° = 3.0901699437$, a computable lower bound, and it is nowhere near either candidate for the constant — it is a bad estimate, not a wrong one. Bounds improve only by adding sides.[^1]

[^1]: The regular pentagon and decagon are also where Golden Pi's own definition can be written in chord language: the Golden Pi half-turn is $\hat\pi/2 = 2/\sqrt\varphi = 1.572302755514847\ldots$, an angle at which the analytic chord function gives $\operatorname{crd}(\hat\pi/2) = 2\sin(0.7861513778) = 1.415277\ldots$ rather than the $\sqrt{2}$ of a true quarter turn. The geometry of a quarter turn is fixed at $\sqrt2$; what moves is the analytic sine's evaluation at the golden coordinate.

## Where the Circle Constant Actually Enters: the Arc, Not the Chord

The constant enters the problem at exactly one point: converting a chord into an arc, or a polygon into a circle. A regular $n$-gon inscribed in a circle of diameter $1$ has perimeter $n\sin(\pi/n)$; circumscribed, $n\tan(\pi/n)$. Both sequences converge to the circle constant as a computed limit — the exhaustion argument Archimedes made rigorous in the third century BCE, and which the [dedicated article on that method](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) develops in full.

| $n$ | inscribed $n\sin(\pi/n)$ | circumscribed $n\tan(\pi/n)$ | bracket width |
|---|---|---|---|
| $12$ | $3.10582854123025$ | $3.21539030917347$ | $3.5276\%$ |
| $96$ | $3.14103195089051$ | $3.14271459964537$ | $0.0536\%$ |
| $192$ | $3.14145247228546$ | $3.14187304997982$ | $0.0134\%$ |

At $n = 96$ — the polygon Archimedes stopped at — the bracket is already narrower than the $0.0959022\%$ that separates Golden Pi from the analytic constant. Doubling again to $n = 192$ makes it seven times narrower still. These are pure rational comparisons of computable lengths: no ruler, no circle to trace, no measurement.

## What Ptolemy's Number Actually Proves

Ptolemy's own value for the constant, recorded in sexagesimal as $3;8;30$, is

$$\pi_{\text{Ptolemy}} = 3 + \frac{8}{60} + \frac{30}{3600} = \frac{377}{120} = 3.1416666666666666\ldots$$

The errors are worth stating precisely, because they are the sharpest test in this series so far:

| Compared with | Absolute error | Relative error |
|---|---|---|
| analytic constant $3.141592653589793$ | $+0.0000740131$ | $+0.0023559\%$ |
| Golden Pi $\hat\pi = 3.144605511029693$ | $-0.0029388444$ | $-0.0934567\%$ |

Ptolemy's computed rational is **40.7 times closer** to the analytic constant than to Golden Pi. That is not a measurement claim and it is not a rounding artifact: the value was computed, the comparison is arithmetic, and the same arithmetic applies to Archimedes' bracket $223/71 < \pi < 22/7$, i.e. $3.1408451$ to $3.1428571$, which was established by inscribing and circumscribing polygons and comparing rational lengths. Golden Pi lies **above** the upper end of that bracket by $0.0556299\%$, and above the $96$-gon circumscribed bound $3.1427145996$ by $0.0601681\%$. The Indian tradition's value $62832/20000 = 3.1416$ (Āryabhaṭīya, c. 500 CE) misses the analytic constant by only $+0.0002338\%$ — twenty-four ten-thousandths of a percent, four hundred and ten times smaller than the golden gap.

This is the honest ledger entry, and the site records it rather than hiding it. The exhaustion inequality is not a physical measurement; it is an inequality between rational numbers derived from constructible lengths. Any position that identifies the circle constant with a specific number whose value lies outside such a bracket has to explain why the bracket — which contains no measurement, no error bar, and no empirical input — does not apply. The [comparative formula audit](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) keeps this ledger deliberately separate from the geometric one.

## Under Golden Pi: What the Relabel Does to the Chords

Now perform the substitution the site performs everywhere else: replace the half-turn $\pi$ with $\hat\pi = 4/\sqrt\varphi$, keeping angles as the same fractions of the turn.

| Quantity | Analytic coordinate | Golden coordinate | Relative shift |
|---|---|---|---|
| decagon chord, $\operatorname{crd}(2\pi/10)$ | $0.618033988749895$ | $0.618607040230972$ | $+0.0927217\%$ |
| pentagon chord, $\operatorname{crd}(2\pi/5)$ | $1.175570504584946$ | $1.176545272253798$ | $+0.0829187\%$ |
| $\varphi$ as $2\cos(\pi/5)$ | $1.618033988749895$ | $1.617325329776677$ | $-0.0437975\%$ |
| inscribed $96$-gon bound | $3.14103195089051$ | $3.14404319366143$ | $+0.0958103\%$ |
| circumscribed $96$-gon bound | $3.14271459964537$ | $3.14573068902112$ | $+0.0959022\%$ |

The shifts are of the same order as the constant's own gap — the decagon chord moves by $0.0927\%$, not by some tiny fraction of it — because a chord is a function of the angle coordinate, and moving the coordinate moves the chord. That matters, because the *true* decagon chord is a geometric fact: a ten-sided figure inscribed in a circle has side $1/\varphi$ because of the pentagon, not because of any constant. Under the golden coordinate, the closed-form evaluation $\operatorname{crd}(\hat\pi/5) = 0.6186070402$ disagrees with the geometric truth $1/\varphi = 0.6180339887$ by $0.0927217\%$. The same happens to $\varphi = 2\cos(\pi/5)$, which becomes $1.6173253298$ — off the golden ratio by $0.0437975\%$, an ugly result for a construction whose entire premise is the golden ratio.

The bracket behaves symmetrically, and this is the most instructive table in the article:

| $n$ | golden inscribed $n\sin(\hat\pi/n)$ | golden circumscribed $n\tan(\hat\pi/n)$ | contains $\hat\pi$? | contains $\pi$? |
|---|---|---|---|---|
| $12$ | $3.10873864012094$ | $3.21861969736819$ | yes | no |
| $96$ | $3.14404319366143$ | $3.14573068902112$ | yes | no |
| $192$ | $3.14446492603107$ | $3.14488671497061$ | yes | no |

Feed $\hat\pi$ into the algorithm and the brackets close on $\hat\pi$; feed $\pi$ in and they close on $\pi$; feed in the *geometric* polygon lengths and the brackets close on $3.14159\ldots$, because those lengths are the chords tabulated at the top of this article — fixed, $\pi$-free, and identical under either coordinate convention. The exhaustion algorithm does not arbitrate between the two labels. The chord lengths do, and they are the one part of this problem no relabeling can move.

## The Honest Ledger

Sorting the pieces mechanically:

- **Fixed by geometry, no constant involved:** every chord length, the decagon side $1/\varphi$, the pentagon side $\sqrt{3-\varphi}$, the supplementary identity, Ptolemy's theorem and its recurrence, and the sexagesimal table that follows from them.
- **Relabels cleanly, as a coordinate choice:** the arc measure of a given turn, the half-turn $\hat\pi$, the full turn $2\hat\pi = 8/\sqrt\varphi = 6.289211022$, and every closed form written in terms of the half-turn — including $\hat\pi/4 = 1/\sqrt\varphi = 0.7861513778$ and $\hat\pi/2 = 2/\sqrt\varphi = 1.5723027555$.
- **Does not relabel, in the site's own published ledger:** identities whose numerical content is a completed computation rather than a geometry. Ptolemy's $377/120$ and Archimedes' bracket belong here, alongside the [Basel sum](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) and Parseval's energy identity — the closed forms that pin the constant to $3.14159265358979323846\ldots$ and refuse the substitution.

The reason the chord table matters is that it isolates the disagreement to one sentence. The geometric chord of a given central angle is a fixed length; the analytic function $2\sin(\theta/2)$ returns a slightly different number when evaluated at the golden coordinate; and the exhaustion bounds, built only from the fixed lengths, land on the analytic constant. Golden Pi's defense — that the relabel is a coherent, complete re-coordinatisation of the turn, algebraic of degree four, the root of $x^4 + 16x^2 - 256 = 0$, as developed in the [constructibility article](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) — is unaffected by this. What is affected is the claim that the circle's own chord geometry prefers the golden value. It does not: a computed, measurement-free inequality that predates the Christian era already places the circle constant in $(3.1408451,\ 3.1428571)$.

```text
Summary of the ledger (all values computed here to 40+ digits)
analytic constant     pi  = 3.14159265358979323846264338327950288
golden constant    hatpi  = 4/sqrt(phi) = 3.14460551102969314427823434337
relative gap              = 0.0959022%
Ptolemy 377/120 = 3;8;30  = 3.14166666666666666666666666666666667
  vs pi                   = +0.0023559%      (40.71x closer to pi than to hatpi)
  vs hatpi                = -0.0934567%
Archimedes bracket        = [223/71, 22/7] = [3.1408450704, 3.1428571429]
  hatpi above 22/7        = +0.0556299%      (outside, by a computed inequality)
96-gon circumscribed      = 3.14271459964537
  hatpi above it          = +0.0601681%      (outside)
fixed chords: crd(36 deg)=1/phi, crd(60 deg)=1, crd(72 deg)=sqrt(3-phi), crd(90 deg)=sqrt(2)
```

## Ptolemy's Table in Practice

For completeness, the values at a fifth-of-a-turn cadence, all computed as $2\sin(\theta/2)$ on the unit circle — the same numbers Ptolemy tabulated pre-scaled to a radius of 60:

| Angle | Chord | Angle | Chord |
|---|---|---|---|
| $12°$ | $0.209056926535307$ | $72°$ | $1.175570504584946$ |
| $24°$ | $0.415823381635519$ | $90°$ | $1.414213562373095$ |
| $36°$ | $0.618033988749895$ | $120°$ | $1.732050807568877$ |
| $48°$ | $0.813473286151600$ | $180°$ | $2.000000000000000$ |
| $60°$ | $1.000000000000000$ | | |

Nothing in that table is measured, and nothing in it changes under a relabel of the angle coordinate — which is exactly why it has survived eighteen centuries as the most durable computational device in the history of the circle.

## Further Reading

- [Archimedes' Exhaustion and Golden Pi](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — the polygon bracket in full, and what it does to the golden substitution.
- [The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the same staircase carried to high $n$, where the pentagon lets $\varphi$ into the algorithm.
- [Viète's Formula: The First Infinite Product](/blog/posts/2026-08-30-vieta-formula-infinite-product-nested-radicals-golden-pi/) — the chord-doubling idea turned into an infinite product of nested radicals.
- [The Constructible Circle Constant](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) — why $4/\sqrt\varphi$ is algebraic of degree four and what that buys the golden position.
- [The Basel Problem](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the archetype of a completed arithmetic limit that no geometric relabel can re-express.
