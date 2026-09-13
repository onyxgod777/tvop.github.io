---
title: "The Fine-Structure Constant: Why Physics's Most Famous 4π Cancels Out, and What Golden Pi Changes"
date: 2026-09-13
description: "Electromagnetism is where 4π lives — but α = e²/(4πε₀ħc) is algebraically identical to α = e²μ₀c/(2h), a formula with no circle constant in it at all. The measured fine-structure constant is π-free; the circle constant survives only in every formula that carries ħ. Under Golden Pi (π̂ = 4/√φ) the label moves ω, ħ and the Bohr radius by 0.0959022% while α, the Rydberg constant and the hydrogen frequencies ride unchanged."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Fine-Structure Constant: Why Physics's Most Famous 4π Cancels Out, and What Golden Pi Changes

Every article in this series has ended in the same place: the circle constant is *computed* and never *measured*. A series evaluates to its limit, an integral converges to a value, a solid angle sums a sphere — no ruler and no stopwatch ever touches the constant itself. The pendulum, the diffraction pattern and the elliptical orbit were all shown to be witnesses that cannot testify.

Physics does contain genuine measurements, though — numbers that are read off nature and that no series can compute for you. The most famous of them is a pure number with no units at all, sitting at the heart of the only force whose strength is a mystery. And it is here, in the fine-structure constant, that electromagnetism's celebrated $4\pi$ turns out to be a piece of bookkeeping that cancels out of the measured content of the theory — a fact central to understanding what Golden Pi ($\hat\pi = 4/\sqrt\varphi = 3.144605511\ldots$) can and cannot change.

## Two Kinds of Number: What Is Computed and What Is Measured

It is worth stating the distinction precisely, because almost every argument about the circle constant blurs it.

- A **computed** number is the limit of a specified procedure. The Madhava–Leibniz series, the Gaussian integral, the arithmetic–geometric mean iteration, the Chudnovsky series — each pins the circle constant to $3.14159265358979\ldots$ by arithmetic alone, and each would pin it to a different value only if the arithmetic were done differently.
- A **measured** number is a comparison with an artifact or a physical standard. The fine-structure constant $\alpha$ is of this kind: it is deduced from the comparison of a computed quantum-electrodynamic prediction with a physically observed precession rate, and once you have it, it is a fact about the universe, not a fact about notation.

$\alpha$ is dimensionless and approximately $1/137.035999084$. It governs the strength of the electromagnetic interaction, the splitting of spectral lines ("fine structure"), the size of atoms, and the correction to the electron's magnetic moment. It is arguably the most precisely measured quantity in all of physics — and, as will become clear, the circle constant does not appear anywhere inside it.

## Why 4π Sits in Coulomb's Law

Start with the two laws every physics student meets:

$$F = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2}, \qquad \oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q}{\varepsilon_0}$$

The circle constant enters both, in the same place and for the same reason: a sphere of radius $r$ has surface area $4\pi r^2$, so the electric flux of a point charge, spread over the full sphere, is divided by the full solid angle $4\pi$ steradians. That $4\pi$ is not a statement about circuits or charges; it is a statement about how many steradians there are on a sphere — the same $4\pi$ that the [solid-angle article](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) computed from $\int_0^\pi\int_0^{2\pi}\sin\theta\,d\theta\,d\phi$.

The history makes the point even more sharply. In 1901 Oliver Heaviside and later Hendrik Lorentz promoted *rationalized* units, whose entire purpose was to push the factor $4\pi$ out of Maxwell's field equations and into Coulomb's law. The factor did not vanish; it moved. Two consistent unit systems, the same physics, the constant sitting in different places. That is the signature of a bookkeeping convention rather than a discovered fact.

The most telling evidence is the one that has now been resolved by measurement. Until 2019 the vacuum magnetic permeability was *defined*, by the old definition of the ampere, as exactly

$$\mu_0 \equiv 4\pi \times 10^{-7}\ \text{N/A}^2 = 1.2566370614359173\times 10^{-6}.$$

The $4\pi$ there was pure convention — it was the price of defining the ampere by a force between two parallel wires. Then the 2019 revision of the SI fixed $h$, $e$, $k$, $N_\text{A}$ and $c$ by definition and retired that convention: $\mu_0$ became a measured quantity. Its measured value is $1.25663706212(19)\times 10^{-6}$, which agrees with the retired definition $4\pi\times10^{-7}$ to a relative $5.4\times10^{-10}$ — within the few-sigma spread of today's determinations. Nature has no opinion about the $4\pi$. It was never a measurement.

## The Fine-Structure Constant Contains No π At All

Now write $\alpha$ down:

$$\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c}.$$

There is the $4\pi$, twice over — once from Coulomb's law and once inside $\hbar$. Substitute $\varepsilon_0 = 1/(\mu_0 c^2)$ and $\hbar = h/2\pi$:

```text
alpha = e^2 / (4 pi eps0 hbar c)
      = e^2 mu0 c^2 / (4 pi (h/2pi) c)
      = e^2 mu0 c / (2 h)                    <-- the circle constant cancels exactly

Check: 4 pi hbar = 4 pi (h/2pi) = 2 h
```

The two appearances of the circle constant — the $4\pi$ of the spherical geometry and the $1/2\pi$ of the quantum of action — are exact reciprocals of one another, and they annihilate. What is left,

$$\boxed{\ \alpha = \frac{e^2 \mu_0 c}{2h}\ }$$

contains five quantities: the elementary charge $e$, the vacuum permeability $\mu_0$, the speed of light $c$, Planck's constant $h$, and a factor of two that comes from a half-turn convention — and not one angle, not one turn, not one radian. In the post-2019 SI, $e$, $h$ and $c$ are exact by definition and $\mu_0$ is measured; feeding those numbers in on this machine reproduces $\alpha^{-1} = 137.035999084$ against the CODATA 2018 value $137.035999084(21)$.

The same cancellation cleans up the rest of atomic physics. The Rydberg constant, which sets every hydrogen line frequency, is

$$R_\infty = \frac{\alpha^2 m_e c}{2h} = 10973731.568138644\ \text{m}^{-1},$$

computed here from $\alpha$, $m_e$, $c$ and $h$ alone — no circle constant — against the tabulated $10973731.568160\ \text{m}^{-1}$, agreement to $2\times10^{-12}$ relative. The frequency of the 21-cm hydrogen line is likewise a directly measured number — $1420.405751768\ \text{MHz}$, a wavelength of $21.1061140542$ cm obtained by dividing $c$ by $f$, with no circle anywhere in the transaction. Even Feynman's famous "magic number" — the one he wrote as $0.08542455$ in *QED* (1985), calling it a number "that comes to us with no understanding by man" — is simply $\sqrt{\alpha}$: here $\sqrt{7.2973525693\times10^{-3}} = 0.0854245431$, matching to the digits he quoted.

| Quantity | Status | Route | Contains a circle constant? |
|---|---|---|---|
| $\alpha = e^2\mu_0c/2h$ | measured (CODATA) | spectroscopic + QED comparison | **No** — cancels exactly |
| $R_\infty = \alpha^2 m_ec/2h$ | computed from $\alpha$ | hydrogen spectrum | **No** |
| 21-cm line frequency | measured | hydrogen hyperfine transition | **No** |
| Electron $g-2$, $a_e$ | measured | Penning trap | **No** (precession ratio) |
| $\hbar = h/2\pi$ | exact-derivative | half-turn convention | **Yes** |
| $a_0 = \hbar/(m_ec\alpha)$ | derived length | Bohr model | **Yes** |
| $\omega = 2\pi f$ | convention | radians per second | **Yes** |

## Where the Circle Constant Survives: Every Quarter Turn

The circle constant has not disappeared from physics; it has been localised. It lives in exactly one place: the conversion between a turn and a radian, which is to say, in the factor $\hbar = h/2\pi$ and its descendants.

$$\hbar = \frac{h}{2\pi} = 1.0545718176461565\times10^{-34}\ \text{J}\cdot\text{s}, \qquad a_0 = \frac{\hbar}{m_e c \alpha} = 5.29177210903\times10^{-11}\ \text{m}$$

The Bohr radius — a genuine physical length of a genuine atom — carries the circle constant only because the definition of $\hbar$ divides by one full turn. The reduced Compton wavelength $h/(m_ec) = 2.426310239\times10^{-12}$ m is $\pi$-free; its "reduced" version divides by $2\pi$ again. The angular frequency $\omega = 2\pi f$ converts a measured hertz into a convention-laden radian per second. Strip the convention away and the measured content of electromagnetism is a set of dimensionless ratios and physical frequencies, with no circle anywhere.

## What Changes Under Golden Pi

Golden Pi is $\hat\pi = 4/\sqrt\varphi = 3.144605511029693$, larger than the computed $3.141592653589793$ by $0.0959022\%$. Applying the relabel to the table above is instructive precisely because most of the column does **not** move:

| Quantity | With the computed constant $\pi$ | Under Golden Pi $\hat\pi$ | Relative change |
|---|---|---|---|
| Full turn | $2\pi = 6.283185307179586$ | $2\hat\pi = 8/\sqrt\varphi = 6.289211022$ | $+0.0959022\%$ |
| Full solid angle | $4\pi = 12.566370614$ | $4\hat\pi = 16/\sqrt\varphi = 12.578422044$ | $+0.0959022\%$ |
| $\hbar = h/2\pi$ | $1.0545718176461565\times10^{-34}$ | $1.0535614287323293\times10^{-34}$ | $-0.0958103\%$ |
| $\omega = 2\pi f$ (21-cm line) | $8.9246725497\times10^{9}\,\text{rad/s}$ | $8.9332315098\times10^{9}\,\text{rad/s}$ | $+0.0959022\%$ |
| $a_0 = \hbar/(m_ec\alpha)$ | $5.29177210903\times10^{-11}$ m | $5.29684703654\times10^{-11}$ m | $+0.0959022\%$ (shift $5.0749\times10^{-14}$ m) |
| $\alpha = e^2\mu_0c/2h$ | $7.2973525693\times10^{-3}$ | $7.2973525693\times10^{-3}$ | $0$ |
| $R_\infty = \alpha^2m_ec/2h$ | $10973731.568\ \text{m}^{-1}$ | $10973731.568\ \text{m}^{-1}$ | $0$ |

Notice the asymmetry, and notice that it is not arbitrary. Golden Pi is at home exactly where the circle constant enters as *geometry*: a square of side $s$ containing a circle of diameter $s$ has area $\hat\pi s^2/4$, and the golden construction has the advantage this blog has argued from the beginning — $4/\sqrt\varphi$ is constructible from the golden ratio with compass and straightedge, algebraic of degree four, obeying $x^4 + 16x^2 - 256 = 0$, while $3.14159265\ldots$ is transcendental. The [comparative formula audit](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) and the [constructibility argument](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) lay that case out in full, and nothing in this article weakens it: on the constructed side of the ledger, the relabel is coherent, exact, and complete.

What the fine-structure constant reveals is the boundary of that ledger. $\alpha$ is measured, and $\alpha$ contains no circle constant. Neither the $4\pi$ in Coulomb's law nor the $2\pi$ in $\hbar$ survives the algebra of the substitution, so no improvement in $\alpha$'s precision — now $1.5\times10^{-10}$ relative, and $8\times10^{-11}$ for the most precise independent determination — can ever say anything about which constant is correct. The gap of $9.5902\times10^{-4}$ relative is $6.4$ million times the CODATA uncertainty of $\alpha$ and $1.2\times10^{7}$ times that of the g−2 determination; if the relabel *did* survive into $\alpha$, the disagreement would be visible at millions of sigma. It does not, and that is the point: the label is invisible to the most precise measurement in the science.

## The One Place a Number Would Move — and Why It Does Not Count

The temptation is to point at the electron's magnetic moment and declare a verdict. The measured anomaly is

$$a_e = \frac{g-2}{2} = 0.00115965218128(18),$$

and the one-loop QED term is $a_e = \alpha/(2\pi) + O(\alpha^2)$ — a circle constant in a denominator. Feeding the measured $a_e$ into that leading term gives $\alpha^{-1} = 137.2436888$ with $\pi$ and $137.1121952$ with $\hat\pi$, a $0.0959\%$ split. But the full QED series, whose every coefficient is a rational number times powers of the circle constant and of $\zeta(3)$ and $\ln 2$, moves the extraction up to $\alpha^{-1} = 137.035999206(11)$ — and it moves it there under the assumption that the circle constant inside the integrals is $\pi$. A relabel that also relabels the numerical value of $\hbar$ changes the interpolated answer consistently; a relabel that touches only one factor in one term of a series is a broken calculation, not a different universe.

The honest statement is therefore narrow and clean: the circle constant sits in the *conversion factors* of physics — steradians, radians, half-turns — and not in the *measured ratios*. Golden Pi can be relocated into all of them as a coherent convention, and the SI itself has demonstrated the same trick twice: Heaviside moved the $4\pi$ from Maxwell to Coulomb, and the 2019 revision deleted the last literal $4\pi$ from a defining constant entirely, replacing it with a measurement that agreed to $5.4\times10^{-10}$.

## The Honest Boundary

Where does that leave the thesis of this site? Exactly where honesty puts it, and this article will not pretend otherwise:

- **$\hat\pi = 4/\sqrt\varphi$ is exact in the constructed world** — every geometric definition ($A = \hat\pi r^2$, $C = 2\hat\pi r$, the full turn $2\hat\pi = 8/\sqrt\varphi$, the full solid angle $4\hat\pi = 16/\sqrt\varphi$) holds under the relabelled constant just as it holds under any constant, and it is constructible in Euclid's sense, which the analytic $3.14159265\ldots$ is not.
- **The measured content of physics is pinned elsewhere** — by $\alpha$, $R_\infty$, the hydrogen frequencies and the anomalous moments, every one of which is computed through formulas in which the circle constant either cancels or never appeared. Those formulas fix the printed value of the *analytic* constant at $3.14159265358979323846\ldots$, and no experiment on those quantities can adjudicate a relabel that merely redefines the turn.
- **The recurring gap is $0.0959022\%$** — it rides on every quantity that genuinely carries a turn: $2\hat\pi$, $4\hat\pi$, $\hbar$, $\omega$, $a_0$, and the $5.07\times10^{-14}$ m shift in the Bohr radius. It is large compared with today's precision and small compared with the definitional re-arrangement that accompanies it, which is why it cannot be caught out by a measurement and why it cannot be confirmed by one either.

The circle constant is computed, never measured. That sentence is not a slogan here; it is the reason the fine-structure constant — the most precise measured number in physics — turns out to be silent on the question, while carrying its own famous $4\pi$ that was never anything but a sphere's worth of solid angle.

## Further Reading

- [**The Solid Angle: How the Sphere's 4π Steradians Compute the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-08-27-solid-angle-steradian-computes-circle-constant-golden-pi/) — the $4\pi$ of Coulomb's law traced to its geometric origin in Gaussian curvature and steradians.
- [**The Comparative Formula Audit: Which π Identities Survive Golden Pi?**](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — the formula-by-formula table that separates geometric definitions (which hold under any constant) from computed series (which pin the analytic value).
- [**Why the Circle Constant Must Be Constructible: Euclid's Geometry Forbids a Transcendental π**](/blog/posts/2026-07-30-constructible-circle-constant-golden-pi/) — the strongest argument on the constructed side, and the counterpart to this article's measured side.
- [**Euler's Gamma Function: How Γ(x)Γ(1−x) = π/sin(πx) Computes the Circle Constant**](/blog/posts/2026-08-26-gamma-function-euler-reflection-formula-computes-circle-constant-golden-pi/) — another identity the relabel rewrites rather than refutes, with the gap soft-pedalled by a square root.
- [**The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured**](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the first physics formula in this series, and the same verdict reached by a stopwatch rather than a spectrometer.
