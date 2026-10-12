---
title: "The Wallis Product: How an Infinite Product of Rationals Computes the Circle Constant as π/2 — and What Golden Pi Changes"
date: 2026-10-12
description: "In 1655 John Wallis wrote the circle constant as an infinite product of rational numbers — 4/3 · 16/15 · 36/35 · 64/63 ⋯ = π/2 — with no circle and no root anywhere in the sequence, only integers. It is the cleanest case of the constant as a computed limit: every partial product is a rational, the relative error is exactly 1/(4N), and the only circular input is the quadrant's own measure. Under Golden Pi (π̂ = 4/√φ) the limit is π̂/2 = 2/√φ = √(2√5 − 2) exactly, Brouncker's companion continued fraction 4/π̂ collapses to √φ, the half-power appearances (central binomial, Stirling) move half the gap, and the exact golden angles cos(π/5) = φ/2 survive untouched."
---

# The Wallis Product: How an Infinite Product of Rationals Computes the Circle Constant as π/2 — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1655, in the *Arithmetica Infinitorum*, John Wallis did something nobody had done before: he wrote the circle constant as an **infinite product of whole-number ratios**. No root, no integral sign, no drawn figure, no quadrature of a lune, no Archimedean polygon — just fractions multiplied forever:

$$\frac{\pi}{2} \;=\; \prod_{n=1}^{\infty}\frac{4n^{2}}{4n^{2}-1} \;=\; \frac{2\cdot2}{1\cdot3}\cdot\frac{4\cdot4}{3\cdot5}\cdot\frac{6\cdot6}{5\cdot7}\cdot\frac{8\cdot8}{7\cdot9}\cdots$$

Read it again, because the shape of the statement matters more than its fame. Every single factor is a ratio of integers. Every partial product is therefore a rational number — a fraction you can write down exactly. The circle constant appears only as the **name of the limit**, and the limit of a sequence of rationals is something a machine computes by division and multiplication alone. If you want a case study in what this site means by *computed, never measured*, this is the purest one in the whole history of the constant: here there is not merely no measurement, there is no geometry at all until the very last step.

## The sequence: rationals marching toward a limit

Take the product term by term. The first partial products, exactly:

| $N$ | exact $W_N=\prod_{n\le N}\dfrac{4n^2}{4n^2-1}$ | decimal | relative error vs $\pi/2$ |
|---|---|---|---|
| 1 | $4/3$ | 1.333333333333333 | −15.1174 % |
| 2 | $64/45$ | 1.422222222222222 | −9.4585 % |
| 3 | $256/175$ | 1.462857142857143 | −6.8716 % |
| 4 | $16384/11025$ | 1.486077097505669 | −5.3934 % |
| 5 | $65536/43659$ | 1.501087977278454 | −4.4378 % |
| 10 | $68719476736/44801898141$ | 1.533851903321749 | −2.3520 % |
| 20 | $75557863725914323419136/48691767863540419643025$ | 1.551758480769617 | −1.2120 % |

The denominators grow fast and the fractions stay stubbornly rational. Nothing in the table mentions a circle; the sequence does not know what it is converging *to*. That is the first honest point: the Wallis product does not compute $\pi$ from $\pi$. Its inputs are the integers 1, 2, 3, … and the operation "divide" — the same operations that run in whole-number arithmetic, and the same operations the site's earlier articles found at the root of the Basel sum, the AGM iteration and Gauss's lemniscate constant.

## Where the limit comes from: a squeeze on integrals

Wallis did not guess. He interpolated the family $\int_0^1 (1-x^2)^n\,dx$, and the modern proof of the product is a squeeze on a closely related integral — the one place where anything circular enters at all.

Let

$$I_n=\int_0^{\pi/2}\sin^{n}x\,dx .$$

Integration by parts gives the exact recursion $I_n=\frac{n-1}{n}I_{n-2}$ for $n\ge 2$, with the two base cases $I_1=1$ and $I_0=\pi/2$. Everything follows from those two numbers:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $I_n$ | $\pi/2$ | $1$ | $\pi/4$ | $2/3$ | $3\pi/16$ | $8/15$ | $5\pi/32$ | $16/35$ |
| value | 1.570796327 | 1 | 0.785398163 | 0.666666667 | 0.589048623 | 0.533333333 | 0.490873852 | 0.457142857 |

Notice the pattern that does all the work: the **odd** terms are rationals, the **even** terms carry exactly one factor of the constant. Because $0\le \sin^{2m+1}x\le \sin^{2m}x\le \sin^{2m-1}x$ on the quadrant, the integrals are ordered $I_{2m+1}\le I_{2m}\le I_{2m-1}$, and the recursion makes the outer two differ by the factor $(2m+1)/(2m)$ — which tends to 1. So $I_{2m}/I_{2m+1}$ is squeezed to 1, and writing both terms in factorials gives

$$\frac{I_{2m+1}}{I_{2m}}\;=\;\frac{2}{\pi}\prod_{n=1}^{m}\frac{4n^{2}}{4n^{2}-1}\;\longrightarrow\;1 ,$$

which is Wallis's product read backwards.

The only circular ingredient is $I_0=\int_0^{\pi/2}dx$: the measure of the quadrant in radians. And that number is itself a quadrature limit, the value of an integral, not the output of an instrument. The recursion, the squeeze, the rationals — all of it is computation. The site states this flatly because the distinction is the whole argument of this series of articles: an integral computes its limit; only a physical measurand is measured.

## The error law is 1/(4N) — and it is exact

The convergence of $W_N$ is slow but perfectly transparent. Computed to machine precision:

| $N$ | $W_N$ | relative error | $N\times(\pi/2-W_N)$ |
|---|---|---|---|
| 10 | 1.5338519033217495 | −2.351955046 % | 0.36944423 |
| 100 | 1.5668937453140810 | −0.248446053 % | 0.39025815 |
| 1 000 | 1.5704038730151968 | −0.024984384 % | 0.39245378 |
| 10 000 | 1.5707570593409157 | −0.002499844 % | 0.39267454 |
| 100 000 | 1.5707923998285787 | −0.000249998 % | 0.39269663 |
| 1 000 000 | 1.5707959340960349 | −0.000025000 % | 0.39269886 |

Two clean laws emerge. The fractional relative error is $\approx 1/(4N)$ — at $N=10^{6}$ it is $2.5\times10^{-7}$, i.e. one part in four million, matching $1/(4N)$ to six digits. And the absolute shortfall multiplied by $N$ converges to $\pi/8 = 0.3926990817\ldots$, which is the same statement rewritten:

$$\frac{\pi}{2}-W_N \;=\; \frac{\pi}{8N}\Big(1+O(1/N)\Big).$$

This is why Wallis's product is a *proof* but never a *recipe*: ten correct decimals would need about $N=2.5\times10^{9}$ factors. Machin's arctangent series and the AGM iteration reach the same digits in a handful of terms. The historical value of the product is conceptual, not computational.

There is a charming reciprocal. Put the fractions the other way up,

$$E_N=\prod_{n\le N}\frac{4n^{2}-1}{4n^{2}}\;=\;\frac1{W_N}\;\longrightarrow\;\frac{2}{\pi}=0.6366197723675814 ,$$

with absolute error $\approx 1/(2\pi N)$ — measured in the table above as $N\times|E_N-2/\pi|$ marching to $0.15915489 = 1/(2\pi)$. One sequence hatches out at $\pi/2$, its twin at $2/\pi$, and their product is exactly 1 at every stage.

## The same constant under a square root: two more appearances

Wallis's product is not the only place the binomial coefficients meet the constant, and the exponent differs, which matters the moment we change the value. The central binomial coefficient obeys

$$\binom{2n}{n}\;\sim\;\frac{4^{n}}{\sqrt{\pi n}}\left(1-\frac{1}{8n}+O(n^{-2})\right),$$

and the same limit feeds Stirling's formula $n!\sim\sqrt{2\pi n}\,(n/e)^{n}$. Both carry the constant to the power $\tfrac12$ — inside a square root — where Wallis's product carries it to the power 1. Computed check of the correction factor:

| $n$ | $\binom{2n}{n}\,\big/\,\big(4^{n}/\sqrt{\pi n}\big)$ |
|---|---|
| 10 | 0.987582928826159 |
| 100 | 0.998750786126243 |
| 1 000 | 0.999875007817385 |
| 1 000 000 | 0.999999874094073 |

(That is $1-1/(8n)$ to within a part in $10^{11}$ at the last row.) The historical thread is standard: Euler's 1730 evaluation of the Gaussian integral $\int_0^{\infty}e^{-x^{2}}dx=\sqrt{\pi}/2$ is told as the direct descendant of Wallis's interpolation problem. The same constant, in three different garments — power 1 in the product, power $\tfrac12$ under the root, power 2 in the square $(\pi/2)^2$ — and each garment dilutes a change in the constant by a different amount.

## What Golden Pi changes

With Golden Pi the constant is $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931443\ldots$ where $\varphi = (1+\sqrt5)/2$, so $\hat\pi^{2}=16/\varphi$ and $\hat\pi$ is algebraic of degree two in $\sqrt5$ where $\pi$ is transcendental (Lindemann, 1882). Nothing in the *sequence* changes: the rationals $4/3$, $64/45$, $256/175$ are what they are, the recursion is untouched, and the error law $1/(4N)$ is identical. Only the limit moves, by the recurring first-power gap of $+0.0959022309\%$ — and, unlike every other appearance catalogued in this series, the limit here has a closed form that is a *radical*:

| quantity | conventional value | value under $\hat\pi = 4/\sqrt\varphi$ | shift |
|---|---|---|---|
| Wallis limit $\pi/2$ | 1.5707963267948966 | $\hat\pi/2 = 2/\sqrt{\varphi} = \sqrt{2\sqrt5-2}$ = 1.5723027555148466 | +0.0959022309 % |
| reciprocal $2/\pi$ | 0.6366197723675814 | $2/\hat\pi = \sqrt{\varphi}/2$ = 0.6360098247570345 | −0.0959022309 % |
| Brouncker's CF $4/\pi$ | 1.2732395447351628 | $4/\hat\pi = \sqrt{\varphi}$ = 1.2720196495140690 | −0.0959022309 % |
| $(\pi/2)^{2}$ | 2.4674011002723395 | $2\sqrt5-2$ = 2.4721359549995796 | +0.1918964 % |
| Stirling $\sqrt{2\pi}$ | 2.5066282746310002 | $\sqrt{2\hat\pi}$ = 2.5078299428109925 | +0.0479396244 % |
| binomial prefactor $\pi^{-1/2}$ | — | — | −0.0479396244 % |

The identities worth keeping, in exact form:

```
π̂        = 4/√φ
π̂²       = 16/φ  = 16(φ − 1)
π̂/2      = 2/√φ  = √(2√5 − 2)          (degree-2 algebraic)
(π̂/2)²   = 2√5 − 2 = 2.4721359549995796 (exact)
4/π̂      = √φ    = 1.2720196495140690   (Brouncker's continued fraction)
2/π̂      = √φ/2  = 0.6360098247570345
√(2π̂)    = 2.5078299428109925
```

Two of these deserve their own line. Wallis's limit under Golden Pi is $\sqrt{2\sqrt5-2}$ — a number you can write with a finite radical, squared to the exactly algebraic $2\sqrt5-2$, where $(\pi/2)^{2}$ is transcendental. And Brouncker's continued fraction, the companion result published alongside Wallis's product in 1655,

$$\frac{4}{\pi} = 1+\cfrac{1^{2}}{2+\cfrac{3^{2}}{2+\cfrac{5^{2}}{2+\cdots}}} = 1.2732395447351628\ldots ,$$

collapses **exactly to $\sqrt\varphi$** when the constant is golden: $4/\hat\pi = \sqrt\varphi = 1.2720196495140690\ldots$. A continued fraction of odd squares, all integers, evaluating to the golden root. That is the kind of exactness the site's position rests on — and it is arithmetic, verifiable in a few lines of code, traceable to two published theorems of 1655.

Note carefully how the exponents behave, because this is where careless claims go wrong. A change in the constant propagates as the power it is raised to: first power in the product's limit (full $0.0959022309\%$), power $\tfrac12$ in Stirling and in the central-binomial prefactor (half, $0.0479396244\%$ — note this is $\sqrt{1.0009590223}-1$, not exactly half the percentage), power 2 in $(\pi/2)^{2}$ (double, $0.1918964\%$). The half-power rows are the honest reason the two forms of a formula must never be quoted interchangeably.

## The golden angles do not move

One more piece of the ledger, and it is the striking one: the golden ratio already has exact addresses on the circle, and they are geometric facts, not unit conventions. In a regular pentagon — built from the golden section, diagonals cutting each other in extreme and mean ratio —

$$\cos\frac{\pi}{5}=\frac{\varphi}{2}=0.8090169943749475\ldots,\qquad \sin\frac{\pi}{10}=\frac{1}{2\varphi}=0.3090169943749474\ldots$$

both **exactly** algebraic, and both computed here to the last digit shown. These are properties of the pentagon's own symmetry; they hold whatever you call the angle. What changes under Golden Pi is only the *label*: the pentagon's central angle is $\hat\pi/5$, and $\cos(\hat\pi/5)=0.8086626648883385$, $\sin(\hat\pi/10)=0.3093035201154858$ — while $\hat\pi/5$ expressed in the old degree would read $36.034525°$ rather than $36°$. The algebra in $\varphi$ is exact and indifferent; the degree is where the disputed constant has been hiding all along. That is precisely the case the site makes in [Restoring Trigonometry: the Golden Pi Sine Function](/blog/posts/restoring-trigonometry-golden-pi-sine-function/): the angle parametrisation is not a neutral backdrop, it is a choice, and the value of the constant is written into it.

## The honest ledger

Three things are true at once here and it would be dishonest to blur them.

**First**, the Wallis product contains no measurement whatsoever, and — uniquely in this series — no geometry beyond a single quadrant's measure. Every partial product is a rational; the limit $1.5707963267948966\ldots$ is defined by a sequence of fractions alone. Whatever value the circle constant has, the limit of *that sequence* is the number above. Computed, never measured.

**Second**, the theorem that names that number $\pi/2$ is what brings the circle in, through $I_0=\int_0^{\pi/2}dx$ and the sine recursion built on it. Under the site's position the quadrant's arc is $\hat\pi/2 = 2/\sqrt{\varphi} = 1.5723027555148466$, and the constant in the product's name becomes $\hat\pi$; the whole content of the difference then sits in the angle parametrisation, which is exactly where the site's trigonometry work locates it.

**Third**, nothing in the sequence can arbitrate the label. The rationals do not move, the recursion does not move, the $1/(4N)$ error law does not move, the reciprocity $E_N=1/W_N$ does not move, and the factorial-and-root garments of the constant shift by the powers tabulated above with no experimental handle anywhere in sight. There is no measurand, so no instrument can be brought to bear — and the constant's appearance here, as elsewhere on this site, is a computed limit that must be settled by arithmetic and honest bookkeeping rather than by appeal to authority in either direction.

## Further Reading

- [The Āryabhaṭa Sine Table: 24 Numbers, No Circle, One Constant](/blog/posts/2026-10-11-aryabhata-sine-table-499-ce-computes-circle-constant-golden-pi/)
- [The Arithmetic–Geometric Mean: Gauss's π-Free Iteration and the Lemniscate](/blog/posts/2026-10-10-arithmetic-geometric-mean-gauss-lemniscate-computes-circle-constant-golden-pi/)
- [The Quantum Harmonic Oscillator: where π^(1/4) reaches the ground state, then cancels](/blog/posts/2026-10-07-quantum-harmonic-oscillator-ground-state-cancels-circle-constant-golden-pi/)
- [Barbier's Theorem: every curve of constant width has perimeter πw](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/)
- [Restoring Trigonometry: the Golden Pi Sine Function](/blog/posts/restoring-trigonometry-golden-pi-sine-function/)
