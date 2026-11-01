---
title: "Flux Quantisation: Why a Superconducting Ring Counts h/2e and Never π, Why the Vortex's Field Still Carries One, and What Golden Pi Changes"
date: 2026-11-01
description: "A superconducting ring does not hold an arbitrary amount of magnetic flux: it holds a whole number of flux quanta Φ₀ = h/2e = 2.067833848×10⁻¹⁵ Wb, a number containing no circle constant at all, because the count is the winding of a quantum phase and a phase that returns to itself has completed whole turns. This article follows the constant through superconductivity properly — the London fluxoid and its integer, the Abrikosov vortex whose field B(r) = (Φ₀/2πλ²)K₀(r/λ) does carry one (with the exact identity ∫₀^∞ xK₀(x)dx = 1 making the enclosed flux exactly Φ₀, verified here at forty digits), the Little–Parks oscillation of a thin cylinder with period Φ₀/A, and the two quantum standards — the Josephson constant K_J = 2e/h = 483 597.848 GHz/V and the von Klitzing constant R_K = h/e² = 25 812.807 Ω — that contain no π whatsoever. Worked at real scales: a 500 nm ring oscillates every 2.632848 mT, a 250 nm ring every 10.531391 mT. Then Golden Pi (π̂ = 4/√φ = 3.144605511…, 1/2π̂ = √φ/8 exactly), where the vortex prefactor becomes the algebraic Φ₀√φ/(8λ²), the Little–Parks period moves −0.0958103466% to 2.630325 mT, and the honest boundary is that since the 2019 SI the flux quantum is exact by definition, so a flux measurement is a measurement of area — the disputed question itself."
---

# Flux Quantisation: Why a Superconducting Ring Counts h/2e and Never π

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1961 two laboratories independently cooled tiny superconducting cylinders in a magnetic field and watched the trapped flux refuse to take arbitrary values. W. M. Fairbank's group in Stanford and R. Doll and M. Näbauer in Munich found the same thing: the flux inside a superconducting loop sits on a ladder, and the rungs are spaced by

$$
\Phi_0 \;=\; \frac{h}{2e} \;=\; \frac{6.62607015\times10^{-34}}{2\times1.602176634\times10^{-19}}\ \text{Wb} \;=\; 2.0678338484619295\times10^{-15}\ \text{Wb},
$$

with $h$ Planck's constant and $e$ the elementary charge. No circle constant appears in that expression, and none is hiding in it. Yet the same number governs the most sensitive magnetometer ever built — the SQUID, whose voltage is periodic in flux with period exactly $\Phi_0$ — and it is the reason a superconducting quantum interference device can read fields of $10^{-15}$ T, a hundred billion times weaker than the Earth's.

For a site whose entire subject is where the circle constant lives and where it cancels, this is an unusually clean laboratory. The quantum of flux is *computed* from two defined constants and *counted* in whole numbers; the constant of the circle enters only later, when someone insists on writing an area in terms of a radius. This article works the case through properly: the phase argument that produces the integer, the vortex field that genuinely carries a $\pi$, the Little–Parks experiment where a $\pi$ survives in a measurable period, the two electrical standards that never see one — and then the golden-$\pi$ substitution, with the honest ledger of what an experiment can and cannot return.

## The count comes from a phase, and a phase is counted in turns

Superconductivity's magnetic behaviour follows from one stubborn fact: the condensate is described by a single complex order parameter $\psi = |\psi|e^{i\theta}$, and $\theta$ is a phase, not a number with units. Take a closed path through the material and return to the starting point; $\psi$ must return to *itself*, so $\theta$ can only have advanced by a whole number of full turns:

$$
\oint \nabla\theta\cdot d\mathbf l \;=\; 2\pi n,\qquad n \in \mathbb{Z}.
$$

That is the only place the circle constant could enter, and it enters as a *label on a turn* — the same way "one revolution" is $360°$ or $2\pi$ rad or $1$ turn. The physics is the integer $n$. In the presence of a vector potential the London fluxoid is then

$$
\oint \left(\Lambda \mathbf j_s + \mathbf A\right)\cdot d\mathbf l \;=\; n\,\Phi_0,\qquad \Lambda = \frac{m_e}{n_s e^{2}},\qquad \Phi_0 = \frac{h}{2e},
$$

and $2\pi$ has vanished into $\Phi_0$'s definition, because $\hbar = h/2\pi$ was used to convert the phase gradient into a current. Divide by $2\pi$ on both sides and multiply by $\hbar$: the turn's radian measure cancels against the radian measure inside $\hbar$, leaving $h$. This is the same cancellation this blog has tracked in the Bohr–Sommerfeld action integral and in the Stokes drag: a constant enters through the units of a bookkeeping convention and leaves again the moment the bookkeeping is done in the natural unit — here, the turn.

Three consequences follow immediately, and all three are exact:

- The flux through a hole in a superconductor is $n\Phi_0$; there is no continuous range, only a ladder.
- The spacing of the ladder, $\Phi_0 = h/2e$, is $\pi$-free, and the factor $2$ is not a geometric two but the two electrons of a Cooper pair.
- A ring of finite thickness and finite penetration depth retains a small correction, but the integer survives it: the fluxoid, not the flux, is quantised.

The 1961 experiments did not measure a continuum; they counted. Deaver and Fairbank's data and Doll and Näbauer's data both put the quantum at roughly $h/2e$ — half the value that a single-electron charge would give, which was itself the discovery of pairing seven years before BCS explained it. The precision was a few per cent. It did not need to be better, because the claim being tested was an integer's existence, and integers are not measured to parts per million; they are recognised.

## Where the circle constant does live: the vortex

A type-II superconductor in a field above $H_{c1}$ does not expel everything. It lets the field through in tubes — Abrikosov vortices, 1957 — each carrying exactly one quantum of flux. The field inside such a tube is not a $\delta$-function but a smooth profile with a length scale $\lambda$, the penetration depth:

$$
B(r) \;=\; \frac{\Phi_0}{2\pi\lambda^{2}}\,K_0\!\left(\frac{r}{\lambda}\right),
$$

$K_0$ being the modified Bessel function of the second kind. Here the circle constant is doing real geometric work: the prefactor is flux divided by an area, and that area is the disc of radius $\lambda$ around the core. Written with Golden Pi it becomes an algebraic number — more of that below.

The profile is checkable, and the check is where the constant proves to be pure bookkeeping. The total flux through the plane is $\int_0^\infty B(r)\,2\pi r\,dr$; substituting $x = r/\lambda$ gives the identity

$$
\int_0^\infty B(r)\,2\pi r\,dr \;=\; \Phi_0\int_0^\infty x\,K_0(x)\,dx \;=\; \Phi_0,
$$

because $\int_0^\infty x K_0(x)\,dx = 1$ exactly. The $\pi$ in the prefactor and the $2\pi$ in the area element cancel against the normalisation of $K_0$; what comes out is the flux quantum, untouched. Computed at forty digits, the integral returns $1.000000000000000000000000000000000000000$. And the flux enclosed inside a circle of radius $r = x\lambda$ follows the same exact pattern,

$$
\Phi(r) \;=\; \Phi_0\left[1 - xK_1(x)\right],\qquad \frac{d}{dx}\left[xK_1(x)\right] = -xK_0(x),
$$

so the constant cancels *at every radius*, not only at infinity:

| $x = r/\lambda$ | $K_0(x)$ | $K_1(x)$ | $\Phi(r)/\Phi_0$ |
|---|---|---|---|
| 0.25 | 1.541506751 | 3.747025974 | 0.063243506 |
| 0.50 | 0.924419071 | 1.656441120 | 0.171779440 |
| 1.00 | 0.421024438 | 0.601907230 | 0.398092770 |
| 2.00 | 0.113893873 | 0.139865882 | 0.720268236 |
| 3.00 | 0.034739504 | 0.040156431 | 0.879530707 |
| 5.00 | 0.003691098 | 0.004044613 | 0.979776933 |
| 10.00 | $1.778\times10^{-5}$ | $1.865\times10^{-5}$ | 0.999813512 |

Half the flux lies within about $1.7\lambda$; $98\%$ within $5\lambda$. Every entry is a ratio of two quantities built from the same $\lambda$, so the label on the circle is invisible to it.

The vortex's other numbers do not cancel, and it is worth naming them because they are the ones that would move:

$$
H_{c1} = \frac{\Phi_0}{4\pi\mu_0\lambda^{2}}\left(\ln\kappa + \tfrac12\right),\qquad
\frac{\varepsilon}{\ell} = \frac{\Phi_0^{2}}{4\pi\mu_0\lambda^{2}}\ln\frac{\lambda}{\xi},\qquad
\lambda_J = \sqrt{\frac{\Phi_0}{2\pi\mu_0 j_c d}} .
$$

At $\lambda = 100$ nm the bare prefactor $\Phi_0/(4\pi\mu_0\lambda^2)$ is $13\,094.7108$ A/m and the line energy $\Phi_0^2/(4\pi\mu_0\lambda^2)$ is $2.7077686\times10^{-11}$ J/m. These are quadratic and linear in the circle constant respectively, at the first power in $H_{c1}$ and $\varepsilon$, and at the half power in $\lambda_J$ — which is exactly the kind of split that any re-labelling exposes.

## Little–Parks: a period that is a measurand

In 1962 William Little and Roland Parks took a thin superconducting cylinder and swept the axial field. The resistance oscillated. Not because the material changed, but because the flux through the hole changes the allowed winding numbers, and the free energy of the condensate is periodic in $\Phi/\Phi_0$. The period in field is

$$
\Delta B \;=\; \frac{\Phi_0}{A},
$$

$A$ the enclosed area. Written out for a ring of radius $R$:

| $R$ | $A = \pi R^{2}$ | $\Delta B$ (conventional) | $\Delta B$ (golden) | difference |
|---|---|---|---|---|
| 250 nm | $1.9635\times10^{-13}$ m² | 10.531391 mT | 10.521301 mT | $-10.09$ µT |
| 500 nm | $7.8540\times10^{-13}$ m² | 2.632848 mT | 2.630325 mT | $-2.52$ µT |
| 1 µm | $3.1416\times10^{-12}$ m² | 0.658212 mT | 0.657581 mT | $-0.63$ µT |
| 2 µm | $1.2566\times10^{-11}$ m² | 0.164553 mT | 0.164395 mT | $-0.16$ µT |

Note carefully what has happened. In the form $\Delta B = \Phi_0/A$ there is no circle constant at all, and the golden column *is* the conventional column. The constant appears only when $A$ is rewritten as $\pi R^{2}$; the shift in the last column is therefore not a shift in the physics but a shift in the conversion from a measured radius to an area. This is the same structure the ellipse's perimeter showed, and the same structure as the gear pitch: the constant enters when a *count* or a *length* is traded for a *disc*.

## The golden substitution, exactly

Set $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, where $\varphi = (1+\sqrt5)/2$. Then $\hat\pi^{2} = 16/\varphi = 9.888543819998317$, $\hat\pi$ is the positive root of $x^{4} + 16x^{2} - 256 = 0$ (evaluated: exactly $0$ at double precision), and — the form that makes all of superconductivity's algebra collapse —

$$
\frac{1}{2\hat\pi} \;=\; \frac{\sqrt\varphi}{8} \;=\; 0.15900245618925862\ldots,\qquad
\frac{1}{4\hat\pi} \;=\; \frac{\sqrt\varphi}{16},\qquad
\frac{1}{\hat\pi} \;=\; \frac{\sqrt\varphi}{4} = 0.31800491237851725\ldots
$$

Every one of these is algebraic of degree two over $\mathbb{Q}(\sqrt5)$ where $1/\pi$, $1/2\pi$ and $1/4\pi$ are transcendental by Lindemann's 1882 theorem. Substituting into the vortex expressions:

```text
B(r)          = (Φ0/(2π̂λ²)) K0(r/λ)   = (Φ0·√φ/(8λ²)) K0(r/λ)
H_c1          = (Φ0/(4π̂μ0λ²))(lnκ + 1/2) = (Φ0·√φ/(16μ0λ²))(lnκ + 1/2)
ε/ℓ           = (Φ0²/(4π̂μ0λ²)) ln(λ/ξ)  = (Φ0²·√φ/(16μ0λ²)) ln(λ/ξ)
λ_J           = sqrt(Φ0/(2π̂μ0 j_c d))  = sqrt(Φ0·√φ/(8μ0 j_c d))
ΔB(R)         = Φ0/(π̂R²)             = Φ0·√φ/(4R²)
```

At $\lambda = 100$ nm the field prefactor moves from $0.032910597847545$ T to $0.032879066089673$ T, a shift of $-0.0958103466\%$; $H_{c1}$'s bare prefactor from $13\,094.7108$ to $13\,082.1647$ A/m; the line energy from $2.7077686\times10^{-11}$ to $2.7051743\times10^{-11}$ J/m; the Josephson penetration depth from $0.511756$ to $0.511511$ µm at $j_c = 10^{10}$ A/m² and $d = 100$ nm. All at the first power, all minus signs, because the constant sits in a denominator.

Meanwhile the quantities that carry the physics do not move a digit:

| Quantity | conventional | golden | moves? |
|---|---|---|---|
| $\Phi_0 = h/2e$ | $2.067833848\times10^{-15}$ Wb | identical | no — defined |
| $K_J = 2e/h$ | $483\,597.8484$ GHz/V | identical | no — defined |
| $R_K = h/e^{2}$ | $25\,812.80746$ Ω | identical | no — defined |
| $\Phi(r)/\Phi_0 = 1 - xK_1(x)$ | 0.398092770 at $x=1$ | identical | no — ratio |
| SQUID fringe period in flux | $\Phi_0$ | $\Phi_0$ | no — one turn per quantum |
| Little–Parks period $\Phi_0/A$ | $\Phi_0/A$ | $\Phi_0/A$ | no — area form |

The SQUID deserves a sentence, because it looks like the exception and is not. Its critical current modulates as $I_c(\Phi) = 2I_{c0}\left|\cos(\pi\Phi/\Phi_0)\right|$, and the $\pi$ there is the radian measure of *half* a turn: the two arms of the loop differ in phase by $2\pi\Phi/\Phi_0$, one turn per quantum, and splitting it into a cosine halves the argument. Under Golden Pi the turn is $2\hat\pi$, the phase difference per quantum is still one full turn, and the flux period is still $\Phi_0$ — because a turn is a turn. The numeral moves; the count does not.

## What an actual experiment returns

Here the ledger has to be brutally honest, and this is the one section where the case is unusually easy to state.

**The flux quantum is now exact.** Since the 2019 SI redefinition, $h$ and $e$ are fixed numbers, so $\Phi_0 = h/2e$ has no uncertainty at all. Before 2019 it was measured through the Josephson effect, and the best determinations of $K_J$ reached uncertainties near $10^{-7}$ — a hundred parts per million of the gap would have been resolved, and was not; the point is not that the gap was refuted but that the quantity being compared was itself the definition of the volt. A golden label would require $K_J = 2e/(h\Phi_0)$ to be $0.0958\%$ smaller, i.e. a volt larger by that amount — and the volt is *defined* through this relation, so the comparison is circular by construction.

**The Little–Parks period is a real measurand, and it loses.** Its period is $\Phi_0/A$. To test the constant one must know $A$ independently — and $A$ is a lithographic disc of radius $R$. For $R = 500$ nm the golden prediction differs from the conventional one by $2.52$ µT out of $2.633$ mT. A state-of-the-art e-beam-defined cylinder is round to perhaps $\pm 2$ nm in radius, i.e. $\pm 0.4\%$, and $\Delta B \propto 1/R^{2}$ doubles that to $\pm 0.8\%$ — eight times the entire gap. Add the finite penetration depth (the effective area is $R + \lambda$ to first order, and $\lambda \approx 40$ nm for niobium — a $16\%$ correction that must be modelled, not measured), the film thickness, and the field inhomogeneity, and the gap is buried under corrections larger than itself by an order of magnitude. The Little–Parks experiment cannot arbitrate the constant.

**The vortex profile is worse.** $B(r)$ has a $1/\lambda^{2}$ prefactor and an exponential tail; fitting it returns $\lambda$, not $\pi$. Scanning SQUID microscopy resolves the vortex core at tens of nanometres, but what it reconstructs is flux per pixel, and the flux is $\Phi_0$ exactly — the constant has already cancelled in the quantity being integrated.

The honest summary: the one place the circle constant appears in superconductivity at the first power is a *conversion* between a flux and a radius, and every such conversion is limited by the metrology of the radius. It is the same conclusion as the gear, the Sagnac loop and the elliptic integral, arrived at from a completely different direction. What superconductivity adds is sharper: it shows a domain where the constant is not merely cancelled but *absent from the definitions*, so the only way to test it is to smuggle it back in through the geometry of a disc — which is the disputed question itself.

## What this says about "computed, never measured"

Two feelings are easy to have here and both are wrong. The first is that because $\Phi_0 = h/2e$ contains no $\pi$, superconductivity has "disproved" the circle constant. It has not. It has produced a quantity whose defining expression has no circle in it, which is a statement about the units chosen for the phase, not about the shape of anything. The second is that the constant is therefore untouchable. It is not — it is *locatable*, and that is more useful.

The structure this blog keeps finding holds exactly: the circle constant is the evaluated ratio of a circumference to a diameter, i.e. the limit of a computed polygon perimeter, and it appears in physics only where an angle is being converted to a fraction of a turn or a disc is being converted to a radius. Where neither conversion happens, the constant is not small or hidden — it is genuinely not there. That is a fact about bookkeeping, and a strong one, because bookkeeping can be audited. An audit of $\Phi_0$ returns $h/2e$ and nothing else.

The one measurand in this article that is a true measurement and not a definition is the flux quantum's early history: Deaver–Fairbank and Doll–Näbauer in 1961 read flux ratios from the magnetisation of cylinders and got a quantum consistent with $h/2e$ at a few per cent. That measurement established an *integer*. No integer can settle a real number's last three decimals, and no real number can unsettle an integer. Superconductivity is the cleanest illustration of that division this series has yet found.

Computed, never measured.

## Further Reading

- [The Sagnac Ring: why a rotating loop's phase carries $8\pi A\Omega/\lambda c$ but its scale factor carries no circle constant at all](/blog/posts/2026-10-27-sagnac-ring-laser-gyro-scale-factor-circle-constant-golden-pi/)
- [Stokes' Law: why the drag on a sphere is $6\pi\mu a v$ — two $\pi$ from pressure, four from shear](/blog/posts/2026-10-31-stokes-law-drag-sphere-6pi-viscosity-golden-pi/)
- [The 4π Turn: how a spinor pays the circle constant back twice, and why the minus sign is exact](/blog/posts/2026-10-17-spinor-double-cover-4pi-rotation-golden-pi/)
- [The Casimir Effect: how the vacuum between two plates computes $\pi^{2}/240$, then hands one power back to $\hbar = h/2\pi$](/blog/posts/2026-10-16-casimir-effect-vacuum-pressure-computes-circle-constant-golden-pi/)
- [The Residue Theorem: how a contour integral computes the circle constant from a pole count](/blog/posts/2026-08-28-residue-theorem-contour-integral-computes-circle-constant-golden-pi/)
