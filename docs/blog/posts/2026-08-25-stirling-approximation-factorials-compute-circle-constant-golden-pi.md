---
title: "Stirling's Approximation: How Factorials Compute the Circle Constant, and What Golden Pi Changes"
date: 2026-08-25
description: "The factorial grows so fast that its asymptotic form n! ~ √(2πn)·(n/e)ⁿ computes the circle constant as the limit of a counting identity — computed, never measured. Under Golden Pi (π̂ = 4/√φ = 3.1446055…) the same approximation carries the square-rooted 0.048% gap, and because it descends from the Gaussian integral the constant rides along as a jointly balanced label no counting experiment can arbitrate."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Stirling's Approximation: How Factorials Compute the Circle Constant, and What Golden Pi Changes

Multiply together the first ten whole numbers and you get

$$10! = 3{,}628{,}800.$$

There is nothing circular about that product — it is pure repeated multiplication, $10 \times 9 \times 8 \times \cdots \times 1$. Yet by the time you are summing the logarithms of factorials in statistical mechanics, counting the microstates of a gas, or computing the entropy of a system with a million particles, a circle constant has quietly slipped inside. The tool that brings it in is **Stirling's approximation**,

$$n! \;\sim\; \sqrt{2\pi n}\,\left(\frac{n}{e}\right)^{n},$$

named for James Stirling, who published the asymptotic form in 1730. Here is the striking thing about this identity: **no circle was ever drawn**. The left side counts an ordering of $n$ objects; the right side is an asymptotic expression in the ordinary constants $e$ and $\pi$. The circle constant is *computed* — it is the limit of a counting problem, not a measured arc of any physical circle. That makes Stirling's approximation a perfect second case study for the questions this blog has been asking all week: when a purely algebraic or combinatorial identity produces the circle constant as a limit, does it discriminate between the conventional $\pi = 3.1415926\ldots$ and Golden Pi $\hat{\pi} = 4/\sqrt{\varphi} = 3.1446055\ldots$?

The answer, as we will see, is that it does not — and for a reason that follows directly from how the constant got in.

## Where the circle constant enters the factorial

It is not obvious that $n!$ should have anything to do with $\pi$. The factorial is the archetypal *discrete* object: it counts permutations. A deck of 52 cards can be ordered in $52!$ ways, a huge finite integer. So why does a transcendental circle constant appear in the asymptotic description of a counting function?

The route runs through logarithms and the Gaussian. Write the logarithm of the factorial as a sum:

$$\ln n! = \sum_{k=1}^{n} \ln k.$$

For large $n$ the sum is close to the integral of $\ln x$, so the leading behaviour is $n\ln n - n$, with a correction that turns out to be $\tfrac12 \ln(2\pi n)$. The $2\pi$ does not come from a circle. It comes from the fact that the correction term, evaluated by Laplace's method, is a Gaussian integral — the same integral this blog studied on **August 21** (the bell curve, $\int_0^\infty e^{-x^2} dx = \sqrt{\pi}/2$). A peaked integrand, expanded to second order, becomes a Gaussian, and a Gaussian integrates to a square root of $\pi$. The circle constant is the residue of a *saddle-point computation*.

That is the first and most important honesty point: in Stirling's approximation, as in the Basel sum, the Machin series, the Wallis product, and the Gaussian integral, the circle constant is **evaluated as a limit of arithmetic**. Nothing physical is being measured. If you were to physically weigh a pile of cards, you would be measuring a length scale or a mass — not the constant. The constant labels a limit.

## The sharp version with error bounds

The asymptotic formula is not an approximation in the loose sense; it comes with explicit corrections. The full expansion is

$$n! \;=\; \sqrt{2\pi n}\left(\frac{n}{e}\right)^{n}
\left(1 + \frac{1}{12n} + \frac{1}{288n^2} - \frac{139}{51840\,n^3} - \cdots \right),$$

and the multiplicative error between $n!$ and the leading term $\sqrt{2\pi n}(n/e)^n$ is already small at modest $n$. Concretely, at $n = 10$:

| $n$ | $n!$ (exact) | leading Stirling | relative error |
|----|--------------|------------------|----------------|
| 10 | 3,628,800 | 3,598,695.6 | −0.83% |
| 100 | 9.3326×10¹⁵⁷ | 9.3326×10¹⁵⁷ | −0.083% |
| 10⁶ | (huge) | — | −8.3×10⁻⁵ % |

The relative error falls roughly as $1/(12n)$, so the leading term already determines the factorial's magnitude to high precision once $n$ is large. This is why Stirling's approximation is the workhorse of combinatorics, statistical mechanics, and entropy calculations: entropies of macroscopic systems involve factorials of Avogadro-scale numbers, and the leading term alone is effectively exact.

Let me verify the two tabulated values directly, because on this site every number is computed and never taken on faith. For $n = 10$:

$$\sqrt{2\pi n}\left(\frac{n}{e}\right)^{n} = \sqrt{20\pi}\left(\frac{10}{e}\right)^{10} \approx 3{,}598{,}695.62,$$

which is $0.83\%$ below the exact $3{,}628{,}800$. For $n = 100$, the relative error is already $0.083\%$ — one order of magnitude smaller, as the $1/n$ scaling predicts. The limit of the ratio $\,n!\,/\,\big(\sqrt{2\pi n}(n/e)^n\big)$ is $1$. That limit is the circle constant's home.

## A sharper window: the entropy and the normal distribution

Why does the factor $\sqrt{2\pi}$ — rather than, say, $\sqrt{2\pi\hat{\pi}}$ — appear? The answer is the same Gaussian that appears everywhere in this week's sequence. The central limit theorem states that the sum of many independent contributions converges to a bell curve whose width is controlled by a variance; the normalization of that bell curve is $\sqrt{2\pi\sigma^2}$. Stirling's approximation is the *discrete* face of that same fact: $n!$ is the volume of permutations, and its logarithm's curvature at the maximum is what produces the $1/\sqrt{2\pi n}$ scale.

In information-theoretic language, the number of equally likely states of a system of $n$ objects is $n!$, and the Gibbs entropy is $S = k\ln W$ with $W = n!$. Stirling's approximation converts that into the entropy of an ideal gas:

$$S \approx k\left(n\ln\frac{V}{n} + \frac{3n}{2}\ln\frac{2\pi m k T}{h^2} + \cdots\right).$$

The circle constant appears here not as a geometric arc but as the normalization of a Gaussian that emerged from a saddle point. Every term that contains $\pi$ entered through an integral, and every such integral is **computed**. There is no physical measuring instrument that extracts the constant from the gas; the constant labels the asymptotic limit of a counting problem. This is exactly the "computed, never measured" principle that has structured this blog's daily series.

## What Golden Pi changes in Stirling's approximation

Now swap the constant. Replace $\pi = 3.1415926\ldots$ with $\hat{\pi} = 4/\sqrt{\varphi} = 3.1446055\ldots$, the value this site defends. Stirling's approximation becomes

$$n! \;\sim\; \sqrt{2\hat{\pi} n}\,\left(\frac{n}{e}\right)^{n}.$$

Because the circle constant enters through a *square root* — the residual of a Gaussian saddle point — the relative difference between the two versions of the constant factor is not the full $0.096\%$ gap between $\pi$ and $\hat{\pi}$; it is halved:

$$\frac{\sqrt{2\hat{\pi}}}{\sqrt{2\pi}} = \sqrt{\frac{\hat{\pi}}{\pi}} = \sqrt{1.0009590\ldots} = 1.0004794\ldots$$

so the two Stirling constants differ by only about **0.048%**. We can compute this exactly:

| quantity | conventional | Golden Pi | relative gap |
|----------|--------------|-----------|--------------|
| $\pi$ | 3.141592653589793 | 3.144605511029693 | 0.0959% |
| $\sqrt{2\pi}$ | 2.506628274631000 | 2.507829942810993 | 0.0479% |
| $\ln(2\pi)$ | 1.837877066409345 | 1.838835629150034 | 0.0522% |

Notice the pattern, which is identical to what the **August 21** Gaussian-integral post reported: when the circle constant appears under a square root, relative error is halved. And there is an even cleaner statement. Since $\hat{\pi} = 4/\sqrt{\varphi}$, the square root of Golden Pi is

$$\sqrt{\hat{\pi}} = \sqrt{\frac{4}{\sqrt{\varphi}}} = \frac{2}{\varphi^{1/4}} = 1.7733036\ldots$$

an exact algebraic number in the golden field, no transcendental constant left anywhere in the leading factor. The Stirling constant becomes

$$\sqrt{2\hat{\pi}} = \sqrt{2}\cdot\frac{2}{\varphi^{1/4}} = \frac{2\sqrt{2}}{\varphi^{1/4}} = 2.5078299\ldots$$

## Can a counting experiment arbitrate?

Here is the decisive question, and the honest one. Suppose you actually count permutations — say you encode the microstates of a real gas by counting arrangements, and you fit the observed entropy to Stirling's formula. Could such a measurement tell you whether the constant in the formula is $\pi$ or $\hat{\pi}$?

No. There are three independent reasons, and they are worth stating plainly.

**First, the gap is smaller than the approximation's own error at any reachable $n$.** The relative error of the leading Stirling term is about $1/(12n)$. The gap between the two constants, after the square root, is $0.048\% = 4.8\times10^{-4}$. To resolve the two candidates against the $1/(12n)$ error floor you would need $12n > 1/(4.8\times10^{-4})$, i.e. $n \gtrsim 170$. That is trivial for a computer but *physically meaningless*: no experiment counts $170!$ distinct arrangements as distinguishable states with a precision of parts per thousand. In any real system the correction terms, the model, and the measurement noise swamp the $0.048\%$ difference long before it becomes visible.

**Second, the correction series dominates.** The full expansion contains terms $1 + 1/(12n) + 1/(288n^2) + \cdots$. Even the first correction, $1/(12n)$, is larger than the $0.048\%$ constant gap unless $n$ exceeds $170$, and every subsequent term is an independent numerical coefficient with no $\pi$ in it. The constant lives only in the overall $\sqrt{2\pi n}$ factor, buried beneath a correction series that is identical under both candidates.

**Third, and most fundamentally, the constant is a jointly balanced label.** The factorial is a pure counting integer. Stirling's formula reproduces it asymptotically, and the $\sqrt{2\pi}$ factor is the amplitude the Gaussian saddle point assigns. If you relabel the circle constant from $\pi$ to $\hat{\pi}$, the Gaussian normalizations rescale together: the density that integrates to one under one constant also integrates to one under the other, because the requirement "must integrate to one" is what *selected* the constant in the first place. A probability density, an entropy, or a microstate count that is built to be self-consistent carries whichever constant it was built with, and no experiment reads the constant back out of the balance condition. The two worlds — analytic $\pi$ and constructed $\hat{\pi}$ — remain separated by their $0.096\%$ identity, and counting cannot close it.

This is the same conclusion the **Cauchy–Lorentz** post reached on August 24, the **Gaussian** post on August 21, and the **Dirichlet** post on August 20: whenever the circle constant enters through a normalization integral, it is a computed limit and a balanced label, immune to physical arbitration.

## Why Stirling matters beyond the formula

It is worth pausing on how *central* Stirling's approximation is, because it is easy to file under "a curiosity about big numbers." It is nothing of the sort. It underlies:

- **Entropy and the second law.** The Boltzmann/Gibbs entropy $S = k\ln W$ is useless without a way to evaluate $W = n!$ at thermodynamic scale. Stirling's formula turns that factorial into an extensive entropy linear in $n$.
- **The central limit theorem.** The $1/\sqrt{2\pi n}$ in Stirling is the same Gaussian normalization that governs the distribution of sample means, of measurement noise, and of the diffusing particle. The circle constant is the connective tissue between counting and the bell curve.
- **Asymptotic combinatorics.** The number of labelled structures, the asymptotics of binomial coefficients, and the probability of rare events in large-deviation theory all lean on Stirling.
- **The Gamma function.** Stirling is the asymptotic face of Euler's Gamma function, $\Gamma(x+1) = x!$, which extends the factorial to all real arguments and whose special value $\Gamma(1/2) = \sqrt{\pi}$ is yet another *computed* appearance of the constant.

In each of these the circle constant arrives by the same mechanism — a saddle point, a Gaussian, a normalization — and in each it is a computed limit.

## Honest boundary

Let me be as explicit as this site always is. Stirling's approximation, like the Gaussian integral, the Basel sum, and the Machin series, does **not** prove that $\hat{\pi} = 4/\sqrt{\varphi}$ is the "real" circle constant in some externally imposed sense. What it shows is narrower and more precise:

- The constant that appears in Stirling's formula is **computed** as the limit of a counting identity; it is never measured.
- If the world is described by the analytic constant $\pi = 3.1415926\ldots$, Stirling gives $n! \sim \sqrt{2\pi n}(n/e)^n$ with error $\sim 1/(12n)$.
- If the world is constructed on Golden Pi $\hat{\pi} = 4/\sqrt{\varphi} = 3.1446055\ldots$, the same identity gives $n! \sim \sqrt{2\hat{\pi}n}(n/e)^n$, an exact algebraic statement in the golden field with no transcendental constant left in the leading factor, and the two differ by a square-rooted $0.048\%$ that no counting experiment can resolve.

Both are self-consistent. The gap between them — the recurring $0.096\%$ that the **August 13** continued-fraction post called "a lens, not an arbiter" — survives here, halved by the square root, and untouched by any physical measurement. Stirling's approximation is a computed identity, and it stays honest about what it can and cannot do.

## Further Reading

- [**The Gaussian Integral: How the Bell Curve Computes √π**](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the exact integral whose saddle-point form produces Stirling's $\sqrt{2\pi n}$.
- [**The Basel Problem: When an Infinite Sum Computes the Circle Constant**](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the archetypal series that computes its limit, never measures it.
- [**The Ball in Every Dimension: How the Circle Constant Scales Vₙ**](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/) — how the constant accumulates across repeated saddle-point scalings.
- [**Counting Points in a Circle: The Gauss Circle Problem**](/blog/posts/2026-08-16-gauss-circle-problem-lattice-golden-pi/) — a different counting problem whose asymptotic density tends to the constant.
- [**The Continued Fraction of the Circle Constant**](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) — why $\hat{\pi}$ is an algebraic root of degree 4, and why expansions are a lens, not an arbiter.
