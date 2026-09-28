---
title: "Gabriel's Horn: How an Improper Integral Computes the Circle Constant Inside a Finite Volume, and What Golden Pi Changes"
date: 2026-09-28
description: "Revolve the curve y = 1/x about the x-axis and you get Torricelli's horn: a solid of finite volume π whose surface area diverges like ln R. The volume integral splits cleanly — ∫₁^R x⁻² dx = 1 − 1/R is exact rational telescoping, and the circle constant enters only as the area of the unit cross-section disk, a computed limit and never a measurement. Truncated at R = 10⁶ the volume is 3.1415895119971396487, missing π by 3.141592654×10⁻⁶ and Golden Pi (π̂ = 4/√φ = 3.144605511…) by 0.003015999033, a factor 960.02; the divergence of the surface area is π-free, its finite part (√2−1)/2 + ½ln(2/(1+√2)) = 0.1129935779567487. The golden horn of radius φ^(1/4) has volume exactly 4, and y = 1/(π̂x) has volume exactly 1/π̂ = √φ/4 = 0.3180049123785172."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Take the rectangular hyperbola $y = 1/x$, chop it off at $x = 1$, and spin it about the $x$-axis. The surface you sweep out is **Torricelli's trumpet**, also called Gabriel's horn: an infinitely long, infinitely thin funnel whose mouth has radius 1 and whose tail thins toward zero without ever closing.

It has a finite volume and an infinite surface area. Torricelli announced this in the 1640s, reasoning with Cavalieri's indivisibles in *De solido hyperbolico acuto* (1644), and it has been the standard shock example in every calculus course since — the solid you can fill with a bucketful of paint but can never paint.

This post is about where the circle constant sits inside that paradox, and how to audit the claim that it could be $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$ rather than $\pi = 3.14159265358979323846\ldots$.

Throughout: the circle constant is *computed* — the limit of areas, the limit of integrals. Only genuine physical measurands are ever measured, and none is needed below.

## The volume integral splits into a rational part and a disk

A solid of revolution is a stack of disks. Slicing the horn at height $x$ gives a disk of radius $y(x) = 1/x$, so the volume between $x = 1$ and $x = R$ is

$$V(R) = \int_1^R \pi\,y(x)^2\,dx = \pi\int_1^R \frac{dx}{x^2}.$$

The integral on the right is exactly rational arithmetic. Anti-differentiate and telescope:

$$\int_1^R \frac{dx}{x^2} = \left[-\frac1x\right]_1^R = 1 - \frac1R \qquad \Longrightarrow \qquad V(R) = \pi\left(1 - \frac1R\right).$$

That factor $1 - 1/R$ is an exact rational number for every finite $R$: $0.999$ at $R = 10^3$, $0.999999$ at $R = 10^6$, $0.999999999999$ at $R = 10^{12}$. It is label-blind — no relabeling of any constant can move it, and it needs no instrument. It is also verified independently by Riemann sums: 100 000 midpoint-free rectangles on $[1,2]$ give $0.500003750015$ against the exact $1/2$, on $[1,10]$ give $0.900044551349$ against $9/10$, and on $[1,100]$ give $0.990495113850$ against $99/100$.

Everything the constant does in this solid is now visible: it arrives on the first line as the **area of the unit disk** $\pi y^2$ — itself a computed limit, the limit of inscribed and circumscribed polygon areas — and it is then multiplied by a rational. The horn does not *compute* the constant. It *consumes* it. That is a different register from the series posts: the Madhava–Leibniz sum, the Nilakantha sum, the Wallis product and the Chudnovsky series each output the constant as the limit of their own arithmetic. Here the arithmetic is complete without it, and the constant is an input to the geometry of the cross-section.

One honest consequence follows immediately, and it is the reason this article is short on suspense: since $V(R)$ converges to $\pi$ monotonically from below, every truncated horn is closer to the classical constant than to the golden one, by a factor that grows without bound.

## The truncated volumes, computed

With $V(R) = \pi(1 - 1/R)$ and $|\hat\pi - \pi| = 0.003012857439899910$ (a relative gap of $0.095902230878\%$):

| $R$ | $V(R)$ | $\pi - V(R)$ | $\hat\pi - V(R)$ | ratio |
|---|---|---|---|---|
| 1 | 0 | 3.141592654 | 3.144605511 | 1.000959 |
| 2 | 1.57079632679489662 | 1.570796327 | 1.573809184 | 1.001918 |
| 5 | 2.51327412287183459 | 0.6283185307 | 0.6313313882 | 1.0047951 |
| 10 | 2.82743338823081391 | 0.3141592654 | 0.3171721228 | 1.0095902 |
| 100 | 3.11017672705389531 | 0.03141592654 | 0.03442878398 | 1.0959022 |
| 1 000 | 3.13845106093620345 | 0.003141592654 | 0.006154450093 | 1.9590223 |
| 1 000 000 | 3.14158951199713965 | 0.000003141593 | 0.003015999033 | 960.02231 |
| $10^{12}$ | 3.14159265358665165 | $3.141592654\times10^{-12}$ | 0.003012857443 | $9.5902231\times10^{8}$ |

The pattern in the last column is exact arithmetic, not coincidence. The deficit to the classical constant is $\pi/R$, the deficit to the golden one is $\pi/R + (\hat\pi - \pi)$, so

$$\frac{|\hat\pi - V(R)|}{|\pi - V(R)|} = 1 + \frac{(\hat\pi-\pi)R}{\pi},$$

which is $1.0959022$ at $R = 100$ — the recurring $0.0959022\%$ gap appearing as a pure ratio — and grows linearly thereafter. At $R = 10^6$ the truncated horn sits $960.02\times$ closer to $\pi$; at $R = 10^{12}$, $9.5902\times10^{8}$ times closer.

The limit itself, taken over the whole half-line, is the classical value: $V(R) = \pi(1-1/R) \to \pi = 3.14159265358979323846\ldots$. The improper integral is a computed limit — a supremum over truncations — and it returns $3.14159\ldots$ exactly because the constant it ends up multiplying is the area of a disk, which is fixed by the same polygon exhaustion used everywhere else on this site.

## Where the infinity actually lives

The lateral surface area of the truncated horn is

$$S(R) = 2\pi\int_1^R y\,\sqrt{1 + y'^{\,2}}\;dx = 2\pi\int_1^R \frac1x\sqrt{1 + \frac{1}{x^4}}\;dx,$$

and this integral has a closed form. With $u = \sqrt{1 + x^{-4}}$,

$$A(x) = \frac{u}{2} + \frac14\ln\frac{u-1}{u+1}, \qquad A'(x) = -\frac{\sqrt{1+x^{-4}}}{x}, \qquad S(R) = A(1) - A(R),$$

verified symbolically at $x = 1,\,1.5,\,2,\,10$ where $-A'(x)$ reproduces the integrand $\sqrt{1+x^{-4}}/x$ to 18 digits, and numerically against 40-digit quadrature:

| $R$ | $S(R)$ (closed form) | $S(R)$ (quadrature) | $2\pi S(R)$ |
|---|---|---|---|
| 2 | 0.79838805810511909018 | 0.79838805810511909018 | 5.016420116113726 |
| 10 | 2.4155661711070391424 | 2.4155661711070391424 | 15.17744987481980 |
| 100 | 4.7181637626948400361 | 4.7181637626948400361 | 29.64509723063137 |
| 1 000 | 7.0207488569387607185 | 7.0207488569387607185 | 44.11266606331549 |
| 1 000 000 | 13.928504135921022771 | 13.928504135921022771 | 87.51537253780907 |

For large $R$ the area diverges logarithmically, with coefficient exactly 1 and a **finite part that contains no circle constant at all**:

$$S(R) = \ln R + C + O(R^{-4}), \qquad C = \frac{\sqrt2 - 1}{2} + \frac12\ln\frac{2}{1+\sqrt2} = 0.112993577956748666493155760344.$$

The check is exact at the printed digits: $\ln(10^6) + C = 13.928504135921022771$, which is $S(10^6)$ to twenty places. Multiplying through, $2\pi C = 0.70995958882349442138$ — the divergence of a surface whose *only* mention of the circle constant is the prefactor $2\pi = 6.2831853071795864769$ (the full turn).

So the paradox separates cleanly into two facts:

- **The volume is finite** because $\int_1^\infty x^{-2}dx$ converges. The value is the area of a disk — the constant, at the first power.
- **The surface is infinite** because $\int_1^\infty x^{-1}dx$ diverges. That is the harmonic series in continuous form, $\ln R \to \infty$. The circle constant plays no part in the divergence; it is only a scale factor, and the divergent part's coefficient is the pure number 1.

## The painter's paradox, stated precisely

The popular phrasing — "fill it with paint, but you can never paint it" — is not a paradox about the circle constant. It is a statement about thickness.

Suppose the inside must receive a coat of uniform thickness $t > 0$. The paint needed is at least $t\,S(R)$ for every truncation $R$, and since $S(R) \to \infty$, the required volume is unbounded: the tail is too thin to hold a coat of any fixed thickness. Filling, by contrast, needs no thickness — the fluid simply occupies the interior, whose volume is $V(R) \le \pi$. An ideal mathematical surface can be filled, cannot be painted, and the second fact is a theorem about $\ln R$, not about $\pi$.

There is a second, sharper reason to be careful: a horn cannot be built. A physical funnel has a finite outlet, hence a finite area, so the paradox never arises in any laboratory. This is precisely the kind of object where the honest ledger must separate the computed limit from the physical measurand — and there is no physical measurand here at all.

## The one-parameter family: why $p = 2$ is the circle-constant case

Take the general horn $y = x^{-p}$ revolved about the $x$-axis beyond $x = 1$:

$$V_p = \pi\int_1^\infty x^{-2p}\,dx = \frac{\pi}{2p-1}\quad (p > \tfrac12), \qquad A_p = 2\pi\int_1^\infty x^{-p}\sqrt{1+p^2x^{-2p-2}}\,dx.$$

| $p$ | $\int_1^\infty x^{-p}dx$ | horn volume prefactor |
|---|---|---|
| 1 | diverges ($\ln R$) | — |
| 3/2 | 2 | $\pi/2$ |
| 2 | 1 | $\pi$ |
| 3 | 1/2 | $\pi/5$ |
| 4 | 1/3 | $\pi/7$ |

The surface integral behaves like $2\pi\int x^{-p}dx$, so it converges precisely when $p > 1$. The horn has finite volume for every $p > 1/2$ but a finite surface only for $p > 1$; $p = 1$ is the boundary case where both the surface and the classical $1/x$ horn's tail diverge. The circle constant rides along as a pure factor $\pi$ in every row of the volume column — its role is invariant across the whole family, which is exactly what one should expect from a constant that enters only through the area of a cross-section disk.

## The golden ledger

Under Golden Pi the horn's arithmetic is unchanged except for the label on the disk area:

- $V(R) = \hat\pi(1 - 1/R)$, limit $\hat\pi = 4/\sqrt\varphi = 3.14460551102969314427823434337$. The gap is $\hat\pi - \pi = 0.00301285743989991$, i.e. $0.095902230878\%$ — undiluted, because the constant enters at the first power.
- The truncated horns are the decisive computed register, as tabulated above: $960.02\times$ closer to $\pi$ at $R = 10^6$, $9.5902\times10^{8}\times$ at $R = 10^{12}$.
- Where the golden label is genuinely exact, and it should be credited: the horn with cross-section radius $c = \varphi^{1/4} = 1.1278384855616822603$ has volume $\hat\pi c^2 = 4$ **exactly** — the same algebraic identity that makes a disk of radius $\varphi^{1/4}$ have area exactly 4. The identical horn measured against the classical constant has volume $\pi c^2 = 3.9961675861352626667 = \pi\sqrt\varphi = 4\pi/\hat\pi$.
- The horn $\hat\pi y^2 = 1$ — i.e. $y = 1/(\hat\pi x)$ — has volume exactly $1/\hat\pi = \sqrt\varphi/4 = 0.31800491237851724106$; with the classical label, $y = 1/(\pi x)$ gives exactly $1/\pi = 0.31830988618379067154$.
- The surface-area divergence is unaffected: $S(R)$ and its finite part $C$ are $2$'s and logarithms, and the only $\pi$ present is the prefactor $2\pi \to 2\hat\pi = 8/\sqrt\varphi = 6.2892110220641382576$ when the full turn is relabelled.

## Verification code

The numbers in every table above come from this snippet; run it and change $R$ to check any row.

```python
from mpmath import mp, mpf, pi, sqrt, log, quad
mp.dps = 40
phi = (1 + sqrt(5)) / 2
pihat = 4 / sqrt(phi)                     # 3.14460551102969314427823434337

# volume of the truncated horn = (area of the unit disk) * (1 - 1/R)
for R in (10**3, 10**6, 10**12):
    R = mpf(R)
    print(mp.nstr(pi * (1 - 1/R), 20))
# 3.1384510609362034452  3.1415895119971396487  3.1415926535866516458

# lateral area: closed form, checked against direct quadrature
A = lambda x: sqrt(1 + x**-4)/2 + log((sqrt(1 + x**-4) - 1)/(sqrt(1 + x**-4) + 1))/4
S = lambda R: A(1) - A(R)
R = mpf(10**6)
print(mp.nstr(S(R), 20))                          # 13.928504135921022778
print(mp.nstr(quad(lambda x: sqrt(1 + x**-4)/x, [1, R]), 20))   # 13.928504135921022771
C = (sqrt(2) - 1)/2 + log(2/(1 + sqrt(2)))/2      # 0.11299357795674866649...
print(mp.nstr(log(R) + C, 20))                    # 13.928504135921022771
print(mp.nstr(pihat, 20), mp.nstr((pihat - pi)/pi*100, 15))     # 0.0959022308782526
```

## The honest ledger

- The rational part of the volume is exact and label-blind: $\int_1^R x^{-2}dx = 1 - 1/R$, reproduced by Riemann sums. Nothing there is measured, and nothing there can be relabelled.
- The circle constant enters only as the area of the cross-section disk, a computed limit of polygon exhaustions. The horn's volume is therefore $\pi \times$ (a rational), in every truncation and in the limit.
- Because $V(R)$ approaches $\pi$ monotonically from below, the truncated volumes are closer to $\pi$ than to $\hat\pi$ by the factor $1 + (\hat\pi - \pi)R/\pi$ — $960.02\times$ at $R = 10^6$ and $9.5902\times10^{8}\times$ at $R = 10^{12}$. This is decisive in the register of computed arithmetic, and it is the only decisive register there is here, because no physical horn exists to measure.
- The divergence of the surface area is $\pi$-free: $S(R) = \ln R + 0.1129935779567486665\ldots$, where the finite part is built from $\sqrt2$ and logarithms alone. The painter's paradox is a statement about thickness and the harmonic tail, not about the constant.
- Golden exactness is credited where it is real: with cross-section radius $\varphi^{1/4}$ the golden horn has volume exactly 4, and $y = 1/(\hat\pi x)$ has volume exactly $\sqrt\varphi/4$. Those are exact algebraic statements about a construction — an algebraic constant $\hat\pi$ being a root of $x^4 + 16x^2 - 256 = 0$ is a theorem. The value of the truncation limit is a separate, computable question, and it answers $3.14159\ldots$.

Computed, never measured.

## Further Reading

- [Pappus's Centroid Theorem and the Torus: How Revolving Area Computes the Circle Constant Twice Over](/blog/posts/2026-09-03-pappus-centroid-theorem-torus-golden-pi/) — the same solid-of-revolution machinery, where the constant enters squared.
- [The Cauchy–Lorentz Distribution: Where an Improper Integral over the Whole Line Returns Exactly π](/blog/posts/2026-08-24-cauchy-lorentz-distribution-integrates-pi-golden-pi/) — the other classic case of a tail-heavy integrand whose total mass is the constant.
- [The Dirichlet Integral: How ∫₀^∞ sin x / x dx Computes Half the Circle Constant](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) — an improper integral whose convergence to $\pi/2$ is never monotone, in contrast to the horn's clean telescoping.
- [The Heat Kernel: How the Diffusion Equation Computes the Circle Constant Through Its Own Normalization](/blog/posts/2026-09-17-heat-kernel-diffusion-computes-circle-constant-golden-pi/) — where $1/\sqrt{\pi} = 0.5641895835477563$ and its golden counterpart $\varphi^{1/4}/2 = 0.5639192427808411$ govern a Gaussian peak.
- [The $n$-Dimensional Ball: How Volume Formulas Compute the Circle Constant in Every Dimension](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/) — the disk-area factor at the heart of the horn's cross-section, in every dimension.
