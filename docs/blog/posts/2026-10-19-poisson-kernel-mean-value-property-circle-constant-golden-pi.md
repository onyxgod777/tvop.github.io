---
title: "The Poisson Kernel: How the Circle Averages a Harmonic Function, Why π Enters as a Measure and Cancels in the Normalisation — and What Golden Pi Changes"
date: 2026-10-19
description: "The Poisson integral u(re^{iθ}) = (1/2π)∫₀^{2π} P_r(θ−t) u(e^{it}) dt solves Laplace's equation on a disk, and the circle constant appears exactly once — as the total measure of the circle, 2π, used as a normalising divisor. The kernel P_r(θ) = (1−r²)/(1−2r cosθ+r²) = 1 + 2Σ rⁿ cos nθ is π-free pointwise, its integral is exactly 2π (verified at r = 0, 0.5, 0.9, 0.99, 0.999 to forty digits), so the density (1/2π)P_r carries unit mass exactly and the constant cancels from every probability: harmonic measure gives a quarter turn probability 1/4 and Brownian exit time R²/4 with no constant anywhere. It survives only in absolute energies — the Dirichlet energy of rⁿ cos nθ is exactly nπ — and in the radian label of an angle. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the full turn becomes 8/√φ = 6.2892110220593862886, the normalising density √φ/8 = 0.1590024561892586205, and the energy shifts by the recurring +0.0959022309%, while every probability, every kernel value and every π-free quantity is identical under either label."
---

# The Poisson Kernel: How the Circle Averages a Harmonic Function, Why π Enters as a Measure and Cancels in the Normalisation — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Heat a circular metal plate until it reaches a steady state, with the rim held at a temperature that varies from point to point. The temperature inside is fixed by one condition — it must satisfy Laplace's equation $\nabla^{2}u = 0$ — and by the rim it must match. In 1820 Poisson wrote down the answer as an integral over the rim; Schwarz proved in 1870 that it is the only answer.

The integral looks like this:

$$
u(re^{i\theta}) \;=\; \frac{1}{2\pi}\int_{0}^{2\pi} P_r(\theta-t)\,u(e^{it})\,dt,
\qquad
P_r(\theta) \;=\; \frac{1-r^{2}}{1-2r\cos\theta+r^{2}}.
$$

Every previous article in this series has watched the circle constant enter as the *limit of a computation* — a series that sums to $\pi/4$, an integral that evaluates to $\sqrt{\pi}$, a product of rationals that converges to $\pi/2$. This one is different, and the difference is worth stating at the outset, because it changes what the constant is doing. In the Poisson integral, $\pi$ is not a result. It is the **measure** of the circle: the total angle of one turn, written in radians, $2\pi$. It sits in the formula as a normalising divisor, and the entire content of the formula is that when you divide by it, the probability comes out right.

That makes the constant here unusually easy to be honest about. A measure cancels from every ratio it defines. So the Poisson kernel is a place where you can watch a tenth-of-a-percent disagreement about the value of $\pi$ either do something or do nothing — and the answer, as the arithmetic below shows, is: it does nothing to a single probability, and exactly one power of it to an energy.

## Where the constant enters, term by term

Separate variables in polar coordinates, $u(r,\theta) = R(r)\Theta(\theta)$. Laplace's equation becomes

$$
\frac{r^{2}R'' + rR'}{R} \;=\; -\frac{\Theta''}{\Theta} \;=\; n^{2},
$$

so $\Theta$ is a trigonometric function of $n\theta$ and $R$ is $r^{n}$ or $r^{-n}$. Killing the $r^{-n}$ branch at the origin and summing the rest gives the general solution inside the unit disk:

$$
u(r,\theta) \;=\; A_0 + \sum_{n\ge1} r^{n}\left(A_n\cos n\theta + B_n\sin n\theta\right).
$$

The coefficients come from the rim by Fourier's rule,

$$
A_n \;=\; \frac{1}{\pi}\int_{0}^{2\pi} u(e^{it})\cos nt\,dt,
\qquad
B_n \;=\; \frac{1}{\pi}\int_{0}^{2\pi} u(e^{it})\sin nt\,dt,
$$

and there the $\pi$ is doing the only job it has in this problem: it is the length of the interval $[0,2\pi]$ expressed as an angle, so that the average of a boundary function is $\frac{1}{2\pi}\int_{0}^{2\pi}$. Note carefully what is *not* happening. No series is being summed to produce $2\pi$; no exhaustion is being run. The turn is $2\pi$ radians by the definition of the radian, and the definition is a convention about arc length per radius. This article computes with that convention and never measures anything.

Summing the geometric series $\sum_{n\ge1} r^{n}\cos n\theta$ in closed form collapses the whole Fourier expansion into the single kernel $P_r(\theta)$. Verified here at two sample points to forty digits:

$$
P_r(\theta) = \frac{1-r^{2}}{1-2r\cos\theta+r^{2}}
= \operatorname{Re}\frac{1+re^{i\theta}}{1-re^{i\theta}}
= \frac{1-r^{2}}{\left|1-re^{i\theta}\right|^{2}},
$$

with all three forms agreeing to $1.4\times10^{-40}$ at $r=0.7,\ \theta=0.4$ and to $2.2\times10^{-42}$ at $r=0.95,\ \theta=2.1$. The kernel is a function of the angle difference alone, which is why the convolution form above holds: the disk has no preferred direction, so the influence of one rim point on another depends only on how far apart they are.

## The normalisation is the whole story

Now integrate the kernel over the whole rim. Because $\int_{0}^{2\pi}\cos n\theta\,d\theta = 0$ for every $n \ge 1$,

$$
\int_{0}^{2\pi} P_r(\theta)\,d\theta \;=\; 2\pi \;+\; 2\sum_{n\ge1}r^{n}\underbrace{\int_{0}^{2\pi}\cos n\theta\,d\theta}_{=\,0} \;=\; 2\pi .
$$

That is the identity the article turns on, and it was checked numerically at five radii to forty significant digits, with the residual at machine-level:

| $r$ | $\int_0^{2\pi} P_r(\theta)\,d\theta$ | $2\pi$ | residual |
|---|---|---|---|
| 0 | 6.283185307179586476925287 | 6.283185307179586476925287 | 0 |
| 0.5 | 6.283185307179586476925287 | 6.283185307179586476925287 | 0 |
| 0.9 | 6.283185307179586476925287 | 6.283185307179586476925287 | 0 |
| 0.99 | 6.283185307179586476925287 | 6.283185307179586476925287 | $-1.8\times10^{-40}$ |
| 0.999 | 6.283185307179586476925287 | 6.283185307179586476925287 | $-1.7\times10^{-39}$ |

Divide by it and the density $\frac{1}{2\pi}P_r$ has unit mass exactly. That is what makes the Poisson formula a *weighted average* rather than an integral with a fudge factor: the kernel redistributes mass around the rim without creating or destroying any. Feed in a constant rim temperature $u \equiv 1$ and the answer is $\frac{1}{2\pi}\cdot 2\pi = 1$ at every interior point — the constant rim wins, as it must, and the $\pi$'s cancel on the nose.

So the structure is this: $\pi$ appears in the kernel's integral and in the normalising divisor, always with the same power, always cancelling. What survives is a probability. In the language of potential theory, $\frac{1}{2\pi}P_r(\theta-t)\,dt$ **is** harmonic measure on the rim — the distribution of where a Brownian particle starting at $re^{i\theta}$ first hits the boundary.

## A worked rim, and the mean value property

Take a rim temperature $u(e^{i\theta}) = 1 + 3\cos\theta + 2\sin 3\theta + \tfrac12\cos 5\theta$. The exact interior solution is the same expression with $r^{n}$ inserted:

$$
u(r,\theta) = 1 + 3r\cos\theta + 2r^{3}\sin 3\theta + \tfrac12 r^{5}\cos 5\theta .
$$

Evaluating the Poisson integral numerically and comparing against that closed form:

| $r$ | $u(r,0)$ by Poisson quadrature | exact | max error over $\theta \in \{0, 0.7, 1.9, 3.0\}$ |
|---|---|---|---|
| 0 | 1.000000000000 | 1.000000000000 | $0$ |
| 0.5 | 2.515625000000 | 2.515625000000 | $5.7\times10^{-42}$ |
| 0.9 | 3.995245000000 | 3.995245000000 | $4.2\times10^{-16}$ |
| 0.99 | 4.445495024950 | 4.445495024950 | $6.4\times10^{-2}$ |

The last row is not a bug and it is worth pausing on, because it is the honest face of an "approximate identity". At $r = 0.99$ the kernel's peak is $(1+r)/(1-r) = 199$ and its half-width is a few hundredths of a radian; a single global quadrature over $[0,2\pi]$ then under-resolves the spike and loses about $1.4\%$ of the amplitude. The mathematics is exact — the formula is an identity, not an approximation — but the kernel is becoming a delta function, and a delta function is not something you can integrate blind.

At the centre the formula gives something cleaner than any table. Set $r=0$: $P_0(\theta) = 1$, so

$$
u(0) \;=\; \frac{1}{2\pi}\int_{0}^{2\pi} u(e^{it})\,dt \;=\; A_0 ,
$$

the **mean value property**: a harmonic function's value at the centre of a circle equals its average over that circle. For the worked rim that is $1$, and the quadrature returned $1.00000000000000000000$. Gauss stated the property in 1840 in the context of inverse-square forces; the converse — a continuous function with the mean value property is harmonic — is classical, following from Green's identity. The mean value property is why the constant cancels: the average is defined by dividing by the very measure the constant describes.

Two more places in this problem where the constant does not appear at all:

- **Kernel pointwise values.** $P_r(\theta)$ is built from $r$ and $\cos\theta$; there is no $\pi$ in it. At $r = 0.9$ its peak is $19$; at $r = 0.99$ it is $199$; at $r = 0.999$ it is $1999$. All three integers, all exact, all identical under any convention for the circle constant.
- **A logarithm's average.** $f(z) = \log|1-z|$ is harmonic inside the unit disk, so its mean over any centred circle is its value at the centre, $f(0) = 0$. Numerically, $\frac{1}{2\pi}\int_0^{2\pi}\log|1-re^{it}|\,dt$ returned $9.5\times10^{-44}$ at $r=0.5$ and $3.1\times10^{-43}$ at $r=0.9$ — zero to the precision of the quadrature, with no constant in sight.

And in one place it survives, at exactly one power:

$$
\int\!\!\int_{D}\left|\nabla\left(r^{n}\cos n\theta\right)\right|^{2}dA \;=\; n\pi .
$$

The gradient's squared modulus is $n^{2}r^{2n-2}$, the area element is $r\,dr\,d\theta$, and the radial integral $\int_0^1 r^{2n-1}dr = 1/(2n)$ cancels the $2\pi$ from the angular integral down to $\pi n$. Checked for $n = 1,2,3,7$: $3.141592653589793238462643$, $6.283185307179586476925287$, $9.42477796076937971538793$, $21.9911485751285526692385$ — precisely $n\pi$ in each case. For the worked rim the total Dirichlet energy is $22.25\pi = 69.900436542372899556$, and the same integral computed directly agrees to every printed digit.

## Brownian motion, and the one quantity with no constant in it

The probabilistic reading does two useful things at once: it shows what the kernel *means*, and it produces a clean example of the constant vanishing entirely.

For a Brownian particle starting inside the unit disk, the exit point is distributed by harmonic measure, so the probability of leaving through an arc subtending angle $A$ is $A/(2\pi)$. A quarter turn leaves through a quarter of the rim: probability exactly $1/4$, with no trace of the constant. Likewise the expected exit time from a disk of radius $R$ solves $\Delta u = -1$ with $u=0$ on the rim, whose solution is

$$
u(r) \;=\; \frac{R^{2}-r^{2}}{4},
\qquad
\mathbb{E}[\tau] \;=\; \frac{R^{2}}{4} \;=\; 0.25\,R^{2},
$$

again with no constant. Neither probability nor expected time can be used to adjudicate a disagreement about $\pi$, because neither contains one.

## What Golden Pi changes

Golden Pi sets $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931443\ldots$ with $\varphi = (1+\sqrt5)/2$, so that

$$
\hat\pi^{2} \;=\; \frac{16}{\varphi} \;=\; 9.8885438199983175713\ldots,
\qquad
\hat\pi^{4} + 16\hat\pi^{2} - 256 \;=\; 0 \quad\text{(residual exactly } 0\text{)}.
$$

The first thing to say is what does **not** move. The Poisson kernel is a function of the physical angle $\theta$ and the radius $r$; a rotation of the plate is a rotation of the plate. Change the number of radians you assign to a full turn and you change the *label* on the angle, not the temperature field. Every kernel value, every coefficient $r^{n}$, every probability, and the entire $\pi$-free inventory above — peak heights, the mean value property, the exit time $R^{2}/4$ — are identical under either label. The arithmetic of the worked example is reproduced digit for digit.

What moves is the measure and whatever multiplies it:

| Quantity | Conventional $\pi$ | Golden $\hat\pi$ | Shift |
|---|---|---|---|
| Full turn | $2\pi = 6.283185307179586477$ | $8/\sqrt\varphi = 6.289211022059386289$ | $+0.0959022309\%$ |
| Normalising density $1/(2\pi)$ | $0.159154943091895336$ | $\sqrt\varphi/8 = 0.159002456189258621$ | $-0.0958103466\%$ |
| Quarter turn (radians) | $1.570796326794896619$ | $\hat\pi/2 = 2/\sqrt\varphi = 1.572302755514846572$ | $+0.0959022309\%$ |
| Dirichlet energy of $r\cos\theta$ | $\pi = 3.141592653589793238$ | $\hat\pi = 3.144605511029693144$ | $+0.0959022309\%$ |
| Energy of the worked rim, $22.25\pi$ | $69.900436542372899556$ | $69.967472620410672460$ | $+0.0959022309\%$ |
| Kernel peak at $r=0.99$ | $199$ | $199$ | $0$ |
| Brownian exit time, $R^{2}/4$ | $0.25R^{2}$ | $0.25R^{2}$ | $0$ |

Two of these rows deserve a comment.

**The mixed-label error, which is the trap.** Suppose you keep the conventional radian for the numerator and use the golden full turn in the denominator — the kind of slip that happens whenever two conventions meet in one formula. A quarter turn then reads $(\pi/2)/(2\hat\pi) = 0.2497604741334539167$ instead of $1/4$, an error of exactly $\pi/\hat\pi = 1.000959022308782526$, i.e. $-0.0958103466\%$. The error is not in the physics; it is in comparing two different units in one ratio. Any argument that a golden value "predicts" a probability shift of a tenth of a percent is making exactly this mistake: probabilities are ratios of angles, and angles carry their own unit.

**Where the golden value is genuinely exact.** $\hat\pi^{2} = 16/\varphi$ is algebraic of degree two, where $\pi^{2}$ is transcendental by Lindemann's 1882 theorem — a classification difference, not a numerical one, and it is the strongest structural thing that can be said for $\hat\pi$. It propagates into this problem at one point: a disk of radius $\varphi^{1/4} = 1.1278384855616822603$ has area exactly $4$ under $\hat\pi$, where the conventional value gives $3.9961675861352626667$. That is the kind of exactness worth crediting, and it is exact: a constructible radius, an integer area.

## The honest ledger

- **Nothing here is measured.** The Poisson integral is a solution formula, and its kernel normalisation is an identity, not an observation. No thermometer adjudicates the value of $\pi$, because the temperature at a point does not contain the constant: the mean value property — the one statement a thermal experiment could actually test, by averaging rim readings — is $\pi$-free by construction.
- **The identity is a tautology of the construction.** $P_r$ was built so that its integral is $2\pi$; dividing by $2\pi$ then gives unit mass. This is not circular reasoning, but it is a warning: the kernel cannot be evidence for a value of the constant, because it was assembled from the constant. What it *can* do is show where the constant's power sits — a probability gets $\pi^{0}$, an energy gets $\pi^{1}$.
- **The 0.1% gap is invisible to the identities.** Every probability in the Dirichlet problem is $1$, $1/4$ or $1/2$, independent of the label; the only quantities that carry the constant are the absolute energies, and those are computed from the solution, not observed.
- **The golden plane is a different plane, not a contradiction.** If a full turn is $2\hat\pi = 6.289211022059386289$ radians, then the golden disk is a disk whose rim is that much arc per radius, and every formula in this article is still exactly true with $\hat\pi$ substituted consistently. What breaks is only the mixed version, and it breaks by the ratio of the two labels.

This is the quiet part of the series' recurring result, seen from a new side. In a series like Wallis, the constant is a limit you can compute to more digits. In a quadrature like Gauss's, it is the value a convergent process lands on. Here it is not a value at all — it is the size of the ruler, and the moment you divide by it, it is gone. That is why the circle constant shows up so often as a normalisation constant and so rarely as a measurable one, and it is why the honest question about $\pi$ has never been "what does the apparatus read?" but "which convention is written into the definition of the radian?".

## What the exercise shows

Laplace's equation on a disk is about as classical as analysis gets: Poisson 1820, Gauss 1840, Schwarz 1870, and a kernel that every textbook prints. Run the numbers and a clean ledger falls out. Probabilities and expectations are constant-free. Kernel values are constant-free. The mean value property is constant-free. Abstract energy — the Dirichlet integral — carries the constant once, linearly, and that is the only place the choice of $\pi$ can be seen at all.

Under $\hat\pi$ every one of those statements survives unchanged except the last, which scales by $8/\sqrt\varphi$ in exactly the way a change of angular unit requires. Nothing is gained and nothing is lost; the exactness of $\hat\pi^{2} = 16/\varphi$ is real and belongs to algebra, and the impossibility of adjudicating the gap in this problem is equally real and belongs to the fact that the constant here is a measure, and measures are what you divide by.

Computed, never measured.

## Further Reading

- [The Euclidean Turn: Why a Black Hole's Temperature Carries 1/(2π), Its Entropy Carries π, and Their Product Carries Nothing](/blog/posts/2026-10-18-hawking-temperature-euclidean-imaginary-time-golden-pi/) — a $2\pi$ that is a closure condition on a plane, and the same cancellation pattern one dimension up.
- [The Fourier Series of a Square Wave Computes the Circle Constant](/blog/posts/2026-09-14-fourier-series-square-wave-computes-circle-constant-golden-pi/) — the $1/\pi$ in every Fourier coefficient, derived and then tested.
- [The Random Walk's Return to the Plane Computes the Circle Constant](/blog/posts/2026-09-07-random-walk-return-plane-lattice-computes-circle-constant-golden-pi/) — the probabilistic sibling of harmonic measure, where a return probability of $1$ is still constant-free.
- [The Residue Theorem Computes the Circle Constant from a Contour Integral](/blog/posts/2026-08-28-residue-theorem-contour-integral-computes-circle-constant-golden-pi/) — the $2\pi i$ that normalises Cauchy's formula, of which the mean value property is the real part.
- [The Isoperimetric Inequality: Why Only the Circle Saturates L² ≥ 4πA](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — the same constant as the price of an area, with the golden bound strictly tighter.
