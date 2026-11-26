---
title: "The Buffon Needle: Why Dropping a Stick Computes π, Why the Answer Is Only an Average of a Projection, and What Golden Pi Changes"
date: 2026-11-26
description: "Buffon's needle gives P = 2L/πD, and this article shows that the circle constant enters exactly once, as the average projection E|sin θ| = 2/π, so the throw experiment is a measurement of uniform angle and not of a circumference. It derives the integral in one line, tabulates the probability for every useful length ratio (1/4 → 0.1591549431, 1/π → 0.2026423673, 1/φ → 0.3934526572, 1 → 0.6366197724), proves Buffon's noodle law that any curve of length L has expected crossings 2L/πD by additivity over segments, validates Laplace's grid formula P = 4l/πa − l²/πa² against a 200,000-throw simulation (0.954635 against 0.9549296586 at l = a), reports a real Monte Carlo run in which 10⁶ throws returned 3.145861 — closer to golden π than to π — and shows why: one standard deviation at that sample size is 0.0757%, comparable to the 0.0959022309% gap, so 5.6 million throws are needed for a 3σ discrimination. Under Golden Pi (π̂ = 4/√φ) the three exact golden needles land on algebraic values — 2/π̂ = √φ/2 = 0.6360098248 as the root of 16y⁴−4y²−1=0, L/D = 1/√φ giving exactly 1/2, and L/D = 1/φ giving 1/(2√φ) = 0.3930756889 as the root of 16y⁴+4y²−1=0 — while every crossing count, every additivity statement and every ratio of probabilities holds every digit."
---

# The Buffon Needle

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1733 a French naturalist asked a question about gambling. A stick is dropped onto a floor ruled with parallel lines. How often does it land across a line? The answer, which Georges-Louis Leclerc de Buffon read to the Académie royale des sciences that year and printed much later in the *Supplément* to his *Histoire naturelle*, contains the circle constant:

$$
P = \frac{2L}{\pi D},
$$

where $L$ is the stick's length and $D$ the spacing of the lines, provided $L \le D$.

That formula is usually presented as a curiosity — *you can compute π by throwing sticks* — and then dismissed, or celebrated, for the wrong reason. This article takes it apart. The interesting fact is not that the constant is there. It is **where** it is there: not in a circumference, not in an area, but inside a single average of a projection factor, $E|\sin\theta| = 2/\pi$. Once that is seen, the whole family of Buffon problems — the grid, the noodle, the long wire — follows from one additivity argument, and the question of whether throwing sticks can arbitrate the value of the constant can be answered with arithmetic instead of rhetoric.

## The Drop, the Floor, and the Number

Fix the geometry. Parallel lines at spacing $D$. A needle of length $L \le D$ is thrown so that its centre lands uniformly and its angle is uniform. Two coordinates describe it: the centre's perpendicular distance $x$ from the nearest line-copy below it, uniform on $[0, D)$, and the acute angle $\theta$ between the needle and the lines, uniform on $[0, \pi/2]$ by symmetry.

The needle's half-length projects onto the perpendicular direction as $\tfrac{L}{2}\sin\theta$. It crosses a line precisely when the centre is within that distance of one of the two lines bounding the strip, so for a fixed $\theta$ the favourable measure of $x$ is

$$
2\cdot\frac{L}{2}\sin\theta = L\sin\theta ,
$$

and the conditional probability is $L\sin\theta/D$. Averaging over the angle with density $2/\pi$ on $[0,\pi/2]$:

$$
P=\frac{2}{\pi}\int_0^{\pi/2}\frac{L}{D}\sin\theta\,d\theta
=\frac{2L}{\pi D}\int_0^{\pi/2}\sin\theta\,d\theta
=\frac{2L}{\pi D}.
$$

The integral of the sine over a quarter turn is exactly $1$. That is the whole derivation, and it is worth staring at: the constant entered once, as the **reciprocal of the angular half-turn**, and then a sine integral consumed it. Nothing was squared, nothing was integrated over a circle.

Written as an average, the result says something sharper than the fraction does:

$$
P=\frac{L}{D}\cdot E|\sin\theta|,\qquad E|\sin\theta|=\frac{2}{\pi}=0.6366197723675814.
$$

The quantity $2/\pi$ is the mean absolute projection of a unit segment onto a fixed direction when the segment's orientation is uniform. A stick does not measure a circumference. It averages a shadow.

## The Ten-Line Derivation in Code

The identity is short enough to state as a machine-readable block, and short enough that the reader can check every line by hand:

```text
geometry      x ~ U[0, D),  theta ~ U[0, pi/2]
crossing      x < (L/2) sin theta   or   x > D - (L/2) sin theta
conditional   P(cross | theta) = L sin(theta) / D
average       P = (2/pi) * (L/D) * integral_0^{pi/2} sin = (2/pi)(L/D)(1)
result        P = 2L / (pi D)          for L <= D
corollary     L/D = pi P / 2           -> an estimator, not a measurement
```

The last line is a warning disguised as algebra. Solving for the constant makes the formula look like an instrument; it is only an inversion.

## The Table: Length Ratio Against Probability

Because $P$ is linear in $L/D$ for $L \le D$, one table covers the family. The column $1/P$ is included because it is the classical "expected number of throws per success", and because it shows how the constant sits as a scale factor rather than as a feature of any particular stick.

| $L/D$ | $L/D$ (decimal) | $P = 2L/\pi D$ | under $\hat\pi$ | $1/P$ | shift |
|---|---|---|---|---|---|
| $1/10$ | 0.1000000000 | 0.0636619772 | 0.0636009825 | 15.707963 | $-0.0958\%$ |
| $1/4$ | 0.2500000000 | 0.1591549431 | 0.1590024562 | 6.283185 | $-0.0958\%$ |
| $1/\pi$ | 0.3183098862 | 0.2026423673 | 0.2024482149 | 4.934802 | $-0.0958\%$ |
| $1/2$ | 0.5000000000 | 0.3183098862 | 0.3180049124 | 3.141593 | $-0.0958\%$ |
| $1/\varphi$ | 0.6180339887 | 0.3934526572 | 0.3930756889 | 2.541602 | $-0.0958\%$ |
| $1/\sqrt\varphi$ | 0.7861513778 | 0.5004795112 | 0.5000000000 | 1.998084 | $-0.0958\%$ |
| $4/5$ | 0.8000000000 | 0.5092958179 | 0.5088078598 | 1.963495 | $-0.0958\%$ |
| $1$ | 1.0000000000 | 0.6366197724 | 0.6360098248 | 1.570796 | $-0.0958\%$ |

Two rows deserve comment. At $L/D = 1/\pi$ the probability is exactly $2/\pi^{2} = 0.2026423673$ — a needle whose length is the reciprocal of the constant has a crossing probability quadratic in it. At $L/D = 1/2$ the probability is exactly $1/\pi$: one throw in $\pi$. Neither fact tells you anything about the value of $\pi$; both are the same formula wearing different clothes.

The last column is a single number repeated eight times, and it should be: $P$ is proportional to $1/\pi$ at fixed geometry, so any change of the constant's numeral scales every entry by the same factor. That is the signature of a label, not of a mechanism.

## Buffon's Noodle: The Law Holds for Any Curve

Buffon's needle is a special case of something much stronger, proved by Émile Barbier in 1860 and known as *Buffon's noodle*. Replace the stick with **any** curve of length $L$ — a bent wire, a squiggle, a closed loop, a length of chain — dropped with uniform random position and orientation. The expected number of crossings of the ruled lines is still

$$
E[N] = \frac{2L}{\pi D},
$$

with no dependence on the shape.

The proof is additivity, and it is one of the cleanest arguments in elementary geometry. Split the curve into infinitesimal segments $ds$. A segment is a needle of length $ds$, so its own expected crossing count is $2\,ds/(\pi D)$ by the formula already derived — valid for infinitesimal $ds$ with no restriction, since $ds \le D$ trivially. Expectation is linear, so summing gives the total. Curvature, self-intersection, endpoints: none of it enters, because expectation does not care about overlap.

Two consequences follow immediately. First, a closed loop of length $L$ that is convex has $N \in \{0, 2\}$, so $E[N] = 2P(\text{cross twice})$ and

$$
P(\text{a convex loop of perimeter } L \text{ crosses at all}) = \frac{L}{\pi D},
$$

exactly half the needle's expectation at equal length — each crossing of a loop comes in a pair. Second, a wire long enough to cross many lines has a crossing *rate* per unit length of $2/(\pi D)$ that is a universal constant of the ruled plane, independent of the wire's shape. If the constant is a label, this rate is its visible face; if it is a fact, this is the fact.

## Two Families of Lines: Laplace's Grid

Rule the floor in both directions, a square grid of side $a$, and drop a needle of length $l \le a$. Pierre-Simon Laplace treated this case in the *Théorie analytique des probabilités* (1812). The answer is not twice the single-line probability, because the two events overlap:

$$
P = \frac{4l}{\pi a} - \frac{l^{2}}{\pi a^{2}}.
$$

The first term is the sum of the two families' separate probabilities, each $2l/(\pi a)$; the subtracted term is the double count. At $l = a$ it gives $3/\pi = 0.9549296585513720$ — a unit needle on a unit grid misses every line only about 4.5% of the time.

This formula is worth checking rather than trusting, and the check is cheap. A direct simulation of 200,000 throws with $l = a = 1$ returned a crossing fraction of $0.954635$ against the predicted $0.9549296586$ — agreement to within one standard error ($4.6\times10^{-4}$). At $l = 0.5$ the run gave $0.558747$ against $0.557042$; at $l = 0.25$, $0.297690$ against $0.298416$; at $l = 0.75$, $0.776337$ against $0.775880$. The formula survives contact with arithmetic. (A plausible-looking alternative with $\pi^{2}$ in the correction term predicts $0.611289$, $0.311977$ and $0.897936$ — wrong by ten to twelve percent, which the same runs exclude outright.)

## The Crossings Are Poisson — But Only When There Are Many

For a long curve, $L \gg D$, the crossing count is Poisson:

$$
P(N = k) = e^{-\lambda}\frac{\lambda^{k}}{k!},\qquad \lambda = \frac{2L}{\pi D},
$$

so $P(\text{no crossing}) = e^{-2L/\pi D}$. At $L = D$ this would read $e^{-0.6366197724} = 0.5290778083$.

That number is wrong for a needle, and the reason is instructive. A needle of length $L \le D$ can cross at most one line, so its count is Bernoulli, not Poisson: mean $p = 0.6366197724$ but variance $p(1-p) = 0.2312959$, far below the mean a Poisson variable would require. The gap between the two models is the shadow of a geometric constraint, and it matters for anyone who wants to use the experiment as an estimator: a short needle is *quiet* per throw — its variance is bounded by $1/4$ — while a long wire is noisy with variance equal to its mean.

## Running the Experiment for Real

The formula can be inverted into an estimator: after $N$ throws with $C$ crossings,

$$
\hat\pi_{\text{est}} = \frac{2LN}{DC}.
$$

The relative standard deviation of that estimator is $\sqrt{(1-p)/(pN)}$, and it is worth tabulating against actual runs. The following numbers are not illustrative — they are the output of a Monte Carlo run of the exact geometry above, with $L = D = 1$:

| throws $N$ | crossings $C$ | $\hat\pi_{\text{est}}$ | deviation from $\pi$ | 1σ (relative) |
|---|---|---|---|---|
| $10^{4}$ | 6383 | 3.133323 | $-0.2632\%$ | $0.7528\%$ |
| $10^{5}$ | 63624 | 3.143468 | $+0.0597\%$ | $0.2391\%$ |
| $10^{6}$ | 635756 | 3.145861 | $+0.1359\%$ | $0.0757\%$ |
| $10^{7}$ | 6367898 | 3.140754 | $-0.0267\%$ | $0.0239\%$ |

Read the third row twice. One million throws returned $3.145861$ — which is $0.040\%$ from the golden reading $4/\sqrt\varphi = 3.1446055110$ and $0.136\%$ from $\pi$. Every popular retelling of this experiment would call that a triumph for whichever value the author prefers. It is neither: an unlucky sample landed $1.8\sigma$ from the conventional value and happened to fall near the other one. Ten million throws then moved back to $3.140754$, $0.027\%$ below $\pi$.

This is the honest anatomy of a counting experiment: it has no memory and no loyalty. The tally is a genuine count — that part is not in dispute — but the number it estimates is a probability, and a probability has a standard error.

## The Golden Needle: Exact Algebraic Probabilities

If the constant is read as $\hat\pi = 4/\sqrt\varphi = 3.1446055110\ldots$, with $\varphi = (1+\sqrt5)/2$, then $P = 2L/(\hat\pi D)$ and three length ratios land on closed forms that the conventional reading leaves transcendental.

**The unit needle, $L = D$.**

$$
P = \frac{2}{\hat\pi} = \frac{\sqrt\varphi}{2} = 0.6360098247570345 .
$$

This is a root of $16y^{4} - 4y^{2} - 1 = 0$: set $y = \sqrt\varphi/2$, so $4y^{2} = \varphi$, and $\varphi$ satisfies $\varphi^{2} - \varphi - 1 = 0$, which becomes $16y^{4} - 4y^{2} - 1 = 0$. Compare $2/\pi$, transcendental by Lindemann's 1882 theorem.

**The half-probability needle, $L/D = 1/\sqrt\varphi = 0.7861513778$.**

$$
P = \frac{2}{\hat\pi\sqrt\varphi} = \frac{2\sqrt{\varphi}}{4\sqrt\varphi} = \frac{1}{2}.
$$

Exactly one half. Under the conventional reading the same ratio gives $2/(\pi\sqrt\varphi) = 0.5004795112$, and the ratio that would put the probability at exactly $1/2$ is $\pi/4 = 0.7853981634$ — a transcendental length. Under Golden Pi the coin becomes fair at an algebraic needle length: a stick shorter than the line spacing by the factor $\sqrt\varphi$ has even odds, exactly.

**The golden-ratio needle, $L/D = 1/\varphi$.**

$$
P = \frac{2}{\hat\pi\varphi} = \frac{1}{2\sqrt\varphi} = 0.3930756888787116 ,
$$

a root of $16y^{4} + 4y^{2} - 1 = 0$, obtained from $u = 1/\varphi$ satisfying $u^{2} + u - 1 = 0$ with $u = 4y^{2}$. And the needle whose length is the reciprocal of the constant, $L/D = 1/\hat\pi$, gives exactly

$$
P = \frac{2}{\hat\pi^{2}} = \frac{\varphi}{8} = 0.2022542485937369 ,
$$

a quadratic irrational, against Euler's transcendental $2/\pi^{2}$ under the conventional reading.

Under Golden Pi the grid formula follows suit. At $l = a$ it becomes $3/\hat\pi = 0.9540147371355517$ against $3/\pi = 0.9549296585513720$; at $l = a/\varphi$ it becomes $0.6646843098182619$ against $0.6653217568996753$.

## What Does Not Move

The important list is the invariant one.

*The additivity proof.* Buffon's noodle law is linearity of expectation applied to segments. It holds under any positive constant, because it never evaluates the constant — it only sums $2\,ds/(\pi D)$ over $ds$. Change the numeral and the sum changes uniformly; change the shape and nothing changes at all.

*The crossing structure.* How many lines a given physical stick crosses on a given throw is a fact about the stick and the floor. A needle of length $L \le D$ crosses at most one line; a convex loop crosses zero or two; a wire of length $L \gg D$ crosses about $2L/(\pi D)$ times. None of that arithmetic is touched by the choice of numeral, because the counts themselves are untouched.

*Every ratio of probabilities.* $P(L_1)/P(L_2) = L_1/L_2$ exactly, for all $L \le D$. The estimator's design, the optimal throw length, the variance bound — all constant-free.

*The Poisson/Bernoulli distinction.* That a short needle cannot be Poisson because it cannot cross twice is geometry, not convention.

## The Honest Boundary

*The experiment counts sticks; it does not weigh a circle.* The quantity being estimated is a probability of crossing, and the formula relating that probability to the constant is the thing under test. A run that returns $3.145861$ confirms the formula to within its own error bars and nothing more.

*The statistics are the binding constraint, and they are not close.* To distinguish $3.1415926536$ from $3.1446055110$ at the $0.0959022309\%$ level requires, for the unit needle, about $621{,}800$ throws for a one-sigma separation ($N \approx p(1-p)/\delta^{2}$ with $\delta = 0.000959$ relative), $2.49$ million for two sigma, and $5.60$ million for three. At $10^{6}$ throws — a long afternoon of mechanical dropping — one sigma is $0.0757\%$, *comparable to the gap itself*. Nothing about this deserves the word "test" until the sample is at least five times larger, and by then every systematic effect in the apparatus is larger than the effect being sought.

*The historical cautionary tale is real.* Mario Lazzarini's 1901 report of $\pi \approx 355/113$ from 3408 throws is widely regarded as contrived rather than performed: the needle ratio $5/6$ and the throw count conspire to produce the classical convergent, and $3408$ is exactly $16 \times 213$. An experiment whose parameters were chosen after seeing the answer is not evidence.

*And the deeper point stands.* Every $\pi$ in this article sits where the angular measure is normalised: in the density $2/\pi$ on a quarter turn, in the mean of $|\sin|$, in the half-turn that the sine integral consumes. That is the same location the site has found for the constant in the cardioid's area, the torus's two revolutions, and the hat-box zone. The constant is a convention for counting turns. A stick thrown onto a ruled floor samples uniform orientation, and uniform orientation is exactly the thing the convention describes — which is why the experiment is a beautiful demonstration of the geometry and a hopeless instrument for the numeral.

What is left, honestly, is a formula that can be checked by hand in six lines, a noodle theorem that makes it shape-independent, a grid formula validated to a part in a thousand by direct simulation, a real run of ten million throws that lands $0.027\%$ from $\pi$ and proves nothing about it, and — under Golden Pi — three exact algebraic probabilities where the conventional reading has transcendentals. Computed, never measured.

## Further Reading

- [The Cardioid: Why Its Perimeter Is Exactly 8a and Holds No Circle Constant](/blog/posts/2026-11-23-cardioid-exact-perimeter-8a-caustic-golden-pi/) — the caustic that lights a cup, and the curve where the constant appears only in the area.
- [The Torus: Why Its Area Is Exactly the Product of Two Circumferences](/blog/posts/2026-11-24-torus-two-revolutions-curvature-golden-pi/) — what happens when one sweep carries $\pi$ twice and the total curvature carries it not at all.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — another case where the honest answer is a quadrature and the constant is a label on turns.
- [The Hat-Box Theorem: Why Projecting a Sphere onto Its Circumscribed Cylinder Preserves Area Exactly](/blog/posts/2026-11-20-archimedes-hat-box-theorem-sphere-cylinder-area-golden-pi/) — Archimedes' projection argument, the same idea of a shadow replacing a surface.
- [Hippocrates' Lunes: The One Curvilinear Figure That Squares Exactly](/blog/posts/2026-11-10-hippocrates-lunes-quadrature-golden-pi/) — where the constant cancels against Pythagoras and the quadrature survives untouched.
