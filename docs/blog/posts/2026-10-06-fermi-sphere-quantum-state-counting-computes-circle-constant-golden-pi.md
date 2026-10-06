---
title: "The Fermi Sphere: How Counting Quantum States in Momentum Space Computes the Circle Constant as 3π² — and What Golden Pi Changes"
date: 2026-10-06
description: "Fill a metal's electron states from the bottom up and the occupied set is a sphere in momentum space — the Fermi sphere — whose radius comes from a pure counting problem: how many modes of a box of side L fit inside a ball of radius k_F? One point per cell (2π/L)³ of k-space, two spin states per point, and the ball's volume (4π/3)k_F³ give n = k_F³/(3π²), so the circle constant enters as the bare number 3π² = 29.6088132032681 — computed from the sphere volume and the mode spacing, never measured. The exponent matters: k_F ∝ π^(2/3) and E_F ∝ π^(4/3), and the general rule k_F ∝ π^(⌈d/2⌉/d) means the constant enters with fractional exponents 1, 1/2, 2/3, 1/2, 3/5 in one to five dimensions. For copper (n = 8.47×10²⁸ m⁻³) this gives k_F = 1.358630845×10¹⁰ m⁻¹, E_F = 7.0327612948 eV, T_F = 81 611.8 K, v_F = 1.5729×10⁶ m/s and a Sommerfeld coefficient of 0.50275 mJ mol⁻¹ K⁻². Under Golden Pi (π̂ = 4/√φ = 3.1446055110296931443…, root of x⁴ + 16x² − 256 = 0) the counting constant becomes 3π̂² = 48/φ = 29.6656314599950 exactly — algebraic, where 3π² is transcendental by Lindemann (1882) — and every quantity shifts by a power of the recurring 0.0959022309% gap: k_F and the specific-heat coefficient by ×2/3 (+0.0639246058%), E_F by ×4/3 (+0.1278900751%), the density of states by ×2 (−0.1915288970%), putting copper's Fermi energy 9.0 meV higher at 7.0417554985 eV. The exact integer ledger is printed: counting lattice points in a sphere of radius R converges on (4/3)πR³ and separates the two labels once R ≳ 40, while the measured ledger is blunt that no experiment can — ARPES resolves E_F to tens of meV and the free-electron bulk modulus of copper misses its measured 140 GPa by more than a factor of two. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Fermi Sphere: How Counting Quantum States in Momentum Space Computes the Circle Constant as 3π² — and What Golden Pi Changes

Take a piece of copper and ask where its electrons live. In the free-electron picture that Arnold Sommerfeld set out in 1927, the answer is startlingly plain: they live in a **sphere**. Not in space — in *momentum* space. Each electron has a wavevector $\mathbf{k}$, and its energy is

$$E = \frac{\hbar^2 k^2}{2m},$$

which depends only on the *length* of $\mathbf{k}$, never on its direction. So if you fill the available states from the bottom up, respecting Pauli's exclusion principle, the occupied set is a solid ball of radius $k_F$ — the **Fermi sphere** — and the entire content of the theory's zero-temperature state is the single number $k_F$, the **Fermi wavevector**.

That number is not a measurement. It is a *count*. And the circle constant falls out of the count as the bare number $3\pi^2$:

$$n = \frac{k_F^{\,3}}{3\pi^2} \qquad\Longleftrightarrow\qquad k_F = (3\pi^2 n)^{1/3}.$$

This article asks the same four questions the rest of this series asks of any formula: where exactly the constant enters, whether it is **computed** or measured, whether it cancels anywhere, and what changes if the constant is the golden value $\hat\pi = 4/\sqrt\varphi$ instead of the analytic $3.14159\ldots$.

## The box, the modes, and the ball

Put the electrons in a cube of side $L$ and impose periodic boundary conditions. The allowed wavevectors are then equally spaced points

$$\mathbf{k} = \frac{2\pi}{L}\,(n_x, n_y, n_z), \qquad n_x, n_y, n_z \in \mathbb{Z},$$

one point per cell of volume $(2\pi/L)^3$ in $\mathbf{k}$-space. That spacing is exact arithmetic — the quantisation of a periodic box, the same computation that fixes the harmonics of a vibrating string and the modes of a microwave cavity. Each $\mathbf{k}$-point carries two spin states, and energy depends only on $|\mathbf{k}|$, so the occupied set is the ball $|\mathbf{k}| \le k_F$. Counting states is then nothing but dividing one volume by another:

$$
N \;=\; 2\cdot\frac{\tfrac{4}{3}\pi k_F^{3}}{(2\pi/L)^{3}}
\;=\; 2\cdot\frac{\tfrac{4}{3}\pi k_F^{3}L^{3}}{8\pi^{3}}
\;=\; \frac{V k_F^{3}}{3\pi^{2}} .
$$

Divide by the volume and the density of electrons is $n = k_F^{3}/(3\pi^{2})$. Everything here is computed: the sphere's volume $\tfrac{4}{3}\pi k_F^{3}$ is the computed limit of inscribed and circumscribed polyhedra — the very quantity Archimedes trapped between $\tfrac{223}{71}$ and $\tfrac{22}{7}$ — and the cell volume $(2\pi/L)^3$ is the exact separation of the box's modes. **Nothing in this derivation is a measurement.** Copper's density of conduction electrons is measured; the constant inside the formula that turns that density into a wavevector is computed.

## Where the constant sits: one sphere, one cell

It is worth isolating the constant's role, because the Fermi gas is a clean example of a case in which it enters **twice** and only once survives.

| Ingredient | Value | Source |
|---|---|---|
| Unit sphere volume (numerator) | $\tfrac{4}{3}\pi$ | computed quadrature limit |
| Cell volume in $\mathbf{k}$-space (denominator) | $(2\pi)^3 = 8\pi^3$ | exact mode spacing of the box |
| Spin degeneracy | $2$ | Pauli / spin |
| Net constant per state | $\dfrac{2\cdot\tfrac43\pi}{8\pi^3} = \dfrac{1}{3\pi^2}$ | arithmetic |

The constant enters once as $\pi$ (the sphere) and once as $\pi^3$ (the cube of the mode spacing), and the quotient leaves $\pi^{-2}$:

$$n = \frac{k_F^{3}}{3\pi^{2}}, \qquad \frac{1}{3\pi^{2}} = 0.0337728039\ldots$$

The bare number in the formula is therefore $3\pi^2 = 29.6088132032680759\ldots$, and it is a *density-of-states* constant: the number of states per unit volume per unit of $k^3$.

A short code block makes the same arithmetic explicit, at twenty digits.

```python
from mpmath import mp, pi
mp.dps = 20
sphere = 4*pi/3              # unit-sphere volume, computed limit
cell   = (2*pi)**3           # one k-point per box-mode cell
net    = 2*sphere/cell       # two spin states per point
print(net)                    # 0.0337728038997893...
print(1/net)                  # 29.6088132032680759...  = 3*pi**2
print(3*pi**2)                # 29.6088132032680759...
```

## Copper in numbers

Everything downstream is algebra on $k_F$. With the standard constants ($\hbar = 1.054571817\times10^{-34}$ J s, $m_e = 9.1093837015\times10^{-31}$ kg) and copper's measured conduction-electron density $n = 8.47\times10^{28}$ m$^{-3}$:

| Quantity | Formula | Value for copper |
|---|---|---|
| Fermi wavevector | $(3\pi^2 n)^{1/3}$ | $1.358630845\times10^{10}$ m$^{-1}$ |
| Fermi energy | $\hbar^2k_F^2/2m_e$ | $7.0327612948$ eV |
| Fermi temperature | $E_F/k_B$ | $81\,611.8$ K |
| Fermi velocity | $\hbar k_F/m_e$ | $1.5729\times10^{6}$ m s$^{-1}$ |
| Mean kinetic energy | $\tfrac35 E_F$ | $4.2196567769$ eV |
| States at $E_F$ | $\tfrac{3}{2E_F}$ | $0.2133$ per eV per electron |
| Free-electron pressure | $\tfrac25 nE_F$ | $38.18$ GPa |
| Free-electron bulk modulus | $\tfrac23 nE_F$ | $63.63$ GPa |

Those are the textbook free-electron values (a quoted $E_F$ of about 7.00 eV for copper; the small difference is the choice of constants, not physics). Note what has *not* moved: the mean energy is $\tfrac35 E_F$, the pressure is $\tfrac25 n E_F$, the bulk modulus $\tfrac23 n E_F$ — every ratio of powers of $k_F$ is pure arithmetic, and the constant sits in one place only, inside $k_F$.

## The constant enters with a fractional exponent

The Fermi gas is where the circle constant first appears under a **fractional power**, and that is the detail that decides how much any change in the label is worth. Count states in one, two and three dimensions with spin degeneracy included and the density relation is:

| Dimension | State count | Density relation | Solve for $k_F$ | $\pi$-power |
|---|---|---|---|---|
| 1D | $Lk_F/\pi$ | $n = k_F/\pi$ | $k_F = \pi n$ | $\pi^{1}$ |
| 2D | $A k_F^2/(2\pi)$ | $n = k_F^2/(2\pi)$ | $k_F = \sqrt{2\pi n}$ | $\pi^{1/2}$ |
| 3D | $V k_F^3/(3\pi^2)$ | $n = k_F^3/(3\pi^2)$ | $k_F = (3\pi^2 n)^{1/3}$ | $\pi^{2/3}$ |

The pattern is not an accident. The number of states with $|\mathbf{k}| \le k_F$ is the volume of a $d$-ball, $\pi^{d/2}k_F^{d}/\Gamma(d/2+1)$, divided by the cell volume $(2\pi)^d$ — and the gamma function carries a $\pi^{1/2}$ precisely when $d$ is odd. The general rule is

$$k_F \propto \pi^{\lceil d/2\rceil/d}\, n^{1/d}, \qquad E_F \propto \pi^{2\lceil d/2\rceil/d}\, n^{2/d},$$

so the constant's exponent runs $1,\ \tfrac12,\ \tfrac23,\ \tfrac12,\ \tfrac35$ in dimensions one through five. In three dimensions the Fermi energy carries $\pi^{4/3}$ — larger than one, smaller than two. Any relabelling of the constant is therefore **diluted or amplified by a rational factor**, and in the three-dimensional metal it is diluted for $k_F$ and amplified for $E_F$. That is the whole story of the table below.

## What Golden Pi changes

Take the golden value $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, where $\varphi = (1+\sqrt5)/2$ is the golden ratio, and $\hat\pi$ is the positive root of $x^4 + 16x^2 - 256 = 0$. The convention throughout this series is the same: the constant is replaced, the algebra is untouched.

| Quantity | Conventional | Golden | Shift |
|---|---|---|---|
| Counting constant $3\pi^2$ | $29.6088132032681$ | $3\hat\pi^2 = 48/\varphi = 29.6656314599950$ | $+0.1915288970\%$ |
| $k_F \propto \pi^{2/3}$ | $1.358630845\times10^{10}$ m⁻¹ | $1.359499344\times10^{10}$ m⁻¹ | $+0.0639246058\%$ |
| $E_F \propto \pi^{4/3}$ | $7.0327612948$ eV | $7.0417554985$ eV | $+0.1278900751\%$ ($+8.994$ meV) |
| $T_F$ | $81\,611.8$ K | $81\,716.2$ K | $+0.1278900751\%$ |
| Density of states $\propto \pi^{-2}$ | — | — | $-0.1915288970\%$ |
| Sommerfeld $\gamma \propto \pi^{2/3}$ | $0.50275$ mJ mol⁻¹ K⁻² | $0.50307$ mJ mol⁻¹ K⁻² | $+0.0639246058\%$ |

The recurring gap of this series, $\hat\pi/\pi - 1 = 0.0959022309\%$, is not what shows up here. Because the constant rides under a cube root in $k_F$, only **two thirds** of the gap survives there; because the Fermi energy squares the wavevector, **four thirds** of it appears in $E_F$; because the density of states carries $\pi^{-2}$, the shift is **twice** the gap and in the opposite direction.

Where the golden claim is exact, it is credited exactly. Two identities hold to forty digits and are not approximations:

$$3\hat\pi^2 = \frac{48}{\varphi} = 48(\varphi - 1), \qquad 2\hat\pi^2 = \frac{32}{\varphi}.$$

So under the golden label the state-counting constant is an **algebraic** number of degree two, and the Fermi wavevector

$$k_F^{\text{golden}} = \left(\frac{48\,n}{\varphi}\right)^{1/3} = (48n)^{1/3}\varphi^{-1/3}$$

is algebraic in $n^{1/3}$ — a root of a polynomial with rational coefficients. The conventional $(3\pi^2n)^{1/3} = 3^{1/3}\pi^{2/3}n^{1/3}$ is not: $\pi$ is transcendental by Lindemann's theorem (1882), so no polynomial with rational coefficients has it as a root, and neither does $\pi^{2/3}$. That contrast — an algebraic constant of the constructed world against a transcendental one — is the honest core of the golden case, and it is a statement about *forms*, not about any metal.

## The discrete ledger: counting beats the gap

The one place where this circle of ideas is genuinely decisive is not a laboratory. It is pure counting. Ask how many integer triples $(n_x,n_y,n_z)$ satisfy $n_x^2+n_y^2+n_z^2 \le R^2$ — the number of box modes inside a sphere of radius $R$ — and compare it with the smooth sphere volume $(4/3)\pi R^3$ that the Fermi-gas formula uses. The count is exact integer arithmetic; the smooth value is the computed limit. They must agree, and the residual is a pure lattice effect, a surface term of order $R^{21/16}$ at worst (the best known bound for the three-dimensional sphere problem, Heath-Brown 1999).

Because the golden gap grows like $R^3$ (it is $\tfrac43(\hat\pi-\pi)R^3$) while the lattice error grows like a power below 2, the counting eventually separates the labels — and the table shows where.

| $R$ | Lattice points | $\tfrac43\pi R^3$ | Residual | Golden target | $\hat\pi$-gap / residual |
|---|---|---|---|---|---|
| 5 | 515 | 523.5987756 | 8.5988 | 9.101 | 0.20× (error wins) |
| 10 | 4 169 | 4 188.790205 | 19.790 | 23.807 | 0.20× |
| 20 | 33 401 | 33 510.32164 | 109.32 | 141.46 | 0.29× |
| 30 | 113 081 | 113 097.3355 | 16.34 | 124.80 | **7.64×** |
| 40 | 267 761 | 268 082.5731 | 321.57 | 578.67 | **1.80×** |
| 50 | 523 305 | 523 598.7756 | 293.78 | 795.92 | **2.71×** |
| 100 | 4 187 857 | 4 188 790.205 | 933.20 | 4 950.35 | **4.30×** |

From $R \approx 40$ onward the integer count sits closer to the conventional sphere volume than to the golden one, and the margin widens as $R^{11/8}$ or faster. This is the same verdict the two-dimensional Gauss circle problem reached in an earlier article: the exact count decides the label, and it decides it in favour of $3.14159\ldots$, because the count knows nothing of any measurement. It is worth stating plainly, as this series always does: an exact integer computation like this is evidence, and here the evidence runs against the golden value.

## The honest ledger: why 9 meV is invisible

The temptation is to carry the same verdict into the laboratory. It does not survive contact with real metal.

**Photoemission.** Angle-resolved photoemission measures the Fermi level of copper at about $7.0$ eV, with instrument resolution and band-structure corrections that push the uncertainty into the tens of millielectronvolts at best, and hundreds when the band is not free-electron-like at all. The golden label would raise copper's free-electron $E_F$ from $7.0327612948$ eV to $7.0417554985$ eV — **9.0 meV**. That is below the resolution of the measurement, and the measurement is not of a free-electron gas anyway: copper's $d$-bands sit right below $E_F$ and reshape the density of states that the simple count assumes.

**Specific heat.** The Sommerfeld coefficient is a genuinely sensitive number at low temperature — $\gamma = (\pi^2/2)R/T_F$ for a free-electron metal, giving $0.50275$ mJ mol⁻¹ K⁻² for copper against a measured value near $0.505$, with the small excess understood as electron–phonon mass enhancement. The golden shift is $+0.0003$ mJ mol⁻¹ K⁻², which is a hundred times smaller than the enhancement the theory already has to correct for.

**The bluntest row.** The same density model predicts a bulk modulus of $63.6$ GPa for copper; the measured value is about $140$ GPa. The model is wrong by more than a factor of two on an absolute mechanical property, because the free-electron picture ignores the ion cores. A model that misses by $120\%$ cannot arbitrate a $0.13\%$ question.

**One channel that is not hopeless.** In a two-dimensional electron gas the relation $n = k_F^2/(2\pi)$ can be checked with two independent measurements — the Hall density and the period of Shubnikov–de Haas oscillations — and there the $\pi$-exponent is $\tfrac12$, so the golden shift is only $0.0479396\%$. High-mobility samples reach a precision of a few parts in $10^{3}$ on each quantity: the same order as the shift. The published agreement is consistent with the analytic constant without closing the door at the $0.05\%$ level, and this series reports that as a **boundary case, not a verdict**. And in every case the constant is still computed: the measurements fix $n$ and the Fermi area $A_F$, and the constant is the number you divide by, never the thing on the bench.

## Computed, never measured

The Fermi sphere is a good place to say plainly what the distinction means. The number $3\pi^2$ in a metal's density formula was never measured and never could be: it is the volume of a ball divided by the volume of a cell, two computed limits whose ratio is a pure number. Copper's electron density is a measurement; the wavevector it implies is a computation; and the constant appears in that computation under a cube root, so that in three dimensions it is worth two thirds of itself to $k_F$, four thirds to $E_F$, and minus two to the density of states.

Under the golden label the algebra does not bend: the sphere is still a sphere, the modes are still one per $(2\pi/L)^3$, and the answer is still a compact algebraic number with $\varphi$ in it. Under the conventional label the same formula carries a transcendental number, which is not in itself a defect — the whole of classical analysis is built on it — but which does mean the constant in a metal's Fermi energy is a **computed** transcendental, not a reading off any instrument. Where the golden value is exact, it is exact: $3\hat\pi^2 = 48/\varphi$, $2\hat\pi^2 = 32/\varphi$, and $k_F$ algebraic in $\varphi$. Where the evidence is decisive — the integer counts — it points to $3.14159\ldots$. Both statements belong in the same article, and neither is allowed to borrow authority from the other.

## Further Reading

- [The Gauss Circle Problem: How Counting Lattice Points Computes the Circle Constant](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/) — the two-dimensional version of this article's exact integer ledger, with Jacobi's $r_2(n)$ and the error programme from Gauss to Huxley.
- [The n-Dimensional Ball: How Hypersphere Volumes Compute the Circle Constant](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/) — the $\pi^{d/2}/\Gamma(d/2+1)$ volume formula behind the dimension table above, and the gamut of exponents it produces.
- [The Planck Spectrum: How Blackbody Radiation Computes the Circle Constant](/blog/posts/2026-09-23-planck-spectrum-blackbody-computes-circle-constant-golden-pi/) — the other great physical constant with $\pi$ under a fractional exponent, and a measured law that cannot separate the labels.
- [The Fine-Structure Constant: How 4π Cancels from the Physical Constant](/blog/posts/2026-09-13-fine-structure-constant-4pi-cancels-golden-pi/) — the case in which the circle constant genuinely cancels from a measured quantity, leaving no handle at all.
- [Kepler's Third Law: How Orbital Mechanics Computes the Circle Constant](/blog/posts/2026-09-22-keplers-third-law-orbital-mechanics-compute-circle-constant-golden-pi/) — a companion case in which a measured constant *does* fix the label, and why the astronomical data are decisive where a metal's are not.
