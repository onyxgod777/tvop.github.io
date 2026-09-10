---
title: "Buffon's Needle: How a Tossed Needle Estimates the Circle Constant, and What Golden Pi Changes"
date: 2026-09-10
description: "Buffon's needle turns a needle tossed onto a ruled floor into an estimate of the circle constant: the geometric probability a needle of length L crosses a line spaced d apart is P = 2L/(πd), an exact ratio that is computed by a two-dimensional integral over the rectangle of positions and angles — never measured. In 1901 Mario Lazzarini reported 3408 tosses with a 5/6-length needle yielding 1808 crossings and the six-digit value 355/113, a result statisticians have long treated as a stopping-rule artifact. A 2,000,000-toss simulation of the same geometry returns 3.139486, still inside the noise. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the same integral relabels the probability to √φ/2 = 0.636009824757… and the expected crossing count changes by only 1.7 crossings out of 3408 — against a binomial spread of ±29 — so no tossing experiment at any realistic scale can arbitrate between the two labels, which differ by the recurring 0.0959%."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Buffon's Needle: How a Tossed Needle Estimates the Circle Constant, and What Golden Pi Changes

Drop a needle on a floor of parallel planks and there is a definite chance it lands across a crack. That chance is a number. And that number is not arbitrary: it is built out of the circle constant, exactly, with nothing left over. The needle problem — posed by Georges-Louis Leclerc, Comte de Buffon, in the eighteenth century and published in his *Essai d'arithmétique morale* (1777) — is the oldest example in mathematics of a physical procedure whose outcome encodes a dimensionless constant, and it is the historical ancestor of what we now call Monte Carlo methods.

It is also the perfect test case for the honest boundary this blog keeps returning to. Every other route we have taken to the circle constant — Madhava's series, Vieta's product, the Gaussian integral, the residues of $1/(z^4+1)$ — computes the constant exactly, from pure arithmetic, in a process that touches no apparatus. Buffon's needle is different. Its formula is computed, but its *procedure* is a genuine physical experiment, with real needles, real planks, and real noise. That makes it the one place where the question "could an experiment settle the value of the circle constant?" is not rhetorical. This article works through the geometry, the numbers, the famous 1901 claim of Mario Lazzarini, and then asks what Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$, honestly does to all of it.

## The Problem, Stated Precisely

A floor is ruled with parallel lines, evenly spaced a distance $d$ apart. A needle of length $L$ is thrown at random. What is the probability that the needle crosses one of the lines?

"At random" needs to be made exact before anything can be computed. A needle's position on this floor is fully described by two numbers:

- $x$, the distance from the needle's midpoint to the nearest line, which lies in the interval $0 \le x \le d/2$;
- $\theta$, the acute angle the needle makes with the lines, which lies in the interval $0 \le \theta \le \pi/2$.

Every possible throw is therefore a single point in a rectangle of area $(d/2)\cdot(\pi/2)$. A uniform random throw is a point chosen uniformly from that rectangle. This is the whole content of the phrase "at random" — no physics, no dynamics, no needle mass. The problem is now a *measure* problem: what fraction of the rectangle corresponds to crossings?

## Where the Circle Constant Enters: The $(x, \theta)$ Rectangle

Fix the angle $\theta$. The needle's two halves each project a vertical reach of $(L/2)\sin\theta$ from the midpoint, so the needle crosses the nearest line precisely when

$$x \le \frac{L}{2}\sin\theta .$$

For a given $\theta$, the set of winning $x$ values is an interval of length $(L/2)\sin\theta$, out of a total $x$-range of length $d/2$. The probability of a crossing at that fixed angle is therefore

$$P(\theta) = \frac{(L/2)\sin\theta}{d/2} = \frac{L}{d}\sin\theta ,$$

and the total probability is the average of this over all angles, weighted uniformly:

$$P = \frac{2}{\pi}\int_0^{\pi/2} \frac{L}{d}\sin\theta \, d\theta = \frac{2L}{\pi d}\Big[-\cos\theta\Big]_0^{\pi/2} = \frac{2L}{\pi d}\big(0 + 1\big) = \frac{2L}{\pi d}.$$

That last step is where the circle constant enters, and it is worth naming what just happened. The integral $\int_0^{\pi/2}\sin\theta\,d\theta = 1$ is a *computed* limit of a summing process; it is exact, it has no apparatus, and it produces a rational number. The circle constant appears only as the normalization of the angle average, $2/\pi$, because the angles were counted uniformly over a quarter turn — the factor that converts "an average over angles" into "an average over a fraction of a turn." This is the same structural fact we saw in the Gaussian integral and the Cauchy–Lorentz density: the constant rides along as a *conversion label* between a linear and an angular measure, and once the average is taken it is a fixed exact number.

Two regimes are worth separating, because they are different formulas:

| regime | formula for $P$ | notes |
|---|---|---|
| short needle, $L \le d$ | $P = \dfrac{2L}{\pi d}$ | the classic case; no overlap corrections |
| long needle, $L > d$ | $P = \dfrac{2L}{\pi d}\left(1 - \sqrt{1 - \dfrac{d^2}{L^2}}\right) + \dfrac{2}{\pi}\arcsin\dfrac{d}{L}$ | crossings can happen more than once per throw |

The arithmetic of the whole model is short enough to write down completely:

```text
P = (2/pi) * (L/d)                 [short needle, L <= d]
pi_estimate = (2 * L * n) / (k * d)

n = number of tosses
k = number of tosses that crossed a line
```

Invert the first line and you have the estimator in the second: count crossings, divide, and the circle constant falls out. That inversion is the entire experimental method.

## Running the Numbers

Set the needle length equal to the line spacing, $L = d$, the cleanest case. Then the geometric probability is

$$P = \frac{2}{\pi} = 0.6366197723675814\ldots$$

and a run of $n$ tosses crossed a line $k$ times gives the estimate $2n/k$. Our earlier Monte Carlo run of $N = 2{,}000{,}000$ tosses returned $k = 1{,}274{,}094$ crossings, giving

$$\frac{2N}{k} = \frac{4\,000\,000}{1\,274\,094} = 3.139486\ldots$$

a result that sits $0.0021$ below $3.14159\ldots$ and $0.0051$ below $3.14461\ldots$. One honest run of two million tosses does not settle anything, which is exactly the lesson of the next two sections.

## Lazzarini's 3408 Tosses

In 1901 the Italian mathematician Mario Lazzarini reported a Buffon needle experiment with needles of length $L = 5/6$ of the plank spacing: 3408 tosses, 1808 crossings, and the resulting estimate

$$\frac{2L n}{k d} = \frac{2\cdot(5/6)\cdot 3408}{1808} = \frac{5680}{1808} = 3.14159292\ldots = \frac{355}{113},$$

accurate to six decimal places. It is the most famous needle experiment in the literature, and it is also the most instructive cautionary tale in the literature, for two reasons that both belong on the honest side of the ledger.

First, the arithmetic of the choice: with $L = 5d/6$ the true probability is $P = 10/(6\pi) = 0.5305164769729845\ldots$, so the *expected* number of crossings in 3408 tosses is $3408 \cdot P = 1808.0002$ — essentially exactly the figure reported. The needle length that makes the target rational $355/113$ fall out of a round number of tosses was chosen in advance, and $355/113$ was already the most famous approximation of the circle constant, known since Zu Chongzhi in the fifth century. Statisticians have long noted that the experimental design was reverse-engineered toward a known answer: the count 1808 is the *only* count in the neighborhood that produces $355/113$ to that many digits, and its probability under honest tossing is about 1.4%. A Dutch science journalist, Hans van Maanen, has argued that Lazzarini's article — aimed at schoolteachers — was not meant to be read as a serious metrological claim at all, since the apparatus he described cannot work as described.

Second, and more important for our purposes: even taken at face value, the run is nowhere near precise enough to say anything about a gap of one part in a thousand. The binomial spread of the crossing count in that experiment is

$$\sigma_k = \sqrt{n P (1-P)} = \sqrt{3408 \cdot 0.5305165 \cdot 0.4694835} = 29.13\ \text{crossings}.$$

Against that spread of $\pm 29$ crossings, the entire question of the constant's label moves the expected count by about 1.7. The experiment's own noise is seventeen times larger than the effect under discussion. This is the general shape of the situation, and it is why the famous "six-digit" needle result was never really a measurement of anything: it was a lucky landing inside a wide distribution, on a target chosen in advance.

## How Much Noise Does a Toss Cost?

The estimator's relative error falls only as $1/\sqrt{n}$, which is the harsh arithmetic of every sampling method:

| tosses $n$ | $\sigma_k$ (crossings, $L=d$) | relative error in the estimate | absolute error in $\hat\pi$ |
|---|---|---|---|
| $10^3$ | 15.2 | 2.389% | 0.0751 |
| $10^4$ | 4.81 | 0.756% | 0.0237 |
| $10^5$ | 1.52 | 0.239% | 0.00751 |
| $10^6$ | 0.481 | 0.0756% | 0.00237 |
| $10^7$ | 0.152 | 0.0239% | 0.000751 |
| $10^8$ | 0.048 | 0.00756% | 0.000237 |

Read the fourth row against the headline number of this blog. A million tosses buy a relative precision of about 0.0756%. The gap between the standard circle constant and Golden Pi is 0.0959%. To reach even a *one-standard-deviation* discrimination between the two labels in this geometry one needs

$$n = \frac{1-P}{P\,\delta^2} = \frac{0.3633802276324186}{0.6366197723675814 \times (0.0009590223087825513)^2} \approx 620{,}617\ \text{tosses},$$

and a conventional three-sigma margin pushes that to roughly $5.6$ million tosses — with $L = d$. Using Lazzarini's shorter needle, where $P$ is closer to $1/2$ and therefore noisier, the figure rises to about $964{,}044$ tosses for one sigma. In practice the real obstacles dwarf even this: a physical needle has thickness, the planks have edges, the lines have width, the tosses are never perfectly uniform, and the needle is never perfectly straight. Every one of those systematics is larger than the $0.0959\%$ effect the experiment would be asked to detect.

## What Golden Pi Changes

Golden Pi $\hat\pi = 4/\sqrt\varphi = 3.144605511029693\ldots$ is an exact algebraic number built from the golden ratio, coherent as the circle constant of a constructed analytic system on this site. Installed in the same integral, nothing about the derivation changes — but every quantity that carries the constant's size moves by the recurring relative gap:

| quantity | standard $\pi$ | Golden $\hat\pi$ | relative gap |
|---|---|---|---|
| probability, $L=d$ | $2/\pi = 0.6366197723675814$ | $2/\hat\pi = \sqrt\varphi/2 = 0.6360098247570345$ | 0.095810% |
| crossings per $10^6$ tosses | 636 619.77 | 636 009.82 | 609.95 crossings |
| probability, $L=5d/6$ | $10/(6\pi) = 0.5305164770$ | $10/(6\hat\pi) = 0.5300081873$ | 0.095810% |
| expected crossings in Lazzarini's 3408 tosses | 1808.000 | 1806.268 | 1.73 crossings |
| crossings per $10^6$ tosses, $L=5d/6$ | 530 516.48 | 530 008.19 | 508.29 crossings |
| one turn, $2\pi$ | 6.283185307179586 | $2\hat\pi = 8/\sqrt\varphi = 6.289211022059386$ | 0.095902% |

The constant enters to the first power here, so the gap appears at full strength and unsoftened — no square root halves it, as it did in the Fresnel integral or the gamma reflection formula. At one million tosses with $L=d$, the two labels predict crossing counts of 636 619.77 against 636 009.82: a separation of 610 crossings, against a standard deviation of 481. That is a 1.27-sigma effect — real in the arithmetic, and unreachable in practice.

## Estimate, Not Measurement

This blog maintains a strict distinction, and the needle problem is where it earns its keep. A series or an integral *computes* its limit; the limit is a fixed arithmetic fact. A physical experiment that reads a genuine measurand — a length, a frequency, a ratio of forces — *measures* it. Buffon's needle is neither of those things, and calling it a measurement of the circle constant would be a category error.

What the needle experiment does is sample a *geometric probability*. The probability $P = 2L/(\pi d)$ is a fact of pure geometry: the area fraction of a rectangle in the $(x,\theta)$ plane, computed above by an integral. Tossing needles samples that fraction, and inverting the formula converts the sampled fraction into an estimate of the constant. The estimand — 1808 crossings in 3408 tosses, or 1 274 094 in two million — is a *count*, and a count is an integer, not a measurement of a transcendental quantity. What has been measured, if anything, is the flatness of the planks and the uniformity of one's tossing.

That also explains why the needle route does not arbitrate: it converges, in the limit of infinite tosses, to the constant embedded in the computed geometric probability. If you accept the geometry — uniform planks, uniform angles, a straight needle — then the number it pins is $3.14159\ldots$, and the golden-π relabel changes the estimator's expectation by one part in a thousand while the estimator's own noise at any achievable $n$ is larger than that. The label of a dimensionless constant is not something an apparatus can read, because every apparatus we build to test it is calibrated in terms of one of the two labels already. This is the same conclusion the cycloid and the pendulum forced on us: dimensionless, scale-invariant ratios are precisely the quantities that physical measurement cannot resolve.

## The Honest Bottom Line

Buffon's needle is the oldest Monte Carlo method in mathematics, and it is genuinely beautiful: throw a needle at a ruled floor and the probability of a crossing is $P = 2L/(\pi d)$, an exact geometric ratio computed by integrating $\sin\theta$ over a quarter turn. That derivation touches no apparatus, and the constant it delivers is the analytic $3.141592653589793\ldots$

The experiment, by contrast, is noisy. Lazzarini's celebrated 1901 result — 3408 tosses, 1808 crossings, $355/113$ — was a design aimed at a known answer, and its own binomial spread of $\pm 29$ crossings dwarfs the 1.7-crossing shift that the entire question of the constant's label produces. A million honest tosses buy 0.0756% precision, less than the 0.0959% that separates Golden Pi ( $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$ ) from the standard constant; one sigma of discrimination needs about 620 617 tosses for $L=d$ and about 964 044 for Lazzarini's needle, before any systematic error is counted.

So: Golden Pi relabels the same integral. It turns $2/\pi = 0.6366197723675814$ into $\sqrt\varphi/2 = 0.6360098247570345$, cuts the expected crossing count in a Lazzarini-sized experiment by 1.73, and moves the predicted count per million tosses from 636 619.77 to 636 009.82 — all at the recurring 0.0959%, undiluted because the constant enters to the first power. What it cannot do is make that difference visible on a floor. The needles are honest; the arithmetic is exact; the noise is in charge.

## Further Reading

- [**Pólya's Random Walk: How Counting the Returns of a Staggering Drunkard on a Plane Lattice Computes the Circle Constant**](/blog/posts/2026-09-07-random-walk-return-plane-lattice-computes-circle-constant-golden-pi/) — the same statistical texture, one dimension up: probability densities in which the constant appears as a coefficient.
- [**The Cauchy–Lorentz Distribution: How 1/(1+x²) Computes the Circle Constant**](/blog/posts/2026-08-24-cauchy-lorentz-distribution-integrates-pi-golden-pi/) — where the constant enters as a normalizing label that probability forces to balance.
- [**The Gaussian Integral: How the Bell Curve Computes √π**](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the square root that halves the gap, contrasted with the full-strength gap of the needle problem.
- [**The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured**](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the companion case where an experiment's error bar swamps the label difference.
- [**Rolling Circles and the Cycloid: Where the Circle Constant Vanishes**](/blog/posts/2026-08-14-cycloid-rolling-circles-golden-pi/) — the standing theme: dimensionless, scale-invariant ratios keep the two labels beyond experimental arbitration.
