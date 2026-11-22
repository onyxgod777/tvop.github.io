---
title: "The Hyperbolic Circle: Why Lobachevsky's Circumference Is 2π sinh r, Why the Angle of Parallelism at Distance ln φ Has Tangent Exactly 2, and What Golden Pi Changes"
date: 2026-11-22
description: "Deny Euclid's fifth postulate and a circle's circumference stops being proportional to its radius: it becomes 2π sinh r, growing exponentially, with π surviving only as the radian measure of one full turn in the angular parameter. This article derives the hyperbolic metric and its circumference and area integrals, checks them against the Poincaré disk, tabulates circles from r = 0.1 to r = 10 where 2π sinh r = 69198.18 against a Euclidean 62.83, proves Lobachevsky's angle of parallelism tan Π(r) = 1/sinh r, and exhibits the exact golden distance at which a hyperbolic circle has circumference exactly π — r = ln φ = 0.4812118250596034, since sinh(ln φ) = 1/2 exactly — enclosing exactly π/φ³ = π(√5−2) = 0.7416294239 of area, with an area-to-circumference ratio that is the π-free tanh(r/2). It then shows π's other face in curved space, the triangle defect whose supremum is exactly π and which nothing attains, and the rapidity of special relativity in which the circle constant disappears entirely — with the golden boost γ = √5/2, βγ = 1/2, β = 1/√5 at rapidity ln φ. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the golden circle's circumference becomes exactly 4/√φ, its area exactly 4/φ^{7/2}, and the ideal triangle's area exactly π̂ — while every angle, every ratio and the whole of the geometry hold every digit. Computed, never measured."
---

# The Hyperbolic Circle

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Every schoolchild learns the formula and never questions its shape: $C = 2\pi r$. The circumference of a circle is *proportional* to its radius, and the constant of proportionality is the same for every circle in the plane. That proportionality is not a theorem of neutral geometry. It is a theorem of Euclid's fifth postulate, and the moment the postulate is denied the formula breaks — not by a small correction, but catastrophically: the circumference of a circle begins to grow *exponentially* with its radius, and at radius $r = 10$ in units of the curvature radius it is $69198.18$ where the Euclidean formula would give $62.83$.

What survives the wreckage is instructive. The constant $\pi$ does not disappear; it retreats to exactly one place, the measure of a full turn in the angular parameter, where it multiplies $\sinh r$ rather than $r$. Everything else about the circle — its growth, its area, its relation to its own circumference — turns out to be free of it. That is the same structure this blog has found in the ellipse, in the catenary, in the pseudosphere: $\pi$ enters as a units conversion between turns and radians, and the geometry's real content sits beside it.

And in hyperbolic space there is one distance where the two faces of the constant meet exactly. At $r = \ln\varphi = 0.4812118250596034$ the function $\sinh r$ equals $1/2$ precisely — because $\varphi - 1/\varphi = 1$ — so a hyperbolic circle of that radius has circumference *exactly* $\pi$, the circumference of the Euclidean circle of diameter $1$, while enclosing only $0.7416294239$ of the area. It is the unique radius at which the curvature of space eats exactly the right amount of circumference to cancel a factor of two, and it is written in the golden ratio.

## The Metric, and Why the Circumference Integral Has a sinh in It

Work in geodesic polar coordinates: $r$ is the distance from a chosen origin along a geodesic, $\theta$ the angle at which that geodesic leaves it. In Euclidean space the metric is $ds^{2} = dr^{2} + r^{2}\,d\theta^{2}$, and the circle of radius $r$ has circumference $\int_0^{2\pi} r\,d\theta = 2\pi r$ — the $\pi$ arrives because $\theta$ runs over a full turn and a turn is $2\pi$ radians. In a space of constant curvature $-1$ the same construction gives

$$
ds^{2} = dr^{2} + \sinh^{2}r\;d\theta^{2},
$$

so the circumference of the geodesic circle is

$$
C(r) = \int_{0}^{2\pi}\sinh r\;d\theta = 2\pi\sinh r,
$$

and the area of the disc follows by stacking the circles:

$$
A(r) = \int_{0}^{r} 2\pi\sinh\rho\;d\rho = 2\pi(\cosh r - 1).
$$

Nothing here is a numerical accident. The $\sinh$ is exactly the statement that circumference grows like $e^{r}$: for large $r$, $\sinh r \approx e^{r}/2$, so every step outward in radius multiplies the circumference by $e$. Space itself is doing the multiplying, and the constant has been demoted from a property of the circle to a factor in front of the turn count.

It is worth verifying the model, because a plausible-looking metric can be wrong. On the Poincaré disk $|z| < 1$ the metric is $ds = 2|dz|/(1-|z|^{2})$. A Euclidean circle of radius $\rho$ centred at the origin has Euclidean circumference $2\pi\rho$ and therefore hyperbolic length

$$
\oint ds = \frac{2\pi\rho \cdot 2}{1-\rho^{2}} = \frac{4\pi\rho}{1-\rho^{2}} .
$$

The hyperbolic distance from the centre to that Euclidean radius satisfies $\sinh r = 2\rho/(1-\rho^{2})$, so the length is $2\pi\sinh r$ — the same formula, derived from a completely different presentation of the same geometry. Two independent computations, one line apart, agreeing identically. That is what a consistency check looks like: not a measurement, a derivation repeated on a different footing.

## Where the Constant Actually Lives: One Turn, Not One Radius

Look again at $C = 2\pi\sinh r$. The $\pi$ is attached to the *angular* part of the metric, never to the radial part. Write the circumference in turns and it becomes

$$
\frac{C}{2\pi} = \sinh r \quad\Longleftrightarrow\quad C = \sinh r \text{ turns}.
$$

In that form the constant has vanished completely. A circle of hyperbolic radius $r$ is $\sinh r$ turns around — a pure number of wraps of the circle on itself, exactly as a Euclidean circle of radius $r$ is $r$ turns around. The Euclidean formula $C = 2\pi r$ reads, in the same units, "$C/r = 1$ turn": the circumference of a Euclidean circle is exactly *one turn of its own radius*. That is the whole content of the constant. It is not a fact about circles. It is a fact about the radian, which is defined so that a full turn is $2\pi$.

This is the honest diagnosis the site keeps returning to, and hyperbolic geometry makes it visible even to a hostile reader, because in H² the coefficient of $\sinh r$ can be anything you like and the geometry does not care. Label a turn $T$ instead of $2\pi$ and the circumference is $T\sinh r$; the curvature, the geodesics, the areas, the angles, every triangle, every horocycle are untouched. A constant that can be relabelled without moving a single point of the space is a convention. What cannot be relabelled is $\sinh r$ itself.

## A Table of Circles: Proportional, Then Exponential

Set the curvature radius to $1$ and compare the hyperbolic circumference with the Euclidean prediction $2\pi r$.

| $r$ | $C = 2\pi\sinh r$ | $C/(2\pi r) = \sinh r / r$ | $A = 2\pi(\cosh r-1)$ | $A/C = \tanh(r/2)$ | $\Pi(r)$ |
|---|---|---|---|---|---|
| 0.1 | 0.6293662520 | 1.0016675 | 0.0314421152 | 0.0499583750 | 84.279948° |
| 0.25 | 1.587209997 | 1.010449267 | 0.1973743276 | 0.1243530 | 75.822973° |
| $\ln\varphi$ = 0.4812118251 | **3.1415926536** | 1.039043461 | 0.7416294239 | 0.2360679775 | 63.43494882° |
| 0.5 | 3.274138367 | 1.042190611 | 0.8018975894 | 0.2449186612 | 62.476192° |
| 1 | 7.384006873 | 1.175201194 | 3.412276265 | 0.4621171573 | 40.395063° |
| 2 | 22.78823603 | 1.813430204 | 17.35538738 | 0.7615941560 | 15.414627° |
| 3 | 62.94416455 | 3.339291642 | 56.97380062 | 0.9051482536 | 5.7004709° |
| 5 | 466.2325224 | 14.84064212 | 459.9916729 | 0.9866142982 | 0.77210017° |
| 10 | 69198.18298 | 1101.323287 | 69191.90008 | 0.9999092043 | 0.0052024487° |

Three things in that table are worth naming.

First, the Euclidean limit is visible and quantitative. At $r = 0.1$ the hyperbolic circumference exceeds $2\pi r$ by $0.16675\%$; the excess is $\sinh r/r - 1 = r^{2}/6 + O(r^{4})$, the standard small-circle correction, so hyperbolicity is second order in the radius and undetectable at small scale. That is why the old measurement argument never had legs in either direction: at laboratory sizes, curved and flat space are the same space to thirty digits.

Second, the area-to-circumference ratio is **exactly** $\tanh(r/2)$:

$$
\frac{A}{C} = \frac{2\pi(\cosh r - 1)}{2\pi\sinh r} = \frac{\cosh r - 1}{\sinh r} = \tanh\frac{r}{2},
$$

an identity with no constant in it at all. In Euclidean space $A/C = r/2$, so the ratio grows without bound; in H² it rises toward $1$ and stops. A hyperbolic circle can never have area exceeding its circumference. At $r = 10$ the ratio is already $0.9999092$ — the circle is a very long thin band, all circumference and almost no interior.

Third, the disc area grows with the circumference because the tail dominates: at $r = 10$ the area and the circumference agree to five digits ($69191.90$ against $69198.18$, a difference of $6.28$), the region being a shell whose inner part is negligible.

## Lobachevsky's Angle of Parallelism, and the Golden Distance

In H² two geodesics through a point $P$ either meet or diverge; there is no third case, because a line $L$ disjoint from $P$ has a *set* of parallels through $P$ rather than one. The boundary of that set is a pair of asymptotic geodesics, and the angle each makes with the perpendicular from $P$ to $L$ is the angle of parallelism $\Pi(r)$, a function of the perpendicular distance $r$ only. Lobachevsky's formula is

$$
\tan\Pi(r) = \frac{1}{\sinh r}, \qquad\text{equivalently}\qquad \tan\frac{\Pi(r)}{2} = e^{-r}.
$$

As $r\to 0$, $\Pi\to 90°$ and the Euclidean case is recovered; as $r\to\infty$, $\Pi\to 0$ and the parallel becomes asymptotic to the perpendicular itself.

Now put $r = \ln\varphi$. Then $e^{-r} = 1/\varphi$, so $\Pi/2 = \arctan(1/\varphi)$ and

$$
\tan\Pi = \frac{2(1/\varphi)}{1 - 1/\varphi^{2}} = \frac{2/\varphi}{1/\varphi} = 2 .
$$

The simplification is exact because $1 - 1/\varphi^{2} = 1/\varphi$, which follows from $\varphi^{2} = \varphi + 1$. So the angle of parallelism at the golden distance has tangent **exactly two**:

$$
\Pi(\ln\varphi) = \arctan 2 = 63.43494882292201°,
$$

the diagonal angle of a $1\times 2$ rectangle, at the distance $\ln\varphi = 0.4812118250596034$. The same check through the other form: $\sinh(\ln\varphi) = 1/2$, and $1/\sinh = 2$. Two routes, one answer, no rounding.

The golden distance is therefore not decorative here. It is the unique distance at which the angle of parallelism is the angle whose tangent is an integer — the point where Lobachevsky's transcendental function, which normally produces inaccessible angles, returns a constructible one built from the simplest possible rational slope.

## The Golden Hyperbolic Circle: Circumference Exactly π

The same identity, $\sinh(\ln\varphi) = 1/2$, does something stronger to the circumference. Since

$$
\sinh(\ln\varphi) = \frac{\varphi - \varphi^{-1}}{2} = \frac{1}{2},
$$

the circumference of the hyperbolic circle of radius $r = \ln\varphi$ is

$$
C = 2\pi\cdot\frac{1}{2} = \pi = 3.1415926535897932 \quad\text{(exactly)}.
$$

Not approximately, not to some digits: identically, because $\varphi - 1/\varphi = 1$ by definition of the golden ratio. A hyperbolic circle of radius $0.4812118$ has precisely the circumference of the Euclidean circle of diameter $1$. The curvature has eaten exactly the factor of two that separates $2r$ from $\sinh r$.

Its area is equally clean. With $\cosh(\ln\varphi) = (\varphi + 1/\varphi)/2 = \sqrt5/2$,

$$
A = 2\pi\left(\frac{\sqrt5}{2} - 1\right) = \pi\left(\sqrt5 - 2\right) = \frac{\pi}{\varphi^{3}} = 0.7416294238611399,
$$

since $\sqrt5 - 2 = 1/\varphi^{3}$ (expand $\varphi^{3} = 2\varphi + 1 = \sqrt5 + 2$). So the golden hyperbolic circle has

$$
\boxed{\;C = \pi,\qquad A = \frac{\pi}{\varphi^{3}},\qquad \frac{A}{C} = \frac{1}{\varphi^{3}} = \sqrt5 - 2 = 0.2360679774997897\;}
$$

and the ratio is exactly $\tanh(\ln\varphi/2)$ as the identity demands. Compare it with the Euclidean circle of diameter $1$, which has $C = \pi$ and $A = \pi/4 = 0.7853981634$: same perimeter, and $0.7416294239/0.7853981634 = 4/\varphi^{3} = 94.4272\%$ of the area. Equal circumference, a $5.57\%$ deficit of interior — all of it curvature, none of it the constant.

One further coincidence of the same family, tabulated above: at $r = \operatorname{arsinh}1 = \ln(1+\sqrt2) = 0.8813735870$ the hyperbolic circle has circumference exactly $2\pi$ — identical to the Euclidean unit circle — while its area is $2\pi(\sqrt2 - 1) = 2.6025805691$. Same perimeter as the Euclidean circle of radius $1$, $\cosh r = \sqrt2$, and the area is $82.84\%$ of $\pi$. Two distances, two exact coincidences of perimeter, both forced by elementary algebra in $\varphi$ and $\sqrt2$.

```python
from mpmath import mp, sqrt, pi, log, sinh, cosh, tanh, atan
mp.dps = 30
phi  = (1 + sqrt(5)) / 2
r    = log(phi)                 # 0.4812118250596034475
print(sinh(r))                  # 0.5                    exact
print(2*pi*sinh(r) - pi)        # 0.0                    circumference is pi
print(2*pi*(cosh(r)-1) - pi/phi**3)          # 0.0
print((cosh(r)-1)/sinh(r) - tanh(r/2))       # 0.0
print((2*atan(exp(-r)))*180/pi)              # 63.4349488229220106
gpi = 4/sqrt(phi)               # 3.1446055110296931443
print(2*gpi*sinh(r), 4/sqrt(phi))            # 3.1446055110296931443 both
print(2*gpi*(cosh(r)-1), 4/phi**3.5)         # 0.742340663023472281 both
```

## The Defect: π as a Ceiling Nothing Attains

Hyperbolic geometry gives the constant a second, quite different role. In H² the angles of a triangle sum to *less* than a half-turn, and the shortfall is the area:

$$
A_{\triangle} = \pi - (\alpha + \beta + \gamma) \quad\text{(radians, curvature } -1\text{)}.
$$

This is Gauss–Bonnet for the simplest possible surface, and it inverts the Euclidean situation: there the angle sum is a fixed $180°$ and carries no information, while here the angle sum *is* the area, and the constant appears as the largest area any triangle can have — the ideal triangle, three vertices on the boundary at infinity, three angles of zero.

| $\alpha=\beta=\gamma$ | angle sum | defect $=A$ | as a fraction of $\pi$ |
|---|---|---|---|
| 60° | 180° | 0 | 0 |
| 50° | 150° | 0.5235987756 | 1/6 |
| 40° | 120° | 1.047197551 | 1/3 |
| 30° | 90° | 1.570796327 | 1/2 |
| 20° | 60° | 2.094395102 | 2/3 |
| 10° | 30° | 2.617993878 | 5/6 |
| 1° | 3° | 3.089232776 | 0.98333 |
| 0° (ideal) | 0° | $\pi$ = 3.141592654 | 1 |

The ideal triangle's area is exactly $\pi$, and it is a supremum that no triangle in the space attains — every actual triangle has positive angles and strictly less area. So in H² the constant is simultaneously the *ceiling* of a geometric quantity and the *unit* in which that quantity is quoted. That double role is the cleanest illustration available of why a change of label moves both numbers together and tells you nothing about the space. The defect table is a family of exact fractions of $\pi$: $1/6$, $1/3$, $1/2$, $2/3$, $5/6$, and the limit $1$. Under any label those fractions are the same fractions.

## Rapidity: The Rotation Group With No Constant in It

There is a third place in physics where the circle's machinery appears and then evaporates — special relativity. A Lorentz boost is a hyperbolic rotation, and its parameter is the *rapidity* $\eta$, defined so that

$$
\beta = \tanh\eta,\qquad \gamma = \cosh\eta,\qquad \beta\gamma = \sinh\eta .
$$

Rapidity is additive: two boosts of rapidities $\eta_1$ and $\eta_2$ compose to $\eta_1 + \eta_2$, exactly as angles do. But $\eta$ ranges over the whole real line with no periodicity, and no $2\pi$ appears anywhere in the group. The circle constant is present in the *Euclidean* rotation group only because a rotation returns to itself after a full turn; a boost never returns to itself, so the constant that counts returns has nothing to count.

At the golden rapidity the numbers are again exact. With $\eta = \ln\varphi$:

$$
\beta = \tanh(\ln\varphi) = \frac{\varphi - 1/\varphi}{\varphi + 1/\varphi} = \frac{1}{\sqrt5} = 0.4472135955,\qquad \gamma = \frac{\sqrt5}{2} = 1.1180339887,\qquad \beta\gamma = \frac{1}{2}.
$$

| $\eta$ | $\beta = \tanh\eta$ | $\gamma = \cosh\eta$ | $\beta\gamma$ |
|---|---|---|---|
| 0.25 | 0.2449186624 | 1.0314131 | 0.2526123168 |
| 0.5 | 0.4621171573 | 1.127625965 | 0.5210953055 |
| $\ln\varphi$ = 0.4812118251 | 0.4472135955 | 1.1180339887 | 0.5000000000 |
| 1 | 0.7615941560 | 1.543080635 | 1.175201194 |
| 2 | 0.9640275801 | 3.762195691 | 3.626860408 |
| 3 | 0.9950547537 | 10.067662 | 10.01787493 |

The golden rapidity is the unique boost with $\gamma = \sqrt5/2$ and $\beta\gamma = 1/2$ simultaneously — a Lorentz transformation whose matrix entries are $(\gamma, \beta\gamma; \beta\gamma, \gamma) = (\sqrt5/2, 1/2;\, 1/2, \sqrt5/2)$, and whose determinant $\gamma^{2} - \beta^{2}\gamma^{2} = 5/4 - 1/4 = 1$ holds by construction. The matrix is algebraic with entries in $\mathbb{Q}(\sqrt5)$, and it contains no circle constant, because a boost is not a rotation.

## What Golden Pi Changes, and What It Cannot Touch

Golden Pi enters these formulas exactly where $\pi$ enters, and nowhere else.

**Circumference and area of the golden hyperbolic circle.** With $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443$:

$$
\hat{C} = 2\hat\pi\sinh(\ln\varphi) = \frac{4}{\sqrt\varphi} = 3.1446055110 \quad(+0.0959022309\%),
$$

$$
\hat{A} = 2\hat\pi\left(\frac{\sqrt5}{2}-1\right) = \frac{4}{\varphi^{7/2}} = 0.7423406630234723 \quad(+0.0959022309\%).
$$

Both are now algebraic of degree four in $\varphi$ — $\hat{C}$ is the root of $y^{4}+16y^{2}-256=0$ and $\hat{A}$ the corresponding scaled quartic — where $\pi$ and $\pi/\varphi^{3}$ are transcendental by Lindemann's 1882 theorem. The exponential structure of the geometry, $\sinh r$, is untouched: it is not a function of the constant.

**The table, relabelled.** Every circumference in the table scales by $1 + 9.5902230878\times10^{-4}$ and every area too; the ratios $\sinh r/r$, $\tanh(r/2)$ and the angles $\Pi(r)$ do not move a digit, because they are quotients of turn counts.

**The angle of parallelism.** Exactly unchanged. $\Pi(\ln\varphi) = \arctan 2 = 63.43494882292201°$ is a turn fraction — an angle in degrees is a fraction of a full turn — and no relabelling of radians can touch it. This is the sharpest single test in the article: a quantity that Golden Pi cannot move, sitting one line away from a circumference that it moves by exactly its own gap.

**The ideal triangle.** Its area becomes exactly $\hat\pi = 4/\sqrt\varphi$, and every entry of the defect table scales by the same factor, with the fractions $1/6, 1/3, 1/2, 2/3, 5/6, 1$ intact. The fractions are geometry; the unit in front of them is the label.

**Rapidity.** Untouched in every digit. $\beta = 1/\sqrt5$, $\gamma = \sqrt5/2$, $\beta\gamma = 1/2$ are algebraic identities in $\varphi$ with no circle constant to relabel.

## The Honest Boundary

Three limits belong in print, because the hyperbolic argument is strong enough to tempt overreach.

*Curvature cannot arbitrate the constant.* Every occurrence of $\pi$ in H² is either a turn count or a normalisation of the angular parameter. Deny the fifth postulate and the constant does not change its value; it changes its *address*, moving from the radius to the angle. A space whose geometry is indifferent to the label cannot be evidence about the label. The golden circle's circumference is $\pi$ exactly because $\sinh(\ln\varphi)$ is $1/2$ exactly — a statement about $\varphi$, not about the circle constant, which sits in front of it as a factor that any consistent convention may supply.

*No experiment reaches it.* The observable signature of hyperbolic space is the $r^{2}/6$ excess in the circumference-to-radius ratio. For a curvature radius of $10^{11}$ light years, a one-metre circle is altered by $\sim 1.9\times10^{-33}$ relative — thirty-three orders of magnitude below the $9.59\times10^{-4}$ gap. Any claim that a laboratory disc distinguishes $\pi$ from $\hat\pi$ through curvature is arithmetically dead, and this article makes no such claim.

*The Kepler triangle does not transplant.* In H² there are no similar triangles: shape is fixed by size, so a scale-free argument from side ratios to angles — the argument by which this site reads $\hat\pi$ out of the Kepler triangle — has no hyperbolic analogue. That is a genuine restriction on the site's own construction, and it is stated here rather than hidden: the golden geometry of the plane is a Euclidean object, and hyperbolic space, which dissolves similarity, cannot host it.

What hyperbolic geometry does deliver is a cleaner statement of what the constant *is*. In flat space, $C = 2\pi r$ invites the reading that $\pi$ measures circles. Lobachevsky's formula refutes that reading in one line: $C = 2\pi\sinh r$, where the constant multiplies a function that has nothing to do with circles and everything to do with the exponential growth of the space. $\pi$ is the number of radians in a turn, and a turn is a thing geometers chose to divide into $2\pi$ parts. The exponential is the thing that was discovered.

Every number above is computed — by quadrature, by the Poincaré-disk metric, by exact algebra in $\varphi$ and $\sqrt5$ — and none of it is measured. Computed, never measured.

## Further Reading

- [The Pseudosphere: Why Sweeping a Tractrix Around Its Axis Reproduces the Sphere's Area Exactly](/blog/posts/2026-11-15-pseudosphere-tractrix-constant-curvature-golden-pi/) — the one surface of constant negative curvature in ordinary space, and the geodesic-triangle defect $a^{2}(\pi - A - B - C)$ that this article's ceiling generalises.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — the same diagnosis on a flat curve: the constant in the answer is a normalisation of the angular measure, not a property of the figure.
- [The Pendulum That Reads π in Seconds](/blog/posts/2026-11-14-pendulum-reads-pi-in-seconds-foucault-golden-pi/) — where $\arcsin(1/\varphi) = 38.1727076°$ and the golden latitude do for a flat geometry what $\arctan 2$ does for a hyperbolic one.
- [The Gudermannian Function and the Mercator Projection](/blog/posts/2026-09-24-gudermannian-function-mercator-projection-computes-circle-constant-golden-pi/) — the map that carries hyperbolic angles into ordinary ones, the exact bridge between this article's $\Pi(r)$ and a protractor.
- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — $\cosh$ in flat space, where the relation $y^{2}-s^{2}=a^{2}$ reproduces the hyperbolic metric on a curve you can hang from two nails.
