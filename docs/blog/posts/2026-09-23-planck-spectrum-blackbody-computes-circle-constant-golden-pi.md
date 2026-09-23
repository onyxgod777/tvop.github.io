---
title: "The Planck Spectrum: How Blackbody Radiation Computes the Circle Constant as π⁴/15, and What Golden Pi Changes"
date: 2026-09-23
description: "Thermal radiation is the one place the circle constant enters at the fifth power — Stefan–Boltzmann's σ = 2π⁵k⁴/(15h³c²) carries a Bose–Einstein integral that computes π⁴/15 as a pure limit, and since the 2019 SI redefinition σ has zero definitional uncertainty, so the golden label's 0.48 % gap has no measurement noise to hide inside."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Planck Spectrum: How Blackbody Radiation Computes the Circle Constant as π⁴/15, and What Golden Pi Changes

Every radiating body carries the circle constant in its light. A hot iron, a filament, the Sun, the leftover glow of the Big Bang — all of them emit a spectrum whose total radiated power is

$$\sigma T^4, \qquad \sigma = \frac{2\pi^5 k^4}{15\,h^3c^2} = 5.6703744191844295\times10^{-8}\ \text{W}\,\text{m}^{-2}\text{K}^{-4}$$

and that formula is unusual among everything this series has audited so far, for two reasons.

First, $\pi$ appears to the **fifth power**, not the first — so the gap between golden π ($\hat\pi = 4/\sqrt{\varphi} = 3.144605511\ldots$, $\varphi = 1.6180339887$) and the analytic constant $3.1415926536$ is amplified, not diluted. Second, and this is the part that matters, $\sigma$ is no longer a *measured* number. Since the 2019 SI redefinition the Boltzmann constant $k$, the Planck constant $h$ and the speed of light $c$ are all fixed by definition, and π is fixed by computation, so $\sigma$ has a **relative uncertainty of exactly zero**. There is no percent-level measurement error down here to swallow a relabelling of the constant. Every digit of $\sigma$ is printed by definition, and this article will compute what the golden label does to them.

Nothing below is measured. Every value is a convergent limit, evaluated.

## Where the fifth power comes from: one Bose–Einstein integral

Planck's law gives the spectral radiance of a blackbody at temperature $T$,

$$B_\nu(T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/kT}-1}$$

The $2$ counts the two polarisations of light. The explicit $h\nu^3$ and the exponential come from quantum statistics and relativity. The circle constant is *not* visible here at all except through the conversion of $h$ into $\hbar = h/2\pi$, which is a unit convention rather than physics.

Integrate the spectral energy density over all frequencies and the constant appears. Substituting $x = h\nu/kT$,

$$u(T) = \frac{8\pi h}{c^3}\int_0^\infty \frac{\nu^3\,d\nu}{e^{h\nu/kT}-1} = \frac{8\pi h}{c^3}\left(\frac{kT}{h}\right)^{4}\int_0^\infty \frac{x^3\,dx}{e^{x}-1}$$

and the remaining integral is a standard one, computed — never measured — by expanding the geometric series $1/(e^x-1) = \sum_{n\ge1} e^{-nx}$ and integrating term by term:

$$\int_0^\infty \frac{x^3\,dx}{e^{x}-1} = \sum_{n=1}^{\infty}\frac{6}{n^4} = 6\,\zeta(4) = \Gamma(4)\zeta(4) = \frac{\pi^4}{15} = 6.4939394022668291491\ldots$$

Evaluated here to thirty significant figures, the sum $\sum 6/n^4$ and the closed form $\pi^4/15$ agree to $9.2\times10^{-41}$, which is the accuracy of the arithmetic rather than any physical statement. This is the whole circle-constant content of thermal radiation: a convergent sum of rationals whose limit happens to be $\pi^4/15$.

The general family is $\int_0^\infty x^{n-1}/(e^x-1)\,dx = \Gamma(n)\zeta(n)$, and the table below is worth looking at closely, because it shows that **the shape of the spectrum is not what carries the constant** — the total is:

| $n$ | integral $\Gamma(n)\zeta(n)$ | value | carries $\pi$? |
|---|---|---|---|
| 2 | $\zeta(2)=\pi^2/6$ | 1.6449340668482264365 | yes, $\pi^2$ |
| 3 | $2\,\zeta(3)$ (Apéry) | 2.4041138063191885708 | **no** |
| 4 | $\pi^4/15$ | 6.4939394022668291491 | yes, $\pi^4$ |
| 5 | $24\,\zeta(5)$ | 24.886266123440878232 | **no** |
| 6 | $120\,\zeta(6)=\pi^6/945$ | 122.08116743813389677 | yes, $\pi^6$ |

The photon-number integral ($n=3$, which counts *how many* photons) is $2\zeta(3) = 2.4041138063$, built from Apéry's constant, which has no known closed form in π at all. The energy integral ($n=4$) is the one that carries $\pi^4$. So the constant enters the *energy* of a photon gas but not the *count*, and the entry point is the four powers of frequency in $\int\nu^3 d\nu$ meeting the four powers of the closed form.

## Wien's law is π-free, which settles the easy objection

Before asking what golden π does, it is worth closing the door on the obvious escape route: surely the spectrum's peak location tells us which constant is right?

It does not, because the peak is located by an equation with no constant in it at all. Maximising $x^3/(e^x-1)$ gives the transcendental condition $x = 3(1-e^{-x})$, whose root is $x = 2.8214393721220788934$; in the wavelength form $x^5/(e^x-1)$ the condition is $x = 5(1-e^{-x})$, with root

$$x = 4.965114231744276303698759131322893944\ldots, \qquad \frac{x^5}{e^x-1} = 21.201435660549920740\ldots$$

Both roots are pure arithmetic — exponentials and rationals, no circle. Wien's displacement constant follows as $b = hc/(kx) = 2.8977719551851726\times10^{-3}\ \text{m}\,\text{K}$, and it is a fixed number whether the circle constant is called π or anything else. The same goes for the Rayleigh–Jeans limit $B_\nu \to 2\nu^2kT/c^2$ in the long-wavelength regime: no circle constant, only the 2 of polarisation.

So the peak of an iron's glow, the shape of the CMB spectrum, the ratio of radiances at two wavelengths — all of that is silent on the question. Only the *normalisation*, the one place where the full turn shows up, carries the constant.

## Now relabel it: what golden π does to the numbers

Put $\hat\pi = 4/\sqrt\varphi$ in place of π in the identities above, hold $k$, $h$, $c$ at their defined SI values, and recompute. Every number below was computed in this article at 40-digit precision.

| quantity | with $\pi = 3.1415926536$ | with $\hat\pi = 3.1446055110$ | shift |
|---|---|---|---|
| $\pi^4$ | 97.409091034002437236 | 97.783298880026918860 | $+0.3841611\%$ |
| $\pi^5$ | 306.01968478528145326 | 307.48990054479627048 | $+0.4804318\%$ |
| $\int_0^\infty \frac{x^3dx}{e^x-1} = \frac{\pi^4}{15}$ | 6.4939394022668291491 | 6.5188865920017945906 | $+0.3841611\%$ |
| $\sigma = \frac{2\pi^5k^4}{15h^3c^2}$ (W m⁻² K⁻⁴) | $5.6703744191844295\times10^{-8}$ | $5.6976166988413216\times10^{-8}$ | $+0.4804318\%$ |
| $a = 4\sigma/c$ (J m⁻³ K⁻⁴) | $7.5657332502800046\times10^{-16}$ | $7.6020814357395497\times10^{-16}$ | $+0.4804318\%$ |
| full solid angle $4\pi$ | 12.566370614359173 | 12.578422044118773 | $+0.0959022\%$ |
| $\hbar = h/2\pi$ (J s) | $1.0545718176461564\times10^{-34}$ | $1.0535614287323293\times10^{-34}$ | $-0.0958103\%$ |
| Wien root $x$ of $x=5(1-e^{-x})$ | 4.9651142317442763 | *(unchanged)* | $0$ |
| $x^5/(e^x-1)$ at the peak | 21.201435660549921 | *(unchanged)* | $0$ |

The shifts are not random: $\pi$ enters the energy integral at the fourth power ($0.3842\%$, four times the recurring $0.0959022\%$ gap) and Stefan–Boltzmann at the fifth ($0.4804\%$, five times), so the gap *compounds* with each power instead of diluting through a square root as it does in the diffusion and Fresnel cases. And the last two rows are the honest counterweight: the spectrum's shape, its peak position and its peak height do not move at any decimal place, because they never contained the constant.

## Where the constant meets a measured length

Now do the thing the rest of the series does: put the relabelled constant into formulas that also contain genuinely *measured* quantities — real lengths, real luminosities, real temperatures — and read the consequences.

The Sun's effective temperature is defined by requiring its measured luminosity to leave through its measured surface:

$$L_\odot = 4\pi R_\odot^2 \sigma T_\text{eff}^4 \quad\Longrightarrow\quad T_\text{eff} = \left(\frac{L_\odot}{4\pi R_\odot^2\sigma}\right)^{1/4}$$

With the measured $L_\odot = 3.828\times10^{26}$ W and $R_\odot = 6.957\times10^{8}$ m, that returns $T_\text{eff} = 5772.0034$ K. Note the structure: $\pi$ and $\sigma$ enter as $\pi\sigma$ under a fourth root, so the shift is $\hat\pi/\pi$ to the power $-6/4$ — damped, not amplified: $-0.1436811\%$, i.e.

$$T_\text{eff} = 5772.0034\ \text{K} \;\longrightarrow\; 5763.7102\ \text{K} \qquad (-8.2933\ \text{K})$$

and the Wien peak of sunlight moves from $502.0392$ nm to $502.7616$ nm, still green. The solar **surface flux** $\sigma T^4$ moves the other way by exactly one factor of the gap ($-0.0959022\%$: $6.2938742\times10^7 \to 6.2878440\times10^7\ \text{W}\,\text{m}^{-2}$), because the $\pi$ in σ survives to the first power there while the $\pi$ in the temperature has already been undone by the fourth root.

For the cosmic microwave background the measured input is the temperature itself — $T = 2.72548 \pm 0.00057$ K from the FIRAS instrument on COBE, a genuinely measured number with a 0.02 % error bar. The derived quantities inherit whichever constant you use:

| CMB quantity | analytic constants | golden constants | shift |
|---|---|---|---|
| energy density $u = aT^4$ | $4.1746783808\times10^{-14}$ J m⁻³ | $4.1947348616\times10^{-14}$ J m⁻³ | $+0.4804318\%$ |
| same, in eV cm⁻³ | 0.260562930 | 0.261814757 | $+0.4804318\%$ |
| photon number density $n = 16\pi\zeta(3)(kT/hc)^3$ | 410.717806 cm⁻³ | 411.111694 cm⁻³ | $+0.0959022\%$ |
| Wien peak wavelength $b/T$ | 1063.2153 µm | *(unchanged)* | $0$ |
| entropy density $s = \tfrac43 aT^3$ | $2.0422963445\times10^{-14}$ J m⁻³ K⁻¹ | — | $+0.4804318\%$ |

The photon density shifts by only one factor of the gap while the energy density shifts by five, and the reason is instructive: the count integral is $2\zeta(3)$ (Apéry, π-free) and its only circle constant is the $4\pi$ of the solid angle over which photons are counted — one power, one gap. Energy multiplies that by the mean photon energy, which drags in the $\pi^4/15$ of the full Bose integral, and the exponents do the rest.

## The honest ledger

Three statements have to stand together, and none of them should be softened.

**The golden label is under maximum pressure here.** $\sigma$ is the sharpest test in this series so far, because it is the only constant audited that is both derived from π at the fifth power *and* definitionally exact. There is no 0.1 % measurement to hide in, no "within experimental error" to appeal to. If a calculator is told that the turn constant is 3.1446055110, the Bose integral it evaluates is 6.5188865920 rather than 6.4939394023, and every Stefan–Boltzmann calculation built on it comes out 0.48 % high. The analytic constant is not merely a convention here; it is the limit the arithmetic reaches.

**But the failure is a failure of a relabelling, not of a geometry.** Everything that did not contain π stayed put: the Wien roots $2.8214393721$ and $4.965114231744276$, the peak height $21.2014356605$, the Rayleigh–Jeans law, the whole spectral shape, the $\zeta(3)$ photon count, and the $\zeta(5)$ and $\zeta(3)$ terms in the gas thermodynamics. A consistent unit change — treating the golden turn as the unit of angle — leaves the spectrum invariant, exactly as it leaves the diffusion kernel invariant. The gap appears when a golden angle is fed into an integral whose upper limit is the natural turn — which is exactly what "$1/15$" encodes, since $\Gamma(4)\zeta(4) = 6\cdot\pi^4/90$.

**And the golden case keeps its genuine wins.** Golden π is algebraic: $\hat\pi = 4/\sqrt\varphi$ is a root of $x^4 + 16x^2 - 256 = 0$, an exact constructible-in-φ quantity, whereas the analytic constant is transcendental and only ever approached by limit. In a thermodynamics where every important coefficient is rational or geometric — $2$ for polarisation, $4\pi$ for the solid angle, the $1/15$ assembled from $\Gamma(4)=6$ and $\zeta(4)=\pi^4/90$, the quantum unit $h$ — an algebraic constant at least speaks the same language as the rest of the formula. That is a real conceptual advantage. It does not change the value the series computes, and this article will not pretend that it does.

The constant in the light of a hot body is computed, never measured. Photons are counted; no tape measure is involved. The number that falls out of the count is 3.1415926535…, and the golden label misses the fifth-power combination it builds from it by 0.48 % — five copies of the recurring $0.0959\,\%$ gap, compounded rather than damped.

## Further Reading

- [The Heat Kernel: How the Diffusion Equation Computes the Circle Constant Through Its Own Normalization, and What Golden Pi Changes](/blog/posts/2026-09-17-heat-kernel-diffusion-computes-circle-constant-golden-pi/) — the Gaussian normalisation $1/\sqrt{4\pi Dt}$, where the constant sits under a square root and the gap is halved instead of quintupled.
- [The Fine-Structure Constant: Why Physics's Most Famous 4π Cancels Out, and What Golden Pi Changes](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — the measured constant that turns out to contain no circle constant at all.
- [The Riemann Zeta Function at Even Integers: How Euler's Bernoulli-Numbers Formula Computes π to Every Even Power, and What Golden Pi Changes](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — the machinery behind $\zeta(4) = \pi^4/90$ used in this article's Bose integral.
- [The Gamma Function and Euler's Reflection Formula](/blog/posts/2026-08-26-gamma-function-euler-reflection-formula-computes-circle-constant-golden-pi/) — $\Gamma(4)\zeta(4)$ is the factorial-and-zeta pair that produces $\pi^4/15$.
- [The Solid Angle: How the Steradian Computes the Circle Constant, and What Golden Pi Changes](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — the $4\pi$ that enters the photon count and the phase-space normalisation.
