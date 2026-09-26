---
title: "The Wallis Product and Stirling's Approximation: How Factorials Compute the Circle Constant as √(2πn), and What Golden Pi Changes"
date: 2026-09-26
description: "Wallis's 1655 product extracts the circle constant from a sequence of exact rationals — 4/3, 64/45, 256/175 … — and Stirling's 1730 approximation puts the same constant in √(2πn). Both are computed limits of arithmetic, never measurements: the partial product at N = 10⁴ already sits 39.4× closer to π/2 than to π̂/2, and Stirling's own truncation error 1/(12N) falls below the golden gap only at N ≈ 87. Under Golden Pi (π̂ = 4/√φ) the constant becomes algebraic, 1/√(2π̂) = φ^(1/4)/(2√2) exactly, while the rational chains do not move at all."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Two of the most consequential formulas in mathematics were both written to answer a question about factorials, and both arrived carrying the same constant.

John Wallis's *Arithmetica Infinitorum* (1655) gives the circle constant as a limit of a ratio of whole numbers. James Stirling's *Methodus Differentialis* (1730) gives $n!$ as $\sqrt{2\pi n}\,(n/e)^n$ — the same constant, this time in a single expression. Neither involves a circle, and neither involves a measurement. Wallis's sequence is built from the integers alone; Stirling's constant is fixed by matching that sequence, and the sequence's limit is an integral — a computed limit, never a reading off an instrument.

That makes this a clean place to audit the claim that the circle constant could be $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$ instead of $\pi = 3.14159265358979323846\ldots$, because here the decisive numbers are **rational**. Nothing empirical intervenes: the partial products are exact fractions and the partial-sum comparison can be run with as many digits as anyone cares to compute.

Throughout: the circle constant is *computed* — an integral, a squeeze, a limit of rationals. Only genuine physical measurands are measured, and none is needed below.

## Wallis's product: the constant as a limit of rationals

Start with the integrals

$$I_n = \int_0^{\pi/2}\sin^n\theta\,d\theta .$$

Their exact values are $I_0 = \pi/2$ and $I_1 = 1$, and integration by parts gives the recurrence $I_n = \dfrac{n-1}{n}\,I_{n-2}$ — a chain of **pure rational multipliers**. Every value follows from the two seeds, evaluated here exactly:

| $n$ | $I_n$ closed form | decimal |
|---|---|---|
| 0 | $\pi/2$ | 1.570796326794896619231322 |
| 1 | $1$ | 1.000000000000000000000000 |
| 2 | $\pi/4$ | 0.785398163397448309615661 |
| 3 | $2/3$ | 0.666666666666666666666667 |
| 4 | $3\pi/16$ | 0.589048622548086232211746 |
| 5 | $8/15$ | 0.533333333333333333333333 |
| 6 | $5\pi/32$ | 0.490873852123405193509788 |
| 7 | $16/35$ | 0.457142857142857142857143 |
| 8 | $35\pi/256$ | 0.429514620607979544321065 |
| 9 | $128/315$ | 0.406349206349206349206349 |
| 10 | $63\pi/512$ | 0.386563158547181589888958 |
| 11 | $256/693$ | 0.369408369408369408369408 |

Two exact formulas generate the whole table:

$$I_{2n} = \frac{\pi}{2}\cdot\frac{\binom{2n}{n}}{4^n},\qquad I_{2n+1} = \frac{4^n}{(2n+1)\binom{2n}{n}} .$$

Since $\sin^{n+1}\theta \le \sin^n\theta$ on $[0,\pi/2]$, the sequence $I_n$ decreases, so $I_{2n} > I_{2n+1}$ and the **ratio** $I_{2n}/I_{2n+1}$ is squeezed to 1 from above. Divide the two exact formulas and everything cancels except one rational factor times the half turn:

$$\frac{I_{2n}}{I_{2n+1}} = \frac{\pi}{2}\cdot\frac{(2n+1)\binom{2n}{n}^2}{4^{2n}} = \frac{\pi/2}{W_n},$$

with

$$W_n = \prod_{k=1}^{n}\frac{4k^2}{4k^2-1} = \frac{16^n\,(n!)^4}{(2n+1)\big((2n)!\big)^2}.$$

That closed form is exactly correct — verified term by term for $n = 5$ and $n = 10$ against the product — and every $W_n$ is a rational number. Wallis's product is the statement $\lim_{n\to\infty} W_n = \pi/2$. Numerically:

| $n$ | $W_n$ (exact) | decimal | $\pi/2 - W_n$ |
|---|---|---|---|
| 1 | $4/3$ | 1.3333333333333333333 | 0.2374629934615632860 |
| 2 | $64/45$ | 1.4222222222222222222 | 0.1485741045726743970 |
| 3 | $256/175$ | 1.4628571428571428571 | 0.1079391839377537621 |
| 4 | $16384/11025$ | 1.4860770975056689342 | 0.0847192292892276850 |
| 5 | $65536/43659$ | 1.5010879772784534689 | 0.0697083495164431503 |
| 10 | $68719476736/44801898141$ | 1.5338519033217494855 | 0.0369444234731471337 |
| 100 | — | 1.5668937453140811206 | 0.0039025814808154986 |
| 1 000 | — | 1.5704038730151972802 | 0.0003924537796993390 |
| 10 000 | — | 1.5707570593409610235 | 0.0000392674539355957 |
| 100 000 | — | 1.5707923998286231896 | 0.0000039269662734296 |
| 1 000 000 | — | 1.5707959340960603573 | 0.0000003926988362619 |

The relative error is itself rational in leading order, $W_n = \dfrac{\pi}{2}\left(1 - \dfrac{1}{4n}\right)+O(n^{-2})$: at $n = 10^6$ the deficit is $2.4999984\times10^{-7}$, against $1/(4n) = 2.5\times10^{-7}$. Note what this means: the *absolute* error term carries the constant ($\pi/2 - W_n \approx \pi/(8n)$), but the *relative* error does not — so arithmetic alone can ask how fast the product converges, with no constant in the question.

The same limit appears in the central binomial coefficient. With $\binom{2n}{n}/4^n$ the probability of a fair coin landing exactly even after $2n$ tosses,

$$\frac{\sqrt{\pi n}}{4^n}\binom{2n}{n} \longrightarrow 1 ,$$

evaluated here at $0.9987507861$ for $n = 100$ and $0.9999987500$ for $n = 10^5$ (the approach is $1 - 1/(8n)$, so $n = 10^5$ is one hundred times closer than $n = 10^3$). These are exact rationals divided by $4^n$ — de Moivre's route to the same constant, and no instrument is anywhere near it.

## Stirling's approximation and where $\sqrt{2\pi}$ comes from

Stirling's result is

$$n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n = 2.5066282746\ldots\times n^{\,n+\frac12}e^{-n},$$

and in logarithmic form

$$\ln n! = n\ln n - n + \tfrac12\ln(2\pi n) + \frac{1}{12n} - \frac{1}{360n^3} + \frac{1}{1260n^5} - \frac{1}{1680n^7} + \cdots$$

Every coefficient after the constant term is **rational** — the Bernoulli numbers $B_{2k}/(2k(2k-1))$, entering as $1/12$, $-1/360$, $1/1260$, $-1/1680$. The constant $\tfrac12\ln(2\pi)$ is the only non-rational piece in the entire asymptotic series, and it is fixed by making the formula agree with Wallis: the limit $\sqrt{n}\binom{2n}{n}/4^n \to 1/\sqrt{\pi}$ is equivalent to Stirling's preface, and the $\sqrt{2\pi}$ in the Gaussian normalisation $1/\sqrt{2\pi} = 0.3989422804014326779399460599\ldots$ comes from the same polar-coordinate integral in which the full turn's angular measure appears. So $\sqrt{2\pi}$ is not an independent fact: it is Wallis's constant, written under a square root, and Wallis's constant is a limit of rationals.

Two checks, computed here:

$$\ln 1000! - \left(1000\ln 1000 - 1000 + \tfrac12\ln(2000\pi)\right) = 8.333333055555634920575969\times10^{-5},$$

against $1/12000 = 8.3333333333\times10^{-5}$ — eight digits of agreement, with the difference $2.777776984\times10^{-12}$ matching $-1/(360\cdot10^9)$ to six digits. The series is honest: it is an *asymptotic* expansion, not a convergent one, and it says so in the growth of the Bernoulli coefficients.

## The honest ledger of a truncation error

Because the Stirling estimate is explicit, its failure is explicit too. The relative error of $\sqrt{2\pi n}(n/e)^n$ against $n!$ is

| $n$ | relative error | $1/(12n)$ | ratio |
|---|---|---|---|
| 100 | $-8.3298343215699983\times10^{-4}$ | $8.3333333\times10^{-4}$ | 0.99958 |
| 1 000 | $-8.3329858430014207\times10^{-5}$ | $8.3333333\times10^{-5}$ | 0.999958 |
| 100 000 | $-8.3333298610842979\times10^{-7}$ | $8.3333333\times10^{-7}$ | 0.9999996 |

The pattern is exact: the relative error is $-1/(12n)$ to better than a part in $10^3$ by $n = 10^5$. This is a **computed** statement about factorials — $100!$ has 159 digits, $1000!$ has 2569 digits, and both are integers anyone can multiply out — so the question "which constant sits in the prefactor?" can be settled by long multiplication, with no measurement and no uncertainty budget. That is the register this site keeps: here the constant is a computed limit, and the evidence against or for a relabelling is arithmetic.

## Entropy, coins and the half-a-logarithm

The constant's only structural role in combinatorics is that single $\tfrac12\ln(2\pi n)$. Take $N$ fair coins. The multiplicity of a macrostate with fraction $p$ of heads is $\binom{N}{pN}$, and Stirling turns its logarithm into

$$\ln \binom{N}{pN} = N\,H(p) - \tfrac12\ln\!\big(2\pi N p(1-p)\big) + O(1/N),\qquad H(p) = -p\ln p-(1-p)\ln(1-p).$$

For $N = 100$ and $p = 1/2$ the exact multiplicity gives $\binom{100}{50}/2^{100} = 0.0795892373871787614981\ldots$, while the Stirling-based estimate $1/\sqrt{50\pi} = 0.0797884560802865355880\ldots$ misses it by $-0.2496836044894912791\%$ — that is $-1/(8\cdot50)$, the leading correction, again with no constant in the error.

Boltzmann's entropy $S = k_B\ln\Omega$ then carries the circle constant exactly once, as

$$\tfrac12\ln(2\pi) = 0.9189385332046727417803297364 ,$$

or in the differential-entropy form $\tfrac12\ln(2\pi e) = 1.4189385332046727417803297364$ nats. In the Sackur–Tetrode expression for a monatomic ideal gas, $S = k_BN\left[\ln\!\big(V/(N\lambda^3)\big) + \tfrac52\right]$, that constant is a single additive term, independent of $N$ — a fixed offset in every absolute entropy tabulated in every thermodynamics text. Its physical size, if the constant were relabelled, would be $k_B\times0.0004792813703444 = 6.6171934468\times10^{-27}\ \text{J}\,\text{K}^{-1}$ — 1446 times smaller than the one-bit entropy $k_B\ln 2 = 9.5699296169\times10^{-24}\ \text{J}\,\text{K}^{-1}$, and, even multiplied across a mole's worth of the same offset, $3.985\times10^{-3}\ \text{J}\,\text{K}^{-1}$ against a standard molar entropy near $150\ \text{J}\,\text{K}^{-1}\text{mol}^{-1}$. The honest reading of those numbers: the constant in Stirling is nowhere near experimentally addressable in any entropy measurement, which is exactly why it has to be settled by computation.

## What Golden Pi changes

Under Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$ with $\varphi = (1+\sqrt5)/2 = 1.6180339887\ldots$ — the root of $x^4+16x^2-256 = 0$, hence algebraic. Because $\hat\pi$ is algebraic, every closed form that contains it becomes algebraic too. The identities of this article become:

$$2\hat\pi = \frac{8}{\sqrt\varphi} = 6.2892110220593862886,\qquad \frac{\hat\pi}{2} = \frac{2}{\sqrt\varphi} = 1.5723027555148465721,$$

$$\sqrt{2\hat\pi} = 2\sqrt2\,\varphi^{-1/4} = 2.5078299428109925749 \quad\text{(exactly)},$$

$$\frac{1}{\sqrt{2\hat\pi}} = \frac{\varphi^{1/4}}{2\sqrt2} = 0.3987511206119157987 \quad\text{(exactly)},$$

$$\sqrt{\hat\pi} = \frac{2}{\varphi^{1/4}} = 1.7733035586243245185 \quad\text{(exactly)},\qquad \Gamma\!\left(\tfrac12\right)^2 = \hat\pi = \frac{4}{\sqrt\varphi},$$

using $\varphi^{1/4} = 1.1278384855616822603$. The shifts are:

- $\sqrt{2\pi} \to \sqrt{2\hat\pi}$: $2.5066282746310005024 \to 2.5078299428109925749$, **$+0.0479396244011876635\%$** — exactly half the recurring $0.095902230878\%$ gap, because the constant sits under a square root.
- $\tfrac12\ln(2\pi) \to \tfrac12\ln(2\hat\pi)$: $0.9189385332046727418 \to 0.9194178145750171023$, a shift of only **$0.0004792813703443604711$ nats** — a logarithm turns a $0.0959\%$ factor into an additive $0.00048$.
- Wallis's product: $\lim W_n$ would become $\hat\pi/2 = 1.5723027555148465721$ instead of $1.5707963267948966192$.
- Stirling's prefactor at $n = 10^5$: $\sqrt{2\hat\pi\,n}(n/e)^n$ sits $+0.0479396244\%$ above $\sqrt{2\pi n}(n/e)^n$ and therefore $+0.0478562512\%$ above $10^5!$ itself, where the ordinary Stirling estimate is $8.3333\times10^{-7}$ *below* it.

The last line shows what a golden relabel would have to buy. The golden Stirling error is $-1/(12n) + 0.0004793962440$ relative, which passes through zero at

$$n^* = \frac{1}{12\times 0.0004793962440} = 173.8297585228240145157 .$$

So a golden Stirling formula **does** reproduce $n!$ exactly at $n \approx 174$ ($n = 174$: relative error $+3.546946\times10^{-7}$; $n = 175$: $+3.091417\times10^{-6}$). A single-value test at the crossover would look like a success. Two values kill it: at $n = 100$ the golden form is $3.5398652\times10^{-4}$ too small, and at $n = 10^5$ it is $4.7856251\times10^{-4}$ too large, while the ordinary form has error $-8.3298343\times10^{-4}$ and $-8.3333299\times10^{-7}$ — the right sign and the right $1/(12n)$ trend at both ends. Since factorials are integers, no measurement uncertainty, however small, can be pleaded here.

## The rational chain cannot reach $\hat\pi/2$

The strongest ledger entry is structural, and it is about Wallis. Every $W_n$ is a rational number, the sequence increases monotonically, and it is bounded above by $\pi/2$ — because the squeeze $I_{2n}/I_{2n+1} \to 1$ is anchored on $I_0 = \pi/2$, the half turn itself. Since

$$\frac{\pi}{2} = 1.5707963267948966192 \;<\; \frac{\hat\pi}{2} = 1.5723027555148465721,$$

no partial product, at any $n$, ever reaches $\hat\pi/2$ — the golden half turn lies above the limit of the whole chain. The nearest the chain gets at $n = 10^6$ is $0.0015068214187862148$ short of it, i.e. $0.0958353227\%$; and the chain's own distance from the true limit there is $3.9269884\times10^{-7}$. The ratio is the size of the audit:

| $n$ | $(\hat\pi/2 - W_n)\,/\,(\pi/2 - W_n)$ |
|---|---|
| $10^4$ | 39.363289925053764 |
| $10^6$ | 3 837.0916326860556 |

At $n = 10^4$ — a product of ten thousand rational factors, computable exactly — the partial product is already **39.4 times closer** to the classical half turn than to the golden one, and the margin grows in proportion to $n$. A relabelled constant would need the product to climb past its own limit and keep going, which a monotone bounded sequence cannot do.

The fair statement of the golden case is this: $\hat\pi$ is algebraic, so the golden versions of these identities are *exact algebraic expressions* rather than limits of rationals — $\varphi^{1/4}/(2\sqrt2)$ really is the right prefactor for a world whose full turn measures $8/\sqrt\varphi$, and a consistent change of angular unit leaves every identity internally exact. What the arithmetic above shows is narrower and unanswerable in that register: the constant extracted by Wallis's rationals, by the central binomial coefficient, by the doubling of the factorial and by the Stirling prefactor is $\pi = 3.14159265358979323846\ldots$, and the whole of that extraction is computation. Computed, never measured.

## Further Reading

- [The Madhava–Leibniz Series: How the First Infinite Series Computes the Circle Constant](/blog/posts/2026-09-02-madhava-leibniz-series-first-infinite-series-computes-circle-constant-golden-pi/) — the sibling limit: an alternating sum of rationals, and how slowly it pays for its simplicity.
- [Ramanujan and Chudnovsky: How Algebraic Series Compute the Circle Constant to Billions of Digits](/blog/posts/2026-09-04-ramanujan-chudnovsky-series-computes-circle-constant-golden-pi/) — where the central binomial coefficient of this article reappears as the engine of record-breaking digit computations.
- [The Gaussian Integral: How the Bell Curve Computes the Root of the Circle Constant](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the polar-coordinate turn that produces the $\sqrt{2\pi}$ used above.
- [The Bessel Functions: How Cylindrical Waves Compute the Circle Constant Through a Half-Turn Integral](/blog/posts/2026-09-21-bessel-functions-cylindrical-waves-compute-circle-constant-golden-pi/) — the half-integer case where $\sqrt{2/(\pi x)}$ and $\Gamma(1/2)$ carry the constant.
- [The Heat Kernel: How the Diffusion Equation Computes the Circle Constant Through Its Own Normalisation](/blog/posts/2026-09-17-heat-kernel-diffusion-computes-circle-constant-golden-pi/) — $1/\sqrt{4\pi Dt}$, the same $\sqrt{\pi}$ under the same square root, and the same $-0.0479166533\%$ golden shift measured against $1/\sqrt{2\pi}$ here.
