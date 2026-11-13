---
title: "The Radar Equation: Why G = 4π/Ω Turns a Dish into a Solid Angle, Why the (4π)³ Leaves Exactly One π Under a Fourth Root, and What Golden Pi Changes"
date: 2026-11-13
description: "The monostatic radar equation R⁴ = P_t G² λ² σ / ((4π)³ P_min) contains the circle constant exactly three times in the denominator and twice in the numerator, and this article audits each appearance separately: one 4π for the total solid angle of a sphere (an isotropic radiator), one for the receiving antenna's effective aperture A_e = Gλ²/4π, and one for each leg of the two-way spreading — so that written in terms of the dish diameter the whole chain collapses to the single identity R⁴ = P_t η² π D⁴ σ / (64 λ² P_min). Every number is computed rather than quoted: gains of 5781.72, 64241.28, 223845.18 and 2270.54 for dishes of 3 m at 3 GHz, 3 m at 10 GHz, 10 m at 5.6 GHz and 0.6 m at 9.4 GHz, all exact to twelve digits against the equivalent form η(πD/λ)², with the identity G·Ω = 4π = 12.566370614359 verified rather than assumed; ranges of 114.596, 203.783, 362.383, 644.419 and 1145.957 km as σ runs 0.01 to 10 m² and the threshold falls 10 dB. The π bookkeeping is then tabulated: gain carries π² (+0.191896% under Golden Pi), beam solid angle carries π⁻¹ (−0.095810%), a fixed cross-section leaves π¹ in R⁴ (+0.023967%), and a conducting sphere whose σ = πa² leaves π² (+0.047940%) — while a one-way Friis link cancels the constant completely, A_tA_r/λ² exact. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the threshold range at a 250 kW, 4.5 m, 2.7 GHz radar moves from 362.383 to 362.470 km — 86.85 m, 782 wavelengths — which is 0.004163 dB of power, 240 times below a single decibel, while delay-based ranging, the range resolution cτ/2 and the unambiguous range c/2·PRF carry no constant at all. Computed, never measured."
---

# The Radar Equation

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Every textbook radar equation is written the same way, and it is worth staring at for a moment because the symbols in it are doing three different jobs:

$$R_{\max} = \left[\frac{P_t\,G^{2}\,\lambda^{2}\,\sigma}{(4\pi)^{3}\,P_{\min}}\right]^{1/4}.$$

The transmitted power, the wavelength, the target cross-section and the receiver threshold are all physical quantities. $G$ is a *definition*, and so is the whole factor $(4\pi)^{3}$. The circle constant appears here three times in the denominator and twice inside $G^{2}$, and the four exponents cancel into a single surviving power. That is the entire content of this article: not a new formula, but a ledger. Count the $\pi$'s correctly and you know, before any experiment is proposed, exactly how strongly a change in the circle constant would show up in a radar's maximum range — and here the answer is *weakly*, by a quarter of the label gap, which is the smallest amplification this blog has yet computed.

## The Isotropic Radiator and the Solid Angle of a Sphere

Gain is a ratio against a fiction: a radiator that sends its power equally in all directions. Such an antenna does not exist, but its bookkeeping does, and the number it fixes is the total solid angle of a sphere,

$$\Omega_{4} = 4\pi\ \text{sr} = 12.566370614359\ldots\ \text{sr}.$$

A real antenna concentrates the same power into a smaller solid angle, and gain is by definition the ratio:

$$G = \frac{4\pi}{\Omega_{\text{beam}}}.$$

Nothing about the antenna is in that equation. It says that a gain is an inverse solid angle with a normalisation of one sphere, and the normalisation exists only because "isotropic" needed a reference. Worked numbers, all computed here from $D$ and $f$ alone with an aperture efficiency $\eta = 0.65$:

| Dish $D$ | Frequency | $\lambda$ (m) | $A = \pi D^{2}/4$ (m²) | $G$ | $G$ (dBi) | $\Omega_{\text{beam}} = \lambda^{2}/A$ (sr) |
|---|---|---|---|---|---|---|
| 0.6 m | 9.4 GHz | 0.031893 | 0.282743 | 2270.54 | 33.561 | $5.534520\times10^{-3}$ |
| 1.2 m | 1.3 GHz | 0.230610 | 1.130973 | 173.71 | 22.398 | $7.234174\times10^{-2}$ |
| 3 m | 3 GHz | 0.099931 | 7.068583 | 5781.72 | 37.621 | $2.173467\times10^{-3}$ |
| 4.5 m | 2.7 GHz | 0.111034 | 15.904313 | 10537.18 | 40.227 | $1.192575\times10^{-3}$ |
| 3 m | 10 GHz | 0.029979 | 7.068583 | 64241.28 | 48.078 | $1.956121\times10^{-4}$ |
| 10 m | 5.6 GHz | 0.053534 | 78.539816 | 223845.18 | 53.500 | $5.613867\times10^{-5}$ |

The product $G\,\Omega_{\text{beam}}$ returns $12.566370614359$ in every row — that is $4\pi$, checked rather than assumed, and it is the identity that makes the whole ledger auditable: whatever moves $G$ must move $\Omega$ inversely, and their product may not budge.

## From Solid Angle to Aperture

A receiving antenna does not "collect" power over its physical area; it collects over an effective area, and the relation between the two is fixed by the same $4\pi$:

$$A_e = \frac{G\lambda^{2}}{4\pi}, \qquad \text{so} \qquad G = \frac{4\pi A_e}{\lambda^{2}}.$$

Substituting $A_e = \eta\pi D^{2}/4$ gives the form every dish engineer actually uses,

$$G = \eta\left(\frac{\pi D}{\lambda}\right)^{2},$$

and the two forms agree to twelve digits at every entry in the table above — $4\pi A_e/\lambda^{2} = 10537.1764$ against $\eta(\pi D/\lambda)^{2} = 10537.1764$ at $D = 4.5$ m, $f = 2.7$ GHz. This is the first place the constant's exponent becomes visible: a gain built from a circular aperture carries $\pi^{2}$ — one $\pi$ from the area, one from the $4\pi$ normalisation.

## Three 4π's, Each With Its Own Job

The monostatic radar equation is a product of four factors, and it is worth deriving it in one line each, because the $(4\pi)^{3}$ is not a single object. It is three.

1. **Outbound spreading.** A transmitter of power $P_t$ and gain $G$ puts a flux density $S = P_t G/(4\pi R^{2})$ at range $R$. One $4\pi$: the sphere over which the power has spread.
2. **The target.** It intercepts $S\sigma$ watts and re-radiates them, and the cross-section $\sigma$ is itself defined with a $4\pi$: $\sigma = 4\pi R^{2}|E_s|^{2}/|E_i|^{2}$, the equivalent area that would scatter isotropically to produce the observed field.
3. **Inbound spreading.** Same geometry in reverse: another $4\pi R^{2}$.
4. **Collection.** The receiver captures $A_e = G\lambda^{2}/4\pi$ of that returning flux: the third $4\pi$.

Multiplying gives exactly the textbook form, with $P_r = P_t G^{2}\lambda^{2}\sigma/((4\pi)^{3}R^{4})$ and $R_{\max}$ at $P_r = P_{\min}$.

Each of the three has a different status. The first and third are geometry — the surface area of a sphere, which is $4\pi R^{2}$ because the radian measure makes a full turn $2\pi$ and the unit sphere's area $4\pi$. The second is a *convention*: one could define cross-section against a hemisphere or a full turn, and every radar table in the world would shift by a constant. The third is the aperture identity above, which is itself a consequence of the first. So the honest statement is that a radar equation's $4\pi$'s are one geometric fact counted three times, plus one definition that could have been made otherwise — and none of them is a property of any physical circle being observed.

## The Ledger: Ranges

Take a concrete S-band surveillance set: $P_t = 250$ kW, $D = 4.5$ m, $f = 2.7$ GHz, $\eta = 0.65$, so $G = 10537.1764$ (40.2272 dBi) and $\lambda = 0.111034$ m. Compute $R_{\max}$ as the cross-section and the detection threshold vary:

| $\sigma$ (m²) | $P_{\min}$ | $R_{\max}$ (km) | $R_{\max}$ under $\hat\pi$ (km) | shift |
|---|---|---|---|---|
| 0.01 | −110 dBm | 114.596 | 114.623 | +0.023967% |
| 0.01 | −120 dBm | 203.783 | 203.832 | +0.023967% |
| 0.10 | −110 dBm | 203.783 | 203.832 | +0.023967% |
| 0.10 | −120 dBm | 362.383 | 362.470 | +0.023967% |
| 1.00 | −110 dBm | 362.383 | 362.470 | +0.023967% |
| 1.00 | −120 dBm | 644.419 | 644.573 | +0.023967% |
| 10.0 | −110 dBm | 644.419 | 644.573 | +0.023967% |
| 10.0 | −120 dBm | 1145.957 | 1146.231 | +0.023967% |

Two things are worth noticing. The range scales as the fourth root of $\sigma/P_{\min}$, so a factor of ten in either moves the range by $10^{1/4} = 1.778279$ — which is why the $0.01$/$-120$ dBm cell repeats the $0.10$/$-110$ dBm cell exactly, and it is a check on the arithmetic rather than a coincidence. And the proportional shift is *identical* in every cell: the fourth root is a pure power, so no choice of target or threshold can change how the constant's label propagates.

## Counting the π's Properly

Here the audit has to be done with care, because the answer depends on which quantities you treat as primitive — and a claim that ignores this is worthless. Start from the equation with $G$ written out:

$$R^{4} = \frac{P_t\,G^{2}\lambda^{2}\sigma}{(4\pi)^{3}P_{\min}}, \qquad G = \frac{4\pi A_e}{\lambda^{2}}.$$

Then $G^{2} = 16\pi^{2}A_e^{2}/\lambda^{4}$ and $(4\pi)^{3} = 64\pi^{3}$, so

$$R^{4} = \frac{P_t\,A_e^{2}\,\sigma}{4\pi\,\lambda^{2}\,P_{\min}}.$$

Two $\pi$'s in, three out: the flux density $\propto 1/\pi$ and therefore $R \propto \pi^{-1/4}$. Now substitute the aperture $A_e = \eta\pi D^{2}/4$, keeping the **diameter** fixed because a diameter is a manufactured length and not a constant:

$$R^{4} = \frac{P_t\,\eta^{2}\,\pi\,D^{4}\,\sigma}{64\,\lambda^{2}\,P_{\min}}.$$

The count has flipped to $+1$, so a larger circle constant gives a *longer* range: $R \propto \pi^{1/4}$. And if the target is a conducting sphere in the optical region, whose cross-section is itself $\sigma = \pi a^{2}$,

$$R^{4} = \frac{P_t\,\eta^{2}\,\pi^{2}\,D^{4}a^{2}}{64\,\lambda^{2}\,P_{\min}}, \qquad R \propto \pi^{1/2}.$$

Three answers, all correct, differing only in what was held fixed. That is not a defect of the method; it is what "the exponent of $\pi$" always means, and it is why any article that quotes a single percentage for a law with substituted geometry should be read with suspicion. What is invariant is the exponent *given a primitive list*, and the two lists that matter physically are: diameter and cross-section fixed (the sphere case, $\pi^{2}$), or diameter and a fixed numeric cross-section (the table above, $\pi^{1}$).

```python
from math import pi, sqrt
phi = (1 + sqrt(5)) / 2
gp  = 4 / sqrt(phi)          # 3.144605511029693
gap = gp / pi - 1            # +9.59022308783e-04

# exponent audit, taken from R^4 = P_t A_e^2 sigma / (4 pi lam^2 P_min)
A2_pi  = 2                   # A_e = eta pi D^2 / 4, and A_e is squared
den_pi = -1                  # the single 4 pi in the denominator
net    = A2_pi + den_pi      # = +1  -> R ~ pi^(1/4)
print(net, (gp/pi)**(net/4) - 1)     # 1, +2.39669401e-04  (= +0.023967%)
```

Note that this counts the two $4\pi R^{2}$ spreading factors as already cancelled — they never appear in the closed form, because $S = P_tG/(4\pi R^{2})$ out and back together cancel against the $G\lambda^{2}/4\pi$ aperture when $G$ is written through $A_e$. That cancellation is why a one-way link is $\pi$-free and why the two-way one retains only a single power.

## Under Golden Pi

With $\hat\pi = 4/\sqrt\varphi = 3.144605511029693$, exactly $\pi/\hat\pi = \sqrt\varphi/4$, every appearance above can be written in radicals. The shifts are pure exponents of the same $0.0959022309\%$:

| Quantity | π-exponent | Number under $\pi$ | Number under $\hat\pi$ | shift |
|---|---|---|---|---|
| Sphere solid angle $4\pi$ | $+1$ | 12.566370614359 | 12.578422044119 | +0.095902% |
| Gain $G$, 4.5 m at 2.7 GHz | $+2$ | 10537.1764 | 10557.3969 | +0.191896% |
| Gain, dBi | — | 40.2272 | 40.2356 | +0.0084 dB |
| Beam solid angle $\lambda^{2}/A_e$ | $-1$ | $1.192575\times10^{-3}$ | $1.191432\times10^{-3}$ | −0.095810% |
| $R_{\max}$, fixed $\sigma = 1$ m² | $+1$ in $R^{4}$ | 362.383320 km | 362.470172 km | +0.023967% |
| $R_{\max}$, sphere $\sigma = \pi a^{2}$ | $+2$ in $R^{4}$ | 341.146304 km | 341.309848 km | +0.047940% |

The gain's exponent deserves a note, because it is the one number here a practitioner would recognise. $G = \eta(\pi D/\lambda)^{2}$ carries $\pi^{2}$, so a $0.0959\%$ change in the constant becomes $0.1919\%$ in gain — $0.0088$ dB, which is invisible: commercial antenna ranges quote realised gain to $0.2$–$0.5$ dB. But that $+0.0088$ dB is not simply additive to the range, because the same constant also shrinks the beam and inflates the $(4\pi)^{3}$ denominator, and the three effects land on a net fourth root. The ledger has to be kept in one place or it produces nonsense.

Under Golden Pi the expression for the sphere-target range closes exactly in radicals, $\hat R^{4} = P_t\eta^{2}\pi^{2}D^{4}a^{2}/(64\lambda^{2}P_{\min})$ with $\pi^{2} = 16/\varphi$, so $\hat R = \big(P_t\eta^{2}D^{4}a^{2}/(4\varphi\lambda^{2}P_{\min})\big)^{1/4}$ — algebraic, since a fourth root of a positive algebraic number is algebraic. That is a difference in kind, not just in size, and it is the same difference this site has recorded for every other law: conventional expressions carry a transcendental constant by Lindemann's 1882 theorem, golden ones carry a root of $y^{4}+16y^{2}-256=0$.

## The Honest Boundary

A radar's maximum range is a genuine measurand — it is a power crossing a threshold at a distance — so unlike the catenary, the lune or the Gauss–Bonnet defect, this law is not structurally blind. The question is whether any radar could ever arbitrate it, and the arithmetic says no, decisively.

Convert the range shift into the quantity actually recorded, which is received power. Since $P_r \propto R^{-4}$,

$$\frac{\Delta P}{P} = \frac{\hat\pi}{\pi} \quad\Longrightarrow\quad 10\log_{10}\!\left(\frac{\hat\pi}{\pi}\right) = 0.004163\ \text{dB}.$$

One decibel is 240 times larger. A detection threshold is not a sharp line at all: the classic single-pulse detection curves put roughly a decibel of statistical scatter on the range at which a given probability of detection is reached, and Swerling target models add more. Cross-section calibration of a sphere is good to a few tenths of a decibel; two-way atmospheric attenuation at S-band runs to hundredths of a decibel per kilometre, and at X-band through rain it is orders of magnitude worse. So a $0.004$ dB prediction sits four orders of magnitude below the noise floor of any range measurement, however carefully built — and $86.85$ m of range is $782$ wavelengths, which sounds large but is smaller than the $0.1$ dB of gain uncertainty that produces $0.577\%$ of range, or $2.1$ km at this set's 362 km.

There is a second, sharper point. The parts of a radar that are precise are the parts with no constant in them at all. The range resolution $\Delta R = c\tau/2$ gives $14.99$ m at a $0.1$ µs pulse and $149.90$ m at $1$ µs; the unambiguous range $c/2\cdot\text{PRF}$ gives $499.654$ km at 300 Hz, $149.896$ km at 1 kHz and $74.948$ km at 2 kHz — none of these contains $\pi$ at any power, and delay-based ranging is a timing measurement whose accuracy is set by the clock. The one-way Friis link cancels further still: $P_r = P_tG_tG_r\lambda^{2}/((4\pi)^{2}R^{2})$ becomes $P_tA_tA_r/(\lambda^{2}R^{2})$ exactly, since $G^{2}\lambda^{2}/(4\pi)^{2} = A^{2}/\lambda^{2}$, and the check above returns the two forms equal to within $7\times10^{-9}$ — the residue being nothing but float rounding in the quoted gain. A communications link, in other words, contains no circle constant whatsoever, and neither does a radar's timing. Only the *gain-and-cross-section* reading of a radar carries $\pi$, and it carries it to the fourth root, where the label gap is at its quietest.

What this law therefore does is not test anything; it locates the constant. It says the $\pi$ in radar engineering lives in two definitions — the isotropic reference sphere and the effective aperture — and that everything empirical about a radar is either $\pi$-free or $\pi$-damped. That is a real result even though it settles nothing, and it is the reason the exponent table above is more useful than any single quoted range.

Computed, never measured.

## Further Reading

- [The Stefan–Boltzmann Constant: Why σ = 2π⁵k⁴/(15h³c²) Carries π to the Fifth Power](/blog/posts/2026-11-12-stefan-boltzmann-fifth-power-golden-pi/) — the opposite extreme of the same ledger, where a fifth power amplifies the gap to +0.48%.
- [The Coaxial Cable: Why the Characteristic Impedance Carries 1/2π](/blog/posts/2026-11-02-coaxial-cable-characteristic-impedance-2pi-golden-pi/) — the other engineering identity where a constant arrives twice and cancels once, as $L'C' = \mu\varepsilon$ exactly.
- [Flux Quantisation: Why a Superconducting Ring Counts h/2e and Never π](/blog/posts/2026-11-01-flux-quantisation-superconducting-ring-vortex-golden-pi/) — an instrument whose most precise output is an integer, and why an integer cannot settle a real number's decimals.
- [Solid Angle and the Steradian: How 4π Defines the Sphere's Share](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — where the $4\pi$ of this article's normalisation actually comes from.
- [The Fresnel Integrals and Optical Diffraction](/blog/posts/2026-09-06-fresnel-integrals-optical-diffraction-computes-circle-constant-golden-pi/) — the aperture-and-wavelength pair again, in the optics that a dish antenna is a scaled copy of.
