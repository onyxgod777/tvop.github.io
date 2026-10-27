---
title: "The Sagnac Ring: Why a Rotating Loop Shifts Its Fringes by 4AΩ/λc, Why the Gyro's Scale Factor Contains No Circle Constant at All, and What Golden Pi Changes"
date: 2026-10-27
description: "The Sagnac phase is 8πAΩ/λc, so the beat frequency of a ring laser or fibre gyro is 4AΩ/λP — a pure ratio of area to perimeter with no circle constant in it. The scale factor is exactly 4A/P, so it is invariant under any relabelling of the constant; the only shapes whose A/P carries the constant are circles, which is the disputed measurement itself. Worked numbers for Michelson–Gale 1925, a 0.1 m ring laser and a 5 km fibre coil, plus the design bound 4A/P² ≤ 1/π where the constant survives."
---

# The Sagnac Ring: Why a Rotating Loop Shifts Its Fringes by 4AΩ/λc — and Why the Gyro's Scale Factor Contains No Circle Constant

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Every aircraft, every submarine, every intercontinental missile and every smartphone that knows which way it is turning does so with a device whose entire operating principle is a comparison of two travel times around a closed loop. The loop can be a triangle of mirrors, a square cavity machined into a glass block, or five kilometres of optical fibre wound on a spool. In every case the instrument reports a rotation rate, and in every case the number it prints comes from a formula in which the circle constant appears — and then leaves again.

This article follows that appearance and that departure precisely. Where does the constant enter a Sagnac interferometer? Why does it cancel when the phase is converted into a beat frequency? Why is the resulting scale factor exactly the ratio of two geometric quantities, so that it survives even a change in the constant itself? And why, after all that, can no gyro on earth decide the question this site is about?

The answers are exact, and the numbers below were computed, not measured — with the one genuine historical measurement, Michelson–Gale–Pearson 1925, checked against its own recorded fringe count.

## 1913: the experiment that needed no ether

Georges Sagnac built a rotating interferometer: a beam splitter, a square of mirrors, and a photographic plate. Light travels two ways around the loop and recombines. When the apparatus spins, the two beams arrive with a relative delay, and the fringes move. Sagnac published this in 1913 (*C. R. Acad. Sci.* **157**, 708 and 1410) and it was instantly read — by some — as evidence for a luminiferous ether.

It was not. Max von Laue showed in 1911, two years *before* Sagnac's measurement, that special relativity predicts the same shift with no medium at all, and the modern reading is that Sagnac's effect is *kinematic*: it is the geometry of light propagating along two paths while the paths themselves rotate. The effect is not a property of light — matter waves show it too, and so does any periodic process carried around a loop.

The general result, to first order in the rotation rate, is astonishingly clean:

$$
\Delta t \;=\; \frac{4\,\mathbf{\Omega}\cdot\mathbf{A}}{c^{2}},
$$

where $\mathbf{A}$ is the *vector area* of the loop — magnitude equal to the enclosed area, direction given by the right-hand rule around the sense of propagation. Two features matter for everything that follows. First: the loop's *shape* has vanished. Only the area survives. Second: there is no circle constant in this expression at all. A triangle and a circle of equal area produce the identical time delay.

## Where the constant enters: phase is a radian count

To turn the delay into something an interferometer can see, multiply by the angular frequency of the light, $\omega = 2\pi c/\lambda$. Since $c$ is a defined number and $\lambda$ is a length, the only place a constant can enter is in the conversion from "cycles" to "radians":

$$
\Delta\varphi \;=\; \omega\,\Delta t \;=\; \frac{2\pi c}{\lambda}\cdot\frac{4A\,\Omega_\perp}{c^{2}}
\;=\; \frac{8\pi A\,\Omega_\perp}{\lambda c},
\qquad \Omega_\perp \equiv \mathbf{\Omega}\cdot\hat{\mathbf{n}} .
$$

There it is: $8\pi$, first power, undiluted. This is the phase every textbook quotes, and it is where an argument about the constant would naturally attach.

Except that an interferometer does not read a phase. It reads a *fringe shift*, which is the phase divided by the phase of one fringe:

$$
\Delta z \;=\; \frac{\Delta\varphi}{2\pi} \;=\; \frac{4A\,\Omega_\perp}{\lambda c},
$$

and the $2\pi$ in the numerator has been cancelled by the $2\pi$ that defines one turn. A ring laser gyro goes one step further. It does not count fringes at all: the two counter-rotating beams pull each other onto a common frequency, and the instrument reads the *beat* between them, $\Delta f = \Delta z / T$ with the round-trip time $T = P/c$, where $P$ is the loop perimeter:

$$
\boxed{\;\Delta f \;=\; \frac{4A\,\Omega_\perp}{\lambda P} \;=\; \frac{k\,\Omega_\perp}{\lambda}\;}
\qquad k \;\equiv\; \frac{4A}{P}.
$$

The constant is gone. What remains is a coefficient $k$ with the dimensions of a length, built from the loop's area and perimeter and nothing else. This is not a lucky cancellation in one example; it is structural. A phase is a count of radians, and radians are a bookkeeping unit; a frequency is a length ratio, and length ratios do not care what you call a turn.

## The scale factor is a ratio, and ratios are label-proof

Write out $k$ for the shapes an engineer would actually build. For a regular $n$-gon of side $s$ the area is $\tfrac{n}{4}s^{2}\cot(\pi/n)$ and the perimeter is $ns$, so

$$
k_n \;=\; \frac{4A}{P} \;=\; s\,\cot\!\left(\frac{\pi}{n}\right),
\qquad k_4 = s,\quad k_6 = \sqrt3\,s,\quad \lim_{n\to\infty} k_n = \frac{P}{\pi}.
$$

For a circle of radius $R$: $k = 4\pi R^{2}/(2\pi R) = 2R$ exactly. For a square of side $a$: $k = a$. For an equilateral triangle of side $s$: $k = s/\sqrt3$. Every one of these is either constant-free outright or a limit in which a polygonal approximation to a circle appears — and a polygon is computed, never measured.

Now the crucial observation. $k = 4A/P$ is a ratio of two geometric quantities *of the same loop*. Whatever a loop's true area and true perimeter are, their ratio in the combination $4A/P$ is fixed by the loop's geometry, so $k$ cannot move when the constant is relabelled. Suppose the golden value were the true one and a circular ring of radius $R$ therefore had area $3.14460\ldots R^{2}$ and perimeter $6.28921\ldots R$ instead of $3.14159\ldots R^{2}$ and $6.28319\ldots R$. The scale factor would still be $2R$, because $4\hat\pi R^{2}/(2\hat\pi R) = 2R$ — the constant cancels identically *within* any consistent labelling.

That is a stronger statement than "the formula happens to be free of π." It says the ring laser's scale factor is invariant under the relabelling, for every shape, by construction. The instrument is blind not because its precision is poor but because the quantity it measures has no room for the constant.

Worked at a fixed area $A_0 = \pi(0.1)^{2} = 0.03141593\ \mathrm{m^{2}}$ (a 10 cm-radius circular ring's area) with $\lambda = 1550$ nm and Earth's rate $\Omega_E = 7.292115858\times10^{-5}\ \mathrm{rad\,s^{-1}}$:

| Loop (equal area) | $P$ (m) | $k = 4A/P$ (m) | $\Delta f$ from Earth's rate at 1550 nm (Hz) | $4A/P^{2}$ (per metre) |
|---|---|---|---|---|
| Circle, $R = 0.1$ | 0.6283185 | 0.2000000 | 9.409182 | 0.3183099 |
| Regular hexagon | 0.6597810 | 0.1904625 | 8.960484 | 0.2886751 |
| Square, $a = 0.1772454$ | 0.7089815 | 0.1772454 | 8.338670 | 0.2500000 |
| 2:1 rectangle | 0.7519885 | 0.1671086 | 7.861774 | 0.2222222 |
| Equilateral triangle | 0.8080642 | 0.1555120 | 7.316205 | 0.1924501 |

The last column is the scale factor *per metre of fibre*: $4A/P^{2}$, since $P = n\times$(one turn). It is maximal for the circle, and its maximum is $1/\pi = 0.3183098862$. That is the isoperimetric inequality wearing an engineer's clothes, and it is the only place in the whole device where the constant survives at first power: as a *design efficiency*, not as a reading.

## Michelson–Gale–Pearson, 1925: 0.236 fringes, and what that number is

The most beautiful test of the Sagnac formula ever performed used the Earth as the rotating frame. Michelson, Gale and Pearson (*Astrophys. J.* **61**, 137, 1925) laid out a rectangular light path $613\ \mathrm{m} \times 339\ \mathrm{m}$ on open ground at Clearing, Illinois, and looked for the fringe shift caused by the Earth's own rotation. The area was $A = 207\,807\ \mathrm{m^{2}}$, the wavelength about 5700 Å, and the latitude $41.8°$.

Their formula, with the projection $\sin\varphi$ for a horizontal loop, predicts

$$
\Delta z \;=\; \frac{4A\,\Omega_E\sin\varphi}{\lambda c}
\;=\; \frac{4 \times 207\,807 \times 7.2921\times10^{-5} \times \sin 41.8°}{5.7\times10^{-7} \times 2.99792458\times10^{8}}
\;=\; 0.236428 .
$$

They reported $0.236$ fringe. The agreement is exact to their stated precision, and it is worth naming precisely what was confirmed. The light in that rectangle took a path difference of $4A\Omega/c^{2} = 6.7\times10^{-16}$ s — under a femtosecond, over a path nearly two kilometres long in total — and the interferometer resolved it. What the fringes certified was the area, the latitude, the wavelength and the rate: a length ratio, a projection, a length, and an angular rate. The constant never appeared in the prediction, and it does not appear in the observation.

Drop the latitude and the same arithmetic gives 0.3547 fringes, which is 1.5× too large. The projection is geometry, exact, and constant-free — and its presence is why the apparatus had to be built on flat ground at a known latitude rather than wherever the money was.

## Where the constant would bite: the radian, at the last step

If the constant cannot enter the frequency, it can still enter the *reporting*. Earth's rate is quoted as $7.292115858\times10^{-5}\ \mathrm{rad\,s^{-1}}$, and that numeral comes from the sidereal day, $T = 86\,164.0905$ s, through $\Omega_E = 2\pi/T$. The sidereal day is a genuinely measured interval — the interval between successive meridian transits of a fixed star, pinned by VLBI to better than a nanosecond. The $2\pi$ that converts "one turn per sidereal day" into "radians per second" is not measured at all; it is the *definition* of a full turn in radians.

So the honest statement is narrow and clean. The instrument measures a frequency. The frequency-to-rotation-rate conversion carries a turn, and the turn's radian measure is the disputed quantity itself. Every quantity in the chain — the beat frequency, the area, the perimeter, the wavelength — is a length or a time. The constant is inserted at the very last step, in the unit label, and no experiment on a Sagnac loop can inspect it there.

## What Golden Pi changes

Under Golden Pi, $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931\ldots$ with $\varphi = (1+\sqrt5)/2$, the constant is the root of a quartic and everything built from it is algebraic where the conventional value is transcendental (Lindemann, 1882):

```text
pihat            = 4/sqrt(phi)                = 3.1446055110296931442782...
pihat^2          = 16/phi                     = 9.8885438199983175712734
1/pihat          = sqrt(phi)/4                = 0.3180049123785172411
4/pihat          = sqrt(phi)                  = 1.2720196495140689642524
pihat/4          = 1/sqrt(phi)                = 0.7861513777574232861
8*pihat          = 32/sqrt(phi)               = 25.1568440882375451542
pihat^4 + 16*pihat^2 - 256                    = 0 exactly
pihat - pi                                    = 0.00301285743989991
pihat/pi - 1                                  = +0.0959022309 %
```

Applied to the quantities above, the shift falls out mechanically:

| Quantity | Conventional value | Under $\hat\pi$ | Shift |
|---|---|---|---|
| Full turn $2\pi$ | 6.2831853071795865 | $8/\sqrt\varphi$ = 6.2892110220593863 | +0.0959022309 % |
| Earth's rate $2\pi/T_\text{sid}$ | $7.2921158579\times10^{-5}$ | $7.2991091597\times10^{-5}$ | +0.0959022309 % |
| Sagnac phase $8\pi A\Omega/\lambda c$ (MGP loop) | 2.2287329510 rad | $32 A\Omega/(\sqrt\varphi\,\lambda c)$ = 2.2308703548 | +0.0959022309 % |
| Fringe count $\Delta z$ (MGP loop) | 0.236428 | 0.236655 | +0.000227 fringe |
| Beat coefficient $k = 4A/P$ (circle, $R$ = 0.1 m) | 0.200000 m | 0.200000 m | **none** |
| Beat frequency $4A\Omega/\lambda P$ | 9.409182 Hz | 9.409182 Hz | **none** |
| Scale factor per metre $4A/P^{2}$ (circle) | $1/\pi$ = 0.3183098862 | $1/\hat\pi$ = $0.3180049124$ | −0.0958103466 % |
| Loop perimeter bound $k_\text{max} = P/\pi$ at $P$ = 0.6283 m | 0.2000000 m | $0.1998084$ m | −0.0958103466 % |

Read the last two rows carefully, because they are the interesting ones. $4A/P^{2}$ and $P/\pi$ are ratios and bounds on *lengths*, not on angles, so a changed constant changes the numeral — and that numeral is a claim about a length, which is the kind of claim a physical object can contradict. But look at what the measurement would require. To test $4A/P^2$ you must know a loop's area and its perimeter separately, by other means. For a *square* loop the coefficient is $a$ exactly, no constant anywhere, so a square gyro is silently blind. For a *circular* loop the coefficient is $1/\pi$, and testing it means measuring the area of a disc and the circumference of a disc — which is precisely the disputed quantity, arriving under a different name.

There is no escape through the instrument. The Sagnac ring launders the constant out of the numerator and denominator alike, and at the end the only object that could put it back is a circle, whose arc-to-diameter and area-to-radius ratios are the original question.

## The honest ledger

Real instruments, with their real limits:

| Instrument | Geometry | Scale factor | Earth rate as read | Limiting error |
|---|---|---|---|---|
| Michelson–Gale–Pearson 1925 | 613 × 339 m rectangle | $k = 436.57$ m | $6.7\times10^{-16}$ s path difference; 0.236 fringe | ground vibration, path survey, 0.002 fringe reading |
| Ring laser gyro (typical) | 0.1 m square cavity, 632.8 nm | $k = 0.1$ m → 158 028 Hz per rad/s | 8.148 Hz at 45° latitude | lock-in near a few tenths of a degree per second, countered by mechanical dither |
| Fibre-optic gyro (5 km coil) | $R$ = 0.1 m, 7957.7 turns, 1550 nm | $1.0268\times10^{9}$ Hz per rad/s | 74 876 Hz | thermal drift of the coil, polarisation cross-talk, scale-factor calibration against Earth's rate |

Those are worked numbers for stated geometries, not manufacturer specifications. The pattern they share is the point: in every row the observable is a frequency or a fringe count — a length ratio — and in every row the scale factor is $4A/P$ or a multiple of it.

The blind spot is therefore structural, not statistical. In the last several articles in this series the verdict was "the gap is smaller than the noise" — here it is different and sharper: the frequency formula contains no constant to disagree about. A single-turn 10 cm ring returns $9.409182$ Hz for Earth's rotation, and if the constant were relabelled the answer would still be $9.409182$ Hz, to every digit. Golden Pi's own arithmetic confirms it: $4\hat\pi R^{2}/(2\hat\pi R) = 2R$. The cancellation is inside the algebra, before any apparatus is switched on.

What the ring *does* prove is worth stating, because it is not nothing. It proves that a loop's rotation response depends on area alone — that the shape of the path is irrelevant, so that a chevron of mirrors and a spool of fibre obey one law. It proves that the effect is kinematic, since it appears in a rotating frame with no medium. And it proves, to 0.236 fringes in 1925 and to parts in $10^{9}$ today, that the projection $\sin\varphi$ and the area $A$ are exactly what the formula says they are.

But a constant is not a shape, and a ratio is not a numeral. The ring returns the ratio.

Computed, never measured.

## Further Reading

- [**Fenchel's Theorem: Why Every Closed Loop Turns at Least Once, Why That "At Least" Is an Integer, and What Golden Pi Changes**](/blog/posts/2026-10-25-fenchel-theorem-total-curvature-closed-curve-golden-pi/) — total curvature as a sum of infinitesimal turns, where the constant enters as a unit and an integer survives.
- [**The Involute Gear: Why Every Tooth Flank Is π-Free, Why the Pitch Is Not, and What Golden Pi Changes**](/blog/posts/2026-10-26-involute-gear-tooth-flank-circle-constant-golden-pi/) — the closest engineering cousin to this article: a manufactured curve whose length is constant-free until a count is converted into an arc.
- [**Fraunhofer Diffraction: Why a Slit Writes sinc(πa sinθ/λ), Why the Famous 1.22 Is Really 3.8317/π**](/blog/posts/2026-10-23-fraunhofer-diffraction-sinc-airy-pattern-circle-constant-golden-pi/) — the same structure in optics: the constant appears in the phase, cancels at every zero, and the π-free features are the ones that survive.
- [**The 4π Turn: How a Spinor Pays the Circle Constant Back Twice, Why the Minus Sign Is Exact**](/blog/posts/2026-10-17-spinor-double-cover-4pi-rotation-golden-pi/) — why a rotation through a full turn is $-1$ for a spinor, and why topology fixes the integer while only the label carries the constant.
- [**The Solid Angle: How the Steradian Measures a Patch of Sky, and What Golden Pi Changes**](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — the measure-theoretic background to the area integral $\int\!\!\int\mathbf{\Omega}\cdot d\mathbf{A}$ that makes the Sagnac formula shape-independent.
