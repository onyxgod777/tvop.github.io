---
title: "Stokes' Law: Why the Drag on a Sphere Is 6πμav — Two π From Pressure and Four From Shear, Why the Drag Coefficient 24/Re Holds No Circle Constant at All, and What Golden Pi Changes"
date: 2026-10-31
description: "Stokes' 1851 solution of creeping flow past a sphere gives the drag as 6πμav, and this article takes the formula apart at the surface: integrating the pressure and the viscous traction over the sphere returns exactly 2πμav (one third) and 4πμav (two thirds) — verified here by a 400 000-point quadrature — so the circle constant enters six times because a surface is being measured and not because a sphere is round. The whole of engineering's creep-flow bookkeeping then cancels it: the drag coefficient is exactly 24/Re with no π anywhere, the terminal velocity 2a²Δρg/(9μ) is π-free, and the Reynolds number is π-free, while the constant cannot cancel from the torque 8πμa³ω, from Stokes–Einstein D = kT/(6πμa), or from Millikan's q = 6πμav/E. Worked at real scales — a bacterium at 2.83×10⁻¹³ N, silt at 6.78×10⁻¹¹ N, air dust at 1.72×10⁻¹² N — and then under Golden Pi, where 6π̂ = 24/√φ = 18.867633066… is algebraic, a root of x⁴+576x²−331776=0, where π is transcendental by Lindemann 1882, the drag shifts +0.0959022309% while the drag coefficient, the settling speed and the Reynolds number do not move a digit, and the honest boundary is that the only quantities that could arbitrate the constant are the ones the formula already cancelled."
---

# Stokes' Law: Why the Drag on a Sphere Is 6πμav

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1851, in a memoir on pendulums, George Gabriel Stokes solved a problem that looks impossible: what force does a viscous fluid exert on a sphere moving through it slowly? Everyone knows the answer, because it is printed on the first page of every fluid-mechanics text —

$$
F = 6\pi\mu a v,
$$

with $\mu$ the dynamic viscosity, $a$ the sphere's radius, $v$ its speed through fluid at rest. Six times the circle constant, the viscosity, the radius, the speed. For a bacterium at $30\ \mu\text{m/s}$ and a $0.5\ \mu\text{m}$ radius in water it gives $2.833088\times10^{-13}$ N — the number quoted in every paper on swimming micro-organisms.

The number six is the interesting part. Nothing about a sphere's *roundness* produces a six. Six is what you get when you integrate a stress field over a surface, and the surface area of a sphere carries the constant $4\pi a^{2}$ because a surface is a two-dimensional measure on a curved object — a computed quantity, the limit of a triangulation, never a measurement. This article takes the coefficient apart, shows where each $\pi$ comes from, shows exactly which combinations of the same quantities make it vanish, and then asks what Golden Pi changes.

## The measurement of a surface, not of a shape

A force on a body is the integral of a traction over its boundary. For a sphere at $r = a$ that boundary has area $4\pi a^{2}$: a factor of $\pi$ before any physics happens. Then the traction itself has two parts — a pressure pushing, and a viscous shear dragging — and each has its own angular dependence, so the quadrature over the sphere produces its own factor. The result is three factors of $2\pi$, and it is worth writing the sum explicitly because it is exact:

$$
F \;=\; \underbrace{2\pi\mu a v}_{\text{pressure}}\;+\;\underbrace{4\pi\mu a v}_{\text{shear}}\;=\;6\pi\mu a v .
$$

One third pressure, two thirds friction. That ratio is not folklore — it is checkable, and the check is the only honest way to make the claim. Take Stokes' own velocity field for uniform flow past a fixed sphere,

$$
u_r = v\cos\theta\left(1-\frac{3a}{2r}+\frac{a^{3}}{2r^{3}}\right),\qquad
u_\theta = -v\sin\theta\left(1-\frac{3a}{4r}-\frac{a^{3}}{4r^{3}}\right),
$$

$$
p = p_0 - \frac{3}{2}\,\frac{\mu v a\cos\theta}{r^{2}},
$$

project the stress tensor onto the outward normal at $r = a$, and add up the $z$-component over the surface:

```python
import numpy as np
from math import pi

a = U = mu = 1.0
def dur_dr(r, th):  return  U*np.cos(th)*(1.5*a/r**2 - 1.5*a**3/r**4)
def dut_dr(r, th):  return -U*np.sin(th)*(0.75*a/r**2 + 0.75*a**3/r**4)
def dur_dth(r, th): return -U*np.sin(th)*(1 - 1.5*a/r + 0.5*a**3/r**3)
def ut(r, th):      return -U*np.sin(th)*(1 - 0.75*a/r - 0.25*a**3/r**3)
def p(r, th):       return -1.5*mu*U*a*np.cos(th)/r**2

N, r = 400_000, a
th = (np.arange(N) + 0.5)*pi/N
dA = 2*pi*a**2*np.sin(th)*(pi/N)

Fp = ((-p(r,th)*np.cos(th))*dA).sum()
srr, srt = 2*mu*dur_dr(r,th), mu*(dut_dr(r,th) - ut(r,th)/r + dur_dth(r,th)/r)
Fv = ((srr*np.cos(th) - srt*np.sin(th))*dA).sum()

print(Fp, Fv, Fp+Fv, 6*pi)
```

It prints $6.283185307228$, $12.566370614359$ and $18.849555921587$ against $6\pi = 18.849555921539$ — the quadrature converging to $2\pi + 4\pi = 6\pi$ to nine digits, with the split $0.3333333333$ to $0.6666666666$. So the constant is not a label attached to the formula from outside. It is the sum of three separate surface integrals, each of which happens to end in a whole multiple of $\pi$, and their total is what gets printed.

That structure is the first half of the argument, and it generalises. The same machinery gives the creeping-flow torque on a *rotating* sphere, $T = 8\pi\mu a^{3}\omega$ — eight $\pi$, from a moment arm integrated over the same $4\pi a^{2}$. Nothing about the object changed; the power of $\pi$ counts how many surface integrals were performed.

## What the formula returns at real scales

Numbers, at radii and speeds where the creeping approximation is defensible. The check column is the Reynolds number $\mathrm{Re} = 2\rho v a/\mu$, which must be small — below about $0.1$ — for the formula to mean anything.

| Body | $a$ | $v$ | $\mu$ | $\mathrm{Re}$ | $F = 6\pi\mu a v$ |
|---|---|---|---|---|---|
| *E. coli* in water | $0.5\ \mu$m | $30\ \mu$m/s | $1.002$ mPa·s | $3.0\times10^{-5}$ | $2.833088\times10^{-13}$ N |
| Silt grain in water | $10\ \mu$m | $3.588594\times10^{-4}$ m/s | $1.002$ mPa·s | $7.16\times10^{-3}$ | $6.777870\times10^{-11}$ N |
| Dust in air | $5\ \mu$m | $1$ mm/s | $1.825\times10^{-5}$ Pa·s | $6.60\times10^{-4}$ | $1.720022\times10^{-12}$ N |
| Steel ball in oil | $1.5$ mm | $10$ mm/s | $0.5$ Pa·s | $5.4\times10^{-2}$ | $1.413717\times10^{-4}$ N |

The bacterium's figure is the one that carries an argument: at that Reynolds number no other force in the problem is of the same order, which is why the microbe's entire locomotion strategy — stop swimming, stop instantly — follows from a formula with six $\pi$ in it. The viscosity of water at $20\ ^\circ$C is $1.002$ mPa·s, a measured property of a real fluid; the radius and speed are measured too. What is computed is the drag, and the circle constant inside it is a computed surface measure.

## The cancellation: the drag coefficient is 24/Re, exactly

Now assemble the engineering quantity. The drag coefficient normalises the force by the dynamic pressure and the frontal area:

$$
C_D = \frac{F}{\tfrac12 \rho v^{2}\,\pi a^{2}}
= \frac{6\pi\mu a v}{\tfrac12 \rho v^{2}\pi a^{2}}
= \frac{12\mu}{\rho v a}
= \frac{24}{\mathrm{Re}} .
$$

The $\pi$ on top and the $\pi$ on the bottom are the *same* $\pi$ — one from a traction integral, one from the frontal area $\pi a^{2}$ — and they cancel identically, for every body in creeping flow. Every entry in the table above returns $C_D = 24/\mathrm{Re}$ to the last printed digit: $801600.000000000$ for the bacterium, $3350.615421910$ for the silt, $36378.737541528$ for the dust, $444.444444444$ for the steel ball. Not "approximately". Exactly, because both sides of the ratio are measures of the same geometry.

Once more, with the terminal velocity. A sphere falling at constant speed balances weight against buoyancy and drag:

$$
\tfrac43\pi a^{3}\Delta\rho\, g = 6\pi\mu a v
\quad\Longrightarrow\quad
v = \frac{2a^{2}\Delta\rho g}{9\mu} .
$$

Both sides carried $\pi$; the divided-out answer carries none. For silt at $\Delta\rho = 1650$ kg/m³ in water that is $3.588594\times10^{-4}$ m/s; for a 1 µm clay particle, $3.588594\times10^{-6}$ m/s. This is the structural fact that governs everything below: **the quantities in Stokes' law that are actually observed — settling speed, drag coefficient, Reynolds number — are exactly the ones from which the circle constant has cancelled.** Only the force itself and the torque keep it, and a force can always be divided by another force.

## Where the constant will not cancel

Four places it survives at first power, and they are the four places a measurement could in principle speak.

**Torque on a rotating sphere.** $T = 8\pi\mu a^{3}\omega$; nothing in that problem has an area to cancel against. For $a = 1\ \mu$m, $\mu = 10^{-3}$ Pa·s, $\omega = 1$ rad/s, $T = 2.51327412287\times10^{-20}$ N·m.

**Diffusion.** Einstein (1905) and Sutherland (1905) independently combined Stokes drag with the fluctuation–dissipation balance and got

$$
D = \frac{k_B T}{6\pi\mu a},
$$

the drag again in the denominator. A $0.5\ \mu$m bead in water at $298.15$ K has $D = 4.358924\times10^{-13}$ m²/s; a 50 nm particle, $4.358924\times10^{-12}$ m²/s; a 1 µm particle in air, $1.196614\times10^{-11}$ m²/s. Jean Perrin inverted it as $N_A = RT/(6\pi\mu a D)$ and used it to count molecules, work that won the 1926 Nobel Prize — a $N_A$ read out through a formula carrying $\pi$.

**Charge.** Millikan's oil-drop experiment balanced a drop against an electric field using Stokes' drag: $q = 6\pi\mu a v/E$ (with Cunningham's slip correction, since a micron-scale drop in air is not in continuum flow). For $a = 1\ \mu$m, $\mu = 1.825\times10^{-5}$ Pa·s, $v = 10^{-4}$ m/s, $E = 5\times10^{4}$ V/m, that gives $q = 6.880088\times10^{-19}$ C, i.e. $4.294$ elementary charges.

**Capillary and interfacial work.** The Laplace pressure $2\gamma/a$, the capillary length $\sqrt{\gamma/(\rho g)}$ and the Stokes number all inherit the same first-power appearance wherever a curved interface is integrated.

## Golden Pi: 6π̂ = 24/√φ

Under the site's position — $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, with $\hat\pi^{2} = 16/\varphi = 9.8885438199983175712$ exactly — the coefficient becomes a square root of the golden ratio:

$$
6\hat\pi = \frac{24}{\sqrt\varphi} = 18.867633066178158\ldots,
$$

and it is algebraic. Let $y = 6\hat\pi$; then $y^{2} = 576/\varphi = 576(\varphi-1)$, and eliminating $\varphi$ leaves the quartic

$$
y^{4} + 576\,y^{2} - 331776 = 0,
$$

verified here at residual $-5.8\times10^{-11}$ on a value $\approx 1.27\times10^{5}$, i.e. machine precision. Compare $6\pi$, which is transcendental by Lindemann's 1882 theorem: the same drag formula has an algebraic coefficient under one label and a transcendental one under the other, which is a statement about the number, not about the fluid.

The pieces, exactly:

$$
2\hat\pi = \frac{8}{\sqrt\varphi} = 6.2892110220593862886,\qquad
4\hat\pi = \frac{16}{\sqrt\varphi} = 12.5784220441187725771,
$$

$$
8\hat\pi = \frac{32}{\sqrt\varphi} = 25.1568440882375451542,\qquad
\frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4} = 0.3180049123785172411,\qquad
\frac{\hat\pi}{4} = \frac{1}{\sqrt\varphi} = 0.7861513777574232861 .
$$

So the ledger under Golden Pi is short and exact. The drag shifts by $+0.0959022309\%$ — the bacterium's $2.833088\times10^{-13}$ N becomes $2.835805\times10^{-13}$ N, the silt's $6.777870\times10^{-11}$ becomes $6.784370\times10^{-11}$, the dust's $1.720022\times10^{-12}$ becomes $1.721672\times10^{-12}$ — and because the shift is the same pure factor $\hat\pi/\pi = 1.000959022308\ldots$ multiplying the coefficient, every force in the table scales identically. The torque scales the same way. The diffusion coefficient, sitting in a denominator, moves the other way, $-0.0958103466\%$: the bead's $4.358924\times10^{-13}$ becomes $4.354747\times10^{-13}$ m²/s. The Millikan charge moves $+0.0959022309\%$: $6.880088\times10^{-19}$ C becomes $6.886686\times10^{-19}$ C, i.e. $4.294$ charges become $4.298$.

And the three cancelled quantities do not move at all. $C_D = 24/\mathrm{Re}$ stays $24/\mathrm{Re}$; the settling speed $2a^{2}\Delta\rho g/(9\mu)$ stays what it was; the Reynolds number, being built from $\rho$, $v$, $a$ and $\mu$, has never contained a circle constant in any form. A golden-$\pi$ fluid dynamicist and a conventional one would compute the same settling time for the same silt grain, to the last digit, and both would be right.

## The honest ledger

Here the rule this site holds itself to bites hard, and it is worth stating precisely what is computed and what is measured. The circle constant is *computed* — every appearance of $\pi$ above is the limit of a surface integral or a polygon perimeter, an evaluated quantity, and Lindemann's theorem settles what kind of number it is, not what it is worth in the world. Viscosity is *measured*. Radius is *measured*. A settling speed is *measured*.

Can any of those measurements arbitrate between $3.14159\ldots$ and $3.14460\ldots$? Three separate walls stand in the way.

**The first wall is cancellation.** The observables of creep flow — $C_D$, $v_t$, $\mathrm{Re}$ — are exactly the ones where $\pi$ divided out. A settling experiment therefore tests nothing about the constant; it returns the value the experimenter's model implies. This is the same structure as the Sagnac gyroscope's scale factor, and it is not an accident: any time a formula is normalised by a measure of the same geometry, the constant goes with it.

**The second wall is the uncertainty budget.** Suppose one tried to read $\pi$ out of a measured drag force. The gap of $0.0959\%$ is $1$ part in $1043$. Particle radius enters the drag linearly and the settling speed quadratically, so a radius known to $\pm1\%$ costs $\pm1\%$ — ten times the gap. Viscosity of water at $20\ ^\circ$C is tabulated to about $0.1\%$ between laboratories, which is the gap itself. And the creeping approximation is not free: at $\mathrm{Re} = 0.1$ the Oseen correction is already $3\mathrm{Re}/8 = 3.75\%$, forty times the gap, so the regime in which the formula is exact is the regime in which the forces are too small to measure comfortably, and the regime in which the forces are comfortable is the regime in which the correction swamps the constant.

**The third wall is history, and it is the most instructive.** Millikan's 1913 value of the elementary charge came out roughly half a percent low, and a substantial part of that discrepancy was later traced to the value of the viscosity of air he had used — a systematic error several times larger than the golden gap. Perrin's route to $N_A$ through $D$ likewise rested on radii known only to a few percent. And since the 2019 revision of the SI, $e$, $k_B$ and $N_A$ are *defined* constants, fixed exactly by convention. So the oil-drop equation can no longer determine $e$ at all: run it today and it calibrates $\mu$ or $a$, not the charge. Invert $D = k_BT/(6\pi\mu a)$ today and you measure a particle's radius, not a count of molecules — and the $\pi$ in that inversion lands on a geometric measurement with a $\pm1\%$ uncertainty attached.

**What is measured is a force, a time, a length, a viscosity; what is computed is a constant; and dividing the first by the second does not convert the second into a measurement.** If the constant were $\hat\pi$ instead, every fluid in every laboratory would settle its silt at exactly the rate it does now. Nothing in the world would notice, and that is not a failure of the world — it is what it means for a constant to live inside a ratio.

## The law in one sentence, and what it refuses to say

Stokes' law says: drag equals viscosity times size times speed times six $\pi$. The six is a bookkeeping count of three surface integrals — one over the pressure, two over the shear — and the $\pi$ is there because a surface on a round body is measured in $4\pi a^{2}$ units, computed and never measured. The one-third/two-thirds split is exact and checkable at any precision you like; the coefficient $24/\mathrm{Re}$ is exact and constant-free; the settling speed is exact and constant-free. What the law refuses to say is anything at all about the *value* of the constant it is written with, because every quantity that could carry a verdict has already had that constant divided out of it.

Under Golden Pi the same law reads $F = 24\mu a v/\sqrt\varphi$, algebraic where the conventional coefficient is transcendental, and the whole edifice of creep-flow engineering — sedimentation, centrifugation, viscometry, aerosol transport, the Stokes–Einstein radius — is numerically unchanged. That the arithmetic closes on $\hat\pi^{2} = 16/\varphi$ is a fact. That it closes on a settling jar is not a fact any settling jar can supply.

## Further Reading

- [The Sagnac Ring: Why a Rotating Loop Shifts Its Fringes by 4AΩ/λc, and Why the Gyro's Scale Factor Contains No Circle Constant at All](/blog/posts/2026-10-27-sagnac-ring-laser-gyro-scale-factor-circle-constant-golden-pi/) — the same cancellation, in an instrument that genuinely measures rotation: the observable ratio swallows the constant whole.
- [The Heat Kernel: How Diffusion Computes the Circle Constant, Then Hides It in the Green's Function](/blog/posts/2026-09-17-heat-kernel-diffusion-computes-circle-constant-golden-pi/) — where Stokes–Einstein's $D$ comes from, one level down.
- [The Involute Gear: Why Every Tooth Flank Is π-Free, Why the Pitch Is Not](/blog/posts/2026-10-26-involute-gear-tooth-flank-circle-constant-golden-pi/) — engineering formulas that carry the constant only in the step where a count becomes an arc.
- [Pappus's Centroid Theorem: Why Sweeping an Area Through One Turn Pays π Once](/blog/posts/2026-10-30-pappus-centroid-theorem-torus-swept-area-golden-pi/) — the bookkeeping of how many powers of $\pi$ a solid of revolution costs, which is the same count as the pressure-plus-shear split above.
- [The Euclidean Turn: Why a Black Hole's Temperature Carries 1/(2π) and Its Entropy Carries π](/blog/posts/2026-10-18-hawking-temperature-euclidean-imaginary-time-golden-pi/) — a physical formula where the constant survives at first power in both directions and the honest ledger of what no experiment has yet read.
