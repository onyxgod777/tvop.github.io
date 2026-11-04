---
title: "The Maxwell–Boltzmann Speed Distribution: Why π Enters Three Times, Each Under a Square Root — One Per Cartesian Axis — Why Every Bulk Thermodynamic Quantity Cancels It, and What Golden Pi Changes"
date: 2026-11-04
description: "Maxwell's 1860 speed distribution f(v) = 4π(m/2πkT)^{3/2}v²e^{−mv²/2kT} contains the circle constant three times at half power, once per Cartesian axis of the Gaussian error factor, and this article shows the whole shape collapses to the single coefficient 4/√π once speeds are counted in units of the most probable speed — the mass and the temperature cancelling exactly — with the plane's polar measure (a full turn) the only place a circle enters at all. Worked at 300 K: hydrogen v_p = 1573.1147 m/s, helium 1116.4043, nitrogen 421.99743, xenon 194.92697, with v_rms/v_p = √(3/2) = 1.2247448714 exactly π-free, mean kinetic energy 3kT/2 π-free, sound speed 353.068381 m/s π-free, Graham effusion ratios 3.727782569 π-free — while 2/√π survives in v_mean, 1/π in the mean free path (6.9441691×10⁻⁸ m), √π in the peak height 4/(√πe) = 0.8302149948, and the transcendental median speed 1.08765203176·v_p that is neither exact nor π-free. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693144…, root of y⁴+16y²−256=0) the shape coefficient becomes the algebraic 4/√π̂ = 2φ^{1/4} = 2.255676971… (root of y⁸−4y⁴−16=0), the mean speed closes exactly as v_mean = √(2kT/m)·φ^{1/4} so that v_mean/v_p = φ^{1/4} = 1.1278384856 with no residue, the third-power normalisation moves +0.2879827%, the half-power quantities −0.0479166533%, the three-halves power −0.1436811%, and the cumulative fractions do not follow any power law at all (−0.035% in the body, −0.0475% in the tail) — a trap for anyone quoting a single percentage. The honest boundary: every quantity thermometry and calorimetry actually read is π-free, and the surviving powers sit in a speed scale that no beam experiment resolves to the 1-part-in-1043 gap. Computed, never measured."
---

# The Maxwell–Boltzmann Speed Distribution

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1860 James Clerk Maxwell asked what a box of gas would look like if he stopped tracking molecules and asked only how many were moving at each speed. His answer — the first statistical law of physics, published in *Illustrations of the Dynamical Theory of Gases* — is a curve that every physics student meets and almost nobody interrogates:

$$
f(v)\,\mathrm{d}v \;=\; 4\pi\left(\frac{m}{2\pi k T}\right)^{3/2} v^{2}\,e^{-mv^{2}/2kT}\,\mathrm{d}v
$$

Read it quickly and there seem to be circles everywhere: a leading $4\pi$, and a $2\pi$ buried inside a three-halves power. Read it carefully and something much more specific is true. The constant appears **three times, each time under a square root, one occurrence per Cartesian axis**, and nowhere else. This article takes that structure apart, works the numbers for real gases at 300 K, and then asks the only question this site ever asks: what changes if the constant is $\hat\pi = 4/\sqrt\varphi$ rather than $\pi = 3.14159265358979\ldots$?

The short answer is that the *shape* changes not at all, four or five specific numerals move by small and differing amounts, and the one quantity that closes into pure algebra is the ratio of the mean speed to the most probable speed, which becomes $\varphi^{1/4}$ exactly.

## The shape, in units that remove the gas

The single most clarifying step is to measure speeds in units of the most probable speed. Setting the derivative of $v^{2}e^{-mv^{2}/2kT}$ to zero gives the mode

$$
v_p \;=\; \sqrt{\frac{2kT}{m}},
$$

a formula with no circle constant in it — a mode is a maximum, and maxima are found by differentiation, an operation blind to labels. Then write $v = x\,v_p$ and substitute. The mass and the temperature cancel **exactly**, all three powers of them, leaving

$$
f(v)\,\mathrm{d}v \;=\; \frac{4}{\sqrt{\pi}}\,x^{2}e^{-x^{2}}\,\mathrm{d}x,
\qquad x = \frac{v}{v_p}.
$$

Every gas in the universe has the identical curve in these units. Hydrogen at 300 K and xenon at 3000 K lie on top of each other. What remains of the constant is precisely one $\sqrt{\pi}$ in the front coefficient — a half power, and nothing else. The leading $4\pi$ did not vanish, it *cancelled*: $4\pi \cdot (2\pi)^{-3/2}\cdot 1 = 4/\sqrt{\pi}$, and the leftover half power is what the three-halves power leaves over when it meets the $4\pi$ and the $v_p^{3}$.

Check the normalisation numerically, as a computation:

```text
∫₀^∞ (4/√π) x² e^{−x²} dx
  = (4/√π) · Γ(3/2)/2
  = (4/√π) · (√π/2)/2
  = 1

numeric quadrature, 200-point Gauss–Legendre on [0,8]:
  0.9999999999999999999999999998
```

The integral returns one because $\Gamma(3/2) = \sqrt\pi/2$, and that is a *computed* identity, not a measured one: it is the statement that the Gaussian's area in one dimension is $\sqrt\pi$.

## Why the constant is under the root, three times

Where does that $\sqrt\pi$ come from? Not from any round object. It comes from the fact that the energy in the exponent is a sum of three squares, one per axis:

$$
e^{-mv^{2}/2kT} \;=\; e^{-mv_x^{2}/2kT}\cdot e^{-mv_y^{2}/2kT}\cdot e^{-mv_z^{2}/2kT}.
$$

Each factor is a one-dimensional Gaussian, and each normalises to $1/\sqrt{2\pi\sigma^{2}}$. Three axes therefore contribute $\pi$ at half power three times, total $\pi^{3/2}$ — which is exactly the $(2\pi)^{-3/2}$ in the prefactor, since $(2)^{3/2}$ from $2kT/m$ is what pushes the $4\pi$ over to $4/\sqrt{\pi}$.

And the one-dimensional Gaussian's $\sqrt\pi$ itself comes from a full turn. Squaring the integral and going polar:

$$
I^{2} = \iint_{\mathbb{R}^{2}} e^{-(x^{2}+y^{2})}\,\mathrm{d}x\,\mathrm{d}y
= \int_{0}^{2\pi}\!\!\mathrm{d}\theta \int_{0}^{\infty} r\,e^{-r^{2}}\,\mathrm{d}r
= 2\pi\cdot\tfrac12 = \pi .
$$

That $2\pi$ is not the circumference of anything. It is the total measure of the angular coordinate on the plane — a **definition** of the full turn, fixed by how the polar chart is set up, and computed by integration that never draws a circle. This is the honest location of the circle constant in statistical mechanics: not in the molecules, which are not circles, and not in the box, which may be any shape, but in the *measure of the plane* used to count states.

## The four speeds, and which of them hold the constant

| Quantity | Formula | π content | Nitrogen, 300 K |
|---|---|---|---|
| Most probable $v_p$ | $\sqrt{2kT/m}$ | none | 421.99743 m/s |
| RMS $v_\mathrm{rms}$ | $\sqrt{3kT/m}$ | none | 516.839189 m/s |
| Mean $\bar v$ | $\sqrt{8kT/\pi m}$ | $\pi^{-1/2}$ | 476.173109 m/s |
| Median $v_{1/2}$ | $x_{1/2}\sqrt{2kT/m}$, $x_{1/2}$ transcendental | $\pi^{-1/2}$, implicitly | 458.9863621 m/s |

with molar masses $M(\mathrm{H_2}) = 2.01588$, $M(\mathrm{He}) = 4.002602$, $M(\mathrm{N_2}) = 28.0134$, $M(\mathrm{Xe}) = 131.293$ g/mol, $k = 1.380649\times10^{-23}$ J/K and $m = M/N_A$:

| Gas | $v_p$ (m/s) | $\bar v$ (m/s) | $v_\mathrm{rms}$ (m/s) | $\bar v$ golden (m/s) |
|---|---|---|---|---|
| H₂ | 1573.1147 | 1775.06982 | 1926.66412 | 1774.21926 |
| He | 1116.4043 | 1259.72739 | 1367.31048 | 1259.12377 |
| N₂ | 421.99743 | 476.173109 | 516.839189 | 475.944943 |
| Xe | 194.92697 | 219.951532 | 238.735807 | 219.846139 |

Two of the four speeds are entirely π-free, and their ratio is exact arithmetic:

$$
\frac{v_\mathrm{rms}}{v_p} \;=\; \sqrt{\tfrac{3}{2}} \;=\; 1.2247448713915890\ldots
$$

No constant, no gas, no temperature. The mean-to-most-probable ratio, by contrast, is where the constant sits at half power and where nothing cancels:

$$
\frac{\bar v}{v_p} \;=\; \sqrt{\frac{4}{\pi}} \;=\; \frac{2}{\sqrt\pi} \;=\; 1.1283791670955126\ldots
$$

and the mean-to-rms ratio, $\sqrt{8/(3\pi)} = 0.9213177319235613\ldots$, likewise. The median is the odd one out: it is defined by a transcendental equation,

$$
\operatorname{erfc}(x_{1/2}) - \frac{2x_{1/2}e^{-x_{1/2}^{2}}}{\sqrt\pi} = \frac12,
\qquad x_{1/2} = 1.08765203176\ldots,
$$

so it is neither exact nor free of the constant — it is *implicitly* a function of it, which is worth remembering when someone quotes "median speed" as a clean number. The peak height of the shape is $4/(\sqrt\pi\,e) = 0.8302149948\ldots$ in units of $v_p$, another half power.

## Where the constant survives at first power

Three standard results carry $\pi$ not under a root but plainly:

1. **Effusion flux** through a small hole, $\Phi = n\bar v/4 = n\sqrt{kT/2\pi m}$. For nitrogen at 300 K and $n = 2.4463133\times10^{25}$ m⁻³ this is a velocity scale of $119.043277$ m/s; for hydrogen, $443.767454$ m/s.
2. **Mean free path**, $\lambda = 1/(\sqrt2\,\pi d^{2}n)$. With $d = 3.64\times10^{-10}$ m and the same density, $\lambda = 6.9441691\times10^{-8}$ m.
3. **Bimolecular collision prefactor**, $\sqrt{8kT/\pi\mu}$, which for N₂–N₂ at 300 K ($\mu = m/2$) is $673.410469$ m/s — the $\pi$ in the Arrhenius prefactor, sitting entirely outside the exponential.

## What is π-free — and therefore what no thermometer can see

This is the part that matters for any claim about the constant's value, and it is a long list:

- mean kinetic energy $\tfrac32 kT = 6.2129205\times10^{-21}$ J, and hence every heat capacity;
- the rms-to-mode ratio $\sqrt{3/2}$;
- the speed of sound, $c_s = \sqrt{\gamma kT/m} = 353.068381$ m/s for N₂ at 300 K with $\gamma = 1.4$ — no circle constant anywhere;
- Graham's law ratios, $\sqrt{M_2/M_1}$: hydrogen effuses $3.727782569$ times faster than nitrogen, exact arithmetic;
- pressure $p = nkT$, and every equation of state;
- the position of the distribution's peak and its entire width in units of $v_p$.

Everything a pressure gauge, a calorimeter, a sound-speed measurement or a diffusion experiment returns is on that list. The circle constant in Maxwell–Boltzmann is confined to a *speed scale*: to convert a dimensionless $x$ into metres per second you need $\bar v$ or $\Phi$, and those carry $\pi$; but nothing you can weigh, heat or listen to carries it at all.

## Under Golden Pi

Take $\hat\pi = 4/\sqrt\varphi = 3.144605511029693144\ldots$, the positive root of $y^{4}+16y^{2}-256 = 0$, with $\hat\pi^{2} = 16/\varphi$ exactly and $\hat\pi\cdot4\sqrt\varphi = 16$ exactly. Three reciprocal identities do all the work here:

$$
\frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4},\qquad
\frac{2}{\hat\pi} = \frac{\sqrt\varphi}{2},\qquad
\sqrt{\hat\pi} = \frac{2}{\varphi^{1/4}} .
$$

The last is the one this article needs. Because $\sqrt{\hat\pi} = 2/\varphi^{1/4}$, every half-power occurrence becomes a rational multiple of $\varphi^{1/4} = 1.12783848556168226026\ldots$, and the shape coefficient closes:

$$
\frac{4}{\sqrt{\hat\pi}} \;=\; 2\varphi^{1/4} \;=\; 2.2556769711233645\ldots
$$

which is algebraic of degree eight — it satisfies $y^{8}-16y^{4}-256 = 0$, since $y^{4} = 16\varphi$ and $\varphi^{2} = \varphi+1$ give $y^{8} = 256(\varphi+1) = 16y^{4}+256$ — where $4/\sqrt\pi = 2.2567583341910251\ldots$ is transcendental by Lindemann's 1882 theorem. The most striking closure is the mean speed:

$$
\bar v = \sqrt{\frac{8kT}{\hat\pi m}} = \sqrt{\frac{2kT\sqrt\varphi}{m}} = \sqrt{\frac{2kT}{m}}\;\varphi^{1/4},
\qquad
\frac{\bar v}{v_p} = \varphi^{1/4} \text{ exactly.}
$$

Under Golden Pi the ratio of the mean speed to the most probable speed is not a transcendental numeral at all: it is the fourth root of the golden ratio, with no residue at any precision. That is the clean algebraic closure this distribution offers, and it is worth stating plainly what it is and is not — it is an exact identity *within* the golden labelling, and it is not evidence for that labelling, because the same derivation under any constant produces the same kind of statement.

The shifts, computed:

| Occurrence | Power of π | Conventional | Golden | Shift |
|---|---|---|---|---|
| Normalisation $A=(m/2\pi kT)^{3/2}$, N₂ 300 K | $3/2$ | $2.38971313899\times10^{-9}$ | $2.38627957309\times10^{-9}$ | $-0.1436811\%$ |
| Mean speed $\bar v$ | $1/2$ | 476.173109 m/s | 475.944943 m/s | $-0.0479166533\%$ |
| Peak height $4/(\sqrt\pi e)$ | $1/2$ | 0.830214994841 | 0.8298171836 | $-0.0479166533\%$ |
| Effusion $\Phi/n$ | $1/2$ | 119.043277 m/s | 118.986236 m/s | $-0.0479166533\%$ |
| $\langle 1/v\rangle$ | $1/2$ | $2.67390056\times10^{-3}$ | $2.67261932\times10^{-3}$ | $-0.0479166533\%$ |
| Mean free path | $1$ | $6.9441691\times10^{-8}$ m | $6.9375159\times10^{-8}$ m | $-0.09581035\%$ |
| $v_\mathrm{rms}/v_p$ | none | 1.2247448714 | 1.2247448714 | $0$ |
| Sound speed, N₂ 300 K | none | 353.068381 m/s | 353.068381 m/s | $0$ |

Two arithmetic traps are worth naming, because both appear in careless writing.

**First, the powers do not scale linearly.** The gap at first power is $+0.0959022309\%$ ($\hat\pi/\pi - 1$). A half power is not half of that: it is $\sqrt{1.0009590223}-1 = 0.0479396\%$ if you raise $\hat\pi$, but $1-\sqrt{\pi/\hat\pi} = -0.0479167\%$ if you lower $\pi$ — different numbers in the fifth digit, because the two are reciprocals and the percentage is not symmetric. Three halves compounds to $-0.1436811\%$ one way and $+0.1438878\%$ the other. Anyone quoting "half the gap" is already wrong in the fourth significant figure.

**Second, the cumulative fractions follow no power law at all.** The fraction of molecules above $x$ most probable speeds is

$$
F(x) = \operatorname{erfc}(x) + \frac{2x\,e^{-x^{2}}}{\sqrt\pi},
$$

and replacing $\sqrt\pi$ by $2/\varphi^{1/4}$ shifts it by an amount that depends on $x$, because the shift is a weighted mixture of a constant term and a term linear in the constant:

| $x$ | Conventional $F(x)$ | Golden $F(x)$ | Ratio |
|---|---|---|---|
| 1 | 0.5724067045 | 0.5722077989 | 0.99965251 |
| 2 | 0.04601170569 | 0.04599189983 | 0.99956955 |
| 3 | 0.0004398496528 | 0.0004396494766 | 0.99954490 |
| 7.12 | $7.813735\times10^{-22}$ | $7.810027\times10^{-22}$ | 0.99952547 |

So the body of the distribution moves by $-0.035\%$ and the deep tail by $-0.0475\%$, converging to the pure half-power value only as $x\to\infty$, where the $\operatorname{erfc}$ term dies. A single headline percentage cannot describe this function; the honest statement is the table. (The vanishingly small tail values are why hydrogen does not evaporate from Earth: at 300 K, $x_\mathrm{esc} = 11\,200/1573.1147 = 7.12$, and the fraction of molecules above escape velocity is $7.8\times10^{-22}$ — a number that is a computation, and that stays a computation under either constant.)

## The honest ledger

What would it take to arbitrate the constant with this distribution? The observable is a speed distribution, and every technique that reads one — Maxwell's own rotating-disc selector, Miller and Kusch's 1955 time-of-flight measurements, modern laser-induced-fluorescence and velocity-map imaging — returns either a *ratio* of count rates or a Doppler shift calibrated against a known transition. The ratios that are cleanest (rms-to-mode, effusion ratios, sound speed over thermal speed) are exactly the π-free ones. The ones that carry the constant carry it at half power, where the whole gap is $4.79$ parts in ten thousand, and they require the temperature and the mass to be known better than that: a $0.05\%$ uncertainty in $T$ — routine in a molecular beam, where the rotational temperature is inferred, not read — contributes $0.025\%$ to $\bar v$, about half the gap, and a $0.1\%$ uncertainty in $T$ already exceeds it.

The deeper point is the one this site keeps returning to. The distribution is a *computed* object: it is the Boltzmann factor times a density of states, and the density of states is a volume in velocity space, which is a measure on the plane and on the sphere, whose normalisation is an integral. Nothing in that chain is a measurement of a circle. The constant enters as the total measure of a turn, once per axis, under a square root; and the moment it is written in units of the most probable speed, mass and temperature cancel and a single $\sqrt\pi$ is all that is left to argue about.

Computed, never measured.

## Further Reading

- [The Coaxial Cable: Why the Characteristic Impedance Carries 1/2π](/blog/posts/2026-11-02-coaxial-cable-characteristic-impedance-2pi-golden-pi/) — the same structural question in electromagnetism: a constant that appears twice in opposite directions and cancels from the observable.
- [Stokes' Law: Why the Drag on a Sphere Is 6πμav](/blog/posts/2026-10-31-stokes-law-drag-sphere-6pi-viscosity-golden-pi/) — six half-turns of surface measure, and a drag coefficient 24/Re that carries none of them.
- [Al-Kashi's 805,306,368-Sided Polygon](/blog/posts/2026-11-03-al-kashi-sexagesimal-polygon-cube-scaling-golden-pi/) — how a polygon's defect amplifies the constant's gap threefold, and why precision was never the arbiter.
- [The Wallis Product: How an Infinite Product of Rationals Computes π/2](/blog/posts/2026-10-12-wallis-product-infinite-product-rationals-computes-circle-constant-golden-pi/) — the $\sqrt\pi$ of the central binomial coefficient, derived from the same Gaussian-type integrals used above.
- [The Casimir Effect: π²/240 Between Two Plates](/blog/posts/2026-10-16-casimir-effect-vacuum-pressure-computes-circle-constant-golden-pi/) — a thermal-mode count that ends at a rational, and the best available test of how far a computed constant travels into a measured force.
