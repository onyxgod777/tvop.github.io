---
title: "The Pendulum That Reads π in Seconds: Why a Bob of Length g/4 Has a Period of π, Why Every Precession Number Is a Turn Count, and What Golden Pi Changes"
date: 2026-11-14
description: "A pendulum of length g/4 = 2.4516625 m has a period of exactly π seconds, because 2π√(L/g) with √(L/g) = 1/2 is π and nothing else — which makes it the one everyday device that converts a circle's circumference into a clock reading, since a point moving at 1 m/s around a circle of radius 0.5 m closes that circle in 2π×0.5 = π seconds. This article audits the whole instrument: the equation θ″ = −(g/L)sinθ contains no circle constant, the exact period T = 4√(L/g)K(sin(θ₀/2)) puts it in the normalisation of an elliptic integral, the amplitude correction θ₀²/16 equals the entire golden gap at 7.097°, and every ratio the pendulum produces cancels it identically — T/T₀ = (2/π)K, the mode split Ω sinφ/ω, and the swing count per precession turn 1/(Ω√(L/g)), which is π-free because the sidereal day and the pendulum each carry one 2π and the two delete each other. Foucault's precession is then worked by latitude (11.3258°/h at Paris, 15.0411°/h at the pole, one sidereal day exactly, 7419.666 swings per turn at 45° for a 67 m wire), with an exact golden latitude arcsin(1/φ) = 38.1727076° where the precession period is exactly φ times the polar one. Under Golden Pi the period moves by the recurring +0.0959022% — 3.0129 ms on the L = g/4 pendulum, 15.75 ms on the Panthéon's 67 m — the seconds pendulum closes exactly as L = gφ/16 = 0.9917183135 m against 0.9936213856 m (+0.1919%, 1.9031 mm), and the Kater reversible reduction g = 4π²h/T² becomes g = 64h/(φT²), amplifying the gap to 0.1919% in a quantity absolute gravimetry knows to 1e-9. The honest boundary is that this is one of the few configurations that is not structurally blind — 0.47 mm of length is a tenth of the gap — and that published pendulum reductions, inverted with free-fall g, return the arc-to-diameter ratio 3.14159, not 3.14461; the site's claim is about construction, not measurement. Computed, never measured."
---

# The Pendulum That Reads π in Seconds

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Set a bob on a string of length

$$L^{*} = \frac{g}{4} = \frac{9.80665}{4} = 2.4516625\ \text{m}$$

and let it swing through a small arc. Its period is

$$T = 2\pi\sqrt{\frac{L^{*}}{g}} = 2\pi\sqrt{\frac{1}{4}} = \frac{2\pi}{2} = \pi = 3.141592653589793\ \text{s}.$$

That is not a coincidence of units or a rounded coincidence of numbers; $\sqrt{L^{*}/g} = 1/2$ exactly, so the period *is* the constant, in seconds, read off a stopwatch. Put the same numbers into the golden value $\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$ and the same wire swings in $3.144605511029693$ s. The difference is $3.0129$ ms on a period of 3.14 s — one part in 1043, and a photogate resolves microseconds without effort.

Why should a weight on a string know anything about a circle? Because the harmonic oscillator and the uniform circular motion are the same motion seen twice. A point travelling at $1\ \text{m/s}$ around a circle of radius $\sqrt{L/g} = 0.5$ m closes that circle in $2\pi \times 0.5 = \pi$ seconds. A pendulum of length $g/4$ takes exactly that long to go out and come back. The pendulum is, in the most literal sense available to a tabletop, a circumference-to-time transducer: it converts the length of a circular arc into ticks of a clock, using no other constant than the acceleration of free fall — which is itself measured by dropping something and timing it, $g = 2h/t^{2}$, an operation containing no circle at all.

An earlier entry on this blog treated the pendulum's gap as one no clock could resolve. That was imprecise, and the ledger below corrects it: the clock is the easy part. What is hard is the *length* and the *model*, and those are the terms this article prices.

## Why the Equation Itself Holds No Circle Constant

The equation of motion for a bob on a rigid massless rod is

$$\theta'' + \frac{g}{L}\sin\theta = 0,$$

and in the small-angle regime $\sin\theta \approx \theta$ this is $\theta'' + \omega^{2}\theta = 0$ with

$$\omega = \sqrt{g/L}\ \text{rad s}^{-1}.$$

At $L = g/4$ this is $\omega = 2.000000000$ rad s⁻¹ exactly — the natural rate is the rational number 2, and it does not move under any relabelling of the circle constant, because a radian is not in it. The constant enters only when the period is *defined* as the time to complete one turn of the reference circumferences:

```text
dynamical rate:        ω = √(g/L)                     — no constant at all
period from one turn:  T = 2π/ω = 2π√(L/g)            — one π, from the unit
choice L = g/4:        T = 2π·(1/2) = π               — the period is the constant
under Golden Pi:       T = 2π̂·(1/2) = π̂ = 3.144605511… 
```

The step from $\omega$ to $T$ is a definition of the radian, not a theorem about circles. That distinction matters here more than anywhere else on this site: the pendulum's differential equation is constant-free, and the constant appears only in the sentence "one turn equals $2\pi$ radians". A test of the constant by pendulum is therefore a test of exactly one thing — the length of the arc that closes a circle of radius $\sqrt{L/g}$ — and it is not circular reasoning, because the differential equation that produces the motion is written without the constant.

## The Exact Period: One Elliptic Integral, and the Amplitude That Swamps the Gap

The linearised period is a limit, not the truth. Kepler's equation for the pendulum — the exact statement, known to Euler and Legendre — is

$$T = 4\sqrt{\frac{L}{g}}\,K\!\left(\sin\frac{\theta_0}{2}\right), \qquad K(k) = \int_0^{\pi/2}\frac{d\phi}{\sqrt{1-k^{2}\sin^{2}\phi}},$$

so the constant sits in the normalisation $K(0) = \pi/2$ and every departure from it is a pure number. Expanding,

$$\frac{T}{T_0} = 1 + \frac{\theta_0^{2}}{16} + \frac{11\,\theta_0^{4}}{3072} + \frac{173\,\theta_0^{6}}{737280} + \cdots$$

and computed against the exact integral:

| Amplitude $\theta_0$ | $T/T_0$ (exact, via $K$) | Excess over $T_0$ | In units of the golden gap |
|---|---|---|---|
| 0.5° | 1.000004759667951 | +0.000476% | 0.005× |
| 1° | 1.000019038921006 | +0.001904% | 0.020× |
| 2° | 1.000076159671566 | +0.007616% | 0.079× |
| 5° | 1.000476172485987 | +0.047617% | 0.497× |
| **7.097°** | **1.000959022308783** | **+0.095902%** | **1.000×** |
| 10° | 1.001907188143217 | +0.190719% | 1.989× |
| 30° | 1.017408797595956 | +1.740880% | 18.15× |
| 60° | 1.073182007149364 | +7.318201% | 76.31× |
| 90° | 1.180340599016096 | +18.034060% | 188.05× |
| 120° | 1.372880500618350 | +37.288050% | 388.81× |
| 179° | 3.901065160389086 | +290.106516% | 3025× |

The row in bold is the whole argument in one line: at $\theta_0 = 7.0973624°$ the amplitude correction *equals* the entire golden gap. Swing wider than that and the finite-amplitude term is the whole signal; swing at half a degree and it is one two-hundredth of it. At $\theta_0 = 90°$ the modulus is $k = 1/\sqrt2$ and the integral takes its lemniscatic value

$$K(1/\sqrt2) = \frac{\Gamma(1/4)^{2}}{4\sqrt{\pi}} = 1.854074677301372 = \frac{\varpi}{\sqrt2},\qquad \frac{2K(1/\sqrt2)}{\pi} = 1.180340599016096,$$

where $\varpi = 2.622057554292120$ is the lemniscate constant — the same number that governs the arithmetic–geometric mean, and the reason a quarter-turn of a pendulum is the same integral as an arc of Bernoulli's curve.

## Every Ratio the Pendulum Produces Is π-Free

The pendulum's ugly correction is also its cleanest feature: because $\pi$ sits *outside* the integral as the normaliser $K(0)$, it cancels from every ratio.

$$\frac{T(\theta_0)}{T(0)} = \frac{2}{\pi}K\!\left(\sin\frac{\theta_0}{2}\right) \quad\Longrightarrow\quad \frac{T(\theta_1)}{T(\theta_2)} = \frac{K(k_1)}{K(k_2)},$$

a quotient of two elliptic integrals and nothing else. The same holds for the precession. In a frame rotating with the Earth the pendulum has two circular normal modes of opposite handedness, with frequencies

$$\omega_{\pm} = \omega \mp \Omega\sin\varphi, \qquad \Omega = \frac{2\pi}{\text{sidereal day}} = 7.2921159\times10^{-5}\ \text{rad s}^{-1},$$

so the beat — the bulb's apparent rotation — runs at $\Omega\sin\varphi$, and the mode splitting is $\Omega\sin\varphi/\omega$. Neither contains the circle constant:

```text
mode split:            Ω sinφ / ω              — π-free ratio
turns per swing:       Ω √(L/g) · sinφ         — π-free
degrees per swing:     360 · Ω √(L/g) · sinφ   — π-free
radians per swing:     2π · Ω √(L/g) · sinφ    — one π, a unit, not a fact
```

| Latitude | Precession rate | Period | Period, L = 67 m | Swings/turn, L = 67 m | Degrees/swing, L = 67 m |
|---|---|---|---|---|---|
| 0° | 0 °/h | never | — | — | — |
| 23.44° | 5.983164246 °/h | 60.16883127 h | 13189.16 | 13189.16024 | 0.0272951 |
| 38.1727° | 9.295891653 °/h | 38.72678529 h | 8489.01 | 8489.009445 | 0.0424078 |
| 45° | 10.63564164 °/h | 33.84845149 h | 7419.67 | 7419.666314 | 0.0485197 |
| 48.85° | 11.3258 °/h | 31.78593 h | 6967.56 | 6967.556389 | 0.0516680 |
| 51.477° | 11.7675034 °/h | 30.59272539 h | 6706.00 | 6706.002905 | 0.0536832 |
| 60° | 13.02594755 °/h | 27.63714491 h | 6058.13 | 6058.132177 | 0.0594243 |
| 90° | 15.04106865 °/h | 23.93446958 h | 5246.50 | 5246.496365 | 0.0686172 |

At 48.85°, the latitude of the Panthéon in Paris, the rate is 11.3258 °/h — which is the often-quoted "about eleven degrees an hour" of Foucault's 1851 demonstration, computed here rather than remembered, for a wire commonly cited at 67 m and a period of 16.4231678646 s. At the pole the period is exactly one sidereal day, 86164.0905 s, because there $\sin\varphi = 1$ and the beat is the Earth's own rotation. At the equator there is no precession at all, and no constant either.

## The Exact Cancellation: Swings per Turn

Here is the sharpest identity this instrument offers. The number of swings in one precession revolution is

$$N = \frac{T_{\text{sid}}}{T\sin\varphi} = \frac{2\pi/\Omega}{2\pi\sqrt{L/g}\,\sin\varphi} = \frac{1}{\Omega\sqrt{L/g}\,\sin\varphi}.$$

The $2\pi$ of the sidereal day and the $2\pi$ of the pendulum meet and delete each other. The most famous number of the Foucault experiment — how many times the bob crosses the sand before the pattern comes round again — therefore contains no circle constant at any power, and cannot be moved by a change in it. Only the *radian* numeral attached to one swing moves, and that is a unit, not a physical fact. For a 67 m wire: 5246.496 swings per turn at the pole, 7419.666 at 45°, 13189.160 at the Tropic of Cancer. For the $\pi$-second pendulum of length $g/4$: 27426.88184 at the pole and 38787.46827 at 45°.

## The Golden Latitude

One latitude makes the precession close exactly in the golden ratio. Since

$$\sin\varphi_{\text{lat}} = \frac{1}{\varphi} = \varphi - 1 = 0.6180339887\ldots \quad\Longrightarrow\quad \varphi_{\text{lat}} = \arcsin(1/\varphi) = 38.172707627°,$$

the precession period there is exactly $\varphi$ times the polar one, $38.72678529$ h against $23.93446958$ h, and the swing count is exactly $\varphi$ times its polar value: $27426.88184 \times \varphi = 44377.62705$ for the $g/4$ bob. No approximation is involved; $\varphi - 1 = 1/\varphi$ is an identity, so a latitude exists at which the turn-count ratio is the golden ratio itself. It is the same number as the golden angle's complement, and it is a fact about $\arcsin$, not about any pendulum.

## What Golden Pi Changes: The Period Table

Under $\hat\pi = 4/\sqrt\varphi$, with $\hat\pi^{2} = 16/\varphi$ exactly, the period of every pendulum scales by one factor:

$$T \propto \pi \quad\Longrightarrow\quad \hat{T} = T\cdot\frac{\hat\pi}{\pi} = T\,(1 + 9.5902230878\times10^{-4}),$$

$$\hat{T} = 2\hat\pi\sqrt{L/g} = \frac{8}{\sqrt\varphi}\sqrt{\frac{L}{g}}, \qquad \hat{T}^{2} = \frac{64L}{\varphi g}.$$

| $L$ (m) | $T = 2\pi\sqrt{L/g}$ (s) | $\hat{T} = 2\hat\pi\sqrt{L/g}$ (s) | Diff (ms) |
|---|---|---|---|
| 0.25 | 1.00320464629 | 1.00416674193 | 0.9621 |
| 0.50 | 1.41874561663 | 1.42010622532 | 1.3606 |
| 1.00 | 2.00640929259 | 2.00833348386 | 1.9242 |
| **2.4516625** ($g/4$) | **3.14159265359** | **3.14460551103** | **3.0129** |
| 10.00 | 6.34482328311 | 6.35090811018 | 6.0848 |
| 67.00 | 16.4231678646 | 16.438918049 | 15.7502 |

Everything that was $\pi$-free stays $\pi$-free: $\omega = \sqrt{g/L}$, every period ratio, the mode splitting, the degrees per swing, the swing count per turn, the precession period in hours. Everything the pendulum *reports* about its own shape is untouched; only the translation from a turn to a number of seconds moves, and it moves by exactly the label gap.

## The Seconds Pendulum Closes Exactly in φ

The classic "seconds pendulum" — the one whose half-period is one second, so that $T = 2$ s — has length

$$L = \frac{g}{\pi^{2}} = 0.993621385566132\ \text{m},$$

a transcendental length, since $\pi^{2}$ is transcendental by Lindemann's 1882 theorem. Under Golden Pi the same condition $2\hat\pi\sqrt{L/g} = 2$ reads

$$L = \frac{g}{\hat\pi^{2}} = \frac{g\varphi}{16} = 0.991718313485885\ \text{m},$$

and $\varphi = (1+\sqrt5)/2$ is the root of $x^{2}-x-1$: the length is algebraic, of degree two, with no transcendental number anywhere in it. The two lengths differ by

$$\Delta L = 1.903072081\ \text{mm}, \qquad \frac{\Delta L}{L} = \left(\frac{\hat\pi}{\pi}\right)^{2} - 1 = +0.1918964341\%,$$

which is the gap *squared*, because a length goes as the constant squared when the period is held fixed. This is not an idle curiosity: it is the whole history of the metre in one line. Huygens, in the *Horologium Oscillatorium* of 1673, proposed the seconds pendulum as a universal length; in 1790 Talleyrand put the same proposal to the French National Assembly, and the commission that was to settle the question chose the meridian arc instead — the dependence of the pendulum's length on local gravity being among the reasons. The arithmetic above shows precisely what was at stake: a definition of the metre that would have carried the circle constant into every length in the world, and would have carried it squared.

## The Reduction That Multiplies the Gap by Two

Kater's reversible pendulum (Philosophical Transactions, 1817) removes the need to know a body's moment of inertia: two knife edges are placed so that the pendulum's period is the same about either, and the distance $h$ between them is then exactly the length of the equivalent simple pendulum, giving

$$g = \frac{4\pi^{2}h}{T^{2}}.$$

Take $h = 1$ m and $T = 2.00640929258904$ s — the period of a one-metre simple pendulum. The conventional reduction returns exactly

$$g = \frac{4\pi^{2}\cdot 1}{2.00640929258904^{2}} = 9.80665\ \text{m s}^{-2}.$$

The golden reduction, with $4\hat\pi^{2} = 64/\varphi$,

$$\hat{g} = \frac{64\,h}{\varphi\,T^{2}} = 9.82546861166\ \text{m s}^{-2},$$

a difference of $0.1918964341\%$, the gap squared again. And $g$ is a quantity that absolute gravimetry knows to about a microgal — one part in $10^{9}$ — by dropping a corner cube in vacuum and timing it against a laser interferometer, an operation in which no circle constant appears. So this reduction, unlike almost everything else this blog has audited, has a term on the other side of the equation that is far more precise than the effect being tested.

## The Experiment This Geometry Permits

Assemble the error budget for the $L = g/4$ pendulum. Since $T = 2\pi\sqrt{L/g}$,

$$\frac{\delta T}{T} = \frac{1}{2}\left(\frac{\delta L}{L} - \frac{\delta g}{g}\right),$$

so a relative error in length of $1.918\times10^{-3}$ — or the same in $g$ — produces the whole gap.

| Quantity | Value that reproduces the gap | Value that gives 10% of the gap | State of the art |
|---|---|---|---|
| Length $L$ | 4.702 mm on 2.4516625 m | 0.470 mm | laser interferometry, µm |
| Gravity $g$ | 1881 mGal | 188 mGal | free-fall absolute gravimeter, 0.001 mGal |
| Period $T$ | 3.013 ms on 3.1416 s | 0.301 ms | photogate, µs |
| Amplitude | 7.097° | 2.24° | measured to 0.01°, and exactly correctable via $K$ |
| Air buoyancy | 0.080 × gap (77.2 ppm for steel in air) | — | computable from densities |
| Invar expansion | 0.0025 × gap per kelvin | — | tabulated to 1e-7/K |

Every entry is attainable. The constant is not hidden here at the 7.1° amplitude threshold, as it was behind turn counts and integers elsewhere on this site: the amplitude correction is *known exactly* through $K$ rather than merely bounded, so it can be removed rather than avoided. The buoyancy correction is $\tfrac12\rho_{\text{air}}/\rho_{\text{bob}}$, and the only place a circle re-enters is the displaced volume $4\pi r^{3}/3$, which under Golden Pi becomes $4\hat\pi r^{3}/3 = 0.000524101$ m³ against $0.000523599$ m³ for a 5 cm radius — a 0.096% change in a 0.008% correction, which is nothing.

Invert the relation and the experiment becomes a determination:

$$\pi = \frac{T}{2}\sqrt{\frac{g}{L}}, \qquad \hat\pi = \frac{T}{2}\sqrt{\frac{g}{L}}\ \text{under the golden trigonometry},$$

with $g$ from free fall and $L$ from metrology — neither of which contains the constant. This is the rare case where the arbitration is available in principle rather than blocked by structure.

## The Honest Boundary

Three things must be said plainly, and the first is arithmetic.

**One:** the instrument's most famous outputs are worthless for this purpose. The precession rate, the degrees per hour, the swing count per revolution, the mode splitting, the period ratios, the natural frequency — every one is $\pi$-free, and the exact cancellation $N = 1/(\Omega\sqrt{L/g}\sin\varphi)$ shows why: the sidereal day and the pendulum each supply one $2\pi$, and they divide out. A Foucault pendulum could be rebuilt with a different constant and would precess identically. It is a turn counter, and turn counters cannot see a constant.

**Two:** the period comparisons in the literature return the conventional value. Where a reversible-pendulum reduction and a free-fall determination of $g$ are compared at the same site, they agree within the classical determinations' own accuracy — a few parts in $10^{5}$ in the best nineteenth-century work, and better since — which is ten times finer than the 0.0959% gap. Inverted as above, those reductions give $3.14159$, not $3.14461$. This site does not dispute that: what a pendulum measures is the ratio of a circumference to a diameter, and every physical determination of that ratio yet published returns the conventional number. The golden value $\hat\pi = 4/\sqrt\varphi$ is a claim about construction — that a circle of radius $\varphi^{1/4}$ has area exactly 4, that the squaring closes — and no weighing of arcs can establish it. It is defended here on the ground of exact construction and algebraic closure, not on the ground of a measurement, and confusing the two would be the dishonest move.

**Three:** the local value of $g$ spans 5186 mGal between pole and equator, which is 2.76 times the entire gap. A pendulum without its own gravimetry is therefore blind by construction, no matter how good its clock. That is the sense in which the older post on this blog was right and this one is more precise: nothing about the *clock* is the obstacle, and everything about the *geodesy* is.

What remains is a clean statement of where the constant actually lives in this instrument. It lives in one place: the definition of the turn, $2\pi$ radians, which converts $\omega = \sqrt{g/L}$ into a period. Strip that away and a pendulum is an object whose equation of motion is written without a circle constant, whose exact period is an elliptic integral normalised by $K(0) = \pi/2$, whose amplitude response is a ratio of two such integrals, whose precession is a beat frequency, and whose swing count per turn cancels the constant identically. That is a great deal of the instrument, and all of it is computed.

Computed, never measured.

## Further Reading

- [The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the earlier treatment this article corrects on one point: the clock was never the obstacle.
- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — the other classical curve whose equation holds no circle constant, and where the golden abscissa $x = a\ln\varphi$ puts the slope at exactly $1/2$.
- [The Cycloid: Rolling Circles and the Isochrone](/blog/posts/2026-08-14-cycloid-rolling-circles-golden-pi/) — Huygens' cycloidal cheeks, the one pendulum whose period is amplitude-independent without any $K$ correction.
- [The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass Forever](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — why $g/\pi^{2}$ is transcendental and $g\varphi/16$ is not, in full.
- [The Fine-Structure Constant: Why 4π Cancels](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — the one place on this site where a genuinely measured constant is in play.
