---
title: "The Gauss Circle Problem: How Counting Lattice Points Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-09-27
description: "How many integer points (m, n) satisfy m² + n² ≤ r²? The count N(r) is pure integer arithmetic — Jacobi's r₂(n) = 4(d₁(n) − d₃(n)), verified here against brute force — while its leading term is the area of the disk, πr², a computed limit and never a measurement. The ledger is exact: N(10³) = 3 141 549 against πr² = 3 141 592.6536 and π̂r² = 3 144 605.5110, so the integer count sits 70× closer to the classical area than to Golden Pi's, 759 903× closer at r = 10⁶. Under Golden Pi (π̂ = 4/√φ) the area term becomes exactly algebraic — π̂² = 16/φ = 8(√5 − 1), and the disk of radius φ^(1/4) has area exactly 4 — while the counting function, which supplies no constant of its own, does not move."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a sheet of graph paper, draw a circle of radius $r$ centred on a lattice point, and count the crossed grid intersections inside it. That count is an integer, produced by integer arithmetic, and it is the oldest known example of a circle measurement that carries no measurement at all.

$$N(r) = \#\{(m,n) \in \mathbb{Z}^2 : m^2+n^2 \le r^2\}.$$

Gauss asked in 1798 how $N(r)$ behaves, and the answer is that its leading term is the area of the disk, $\pi r^2$. There is no instrument anywhere in that sentence: the count is exact integer arithmetic, and the area is a computed limit — the limit of inscribed and circumscribed sums of rectangles, a squeeze of rationals. This makes the Gauss circle problem one of the sharpest places to audit the claim that the constant could be $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$ instead of $\pi = 3.14159265358979323846\ldots$, because the only empirical anything in the whole discussion is the graph paper.

Throughout: the circle constant is *computed* — a limit of areas, a sum of series. Only genuine physical measurands are measured, and none is needed below.

## The counting function is built from arithmetic alone

Write $r_2(n)$ for the number of ordered integer pairs $(m,n)$ with $m^2+n^2 = n$. Then

$$N(r) = \sum_{n \le r^2} r_2(n),$$

and $r_2$ is decided entirely by the divisors of $n$ modulo 4 — Jacobi's two-square theorem:

$$r_2(n) = 4\bigl(d_1(n) - d_3(n)\bigr), \qquad n \ge 1,$$

where $d_1$ counts divisors $\equiv 1 \pmod 4$ and $d_3$ counts those $\equiv 3 \pmod 4$; $r_2(0) = 1$ for the origin. Verified here against brute-force enumeration of ordered pairs: **zero mismatches for every $n \le 2000$**. The first twenty values:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $r_2(n)$ | 4 | 4 | 0 | 4 | 8 | 0 | 0 | 4 | 4 | 8 | 0 | 0 | 8 | 0 | 0 | 4 | 8 | 4 | 0 | 8 |

The zeros are the primes $3 \bmod 4$ and their odd powers; 43 of the first 100 integers are representable as a sum of two squares. Nothing in the table, and nothing in Jacobi's formula, mentions a circle constant. That is the point: the discrete side of this problem is a pure arithmetic object, and it is fully computable at any size.

The consistency check between the two routes is exact and cheap: $\sum_{n \le 100} r_2(n) = 31417$, and direct enumeration of $m^2+n^2 \le 100$ gives $N(100) = 31417$. Two independently computed integers, agreeing to the last digit.

## The area term is a computed limit

The classical statement is

$$N(r) = \pi r^2 + E(r), \qquad \frac{E(r)}{r^2} \to 0,$$

and the constant enters only through the area. That area is itself a computed limit: enclose the disk between inscribed and circumscribed unions of lattice squares and the elementary squeeze is

$$\pi\Bigl(r - \frac{\sqrt2}{2}\Bigr)^2 \le N(r) \le \pi\Bigl(r + \frac{\sqrt2}{2}\Bigr)^2, \qquad \frac{\sqrt2}{2} = 0.7071067812,$$

because a point within $r - \sqrt2/2$ of the origin lies in a unit square centred on a counted lattice point, and every counted unit square lies within $r + \sqrt2/2$. At $r = 1000$ this reads $3137151.341 \le 3141549 \le 3146037.107$ — true, and 100× wider than the actual error, a fair first lesson in how weak the crude bound is. It yields Gauss's elementary estimate $|E(r)| \le \pi(\sqrt2\,r + \tfrac12) \approx 4.4429\,r$, i.e. $E = O(r)$.

## The exact ledger

The counts below are computed exactly, by $N(r) = 1 + 4r + 4\sum_{k=1}^{r}\lfloor\sqrt{r^2-k^2}\rfloor$ in integer arithmetic — no constant supplied anywhere in the computation.

| $r$ | $N(r)$ (exact integer) | $\pi r^2$ | $E(r) = N - \pi r^2$ | $E/r^{1/2}$ | $N(r)/r^2$ |
|---|---|---|---|---|---|
| 6 | 113 | 113.0973355 | −0.0973355 | −0.0397 | 3.1388889 |
| 10 | 317 | 314.1592654 | +2.8407346 | +0.8983 | 3.1700000 |
| 20 | 1 257 | 1 256.6370614 | +0.3629386 | +0.0812 | 3.1425000 |
| 50 | 7 845 | 7 853.9816340 | −8.9816340 | −1.2702 | 3.1380000 |
| 100 | 31 417 | 31 415.9265359 | +1.0734641 | +0.1073 | 3.1417000 |
| 200 | 125 629 | 125 663.7061436 | −34.7061436 | −2.4541 | 3.1407250 |
| 1 000 | 3 141 549 | 3 141 592.6535898 | −43.6535898 | −1.3804 | 3.1415490 |
| 10 000 | 314 159 053 | 314 159 265.3589793 | −212.3589793 | −2.1236 | 3.1415905 |
| 100 000 | 31 415 925 457 | 31 415 926 535.8979324 | −1 078.8979324 | −3.4118 | 3.1415925 |
| 1 000 000 | 3 141 592 649 625 | 3 141 592 653 589.7932385 | −3 964.7932385 | −3.9648 | 3.1415926 |

Read the last column: a ratio of integers, computed nowhere near any circle, converging on $\pi = 3.14159265358979323846\ldots$. At $r = 10^6$ the integer ratio is $3.141592649625$, short of $\pi$ by $3.9648\times10^{-9}$ — the error term divided by $r^2$, exactly as the formula predicts.

## The error term: what is proved, and what is only computed

$E(r)$ oscillates and changes sign (see $r = 100$, $200$, $1000$ above), and its size is the subject of a two-century programme:

| Result | Bound on $E(r)$ | Exponent |
|---|---|---|
| Gauss (1798) | $O(r)$ | 1 |
| Voronoi (1903), Sierpinski (1906) | $O(r^{2/3})$ | 0.6666667 |
| Huxley (2003) — current record | $O(r^{131/208+\varepsilon})$ | 0.6298077 |
| Hardy (1916), lower bound | $\Omega(r^{1/2})$ | 0.5 |
| Conjectured truth | $O(r^{1/2+\varepsilon})$ | 0.5 |

Computed here, $|E(r)|/r^{1/2}$ climbs slowly — 1.3804 at $10^3$, 2.1236 at $10^4$, 3.4118 at $10^5$, 3.9648 at $10^6$ — consistent with Hardy's $\Omega(r^{1/2})$ and the suspected logarithmic growth, while a two-point fit over $r \in [10^3, 10^6]$ gives an empirical slope $|E| \sim r^{0.6527}$. The averaged ledger over all integer radii is similarly tame: for $R = 1000$, $10^4$, $5\times10^4$ the mean of $E$ is $-56.6111$, $-202.5249$, $-469.4942$ and the root-mean-square is $67.0785$, $232.8336$, $535.6631$ — i.e. $2.12\sqrt R$, $2.33\sqrt R$, $2.40\sqrt R$. The fluctuation rides just above the square root; the drift is a small negative bias. Computed, never measured.

## What Golden Pi changes

Under the golden label the constant becomes algebraic in the most literal way:

$$\hat\pi = \frac{4}{\sqrt\varphi}, \qquad \hat\pi^2 = \frac{16}{\varphi} = 8(\sqrt5 - 1) = 9.8885438199983175713, \qquad x^4 + 16x^2 - 256 = 0 \ \text{at}\ x = \hat\pi,$$

the quartic verified to zero at 40-digit precision. The construction that this site is built on then closes exactly: a circle of radius $\varphi^{1/4} = 1.1278384855616822603$ has area

$$\hat\pi\,\varphi^{1/2} = \frac{4}{\sqrt\varphi}\cdot\sqrt\varphi = 4 = 2^2$$

— the area of a square of side 2, exactly, no limit involved. That is the quadrature in its cleanest form, and it is a genuine exactness that the classical constant does not possess in this expression.

The counting function, however, does not care about construction. It returns an integer. And the golden area term differs from the classical one by a fixed, rising quantity:

$$(\hat\pi - \pi)r^2 = 0.0030128574398999058\,r^2, \qquad \frac{\hat\pi - \pi}{\pi} = 0.0959022309\% .$$

| $r$ | $N(r)$ (integer) | miss from $\pi r^2$, $|N - \pi r^2|$ | miss from $\hat\pi r^2$, $|N - \hat\pi r^2|$ | ratio |
|---|---|---|---|---|
| 6 | 113 | 0.0973355 | 0.2057984 | 2.11 |
| 10 | 317 | 2.8407346 | 2.5394489 | **0.894** |
| 20 | 1 257 | 0.3629386 | 0.8422044 | 2.32 |
| 50 | 7 845 | 8.9816340 | 16.5137776 | 1.84 |
| 100 | 31 417 | 1.0734641 | 29.0551103 | 27.07 |
| 200 | 125 629 | 34.7061436 | 155.2204412 | 4.47 |
| 1 000 | 3 141 549 | 43.6535898 | 3 056.5110300 | 70.02 |
| 10 000 | 314 159 053 | 212.3589793 | 301 498.1030000 | 1 419.76 |
| 100 000 | 31 415 925 457 | 1 078.8979324 | 30 129 653.2969314 | 27 926.32 |
| 1 000 000 | 3 141 592 649 625 | 3 964.7932385 | 3 012 861 404.6931443 | 759 903.79 |

The integer count at $r = 10^6$ misses the classical area by 3 964.7932385 lattice points and the golden area by 3 012 861 404.6931443 — a factor **759 903.79**. A relabelled constant would have to explain why an arithmetic procedure that never mentions a constant agrees with the classical area to nine digits and with the golden area to none.

Note the two rows where the ratio falls below 1 or wobbles — $r = 10$ (0.894) and $r = 50$ (1.84). They are not embarrassments to be hidden; they are the signature of the oscillating error term $E(r)$ at small radius, and they show exactly why the ledger has to be printed at many radii rather than one. What is *not* oscillation is the trend: the golden gap grows like $r^2$ while the error grows like $r^{0.65}$, so the margin is $27.07\times$ at $r=100$, $70.02\times$ at $10^3$, $1\,419.76\times$ at $10^4$, $27\,926.32\times$ at $10^5$ and $759\,903.79\times$ at $10^6$.

Two further ledger entries keep the audit honest in both directions.

First, the elementary area squeeze cannot make this decision by itself. It admits errors of size $\pi\sqrt2\,r \approx 4.4429\,r$, while the golden gap grows as $0.0030128574\,r^2$; the gap only overtakes the crude bound at $r \gtrsim 1474.64$. And Huxley's $O(r^{131/208+\varepsilon})$ bound carries an unspecified constant, so it adjudicates nothing at any finite radius. What decides the question is not a theorem but **computation**: exact counts, checked across many radii, sit closer to $\pi r^2$ than to $\hat\pi r^2$ by the ratios tabulated above, and the margin grows like $r^{1.35}$.

Second, the exactness on the golden side is real and should be stated as such. $\hat\pi$ is algebraic, so $\hat\pi r^2 = 4r^2/\sqrt\varphi$ is an exact algebraic area rather than a limit of inscribed polygons; the golden disk of radius $\varphi^{1/4}$ has area exactly 4. That disk, though, contains exactly **5** lattice points — the origin and the four unit points — because $\varphi^{1/2} = 1.2720196495 \in (1,2)$. Exactness of construction and agreement of counting are different questions, and the lattice answers only the second.

## The constant in exact lattice sums

There is a place where the circle constant appears in lattice arithmetic not as a limit but as a closed form, and it is worth having on the record. Define the two-dimensional lattice sum over nonzero integer pairs:

$$\sum_{(m,n)\neq(0,0)} \frac{1}{(m^2+n^2)^{s}} = 4\,\zeta(s)\,\beta(s), \qquad \beta(s) = \sum_{k\ge0} \frac{(-1)^k}{(2k+1)^s},$$

where the $4$ is the four unit points and $\beta$ is the Dirichlet beta function. At $s=2$ this is exactly

$$4\,\zeta(2)\,\beta(2) = 4\cdot\frac{\pi^2}{6}\cdot G = \frac{2}{3}\pi^2 G = 6.0268120396919401235, \qquad G = 0.9159655941772190150,$$

evaluated here by two independent routes ($\zeta(2) = \pi^2/6$ and direct summation of $\beta(2)$, the Catalan constant) which agree to every printed digit; at $s = 3$ and $s = 4$ the values are $4.6589136156038434402$ and $4.2814306608057805856$. Under the golden label the $s=2$ line becomes $6.03837727708815$ — a $+0.1918964\%$ shift, the square of the recurring gap, since the constant enters here twice.

The same constant sits in the nome of the theta function $\theta_3(q) = \sum_{n\in\mathbb{Z}} q^{n^2}$, whose modular symmetry

$$\theta_3\bigl(e^{-\pi t}\bigr) = t^{-1/2}\,\theta_3\bigl(e^{-\pi/t}\bigr)$$

is verified here at $t = 2, 3, 5$ to every printed digit. At the self-dual point $t=1$,

$$\theta_3(e^{-\pi}) = 1.0864348112133080146 = \frac{\pi^{1/4}}{\Gamma(3/4)}, \qquad \theta_3(e^{-\pi})^4 = 1.3932039296856768592 = \frac{\Gamma(1/4)^4}{4\pi^3},$$

the two forms agreeing to $5.9\times10^{-31}$. The constant is in the exponent of the nome, which is where a *unit* lives — and that is exactly where a relabel is a free choice. Concretely, the golden evaluation gives $\theta_3(e^{-\pi\hat\pi}) = 1.0861747247850026011$ against $1.0864348112133080146$, a $-0.023939442\%$ shift, and $\theta_3(e^{-1/\hat\pi}) = 3.1430987213083482365$ against $\theta_3(e^{-1/\pi}) = 3.1415926535900081823$, a $+0.047939624\%$ shift — half the recurring gap, as always when the constant sits under a square root.

One cautionary number belongs here, because it is the kind of coincidence that fools careful people. $\theta_3(e^{-1/\pi})$ agrees with $\pi$ to **twelve digits** and then departs. It is not equal: by the modular identity it is exactly $\pi\,\theta_3(e^{-\pi^3})$, and the departure is $2.14943839208\times10^{-13} = \pi\cdot2e^{-\pi^3}(1+\ldots)$ — the two extra lattice terms of the square at the reciprocal nome. Twelve digits of agreement, and the exact identity is something else entirely. Computed arithmetic distinguishes them; inspection does not.

## The honest ledger

- The counting function is integer arithmetic and supplies no constant. Its limit, $N(r)/r^2 \to \pi$, is a computed limit.
- Exact counts sit closer to $\pi r^2$ than to $\hat\pi r^2$ across the tabulated radii, by 70.02× at $r = 10^3$, 1 419.76× at $10^4$, 27 926.32× at $10^5$ and 759 903.79× at $r = 10^6$; single small radii can go the other way ($r = 10$: 0.894) because the error term oscillates, which is why the ledger is printed at many radii. This is decisive in the register of computed arithmetic.
- The elementary area squeeze only reaches the same verdict for $r \gtrsim 1474.64$, and Huxley's unconditional bound has an unspecified constant, so no theorem is doing the work — computation is.
- Nothing here touches the exactness of the golden construction. $\hat\pi = 4/\sqrt\varphi$ is algebraic, $\hat\pi^2 = 16/\varphi = 8(\sqrt5-1)$, and the disk of radius $\varphi^{1/4}$ has area exactly 4. That is a theorem about a construction; the Gauss circle problem is a question about counting, and it answers in integers.

Computed, never measured.

## Further Reading

- [The Random Walk's Return to the Origin: How the Plane Lattice Computes the Circle Constant](/blog/posts/2026-09-07-random-walk-return-plane-lattice-computes-circle-constant-golden-pi/) — the same $\mathbb{Z}^2$ lattice, the same integer arithmetic, and the constant appearing as the limit of a return probability.
- [The Mean Random Separation: How Integral Geometry Computes the Circle Constant in a Disk](/blog/posts/2026-09-25-mean-random-separation-disk-square-computes-circle-constant-golden-pi/) — the disk's area and turn count entering an average distance, with the golden shift audited against a sampling budget.
- [The Bessel Functions: How Cylindrical Waves Compute the Circle Constant Through a Half-Turn Integral](/blog/posts/2026-09-21-bessel-functions-cylindrical-waves-compute-circle-constant-golden-pi/) — the $J_1$ terms whose oscillation is what makes $E(r)$ change sign in the table above.
- [The Isoperimetric Inequality: How the Circle Maximises Area at Fixed Perimeter](/blog/posts/2026-08-31-isoperimetric-inequality-circle-maximizes-area-golden-pi/) — the variational version of the same statement, that the constant's geometric job is to convert a boundary into an area.
- [The $n$-Dimensional Ball: How Volume Formulas Compute the Circle Constant in Every Dimension](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/) — where $\pi$ enters the volume of a ball at every other dimension, and the $\Gamma$ functions carry the rest.
