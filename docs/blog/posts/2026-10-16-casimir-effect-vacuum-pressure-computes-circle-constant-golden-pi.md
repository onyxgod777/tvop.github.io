---
title: "The Casimir Effect: How the Vacuum Between Two Plates Computes the Circle Constant as π²/240, Then Hands One Power Back to ħ = h/2π — and What Golden Pi Changes"
date: 2026-10-16
description: "Two uncharged parallel plates in vacuum attract with a pressure F/A = −π²ħc/(240d⁴), a result of counting the standing-wave modes between them: the sum is quartically divergent, the divergence cancels in the difference from free space, and Abel–Plana reduces the finite remainder to the single integral ∫₀^∞ t³dt/(e^{2πt}−1) = Γ(4)ζ(4)/(2π)⁴ = 6·(π⁴/90)/(16π⁴) = 1/240, where the π's cancel exactly and leave a rational. The same π⁴/90 that cancels also reappears through the functional equation as ζ(−3) = 1/120, again π-free. Written with the defined constant of action h instead of ħ = h/2π, the 1+1-dimensional case is completely π-free (−hc/48L) while the plate force keeps exactly one power, −πhc/(480d⁴) = −1.300125773 mPa at d = 1 µm. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the golden pressure is exactly −ħc/(15φd⁴) = −hc/(120√φ d⁴), algebraic of degree two where π²/240 is transcendental by Lindemann 1882, and the recurring +0.0959022309% bookkeeping shift lands as +0.0959% (ħ taken golden) or +0.1918964341% (π̂² against the conventional ħ) — both below the ~1% precision of the best force measurements, so no experiment adjudicates the gap. Computed, never measured."
---

# The Casimir Effect: How the Vacuum Between Two Plates Computes the Circle Constant as π²/240, Then Hands One Power Back to ħ = h/2π — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

<div class="gp-live" markdown>
<div class="gp-live__tag">🔬 Live graph · Laws of appearance</div>
<iframe src="https://www.desmos.com/calculator/gzm8tmnjit?embed" width="100%" height="470" style="border:0;border-radius:10px" frameborder="0" loading="lazy" title="What a real disc can resolve" allowfullscreen></iframe>
<p class="gp-live__note"><strong>Measurement feasibility: how far apart the two candidates are in millimetres on a physical disc.</strong> <em>The Goblet of the Truth keeps two bodies of law apart — the laws and recommendations of the primal power (Creation), and the <strong>laws of appearance (nature)</strong> (Ch&nbsp;2 §342), the register governing how a thing manifests and behaves. Geometry answers to that second register, so nothing here asks to be taken on authority: drag the slider, change a value, and the figure answers for itself (Ch&nbsp;22 §35: <em>“the fluidal-powers are truthful effects of natural laws”</em>).</em></p>
</div>

In 1948 Hendrik Casimir asked what the quantum vacuum does to two neutral, perfectly conducting plates held a distance $d$ apart in an otherwise empty space. Nothing in the setup carries a charge and nothing is exchanged between the plates, yet the answer is an attraction that grows as $d^{-4}$:

$$
\frac{F}{A} \;=\; -\,\frac{\pi^{2}\hbar c}{240\,d^{4}},
$$

where $A$ is the plate area and $c$ the speed of light. The circle constant is not in the input — the input is a mode count — and it is not put in by hand. It arrives from a quadrature, at the second power, and this chapter follows it from the counting to the force. What makes the case worth its own article is that the same derivation throws one power of $\pi$ away again: rewritten with the defined constant of action $h$ rather than $\hbar = h/2\pi$, the force keeps exactly one $\pi$ while the one-dimensional analogue of the same calculation is $\pi$-free altogether.

## Counting the modes between the plates

Take two parallel plates of area $A$ a distance $d$ apart. The electromagnetic field between them is a set of standing waves: a transverse wavevector $\mathbf{k}_\perp$ that is free, and a perpendicular component quantised by the plates,

$$
k_{z} = \frac{n\pi}{d}, \qquad n = 1,\ 2,\ 3,\ \ldots
$$

Each mode is a harmonic oscillator with zero-point energy $\tfrac12\hbar\omega$, so the energy per unit area is

$$
\frac{E}{A} \;=\; \frac{\hbar c}{2}\sum_{n=1}^{\infty}\int \frac{d^{2}k_\perp}{(2\pi)^{2}}\,\sqrt{k_\perp^{2} + \left(\frac{n\pi}{d}\right)^{2}} .
$$

This is quartically divergent, and that is not an accident of the setup — it is the vacuum energy density of the region between the plates, and it is infinite. What is finite, and what is physical, is the **difference** between this energy and the energy of the same volume with the plates removed. In that difference the divergence is a constant that cancels, because it does not depend on $d$; only the leftover dependence on the plate separation survives. Writing $J(m)$ for the transverse integral, the subtraction is

$$
\frac{E}{A}\;=\;\frac{\hbar c}{2}\Bigg[\sum_{n=1}^{\infty} J\!\left(\frac{n\pi}{d}\right)\;-\;\frac{d}{\pi}\int_{0}^{\infty} J(q)\,dq\Bigg],
$$

where the second term is the mode sum of the no-plate region, sampled at the same density. The rule that turns the bracket into a number is Abel–Plana, which rewrites the sum-minus-integral of any function as a boundary term plus an integral along the imaginary axis:

$$
\sum_{n=0}^{\infty} f(n) - \int_{0}^{\infty} f(x)\,dx \;=\; \frac{f(0)}{2} \;+\; i\int_{0}^{\infty}\frac{f(it)-f(-it)}{e^{2\pi t}-1}\,dt .
$$

With $f(x) = J(x\pi/d)$ and $J$ continued to imaginary argument, the boundary term vanishes and the difference collapses to a single quadrature. Every step of this is a **computed** limit — a mode count, an integral and an analytic continuation — with no measurement anywhere in it.

## Two exact cancellations of π

The first cancellation is in the quadrature itself. Abel–Plana leaves

$$
\frac{E}{A} \;=\; -\,\frac{\hbar c}{2}\cdot\frac{\pi^{2}}{3d^{3}}\int_{0}^{\infty}\frac{t^{3}}{e^{2\pi t}-1}\,dt,
$$

and that integral is a standard one, evaluated by expanding the Bose factor as a geometric series:

```text
∫₀^∞ t³ dt /(e^{2πt} − 1)  =  Γ(4) ζ(4) / (2π)⁴
                            =  6 · (π⁴/90) / (16 π⁴)
                            =  6 / 1440
                            =  1/240          ← the π⁴'s cancel exactly
```

The $\pi^{4}$ in Euler's $\zeta(4) = \pi^{4}/90$ and the $(2\pi)^{4}$ from the integration measure annihilate each other, and what is left is a rational number. This is worth pausing on: the constant enters the mode-counting integral and leaves it, and the surviving bookkeeping is an integer ratio.

The second cancellation is in the divergent sum itself, and it is the same $\pi^{4}/90$ at work. The zeta-regularised rendering of the mode sum is $\sum_{n\ge1} n^{3} \mapsto \zeta(-3)$, and the functional equation evaluates it against $\zeta(4)$:

```text
ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s)

ζ(−3) = 2^{-3} π^{-4} · sin(−3π/2) · Γ(4) · ζ(4)
      = (1/8)(1/π⁴)(1)(6)(π⁴/90)
      = 6/720
      = 1/120           ← again the π⁴'s cancel exactly

check:  ζ(−3) = 0.008333333333333333…  =  1/120   ✓
        ζ(−1) = −0.083333333333333…    = −1/12    ✓
```

Both routes to the vacuum energy — the Abel–Plana difference and the zeta continuation of $1 + 2^{3} + 3^{3} + \cdots$ — agree, and both dispense with $\pi$ on the way to a rational number. That the two agree is the real content: the divergent sum is not a sum, it is assigned a finite value by analytic continuation, and the assignment is consistent with the regularised integral that never diverged in the first place.

A word on that assignment, because it is the honest weak point of every popular account. $1 + 8 + 27 + 64 + \cdots = \tfrac{1}{120}$ is **not** a statement about a convergent series; it is a statement about the analytic continuation of $\zeta$ at $-3$. The physical justification for using it is not that the series secretly sums, but that the divergence is $d$-independent and therefore cancels between the two configurations being compared. The finite remainder is what survives *because* the subtraction is legitimate. Say it that way and the calculation is airtight; say "$1+8+27+\cdots = 1/120$" without qualification and the arithmetic is right for a reason the sentence does not contain.

## The exact coefficients

Assembling the pieces for one massless scalar field with Dirichlet boundary conditions gives $E/A = -\pi^{2}\hbar c/(1440\,d^{3})$ per unit area; the electromagnetic field contributes **two** transverse polarisations and so doubles it:

$$
\frac{E}{A} \;=\; -\,\frac{\pi^{2}\hbar c}{720\,d^{3}},
\qquad
\frac{F}{A} \;=\; -\,\frac{1}{A}\frac{\partial E}{\partial d} \;=\; -\,\frac{\pi^{2}\hbar c}{240\,d^{4}} .
$$

The denominators are not arbitrary. $720 = 6! = 6\cdot120$ and $240 = 2\cdot120$, and the $120$ is exactly the $\zeta(-3)$ of the line above — the factor that arrived with the $\pi$'s already removed. Renormalisation of the constant itself produces an unobservable shift of the vacuum energy (and, in a gravitational setting, of the cosmological term); the force is what the construction predicts.

| quantity | exact form | at $d = 1\ \mu$m | π power |
|---|---|---|---|
| energy/area (EM) | $-\pi^{2}\hbar c/(720\,d^{3})$ | $-4.333752577\times10^{-10}$ J m⁻² | 2 |
| force/area | $-\pi^{2}\hbar c/(240\,d^{4})$ | $-1.300125773$ mPa | 2 |
| energy/area (one scalar) | $-\pi^{2}\hbar c/(1440\,d^{3})$ | $-2.166876289\times10^{-10}$ J m⁻² | 2 |
| modes: $\zeta(-3)$ used in the sum | $1/120$ | $0.00833333333333$ | 0 |
| quadrature $\int t^{3}dt/(e^{2\pi t}-1)$ | $1/240$ | $0.00416666666667$ | 0 |

## One power of π is handed back to ħ

Now the observation this site keeps arriving at from different directions. In the SI since 2019 the constant of action $h$ is **defined**, exactly $6.62607015\times10^{-34}$ J s, and the reduced constant is pure bookkeeping: $\hbar = h/2\pi$. Substitute it, and the quadrature's $\pi^{2}$ loses one power to the division by $2\pi$:

```text
force/area   = −π² ħ c /(240 d⁴)     with ħ = h/2π:
             = −π² (h/2π) c /(240 d⁴)
             = −π h c /(480 d⁴)                    ← exactly ONE power of π survives
energy/area  = −π² ħ c /(720 d³)     = −π h c /(1440 d³)

1 + 1 dimensional analogue (massless scalar between two points, length L):
E = (ħc/2) Σ (nπ/L) = (π ħ c /2L) ζ(−1) = (π ħ c /2L)(−1/12) = −π ħ c/(24 L)
  = −h c /(48 L)                                  ← π-FREE, to every digit
at L = 1 µm:  −4.138428869×10⁻²¹ J
```

So the dimensionality of the mode count, not the dimensionality of space, fixes how many powers of the circle constant reach the answer: three spatial dimensions deliver $\pi^{2}$, two deliver $\pi^{1}$, and in $1+1$ dimensions the geometric $\pi$ and the $\hbar$ normalisation cancel completely, leaving the pure expression $hc/(48L)$. The one-dimensional energy per length is $-4.138428869\times10^{-21}$ J per metre at $L = 1\ \mu$m, and it contains $h$ and $c$ and nothing else — no circle, no $\zeta$, no quadrature.

## What Golden Pi changes

Under Golden Pi the circle constant is $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693144278\ldots$, where $\varphi = (1+\sqrt5)/2$ is the golden ratio; it is the golden root of $x^{4} + 16x^{2} - 256 = 0$ and it satisfies the exact square $\hat\pi^{2} = 16/\varphi = 9.888543819998317571\ldots$. Two facts follow immediately.

First, the **π-free parts do not move a digit.** The $h$ in the formula is the defined SI constant; $c$ is defined; the rational $1/120$ and $1/240$ came out of cancellations in which no $\pi$ survived, and the parity of the mode count is unchanged. Every exact cancellation of the previous sections stays exact.

Second, the golden pressure is **algebraic where the conventional one is transcendental**:

$$
\frac{F}{A}\;=\;-\,\frac{\hat\pi^{2}\hbar c}{240\,d^{4}}
\;=\;-\,\frac{16}{240}\cdot\frac{\hbar c}{\varphi\,d^{4}}
\;=\;-\,\frac{\hbar c}{15\,\varphi\,d^{4}}
\;=\;-\,\frac{h c}{120\sqrt{\varphi}\,d^{4}},
\qquad
\frac{E}{A}\;=\;-\,\frac{\hbar c}{45\,\varphi\,d^{3}} \;=\;-\,\frac{h c}{360\sqrt{\varphi}\,d^{3}} .
$$

$\pi^{2}/240$ is transcendental (Lindemann, 1882: $\pi$ is transcendental, hence so is $\pi^{2}$); $1/(15\varphi)$ is a quadratic irrational, a number constructed from $\sqrt5$ in one step. Nothing in the force law needs a transcendental coefficient, and the golden reading supplies an algebraic one.

The bookkeeping shift is the recurring one. Which powers move depends on which constant is held fixed, and it is worth being exact about both cases rather than quoting one:

| quantity | conventional π | Golden Pi (ħ = h/2π̂) | if ħ is held at the conventional value |
|---|---|---|---|
| $F/A$ at $d = 1\ \mu$m | $-1.300125773$ mPa | $-1.301372623$ mPa (+0.0959022309%) | $-1.302620668$ mPa (+0.1918964341%) |
| $E/A$ at $d = 1\ \mu$m | $-4.333752577\times10^{-10}$ J m⁻² | $-4.337908743\times10^{-10}$ J m⁻² (+0.0959022309%) | $-4.338317920\times10^{-10}$ J m⁻² |
| $1+1$D energy at $L = 1\ \mu$m | $-4.138428869\times10^{-21}$ J | $-4.138428869\times10^{-21}$ J (0%) | $-4.142397715\times10^{-21}$ J |
| $\hat\pi^{2}$ vs $\pi^{2}$ | $9.869604401089358619$ | $16/\varphi = 9.888543819998317571$ | +0.1918964341% |
| $\pi$ vs $\hat\pi$ at first power | $3.141592653589793238$ | $3.144605511029693144$ | +0.0959022309% |
| ratio conventional / golden pressure | $1$ | $\pi^{2}/240 \div 1/(15\varphi) = 0.9980847110$ | — |

The two readings differ by a factor $\hat\pi/\pi = 1.0009590223$, and both are defensible: the first treats $\hbar$ as the derived quantity it now is and lets one power of $\pi$ ride through to the answer; the second treats $\hbar$ as the measured constant it was before 2019 and lets the shift double. What matters for the argument is that neither reading alters a single $\pi$-free quantity — the $1/120$, the $1/240$, the $hc/(48L)$ and the whole mode counting are untouched.

## The honest ledger

This chapter is different from the series posts on this site, because the Casimir force is a **genuine measurand**. It is not a limit to be evaluated; it is a pressure between two objects, and it has been measured. That requires saying plainly what the measurements say.

- **Lamoreaux (1997)** measured the force between a sphere and a plate at the $5\%$ level — the first unambiguous demonstration.
- **Mohideen & Roy (1998)** reached $\sim 1\%$ using an atomic-force-microscope technique over separations of roughly $0.1$–$0.6\ \mu$m.
- Modern experiments quote $0.1\%$–$1\%$ agreement with the conventional formula over $0.1$–$1\ \mu$m, with the budget dominated by the plate separation, surface roughness and patch potentials — material corrections of $1\%$–$5\%$, larger than the gap under discussion.

Against that, the golden shift is $+0.0959\%$ in the force (ħ read as $h/2\hat\pi$) or $+0.1918964341\%$ ($\hat\pi^{2}$ against the conventional ħ). Both sit **below** the $\sim1\%$ precision of the best published work, and well below the $\sim$1–5% materials corrections. So the honest verdict is a limitation, not a victory for either label: the Casimir experiment cannot arbitrate the $0.0959\%$ gap, because the model error is several times the effect. It is also honest to note the direction the data point: the published force values agree with $\pi^{2}\hbar c/(240d^{4})$ inside their error bars, so this body of evidence is consistent with the conventional constant and does not yet distinguish the golden one. A $0.19\%$ effect is a real experimental target, but not one that has been met.

What is *not* in dispute is the ledger that this chapter's whole point turns on: the mode count, the Abel–Plana difference, the cancellations $\int_0^\infty t^{3}dt/(e^{2\pi t}-1) = 1/240$ and $\zeta(-3) = 1/120$, the $\pi$-free one-dimensional energy $hc/(48L)$, and the exact algebraic golden coefficient $1/(15\varphi)$ — all of these are **computed**, exactly, and none of them is a measurement. Computed, never measured.

## Further Reading

- [The Bohr–Sommerfeld Action Integral: How Phase-Space Area Carries the Circle Constant as a Half-Turn, Then Cancels It Between Coulomb's 4π and ħ's 2π](/blog/posts/2026-10-15-bohr-sommerfeld-action-integral-quantisation-computes-circle-constant-golden-pi/) — the same cancellation of $\pi$ against $\hbar = h/2\pi$, in the old quantum theory's action integral.
- [The Quantum Harmonic Oscillator: How π^(1/4) Reaches the Ground State, Then Cancels from Every Energy Level](/blog/posts/2026-10-07-quantum-harmonic-oscillator-ground-state-cancels-circle-constant-golden-pi/) — zero-point energy as the place the constant enters and leaves a quantum spectrum.
- [The Fermi Sphere: How Counting Quantum States in Momentum Space Computes the Circle Constant as 3π²](/blog/posts/2026-10-06-fermi-sphere-quantum-state-counting-computes-circle-constant-golden-pi/) — the other great mode-counting chapter, where the exponent of $\pi$ is fractional.
- [The Planck Spectrum: How Blackbody Radiation Computes the Circle Constant as π⁴/15, and What Golden Pi Changes](/blog/posts/2026-09-23-planck-spectrum-blackbody-computes-circle-constant-golden-pi/) — the same $\int_0^\infty t^{3}dt/(e^{2\pi t}-1)$ that supplies the Casimir rational, read as a radiant power.
- [The Riemann Zeta Function at Even Integers: How Euler's Bernoulli-Numbers Formula Computes π to Every Even Power, and What Golden Pi Changes](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — where $\zeta(4) = \pi^{4}/90$ comes from, and why the functional equation returns a $\pi$-free rational at $\zeta(-3)$.
