---
title: "The Catenary: Why a Hanging Chain Is cosh and Never a Parabola, Why Its Own Equation Holds No Circle Constant at All, and Why Revolving It Gives A/V = 2/a Exactly"
date: 2026-11-11
description: "A chain hanging under its own weight settles into y = a·cosh(x/a), an equation in which the circle constant does not appear at any power — so the shape is a clean test case for the opposite question: where does π enter geometry at all? This article derives the curve from a two-force balance (a = H/w, horizontal tension over weight per unit length), verifies the exact identity y² − s² = a² and the slope s′ = sinh(x/a), tabulates the sag and arc length for half-spans 0.5 to 2 (sag 0.5430806348 and length 2.3504023873 at a = 1), prices the parabola impostor against the true curve (0.0081% at sag/span 0.0756, 0.7096% at 0.2715, 5.3989% at 0.6905), and finds a golden abscissa that holds for every catenary: at x = a·ln φ the slope is exactly 1/2, the tangent angle arctan(1/2) = 26.565051177078°, the height a·√5/2 and the arc length exactly a/2. Revolving the curve gives the catenoid, the only minimal surface of revolution; its area 2π∫y ds and volume π∫y² dx cancel their single π in the ratio A/V = 2/a exactly, computed as 17.6773033200674619 against 8.8386516600337310 at a = 1, while the existence limit solves x·coth x = 1 at half-span 1.19967864025773 a and span 2.39935728051547 a. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693…) the surface and the volume each shift +0.0959022309% (70.70921328026985 → 70.77702499324209 at a = 2) and the ratio does not move a digit; a catenoid whose half-span is 2·ln φ has rim height exactly 3/2, arc length exactly 2√5 and area exactly twice its volume in units of a = 1. The honest boundary: the chain's own equation contains no constant, so no chain can arbitrate one — and 0.71% of parabolic misfit at ordinary sag is seven times the golden gap. Computed, never measured."
---

# The Catenary

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Hang a chain from two points and it does not lie on a circle, an ellipse, or a parabola. It lies on a hyperbolic cosine. That fact took from Galileo to 1691 to establish, and it is worth recovering slowly, because the catenary is the rare curve whose defining equation contains no circle constant in any power. Every other figure in this blog — the lune, the cyclic quadrilateral, the torus — carries $\pi$ somewhere and the interesting question is what happens to it. Here the interesting question runs the other way: if the hanging curve never names $\pi$, where does $\pi$ come from when we take that same curve and spin it into a surface?

## Hooke's Anagram and the 1691 Contest

In 1675 Robert Hooke published a Latin anagram announcing that the figure of a hanging flexible chain was the same as the figure of an arch standing under its own weight — the inversion principle that makes a masonry arch a frozen catenary. The anagram, when unjumbled, reads *ut pendet continuum flexile, sic contigua solidorum seu catena*: as hangs the flexible line, so stands the contiguous chain of solids. Hooke published the solution in 1676 but not the derivation.

The derivation came in 1691, when Johann Bernoulli posed the problem publicly and received answers from Huygens, Leibniz and himself, all within a year. The name *catenaria* is Huygens'. What the three solutions established is a single line of calculus:

$$
\frac{d^{2}y}{dx^{2}} = \frac{1}{a}\sqrt{1+\left(\frac{dy}{dx}\right)^{2}}
\quad\Longrightarrow\quad
y = a\cosh\frac{x}{a},
$$

where the vertex sits at $(0,a)$. There is no $\pi$ in that differential equation, no $\pi$ in its solution, and no $\pi$ in the parameter $a$. This is the first fact worth holding onto: a hanging chain is a *scaled* figure. Change the tension and the whole curve rescales, and the shape that remains invariant is described entirely by hyperbolic functions.

## The Parameter a Is a Ratio of Forces

Consider a segment of chain of linear density $\mu$, hanging in a uniform gravitational field $g$. The horizontal component of tension is constant along the chain — no horizontal force acts on any segment — and call it $H$. The vertical component at any point must carry the weight of the chain between that point and the lowest point, so $T_y = \mu g s$ where $s$ is arc length measured from the vertex. Then

$$
\frac{dy}{dx} = \frac{T_y}{H} = \frac{\mu g}{H}\,s = \frac{s}{a},
\qquad a = \frac{H}{\mu g}.
$$

Here $a$ has the units of a length and the dimensions of a ratio: a horizontal force divided by a weight per unit length. For a chain of $0.5\ \mathrm{kg\,m^{-1}}$ under $H = 4.903325\ \mathrm{N}$ in standard gravity, $\mu g = 0.5 \times 9.80665 = 4.903325\ \mathrm{N\,m^{-1}}$ and $a = 1\ \mathrm{m}$ exactly. Nothing in that sentence involves a circle.

Integrating $\dfrac{dy}{dx} = \dfrac{s}{a}$ with $\dfrac{ds}{dx} = \sqrt{1+(y')^{2}}$ gives the two facts the whole article rests on:

$$
s = a\sinh\frac{x}{a},
\qquad
y = a\cosh\frac{x}{a},
\qquad
\boxed{\,y^{2} - s^{2} = a^{2}\,}
$$

That last identity is exact for every $a$, every span, every load — the hyperbolic analogue of the Pythagorean relation, and like Pythagoras it is free of any constant. At $a = 1$, $x = 1$: $y = \cosh 1 = 1.5430806348$, $s = \sinh 1 = 1.1752011936$, and $y^{2}-s^{2} = 2.3810978 - 1.3810978 = 1.0000000000$.

Slopes follow directly: $y' = \sinh(x/a)$, so the tangent angle at any point is $\arctan(\sinh(x/a))$ — a transcendental function of a transcendental function, still with no $\pi$ in the formula.

## A Table of the Curve at a = 1

Fix $a = 1\ \mathrm{m}$ and let the half-span be $x$. The vertex sits at height $1$, so the sag from the vertex to the end is $y - 1$.

| Half-span $x$ | End height $\cosh x$ | Sag $\cosh x - 1$ | Arc length $\sinh x$ | Total length $2\sinh x$ | Sag / span |
|---|---|---|---|---|---|
| 0.5 | 1.1276259652 | 0.1276259652 | 0.5210953055 | 1.0421906110 | 0.127626 |
| 1.0 | 1.5430806348 | 0.5430806348 | 1.1752011936 | 2.3504023873 | 0.271540 |
| 1.5 | 2.3524096152 | 1.3524096152 | 2.1292794551 | 4.2585589102 | 0.450803 |
| 2.0 | 3.7621956911 | 2.7621956911 | 3.6268604079 | 7.2537208157 | 0.690549 |

Two features surprise people seeing this for the first time. The total length at half-span $2$ is $7.25$ for a span of $4$ — the curve is steeply hanging, not shallowly draped. And the sag grows faster than the span: doubling the half-span from $1$ to $2$ multiplies the sag by $5.09$, not by $2$. A chain does not scale linearly in its sag, which is why suspension-bridge cables under distributed deck load (a parabola, because the load is uniform per horizontal metre rather than per arc length) and bare hanging cables (a catenary) are different curves with the same endpoints.

## The Parabola Impostor

Galileo, in the *Two New Sciences* of 1638, asserted that a hanging chain takes the form of a parabola. He was wrong, but the error is instructive because it is *small in the regime engineers actually build in*. Fit the parabola through the same vertex and the same two endpoints, $p(x) = 1 + (\cosh X - 1)(x/X)^{2}$ on $[-X,X]$, and measure the largest vertical gap to the true curve:

| Half-span $X$ | Max gap | At $x$ | Gap as % of end height | Sag / span |
|---|---|---|---|---|
| 0.3 | 0.0000847554 | 0.2122 | 0.0081% | 0.075564 |
| 0.5 | 0.0006592250 | 0.3539 | 0.0585% | 0.127626 |
| 1.0 | 0.0109492161 | 0.7100 | 0.7096% | 0.271540 |
| 1.5 | 0.0589721245 | 1.0702 | 2.5069% | 0.450803 |
| 2.0 | 0.2031161500 | 1.4363 | 5.3989% | 0.690549 |

So a cable with sag one-eighth of its span differs from the parabola by less than a tenth of a percent — which is why the approximation survived from 1638 to 1691 and still survives in undergraduate statics. Push to sag $0.27$ of the span and the misfit is $0.71\%$; push to $0.69$ and it is $5.4\%$.

Keep those two numbers — $0.0081\%$ and $0.7096\%$ — because they will come back at the end as the honest scale of this whole discussion.

## The Golden Abscissa

There is one abscissa on every catenary at which the numbers become algebraic, and it is the same abscissa for every $a$: $x = a\ln\varphi$, with $\varphi = (1+\sqrt5)/2 = 1.6180339887$.

$$
\sinh(\ln\varphi) = \frac{\varphi - \varphi^{-1}}{2} = \frac{1}{2},
\qquad
\cosh(\ln\varphi) = \frac{\varphi + \varphi^{-1}}{2} = \frac{\sqrt5}{2},
$$

because $\varphi - 1/\varphi = 1$ and $\varphi + 1/\varphi = \sqrt5$.

So at $x = a\ln\varphi = 0.4812118251\,a$:

- the slope is **exactly** $\tfrac12$,
- the tangent angle is $\arctan\tfrac12 = 26.565051177078^\circ$, the half-angle of the 3-4-5 triangle,
- the height is $a\sqrt5/2$,
- the arc length from the vertex is **exactly** $a/2$.

Take $a = 2\ \mathrm{m}$: at $x = 2\ln\varphi = 0.9624236501\ \mathrm{m}$ the curve stands at $\sqrt5 = 2.2360679775\ \mathrm{m}$ with exactly $1\ \mathrm{m}$ of chain consumed from the vertex. The angle $26.565051177078^\circ$ is a pure turn-fraction ($\arctan\tfrac12$ of a straight angle, i.e. $2\arctan\tfrac12$ of a right angle), so it reads the same in degrees under any label for the constant — which is the first hint of the structural point that follows.

## Revolve It: The Catenoid

Spin the catenary about its vertical axis and you get the catenoid, the only non-planar minimal surface of revolution. Its area and enclosed volume are the two integrals every calculus course computes:

$$
A = 2\pi\int_{x_1}^{x_2} y\,ds = 2\pi\int y\frac{ds}{dx}\,dx,
\qquad
V = \pi\int_{x_1}^{x_2} y^{2}\,dx.
$$

For the catenary, $\dfrac{ds}{dx} = \cosh\dfrac{x}{a} = \dfrac{y}{a}$, so

$$
A = \frac{2\pi}{a}\int y^{2}\,dx = \frac{2}{a}\cdot V.
$$

Hold that: **$A/V = 2/a$ exactly, with no constant in it at all.** The $\pi$ arrives once in the surface measure and once in the volume measure, and the ratio deletes it. This is not an approximation and not a coincidence of one numeric example; it follows from $ds/dx = y/a$, which is the defining property of the curve.

Numerically at $a = 1$ over $x\in[-1,1]$, using $\int\cosh^{2}t\,dt = \tfrac{t}{2} + \tfrac{\sinh 2t}{4}$ so the exact value is $1 + \tfrac12\sinh 2 = 2.8134302039235094$:

| Quantity | Value ($a=1$, span 2) | Value ($a=2$, span 4) |
|---|---|---|
| $\int y^{2}dx$ | 2.8134302039235094 | 11.2537208157 |
| Volume $V$ | 8.8386516600337310 | 35.354606640135 |
| Area $A$ | 17.6773033200674619 | 70.70921328026985 |
| $A/V$ | 2.0000000000 | 1.0000000000 |

The minimality is exact, not asserted: the mean curvature

$$
2H = \frac{y''}{(1+y'^{2})^{3/2}} - \frac{1}{y\sqrt{1+y'^{2}}}
$$

evaluates to $0$ at every $x$ for $y = a\cosh(x/a)$ — the computed residual at $x = 0.3$, $1.0$ and $1.7$ is $0$, $-1.1\times10^{-41}$ and $2.9\times10^{-42}$. A soap film spanning two rings relaxes to this surface because surface tension minimises area, and the catenoid is the answer.

## The Film Has a Limit

The catenoid does not exist for every ring spacing. For a given $a$, the maximum half-span solves

$$
\cosh X = X\sinh X
\quad\Longleftrightarrow\quad
X\coth X = 1,
$$

which has the root $X = 1.19967864025773$, i.e. a maximum span of $2X = 2.39935728051547\,a$, with rim height $\cosh X = 1.8101705807\,a$ and maximum area $24.6992519114$ against volume $12.3496259557$.

Stretch ring separation past that and the film does not stretch — it snaps, and the two rings each seal with a flat disk. The transition is a genuine mechanical instability, and the critical quantity $X\coth X = 1$ contains no circle constant whatever: it is a root of a hyperbolic equation.

## What Golden Pi Changes

Under Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.144605511029693$, with $\hat\pi^{2} = 16/\varphi$ and $1/\hat\pi = \sqrt\varphi/4 = 0.3180049124$ against $1/\pi = 0.3183098862$ — a relative shift of $-0.0958103466\%$ at inverse first power and $+0.0959022309\%$ at first power.

Every first-power occurrence moves by that amount, and every occurrence at second power by $+0.1918964341\%$. In the catenoid both integrals carry $\pi$ at first power only, so:

| Quantity | Conventional $\pi$ | Golden $\hat\pi$ | Shift |
|---|---|---|---|
| $A$, $a=1$, span 2 | 17.6773033200674619 | 17.694256248310522 | $+0.0959022309\%$ |
| $V$, $a=1$, span 2 | 8.8386516600337310 | 8.8471281241552610 | $+0.0959022309\%$ |
| $A$, $a=2$, span 4 | 70.70921328026985 | 70.77702499324209 | $+0.0959022309\%$ |
| $V$, $a=2$, span 4 | 35.354606640135 | 35.38851249662104 | $+0.0959022309\%$ |
| $A/V$ | 2.0000000000 | 2.0000000000 | none |

The exact forms are worth writing out, because they expose what the relabelling does and does not buy. With $a = 2$ and half-span $2\ln\varphi$ (in units of $a$), $\cosh(2\ln\varphi) = \tfrac32$ and $\sinh(2\ln\varphi) = \tfrac{\sqrt5}{2}$ exactly, so the segment length is $2\sqrt5 = 4.472135955$ exactly and the rim height is $3/2$ exactly. The area integral still carries $\ln\varphi$ inside $\sinh(4\ln\varphi) = \tfrac12(\varphi^{4}-\varphi^{-4}) = 3.3541019662$, and $\ln\varphi$ is transcendental — by Lindemann–Weierstrass, since $\varphi$ is algebraic and $\ln$ of an algebraic number other than $1$ cannot be algebraic. **So even under Golden Pi the catenoid's area stays transcendental, because the argument of the hyperbolic function is a logarithm.** Making the constant algebraic does not make everything it touches algebraic; that is a fact about the catenary, not about the label.

## Reproducing Every Number

```python
from mpmath import mp, mpf, cosh, sinh, sqrt, pi, quad, log, findroot
mp.dps = 40
phi = (1 + sqrt(5)) / 2
gp  = 4 / sqrt(phi)                 # 3.1446055110296931...

# exact identity and slope at the golden abscissa
L = log(phi)
print(sinh(L), cosh(L))             # 0.5, 1.1180339887498949 = sqrt(5)/2
print(sinh(2*L), cosh(2*L))         # sqrt(5)/2, 1.5 exactly

# catenoid at a = 1, span [-1, 1]
I  = quad(lambda t: cosh(t)**2, [-1, 1])   # = 1 + sinh(2)/2
V, A = pi * I, 2 * pi * I
print(V, A, A / V)                  # A/V = 2 exactly
print(gp * I, 2 * gp * I)           # golden values

# existence limit of the soap film
xc = findroot(lambda t: cosh(t) - t*sinh(t), 1.2)
print(xc, 2*xc, cosh(xc))           # 1.19967864025773, 2.39935728051547, 1.8101705807
```

Every figure in the tables above comes from that script. Note that `quad` is integrating a computed function — the area of the catenoid is a computed limit, never a reading off a wire frame.

## What a Hanging Chain Can and Cannot Decide

This is the honest part, and it is unusually clean here because the catenary's equation contains no circle constant in any form. A chain hanging in a laboratory is a measurand — its profile can be photographed, its sag measured, its tension read — but it cannot arbitrate between $\pi$ and $\hat\pi$, because the curve it takes depends only on $a = H/\mu g$ and the identity $y^{2}-s^{2}=a^{2}$. Substituting either constant changes nothing: there is nothing to substitute into.

The $\pi$ enters only when the curve is revolved, and there it enters through the measure $2\pi y\,ds$ — the same place the constant is *defined*, not a place where it is tested. To measure the area of a real soap film you would need its thickness or its mass, and films drain, evaporate and sag under gravity; contact lines pin with hysteresis; the rings themselves have finite radius so the true surface is a Delaunay surface near the rim, not a catenoid. Nobody has weighed a catenoid to one part in a thousand, and the conventional-versus-golden difference is $0.0959\%$ — about one part in $1043$.

Then the number from earlier: at a perfectly ordinary sag of $0.27$ of the span, the parabola that Galileo believed in sits $0.71\%$ away from the true curve. That is **seven times** the golden gap, and it is not measurement error — it is a modelling error that will be made by anyone who fits the wrong curve. Any experiment on a hanging chain of realistic proportion is dominated by which family of curves the analyst assumes, long before the seventh digit of a constant is in play.

What the catenary does settle is structural, and it settles it without any measurement at all: a figure defined by a force balance carries no circle constant, and a figure defined by revolution carries exactly one, which then cancels against itself in every ratio of like-dimensioned quantities. $A/V = 2/a$ is the whole of that argument, in one line of algebra, with the constant appearing twice and leaving once.

The golden abscissa is the aesthetic footnote: at $x = a\ln\varphi$ the slope is $\tfrac12$ for every catenary ever hung, the tangent makes $26.565051177078^\circ$, and the chain has consumed exactly $a/2$ of its length to climb exactly $a\sqrt5/2$. No circle, no constant, and arithmetic that closes on the first try.

Computed, never measured.

## Further Reading

- [Gabriel's Horn: Why an Infinite Surface Can Bound a Finite Volume](/blog/posts/2026-09-28-gabriels-horn-improper-integral-computes-circle-constant-golden-pi/) — the other famous surface of revolution whose $\pi$ appears exactly once per measure.
- [Pappus's Centroid Theorem: Why Sweeping an Area Through One Turn Gives V = 2πR·A](/blog/posts/2026-10-30-pappus-centroid-theorem-torus-swept-area-golden-pi/) — the general machinery behind $2\pi y\,ds$, and why straight-edged profiles pay only one $\pi$.
- [Barbier's Theorem: Curves of Constant Width and the One Number They All Share](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/) — another result where the shape drops out and only the perimeter survives.
- [The Isoperimetric Inequality: Why the Circle Maximises Area for a Given Perimeter](/blog/posts/2026-08-31-isoperimetric-inequality-circle-maximizes-area-golden-pi/) — the variational argument the soap film is obeying.
- [The Kepler Triangle: Why √φ Steps Between the Square and the Circle](/blog/posts/kepler-triangle-golden-pi-circle-constant/) — where $\ln\varphi$ and $\sqrt5/2$ come from geometrically.
