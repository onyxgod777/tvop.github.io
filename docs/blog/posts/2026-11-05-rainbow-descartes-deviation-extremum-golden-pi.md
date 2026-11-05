---
title: "The Rainbow: Why Descartes' 42° Is the Minimum of a π-Free Deviation Function, Why the Half-Turn Cancels From the Primary Bow Entirely, and What Golden Pi Changes"
date: 2026-11-05
description: "The primary rainbow's 42° is not a circle measurement — it is the extremum of the deviation D(i) = π + 2i − 4r of a ray refracted into a sphere and reflected once inside, and for the primary bow the half-turn cancels identically, leaving the pure refraction expression 4r − 2i with no circle constant in it anywhere. This article derives the extremum condition cos²i = (n² − 1)/(k² + 2k) in two lines, works it for real water (red n = 1.331: i = 59.52674718°, r = 40.35583389°, D = 137.6301588°, bow 42.3698412°; violet n = 1.343: 58.83032955°, 39.57663491°, 139.3541195°, 40.64588052°), for n = 4/3 (42.02965887° primary, 50.97809353° secondary, Alexander band 8.9484347° wide), and traces the one place the constant does survive — Airy's 1838 caustic, whose asymptotic amplitude carries π^(−1/2) = 0.564189583548 and whose supernumerary zeros sit at −2.33810741, −4.087949444, −5.520559828, with fringe scales of 0.68247205° (a = 0.5 mm), 0.42993045° (1 mm) and 0.27083921° (2 mm). Under Golden Pi (π̂ = 4/√φ = 3.144605511029693144…) the geometry is untouched and only radian numerals shift by +0.0959022309% at first power and −0.04791665334% at half power, so a 2.40209942102 rad deviation re-reads as 137.4982949° against 137.6301588° while 42.3698412° does not move a digit; the exact golden closure is a droplet of refractive index φ, where cos²i = φ/3 = 0.53934466291663161607 for the primary and φ/8 = 0.20225424859373685603 for the secondary, giving bows of 13.71763558° and 105.5188004° — algebraic where the general condition is a quotient of measured indices. The honest boundary: the bow formula contains no circle constant at all, so no rainbow, however finely read, can arbitrate one. Computed, never measured."
---

# The Rainbow

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1637 René Descartes, in the eighth discourse of *Les Météores*, did something that had defeated every natural philosopher before him: he explained why the rainbow's primary arc sits at about 42° from the antisolar point and the secondary at about 51° — not by naming a cause, but by finding an **extremum**. A ray entering a spherical drop, refracting, reflecting once inside, and refracting out again leaves at a total deviation $D(i)$ that depends on where it struck. Descartes traced rays by hand, found that $D$ does not vary monotonically, and saw that it stalls at a minimum. Rays crowd into the neighbourhood of that minimum; light piles up; a bright arc appears where a smooth function turns around.

That is the whole mechanism, and it is worth noticing what it is *not*: it is not a measurement of a circle. It is a computation of a stationary point. This article derives the extremum in closed form, works it for real water and for $n = 4/3$, locates the single place where the circle constant genuinely survives (Airy's caustic), and then asks the site's standing question: what changes if the constant is $\hat\pi = 4/\sqrt\varphi$ rather than $\pi = 3.14159265358979\ldots$?

## The deviation of one ray

Let $i$ be the angle of incidence at the drop's surface, $r$ the refracted angle with $\sin i = n\sin r$, and let $k$ be the number of internal reflections. At entry the ray is bent by $i - r$. Each internal reflection turns it by $\pi - 2r$. At exit it is bent by $i - r$ again. Summing:

$$
D_k(i) \;=\; 2(i-r) + k(\pi - 2r) \;=\; k\pi + 2i - 2(k+1)r .
$$

For the primary bow ($k = 1$) this reads $D_1 = \pi + 2i - 4r$, and the angle that an observer actually sees, measured from the antisolar axis, is the departure of the outgoing ray from the direction *back to the sun*:

$$
\beta_1 \;=\; \left| D_1 - \pi \right| \;=\; \left| 2i - 4r \right| .
$$

The $\pi$ has gone. It cancelled against the half-turn that defines "antisolar" — and what is left, $4r - 2i$, contains nothing but two refraction angles. The number everyone quotes as "42°" is a difference of arcsines. That cancellation is the structural fact this article is about, and it is exact, not approximate.

## The extremum, in two lines

Set $dD_k/di = 0$. From $D_k = k\pi + 2i - 2(k+1)r$ and $\sin i = n\sin r$:

$$
\frac{dD_k}{di} = 2 - 2(k+1)\frac{dr}{di} = 0,
\qquad
\frac{dr}{di} = \frac{\cos i}{n\cos r},
$$

so the stationary point satisfies $n\cos r = (k+1)\cos i$. Squaring and using $n^2\sin^2 r = \sin^2 i$:

$$
n^2 - \sin^2 i = (k+1)^2\cos^2 i
\;\Longrightarrow\;
n^2 - 1 + \cos^2 i = (k^2 + 2k + 1)\cos^2 i,
$$

$$
\boxed{\;\cos^2 i \;=\; \frac{n^2 - 1}{k^2 + 2k}\;}
$$

For $k = 1$ the denominator is $3$; for $k = 2$ it is $8$. No circle constant anywhere in the derivation — the equation is a condition on a cosine, i.e. on a length ratio in a right triangle.

There is also an existence condition, and it is the reason the bow is sometimes absent from a real sky: the internal reflection must not be total, so $r < \arcsin(1/n)$. For $n = 4/3$ that ceiling is $48.59037789°$, comfortably above the $40.20°$ and $45.45°$ the two bows actually use.

## Worked for water

Water's refractive index is a measured quantity, and it varies across the visible spectrum — that variation is the bow's colour. Taking $n = 1.331$ for the red end and $n = 1.343$ for the violet end:

| | $n$ | $i$ (stationary) | $r$ | $D$ | bow $\beta$ |
|---|---|---|---|---|---|
| Red, primary ($k=1$) | 1.331 | 59.52674718° | 40.35583389° | 137.6301588° | **42.3698412°** |
| Violet, primary ($k=1$) | 1.343 | 58.83032955° | 39.57663491° | 139.3541195° | **40.64588052°** |
| Red, secondary ($k=2$) | 1.331 | 71.90724988° | 45.57489696° | 230.3651180° | **50.36511802°** |
| Violet, secondary ($k=2$) | 1.343 | 71.52153849° | 44.92755224° | 233.4777635° | **53.47776353°** |

The primary spans $1.724°$ of colour; the secondary spans $3.113°$ and runs the *other* way — red inside, violet outside — which is why the secondary is called reversed. For a monochromatic droplet of $n = 4/3$:

| $k$ | $i$ | $r$ | $D$ | bow | $\pi$ remaining in $\beta$ |
|---|---|---|---|---|---|
| 1 | 59.39110234° | 40.20296589° | 137.9703411° | **42.02965887°** | none — $\beta = 4r - 2i$ |
| 2 | 71.83197124° | 45.44764149° | 230.9780935° | **50.97809353°** | one half-turn: $\beta = \pi + 2i - 6r$ |

Between the two bows lies Alexander's dark band, $50.97809353° - 42.02965887° = 8.9484347°$ wide, and its darkness has the same cause as the bows' brightness: no ray's stationary deviation falls in that interval, so nothing accumulates there.

A short script that reproduces every number in the table, with no circle constant typed anywhere:

```python
from math import asin, acos, sin, pi, degrees

def bow(n, k):
    # stationary incidence from cos^2 i = (n^2-1)/(k^2+2k)
    i = acos(((n*n - 1)/(k*k + 2*k))**0.5)
    r = asin(sin(i)/n)
    D = k*pi + 2*i - 2*(k+1)*r
    return degrees(i), degrees(r), degrees(D), degrees(abs(D - pi))

for n in (1.331, 1.343, 4/3):
    for k in (1, 2):
        print(n, k, ["%.8f" % x for x in bow(n, k)])
```

Run it and the fourth column returns $42.3698412$, $40.64588052$, $50.36511802$, $53.47776353$, $42.02965887$, $50.97809353$ — all *computed*, from a measured $n$ and a stationary-point condition. No protractor touched a drop.

## Where the constant actually survives: Airy's caustic

At the extremum the intensity would be infinite in geometric optics, since neighbouring rays arrive at the same angle. George Biddell Airy in 1838 replaced the singularity with a diffraction integral, and the pattern near the bow is the square of the Airy function, $I(\theta) \propto \operatorname{Ai}^2(z)$, with $z$ measuring angular displacement in units of the natural scale $(\lambda/a)^{2/3}$, $a$ the drop radius.

| drop radius $a$ | scale $(\lambda/a)^{2/3}$ | in degrees | in arcminutes |
|---|---|---|---|
| 0.5 mm | 0.011911384 | 0.68247205° | 40.948 |
| 1 mm | 0.007503702 | 0.42993045° | 25.796 |
| 2 mm | 0.004727036 | 0.27083921° | 16.250 |

Smaller drops give wider fringes — the reason faint supernumerary arcs are a feature of fine drizzle rather than fat raindrops. The minima of that pattern are the zeros of $\operatorname{Ai}$ on the negative axis:

$$
\operatorname{Ai}(z) = 0 \quad\text{at}\quad z = -2.33810741,\; -4.087949444,\; -5.520559828,\;\ldots
$$

spaced $1.749842$, then $1.4326104$ apart — the fringes crowd together away from the caustic. These zeros are pure numbers of the Airy differential equation $y'' = zy$; they contain no circle, and they are what a photograph of a supernumerary bow actually records.

**Here, at last, is a $\pi$** — but only in the far-field asymptotic amplitude of the Airy function,

$$
\operatorname{Ai}(-x) \;\sim\; \frac{1}{\sqrt\pi\,x^{1/4}}\sin\!\left(\tfrac{2}{3}x^{3/2} + \tfrac{\pi}{4}\right),
$$

where $\pi^{-1/2} = 0.564189583548$ normalises the oscillation. That number is the computed limit of a diffraction integral, never a measurement of anything round. Under Golden Pi it becomes $\hat\pi^{-1/2} = 2^{-1/2}\varphi^{1/4} = 0.563919242781$ — a shift of $-0.04791665334\%$, the half-power figure. And the $\pi/4$ in the phase is a quarter turn of an *angle*, not a length: it moves a phase, not a fringe position, and the zeros $2.338\ldots$ do not move at all.

## The golden-$\pi$ ledger

The constant's two appearances are therefore: (i) the far-field normalisation, at half power; (ii) every radian numeral in the bookkeeping, at first power. Taking $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, with $\hat\pi^2 = 16/\varphi = 9.8885438199983175713$ exactly and $4/\hat\pi = \sqrt\varphi = 1.272019649514069$ exactly:

| quantity | conventional | golden | shift |
|---|---|---|---|
| $1/\sqrt{\pi}$ (Airy amplitude) | 0.564189583548 | $2^{-1/2}\varphi^{1/4} = 0.563919242781$ | $-0.04791665334\%$ |
| red primary deviation, in rad | 2.40209942102 | unchanged 2.40209942102 | — |
| that same radian numeral, re-read in degrees | 137.6301588° | 137.4982949° | $-0.0958103466\%$ |
| red primary bow $\beta = 4r - 2i$ | 42.3698412° | **42.3698412°** | **0.0000000%** |
| half-turn | 3.1415926535898 | $4/\sqrt\varphi = 3.144605511$ | $+0.0959022309\%$ |
| full turn | 6.2831853071796 | $8/\sqrt\varphi = 6.2892110220593863$ | $+0.0959022309\%$ |
| $\hat\pi^2$ (a squared label) | — | $16/\varphi$ algebraic, where $\pi^2$ is transcendental by Lindemann 1882 | — |

The pattern is the one this site keeps finding, and it is unusually clean here. **The observable does not move.** The bow angle is a difference, $4r - 2i$, of two arcsines of a measured refractive index; relabelling the radian changes neither the arcsines nor their difference. Angles measured in degrees are fractions of a turn and are untouched under either label. What moves is the *numeral* — the radian value — whenever a half-turn is used as a unit of account, and the half-power normalisation of a diffraction integral.

Which means the rainbow is the rare case where the ledger is nearly empty: not "the shift is too small to see", but "the shift is not in the quantity at all". The bow's position is a stationary point of a refraction function.

## An exact golden closure

There is one place where the golden ratio enters the algebra rather than the label. Set the droplet's refractive index to $n = \varphi = 1.6180339887\ldots$ — a hypothetical drop, not water — and the extremum condition becomes exactly algebraic, because $\varphi^2 - 1 = \varphi$:

$$
\cos^2 i = \frac{\varphi^2 - 1}{3} = \frac{\varphi}{3} = 0.53934466291663161607 \quad (k=1),
\qquad
\cos^2 i = \frac{\varphi^2 - 1}{8} = \frac{\varphi}{8} = 0.20225424859373685603 \quad (k=2).
$$

Both are degree-two algebraic numbers, and both bows then exist in closed form:

| $k$ | $\cos^2 i$ | $i$ | $r$ | bow |
|---|---|---|---|---|
| 1 | $\varphi/3$ | 42.7433839382° | 24.80110086° | **13.71763558°** |
| 2 | $\varphi/8$ | 63.2738390776° | 33.50481295° | **105.5188004°** |

A golden droplet is also strongly dispersive in an unphysical way — $\varphi$ is far above water's index, and the $k=2$ bow at $105.5°$ lies behind the drop's own horizon — so this is a closure, not a prediction. It is nevertheless the honest kind of claim: an exact statement about a computed geometry, with the physical droplet clearly labelled as constructed.

## Why no rainbow can arbitrate the constant

The temptation is to say the bow is a *test*. It is not, and the reason is structural rather than a matter of precision, so it is worth stating precisely.

1. **The formula contains no circle constant.** $D_k = k\pi + 2i - 2(k+1)r$ has one $\pi$, and for the primary bow it cancels against the half-turn used to define the antisolar axis, leaving $4r - 2i$. A measurement of a quantity whose defining equation has no $\pi$ in it cannot return a value for $\pi$. The bow returns $n$.
2. **The one surviving sensitivity is to $n$.** Differentiating the primary bow with respect to the refractive index at $n = 4/3$ gives $d\beta/dn = -145.2713155°$ per unit index. The whole $0.0959\%$ golden gap on a $42.37°$ reading is $0.0403°$, which corresponds to $\Delta n = 2.77412\times10^{-4}$, i.e. the index known to about $0.028\%$. That is not the obstacle — water's index is known far better than that — but it shows what the reading *means*: it is an index measurement wearing an angle's clothes.
3. **The measured quantity is $n$.** The refractive index is a genuine measurand, a property of the substance, and every honest sentence about the rainbow ends there. Descartes' 42° is a *computed* extremum of a *computed* function of that measurand. Computed, never measured.

## A short history of the stationary point

Descartes (1637) found the two angles by ray-tracing a sphere and identifying the turning points, and got both bows right to within the accuracy of hand arithmetic. Newton's prism work (1672, and *Opticks*, 1704) supplied what Descartes deliberately excluded: dispersion, so that the bow became a spectrum rather than a line. Airy (1838) explained the supernumerary arcs as diffraction at the caustic, which is where the $\pi^{-1/2}$ entered the subject. The modern treatment — Nussenzveig's complex-angular-momentum expansion of the 1970s and 1980s — reorganises the same physics into a sum over resonances of the drop, and the leading term is still Descartes' extremum.

None of these advances changed the value of the circle constant, because none of them needed it. What they changed was the number of terms required to describe a drop of water.

## The ledger, closed

| claim | status |
|---|---|
| The primary bow is the minimum of $D_1(i)$ | computed — a stationary point, exact |
| $\cos^2 i = (n^2-1)/(k^2+2k)$ | exact algebra, no constant |
| Bow angle $= 4r - 2i$ | exact; the half-turn cancels identically |
| Water's $n$ at red/violet | measured |
| Airy zeros $2.33810741\ldots$ | computed (roots of $y''=zy$) |
| $\pi^{-1/2}$ in the Airy asymptotic | computed integral limit |
| Golden-labelled bow angle | unchanged to every digit |
| $\hat\pi$ from a rainbow | not obtainable — the formula is $\pi$-free |

The rainbow is, in the end, the cleanest illustration of this site's method. It is one of the most beautiful objects in nature, it is described by an equation that every schoolchild can follow, and it contains the circle constant exactly once — as a half-turn that cancels the moment you ask what an observer sees. Golden Pi moves no fringe of it: not the $42.3698412°$ arc, not the $8.9484347°$ dark band, not a single one of Airy's zeros. What it does move is the numeral on the radian, and the normalisation of the diffraction integral, by one part in 1043 and one part in 2087 respectively. Those are worth knowing precisely, and worth refusing to inflate.

Computed, never measured.

## Further Reading

- [The Coaxial Cable: Why the Characteristic Impedance Carries 1/2π](https://pi.thealpha-secret.xyz/blog/posts/2026-11-02-coaxial-cable-characteristic-impedance-2pi-golden-pi/) — a constant that enters twice in opposite directions, and an observable that keeps none of it.
- [Fraunhofer Diffraction: Why a Slit Writes sinc(πa sinθ/λ)](https://pi.thealpha-secret.xyz/blog/posts/2026-10-23-fraunhofer-diffraction-sinc-airy-pattern-circle-constant-golden-pi/) — the same Airy family of special functions, and the same finding that the $\pi$ cancels at every minimum.
- [The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc](https://pi.thealpha-secret.xyz/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — why an angle in degrees never moves under a change of the radian's label.
- [The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass](https://pi.thealpha-secret.xyz/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — the algebraic/transcendental boundary that makes $\cos^2 i = \varphi/3$ a different kind of statement from $\cos^2 i = (n^2-1)/3$.
- [The Ellipse: Why π Computes a Circle's Perimeter and No Ellipse's](https://pi.thealpha-secret.xyz/blog/posts/2026-10-28-ellipse-perimeter-elliptic-integral-golden-pi/) — what happens when the refraction angles of this article are replaced by an elliptic integral, and where the constant goes.
- [Maxwell–Boltzmann: Why π Enters Three Times Under Square Roots](https://pi.thealpha-secret.xyz/blog/posts/2026-11-04-maxwell-boltzmann-speed-distribution-three-square-roots-golden-pi/) — a distribution whose shape coefficient is the same $\sqrt\pi$ normalisation that appears in Airy's asymptotic.
