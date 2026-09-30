---
title: "The Coprime Density: How Counting Pairs of Integers Computes 6/π², and What Golden Pi Changes"
date: 2026-09-30
description: "The probability that two integers chosen at random are coprime is 6/π² = 0.607927101854…, the value of the Euler product ∏(1 − p⁻²) — computed by counting, never measured. This article counts the coprime pairs exactly: with Euler's totient, the number of coprime pairs in an n × n grid is 2Σφ(k) − 1 (Mertens, 1874), which gives 63 at n = 10, 608 383 at n = 1000 and 607 927 104 783 at n = 10⁶ — a density of 0.607927104783 against 6/π² = 0.607927101854, eight digits out of nothing but integer arithmetic. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the same density relabels to 6/π̂² = 3φ/8 = 0.606762745781…, an exact algebraic number in the golden field, because π̂² = 16/φ = 8(√5 − 1); the constant enters squared, so the recurring 0.0959% gap doubles to 0.19190%. Here the two labels are not equally protected by noise: a million sampled pairs separate them by less than 2σ, while the exact count is arithmetic and has no noise floor at all — which is exactly why the honest ledger has to be printed. Includes the π-free cousins (setwise coprimality 1/ζ(k), pairwise coprimality ∏(1 − 3/p² + 2/p³) = 0.2867477…, Euclid's orchard) and the Möbius sum Σμ(n)/n² = 6/π²."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Coprime Density: How Counting Pairs of Integers Computes 6/π², and What Golden Pi Changes

Almost every article in this series has taken a *continuous* object — a series, an integral, a product of factors — and asked where the circle constant sits inside it. This one takes something with no geometry in it at all: pairs of whole numbers. Two integers are either coprime or they are not; there is nothing to measure, no continuum to smear over, and no instrument anywhere in the question. Ask what fraction of the integer grid is coprime and a constant falls out — and that constant is the same one the integrals were converging to.

That makes it the cleanest possible test of a claim this blog keeps making: **the circle constant is computed, and what is computed is 3.14159265358979323846…** — a limit of exact arithmetic, not a reading off a ruler.

## The question, and why a constant appears at all

Write $(a,b)$ for a pair of positive integers and call it coprime when $\gcd(a,b)=1$. Ask: if you pick a pair at random, how likely is it coprime? "At random" needs care — there is no uniform probability on the positive integers — so the statement is made precise with density: let

$$P_N = \frac{\#\{(a,b) : 1 \le a,b \le N,\ \gcd(a,b)=1\}}{N^2}$$

and ask for $\lim_{N\to\infty} P_N$. Dirichlet (1849) settled that the limit exists and equals $6/\pi^2$; the probabilistic phrasing — "the chances are 61 to 39" — was put forward by Ernesto Cesàro in 1881 (*Mathesis* 1, 184) and justified in his following papers. The rigorous route is the one Dirichlet and later Mertens used; the standard reference is Hardy & Wright, *An Introduction to the Theory of Numbers*, Theorem 332.

Where does a circle constant come from in a counting problem about divisibility? From the primes. A prime $p$ divides both entries of a pair with probability $1/p^2$, so it fails to do so with probability $1 - 1/p^2$, and divisibility by distinct primes is independent. Multiplying over all primes:

$$\prod_{p\ \text{prime}}\left(1 - \frac{1}{p^2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2} = 0.607927101854026628663276779\ldots$$

That product is pure arithmetic — every factor is a rational — and its reciprocal is Euler's 1735 sum $\zeta(2)=\sum n^{-2}=\pi^2/6$. **The circle constant enters this problem through the Basel problem and nowhere else.** Nothing in the counting mentions a circle.

The convergence is slow and visibly so, which is why the table below is worth printing rather than asserting:

| cutoff | $\prod_{p\le M}(1-p^{-2})$ | error vs $6/\pi^2$ |
|---|---|---|
| $p \le 10$ | 0.626938775510204081633 | $+1.90\times10^{-2}$ |
| $p \le 100$ | 0.609033725399516660994 | $+1.11\times10^{-3}$ |
| $p \le 1000$ | 0.608004307306125306666 | $+7.72\times10^{-5}$ |
| $p \le 100000$ | 0.607927589563138868522 | $+4.88\times10^{-7}$ |

Four hundred and eighty-eight parts per billion after all primes to a hundred thousand: the primes deliver the constant the way an infinite sum does, one correction at a time.

## The exact count: Mertens' identity

The product argument is the intuitive one. The *exact* one is better, because it is finite arithmetic and can be evaluated. Euler's totient function $\varphi(k)$ counts the integers in $1..k$ that are coprime to $k$, and summing it over $k \le N$ counts the coprime pairs in the grid exactly:

$$\#\{(a,b): 1\le a,b\le N,\ \gcd(a,b)=1\} \;=\; 2\sum_{k=1}^{N}\varphi(k) - 1, \qquad 2\sum_{k\le N}\varphi(k)-1 = \frac{6}{\pi^2}N^2 + O(N\log N),$$

the asymptotic form being Mertens' 1874 result. Walfisz (1963) sharpened the error term to $O(N(\log N)^{2/3}(\log\log N)^{4/3})$, and Montgomery (1987) showed the fluctuations are at least of order $\sqrt{\log\log N}/N$ — so that error term can never simply vanish.

Computed here by totient sieve and exact integer arithmetic, with no floating point in the counts:

| $N$ | coprime pairs $2\sum\varphi(k)-1$ | count / $N^2$ | vs $6/\pi^2$ | vs $3\varphi/8$ |
|---|---|---|---|---|
| 10 | 63 | 0.63 | $+2.21\times10^{-2}$ | $+2.32\times10^{-2}$ |
| 100 | 6 087 | 0.6087 | $+7.73\times10^{-4}$ | $+1.94\times10^{-3}$ |
| 1000 | 608 383 | 0.608383 | $+4.56\times10^{-4}$ | $+1.62\times10^{-3}$ |
| 10 000 | 60 794 971 | 0.60794971 | $+2.26\times10^{-5}$ | $+1.19\times10^{-3}$ |
| 100 000 | 6 079 301 507 | 0.6079301507 | $+3.05\times10^{-6}$ | $+1.17\times10^{-3}$ |
| 1 000 000 | 607 927 104 783 | 0.607927104783 | $+2.93\times10^{-9}$ | $+1.16\times10^{-3}$ |

At one million the count itself is $607\,927\,104\,783$ and $\sum_{k\le10^6}\varphi(k) = 303\,963\,552\,392$, whose doubling minus one returns exactly that integer. The density lands on $0.607927104783$ against $6/\pi^2 = 0.607927101854$: **eight digits, from nothing but counting.** A parenthetical honesty note: at $N=10$ the count already leans the right way but by only five percent of the margin between the two candidate values — small grids do not decide anything, and anyone who reads a constant off a ten-by-ten grid is reading noise.

## The golden relabel: the constant enters squared

Golden Pi is $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693144\ldots$ with $\varphi = (1+\sqrt5)/2$. Its square is *exactly* rational in the golden field:

$$\hat\pi^2 = \frac{16}{\varphi} = 8(\sqrt5 - 1) = 9.888543819998317571\ldots, \qquad \hat\pi^4 + 16\hat\pi^2 - 256 = 0.$$

Because the coprime density depends on the constant **squared**, the golden relabel of $6/\pi^2$ is not a decimal accident but a closed form:

$$\frac{1}{\hat\pi^{2}} = \frac{\varphi}{16} = 0.101127124296868428\ldots, \qquad \frac{6}{\hat\pi^{2}} = \frac{3\varphi}{8} = 0.606762745781210568\ldots$$

and the gap between the two densities is the *square* of the gap between the two constants:

$$\frac{6/\pi^2}{6/\hat\pi^2} = \left(\frac{\hat\pi}{\pi}\right)^{\!2} = 1.001918964341353794\ldots \qquad (0.19189643\%), \qquad \frac{\hat\pi}{\pi}-1 = 0.095902230878\% .$$

So the recurring $0.09590\%$ separation between the two labels appears here doubled to $0.19190\%$, exactly as in Pappus's torus and the reciprocal-power family — a squared constant doubles its own error. The companion quantities follow the same rule: $3/\pi^2 = 0.303963550927013314332\ldots$ becomes $3/\hat\pi^2 = 3\varphi/16 = 0.303381372890605284\ldots$, so the classical coefficient $3/\pi^2$ of the totient-sum asymptotic $\sum_{k\le N}\varphi(k) \approx 3N^2/\pi^2$ becomes $3\varphi/16$ under the relabel. At $N=10^6$:

$$\sum_{k\le10^6}\varphi(k) = 303\,963\,552\,392, \qquad \frac{3N^2}{\pi^2} = 303\,963\,550\,927.013, \qquad \frac{3N^2}{\hat\pi^2} = 303\,381\,372\,890.605 .$$

The counted sum misses the analytic value by $1\,465$; it misses the golden value by $582\,179\,501$. Those two numbers are not in the same universe of size, and no square-root softening rescues the second one — the squared entry into the formula makes it worse, not better.

## The Möbius route, and why counting beats sampling

The same constant has a third independent expression, by Möbius inversion: the indicator of coprimality is $\sum_{d \mid \gcd(a,b)}\mu(d)$, which gives

$$\frac{1}{\zeta(2)} = \sum_{n=1}^{\infty}\frac{\mu(n)}{n^{2}} .$$

Truncated here in exact arithmetic: $0.616258503401$ at $n\le10$, $0.608247717304$ at $n\le100$, $0.607931911854$ at $n\le1000$ ($+4.81\times10^{-6}$), $0.607927096761290$ at $n\le10^5$ ($-5.09\times10^{-9}$) and $0.607927102040462$ at $n\le10^6$ ($+1.86\times10^{-10}$ versus $6/\pi^2$, against $+1.16\times10^{-3}$ versus $3\varphi/8$). Note the alternating sign of the error: this is a genuine limit, not a monotone approach, and its fine structure is precisely what the Riemann-hypothesis connection probes.

Now the part that matters for honest accounting. A Monte Carlo estimate is the obvious way to *look* at this density, and it is a disaster next to the exact count. Sampling a million pairs of random integers below $10^9$ returned $0.607623 \pm 0.000488$ ($-0.62\sigma$ from $6/\pi^2$, $+1.76\sigma$ from $3\varphi/8$); a hundred thousand pairs returned $0.609180 \pm 0.001543$ ($+0.81\sigma$ and $+1.57\sigma$). The gap between the labels is $0.0011643561$, so a simple binomial estimate needs about **175 800 pairs for a one-sigma separation and 703 250 pairs for a two-sigma one** — meaning that at a million samples the two labels are still less than two standard deviations apart. Sampling cannot arbitrate. Counting can, because counting has no error bar: $607\,927\,104\,783$ integer pairs is an exact rational whose deviation from $6/\pi^2$ is $O(\log N/N)$ and already down to $2.9\times10^{-9}$ at $N=10^6$, six orders of magnitude below the $1.16\times10^{-3}$ golden offset. **The integer grid decides this one, and it decides it for the analytic constant.**

## What the constant is *not* doing here

Two of the three cousins of this density are entirely π-free, and printing them is part of keeping the site honest about what is really carrying the constant.

- **Setwise coprimality of $k$ integers** is $1/\zeta(k)$: $1/\zeta(3) = 0.831907372580707469\ldots$ and $1/\zeta(4) = 0.923938402921590167\ldots$. For $k\ge3$ the answer has no circle constant in it at all — it is $\zeta(3)$, $\zeta(4)$, irreducibly.
- **Pairwise coprimality** — a stronger condition, that *every* pair in the set is coprime — has density $\prod_p\left(1 - 3p^{-2} + 2p^{-3}\right) = 0.2867477554715617858\ldots$ for three integers. That product is arithmetic over the primes; no $\pi$ appears in it anywhere, under either label.
- **Euclid's orchard**: coprime pairs are exactly the lattice points visible from the origin, the ones no nearer lattice point shadows. That picture is geometry, and it too is constant-free — visibility is a property of $\gcd$, not of any turn.

So the circle constant is not "everywhere in number theory". It is in exactly one place here: the infinite product over the primes, whose reciprocal is $\zeta(2)$, and whose evaluation is Euler's sum. That is a *computation* — an exact limit — and the claim that it is a measurement would be false on its face, since nothing in this article has units.

## The honest boundary

The ledger, stated plainly:

| statement | status |
|---|---|
| Coprime pairs have density $6/\pi^2$ (Dirichlet 1849; Cesàro 1881) | exact, and the count confirms it to eight digits by $N=10^6$ |
| The density is $6/\hat\pi^2 = 3\varphi/8$ under Golden Pi | exact in the golden field — $\hat\pi^2 = 16/\varphi$ — and $0.19190\%$ away from the counted value |
| $3\varphi/16$ replaces $3/\pi^2$ in $\sum\varphi(k)$ | exact algebra; the counted sum at $10^6$ misses it by $5.8\times10^8$ |
| Pairwise-coprime and $k\ge3$ densities | π-free — nothing for either label to change |
| Monte Carlo can decide between the labels | false: $\sim1.8\sigma$ at a million pairs |
| Exact counting can decide | true in principle, and it does so at $N\ge10^4$ |

What this example *does* show the golden case is the algebraic exactness that the analytic constant does not have: $\hat\pi$ is a root of $x^4 + 16x^2 - 256$ and is constructible from $\varphi$ by square roots, so the golden density $3\varphi/8$ is a closed-form algebraic number rather than a transcendental limit. That is real, and it is credited. What it does not show is that the number of coprime pairs in a grid of integers is $0.606762745781\ldots$: it is $0.607927104783$ at a million, and the difference is arithmetic, not experimental. The circle constant was computed here, on both sides of the ledger — never measured, by either side.

## Further Reading

- [The Basel Problem: When an Infinite Sum Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the 1735 evaluation of $\zeta(2)=\pi^2/6$ that the Euler product in this article leans on.
- [The Riemann Zeta Function at Even Integers: How Euler's Bernoulli-Numbers Formula Computes π to Every Even Power](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — where the constant's power, and therefore the size of the golden gap, is governed.
- [Counting Points in a Circle: The Gauss Circle Problem Computes the Circle Constant](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/) — the same integer-grid counting idea applied to a disk instead of a gcd.
- [Buffon's Needle: How a Tossed Needle Estimates the Circle Constant, and What Golden Pi Changes](/blog/posts/2026-09-10-buffon-needle-geometric-probability-estimates-circle-constant-golden-pi/) — the geometric-probability sibling, and the arithmetic of how much sampling noise hides.
- [Pólya's Random Walk: How Counting the Returns of a Staggering Drunkard on a Plane Lattice Computes the Circle Constant](/blog/posts/2026-09-07-random-walk-return-plane-lattice-computes-circle-constant-golden-pi/) — $1/(\pi n)$ from a lattice count, the same "the integer carries the constant" pattern in a different setting.
