---
title: "The Hardy–Ramanujan Partition Asymptotic: How the Circle Method Counts Integer Partitions and Computes the Circle Constant in an Exponent — and What Golden Pi Changes"
date: 2026-10-09
description: "Counting the partitions of an integer is pure integer arithmetic with no circle in sight, yet the asymptotic count p(n) ~ exp(π√(2n/3))/(4n√3) carries the circle constant in an exponent — and it gets there by integrating around the unit circle in the complex plane, the original 'circle method'. All of it is computed, never measured. Under Golden Pi the constant sits in the exponent, so the recurring 0.0959% gap is amplified by the exponent itself: +2.49% at n = 100, +8.09% at n = 1000, and a factor of ~11.7 at n = 10⁶, while the integer count does not move a digit."
---

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

## The count that has nothing to do with circles

Ask how many ways an integer can be written as a sum of positive integers, order ignored. The answer, the *partition number* $p(n)$, is about as circle-free a quantity as mathematics produces: it is a count of integer multisets, built by additions, and every one of its values is a whole number.

$$p(0)=1,\quad p(1)=1,\quad p(2)=2,\quad p(3)=3,\quad p(4)=5,\quad p(5)=7,\quad p(6)=11,\quad \ldots$$

So it is a genuine surprise that the large-$n$ behaviour of this count — its analytic asymptotic — contains the circle constant, and contains it inside an exponent, where its value is amplified rather than merely carried. The number $p(n)$ itself never touches a circle. The *formula that describes how it grows* is built by integrating around a circle, and that is where the circle constant enters. This is the "circle method" of Hardy and Ramanujan, and the whole story is a computation: the count is exact integer arithmetic, and the asymptotic is an evaluated limit, not a reading from any instrument.

## Euler's product and the generating function

The counting function has a generating function that is an infinite product, found by Euler in the 1740s:

$$
\sum_{n\ge 0} p(n)\,q^{n} \;=\; \prod_{k\ge 1} \frac{1}{1-q^{k}}, \qquad |q|<1 .
$$

The same series is the reciprocal of the Euler function, and the same identity also yields Euler's pentagonal number theorem — the fastest exact way to compute $p(n)$ by hand:

$$
\prod_{k\ge 1}(1-q^{k}) \;=\; \sum_{m=-\infty}^{\infty} (-1)^{m} q^{\,m(3m-1)/2},
$$

so that

$$
p(n) \;=\; \sum_{m\ne 0} (-1)^{m-1}\, p\!\left(n - \tfrac{m(3m-1)}{2}\right),
$$

over those $m$ for which the argument is non-negative. The pentagonal numbers are $0,1,2,5,7,12,15,22,26,\ldots$ (from $m=0,\pm1,\pm2,\pm3,\pm4$). Nothing in this recurrence involves the circle constant — it is a signed sum of earlier integers, and it is how the exact rows printed later in this article were produced. The circle constant has to come from somewhere else, and it does: from analysis.

## The circle method: a contour integral around the unit circle

Cauchy's coefficient formula turns the generating function into a count by an integral on a circle of radius $r<1$ centred at the origin:

$$
p(n) \;=\; \frac{1}{2\pi i}\oint_{|q|=r} \frac{F(q)}{q^{\,n+1}}\,dq,
\qquad F(q)=\prod_{k\ge 1}\frac{1}{1-q^{k}} .
$$

This is the literal origin of the name. The count is obtained by integrating once around a closed circle in the complex plane, and the factor $\tfrac{1}{2\pi i}$ is the normalisation of a full turn — the arclength of the unit circle, $2\pi$, sitting in the computation as a division. It is a computed constant (the circumference limit of the circle), and here it is not merely present: it is *structural*, because the contour itself is a circle and the move to exponential variables $q = e^{-t}$ turns the arc of that circle into the real line of the saddle-point integral.

Write $q=e^{-t}$ and let $t\to 0^{+}$ along the circle of radius $e^{-t}$; the integrand's logarithm is

$$
\Phi(t) \;=\; \ln F(e^{-t}) + n t ,
$$

and the count is recovered by the saddle-point (Laplace) method as $\ln p(n) \sim \max_t \Phi(t)$. The key input is the modular behaviour of $F$ near the unit circle — for $t>0$ small,

$$
\ln F(e^{-t}) \;=\; \frac{\pi^{2}}{6t} + O(\log t),
$$

because $\sum_{k\ge1} k^{-1}e^{-kt}$ sums to the harmonic behaviour $\;-1/(e^{-t}-1)$ … $-1/t$ — i.e. the elementary limit $\ln F = \sum_{k\ge1}-\ln(1-e^{-kt}) = \sum_{m\ge1}\frac{1}{m}\frac{1}{e^{mt}-1}\to \frac{\pi^2}{6t}$. The constant $\pi^2/6$ is the Basel sum, a *computed* limit, and it arrives here through the very same $\zeta(2)$ that has been the archetype of a computed — never measured — circle-constant identity. So the exponent is powered by the evaluated Basel integral, and the circle enters twice over: once as the contour, once as the Basel value.

## The saddle point and the Hardy–Ramanujan asymptotic

Maximising $\Phi(t) = \pi^2/(6t) + nt$ gives the saddle at

$$
t_{0} \;=\; \frac{\pi}{\sqrt{6n}}, \qquad
\Phi(t_{0}) \;=\; \pi\sqrt{\frac{2n}{3}} .
$$

Feeding that exponent back into the coefficient formula and keeping the Gaussian fluctuation of the saddle yields the Hardy–Ramanujan asymptotic (1918):

$$
\boxed{\,p(n)\;\sim\;\frac{1}{4n\sqrt{3}}\;\exp\!\left(\pi\sqrt{\frac{2n}{3}}\right)\,}
$$

The prefactor $1/(4n\sqrt3)$ is entirely circle-constant-free — it is the piece that contains no $\pi$ at all. The circle constant appears *once and only once*, inside the exponent, as the coefficient of $\sqrt{2n/3}$. That placement is what makes this case distinctive: the constant is not multiplied against the answer, it is exponentiated, so any change in the constant is amplified by the size of the exponent.

## The exact count, computed

Because the recurrence is pure integer arithmetic, the true values of $p(n)$ are computable exactly and set a hard benchmark no asymptotics can argue with. The rows below were produced with the Euler pentagonal recurrence in exact integers.

| $n$ | $p(n)$ (exact integer) | Hardy–Ramanujan $\dfrac{e^{\pi\sqrt{2n/3}}}{4n\sqrt3}$ | relative error |
|---:|---:|---:|---:|
| 5 | 7 | 8.941459 | +27.7% |
| 10 | 42 | 48.10431 | +14.5% |
| 20 | 627 | 692.3846 | +10.4% |
| 50 | 204 226 | 217 590.5 | +6.5% |
| 100 | 190 569 292 | 199 280 900 | +4.6% |
| 200 | 3 972 999 029 388 | 4.100251 × 10¹² | +3.2% |
| 500 | 2 300 165 032 574 323 995 027 | 2.346387 × 10²¹ | +2.0% |
| 1000 | 24 061 467 864 032 622 473 692 149 727 991 | 2.440200 × 10³¹ | +1.42% |

The leading asymptotic overshoots, and the overshoot decays only like $1/\sqrt{n}$ — it is still 1.4% high at $n=1000$. That is the honest state of the pure Hardy–Ramanujan formula: it captures the exponential character of the count but leaves a slowly vanishing arithmetic residue.

## Rademacher's exact series

In 1937 Hans Rademacher turned the asymptotic into an *exact* convergent series, correcting Hardy and Ramanujan's own error term:

$$
p(n) \;=\; \frac{1}{\pi\sqrt2}\sum_{k\ge 1} A_{k}(n)\,\sqrt{k}\;
\frac{d}{dn}\!\left[\frac{\sinh\!\Big(\frac{\pi}{k}\sqrt{\tfrac{2}{3}\big(n-\tfrac{1}{24}\big)}\Big)}{\sqrt{n-\tfrac{1}{24}}}\right],
$$

with the Dedekind-sum weight $A_{k}(n)$ a finite arithmetic sum. The single $k=1$ term ($A_1=1$) already reproduces $p(n)$ to startling precision:

| $n$ | $p(n)$ exact | Rademacher $k=1$ term | relative error |
|---:|---:|---:|---:|
| 10 | 42 | 41.62779 | −0.886% |
| 20 | 627 | 625.7577 | −0.198% |
| 50 | 204 226 | 204 211.1 | −0.0073% |
| 100 | 190 569 292 | 190 568 900 | −0.00018% |
| 200 | 3 972 999 029 388 | 3.972999 × 10¹² | < 10⁻⁵ % |
| 500 | 2 300 165 032 574 323 995 027 | 2.300165 × 10²¹ | machine precision |

The one structural number $1/24$ is no accident: the generating function is $F(q)=q^{-1/24}/\eta(\tau)$ with $q=e^{2\pi i\tau}$ and $\eta$ the Dedekind eta function, so the modular transformation $\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)$ — which carries a square root and a quarter-turn phase, hence a circle constant through $\sqrt{-i}$ — is exactly what converts the hard region near the unit circle into the tame region near the origin. The circle constant enters the exact formula the same way it entered the asymptotic: as an evaluated limit inside the modular transformation and the contour normalisation, computed and never measured.

## Computed, never measured

Every appearance of the circle constant here is the evaluation of a limit:

- the contour normalisation $1/2\pi i$ is the full-turn arclength of the unit circle, a computed circumference;
- the exponent's fuel is $\zeta(2)=\pi^2/6$, the *computed* Basel sum;
- the modular factor $\sqrt{-i\tau}$ is a quarter-turn phase, again an evaluated constant;
- the saddle-point integral evaluates to a Gaussian, whose normalisation is the computed $\sqrt{2\pi}$.

No ruler, no clock, no instrument: the circle constant in this chapter is a value that the arithmetic returns, not a length anyone reads off a physical circle. That is the site's standing rule, and the partition asymptotic obeys it cleanly.

## Under Golden Pi (π̂ = 4/√φ)

The site's position is that the circle constant is the golden-algebraic value

$$
\hat\pi \;=\; \frac{4}{\sqrt{\varphi}} \;=\; 3.1446055110296931443\ldots,
\qquad \varphi=\frac{1+\sqrt5}{2},
$$

the positive root of $x^{4}+16x^{2}-256=0$, an algebraic number of degree 4 entirely inside the field $\mathbb{Q}(\sqrt\varphi)$. The recurring gap against the analytic constant is

$$
\frac{\hat\pi-\pi}{\pi} \;=\; 0.0009590223\ldots = 0.0959022309\% .
$$

Substituting $\hat\pi$ into the partition asymptotic touches only the exponent, because the prefactor $1/(4n\sqrt3)$ mentions no constant at all:

$$
p_{\hat\pi}(n) \;\sim\; \frac{1}{4n\sqrt3}\,\exp\!\Big(\hat\pi\sqrt{\tfrac{2n}{3}}\Big)
\;=\; \frac{1}{4n\sqrt3}\,\exp\!\Big(\pi\sqrt{\tfrac{2n}{3}}\cdot\frac{\hat\pi}{\pi}\Big).
$$

The exponent is multiplied by $\hat\pi/\pi = 1.00095902\ldots$, so the ratio of the golden asymptotic to the conventional one is

$$
\frac{p_{\hat\pi}(n)}{p(n)} \;=\; \exp\!\Big(\pi\sqrt{\tfrac{2n}{3}}\;\cdot\;\frac{\hat\pi-\pi}{\pi}\Big) \;=\; \exp\!\Big(0.0030128\ldots\sqrt{n}\Big),
$$

a shift that grows without bound as $\sqrt{n}$ — the constant sits in an exponent, so it is amplified by the exponent's own size.

| $n$ | exponent $\pi\sqrt{2n/3}$ | golden exponent $\hat\pi\sqrt{2n/3}$ | $p_{\hat\pi}/p$ (asymptotic) |
|---:|---:|---:|---:|
| 100 | 25.65099660 | 25.67559648 | +2.49% |
| 200 | 36.2757… | 36.3105… | +3.54% |
| 500 | 57.35… | 57.405… | +5.65% |
| 1000 | 81.11557352 | 81.19336516 | +8.09% |
| 10⁶ | ≈ 2565.0 | ≈ 2567.46 | ≈ +11.7× |

So while the exact integer count $p(n)$ is label-blind — it is what it is, by addition and the pentagonal recurrence, and moves by not one unit under any relabel — the *growth law* diverges from it under the golden label, and diverges *faster than linearly*: the gap that is 2.49% at $n=100$ is 8.09% at $n=1000$ and a factor of roughly eleven at a million. This is the mirror image of the Lévy-constant case, where the constant also sat in an exponent; there the exponent was small, here it grows like $\sqrt n$.

## The honest ledger

The arithmetic of this chapter is unusually clean about what can and cannot discriminate the two labels, and it says so on the record:

- **The count is exact and free.** $p(n)$ is computed by the Euler pentagonal recurrence in whole numbers; it carries no circle constant and no uncertainty. A relabel of $\pi$ does not change a single partition.
- **The asymptotic is computed, and it is where the constant lives.** Hardy–Ramanujan, Rademacher and the circle method are all evaluations of limits — contour integrals, the Basel sum, the modular transformation — computed and never measured.
- **The gap compounds rather than hides.** Because the constant is exponentiated, the conventional golden relabel is not a 0.0959% perturbation of the answers; it is +2.49% at $n=100$ and +8.09% at $n=1000$. Unlike cases where a scale factor can be absorbed into a measured coefficient, here the mismatch grows with $n$ and cannot be masked.
- **What the integer count does and does not settle.** The partitions of $n$ are a definitional whole number; the asymptotic of a definition is not a physical measurement, so it does not *measure* the constant either way. What it does is pin the constant to the value 3.14159265… through the exact, machine-precision agreement of Rademacher's $k=1$ term with the integer count — a computed agreement that the golden exponent, drifting by whole percents, does not reproduce.

Nothing here is at odds with the site's position that golden-π is the constructible, algebraic circle constant that squares the circle exactly and closes the golden field: that is a claim about the *constructed* system, and it is credited where it is real. The partition asymptotic is a claim about a *computed* limit, and the computation returns $3.14159265\ldots$ to whatever precision the integer count demands. Both statements are true, and the boundary between them is drawn here in the open: the constant is computed, never measured — by us or by anyone.

## Further Reading

- [**The Basel Problem: When an Infinite Sum Computes the Circle Constant**](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the evaluated sum $\zeta(2)=\pi^2/6$ that fuels the partition exponent.
- [**The Riemann Zeta Function at Even Integers: How Euler's Bernoulli-Numbers Formula Computes π to Every Even Power**](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — the same zeta values at higher arguments, where the golden gap compounds by the power.
- [**Euler's Gamma Function: How Γ(x)Γ(1−x) = π/sin(πx) Computes the Circle Constant**](/blog/posts/2026-08-26-gamma-function-euler-reflection-formula-computes-circle-constant-golden-pi/) — the reflection formula, the analytic neighbour of the modular transformation used here.
- [**The Wallis Product and Stirling's Approximation: How Factorials Compute the Circle Constant**](/blog/posts/2026-09-26-wallis-product-stirling-approximation-factorals-compute-circle-constant-golden-pi/) — another integer-counting asymptotic whose constant enters through a Gaussian normalisation.
- [**Lévy's Constant and Khinchin's Constant: How the Typical Continued Fraction Computes the Circle Constant**](/blog/posts/2026-10-08-levy-khinchin-constants-continued-fraction-computes-circle-constant-golden-pi/) — the companion case where a circle constant inside an exponent is amplified by a small exponent.
