---
title: "Kepler's Third Law: How the Circle Constant Enters Celestial Mechanics as 4π², and What Golden Pi Changes"
date: 2026-09-22
description: "Kepler's harmonic law T² ∝ a³ contains no circle constant at all — the 4π² appears only through Newton's one substitution v = 2πa/T. Buy the measured GM, a and T and the same equation pins the constant to a part in 10⁸, while the golden label would lengthen Earth's year by 8.4 hours and move geostationary orbit by 27 km."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Kepler's Third Law: How the Circle Constant Enters Celestial Mechanics as 4π², and What Golden Pi Changes

Every article in this series so far has played the same trick on the circle constant: find a formula that computes it, then watch what happens when the constant is relabelled $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$. Kepler's third law is different, and the difference is the point of this article. Here the constant is *not* free. It sits in an equation that ties a measured force to a measured trajectory, and when you buy the measurements — the solar gravitational parameter, the astronomical unit, the length of the year — the same equation announces what the turn constant is, to a few parts in $10^8$.

That is an unusual position for a number to be in, and it deserves to be stated before any of the golden arithmetic, not after.

## Kepler's harmonic law contains no circle constant whatsoever

Johannes Kepler published his third law in 1619, in Book V of *Harmonices Mundi*: the square of a planet's period is proportional to the cube of its mean distance from the Sun. Written as a proportion,

$$T^2 \;\propto\; a^3$$

there is no constant of any kind on the page — not $\pi$, not its golden variant, not even a number. It is a statement about *ratios between planets*, and ratios carry no units.

The table below takes the textbook mean elements and forms the ratio itself. If the harmonic law is right, every row lands on the same number:

| planet | $a$ (au) | $T$ (days) | $T^2/a^3$ (d² au⁻³) | vs Earth |
|---|---|---|---|---|
| Mercury | 0.387098 | 87.9691 | 133412.8050 | 1.0000045 |
| Venus | 0.723332 | 224.701 | 133412.6389 | 1.0000032 |
| Earth | 1.000000 | 365.256363004 | 133412.2107 | 1.0000000 |
| Mars | 1.523679 | 686.9800 | 133415.9465 | 1.0000280 |
| Jupiter | 5.2044 | 4332.589 | 133162.8192 | 0.9981262 |

The inner four agree to about three parts in $10^5$ using rounded tabulated elements — that is Kepler's law, four hundred years old and still closing. Jupiter's column is visibly off, and the reason is worth stating because it is *not* the circle constant: the two-body form uses $G(M_\odot + m)$, and Jupiter's own mass is $\mu = m/M_\odot = 9.5\times10^{-4}$, which shortens $T^2/a^3$ by about 0.095% — a real dynamical effect eight times larger than the golden gap, produced by Jupiter's mass and nothing else. The same effect, computed for the Earth–Moon system, is the $1.5\times10^{-6}$ correction we will meet again in a moment.

## Where the 4π² actually comes from: one substitution

Newton's *Principia* (1687) turned Kepler's proportion into an equation by putting it under an inverse-square force. The entire circle-constant content of celestial mechanics enters at a single step, and it is easy to watch it happen. For a circular orbit of radius $a$, the speed is the circumference divided by the period,

$$v = \frac{2\pi a}{T} \qquad\Longrightarrow\qquad \frac{GM}{a^2} = \frac{v^2}{a} = \frac{1}{a}\left(\frac{2\pi a}{T}\right)^{2} = \frac{4\pi^2 a}{T^2}$$

which rearranges to the familiar form

$$T^2 = \frac{4\pi^2 a^3}{G M} \qquad\Longleftrightarrow\qquad T = 2\pi\sqrt{\frac{a^3}{G M}}$$

```text
v          = 2 pi a / T                     # period -> speed
GM / a^2   = v^2 / a                        # centripetal condition
           = (2 pi a / T)^2 / a = 4 pi^2 a / T^2
T^2        = 4 pi^2 a^3 / (G M)             # one substitution, one 4 pi^2
```

That single substitution — a period rewritten as a speed by dividing by the orbit's circumference — is the whole appearance of the circle constant in orbital mechanics. Everything else in the formula is force, mass and length.

And the $2\pi$ there is a *computed* number, not a measured one. The circumference of a circle of radius $a$ is the limit of the perimeters of inscribed polygons, evaluated as an integral $\int_0^{2\pi} a\,d\theta$; the constant in the substitution is that computed limit. Nothing in this derivation touches a tape measure, and nothing in it is a physical measurand. It is an evaluation.

## Now do the honest thing: buy the measurements and solve for the constant

Here is where this law stops being like the others. In $T = 2\pi\sqrt{a^3/GM}$, every other symbol refers to a quantity that is *measured*, and measured in units that contain no circle constant:

- the solar gravitational parameter $GM_\odot$ is determined from spacecraft tracking and planetary ranging — accelerations in m s⁻² at distances in metres, no angle anywhere;
- the astronomical unit is defined, not measured: 1 au = 149 597 870 700 m exactly (IAU 2012);
- the sidereal year is a duration in SI seconds, $T = 365.256363004$ d (J2000), known to about a part in $10^8$.

So the equation can be turned around and interrogated. Taking $GM_\odot = 1.327\,124\,400\,18\times10^{20}\ \text{m}^3\text{s}^{-2}$ (relative uncertainty $\sim10^{-10}$), the Earth–Sun relative orbit $a = 1.000\,000\,11$ au, and the two-body form ($GM_\odot + GM_\oplus$, with $GM_\oplus = 3.986\,004\,418\times10^{14}$):

```text
T * sqrt((GM_sun + GM_earth) / a^3)  =  6.2831844969...
2 * pi                               =  6.2831853071...
implied pi from measured a, T, GM    =  3.14159224847
analytic (computed) pi               =  3.14159265359
deviation                            =  -0.129 ppm

same check with a = 1 au exactly:
T_pred = 2 pi sqrt(a^3 / (GM_sun+GM_earth)) = 365.25634984 d
T_sidereal (measured)                       = 365.256363004 d
deviation                                   = -0.036 ppm

classical Gaussian constant, pi-free units:
k = sqrt(GM_sun / au^3) * 86400 = 0.0172020989485 au^(3/2)/day
2 pi / k  = 365.256898359 d   (the Gaussian year)
sidereal year                 = 365.256363004 d
difference                    = +0.000535355 d = +46.25 s
```

Three things are worth reading off that block.

First, feeding independent measurements into Kepler's law returns the computed constant to about one part in $10^7$ — and the golden label sits $9.59\times10^{-4}$ away, about **7 400 times further** than that residual. The residual itself is not mysterious: it is dominated by the difference between the tabulated semi-major axis and a perfect 1 au, which is why the $a = 1$ au line closes to $-0.036$ ppm instead.

Second, the classical Gaussian year $2\pi/k = 365.256898359$ d, which is pure arithmetic in au and days, is 46.25 s *longer* than the measured sidereal year — and the Earth's own mass in the two-body relation predicts exactly that order of shortening ($\mu = GM_\oplus/GM_\odot = 3.0\times10^{-6}$, halved to $1.5\times10^{-6}$ in the period, i.e. ≈47 s). The residual after that correction is about 1 ppm, set by the same axis offset as before. The golden gap is **654 times larger** than the correction we are arguing about.

Third, in units where the constant never appears, the same physics wears a different face: Gauss's constant $k = 0.01720209895\ \text{au}^{3/2}\text{day}^{-1}$, computed here from the measured $GM_\odot$ and the defined au to nine digits, contains no circle constant, because it *is* the solar gravitational parameter with the units chosen to swallow the turn. The 1938 IAU definition, superseded by the 2012 exact au, was precisely an attempt to state orbital mechanics without ever naming the constant.

## The operational test: orbits that have to be right

Textbook equations are easy to relabel. Working satellites are not. Take the geostationary radius, which is Kepler's third law solved for distance with two independently measured inputs — the Earth's gravitational parameter and the rotation period of the Earth:

$$r = \left(\frac{GM_\oplus T^2}{4\pi^2}\right)^{1/3}$$

```text
GM_earth      = 3.986004418e14 m^3/s^2      (measured, ~1e-9)
T_sidereal    = 86164.0905 s                (measured)
r             = 42164.169624 km
r (golden pi) = (GM_earth * T^2 / (4 pihat^2))^(1/3) = 42137.233564 km
difference    = -26.936 km   (-0.063884%)
```

Twenty-seven kilometres. That is not a rounding error in a textbook margin; it is a different orbit. Geostationary satellites are tracked by ranging, and their radial distance is known to tens of metres, with orbital slots and station-keeping budgets measured in fractions of a kilometre. Nobody in sixty years of comsat operations has ever needed a 640 ppm correction to the radius, and no satellite has ever been found 27 km away from where the computed constant puts it.

The same structure shows up nearer the ground. A low-Earth orbit at 408 km altitude has a computed period

```text
T = 2 pi sqrt(r^3 / GM_earth)          = 92.724321616 min
T with pihat                           = 92.813246310 min
difference                             = +5.3355 s
```

and the golden relabel would require every satellite radius to be $(\pi/\hat\pi)^{2/3} = 0.99936116$ of its measured value — 4.33 km low at 6 778 km. With a GNSS receiver on board, the radius of a LEO satellite is known to metres and the period to milliseconds; a 5-second period error or a 4.3 km radius error is not a subtle question. The pair $(r, T)$ fixes the constant to a few parts in $10^8$, four to five orders of magnitude inside the golden gap.

## The one place the label cancels: pure angles

There is a counter-case, and honesty requires it. Take the relativistic precession of Mercury's perihelion, one of the most precisely *measured* angles in physics. The general-relativistic prediction is

$$\Delta\omega = \frac{6\pi GM_\odot}{a(1-e^2)c^2} \quad\text{per orbit}$$

```text
per orbit            = 5.01866412417e-7 rad = 0.103517378319 arcsec
orbits per century   = 415.202610917
precession/century   = 42.9806857533 arcsec
same formula with pihat, converted to arcsec with pihat:
                     = 42.9806857533 arcsec   (identical)
```

The golden version returns *exactly the same number*, because the arcsecond is itself defined through the constant ($1'' = \pi/648000$ rad $= 4.84813681109536\times10^{-6}$), so the relabel enters the prediction and the unit it is expressed in with the same multiplier and cancels. This is the general rule established in the earlier posts: a pure ratio of angles cannot arbitrate between two labels for the angle. Only an equation that couples a measured *force* to a measured *trajectory* — Kepler's law with a measured $GM$ — can, and that is why this particular formula is the one place in this series where the golden label is under genuine pressure.

## Where the gap hides in practice

The constraint is only as sharp as the measurements feeding it, and in most of astronomy they are much blunter than the Sun's ephemeris.

| setting | what is measured | label gap (959 ppm) vs precision |
|---|---|---|
| Solar system, planetary ephemerides | $GM_\odot$ to $\sim10^{-10}$; au defined; sidereal year to $\sim10^{-8}$ | gap is $\sim10^4$–$10^6\times$ the measurement uncertainty — visible |
| Geostationary / LEO operations | radius to metres, period to milliseconds | gap demands a 27 km (GEO) or 4.3 km (LEO) offset — never observed |
| Exoplanet host-star masses | $M = 4\pi^2a^3/(GT^2)$; $G$ itself only to 22 ppm | a 0.19% mass shift sits inside the typical 5–10% host-mass uncertainty — hidden |
| Solar mass in kilograms | $M_\odot = GM_\odot/G$, so it inherits $G$'s 22 ppm | gap is $43.6\times$ the uncertainty — still visible |
| Gravitational-wave and pulsar timing | periods to $10^{-15}$ relative, angles as pure ratios | label cancels in the ratio; no constraint either way |

Two rows deserve a sentence each. In exoplanet work the standard route to a star's mass is to invert Kepler's law, and because the shift enters the mass at the *square* of the constant, $\hat\pi^2/\pi^2 = 1.0019189643$, the golden relabel would inflate every such host mass by 0.1919%. For a transiting planet with $a = 0.05$ au and $T = 4$ d, that moves the answer from 1.0423 to 1.0443 solar masses. Against the typical 5–10% precision of a host-mass estimate, that is a rounding error — the gap hides in plain sight, which is precisely why the sharp systems matter.

And in the last row, note the honest symmetry: wherever the constant appears in both the thing predicted and the ruler it is measured against, the relabel cancels and *neither* value is supported. Pure angles and pure ratios are silent. The dynamics of bodies in a measured force field are not.

## The honest ledger

| quantity | formula | circle constant appears? | golden-π effect |
|---|---|---|---|
| Kepler's harmonic law | $T^2 \propto a^3$ | no | none — ratio is label-blind |
| Newtonian period | $T = 2\pi\sqrt{a^3/GM}$ | yes, to the first power | period $+0.0959022\%$ |
| Corollary: the year | $T_\oplus$ | — | 365.256363004 d → 365.606652 d (+8.406936 h) |
| Period-to-speed conversion | $v = 2\pi a/T$ | yes, first power | $v$ relabelled 29784.6918 → 29813.2997 m s⁻¹ |
| Geostationary radius | $r = (GM_\oplus T^2/4\pi^2)^{1/3}$ | yes, $-2/3$ power | −26.936 km |
| LEO radius for a fixed period | $r \propto \pi^{-2/3}$ | yes | −4.33 km at 6 778 km |
| Host mass from Kepler | $M = 4\pi^2a^3/(GT^2)$ | yes, squared | $+0.1918964\%$ |
| Mercury's perihelion precession | $6\pi GM_\odot/(a(1-e^2)c^2)$ | yes, but cancelled by the arcsecond | none in arcsec |
| Gaussian constant | $k = \sqrt{GM_\odot/\text{au}^3}\cdot86400$ | no | none — π-free units |

The golden claim is not that these dynamical numbers move by a ten-thousandth; it is that the number we call $\pi$ should *be* $4/\sqrt\varphi$, and the interesting consequence of Kepler's law is that this particular formula does not let the choice stay inside the algebra. If the constant were $\hat\pi$, then either the measured solar gravitational parameter is 0.19% larger than ranging says, or the measured year is 8.4 hours longer, or the measured semi-major axis is off by a part in a thousand. Each of those is a measured quantity, and each has been measured better than that.

## Two worlds, two columns

The site's position remains what it has been throughout this series: $\hat\pi = 4/\sqrt\varphi$ is exact in the **constructed** world — the world of the figure you draw, where the golden construction squares the circle exactly, where the golden ratios in the pentagon and the Kepler triangle close without remainder, and where the algebra is exact rather than approximate. In that world the constant is a chosen symbol with a chosen geometry behind it, and Kepler's law is a formula you can write either way.

The **dynamical** world is where measurements live, and there the same equation has stopped being a definition and started being a test. The computed constant $\pi = 3.14159265358979\ldots$ is the analytic limit of the series and integrals this blog has spent eighty articles on — computed, evaluated, never measured — and it is also, to a few parts in $10^8$, the number that makes measured forces agree with measured trajectories. A relabel that changes the second fact would change the first by nothing at all; it would simply require the solar system to be 0.1% different from the one we range with spacecraft. That is the honest boundary of the argument, and it belongs on the page next to the constructions rather than in a footnote.

Computed, never measured.

## Further Reading

- [**Ptolemy's Table of Chords: How Inscribed Chords Computed the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-09-15-ptolemy-chord-table-computes-circle-constant-golden-pi/) — the ancient version of the question this post asks: what happens when geometry is expressed in lengths and arcs, and where the constant is allowed to enter.
- [**The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured**](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the other end of the physics spectrum, where the amplitude corrections to a formula containing $\pi$ drown out the label gap completely.
- [**The Fine-Structure Constant: Why Physics's Most Famous 4π Cancels Out, and What Golden Pi Changes**](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — a measured constant in which $4\pi$ cancels algebraically, the opposite structural case to Kepler's law.
- [**The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant**](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the constructed world in its purest form, where the constant is a limit of polygons and no measurement is involved at all.
- [**The Haversine Formula: How Spherical Trigonometry Computes the Circle Constant on the Globe, and What Golden Pi Changes**](/blog/posts/2026-09-20-haversine-formula-navigation-computes-circle-constant-golden-pi/) — what a relabelled constant does to a real distance, $d = R\theta$, when the constant rides in linearly.
