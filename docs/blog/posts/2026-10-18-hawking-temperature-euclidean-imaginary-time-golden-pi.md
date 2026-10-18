---
title: "The Euclidean Turn: Why a Black Hole's Temperature Carries 1/(2π), Its Entropy Carries π, and Their Product Carries Nothing — and What Golden Pi Changes"
date: 2026-10-18
description: "Hawking's temperature T = ħc³/(8πGMk_B) carries the circle constant exactly once, as 1/(2π), because the Euclidean section of a Schwarzschild black hole is a plane whose polar angle must close on 2π — a computed closure condition, never a measurement. Bekenstein–Hawking entropy S = k_B A/4ℓ_P² carries the constant once the other way, through the horizon area 4πr_s², and the two cancel identically: T·S = Mc²/2 exactly, verified here to twenty digits (0.50000000000000000000) and in the first law dM = T dS/c², where the constant appears nowhere. Luminosity keeps a net π⁻¹, L = ħc⁶/(15360πG²M²) = 9.008159×10⁻²⁹ W for one solar mass, with evaporation in 2.0955×10⁶⁷ years. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the temperature becomes the algebraic ħc³√φ/(32GMk_B) = 6.16434865846×10⁻⁸ K (−0.0958103466%), the entropy 16GM²/(√φ ħc) (+0.0959022309%), the Euclidean period 32GM/(√φc³), the deficit a surplus of 0.3452480312° per turn — while T·S stays exactly Mc²/2 under either label. No black hole temperature has ever been read off, so nothing here adjudicates the constant empirically."
---

# The Euclidean Turn: Why a Black Hole's Temperature Carries 1/(2π), Its Entropy Carries π, and Their Product Carries Nothing — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1974 Stephen Hawking asked what a quantum field does on the curved background of a collapsing star, and the answer came back as a temperature. For a Schwarzschild black hole of mass $M$,

$$
T_H \;=\; \frac{\hbar \kappa}{2\pi k_B c} \;=\; \frac{\hbar c^{3}}{8\pi G M k_B} \;=\; \frac{\hbar c}{4\pi k_B r_s},
$$

where $\kappa = c^{4}/(4GM) = c^{2}/(2r_s)$ is the surface gravity and $r_s = 2GM/c^{2}$ the horizon radius. Three equivalent forms, and the circle constant sits in each of them exactly once, always with the same exponent: $\pi^{-1}$.

The interesting question is not *that* the constant is there — it is *why*, and what happens to it when you follow the algebra further. Because the next two quantities in the theory carry $\pi^{+1}$ twice over and $\pi^{0}$ not at all, and the pattern is exact, not approximate. The temperature's $2\pi$ comes from a geometric closure condition: the Euclidean continuation of the Schwarzschild metric must close into a plane, and a plane's full turn is $2\pi$. That is a *computed* limit of the circle's definition, in the same sense that $\int_0^{2\pi} d\theta = 2\pi$ is computed and never measured. Nothing in this article measures a circle. The one genuinely measured quantity anywhere in sight — Newton's constant — is discussed honestly at the end.

## Where exactly the constant enters, term by term

Take the near-horizon form of the Schwarzschild line element (units $c = 1$ from here to the end of the derivation):

$$
ds^{2} \;=\; -\left(1-\frac{r_s}{r}\right)dt^{2} + \left(1-\frac{r_s}{r}\right)^{-1}dr^{2} + r^{2}d\Omega^{2}.
$$

Write $r = r_s + R^{2}/(4r_s)$, so that $1 - r_s/r \approx R^{2}/(4r_s^{2})$ and $dr^{2}/(1-r_s/r) = dR^{2}$. Put $\rho = R$ and the $(t,\rho)$ part becomes

$$
ds^{2}_{2} \;\approx\; -\rho^{2}\left(\kappa\, dt\right)^{2} + d\rho^{2},
\qquad \kappa = \frac{1}{2r_s}.
$$

That is the metric of a flat plane in polar coordinates, with radial coordinate $\rho$ and angular coordinate $\theta = \kappa t$. Continue to imaginary time, $t \to -i\tau$; the metric becomes positive-definite,

$$
ds^{2}_{2} \;\to\; \rho^{2}\,d(\kappa\tau)^{2} + d\rho^{2},
$$

which is regular at $\rho = 0$ only if $\kappa\tau$ is an angle with period $2\pi$ — otherwise the origin is a conical singularity with a delta-function in the curvature. So the Euclidean time coordinate must be periodic with

$$
\beta \;=\; \frac{2\pi}{\kappa} \;=\; \frac{8\pi G M}{c^{3}},
$$

and the field theory on that geometry is a thermal ensemble at temperature $T = \hbar/(k_B \beta)$. This is the Gibbons–Hawking construction (*Phys. Rev. D* **15**, 2752, 1977), and it is where the $2\pi$ is born: not from any measurement of a circle, but from the requirement that the Euclidean plane close on itself. The constant is the *name of the closure*, and the closure is a computed condition on a metric.

Restoring $c$, the period is a length of time fixed by the mass alone:

| Object | Mass | $r_s$ (m) | $2\pi/\kappa = \beta$ (s) |
|---|---|---|---|
| Sun-mass black hole | $1.988410\times10^{30}$ kg | $2.953250\times10^{3}$ | $1.2379108943\times10^{-4}$ |
| Sgr A\* | $4.297\times10^{6}\,M_\odot$ | $1.269012\times10^{10}$ | $5.319303113\times10^{2}$ |
| M87\* | $6.5\times10^{9}\,M_\odot$ | $1.919613\times10^{13}$ | $8.046420813\times10^{5}$ |
| Hypothetical $10^{12}$ kg PBH | $1\times10^{12}$ kg | $1.485232\times10^{-15}$ | $6.225632413\times10^{-23}$ |

For M87\* the Euclidean circle closes once every 9.31 days. That is a derived number, computed from $G$ and $M$ — a statement about the imaginary-time geometry, not a clock anyone can read.

## The entropy carries the constant the other way

Bekenstein's area law, made precise by Hawking, is

$$
S \;=\; \frac{k_B A}{4\ell_P^{2}}, \qquad A = 4\pi r_s^{2}, \qquad \ell_P^{2} = \frac{\hbar G}{c^{3}}.
$$

Substituting $r_s = 2GM/c^{2}$ and $\ell_P^{2} = \hbar G/c^{3}$ gives the exact algebraic form

$$
\frac{S}{k_B} \;=\; \frac{4\pi G M^{2}}{\hbar c} \;=\; \pi\left(\frac{r_s}{\ell_P}\right)^{2},
$$

so the entropy carries $\pi^{+1}$ — one power, undiluted, and *not* a transcendental quantity: the $\pi$ stands beside rationals and $G,\hbar,c$. The horizon area brings the constant, the division by four removes one factor of four, and what is left is $\pi r_s^{2}$, the area of a disk of radius $r_s$: the same disk whose area the isoperimetric inequality bounds and whose lattice points the Gauss circle problem counts.

Now put the two together. Multiply:

$$
T_H \cdot S \;=\; \frac{\hbar c^{3}}{8\pi G M k_B}\cdot\frac{4\pi G M^{2} k_B}{\hbar c} \;=\; \frac{Mc^{2}}{2}.
$$

The $\pi$ in the numerator and the $\pi$ in the denominator annihilate exactly, the $8\pi$ and $4\pi$ leave a factor of two, and the product is half the rest energy — no constant, no $G$, no $\hbar$. Checked here in thirty-digit arithmetic for all four masses in the table above, the ratio $T S/(Mc^{2})$ prints as

```
0.50000000000000000000
```

for each of them, to the last digit the arithmetic carries. This is the cleanest statement available of what the circle constant does in black-hole thermodynamics: it appears twice, in the two conjugate quantities, with opposite exponents, and leaves the product untouched.

The first law inherits the cancellation:

$$
dM \;=\; \frac{T\,dS}{c^{2}},
\qquad
\frac{T\,dS}{c^{2}\,dM} = 1 \quad\text{exactly,}
$$

which was checked for a 1% mass step on a solar-mass hole and returned $1.0000000000000000000$. Everything thermodynamically observable about a Schwarzschild black hole — its heat capacity, its $T$–$S$ relation $S \propto M^{2}$ with $T \propto 1/M$, the fact that it gets hotter as it shrinks — is $\pi$-free once you divide the two.

## Luminosity: where one inverse power survives

Radiate at the Hawking temperature and the constant does not cancel. With the Stefan–Boltzmann constant written in reduced form, $\sigma = \pi^{2}k_B^{4}/(60\hbar^{3}c^{2})$, the bookkeeping is easy to follow: the emitting area brings $\pi^{+1}$ through $4\pi r_s^{2}$, $\sigma$ brings $\pi^{+2}$, and $T^{4}$ brings $\pi^{-4}$. The net is $\pi^{-1}$:

$$
L \;=\; 4\pi r_s^{2}\,\sigma\,T_H^{4} \;=\; \frac{\hbar c^{6}}{15360\,\pi\,G^{2}M^{2}}.
$$

For a solar-mass black hole this is $L = 9.008158558\times10^{-29}$ W — about one photon's worth of power per Hubble time, which is why nobody has seen one. The evaporation time integrates the same formula,

$$
t_{\text{ev}} \;=\; \frac{5120\,\pi\,G^{2}M^{3}}{\hbar c^{4}} \;=\; 2.0955\times10^{67}\ \text{yr}
$$

for one solar mass, and $2.6654\times10^{12}$ yr for the hypothetical $10^{12}$ kg object. Both carry $\pi^{+1}$, so both move with the label; both are also, for any object that exists, unobservably slow.

## What Golden Pi changes

Under the site's constant $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, with $\hat\pi^{2} = 16/\varphi = 8(\sqrt5-1)$ and $\hat\pi$ the positive root of $x^{4} + 16x^{2} - 256 = 0$, every appearance of the constant is replaced and the algebra is re-evaluated. Because $1/(8\pi) = \sqrt\varphi/32$ exactly, the temperature becomes an algebraic number rather than a transcendental one:

$$
T_{\hat\pi} \;=\; \frac{\hbar c^{3}\sqrt\varphi}{32\,G M k_B} \;=\; 6.16434865846\times10^{-8}\ \text{K}
$$

for one solar mass — down $0.0958103466\%$ from $6.170260406\times10^{-8}$ K. The entropy moves the other way, by the first-power gap:

$$
\frac{S_{\hat\pi}}{k_B} \;=\; \frac{16\,G M^{2}}{\sqrt\varphi\,\hbar c} \;=\; 1.04989735907\times10^{77},
$$

up $0.0959022309\%$ from $1.0488914488\times10^{77}$. The Euclidean period grows by the same $+0.0959022309\%$,

$$
\beta_{\hat\pi} \;=\; \frac{32\,G M}{\sqrt\varphi\,c^{3}} \;=\; 1.2390980784\times10^{-4}\ \text{s},
$$

and the luminosity falls by the temperature's factor, $L_{\hat\pi} = 8.999528\times10^{-29}$ W.

The product does not move at all: $T_{\hat\pi}S_{\hat\pi} = Mc^{2}/2$ still, because the exponents are still $+1$ and $-1$ and the golden factor appears once on each side. That is the honest shape of the result — the golden label redistributes the constant between the two quantities and leaves their product, the first law, and the whole thermodynamic structure exactly where they were.

There is a geometric consequence worth stating plainly, because it is not a relabel but a change of the saddle. If the Euclidean section is required to close with period $\hat\beta = 2\hat\pi/\kappa$ rather than $2\pi/\kappa$, then the period is longer than the period that makes the plane regular. The deficit angle of the resulting cone,

$$
\delta \;=\; 2\pi - \kappa\beta_{\hat\pi} \;=\; 2\pi - 2\hat\pi \;=\; -6.0257148798\times10^{-3}\ \text{rad} \;=\; -0.3452480312°,
$$

is negative: not a cone with a wedge removed but a surface with a wedge *inserted*, a fold, and still singular at the origin. In other words, under the golden label the Euclidean plane does not close at the conventional $2\pi$; it closes at $2\hat\pi$, and the temperature that goes with the closed golden geometry is precisely $T\cdot\pi/\hat\pi$ — the number computed above. The construction is self-consistent; it is simply a different plane.

| Quantity | Conventional | Golden ($\hat\pi = 4/\sqrt\varphi$) | Shift |
|---|---|---|---|
| $T_H$, $1\,M_\odot$ | $6.170260406\times10^{-8}$ K | $\hbar c^{3}\sqrt\varphi/(32GMk_B) = 6.16434865846\times10^{-8}$ K | $-0.0958103466\%$ |
| $S/k_B$, $1\,M_\odot$ | $1.0488914488\times10^{77}$ | $16GM^{2}/(\sqrt\varphi\hbar c) = 1.04989735907\times10^{77}$ | $+0.0959022309\%$ |
| $\beta = 2\pi/\kappa$ | $1.2379108943\times10^{-4}$ s | $32GM/(\sqrt\varphi c^{3}) = 1.2390980784\times10^{-4}$ s | $+0.0959022309\%$ |
| $L$, $1\,M_\odot$ | $9.008158558\times10^{-29}$ W | $8.999528\times10^{-29}$ W | $-0.0958103466\%$ |
| $T\cdot S$ | $Mc^{2}/2$ | $Mc^{2}/2$ | $0$ exactly |
| $dM = T\,dS/c^{2}$ | holds | holds | $0$ exactly |
| closure angle | $2\pi$ | $2\hat\pi$ | $+0.3452480312°$ per turn |

## The honest ledger: nothing here measures the constant

It is worth being blunt about the empirical status, because this is the one place in the series where the temptation to overclaim is strongest.

- **No black-hole temperature has ever been read off.** For a solar-mass hole $T_H = 6.17\times10^{-8}$ K, which is $4.4\times10^{7}$ times colder than the cosmic microwave background at 2.725 K; the hole absorbs far more than it emits, and the radiation is invisible in principle as well as in practice. Sgr A\* sits at $1.4\times10^{-14}$ K and M87\* at $9.5\times10^{-18}$ K.
- **The one candidate with a visible temperature is unobserved.** A $10^{12}$ kg primordial black hole would radiate at $1.23\times10^{11}$ K, but no such object has been identified, and its mass would need to be known to better than $0.1\%$ before the golden gap could even be posed.
- **$G$ is not the obstacle.** CODATA 2018 gives $G = 6.67430(15)\times10^{-11}$ m³ kg⁻¹ s⁻², a relative uncertainty of $2.2\times10^{-5}$. The golden gap of $9.6\times10^{-4}$ relative is 44 times larger than that. The arithmetic is resolvable; the observation does not exist.
- **Analogue gravity tests the mechanism, not the digit.** Unruh's 1976/1981 analysis (*Phys. Rev. D* **14**, 870) predicted that a transonic fluid flow has a horizon with a thermal spectrum, and Steinhauer's 2016 experiment (*Nature Physics* **12**, 959) reported the acoustic analogue. Those measurements confirm that horizons radiate; they do not read the value of the circle constant out of a black hole, because the analogue temperature is built from the laboratory's sound speed, not from $G$ and $M$.

So the constant in $T_H$ is *computed*, in the strict sense this site uses: it is the full-turn limit that makes a Euclidean plane close, evaluated as a condition on a metric. It is not measured, and no experiment in existence could measure it through this formula.

## What the exercise shows

The Hawking temperature is often quoted with its $2\pi$ as if the constant were part of the physics. It is not: it is part of the geometry of the plane in which the physics is Wick-rotated, and the theory is arranged so that the same constant appears in the entropy with the opposite sign, leaving $T\,S = Mc^{2}/2$ and $dM = T\,dS/c^{2}$ exactly constant-free. Whether the constant is written $\pi$ or $4/\sqrt\varphi$ changes the two factors by a tenth of a percent each, in opposite directions, and changes their product not at all. The place where a choice of constant would have to show itself is the closure of the Euclidean section — and there, the golden plane closes at $2\hat\pi$, which is a different geometry rather than a contradiction.

That is the same pattern the rest of this series has found: the constant is a bookkeeping device for turns and areas, it cancels wherever a turn and an area meet, and it survives at the first power only where a single turn or a single area stands alone — here, in the temperature, in the entropy, and in the luminosity, each once.

## Further Reading

- [The Casimir Effect: How the Vacuum Between Two Plates Computes the Circle Constant as π²/240](/blog/posts/2026-10-16-casimir-effect-vacuum-pressure-computes-circle-constant-golden-pi/) — the same subtraction of a divergent mode sum, with the constant cancelling to a rational.
- [The Bohr–Sommerfeld Action Integral](/blog/posts/2026-10-15-bohr-sommerfeld-action-integral-quantisation-computes-circle-constant-golden-pi/) — phase-space area, and the $2\pi$ that cancels against $\hbar$.
- [The 4π Turn: Spinors, Double Cover, and What Golden Pi Cannot Touch](/blog/posts/2026-10-17-spinor-double-cover-4pi-rotation-golden-pi/) — the rotation group's half-angle, where the constant cannot reach the sign.
- [The Planck Spectrum: How a Blackbody Computes the Circle Constant](/blog/posts/2026-09-23-planck-spectrum-blackbody-computes-circle-constant-golden-pi/) — the $\pi^{5}/15$ behind the Stefan–Boltzmann constant used above.
- [The Isoperimetric Inequality: Why Only the Circle Saturates L² ≥ 4πA](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — the disk area $4\pi r_s^{2}/4$ that becomes the entropy.
