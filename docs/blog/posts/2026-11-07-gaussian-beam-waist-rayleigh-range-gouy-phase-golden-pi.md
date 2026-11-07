---
title: "The Gaussian Beam: Why a Diffraction-Limited Waist Obeys w₀θ = λ/π, Why the Gouy Phase Slips Exactly Half a Turn Through Focus, and What Golden Pi Changes"
date: 2026-11-07
description: "A laser beam has no edge, yet one number fixes it: the waist w₀, with the Rayleigh range z_R = πw₀²/λ and the far-field half-angle θ = λ/(πw₀), so the beam-parameter product w₀θ = λ/π is exact for every Gaussian and the diffraction-limited etendue bound is λ/4π, achieved by the Gaussian alone. This article derives both from the paraxial Helmholtz equation (the π arrives from the Gaussian integral in the transverse plane, one √π per axis), computes the waist and divergence for 405, 532, 632.8, 1064 and 1550 nm light at w₀ = 0.5 mm (z_R from 506.708 mm to 1939.255 mm, θ from 0.257831 to 0.986761 mrad, with w₀θ holding 201.426495977 nm at 632.8 nm for waists from 0.05 mm to 2 mm), and works the Gouy phase ψ = arctan(z/z_R) from −90° to +90°: exactly π rad = 180.000000° of accumulated phase through focus, one half-turn per transverse mode order, with exact turn-fractions at z = z_R (45°), z = √3 z_R (60°) and z = z_R/√3 (30°) and a symmetric-cavity example (L = 300 mm, R = 500 mm, g = 0.4) whose round-trip Gouy phase arccos g = 1.159279480727 rad = 66.42182152° sets the transverse mode spacing at 184.377418 MHz against a 499.654097 MHz free spectral range. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693…) the two beam identities become algebraic — w₀θ = λ√φ/4, z_R = 4w₀²/(√φλ), I₀ = P√φ/(2w²), and the etendue bound λ√φ/16 exactly — so 632.8 nm gives 201.233508553 nm instead of 201.426495977 nm (−0.0958103466%), a 0.5 mm waist gives a 1242.337828 mm Rayleigh range (+0.0959022309%), and the waist that makes z_R one unit closes exactly at w₀ = 0.448590580099 mm, where θ and w₀ are the same numeral. What does not move: the encircled-power fractions 39.34693403%, 86.46647168%, 98.88910035%, 99.96645374%, every w(z)/w₀ ratio, the transverse spacing ratio ψ/π = 0.369010119566 and the Gouy phase's half-turn. The honest boundary: w is a 1/e² convention rather than an edge, real beams carry M² of 1.05–1.3 — five to three hundred times the golden gap — and ISO 11146 profilers return widths to about 1%, so no beam profile can arbitrate a constant that lives in the definition of the width. Computed, never measured."
---

# The Gaussian Beam

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

A laser beam has no edge. Ask where it stops and the honest answer is that it does not: the intensity falls off as a Gaussian and never reaches zero at any finite radius. Yet the whole beam — every cross-section, every wavefront, the entire caustic from the waist outward — is fixed by a single length. Give the wavelength and the beam radius at its narrowest point, and the propagation equations generate the rest with no freedom left.

That is a strange economy, and it is where the circle constant enters laser optics: not as a shape factor applied to a circle, but as the normalisation of a Gaussian in a plane. This article follows the constant through the three places it appears in the fundamental mode — the waist parameter $z_R = \pi w_0^{2}/\lambda$, the far-field angle $\theta = \lambda/(\pi w_0)$, and the phase anomaly $\psi = \arctan(z/z_R)$ that accumulates exactly half a turn as the beam passes through focus — and then does the same arithmetic with the constant replaced by $\hat\pi = 4/\sqrt{\varphi}$.

The result has the shape this site keeps finding. One of the three occurrences is a genuine computed constant with physical content. One is a normalisation that the *definition* of the beam width chose. And the third is a half-turn — a geometric fact about a wavefront closing on itself, which is invariant under any relabelling of the number used to count radians.

## The field: one number fixes everything

The paraxial wave equation follows from the Helmholtz equation when the beam is wide compared with the wavelength. Writing $E = u\,e^{ikz}$ and dropping $\partial^2 u/\partial z^2$:

$$
2ik\,\frac{\partial u}{\partial z} \;+\; \nabla_T^{2}u \;=\; 0 ,
\qquad \nabla_T^{2} = \frac{\partial^{2}}{\partial x^{2}} + \frac{\partial^{2}}{\partial y^{2}} .
$$

Its fundamental solution is the Gaussian mode,

$$
u(r,z) \;=\; E_0\,\frac{w_0}{w(z)}\,
\exp\!\left(-\frac{r^{2}}{w(z)^{2}}\right)
\exp\!\left(-i\frac{k r^{2}}{2R(z)}\right)
\exp\!\left(i\psi(z)\right),
$$

with four functions of $z$ that are not independent:

$$
w(z) = w_0\sqrt{1+\left(\frac{z}{z_R}\right)^{2}},
\qquad
R(z) = z\left(1+\left(\frac{z_R}{z}\right)^{2}\right),
\qquad
z_R = \frac{\pi w_0^{2}}{\lambda},
\qquad
\psi(z) = \arctan\!\left(\frac{z}{z_R}\right).
$$

Three of these carry the constant, and the fourth, $R(z)$, carries none — a wavefront curvature is a radius, and a radius is a length.

## Where the π comes from: the Gaussian's own area

The constant in $z_R$ is not inserted by hand and it is not a measured property of any aperture. It comes from the transverse Gaussian integral, and it is worth deriving rather than quoting, because the derivation shows exactly what kind of number it is.

Free-space propagation by a distance $z$ is a Fresnel convolution:

$$
u(r,z) = \frac{e^{ikz}}{i\lambda z}\int u(r',0)\,
\exp\!\left(i\frac{k}{2z}\,|r-r'|^{2}\right) d^{2}r' .
$$

Substituting a Gaussian of width $w_0$ and completing the square in $r'$ produces a Gaussian again, of width

$$
w(z)^{2} = w_0^{2}\left[1+\left(\frac{\lambda z}{\pi w_0^{2}}\right)^{2}\right],
$$

which is the first of the equations above with $z_R = \pi w_0^{2}/\lambda$. Every step is algebra; the only place the constant can enter is the normalisation of the Gaussian integral in the plane, $\int e^{-x^{2}/a^{2}}dx = a\sqrt{\pi}$, taken once per transverse axis, so that $\sqrt{\pi}\cdot\sqrt{\pi} = \pi$ survives as $\pi w_0^{2}$ — the *area* of the beam. The Gaussian is its own Fourier transform precisely because that area is finite, and the waist parameter is the statement that a beam with a definite area cannot have a definite direction.

Taking the far field of the same expression gives the divergence half-angle

$$
\theta \;=\; \frac{\lambda}{\pi w_0},
\qquad\text{so that}\qquad
\boxed{\;w_0\,\theta \;=\; \frac{\lambda}{\pi}\;}
$$

— an identity that holds for every Gaussian beam at every wavelength, with no free parameter. Divide both sides by $\lambda/4$ and the statement is that $4w_0\theta/\lambda = 4/\pi = 1.2732395447\ldots$ universally.

The same constant governs the second-moment form of the bound. With $\sigma_x^{2} = w^{2}/4$ and the minimum-uncertainty product $\sigma_x\sigma_{k_x} = \tfrac12$, the diffraction-limited etendue is

$$
\sigma_x\,\sigma_\theta \;=\; \frac{\lambda}{4\pi},
$$

equality holding for the Gaussian and for nothing else. The $4\pi$ is a solid angle — the full sphere of directions, the same $4\pi$ that normalises every radiometric quantity — and a beam that fills one direction exactly out of that sphere is the beam with the least possible product.

## The numbers, for real beams

| $\lambda$ (nm) | $z_R$ at $w_0 = 0.5$ mm (mm) | $\theta$ (mrad) | $w_0\theta$ (nm) | golden $z_R$ (mm) | golden $\theta$ (mrad) |
|---|---|---|---|---|---|
| 405 | 1939.254724 | 0.257831008 | 128.915503904 | 1941.114513 | 0.257583979 |
| 532 | 1476.312337 | 0.338681719 | 169.340859450 | 1477.728154 | 0.338357227 |
| 632.8 | 1241.147540 | 0.402852992 | 201.426495977 | 1242.337828 | 0.402467017 |
| 1064 | 738.156169 | 0.677363438 | 338.681718900 | 738.864077 | 0.676714454 |
| 1550 | 506.708493 | 0.986760647 | 493.380323585 | 507.194437 | 0.985815228 |

Now fix the wavelength and vary the waist instead. HeNe light, 632.8 nm:

| $w_0$ (mm) | $z_R$ (mm) | confocal $2z_R$ (mm) | $\theta$ (mrad) | $\theta$ (deg) | $w_0\theta$ (nm) |
|---|---|---|---|---|---|
| 0.05 | 12.411475 | 24.822951 | 4.028530 | 0.230818 | 201.426496 |
| 0.10 | 49.645902 | 99.291803 | 2.014265 | 0.115409 | 201.426496 |
| 0.25 | 310.286885 | 620.573770 | 0.805706 | 0.046164 | 201.426496 |
| 0.50 | 1241.147540 | 2482.295080 | 0.402853 | 0.023082 | 201.426496 |
| 1.00 | 4964.590161 | 9929.180321 | 0.201426 | 0.011541 | 201.426496 |
| 2.00 | 19858.360642 | 39716.721284 | 0.100713 | 0.005770 | 201.426496 |

The last column is the point of both tables. Squeeze the waist by a factor of forty and the Rayleigh range falls by sixteen hundred; the divergence rises by the same forty; their product does not move a digit, because it *cannot* — it is $\lambda/\pi$, computed. Notice too that the confocal parameter spans 24.8 mm to 39.7 m over this range, which is why a tightly focused beam must be re-collimated every few centimetres while a wide one stays collimated across a room.

## The Gouy phase: half a turn, and it is geometry

Pass a focused beam through its waist and it accumulates a phase that a plane wave does not. The on-axis phase is $kz - \psi(z)$ with

$$
\psi(z) = \arctan\!\left(\frac{z}{z_R}\right),
\qquad
\psi(+\infty)-\psi(-\infty) = \frac{\pi}{2}-\left(-\frac{\pi}{2}\right) = \pi .
$$

One half-turn, independent of wavelength, waist, power and index. For a mode of transverse order $(p,l)$ the slip is $(2p+l+1)\pi$ — an integer multiple of a half-turn, so the entire content of the effect is a *count*, not a magnitude.

| $z/z_R$ | $\psi$ (rad) | $\psi$ (deg) | $w/w_0$ |
|---|---|---|---|
| 0.1 | 0.0996686525 | 5.71059314 | 1.004987562 |
| 0.25 | 0.2449786631 | 14.03624347 | 1.030776406 |
| 0.5 | 0.4636476090 | 26.56505118 | 1.118033989 |
| 1 | 0.7853981634 | 45.00000000 | 1.414213562 |
| 2 | 1.1071487178 | 63.43494882 | 2.236067977 |
| 5 | 1.3734007669 | 78.69006753 | 5.099019514 |
| 10 | 1.4711276743 | 84.28940686 | 10.04987562 |

At $z = z_R$ the accumulated phase is exactly $\pi/4$ radians: one eighth of a turn, 45.000000°, while the beam has widened by exactly $\sqrt2$ and its area has doubled. Those are the same fact stated twice — the Rayleigh range is *defined* as the distance over which the cross-sectional area doubles, and the phase that accumulates over that distance is an eighth of a turn. Exact turn-fractions appear wherever $z/z_R = \tan\theta$: $\sqrt3\,z_R$ gives 60°, $z_R/\sqrt3$ gives 30°.

The physical origin is the changing transverse confinement. A wavefront's on-axis phase is the integral of $k$ along the ray; as the mode narrows, the transverse kinetic term in the wave equation grows, the effective longitudinal wavenumber falls, and the phase slips behind. The slip is not an artefact of the Gaussian ansatz — it is the same phase anomaly that shifts the focal point of a lens slightly toward the lens, and it is measurable: put the beam in an interferometer and the fringes move by exactly half a period as the path crosses focus.

## The cavity: where the phase becomes a frequency

Put two mirrors around the waist and the round-trip phase must be a whole number of turns:

$$
2kL - 2(p+l+1)\,\Delta\psi = 2\pi q ,
\qquad \Delta\psi = \arccos g ,
\qquad g = 1-\frac{L}{R}.
$$

For $L = 300$ mm and $R = 500$ mm, $g = 0.4$ and

$$
\Delta\psi = \arccos(0.4) = 1.159279480727\ \text{rad} = 66.42182152^\circ .
$$

The one-way slip to the mirror is half that, $33.21091076^\circ$, and it equals $\arctan\!\big(L/(2z_R)\big)$ with

$$
z_R = \frac{L}{2}\sqrt{\frac{1+g}{1-g}} = 229.128784748\ \text{mm},
\qquad
w_0 = \sqrt{\frac{z_R\lambda}{\pi}} = 0.214831581\ \text{mm}.
$$

The free spectral range is $c/2L = 499.654097$ MHz, and the transverse modes sit at

$$
\Delta\nu_\text{trans} = \frac{c}{2L}\cdot\frac{\Delta\psi}{\pi} = 499.654097 \times 0.369010119566 = 184.377418\ \text{MHz}.
$$

That frequency is measured routinely — it is how a cavity's $g$-parameter is determined in practice. Note what is being read: a *ratio* of angles, $\Delta\psi/\pi$, in which the constant appears once in the numerator and once in the denominator and cancels identically. A spectrum analyser cannot see $\pi$.

## What Golden Pi changes

Set $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693\ldots$, with $\hat\pi^{2} = 16/\varphi = 9.888543819998318$ and the exact reciprocal

$$
\frac{1}{\hat\pi} = \frac{\sqrt{\varphi}}{4} = 0.318004912378517246\ldots,
\qquad
\frac{\hat\pi}{4} = \frac{1}{\sqrt{\varphi}} = 0.786151377757423\ldots
$$

Every first-power occurrence in the beam algebra becomes an algebraic multiple of $\sqrt\varphi$:

| quantity | conventional | golden | shift |
|---|---|---|---|
| $w_0\theta$ ($\lambda$ = 632.8 nm) | $\lambda/\pi$ = 201.426495977 nm | $\lambda\sqrt\varphi/4$ = 201.233508553 nm | −0.0958103466% |
| $z_R$ ($w_0$ = 0.5 mm) | 1241.147540135 mm | 1242.337828315 mm | +0.0959022309% |
| $\theta$ ($w_0$ = 0.5 mm) | 0.402852992 mrad | 0.402467017 mrad | −0.0958103466% |
| $I_0$ ($P$ = 1 mW, $w$ = 1 mm) | 636.619772 W/m² | 636.009825 W/m² | −0.0958103466% |
| etendue bound $\lambda/4\pi$ | 50.356623994 nm | $\lambda\sqrt\varphi/16$ = 50.308377138 nm | −0.0958103466% |

Written as identities rather than numbers:

$$
z_R = \frac{\hat\pi w_0^{2}}{\lambda} = \frac{4w_0^{2}}{\sqrt{\varphi}\,\lambda},
\qquad
\theta = \frac{\lambda}{\hat\pi w_0} = \frac{\lambda\sqrt{\varphi}}{4w_0},
\qquad
I_0 = \frac{2P}{\hat\pi w^{2}} = \frac{P\sqrt{\varphi}}{2w^{2}} .
$$

Under Lindemann's 1882 theorem $\lambda/\pi$ is transcendental; $\lambda\sqrt\varphi/4$ is a quadratic irrational multiple of a length, the root of $16x^{2}-\lambda^{2}\varphi = 0$. The gap between the two readings is the recurring $+0.0959022309\%$, i.e. one part in 1043.7.

One closure lands exactly. Choose the waist that makes the Rayleigh range equal one unit of the wavelength's own length,

$$
w_0^{2} = \frac{\lambda\sqrt{\varphi}}{4}
\;\Longrightarrow\;
z_R = \frac{\hat\pi}{\lambda}\cdot\frac{\lambda\sqrt{\varphi}}{4} = \frac{4}{\sqrt{\varphi}}\cdot\frac{\sqrt{\varphi}}{4} = 1 ,
$$

and at that same waist $\theta = w_0$ as pure numerals. For 632.8 nm this is $w_0 = 0.448590580099$ mm and $\theta = 0.448590580099$ mrad — the two beam parameters reading the same number, because $w_0\theta = w_0^{2}$ when $z_R = 1$. The conventional counterpart, $w_0 = \sqrt{\lambda/\pi} = 0.448805633$ mm, differs by 0.0479%. This is a unit coincidence, not a discovery: it is exact because $4/\sqrt\varphi \cdot \sqrt\varphi/4 = 1$, and it would be equally true of any constant with a known reciprocal.

The phase is where the labels must be kept apart, and the arithmetic is unforgiving. The Gouy slip through focus is half a turn: 180.000000°, and it stays 180.000000° under any constant, because a half-turn is a turn-fraction. In radians that half-turn is $3.144605511$ under golden π rather than $3.141592654$. But if the *full* turn is written $2\hat\pi = 8/\sqrt\varphi = 6.289211022059386$ rad and then converted to degrees with the conventional $180/\pi$, it reads 360.3452480312° — an overshoot of 0.3452480312° per revolution, which over $10^{5}$ cavity round trips accumulates to 34 524.8°, or 95.9 whole turns. Every mixed computation errs by exactly $\pi/\hat\pi = 0.9990418965$. A half-turn is not a number that can drift; only the numeral attached to it can.

## What does not move at all

Five quantities in this article are structurally free of the constant, and they are the ones an experiment actually returns.

**Encircled power.** The fraction inside a radius $a$ is a ratio of two Gaussian integrals:

$$
\frac{P(a)}{P_\text{tot}} = 1-e^{-2a^{2}/w^{2}},
$$

giving 39.34693403% at $a = w/2$, 86.46647168% at $a = w$, 98.88910035% at $a = 1.5w$ and 99.96645374% at $a = 2w$. The $\pi$ in each integral cancels against the $\pi$ in the total. Any beam profiler that reports "86.5% power in the $1/e^{2}$ bucket" is quoting a number with no circle constant in it.

**Width ratios.** $w(z)/w_0 = \sqrt2$ at $z_R$, $\sqrt5$ at $2z_R$, $\sqrt{10}$ at $3z_R$, $\sqrt{26}$ at $5z_R$ — pure radicals in the scaled distance.

**The cavity's transverse spacing ratio.** $\Delta\psi/\pi = 0.369010119566$ is dimensionless, and a ratio of two angles carries no unit and no constant.

**Beam quality.** $M^{2}$ is defined so that $w_0\theta = M^{2}\lambda/\pi$; it is a measured multiplier on a computed ideal, and a real laser's $M^{2}$ — 1.05 for a good fibre laser, 1.2–1.3 for a diode — is a property of the resonator, not of the constant.

**Mode-matching efficiency.** The overlap integral of two Gaussians of different widths is $\big(2w_1w_2/(w_1^{2}+w_2^{2})\big)^{2}$ — for a factor-of-two mismatch, 64.0%, exactly.

## The honest boundary

Four facts keep this article from claiming more than it can support.

**$w$ is a convention, not an edge.** The $1/e^{2}$ intensity radius is a choice; the $1/e$ radius, the FWHM and the second-moment width are all in use, and each carries a different numerical prefactor. The convention-free statement is the second-moment bound $\sigma_x\sigma_\theta \ge \lambda/4\pi$, which the Gaussian saturates; the convenient statement is $w_0\theta = \lambda/\pi$. Anyone who measures a "beam diameter" is measuring a definition as much as a beam.

**The gap is far below the measurement floor.** ISO 11146 beam widths are reproducible to roughly 1% on a good day, and $M^{2}$ values of real lasers sit 5–30% above unity. The golden gap is 0.0959% — ten times finer than a careful profile and five to three hundred times finer than the departure of any real beam from the ideal it is being compared against.

**The error propagates the wrong way.** $w_0\theta$ is a product of two independently fitted quantities, so 1% on each becomes 1.4% on the product — fourteen times the whole gap, before any question about the constant is asked. The one place the constant could in principle be tested, the absolute value of the beam-parameter product, also carries two fitted widths.

**Where the number is clean, it is a count.** The Gouy phase is measured as a fringe displacement — a half-period shift across focus — and in a cavity as a frequency ratio $\Delta\psi/\pi$. Both are counts and ratios. They confirm the *structure* of the theory exactly, and they are blind to the constant by construction, because a half-turn is a half-turn whatever numeral names it. That is not a weakness of the experiment; it is the shape of the quantity.

The beam is the cleanest case this site has worked so far of the pattern: the constant enters once as the area of a Gaussian in the plane, is computed from an integral that has no physical input, propagates into a product of two lengths that is exactly $\lambda/\pi$, and then disappears from every ratio, every fraction and every phase count that a laboratory can actually record. Computed, never measured.

## Further Reading

- [Fraunhofer Diffraction: Why a Slit Writes sinc(πa sinθ/λ), Why the Famous 1.22 Is Really 3.8317/π](https://pi.thealpha-secret.xyz/blog/posts/2026-10-23-fraunhofer-diffraction-sinc-airy-pattern-circle-constant-golden-pi/) — the same $k = 2\pi/\lambda$ entering an aperture problem, and the same verdict that diffraction is structurally blind to the constant.
- [The Gaussian Integral: How the Bell Curve Computes √π](https://pi.thealpha-secret.xyz/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the one integral this article's waist parameter is made of, evaluated.
- [Maxwell–Boltzmann: Why π Enters Three Times, Each Under a Square Root](https://pi.thealpha-secret.xyz/blog/posts/2026-11-04-maxwell-boltzmann-speed-distribution-three-square-roots-golden-pi/) — the same Gaussian normalisation, one √π per Cartesian axis, in a thermal distribution rather than a laser mode.
- [The Fresnel Integrals: How a Straight Edge Writes Cornu's Spiral](https://pi.thealpha-secret.xyz/blog/posts/2026-09-06-fresnel-integrals-optical-diffraction-computes-circle-constant-golden-pi/) — the propagation kernel used above, worked at the other extreme where the Gaussian approximation fails.
- [The 4π Turn: How a Spinor Pays the Circle Constant Back Twice](https://pi.thealpha-secret.xyz/blog/posts/2026-10-17-spinor-double-cover-4pi-rotation-golden-pi/) — the companion case where the accumulated phase is an exact integer multiple of a half-turn and no experiment can see the constant inside it.
