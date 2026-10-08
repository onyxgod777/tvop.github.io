---
title: "Lévy's Constant and Khinchin's Constant: How the Typical Continued Fraction Computes the Circle Constant as π²/(12 ln 2) — and What Golden Pi Changes"
date: 2026-10-08
description: "Almost every real number has a continued fraction whose partial quotients obey the Gauss–Kuzmin law, and two exact constants govern it: Khinchin's constant K₀ = 2.685452001065306… is completely π-free, while Lévy's constant is e^{π²/(12 ln 2)} = 3.275822918721811…, carrying the circle constant in the exponent through the alternating Basel sum η(2) = π²/12 = 1 − 1/2² + 1/3² − … Both are computed limits of a measure-theoretic average, never measurements. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693…, π̂² = 16/φ) every π-carrying quantity here scales as π², so the recurring 0.0959022309% gap doubles to 0.1918964% in the exponent — Lévy's constant becomes the exact e^{4/(3φ ln 2)} = 3.283290412932232… (+0.2279578%), the Gauss–Kuzmin entropy π²/(6 ln 2) = 2.373138220831250… becomes 8/(3φ ln 2) = 2.377692188454129…, Lochs' constant 6 ln 2 ln 10/π² = 0.970270114392033… (one CF term per decimal digit) becomes 0.968411766743904…, while Khinchin's constant — the one constant in the pair that has no π in it at all — does not move by a single digit. The honest ledger is public: Khinchin's constant is proven only for almost every number and is not known for π, e, √2, or any naturally occurring constant, so the theory's own statistics supply a place where the label cannot be read off a measurement. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Lévy's Constant and Khinchin's Constant: How the Typical Continued Fraction Computes the Circle Constant as π²/(12 ln 2)

Ask a computer for the digits of π and it hands you a string. Ask it for the **continued fraction** of π and it hands you something stranger:

$$3 + \cfrac{1}{7 + \cfrac{1}{15 + \cfrac{1}{1 + \cfrac{1}{292 + \cdots}}}} = [3;\,7,\,15,\,1,\,292,\,1,\,1,\,1,\,2,\,1,\,3,\,1,\,14,\,2,\ldots]$$

That lone $292$ is why $\tfrac{355}{113}$ is such a famously good approximation to the circle constant — the next term after a huge one is always tiny, and a tiny term means the convergent is already as good as it can be. But the continued fraction of a *specific* number is not what this article is about. It is about the **continued fraction of a typical number**, the statistics that hold for almost every real, and the two exact constants — Lévy's and Khinchin's — that summarise those statistics. One of them is built, digit for digit, out of the circle constant. The other, remarkably, contains no trace of it. Both are **computed**, never measured.

## The four questions

As with every entry in this series, the same four questions are put to the subject: *where* exactly does the circle constant enter, is it **computed** or measured, does it cancel anywhere, and what changes when the constant is the golden value $\hat\pi = 4/\sqrt\varphi$ instead of the analytic $3.14159\ldots$? Here the answers are unusually clean — because the whole theory rests on one integral, $\int_0^1 \frac{\ln x}{1+x}\,dx = -\frac{\pi^2}{12}$, and on one product that has no circle constant in it at all.

## Continued fractions in one paragraph

Every real number $x$ has a continued fraction

$$x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}} = [a_0;\,a_1,\,a_2,\,a_3,\ldots],$$

with integer **partial quotients** $a_0, a_1, a_2,\ldots$ ($a_n \ge 1$ for $n \ge 1$). Truncating at the $n$-th term gives a **convergent** $p_n/q_n$ — the best rational approximation to $x$ with denominator at most $q_n$. The engine behind all of this is the **Gauss map**

$$T(x) = \frac{1}{x} \bmod 1,$$

which shifts the continued-fraction expansion one place to the left: if $x = [a_0; a_1, a_2,\ldots]$ then $T(x) = [a_1; a_2, a_3,\ldots]$. The partial quotients are simply the iterates $a_n = \lfloor T^{n-1}(x)\rfloor$ (after the first). Everything that follows is a statement about the long-run behaviour of this map.

## The Gauss map has a measure, and Gauss knew it

In a letter to Laplace around 1812, Gauss observed that for *almost every* real $x$ (in the sense of Lebesgue measure — every $x$ except a set of measure zero) the partial quotients are distributed according to

$$\mu(a_n = k) = -\log_2\!\left(1 - \frac{1}{(k+1)^2}\right) = \log_2\frac{(k+1)^2}{k(k+2)}.$$

This is the **Gauss–Kuzmin distribution**. The first few values are genuinely informative about how lopsided it is:

| $k$ | $\mu(a=k)$ |
|---:|:----------|
| 1 | 0.415037499278844 |
| 2 | 0.169925001442312 |
| 3 | 0.093109404391482 |
| 4 | 0.058893689053569 |
| 5 | 0.040641984913019 |
| 10 | 0.011972634221981 |

More than two fifths of all partial quotients in a typical expansion are the number $1$; the average is infinite in the naive sense, because $\sum_k k\,\mu(k)$ diverges — yet the *logarithmic* average is perfectly finite and exact, which is the whole story. The measure $\mu$ is the invariant measure of the Gauss map, its density $g(x) = \frac{1}{(1+x)\ln 2}$ on $[0,1)$, and the theorem that the empirical counts converge to it is the **Gauss–Kuzmin–Lévy theorem**. Kuzmin (1928) gave the first geometric rate of approach, Lévy (1929) sharpened it, and Wirsing (1974) gave the best-known refinement. As with every quadrature in this series: it is a **computed** limiting average of an iteration, not a measurement of anything physical.

## Lévy's constant: the price of a digit

The convergents' denominators do not grow by a constant *ratio* — they grow by a constant **exponential rate**. Lévy's theorem states that for almost every $x$,

$$\lim_{n\to\infty} q_n^{1/n} = e^{\lambda}, \qquad \lambda = \frac{\pi^2}{12\ln 2} = 1.1865691104156254528\ldots$$

so that

$$e^{\lambda} = e^{\pi^2/(12\ln 2)} = 3.275822918721811159787681882453843863608\ldots$$

This is **Lévy's constant**: the amount each additional continued-fraction term multiplies the denominator by, on average. Ten terms buy you a denominator roughly $3.2758^{10} \approx 1.5\times10^{5}$; twenty buy about $2.3\times10^{10}$; a hundred buy a denominator with about fifty decimal digits. The constant is a *rate of growth*, exact, universal, and the same for almost every number.

### Where π enters: it is ζ(2), computed

The circle constant enters through exactly one integral. Write $\lambda$ as the logarithmic average of a partial quotient under the Gauss–Kuzmin measure, and the computation reduces to

$$\int_0^1 \frac{\ln x}{1+x}\,dx = -\eta(2) = -\frac{\pi^2}{12},$$

where $\eta$ is the Dirichlet eta function, the alternating Basel sum

$$\eta(2) = 1 - \frac{1}{2^2} + \frac{1}{3^2} - \frac{1}{4^2} + \cdots = \frac{\pi^2}{12} = 0.82246703342411321824\ldots$$

So $[\pi]^2/12$ is not smuggled in and it is not fitted: it is the **evaluated limit of an alternating series**, the same kind of computation that gives $\zeta(2) = \pi^2/6$ in the Basel problem. Expanded with the Gauss-map density,

$$\lambda = -\frac{1}{\ln 2}\int_0^1 \frac{\ln x}{1+x}\,dx = \frac{\pi^2}{12\ln 2} = 1.186569110415625\ldots, \qquad e^{\lambda} = 3.275822918721811\ldots$$

The constant is in the **exponent**, sitting on a $\pi^2$, and this placement controls everything Golden Pi will do to it below.

## The π-free twin: Khinchin's constant

Now the surprise. The other famous constant of typical continued fractions is **Khinchin's constant** (Khinchin, 1934): for almost every $x$,

$$\lim_{n\to\infty}\left(a_1 a_2 \cdots a_n\right)^{1/n} = K_0 = \prod_{n=1}^{\infty}\left(1 + \frac{1}{n(n+2)}\right)^{\log_2 n} = 2.685452001065306445309714835481795693820\ldots$$

Look at that product: it is built entirely out of the integers $n$ and the number $2$ (inside the logarithm base). **There is no circle constant in it.** The product converges with maddening slowness, which is why $K_0$ is quotable only by its computed value — the partial products are

| $N$ | $\prod_{n=1}^{N}\left(1+\frac{1}{n(n+2)}\right)^{\log_2 n}$ |
|---:|:---|
| 100 | 2.479449507190304 |
| 1 000 | 2.655030716354816 |
| 10 000 | 2.681499686663012 |
| 100 000 | 2.684967264898291 |
| $\to\infty$ | 2.685452001065306… |

This is the honest heart of the article. Lévy's constant carries $\pi$ in its exponent; the Gauss–Kuzmin entropy carries $\pi$; Lochs' constant carries $\pi$ — and Khinchin's constant carries none. The circle constant is not welded to the theory of continued fractions; it appears in a specific, replaceable coefficient ($\eta(2)$), and one of the theory's two flagship constants does not touch it.

There is a second, sharper honesty point. Khinchin's constant is proven for **almost every** number — the exceptional set has measure zero — and has **never been proven** for $\pi$, for $e$, for $\sqrt2$, or for any number a human has ever actually cared about. The same pattern in $\pi$'s own expansion is therefore a conjecture, not a theorem.

## Lochs' theorem: how many terms buy a decimal digit

Gustav Lochs (1964) connected continued fractions to ordinary decimal accuracy. If $n$ decimal digits of accuracy require $m$ continued-fraction terms, then for almost every $x$,

$$\lim \frac{n}{m} = \frac{6\ln 2\,\ln 10}{\pi^2} = 0.9702701143920339257402560192100108337813\ldots$$

or inverted, $1/0.970270114\ldots = 1.0306408341007129$ — **about 1.03 continued-fraction terms buy one decimal digit.** Converted to bits, the same statement reads that one term carries $\log_2(10)\times0.97027 = 3.223$ bits of information about $x$, matching the Gauss–Kuzmin source entropy $H$ below.

## π's own continued fraction — and the honest caveat

Here is the continued fraction of the circle constant itself, to enough terms to be interesting:

$$[3;\,7,\,15,\,1,\,292,\,1,\,1,\,1,\,2,\,1,\,3,\,1,\,14,\,2,\,1,\,1,\,2,\,2,\,2,\,2,\,1,\,84,\,2,\,1,\,1,\,15,\,3,\,13,\,1,\,4,\ldots]$$

The term $292$ is famously anomalous, and it is precisely why $355/113$ is so good: from it, $355/113 = 3.141592920353982\ldots$, correct to six decimal places. But the statistics of a *finite* prefix wander wildly, and this is worth watching concretely. The geometric mean of the first $n$ partial quotients of $\pi$ (skipping the leading $3$) is

| $n$ | geometric mean of $a_1\ldots a_n$ |
|---:|:---|
| 10 | 3.361030 |
| 20 | 2.487712 |
| 30 | 2.886591 |
| 40 | 3.147711 |
| 59 | 2.750654 |

It is nowhere near $K_0 = 2.685452$ after these many terms — and it need not be. Convergence to the Khinchin constant is glacial, and for $\pi$ it is not even known to occur. Nothing on this page allows a reader to claim that $\pi$'s continued fraction *measures* the circle constant: the partial quotients are integers, produced by a deterministic algorithm, and the constants they are supposed to approach are limiting averages that no finite computation reaches.

## What Golden Pi changes

The golden constant is $\hat\pi = 4/\sqrt\varphi$, the root of $x^4 + 16x^2 - 256 = 0$, with the exact square

$$\hat\pi^2 = \frac{16}{\varphi} = 8(\sqrt5 - 1) = 9.888543819998317571273389349850209883525\ldots$$

against $\pi^2 = 9.869604401089358618834490999876151135314\ldots$. Every quantity in this article carries $\pi$ **squared**, so the recurring one-power gap of $0.0959022309\%$ doubles to $0.1918964\%$, undiluted:

| quantity | conventional | Golden Pi | shift |
|:---|:---|:---|:---|
| $\pi^2/12 = \eta(2)$ | 0.8224670334241132182 | $\frac{4}{3\varphi} = 0.8240453183331931309$ | $+0.1918964\%$ |
| Lévy exponent $\lambda = \pi^2/(12\ln 2)$ | 1.1865691104156254528 | $\frac{4}{3\varphi\ln 2} = 1.1888460942270649314$ | $+0.1918964\%$ |
| Lévy's constant $e^{\lambda}$ | 3.2758229187218111598 | $e^{4/(3\varphi\ln 2)} = 3.2832904129322327269$ | $+0.2279578\%$ |
| Gauss–Kuzmin entropy $H = \pi^2/(6\ln 2)$ | 2.3731382208312509056 | $\frac{8}{3\varphi\ln 2} = 2.3776921884541298627$ | $+0.1918964\%$ |
| Lochs' constant $6\ln2\ln10/\pi^2$ | 0.9702701143920339257 | 0.9684117667439049437 | $-0.1915289\%$ |
| Khinchin's constant $K_0$ | 2.6854520010653064453 | 2.6854520010653064453 | none |

The Lévy constant shifts by more than the others — $0.2279578\%$ rather than $0.1918964\%$ — and for an exact reason: it sits in an **exponent**. If $\text{Lévy} = e^{\lambda}$ with $\lambda \propto \pi^2$, then the relative change is $\lambda$ times the exponent's relative change, and $\lambda = 1.1865691$ gives

$$\frac{\Delta \text{Lévy}}{\text{Lévy}} = \lambda \times 0.1918964\% = 1.1865691 \times 0.001918964 = 0.002279578.$$

That is precisely the $+0.2279578\%$ in the table — the extra size is the amplified leverage of an exponent, not a new effect. Khinchin's constant, having no circle constant inside it, does not move by a single digit under the relabel, which is the cleanest possible statement of where the constant lives and where it does not.

### The exact golden relations

Where the relabel produces exact algebraic forms rather than shifted decimals, they are credited plainly:

$$\hat\pi^2 = \frac{16}{\varphi}, \qquad \frac{\hat\pi^2}{16} = \frac{1}{\varphi} = 0.6180339887498948482\ldots \text{ exactly}, \qquad \text{Lévy}_{\text{golden}} = 2^{\,4/(3\varphi(\ln 2)^2)} = e^{\,4/(3\varphi\ln 2)}.$$

And the recurring geometric exactness of the golden value holds here too: a disk of radius $\varphi^{1/4} = 1.1278384855616822603$ has area **exactly $4$** under Golden Pi, where the conventional value gives $3.996167586135262\ldots$ — short by exactly the gap.

## Computed, never measured

Nothing on this page is a measurement, and it is worth saying why explicitly. The quantity $\pi^2/12$ is the **evaluated limit** of the alternating series $\eta(2)$; the Gauss–Kuzmin density is the computed invariant measure of an iteration; Lévy's constant is the exponential of a computed integral; Khinchin's constant is the limit of a computed product. Every one of them is a limit of a computation, fixed by arithmetic alone, with no physical input anywhere.

This has a consequence for the π dispute that the site always states plainly. The recurring $0.0959022309\%$ gap between $\pi$ and $\hat\pi$ is **not** something a laboratory could settle here, and not because the equipment is too coarse — but because there is no measurable quantity in the theory of typical continued fractions at all. One cannot measure the limiting geometric mean of the infinite partial-quotient sequence of a typical real number, because "typical" is a statement about almost every number, not about a physical object. The comparison is decided the only way it can be: by arithmetic, in the open, on an exact series and an exact integral. Contrast with a genuine measurand — the fine-structure constant, or a physical length — where the apparatus does arbitrate. Here it does not, and no honest ledger pretends otherwise.

Computed, never measured.

## Further Reading

- [The Basel Problem: How the Alternating and Even-Integer Series Compute the Circle Constant as π²/6 — and What Golden Pi Changes](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the series that supplies $\pi^2/12$ here.
- [The Continued Fraction of the Circle Constant: How Best Rational Approximations Compute π — and What Golden Pi Changes](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) — the finite expansion of $\pi$ itself.
- [The Riemann Zeta Function at Even Integers: How Bernoulli Numbers Compute π², π⁴, π⁶ — and What Golden Pi Changes](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — where the $\pi^2$ in $\eta(2)$ ultimately comes from.
- [The Gauss Circle Problem: How Counting Lattice Points Computes the Circle Constant, and What Golden Pi Changes](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/) — the other place Gauss's name meets the circle constant.
- [Euler's Identity: How e^{iπ} + 1 = 0 Computes the Circle Constant — and What Golden Pi Changes](/blog/posts/2026-09-19-euler-identity-computes-circle-constant-golden-pi/) — the connection between $e$ and the constant, in one line.
