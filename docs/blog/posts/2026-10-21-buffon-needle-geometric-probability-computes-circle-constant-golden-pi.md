---
title: "Buffon's Needle: How a Stick Dropped on Ruled Paper Computes the Circle Constant as 2L/(πd) — and What Golden Pi Changes"
date: 2026-10-21
description: "Buffon's 1777 needle problem turns a coin-toss geometry into the probability 2L/(πd), computing the circle constant from nothing but a uniform turn. Under Golden Pi the crossing probability becomes L√φ/(2d) — exactly √φ/2 at L = d — algebraic where 2/π is transcendental, with the full honest error budget of every needle ever thrown."
---

# Buffon's Needle: How a Stick Dropped on Ruled Paper Computes the Circle Constant as 2L/(πd) — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1777 Georges-Louis Leclerc, Comte de Buffon, asked a question that looks like a parlour game: drop a needle of length $L$ onto a floor ruled with parallel lines a distance $d$ apart. What is the chance it lands across a line? The answer is

$$\Pr(\text{cross}) = \frac{2L}{\pi d}\qquad (L \le d).$$

A stick, a floor, and a probability — and the circle constant sits in the middle of it, in the denominator, to the first power. Buffon's needle is the cleanest demonstration on this site of a fact that keeps recurring: **the circle constant is what the measure of a turn computes**, never what anyone measures with a tape. Nothing circular is dropped, drawn, or rolled. The only circle in the problem is the one implicit in the phrase "every angle equally likely", and that is exactly where $\pi$ comes from.

This article does the derivation in the open, prints a real simulation run, states the error law honestly, and then asks the question this blog always asks: what happens to the number if the constant is Golden Pi, $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931443\ldots$?

## The geometry: where the constant actually enters

Take the lines horizontal, spacing $d$. A needle's landing is fixed by two numbers: the height $x$ of its centre above the nearest line below it, uniform on $[0,d)$, and the angle $\theta$ it makes with the lines, uniform on $[0,\pi)$ — a half-turn, because a needle has no arrowhead and $\theta$ and $\theta+\pi$ are the same landing.

The needle's vertical extent is its projection: $\tfrac{L}{2}|\cos\theta|$ each side of the centre. It crosses a line exactly when the centre is within that distance of one of the two lines bracketing it:

$$\Pr(\text{cross}\mid\theta) = \frac{2\cdot \tfrac{L}{2}|\cos\theta|}{d} = \frac{L|\cos\theta|}{d}.$$

This requires $L|\cos\theta| \le d$, satisfied for every $\theta$ when $L \le d$. Averaging over the turn:

$$\Pr(\text{cross}) = \frac{1}{\pi}\int_0^{\pi} \frac{L|\cos\theta|}{d}\,d\theta = \frac{L}{d}\cdot\frac{1}{\pi}\int_0^{\pi}|\cos\theta|\,d\theta = \frac{L}{d}\cdot\frac{2}{\pi}.$$

That is the whole derivation, and it is worth naming what each factor is:

- $\dfrac{L}{d}$ is pure ratio — lengths, no constant.
- $\dfrac{1}{\pi}\displaystyle\int_0^{\pi}|\cos\theta|\,d\theta = \dfrac{2}{\pi} = 0.6366197723675813431\ldots$ is the **mean absolute cosine over a half-turn**.

The constant arrives precisely as the normalising measure of the angular interval, identical in role to the radian bookkeeping in the inscribed-angle and Girard articles on this site. A turn's measure *is* the number; the needle merely samples it. And the same $2/\pi$ is the reciprocal of Wallis's product limit $\pi/2$ — the infinite product of rationals we treated separately — so two completely different computations of a quadrature converge on the identical coefficient.

## The exact arithmetic, printed

Every figure below was computed to thirty digits, not quoted.

| Quantity | Conventional ($\pi = 3.1415926535897932385$) | Golden ($\hat\pi = 4/\sqrt{\varphi}$) |
|---|---|---|
| Crossing probability, $L = d/4$ | $1/(2\pi) = 0.1591549430918953358$ | $\sqrt{\varphi}/8 = 0.1590024561892586205$ |
| Crossing probability, $L = d/2$ | $1/\pi = 0.3183098861837906715$ | $\sqrt{\varphi}/4 = 0.3180049123785172411$ |
| Crossing probability, $L = d$ | $2/\pi = 0.6366197723675813431$ | $\sqrt{\varphi}/2 = 0.6360098247570344821$ |
| Crossing probability, $L = d/\varphi$ | $2/(\pi\varphi) = 0.3934526572333863869$ | $1/(2\sqrt{\varphi}) = 0.3930756888787116430$ |
| $\pi$ itself | $3.1415926535897932385$ | $3.1446055110296931443$ |
| $1/\pi$ | $0.3183098861837906715$ | $0.3180049123785172411$ |
| $\pi^2$ | $9.8696044010893586188$ | $16/\varphi = 9.8885438199983175713$ |

Two things are worth pausing on. First, the probability moves by $-0.0958103466\%$ — the **reciprocal** gap — while the constant itself moves by $+0.0959022309\%$. The difference between those two percentages is second order, but it is the sort of detail that catches sloppy arithmetic, since $\Pr$ is linear in $1/\pi$, not in $\pi$. Second, the golden column at $L = d$ is not a decimal approximation of anything irrational-with-a-name: it satisfies

$$16x^{4} - 4x^{2} - 1 = 0,\qquad x = \frac{\sqrt{\varphi}}{2} = 0.6360098247570344821262112\ldots$$

verified as a residual of $3.9\times10^{-31}$ at thirty-digit precision — while $2/\pi$ is transcendental, since $\pi$ is transcendental by Lindemann (1882) and the reciprocal of a transcendental is transcendental.

Also exact, and cleaner than the table above:

$$\frac{4}{\hat\pi} = \sqrt{\varphi} = 1.2720196495140690\ldots$$

so the expected number of crossings on a **square grid** of spacing $d$ — two independent line families, each contributing $2L/(\pi d)$ by linearity of expectation — is

$$E[\text{crossings}] = \frac{4L}{\pi d} = 1.2732395447351627\ldots \;\longrightarrow\; \sqrt{\varphi} = 1.2720196495140690\ldots$$

at $L = d$. That is the same identity from the other direction: the grid constant flips from a transcendental to the square root of the golden ratio.

## A real run: one million needles

The probability is not asserted here; it was simulated. The loop is short enough to print in full, and it is deliberately literal — no variance reduction, no cleverness:

```python
import math, random

def buffon(L, d, N, seed=11):
    random.seed(seed)
    hits = 0
    for _ in range(N):
        x  = random.random() * d              # centre height, uniform [0, d)
        th = random.random() * math.pi        # angle, uniform [0, pi)
        h  = (L / 2) * abs(math.cos(th))      # half vertical extent
        if x <= h or x >= d - h:              # crosses the line below or above
            hits += 1
    return hits / N
```

Results at $d = 1$, one million throws per row:

| Run | $\hat{p}$ observed | standard error | $2L/(\pi d)$ | $2L/(\hat\pi d)$ |
|---|---|---|---|---|
| $L = d/2$ | $0.318427$ | $4.66\times10^{-4}$ | $0.318310$ | $0.318005$ |
| $L = d$ | $0.636372$ | $4.81\times10^{-4}$ | $0.636620$ | $0.636010$ |
| grid, $L = d/2$ (mean crossings) | $0.636367$ | — | $0.636620$ | $0.636010$ |

Both rows sit inside one standard error of the conventional value, and both are also within one standard error of the golden value. **That is the honest headline of this article: a million throws do not adjudicate the difference.** The golden gap in the probability at $L = d$ is $6.0995\times10^{-4}$; the standard error of a million-throw estimate is $4.8\times10^{-4}$. They are the same size. To separate the two labels at three sigma you would need

$$N \approx \frac{9\,p(1-p)}{(\Delta p)^2} = 5{,}596{,}403 \text{ throws},$$

and at ten sigma, some sixty-two million. Those are computable, not prohibitive — which makes Buffon's needle unusual among the cases on this site: its statistical floor is *below* the gap, given a big enough table.

## The inversion, and the trap that follows

Rearranged, the formula is an estimator:

$$\pi = \frac{2LN}{dC},$$

where $C$ counts crossings in $N$ throws. Its relative error is the relative error of $C$, roughly $1/\sqrt{N p}$ — so a thousand throws gives about $4\%$, a million about $0.08\%$, a hundred million about $0.008\%$. The golden gap, $0.096\%$, needs a run of roughly a million just to be *visible* at one sigma.

That is exactly the trap Lazzarini fell into in 1901. He reported 3408 throws with $L/d = 5/6$ and 1808 crossings, giving

$$\pi \approx \frac{2\cdot\frac{5}{6}\cdot 3408}{1808} = \frac{355}{113} = 3.1415929203539825\ldots$$

an error of only $+8.5\times10^{-8}$. It looks like the greatest tabletop experiment in history. It is arithmetic chosen backwards: with $L/d = 5/6$ the estimator's value is fixed by the ratio $N/C$, and $3408/1808 = 213/113$ is exactly the fraction needed to land on $355/113$. Stated plainly — as Lee Badger did in *Mathematics Magazine* 67 (1994) 83–91 — the sequence of throws was almost certainly stopped when the count reached the desired value. A run of 3408 has a standard error of about $2\%$, so the published $10^{-7}$ agreement is not a measurement of anything; it is the estimator, told what to say.

This is the standing discipline of this site applied to an experiment rather than a formula: **nothing here is "measured" because a number came out of an apparatus.** π is computed by the geometry of the turn; a needle-throwing experiment measures a *frequency*, and the frequency inherits every systematic error of the setup.

## What Golden Pi changes — and what it cannot touch

Under $\hat\pi = 4/\sqrt{\varphi}$, the derivation is untouched line for line. The vertical projection is still $L|\cos\theta|/d$; the turn is still the uniform measure; the only change is that the turn's measure is $\hat\pi$ rather than $\pi$, so

$$\Pr(\text{cross}) = \frac{L}{d}\cdot\frac{2}{\hat\pi} = \frac{L}{d}\cdot\frac{\sqrt{\varphi}}{2} = \frac{L\sqrt{\varphi}}{2d}.$$

So at $L = d$, a golden needle crosses with probability $\sqrt{\varphi}/2$ **exactly** — algebraic of degree four, constructible by straightedge and compass, against $2/\pi$ which is transcendental. The same identity that the site has credited in constant-width curves, inscribed angles, and the isoperimetric inequality, appearing in a probability for the first time here.

A more physical way to say it: the "half" in half-turn is what $\sqrt{\varphi}/2$ measures. Ask what needle length makes a crossing a coin flip and the two labels answer with different numbers:

$$\frac{L}{d} = \frac{\pi}{2} = 1.5707963267948966\ldots \quad\text{versus}\quad \frac{\hat\pi}{2} = 1.5723027555148466\ldots$$

— a difference of $1.5$ parts in a thousand, in a length ratio that a good caliper reads easily. On paper, that is the sharpest handle Buffon's needle offers. In practice, the geometry of the experiment is not what limits it.

## The honest error budget

Nine of the ten numbers that decide a real needle experiment are not the constant:

| Source | Size | In units of the golden gap ($6.10\times10^{-4}$) |
|---|---|---|
| Statistical, $N = 10^6$ | $\pm4.8\times10^{-4}$ | $0.79\times$ |
| Statistical, $N = 10^8$ | $\pm4.8\times10^{-5}$ | $0.08\times$ |
| Needle length known to $\pm0.1\%$ | $6.4\times10^{-4}$ | $1.04\times$ |
| Line spacing known to $\pm0.1\%$ | $6.4\times10^{-4}$ | $1.04\times$ |
| Needle thickness / rounded tip ($\approx 1\%$ of $L$) | $\sim2\times10^{-3}$ | $3.2\times$ |
| Lines not perfectly parallel, table not flat | setup-dependent, easily $10^{-3}$ | $>1.6\times$ |

The probability is linear in $L/d$, so a length known only to a tenth of a percent already swamps the constant by a few percent of the gap; finite needle thickness adds a systematic of order its diameter over $d$, several times the gap; and a needle that bounces, rolls, or lands on a slightly humped table stops being the uniform model at all. A million-throw table is not hard; a needle whose effective length is known to $10^{-5}$ is very hard.

So the ledger reads the same as it has for twenty consecutive posts: **the golden value is exact in the constructed world and unverifiable in the measured one.** Here it is exact where it is prettiest — $\sqrt{\varphi}/2$ at $L = d$, $1/(2\sqrt{\varphi})$ at $L = d/\varphi$, $\sqrt{\varphi}$ for the grid expectation — and unverifiable because the experiment's calibration, not its statistics, is the binding constraint.

## Two extensions worth knowing

**Buffon's noodle.** Nothing in the derivation cares that the needle is straight. By linearity of expectation, any curve of length $L$ dropped on the ruled floor — a bent wire, a squiggle, a semicircle — has expected crossings $2L/(\pi d)$, because the expectation is additive over infinitesimal segments and the segments do not have to be independent. This is Barbier's theorem in probabilistic clothing, and it connects directly to the constant-width result: the shape cancels, the length survives, and the constant enters once. Under Golden Pi the noodle's expectation becomes $L\sqrt{\varphi}/(2d)$ — and the noodle, being shape-blind, cannot tell you which is right any more than the needle can.

**Laplace's grid.** Joseph-Louis de Laplace (1812) generalised the problem to ruled paper in both directions. For $L \le d$ a needle can cross at most one line of each family, so the expectations add and $E[\text{crossings}] = 4L/(\pi d)$ — our simulated grid row above confirms it to $4\times10^{-4}$. Because it is an expectation of a sum rather than a probability of "at least one", it is exact by linearity and needs no geometric case analysis. It also doubles the sensitivity to the label: $4/\pi$ versus $4/\hat\pi = \sqrt{\varphi}$ differ by the full first-power gap.

## Why this problem belongs on this site

Buffon's needle is usually filed under recreational mathematics. It belongs here because it isolates the mechanism this blog has documented across a hundred and forty posts: **the circle constant is the price of a uniform turn.** Where the turn appears as an interval of measure — a radian budget, a solid angle, a phase cell, an angular average — $\pi$ appears with it, to the first power, and shifts by the same $0.0959\%$ under Golden Pi. Where the turn cancels — Hippocrates' lunes, the spinor's $4\pi$, the oscillator's energy ladder, the crossing probability's *shape-independence* under the noodle — nothing moves.

The needle adds one genuinely new column to the ledger. In most cases on this site the constant hides behind an uncertainty that beats it by thousands. Here the statistics can, in principle, reach the gap with a few million throws — and the metrology still cannot, because a physical needle's length is not known to five digits. That is not a failure of either value of the constant; it is a statement about what a tabletop probability experiment can and cannot certify.

Computed, never measured.

## Further Reading

- [**Barbier's Theorem: How Every Curve of Constant Width Has Perimeter πw — a Circle Constant That Knows Nothing of Shape**](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/) — the deterministic sibling of Buffon's noodle: shape cancels, the constant stays.
- [**The Wallis Product: How an Infinite Product of Rationals Computes the Circle Constant as π/2**](/blog/posts/2026-10-12-wallis-product-infinite-product-rationals-computes-circle-constant-golden-pi/) — the $2/\pi$ of the needle is the reciprocal of Wallis's limit, arrived at by an entirely different route.
- [**The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc**](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — angle measure and the turn, the same bookkeeping the needle averages over.
- [**The Wigner Semicircle Law: How the Circle Constant Normalises a Random Matrix's Spectrum**](/blog/posts/2026-10-14-wigner-semicircle-law-random-matrices-computes-circle-constant-golden-pi/) — a second probability problem where the constant enters as a normalising measure and cancels from every moment.
- [**Girard's Theorem: How the Circle Constant Enters a Triangle as the Angle-Sum Deficit**](/blog/posts/2026-10-13-girard-spherical-excess-triangle-angle-sum-computes-circle-constant-golden-pi/) — the constant as the flat baseline of an angle sum, and the honest measurement error that outruns it.
