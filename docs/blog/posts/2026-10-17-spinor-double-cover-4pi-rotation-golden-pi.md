---
title: "The 4π Turn: How a Spinor Pays the Circle Constant Back Twice, Why the Minus Sign Is Exact — and What Golden Pi Cannot Touch"
date: 2026-10-17
description: "A spin-½ state rotated through one full turn returns as −|ψ⟩ and only through two turns as +|ψ⟩: the rotation operator exp(−iθ n·σ/2) has the circle constant in its exponent as a half-angle, because SU(2) covers SO(3) two-to-one and the loop that a 2π rotation traces in SO(3) is the non-trivial class of π₁(SO(3)) = ℤ₂. The ± sign is exact — an algebraic group element, −I — and needs no numerical value of π at all: it is holonomy, not arithmetic, and neutron interferometry (Rauch et al., 1975) observed the interference pattern return only after 720°. Verified here, the matrices are exactly −I at θ = 2π and exactly +I at θ = 4π, det = 1 throughout. The one place the constant survives at the first power in this subject is the Berry phase of a spin in a slowly turned field, γ = −½Ω with Ω = 2π(1 − cos θ) the cone's solid angle — and Ω = π sr exactly at a 60° cone. Under Golden Pi (π̂ = 4/√φ = 3.144605511…, π̂² = 16/φ, root of x⁴ + 16x² − 256 = 0) every solid angle and every Berry phase scales by the recurring +0.0959022309%, the sphere's 4π sr becomes the algebraic 16/√φ sr = 12.5784220441187724, the 45° Berry phase π(1−√2/2) = 0.9201511850 becomes the algebraic 2(2−√2)/√φ = 0.9210336300, and one steradian drops from 3282.806350 deg² to 3276.518827 deg² (−0.1915288970%, the squared power) — while the double cover is untouched, because a golden '2π̂' would be 360.345° of actual rotation, overshooting a closed loop by 0.3452480310° and leaving the spinor at −exp(−i·0.0060257149 n·σ) instead of −I. Topology fixes the integer; only the label carries the constant. Computed, never measured."
---

# The 4π Turn: How a Spinor Pays the Circle Constant Back Twice, Why the Minus Sign Is Exact — and What Golden Pi Cannot Touch

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Rotate any ordinary object through one full turn and it comes back to itself. Rotate an electron, a neutron, or any spin-½ particle through one full turn and its quantum state comes back with a minus sign in front of it: $|\psi\rangle \to -|\psi\rangle$. Only a second full turn restores the original state, $|\psi\rangle \to +|\psi\rangle$, and the interference pattern of a split beam returns to itself only after **720°** of rotation rather than 360°.

This article follows the circle constant through that fact. It enters the rotation operator as a **half-angle** in the exponent, it is present in the very expression that produces the minus sign — and yet the minus sign is *exact*, an algebraic group element with no numerical constant in it at all. That combination, a constant visibly in the formula and wholly absent from the result, is worth a chapter of its own, because it is the cleanest case on this site where a $\pi$ can be seen being used and then being paid back in full.

## The rotation operator, written out

A rotation of a spin-½ state by angle $\theta$ about a unit axis $\mathbf{n}$ is performed by the unitary

$$
U(\theta,\mathbf{n}) \;=\; \exp\!\left(-\,\frac{i\,\theta}{2}\,\mathbf{n}\cdot\boldsymbol{\sigma}\right)
\;=\; \cos\frac{\theta}{2}\,\mathbb{1} \;-\; i\,\sin\frac{\theta}{2}\;\mathbf{n}\cdot\boldsymbol{\sigma},
$$

where $\boldsymbol{\sigma} = (\sigma_x,\sigma_y,\sigma_z)$ are the Pauli matrices and $\mathbb{1}$ is the $2\times2$ identity. The step from the exponential to the cosine and sine is not an approximation: it follows because $(\mathbf{n}\cdot\boldsymbol{\sigma})^{2} = \mathbb{1}$ for any unit $\mathbf{n}$, so the power series splits into the even and odd series of $\cos$ and $\sin$ exactly.

Now put in the three interesting angles. Since $\sigma_z = \mathrm{diag}(1,-1)$,

| Rotation angle | $\cos(\theta/2)$ | $\sin(\theta/2)$ | $U(\theta,\hat z)$ |
|---|---|---|---|
| $\theta = \pi/2$ (quarter turn) | $\sqrt2/2$ | $\sqrt2/2$ | $\tfrac{1}{\sqrt2}\begin{pmatrix}1-i&0\\0&1+i\end{pmatrix}$ |
| $\theta = \pi$ (half turn) | $0$ | $1$ | $-i\sigma_z = \begin{pmatrix}-i&0\\0&i\end{pmatrix}$ |
| $\theta = 2\pi$ (one turn) | $-1$ | $0$ | $-\mathbb{1}$ |
| $\theta = 4\pi$ (two turns) | $+1$ | $0$ | $+\mathbb{1}$ |

Every entry is an exact algebraic number. The minus sign at one full turn is the single number $-1$, delivered by $\cos(\pi/2 \cdot 2) = \cos\pi = -1$ — but note what kind of statement that is: the $-1$ does not depend on *what* $\pi$ equals. It depends on the fact that the argument of the cosine has reached **half a period**, and half a period of the cosine is where it takes its minimum value. Any constant that names half a period would produce $-1$ there, by construction.

Run the matrices and check it directly:

```python
import math

def U(theta, n=(0, 0, 1)):                     # exp(-i theta n.sigma/2)
    nx, ny, nz = n
    s = [[nx, ny - 1j*nz], [ny + 1j*nz, -nx]]  # sigma.n
    c, sn = math.cos(theta/2), math.sin(theta/2)
    return [[(c if i == j else 0) - 1j*sn*s[i][j] for j in range(2)]
            for i in range(2)]

def resid(M, sign):                            # max |M - sign*I|
    return max(abs(M[i][j] - sign*(1 if i == j else 0))
               for i in range(2) for j in range(2))

det = lambda M: M[0][0]*M[1][1] - M[0][1]*M[1][0]

for label, t, sign in (("2*pi", 2, -1), ("4*pi", 4, +1)):
    M = U(t*math.pi)
    print("theta = %s  max|U - (%sI)| = %.1e  |det - 1| = %.1e"
          % (label, "-" if sign < 0 else "+", resid(M, sign), abs(det(M) - 1)))
```

```
theta = 2*pi  max|U - (-I)| = 1.2e-16  |det - 1| = 0.0e+00
theta = 4*pi  max|U - (+I)| = 2.4e-16  |det - 1| = 0.0e+00
```

The residuals are machine epsilon — $10^{-16}$ on a matrix whose entries are of order one — so the deviation from $-\mathbb{1}$ at one turn and from $+\mathbb{1}$ at two is floating-point noise, not structure. The determinant is $+1$ exactly as computed, which is the statement that these matrices live in $SU(2)$ and not merely in $U(2)$.

## Where the half-angle comes from

The factor $\theta/2$ in the exponent is the whole story, and it has a topological origin. Rotations of three-dimensional space form the group $SO(3)$; the matrices above form $SU(2)$; and $SU(2)$ is a **double cover** of $SO(3)$ — a two-to-one map, so that two distinct $SU(2)$ elements, $U$ and $-U$, describe the *same* rotation of space. In quaternion language the same fact looks like this: the unit quaternion for a rotation by $\theta$ about $\mathbf{n}$ is

$$
q \;=\; \cos\frac{\theta}{2} \;+\; \sin\frac{\theta}{2}\,\bigl(n_x\,\mathbf{i} + n_y\,\mathbf{j} + n_z\,\mathbf{k}\bigr),
$$

and a rotation is applied by the sandwich $v \mapsto q\,v\,q^{*}$, in which the half-angle appears **twice** and cancels back to $\theta$. Set $\theta = 2\pi$: the quaternion is $\cos\pi + \sin\pi\,(\cdot) = -1$, the quaternion $-1$, which is not the identity quaternion $+1$ even though the sandwich by $-1$ returns every vector unchanged, because $(-1)v(-1)^{*} = v$.

The topological content is exact and integer-valued. The set of rotations reachable by continuous turning from the identity is the fundamental group $\pi_1(SO(3)) = \mathbb{Z}_2$: there are exactly two homotopy classes of closed loops, the contractible ones and the non-contractible ones, and a full $2\pi$ rotation is the generator of the non-trivial class. That is the "belt trick" or "plate trick" you can perform with your hand: a $360°$ twist of a book held on a belt cannot be undone without rotating the book, while a $720°$ twist can be undone by passing the belt around it. The loop in $SO(3)$ traced by $2\pi$ does not close up to nothing; the spinor records that failure as a sign. No number of digits of any circle constant enters that count. It is $\mathbb{Z}_2$, an integer mod 2.

This is the first half of the ledger, and it is worth stating in the sharpest form available: **the sign is holonomy, not arithmetic.** The constant $\pi$ names the angle at which the loop closes; the sign records that the loop does not close in the covering group; and the second statement is true for every value of the first.

## The interferometer that saw it

A global minus sign on a state is not directly observable — $|\psi\rangle$ and $-|\psi\rangle$ give the same probabilities. It becomes observable only as a **relative** phase, in interference against a reference beam, and that is how it was seen.

In 1975 a group at Grenoble and Vienna — H. Rauch, A. Zeilinger, G. Badurek, A. Wilfing, W. Bauspiess and U. Bonse, *Physics Letters A* **54** (1975) — split a thermal neutron beam in a perfect-crystal interferometer, passed one arm through a magnetic field region that rotates the neutron's spin, and recorded the count rate as the rotation angle was advanced. The result is the one the group theory demands: the interference pattern runs through its full cycle with a period of $4\pi$ in rotation angle, so that at $2\pi$ the fringes are inverted — the count rate at a given analyzer position has gone from maximum to minimum — and only at $4\pi$ have they returned.

That experiment is a genuine measurement, and it is a measurement of something specific: the period of a fringe pattern in units of **rotation angle**. The beam was turned through a physical angle, read off a mechanical or field-calibrated scale, and the pattern was counted. Nothing in the apparatus measured the ratio of a circumference to a diameter; the apparatus measured whether the fringes came back after one turn or after two. They came back after two. That is a fact about $\mathbb{Z}_2$.

The honest ledger must also record what such a measurement can and cannot bound. What it bounds is the *integer*: the pattern period is $4\pi$ and not $2\pi$ and not $6\pi$, a discrete alternative, and it has been settled since 1975. (The companion experiment of the same era, Colella, Overhauser and Werner, *Phys. Rev. Lett.* **35**, 1053 (1975), used the same interferometer technique to see the *gravitational* phase shift of a neutron — a different and equally real measurand, with $\hbar$ and $g$ in it but no circle constant at the first power in the fringe count.) What no interferometer of this kind bounds is the numerical value of the constant in the exponent, because the fringe period is an integer multiple of half-turns by construction. A golden constant would predict the same integer. The experiment is silent on the gap.

## Berry phase: the one place the constant survives at the first power

There is a second, closely related phase in the same physics, and it is where the circle constant genuinely does survive in a printed number. If the direction of the magnetic field is turned slowly around a closed circuit on the sphere, a spin prepared along the field returns to its original eigenstate with an extra phase — Berry's geometric phase (M. V. Berry, *Proc. R. Soc. A* **392**, 45 (1984)):

$$
\gamma \;=\; -\,m\,\Omega,
$$

where $m$ is the spin projection along the field ($m = \tfrac12$ for a spin-½) and $\Omega$ is the **solid angle** the field direction sweeps out on the unit sphere. For a cone of half-angle $\theta$,

$$
\Omega \;=\; 2\pi\left(1 - \cos\theta\right).
$$

Here $\pi$ is at the first power and there is no cancellation: the solid angle is a genuine area on a sphere of radius one, and its measure carries the constant once. One exact landmark is worth pausing on — at half-angle $\theta = 60°$, $\cos\theta = \tfrac12$ and

$$
\Omega \;=\; 2\pi\left(1 - \tfrac12\right) \;=\; \pi\ \text{steradians exactly.}
$$

A $60°$ cone encloses $\pi$ steradians. Not approximately: the identity is $\Omega(60°) = \pi$, a statement about the exact value of a transcendental number obtained from a rational half-angle, and the spin-½ Berry phase around that cone is $-\pi/2$.

| Cone half-angle $\theta$ | Solid angle $\Omega$ (sr) | Berry phase $\gamma = -\Omega/2$ (rad) |
|---|---|---|
| $30°$ | $0.841787214$ | $-0.420893607$ |
| $45°$ | $1.840302369$ | $-0.920151185$ |
| $60°$ | $\pi = 3.141592654$ | $-\pi/2 = -1.570796327$ |
| $90°$ (hemisphere) | $2\pi = 6.283185307$ | $-\pi = -3.141592654$ |
| $180°$ (full sphere) | $4\pi = 12.566370614$ | $-2\pi = -6.283185307$ |

These phases have been measured. In the neutron interferometer the spin-rotation experiment above is itself a Berry-phase measurement in disguise: turning the field through $360°$ encloses a solid angle and produces a phase that is read as a fringe shift, and the observed shifts follow $-\tfrac12\Omega$ to the accuracy of the fringe count. In optics the same geometry appears as the Pancharatnam phase, measured to high precision in polarization interferometers. So this is the second genuine measurand in the chapter — a phase, in radians, from an area on a sphere.

## Under Golden Pi

Set $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931\ldots$, with $\varphi = (1+\sqrt5)/2$. The exact identities used below, each checkable in a line of algebra:

```
π̂  = 4/√φ = 2√(2√5 − 2)                    = 3.1446055110296931
π̂² = 16/φ = 8(√5 − 1)                      = 9.8885438199983167
π̂⁴ + 16π̂² − 256 = 0                        (verified: 0.000e+00)
2π̂  = 8/√φ                                 = 6.2892110220593862
4π̂  = 16/√φ                                = 12.5784220441187724
```

So the sphere's total solid angle becomes the **algebraic** number $16/\sqrt\varphi$ steradians, of degree two over $\mathbb{Q}(\sqrt5)$, where $4\pi = 12.5663706143591725$ is transcendental by Lindemann's 1882 theorem. The same substitution runs through the table:

| Quantity | Conventional | Golden | Shift |
|---|---|---|---|
| Full turn in radians | $2\pi = 6.2831853072$ | $2\hat\pi = 6.2892110221$ | $+0.0959022309\%$ |
| Sphere's solid angle | $4\pi = 12.5663706144$ | $16/\sqrt\varphi = 12.5784220441$ | $+0.0959022309\%$ |
| $60°$ cone | $\pi$ sr | $\hat\pi = 4/\sqrt\varphi$ sr | $+0.0959022309\%$ |
| $45°$ Berry phase | $\pi\left(1-\tfrac{\sqrt2}{2}\right) = 0.9201511850$ | $\dfrac{2\left(2-\sqrt2\right)}{\sqrt\varphi} = 0.9210336300$ | $+0.0959022309\%$ |
| One steradian in square degrees | $\left(\dfrac{180}{\pi}\right)^{2} = 3282.8063500$ | $\left(\dfrac{180}{\hat\pi}\right)^{2} = 3276.5188272$ | $-0.1915288970\%$ |

Two structural facts about that table deserve emphasis, because they pull in opposite directions.

The **first power** is the clean case: every radian measure scales by exactly $\hat\pi/\pi$, the recurring $+0.0959022309\%$, with no further structure — because every one of these quantities is $\pi$ times a pure number fixed by geometry (a half, a $(1-\cos\theta)$, a turn count).

The **square degree** row is the one place in this chapter where the shift is amplified rather than passed through: the steradian is *defined* as an area over a squared radius, so converting it to the traditional degree-based unit squares the constant's reciprocal, and the shift doubles to $-0.1915288970\%$ — which is not $2 \times 0.0959022309\% = 0.1918044618\%$, but slightly less, because a percentage of a reciprocal is not a percentage of the quantity. The sphere still contains $41252.96$ square degrees under either label, but a golden reading puts the steradian at $3276.52$ square degrees instead of $3282.81$. That is a printed number that changes — and it is still not a measurement, only a relabelling of a unit that is defined, not found.

## The arithmetic of a golden turn

Here is where the double cover and the constant finally meet, and the meeting is informative. Suppose the golden value were the true one. Then the physical angle of one full turn would be $2\hat\pi$ radians, and $2\hat\pi$ rad, converted with the conventional degree, is

$$
\frac{2\hat\pi \cdot 180}{\pi} \;=\; 360.3452480312°. 
$$

A "full turn" of $2\hat\pi$ radians would therefore be $0.3452480310°$ **more** than a closed loop — it would overshoot. Put that overshoot into the rotation operator and the spinor does not come back to $-\mathbb{1}$:

$$
U(2\hat\pi,\mathbf{n}) = \cos\hat\pi\,\mathbb{1} - i\sin\hat\pi\,\mathbf{n}\cdot\boldsymbol{\sigma}
= -0.9999954613\,\mathbb{1} + i\,0.0030128574\,\mathbf{n}\cdot\boldsymbol{\sigma},
$$

and since $\hat\pi - \pi = 0.0030128574$ rad, this is exactly

$$
U(2\hat\pi,\mathbf{n}) \;=\; -\,\exp\!\left(-\,i\,(2\hat\pi - 2\pi)\,\mathbf{n}\cdot\boldsymbol{\sigma}\right)
\;=\; -\,\exp\!\left(-\,i\,0.0060257149\,\mathbf{n}\cdot\boldsymbol{\sigma}\right),
$$

a minus sign **plus** a residual rotation of $0.0060257149$ rad in $SU(2)$ — $0.3452480310°$ in $SO(3)$, the same overshoot, as it must be. The state would not be $-|\psi\rangle$; it would be $-|\psi\rangle$ rotated slightly. The predicted fringe inversion at one turn would be imperfect by that amount, and at two turns the pattern would not return to itself either but be offset by $0.6904960620°$.

There are only two consistent readings of this, and neither helps the golden case:

1. **Keep the rotation closed.** A full turn is $360°$ by definition of a turn, the sign flip is exact at $-1$, and the constant in the exponent is whatever constant makes the exponent reach $\pi$ at a closed loop — in which case the exponent's constant is *defined* by the geometry and carries no empirical content. The double cover is safe under any label; the label simply has to agree with the loop.
2. **Insist the label is golden.** Then $2\hat\pi$ rad is not a closed loop, the "one full turn" that produces $-1$ happens at $360.345°$ of actual rotation, and the physical statement of the spinor's periodicity changes with no change in the mathematics. The fringes would still return after two of whatever the apparatus does — the loop count is unchanged.

Reading 1 is the one physics uses, and it is why the double cover is the strongest example on this site of a $\pi$ that cannot be renegotiated by relabelling: **the sign is an integer, and the integer is fixed before the constant is ever consulted.** The $4\pi$ periodicity is a statement about $\mathbb{Z}_2$, not about $3.14159$.

## The honest ledger

This chapter has to be blunt about what is and is not at stake, because the subject invites overstatement in both directions.

- **Computed, exactly.** The matrices $\cos(\theta/2)\mathbb{1} - i\sin(\theta/2)\mathbf{n}\cdot\boldsymbol{\sigma}$; the values $-\mathbb{1}$ at $\theta = 2\pi$ and $+\mathbb{1}$ at $\theta = 4\pi$; $\det = +1$ throughout; $q = -1$ for a $2\pi$ quaternion; $\pi_1(SO(3)) = \mathbb{Z}_2$; $\Omega(60°) = \pi$ exactly; the golden algebraic forms $4\hat\pi = 16/\sqrt\varphi$ and $\gamma_{45°} = 2(2-\sqrt2)/\sqrt\varphi$. All verified in the arithmetic above, none of them a measurement.
- **Genuinely measured.** Two things, and only two. First, the *period* of the neutron interference pattern in rotation angle, which is $4\pi$ and was observed to be so in 1975 — a measurement of an integer, and therefore blind to the constant's value. Second, the *magnitude* of a geometric phase, $\gamma = -\tfrac12\Omega$, read as a fringe shift against the fringe period; this is a radian measurement, it carries the constant at the first power, and its published precision is set by fringe counting and beam contrast, not by any circle constant.
- **What the ledger says about the gap.** The golden shift here is $+0.0959022309\%$ on every first-power radian quantity. Berry-phase experiments quote agreement with the conventional formula at the level of a fraction of a fringe and a few percent of the predicted phase, with contrast loss and beam divergence dominating the budget. The golden shift is smaller than those uncertainties, so **no existing measurement of a geometric phase decides the question** — and the $4\pi$ topology cannot decide it in principle, because it never consults the number. The honest position is a limitation, not a verdict.
- **What the geometry does say.** The double cover, the belt trick, the sign of the fermion, the integer $4\pi$ — these are exact structures that any consistent system of angular measure must reproduce, and the golden value reproduces them by construction, because "$\hat\pi$" is defined as the angle of a half-turn in a system where a turn still closes. The convention is not evidence for a value; it is bookkeeping around a loop that closes.

The temptation in a chapter like this is to score a point for one constant against the other. There is no point available. What there is, is a clean illustration of the site's standing rule, in its sharpest form yet: a constant can sit visibly in the exponent of the operator that produces a minus sign and still be entirely absent from the minus sign. The number names the angle; the topology supplies the sign; and only the second one is physics. Computed, never measured.

## Further Reading

- [The Casimir Effect: How the Vacuum Between Two Plates Computes the Circle Constant as π²/240, Then Hands One Power Back to ħ = h/2π](/blog/posts/2026-10-16-casimir-effect-vacuum-pressure-computes-circle-constant-golden-pi/) — yesterday's chapter, where a power of the constant cancels against the defined action quantum rather than against topology.
- [The Bohr–Sommerfeld Action Integral: How Phase-Space Area Carries the Circle Constant as a Half-Turn, Then Cancels It Between Coulomb's 4π and ħ's 2π](/blog/posts/2026-10-15-bohr-sommerfeld-action-integral-quantisation-computes-circle-constant-golden-pi/) — the other half-turn story, and the same $2\pi$ bookkeeping that the spinor doubles.
- [The Quantum Harmonic Oscillator: How π^(1/4) Reaches the Ground State, Then Cancels from Every Energy Level](/blog/posts/2026-10-07-quantum-harmonic-oscillator-ground-state-cancels-circle-constant-golden-pi/) — the fractional-power counterpart: where the constant enters a quantum amplitude as a fourth root.
- [Euler's Identity: How e^{iπ} = −1 Closes the Complex Plane, and What Golden Pi Changes](/blog/posts/2026-09-19-euler-identity-computes-circle-constant-golden-pi/) — the $-1$ in this chapter's exponent, seen as the closing of a half-period of the exponential.
- [The Wigner Semicircle Law: How the Circle Constant Normalises a Random Matrix's Spectrum, Then Cancels from Every Moment](/blog/posts/2026-10-14-wigner-semicircle-law-random-matrices-computes-circle-constant-golden-pi/) — another case where the constant appears once as normalisation and leaves every exact integer moment untouched.
