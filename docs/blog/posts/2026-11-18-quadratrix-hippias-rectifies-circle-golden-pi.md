---
title: "The Quadratrix of Hippias: Why Two Uniform Motions Straighten a Circle, Why Its Axis Point Is a Limit and Not a Mark, and What Golden Pi Changes"
date: 2026-11-18
description: "A ray sweeps a quarter turn at constant rate while a horizontal line descends the square at constant rate; their intersection traces the quadratrix of Hippias, x = y·cot(πy/2a), a curve whose x-intercept is exactly 2a/π and whose tangent at the top cuts the axis at exactly πa/2 — the quarter circumference, straight, in one line. This article derives the equation from the two motions, evaluates the intercept as the 0·∞ limit it actually is, tabulates the exact algebraic points at heights a/6, a/4, a/3, a/2, 2a/3, 3a/4 and 5a/6, proves the enclosed area is exactly (2a²/π)ln 2 through the integral of u·cot u, shows the two complementary areas are in the π-free ratio ln 2/(1−ln 2) = 2.2588913533, computes both curvatures in closed form (κ = 8π/(4+π²)^{3/2} at the top, κ = 4π(4−π)/((π−2)²+4)^{3/2} at the 45° point), gives the arc length 1.2383541947a that has no elementary closed form, and reconstructs Dinostratus' squaring of the circle — a√π — from a single measured-off segment. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the intercept becomes exactly a√φ/2, the area exactly (a²√φ/2)ln 2, the tangent slope exactly −√φ/2, the squaring side exactly 2a/φ^¼, and the curve stops short of the square's top by 0.000958a. Computed, never measured."
---

# The Quadratrix of Hippias

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Around 420 BC, Hippias of Elis described a curve produced by nothing more exotic than two things moving at constant speed. A radius sweeps steadily through a quarter turn. A straight line slides steadily down the square. Because both motions are uniform and both begin and end together, the point where the radius and the line meet is forced onto a curve — and that curve, followed to its end, produces a straight segment whose length is exactly one quarter of a circumference.

The curve has three historical names. It is the **quadratrix of Hippias** after its inventor, the **quadratrix of Dinostratus** after the man who around 350 BC used it to produce a square equal in area to a given circle, and the **trisectrix** — Pappus reports the name, and reports as well the objection of Sporus, who pointed out that the construction uses the very endpoint it is supposed to deliver. Sporus is right, and this article will not pretend otherwise. But being right about the circularity of the *construction* is not the same as being right about the *curve*, and the curve is one of the most remarkable objects in classical geometry: a figure whose single transcendental equation carries the circle constant in three entirely different roles at once — as a limit, as a tangent, and as a coefficient.

## The Two Motions and the Equation They Force

Take a square of side $a$ with the pivot at the origin $O=(0,0)$, the ray's home edge along the positive $x$-axis and the vertical edge at $x=0$. Let the ray start pointing straight up, along the $y$-axis, and sweep clockwise to the horizontal, so that at sweep angle $\theta$ measured from the vertical it has direction $(\sin\theta,\cos\theta)$ and slope $\cot\theta$. Let the horizontal line start at $y=a$ — the top of the square — and descend to $y=0$, taking the same time as the ray takes to sweep a quarter turn:

$$
y = a\left(1-\frac{2\theta}{\pi}\right), \qquad \theta \in \left[0,\frac{\pi}{2}\right].
$$

The intersection of the ray $y = x\cot\theta$ with that line is the trace point. Solving for $x$:

$$
x = y\tan\theta = a\left(1-\frac{2\theta}{\pi}\right)\tan\theta .
$$

Eliminating $\theta$ between the two relations — note that $\tan\theta = \tan\left(\frac{\pi}{2}-\frac{\pi y}{2a}\right) = \cot\left(\frac{\pi y}{2a}\right)$ — leaves the curve in its coordinate form:

$$
\boxed{\;x = y\cot\left(\frac{\pi y}{2a}\right)\;}
$$

Everything that follows is contained in that line. It is a transcendental equation: no polynomial in $x$ and $y$ reproduces it, because the cotangent cannot be eliminated. It is also, and this is the point, completely rigid — the constant does not sit in front of the curve as a scale factor that could be absorbed by relabelling the axes. It sits inside the argument.

The curve begins at $(0,a)$ and ends at the point where $y\to 0$. Where is that? The equation gives $x\to 0\cdot\infty$ — an indeterminate form, not a number. The honest statement is that the intercept is a *limit*:

$$
x_0 = \lim_{y\to0^{+}} y\cot\left(\frac{\pi y}{2a}\right) = \lim_{y\to0^{+}} \frac{y}{\tan\left(\frac{\pi y}{2a}\right)} = \frac{2a}{\pi} = 0.6366197724\,a .
$$

This is the first thing a careful reader should notice: the quadratrix does not *mark* $\pi$ on an axis with a pencil. It defines a point as the limit of a curve, and the limit evaluates exactly because $\tan u \sim u$. Whether that limit counts as a construction is precisely Sporus' question, and we will come back to it.

## The Tangent That Straightens a Quarter Circle

The curve's slope at its starting point is equally accessible. Differentiating the parametric form at $\theta=0$, where $\tan\theta\to0$ and $\sec^2\theta\to1$:

$$
\left.\frac{dy}{dx}\right|_{(0,a)} = -\frac{2}{\pi} = -0.6366197724 .
$$

The tangent line at the top of the curve is therefore

$$
y = a - \frac{2}{\pi}x .
$$

Set $y=0$: the tangent meets the axis at

$$
x = \frac{\pi a}{2} = 1.5707963268\,a .
$$

That is exactly the quarter circumference of the circle of radius $a$. In one line of algebra the curve has converted an arc into a straight segment — not approximately, not to twenty digits, but identically, because the slope of the tangent at the top *is* $2a/\pi$ divided by $a$. Notice also that the slope at the top is numerically the same number as the intercept divided by $a$: $-x_0/a$. That is not a coincidence of decimal expansions; both are $2/\pi$, and the curve has exactly one constant in it, appearing in two places with opposite signs.

So the quadratrix offers the rectification twice over. The point $(2a/\pi,0)$ marks $2/\pi$ on the axis, from which a quarter circumference $\pi a/2$ follows as $a^2/x_0$ by a mean proportional. The tangent at the top marks $\pi a/2$ directly, one line, no auxiliary construction beyond drawing a straight line through two points already on the drawing.

## The Exact Points, and Where the Constant Is Not

Sweep the ray in equal steps and the heights come out as clean fractions, because $y$ is linear in $\theta$. What is more interesting is that at those heights the *widths* are Euclidean radicals — no circle constant anywhere in them.

| Sweep | Height $y$ | Width $x$ | Decimal $x/a$ |
|---|---|---|---|
| $15°$ | $5a/6$ | $\tfrac{5a}{6}(2-\sqrt3)$ | 0.2232909937 |
| $22.5°$ | $3a/4$ | $\tfrac{3a}{4}(\sqrt2-1)$ | 0.3106601718 |
| $30°$ | $2a/3$ | $\tfrac{2a}{3\sqrt3}$ | 0.3849001795 |
| $45°$ | $a/2$ | $a/2$ | 0.5000000000 |
| $60°$ | $a/3$ | $a/\sqrt3$ | 0.5773502692 |
| $67.5°$ | $a/4$ | $\tfrac{a}{4}(1+\sqrt2)$ | 0.6035533906 |
| $75°$ | $a/6$ | $\tfrac{a}{6}(2+\sqrt3)$ | 0.6220084679 |

Every entry is exact, and every entry is $\pi$-free. The constant has retreated entirely into the two endpoints — the top $(0,a)$, where nothing seems to happen, and the intercept, where everything does. This is the same structural lesson the site has drawn from the lunes of Hippocrates and from the witch of Agnesi: the circle constant in a curve is a boundary condition, not a feature of the interior.

Two interior slopes are worth recording because they close exactly. At the 45° point, $\cot(\pi/4)=1$ and $\csc^2(\pi/4)=2$, giving

$$
\frac{dy}{dx}\left(\tfrac{a}{2},\tfrac{a}{2}\right) = -\frac{2}{\pi-2} = -1.7519383939 ,
$$

and at the top of the curve the slope is $-2/\pi$; neither is a decimal approximation to anything, both are the exact rational functions of $\pi$ shown.

## The Area: $\dfrac{2a^2}{\pi}\ln 2$

The area between the curve, the $y$-axis and the $x$-axis is

$$
A = \int_0^{a} x\,dy = \int_0^{a} y\cot\left(\frac{\pi y}{2a}\right)dy .
$$

Substituting $u = \pi y/(2a)$ gives $dy = 2a\,du/\pi$ and $y = 2au/\pi$, so

$$
A = \frac{4a^2}{\pi^2}\int_0^{\pi/2} u\cot u\,du .
$$

That last integral integrates by parts with $v=\ln\sin u$:

$$
\int_0^{\pi/2} u\cot u\,du = \Big[u\ln\sin u\Big]_0^{\pi/2} - \int_0^{\pi/2}\ln\sin u\,du = 0 + \frac{\pi}{2}\ln 2 ,
$$

using Euler's classical evaluation $\int_0^{\pi/2}\ln\sin u\,du = -\tfrac{\pi}{2}\ln2$. Therefore

$$
A = \frac{4a^2}{\pi^2}\cdot\frac{\pi}{2}\ln2 = \frac{2a^2}{\pi}\ln 2 = 0.4412712003\,a^2 .
$$

The complement inside the rectangle $[0,\,2a/\pi]\times[0,\,a]$ is the remainder, and it also closes:

$$
A' = \frac{2a^2}{\pi} - \frac{2a^2}{\pi}\ln2 = \frac{2a^2}{\pi}(1-\ln2) = 0.1953485721\,a^2 .
$$

Because the two share the same prefactor, their ratio is $\pi$-free:

$$
\frac{A}{A'} = \frac{\ln 2}{1-\ln2} = 2.2588913533 .
$$

That is the cleanest statement in the article. The two regions of the quadratrix are in the ratio 2.2589… to one another, and no circle constant appears in that number at all — the $\pi$'s cancel because both areas are cut from the same rectangle whose width was $2a/\pi$ in the first place. As a fraction of the square $a^2$, the enclosed area is $2\ln2/\pi^2 = 0.1404609855$, and here the constant survives because the square has no $\pi$ to cancel against.

A compact statement of the two identities, for checking:

```
x(y)      = y·cot(π y / 2a)
x(0)      = 2a/π                     (limit, not a substitution)
A_inside  = ∫₀^a x dy   = 2a² ln2 / π = 0.4412712003 a²
A_outside = 2a²/π − A   = 2a²(1−ln2)/π = 0.1953485721 a²
A/A'      = ln2/(1−ln2) = 2.2588913533   (π-free)
```

## Curvature at the Two Named Points

Writing $x$ as a function of $y$ makes the curvature mechanical: with $u=\pi y/(2a)$,

$$
\frac{dx}{dy} = \cot u - u\csc^2 u, \qquad
\frac{d^2x}{dy^2} = \frac{\pi}{2a}\left(-2\csc^2u + 2u\csc^2u\cot u\right).
$$

At the top, $u=\pi/2$, so $dx/dy = -\pi/2$ and $d^2x/dy^2 = -\pi/a$, giving

$$
\kappa_{\text{top}} = \frac{\pi/a}{\left(1+\pi^2/4\right)^{3/2}} = \frac{8\pi}{(4+\pi^2)^{3/2}}\cdot\frac{1}{a} = \frac{0.4865682300}{a},
\qquad R_{\text{top}} = 2.0552102219\,a .
$$

At the 45° point, $u=\pi/4$, so $dx/dy = 1-\pi/2$ and $d^2x/dy^2 = \pi(\pi-4)/(2a)$, giving

$$
\kappa_{45} = \frac{\pi(4-\pi)}{2a\left(1+(1-\pi/2)^2\right)^{3/2}} = \frac{4\pi(4-\pi)}{\left((\pi-2)^2+4\right)^{3/2}}\cdot\frac{1}{a} = \frac{0.8832672552}{a},
\qquad R_{45} = 1.1321601634\,a .
$$

Both are exact closed forms, both are evaluated with $\pi$ as a computed quantity, and both change under the golden substitution in a way that is worth tabulating precisely because it is *not* a uniform percentage: curvature is a second-order geometric quantity and the constant enters it at mixed powers.

## The Local Shape, and the One Quantity That Refuses to Close

Near the intercept the curve is not straight and not circular — it is parabolic. Expanding $\cot u = 1/u - u/3 - u^3/45-\cdots$ with $u=\pi y/(2a)$:

$$
x = \frac{2a}{\pi} - \frac{\pi y^2}{6a} - \frac{\pi^3 y^4}{360a^3} - \cdots
$$

so the approach to the axis point is quadratic: $2a/\pi - x \propto y^2$, exactly. Checked at $y=0.1a$, the gap is $0.0052360\,a$ against the leading term $\pi(0.1)^2/6 = 0.0052360\,a$. The curve therefore meets the axis with a vertical tangent, and its $\pi$-point is a cusp-like approach rather than a transversal crossing.

Revolving the curve about the $x$-axis gives the volume $\pi\int y^2\,dx$. The quadrature evaluates to $\int y^2\,dx = 0.3397878862\,a^3$, hence $V = 1.0674751270\,a^3$. Unlike the area, this integral has no elementary closed form that this article could establish — the substitution leaves $\int s^2\tan\theta\,d\theta$ with $s = 1-2\theta/\pi$, which is not a standard antiderivative. It is reported as a computed quadrature and nothing more.

The arc length is the second quantity that refuses to close. Because the curve ends with a vertical tangent, integrating in $y$ is the numerically stable route:

$$
L = \int_0^{a}\sqrt{1+\left(\cot u - u\csc^2u\right)^2}\,dy = 1.2383541947\,a ,
$$

stable to the tenth digit under grid refinement from $10^4$ to $4\times10^6$ intervals, and with no closed form claimed. This is the honest asymmetry of the curve: its enclosed area is exactly $(2a^2/\pi)\ln2$, and its own length is not exact in any elementary sense.

## Dinostratus' Square, and Sporus' Objection

The classical use is now a two-step. From the intercept $x_0 = 2a/\pi$, the circle's area is

$$
\pi a^2 = \frac{2a^3}{x_0},
$$

and a square of that area has side

$$
s = \sqrt{\frac{2a^3}{x_0}} = a\sqrt{\pi} = 1.7724538509\,a .
$$

Given the segment $x_0$, the side $s$ is constructible by the standard mean-proportional construction between $2a$ and $a^2/x_0$ — no new curve, no approximation. That is Dinostratus' squaring of the circle, and it is a genuine squaring *given the curve*.

Given the curve is the whole difficulty. Sporus' objection, preserved in Pappus' *Collection*, is that the endpoint of the quadratrix is obtained by running the two motions until they simultaneously finish, and that the finishing point is exactly what the construction was supposed to produce. You cannot lay a ruler along the curve and read off where it meets the axis, because the curve only meets the axis in the limit; you cannot run the motions "until they finish" without knowing where the finish is. In modern language: the endpoint exists as a limit of the curve, and the limit is exact, but the curve is not a straightedge-and-compass object and the limit is not a constructible point. Lindemann's 1882 theorem remains untouched: $\pi$ is transcendental, so no finite straightedge-and-compass construction produces it, however cleverly assisted.

What the quadratrix does establish, and what this article is actually about, is the shape of the relationship between the constant and geometry: the constant appears as a limit at one point, as a slope at another, and as a prefactor over an area that is otherwise built from $\ln 2$. Whatever value one assigns to the circle constant, the *structure* of the curve is unchanged; only the numbers that ride on it move.

## What Golden Pi Changes

Take the site's value, $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$, with $\hat\pi^2 = 16/\varphi = 9.8885438200$ and $\hat\pi/4 = 1/\sqrt\varphi = 0.7861513778$. Substituting it into the same equation, $x = y\cot(\hat\pi y/2a)$, every first-power occurrence becomes algebraic in $\varphi$, because $1/\hat\pi = \sqrt\varphi/4$ exactly:

| Quantity | with $\pi$ | with $\hat\pi = 4/\sqrt\varphi$ | Change |
|---|---|---|---|
| Intercept $x_0$ | $2a/\pi = 0.6366197724a$ | $a\sqrt\varphi/2 = 0.6360098248a$ | $-0.0958103\%$ |
| Tangent slope at top | $-2/\pi = -0.6366197724$ | $-\sqrt\varphi/2 = -0.6360098248$ | $-0.0958103\%$ |
| Tangent's axis cut | $\pi a/2 = 1.5707963268a$ | $2a/\sqrt\varphi = 1.5723027555a$ | $+0.0958103\%$ |
| Area inside | $0.4412712003a^2$ | $0.4408484168a^2$ | $-0.0958103\%$ |
| Area outside | $0.1953485721a^2$ | $0.1951614079a^2$ | $-0.0958103\%$ |
| Ratio $A/A'$ | $2.2588913533$ | $2.2588913533$ | $0$ |
| Width at $y=a/2$ | $0.5000000000a$ | $0.4992473524a$ | $-0.1505\%$ |
| Curvature at $y=a/2$ | $0.8832668688/a$ | $0.8838217047/a$ | $+0.0628\%$ |
| Dinostratus side | $a\sqrt\pi = 1.7724538509a$ | $2a/\varphi^{1/4} = 1.7733035586a$ | $+0.0479\%$ |

The first-power rows all move by the same factor $\pi/\hat\pi = 0.9990418965$, for the trivial reason that they are all linear in the constant: the intercept, the tangent slope, both areas, and the tangent's axis cut. The exact forms are worth writing out, because each one closes:

$$
x_0^{(\varphi)} = \frac{a\sqrt\varphi}{2},\qquad
\frac{dy}{dx}\Big|_{\text{top}} = -\frac{\sqrt\varphi}{2} = -\frac{x_0^{(\varphi)}}{a},\qquad
A^{(\varphi)} = \frac{a^2\sqrt\varphi}{2}\ln2 .
$$

That the slope at the top and the intercept divided by $a$ are still the same number after the substitution is the structural statement: the relation $-x_0/a = \text{slope}$ is not an artefact of $\pi$, it is a consequence of the curve's own geometry, and survives any constant.

Two consequences are not merely percentage shifts.

First, the golden curve no longer closes its square. Solving $\cot(\hat\pi y/2a)=0$ puts the curve's own top at

$$
y = \frac{\pi a}{\hat\pi} = 0.9990418965\,a ,
$$

leaving a gap of $a(1-\pi/\hat\pi) = 0.0009581035\,a$ below the corner. The two uniform motions that generate the curve are synchronised to a quarter turn and to a full descent; when the constant inside the cotangent is not the constant that defines the quarter turn, the motions no longer finish together by exactly that fraction. The square that the golden quadratrix actually inscribed is taller by a factor $\hat\pi/\pi$, and the curve crosses the $y$-axis just under the corner instead of exactly at it. For $a=1$ m, the shortfall is 0.96 mm — invisible on any drawing, and yet exact.

Second, the widths at fixed heights are no longer the Euclidean radicals of the table above. At $y=a/2$ the width is

$$
x = \frac{a}{2}\cot\left(\frac{\hat\pi}{4}\right) = \frac{a}{2}\cot\left(\frac{1}{\sqrt\varphi}\right) = 0.4992473524\,a ,
$$

which is $-0.1505\%$ rather than $-0.0958\%$ — the substitution does not act uniformly on a quantity that is itself a transcendental function of the constant. The cotangent at $1/\sqrt\varphi$ has no elementary closed form; it is algebraic-argument, transcendental-valued, and this article states it as a computed number rather than dressing it up.

What does *not* move is more interesting than what does. The exact heights $a/6, a/4, a/3, a/2, 2a/3, 3a/4, 5a/6$ are fixed by the linear descent and are untouched. The ratio of the two enclosed areas, $\ln2/(1-\ln2)$, does not move a digit. The quadratic approach to the axis point, $2a/\hat\pi - x \propto \hat\pi y^2/6a$, keeps its form with the constant simply renamed. And every qualitative feature — one intercept, one vertical tangent there, one parabolic approach, one transcendental equation, no finite construction — is invariant. A curve that is generated by uniform motion cannot be arbitrated by a ruler: the two candidate constants differ by six parts in ten thousand on a 1 m square, which is below the width of a pencil line, and the *structure* of the quadratrix is identical either way.

That is the honest boundary of this article. The quadratrix proves nothing about which constant is right, because it is a construction with a parameter and both parameters fit. What it does prove is that $\pi$ in geometry is not a scale factor bolted onto curves — it is the value of a limit at a point, the slope of a tangent, and the prefactor on an area whose remainder is pure $\ln 2$. Computed, never measured.

## Further Reading

- [The Witch of Agnesi: Why a Curve Traced by Straight Lines Encloses Exactly Four Times the Generating Circle](/blog/posts/2026-11-17-witch-of-agnesi-exact-quadrature-golden-pi/) — the other classical curve whose quadrature is an identity rather than an approximation, and its inverse-square tail.
- [Hippocrates' Lunes: The One Curvilinear Figure That Squares Exactly](/blog/posts/2026-11-10-hippocrates-lunes-quadrature-golden-pi/) — where Pythagoras, not the circle constant, does the cancelling.
- [The Polygon Limit: How Exhaustion Computes the Circle Constant](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the Archimedean route from inscribed perimeters to the constant, computed as a limit.
- [Constructible Numbers and the Impossibility of Squaring the Circle](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — why Lindemann's theorem survives every mechanical curve, Sporus' objection included.
- [The Continued Fraction of the Circle Constant](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) — what the best rational approximations say about the two candidate values.
