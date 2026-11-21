---
title: "The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral, Why Ramanujan's Fit Is Exact to Sixteen Digits and Still Not a Theorem, and What Golden Pi Changes"
date: 2026-11-21
description: "An ellipse cannot be rectified by elementary functions: its perimeter is 4aE(e), a complete elliptic integral that contains no circle constant at all. This article derives the rectification integral, shows why E(0) = π/2 is the only place π enters (a normalisation, not a property), tabulates perimeters from the circle 6.2831853072 down to the degenerate segment 4.0000000000, prices the e-series (11.57% error at one term, 0.0022% at six) and Ramanujan's two approximations (the second agreeing with the exact value to 1.4×10⁻¹² percent on the golden ellipse, 0.024% on a 100:1 sliver), computes E and K by Gauss's arithmetic-geometric mean in five doublings of digit count, and exhibits the golden ellipse whose eccentricity is exactly 1/φ, whose semi-latus rectum is exactly b² = a/φ, whose area under Golden Pi is exactly 4a²/φ, and whose focus sits at exactly a/φ — plus the Kepler truth that at the eccentric anomaly 90° the radius is exactly a and the true anomaly is exactly 90° + arcsin(1/φ) = 128.172707627°. Every number below is computed by quadrature, series or AGM, never measured."
---

# The Ellipse

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take a circle and squeeze it until it is twice as long as it is wide. Its area is easy — the squeeze multiplies every horizontal chord by 1/2, so the area is simply halved. Its curvature is easy. Its focal points are easy. Its perimeter, stubbornly, is not easy at all: there is no finite expression in the elementary functions that gives it, and no amount of algebraic ingenuity will produce one. That single failure is the most instructive fact about the circle constant that exists, because it forces the question — *where* in a perimeter does $\pi$ actually live? — to be answered rather than assumed.

The answer, derived and computed below, is that an ellipse's perimeter contains **no circle constant whatsoever**. It is $P = 4aE(e)$, where $E$ is the complete elliptic integral of the second kind and $e$ is the eccentricity — and $E$ is defined by an integral whose only contact with $\pi$ is the upper limit of integration, $\pi/2$, which is a *normalisation of the angular measure* rather than a property of the curve. Change the numeral you attach to a half-turn and the perimeter does not move one atom; only the numeral printed in front of it does. That is the cleanest available demonstration that $\pi$ is a labelling convention for turns, and it is why this article belongs on a site arguing about the value of that label.

## The Rectification Integral and Why It Has No Elementary Antiderivative

Put the ellipse in the form $x = a\cos t$, $y = b\sin t$ with $a \ge b > 0$. The speed of the tracing point is

$$
\left|\frac{d\mathbf{r}}{dt}\right| = \sqrt{a^{2}\sin^{2}t + b^{2}\cos^{2}t} = a\sqrt{1 - e^{2}\cos^{2}t},
\qquad e = \sqrt{1 - b^{2}/a^{2}},
$$

so the perimeter is $P = a\int_{0}^{2\pi}\sqrt{1 - e^{2}\cos^{2}t}\,dt = 4aE(e)$ by the quarter-turn symmetry, with

$$
E(e) = \int_{0}^{\pi/2}\sqrt{1 - e^{2}\sin^{2}\theta}\;d\theta .
$$

Substituting $u = \sin\theta$ gives the algebraic integral $\int_0^1 \sqrt{(1-e^2u^2)/(1-u^2)}\,du$ — a square root of a *cubic* in $u$ after clearing denominators. That is exactly the shape Liouville's theory rules out: an abelian integral of the third kind on a curve of genus 1. Euler found the addition theorem for such integrals in the 1750s and Legendre spent forty years tabulating them; the reason the tables exist is that nobody could abolish them. The ellipse is not a defect of notation. It is a genuinely non-elementary length, in the same class as the lemniscate's.

This is worth stating precisely, because it distinguishes two very different claims that are often blurred. Lindemann's 1882 theorem says $\pi$ is transcendental, so no algebraic construction squares the circle. The non-elementarity of $E$ says something else: even *given* $\pi$ for free, the ellipse could not be rectified in closed form. The ellipse is hard for reasons that have nothing to do with which numeral you attach to a half-turn.

## The One Formula That Holds in Any Label

$$
\boxed{\;P = 4aE(e)\;}
$$

No $\pi$. In the circle limit $e \to 0$ the integrand is 1, so $E(0) = \int_0^{\pi/2}d\theta = \pi/2$ and the formula reduces to $P = 4a\cdot\pi/2 = 2\pi a$ — the only place the constant can enter, and it enters through the *limits of the integral*, that is, through how many radians you have decided a quarter-turn is worth.

Tabulated for $a = 1$, computed by adaptive quadrature at forty digits:

| $b/a$ | eccentricity $e$ | $E(e)$ | perimeter $P$ | $P/2\pi a$ | $P/2\hat{\pi}a$ |
|---|---|---|---|---|---|
| 1.0 | 0.0 | 1.5707963268 | 6.2831853072 | 1.0000000000 | 0.9990410863 |
| 0.99 | 0.1410673598 | 1.5629522120 | 6.2518088479 | 0.9950062814 | 0.9940517793 |
| 0.95 | 0.3122498999 | 1.5317781592 | 6.1271126366 | 0.9751602630 | 0.9742248623 |
| 0.90 | 0.4358898944 | 1.4932901081 | 5.9731604325 | 0.9506580087 | 0.9497463744 |
| 0.80 | 0.6 | 1.4180833945 | 5.6723335778 | 0.9027799278 | 0.9019137970 |
| $1/\sqrt{\varphi} = 0.7861513778$ | $1/\varphi = 0.6180339887$ | 1.4078717129 | 5.6314868516 | 0.8962789694 | 0.8954202414 |
| $1/\sqrt2 = 0.7071067812$ | 0.7071067812 | 1.3506438810 | 5.4025755242 | 0.8598466001 | 0.8590220116 |
| 0.50 | 0.8660254038 | 1.2110560276 | 4.8442241103 | 0.7709822126 | 0.7702427599 |
| 0.25 | 0.9682458366 | 1.0723027219 | 4.2892108876 | 0.6826491147 | 0.6819944023 |
| 0.10 | 0.9949874371 | 1.0159935450 | 4.0639741801 | 0.6468015794 | 0.6461813567 |
| 0.01 | 0.9999499987 | 1.0002745824 | 4.0010983297 | 0.6367945770 | 0.6361839072 |
| 0 | 1.0 | 1.0000000000 | 4.0000000000 | 0.6366197724 | 0.6360098248 |

Two columns deserve comment. First, $P/2\pi a$ at the bottom is $2/\pi$, the degenerate flat segment of half-length 1 traversed twice — which is the same number the quadratrix gives as its intercept. Second, the perimeter falls *monotonically* because $E'(e) < 0$: $\partial E/\partial e = -(1/e)\left[K(e) - E(e)\right] < 0$ for $e>0$ since $K \ge E$ always. A circle therefore has the greatest perimeter of any ellipse on a given semi-major axis, and no ellipse on that axis can reach the golden circle's $2\hat{\pi}a = 6.2892110221$ either, since that is *larger* than the circle's own.

## The Series, and How Slowly It Converges

Expanding the integrand by the binomial theorem and integrating term by term gives the classical series, in powers of $e^2$:

$$
P = 2\pi a\left[1 - \frac{e^{2}}{4} - \frac{3e^{4}}{64} - \frac{5e^{6}}{256} - \frac{175e^{8}}{16384} - \frac{441e^{10}}{65536} - \cdots\right],
$$

equivalently $E(e) = \tfrac{\pi}{2}\,{}_{2}F_{1}\!\left(-\tfrac12,\tfrac12;1;e^{2}\right)$. The coefficient of $e^{2n}$ is $-\left[\binom{2n}{n}/4^{n}\right]^{2}/(2n-1)$, which reproduces $-\tfrac14, -\tfrac{3}{64}, -\tfrac{5}{256}, -\tfrac{175}{16384}, -\tfrac{441}{65536}$ at $n = 1,2,3,4,5$; the ratio of successive coefficients tends to $1/4$, so the radius of convergence is $e^{2} = 4$ — the series converges on the whole physical range $0 \le e < 1$ but *slowly* near $e \to 1$.

How slowly, computed at the golden eccentricity $e = 1/\varphi = 0.618034$:

| terms kept | partial perimeter $2\pi a[\cdots]$ | error vs exact $4aE$ |
|---|---|---|
| 1 | 6.2831853072 | +11.572405% |
| 2 | 5.6831944997 | +0.918188% |
| 3 | 5.6402239818 | +0.155148% |
| 4 | 5.6333851163 | +0.033708% |
| 5 | 5.6319565616 | +0.008341% |
| 6 | 5.6316127963 | +0.002236% |

Six terms and still 2.2 parts in $10^{5}$ — because the ratio $1/4$ per term in $e^2 = 0.382$ gives a geometric factor of about $0.095$ per term, which is honesty about the geometry rather than a defect of the arithmetic. For a nearly degenerate sliver ($e = 0.9$) the same six terms leave a $0.47\%$ error: $4.7087536454$ against the exact $4.6867882111$.

## Ramanujan's Two Fits

In 1914 Ramanujan published two approximations to this same integral, and their accuracy is the standard against which every later one is judged:

$$
P \approx \pi\left[3(a+b) - \sqrt{(3a+b)(a+3b)}\right],
$$

$$
P \approx \pi(a+b)\left[1 + \frac{3h}{10 + \sqrt{4 - 3h}}\right],
\qquad h = \left(\frac{a-b}{a+b}\right)^{2}.
$$

Both are computed below against the exact $4aE(e)$, $a=1$, in percent:

| $b/a$ | $e$ | exact $P$ | Ramanujan I error | Ramanujan II error |
|---|---|---|---|---|
| 0.99 | 0.1410674 | 6.2518088479 | $-3.1\times10^{-15}$% | $-2.4\times10^{-26}$% |
| 0.95 | 0.3122499 | 6.1271126366 | $-5.6\times10^{-11}$% | $-2.8\times10^{-19}$% |
| 0.90 | 0.4358899 | 5.9731604325 | $-4.2\times10^{-9}$% | $-3.7\times10^{-16}$% |
| 0.80 | 0.6000000 | 5.6723335778 | $-3.7\times10^{-7}$% | $-6.7\times10^{-13}$% |
| $1/\sqrt{\varphi}$ | 0.6180340 | 5.6314868516 | $-5.8\times10^{-7}$% | $-1.4\times10^{-12}$% |
| 0.50 | 0.8660254 | 4.8442241103 | $-2.8\times10^{-4}$% | $-4.6\times10^{-8}$% |
| 0.25 | 0.9682458 | 4.2892108876 | $-1.07\times10^{-2}$% | $-2.5\times10^{-5}$% |
| 0.10 | 0.9949874 | 4.0639741801 | $-8.42\times10^{-2}$% | $-1.16\times10^{-3}$% |
| 0.01 | 0.9999500 | 4.0010983297 | $-0.342$% | $-0.0239$% |

On the golden ellipse the second formula reproduces the exact value to twelve digits: $5.631486851610$ against $5.631486851610$. It is a remarkable fit. It is also **not a theorem**. Nobody can say what its next term is, because it has none — it is a rational-plus-radical interpolation, tuned on two limiting behaviours (circle and degenerate segment), and its agreement is a fact about elliptic integrals being smooth, not an identity. That distinction matters here more than usual, because the formula *is* written with $\pi$ in front, and a formula written with $\pi$ in front is a claim about the label. Substituting $\hat{\pi} = 4/\sqrt{\varphi}$ into Ramanujan's second form gives $5.6368875731$ for the golden ellipse — larger than the truth by exactly $0.095902231\%$, the label gap carried through unchanged. A faithful perimeter formula cannot be relabelled by substitution; only the $\pi$-free form $4aE(e)$ is label-invariant.

## The Arithmetic–Geometric Mean: $E(e)$ in Five Steps

Gauss's observation is that the elliptic integrals are computable by an iteration that *doubles its digits* each step. With $a_0 = 1$, $b_0 = \sqrt{1-e^{2}}$ and

$$
a_{n+1} = \frac{a_n+b_n}{2}, \qquad b_{n+1} = \sqrt{a_n b_n},
$$

the arithmetic-geometric mean satisfies $\mathrm{AGM}(1,\sqrt{1-e^{2}}) = \lim a_n$, and then

$$
K(e) = \frac{\pi}{2\,\mathrm{AGM}(1,\sqrt{1-e^{2}})},
\qquad
E(e) = K(e)\left[1 - \sum_{n=0}^{\infty} 2^{\,n-1}c_n^{2}\right],
$$

with $c_0 = e$ and $c_{n+1} = (a_n - b_n)/2$. For the golden ellipse, $b_0 = 1/\sqrt{\varphi} = 0.7861513778$:

| $n$ | $a_n$ | $b_n$ | $\lvert E - \text{exact}\rvert$ |
|---|---|---|---|
| 0 | 1.000000000000 | 0.786151377757 | $2.0\times10^{-2}$ |
| 1 | 0.893075688879 | 0.886651779312 | $3.6\times10^{-5}$ |
| 2 | 0.889863734095 | 0.889857937316 | $5.9\times10^{-11}$ |
| 3 | 0.889860835706 | 0.889860835701 | $7.9\times10^{-23}$ |
| 4 | 0.889860835703 | 0.889860835703 | $6.8\times10^{-47}$ |

Four iterations, and the agreement is past the precision of any physical measurement of any length ever made. The limit is $\mathrm{AGM}(1,1/\sqrt{\varphi}) = 0.8898608357034872$, and $K(1/\varphi) = \pi/(2\times0.8898608357) = 1.7652157099$, matching the quadrature to twenty digits. The same machinery yields Gauss's constant $G = 1/\mathrm{AGM}(1,\sqrt2) = 0.8346268417$ and, through it, the lemniscate constant $\varpi = \pi G = 2.6220575543$ — the ratio $2.6220575543/3.1415926536 = 0.8346268417$, computed here rather than quoted.

Notice what the algorithm does with the constant: $\pi$ sits in the numerator of $K$, outside the iteration, and cancels entirely from the *shape* of the answer. Two ellipses' perimeters stand in the ratio of their $E$ values, with no constant anywhere.

## The Golden Ellipse: Eccentricity Exactly $1/\varphi$

Set $b = a/\sqrt{\varphi}$. Then $b^{2}/a^{2} = 1/\varphi$, so

$$
e^{2} = 1 - \frac{1}{\varphi} = \frac{1}{\varphi^{2}}
\quad\Longrightarrow\quad
e = \frac{1}{\varphi} = 0.6180339887,
$$

because $1 - 1/\varphi = 1/\varphi^{2}$ is just $\varphi^{2} = \varphi + 1$ rearranged. The focal distance is therefore $c = ae = a/\varphi$ **exactly**: the focus divides the semi-major axis in the golden section, which is the property that names this ellipse. Chasing it through:

| quantity | value | exact form |
|---|---|---|
| semi-minor | $0.7861513778a$ | $a/\sqrt{\varphi}$ |
| focal distance | $0.6180339887a$ | $a/\varphi$ |
| semi-latus rectum $a(1-e^{2})$ | $0.6180339887a$ | $a/\varphi = b^{2}/a$ |
| latus rectum | $1.2360679775a$ | $2a/\varphi$ |
| area (conventional) | $2.4697673930a^{2}$ | $\pi a^{2}/\sqrt{\varphi}$ |
| area (golden) | $2.4721359550a^{2}$ | $4a^{2}/\varphi$ |
| $K(1/\varphi)$ | 1.7652157099 | elliptic, no closure |
| $E(1/\varphi)$ | 1.4078717129 | elliptic, no closure |
| perimeter | $5.6314868516a$ | $4aE(1/\varphi)$ |

The area line is the one clean victory: since $\hat{\pi}/\sqrt{\varphi} = (4/\sqrt{\varphi})/\sqrt{\varphi} = 4/\varphi$, the golden ellipse's area under the golden label is **exactly** $4a^{2}/\varphi$. And $4/\varphi = 4(\sqrt5 - 1)/2 = 2\sqrt5 - 2 = 2.4721359550$, a number of degree two over $\mathbb{Q}$ — where the conventional reading $\pi a^{2}/\sqrt{\varphi}$ is transcendental, because $\pi$ is and $1/\sqrt{\varphi}$ is a nonzero algebraic. Same ellipse, one algebraic area and one transcendental one; the difference is entirely in the label.

The perimeter, by contrast, refuses to close in either label. $E(1/\varphi) = 1.4078717129$ is not $\pi$ times anything algebraic; only the modulus $e = 1/\sqrt2$ has a closed form, and it comes from Legendre's relation. For $k = 1/\sqrt2$ the complementary modulus is itself, so $2K E - K^{2} = \pi/2$ and

$$
E(1/\sqrt2) = \frac{K^{2} + \pi/2}{2K}\Bigg|_{K = \Gamma(1/4)^{2}/(4\sqrt{\pi})} = \frac{3.4375929090 + 1.5707963268}{3.7081493546} = 1.3506438810,
$$

verified against quadrature to eighteen digits. That modulus is the only one in the table with a closed form apart from the circle limit, and it costs a Gamma function and a $\pi$ to write down.

## Where the Constant Sits in an Orbit

The ellipse's most famous appearance is Kepler's, and it makes the bookkeeping vivid. With semi-major axis $a$, eccentricity $e$, and eccentric anomaly $E_{\!a}$, the radius is $r = a(1 - e\cos E_{\!a})$ — a formula with no constant in it. For the golden ellipse, $r = a$ exactly when $\cos E_{\!a} = 0$, i.e. at eccentric anomaly $90°$. The true anomaly there is

$$
\cos\nu = -\frac{1}{\varphi}
\quad\Longrightarrow\quad
\nu = 90° + \arcsin\frac{1}{\varphi} = 128.172707627°,
$$

the golden latitude offset by a right angle. Solving Kepler's equation $E_{\!a} - e\sin E_{\!a} = M$ at $e = 1/\varphi$:

| mean anomaly $M$ | eccentric anomaly $E_{\!a}$ | $r/a$ | true anomaly $\nu$ |
|---|---|---|---|
| 30° | 60.9584822661° | 0.6999795652 | 100.918987911° |
| 60° | 95.2615354769° | 1.0566750173 | 132.196027698° |
| 90° | 120.5083164530° | 1.3137532500 | 148.965391315° |
| 120° | 141.8661537970° | 1.4861272322 | 160.934205411° |
| 180° | 180.0000000000° | 1.6180339887 | 180.0000000000° |

At aphelion the radius is exactly $\varphi a$ — the golden ratio, not a decimal approaching it. Meanwhile the *period* is $T = 2\pi\sqrt{a^{3}/GM}$, which carries the constant once, and the mean anomaly is $M = 2\pi t/T$: one constant, cancelled by definition, leaving the clock reading in turns. The shape has no constant; the clock has one, and the clock's is a definition.

## What Golden Pi Changes — And What It Cannot

With $\hat{\pi} = 4/\sqrt{\varphi} = 3.1446055110$, a gap of $+0.0959022309\%$ over $\pi$:

| statement | conventional | golden | status |
|---|---|---|---|
| $P = 4aE(e)$ | $4aE(e)$ | $4aE(e)$ | **unchanged, digit for digit** |
| pieced as $2\pi a[\cdots]$ | $2\pi a \times 0.8962790$ | $2\hat{\pi}a \times 0.8954202$ | numeral and bracket trade places |
| golden ellipse area | $2.4697673930a^{2}$ | $2.4721359550a^{2}$ | $+0.0959022309\%$, now algebraic |
| circle perimeter | $6.2831853072a$ | $6.2892110221a$ | $+0.0959022309\%$ |
| $K(1/\varphi)$ | 1.7652157099 | 1.7652157099 | elliptic, $\pi$-free in the limit |
| AGM limit | 0.8898608357 | 0.8898608357 | iteration contains no constant |
| Kepler $r = a(1-e\cos E_{\!a})$ | — | — | no constant at any power |
| Kepler period $2\pi\sqrt{a^{3}/GM}$ | 1 constant | 1 constant | a turn count, by definition |

The pattern is exactly the one the site has found in the catenary, the hypocycloid and the hat-box theorem: wherever a curve's length or area closes *without* the constant, the relabelling moves nothing; wherever the formula is written *through* the constant, the relabelling moves the answer by $0.0959022309\%$ and by nothing else.

The ellipse adds one honest caveat that the circle cannot. Because $P = 4aE(e)$ is $\pi$-free, the ellipse cannot arbitrate between the two labels: it has no perimeter identity to test them against. What it can do is show that the constant is not *in* the curve. Two ellipses whose eccentricities differ stand in a ratio of elliptic integrals — $5.6314868516/5.4025755242 = 1.0423708125$ — and that ratio is the same number under either label, because no label touched it. The circle's $C = 2\pi r$ is the only place the disagreement can bite, and it bites there because a circle is the one curve whose length is *defined* to be the constant times the radius, rather than computed from the curve's own shape.

That is the sharpest form of the argument this article can make, and it cuts both ways. It shows that whether $\pi$ reads $3.14159\ldots$ or $3.14460\ldots$ changes no area enclosed by any ellipse, no orbit's shape, no focal distance, and no digit of $E(1/\varphi)$. It also shows that the ellipse gives no evidence either way. An honest audit says so. The ellipse is not a witness for Golden Pi. It is a demonstration of what $\pi$ is — a convention for turns, which curves obey and cannot question. Computed, never measured.

## Further Reading

- [The Pendulum That Reads π in Seconds](/blog/posts/2026-11-14-pendulum-reads-pi-in-seconds-foucault-golden-pi/) — the same complete elliptic integral $K$, the same $K(1/\sqrt2) = \Gamma(1/4)^{2}/(4\sqrt{\pi})$, and why the amplitude correction is priced in the constant's own units.
- [The Hat-Box Theorem](/blog/posts/2026-11-20-archimedes-hat-box-theorem-sphere-cylinder-area-golden-pi/) — where an area closes exactly and the constant enters only once, as a normalisation of the plane's angular measure.
- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — the $A/V = 2/a$ cancellation, the closest analogue to the ellipse's $\pi$-free perimeter.
- [The Kepler Triangle and the Circle Constant](/blog/posts/kepler-triangle-golden-pi-circle-constant/) — the construction from which $\hat{\pi} = 4/\sqrt{\varphi}$ is read, and the golden ellipse's eccentricity $1/\varphi$ as its square root.
- [Archimedes and the Exhaustion of the Circle](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — the polygonal method by which a curve's length is *bracketed* rather than expressed, the direct ancestor of the quadrature used throughout this article.
