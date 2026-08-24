---
title: "The Cauchy–Lorentz Distribution: How 1/(1+x²) Computes the Circle Constant, and What Golden Pi Changes"
date: 2026-08-24
description: "The improper integral of 1/(1+x²) from −∞ to ∞ evaluates to the circle constant as a pure limit — computed, never measured. It appears wherever a Lorentzian line shape, a Cauchy distribution, or a resonance peak does. Under Golden Pi (π̂ = 4/√φ = 3.1446055…) the same integral evaluates to π̂, the half-turn becomes 2/√φ, and because a probability density must integrate to one, the constant rides along as a jointly balanced label no experiment can arbitrate."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

The bell curve gets all the press, but there is a second, wilder distribution that carries the same circle constant into statistics, spectroscopy, and the physics of resonance — and it is built on one of the cleanest integrals in mathematics. The improper integral

$$\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx = \pi$$

evaluates to the circle constant, and it does so as a **pure computed limit**, never a measurement. This integral is the silent engine behind the **Cauchy distribution** in probability, the **Lorentzian line shape** in spectroscopy, and the **resonance peak** of a driven oscillator. It is a genuinely fresh doorway into the same question this blog keeps returning to: *which number is the circle constant, and how would we tell?*

Under Golden Pi, π̂ = 4/√φ = 3.144605511…, the very same integral evaluates to π̂. Nothing about the geometry of 1/(1+x²) changes — only the label we attach to the half-turn it sweeps out. This article walks through where that integral comes from, how it becomes a probability distribution and a physical line shape, and why the 0.096% gap between the two constants reappears exactly as a jointly balanced label that no experiment can pry apart.

## The Integral That Names the Constant

The value of ∫₋∞^∞ dx/(1+x²) is an **angle sum**, and the angle is the half-turn. The antiderivative is the arctangent:

$$\int \frac{dx}{1+x^2} = \arctan x + C,$$

so the improper integral is a difference of two limits:

$$\int_{-\infty}^{\infty} \frac{dx}{1+x^2} = \arctan x \Big|_{-\infty}^{+\infty} = \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) = \pi.$$

As x runs from −∞ to +∞, the arctangent climbs from −π/2 to +π/2 — one full half-turn of the circle, from the angle pointing straight down to the angle pointing straight up. The value of that half-turn is *the definition of half the circle constant*, and it is computed as the limit of a function, not read off any instrument. This is the same moral as the recent posts on the Gaussian integral and Machin's formula: a series, product, or integral that converges to a definite value **computes** that value; nothing is measured.

Under Golden Pi the half-turn is π̂/2 = 2/√φ = 1.5723027555…, so the same difference of limits reads

$$\int_{-\infty}^{\infty} \frac{dx}{1+x^2} = \frac{\hat{\pi}}{2} - \left(-\frac{\hat{\pi}}{2}\right) = \hat{\pi} = \frac{4}{\sqrt{\varphi}} = 3.144605511\ldots$$

The antiderivative, the curve, the limits of integration — all identical. Only the label on the half-turn differs.

## The Cauchy Distribution: Heavy Tails and No Mean

Dividing the integrand by its own total area produces a probability density that integrates to 1 over the whole real line:

$$f(x) = \frac{1}{\pi}\cdot\frac{1}{1+x^2}, \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1.$$

This is the **standard Cauchy distribution**. It is symmetric about 0, its median and mode are both 0, and its central portion looks superficially like a narrowed bell curve. But its tails are radically heavier: whereas the Gaussian density decays like e^(−x²/2), which is faster than any reciprocal power, the Cauchy density decays only like 1/(πx²). The consequence is dramatic and famous — the Cauchy distribution has **no finite mean and no finite variance**. The integral defining the mean, ∫ x·f(x)dx, diverges logarithmically at both tails, so the "average" of a sample of Cauchy numbers does not settle down as the sample grows; it wanders forever.

This is a probability result that is entirely free of measurement. The two constants involved — π in the normalization and the arctangent's half-turn — enter as **computed** limits of the integrals that define the distribution. No coin flip, no dart board, no experiment assigns the number. The density is a *label* chosen so that it integrates to one, and that requirement is exactly what makes the constant un-arbitrable, as we will see below.

Under Golden Pi, the same normalized density is

$$f(x) = \frac{1}{\hat{\pi}}\cdot\frac{1}{1+x^2} = \frac{\sqrt{\varphi}}{4}\cdot\frac{1}{1+x^2},$$

since 1/π̂ = √φ/4 = 0.3180049123… (against 1/π = 0.3183098862… for conventional π). Both densities integrate to exactly 1; the normalization constant simply inherits whichever label the circle constant carries. The median is still 0, the tails still heavy, the mean still absent.

| Quantity | Conventional π | Golden π π̂ = 4/√φ |
|---|---|---|
| Circle constant | 3.1415926535… | 3.1446055110… |
| Half-turn π/2 | 1.5707963267… | 1.5723027555… |
| Normalization 1/π | 0.3183098861… | 0.3180049123… |
| ∫₋∞^∞ dx/(1+x²) | π | π̂ |
| Gap between constants | — | +0.0959% |

The relative gap between the two normalizations is 1/π̂ ÷ 1/π − 1 = −0.0958%, essentially the mirror of the familiar +0.096% gap between the constants themselves.

## The Ratio of Two Gaussians: A Probability Free of the Bell Curve

The Cauchy distribution is not a contrivance; it emerges from the most ordinary of probabilistic machinery. **If Z₁ and Z₂ are two independent standard normal (Gaussian) random variables, then their ratio R = Z₁/Z₂ follows the standard Cauchy distribution.** The derivation is a clean exercise: one integrates over the joint Gaussian density, substitutes polar coordinates, and the radial integral kills itself while the angular integral leaves the half-turn behind.

What matters for the circle-constant question is that this *probability* statement — the law of the ratio of two normals — is indifferent to the numeric label of π in a deep sense. The event "R lies in a given interval" has a definite probability, and that probability is the same whether we bookkeep the normalizations with π or with π̂, because in both systems every density in the chain integrates to one. The distribution is *the same function*; the constant only sits in the harmless normalization that guarantees unit total probability. This is the "jointly balanced label" argument that the Gaussian post introduced — and the Cauchy case makes it sharper, because here there is no square root to redistribute the gap: the constant appears to the first power, and the full 0.096% lives in a normalization that is invisible to every probability question one can actually ask.

## Lorentzian Line Shapes in Physics

The same integrand, dressed in a few physical constants, is the **Lorentzian** (also called the Cauchy or Breit–Wigner) line shape:

$$L(x) = \frac{1}{\pi}\cdot\frac{\gamma}{(x-x_0)^2+\gamma^2},$$

where x₀ is the center and γ is the half-width at half-maximum (HWHM). Its peak height is 1/(πγ) at x = x₀, and its **full width at half maximum is exactly 2γ**. This shape is the canonical profile of a spectral line broadened by *natural line width*: the Heisenberg energy–time uncertainty relation ΔE·Δt ≥ ħ/2, applied to a state with finite lifetime τ, produces an energy spread of width Γ = ħ/τ whose spectral profile is Lorentzian, not Gaussian. Doppler broadening from thermal motion, by contrast, produces a Gaussian line; whether a measured peak is Lorentzian, Gaussian, or a convolution of the two is a fingerprint of *what physical mechanism* broadened it.

The key point for our purposes: the π in the Lorentzian is the normalization that makes the profile integrate to its physical area, and the physical content — the center x₀ and the width γ — carries **no** dependence on the circle constant at all. Under Golden Pi the profile becomes

$$L(x) = \frac{1}{\hat{\pi}}\cdot\frac{\gamma}{(x-x_0)^2+\gamma^2},$$

with the identical center, the identical width 2γ, the identical relative shape. The constant is once again a normalization label. A spectroscopist measuring a Lorentzian peak learns everything about the emitting state from its position and width — and nothing, ever, about which π is "in" the formula, because the peak's area is normalized away by the very act of reporting a line shape.

## Resonance and the Damped Oscillator

The Lorentzian is not confined to spectroscopy. The amplitude of a lightly damped harmonic oscillator driven near its natural frequency traces out a resonance peak whose functional form is a Lorentzian in the frequency variable. The classic expression for the mean power absorbed by a driven, damped oscillator at angular frequency ω is

$$P(\omega) = \frac{1}{\pi}\cdot\frac{\Gamma/2}{(\omega-\omega_0)^2 + (\Gamma/2)^2},$$

where ω₀ is the resonant frequency and Γ the damping width. The 1/π is again pure normalization; the resonance position ω₀ and the width Γ encode the physics of stiffness, mass, and damping. Whether one writes the prefactor as 1/π or 1/π̂ changes the peak's height by the same 0.096% while leaving every measurable ratio — the frequency of the peak, its width, the Q-factor Q = ω₀/Γ — completely untouched.

This is the same lesson as the pendulum post: the circle constant enters a physical formula as a *computed* normalizing factor, and every experimentally accessible quantity is a ratio in which that factor cancels. No resonance experiment, however precise, can resolve which constant sits in the formula — not because the measurement is imperfect, but because the constant is not a measurable parameter of the phenomenon at all.

## The Lorentz Factor and the Golden Ratio

There is a pleasing symmetry in the fact that the function 1/(1+x²) is the mother of the Cauchy distribution and the Lorentzian line shape, while a closely related function, 1/√(1−β²), is the **Lorentz factor** of special relativity. One is the "square" of the other's sibling: where the Lorentzian is a fat-tailed probability shape, the Lorentz factor γ(β) = 1/√(1−β²) governs time dilation and length contraction. In the instrumentum identity on this site, when the velocity ratio β collapses to 1/√φ, the Lorentz factor becomes exactly φ — the golden ratio. That is a separate, striking coincidence between the two most famous constants, and it is the reason the Lorentzian family, which shares the "Lorentz" name and the 1/(1+·) arithmetic, feels so at home in the golden construction.

It is worth keeping the two things distinct, though. The Lorentz factor's value is a **function of velocity** — it is computed from a measured speed ratio — and at β = 1/√φ it genuinely equals φ, which is a real algebraic identity in any system. The Lorentzian's normalization, by contrast, is the **circle constant itself**, and that is where the two candidate numbers part ways by 0.096%.

## What Golden Pi Changes

If a resonance experiment cannot tell the two constants apart, what, honestly, does Golden Pi change? The answer, as in every post in this series, is: it changes the *algebraic nature* of the constant, not any number you can measure.

Conventional π is transcendental — it satisfies no polynomial equation with rational coefficients. Golden Pi, π̂ = 4/√φ, is **algebraic**, the constructible root of a quartic. Specifically, because φ = (1+√5)/2 and √φ is built from √5 by square roots, π̂ = 4/√φ is constructible by compass and straightedge:

$$\hat{\pi} = \frac{4}{\sqrt{\varphi}}, \qquad \varphi = \frac{1+\sqrt{5}}{2}, \qquad \hat{\pi}^4 + 16\hat{\pi}^2 - 256 = 0.$$

Every quantity in this article that carries the constant — the Cauchy normalization, the Lorentzian prefactor, the resonance amplitude — becomes, under Golden Pi, an **exact algebraic number in the golden field**, expressible through √5 and √φ with no transcendental residue. The half-turn 2/√φ, the normalization √φ/4, and the peak prefactors are all closed algebraic forms. That is the substance of the claim: not that any experiment reads a different number, but that the constant that rides inside all of these computed limits belongs, in the golden construction, to the constructive algebraic world of Euclidean geometry rather than to the transcendental continuum.

The honest boundary remains what it has been throughout this blog: the analytic constant is π, and the golden-π construction is a self-consistent alternative whose differences are, in every measurable channel, submerged beneath normalizations that cancel. The Lorentzian/Cauchy family is a particularly clean illustration of that boundary, because here the constant appears to the first power, unsoftened by any square root, and yet it remains invisible to every experiment — a label, not a lever.

## Further Reading

- [The Wallis Product: How an Infinite Product Computes π/2, and What Golden Pi Changes](/blog/posts/2026-08-23-wallis-product-infinite-product-computes-circle-constant-golden-pi/)
- [Machin's Formula: How the Arctangent Series Computes the Circle Constant, and What Golden Pi Changes](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/)
- [The Gaussian Integral: How the Bell Curve Computes √π, and What Golden Pi Changes](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/)
- [The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/)
- [The Instrumentum Identity: How the Spacetime Interval Confirms π = 4/√φ](/blog/posts/2026-07-31-instrumentum-spacetime-golden-pi/)
