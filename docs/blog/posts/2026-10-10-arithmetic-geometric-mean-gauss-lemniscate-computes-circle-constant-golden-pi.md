---
title: "The Arithmetic–Geometric Mean: How Gauss's π-Free Iteration and the Lemniscate Compute the Circle Constant — and What Golden Pi Changes"
date: 2026-10-10
description: "Gauss's arithmetic–geometric mean iterates two numbers with no circle in sight, yet its limit hides the circle constant through K(k) = π/(2·AGM). The lemniscate, the pendulum, and what golden π changes."
---

# The Arithmetic–Geometric Mean: How Gauss's π-Free Iteration and the Lemniscate Compute the Circle Constant — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take two positive numbers and repeatedly replace them by their arithmetic and geometric means. No circles, no angles, no series — just averaging and a square root. And yet, in 1799, the twenty-two-year-old Carl Friedrich Gauss found that this innocent iteration carries the circle constant inside it, hides it in an arc length, and computes it to arbitrary precision faster than almost any classical formula. This is the arithmetic–geometric mean (AGM), and its story is one of the cleanest examples of the constant π being **computed** — evaluated as an algebraic limit — and never measured.

## The iteration, and how fast it eats digits

Define, for two starting values $a_0, b_0$:

$$
a_{n+1} = \frac{a_n + b_n}{2}, \qquad b_{n+1} = \sqrt{a_n b_n}.
$$

The arithmetic mean always exceeds the geometric mean, so $a_n$ descends and $b_n$ ascends, and the two meet at a common limit — the **arithmetic–geometric mean** $\mathrm{AGM}(a_0,b_0)$. Ordinary sequences converge linearly. This one converges **quadratically**: the number of correct digits roughly doubles every step. Starting from $1$ and $\sqrt2$, here is the actual machine trace (60-digit arithmetic):

| step $n$ | $a_n$ | correct digits |
|---|---|---|
| 0 | 1.000000000000000000000000000000000000 | 0 |
| 1 | 1.207106781186547524400844362104849039 | 2 |
| 2 | 1.198156948094634295559172166332662477 | 5 |
| 3 | 1.198140234793877209082878869076407464 | 10 |
| 4 | 1.198140234735592207440631328633104086 | 21 |
| 5 | 1.198140234735592207439922492280323878 | 43 |
| 6 | 1.198140234735592207439922492280323878 | 51 |

Six iterations. That is the whole cost of $\mathrm{AGM}(1,\sqrt2) = 1.1981402347355922074399224922803238782\ldots$ to more than fifty places. No circle constant appears anywhere in the loop — the iteration is pure algebra, and its limit is a specific transcendental number that has nothing to do with π in its definition.

## Where the circle constant enters: Gauss, 1799

The constant walks in through an *integral*, not the iteration. Gauss proved the identity

$$
\mathrm{AGM}(1, \sqrt{1-k^2}) = \frac{\pi}{2\,K(k)},
\qquad\text{equivalently}\qquad
K(k) = \frac{\pi}{2\,\mathrm{AGM}\bigl(1,\sqrt{1-k^2}\bigr)} ,
$$

where $K(k) = \int_0^{\pi/2} \dfrac{d\theta}{\sqrt{1 - k^2\sin^2\theta}}$ is the complete elliptic integral of the first kind. Read that identity carefully, because it is the whole post: the right-hand side has **π to exactly the first power**, multiplied by a factor built entirely from the AGM — an iteration that contains no circle constant at all. So $K(k)$ is *linear* in π. Everything downstream of $K$ inherits that single power, undiluted.

For the symmetric case $k = 1/\sqrt2$:

$$
K\!\left(\tfrac{1}{\sqrt2}\right) = \frac{\pi}{2\,\mathrm{AGM}(1,1/\sqrt2)} = 1.8540746773013719184338503471952600\ldots
$$

The π-free factor is $\mathrm{AGM}(1,1/\sqrt2) = 0.8472130847939790866064991234821916\ldots$, purely algebraic. The circle constant is the only transcendental ingredient, and it stands there to the first power.

## The lemniscate and Gauss's constant

The identity is not an idle curiosity; it was Gauss's route to the **lemniscate**, the curve $(x^2+y^2)^2 = x^2 - y^2$. Its full arc length is the *lemniscate constant* $\varpi$ (a variant pi), and Gauss showed

$$
\varpi = \frac{\pi}{\mathrm{AGM}(1,\sqrt2)} = 2.6220575542921198104648395898911194\ldots
$$

so the lemniscate is $2\varpi = 5.2441151085842396209\ldots$ long. The same number appears as the integral

$$
\int_0^1 \frac{dx}{\sqrt{1-x^4}} = \frac{\varpi}{2} = 1.3110287771460599052\ldots,
\qquad \frac{2}{\pi}\int_0^1 \frac{dx}{\sqrt{1-x^4}} = \frac{1}{\mathrm{AGM}(1,\sqrt2)} = 0.8346268416740731862\ldots
$$

That last quantity is **Gauss's constant** $G = 1/\mathrm{AGM}(1,\sqrt2) = 0.8346268416740731862814297327990468\ldots$, an arc-length constant that equals a reciprocal-AGM — a genuine bridge between an elliptic curve and a square-root iteration. The lemniscate constant also has a purely classical closed form,

$$
\varpi = \frac{\Gamma\!\left(\tfrac14\right)^2}{2\sqrt{2\pi}} = \frac{3.6256099082\ldots^2}{2\sqrt{2\pi}} = 2.6220575542921198104\ldots,
$$

where the fourth-root of two rides on the circle constant under one square root — so a second power of π sits in the denominator, and the shift compounds (see the golden table below).

## The pendulum is the same integral

The reason this matters beyond Gaussian arc length is that $K$ governs a physical object: the large-amplitude pendulum. The exact period of a pendulum of length $L$ swinging to amplitude $\theta_0$ is

$$
T = 4\sqrt{\frac{L}{g}}\; K\!\left(\sin\frac{\theta_0}{2}\right).
$$

The small-angle limit $\theta_0 \to 0$ collapses to the textbook $T_0 = 2\pi\sqrt{L/g}$, which is just $\pi$ to the **first power** times $\sqrt{L/g}$ — the same linear dependence the AGM identity already told us to expect. For a one-metre pendulum at $g = 9.80665\ \mathrm{m\,s^{-2}}$, $\sqrt{1/g} = 0.3193299567810587110$:

| amplitude $\theta_0$ | $K(\sin\tfrac{\theta_0}{2})$ | exact period $T$ (s) | under $\hat\pi$ (s) | shift |
|---|---|---|---|---|
| 0° (small angle) | 1.5707963267948966192 | 2.0064092925890404509 | 2.0083334838611819071 | +0.0959022309% |
| 15° | 1.5775516607636663548 | 2.0150380146061958807 | 2.0169704810152480720 | +0.0959022309% |
| 30° | 1.5981420021125401445 | 2.0413384658583683343 | 2.0432961549869024063 | +0.0959022309% |
| 45° | 1.6335863074581478933 | 2.0866121798349586170 | 2.0886132874651976783 | +0.0959022309% |
| 60° | 1.6857503548125960429 | 2.1532423517838427274 | 2.1553073592354187842 | +0.0959022309% |
| 90° | 1.8540746773013719184 | 2.3682463462860098842 | 2.3705175473647908748 | +0.0959022309% |

Every row, every amplitude, moves by the *same* fraction, because $K$ is linear in π and the AGM factor beside it is unchanged. The series expansion makes the same point order by order:

$$
K(k) = \frac{\pi}{2}\left(1 + \frac{m}{4} + \frac{9m^2}{64} + \frac{25m^3}{256} + \cdots\right), \qquad m = k^2,
$$

so at $30°$ ($m = 0.0669872981\ldots$) the three-term truncation gives $1.5981395013\ldots$ against the exact $1.5981420021\ldots$ — and each bracket term is multiplied by the one and only π. There is no way to make the circle constant enter this problem except linearly.

## What golden π changes

Golden π is $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, where $\varphi = (1+\sqrt5)/2$, so $\hat\pi^2 = 16/\varphi = 8(\sqrt5-1)$ exactly. The recurring gap to the conventional constant is

$$
\frac{\hat\pi - \pi}{\pi} = 0.0959022308782525963\ldots\% .
$$

Now re-read the AGM identity with that gap in mind. Everything on the AGM side is **π-free algebra** — $\mathrm{AGM}(1,\sqrt2) = 1.1981402347355922074\ldots$, $\mathrm{AGM}(1,1/\sqrt2) = 0.8472130847939790866\ldots$, $\mathrm{AGM}(1,\sqrt\varphi) = 1.1319204683478462840\ldots$, Gauss's constant $G = 0.8346268416740731863\ldots$ — and **not one of them moves a digit**. Only the quantities the π rides on move, and they move by exactly the first-power gap:

| quantity | conventional π | under golden π̂ | shift |
|---|---|---|---|
| $\mathrm{AGM}(1,\sqrt2)$ | 1.1981402347355922074399 | 1.1981402347355922074399 | 0 (π-free) |
| Gauss's constant $G$ | 0.8346268416740731862814 | 0.8346268416740731862814 | 0 (π-free) |
| lemniscate constant $\varpi$ | 2.6220575542921198104648 | 2.6245721659815977026262 | +0.0959022309% |
| $K(1/\sqrt2)$ | 1.8540746773013719184339 | 1.8558521944473080045155 | +0.0959022309% |
| 1 m pendulum, 30° | 2.0413384658583683343045 | 2.0432961549869024062558 | +0.0959022309% |
| $\varpi = \Gamma(\tfrac14)^2/(2\sqrt{2\pi})$ | 2.6220575542921198104648 | 2.623... | +0.1918044618% (π under a root) |

The last row is the honest wrinkle: where the constant appears **squared** (the $\Gamma(1/4)^2/\sqrt{\pi}$ form), the gap **doubles** to 0.1918964%. The AGM route carries π once and moves by the single gap; the classical $\Gamma$ route carries it under a root and compounds. Same number, two bookkeepings — and the golden value of $\varpi$ differs between them unless the AGM is recomputed, which is exactly why the two forms should *not* be quoted interchangeably under a changed π. The first-power statements are the robust ones; the second-power identity is a warning about careless substitution.

### Where the golden case is genuinely exact

The golden constant's *real* strength is algebraic exactness, and it is fair to state it precisely:

- A disk of radius $\varphi^{1/4} = 1.1278384855616822603\ldots$ has area **exactly** $4$ under $\hat\pi$, since $\hat\pi \cdot \varphi^{1/2} = 4$. Conventional π leaves it at $3.9961675861\ldots$, short by exactly the gap — and $\varphi^{1/4}$ is the radius whose square is $\sqrt\varphi$, the radius for which the constant and the area conspire.
- $\hat\pi^2 = 16/\varphi = 9.8885438199983175713\ldots$ is **algebraic of degree two** in $\sqrt5$; the conventional $\pi^2 = 9.8696044010893586188\ldots$ is transcendental by Lindemann (1882).
- $\hat\pi/4 = 1/\sqrt\varphi$ exactly, and $2/\hat\pi = \varphi^{1/4}/\sqrt2$ — the same $\varphi^{1/4}$ that squares the circle.

So the lemniscate and pendulum constants become algebraic at every step *except* the one place the single power of π survives — and there, the gap is exactly $0.0959022308782526\ldots\%$, in and out, for every amplitude.

## Computed, never measured

The circle constant in this story is a **limit that is evaluated**, not a length that is stretched. The AGM enters as an algebraic iteration; $K(k)$ enters as the definite quadrature $\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}d\theta$; $\varpi$ enters through $\int_0^1(1-x^4)^{-1/2}dx$. None of them touches a physical circle, and none of them is a measurement — they *compute* a number, and that number is $3.14159265\ldots$ with the AGM identity sitting right there as the check.

The honest caveat is the pendulum, where $g = 9.80665\ \mathrm{m\,s^{-2}}$ **is** a measured quantity and $L$ is a physical length, so the period $T$ is a genuine measurand. But the label is not decidable there either. A precision pendulum's error budget is dominated by air drag, pivot friction, finite bob size, temperature, and the timing clock — spreads that vastly exceed a $0.0959\%$ difference, and the amplitude itself must be known to better than that for $K(m)$ to be pinned, which is exactly where real pendulums, accumulating nonlinear amplitude drift, cannot go. Swinging a bob arbitrates nothing; the identity $K(k) = \pi/(2\,\mathrm{AGM}(1,\sqrt{1-k^2}))$ decides the value analytically, with the AGM side computed and the π the limit of the elliptic quadrature.

The arithmetic–geometric mean therefore sits in the same ledger as every other entry on this site: an iteration with no circle in it, a limit that computes the circle constant to arbitrary precision in six steps, and a chosen coefficient — $\hat\pi = 4/\sqrt\varphi$ — that is algebraic where the computed one is transcendental, and that shifts every first-power formula by exactly one recurring gap. Computed, never measured.

## Further Reading

- [The Ellipse Perimeter: How the Elliptic Integral Computes the Circle Constant — and What Golden Pi Changes](/blog/posts/2026-09-12-ellipse-perimeter-elliptic-integral-computes-circle-constant-golden-pi/) — the same $K$ and $E$ family, applied to the ellipse's arc length.
- [The Gauss Circle Problem: How Lattice Counting Computes the Circle Constant](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/) — Gauss again, with the constant recovered by counting integer lattice points.
- [Wallis, Stirling and the Factorials: How Infinite Products Compute the Circle Constant](/blog/posts/2026-09-26-wallis-product-stirling-approximation-factorals-compute-circle-constant-golden-pi/) — the Γ-function route to π, and the Stirling correction that rides on it.
- [The Ramanujan and Chudnovsky Series: How the Fastest π Algorithms Converge](/blog/posts/2026-09-04-ramanujan-chudnovsky-series-computes-circle-constant-golden-pi/) — the AGM's descendants, the quadratically convergent algorithms that hold the record for π.
- [The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — where the constant enters a theorem as exactly one coefficient.
