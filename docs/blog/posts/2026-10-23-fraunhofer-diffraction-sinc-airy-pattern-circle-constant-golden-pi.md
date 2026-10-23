---
title: "Fraunhofer Diffraction: Why a Slit Writes sinc(πa sinθ/λ), Why the Famous 1.22 Is Really 3.8317/π — and What Golden Pi Changes"
date: 2026-10-23
description: "A laser through a slit produces a pattern whose minima sit at a sinθ = mλ — an exact integer condition with no circle constant anywhere in it, while the π in sinc(πa sinθ/λ) is the bookkeeping of the Fourier convention and the textbook 1.22 of the Airy disk is exactly 3.8317/π. Working the numbers for 632.8 nm light through 20 µm to 1 mm slits, the Airy zeros, the −13.26 dB sidelobe and the 83.78% encircled energy, then re-labeling every radian under Golden Pi (4/√φ = 3.144605511…), where 4/π̂ collapses to exactly √φ: the geometry does not move a digit and the diffraction pattern turns out to be structurally blind to the value of the constant."
---

# Fraunhofer Diffraction: Why a Slit Writes sinc(πa sinθ/λ), Why the Famous 1.22 Is Really 3.8317/π — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Shine a helium–neon laser at 632.8 nm through a slit 100 µm wide and put a screen a metre behind it. What lands on the screen is a bright central bar with dimmer bars either side, and if you mark where the darkness falls and measure with a ruler you get positions like 6.33 mm, 12.66 mm, 18.99 mm from the centre. Those are lengths. Real ones, read off real hardware, with all the usual experimental mess attached.

And the formula that predicts them is

$$a\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \pm3, \ldots$$

where $a$ is the slit width and $\lambda$ the wavelength. Look at that expression closely, because it is the whole argument of this article in one line: **there is no circle constant in it.** Not $\pi$, not $\hat\pi$, not anything. The minima of a single-slit diffraction pattern are fixed by an integer and a ratio of two lengths. Whatever you decide to call a half-turn is completely irrelevant to where the darkness goes.

So why does every textbook write the pattern as $\operatorname{sinc}(\pi a\sin\theta/\lambda)$, with a $\pi$ sitting right there in the argument? That is the question worth answering honestly, and the answer separates two things that get muddled constantly: a constant that is **computed** as a quadrature value, and a constant that is merely **written down** as a unit label.

## The integral that produces the pattern

Fraunhofer diffraction is the squared modulus of the aperture's Fourier transform. For a slit of width $a$ centred at the origin, the field at angle $\theta$ is the phase sum across the opening:

$$E(\theta) \propto \int_{-a/2}^{a/2} e^{-i k x \sin\theta}\,dx = a\,\frac{\sin\!\left(\tfrac{ka}{2}\sin\theta\right)}{\tfrac{ka}{2}\sin\theta}, \qquad k = \frac{2\pi}{\lambda}.$$

The integral evaluates to $a\,\operatorname{sinc}(u)$ with $u = \tfrac{ka}{2}\sin\theta = \pi a\sin\theta/\lambda$. Every $\pi$ in the final expression entered through $k = 2\pi/\lambda$, and that definition is a **convention**: $2\pi$ radians per cycle is how we chose to count angle. Write the same physics in spatial frequency $f = \sin\theta/\lambda$ and the transform reads

$$E(f) \propto a\,\operatorname{sinc}(\pi a f),$$

while the unitary angular-frequency convention absorbs the constant into the prefactor instead:

$$\tilde E(\omega) = \frac{1}{\sqrt{2\pi}}\int E(x)e^{-i\omega x}dx .$$

Move the constant around as much as you like — exponent, prefactor, or argument — the intensity is the same function of the same measured angle:

$$I(\theta) = I_0\left[\frac{\sin(\pi a\sin\theta/\lambda)}{\pi a\sin\theta/\lambda}\right]^{2}.$$

The zeros are where the sine vanishes but the denominator does not: $\pi a\sin\theta/\lambda = m\pi$ for integer $m \ne 0$. The $\pi$ on the left cancels the $\pi$ on the right, exactly, and out falls $a\sin\theta = m\lambda$. This is not a coincidence and it is not an approximation. The circle constant appears in the argument of the sinc and cancels against itself at every zero, which is why the observable — the position of the darkness — is completely free of it.

## The zeros the integers dictate

Here is the numbers for the same laser, $\lambda = 632.8$ nm, worked at forty digits and then rounded:

| Slit width $a$ | $\sin\theta_1 = \lambda/a$ | $\theta_1$ (rad) | $\theta_1$ (deg) | $y_1$ at 1 m |
|---|---|---|---|---|
| 20 µm | 0.0316400 | 0.0316452815 | 1.8131411° | 31.656 mm |
| 50 µm | 0.0126560 | 0.0126563379 | 0.7251547° | 12.657 mm |
| 100 µm | 0.0063280 | 0.0063280422 | 0.3625701° | 6.3281 mm |
| 500 µm | 0.0012656 | 0.0012656003 | 0.0725136° | 1.2656 mm |
| 1 mm | 0.0006328 | 0.0006328000 | 0.0362568° | 0.6328 mm |

None of those entries required a value of $\pi$ to compute. The radian column is just the arcsine in radians; the degree column is the same angle in the other unit; the millimetre column is $\tan\theta$ times the screen distance. A student with a ruler and a slit of known width is measuring the ratio $\lambda/a$, and that ratio is what the pattern reports.

The higher orders follow the same integer ladder, and the intensity between them is set by the sinc² envelope, again π-free in its structure:

| Feature | Exact location | Value |
|---|---|---|
| First zero | $u = \pi$ | $I = 0$ exactly |
| First sidelobe | $u = 4.49340945790906$, root of $\tan u = u$ | $0.04719044923$, i.e. $-13.2614589$ dB |
| Second zero | $u = 2\pi$ | $I = 0$ exactly |
| Half-maximum points | $u = \pm1.39155737825$ | FWHM $= 2.7831147565$ in $u$, $= 0.8858929\pi$ |

The sidelobe height is the squared value $\left(\sin u/u\right)^2$ at the root of $\tan u = u$ — a transcendental root, a pure number, and one that no redefinition of the radian can touch, because it is the solution of an equation written entirely in integers and algebra.

## The 1.22 that is really 3.8317/π

Now the circular aperture, which is where the famous number lives. A round hole of diameter $D$ gives the Airy pattern

$$I(\theta) = I_0\left[\frac{2J_1(x)}{x}\right]^{2}, \qquad x = \frac{\pi D\sin\theta}{\lambda},$$

and the first dark ring is at the first zero of the Bessel function $J_1$:

$$j_{1,1} = 3.8317059702075123156\ldots$$

so the first minimum sits at

$$\sin\theta = \frac{j_{1,1}}{\pi}\cdot\frac{\lambda}{D} = 1.21966989126650445\,\frac{\lambda}{D}.$$

Every optics text prints **1.22**. That printed 1.22 is $1.2196698913$ rounded up — an error of $+270.65$ parts per million — and, more to the point, it is nothing but the Bessel zero divided by a half-turn. The number is a ratio between two unrelated things: a root of a transcendental equation, and the definition of the radian. Under Golden Pi ($\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$) the same root gives

$$\frac{j_{1,1}}{\hat\pi} = 1.21850132131608135,$$

a shift of $-0.0958103466\%$, the reciprocal gap $\pi/\hat\pi - 1$. The physical angular radius of the Airy disk does not change by any amount, because the angle is a direction in space; only the printed coefficient moves, and it moves because the denominator moved.

That is the honest status of 1.22: **it is not a measurement of anything.** It is $3.8317$ over a bookkeeping constant. A textbook could print 1.2185 with equal validity if it defined the radian with the golden constant, and a lens would focus identically.

## What Golden Pi changes

Write the golden constant in its exact forms:

$$\hat\pi = \frac{4}{\sqrt\varphi} = 3.1446055110296931443\ldots, \qquad \hat\pi^{2} = \frac{16}{\varphi} = 9.8885438199983175713\ldots$$

with $\varphi = (1+\sqrt5)/2$. The gap to the conventional constant is

$$\frac{\hat\pi}{\pi} - 1 = +0.0959022308782526\%,$$

about one part in 1043 — far coarser than the precision of the optical measurements discussed below, and still invisible in the pattern itself, for the reason already given: the pattern is a function of integers and length ratios.

| Quantity | Conventional | Golden | Movement |
|---|---|---|---|
| First zero of slit pattern | $a\sin\theta = \lambda$ | $a\sin\theta = \lambda$ | none — π-free |
| Airy coefficient $j_{1,1}/\pi$ | 1.2196698913 | 1.2185013213 | $-0.0958\%$ (label) |
| Half turn in radians | 3.141592653589793 | 3.144605511029693 | $+0.0959\%$ (label) |
| Quarter turn | $\pi/4 = 0.785398163397448$ | $\hat\pi/4 = 1/\sqrt\varphi = 0.786151377757423$ | exact algebraic under GP |
| Square / inscribed-circle area ratio | $4/\pi = 1.2732395447$ | $4/\hat\pi = \sqrt\varphi = 1.2720196495$ | exact algebraic under GP |
| Sidelobe | $-13.2614589$ dB | $-13.2614589$ dB | none |
| Encircled energy, first dark ring | $83.7784869\%$ | $83.7784869\%$ | none |

Two rows deserve emphasis because they are the ones the golden reading can state *exactly*, in closed form, with no decimal:

- $\hat\pi/4 = 1/\sqrt\varphi$ precisely, because $\hat\pi = 4/\sqrt\varphi$ by definition. The quarter turn is a reciprocal square root of the golden ratio.
- $4/\hat\pi = \sqrt\varphi$ precisely. The ratio of a square's area to the area of its inscribed circle — conventionally $4/\pi = 1.2732395447$, transcendental by Lindemann's 1882 theorem — becomes, under the golden constant, the algebraic number $\sqrt\varphi = 1.2720196495140689643$, a root of $x^{4} - x^{2} - 1 = 0$.

That second row is a real structural difference and it should be stated plainly: $4/\pi$ is transcendental, $4/\hat\pi$ is not. Any expression in which the circle constant enters to the first power inherits that difference. It is the same class of observation the site has made elsewhere — a constant that is algebraic where the conventional one is transcendental — and it is a statement about the *form* of the answer, not about a measured length.

What does the label change do to an actual observed angle? Take a 200 mm aperture at 550 nm, where the Rayleigh angle is $\sin\theta = 1.22\lambda/D$:

| Reading | Rayleigh angle (rad) | (arcsec) |
|---|---|---|
| Conventional, $j_{1,1}/\pi$ | $3.3550000\times10^{-6}$ | 0.692018 |
| Golden, $j_{1,1}/\hat\pi$ | $3.3508786\times10^{-6}$ | 0.691168 |

A difference of $0.00085$ arcsec — below the diffraction-limited resolution of the telescope that would be doing the measuring, and, more importantly, a difference between two *definitions*, not between two predictions about where light goes. The light goes to the same place; the number in the footnote changes.

## Where π is genuinely computed in this problem

There is one place where the circle constant is not merely written but *obtained*: the normalisation of the transform. The Fourier inversion relies on

$$\int_0^{\infty}\frac{\sin x}{x}\,dx = \frac{\pi}{2} = 1.5707963267948966192\ldots$$

and this is a computed limit — the value of a quadrature over the zeros of the sine, converging with the slow $1/X$ envelope familiar from every Gibbs-phenomenon plot. Truncating the integral at $X$:

| $X$ | $\int_0^{X}\frac{\sin x}{x}dx$ |
|---|---|
| 100 | 1.56222546689 |
| 1 000 | 1.57023312197 |
| 10 000 | 1.57089154539 |

Likewise, by Parseval's theorem, $\int_{-\infty}^{\infty}\operatorname{sinc}^{2}x\,dx = \pi$ exactly — the same constant emerging from the energy of the pattern rather than its amplitude. These are computations: a limit of sums, evaluated, never measured. The $\pi$ in $1/\sqrt{2\pi}$ and $1/2\pi$ is exactly this quadrature value, sitting where it does because we chose cycles-per-length as the unit of frequency.

Under the golden constant the same quadrature reads $2/\sqrt\varphi = 1.5723027555\ldots$ — but here honesty requires a distinction the site has drawn before: a quadrature is defined by the integers (the zeros of the sine), so a re-labelled constant is a choice of unit, not an observation of nature. Nothing in a screen's brightness pattern observes a constant. The pattern observes ratios.

## Why no photograph settles it

Collect the measured quantities from an actual diffraction experiment: irradiance as a function of position on a screen, the screen distance, the slit width from a micrometer, the wavelength from a calibrated laser. Every one of them enters the prediction as a **ratio** — $y/L$, $\lambda/a$, $D/\lambda$. The circle constant enters only through the normalisation, and the normalisation cancels in every ratio. The experiment is therefore structurally blind: it can distinguish $a\sin\theta = \lambda$ from $a\sin\theta = 2\lambda$, badly and with effort, and it cannot distinguish $\pi$ from $\hat\pi$ at all, because neither appears in the observable.

This is the same lesson the polyhedron's angle defect taught, in a different medium: when the physics is an integer count or a length ratio, the constant's value is not in the answer. It is worth noting where the usual failure mode lies. In the Buffon-needle problem the gap is masked by calibration error — a needle length known to 0.1% swamps the 0.0959% difference. Here calibration is not even the obstacle: an HeNe wavelength known to 0.001 nm is $1.58\times10^{-6}$ in relative terms, some six hundred times finer than the gap, so the precision is more than adequate. The obstacle is that the formula has no slot for the constant to sit in. Precision cannot recover a quantity that was never in the equation.

What would speak, then? A genuine physical measurand in which the constant enters at the first power and does not cancel — the fine-structure constant is the standing candidate, since $\alpha$ is measured rather than computed, and its CODATA uncertainty is far below the golden gap. Even there the question is one of interpretation of a measured dimensionless number, not of a geometric construction. That is the honest boundary of this whole line of enquiry, and it is better drawn sharply than blurred.

A closing note on the history, kept accurate: Fresnel's 1818 memoir on diffraction was examined by a commission including Poisson, who argued that the wave theory predicted a bright spot in the centre of the shadow of a circular obstacle — an apparently absurd consequence. Arago had the experiment performed and the spot was there. That episode is a genuine triumph of prediction over intuition, and it is a triumph about *where light goes*, about the wave picture of Huygens and Fresnel. It says nothing whatsoever about the numerical value of the circle constant, and it should not be conscripted into that argument. The pattern is exact, integer-indexed, and silent on the constant.

## Honest ledger

- **Computed, not measured:** $\int_0^\infty \sin x/x\,dx = \pi/2$, $\int \operatorname{sinc}^2 = \pi$, the Bessel zero $j_{1,1} = 3.8317059702$, the sidelobe root $\tan u = u$ at $4.4934094579$.
- **Measured, and π-free:** the positions of the minima, $a\sin\theta = m\lambda$; the Airy ring radii in angle; the 83.7784869% encircled energy inside the first dark ring, which is $1 - J_0(j_{1,1})^{2}$ and contains no constant at all.
- **Pure bookkeeping:** the printed 1.22, which is $j_{1,1}/\pi$ rounded up by 270.65 ppm, and the $\pi$ in the sinc argument, which cancels at every zero.
- **Under Golden Pi:** $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443$, $\hat\pi^{2} = 16/\varphi = 9.8885438199983175713$, label shifts of $+0.0959022309\%$ (constant) and $-0.0958103466\%$ (its reciprocal), with $4/\hat\pi = \sqrt\varphi$ and $\hat\pi/4 = 1/\sqrt\varphi$ exact.
- **Not claimed:** that any diffraction experiment has ever favoured one value over the other. It cannot, and the reason is structural rather than technical.

Computed, never measured — and in this problem, mostly not even present.

## Further Reading

- [Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°](/blog/posts/2026-10-22-descartes-angle-defect-gauss-bonnet-720-degrees-golden-pi/)
- [Buffon's Needle: How a Stick Dropped on Ruled Paper Computes the Circle Constant](/blog/posts/2026-10-21-buffon-needle-geometric-probability-computes-circle-constant-golden-pi/)
- [The 4π Turn: How a Spinor Pays the Circle Constant Back Twice](/blog/posts/2026-10-17-spinor-double-cover-4pi-rotation-golden-pi/)
- [The Wallis Product: How an Infinite Product of Rationals Computes π/2](/blog/posts/2026-10-12-wallis-product-infinite-product-rationals-computes-circle-constant-golden-pi/)
- [Squaring the Circle with Golden Pi: The Exact Geometric Construction](/blog/posts/squaring-circle-golden-pi-geometric-proof/)
