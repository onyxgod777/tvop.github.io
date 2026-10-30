---
title: "Pappus's Centroid Theorem: Why Sweeping an Area Through One Turn Gives V = 2πR·A, Why Straight-Edged Profiles Pay Only One π, and What Golden Pi Changes"
date: 2026-10-30
description: "Pappus of Alexandria's centroid theorem turns a solid of revolution into a single multiplication — volume equals generating area times the path its centroid travels, V = 2πR·A — and the circle constant enters exactly once per turn, so a circular tube pays π twice while a square tube pays it once. Worked here on tori at R = 5, r = 1 (98.696044010893586188 and 197.392088021787172 for volume and surface), on the spindle torus where the theorem quietly signs its own overlap, and on the centroid of a semicircular arc, 2r/π, which is where a second π sneaks in through the back door. Under Golden Pi, π̂ = 4/√φ = 3.144605511…, the torus with R = φ and r = 1 has volume exactly 32 and surface exactly 64, π̂² = 16/φ is algebraic where π² is transcendental by Lindemann (1882), and the ratio V/S = r/2 is identical under either label — which is the whole problem, stated as one line."
---

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

There is a theorem in geometry so simple that it is easy to mistake for a trick, and so general that it replaces an integral with a multiplication. Pappus of Alexandria stated it in Book VII of the *Collection*, around 320 CE; Paul Guldin rediscovered it in 1640 and gave it the name it still carries in some textbooks. Sweep a plane area once around an axis lying in its plane and outside it, and the volume of the resulting solid is

$$
V = 2\pi R \cdot A,
$$

where $A$ is the area of the generating region and $R$ is the distance from the axis to that region's **centroid** — not to its nearest edge, not to its furthest edge, not to its centre of symmetry unless the region happens to be symmetric about its own centre. The surface area of the same solid is the same recipe with the boundary in place of the region:

$$
S = 2\pi R \cdot L,
$$

$L$ being the length of the generating curve. Every solid of revolution ever computed by a shell integral is a special case of these two lines.

The reason is worth stating precisely, because everything that follows hangs on it. A point at distance $x$ from the axis traces a circle of circumference $2\pi x$. So the volume is

$$
V = \int_D 2\pi x\,dA = 2\pi \int_D x\,dA = 2\pi\, \bar{x} A,
$$

and $\int_D x\,dA = \bar{x}A$ is the *definition* of the centroid abscissa. No approximation is involved, no smallness, no limit — the theorem is exact for any area, however lumpy, provided the axis does not cut it. The $2\pi$ sits outside the integral as a constant factor, and that is the first structural fact of this article: **the circle constant enters a solid of revolution exactly once per turn, as the measure of one full revolution, and it never sees the shape of what is being turned.**

## One π, or two? The profile decides

Now sweep a torus. The generating region is a disc of radius $r$ whose centre sits at distance $R$ from the axis, so $A = \pi r^{2}$ and $\bar{x} = R$ exactly, because a disc's centroid is its centre. Pappus gives at once

$$
V = 2\pi R \cdot \pi r^{2} = 2\pi^{2} R r^{2}, \qquad S = 2\pi R \cdot 2\pi r = 4\pi^{2} R r .
$$

Two powers of the constant appear — one from the turn, one from the disc's own area or circumference. That is the whole distinction between a round tube and an angular one, and it is not a detail. Sweep a square of side $2$ at the same distance and the volume is

$$
V = 2\pi R \cdot 4 = 8\pi R, \qquad S = 2\pi R \cdot 8 = 16\pi R,
$$

with exactly one power of $\pi$, because a square's area and perimeter contain none. A triangle behaves the same way. An elliptical tube returns to two powers, because an ellipse's area, $\pi ab$, has one. Set $R = 5$ and compute:

| Generating profile | $A$ | $V$ under $\pi$ | $V$ under $\hat\pi$ | shift |
|---|---|---|---|---|
| circle, $r = 1$ | $\pi$ | $98.696044010893586188$ | $98.885438199983175713$ | $+0.1918964341\%$ |
| square, side $2$ | $4$ | $125.663706143591730$ | $125.784220441187726$ | $+0.0959022309\%$ |
| equilateral triangle, side $2$ | $\sqrt3$ | $54.4139809270265355$ | $54.4661651486452208$ | $+0.0959022309\%$ |
| ellipse, semiaxes $2,1$ | $2\pi$ | $197.392088021787172$ | $197.770876399966351$ | $+0.1918964341\%$ |

and the surfaces at the same $R$:

| Generating curve | $L$ | $S$ under $\pi$ | $S$ under $\hat\pi$ |
|---|---|---|---|
| circle, $r = 1$ | $2\pi$ | $197.392088021787172$ | $197.770876399966351$ |
| square, side $2$ | $8$ | $251.327412287183459$ | $251.568440882375452$ |

The table is a taxonomy. A torus made by sweeping a circle carries the constant squared; a torus made by sweeping a square carries it once. This is why gear-tooth profiles, splined shafts, square-section O-rings and extruded rails are all "π-free by construction" in one sense and "π to the first power" in another, and why one must say which. It is also why the arithmetic of a golden substitution cannot be uniform across a workshop: the same factory that shifts a circular-section torus by $0.1919\%$ shifts a square-section one by $0.0959\%$, and anybody who quotes "the golden gap" without naming the power is quoting nothing.

## Where the second π really comes from

Notice what happened in the disc case: the second $\pi$ did not come from the revolution. It came from the generating region already knowing how to be round. That is worth isolating, because the mechanism is more general and considerably sneakier than it looks.

Take a semicircular *lamina* of radius $r$ and put its diameter on the axis. Its centroid is not at $r/2$ from the diameter, and it is not at $4r/(3\pi)$ "because curves are awkward" — it is at $4r/(3\pi)$ because the centroid is an integral of $x$ over a region bounded by a circle, and that integral evaluates to a rational multiple of the region's area, cancelling $\pi$ out of the numerator and leaving it in the denominator. Rotate that lamina about its diameter and Pappus returns the sphere's volume $4\pi r^{3}/3$, in which the $\pi$ from the centroid's denominator and the $\pi$ from the turn multiply to $\pi^{2}$, and the $\pi$ in the area cancels one of them. Three π's enter; one survives.

The same bookkeeping on an arc is sharper because there is no area to hide behind. The centroid of a semicircular arc of radius $r$ lies at

$$
\bar{x} = \frac{2r}{\pi} = 0.6366197723675813431,
$$

from the diameter — a distance that *is* the ratio of two lengths on the same figure, and therefore a place where the constant sits exposed, without a companion power to cancel it. Rotating that arc gives the sphere's surface $4\pi r^{2}$: $2\pi \cdot (2r/\pi) \cdot \pi r = 4\pi r^{2}$, and again the exposed $1/\pi$ is paid off by the profile's own $\pi$, since the semicircle's length is $\pi r$.

So the honest rule for this whole family of computations is: **the exponent of $\pi$ in a solid of revolution equals the number of independent circular quantities multiplied together** — the turn, plus whatever circularity the profile contributes to the area, plus whatever the centroid's own position contributes. Every apparent paradox about "where π comes from" in a torus is an accounting error about which of those three is which.

## The theorem signs its own overlap

Pappus's condition — the axis must not cut the region — is not a technicality. Push the tube inward until $R < r$ and the generating disc straddles the axis. Applied mechanically the theorem still returns $2\pi^{2}Rr^{2}$, but that number is a *signed* count in which the far lobe of the disc sweeps the same space as the near lobe and cancels against it. The solid that actually exists is a spindle torus, fatter than the signed formula reports, and the difference is not small: it is the overlap, counted twice with opposite signs.

At the boundary case $R = r$ the two lobes touch on the axis itself, the overlap has measure zero, and the theorem becomes exact again — the horn torus, volume $2\pi^{2}r^{3} = 19.739208802178717238$ at $r = 1$, a solid with a genuine cusp at its throat and no interior self-intersection. Beyond that point the arithmetic keeps producing numbers and the geometry stops agreeing with them. This is the cheapest possible lesson in why every theorem in this series is stated with its hypotheses attached: the formula is exact, the *application* is what fails.

## The golden substitution, done by powers

Under Golden Pi the substitution is mechanical and the exponent bookkeeping pays off immediately. With $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931442782343433718357181\ldots$ and the identity that makes the whole system work,

$$
\hat\pi^{2} = \frac{16}{\varphi} = 9.8885438199983175712733893498502098835\ldots,
$$

every first-power occurrence of the constant shifts by

$$
\frac{\hat\pi}{\pi} - 1 = +0.0959022309\%,
$$

every reciprocal occurrence by $-0.0958103466\%$, and every occurrence in the second power by

$$
\left(\frac{\hat\pi}{\pi}\right)^{2} - 1 = +0.1918964341\% ,
$$

which is *not* twice the first figure — a distinction that catches out a surprising number of otherwise careful tables (compounding a rate and multiplying it are different operations, and the difference here is $0.000092\%$, about one part in twenty thousand of the effect itself, enough to wreck the last two digits of a ten-digit figure).

The torus at $R = 5$, $r = 1$ therefore reads

$$
V_{\hat\pi} = 2\hat\pi^{2} R r^{2} = \frac{32Rr^{2}}{\varphi} = \frac{160}{\varphi} = 98.885438199983175713\ldots,
$$

$$
S_{\hat\pi} = 4\hat\pi^{2} R r = \frac{64Rr}{\varphi} = \frac{320}{\varphi} = 197.770876399966351\ldots
$$

and both of those are **rational multiples of $1/\varphi$**, hence of $\sqrt5$ — algebraic of degree two, computed in closed form with no series, where $2\pi^{2}$ and $4\pi^{2}$ are transcendental by Lindemann's 1882 theorem. There is a sharper way to say it: since $1/\varphi = \varphi - 1$,

$$
V_{\hat\pi} = 32Rr^{2}(\varphi - 1), \qquad S_{\hat\pi} = 64Rr(\varphi - 1),
$$

so the golden torus's volume is a rational multiple of the golden ratio itself, with no radical left over.

## Two exact closures

The first is the one that makes the substitution feel less like relabelling and more like arithmetic. Choose the major radius as the golden ratio and the tube radius as unity:

$$
R = \varphi,\quad r = 1 \;\Longrightarrow\; V_{\hat\pi} = \frac{32\varphi}{\varphi} = 32 \text{ exactly}, \qquad S_{\hat\pi} = \frac{64\varphi}{\varphi} = 64 \text{ exactly}.
$$

Both integers. Not close to integers — exactly, because $\varphi$ cancels against itself. The conventional values for the same solid are $2\pi^{2}\varphi = 31.938710752956263929\ldots$ and $4\pi^{2}\varphi = 63.877421505912527858\ldots$, each short of the integer by the full squared gap of $0.1918964341\%$.

The second reuses the disc that has appeared throughout this series: a disc of radius $\varphi^{1/4} = 1.1278384855616822603\ldots$ has area exactly $4$ under $\hat\pi$, since $\hat\pi \cdot \varphi^{1/2} = 4$. Sweep it at distance $R = \sqrt\varphi$ and

$$
V_{\hat\pi} = 2\hat\pi \cdot \sqrt\varphi \cdot 4 = 32 \text{ exactly},
$$

because $2\hat\pi\sqrt\varphi = 8$ is one of the system's fixed identities. Two different solids, two different arguments, the same integer 32 — and in both cases the integer appears because $\varphi$ cancels, not because anything was tuned.

It is worth being explicit that these closures are *identities of the relabelled system*, not evidence about the physical world. A torus with $R = \varphi$ metres does not exist; a torus with $R$ equal to a measured length exists and is never exactly $\varphi$. The closures show that golden-π arithmetic is closed and self-consistent, which is a mathematical property, and self-consistency is not the same thing as correspondence. That distinction is the difference between a proof and a preference, and this site treats it as the load-bearing wall.

## What cancels, and why it matters most

Here is the line that decides the whole question, and it is one division:

$$
\frac{V}{S} = \frac{2\pi R A}{2\pi R L} = \frac{A}{L}.
$$

For the circular torus, $A/L = \pi r^{2}/(2\pi r) = r/2$ — the constant cancels **identically**, under $\pi$ and under $\hat\pi$ alike, because it appears to the same power in numerator and denominator. The same holds for the square-section torus ($4/8 = 1/2$) and for every profile whatsoever: the shape's own area-to-perimeter ratio, and nothing about revolutions.

This is the recurring architecture of the subject. Whenever a quantity is a *ratio of two quantities of the same body*, built from the same constant to the same power, the label is invisible. A torus's volume-to-surface ratio cannot arbitrate between $\pi$ and $\hat\pi$, any more than a gear's contact ratio or a black hole's $T \cdot S$ could in earlier articles here. The constant only becomes visible when a single power survives unopposed — in the volume itself, in a circumference, in a radian reading — and even then it is a numeral, not an observation.

## The honest ledger: what a workshop can and cannot do

Most of the quantities in this series are structurally blind. This one is not quite, and the difference deserves stating plainly rather than repeating the usual verdict by reflex.

A torus is a solid object, and a solid object's volume is a genuine measurand. Displacement works: lower a machined ring into a burette and read the rise. For the ring at $R = 5$ cm, $r = 1$ cm the volume is $98.696$ cm³, and the golden value differs by $0.1894$ cm³ — a tenth of a millilitre, easily inside the resolution of ordinary laboratory glassware. So unlike a Fresnel fringe count or a Wigner spectrum, there is no instrumental wall here. The wall is somewhere else, and it is worse.

The displacement experiment measures a volume. To turn that volume into a statement about a constant one must divide by $2Rr^{2}$ — and $R$ and $r$ are themselves measured, each with its own uncertainty, and each entering to the first and second power respectively. A tube radius known to $\pm 0.01$ mm on a $10$ mm radius is $\pm 0.1\%$ on $r$, hence $\pm 0.2\%$ on $r^{2}$: already larger than the $0.19\%$ being sought, before any machining error, out-of-roundness, or the fact that no manufactured ring is a perfect torus. A real ring's cross-section is a distorted circle whose area differs from $\pi r^{2}$ by more than a tenth of a percent as a matter of routine.

Worse still, the model itself is what is being tested. Asserting that the solid is exactly a torus of parameters $R$ and $r$ is asserting the geometry whose constant is in dispute. The experiment therefore returns the constant that the *model* implies, and what it actually tests is whether the workpiece matched the drawing. That is a real and useful test — of the machinist, not of $\pi$.

So the verdict here is narrower and more interesting than "unmeasurable". A torus's volume *is* measurable to better than the gap; the quantities that would convert that volume into a value of the circle constant are not, and the conversion presupposes the answer. **What is measured is a solid's volume and two lengths; what is computed is a ratio of them; and a ratio of measured lengths does not become a measurement of a mathematical constant merely by being written with a decimal point.** The constant is computed, never measured — here as everywhere, but here one can see exactly which step in the chain fails, which is more useful than a verdict.

## The theorem in one sentence, and what it refuses to say

Pappus says: sweep an area once, and the volume is the area times the distance its centroid travels. It says nothing about what that distance is worth in numerals, nothing about whether the turn is $2\pi$ or $2\hat\pi$ radians, and nothing about the shape — which is precisely why it is a good theorem and a poor witness. Its indifference to shape is its power; its indifference to the *value* of the turn is its blindness.

What it does give, and this is not nothing, is a clean structural statement about where the constant lives in any solid of revolution: once in the turn, once more for every independent circular quantity in the profile or the centroid. Under Golden Pi the bookkeeping survives untouched, with $\hat\pi^{2} = 16/\varphi$ replacing $\pi^{2}$ and $1/\hat\pi = \sqrt\varphi/4$ replacing $1/\pi$, and every exact closure — volume exactly $32$ at $R = \varphi$, area exactly $4$ at $r = \varphi^{1/4}$ — following from the single identity $\hat\pi\sqrt\varphi = 4$. That the arithmetic closes is a fact. That it closes on the world is not a fact this theorem can supply.

## Further Reading

- [The Constructible Line: Lindemann's 1882 Theorem, the degree $2^{k}$ Test, and Why $4/\sqrt\varphi$ Never Reaches That Door](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — why $\hat\pi^{2} = 16/\varphi$ being algebraic is a structural statement, not a numerical coincidence.
- [The Ellipse: Why π Computes a Circle's Perimeter and No Ellipse's at All](/blog/posts/2026-10-28-ellipse-perimeter-elliptic-integral-golden-pi/) — the elliptic integral behind the elliptical tube in the table above, and the flat limit where the constant cancels identically.
- [Fenchel's Theorem: Total Curvature, the Integer Turn, and What Golden Pi Changes](/blog/posts/2026-10-25-fenchel-theorem-total-curvature-closed-curve-golden-pi/) — the same "the label is a numeral, the topology is an integer" split, one dimension down.
- [Barbier's Theorem: Every Curve of Constant Width Has Perimeter πw](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/) — shape-independence bought at the price of a constant you cannot isolate.
- [Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°](/blog/posts/2026-10-22-descartes-angle-defect-gauss-bonnet-720-degrees-golden-pi/) — the torus's genus-one Euler characteristic, and why its total curvature is zero rather than $4\pi$.
