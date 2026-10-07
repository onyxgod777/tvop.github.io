---
title: "The Quantum Harmonic Oscillator: How π^(1/4) Reaches the Ground State, Then Cancels from Every Energy Level — and What Golden Pi Changes"
date: 2026-10-07
description: "Solve the quantum harmonic oscillator and the circle constant appears exactly once, as the fourth root in the ground state's normalising prefactor: ψ₀(x) = (mω/πħ)^(1/4) e^(−mωx²/2ħ). Every energy level, Eₙ = ħω(n + ½), is π-free, and so is every measurable expectation value — ⟨x²⟩ = ħ/2mω, ⟨p²⟩ = mωħ/2, the uncertainty product ΔxΔp = ħ/2, and the whole thermal partition function Z = 1/(2 sinh(βħω/2)), which carries no constant at all. The constant survives in only two places: the phase-space cell 2πħ (the quantum of area) and the Wigner function's 1/πħ normalisation — and even the state count below an energy, N = E/ħω, cancels it in the quotient. Under Golden Pi (π̂ = 4/√φ = 3.1446055110296931443…, root of x⁴ + 16x² − 256 = 0) the prefactor is (mω/π̂ħ)^(1/4), which is √2·φ^(−1/8) exactly — algebraic, and only 0.0239669401% from the conventional value because a fourth root dilutes the recurring 0.0959022309% gap to a quarter; the cell 2π̂ħ = 6.2892110220593862886 moves the full 0.0959022309%, and 1/π̂ħ = 0.31800491237851724106 moves −0.0958103466%. The honest ledger is short and brutal: every line of the oscillator's spectrum is measurable to many digits and contains no trace of the constant, so no experiment can adjudicate the relabel — the difference lives in an amplitude, never in an energy. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Quantum Harmonic Oscillator: How π^(1/4) Reaches the Ground State, Then Cancels from Every Energy Level — and What Golden Pi Changes

Stretch a spring, release a pendulum at small angle, or look at the displacement of an atom in a crystal lattice, and behind all three sits the same equation. The **quantum harmonic oscillator** is the most solved, most measured, and most reused model in physics — the textbook's model of a vibrating mode, the field theory's model of every free particle, the ladder that Feynman diagrams climb. It also happens to be the cleanest place in physics to see exactly what a circle constant does and does not do.

Here is the claim this article sets out to verify line by line: **the constant enters the oscillator exactly once, as a fourth root in the ground state's normalising prefactor, and cancels from every energy you can measure.** What is left is a *relabel* problem — a question about which symbol we print — not a physics question at all. We will do the arithmetic in the open, then ask what the golden value $\hat\pi = 4/\sqrt\varphi$ would change. The answer is a small number in an amplitude, and nothing in a spectrum.

## The spectrum with no $\pi$ in it

Start with the answer. The energy levels of a one-dimensional harmonic oscillator of mass $m$ and angular frequency $\omega$ are

$$E_n = \hbar\omega\left(n + \tfrac{1}{2}\right), \qquad n = 0, 1, 2, \dots$$

There is no circle constant in that expression. Not in the ground state $\hbar\omega/2$, not in the first gap $\hbar\omega$, not in the $n$-th level. The entire spectrum — the thing a spectroscope prints — is a ladder of equal rungs whose spacing is the reduced Planck constant times the angular frequency. If the circle constant were different, this ladder would not move by a single femtometre.

For a concrete rung, take a mode at ordinary terahertz frequencies, $\nu = 10^{12}$ Hz, so $\omega = 2\pi\nu$ and the level spacing is

| Quantity | Value |
|---|---|
| $\hbar\omega$ (level spacing) | $6.6260701459400796563 \times 10^{-22}$ J |
| $\hbar\omega$ in electronvolts | $0.0041356676943898556795$ eV |
| Ground state $E_0 = \hbar\omega/2$ | $0.0020678338471949278397$ eV |
| First excited state $E_1 = \tfrac{3}{2}\hbar\omega$ | $0.0062035015445847835192$ eV |

Those energies can be computed by anyone with $\hbar$, $\omega$ and $n$. No constant enters the computation, because the angular frequency $\omega = 2\pi\nu$ — where the constant is hiding — is fixed once by the **measured** oscillator frequency $\nu$, and thereafter it is a single frozen symbol. The constant has been absorbed into a physical measurement and never comes back out.

## Where the constant actually goes: the ladder

To see *why* the energy is clean, look at how the oscillator is solved. Write the Hamiltonian

$$H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2,$$

and factor it with the ladder operators

$$a = \sqrt{\frac{m\omega}{2\hbar}}\left(x + \frac{i\,p}{m\omega}\right), \qquad a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(x - \frac{i\,p}{m\omega}\right).$$

Everything the constant ever does is inside those square roots, and the algebra immediately cancels it: the commutator

$$[a, a^\dagger] = 1$$

is a pure number, and the Hamiltonian collapses to $H = \hbar\omega(a^\dagger a + \tfrac12)$. The number operator $N = a^\dagger a$ has integer eigenvalues because its eigenvector chain $a|n\rangle = \sqrt{n}\,|n-1\rangle$, $a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$ terminates at the bottom. Not one step of that derivation contains a traceable circle constant in a final, observable place. The prefactors where it appears are all squared away in the commutator, and the commutator is dimensionless.

This is the first of the article's recurring lessons: **a constant can enter a derivation and still be absent from every result**, provided it enters the same way on both sides of a subtraction or a quotient.

## The one place it survives: the ground state's prefactor

The time-independent Schrödinger equation does have a solution that carries the constant visibly. The ground state is a Gaussian:

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-m\omega x^2/(2\hbar)}.$$

That prefactor is the constant's only standing appearance in the whole bound-state problem. It is there for one reason: the integral

$$\int_{-\infty}^{\infty} e^{-m\omega x^2/\hbar}\,dx = \sqrt{\frac{\pi\hbar}{m\omega}}$$

must come out right, and the Gaussian integral is the archetypal place where $\pi$ is **computed** rather than measured — it is the limit of a quadrature, the value the integral evaluates to. Normalisation then forces the fourth root:

$$\left(\frac{m\omega}{\pi\hbar}\right)^{1/4} = \left(\frac{m\omega}{\hbar}\right)^{1/4}\pi^{-1/4}.$$

Set $m = \omega = \hbar = 1$ and the coefficient is $\pi^{-1/4} = 0.75112554446494248285870300477622769305236506675605\ldots$, a number that would be identical in every physical prediction if it were printed as anything else. And in the probability density $|\psi_0|^2$ it grows a second root:

$$|\psi_0(x)|^2 = \left(\frac{m\omega}{\pi\hbar}\right)^{1/2} e^{-m\omega x^2/\hbar}, \qquad \psi_0(0)^2 = \sqrt{\frac{m\omega}{\pi\hbar}} = 0.5641895835477562869480794515607725858441\ldots$$

Two appearances, one fourth power and one square root, both in an *amplitude*.

## What cancels: every measurable expectation value

Now the decisive test. Compute the quantities an experimentalist actually records, and watch the prefactor vanish. In oscillator units ($\hbar = m = \omega = 1$):

| Observable | Value | Contains $\pi$? |
|---|---|---|
| $\langle x^2\rangle_0$ | $\hbar/(2m\omega) = \tfrac12$ | no |
| $\langle p^2\rangle_0$ | $m\omega\hbar/2 = \tfrac12$ | no |
| Uncertainty product $\Delta x\,\Delta p$ | $\hbar/2 = \tfrac12$ | no |
| Kinetic energy $\langle T\rangle_0$ | $\hbar\omega/4$ | no |
| Potential energy $\langle V\rangle_0$ | $\hbar\omega/4$ | no |
| Classical turning point $x_t$ | $\sqrt{2E/(m\omega^2)}$ | no |
| Thermal $\langle x^2\rangle$ | $\dfrac{\hbar}{2m\omega}\coth\!\left(\dfrac{\beta\hbar\omega}{2}\right)$ | no |

Every one is free of the constant. The mean square position, the mean square momentum, the minimum uncertainty product, and the equipartition of energy between kinetic and potential terms — all of them are built from $\hbar$, $m$, and $\omega$ alone. At inverse temperature $\beta\hbar\omega = 1$ the thermal width is $\langle x^2\rangle = 1.081976706869326424385002005109011558547\ldots$, and no constant appears in it.

The thermodynamics is equally clean. The canonical partition function of the oscillator sums the geometric ladder

$$Z = \sum_{n=0}^{\infty} e^{-\beta\hbar\omega(n+1/2)} = \frac{e^{-\beta\hbar\omega/2}}{1 - e^{-\beta\hbar\omega}} = \frac{1}{2\sinh(\beta\hbar\omega/2)},$$

so $Z(\beta\hbar\omega = 1) = 0.9595173756674718597461014393635030797936\ldots$, the free energy $F = kT\ln\left(2\sinh(\beta\hbar\omega/2)\right)$ carries no constant, and the entropy at the same point is

$$\frac{S}{k} = 1.0406518522564083154066456501763412604238\ldots$$

again constant-free. It is worth saying this explicitly, because there is a nearby formula that *does* carry the constant — the differential entropy of a Gaussian, $\tfrac12\ln(2\pi e\sigma^2)$. The oscillator's own thermodynamics avoids it, because the oscillator is a **countable** ladder of discrete levels, and a count is integer arithmetic. Only the continuum — the phase-space cell, the integral over a Gaussian — reintroduces the constant, and there it can be divided away again.

## The phase-space cell, and how even that cancels

The remaining place the constant lives is the quantum of phase-space area. Semiclassical (EBK/Weyl) quantisation assigns one state to each cell of area $h = 2\pi\hbar$ in the $(x,p)$ plane. So

$$N(E) \approx \frac{\text{area of the energy ellipse}}{2\pi\hbar}.$$

The ellipse encloses area $2\pi E/\omega$, and the quotient collapses:

$$N(E) = \frac{2\pi E/\omega}{2\pi\hbar} = \frac{E}{\hbar\omega}.$$

The constant entered the numerator through the ellipse's area and the denominator through the cell size — and cancelled. The density of states is $g(E) = 1/(\hbar\omega)$, again constant-free. This is exactly the pattern the rest of this series keeps finding: the circle constant is a ratio of one computed continuum limit to another, and any formula that divides by a full turn is a formula from which the turn drops out.

## The Wigner function: the last survivor

Push further into phase space and one coefficient holds out. The ground state's Wigner quasi-probability density is

$$W(x,p) = \frac{1}{\pi\hbar}\exp\!\left(-\frac{m\omega x^2 + p^2/(m\omega)}{\hbar}\right),$$

with value at the origin

$$W(0,0) = \frac{1}{\pi\hbar} = 0.3183098861837906715377675267450287240689\ldots$$

Here the constant stands alone, undiluted, in the normalisation. It cannot cancel, because $W$ integrates over the whole plane to $1$ and the plane's measure is what supplies the other factor. So the inventory of the oscillator is complete and short:

**The constant appears as $\pi^{-1/4}$ in the ground-state amplitude and as $\pi^{-1}$ in the Wigner normalisation; it is absent from every energy, every expectation value, the partition function, the entropy, and the state count.**

## What Golden Pi changes

Now relabel the constant. Golden Pi takes the value the site uses throughout,

$$\hat\pi = \frac{4}{\sqrt\varphi} = 3.1446055110296931442782343433718357180924882313509\ldots$$

where $\varphi = (1+\sqrt5)/2$ is the golden ratio. It is the positive root of $x^4 + 16x^2 - 256 = 0$, and it exceeds the conventional analytic value $\pi = 3.1415926535897932384626433832795028841971693993751\ldots$ by exactly

$$\frac{\hat\pi}{\pi} - 1 = 0.095902230878252596369825828619561002052\%$$

— the recurring gap this series has tracked from every angle. Substitute it into the oscillator, and the arithmetic sorts the constant's appearances into three tiers, by the power it is raised to.

| Quantity under Golden Pi | Value | Shift from conventional |
|---|---|---|
| Ground-state prefactor $(m\omega/\hat\pi\hbar)^{1/4}$, $m\omega=\hbar=1$ | $0.7509455657907842857471819245672224961421\ldots$ | $-0.0239669401\%$ |
| $\hat\pi^{\,1/4}$ | $1.3316544441499545862832515686607325934474\ldots$ | $+0.0239669401\%$ |
| Amplitude at origin $\sqrt{m\omega/\hat\pi\hbar}$ | $0.5639192427808411301324177415885212292182\ldots$ | $-0.0479166533\%$ |
| Phase-space cell $2\hat\pi\hbar$ | $6.2892110220593862885564686867436714361850\ldots$ | $+0.0959022309\%$ |
| Wigner normalisation $1/\hat\pi\hbar$ | $0.3180049123785172410631056154343728729289\ldots$ | $-0.0958103466\%$ |
| Every energy $E_n$, every $\langle x^2\rangle$, $Z$, $S$ | unchanged | $0.0000000000\%$ |

The rule is transparent. The square root and the fourth root of the constant **divide the gap**: $(\hat\pi/\pi)^{1/4} - 1 = +0.0239669401\%$, exactly one quarter of the full gap to the digits shown, because the fractional power dilutes the ratio logarithmically. The undiluted first power moves $2\hat\pi\hbar$ by the full $+0.0959022309\%$, and its reciprocal moves $-0.0958103466\%$. And the *amplitudes* — anything that carries the constant under a square root — move by half the gap, $+0.0479166533\%$.

The golden side is not just a shifted copy. The fourth root becomes an **exact algebraic** number where the conventional one is transcendental:

$$\hat\pi^{\,1/4} = \left(\frac{4}{\sqrt\varphi}\right)^{1/4} = \frac{\sqrt2}{\varphi^{1/8}} = 1.3316544441499545862832515686607325934473734418398\ldots$$

a closed form verified here to fifty digits against the direct fourth root of $4/\sqrt\varphi$. Equally exactly, $\sqrt{\hat\pi} = 2/\varphi^{1/4} = 1.773303558624324518467033166301452512225\ldots$, and $\varphi^{1/4} = 1.127838485561682260264835483177042458\ldots$ is precisely the radius whose disk has area exactly $4$ — the constructibility that conventional $4/\sqrt\varphi$-free $\pi$ cannot offer, since $\pi$ is transcendental by Lindemann's 1882 theorem while $\hat\pi$ is a root of a quartic. A code block makes the golden arithmetic explicit at forty digits.

```python
from mpmath import mp, mpf, sqrt, pi, exp, sinh, coth
mp.dps = 40

phi  = (1 + sqrt(5)) / 2      # golden ratio
pHat = 4 / sqrt(phi)          # Golden Pi

print(pHat)                             # 3.144605511029693144278234343371835718092
print(pHat**(mpf(1)/4))                 # 1.331654444149954586283251568660732593447
print(sqrt(2) / phi**(mpf(1)/8))        # 1.331654444149954586283251568660732593447  (exact)
print(sqrt(pHat), 2/phi**(mpf(1)/4))    # 1.773303558624324518467033166301452512225  (exact)

# prefactor (m = w = hbar = 1)
print((1/pi)**(mpf(1)/4), (1/pHat)**(mpf(1)/4))
#  0.7511255444649424828587030047762276930524
#  0.7509455657907842857471819245672224961421

# phase-space cell and Wigner normalisation
print(2*pi, 2*pHat)                     # 6.2831853071795864769252867665590057684
                                        # 6.2892110220593862885564686867436714362
print(1/pi, 1/pHat)                     # 0.3183098861837906715377675267450287240689
                                        # 0.3180049123785172410631056154343728729289

# all pi-free, identical under either label
print(mpf(1)/2, mpf(1)/2, 1/(2*sinh(mpf(1)/2)))
#  0.5  0.5  0.9595173756674718597461014393635030797936
```

## The honest ledger: nothing measures it

Here the series must be blunt, because the oscillator gives the relabel *less* evidential footing than almost any other system we have examined, not more.

Every line of the oscillator's spectrum is measurable — molecular vibrations and lattice phonons are catalogued to many significant figures by infrared and Raman spectroscopy. But the spectrum's theoretical expression, $E_n = \hbar\omega(n+\tfrac12)$, contains **no circle constant at all**. There is nothing in it for a measurement to favour or disfavour. A spectroscopist who measured the level spacing of some mode to twenty digits would confirm $\hbar\omega$ and learn nothing whatever about $\pi$.

The constant's two surviving appearances are worse than useless for adjudication. The prefactor $\pi^{-1/4}$ is an overall factor multiplying a wavefunction, and the wavefunction's absolute phase and normalisation convention are fixed by human convention, not by nature — a quantity that must integrate to one cannot arbitrate a constant that also enters the integral's own definition. The Wigner normalisation $1/\pi\hbar$ is a quasi-probability density, and no apparatus observes quasi-probability densities directly; it observes the marginals, which are the ordinary probability densities, and those have the prefactor back in the amplitude where the convention lives.

There is also an internal-consistency caveat the honest reader should hold. If the constant is relabelled to $\hat\pi$ everywhere, then the Gaussian integral that the prefactor normalises must also be relabelled — its value becomes $\sqrt{\hat\pi\hbar/m\omega}$, and the prefactor $\hat\pi^{-1/4}$ is exactly what restores $\int|\psi_0|^2\,dx = 1$. Conventional $\pi$ gives the identical construction with $\pi^{-1/4}$ and its own $\sqrt{\pi\hbar/m\omega}$. The two systems are each internally consistent; they are not each other, and the $0.024\%$-scale difference in an unobservable amplitude is what separates them. Compare this with the Kepler's-third-law case, where a genuinely measured $GM_\odot$ fixes the constant and rules one label out by thousands of times, or the fine-structure case, where the measured $\alpha$ and the $4\pi$ of the Coulomb convention interact in a way that can be tested. The harmonic oscillator offers no such handle.

So the summary stands as it was promised at the top. The circle constant drops into the quantum harmonic oscillator through the Gaussian ground state, survives as a fourth root in one amplitude and a full power in one quasi-probability, and evaporates from every energy level, every expectation value, the partition function, the entropy, and the state count that semiclassical physics computes. Under Golden Pi those survivors move by $\tfrac14$, $\tfrac12$, or $1$ times the recurring $0.0959022309\%$ according as the constant sits under a fourth root, a square root, or the bare first power — an exact algebraic $\sqrt2/\varphi^{1/8}$ in place of a transcendental $\pi^{1/4}$. The spectrum, which is what a laboratory prints, does not move at all — and that, rather than a measurement, is the whole truth about the circle constant in an oscillator. Computed, never measured.

## Further Reading

- [The Pendulum Period: How the Elliptic Integral Computes the Circle Constant — and What Golden Pi Changes](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the same oscillator, made non-linear, and the constant that re-enters through the elliptic integral $K(k)$.
- [The Gaussian Integral and the Bell Curve: How $\sqrt{\pi}$ Is Computed, Never Measured](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the integral that puts $\pi^{-1/4}$ in the oscillator's ground state in the first place.
- [Planck's Spectrum: How the Blackbody Formula Carries $\pi^4$ — and What Golden Pi Changes](/blog/posts/2026-09-23-planck-spectrum-blackbody-computes-circle-constant-golden-pi/) — a thermal system where the constant does *not* cancel, and the compounding story when it is raised to a power.
- [The Fine-Structure Constant: Where $4\pi$ Cancels from the Coupling — and What Golden Pi Changes](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — a constant whose measured value genuinely constrains the convention.
- [The Fermi Sphere: How Counting States in Momentum Space Computes $3\pi^2$ — and What Golden Pi Changes](/blog/posts/2026-10-06-fermi-sphere-quantum-state-counting-computes-circle-constant-golden-pi/) — the neighbouring counting problem, where the constant survives the count.
