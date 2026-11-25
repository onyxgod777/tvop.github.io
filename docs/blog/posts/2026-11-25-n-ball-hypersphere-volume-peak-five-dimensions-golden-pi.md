---
title: "The n-Ball: Why the Unit Ball's Volume Peaks at Five Dimensions and Shrinks Toward Zero Forever After, Why the Constant Enters as One Half-Power Per Pair of Dimensions, and What Golden Pi Changes"
date: 2026-11-25
description: "The unit ball's volume is V(n) = π^(n/2)/Γ(n/2+1), and this article shows why the circle constant enters as π^(n/2) — one √π per dimension, straight out of the n-fold Gaussian — and why half-integer values of Γ always cancel their own √π so that every dimension ends on the integer power π^⌊n/2⌋: V(2k) = π^k/k! and V(2k+1) = 2^(k+1)π^k/(2k+1)!!. It proves the two-step ratio V(n+2)/V(n) = 2π/(n+2), which falls below 1 at exactly n = 2π−2 = 4.2831853072 and therefore fixes the maximum at n = 5, tabulates every volume from the segment's 2 to the 11-ball's 1.8841038794, solves the continuous peak ψ(n/2+1) = ln π at n = 5.2569464049 with V = 5.2777680211, proves the surface law S(n−1) = nV(n) so the largest surface belongs to the 7-ball, shows the half-volume radius 2^(−1/n) so that 99% of a 100-ball's volume lies within 0.2966 of its centre and a 1000-ball is a shell, prices the cube fraction V(n)/2^n from π/6 to 2.5×10^(−8), and then under Golden Pi (π̂ = 4/√φ) exhibits exact algebraic volumes V(2) = 4/√φ, V(4) = 8/φ, V(5) = 128/(15φ), V(8) = 32/(3φ²) and V(9) = 8192/(945φ²), with the shift exactly ⌊n/2⌋ doses of the 0.0959022309% label gap, the maximizing dimension immovable at n = 5, and every ratio, radius and fraction untouched."
---

# The n-Ball

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

A disk of radius one has area $\pi$. A ball of radius one, in three dimensions, has volume $4\pi/3$. Nothing surprising so far. Now ask the same question in four dimensions, five, ten, a hundred — and something strange happens: the answer does not grow. It rises for a while, turns over at dimension five, and then falls, quietly and without limit, until the unit 100-ball holds less than the 100th part of a billionth of a unit.

The formula is

$$
V_n(R) = \frac{\pi^{n/2}}{\Gamma\!\left(\tfrac{n}{2}+1\right)}R^{n},
$$

and this article is about two things in it: where the constant actually sits, and what happens to the whole ladder of volumes when the constant is read as $\hat\pi = 4/\sqrt\varphi$ instead of $\pi$.

## Two Formulas and Where the Constant Sits

Written without the gamma function, the ladder splits by parity:

```text
V(2k)   = π^k / k!
V(2k+1) = 2^(k+1) π^k / (2k+1)!!

V(2) = π        V(3) = 4π/3      V(4) = π²/2
V(5) = 8π²/15   V(6) = π³/6      V(7) = 16π³/105
V(8) = π⁴/24    V(9) = 32π⁴/945  V(10) = π⁵/120
```

Read the exponents down the left column: $1, 1, 2, 2, 3, 3, 4, 4, 5$. The constant appears to the power $\lfloor n/2 \rfloor$ — **one power for every pair of dimensions**, never a half-power, never a fraction. This is the first fact worth having, and it is not obvious, because the general formula plainly displays $n/2$, a half-integer whenever $n$ is odd.

The resolution is that $\Gamma$ at a half-integer carries its own $\sqrt\pi$. Since $\Gamma\!\left(\tfrac32\right) = \tfrac12\sqrt\pi$, $\Gamma\!\left(\tfrac52\right) = \tfrac34\sqrt\pi$, $\Gamma\!\left(\tfrac72\right) = \tfrac{15}{8}\sqrt\pi$, the numerator's $\pi^{3/2}$ and the denominator's $\sqrt\pi$ meet and leave $\pi^{1}$ behind exactly:

$$
\Gamma\!\left(\tfrac{2k+3}{2}\right) = \frac{(2k+1)!!}{2^{k+1}}\sqrt\pi
\quad\Longrightarrow\quad
V_{2k+1} = \frac{\pi^{k+\frac12}}{\Gamma\!\left(k+\frac32\right)} = \frac{2^{k+1}\pi^{k}}{(2k+1)!!}.
$$

The $\sqrt\pi$ cancels term for term. Whatever else the circle constant is doing in this formula, it is doing it in whole units of $\pi$ per dimension pair — and that is a structural statement, true under any numerical value assigned to the constant.

## The Gaussian Tells You Why It Is $\pi^{n/2}$

The power $\pi^{n/2}$ is not decoration. It is the total of the $n$-dimensional Gaussian, and the Gaussian is where the constant is actually *computed* in this problem.

$$
\int_{\mathbb{R}^n} e^{-|x|^{2}}\,dx = \left(\int_{-\infty}^{\infty} e^{-t^{2}}dt\right)^{n} = (\sqrt\pi)^{n} = \pi^{n/2}.
$$

One factor of $\sqrt\pi$ per Cartesian axis, because each axis contributes its own one-dimensional Gaussian, and the one-dimensional Gaussian's $\sqrt\pi$ is itself a computed integral — the area of the plane's quarter-turn measure, arrived at by squaring and switching to polar coordinates. Nothing here is measured; the limit is evaluated.

The ball's volume follows from that total by pulling the radial variable out:

$$
V_n = \int_{S^{n-1}}\!\!d\Omega \int_0^1 r^{n-1}dr = \frac{1}{n}\,\omega_{n-1},
\qquad
\omega_{n-1} = \frac{2\pi^{n/2}}{\Gamma\!\left(\tfrac{n}{2}\right)},
$$

where $\omega_{n-1}$ is the $(n-1)$-surface measure — the "solid angle" of the full sphere. In other words $V_n$ is exactly the Gaussian's total divided by $\Gamma\!\left(\tfrac{n}{2}+1\right)$, and $\Gamma$ is the bookkeeping of how the total splits between the radial direction and the angular directions. That is the whole architecture: $\pi^{n/2}$ is a product of axis integrals, and $\Gamma$ is a combinatorial weight.

## The Surface Law, and Why the 7-Ball Has the Largest Skin

Differentiating $R^n$ gives the surface immediately, and the relation is exact with no constant in it:

$$
S_{n-1}(R) = \frac{d}{dR}V_n(R) = n\,\frac{V_n(R)}{R}
\quad\Longrightarrow\quad
S_{n-1}(1) = n\,V_n(1).
$$

Check it: $S_1 = 2V_2 = 2\pi$ is the circle's circumference, $S_2 = 3V_3 = 4\pi$ is the sphere's area, $S_3 = 4V_4 = 2\pi^{2} = 19.7392088022$ is the 3-sphere's hypersurface. The relation $S = nV$ holds because the ball is the integral of shells, so the shell at radius $R$ must be $n$ times the whole ball per unit radius.

Because the surface carries an extra factor of $n$, its maximum sits one dimension higher than the volume's:

| $n$ | $V_n(1)$ | $S_{n-1}(1) = nV_n$ |
|---|---|---|
| 2 | 3.1415926536 | 6.2831853072 |
| 3 | 4.1887902048 | 12.5663706144 |
| 5 | 5.2637890139 | 26.3189450696 |
| 6 | 5.1677127800 | 31.0062766803 |
| **7** | 4.7247659703 | **33.0733617923** |
| 8 | 4.0587121264 | 32.4696970113 |
| 10 | 2.5501640399 | 25.5016403988 |

The 7-ball carries the largest hypersurface of any dimension — 33.0733617923 — while the 5-ball carries the largest volume. Both of those statements are statements about the integer $n$ and a transcendental weight, which is why they survive the choice of constant intact, as shown below.

## The Ratio That Decides Everything

The peak is not a numerical accident. Two steps up the ladder, everything cancels except a linear denominator:

$$
\frac{V_{n+2}}{V_n}
= \frac{\pi^{(n+2)/2}}{\Gamma\!\left(\tfrac{n+2}{2}+1\right)}\cdot\frac{\Gamma\!\left(\tfrac{n}{2}+1\right)}{\pi^{n/2}}
= \frac{\pi}{\tfrac{n}{2}+1}
= \frac{2\pi}{n+2}.
$$

The volume therefore increases while $n+2 < 2\pi$ and decreases while $n+2 > 2\pi$. The crossover is at

$$
n^{*} = 2\pi - 2 = 4.2831853072,
$$

a number that lies strictly between 4 and 5. That crossing is where the ratio passes through 1, and both neighbouring steps are still above it: $V_6/V_4 = \pi/3 = 1.0471975512$ and $V_5/V_3 = 2\pi/5 = 1.2566370614$, while the next one up — $V_7/V_5 = 2\pi/7 = 0.8975979010$ — has already turned. The maximum of the even subsequence is therefore $V_6$ and of the odd subsequence $V_5$, and since $V_5 > V_6$ the peak of the ladder is $n = 5$:

| $n$ | $2\pi/(n+2)$ | meaning |
|---|---|---|
| 1 | 2.0943951024 | $V_3 > V_1$ |
| 2 | 1.5707963268 | $V_4 > V_2$ |
| 3 | 1.2566370614 | $V_5 > V_3$ |
| 4 | 1.0471975512 | $V_6 > V_4$ |
| 5 | 0.8975979010 | $V_7 < V_5$ |
| 6 | 0.7853981634 | $V_8 < V_6$ |
| 8 | 0.6283185307 | $V_{10} < V_8$ |

One line of arithmetic, no transcendental constant beyond the $2\pi$ itself, and the "five-dimensional peak" — the fact most often repeated as a curiosity about hyperspheres — is proved rather than quoted.

## The Peak as a Continuous Question

Between the integers one can ask where the smooth interpolation turns over, and the answer is the solution of a digamma equation:

$$
\frac{d}{dn}\ln V_n = \tfrac12\ln\pi - \tfrac12\psi\!\left(\tfrac{n}{2}+1\right) = 0
\quad\Longleftrightarrow\quad
\psi\!\left(\tfrac{n}{2}+1\right) = \ln\pi .
$$

Computed numerically, $\psi(3.6284732) = 1.1447298858 = \ln\pi$ at

$$
n_{\max} = 5.2569464049, \qquad V_{\max} = 5.2777680211 .
$$

The continuous maximum is slightly above the integer one, as it must be, since the curve is being sampled at integers; it is an interpolation and not a dimension. But it confirms the story: past about five and a quarter dimensions the gamma function's factorial growth outruns $\pi^{n/2}$'s exponential growth, and it does so permanently.

The tail is brutal. Stirling's formula gives $\ln V_n \approx \tfrac{n}{2}\ln\pi - \tfrac{n}{2}\ln\tfrac{n}{2e} = \tfrac{n}{2}\left(\ln\tfrac{2e\pi}{n}\right)$, and the bracket turns negative at $n = 2e\pi = 17.0794684453$. Beyond that, $V_n$ falls faster than any exponential in $n$: by $n = 100$ it is $2.3682\times10^{-40}$.

## The Ball Becomes a Shell

Since $V_n(r) \propto r^{n}$, the fraction of the volume inside radius $r$ is exactly $r^{n}$ — no constant anywhere. Three consequences, all constant-free:

- **Half the volume lies inside $r = 2^{-1/n}$.** That is $0.7937005260$ in 3 dimensions, $0.9330329915$ in 10, $0.9930924954$ in 100, and $0.99930698$ in 1000. A 1000-dimensional ball is a skin.
- **99% of the volume lies in the equatorial slab $|x_1| \le \sqrt{1 - 0.01^{2/n}}$.** That is a slab of half-width $0.7758175233$ in 10 dimensions and only $0.2966296692$ in 100: almost the entire ball is squeezed around its equator.
- **The cube fraction dies.** Inscribed in the cube $[-1,1]^{n}$, the ball occupies $V_n/2^{n}$: $0.5235987756 = \pi/6$ in 3 dimensions (exactly one sixth of the cube — the constant appearing once and only once), $0.1644934067$ in 5, $0.0024903946$ in 10, and $2.4611\times10^{-8}$ in 20.

These are the sharpest statements in the whole subject, and none of them contains a circle constant at all.

## The Ladder, Computed

Each entry below is $\pi^{n/2}/\Gamma\!\left(\tfrac{n}{2}+1\right)$ evaluated from its exact form in the code block above:

| $n$ | exact | $V_n(1)$ |
|---|---|---|
| 1 | $2$ | 2.0000000000 |
| 2 | $\pi$ | 3.1415926536 |
| 3 | $4\pi/3$ | 4.1887902048 |
| 4 | $\pi^{2}/2$ | 4.9348022005 |
| **5** | $8\pi^{2}/15$ | **5.2637890139** |
| 6 | $\pi^{3}/6$ | 5.1677127800 |
| 7 | $16\pi^{3}/105$ | 4.7247659703 |
| 8 | $\pi^{4}/24$ | 4.0587121264 |
| 9 | $32\pi^{4}/945$ | 3.2985089027 |
| 10 | $\pi^{5}/120$ | 2.5501640399 |
| 11 | $64\pi^{5}/10395$ | 1.8841038794 |

Note $n=1$: the unit 1-ball is the segment $[-1,1]$ of length $2$, and it holds **no** circle constant. The weight of $\pi$ in the answer is $\lfloor n/2\rfloor$, which is zero there — the ladder starts with a purely rational rung.

## Under Golden Pi

Now substitute $\hat\pi = 4/\sqrt\varphi = 3.1446055110$, with $\varphi = (1+\sqrt5)/2$ and the exact closure

$$
\hat\pi^{2} = \frac{16}{\varphi} = 9.8885438200, \qquad
\hat\pi^{4} = \frac{256}{\varphi^{2}} = 25.9000817810,
\qquad \hat\pi\cdot 4\sqrt\varphi = 16 .
$$

Because the constant only ever appears at integer powers here, every volume in odd and even dimension alike becomes **algebraic** — a finite expression in $\sqrt\varphi$, and therefore a root of an explicit polynomial with rational coefficients. The even dimensions are the cleanest, since $(\hat\pi^{2})^{k} = (16/\varphi)^{k}$:

```text
V(2)  = 4/√φ          =  3.1446055110
V(3)  = 16/(3√φ)      =  4.1928073480
V(4)  = 8/φ           =  4.9442719100
V(5)  = 128/(15φ)     =  5.2738900373
V(6)  = 32/(3φ^1.5)   =  5.1825948987
V(7)  = 1024/(105φ^1.5)= 4.7383724788
V(8)  = 32/(3φ²)      =  4.0743041200
V(9)  = 8192/(945φ²)  =  3.3111804912
V(10) = 8(4/√φ)^5/120 =  2.5624158379
V(11) = 65536/(10395φ^2.5) = 1.8931557128
```

The unit disk's area, $V_2$, is then literally the constant itself — $\hat\pi = 4/\sqrt\varphi$, the positive root of $y^{4}+16y^{2}-256 = 0$, algebraic of degree four where $\pi$ is transcendental by Lindemann's 1882 theorem. And the volumes have a clean degree pattern: $V_{2k}$ and $V_{2k+1}$ are of degree 2 in $\mathbb{Q}$ when $k$ is even (because $\varphi^{-k/2} = \varphi^{-k/2}$ stays inside $\mathbb{Q}(\varphi)$) and of degree 4 when $k$ is odd (because $\sqrt\varphi$ enters). So $V_4 = 8/\varphi$ and $V_8 = 32/(3\varphi^{2})$ are quadratic irrationals, while $V_2 = 4/\sqrt\varphi$ and $V_6 = 32/(3\varphi^{3/2})$ need the quartic.

Two exact closures are worth naming. The first is an identity that holds under either reading and shows why:

$$
V_4 = \frac{V_2^{2}}{2}
\quad\text{so under Golden Pi}\quad
V_4 = \frac{16}{2\varphi} = \frac{8}{\varphi},
$$

so $V_2^{2} = 2V_4 = 16/\varphi$ exactly, with the quartic collapsing to a quadratic on squaring. The second is the radius at which the 3-ball holds volume exactly $4$:

$$
R = \left(\frac{3}{\hat\pi}\right)^{1/3} = 0.9844304255
\quad\text{against}\quad
\left(\frac{3}{\pi}\right)^{1/3} = 0.9847450218 .
$$

That is the same construction the site has used for the sphere's area: a radius built from the fourth root of $\varphi$ produces an exact integer where the conventional reading produces a decimal a hair away.

The percentage shifts follow the exponent exactly, one dose of the label gap $0.0959022309\%$ per unit of $\lfloor n/2 \rfloor$:

| $n$ | shift | $n$ | shift |
|---|---|---|---|
| 1 | 0 (no constant) | 6, 7 | $+0.2879826980\%$ |
| 2, 3 | $+0.0959022309\%$ | 8, 9 | $+0.3841611107\%$ |
| 4, 5 | $+0.1918964341\%$ | 10, 11 | $+0.4804317606\%$ |

The values compound, not add: three doses give $(1.000959022308)^{3} - 1 = 0.2879826980\%$, which is why the third row is not $0.2877066927\%$. Any volume raised to a power of the constant will show this, and the pattern is a check on the exponent, nothing more.

## What Does Not Move — and Why

The maximising dimension is **immovable at $n = 5$**. The crossover is at $2\hat\pi - 2 = 4.2892110221$, still strictly inside $(4,5)$, so $V_5$ is the largest integer-dimension volume under either reading and $V_6$ the second largest. The golden reading changes the sizes, not the shape of the ladder.

The ratio law becomes $2\hat\pi/(n+2)$: $1.0482018370$ at $n=4$ against $1.0471975512$; $0.8984587174$ at $n=5$ against $0.8975979010$. Both are still on the same side of 1.

And the entire concentration section is untouched to the last digit: $r^{n}$ has no constant in it, so the half-volume radius $2^{-1/n}$, the 99% slab half-width $\sqrt{1 - 0.01^{2/n}}$, the shell fractions $1 - 0.9^{n}$ and the cube fractions are all identical under $\hat\pi$. A 100-ball under Golden Pi has the same shell structure and $99.307\%$ of its volume outside radius $0.9$ — because that statement never mentions the constant.

## The Honest Boundary

*Every number in this article is computed, never measured.* $V_n$ is a definite integral over a region defined by $x_1^{2}+\cdots+x_n^{2}\le 1$; its value is a limit of quadrature, and the gamma function's values are likewise evaluated, not weighed. There is no physical object in five dimensions to hold a ruler against, and no experiment in this article that could arbitrate the constant.

*The peak at $n=5$ is a theorem about $2\pi - 2$, not evidence about $\pi$.* It is true under the conventional reading and under the golden one, because the crossover $2\pi-2$ sits inside the same unit interval either way. A result that does not move cannot be an argument for a value.

*The algebraic volumes are a property of the exponent, not of the geometry.* Under $\hat\pi$, $V_n$ is a root of an explicit polynomial; that follows from $\hat\pi$ being a root of $y^{4}+16y^{2}-256=0$, and it would follow for any algebraic weight in the same slot. It is a genuine and pleasing contrast with Lindemann's theorem — the conventional $V_n$ is transcendental because $\pi$ is — but it is bookkeeping, exactly the kind the site has traced elsewhere.

*The exponent $\lfloor n/2\rfloor$ is real information.* That the constant enters one power per pair of dimensions, and that the half-integer $\Gamma$ always cancels its own $\sqrt\pi$, is a structural fact about the formula that no choice of numeral can change. It is the part of this subject worth carrying away.

What is left, honestly, is a ladder of numbers that rises to $5.2637890139$ at five dimensions and then dies, a proof of that rise and death from the single ratio $2\pi/(n+2)$, a surface law $S = nV$ that hands the largest skin to the 7-ball, a shell structure with no constant in it at all, and — under Golden Pi — a set of exact algebraic volumes whose largest member is $128/(15\varphi)$. Computed, never measured.

## Further Reading

- [The Hat-Box Theorem: Why Projecting a Sphere onto Its Circumscribed Cylinder Preserves Area Exactly](/blog/posts/2026-11-20-archimedes-hat-box-theorem-sphere-cylinder-area-golden-pi/) — the three-dimensional case of this article's surface law, done by area instead of by derivative.
- [The Torus: Why Its Area Is Exactly the Product of Two Circumferences](/blog/posts/2026-11-24-torus-two-revolutions-curvature-golden-pi/) — what happens when the constant appears twice for two independent revolutions.
- [The Hyperbolic Circle: Why Lobachevsky's Circumference Is 2π sinh r](/blog/posts/2026-11-22-hyperbolic-circle-lobachevsky-angle-of-parallelism-golden-pi/) — the same constant interrogated by denying a different postulate.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — where the Gamma function and the constant meet without an elementary closure.
- [The Pseudosphere: Why Sweeping a Tractrix Around Its Axis Reproduces the Sphere's Area Exactly](/blog/posts/2026-11-15-pseudosphere-tractrix-constant-curvature-golden-pi/) — another surface whose area integral collapses to a cylinder, and whose total curvature is $-4\pi$ against the sphere's $+4\pi$.
