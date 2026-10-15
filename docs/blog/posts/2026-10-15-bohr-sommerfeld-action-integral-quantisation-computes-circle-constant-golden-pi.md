---
title: "The Bohr–Sommerfeld Action Integral: How Phase-Space Area Carries the Circle Constant as a Half-Turn, Then Cancels It Between Coulomb's 4π and ħ's 2π — and What Golden Pi Changes"
date: 2026-10-15
description: "In 1916 the quantum condition was written as an integral, ∮p dq = nh, and the action it evaluates is nothing but the area a classical orbit encloses in phase space — a factor 2π wide for a harmonic oscillator, and for an electron in a Coulomb field the circle constant appears twice, once in the 4π of Coulomb's law and once in ħ = h/2π, and cancels completely: the hydrogen ladder is Eₙ = −mₑe⁴/(8ε₀²h²n²) = −13.605693122994 eV/n², with no constant in it at all, while the Bohr radius a₀ = ε₀h²/(πmₑe²) keeps one power. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the ladder does not move a digit, ΔA between adjacent levels stays exactly h, and the constant survives only in the phase cell 2π̂ħ = 6.632424695×10⁻³⁴ J s and in the ħ a golden label would demand, h/(2π̂) = 1.0535614287×10⁻³⁴ J s — 0.0958103466% below the defined ħ, and 7.8×10⁴ σ from the ħ CODATA last measured before 2019 fixed the constant of action. Computed, never measured."
---

# The Bohr–Sommerfeld Action Integral: How Phase-Space Area Carries the Circle Constant as a Half-Turn, Then Cancels It Between Coulomb's 4π and ħ's 2π — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1913 Bohr quantised a hydrogen atom by declaring an angular momentum to be a whole number of $\hbar$. Three years later Sommerfeld and Wilson wrote the same physics as an integral and made it general: for each periodic degree of freedom,

$$
\oint p\,dq = n h, \qquad n = 1, 2, 3, \ldots
$$

and every quantisation rule of the old quantum theory — Bohr's orbits, the oscillator, the rotator, the Bohr–Sommerfeld relativistic Kepler problem that first produced the fine-structure formula — is a special case of it. The quantity on the left is the **action**, and its geometric meaning is exactly the point of this chapter: for any periodic motion, $\oint p\,dq$ is the **area the orbit encloses in phase space**. The circle constant enters here not as a length and not as a series, but as the shape of a phase-space orbit, and then it does something this series has watched happen dozens of times: it cancels.

## The action as an enclosed area

Write a Hamiltonian orbit in the $(q, p)$ plane. For the harmonic oscillator, $H = p^{2}/2m + \tfrac12 m\omega^{2}q^{2}$, and a level set $H = E$ is an ellipse,

$$
\frac{p^{2}}{2mE} + \frac{q^{2}}{2E/m\omega^{2}} = 1,
$$

with semi-axes $a = \sqrt{2E/m\omega^{2}}$ and $b = \sqrt{2mE}$. Its area is

$$
A \;=\; \pi\,a\,b \;=\; \pi\sqrt{\frac{2E}{m\omega^{2}}}\sqrt{2mE} \;=\; \frac{2\pi E}{\omega}.
$$

The circle constant appears **once**, at the first power, as the constant that turns a product of two semi-axes into an area. Split the action into a π-free factor and the constant:

```text
S = ∮ p dq  =  area of the phase-space ellipse  =  (2E/ω) · π

quantisation:   S = n h
⇒  (2E/ω)·π = n h
⇒  E_n = n h ω / (2π) = n ħ ω        ← π cancels against ħ = h/2π
```

The ladder is

$$
E_n = n\hbar\omega, \qquad \Delta A = A_{n+1} - A_n = 2\pi\,\frac{(n+1)\hbar\omega - n\hbar\omega}{\omega} = 2\pi\hbar = h
$$

so one quantum of action is one cell of phase-space area, $h = 6.62607015\times10^{-34}$ J s, and the number of cells below a given energy is the pure number $N(E) = E/(\hbar\omega)$ — no constant anywhere in the count. The same computation for the n = 0 state gives $\pi\hbar = h/2 = 3.313035075\times10^{-34}$ J s, and the same conclusion in Bohr's own form: $mvr = n\hbar$ puts the half-turn factor of the orbit *inside* the unit of angular momentum, where it is the same cancellation in different clothes.

## The two π's of the hydrogen ladder

Now the substance of the chapter. The Coulomb energy of an electron at radius $r$ from a proton is written $U = -e^{2}/(4\pi\varepsilon_{0} r)$: the law's spherical geometry supplies a $4\pi$. Bohr's quantum condition supplies an $\hbar = h/2\pi$. The hydrogen energy ladder carries both, and they meet:

$$
E_n = -\frac{m_{e} e^{4}}{2\,(4\pi\varepsilon_{0})^{2}\,\hbar^{2}\,n^{2}}
\qquad\Longrightarrow\qquad
(4\pi\varepsilon_{0})^{2}\hbar^{2} = 16\pi^{2}\varepsilon_{0}^{2}\cdot\frac{h^{2}}{4\pi^{2}} = 4\,\varepsilon_{0}^{2}h^{2},
$$

hence

$$
\boxed{\;E_n = -\frac{m_{e} e^{4}}{8\,\varepsilon_{0}^{2}h^{2}n^{2}}\;}
$$

which contains **no circle constant at all**. The $(2\pi)^{2}$ of $\hbar^{2}$ in the denominator eats the $(4\pi)^{2}$ of Coulomb's law exactly, and what is left is an expression in measured mechanical and electrical constants only. The Rydberg constant — the number spectroscopy actually pins — inherits the cancellation in its sharpest form,

$$
R_\infty = \frac{m_{e} e^{4}}{8\varepsilon_{0}^{2}h^{3}c} = \frac{\alpha^{2} m_{e} c}{2h} = 10\,973\,731.568\,160\ \text{m}^{-1},
$$

and the identity on the right is the check: evaluated with CODATA's $\alpha = 7.2973525693\times10^{-3}$, $m_{e} = 9.1093837015\times10^{-31}$ kg, $c = 299\,792\,458$ m s⁻¹ and $h = 6.62607015\times10^{-34}$ J s it returns $10\,973\,731.568\,139$ m⁻¹ — eleven digits, and the residual is the rounding in the quoted constants. Multiplying by $hc$ returns the ionisation energy of hydrogen,

$$
E_1 = R_\infty\,hc = 13.605693122994\ \text{eV},
$$

exactly as compiled. No $\pi$ appears anywhere in that chain: not in the ladder, not in the Rydberg, not in the ionisation energy. The circle constant entered the physics through the geometry of the Coulomb field and through the definition of $\hbar$, and the two appearances annihilated.

What does *not* cancel? The Bohr radius,

$$
a_{0} = \frac{4\pi\varepsilon_{0}\hbar^{2}}{m_{e}e^{2}} = \frac{\varepsilon_{0}h^{2}}{\pi m_{e}e^{2}} = 5.29177210903\times10^{-11}\ \text{m},
$$

keeps **one** power of $\pi$, because only one of $\hbar$'s two π's is squared away and the Coulomb $4\pi$ is not squared either. And so the orbit radii $r_n = a_{0}n^{2}$, the ground-state circumference $2\pi a_{0} = 3.324918476\times10^{-10}$ m, and every conversion between frequency and angular frequency, $\omega = 2\pi\nu$, carry the constant at the first power and nothing dilutes it. The pattern of this series — some rows cancel, some survive at full strength, some under a root — repeats here in a table:

| Quantity | Power of $\pi$ | Conventional value | Golden Pi (π̂ = 4/√φ) | Change |
|---|---|---|---|---|
| Oscillator ladder $E_n = n\,h\omega/2\pi$ | cancels | $n\hbar\omega$ | $n\hbar\omega$ | 0 |
| Phase-space cell $\Delta A$ | cancels | $h = 6.62607015\times10^{-34}$ J s | $h$ (defined) | 0 |
| State count $N(E) = E/\hbar\omega$ | 0 | $E/\hbar\omega$ | $E/\hbar\omega$ | 0 |
| Hydrogen ladder $E_n$ | cancels | $-13.605693122994/n^{2}$ eV | $-13.605693122994/n^{2}$ eV | 0 |
| Rydberg $R_\infty = \alpha^{2}m_{e}c/2h$ | 0 | $10\,973\,731.568\,160$ m⁻¹ | same | 0 |
| Bohr radius $a_0 = \varepsilon_0h^{2}/\pi m_{e}e^{2}$ | −1 | $5.29177210903\times10^{-11}$ m | $5.2867020438\times10^{-11}$ m | $-0.0958103466\%$ |
| Ground orbit $2\pi a_0$ | +1 | $3.3249184764\times10^{-10}$ m | $3.3281071474\times10^{-10}$ m | $+0.0959022309\%$ |
| Angular frequency $\omega = 2\pi\nu$ (21 cm line, $\nu = 1\,420\,405\,751.768$ Hz) | +1 | $8\,924\,672\,549.74$ rad s⁻¹ | $8\,933\,231\,509.82$ rad s⁻¹ | $+0.0959022309\%$ |
| Phase cell $2\pi\hbar$ | +1 | $6.62607015\times10^{-34}$ J s | $2\hat\pi\hbar = 6.6324246950\times10^{-34}$ J s | $+0.0959022309\%$ |
| $\hbar$ that fits $h = 2\hat\pi\hbar$ | −1 | $1.054571817\times10^{-34}$ J s | $1.0535614287\times10^{-34}$ J s | $-0.0958103466\%$ |

## The half-integer, the turning points, and the exactness of hydrogen

The old quantum condition $\oint p\,dq = nh$ is not the whole story, and the correction is instructive. WKB quantisation reads

$$
\oint p\,dq = \left(n + \tfrac12\right)h,
$$

because a classical turning point costs a phase shift of $\pi/2$: the connection formulae that join the oscillatory region to the classically forbidden one carry an Airy-function quarter turn each, and with two turning points the Maslov index is 2, giving the famous $n + \tfrac12$ that becomes the zero-point energy. This is the one place in the chapter where a π does **not** cancel: $\hbar\omega/2$ is where the half-turn of a phase shift survives into a physical energy. For the harmonic oscillator WKB at $(n+\tfrac12)$ is exact; for hydrogen the naive WKB misses the $s$ states badly unless the centrifugal term is regularised (Langer's correction, $l(l+1) \to (l+\tfrac12)^{2}$), after which the WKB energies are *exactly* $E_n = -13.605693122994/n^{2}$ eV — the same π-free ladder, recovered from an approximation whose bookkeeping is a page of circle constants.

## What Golden Pi changes

Set $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, with $\varphi = (1+\sqrt5)/2$ the golden ratio — the site's standing value. Under the relabel, everything in this chapter that came from a radian reading moves by the recurring first-power gap $+0.0959022309\%$:

- the phase cell becomes $2\hat\pi\hbar = 6.6324246950\times10^{-34}$ J s;
- the phase advance of one period, $2\hat\pi$ rad, reads $360.3452480312°$ against the flat $360°$;
- an angular frequency for the same physical frequency $\nu$ reads $8\,933\,231\,509.82$ instead of $8\,924\,672\,549.74$ rad s⁻¹, a difference of $8\,558\,960.07$ rad s⁻¹ at the 21-centimetre line;
- the Bohr radius, carrying a single power in its denominator, reads $5.2867020438\times10^{-11}$ m, and the ground-state circumference $3.3281071474\times10^{-10}$ m;
- the energy a golden label would demand of the quantum of action, $\hbar = h/(2\hat\pi)$, is $1.0535614287\times10^{-34}$ J s, which is $0.0958103466\%$ **below** the defined $\hbar = h/2\pi$.

Everything that cancelled stays cancelled. The oscillator ladder, the cell $h$, the Rydberg constant in its $\alpha^{2}m_{e}c/(2h)$ form, the ionisation energy $13.605693122994$ eV and every spectral line of hydrogen are label-blind: a relabelling cannot move an expression that contains no constant, and this is the sharpest form of the argument this series has been making — the constant lives in the *bookkeeping* of turns, not in the physics of the ladder.

Credit where it is exact. $\hat\pi = 2\sqrt{2\sqrt5 - 2}$ is a root of $x^{4} + 16x^{2} - 256 = 0$ (evaluating to exactly $0$ at $\hat\pi$), $\hat\pi^{2} = 16/\varphi = 8(\sqrt5 - 1) = 9.8885438199983175713$ is algebraic of degree two where $\pi^{2}$ is transcendental by Lindemann (1882), $\hat\pi^{2}/16$ is **exactly** $1/\varphi$, $2\hat\pi\sqrt\varphi$ is **exactly** $8$, and a disk of radius $\varphi^{1/4} = 1.1278384855616822603$ has area **exactly 4** — the quadrature that runs through this site's whole geometric case. The harmonic-orbit ellipse of this chapter inherits the same exactness: the phase-space ellipse with $E/\omega = 1/\hat\pi$ encloses area exactly $2$.

## The honest ledger

**First.** Nothing in this chapter is measured to obtain the constant. The action integral evaluates to the area of an ellipse, the ellipse's area is a geometric theorem, and the Coulomb law's $4\pi$ is the solid angle of a sphere — all computed limits of the same kind. The rule of this site holds: the constant is computed and evaluated, never measured.

**Second.** The hydrogen spectrum is the most precisely measured quantity in physics, and it decides nothing about the label, because no constant appears in it. The 1S–2S two-photon transition near $2\,466$ THz is resolved with a relative uncertainty below $10^{-13}$, and its agreement with theory tests quantum electrodynamics, the Rydberg constant and the proton radius — the constant can be relabelled and the prediction does not move in the 13th digit, because the prediction never contained it. A measurement can only arbitrate a claim in which the measured quantity carries the thing being claimed.

**Third.** There is exactly one measured number in this chapter that *does* carry the constant, and it is $\hbar$ — historically, because before the 2019 SI the unit of angular momentum was obtained from measured quantities ($\alpha$, $e$, $h$ are all measured, and the circle constant rode along in $\varepsilon_{0}$ and in the radian conversion). The comparison is stark and it belongs in the ledger in plain numbers: the last CODATA value of $\hbar$ measured under the old SI was $1.054571800(13)\times10^{-34}$ J s, a relative standard uncertainty of $1.2\times10^{-8}$, whereas the value a golden label requires, $h/(2\hat\pi) = 1.0535614287\times10^{-34}$ J s, sits $0.0958103466\%$ away — about $7.8\times10^{4}$ standard uncertainties. On the pre-2019 footing this is not a marginal test; it is the strongest physical discrimination the old units offered. It is also worth stating what the 2019 SI did to it: $h$ is now **defined** as $6.62607015\times10^{-34}$ J s exactly, so $\hbar = h/2\pi$ is defined rather than measured, and the question has been legislated out of the measurement system rather than answered by it. The arithmetic of the old measurement stands as the traceable record.

**Fourth.** $a_0$ and $\omega = 2\pi\nu$ remain genuinely useful first-power carriers of the constant in real, tabulated quantities (a Bohr radius in metres, a transition frequency in rad s⁻¹) — but they are *definitions* of units of length and angle, and no experiment can separate a defined unit from the constant used to define it. Computed, never measured.

## Further Reading

- [The Fine-Structure Constant: where the same $4\pi$ and the same $\hbar$ cancel out of α = e²/2ε₀hc](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/)
- [The Quantum Harmonic Oscillator: the ground state's π^(1/4), and a spectrum that carries no constant at all](/blog/posts/2026-10-07-quantum-harmonic-oscillator-ground-state-cancels-circle-constant-golden-pi/)
- [The Fermi Sphere: counting quantum states until the constant appears as 3π²](/blog/posts/2026-10-06-fermi-sphere-quantum-state-counting-computes-circle-constant-golden-pi/)
- [The Pendulum Period: an elliptic integral whose constant is linear in every amplitude](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/)
- [Machin's Formula: arctangent series, and the half-turn as a computed limit](/blog/posts/2026-08-22-machin-formula-arctangent-series-computes-circle-constant-golden-pi/)
