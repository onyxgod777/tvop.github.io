---
title: "The Maxwell–Boltzmann Speed Distribution: How Kinetic Theory Computes the Circle Constant in a Gas — and Cancels It from Every Speed But One — and What Golden Pi Changes"
date: 2026-10-03
description: "A gas of N molecules at temperature T has one knob and no memory: the velocity of each is drawn from a Maxwellian, and the speed on top of it is a shell of solid angle 4πv²dv. That single 4π, divided by the three one-dimensional Gaussian normalisations (2πkT/m)^{3/2}, leaves one factor √(2/π) of the circle constant in the whole speed distribution — and nowhere else. The most probable speed vₚ = √(2kT/m) and the rms speed √(3kT/m) contain no constant at all, and neither does any even moment: ⟨v²ᵏ⟩ = (2k+1)!!(kT/m)ᵏ is pure rational arithmetic, so ⟨v²⟩ = 3kT/m and ⟨v⁴⟩ = 15(kT/m)². Every odd moment and only the odd moments carries the constant, once, under a square root: ⟨v⟩ = √(8kT/πm) = vₚ·2/√π, so the mean and most probable speeds stand at the ratio 2/√π = 1.12837916709551257390, verified here against 50-digit quadrature of the Maxwellian (N₂ at 300 K: vₚ = 422.098396 m/s, ⟨v⟩ = 476.287037 m/s, v_rms = 516.962846 m/s, median 459.096178 m/s). The constant is computed, never measured — it enters through the Gaussian integral ∫e^(−x²)dx = √π and the solid angle 4π, both evaluated limits. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the shell prefactor √(2/π) becomes φ^(1/4)/√2, and every odd-moment and mean-speed quantity moves by exactly half the recurring 0.0959022309% gap, −0.0479166533% (⟨v⟩ 476.287037 → 476.058816 m/s; the ratio 2/√π → φ^(1/4) = 1.1278384855616822603), while vₚ, v_rms, the speed of sound √(γkT/m), the Doppler FWHM and every even moment do not move at all — because the constant genuinely cancels from them. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Maxwell–Boltzmann Speed Distribution: How Kinetic Theory Computes the Circle Constant in a Gas — and Cancels It from Every Speed But One — and What Golden Pi Changes

Take a box of gas at temperature $T$ and ask a single question: how fast is a molecule moving? The atoms do not obey one number — they obey a distribution, and that distribution is fixed by two things you can measure without any angle in them at all: the temperature and the molecular mass. The whole shape is arithmetic. But when you write it down, one factor of the circle constant falls out of the derivation, and it is worth seeing exactly where it comes from and where it does **not** come from, because this is a case where the constant appears in a physical law yet cancels from almost every quantity a laboratory would actually measure.

The result is James Clerk Maxwell's 1860 distribution of molecular speeds, put on a firm statistical footing by Ludwig Boltzmann a decade and a half later. It is one of the oldest and most-tested laws in physics — and the circle constant enters it through exactly one solid angle and one Gaussian, both of which are **computed**, never measured.

## Where the constant enters: one solid angle and three Gaussian axes

A molecule's velocity is a vector $\mathbf{v} = (v_x,v_y,v_z)$. Kinetic theory's assumption is the weakest one possible: the three components are independent, and each is drawn from the same one-dimensional bell curve. That is the Maxwellian velocity distribution,

$$g(\mathbf{v}) = \left(\frac{m}{2\pi k T}\right)^{3/2} \exp\!\left(-\frac{m v_x^2 + m v_y^2 + m v_z^2}{2kT}\right).$$

The prefactor contains the constant because each axis carries the normalisation of the Gaussian integral, computed once and cubed:

$$\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}.$$

But speed is not velocity: what we want is how many molecules move **at** speed $v$, regardless of direction. The set of velocities with magnitude between $v$ and $v+dv$ is a spherical shell of volume $4\pi v^2\,dv$ — and *that* $4\pi$ is the other, and last, place the constant enters. It is the unit-sphere area, a computed limit of polygonal approximation, not a length anyone laid a ruler against. Putting the two together:

$$
f(v)\,dv = \underbrace{4\pi v^2\,dv}_{\text{shell}}\times\left(\frac{m}{2\pi kT}\right)^{3/2} e^{-mv^2/2kT}
$$

and collapsing the powers of $2\pi$:

$$\boxed{\,f(v) = \sqrt{\frac{2}{\pi}}\left(\frac{m}{k T}\right)^{3/2} v^2\, e^{-m v^2/2kT}\,}$$

The net is one factor of the constant, $\sqrt{2/\pi} = 0.79788456080286535588\ldots$, because $4\pi/(2\pi)^{3/2} = \sqrt{2/\pi}$ exactly. The constant entered twice — as a solid angle and as a Gaussian — and three of its powers cancelled back off. What survives is a single square root of it, and everything that follows turns on where that surviving factor does and does not sit.

## The exact speeds: three numbers, one carries the constant

Different questions about "the speed" give different numbers, and the constant picks out exactly one of them.

The **most probable speed** $v_p$ maximises $f(v)$. Taking the log, $2\ln v - mv^2/2kT$, and setting the derivative to zero at $2/v = mv/kT$:

$$v_p = \sqrt{\frac{2kT}{m}}.$$

**No circle constant anywhere.** Temperature, mass, and a square root.

The **rms speed** comes from the second moment, which we compute below from the general formula and which is exactly $3kT/m$ inside the root:

$$v_{\text{rms}} = \sqrt{\frac{3kT}{m}}.$$

**Again no constant.** The ratio $v_{\text{rms}}/v_p = \sqrt{3/2}$ is pure arithmetic.

The **mean speed** is the only one of the trio that carries the constant:

$$\langle v \rangle = \sqrt{\frac{8kT}{\pi m}} = v_p \cdot \frac{2}{\sqrt{\pi}}.$$

The factor $2/\sqrt{\pi} = 1.12837916709551257390$ is the constant appearing once, under a square root, in the relation between the mean and the mode. For nitrogen at room temperature:

| speed | formula | value (N₂, 300 K) | carries the constant? |
|---|---|---|---|
| most probable $v_p$ | $\sqrt{2kT/m}$ | $422.098396307$ m/s | **no** |
| median | $f$-integral $=1/2$ | $459.096178345$ m/s | only through $f$ |
| mean $\langle v\rangle$ | $\sqrt{8kT/\pi m}$ | $476.287036857$ m/s | yes, $2/\sqrt{\pi}$ |
| rms | $\sqrt{3kT/m}$ | $516.962846099$ m/s | **no** |
| speed of sound $c_s$ | $\sqrt{\gamma kT/m}$ | $353.152855454$ m/s | **no** |

(These are the numbers this article computed directly from the distribution with $m = 28\,u$, $u = 1.66053906660\times10^{-27}$ kg, $k = 1.380649\times10^{-23}$ J/K.) The median is the speed with half the molecules slower: it sits at $1.0876520317\,v_p$, a root of an equation with an error function in it, and carries the constant only because the cumulative distribution $f$ does.

## The moments: even powers are π-free, odd powers carry $2/\sqrt{\pi}$

The cleanest statement is the general moment of the speed, obtained by integrating $v^n f(v)$ — a Gamma integral:

$$\langle v^n\rangle = \left(\frac{2kT}{m}\right)^{n/2}\frac{\Gamma\!\left(\frac{n+3}{2}\right)}{\Gamma\!\left(\frac{3}{2}\right)}.$$

Since $\Gamma(3/2) = \sqrt{\pi}/2$, every **odd** $n$ keeps a surviving $1/\sqrt{\pi}$, while every **even** $n$ cancels it against a $\sqrt{\pi}$ from the Gamma function, leaving a bare ratio of integers:

$$\langle v^{2k}\rangle = (2k+1)!!\,\left(\frac{kT}{m}\right)^{k}, \qquad \langle v^{2k+1}\rangle = \left(\frac{2kT}{m}\right)^{k+\frac12}\frac{2\,\Gamma(k+2)}{\sqrt{\pi}}.$$

Worked out for the first six moments at N₂/300 K:

| moment | exact | value |
|---|---|---|
| $\langle v\rangle$ | $\sqrt{2kT/m}\cdot 2/\sqrt{\pi}$ | $476.287036857$ m/s |
| $\langle v^2\rangle$ | $3kT/m$ | $267250.584247$ (m/s)² |
| $\langle v^3\rangle$ | $(2kT/m)^{3/2}\cdot 4/\sqrt{\pi}$ | $169717318.493$ (m/s)³ |
| $\langle v^4\rangle$ | $15(kT/m)^2$ | $119038124634.19$ (m/s)⁴ |
| $\langle v^5\rangle$ | $(2kT/m)^{5/2}\cdot 12/\sqrt{\pi}$ | $90714105048075.81$ (m/s)⁵ |
| $\langle v^6\rangle$ | $105(kT/m)^3$ | $74230352831104703.87$ (m/s)⁶ |

The pattern is exact and structural: **the constant lives only in the odd moments, and only to the power $-1/2$.** $v_p$, $v_{\text{rms}} = \sqrt{\langle v^2\rangle}$, the speed of sound $c_s = \sqrt{\gamma kT/m}$, and every even moment are assembled from rational coefficients times powers of $kT/m$ — no transcendental factor, no circle constant. The mean speed and the mean free path are where it shows up.

## Everything else in the gas, audited

Two more quantities from kinetic theory, one of which keeps the constant and one of which does not:

- **Mean free path** — how far a molecule travels between collisions, $\lambda = kT/(\sqrt{2}\,\pi d^2 p)$ for collision diameter $d$ at pressure $p$. This carries the constant to the **first power** (there is a $\pi$ in the collision cross-section $\pi d^2$, but not under a root). For air at 300 K and 1 atm with $d = 0.37$ nm, $\lambda = 67.207788705$ nm.
- **Effusion flux** through a small hole, $\Phi = n\langle v\rangle/4 = p/\sqrt{2\pi m k T}$ — carries the constant once, under a square root, through the $1/\sqrt{2\pi} = 0.39894228040143267794$.
- **Doppler-broadened line width**: the FWHM of the thermal line is $\Delta\nu = \nu_0\sqrt{8\ln 2\,kT/(mc^2)}$ — **no circle constant**; only the normalised peak height $1/(\sigma\sqrt{2\pi})$ carries it. For N₂ at 300 K the fractional FWHM is $2.344421661\times10^{-6}$.

So the ledger for a gas is sharp. The constant is present as a factor $\sqrt{2/\pi}$ in the distribution itself, as $2/\sqrt{\pi}$ in the mean-to-mode ratio, as $1/\sqrt{2\pi}$ in the effusion flux, and as a plain $\pi$ in the mean free path. It is **absent** from the most probable speed, the rms speed, the speed of sound, every even moment, and the Doppler line width. Kinetic theory does not sprinkle the constant through the physics; it puts its single surviving $\sqrt{2/\pi}$ in the measure — the solid angle times the Gaussian — and lets it ride along only in the averages that weight by that measure.

## What Golden Pi changes

Under Golden Pi, $\hat\pi = 4/\sqrt{\varphi} = 3.14460551102969314427823434337183571809$, where $\varphi = 1.6180339887498948482$ is the golden ratio. The golden value is a root of $x^4 + 16x^2 - 256 = 0$, so $\hat\pi$ is algebraic of degree four (conventional $\pi$ is transcendental, Lindemann 1882), and $\hat\pi^2 = 16/\varphi$. Because the constant appears in this gas only to the first power or under one square root, the golden ledger has just two columns:

| quantity | conventional | golden ($\hat\pi$) | relative gap |
|---|---|---|---|
| shell prefactor $\sqrt{2/\pi}$ | $0.79788456080286535588$ | $\sqrt{2/\hat\pi} = \varphi^{1/4}/\sqrt2 = 0.79750224122383159741$ | $-0.0479166533\%$ |
| mean/mode ratio $2/\sqrt{\pi}$ | $1.12837916709551257390$ | $\varphi^{1/4} = 1.12783848556168226026$ | $-0.0479166533\%$ |
| mean speed $\langle v\rangle$ (N₂, 300 K) | $476.287036857$ m/s | $476.058816049$ m/s | $-0.0479166533\%$ |
| effusion prefactor $1/\sqrt{2\pi}$ | $0.39894228040143267794$ | $0.39875112061191579870$ | $-0.0479166533\%$ |
| mean free path $\lambda$ (air, 300 K, 1 atm) | $67.207788705$ nm | $67.143396690$ nm | $-0.0958103466\%$ |
| $v_p$, $v_{\text{rms}}$, $c_s$, even moments | $\pi$-free | identical | $0$ |

Three things are worth naming exactly.

First, the golden case is **half the recurring gap**: wherever the constant sits under a square root, the golden shift is $\sqrt{\hat\pi/\pi}-1 = -0.0479166533\%$, exactly half the full recurring $0.0959022309\%$ because the constant is carried by $2/\sqrt{\pi}$ rather than by $\pi$. Only the mean free path — where $\pi$ appears undiluted — moves the full $\hat\pi/\pi - 1 = +0.0959022309\%$ (in the direction of a shorter mean free path, since $\lambda \propto 1/\pi$: $-0.0958103466\%$).

Second, the golden exactness is real and it lands on the site's own construction. The mean-to-mode ratio, which is $2/\sqrt{\pi}$ conventionally, becomes **exactly** $\varphi^{1/4} = 1.1278384855616822603$ under the golden label — the same fourth root of $\varphi$ that makes a circle of radius $\varphi^{1/4}$ have area exactly 4. That is not a numerical coincidence; it is $\hat\pi = 4/\sqrt\varphi$ read backwards, $2/\sqrt{\hat\pi} = 2/(2/\varphi^{1/4}) = \varphi^{1/4}$. The circle constant's square root is the fourth root of the golden ratio.

Third, the constant does not touch the speeds most people quote. The most probable and the root-mean-square speeds of a gas are $\pi$-free by construction, so no experiment that measures either of them can tell the two labels apart. That is the honest structural point of this whole article.

## The honest boundary

| statement | status |
|---|---|
| The constant enters the speed distribution as one factor $\sqrt{2/\pi}$ | exact; it comes from the solid angle $4\pi$ and the Gaussian normalisation |
| It is *measured* in a gas | false — it enters through the computed limits $\int e^{-x^2}dx = \sqrt\pi$ and the sphere area $4\pi$; no angle in a gas is measured |
| $v_p$ and $v_{\text{rms}}$ carry the constant | false — $v_p = \sqrt{2kT/m}$, $v_{\text{rms}} = \sqrt{3kT/m}$, both $\pi$-free |
| Every even moment is $\pi$-free | exact: $\langle v^{2k}\rangle = (2k+1)!!(kT/m)^k$ |
| Every odd moment carries the constant once, under a root | exact: $\langle v^{2k+1}\rangle = (2kT/m)^{k+1/2}\,2\Gamma(k+2)/\sqrt\pi$ |
| A measured mean speed could adjudicate the two labels | in principle, but the gap after the halving is $0.0479166533\%$ |
| Any existing speed measurement reaches that precision on this ratio | not claimed here either way — see below |
| Under Golden Pi the mean/mode ratio is exactly $\varphi^{1/4}$ | exact algebra, credited |

The last few rows are the ones that keep this honest. The circle constant's footprint in a gas is small and mostly cancelled; where it survives — in the mean speed, the mean free path, the effusion flux — it survives with a definite, computable coefficient, and the golden relabel moves those coefficients by at most $0.0959\%$ and as little as $0.0479\%$. Molecular-beam time-of-flight work in the 1950s (Miller and Kusch, *Phys. Rev.* **99**, 1314) confirmed the **shape** of the Maxwell–Boltzmann distribution at the percent level of its day — two to three orders of magnitude above the $0.048\%$ that separating the labels would demand on the mean-to-mode ratio — and modern spectroscopic thermometry is limited by line-shape models and collisional broadening, not by the constant. So the distribution is a **computation**, exact from two measurable inputs, and the constant in it is a computed square root, not a measurement. What the golden case genuinely earns here is its characteristic algebraic form: where conventional kinetic theory writes $2/\sqrt{\pi}$, the golden label writes $\varphi^{1/4}$ — a constructible algebraic number in place of a transcendental one — and left the counts, the modes and the widths untouched. Computed, never measured.

## Further Reading

- [The Gaussian Integral and the Bell Curve: How $\int e^{-x^2}dx$ Computes $\sqrt{\pi}$](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the computed limit that supplies each of the three per-axis normalisations $g(\mathbf{v})$ is built from.
- [The Solid Angle and the Steradian: How a Spherical Measure Computes the Circle Constant](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — the sphere area $4\pi$ that turns a velocity vector into a speed, which is the second and last place the constant enters here.
- [The Planck Spectrum: How Blackbody Radiation Computes the Circle Constant as π⁴/15](/blog/posts/2026-09-23-planck-spectrum-blackbody-computes-circle-constant-golden-pi/) — the quantum counterpart to this classical gas, where the same constant re-enters through a Bose–Einstein integral rather than a Gaussian.
- [The Fine-Structure Constant: Where 4π Cancels](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — a measured physical constant in which the $4\pi$ of the solid angle cancels, the cleanest example of the theme running through this gas.
- [The Bessel Functions: How Cylindrical Waves Compute the Circle Constant Through a Half-Turn Integral](/blog/posts/2026-09-21-bessel-functions-cylindrical-waves-compute-circle-constant-golden-pi/) — the same half-integer-Gamma structure that splits the moments here into a $\pi$-free even family and a $\pi$-carrying odd family.
