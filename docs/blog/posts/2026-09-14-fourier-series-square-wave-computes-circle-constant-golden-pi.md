---
title: "The Fourier Series: How a Square Wave Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-09-14
description: "Fourier's theorem writes any periodic signal as a sum of sines whose period carries the circle constant, so the ideal square wave's fundamental amplitude is 4/π = 1.2732395447 — exactly √φ = 1.2720196495 under Golden Pi (π̂ = 4/√φ = 3.144605511…). The harmonic series still converges to the waveform by a computed limit no relabel can move, Parseval's energy identity refutes the substitution outright (π̂²/8 = 2/φ = 1.2360679775 against the fixed sum 1.2337005501, a 0.1919167% mismatch), and the Gibbs ring at 8.948987% of the jump is computed from Si(π), never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Fourier Series: How a Square Wave Computes the Circle Constant, and What Golden Pi Changes

Every article in this series has run into the same wall, and the wall has always been in the same place. A series evaluates to its limit; an integral converges to a value; a solid angle sums a sphere. Nowhere does a ruler touch the circle constant. Fourier analysis is the most useful branch of mathematics ever built on that fact — and it is also, unexpectedly, the branch that puts the constant in the least geometric place of all.

<div class="gp-live" markdown>
<div class="gp-live__tag">🔬 Live graph · Laws of appearance</div>
<button class="gp-live__facade" type="button" data-embed="https://www.desmos.com/calculator/qbzqmljdx3?embed" data-label="The circle squeeze - A(n), B(n) and the golden chain" aria-label="Open the interactive Desmos graph: The circle squeeze - A(n), B(n) and the golden chain">
<img src="/img/desmos/qbzqmljdx3.png" alt="The circle squeeze - A(n), B(n) and the golden chain" width="970" height="633" loading="lazy" decoding="async">
<span class="gp-live__play">▶&nbsp; Open the interactive graph</span>
</button>
<p class="gp-live__note"><strong>Regular polygons inscribed and circumscribed, side count doubling, against the golden-rooted pentagon chain.</strong> <em>The Goblet of the Truth keeps two bodies of law apart — the laws and recommendations of the primal power (Creation), and the <strong>laws of appearance (nature)</strong> (Ch&nbsp;2 §342), the register governing how a thing manifests and behaves. Geometry answers to that second register, so nothing here asks to be taken on authority: drag the slider, change a value, and the figure answers for itself (Ch&nbsp;22 §35: <em>“the fluidal-powers are truthful effects of natural laws”</em>).</em></p>
</div>

In a Fourier expansion the circle constant is not the shape of anything. It is the **unit of the axis**: the conversion between a period counted in seconds and an angle counted in radians. That relocation turns out to be the most important thing to understand about what Golden Pi ($\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$) can and cannot do, because it separates the parts of a signal that are computed by the mathematics from the parts that are fixed by the waveform.

## The Series: A Square Wave Written in Sines

Joseph Fourier's *Théorie analytique de la chaleur* (1822) proposed something scandalous for its time: that *any* periodic function, however jagged, can be rebuilt as a sum of pure sines and cosines. Peter Gustav Lejeune Dirichlet supplied the convergence conditions in 1829, and the ideal square wave is the standard example. Take the odd function that equals $+1$ for $0 < x < \pi$ and $-1$ for $-\pi < x < 0$, repeating with period $2\pi$. Its Fourier series is

$$f(x) = \frac{4}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \frac{\sin 7x}{7} + \cdots\right),$$

or, in one line,

$$\boxed{\ f(x) = \sum_{\substack{n=1\\ n\ \text{odd}}}^{\infty} \frac{4}{n\pi}\sin(nx)\ }$$

Read the boxed line carefully, because the circle constant appears exactly once per coefficient, in the denominator of the normalisation $4/\pi$. Nothing about a square wave is round. The constant is there because $x$ is an angle: the waveform's argument advances by $2\pi$ per cycle, and that $2\pi$ is a choice of unit — the full turn expressed in radians.

At $x = 0$ the waveform jumps from $-1$ to $+1$, and Dirichlet's theorem says the series converges to the average of the two sides — zero, which is precisely what the odd sines give. The value of the reconstructed waveform is a property of the waveform. The number inside the coefficient is a property of the *coordinate*, and that distinction is the whole article.

## Where the Circle Constant Enters — as a Period, Not a Shape

Write the same series in time. A square wave of frequency $f$ and amplitude $V$ is $v(t) = V\, f(2\pi f t)$, and the fundamental component is

$$v_1(t) = \frac{4V}{\pi}\sin(2\pi f t).$$

The measured quantities here are honest ones: a frequency counter measures a period of one millisecond, and a voltmeter measures an amplitude in volts. Neither is the circle constant. What the constant does is convert: the angular frequency is $\omega = 2\pi f$, the full turn of the phasor, and at $f = 1\ \text{kHz}$ that is

$$\omega = 2\pi(1000) = 6283.185307\ \text{rad/s}.$$

Under Golden Pi the same waveform has the same period and the same amplitude — both are measurements of the signal, not of the coordinate — but the conversion factor becomes $\omega = 2\hat\pi f$:

$$2\hat\pi = \frac{8}{\sqrt\varphi} = 6.289211022, \qquad \omega = 6289.211022\ \text{rad/s},$$

a shift of $+0.0959022\%$ on every phasor in every textbook on the subject. This is the same arithmetic the [fine-structure constant article](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) performed on $\hbar$ and the Bohr radius, and it is worth noting at the outset that no measurement of a physical signal adjudicates it: the signal has one period, and the axis label that describes it can be rescaled without touching the signal.

## The Fundamental Is 4/π — and Under Golden Pi It Is Exactly √φ

The coefficients of the ideal square wave are the cleanest place to see what the relabel does, because each one is a closed algebraic expression. The $n$-th odd harmonic has amplitude $4/(n\pi)$. Under Golden Pi that amplitude is

$$\frac{4}{n\hat\pi} = \frac{4}{n \cdot 4/\sqrt\varphi} = \frac{\sqrt\varphi}{n},$$

so the entire harmonic ladder is rescaled by the cube-free, degree-two algebraic number $\sqrt\varphi = 1.272019649514069$. The fundamental $n=1$ becomes exactly $\sqrt\varphi$ — the same $\sqrt\varphi$ that defines the constant itself, since $\hat\pi\sqrt\varphi = 4$ is the identity from which the whole site's construction begins.

| Harmonic | Conventional π: $4/(n\pi)$ | Golden π: $\sqrt\varphi/n$ | Relative shift |
|---|---|---|---|
| $n=1$ | $1.2732395447$ | $1.2720196495$ | $-0.0958103\%$ |
| $n=3$ | $0.4244131816$ | $0.4240065498$ | $-0.0958103\%$ |
| $n=5$ | $0.2546479089$ | $0.2544039299$ | $-0.0958103\%$ |
| $n=7$ | $0.1818913635$ | $0.1817170928$ | $-0.0958103\%$ |
| $n=9$ | $0.1414710605$ | $0.1413355166$ | $-0.0958103\%$ |

Note the direction of the shift: because $\sqrt\varphi = 1.2720196495 < 4/\pi = 1.2732395447$, every harmonic amplitude under Golden Pi is *smaller* by the same $0.0958103\%$. That is the reciprocal-side of the $0.0959022\%$ gap — the constant is larger, so its reciprocal $\sqrt\varphi/4 = 0.3180049124$ is smaller — and the small difference between the two percentages ($0.0959022\%$ on the constant, $0.0958103\%$ on its reciprocal) is the second-order term, $(0.0959\%)^2 \approx 9.2\times10^{-7}$ relative, that a first-principles expansion predicts.

At the waveform's peak the reconstructed value matters too. Truncating the series after 1, 5, 21 and 101 odd terms at $x = \pi/2$ gives $1.2732395$, $1.1034743$, $1.0288781$ and $1.0062408$ — climbing to the amplitude 1 as $1/(N\pi)$-style tails die off. Those numbers are rationals added together: the series *computes* its limit, and the limit is the amplitude of the waveform, a fact about the waveform, not about the constant. The constant only sets how many terms are named "one volt".

## Parseval's Theorem: The Energy Identity and the Honest Refutation

The decisive test is Parseval's theorem, the harmonic accounting of energy. For a $2\pi$-periodic $f$,

$$\frac{1}{\pi}\int_{-\pi}^{\pi} |f(x)|^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty}\left(a_n^2 + b_n^2\right).$$

For the unit square wave the left side is exactly $2$ — the mean square of a $\pm1$ signal, a number no one disputes — and the right side gives

$$2 = \sum_{n\ \text{odd}} \left(\frac{4}{n\pi}\right)^2 = \frac{16}{\pi^2}\sum_{n\ \text{odd}}\frac{1}{n^2} \quad\Longrightarrow\quad \sum_{n\ \text{odd}}\frac{1}{n^2} = \frac{\pi^2}{8}.$$

The odd reciprocal-square sum is a fixed arithmetic constant — computed to $1.2337005501361697$, the same value Euler's machinery produces in the [Basel problem](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) and its odd-partner identity. Now substitute Golden Pi into the *formula* and read off what it demands:

$$\frac{\hat\pi^2}{8} = \frac{16/\varphi}{8} = \frac{2}{\varphi} = 1.2360679774997896.$$

The relabeled formula does not equal the sum. It is too large by $0.1919167\%$ — exactly twice the gap, because $\hat\pi$ enters squared. And the direction is not a coincidence: relabelling the constant changes the value that Parseval's identity *computes*, while the sum of reciprocal odd squares is a statement about integers that no relabeling touches.

```text
Parseval for the unit square wave
left side  : 2  (exact, fixed by the waveform)
right side : (16/pi^2) * sum_{n odd} 1/n^2
sum_{n odd} 1/n^2        = 1.2337005501361697   (fixed arithmetic constant)
pi^2 / 8                 = 1.2337005501361697   -- identity holds
hatpi^2 / 8 = 2/phi      = 1.2360679774997896   -- identity fails by +0.1919167%
```

This is the honest boundary of the Fourier argument, stated without softening. Golden Pi does not "fix" Parseval's theorem; it *breaks* it, in exactly the way it breaks the Basel identity and every other closed form whose numerical content is not a pure geometry but a completed arithmetic limit. The site's [comparative formula audit](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) keeps the two ledgers separate for precisely this reason: geometric definitions relabel cleanly, computed sums do not.

## What Does Relabel Cleanly, and What Does Not

The harmonic bookkeeping lets the two ledgers be sorted mechanically.

| Quantity | Conventional π | Under Golden Pi ($\hat\pi$) | Status |
|---|---|---|---|
| Full turn / period of $\sin$ | $2\pi = 6.283185307179586$ | $2\hat\pi = 8/\sqrt\varphi = 6.289211022$ | relabels, $+0.0959022\%$ |
| $\omega = 2\pi f$ at 1 kHz | $6283.185307\ \text{rad/s}$ | $6289.211022\ \text{rad/s}$ | relabels, $+0.0959022\%$ |
| Fundamental of a $\pm1$ square wave | $4/\pi = 1.2732395447$ | $\sqrt\varphi = 1.2720196495$ | relabels, $-0.0958103\%$ |
| Fraction of energy in the fundamental | $8/\pi^2 = 0.8105694691$ | $\varphi/2 = 0.8090169944$ | relabels, $-0.1915289\%$ |
| Fraction of energy in harmonics 1–9 | $0.9596047868$ | $0.9577668663$ | relabels, $-0.1915289\%$ |
| Total harmonic distortion | $\sqrt{\pi^2/8 - 1} = 0.4834258476$ | $1/\varphi^{3/2} = 0.4858682718$ | relabels, $+0.5052324\%$ |
| Energy outside the fundamental | $\pi^2/8 - 1 = 0.2337005501$ | $1/\varphi^3 = 0.2360679775$ | $\hat\pi$ breaks the fixed sum |
| Value of the waveform at a jump | $0$ | $0$ | fixed |
| RMS of a $\pm1$ square wave | $1$ | $1$ | fixed |
| Only odd harmonics present | true | true | fixed |
| Frequency of the $n$-th harmonic | $nf$ | $nf$ | fixed |

Look at the last four rows. The waveform's RMS, its zero-crossing value, its odd-harmonic structure and the physical frequency of every line in its spectrum are all untouched — they are facts about the signal. Everything that carries the *axis* moves, and it moves with the gap: the turn by $0.0959022\%$, the amplitude ladder by the reciprocal $0.0958103\%$, and anything quadratic in the constant by twice that.

The total harmonic distortion deserves a second look, because THD is a number engineers quote in percent on real datasheets. For an ideal square wave,

$$\text{THD} = \sqrt{\frac{\pi^2}{8} - 1} = 0.4834258476 = 48.3426\%,$$

and under Golden Pi it is $\sqrt{2/\varphi - 1} = \varphi^{-3/2} = 0.4858682718 = 48.5868\%$ — a shift of $0.5052324\%$, five times larger than the constant's own gap, since THD varies as the square root of a quantity already carrying the gap squared. It is a striking reminder that nonlinear functions of the constant amplify it, and it is also a reminder that an engineer who *measured* 48.34% on a real inverter would be measuring the inverter: finite rise time, ringing, and load-dependent overshoot move a practical square wave's THD by whole percentage points.

## The Sawtooth at π̂/2: Where the Relabel Is Exact

One case shows the relabel operating without any error at all, and it is instructive to see why. For $|x| < \pi$ the sawtooth series is

$$\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx) = \frac{x}{2}.$$

This is a statement about a *real variable* $x$, not about the symbol $\pi$: the series converges to half its argument, wherever the argument happens to be. So evaluate it at the Golden Pi half-turn, $x = \hat\pi/2 = 2/\sqrt\varphi = 1.5723027555$, which lies comfortably inside the convergence interval because $1.5723 < \pi = 3.1416$:

$$\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin\!\left(\frac{n\hat\pi}{2}\right) = \frac{\hat\pi}{4} = \frac{1}{\sqrt\varphi} = 0.7861513777574233.$$

The relabel here is not an approximation and not an error: it is the same identity, read on a rescaled axis, and the value it lands on is the exact algebraic number $1/\sqrt\varphi$ rather than the transcendental $\pi/4 = 0.7853981634$. Written in the code block in which this site keeps its identities:

```text
sawtooth series    : sum (-1)^(n+1) sin(n x)/n = x/2   for |x| < pi
conventional       : x = pi/2   ->  pi/4  = 0.7853981633974483
golden             : x = hatpi/2 = 2/sqrt(phi) = 1.5723027555
                     sum = hatpi/4 = 1/sqrt(phi) = 0.7861513777574233
relative difference: 0.0959022%   (the same gap, undiluted)
```

The algebra is the cleanest illustration in this article of what the site claims and what it does not. What it claims: $4/\sqrt\varphi$ is a *constructible* number, algebraic of degree four, the root of $x^4 + 16x^2 - 256 = 0$, and every angular identity re-expressed in it lands on an algebraic value in $\mathbb{Q}(\sqrt\varphi)$ — a genuine, coherent, complete re-coordinatisation of the turn, argued at length in the [constructibility article](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/). What it does not claim: that $\hat\pi$ repairs a single one of the arithmetic limits — Basel, Parseval, the even zeta values — whose numerical content is integer sum rather than geometry. Those pin the constant at $3.14159265358979323846\ldots$, which is why the honest column in every table on this site is the one that simply reports the gap.

## The Gibbs Ring: A Computed Overshoot, Not a Measured One

One more number belongs in this article, because it is the most visual thing about square waves and the one most often described as though it were observed. Truncating the square-wave series at $N$ odd terms leaves an overshoot of about 9% just before the jump — the ringing every oscilloscope photograph of a fast edge seems to confirm. Henry Wilbraham described it in 1848; J. Willard Gibbs rediscovered it in 1899.

It is not measured, it is computed. The truncated series is

$$f_N(x) = \frac{2}{\pi}\int_0^x \frac{\sin(2N+1)\,t}{\sin t}\,dt \quad\Longrightarrow\quad \text{overshoot} \to \frac{2}{\pi}\operatorname{Si}(\pi) - 1 = 0.1789797445,$$

where $\operatorname{Si}$ is the sine integral — the very function whose value at infinity the [Dirichlet integral article](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) evaluated as $\pi/2$. The limit is $0.1789797445$ relative to a jump of height 2, that is $8.9489872\%$, and it is the same number at every truncation order: the ring does not shrink, it narrows. Evaluating the same expression with the Golden Pi half-turn in the upper limit gives $2\operatorname{Si}(\hat\pi)/\hat\pi - 1 = 0.1778494914$, or $8.8924746\%$ of the jump — a $0.63\%$ relative shift in the overshoot, which is exactly the kind of quantity in which the circle constant enters as an integration ceiling and therefore as a *label* rather than as a shape.

And here the honesty has to be sharpest, because unlike the fine-structure constant, the Gibbs overshoot does not vanish from the formula. It really does contain the constant. What saves the measurement from adjudicating is the mathematics on the other side: the ideal square wave, with its jump discontinuity and its infinitely many harmonics, is a mathematical limit that no physical signal attains. Real edges are exponential or error-function transitions, and their overshoot depends on rise time, source impedance, probe inductance and bandwidth — parameters that move the observed ring by tens of percent. A 0.63% shift in the theoretical ceiling is invisible inside the model error of the model that produced it.

## The Honest Boundary

Where this leaves the Fourier argument, stated plainly:

- **The constant enters as the axis, not as a shape.** Every angular identity relabels cleanly: the turn becomes $2\hat\pi = 8/\sqrt\varphi$, the phasor $\omega = 2\hat\pi f$, the fundamental amplitude $4/\hat\pi = \sqrt\varphi$, the sawtooth limit $\hat\pi/4 = 1/\sqrt\varphi$. All of these are exact algebraic values in $\mathbb{Q}(\sqrt\varphi)$, and all of them are the same mathematics read on a rescaled coordinate.
- **The waveform's own facts do not move.** RMS, the value at a jump, the presence of only odd harmonics, and the physical frequency of every spectral line are properties of the signal, not the coordinate — which is why a spectrum analyser, which is a measuring instrument in the strict sense, cannot arbitrate a relabel of the radians it uses to describe angles.
- **The arithmetic identities are refuted, not relabelled.** Parseval's theorem for the unit square wave demands $\hat\pi^2/8 = 2/\varphi = 1.2360679775$ against the fixed reciprocal-square sum $1.2337005501$, a $0.1919167\%$ shortfall. The same failure mode appeared in the Basel post and reappeared through the even zeta values; it is the honest price of the thesis, and this site keeps paying it in public.
- **The recurring gap is $0.0959022\%$.** It is unsoftened where the constant enters to the first power, doubled where it enters squared, amplified to $0.5052324\%$ in the total harmonic distortion, and rotated to $0.0958103\%$ on amplitudes because it rides through the reciprocal $1/\hat\pi = \sqrt\varphi/4 = 0.3180049123785172$.

The circle constant is computed, never measured. Fourier analysis is where that sentence stops being a slogan about series and becomes a statement about coordinate systems: the signal is real, the spectrum is real, the frequencies are measured — and the turn in which they are written is a choice, one that Golden Pi rewrites exactly and that no oscilloscope can put back.

## Further Reading

- [**The Dirichlet Integral and the Sinc: How ∫₀^∞ sin(x)/x dx Computes the Circle Constant**](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) — the sine integral $\operatorname{Si}(\pi) = \pi/2$ whose value sets the Gibbs ring computed above.
- [**The Basel Problem: When an Infinite Sum Computes the Circle Constant**](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the sister identity to Parseval's energy sum, and the same honest verdict on substituting the constant.
- [**The Fine-Structure Constant: Why Physics's Most Famous 4π Cancels Out**](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — where the $2\pi$ of a phasor and the $\hbar$ of the quantum of action either cancel or shift by the gap.
- [**The Roots of Unity: How the Complex Solutions of zⁿ = 1 Compute the Circle Constant**](/blog/posts/2026-09-09-roots-of-unity-compute-circle-constant-golden-pi/) — the discrete counterpart of a Fourier series, where the same $2\pi k/n$ coordinates the harmonics.
- [**The Comparative Formula Audit: Which π Identities Survive Golden Pi?**](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — the formula-by-formula ledger separating geometry that relabels from analysis that refutes.
