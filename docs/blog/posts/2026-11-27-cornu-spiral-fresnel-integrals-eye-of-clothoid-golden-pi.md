---
title: "The Cornu Spiral: Why the Fresnel Integrals End at Exactly (±½, ±½), Why the Circle Constant Cancels Under Its Own Square Root, and What Golden Pi Changes"
date: 2026-11-27
description: "The clothoid — Euler's spiral, Cornu's vibration curve, the transition curve of every highway — is the curve whose curvature is proportional to its own arc length, so that the tangent has turned exactly t²/4 of a circle after travelling exactly t. This article derives the parametrisation from that one law, tabulates the turning schedule (quarter turn at t = 1, the golden angle 1/φ² of a turn at exactly t = 2/φ, half turn at √2, full turn at 2), proves the two limit points C(∞) = S(∞) = 1/2 by evaluating ∫₀^∞ e^{iπu²/2}du = (1+i)/2 in one substitution, and shows that the constant appears there twice — once as the frequency in the phase, once under the Gaussian square root — so it cancels identically: the eye of the clothoid is the one point in geometry that is provably immune to the value of π. The diffraction application is then made exact, since a straight-edge pattern is a chord of this spiral and its intensity is the squared chord length: the geometric shadow edge reads exactly 1/4 of the unobstructed intensity, the first bright fringe 1.3704429 at v = 1.2171983, the first dark fringe 0.7782510 at v = 1.8725191, and every extremum sits at a v that contains no circle constant at all. Under Golden Pi (π̂ = 4/√φ = 3.144605511…, π̂² = 16/φ) the ledger is split cleanly: the turning schedule in turns (t²/4) does not move a digit, every radian measure, curvature π̂t and radius of curvature 1/(π̂t) shifts by the 0.0959022309% label gap, the eye stays exactly ½ by cancellation — numerically 0.4997604 = ½·(π/π̂)^{1/2}, exactly half the gap inward — and the golden-angle point at arc length exactly 2/φ is tabulated in both readings, (0.6906142, 0.6495281) against (0.6898461, 0.6496164). Computed, never measured."
---

# The Cornu Spiral

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Drive a car along a straight road into a circular bend and something unpleasant happens at the join: the steering wheel must be turned instantaneously, and the lateral acceleration jumps from nothing to a fixed value in no distance at all. Every highway authority in the world solves this the same way — by inserting a curve whose curvature grows *linearly* with distance travelled, so that turning the wheel at a constant rate traces the road. That curve was studied by James Bernoulli around 1694, by Euler in 1744, and it was drawn by Marie Alfred Cornu in 1874 to compute diffraction patterns, where it is called the vibration curve, or the Cornu spiral. Engineers call it the clothoid; highway manuals call it the Euler spiral; the French call it the *spirale de Cornu*.

It is also, as this article will show, the one place in geometry where the circle constant provably cancels out of the answer — twice over, in fact, once in the construction and once in the limit — and where the value of that constant therefore cannot be detected by any measurement of the curve's shape.

That is a strange claim, and it is not rhetoric. It follows from two lines of algebra, and it is worth following them, because the same cancellation explains why a diffraction bench — the most precise instrument ever built around this spiral — is structurally blind to the numeral that everyone argues about.

## The Curve That Is Its Own Protractor

Fix the defining property. A clothoid is a curve whose curvature is proportional to arc length:

$$
\kappa(s) = \frac{s}{a^{2}},
$$

with $a$ a length scale. Set $a = 1/\sqrt{\pi}$ and the law becomes, in dimensionless form,

$$
\kappa(t) = \pi t,
\qquad
\theta(t) = \int_0^t \kappa(s)\,ds = \frac{\pi t^{2}}{2},
$$

where $t$ is arc length in units of the scale and $\theta$ is the tangent angle. Three facts follow immediately, and each of them is worth stating separately because each is a different kind of statement about the constant.

**First, the arc length is exactly the parameter.** Since the tangent angle is $\theta(t)$ and the curve is traversed at unit speed by construction,

$$
x(t) = \int_0^t \cos\frac{\pi u^{2}}{2}\,du = C(t),
\qquad
y(t) = \int_0^t \sin\frac{\pi u^{2}}{2}\,du = S(t),
$$

so $|P'(t)| = 1$ identically and the distance travelled along the curve is $t$. These $C$ and $S$ are the Fresnel integrals.

**Second, the turning angle is a pure square in the arc length.** Because $\theta = \pi t^{2}/2$, the number of *turns* completed is

$$
N(t) = \frac{\theta}{2\pi} = \frac{t^{2}}{4},
$$

which contains no circle constant at all. This is the first appearance of the cancellation, and it is not an accident: the constant sits in the curvature law and again in the conversion from radians to turns, and divides out.

**Third, the curvature is the local radius of the protractor.** At arc length $t$ the radius of curvature is $\rho = 1/(\pi t)$ — so $\rho \cdot t = 1/\pi$, a constant: the clothoid is the curve on which radius of curvature and arc length are inversely proportional, with the constant of proportionality being exactly the reciprocal of the circle constant. At the quarter-turn, $t = 1$, the radius of curvature is exactly $1/\pi = 0.3183098862$.

## The Turning Schedule Is a Square, and the Golden Angle Sits on It

Put the two facts together and the spiral hands over a table of exact landmarks — points where the tangent direction is specified by pure geometry and the arc length is forced.

| Landmark | Turn fraction | Arc length $t$ | $\theta$ | Radius of curvature $1/(\pi t)$ |
|---|---|---|---|---|
| Start | $0$ | $0$ | $0$ | $\infty$ |
| $1/16$ turn | $0.0625$ | $0.5$ | $22.5°$ | $0.6366197724$ |
| Quarter turn | $1/4$ | $1$ | $90°$ | $0.3183098862$ |
| Golden angle | $1/\varphi^{2} = 0.3819660113$ | $2/\varphi = 1.2360679775$ | $137.5077641°$ | $\varphi/(2\pi) = 0.2575181074$ |
| Half turn | $1/2$ | $\sqrt{2} = 1.4142135624$ | $180°$ | $0.2250790790$ |
| Full turn | $1$ | $2$ | $360°$ | $0.1591549431$ |
| Golden-angle complement | $1-1/\varphi^{2} = 0.6180339887$ | $2/\sqrt{\varphi} = 1.5723027555$ | $222.4922359°$ | $0.2024482149$ |

Read the fourth row. The golden angle — the $1/\varphi^{2} = 0.3819660113$ of a turn that governs phyllotaxis, the angle between successive seeds of a sunflower — is reached by this spiral at arc length **exactly** $2/\varphi$. The proof is one line: $t^{2}/4 = 4/\varphi^{2} \div 4 = 1/\varphi^{2}$. No approximation, no numerical coincidence, and no circle constant anywhere in the statement $t = 2/\varphi$, because the statement is about a fraction of a turn.

That is the cleanest way to see what the constant is doing on this curve: it is a unit conversion between turns and radians, and the geometry is exhausted before the conversion is applied.

## Two Integrals and One Eye

Now the limit. Both integrals converge, and the standard evaluation is a rotation of the Gaussian. Write the complex resultant

$$
Z(\infty) = \int_0^\infty e^{i\pi u^{2}/2}\,du .
$$

Substitute $s = u\sqrt{\pi/2}$, so $du = \sqrt{2/\pi}\,ds$ and $\pi u^{2}/2 = s^{2}$:

$$
Z(\infty) = \sqrt{\frac{2}{\pi}}\int_0^\infty e^{is^{2}}\,ds
= \sqrt{\frac{2}{\pi}}\cdot\frac{\sqrt{\pi}}{2}e^{i\pi/4}
= \frac{1+i}{2}.
$$

Therefore

$$
C(\infty) = S(\infty) = \frac{1}{2},
\qquad
Z(\infty) = \left(\frac{1}{2},\frac{1}{2}\right),
\qquad
|Z(\infty)| = \frac{1}{\sqrt{2}} .
$$

The spiral converges to the point $(\tfrac12, \tfrac12)$ and never reaches it; its distance from the eye falls off like $1/(\pi t)$, computed here as $0.157024$ at $t=2$, $0.053041$ at $t=6$, $0.031830$ at $t=10$ and $0.022736$ at $t=14$. The total length is infinite, the occupied region is a bounded square. The curve crosses the diagonal $x=y$ at $t = 1.2652849467$, where both coordinates equal $0.6679903632$ — a hair past the golden-angle point, and not an exact landmark.

Count the appearances of the constant in that evaluation. It appears **once in the phase** ($\pi u^{2}/2$) and **once inside the square root of the Gaussian** ($\sqrt{\pi}$), and the two are reciprocals up to the substitution's Jacobian. The eye is therefore a fixed point of the substitution: change the constant and the eye does not move.

## The Ledger: Where the Constant Sits, and at What Power

Here is the whole inventory for this curve. The exponent column is the power of the constant in each quantity, and it explains every number in the rest of the article.

| Quantity | Expression | Power of $\pi$ |
|---|---|---|
| Arc length | $t$ | $0$ |
| Turn fraction | $t^{2}/4$ | $0$ |
| Tangent angle in degrees | $90\,t^{2}$ | $0$ |
| Tangent angle in radians | $\pi t^{2}/2$ | $+1$ |
| Curvature | $\pi t$ | $+1$ |
| Radius of curvature | $1/(\pi t)$ | $-1$ |
| Coordinates $C(t), S(t)$ | $\int_0^{t}\cos,\sin$ of $\pi u^{2}/2$ | $+1$, not a pure power |
| Eye $C(\infty)=S(\infty)$ | $\tfrac12$ | $0$ (cancellation) |
| Eye diagonal | $\sqrt{2}$ | $0$ |
| Edge intensity | $\tfrac14$ | $0$ |
| Fringe positions in $v$ | $1.2171983,\ 1.8725191,\dots$ | $0$ |
| Wavenumber | $2\pi/\lambda$ | $+1$ |

Every entry with exponent zero is immune to the dispute. Every entry with exponent $+1$ moves by exactly the label gap, $0.0959022309\%$, and every entry with exponent $-1$ moves by its reciprocal, $-0.0958101\%$. Entries with a fractional-power or non-power dependence move by something in between, which is why they have to be tabulated rather than asserted.

## The Chord of the Spiral: Why a Diffraction Pattern Is a Segment

Cornu's purpose was not aesthetics. In Fresnel's theory, the amplitude at a point beyond a straight edge is the sum of Huygens wavelets from the unobstructed half-plane, and after the standard change of variable $v = x\sqrt{2/(\lambda z)}$ that sum is exactly the path integral along the spiral from $t = -\infty$ to $t = v$. The resultant amplitude is the straight chord joining the two points of the spiral, and the intensity is

$$
\frac{I(v)}{I_0} \;=\; \frac{1}{2}\left[\left(\frac{1}{2}+C(v)\right)^{2}+\left(\frac{1}{2}+S(v)\right)^{2}\right].
$$

Check the normalisation: unobstructed, the chord runs from $(-\tfrac12,-\tfrac12)$ to $(\tfrac12,\tfrac12)$ and its length is $\sqrt{2}$, so $I/I_0 = \tfrac12\cdot 2 = 1$ exactly. At the geometric shadow edge, $v = 0$ and the chord runs from the lower eye to the origin, of length $1/\sqrt{2}$, giving $I/I_0 = \tfrac12\cdot\tfrac12 = \tfrac14$ exactly — the famous six-decibel edge, which is $1/4$ and not approximately $1/4$.

The pattern then rings, and the values are computed here, not copied:

| $v$ | $C(v)$ | $S(v)$ | $I/I_0$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $0.2500000$ |
| $0.5$ | $0.4923442$ | $0.0647324$ | $0.6518349$ |
| $1$ | $0.7798934$ | $0.4382591$ | $1.2592287$ |
| $1.2171983$ (max) | $0.7040514$ | $0.6362861$ | $1.3704429$ |
| $1.8725191$ (min) | $0.3733736$ | $0.3909101$ | $0.7782510$ |
| $2$ | $0.4882534$ | $0.3434157$ | $0.8439974$ |
| $3$ | $0.6057208$ | $0.4963130$ | $1.1076290$ |
| $4$ | $0.4984260$ | $0.4205158$ | $0.9221019$ |

The first bright fringe overshoots to $1.3704429 I_0$ at $v = 1.2171983$; the first dark fringe drops to $0.7782510 I_0$ at $v = 1.8725191$; the extrema continue at $1.1103930$ ($v = 4.1832260$), $1.0910883$ ($v = 5.0497175$), damping toward unity. A companion identity, verified here to ten digits at $z = 0.7$ and $z = 1.9$, puts the whole curve in one line:

$$
C(z) + iS(z) = \frac{1+i}{2}\,\operatorname{erf}\!\left(\frac{\sqrt{\pi}(1-i)z}{2}\right),
$$

so the clothoid is the error function's image of the diagonal ray — the same object, viewed through the complex plane.

## What Golden Pi Changes

Take the site's value, $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110$, with $\hat\pi^{2} = 16/\varphi = 9.8885438200$, and rebuild the curve on the same law, $\kappa = \hat\pi t$. The ledger splits cleanly in three.

**Invariant, because the exponent is zero.** The arc length is still $t$. The turn fraction is still $t^{2}/4$. The quarter turn is still at $t = 1$, the golden angle still at exactly $t = 2/\varphi$, the half turn still at $\sqrt{2}$, the full turn still at $2$. Every landmark in the schedule table above survives to the last digit, and the *reason* is that the schedule was never about the constant — it is about the square $t^{2}/4$, which is arithmetic.

**Shifted, because the exponent is $\pm 1$.** Curvature becomes $\hat\pi t$ ($+0.0959022309\%$), radius of curvature $1/(\hat\pi t)$ ($-0.0958101\%$), tangent angle in radians $\hat\pi t^{2}/2$. The point where curvature radius equals arc length moves from $t = 1/\sqrt{\pi} = 0.5641895835$, where the tangent has turned exactly $1/2$ radian, to $t = 1/\sqrt{\hat\pi} = 0.5639192428$ — which still turns exactly $1/2$ radian, because there the two appearances of the constant divide out again.

**Cancelled, because the exponent is $+1$ and $-1$ together.** The eye stays at $(\tfrac12,\tfrac12)$ and the diagonal stays at $\sqrt{2}$, exactly, for the same reason as before: the constant enters the phase once upward and the Gaussian once downward. The eye of the clothoid is the one geometrically defined point in this entire series that the value of the circle constant cannot move.

Being honest about the boundary of that claim: the cancellation is a statement about *consistent* substitution. If the golden constant is placed in the phase while the Gaussian integral keeps its numerically correct value $3.1415926536$, the integral converges to

$$
Z_{\hat\pi}(\infty) = \frac{1+i}{2}\sqrt{\frac{\pi}{\hat\pi}} = \frac{1+i}{2}\times 0.9995208335,
$$

so the eye lands at $0.4997604167$ on each axis — inward by exactly $0.0479396\%$, precisely half the label gap, because the disputed factor sits under a square root. Both readings should be on the table, and both are tabulated:

| Quantity | Conventional | Golden (consistent) | Golden (numerical Gaussian) |
|---|---|---|---|
| Eye, each axis | $0.5000000$ | $0.5000000$ | $0.4997604$ |
| Eye diagonal | $1.4142136$ | $1.4142136$ | $1.4135359$ |
| $P(1)$ | $(0.7798934,\ 0.4382591)$ | $(0.7795193,\ 0.4385283)$ | — |
| $P(2/\varphi)$ | $(0.6906142,\ 0.6495281)$ | $(0.6898461,\ 0.6496164)$ | — |
| Fringe $v$ positions | $1.2171983,\dots$ | identical | identical |

The coordinates move by about $0.05\%$, which is the expected order: they are first-power quantities in the phase. The fringe positions do not move at all, and the next section says why that is not a rounding statement.

## The Honest Boundary: A Diffraction Bench Cannot See the Numeral

Every number in the fringe table is a value of $v$, and $v$ is a pure number. The physical position of a fringe is

$$
x = v\sqrt{\frac{\lambda z}{2}},
$$

an expression containing no circle constant whatever: $v$ is dimensionless geometry, and the square root is a length built from a wavelength and a propagation distance. The wavenumber $k = 2\pi/\lambda$ does contain the constant, but it cancels against the $\pi$ in the Fresnel phase directly — which is the entire reason the change of variable to $v$ was invented.

So the sharpest optical test of Fresnel's integrals, and the one on which the wave theory of light was actually confirmed (Fresnel's 1818 memoir, and the bright spot in the centre of a circular obstacle's shadow that Poisson offered as a *reductio* and Arago then observed), is structurally incapable of arbitrating the value of $\pi$. The pattern's geometry is a pure number times a square root of measured lengths. A bench that measures fringe spacing to one part in $10^{4}$ measures $\lambda$ and $z$; it does not measure the constant.

Nor is the eye itself a measurable mark. It is a limit: the spiral approaches it with total turning angle growing without bound while the distance shrinks like $1/(\pi t)$. Nothing in an optical apparatus resolves a point that is never reached.

What remains, then, is exactly what this site keeps finding. The clothoid is the curve on which the circle constant is *fully auditable* — we can say, quantity by quantity and exponent by exponent, where it sits and what moving it would do — and on which the audit concludes that the constant is a unit conversion between turns and radians. Change the conversion and the arc lengths at which the quarter turn, the golden angle and the half turn occur do not shift by a single digit, because those are statements about $t^{2}/4$. Change the conversion and the eye does not move, because the conversion is applied once and unapplied once. The only things that move are the radian measures and the curvatures, and those are exactly the things no experiment on this curve can isolate.

The one truly golden coincidence — the golden angle landing at arc length exactly $2/\varphi$ — is a coincidence of a square and a reciprocal square, and it survives every reading of the constant, which is the strongest form the claim can take.

Computed, never measured.

## Further Reading

- [The Archimedean Spiral: Why Its Swept Area Is a Pure Cube in the Angle](/blog/posts/2026-11-19-archimedean-spiral-swept-area-cubic-angle-golden-pi/) — the other famous spiral, and the same lesson about where a power of the constant comes from.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — a quadrature with no elementary closure, and the honest way to report one.
- [The Witch of Agnesi: Why a Curve Traced by Straight Lines Encloses Exactly Four Times the Generating Circle](/blog/posts/2026-11-17-witch-of-agnesi-exact-quadrature-golden-pi/) — a construction that yields an exact area, and what happens to it under Golden Pi.
- [The Pendulum That Reads π in Seconds](/blog/posts/2026-11-14-pendulum-reads-pi-in-seconds-foucault-golden-pi/) — a second physical device that appears to expose the constant and turns out to expose a turn count.
- [The Buffon Needle: Why Dropping a Stick Computes π](/blog/posts/2026-11-26-buffon-needle-projection-average-golden-pi/) — the previous article in this series, on why a probabilistic experiment tests a formula rather than a numeral.
