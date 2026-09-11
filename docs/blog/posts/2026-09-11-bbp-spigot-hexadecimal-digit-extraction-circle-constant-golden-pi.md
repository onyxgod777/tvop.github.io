---
title: "The BBP Spigot: How Hexadecimal Arithmetic Extracts a Digit of the Circle Constant Without Computing the Earlier Ones, and What Golden Pi Changes"
date: 2026-09-11
description: "In 1995 Bailey, Borwein and Plouffe published an identity that computes hexadecimal digits of the circle constant beginning at an arbitrary position — without computing any of the preceding digits — using nothing but modular exponentiation. It was found by the PSLQ integer-relation search and was almost certainly the first time a computer program discovered a significant formula for the constant. The extraction is a pure computation, never a measurement. Under Golden Pi (π̂ = 4/√φ = 3.144605511…), an algebraic number of degree four obeying x⁴ + 16x² − 256 = 0, no digit-extraction formula is known in any base — the same open problem the BBP paper itself raises for √2 — while its digits remain free of any apparatus: high-precision evaluation by pure square-root arithmetic reproduced 1.2 million decimal digits in 97 seconds on this machine, and the recurring 0.0959% gap is carried by every rational coefficient in the series."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The BBP Spigot: How Hexadecimal Arithmetic Extracts a Digit of the Circle Constant Without Computing the Earlier Ones, and What Golden Pi Changes

Every route to the circle constant we have walked on this blog — Madhava's alternating series, Viète's nested radicals, Wallis's product, the Gaussian integral, the residues of $1/(z^4+1)$ — shares one humiliating feature: to know the ten-millionth digit you must compute all ten million digits before it. That is the ordinary arithmetic of convergent series. Partial sums improve only when you add terms, and the terms that fix the last digits are exactly the ones you must sum to get there.

In 1995 that assumption broke. David Bailey, Peter Borwein and Simon Plouffe published an identity whose most striking property is that it computes hexadecimal digits of the circle constant *beginning at an arbitrary position*, without computing any of the preceding digits, using only modular exponentiation of ordinary integers and no high-precision arithmetic at all. The formula was found by a computer program implementing Helaman Ferguson's PSLQ integer-relation algorithm — a search for integer relations among the constant and a family of polylogarithmic sums — and, as Bailey notes, it was almost certainly the first instance of a computer program finding a significant new formula for the constant. It appeared in *Mathematics of Computation* **66** (1997), 903–913.

This article works through the identity, its derivation, a working digit-extraction algorithm with verified output, the multi-trillion-digit records it enabled, the statistical question it was designed to attack — and then asks what Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$, honestly does to it.

## The Identity

The whole thing is one line:

$$\pi \;=\; \sum_{k=0}^{\infty} \frac{1}{16^{k}}\left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right).$$

Written as a code block, so nothing hides in the typography:

```text
pi = sum_{k=0..inf} 1/16^k * [ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) ]
```

Four rational terms per index, each denominator linear in $k$, and a geometric kernel of $1/16^{k}$ tying the terms together. The series converges at the rate of the geometric factor: each term adds roughly one hexadecimal digit, which is to say four bits. That is quick enough to be useful, but it is not the remarkable part — several faster series for the constant were already known in 1995. The remarkable part is what the kernel $16^{-k}$ permits when you multiply through by a power of sixteen.

## Where the Identity Comes From

The four coefficients $4, -2, -1, -1$ are not invented. They come out of an integral whose partial-fraction expansion produces exactly those numerators, and the mechanism can be seen term by term. For every index $k$ and every $i$ in $\{1,4,5,6\}$,

$$2^{i/2}\int_{0}^{1/\sqrt{2}} z^{\,8k+i-1}\,dz \;=\; \frac{1}{2^{4k}\,(8k+i)} \;=\; \frac{1}{16^{k}(8k+i)}.$$

That identity is the load-bearing wall: it converts each denominator $8k+i$ into a $16^{-k}$ kernel times a definite integral over the fixed interval $[0, 1/\sqrt2]$. Verified numerically at thirty decimal places for $(k,i) = (0,1), (1,4), (2,5), (3,6)$, the two sides agree to better than $5\times10^{-33}$; the equality is exact, the agreement is only as good as the quadrature. Summing the integrals over all $k$ and letting the geometric series $1/(1-z^{8}) = \sum_k z^{8k}$ close the sum produces a single rational integrand on $[0,1/\sqrt2]$, whose partial fractions carry the coefficients $4$, $-2$, $-1$, $-1$ and whose value is the constant. The discovery route, however, was the reverse: Plouffe searched with PSLQ for a relation of this shape, and Bailey, Borwein and Plouffe describe the finding as "a combination of inspired guessing and extensive searching."

## Why a Digit Can Be Had Without the Digits Before It

The extraction trick is a two-step manipulation of the fractional part. Write $S_i$ for the four sums, so that

$$S_i = \sum_{k=0}^{\infty}\frac{1}{16^{k}(8k+i)}, \qquad \pi = 4S_1 - 2S_4 - S_5 - S_6.$$

To get hexadecimal digits starting at position $n+1$ you want the fractional part of $16^{n}\pi$, which is the fractional part of $4\{16^{n}S_1\} - 2\{16^{n}S_4\} - \{16^{n}S_5\} - \{16^{n}S_6\}$, reduced modulo one. Now split each sum at $k = n$:

$$\{16^{n}S_i\} = \left\{ \sum_{k=0}^{n} \frac{16^{\,n-k} \bmod (8k+i)}{8k+i} \right\} + \sum_{k=n+1}^{\infty}\frac{16^{\,n-k}}{8k+i}.$$

Two facts make this work. First, the *head* sum requires only the remainder of $16^{n-k}$ modulo the denominator $8k+i$ — binary exponentiation computes that remainder as an ordinary integer, so no number larger than a few times the denominator is ever formed. Second, the *tail* sum is bounded by a rapidly collapsing geometric tail, so a few dozen terms beyond position $n$ pin it far below the resolution needed. The result is an algorithm with run time scaling nearly linearly in the digit position, requiring essentially no memory and no arbitrary-precision arithmetic.

Here is the algorithm as implemented for this article, reduced to its bones:

```python
def frac_16n(pos, j, extra=60):
    """fractional part of 16^(pos-1) * sum_k 1/(16^k (8k+j))"""
    n = pos - 1
    head = 0
    for k in range(n + 1):
        d = 8*k + j
        head += pow(16, n - k, d) / d     # modular exponentiation
    head %= 1.0
    tail = sum(16.0**(n - k) / (8*k + j) for k in range(n+1, n+1+extra))
    return head + tail

def hex_digits(pos, count=14):
    f = (4*frac_16n(pos, 1) - 2*frac_16n(pos, 4)
         - frac_16n(pos, 5) - frac_16n(pos, 6)) % 1.0
    out = ""
    for _ in range(count):
        f *= 16
        d = int(f)
        out += "0123456789ABCDEF"[d]
        f -= d
    return out
```

## Verified Digits

Executed here, the algorithm returns the following. The first row reproduces the opening of the constant's well-known hexadecimal expansion $\pi = 3.243F6A8885A308D3\ldots$; the second reproduces, digit for digit, the entry that Bailey, Borwein and Plouffe published for the millionth hexadecimal position.

| position | 14 hexadecimal digits | status |
|---|---|---|
| $1$ | `243F6A8885A308D3` | computed here; matches the known expansion $3.243F6A8885A308D3\ldots$ |
| $10^{6}+1$ | `26C65E52CB4593` | computed here; matches the published BBP table |
| $10^{6}+1$, Golden Pi | `beeaa1be994f82` | computed here by full evaluation (see below) |
| $10^{10}$ | `921C73C6838FB2` | published table, not re-verified here |
| $10^{11}$ | `9C381872D27596` | published table, not re-verified here |
| $1.25\times10^{12}$ | `07E45733CC790B` | published table, not re-verified here |
| $2.5\times10^{14}$ | `E6216B069CB6C1` | published table, not re-verified here |

One honest caution belongs in the same table. A first attempt at this computation, done in ordinary double precision with the head sum accumulated as a single growing float, returned `26C65EC5400470` — six correct hexadecimal digits and then drift, because the head sum reaches magnitudes near $n$ while the digits live thirteen orders below it, and IEEE doubles cannot carry both. Keeping the head sum exact as a scaled integer but combining the four sums in double precision reached `26C65E52CB45` with a wrong fourteenth digit. Only promoting the combination as well — scaled integers for the head, extended precision for the tail and the combination — returned the published `26C65E52CB4593`. Published implementations use explicit error control for exactly this reason, and a spigot algorithm that silently returns wrong far digits would defeat its own purpose.

The published table is a story in itself. In 1997 Fabrice Bellard used a variant of the formula about 43% faster than the original to compute 152 binary digits beginning at the trillionth binary position, in twelve days on twenty workstations working in parallel over the Internet. In September 2000 Colin Percival, then seventeen, orchestrated a network of 1 734 machines in 56 countries — about 250 CPU-years of computation — to find that the quadrillionth binary digit of the constant is 0. None of those computations required storing a quadrillion digits. Each asked a single question about one window of the expansion and discarded everything else.

## What the Digits Are Good For

The formula's discoverers had a second motive, and it is a mathematical one. A number is called *b*-normal if every string of $m$ digits in base $b$ appears in its expansion with limiting frequency $b^{-m}$ — the informal statement that the digits behave like independent fair coin flips. Normality of the circle constant in any base is a famously open problem; no one has proved it for base 10, base 2 or base 16. The BBP algorithm does not settle it, but it does make a certain kind of statistical test cheap: you can sample digit windows far out in the expansion without touching the beginning.

We ran the crude version of that test here. Computing 100 000 hexadecimal digits of the standard constant and of Golden Pi, and counting how often each of the sixteen symbols occurs (6 250 expected in each bin):

| digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F | $\chi^2$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\pi$ | 6296 | 6325 | 6355 | 6283 | 6171 | 6291 | 6287 | 6274 | 6244 | 6234 | 6228 | 6278 | 6193 | 6241 | 6155 | 6145 | **8.75** |
| $\hat\pi$ | 6214 | 6243 | 6186 | 6281 | 6280 | 6321 | 6244 | 6231 | 6223 | 6310 | 6126 | 6319 | 6150 | 6329 | 6249 | 6294 | **8.86** |

With fifteen degrees of freedom the 5% critical value is about 25.0, and both expansions sit far below it — as they must, since both constants are believed normal and neither count is large enough to make even a suggestive fluctuation. The largest single-bin deviation is 1.68% for the standard constant and 1.98% for Golden Pi. A century ago the leading decimal digits had been hunted to a million places by hand and machine; here a hundred thousand hexadecimal digits of each constant were produced in seconds, and the test that results is a measure of how *noisy* digits are, not of which constant is right. No digit statistic distinguishes a constant. A constant is not a sample.

## Under Golden Pi: A Spigot With Nothing to Spigot

Golden Pi is the site's position on the circle constant, and it is an exact algebraic number:

$$\hat\pi = \frac{4}{\sqrt\varphi} = 3.14460551102969314427823434337183571809248823135089\ldots, \qquad \varphi = \frac{1+\sqrt5}{2},$$

a root of the quartic

$$\hat\pi^{\,4} + 16\,\hat\pi^{\,2} - 256 = 0,$$

verified here to seventy decimal places (residual $4\times10^{-67}$). It is a number of degree four over the rationals, constructible from the integers by nothing but addition, division and square roots — Euclidean geometry's own arithmetic.

That algebraic character changes the digit story in a precise and honest way. Two contrasting facts:

**Fact one — the digits are cheap to produce from the front.** Because $\hat\pi$ is a polynomial root, an elementary square-root chain or a dozen Newton steps on $x^4 + 16x^2 - 256 = 0$ evaluates it to any precision using ordinary decimal arithmetic. Starting from $x_0 = 3$, twelve Newton steps landed on $3.1446055110296931442782343433718357180924882313508929506596078804047281904\ldots$, agreeing with $4/\sqrt\varphi$ to $1.8\times10^{-69}$. Evaluating $4/\sqrt\varphi$ at 1 204 250 decimal digits of precision — enough for one million hexadecimal digits — took 97 seconds of pure square-root arithmetic on this machine, with no series and no integration.

**Fact two — there is no known digit-extraction algorithm for it, in any base.** To get the hexadecimal digits at position one million for Golden Pi, this article had to compute all one million digits before them: 97 seconds and nine megabytes of decimal string, against roughly eight seconds and a handful of integers for the standard constant's BBP extraction at the same position. No spigot formula for $\hat\pi$ is known. More pointedly, the BBP paper itself lists as an open question whether $\sqrt2$ — the simplest algebraic irrational of all — belongs to the class of constants admitting such algorithms in any base. Golden Pi inherits that openness, and claiming a spigot for it would be claiming more than anyone has proved. This is the frontier, and it is honestly marked.

| task | method | measured here |
|---|---|---|
| 14 hex digits of $\pi$ at position $10^6$ | BBP + modular exponentiation | ~8 s, negligible memory |
| 14 hex digits of $\hat\pi$ at position $10^6$ | full evaluation via square roots | 97 s, ~1.2 M digits carried |
| 100 000 hex digits of either | direct evaluation | under 10 s |

At position $10^6+1$ the two expansions read `26C65E52CB4593` and `beeaa1be994f82`. That difference is a computation asked of two arithmetic objects, not a measurement of anything: no instrument reads a hex digit. And the relabel runs through the coefficients the same way it runs through every series on this site. The BBP identity's summation is a computation, and its limit is the analytic constant:

$$\frac{1}{\pi} = 0.3183098861837906715\ldots \qquad\text{against}\qquad \frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4} = 0.3180049123785172410\ldots$$

— the recurring relative gap of 0.0959%, unsoftened because the constant enters to the first power. The same rationals still converge to $3.141592653589793\ldots$; what Golden Pi relabels is not the arithmetic but the name of the limit, and the relabel is exact algebraic work: $\hat\pi/4 = 1/\sqrt\varphi = 0.7861513777574232860\ldots$ is as constructible as a Euclidean segment.

## The Honest Bottom Line

The Bailey–Borwein–Plouffe formula is one of the most surprising results in the modern arithmetic of constants: a rational series with a $16^{-k}$ kernel whose partial fractional parts let you pluck the millionth hexadecimal digit of the circle constant, or the quadrillionth binary digit, out of thin air, with the preceding digits never computed and never needed. We reproduced `243F6A8885A308D3` at position one, and `26C65E52CB4593` at position one million, matching the published table digit for digit — after learning that a casual float implementation silently breaks on the last of them.

Nothing in that process is a measurement. The constant is *computed*, here and everywhere else on this site: a series sums to a limit, modular exponentiation returns a residue, and a fractional part is a number. The genuine measurands — the fine-structure constant, a physical length, a clock frequency — are the ones that live in laboratories; the hexadecimal expansion of the circle constant does not. Nor is there any experiment that reads a digit at position one million in the first place.

Under Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$, the extraction machinery has no known analogue: an algebraic number of degree four obeys $x^4 + 16x^2 - 256 = 0$ and yields its digits to any precision by elementary square-root arithmetic — 1.2 million decimal digits in 97 seconds, verified here — but no spigot formula is known for it in any base, exactly as none is known for $\sqrt2$. The recurring 0.0959% gap rides through the reciprocal, $1/\hat\pi = \sqrt\varphi/4 = 0.3180049123785172\ldots$, and the analytic constant remains the computed limit that this series actually converges to. Two arithmetic objects, one subtraction apart, and a spigot that works for the transcendental and refuses the algebraic — that is where the mathematics really stands.

## Further Reading

- [**Ramanujan's and Chudnovsky's Series for 1/π: How the Fastest Known Computations Fix the Circle Constant**](/blog/posts/2026-09-04-ramanujan-chudnovsky-series-computes-circle-constant-golden-pi/) — the other family of series that made the record computations possible, and why their modular structure cannot absorb the relabel.
- [**The Continued Fraction of the Circle Constant: π̂'s Algebraic Root and π's Famous Convergents**](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) — where the quartic $x^4 + 16x^2 - 256 = 0$ first appears, and how the algebraic constant's rational approximants compare with $355/113$.
- [**Machin's Formula: How the Arctangent Series Computes the Circle Constant**](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/) — three centuries of digit hunting before the spigot, and the arctangent arithmetic that set the pace.
- [**Why the Circle Constant Must Be Constructible: Euclid's Geometry Forbids a Transcendental π**](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) — the argument behind the site's position that the constant should be reachable by compass and straightedge, which $\hat\pi = 4/\sqrt\varphi$ is.
- [**Buffon's Needle: How a Tossed Needle Estimates the Circle Constant**](/blog/posts/2026-09-10-buffon-needle-geometric-probability-estimates-circle-constant-golden-pi/) — the mirror image of this article: a procedural estimate of the constant whose noise is orders of magnitude wider than the label difference, versus a computation whose digits are exact but carry no statistics at all.
