---
title: "The Witch of Agnesi: Why a Curve Traced by Straight Lines Encloses Exactly Four Times the Generating Circle, Why Its Arc Length Is Infinite and Its Area Finite, and What Golden Pi Changes"
date: 2026-11-17
description: "Grandi's construction draws a curve from a single circle using nothing but straight lines — a chord from the origin, a tangent, and a horizontal — and the curve it produces, y = 8a³/(x² + 4a²), encloses exactly 4πa² between itself and its asymptote: the area of a circle of radius 2a, and exactly four times the generating circle. This article derives the equation from the construction, proves the quadrature by the arctangent integral, and shows that the enclosed fractions are exact turn-fractions — one sixth of the area lies within |x| ≤ 2a/√3, one quarter within |x| ≤ 2a, one third within |x| ≤ 2a√3 — so the constant appears once and the bookkeeping around it is π-free. It then computes the shape: unit curvature at the vertex with the generating circle as the osculating circle, inflection points at x = ±2a/√3 and y = 3a/2, slope −0.6495190528 (−33.0044916°) there, and the inverse-square tail that makes the arc length diverge logarithmically in width while the area stays 4πa² = 12.566370614 — a Gabriel's horn drawn in the plane, with 4.5183 of length inside |x| ≤ 2a against 200.7378 inside |x| ≤ 100a. Revolving the figure about its asymptote gives V = 4π²a³ = 39.4784176044, the one place the constant is squared, and the centroid sits at exactly a/2 by two independent routes, Pappus and direct integration. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the area becomes exactly 16a²/√φ and the volume exactly 64a³/φ — algebraic, degree two — while the centroid, every enclosed fraction and the whole construction do not move a digit. Computed, never measured."
---

# The Witch of Agnesi

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Draw a circle. Pick a point on it. From that point, send out a line at any angle — it cuts the circle again, and it cuts a horizontal tangent line somewhere out to the side. Now do something that looks almost like a mistake: take the *height* from the second crossing and the *width* from the tangent, and mark the point that combines them. Sweep the line through every angle and those marks trace a curve.

The curve is called the witch of Agnesi. It looks like a bell with a long, flat tail, and it has a property that ought to be impossible in this company: the area between the curve and its asymptote is **exactly** the area of a circle of radius $2a$ — exactly four times the area of the circle that generated it. No approximation, no limit quoted to twenty digits. An equality.

That is not a squaring of the circle in the classical sense — no straightedge-and-compass construction is involved, and Lindemann's 1882 theorem is untouched. But it is an exact quadrature between two curvilinear figures, and it is the cleanest example in the whole of classical geometry of a curve built entirely from straight lines whose enclosed area is a circle's area with nothing left over.

This article derives the curve from its construction, proves the area identity, maps exactly where the area sits, and then does what a curve of finite area and infinite perimeter forces you to do: count carefully. At the end, the golden substitution.

## The Construction, and Why the Equation Is What It Is

Let the generating circle have radius $a$ and sit with its centre at $(0,a)$, so it touches the origin and its top is the line $y = 2a$. From the origin $O$ draw a ray of slope $m$:

$$
y = mx .
$$

It meets the circle where $x^{2} + y^{2} = 2ay$. Substituting gives $x^{2}(1+m^{2}) = 2amx$, whose non-zero root is the second crossing

$$
x_{D} = \frac{2am}{1+m^{2}}, \qquad y_{D} = \frac{2am^{2}}{1+m^{2}} .
$$

The same ray meets the tangent line $y = 2a$ at $x_{E} = 2a/m$. Grandi's point is the combination $P = (x_{E},\, y_{D})$:

$$
x = \frac{2a}{m}, \qquad y = \frac{2am^{2}}{1+m^{2}} .
$$

Eliminate $m = 2a/x$:

$$
y = \frac{2a\left(\dfrac{4a^{2}}{x^{2}}\right)}{1 + \dfrac{4a^{2}}{x^{2}}}
  = \frac{8a^{3}}{x^{2} + 4a^{2}} .
$$

$$
\boxed{\,y(x) = \frac{8a^{3}}{x^{2}+4a^{2}}\,}
$$

Every feature of the curve is now inspection. At $x = 0$ the height is $2a$, the top of the generating circle, so the curve peaks exactly at the circle's apex. At $x = 2a$ the height is $8a^{3}/(8a^{2}) = a$ — the curve passes through the point $(2a, a)$, a square of side $a$ measured from the origin. At $x = 2a\sqrt3$ the height is $8a^{3}/(16a^{2}) = a/2$. The tail is inverse-square:

$$
y \sim \frac{2a^{3}}{x^{2}} \quad (x \gg a),
$$

the same decay law as an inverse-square field, which is the source of everything strange about this curve's perimeter.

The trigonometric form is worth having, because it makes the geometry visible. Writing $x = 2a\cot\theta$ turns $x^{2}+4a^{2} = 4a^{2}\csc^{2}\theta$ and gives

$$
x(\theta) = 2a\cot\theta, \qquad y(\theta) = 2a\sin^{2}\theta, \qquad 0 < \theta \le \frac{\pi}{2},
$$

so the height is twice the square of a sine — the *versed sine* scaled — which is precisely where the name comes from. Grandi called it *la versiera*, from the Latin *vertere*, to turn; in 1748 Maria Gaetana Agnesi gave it a full treatment in the *Instituzioni analitiche*; and John Colson's 1801 English translation rendered *versiera* as "witch", through confusion with *avversiera*, the devil's wife. The usual account is that a mistranslation gave the curve its English name. Fermat had studied the same curve in the 1630s, so the mathematics is older than either name.

## The Exact Quadrature

The area between the curve and the $x$-axis is the arctangent integral. With $u = x/2a$:

$$
A = \int_{-\infty}^{\infty} \frac{8a^{3}}{x^{2}+4a^{2}}\,dx
  = 8a^{3}\cdot\frac{1}{2a}\Bigl[\arctan\frac{x}{2a}\Bigr]_{-\infty}^{\infty}
  = 4a^{2}\cdot\pi .
$$

$$
\boxed{\,A = 4\pi a^{2}\,}
$$

For $a = 1$: $A = 12.56637061435917$. That is the area of a circle of radius $2a$ — and four times the area of the generating circle, $\pi a^{2}$. The identity is exact because the arctangent's total rise is exactly $\pi/2$ per half-line and the prefactor $4a^{2}$ is exactly the reciprocal of what the substitution produced. Nothing is being approximated: the prefactor and the arctangent limit cancel into an integer multiple.

The same integral run from $-X$ to $X$ gives the enclosed fraction, and here the numbers arrange themselves into exact turn-fractions:

$$
\frac{A(X)}{A} = \frac{2\arctan(X/2a)}{\pi} .
$$

| $X$ | $y(X)$ | $A(X)/A$ | exact? |
|---|---|---|---|
| $2a/\sqrt3 = 1.154700538379$ | $1.5a$ | $16.6666667\%$ | exactly $1/6$ |
| $a$ | $1.6a$ | $14.7583618\%$ | $\arctan(1/2)/\pi$ |
| $2a$ | $a$ | $25.0000000\%$ | exactly $1/4$ |
| $2a\sqrt3 = 3.464101615138$ | $0.5a$ | $33.3333333\%$ | exactly $1/3$ |
| $4a$ | $0.4a$ | $35.2416382\%$ | $\arctan 2/\pi$ |
| $10a$ | $0.076923a$ | $43.7167042\%$ | $\arctan 5/\pi$ |
| $100a$ | $0.00079968a$ | $49.363465\%$ | $\arctan 50/\pi$ |

Three of those rows are exact and π-free once written as turn-fractions: the curve holds **one sixth** of its area inside $|x| \le 2a/\sqrt3$, **one quarter** inside $|x| \le 2a$, **one third** inside $|x| \le 2a\sqrt3$. The widths are $2a\tan30°$, $2a\tan45°$, $2a\tan60°$ — the widths are tangents of exact turn-fractions, which is why the areas are exact turn-fractions too. That is the whole mechanism of the quadrature in one sentence: the arctangent converts width into angle, the angle is a turn-fraction, and the $\pi$ in the denominator is the same $\pi$ that converts a turn into radians. Divide one by the other and it is gone.

Two rows are worth reading as geometry rather than arithmetic. At $X = 2a$ the curve is at height $a$ and has enclosed exactly a quarter of its own area; the "core" of the curve is a square of side $a$ cut by the curve, and the other three quarters of the area lies outside it. At $X = 2a\sqrt3$ the height is exactly half the centroid height computed below, and a third of the area is enclosed.

Scaling note, since conventions differ: some sources write the witch as $y = a^{3}/(x^{2}+a^{2})$, with area $\pi a^{2}$. That is the same curve with the circle's radius relabelled; the version built from the construction above carries the factor 4 in the denominator and therefore the factor 4 in the area. Both statements are correct about their own parametrisation, and the fourfold relation to the generating circle holds only for the construction-derived form.

## Curvature, Inflections, and the Osculating Circle

Differentiate twice:

$$
y' = -\frac{16a^{3}x}{(x^{2}+4a^{2})^{2}}, \qquad
y'' = \frac{16a^{3}\left(3x^{2}-4a^{2}\right)}{(x^{2}+4a^{2})^{3}} .
$$

At the vertex $x = 0$: $y' = 0$ and $y'' = -16a^{3}/(64a^{4}) = -1/a$, so the curvature is $\kappa = 1/a$ and the radius of curvature is **exactly** $a$. The osculating circle at the peak of the witch is the generating circle itself, sitting on the axis at the origin. The curve is born with the curvature of the circle it came from and then unwinds from it.

The second derivative vanishes where $3x^{2} = 4a^{2}$, that is at

$$
x = \pm\frac{2a}{\sqrt3} = \pm 1.1547005383792515\,a, \qquad y = \frac{3a}{2},
$$

so the inflections sit exactly above and below at one and a half times the generating radius — and, by the table above, at the width that encloses exactly one sixth of the area. The slope there is

$$
y'\!\left(\frac{2a}{\sqrt3}\right) = -\frac{16a^{3}\cdot 2a/\sqrt3}{\left(4a^{2}/3+4a^{2}\right)^{2}} = -\frac{32a^{4}/\sqrt3}{\left(16a^{2}/3\right)^{2}} = -\frac{3\sqrt3}{8} = -0.6495190528383290,
$$

an angle of $-33.0044916°$ below horizontal. That the slope at inflection is algebraic while the height is rational is the ordinary state of affairs; what matters is that no circle constant enters either.

## Finite Area, Infinite Perimeter

Take the arc-length integrand $\sqrt{1+y'^{2}}$. Because $y' \sim -16a^{3}/x^{3}$ for large $x$, the integrand tends to $1$ from above — every far segment of the curve contributes its own width in length and no more. The accumulated length from $-X$ to $X$ therefore grows without bound, linearly, while the area converges geometrically fast:

| $X$ | arc length, $-X$ to $X$ | enclosed fraction of area |
|---|---|---|
| $0.5a$ | $1.0350163a$ | $7.797913\%$ |
| $a$ | $2.1845552a$ | $14.758362\%$ |
| $2a$ | $4.5183464a$ | $25.000000\%$ |
| $2a\sqrt3$ | $7.6209944a$ | $33.333333\%$ |
| $4a$ | $8.7114268a$ | $35.241638\%$ |
| $10a$ | $20.7373814a$ | $43.716704\%$ |
| $100a$ | $200.7378391a$ | $49.363465\%$ |

Read the last two rows together. Going from $X = 10a$ to $X = 100a$ multiplies the arc length by roughly ten — $20.74 \to 200.74$, which is $180$ of new length for $90$ of new width — while the enclosed area rises from $43.72\%$ to $49.36\%$ of its total. Half the area is never reached; the length is unbounded. The curve is a Gabriel's horn drawn in the plane: finite area, infinite perimeter, and a tail that is $6.28\%$ of the area beyond $10a$ and $0.64\%$ beyond $100a$ while contributing infinite length.

This is the honest constraint on any physical realisation. A drawn witch, a wire witch, a 3-D-printed witch all have finite perimeter because they are truncated; the mathematical object does not. Nothing about the golden substitution changes this — the divergence is a statement about $y \sim x^{-2}$, and $x^{-2}$ has nothing to do with any circle constant.

There is one more divergence, and it is instructive. The first moment of the area about the $y$-axis, $\int x\,y\,dx$, behaves like $\int 8a^{3}x/x^{2}\,dx = 8a^{3}\ln x$ — logarithmically divergent. So a half of the witch has infinite moment about the $y$-axis even though the whole figure is symmetric about it. The symmetry saves the centroid; the divergent moment would forbid computing one from a single half.

## The Solid of Revolution, and the One Place π Is Squared

Rotate the figure about its asymptote. Disks of radius $y$ give

$$
V = \pi\int_{-\infty}^{\infty} y^{2}\,dx = 64\pi a^{6}\int_{-\infty}^{\infty}\frac{dx}{(x^{2}+4a^{2})^{2}} = 64\pi a^{6}\cdot\frac{\pi}{16a^{3}} = 4\pi^{2}a^{3}.
$$

$$
V = 4\pi^{2}a^{3} = 39.47841760435743\,a^{3}.
$$

The second $\pi$ comes from the same arctangent family: $\int dx/(x^{2}+c^{2})^{2} = \pi/(2c^{3})$. So the witch is, in this one measurement, a $\pi^{2}$ object — the only place in the article where the exponent is not one.

Pappus's centroid theorem gives an independent route and a check on the centroid height:

$$
V = 2\pi\,\bar y\,A \;\Longrightarrow\; \bar y = \frac{4\pi^{2}a^{3}}{2\pi\cdot 4\pi a^{2}} = \frac{a}{2}.
$$

Direct integration agrees, and it is the cleaner statement of why:

$$
\bar y = \frac{1}{A}\int \frac{y}{2}\cdot y\,dx = \frac{1}{4\pi a^{2}}\cdot\frac{1}{2}\cdot 4\pi a^{3} = \frac{a}{2} = 0.5a .
$$

The centroid of the region under the witch sits at exactly **half the peak height**, with no circle constant anywhere — the $4\pi a^{3}$ from the second moment and the $4\pi a^{2}$ from the area cancel coefficient for coefficient. The area carries $\pi$; the second moment carries the same $\pi$; the ratio does not carry it at all. This is the pattern the whole series keeps finding: the constant lives in the normalisation of a measure, and dies in every ratio of two such measures.

(A side note for readers who met this curve in probability: $y/(4\pi a^{2}) = \frac{1}{2\pi a}\cdot\frac{1}{1+(x/2a)^{2}}$ is exactly the Cauchy density with scale $2a$, so the witch is the Cauchy distribution's geometric construction. That identity, and the $1/\pi$ normalisation that makes it integrate to one, was worked separately and is linked below.)

## Under Golden Pi

Set $\hat\pi = 4/\sqrt\varphi = 3.144605511029693\ldots$ with $\varphi = (1+\sqrt5)/2$. The label sits $+0.0959022309\%$ above $\pi$, so the substitution changes every absolute area and every absolute length at first power by that amount, every square by twice it, and nothing that is a ratio.

**Areas.** With $\hat\pi^{2} = 16/\varphi$:

$$
A = 4\hat\pi a^{2} = \frac{16a^{2}}{\sqrt{\varphi}} = 12.57842204411877\,a^{2} \quad (+0.0959022309\%).
$$

This is the payoff the curve has been withholding. The quadrature survives intact — the witch's area still equals the area of the circle of radius $2a$ under *either* label, because both sides move together, and $4\hat\pi a^{2} = 16a^{2}/\sqrt\varphi$ is algebraic of degree two whereas $4\pi a^{2}$ is transcendental by Lindemann. An exact geometric equality, one side of which becomes a radical expression.

**Volume.** Squaring the constant doubles the shift:

$$
V = 4\hat\pi^{2}a^{3} = \frac{64a^{3}}{\varphi} = 39.55417527999327\,a^{3} \quad (+0.1918964341\%).
$$

$64/\varphi$ is the entire volume, with no $\pi$ and no limit left in it: rational over the golden ratio. A solid of revolution whose volume is algebraic — that is a stronger closure than the plane figure achieves, and it comes from the single exponent-2 occurrence.

**What does not move.** The construction, every one of them: it uses chords, tangents and horizontals. The vertex height $2a$, the point $(2a,a)$, the inflection abscissa $2a/\sqrt3$, the inflection height $3a/2$, the slope $-3\sqrt3/8$, the centroid height $a/2$, the enclosed fractions $1/6$, $1/4$, $1/3$, the entire arc-length divergence. Radian numerals move $\pm0.0958\%$ and mean nothing physical; turn-fractions and slopes do not move a digit.

**The golden point.** One abscissa is worth singling out because both coordinates close in $\varphi$. Set the height equal to $a\varphi$:

$$
\frac{8a^{3}}{x^{2}+4a^{2}} = a\varphi
\;\Longrightarrow\;
x^{2} = \frac{8a^{2}}{\varphi}-4a^{2} = \frac{4a^{2}}{\varphi^{3}},
$$

using $\varphi^{2} = \varphi+1$ to reduce $8/\varphi - 4 = 4(2-\varphi)/\varphi = 4/\varphi^{3}$ since $2-\varphi = 1/\varphi^{2}$. So the witch passes through

$$
\left(\frac{2a}{\varphi^{3/2}},\, a\varphi\right) = \left(0.9717365435\,a,\; 1.6180339887\,a\right),
$$

both coordinates algebraic in $\varphi$, and verified numerically to the last digit printed. It is the one point on the curve where the ordinate is a pure golden multiple of the generating radius.

## The Honest Boundary

Three limits, stated plainly.

First, this is not a squaring of the circle. The classical problem asks for a square of equal area built with straightedge and compass from a given circle; a square of side $2a\sqrt\pi$ has side $\sqrt\pi\cdot 2a$, and $\sqrt\pi$ is transcendental, so no such construction exists — Wantzel and Lindemann closed that door. The witch gives an equality between two *curvilinear* areas, which is a different and legitimate thing, and it is precisely because straight-line construction reached a circular area that the curve was interesting to Grandi and Agnesi.

Second, the area identity does not privilege a value of the constant. It holds for every candidate $\pi$, because it is the statement that the arctangent's total rise equals the constant. Under $\hat\pi$ the arctangent's numerical output in radians scales with $\hat\pi$, the prefactor does not, and the product $4\hat\pi a^{2}$ follows. The identity is a *structural* fact about the arctangent integral, and structure of that kind is invariant under relabelling. Anyone wanting to distinguish $\pi$ from $\hat\pi$ with this curve must bring a physical annulus or a physical wire, and then the argument is about the wire, not about the integral.

Third, nothing here is measured. The area $4\pi a^{2}$ is computed — the limit of an integral, evaluated in closed form. The arc length infinity is computed. The volume $4\pi^{2}a^{3}$ is computed. Fine-structure constants and physical lengths are measured; series, integrals and arctangent limits are not, and the vocabulary should not blur.

What the witch does deliver is a clean specimen of where the constant sits and where it does not: once in the area, twice in the volume, zero times in the centroid, zero times in every turn-fraction, zero times in the construction. Under the golden substitution the one occurrence becomes $16a^{2}/\sqrt\varphi$ and the two occurrences become $64a^{3}/\varphi$ — algebraic, exactly, and honestly traceable to the arctangent integral that put them there.

## Further Reading

- [**Constructible Numbers and the Impossibility of Squaring the Circle**](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — what straightedge and compass can and cannot reach, and why $\sqrt\pi$ is out of range.
- [**Hippocrates' Lunes: The One Curvilinear Figure That Squares Exactly**](/blog/posts/2026-11-10-hippocrates-lunes-quadrature-golden-pi/) — the other classical case of an exact quadrature between curvilinear figures.
- [**The Ellipse: Why Its Perimeter Needs an Elliptic Integral**](/blog/posts/2026-10-28-ellipse-perimeter-elliptic-integral-golden-pi/) — the companion lesson: some arc lengths have no closed form at all, and the witch's is not merely closed but divergent.
- [**Pappus's Centroid Theorem**](/blog/posts/2026-10-30-pappus-centroid-theorem-torus-swept-area-golden-pi/) — the swept-area theorem used above to check the solid of revolution two ways.
- [**The Cauchy–Lorentz Distribution**](/blog/posts/2026-08-24-cauchy-lorentz-distribution-integrates-pi-golden-pi/) — the witch as a probability density, and the $1/\pi$ normalisation that makes it integrate to one.
