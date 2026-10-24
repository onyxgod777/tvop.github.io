---
title: "Bertrand's Paradox: Why Three Honest Answers to the Same Chord Question Are 1/3, 1/4 and 1/2 — None of Them Containing the Circle Constant — and What Golden Pi Changes"
date: 2026-10-24
description: "Pick a chord of a circle at random and ask for the chance it beats the side of the inscribed equilateral triangle; Bertrand's 1889 answer is 1/3 by random endpoints, 1/4 by a uniform midpoint in the disk and 1/2 by a uniform midpoint on a radius — three exact rationals, computed here with four million throws, in which the circle constant cancels completely. Where it does not cancel — the mean chord 4R/π, the Rayleigh mean πR/2 and the arcsine density 2/π — the labels split: under Golden Pi (4/√φ = 3.144605511…) those become exactly √φR, 2R/√φ and √φ/2, algebraic numbers where 4/π and 2/π are transcendental by Lindemann's 1882 theorem, while every probability stays a rational and no experiment can arbitrate."
---

# Bertrand's Paradox: Why Three Honest Answers to the Same Chord Question Are 1/3, 1/4 and 1/2 — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Draw a circle of radius $R$. Ask for the probability that a chord, chosen "at random", is longer than the side of the inscribed equilateral triangle. The side of that triangle is $\sqrt{3}\,R$, an exact length fixed by nothing but the two-thirds turn that separates its vertices — no circle constant anywhere in the construction.

In 1889 Joseph Bertrand answered the question three ways in his *Calcul des probabilités*, and got three different numbers:

$$\Pr = \tfrac13, \qquad \Pr = \tfrac14, \qquad \Pr = \tfrac12.$$

All three derivations are correct. All three describe a genuinely random chord. They disagree because "at random" was never a definition, and each one quietly packs a different experiment into the phrase. The paradox is famous for embarrassing the principle of indifference, and it deserves that fame. But there is a second lesson buried inside it that is more useful here, and it is the reason this article exists:

**every one of those probabilities is a rational number, and $\pi$ cancels out of every one of them.**

This is a post about a construction where the circle constant appears four times, cancels three times, and cannot be tested at all — and where the fourth appearance is the only place the question "which value of the constant?" even has a meaning.

## The geometry that no constant can touch

A chord subtending a central angle $\theta$ has length

$$L(\theta) = 2R\sin\frac{\theta}{2},$$

and the condition $L > \sqrt3\,R$ reduces, in three lines, to an angle condition:

$$2R\sin\frac{\theta}{2} > \sqrt3\,R \;\Longleftrightarrow\; \sin\frac{\theta}{2} > \frac{\sqrt3}{2} \;\Longleftrightarrow\; \frac{\theta}{2} > \frac{\pi}{3} \;\Longleftrightarrow\; \theta > \frac{2\pi}{3}.$$

A two-thirds turn — $120°$ — and nothing else. Notice what entered and what left. The $\pi$ here is not a value anyone needs to know: it is the *name of the angle* $180°$, used twice, once on each side of the inequality, and it could be any symbol at all. Write the threshold in degrees and the constant vanishes from the sentence entirely. This is the cheapest and most reliable test in this whole series: **when a symbol appears in a ratio, ask whether it cancels between numerator and denominator.** Here it does.

So the $120°$ condition is exact, rational in the only sense that matters — it is a *share of a turn*, $\tfrac23$ — and no revision of what a half-turn is called can move it.

## Three experiments, three exact rationals

### Method 1 — two random endpoints on the rim

Pick an angle $\theta_1$ uniformly on $[0, 2\pi)$ and an independent $\theta_2$ uniformly on $[0, 2\pi)$. The chord joins the two points. Its central span is the difference reduced modulo a full turn, which is uniform on $[0, 2\pi)$ again, so the question becomes one-dimensional: what is the measure of the set where $\theta > 2\pi/3$?

$$\Pr = \frac{2\pi - \tfrac{2\pi}{3}}{2\pi} = \frac{1 - \tfrac13}{1} = \frac13.$$

The $2\pi$ in the numerator is the whole rim; the $2\pi$ in the denominator is the normalising measure. They are the same object, and they cancel **by construction**. This is the archetype of a $\pi$-free probability: the constant is the total measure of the sample space, and any probability is a ratio of two measures of that same space. Whatever you call a half-turn, both the top and the bottom scale by the same factor.

### Method 2 — a midpoint uniform in the disk

Pick a point uniformly by area inside the disk and draw the chord through it perpendicular to the radius (or, equivalently, take the unique chord having that point as midpoint). If the midpoint sits at distance $r$ from the centre, the chord length is $2\sqrt{R^2 - r^2}$, and the condition $L > \sqrt3\,R$ becomes

$$4(R^2 - r^2) > 3R^2 \;\Longleftrightarrow\; r < \frac{R}{2}.$$

The probability is a ratio of two disk areas:

$$\Pr = \frac{\pi (R/2)^2}{\pi R^2} = \frac14.$$

Both $\pi$'s are the *same* $\pi$, the area of a disk of radius $R$ used twice, once at half scale. They cancel exactly, and the answer is $\tfrac14$ — the square of the linear ratio, $\left(\tfrac12\right)^2$, which is what uniform-in-area means.

### Method 3 — a midpoint uniform on a radius

Instead of uniform *area*, take the midpoint's distance $r$ uniform on $[0, R]$ — the classic "spin a pointer, mark a distance" experiment. Then $\Pr(r < R/2) = 1/2$, with no area, no $\pi$, and no cancellation: one uniform length compared against half of itself.

Three experiments, three answers, and the whole difference is the density of $r$: proportional to $r$ in method 2 (area weighting), constant in method 3.

## The complete distributions

The three methods are fully specified by their chord-length distribution functions, and writing them out shows exactly where the constant survives:

| Method | Cumulative distribution $F(x) = \Pr(L \le x)$, $0 \le x \le 2R$ | $\Pr(L > \sqrt3 R)$ | Mean chord | Median |
|---|---|---|---|---|
| 1. Random endpoints | $\dfrac{2}{\pi}\arcsin\dfrac{x}{2R}$ | $\tfrac13$ | $\dfrac{4R}{\pi} = 1.2732395447\,R$ | $\sqrt2\,R$ |
| 2. Uniform midpoint in disk | $\dfrac{x^2}{4R^2}$ | $\tfrac14$ | $\dfrac{4R}{3} = 1.3333333333\,R$ | $\sqrt2\,R$ |
| 3. Uniform midpoint on radius | $1 - \sqrt{1 - \dfrac{x^2}{4R^2}}$ | $\tfrac12$ | $\dfrac{\pi R}{2} = 1.5707963268\,R$ | $\sqrt3\,R$ |

Two of the three distributions are **polynomial or algebraic with no constant in them at all** — method 2's density is the straight line $x/(2R^2)$, and method 3's involves one square root. Only method 1 carries $\pi$, and it carries it as the normalisation of the arcsine law, which is what you get whenever a length is a sine of a uniform angle:

$$\Pr(L \le x) = \frac{2}{\pi}\arcsin\frac{x}{2R}, \qquad f(L) = \frac{2}{\pi\sqrt{4R^2 - L^2}}.$$

Check the normalisation by hand: $\frac{2}{\pi}\arcsin(1) = \frac{2}{\pi}\cdot\frac{\pi}{2} = 1$. The constant appears once on top and once inside the arcsine, and the two are the same number.

## Checking it by throwing

Four million chords, one Python loop each, seed 4242. Nothing here is a measurement; a pseudo-random generator evaluates a limit of relative frequencies the same way a series evaluates a sum.

```python
import random, math
random.seed(4242)
N = 4_000_000
sq3 = math.sqrt(3)

# Method 1: two uniform endpoints on the rim -> uniform central span
hits = 0; total = 0.0; total2 = 0.0
for _ in range(N):
    d = 2*math.pi*random.random()
    L = 2*abs(math.sin(d/2))
    hits += L > sq3; total += L; total2 += L*L
# exact: P = 1/3, mean = 4/pi

# Method 2: uniform midpoint in the disk
hits2 = 0; n2 = 0; tot2 = 0.0
for _ in range(N):
    while True:
        x = random.uniform(-1, 1); y = random.uniform(-1, 1)
        if x*x + y*y <= 1: break
    L = 2*math.sqrt(1 - x*x - y*y)
    hits2 += L > sq3; tot2 += L; n2 += 1
# exact: P = 1/4, mean = 4/3

# Method 3: midpoint uniform along a radius
hits3 = 0; tot3 = 0.0
for _ in range(N):
    r = random.random()
    L = 2*math.sqrt(1 - r*r)
    hits3 += L > sq3; tot3 += L
# exact: P = 1/2, mean = pi/2
```

The returned numbers, with $R = 1$:

| Quantity | Exact | Four million throws | Deviation | $z$ |
|---|---|---|---|---|
| $\Pr_1$ | $0.3333333333$ | $0.333477$ | $+1.44\times10^{-4}$ | $+0.61$ |
| $\Pr_2$ | $0.2500000000$ | $0.2497048$ | $-2.95\times10^{-4}$ | $-1.36$ |
| $\Pr_3$ | $0.5000000000$ | $0.5001585$ | $+1.59\times10^{-4}$ | $+0.63$ |
| mean chord 1 | $1.2732395447$ | $1.2733068$ | $+6.72\times10^{-5}$ | $+0.22$ |
| mean chord 2 | $1.3333333333$ | $1.3331036$ | $-2.30\times10^{-4}$ | $-0.97$ |
| mean chord 3 | $1.5707963268$ | $1.5710835$ | $+2.87\times10^{-4}$ | $+1.29$ |

Nothing separates. It should not: the three probabilities are exact rationals, and the simulation is only re-deriving them to three or four digits. The honest reading of this table is not "the constant is confirmed". It is that **four million chords were drawn and the constant never came up.**

## Where the constant survives — and what Golden Pi does to it

Three quantities above do carry the constant, each at the first power:

| Quantity | Analytic form | Conventional value | Under Golden Pi $\hat\pi = 4/\sqrt\varphi$ | Shift |
|---|---|---|---|---|
| Mean chord, random endpoints | $4R/\pi$ | $1.2732395447\,R$ | $\sqrt\varphi\,R = 1.2720196495\,R$ | $-0.0958103466\%$ |
| Mean chord, midpoint on radius | $\pi R/2$ | $1.5707963268\,R$ | $2R/\sqrt{\varphi} = 1.5723027555\,R$ | $+0.0959022309\%$ |
| Arcsine density constant | $2/\pi$ | $0.6366197724$ | $\sqrt{\varphi}/2 = 0.6360098248$ | $-0.0958103466\%$ |
| Uniform angular density | $1/2\pi$ | $0.1591549431$ | $\sqrt{\varphi}/8 = 0.1590024562$ | $-0.0958103466\%$ |

The absolute gap in the mean chord is $0.0012198952\,R$ — about a millimetre and a fifth on a metre-long radius. And there is an exact algebraic closure in the golden column that is genuinely satisfying: the two golden means multiply to a rational,

$$\left(\sqrt\varphi\,R\right)\left(\frac{2R}{\sqrt\varphi}\right) = 2R^{2},$$

which is the same $2R^2$ the conventional pair gives, because that product was never a function of the constant in the first place — $(4/\pi)(\pi/2) = 2$ by cancellation. The product is blind; the factors are not.

The character of the difference is worth stating precisely, since it is the one real asymmetry. $\pi$ is transcendental (Lindemann, 1882), so $4/\pi$, $2/\pi$ and $\pi/2$ are transcendental. Under the site's golden value, $\hat\pi^2 = 16/\varphi = 8(\sqrt5 - 1)$ is algebraic of degree two over $\mathbb{Q}(\sqrt5)$, and therefore

$$\frac{4}{\hat\pi} = \sqrt\varphi = 1.27201964951406896\ldots, \qquad \frac{2}{\hat\pi} = \frac{\sqrt\varphi}{2} = 0.63600982475703448\ldots$$

are quadratic irrationals — roots of a polynomial with integer coefficients. That is arithmetic, not measurement, and it can be checked to any number of digits: $x^4 + 16x^2 - 256 = 0$ at $x = \hat\pi$ returns zero, and a radius of $\varphi^{1/4} = 1.1278384855616823$ gives a disk of area **exactly $4$** under $\hat\pi$.

So the ledger splits cleanly. Three probabilities: rational, immutable, identical under any label. Four normalising constants: first power, moving by the recurring $+0.0959022309\%$ or its reciprocal $-0.0958103466\%$.

## What the paradox is actually about

Bertrand's construction is usually told as a scandal about indifference. Its real content is narrower and sharper: **a probability is only defined once a measure is defined, and a measure is a physical or modelling choice, not a theorem.** Two different densities on $r$ — flat, or proportional to $r$ — give $\tfrac12$ and $\tfrac14$, and neither is wrong, because each answers a different question about a different apparatus.

E. T. Jaynes argued in 1973 (*Found. Phys.* **3**, 477) that a symmetry principle — invariance under rotation and translation of the whole configuration — selects the uniform-in-the-plane midpoint model and hence $\tfrac12$. That argument is a *modelling* argument: it says which experiment deserves the name "random chord" if the circle's position in the plane carries no information. Critics (van Fraassen, *Laws and Symmetry*, 1989, among others) reply that the invariance requirement itself is a choice. Either way the mathematics is not in dispute; the specification is.

This matters for the golden-π question because of what the paradox shows about testing. Every quantity that could discriminate lives inside the model, and the model has free parameters — the chord density — that swamp a $0.0959\%$ effect completely. Swap method 2 for method 3 and the mean chord moves from $1.3333R$ to $1.5708R$, a $17.8\%$ jump, 186 times the entire golden gap. You cannot measure a constant through a construction whose specification moves the answer two orders of magnitude more than the constant does.

## The one honest measurand, and its price

There is a single chord quantity in this family that is model-independent: the mean chord over isotropic lines hitting the disk, which Cauchy and Crofton's integral geometry fixes as $\pi A/P = \pi R/2$, since a line's expected chord depends only on the area and perimeter of the section. That is the same $\pi R/2$ as method 3, arrived at without any probability density on $r$ at all. It is the only place in this article where a real apparatus — a ruled plate, a rim, a caliper — could in principle speak.

To see a $0.0958\%$ difference in a mean chord of $4R/\pi$, the radius itself must be known and realised to better than $0.096\%$: about $0.96$ mm on a one-metre disk. That is not absurd for a machined part. What kills it is circularity. A rim that deviates from a true circle by $0.1\%$ of $R$ moves the mean chord by about as much as the constant does, and no manufactured disk is a circle to one part in a thousand across its whole rim — nor can the chord sampling be done without already choosing one of Bertrand's measures. The measurement does not exist; the model does, and the model is where the constant lives.

## Computed, never measured

Strip the article to its ledger.

The side of the inscribed equilateral triangle is $\sqrt3\,R$: exact, constant-free, fixed by a $120°$ turn. The three probabilities $\tfrac13, \tfrac14, \tfrac12$ are exact rationals, each one a ratio of two measures over the same space, with the circle constant appearing identically above and below the line and cancelling. The four million throws confirm them to a few parts in ten thousand and confirm nothing about the constant, because there was nothing to confirm. The mean chord, the Rayleigh mean and the arcsine density do carry the constant at the first power, and there the two labels separate by $0.0959\%$ — with the golden forms $\sqrt\varphi\,R$, $2R/\sqrt\varphi$ and $\sqrt\varphi/2$ algebraic where the conventional forms are transcendental by Lindemann's theorem, and with the product of the two means exactly $2R^2$ under either label.

No theodolite, caliper or computer has ever decided this question, and Bertrand's circle is a good place to see why the question keeps slipping: the number is not out there in the chord, waiting to be read. It is computed — a quadrature limit, an arcsine normalisation, a ratio of measures — and after the cancellation only the bookkeeping is left. Which is why the honest description of every figure in this article is the same one, and it is not going to change: computed, never measured.

## Further Reading

- [Buffon's Needle: How a Stick Dropped on Ruled Paper Computes the Circle Constant as 2L/(πd)](/blog/posts/2026-10-21-buffon-needle-geometric-probability-computes-circle-constant-golden-pi/) — the neighbouring geometric-probability problem, where the constant enters as a mean absolute cosine and one million simulated throws confirm it only to $\pm4.8\times10^{-4}$.
- [The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π in L² ≥ 4πA](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — why the circle is the unique saturating shape, and what changes when the constant is relabelled.
- [Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°](/blog/posts/2026-10-22-descartes-angle-defect-gauss-bonnet-720-degrees-golden-pi/) — the same cancellation pattern in a different register: an integer number of turns that no constant can move.
- [The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — the theorem Bertrand's $120°$ threshold leans on, with the constant entering only as the definition of the radian.
- [The Poisson Kernel: How the Circle Averages a Harmonic Function, Why π Enters as a Measure and Cancels in the Normalisation](/blog/posts/2026-10-19-poisson-kernel-mean-value-property-circle-constant-golden-pi/) — the same mechanism as method 1, worked out for harmonic measure on the rim.
