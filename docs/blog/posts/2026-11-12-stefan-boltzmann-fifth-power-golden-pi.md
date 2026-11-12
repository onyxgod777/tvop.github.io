---
title: "The Stefan–Boltzmann Constant: Why σ = 2π⁵k⁴/(15h³c²) Carries π to the Fifth Power — One from the Solid Angle and Four from Euler's ζ(4) — Why Wien's Law Carries None, and What Golden Pi Changes"
date: 2026-11-12
description: "The Stefan–Boltzmann constant σ = 2π⁵k⁴/(15h³c²) = 5.67037441918×10⁻⁸ W m⁻² K⁻⁴ prints the circle constant to the fifth power, and this article separates the five: one power from the 8π = 2 polarisations × 4π steradians in the mode density, four from the Bose integral ∫₀^∞ x³/(eˣ−1)dx = π⁴/15 = Γ(4)ζ(4), which is Euler's Basel problem in disguise. Every piece is recomputed numerically — the whole Stefan integral quadrature returning 5.67037441918×10⁻⁸ with residual −6.8×10⁻⁴⁹, the flux table (CMB 2.7255 K → 3.128934574×10⁻⁶ W m⁻², 300 K → 459.300328, 1000 K → 5.670374419×10⁴, 5772 K → 6.293859247×10⁷), the Sun's luminosity 3.827990903×10²⁶ W from R = 6.957×10⁸ m and T = 5772 K, the photon density 5.477448429×10¹⁴ m⁻³ at 300 K carrying π¹ rather than π⁵, and the mean photon energy 3ζ(4)/ζ(3) = 2.7011780329 kT. Wien's displacement law is then shown to be π-free in every digit: x = 5(1−e^{−x}) at x = 4.965114231744276 gives b = 2.897771955185 m·K and a peak of 103.45619415 GHz/K, and the median photon at x = 1.4000197860 is a pure zeta ratio. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the fifth power turns the 0.0959022309% label gap into +0.4804317606% — σ̂ = 2048 k⁴/(15φ^{5/2}h³c²) = 5.6976166988×10⁻⁸ exactly algebraic where π⁵ is transcendental by Lindemann 1882 — while photon density moves only +0.0959022%, b, every T/T′ ratio and every 2.7011780329 stay identical. The honest boundary: since 2019 the SI fixes k and h exactly, so σ is computed from a definition and can carry no evidence either way."
---

# The Stefan–Boltzmann Constant

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1879 Josef Stefan read off his own experiments that a hot body's radiated power grows as the fourth power of its absolute temperature; in 1884 Ludwig Boltzmann derived the fourth power from thermodynamics alone, and the constant of proportionality came out of Maxwell's radiation pressure as $\sigma = ac/4$. Neither man could compute $a$. That took Planck's 1900 spectral law, and when the dust settled the constant carried the circle constant to the **fifth** power:

$$\sigma = \frac{2\pi^{5}k^{4}}{15\,h^{3}c^{2}} = 5.67037441918\ldots\times10^{-8}\ \text{W m}^{-2}\text{K}^{-4}.$$

Five $\pi$'s is a lot, and it is the reason this law is worth a careful article rather than a passing citation. Every other figure in this blog carries $2\pi$ or $\pi^{2}$ and the interesting question is where the one or two copies sit. Here the exponent itself is a bookkeeping fact that can be audited: **one** power comes from an angular measure, **four** come from a single definite integral — and that integral is Euler's Basel problem wearing a Planck spectrum. Separate the five and you know, without measuring anything, which observable is sensitive to the constant and which is blind to it. That distinction is the whole of the dispute.

## Where the Fifth Power Comes From

Start from the spectral energy density of blackbody radiation in frequency,

$$u(\nu)\,d\nu = \frac{8\pi h\nu^{3}}{c^{3}}\cdot\frac{d\nu}{e^{h\nu/kT}-1}.$$

The prefactor $8\pi$ is pure counting, and it factors immediately:

$$8\pi = \underbrace{2}_{\text{polarisations}}\times\underbrace{4\pi}_{\text{steradians}}.$$

Two independent polarisation states per mode, and a full turn of solid angle, because the modes fill a sphere in wavevector space. That is **one** power of $\pi$, and it enters not from any circle in the geometry of a radiating body but from the fact that a sphere's surface is measured in steradians. The radiator's shape never appears; a cube, a needle and a dust grain all emit the same spectrum. A sphere enters only as the space of directions, which is why a single power of $\pi$ — not two, not $4\pi$ left dangling — is the right count.

Now substitute the dimensionless variable $x = h\nu/kT$, so that $d\nu = (kT/h)\,dx$:

$$u = \frac{8\pi h}{c^{3}}\left(\frac{kT}{h}\right)^{4}\int_{0}^{\infty}\frac{x^{3}\,dx}{e^{x}-1}.$$

Everything thermal is now in $(kT)^{4}$; everything constant is in the prefactor; and everything hard is in the integral. Note that the substitution is the whole trick: the exponent 4 on temperature and the exponent 4 on $\pi$ are the *same* exponent, because both come from the cubic measure $\nu^{3}d\nu$ being rewritten in $x$. This is the structural reason the two are tied together, and it is the reason an error in the constant propagates to the fifth power into $\sigma$.

## The Bose Integral Behind the π⁴

The integral is elementary only in the sense that its value is known:

$$\int_{0}^{\infty}\frac{x^{3}\,dx}{e^{x}-1} = \Gamma(4)\,\zeta(4) = 6\cdot\frac{\pi^{4}}{90} = \frac{\pi^{4}}{15}.$$

Expanding $1/(e^{x}-1) = \sum_{n\ge1}e^{-nx}$ and integrating term by term gives $\sum 6/n^{4} = 6\zeta(4)$, and Euler's 1735 evaluation $\zeta(4) = \pi^{4}/90$ supplies the four powers at once. So the fifth power of $\pi$ in $\sigma$ decomposes exactly as

$$\pi^{5} = \underbrace{\pi}_{\text{2 pol.}\times 4\pi\ \text{sr}}\times\underbrace{\pi^{4}}_{\zeta(4)=\pi^{4}/90},$$

or, in the assembled constant, $\sigma = \left(\tfrac{8\pi}{4}\right)\left(\tfrac{\pi^{4}}{15}\right)\tfrac{k^{4}}{h^{3}c^{2}} = \tfrac{2\pi^{5}}{15}\tfrac{k^{4}}{h^{3}c^{2}}$, where the division by 4 is the $c/4$ of the flux through a surface.

Check the numbers. Computed in `mpmath` at forty digits:

```python
from mpmath import mp, mpf, pi, quad, exp
mp.dps = 40
k, h, c = mpf('1.380649e-23'), mpf('6.62607015e-34'), mpf('299792458')

I = quad(lambda x: x**3/(exp(x)-1), [0, mp.inf])
print(I, pi**4/15)                 # 6.493939402266829149096022179247007416648
                                   # 6.493939402266829149096022179247007416649

sigma = 2*pi**5*k**4/(15*h**3*c**2)
print(sigma)                       # 5.67037441918442945397099673188923087584e-8

sig_num = 2*pi/(h**3*c**2)*k**4*I  # the whole law from first principles
print(sig_num - sigma)             # -6.8e-49
```

The quadrature residual is $-6.8\times10^{-49}$ at forty-digit working precision: the closed form and the integral are the same number, so the four powers of $\pi$ in $\zeta(4)$ are not an approximation to anything — they *are* the integral. The value $5.670374419184429\ldots\times10^{-8}$ agrees with the CODATA figure $5.670374419\times10^{-8}$, which is not a coincidence and not a confirmation: since the 2019 revision of the SI, $k$ and $h$ are exact by definition, so that tabulated number is computed from the formula above with the conventional $\pi$. It is a definition, not a measurement, and we return to that at the end.

## Assembling the Constant

With $\sigma$ in hand the rest of the radiation constants follow by multiplication and division, and their $\pi$-powers are worth tabulating because they differ:

| Quantity | Formula | Value | Power of π |
|---|---|---|---|
| Stefan–Boltzmann | $\sigma = 2\pi^{5}k^{4}/(15h^{3}c^{2})$ | $5.67037441918\times10^{-8}$ W m⁻²K⁻⁴ | 5 |
| Radiation constant | $a = 4\sigma/c = 8\pi^{5}k^{4}/(15h^{3}c^{3})$ | $7.56573325028\times10^{-16}$ J m⁻³K⁻⁴ | 5 |
| Energy density | $u = aT^{4}$ | $6.12824393273\times10^{-6}$ J m⁻³ at 300 K | 5 |
| Radiation pressure | $P = u/3$ | $2.042747978\times10^{-6}$ Pa at 300 K | 5 |
| Entropy density | $s = 4aT^{3}/3$ | $2.72366397\times10^{-8}$ J m⁻³K⁻¹ at 300 K | 5 |
| Photon density | $n = 16\pi\zeta(3)(kT/hc)^{3}$ | $5.477448429\times10^{14}$ m⁻³ at 300 K | **1** |
| Mean photon energy | $u/n = 3\zeta(4)kT/\zeta(3)$ | $2.7011780329\,kT$ | 4 (cancels to a zeta ratio) |
| Wien parameter | $b = hc/(kx)$ | $2.897771955185\times10^{-3}$ m·K | **0** |

The table is the article in miniature. Energy density, pressure and entropy all carry $\pi^{5}$; the photon *count* carries only $\pi^{1}$, because counting modes needs the solid angle once and no Basel sum; and the mean energy per photon carries the ratio $\zeta(4)/\zeta(3)$, in which the fourth power survives only through $\zeta(4)$'s evaluation and the number itself, 2.7011780329, moves with nothing else.

Fluxes, computed for the temperatures that matter:

| $T$ | $\sigma T^{4}$ (W m⁻²) | Setting |
|---|---|---|
| 2.7255 K | $3.128934574\times10^{-6}$ | the cosmic microwave background |
| 300 K | $459.300328$ | a room-temperature surface |
| 1000 K | $5.670374419\times10^{4}$ | a dull-red heater |
| 5772 K | $6.293859247\times10^{7}$ | the solar photosphere |

And the Sun as a whole, from $L = 4\pi R^{2}\sigma T^{4}$ with the IAU nominal $R = 6.957\times10^{8}$ m and $T = 5772$ K, returns $3.827990903\times10^{26}$ W — one power of $\pi$ from the sphere's area, four from the spectrum, against the adopted $3.828\times10^{26}$ W. The agreement to four digits is a check on the arithmetic of the model, not on the constant: the solar radius and effective temperature are measurands, each known to far worse than 0.1%, which is already the size of the gap we are about to price.

## Wien's Law Has No Circle Constant At All

Differentiate the spectral density and set it to zero and every power of $\pi$ cancels, because the prefactor is a constant multiplying a function of $x$ alone:

$$\frac{d}{dx}\left[\frac{x^{3}}{e^{x}-1}\right] = 0 \;\Longrightarrow\; x = 5\left(1-e^{-x}\right),$$

a transcendental equation with one positive root, $x = 4.965114231744276304$ (residual $-7.2\times10^{-42}$ at forty digits). Because $x = h\nu_{\max}/kT$ is a pure number fixed by the shape of the Bose factor, the displacement constant is

$$b = \frac{hc}{kx} = 2.897771955185\times10^{-3}\ \text{m·K}, \qquad \frac{\nu_{\max}}{T} = \frac{kx}{h} = 103.45619415\ \text{GHz/K},$$

and neither digit depends on the circle constant in any way. This is the cleanest example in physics of a $\pi$-rich law whose *observable consequence* is $\pi$-free: the peak of the spectrum is where the derivative vanishes, and a constant multiplying the whole curve cannot move a maximum. The same is true of the median photon, which solves $\int_{0}^{x}t^{2}/(e^{t}-1)\,dt = \zeta(3)/2$ at $x = 1.4000197859$ (a median of 29.17167904 GHz/K, or $\lambda T = 10.276832456$ mm·K), and of every cumulative fraction: 14.72223307% of photons lie below $x=1$, 41.01990868% below $x=2$, and 74.99454532% of the *energy* lies below the spectral peak. All of these are ratios of two integrals with the same prefactor, so the constant is cancelled before the arithmetic begins.

## What Golden Pi Changes

Golden Pi puts $\hat\pi = 4/\sqrt\varphi = 3.144605511029693\ldots$ in place of $\pi$, with $\varphi = (1+\sqrt5)/2$ and the exact identities $\hat\pi^{2} = 16/\varphi$, $4/\hat\pi = \sqrt\varphi$, and $\hat\pi\cdot4\sqrt\varphi = 16$. Because the constant appears as a pure fifth power, the entire question reduces to one multiplication:

$$\left(\frac{\hat\pi}{\pi}\right)^{5} = 1.004804317606386639\ldots \quad \text{i.e.}\quad +0.4804317606\%.$$

The fifth power **amplifies** the recurring label gap of $+0.0959022309\%$ exactly fivefold — and this is the one place in the blog where amplification is clean rather than disguised, because no cancellation sits between the constant and the observable. Writing the golden constant out, $2\hat\pi^{5}/15 = 2048/(15\varphi^{5/2})$ with $\varphi^{5/2} = \varphi^{2}\sqrt\varphi = 3.330190676785561$:

$$\hat\sigma = \frac{2048\,k^{4}}{15\,\varphi^{5/2}\,h^{3}c^{2}} = 40.9986534059728\ \frac{k^{4}}{h^{3}c^{2}} = 5.69761669884\times10^{-8}\ \text{W m}^{-2}\text{K}^{-4}.$$

That coefficient $40.9986534059728\ldots$ is algebraic — it lies in $\mathbb{Q}(\sqrt\varphi)$, degree four, since $\sqrt\varphi$ satisfies $u^{4}-u^{2}-1=0$ — where $\pi^{5}$ is transcendental by Lindemann's 1882 theorem. The golden constant is therefore the algebraic multiple $2048/(15\varphi^{5/2})$ of the same dimensional lump $k^{4}/(h^{3}c^{2})$, and $\hat\sigma\cdot15\varphi^{5/2} = 2048\,k^{4}/(h^{3}c^{2})$ closes exactly with no residue.

Priced at the same temperatures:

| $T$ | $\sigma T^{4}$ | $\hat\sigma T^{4}$ | Shift |
|---|---|---|---|
| 2.7255 K | $3.128934574\times10^{-6}$ | $3.143966969\times10^{-6}$ | $+0.4804318\%$ |
| 300 K | $459.300328$ | $461.5069526$ | $+0.4804318\%$ |
| 5772 K | $6.293859247\times10^{7}$ | $6.324096946\times10^{7}$ | $+0.4804318\%$ |

What does **not** move is as instructive as what does. The photon density carries $\pi^{1}$, so it shifts only $+0.0959022\%$; the mean photon energy carries the fourth power, so it shifts $+0.3841611\%$; Wien's $b$, the peak frequency per kelvin, the median photon, the cumulative fractions and every ratio $\sigma T_{1}^{4}/\sigma T_{2}^{4} = (T_{1}/T_{2})^{4}$ do not move a digit under either label, because a ratio of two instances of the same formula cancels the constant identically. A body that must radiate a fixed flux under $\hat\sigma$ sits $0.1197\%$ cooler, since $T \propto \sigma^{-1/4}$ and $(1.0048043)^{-1/4} = 0.998802514$.

The exponent is thus a map of sensitivity: a measurement that counts photons tests $\pi^{1}$; a measurement that weighs energy tests $\pi^{5}$; a measurement of the spectral peak tests neither.

## The Honest Boundary: A Constant Fixed by Definition

Here the honesty has to be sharper than usual, because this quantity looks like a test and mostly is not one.

Since 20 May 2019 the SI defines the Boltzmann constant as exactly $k = 1.380649\times10^{-23}$ J/K and the Planck constant as exactly $h = 6.62607015\times10^{-34}$ J s. Both are *definitions*, not measurements. It follows that every tabulated value of $\sigma$ is computed from $\sigma = 2\pi^{5}k^{4}/(15h^{3}c^{2})$ with the conventional $\pi$ — the number $5.670374419\times10^{-8}$ is the output of that formula, so citing it against $\hat\sigma$ would be circular reasoning of the plainest kind. The same applies to $a$, to $u$, to the radiation pressure and to the entropy density: they are all one multiplication away from a definition. None of them is evidence for or against a value of the circle constant, and no table in a handbook should be read as if it were.

What *does* carry independent information is the other route: absolute radiometry and acoustic gas thermometry, which determine the Stefan–Boltzmann constant (or $k$) from first principles at the parts-per-million level. Those experiments measure a physical flux and a physical temperature — genuine measurands — and a $0.48\%$ shift in $\sigma$ is roughly five hundred times the present relative uncertainty, so unlike the catenary, the lune or the Gauss–Bonnet defect, this law is not structurally blind. It is simply that the quantity in the tables is a definition, and a definition cannot adjudicate a dispute about what a symbol means. The prediction is stated plainly here and left to stand on its own: under $\hat\pi = 4/\sqrt\varphi$ the flux at 5772 K is $6.324096946\times10^{7}$ W m⁻² rather than $6.293859247\times10^{7}$, a difference of $3.02\times10^{5}$ W m⁻² that no rearrangement of the algebra removes.

One more honest note: the fifth power does not make the golden value harder to state, only louder. The whole of the disagreement is the same $1$ part in $1043.7$ that appears in every other article on this site, and the exponent merely decides how many times it is multiplied by itself. The integral of $\zeta(4)$ is exact under either label; it is the label that differs.

Computed, never measured.

## Further Reading

- [The Catenary: Why a Hanging Chain Is cosh and Never a Parabola](/blog/posts/2026-11-11-catenary-catenoid-golden-pi/) — a curve whose defining equation holds no circle constant at any power, and the surface obtained by revolving it.
- [The Thermal de Broglie Wavelength: Why 2π Sits Under the Square Root](/blog/posts/2026-11-08-thermal-de-broglie-wavelength-bose-einstein-condensation-golden-pi/) — the other place where a Gaussian or Bose integral manufactures the constant, here at half power.
- [The Debye Specific Heat: Why 6π² Counts the Modes of a Crystal](/blog/posts/2026-11-06-debye-specific-heat-mode-count-t3-law-golden-pi/) — the same mode-counting argument in a solid, where the exponent of $\pi$ depends on where you stop unrolling.
- [The Gaussian Beam: Why a Diffraction-Limited Waist Obeys w₀θ = λ/π](/blog/posts/2026-11-07-gaussian-beam-waist-rayleigh-range-gouy-phase-golden-pi/) — a case where every first-power occurrence turns algebraic under Golden Pi.
- [The Basel Problem: How ζ(2) Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — where the $\pi^{4}$ inside $\zeta(4)$ comes from, and why the fourth power is Euler's, not the circle's.
