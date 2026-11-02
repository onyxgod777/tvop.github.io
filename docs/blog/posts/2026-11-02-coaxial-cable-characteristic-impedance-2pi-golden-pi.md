---
title: "The Coaxial Cable: Why the Characteristic Impedance Carries 1/2π, Why L·C = με Cancels It Entirely, and What Golden Pi Changes"
date: 2026-11-02
description: "A coaxial cable's impedance is written 50 Ω and its impedance formula is (1/2π)√(μ/ε)·ln(D/d), so the circle constant is visibly present in every RF design book. This article derives the cable from first principles and shows where the constant actually sits: Gauss's law gives E = q′/(2πε₀r) with 2πr the circumference of the Gaussian cylinder, Ampère's law gives B = μ₀I/(2πr), and the two 2π's land on opposite sides of the ratio — so the capacitance per metre carries 2π in the numerator and the inductance per metre carries it in the denominator, and their product is exactly με with no circle constant left. Worked on real cables: RG-58 with εr = 2.25 gives C′ = 100.0692285594456 pF/m, L′ = 250.1730713986140 nH/m, Z₀ = 50.000000 Ω and v = c/√εr = 199 861 638.667 m/s, with C′L′ − μ₀ε₀εr = 0 to twenty-two digits. The surviving 1/2π is worked as the 59.9584916 Ω of the cable-maker's 60 ln(D/d), the 376.7303137 Ω of free space against the folklore's 120π = 376.9911 Ω (+0.069%), and the catalogues' 50/75 Ω. Then Golden Pi (π̂ = 4/√φ = 3.144605511…), where 1/2π̂ = √φ/8 exactly — algebraic, root of 4096y⁴ − 64y² − 1 = 0 — a 50 Ω cable relabelling to 49.9520948 Ω, Γ(75 Ω load) moving 0.200000 → 0.200460, and the honest boundary: absorbing that 0.0959% needs the dielectric constant to 0.192% while solid polyethylene is only specified to 0.44%, and any measured Z₀ is degenerate between π and the logarithm."
---

# The Coaxial Cable: Why the Characteristic Impedance Carries 1/2π

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Every RF laboratory in the world is full of 50 Ω cable, and every textbook that describes it prints the same line:

$$
Z_0 \;=\; \frac{1}{2\pi}\sqrt{\frac{\mu}{\varepsilon}}\;\ln\!\frac{D}{d}
\;=\; 59.9584916\ \Omega \cdot \ln\!\frac{D}{d}\quad(\text{vacuum dielectric}).
$$

There is the circle constant, sitting in plain sight at first power, in a formula that an engineer uses to cut a cable. It is the kind of appearance that looks like evidence: if you want to know the value of $\pi$, here is a machine whose impedance is built out of it, and the machine is manufacturable to a thousandth of an inch.

The point of this article is that the appearance is *placed*, not observed. The $2\pi$ in that formula comes from one place only — the circumference of a cylinder drawn inside Gauss's law — and it arrives twice, once in the electric field and once in the magnetic field, and the two arrivals sit on opposite sides of the ratio. What an instrument reads off a cable is a capacitance per metre and an inductance per metre, and their **product is exactly $\mu\varepsilon$**, with no circle constant anywhere in it. The constant is in the cross-section; the physics is in the product. That distinction decides, at the end, whether a cable can arbitrate the value of $\pi$ — and it cannot, for a reason that has nothing to do with precision and everything to do with what the cable actually measures.

## The field of a line charge is one circumference

Take the inner conductor of a coax as a line of charge with linear density $q'$ coulombs per metre. Gauss's law over a cylinder of radius $r$ coaxial with it gives

$$
\oint \mathbf{E}\cdot d\mathbf{A} \;=\; E(r)\cdot 2\pi r \ell \;=\; \frac{q'\ell}{\varepsilon},
\qquad\text{so}\qquad
E(r) \;=\; \frac{q'}{2\pi\varepsilon r}.
$$

That $2\pi r\ell$ is the lateral area of the Gaussian cylinder, and the $2\pi r$ inside it is the circumference — a *computed* limit, the perimeter of a regular $n$-gon as $n\to\infty$, never a measured length. So the constant enters at first power in the field, exactly where the geometry of a round cross-section enters, and only there.

Integrating the field between the conductors gives the potential difference, and dividing the charge by it gives the capacitance per unit length:

$$
V \;=\; \int_a^b E\,dr \;=\; \frac{q'}{2\pi\varepsilon}\ln\frac{b}{a},
\qquad
C' \;=\; \frac{2\pi\varepsilon}{\ln(D/d)}.
$$

The magnetic side is the same story in the other direction. Ampère's law around a loop of radius $r$ gives $B = \mu I/(2\pi r)$; the flux threaded between the conductors is $\Phi = (\mu I/2\pi)\ln(D/d)\,\ell$; dividing by the current gives the inductance per unit length:

$$
L' \;=\; \frac{\mu}{2\pi}\ln\frac{D}{d}.
$$

Look at the two results side by side. $C'$ has $2\pi$ in the **numerator**. $L'$ has $2\pi$ in the **denominator**. Everything else in both expressions is the same number $\ln(D/d)$, the same $\mu$ and $\varepsilon$ — because it is the same electric and magnetic field of the same geometry, seen twice.

## The product cancels to the last digit

Multiply them:

```
C' · L' = (2πε / ln(D/d)) · (μ ln(D/d) / 2π) = με          exactly
```

The $\ln(D/d)$ cancels. The $2\pi$ cancels. What survives is $\mu\varepsilon$, and therefore the wave speed on the line is

$$
v \;=\; \frac{1}{\sqrt{L'C'}} \;=\; \frac{1}{\sqrt{\mu\varepsilon}} \;=\; \frac{c}{\sqrt{\varepsilon_r}},
$$

with no circle constant in it at all. This is worth checking on a real cable rather than asserting. Take RG-58/U with solid polyethylene, $\varepsilon_r = 2.25$, and a 50 Ω design impedance. Inverting the impedance formula gives $\ln(D/d) = 2\pi Z_0\sqrt{\varepsilon_r}/Z_\text{vac} = 1.2508653563121295$, i.e. $D/d = 3.493364655$ — which is exactly the 0.116″ over 0.033″ of the real cable. Then

$$
C' = \frac{2\pi\varepsilon_0\varepsilon_r}{\ln(D/d)} = 100.06922855944561487\ \text{pF/m},
\qquad
L' = \frac{\mu_0\ln(D/d)}{2\pi} = 250.17307139861403718\ \text{nH/m},
$$

and the product:

| Quantity | Value |
|---|---|
| $C'$ | $100.06922855944561487$ pF/m |
| $L'$ | $250.17307139861403718$ nH/m |
| $\sqrt{L'/C'}$ | $50.000000000000$ Ω |
| $v = 1/\sqrt{L'C'}$ | $199\,861\,638.666667$ m/s |
| $c/\sqrt{2.25}$ | $199\,861\,638.666667$ m/s |
| $C'L' - \mu_0\varepsilon_0\varepsilon_r$ | $0$ (to twenty-two digits) |

A 2.25 dielectric slows light by exactly a factor $1.5$: velocity factor $0.6666667$. The catalogue value for RG-58 is 0.66, and the small shortfall is because real foam and real PE are not exactly 2.25 — not because any $\pi$ was involved. Across the standard cable families the same arithmetic reproduces the datasheets from $C'$ and $Z_0$ alone:

| Cable | $Z_0$ (Ω) | $C'$ (pF/m) | $L' = Z_0^2 C'$ (nH/m) | VF $= 1/(c\sqrt{L'C'})$ | $\varepsilon_r$ |
|---|---|---|---|---|---|
| RG-58/U | 50 | 100.0 | 250.000 | 0.6671 | 2.2469 |
| RG-213/U | 50 | 101.0 | 252.500 | 0.6605 | 2.2921 |
| RG-6/U | 75 | 53.1 | 298.688 | 0.8376 | 1.4255 |
| RG-11A/U | 75 | 67.0 | 376.875 | 0.6638 | 2.2694 |
| LMR-400 | 50 | 78.7 | 196.750 | 0.8477 | 1.3917 |

Two cables with the same impedance, RG-58 and LMR-400, differ by a factor 1.27 in velocity factor and 1.39 in $\varepsilon_r$ — and $Z_0$ does not see it, because $Z_0 = \sqrt{L'/C'}$ is a ratio and the dielectric scales both terms equally.

## Where the 1/2π survives, and what 60 Ω really is

The ratio form of the impedance keeps one power of the constant:

$$
Z_0 \;=\; \sqrt{\frac{L'}{C'}} \;=\; \frac{1}{2\pi}\sqrt{\frac{\mu}{\varepsilon}}\;\ln\frac{D}{d}.
$$

With vacuum dielectric, $\sqrt{\mu_0/\varepsilon_0} = \mu_0 c = 376.730313666853$ Ω, and

$$
\frac{376.730313666853}{2\pi} \;=\; 59.958491632639947\ \Omega,
$$

which is the origin of the cable maker's rule of thumb "$60\ln(D/d)$ ohms" — a rounded 59.958. The rounding matters more than people expect: the folklore value for the impedance of free space, $120\pi = 376.991118$ Ω, is $+0.0692\%$ above the actual $\mu_0 c$. Before 2019 the discrepancy was different in kind (with $\mu_0 = 4\pi\times10^{-7}$ exact, $Z_0 = 4\pi c\times10^{-7} = 376.730313461$ Ω); since the 2019 SI, $c$ is exact and $\mu_0$ is a measured quantity with a relative uncertainty of $1.5\times10^{-10}$ — so $Z_\text{vac}$ is now a *measurement*, not a definition, and $120\pi$ was never more than an approximation.

Inverting the formula gives the geometry that a design impedance forces:

$$
\ln\frac{D}{d} = \frac{2\pi Z_0}{Z_\text{vac}}:
\qquad
Z_0 = 50\ \Omega \Rightarrow \ln = 0.833910238,\ \frac{D}{d} = 2.302304;
\qquad
Z_0 = 75\ \Omega \Rightarrow \ln = 1.250865356,\ \frac{D}{d} = 3.493365.
$$

And here is the honest note on the famous 50 Ω: it is not a constant of nature and contains no circle constant. It is a compromise between power handling (which favours about 30 Ω) and attenuation (which favours about 77 Ω), struck by US Navy practice in the 1940s. The number 50 has nothing to do with $\pi$; the *formula* has a $2\pi$ in it because the cross-section is round.

## What the cable never sees

Three more places in ordinary transmission-line work where the constant is present in the notation and absent from the physics:

**Reflection.** For a load $Z_L$ on a line $Z_0$, $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$ and $\text{VSWR} = (1+|\Gamma|)/(1-|\Gamma|)$. A 75 Ω load on a 50 Ω line gives exactly $\Gamma = 0.2$ and $\text{VSWR} = 1.5$ — a ratio of two impedances, both of which carry the same $1/2\pi$, so the constant cancels identically.

**The quarter-wave transformer.** To match 50 Ω to 112 Ω, insert a section of impedance $Z_1 = \sqrt{50\times112} = 74.833148$ Ω — pure arithmetic, constant-free — whose *length* is $\lambda/4$: at 1 GHz with VF 0.66, $\lambda = 197.863$ mm and the section is $49.466$ mm. The impedance is $\pi$-free; the length carries the constant because a length is being converted into a number of turns.

**Phase.** The propagation constant is $\beta = 2\pi/\lambda$, so $\pi$ appears in every phase calculation — and cancels in every phase *difference measured in turns*: over one metre at 1 GHz and VF 0.66 the phase advances 5.054001 turns, and the number of turns is $\ell/\lambda$, a pure length ratio. The $2\pi$ is the exchange rate between turns and radians, which is $2\pi$ by definition of the radian.

## What Golden Pi changes: 1/2π becomes √φ/8 exactly

Under $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$ every first-power occurrence of the constant is an algebraic number, because $\hat\pi$ itself is one ($\hat\pi^2 = 16/\varphi$, root of $x^4 + 16x^2 - 256 = 0$). The cable's constant is

$$
\frac{1}{2\hat\pi} \;=\; \frac{1}{2}\cdot\frac{\sqrt\varphi}{4} \;=\; \frac{\sqrt\varphi}{8} \;=\; 0.15900245618925862053\ldots,
\qquad 4096y^4 - 64y^2 - 1 = 0,
$$

a root of that quartic with residual $2.3\times10^{-41}$ at forty digits — where $1/2\pi = 0.15915494309189533577\ldots$ is transcendental by Lindemann (1882), since $\pi$ is. Every dependent quantity then moves by the same relative amount:

| Quantity | $\pi$ | $\hat\pi = 4/\sqrt\varphi$ | Shift |
|---|---|---|---|
| $1/2\pi$ | 0.159154943091895 | $\sqrt\varphi/8 = 0.159002456189259$ | $-0.0958103466\%$ |
| $\sqrt{\mu_0/\varepsilon_0}/2\pi$ | 59.9584916326399 Ω | 59.9010451939795 Ω | $-0.095810\%$ |
| $Z_0$ of a 50 Ω design | 50.0000000 Ω | 49.9520948 Ω | $-0.095810\%$ |
| $\ln(D/d)$ for that 50 Ω | 0.833910238 | 0.834709976 | $+0.095902\%$ |
| $D/d$ for that 50 Ω | 2.302304 | 2.304146 | $+0.095902\%$ |
| $D/d$ for 75 Ω | 3.493365 | 3.497558 | $+0.095902\%$ |
| $\Gamma$ (75 Ω load on 50 Ω) | 0.200000 | 0.200460 | $+0.2300\%$ |
| VSWR | 1.500000 | 1.501439 | $+0.0959\%$ |

Two things are worth separating in that table. The shifts are not independent — a single relabelling of the radian drives all of them, $+0.0959022309\%$ on every quantity carrying the constant to the first power and $-0.0958103466\%$ on every reciprocal. And the *product* $L'C'$ does not appear in the table at all, because $\mu\varepsilon$ is not a function of the circle constant under either label: $\hat\pi$ changes the number attached to a turn, not the physics of a dielectric. If a golden-$\pi$ engineer builds the same cable, the cable is the same cable; only the printed impedance changes, to $49.952$ Ω.

The $\Gamma$ entry deserves its $+0.23\%$: $\Gamma$ is a ratio, so it should cancel — but here the *load* (75 Ω, a real resistor) is held fixed while the line's impedance is recomputed. The mismatch deepens because the golden label makes the 50 Ω cable slightly "larger" in impedance terms relative to a fixed 75 Ω. Change the load too, and $\Gamma$ returns to exactly $0.2$.

## Can a cable arbitrate? No — and the reason is geometric

The tempting experiment: measure $Z_0$ to a part in a thousand and read off $\pi$. It fails, and the failure is instructive rather than merely quantitative.

What a cable measurement actually returns is $C'$ and $L'$ — from an LCR bridge over a cut length, or from a time-domain reflectometer step, which returns $\sqrt{L'/C'}$ directly. Both routes terminate in the same place: $Z_0 = (1/2\pi)\sqrt{\mu/\varepsilon}\ln(D/d)$ contains **two** unknowns besides the constant. A measured 50.000 Ω is exactly reproduced by $(\pi, \ln = 0.833910)$ and by $(\hat\pi, \ln = 0.834710)$. Dimensional metrology cannot break the tie either — $D/d$ is measurable, but it sits inside a logarithm, so a $0.0959\%$ error in the ratio enters the impedance as one part in 1043, which is the same size as the effect being sought.

The decisive number is the dielectric. Absorbing the golden gap in an impedance measurement requires $\varepsilon_r$ to be known to $0.192\%$ ($2.25 \to 2.25432$). Solid polyethylene is specified as 2.25–2.26 and varies by a few tenths of a percent between batches, grades and temperatures; foam dielectrics vary more. The material uncertainty is roughly twice the effect, and unlike a constant of nature it cannot be removed by better instruments, only by a different material.

So the cable joins the growing list of structures that are *blind by construction*: nothing in it converts a circumference into a number that survives. What survives is a product, and a product of a capacitance and an inductance is a dielectric constant and a speed — quantities in which the circle constant has already cancelled against itself. The $2\pi$ was never measured here. It was **computed** into the cross-section, twice, in opposite directions, and then taken back out.

## Further Reading

- [The Solid Angle: How the Sphere's 4π Steradians Compute the Circle Constant](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — why the $4\pi$ of a full sphere is an integral of a sine, and what a measure of directions costs.
- [Stokes' Law: Why the Drag on a Sphere Is 6πμav](/blog/posts/2026-10-31-stokes-law-drag-sphere-6pi-viscosity-golden-pi/) — the same accountants' trick at a different scale: two powers of $\pi$ from pressure, four from shear, and a drag coefficient that holds none.
- [The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass Forever](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — the degree count that makes $(1/2\pi)$ transcendental and $(1/2\hat\pi)$ algebraic.
- [Fraunhofer Diffraction: Why a Slit Writes sinc(πa sinθ/λ)](/blog/posts/2026-10-23-fraunhofer-diffraction-sinc-airy-pattern-circle-constant-golden-pi/) — where the constant enters through $k = 2\pi/\lambda$ and cancels at every zero.
- [The Poisson Kernel: How the Circle Averages a Harmonic Function](/blog/posts/2026-10-19-poisson-kernel-mean-value-property-circle-constant-golden-pi/) — $\pi$ as the total measure of a rim, used once as a normalising divisor.
