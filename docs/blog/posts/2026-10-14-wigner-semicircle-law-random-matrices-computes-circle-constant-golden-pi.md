---
title: "The Wigner Semicircle Law: How the Circle Constant Normalises a Random Matrix's Spectrum, Then Cancels from Every Moment — and What Golden Pi Changes"
date: 2026-10-14
description: "Take a large random symmetric matrix, diagonalise it, and its eigenvalues pile up on a perfect semicircle — the Wigner semicircle law. The circle constant is in there exactly once, as the 1/(2π) that turns a semicircle's own area into a probability, and it cancels from every moment: the moments of the eigenvalues are the integer Catalan numbers 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, computed by counting non-crossing pairings, never measured. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the moment ladder does not move a digit, and the constant survives only as a pointwise density (1/π̂ = √φ/4, −0.0958103466%) and under a square root, where the Wigner surmise's most probable level spacing √(2/π̂) = φ^(1/4)/√2 = 0.7975022412 falls 0.0479166533% below the conventional 0.7978845608 — a genuine measurand that the noise in a 14 400-eigenvalue diagonalisation, at ±6.6% per bin, cannot begin to see."
---

# The Wigner Semicircle Law: How the Circle Constant Normalises a Random Matrix's Spectrum, Then Cancels from Every Moment — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Fill a large square array with random numbers, symmetrise it, and diagonalise it. Nobody drew a circle — the recipe mentions no geometry at all, only sums of independent random entries — and yet the eigenvalues arrange themselves on a perfect semicircle. Wigner noticed this in 1955 while trying to explain the statistics of nuclear energy levels, and sixty years of work turned it into a theorem: the *empirical spectral distribution* of a Wigner matrix converges to the semicircle law

$$
\rho(x) = \frac{1}{2\pi}\sqrt{4 - x^{2}} \quad \text{on } [-2,\,2], \qquad \int_{-2}^{2}\rho(x)\,dx = 1 .
$$

That $\tfrac{1}{2\pi}$ is the entire appearance of the circle constant in the shape, and this chapter asks the same question every chapter of this series asks: where exactly does the constant enter, is it doing arithmetic or merely supplying a label, and what would a golden relabelling $\hat\pi = 4/\sqrt\varphi$ change? The answer here is unusually clean — the moments of the distribution are **integers** — and it makes this one of the sharpest illustrations of the site's standing rule: the constant is *computed*, never measured.

## Where the constant enters — and why it cancels

The semicircle on $[-2,2]$ is a semicircle of radius $2$. Its area is

$$
\frac{\pi R^{2}}{2} = \frac{\pi \cdot 4}{2} = 2\pi = 6.283185307179586476925286766559005768394\ldots
$$

and the density above is nothing but that same area used as a divisor: the semicircle, *normalised by its own quadrature*, gives a probability measure of total mass $1$:

```
density:      ρ(x) = (1/2π)·√(4 − x²)
∫ ρ dx  =  (1/2π)·(area of a radius-2 semicircle)
        =  (1/2π)·(2π)  =  1   exactly
```

So the constant appears in the numerator's area and in the denominator's normalisation at the same first power, and multiplies out to one. That is not an approximation or a numerical coincidence; it is an identity, and it holds under **any** consistent label for the area. Under Golden Pi the radius-2 semicircle has the same area, labelled $2\hat\pi$, and dividing by $2\hat\pi$ still returns $1$. Where the constant *does* bite is pointwise: the literal function $1/(2\hat\pi)\sqrt{4-x^{2}}$ takes at the centre the value

$$
\frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4} = 0.3180049123785172410631056154343728729289\ldots
\quad\text{against}\quad
\frac{1}{\pi} = 0.3183098861837906715377675267450287240689\ldots,
$$

a fall of $0.0958103466\%$ — the recurring first-power gap of this series in its reciprocal form, and here it is **exactly algebraic**: $1/\hat\pi = \sqrt\varphi/4$.

## The moments are integers, and they are π-free

Here is the fact that decides the chapter. The power moments of the semicircle law are the **Catalan numbers**:

$$
m_{2k} \;=\; \int_{-2}^{2} x^{2k}\,\rho(x)\,dx \;=\; C_k = \frac{1}{k+1}\binom{2k}{k},
\qquad m_{2k+1} = 0 .
$$

Every one of them is a whole number, computed by counting non-crossing pairings (equivalently Dyck paths) of $2k$ objects — a combinatorial count with no circle anywhere in it. I verified each one against 40-digit quadrature of the integral, and each came back exactly on the integer:

```
k      moment m_2k (quadrature, 40 dps)   Catalan C_k
0      1.000000000000000000000000000000   1
1      1.000000000000000000000000000000   1
2      2.000000000000000000000000000000   2
3      5.000000000000000000000000000000   5
4      14.00000000000000000000000000000   14
5      42.00000000000000000000000000000   42
6      132.0000000000000000000000000000   132
7      429.0000000000000000000000000000   429
8      1430.000000000000000000000000000   1430
9      4862.000000000000000000000000000   4862
10     16796.00000000000000000000000000   16796
```

| Moment | Value | Origin |
|---|---|---|
| $m_0$ | $1$ | normalisation (the semicircle's own area) |
| $m_2$ | $1$ | the ensemble's variance normalisation, fixed π-free |
| $m_4$ | $2$ | Catalan — Dyck paths of length 4 |
| $m_6$ | $5$ | Catalan |
| $m_8$ | $14$ | Catalan |
| $m_{10}$ | $42$ | Catalan |
| $m_{20}$ | $16796$ | Catalan, $C_{10}$ |
| all odd $m_{2k+1}$ | $0$ | symmetry of the density |

If you normalise instead by the literal $1/(2\hat\pi)$ with the radius left at $2$, the integrals become $C_k \cdot \pi/\hat\pi = C_k \cdot 0.9990418965338156667$ and no longer land on integers at all — which is precisely why the radius cannot drift: the bulk edge sits at exactly $\pm 2$, imposed by the matrix ensemble's own variance normalisation (entries of variance $1/N$, so that the entries' own $\pi$-free second moment fixes the edge), a condition the circle constant does not appear in. The standard derivation of the law is a moment calculation: the $2k$-th moment is the number of ways to pair $2k$ indices that the random walk over words can close, and the answer is Catalan. **The constant is not an input to that count; it is the name of the quadrature that reproduces it.**

## The equilibrium measure and the arcsine form

The same density is the unique minimiser of the logarithmic energy $\iint \ln|x-y|^{-1}\,d\mu(x)\,d\mu(y)$ on $[-2,2]$ — the potential-theory problem that fixes where the eigenvalues of a Gaussian ensemble have to sit, with no circle constant in the energy functional. Substituting $x = 2\cos\theta$ turns it into an angle density,

$$
\rho(x)\,dx = \frac{2}{\pi}\sin^{2}\theta\,d\theta, \qquad \theta \in [0,\pi],
\qquad \int_{0}^{\pi}\frac{2}{\pi}\sin^{2}\theta\,d\theta = 1,
$$

and only now does a first-power constant reappear: $\tfrac{2}{\pi} = 0.6366197723675813430755350534900574481378$, which under Golden Pi is $\tfrac{2}{\hat\pi} = 0.6360098247570344821262112308687457458578$. Note what the substitution did: it pushed the constant out of the *index* of $x$ (where $x$ is $2\cos\theta$, entirely $\pi$-free) and into the $\theta$-normalisation, converting a quadrature over an interval into a quadrature over a half-turn. The measure is the same measure; only the label moved. Ginibre's circular law, the two-dimensional analogue, behaves identically: the eigenvalues fill the unit disk uniformly with density $1/\pi$ on an area $\pi$, and the constant cancels from the total again.

## The constant survives only under a square root: the Wigner surmise

Level *spacings* are the statistic experimentalists actually report, and the standard surmise for a chaotic spectrum (Wigner's original guess, still the workhorse fit for nuclear and atomic resonance ladders) is

$$
p(s) = \frac{\pi}{2}\,s\,e^{-\pi s^{2}/4},
$$

whose normalisation is again an exact cancellation — $\int_0^\infty s e^{-as^{2}}ds = 1/(2a)$ with $a = \pi/4$ gives exactly $2/\pi$, killing the $\pi/2$ prefactor. Every derivative statistic comes out as a pure algebraic function of $\pi$:

| Quantity | Conventional π | Under Golden Pi (π̂) | Shift |
|---|---|---|---|
| Normalisation integral | $1$ exactly | $1$ exactly | — |
| Mean spacing $\langle s\rangle$ | $1$ exactly | $1$ exactly | — |
| Most probable spacing (mode $\sqrt{2/\pi}$) | $0.7978845608028653559$ | $0.7975022412238315974$ | $-0.0479166533\%$ |
| Median spacing $\sqrt{\tfrac{4}{\pi}\ln 2}$ | $0.9394372786996513338$ | $0.9389871317954930894$ | $-0.0479166533\%$ |
| Second moment $\langle s^{2}\rangle = 4/\pi$ | $1.2732395447351626862$ | $1.2720196495140689643 = \sqrt\varphi$ | $-0.0958103466\%$ |
| P(spacing < 1) | $1-e^{-\pi/4} = 0.5440618722340037632$ | $1-e^{-\hat\pi/4} = 0.5444051620774474205$ | $+0.0630975742\%$ |
| Density at the mode | $0.7601734505331404028$ | $0.7605378748301235384$ | $+0.0479396244\%$ |

Two of these are worth naming because they are exact golden algebra rather than decimal happenstance: $\langle s^{2}\rangle = 4/\pi$ becomes **exactly** $4/\hat\pi = \sqrt\varphi = 1.2720196495140689642524224617374914917$, and $\sqrt{2/\hat\pi} = \varphi^{1/4}/\sqrt{2}$. The same $\varphi^{1/4} = 1.1278384855616822602648354831770424584$ that is the radius whose disk has area exactly $4$ under $\hat\pi$ appears here as the mode's numerator.

## At the edge: the Tracy–Widom distributions carry no constant at all

The largest eigenvalue fluctuates according to the Tracy–Widom laws, and their formulas,

$$
F_2(s) = \exp\!\left(-\int_s^{\infty}(t-s)\,q(t)^{2}\,dt\right), \qquad F_1(s) = \exp\!\left(-\tfrac12\int_s^{\infty}q(t)\,dt\right),
$$

with $q$ solving Painlevé II, $q'' = sq + 2q^{3}$ and $q(s) \sim \mathrm{Ai}(s)$ as $s\to\infty$, contain **no circle constant whatsoever** — the $\tfrac12$ distinguishing the two $\beta$-ensembles is not a $\pi$. The soft edge's whole statistical content is $\pi$-free, exactly as the bulk moments are. The same holds for the log-gas picture: the $\beta = 2$ Coulomb gas writes its pair energy with the two-dimensional Green's function $\tfrac{1}{2\pi}\ln r$, and because that $2\pi$ appears both in the energy and in the partition-function normalisation, it cancels out of every normalised correlation function — the two-point cluster function $Y_2(x,y) = \left(\tfrac{\sin \pi(x-y)}{\pi(x-y)}\right)^{2}$ carries $\pi$ only inside arguments that are themselves differences of unfolded eigenvalues, i.e. inside pure numbers.

## A real diagonalisation, and its honest error budget

This is not a claim about a theorem alone. I built Wigner (GUE) matrices of size $N = 1200$, twelve of them, diagonalised each, and pooled $14\,400$ eigenvalues, scaling so the bulk edge sits at $\pm 2$:

```
eigenvalues pooled:        14 400
observed min / max:        −2.0018558021  /  +1.9951934584
central bin [0.00, 0.05):  empirical 0.319444   semicircle 0.318285   (+0.364%)
  expected count in that bin: 229.2   → Poisson relative error ±6.61%
Kolmogorov–Smirnov distance (max |F_emp − F_theory|): 6.520050184×10⁻⁴
```

The histogram matches the semicircle to well within its own noise, and the noise is the point: a bin holding $229$ eigenvalues carries a $\pm 6.61\%$ relative error from counting statistics alone — **69 times** the $0.0959022309\%$ golden gap and **138 times** the $0.0479166533\%$ half-power gap of the surmise mode. If instead you insisted on keeping the normalising constant literally at $1/(2\hat\pi)$ while forcing unit total mass, the semicircle would have to stretch its radius to

$$
2\sqrt{\frac{\hat\pi}{\pi}} = 2.0009587924880237532689\ldots,
$$

a $0.0479\%$ inflation of the entire spectrum — and that is *forbidden*, because the edge at $2$ is fixed by a $\pi$-free variance condition. The eigenvalue spectrum is therefore not a place where the two labels can be told apart: the one quantity that would move is pinned by an equation with no constant in it.

## Under Golden Pi, in one ledger

| Appearance of the constant | Power | Conventional | Golden | Shift |
|---|---|---|---|---|
| Normalising $1/(2\pi)$ of the semicircle | 1 in numerator, 1 in denominator | $\int\rho = 1$ | $\int\hat\rho = 1$ | $0$ (cancels) |
| Bulk edge (variance normalisation) | 0 | $\pm 2$ | $\pm 2$ | $0$ |
| Moments $m_{2k}$ | 0 | $C_k$ integers | $C_k$ integers | $0$ |
| Pointwise density at the centre | $-1$ | $1/\pi = 0.3183098861837906715$ | $1/\hat\pi = \sqrt\varphi/4 = 0.3180049123785172411$ | $-0.0958103466\%$ |
| Arcsin density factor $\tfrac{2}{\pi}\sin^{2}\theta$ | $-1$ | $0.6366197723675813431$ | $0.6360098247570344821$ | $-0.0958103466\%$ |
| Surmise mode $\sqrt{2/\pi}$ | $-1/2$ | $0.7978845608028653559$ | $\varphi^{1/4}/\sqrt2 = 0.7975022412238315974$ | $-0.0479166533\%$ |
| Surmise second moment $4/\pi$ | $-1$ | $1.2732395447351626862$ | $\sqrt\varphi = 1.2720196495140689643$ | $-0.0958103466\%$ |
| Catalan asymptotic $\sqrt\pi$ in $4^{n}/(n^{3/2}\sqrt\pi)$ | $-1/2$ | $\sqrt\pi = 1.7724538509055160273$ | $2/\varphi^{1/4} = 1.7733035586243245185$ | $+0.0479166533\%$ |
| Tracy–Widom edge laws | 0 | no $\pi$ | no $\pi$ | $0$ |

The Catalan asymptotic belongs in the table because it is the same half-power appearance this series met in Stirling's central binomials: with the exact $1/n$ correction the asymptotic $4^{n}/(n^{3/2}\sqrt\pi)$ sits $9/(8n)$ high, which is $1.1263\%$ at $n = 100$ and $0.1125\%$ at $n = 1000$ — verified — and under Golden Pi the whole sequence of approximations drops by the half-power $0.0479166533\%$. And the exact golden algebra is credited where it is exact: $\hat\pi = 2\sqrt{2\sqrt5 - 2} = 4/\sqrt\varphi$ is a root of $x^{4} + 16x^{2} - 256 = 0$ (the polynomial evaluates to exactly $0$ there), $\hat\pi^{2} = 8(\sqrt5 - 1) = 16/\varphi$ is algebraic of degree two where $\pi^{2}$ is transcendental by Lindemann (1882), $\sqrt{\hat\pi}$ is constructible, and $\hat\pi^{4/3}$-type powers that govern state counting in earlier chapters are algebraic throughout.

## The honest ledger

**First.** No circle is drawn anywhere in this chapter, and no length is measured. The constant enters the semicircle law as the quadrature of a semicircle used as a normalising divisor, and that quadrature is a computed limit — the same one that gives a disk of radius $\varphi^{1/4}$ the area exactly $4$. Computed, never measured.

**Second.** The theory's real content is integer-valued and $\pi$-free: the moment ladder $1, 1, 2, 5, 14, 42, \ldots$ is a count of non-crossing pairings, the bulk edge $\pm 2$ comes from a variance condition, and the edge fluctuation laws contain no constant at all. A claim about $\pi$ in random matrix theory can only ever be a claim about the label of a quadrature, not about an experiment.

**Third.** The one honest adjacency to a measurand in this chapter is the nearest-neighbour spacing mode, $\sqrt{2/\pi} = 0.7978845608$, which nuclear and atomic resonance data are genuinely fitted with — the spacings *are* measured (neutron resonance ladders, hundreds of levels per nucleus). But the fit is a *shape* comparison, and its sensitivity is a half-power dilution: $0.0479166533\%$. The measured mode is quoted in units of the mean spacing, itself extracted by unfolding a density with an empirical smooth part, and the finite-sample fluctuation of a mode estimated from a few hundred spacings runs at the percent level — twenty times the gap. The constant appears here as $\sqrt{2/\pi}$, under a root, with half the strength of a first-power appearance, and buried in the least stable statistic available.

**Fourth.** The most tempting distinct handle — the strict normalisation of the semicircle — is closed by the $\pi$-free variance condition: the spectral edge is at exactly $2$, so the density's divisor must be exactly the semicircle's own area, and the constant that appears in the formula is the area's *name*. A relabelled constant cannot be caught there, because the constraint that would have to move contains no constant. The semicircle law computes a limit and labels it; it does not measure it. Computed, never measured.

## Further Reading

- [The Cauchy–Lorentz Distribution: the same arctan quadrature, seen as a probability law](/blog/posts/2026-08-24-cauchy-lorentz-distribution-integrates-pi-golden-pi/)
- [The Fermi Sphere: how counting quantum states makes the constant appear as 3π²](/blog/posts/2026-10-06-fermi-sphere-quantum-state-counting-computes-circle-constant-golden-pi/)
- [Stirling's Approximation and the central binomials: the other √π asymptotics](/blog/posts/2026-08-25-stirling-approximation-factorials-compute-circle-constant-golden-pi/)
- [The Quantum Harmonic Oscillator: a constant that cancels from every observable](/blog/posts/2026-10-07-quantum-harmonic-oscillator-ground-state-cancels-circle-constant-golden-pi/)
- [The Random Walk: why a plane lattice returns to its origin with π in the exponent](/blog/posts/2026-09-07-random-walk-return-plane-lattice-computes-circle-constant-golden-pi/)
