---
title: "The Thermal de Broglie Wavelength: Why 2π Sits Under the Square Root, Why nλ³ = ζ(3/2) Is the Whole Criterion for Condensation, and What Golden Pi Changes"
date: 2026-11-08
description: "Cool a gas and its quantum size grows: λ_T = h/√(2πmkT), one √(2π) per Cartesian axis from the Gaussian momentum integral, so the entire single-particle partition function is Z₁ = V/λ_T³ with no other constant in it. This article derives λ_T from the phase-space cell h³, shows that the occupation of the ground state turns macroscopic exactly when the degeneracy parameter reaches nλ³ = ζ(3/2) = 2.6123753486854883 — a pure number, containing no circle constant, because the constant has already been absorbed into λ — and then computes the critical temperature T_c = (h²/2πmk_B)(n/ζ(3/2))^(2/3): 85.8177461 nK for ⁸⁷Rb at n = 10¹⁹ m⁻³, 324.4203931 nK for ²³Na, 1063.048223 nK for ⁷Li, 56.11771284 nK for ¹³³Cs, with 170 nK requiring n = 2.788096×10¹⁹ m⁻³, the condensed fraction 1 − (T/T_c)^(3/2) giving exactly 1 − √2/4 = 0.6464466094 at half the critical temperature, and the pressure below T_c becoming volume-independent with PV/NkT_c = ζ(5/2)/ζ(3/2) = 0.5135124468 and U/NkT_c = 0.7702686702, both π-free. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693…) the wavelength becomes the algebraic λ̂_T = hφ^(1/4)/(2√2√(mkT)) = 0.9995206038 λ_T, the quantum concentration shifts +0.1438878304%, the critical temperature −0.0958103466% (85.73552382 nK for the same rubidium gas), the entropy only +0.0119549 J mol⁻¹ K⁻¹ because the constant enters it logarithmically, and nothing at all moves in nλ³, the condensed fraction, the 0.770 or the 0.5135. The honest boundary is that no condensate ever tested the last three digits: liquid helium at 2.2×10²⁸ m⁻³ has an ideal-gas prediction of 3.1519695 K against a measured λ-point of 2.1768 K, an error of +44.80%, four hundred and sixty-seven times the golden gap. Computed, never measured."
---

# The Thermal de Broglie Wavelength

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

A gas has a size, and the size is not the size of its atoms. It is the size of the region over which one atom's wavefunction still has a definite phase — and that region grows as the gas is cooled, without any atom changing. At room temperature a rubidium atom's thermal wavelength is 10.812 picometres, a fiftieth of the atom's own diameter. At a hundred nanocelvin the same atom's wavelength is 592 nanometres, six hundred times its diameter, and the waves of neighbouring atoms overlap. When the overlap becomes total, the gas stops behaving like a gas: a macroscopic fraction of its atoms falls into the single lowest quantum state and stays there.

The length that governs this is written

$$
\lambda_T \;=\; \frac{h}{\sqrt{2\pi m k_B T}},
$$

and the circle constant sits in it under a square root, at first power inside the root. This article follows that constant through the derivation — it arrives exactly once, from a Gaussian integral over momentum, and then disappears from every number that decides whether condensation happens — and then repeats the arithmetic with $\hat\pi = 4/\sqrt{\varphi}$ in place of $\pi$.

The shape of the answer is the one this site keeps finding. The constant is real and computed, not decorative. But it is consumed in the definition of the length, and after that the physics is a count of states, and a count of states is an integer-valued business with the constant already divided out.

## Where the 2π comes from: one per axis

The canonical partition function of one particle of mass $m$ in a box of volume $V$ at temperature $T$ is the phase-space integral divided by the cell volume $h^{3}$:

$$
Z_1 \;=\; \frac{1}{h^{3}}\int_V d^{3}q \int d^{3}p \; e^{-p^{2}/2mk_BT}
\;=\; \frac{V}{h^{3}}\left(\int_{-\infty}^{\infty} e^{-p_x^{2}/2mk_BT}\,dp_x\right)^{3}.
$$

The momentum integral separates because the kinetic energy does, and each factor is a Gaussian:

$$
\int_{-\infty}^{\infty} e^{-p_x^{2}/2mk_BT}\,dp_x \;=\; \sqrt{2\pi m k_B T} \;=\; \sqrt{2\pi}\,\sqrt{m k_B T}.
$$

So the whole thing is

$$
Z_1 \;=\; \frac{V}{h^{3}}\,(2\pi m k_B T)^{3/2} \;=\; \frac{V}{\lambda_T^{3}},
\qquad
\lambda_T \;=\; \frac{h}{\sqrt{2\pi m k_B T}} .
$$

Three axes, three Gaussians, one $\sqrt{2\pi}$ each — the exponent of the constant is exactly the number of Cartesian directions, because $\int e^{-x^{2}}dx = \sqrt{\pi}$ is what a Gaussian contributes per direction and a plane has three of them. Below two dimensions the same derivation would carry $\pi$ per axis and the constant's power would be a bookkeeping fact about the dimension of the space, not about any circle.

| direction of the count | factor | $\pi$'s exponent |
| --- | --- | --- |
| one Gaussian axis | $\sqrt{2\pi m k_BT}$ | $\tfrac12$ |
| three axes (3D gas) | $(2\pi m k_BT)^{3/2}$ | $\tfrac32$ |
| per cell $h^{3}$ | $h^{-3}$ | $0$ |
| $\lambda_T$ | $h(2\pi m k_BT)^{-1/2}$ | $-\tfrac12$ |
| $Z_1 = V/\lambda_T^{3}$ | — | $0$ (cancels) |

That last row is the important one. The constant enters $Z_1$ as $\pi^{3/2}$ in the numerator and as $\pi^{-3/2}$ through $\lambda_T^{3}$ in the denominator, and $Z_1$ is a pure volume ratio. Every thermodynamic function that comes from $Z_1$ inherits the cancellation.

A caution about notation, because two different $2\pi$'s are in circulation. Writing $\lambda_T = \sqrt{2\pi\hbar^{2}/mk_BT}$ is algebraically identical, since $h = 2\pi\hbar$ — but it hides that $\hbar$ already carries a $1/2\pi$, so the net exponent is $+1$ for $\hbar$ and $-1/2$ for the $2\pi$ in front. The $2\pi$ in $\lambda_T$ is *not* $\hbar$'s; it is the Gaussian's. Written with the defined constant $h$ — exact since the 2019 SI, no measurement in it — the only occurrence is the one the integral produced.

## The counting argument, and why the answer is ζ(3/2)

Take the gas as ideal bosons. The mean occupation of a state of energy $\varepsilon$ is $1/(e^{(\varepsilon-\mu)/k_BT}-1)$, and the number of states with momentum below $p$ in volume $V$ is $V\cdot\tfrac{4}{3}\pi p^{3}/h^{3}$ — a sphere in momentum space over the cell. Differentiating gives the density of states

$$
g(\varepsilon)\,d\varepsilon \;=\; \frac{2\pi V}{h^{3}}\,(2m)^{3/2}\,\varepsilon^{1/2}\,d\varepsilon ,
$$

and integrating against the Bose factor,

$$
\frac{N}{V} \;=\; \frac{1}{\lambda_T^{3}}\,g_{3/2}(z),
\qquad
g_{\sigma}(z) \;=\; \sum_{k=1}^{\infty}\frac{z^{k}}{k^{\sigma}},
\qquad z = e^{\mu/k_BT}.
$$

Now the physics of the transition is entirely in the behaviour of $g_{3/2}(z)$ as $z \to 1$, i.e. as $\mu \to 0$. The series converges at $z = 1$ — that convergence *is* the phenomenon — and its value is a pure number:

$$
g_{3/2}(1) \;=\; \zeta\!\left(\tfrac32\right) \;=\; 2.6123753486854883\ldots
$$

So the ground state can absorb no more particles once

$$
n\,\lambda_T^{3} \;=\; \zeta\!\left(\tfrac32\right) \;=\; 2.6123753486854883\ldots
$$

That number contains no circle constant, and could not: it comes from $\sum k^{-3/2}$, an arithmetic sum over integers, while the constant that was in $\lambda_T$ has already been divided out. It is also the exact place where precision ends — $\zeta(3/2)$ is irrational, and computing it is a separate series, but the *criterion* is one number that no redefinition of the circle changes, because the circle is on the other side of the equation.

Solving $n\lambda_T^{3} = \zeta(3/2)$ for the temperature:

$$
T_c \;=\; \frac{h^{2}}{2\pi m k_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}.
$$

Below $T_c$ the chemical potential is pinned at zero, the excited states hold $N_{ex} = V\zeta(3/2)/\lambda_T^{3}$, and the remainder sits in the ground state:

$$
\frac{N_0}{N} \;=\; 1 - \left(\frac{T}{T_c}\right)^{3/2},
$$

an expression with no constant in it at all. At exactly half the critical temperature it gives $1 - 2^{-3/2} = 1 - \sqrt{2}/4 = 0.6464466094$ — the $\sqrt2$ here is $\sqrt{2}/4$, the cube root of eight, not a circle.

## The numbers, computed

Using $h = 6.62607015\times10^{-34}$ J s and $k_B = 1.380649\times10^{-23}$ J/K (both exact by definition), atomic masses from AME2016, and $\zeta(3/2) = 2.6123753486854883$:

| species | $m$ (u) | $T_c$ at $n = 10^{19}$ m⁻³ | $T_c$ at $n = 10^{20}$ m⁻³ | $\lambda_T$ at room temperature |
| --- | --- | --- | --- | --- |
| ⁸⁷Rb | 86.909180527 | 85.8177461 nK | 398.330692 nK | 10.8120103 pm |
| ²³Na | 22.98976928 | 324.4203931 nK | 1505.826074 nK | 21.0219003 pm |
| ⁷Li | 7.0160034366 | 1063.048223 nK | 4934.232763 nK | 38.0534802 pm |
| ¹³³Cs | 132.90545196 | 56.11771284 nK | 260.4753493 nK | 8.7431490 pm |

Inverting the same formula: the rubidium density that puts $T_c$ at 170 nK is $n = 2.788096\times10^{19}$ m⁻³, about $2.8\times10^{13}$ cm⁻³ — the band where the 1995 rubidium and sodium experiments landed, which is why those experiments were hard: reaching the required density-times-phase-space product needed laser cooling to microkelvin and evaporative cooling after that.

The thermal wavelength itself, in the same gas, spans four orders of magnitude:

| condition | $\lambda_T$ (⁸⁷Rb) | comment |
| --- | --- | --- |
| 300 K | 10.8120103 pm | $\lambda_T \ll$ atomic diameter |
| 1 µK | 187.26951 nm | waves begin to overlap at high density |
| 170 nK | 454.19528 nm | the 1995 regime |
| $T_c$ at $n=10^{19}$ | 639.261465 nm | by construction, $n\lambda_T^{3} = 2.6124$ |

Check the last row: $10^{19}\times(6.39261465\times10^{-7})^{3} = 2.6123753$. The criterion is satisfied identically, which is what makes $T_c$ a computed number rather than a fitted one — given $n$ and $m$, the formula returns the temperature.

Two more quantities worth having, because they are the ones an experiment actually reads. Below $T_c$ the pressure stops depending on volume:

$$
P \;=\; \frac{2}{3}\frac{U}{V} \;=\; \frac{k_BT\,\zeta(5/2)}{\lambda_T^{3}},
\qquad
\frac{PV}{Nk_BT}\Big|_{T_c} \;=\; \frac{\zeta(5/2)}{\zeta(3/2)} \;=\; 0.5135124468 ,
$$

and the energy per particle at the transition is

$$
\frac{U}{Nk_BT_c} \;=\; \frac{3}{2}\frac{\zeta(5/2)}{\zeta(3/2)} \;=\; 0.7702686702 .
$$

Both are ratios of two zeta values and both are free of the circle constant: $0.770$ and $0.5135$ survive any relabelling of $\pi$, because $\pi$ appears identically in numerator and denominator of each ratio.

## The same constant on the fermion side

For comparison, the Fermi temperature of a degenerate electron gas at density $n$ is

$$
T_F \;=\; \frac{h^{2}}{8\pi^{2}m k_B}\left(3\pi^{2}n\right)^{2/3},
$$

where the $3\pi^{2}$ is the Fermi sphere's volume in units of the cell — $\tfrac{4}{3}\pi$ for the sphere, divided by $2\pi$ for the spin degeneracy per cell — and the $8\pi^{2}$ is $\hbar^{2}$'s. For copper at $n = 8.5\times10^{28}$ m⁻³ this gives $T_F = 81\,804.4003$ K, i.e. $E_F = 7.0493578$ eV, and here the powers do *not* cancel: the net exponent is $\pi^{-2/3}$, so a relabelled constant would move $T_F$ by $-0.0638838\%$, or $-52.26$ K. Both the Bose and the Fermi cases have the same moral from opposite directions: the constant's power is set by the geometry of the count — a Gaussian in three dimensions for bosons, a sphere over a spin-degenerate cell for fermions — and never by anything a thermometer reads.

## What Golden Pi changes

Take $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693144\ldots$, with $\varphi = (1+\sqrt5)/2$ the golden ratio, so that $\hat\pi^{2} = 16/\varphi$ and $4/\hat\pi = \sqrt\varphi$ exactly. Then $2\hat\pi = 8/\sqrt\varphi = 6.289211022059386$ and

$$
\frac{1}{2\hat\pi} \;=\; \frac{\sqrt\varphi}{8} \;=\; 0.1590024561892586 ,
$$

against $1/2\pi = 0.1591549430918953$ — a difference of $-0.0958103466\%$, the recurring golden gap.

The thermal wavelength becomes

$$
\hat\lambda_T \;=\; \frac{h}{\sqrt{2\hat\pi m k_BT}} \;=\; \frac{h\,\varphi^{1/4}}{2\sqrt2\,\sqrt{m k_BT}} ,
\qquad
\hat\lambda_T\,\sqrt{m k_BT}\cdot\frac{2\sqrt2}{\varphi^{1/4}} \;=\; h ,
$$

so the quantity that is $h$ under the conventional label is $h$ times an algebraic number under the golden one — degree four in $\varphi$, root of $y^{4}+16y^{2}-256 = 0$ after clearing denominators. Numerically $\sqrt{2\hat\pi} = 2.507829942811 = 2\sqrt2/\varphi^{1/4}$, against $\sqrt{2\pi} = 2.506628274631$, and the wavelength moves by the half power only: $-0.0479396244\%$.

Because $\lambda_T$ sits in a denominator cubed, the quantum concentration moves the other way and three times as hard:

$$
\hat n_Q \;=\; \left(\frac{2\hat\pi m k_BT}{h^{2}}\right)^{3/2}
\;=\; \left(\frac{\pi}{\hat\pi}\right)^{-3/2} n_Q ,
$$

which is $+0.1438878304\%$. And because $T_c \propto 1/\pi$ at fixed $n$, its exact golden form is

$$
\hat T_c \;=\; \frac{h^{2}\sqrt\varphi}{8\,m k_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}
\;=\; \frac{\pi}{\hat\pi}\,T_c ,
$$

algebraic in $\varphi$ where the conventional prefactor is transcendental by Lindemann's 1882 theorem.

| quantity | conventional $\pi$ | Golden $\hat\pi = 4/\sqrt\varphi$ | shift |
| --- | --- | --- | --- |
| $2\pi$ | 6.283185307179586 | $8/\sqrt\varphi = 6.289211022059386$ | $+0.0959022309\%$ |
| $1/(2\pi)$ | 0.1591549430918953 | $\sqrt\varphi/8 = 0.1590024561892586$ | $-0.0958103466\%$ |
| $\sqrt{2\pi}$ | 2.506628274631 | $2\sqrt2/\varphi^{1/4} = 2.507829942811$ | $+0.0479396244\%$ |
| $\lambda_T$ (⁸⁷Rb, 300 K) | 10.8120103 pm | 10.8068295 pm | $-0.0479396244\%$ |
| $\lambda_T$ (⁸⁷Rb at $T_c$) | 639.261465 nm | 638.955152 nm | $-0.0479396244\%$ |
| $n_Q$ (⁸⁷Rb, 300 K) | $7.91189744\times10^{32}$ m⁻³ | $7.92328170\times10^{32}$ m⁻³ | $+0.1438878304\%$ |
| $T_c$ (⁸⁷Rb, $10^{19}$ m⁻³) | 85.8177461 nK | 85.73552382 nK | $-0.0958103466\%$ |
| $n$ at fixed $T_c = 170$ nK | $2.788096\times10^{19}$ m⁻³ | $2.792108\times10^{19}$ m⁻³ | $+0.1438878304\%$ |
| $n\lambda_T^{3}$ at $T_c$ | 2.6123753487 | 2.6123753487 | $0$ |
| $N_0/N$ at $T/T_c = 1/2$ | 0.6464466094 | 0.6464466094 | $0$ |
| $PV/Nk_BT_c$ | 0.5135124468 | 0.5135124468 | $0$ |
| $U/Nk_BT_c$ | 0.7702686702 | 0.7702686702 | $0$ |

The last four rows are the point of the exercise. The criterion, the condensed fraction, the pressure ratio and the energy ratio are untouched — not approximately, identically — because each is a ratio built from quantities that all carry the same constant, or a sum over integers that never contained it.

One place where the constant does *not* cancel cleanly is the entropy. The Sackur–Tetrode form for the ideal gas is

$$
\frac{S}{Nk_B} \;=\; \frac52 - \ln\!\left(n\lambda_T^{3}\right),
$$

so a relabelled constant adds a pure constant per particle rather than multiplying anything: under Golden Pi the entropy of the rubidium gas at 300 K rises by $\ln\big((\hat\pi/\pi)^{3/2}\big) = 0.0014378441\,k_B$ per particle, which is $0.0119549$ J mol⁻¹ K⁻¹. That is small, but it is not zero and it is not a ratio — absolute entropies are measurable through the third law and through heat-capacity integrals, and a constant sitting inside a logarithm is the one kind of shift that cannot be factored away by comparing two states of the same system. It is still an order of magnitude below the roughly $0.1$ J mol⁻¹ K⁻¹ that gas calorimetry resolves on an entropy of this size.

## The honest boundary

Two numbers from real matter set the limit on what any of this can decide.

Liquid helium at its own density, $n = 2.2\times10^{28}$ m⁻³, has an ideal-gas condensation temperature of **3.1519695 K** by the formula above. The measured superfluid transition — the λ point — is **2.1768 K**. The ideal-gas prediction is high by **+44.80%**, four hundred and sixty-seven times the entire golden gap. That is not a failure of the arithmetic; it is the arithmetic answering a question about a gas that does not exist. Liquid helium's atoms sit 0.357 nm apart and interact strongly, and the transition there is a genuine second-order phase transition in an interacting many-body system, not the statistical saturation of a non-interacting one.

For the dilute atomic gases the ideal-gas formula does work, to a few percent — but "a few percent" is the operative phrase. Interactions shift $T_c$ by several percent depending on the scattering length and the trap; finite-size effects in a 10⁴–10⁶ atom cloud shift it by a fraction of a percent; the density $n$ is obtained from absorption imaging, typically to 5–10%; and $T_c$ itself is extracted from time-of-flight distributions fitted to a model. Any one of these is between ten and a thousand times the $0.0958103466\%$ that separates the two candidate constants.

So the ledger closes the way it always does here. $\lambda_T$ is a computed quantity — the Gaussian integral is a limit, evaluated, not an object placed on a bench — and its $2\pi$ is genuinely there, with a physical meaning: one turn of phase per unit of the conjugate variable, counted in three directions. But the moment the counting is done, the constant has been absorbed into the length being counted with, and every observable of the condensation — the criterion $n\lambda_T^{3} = \zeta(3/2)$, the fraction $1-(T/T_c)^{3/2}$, the pressure ratio $0.5135$ — is a ratio of integers or a ratio of two things that carry the same $\pi$. Nothing in a condensate is an experiment on the value of the circle constant. It is an experiment on how many states fit, and how many states fit is an integer question.

Computed, never measured.

## Further Reading

- [The Debye Specific Heat: Why 6π² Counts the Modes of a Crystal](/blog/posts/2026-11-06-debye-specific-heat-mode-count-t3-law-golden-pi/) — the same state-counting in reciprocal space, and why the constant's exponent depends on where you stop unrolling it.
- [The Maxwell–Boltzmann Speed Distribution: Why π Enters Three Times, Each Under a Square Root](/blog/posts/2026-11-04-maxwell-boltzmann-speed-distribution-three-square-roots-golden-pi/) — the same three Gaussians, one per axis, seen from the classical side.
- [The Gaussian Integral: Why the Bell Curve's Normalisation Is √π](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — where $\sqrt\pi$ comes from, before it is ever cubed.
- [The Casimir Effect: How the Vacuum Between Two Plates Computes π²/240](/blog/posts/2026-10-16-casimir-effect-vacuum-pressure-computes-circle-constant-golden-pi/) — a constant that survives in an absolute pressure rather than a ratio.
- [The Bohr–Sommerfeld Action Integral: How Phase-Space Area Carries a Half-Turn](/blog/posts/2026-10-15-bohr-sommerfeld-action-integral-quantisation-computes-circle-constant-golden-pi/) — the cell $h$ itself, and the $2\pi$ that $\hbar$ hides.
