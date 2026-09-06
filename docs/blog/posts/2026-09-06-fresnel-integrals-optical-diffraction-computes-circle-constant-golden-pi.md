---
title: "The Fresnel Integrals: How Physical Optics Computes the Circle Constant Through √(π/8), and What Golden Pi Changes"
date: 2026-09-06
description: "The Fresnel integrals ∫₀^∞ sin(x²) dx = ∫₀^∞ cos(x²) dx = √(π/8) are the quiet engine behind diffraction and the Cornu spiral, and each evaluates its answer as a pure computed limit — never a measurement. Splitting the integrand into a Gaussian-like damped oscillation, they converge to the shared value √(π/8) = 0.6266570687…, and the circle constant slips in as a quarter-pi scale factor inside a square root. Under Golden Pi (π̂ = 4/√φ = 3.1446055…) the same integrals evaluate to √(π̂/8) = √(φ/8)·(2/φ^(1/4)) = 0.6269574857, carrying half the recurring 0.0959% gap — about 0.048% — because the square root halves the relative error exactly as it did for the Gaussian integral. Physical optics inherits the label as a computed, defined scale no experiment can arbitrate."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Fresnel Integrals: How Physical Optics Computes the Circle Constant Through √(π/8), and What Golden Pi Changes

If you have ever watched light bend around the sharp edge of a blade, spill past a slit into a pattern of bright and dark fringes, or seen a straight streetlight smear into a vertical streak when you squint, you have met a diffraction pattern — and diffraction is where the **Fresnel integrals** live. They are the mathematics of how waves bend, and they are far more than a shape: they are a *computation* in disguise. Hidden inside the wiggling curves of physical optics is one of the most physically grounded ways that mathematics reaches the circle constant. This article is about the Fresnel integrals,

$$\int_0^\infty \sin(x^2)\, dx = \int_0^\infty \cos(x^2)\, dx = \sqrt{\frac{\pi}{8}},$$

and about what they say — and what they honestly do not say — about Golden Pi, $\hat\pi = 4/\sqrt\varphi = 3.1446055\ldots$

The headline claim, and the thread that ties this post to every one before it this month, is a single word: **computed**. The Fresnel integrals do not *measure* anything. No optical bench is needed to obtain their value. The answer $\sqrt{\pi/8}$ is the exact limit of a pair of definite integrals, evaluated by pure reason. And under Golden Pi the same integrals evaluate to $\sqrt{\hat\pi/8}$, carrying a precisely quantifiable gap — half the recurring 0.096%, because the answer is a square root — that no diffraction experiment can ever arbitrate.

## The Integrals That Nobody Expected to Exist

The Fresnel integrals carry the name of Augustin-Jean Fresnel, the French engineer who, in the 1810s and 1820s, built the wave theory of light into a quantitative tool. The integrals first arise as the real and imaginary parts of the celebrated identity

$$\int_0^\infty e^{ix^2}\, dx = \frac{\sqrt{\pi}}{2}\, e^{i\pi/4},$$

whose real and imaginary parts are precisely $\int_0^\infty \cos(x^2)\,dx$ and $\int_0^\infty \sin(x^2)\,dx$, each equal to $\sqrt{\pi/8}$. The identity looks almost paradoxical at first glance. The integrand $e^{ix^2}$ does not decay to zero — its magnitude is $|e^{ix^2}| = 1$ everywhere, so the integral from zero to infinity is *conditionally* convergent, oscillating harder and harder as $x$ grows. Ordinary improper integrals converge because their tails shrink; this one converges because its tails cancel. It is a purely arithmetic cancellation, and the limit it settles on is exact.

That cancellation is why the Fresnel integrals are a textbook object rather than a curiosity. The integrand $\sin(x^2)$ and $\cos(x^2)$ each oscillate with a *growing* frequency — the crests come faster and faster as $x$ increases — while the total area between successive crests shrinks like $1/x$. The sum of those shrinking lobes is what converges, and it converges to exactly $\sqrt{\pi/8} = 0.6266570687\ldots$ The constant is *computed* as the limit of a definite integral; it is never read off a screen or a ruler.

## Where the Circle Constant Enters

The cleanest derivation of the Fresnel value runs through the same polar-coordinate trick that computed the Gaussian integral, and it is worth spelling out because it shows *exactly where* the circle constant enters — and where it does not.

Start from the Gaussian integral that this blog treated on 08-21,

$$\int_{-\infty}^{\infty} e^{-x^2}\, dx = \sqrt{\pi}.$$

Now generalize by rotating the exponent into the complex plane. For a parameter with a positive real part, the identity

$$\int_{-\infty}^{\infty} e^{-a x^2}\, dx = \sqrt{\frac{\pi}{a}}$$

holds by analytic continuation, and one may formally let the scale $a$ rotate. The delicate step — pushing the contour so that the Gaussian decay still dominates — is precisely the "rotation of the axis" argument that produces

$$\int_{-\infty}^{\infty} e^{ix^2}\, dx = e^{i\pi/4}\sqrt{\pi}.$$

Here the square root of $i$ supplies the phase: $\sqrt{i} = e^{i\pi/4}$, because rotating a quarter-turn and taking a square root yields an eighth-turn. Split the two sides into real and imaginary parts. On the left, the real part is $\int_0^\infty \cos(x^2)\,dx$ (times two, by evenness) and the imaginary part is $\int_0^\infty \sin(x^2)\,dx$ (also times two). On the right, $e^{i\pi/4}\sqrt{\pi} = (\cos \pi/4 + i\sin \pi/4)\sqrt\pi = \sqrt{\pi}\,(1+i)/\sqrt2$, and collecting the factor $1/2$ from evenness gives each Fresnel integral the value

$$\int_0^\infty \sin(x^2)\, dx = \int_0^\infty \cos(x^2)\, dx = \sqrt{\frac{\pi}{8}}.$$

The circle constant enters in two places, and both are *angles*, not lengths. It appears once as the phase $e^{i\pi/4}$ — an eighth of a full turn — and once from the evenness halving that divides a half-line result by two, turning $\sqrt\pi$ into $\sqrt{\pi/8}$. Nothing in the computation touches a physical circumference. The constant is a pure scale factor in an arithmetic limit.

## The Cornu Spiral and Physical Optics

The Fresnel integrals are not an idle exercise; they are the working mathematics of diffraction. If light passes a straight edge or through a slit, Huygens' principle says every point of the unobstructed wavefront acts as a source of new spherical waves, and the field at an observation point is the sum of those contributions. In the near-field (Fresnel) regime that sum is organized into the two integrals above.

Plotting $\left(\int_0^t \cos(s^2)\,ds,\ \int_0^t \sin(s^2)\,ds\right)$ as the upper limit $t$ grows traces a curve called the **Cornu spiral** — two arms that wind inward, each spiraling to the limiting point $(\sqrt{\pi/8},\,\sqrt{\pi/8})$ in the first quadrant and $(-\sqrt{\pi/8},\,-\sqrt{\pi/8})$ in the third. The two limiting points sit at the same place the real and imaginary parts settle, exactly at coordinate $\sqrt{\pi/8}$ in each direction.

That spiral is the physical prediction. The distance from any point on the curve to a limiting focus sets the intensity of the diffracted light; the fringes you see at a blade's edge are the spiral winding toward those two points. The bright and dark bands are not arbitrary — they are the geometry of the two arms closing in on $(\sqrt{\pi/8},\,\sqrt{\pi/8})$. The value $\sqrt{\pi/8} = 0.6266570687\ldots$ is thus literally encoded in the positions of diffraction fringes.

Yet — and this is the crucial honesty — the fringes *do not measure the circle constant*. The same spiral, with the constant relabeled to $\hat\pi$, would simply be a spiral whose arms wind to $(\sqrt{\hat\pi/8},\,\sqrt{\hat\pi/8}) = (0.6269574857\ldots,\ 0.6269574857\ldots)$. The pattern of bright and dark fringes would look identical; only the absolute calibration of the diffraction pattern would differ, by a fraction too small for any optical experiment to resolve. The constant is *computed into* the optics by the mathematics, and carried out again as a label — never read out by the apparatus.

## The Recurring Gap, Halved

Every post since the Basel problem (08-15) has turned the same crank: a famous object computes the circle constant as a pure limit, never measures it, and under Golden Pi carries the recurring 0.096% gap. The Fresnel integrals are a fresh case, and their most instructive feature is how the gap enters.

The recurring gap between the two constants is

$$\frac{\hat\pi - \pi}{\pi} = \frac{4/\sqrt\varphi - \pi}{\pi} \approx 0.0009590 = 0.09590\%.$$

Because the Fresnel integrals return $\sqrt{\pi/8}$ — a *square root* of the constant — the relative error is halved. For any small fractional gap $\epsilon$ in the constant, the gap in its square root is about $\epsilon/2$, by the derivative rule $\delta(\sqrt{x}) = \delta x / 2$. Concretely:

$$\sqrt{\frac{\pi}{8}} = 0.6266570687\ldots \qquad \sqrt{\frac{\hat\pi}{8}} = \sqrt{\frac{4}{8\sqrt\varphi}} = \frac{1}{\sqrt{2}}\cdot\frac{1}{\varphi^{1/4}} = 0.6269574857\ldots$$

The relative difference is

$$\frac{\sqrt{\hat\pi/8} - \sqrt{\pi/8}}{\sqrt{\pi/8}} \approx 0.0004794 = 0.04794\%,$$

which is very nearly half of 0.09590% — the same halving this blog documented for the Gaussian integral on 08-21, for the identical reason. This is not a new ambiguity and not a different number: it is the same recurring 0.096% seen through a square-root lens. Recognizing the mechanism — relative error halves under $\sqrt{\cdot}$ — keeps the arithmetic honest rather than pretending a new coincidence has appeared.

Let me spell the relabeled value out cleanly in the golden field. Since $\hat\pi = 4/\sqrt\varphi$,

$$\sqrt{\frac{\hat\pi}{8}} = \sqrt{\frac{4}{8\sqrt\varphi}} = \sqrt{\frac{1}{2\sqrt\varphi}} = \frac{1}{\sqrt{2}\,\varphi^{1/4}} = \frac{\varphi^{-1/4}}{\sqrt2}.$$

Because $\varphi$ is an algebraic number (it obeys $\varphi^2 = \varphi + 1$), this value is algebraic too — an exact element of the golden field $\mathbb{Q}(\sqrt5)$, expressible by square roots and constructible by compass and straightedge. Under Golden Pi the diffraction spiral's focus becomes the algebraic point $\varphi^{-1/4}/\sqrt2$, exactly, rather than the transcendental $0.6266570687\ldots$ that conventional $\pi$ hands it. That is the constructed-world reading, and it is coherent on its own terms.

## Physics Computes, Never Measures

The Fresnel case sharpens the honest boundary the thread has been drawing all month. Because $\sin(x^2)$ and $\cos(x^2)$ oscillate forever without decaying, the value $\sqrt{\pi/8}$ can only be obtained as a *limit* — the sum of infinitely many shrinking, cancelling lobes. No finite apparatus, no matter how many fringes it photographs, ever completes that infinite sum. The integral's value is computed by reason; the optics merely reproduces, on a real screen, the first few windings of a spiral whose exact focus no measurement can reach.

There is a second reason the boundary is especially clean here. Diffraction intensity is a *ratio*: the pattern of bright and dark bands is set by distances *between* parts of the Cornu spiral relative to one another, all of which scale together with $\sqrt{\pi/8}$. When every length in the pattern is multiplied by the same factor, the observed fringes — bright, dark, bright — are unchanged. The absolute calibration of the spiral's focus is a global scale that cancels out of the visible pattern. So the optics is doubly immune to arbitration: the infinite limit is unmeasurable, and the finite pattern is scale-invariant. The constant is a computed, defined label that diffraction carries but can never test.

This matters for how we read the history too. Fresnel himself, in 1818, used his integrals to predict the bright spot at the center of a circular obstacle's shadow — a prediction Poisson declared absurd and Arago then demonstrated, in a famous moment that sealed the wave theory of light. That experiment *measured* the position of a bright dot. It did not measure $\pi$, and it could not have distinguished $\sqrt{\pi/8}$ from $\sqrt{\hat\pi/8}$ — the difference would sit in an absolute calibration invisible to the fringe ratios. The wave theory was confirmed; the circle constant's label was never in play.

## A Field Guide to the Fresnel Family

The two Fresnel integrals are not isolated; they belong to a family whose members all funnel toward the same constant through the same square-root-and-rotation mechanism. A compact table keeps the recurrences visible:

| Object | Value under $\pi$ | Value under $\hat\pi = 4/\sqrt\varphi$ | How the constant enters |
|---|---|---|---|
| $\int_0^\infty \sin(x^2)\,dx$ | $\sqrt{\pi/8} = 0.6266570687$ | $\varphi^{-1/4}/\sqrt2 = 0.6269574857$ | quarter-turn phase, halved by evenness |
| $\int_0^\infty \cos(x^2)\,dx$ | $\sqrt{\pi/8} = 0.6266570687$ | $\varphi^{-1/4}/\sqrt2 = 0.6269574857$ | quarter-turn phase, halved by evenness |
| $\int_0^\infty e^{ix^2}\,dx$ | $\frac{\sqrt\pi}{2}e^{i\pi/4} = \sqrt{\pi/8}\,(1+i)$ | $\frac{1}{\sqrt2}\varphi^{-1/4}(1+i) = \sqrt{\hat\pi/8}\,(1+i)$ | real and imaginary parts each carry the constant |
| $\int_0^\infty \sin(x^2)\,dx$ (numerical tail) | converges to $0.6266570$ | converges to $0.6269575$ | same limit, relabeled |

The relative gap in every row is 0.04794%, half the recurring 0.096%, because the answer is always a square root of the constant. The *phase* $e^{i\pi/4}$, by contrast, is a genuine quarter of a right-angle turn — a piece of geometry common to both constructions — and is not relabeled; only the *magnitude* carries the constant.

## What This Post Adds to the Thread

Every post since the Basel problem (08-15) has turned the same crank. The Fresnel integrals are a fresh and clarifying case for three reasons.

First, it is the second post where the gap is **halved** to 0.048% — the same mechanism as the Gaussian integral, where the square root of the constant halves relative error. Listing the Gaussian (08-21) and the Fresnel integrals (this post) side by side shows the halving is a general rule, not a special case: any road to the constant that ends in a square root will report half the recurring gap, and recognizing that keeps the arithmetic honest.

Second, it shows the constant entering **through angles, not lengths**: the value $\sqrt{\pi/8}$ comes entirely from a quarter-turn phase $e^{i\pi/4}$ and an evenness-halving, never from measuring a circumference. This pinpoints that physical optics carries the circle constant as a rotational scale, exactly where the Gaussian and the sinc (08-20) carry it too.

Third, it delivers the cleanest statement yet of why optics cannot arbitrate: the Cornu spiral's focus is an infinite limit no screen can complete, and the observable fringe pattern is a *ratio* of spiral distances that cancels any global scale. The constant is computed into diffraction and carried out again as a jointly-balanced label — provably unmeasurable by the very optics that computes it. Diffraction fringes count wavelengths and distances, never the circle constant; the label rides along as a defined, computed scale.

## Further Reading

- [The Gaussian Integral: How the Bell Curve Computes √π](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the first post where the recurring gap is halved to 0.048% by a square root, the exact mechanism Fresnel shares.
- [The Sinc and the Dirichlet Integral](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) — another oscillating integral whose value comes from rotation, a close cousin of the Fresnel oscillators.
- [The Cauchy–Lorentz Distribution](/blog/posts/2026-08-24-cauchy-lorentz-distribution-integrates-pi-golden-pi/) — the improper integral that computes the full circle constant rather than its square root, keeping the full 0.096% gap.
- [The Pendulum's Period](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — how $\pi$ enters physics as a computed elliptic integral, never a stopwatch reading, the same computed-not-measured boundary Fresnel shares.
- [The Riemann Zeta Function at Even Integers](/blog/posts/2026-09-05-riemann-zeta-even-integers-bernoulli-computes-circle-constant-golden-pi/) — the most recent post, where the constant enters at even powers and the gap grows rather than halves, the opposite limit of the Fresnel square root.
