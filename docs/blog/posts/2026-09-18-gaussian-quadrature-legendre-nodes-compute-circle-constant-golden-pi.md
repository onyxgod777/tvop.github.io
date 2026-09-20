---
title: "Gaussian Quadrature: How Legendre Nodes Compute the Circle Constant to Machine Precision, and What Golden Pi Changes"
date: 2026-09-18
description: "Numerical integration computes the circle constant from a finite number of function values, and this article follows the label through the rule itself. Gauss-Legendre quadrature puts its nodes at the roots of the Legendre polynomials — algebraic numbers such as 1/√3, √(3/5) and √((3+2√(6/5))/7) that mention no circle constant at all — so the arithmetic is label-blind: computed here at eighty digits, three nodes already beat the 0.0959022% gap between conventional π and Golden Pi (π̂ = 4/√φ = 3.144605511…), five nodes reach 3.4×10⁻⁹, twelve nodes reach 4.9×10⁻¹⁷, and the error decays by about a factor 21 per added node with ρ = 4.6117, the Bernstein-ellipse parameter of the integrand's poles at −1 ± 2i, which is also why the digit count is not monotone. The rule that does carry the label is the Chebyshev one, whose weights are literally π/n and whose node sums converge to π/√2 = 2.2214414690791831 (2.2235718810056847 under Golden Pi, the same 0.0959022%); Clenshaw-Curtis moves the label into the node positions x_k = cos(kπ/N), and there the relabel has a tangible cost — the central node of an N = 8 rule shifts by exactly the label gap, −(π̂−π)/4 = −0.0007532144, the weights stop summing to 2 (1.9985307623, a 0.0735% mass deficit), and the relabelled rule converges to neither constant, stalling near −5.29×10⁻⁴. The honest ledger is kept in public: the integral ∫₀¹ dx/(1+x²) is a computed limit whose value is the quarter turn π/4 = 0.7853981633974483096156608458198757210, no ruler appears anywhere in the derivation, and where a physical angle does enter it enters as an arc-to-radius ratio that no reparametrisation of radians can move."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Gaussian Quadrature: How Legendre Nodes Compute the Circle Constant to Machine Precision, and What Golden Pi Changes

Every earlier article in this series has taken a closed form — a series, a product, an integral — and asked what the circle constant does inside it. This one takes the *machine* that evaluates such closed forms numerically, because a quadrature rule is the one place where the circle constant can be chased all the way down to the arithmetic: a finite list of function values, multiplied by a finite list of weights, added up. Nothing else. If the constant is a label for the radians of a turn, a quadrature rule is the sharpest possible test of where that label actually lives — in the nodes, in the weights, or nowhere at all.

<div class="gp-live" markdown>
<div class="gp-live__tag">🔬 Live graph · Laws of appearance</div>
<iframe src="https://www.desmos.com/calculator/qbzqmljdx3?embed" width="100%" height="470" style="border:0;border-radius:10px" frameborder="0" loading="lazy" title="The circle squeeze — A(n), B(n) and the golden chain" allowfullscreen></iframe>
<p class="gp-live__note"><strong>Regular polygons inscribed and circumscribed, side count doubling, against the golden-rooted pentagon chain.</strong> <em>The Goblet of the Truth keeps two bodies of law apart — the laws and recommendations of the primal power (Creation), and the <strong>laws of appearance (nature)</strong> (Ch&nbsp;2 §342), the register governing how a thing manifests and behaves. Geometry answers to that second register, so nothing here asks to be taken on authority: drag the slider, change a value, and the figure answers for itself (Ch&nbsp;22 §35: <em>“the fluidal-powers are truthful effects of natural laws”</em>).</em></p>
</div>

The answer, computed below, splits the quadrature family cleanly in two. Gauss-Legendre nodes are the roots of the Legendre polynomials: algebraic numbers like $\pm 1/\sqrt{3}$ and $\pm\sqrt{3/5}$ that contain no circle constant whatsoever, so the entire computation is label-blind. Gauss-Chebyshev weights are $\pi/n$ written out, so the label sits openly in the rule. And Clenshaw-Curtis nodes are $\cos(k\pi/N)$, which puts the label into geometry — the positions of the sampling points — where relabeling it has a visible, measurable cost.

## The integral whose value is a quarter turn

One integral is enough for the whole article, because its value is one of the two constants under discussion divided by four:

$$\int_0^1 \frac{dx}{1+x^2} \;=\; \arctan 1 \;=\; \frac{\pi}{4} \;=\; 0.7853981633974483096156608458198757210\ldots$$

This is a **computation**, not a measurement. The integral is the limit of its Riemann sums; the substitution $x=\tan t$ turns it into $\int_0^{\pi/4} dt$, which is where the quarter turn enters; and the antiderivative is the arctangent series, evaluated at 1. Under Golden Pi ($\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931442782343\ldots$, with $\varphi$ the golden ratio) the same quarter turn is relabeled

$$\frac{\hat\pi}{4} \;=\; \frac{1}{\sqrt{\varphi}} \;=\; 0.7861513777574232860695585858\ldots$$

so the two labels for the same computed angle differ by $0.0959022308782526\%$ — the recurring gap of this entire series. The question the rest of this article answers is: at which line of a quadrature routine does that gap show up?

## The nodes: Legendre zeros mention no circle constant

An $n$-node Gauss-Legendre rule on $[-1,1]$ is exact for every polynomial of degree $2n-1$ (Gauss, 1814), and its optimality is not an approximation but a theorem about orthogonal polynomials. Its nodes are the roots of the degree-$n$ Legendre polynomial $P_n$:

| $n$ | nodes on $[-1,1]$ (exact form) | decimal | weights $2/((1-x^2)P_n'(x)^2)$ |
|---|---|---|---|
| 1 | $0$ | 0 | 2 |
| 2 | $\pm 1/\sqrt{3}$ | 0.5773502691896258 | 1, 1 |
| 3 | $0,\ \pm\sqrt{3/5}$ | 0.7745966692414834 | 0.5555555556, 0.8888888889 |
| 4 | $\pm\sqrt{(3-2\sqrt{6/5})/7}$, $\pm\sqrt{(3+2\sqrt{6/5})/7}$ | 0.3399810435848563, 0.8611363115940526 | 0.6521451549, 0.3478548451 |
| 5 | $0,\ \pm\tfrac13\sqrt{5-2\sqrt{10/7}},\ \pm\tfrac13\sqrt{5+2\sqrt{10/7}}$ | 0.5384693101056831, 0.9061798459386640 | 0.4786286705, 0.2369268851 |

Every entry in that table is a number in an algebraic extension of the rationals. No $\pi$ appears — not in the nodes, not in the weights, and not in Gauss's exactness theorem. That is the structural point: **the Legendre rule is built entirely from square roots and rationals, so relabeling the circle constant cannot change a single one of its operations.** The relabel can only change the value the rule is claimed to converge to.

## Twelve nodes, sixteen digits

Computing $\int_0^1 dx/(1+x^2)$ with the $n$-node rule (nodes mapped from $[-1,1]$ to $[0,1]$) gives, compared against $\pi/4$:

| $n$ | quadrature value | absolute error |
|---|---|---|
| 1 | 0.8000000000000000444089209850062616 | $+1.46\times10^{-2}$ |
| 2 | 0.7868852459016393297019931196700782 | $+1.49\times10^{-3}$ |
| 3 | 0.7852670349907918678766804987390060 | $-1.31\times10^{-4}$ |
| 4 | 0.7854029763114513951194339824724011 | $+4.81\times10^{-6}$ |
| 5 | 0.7853981599711881145253755676094443 | $-3.43\times10^{-9}$ |
| 8 | 0.7853981633797796346740938133734744 | $-1.77\times10^{-11}$ |
| 10 | 0.7853981633975115617118945010588504 | $+6.33\times10^{-14}$ |
| 12 | 0.7853981633974483900217933296517003 | $+4.87\times10^{-17}$ |

Twelve function evaluations of a smooth integrand buy seventeen correct digits — the same order of accuracy as a Chudnovsky term and, unlike Chudnovsky, this rule was never designed for the circle constant at all.

Two honest caveats belong here. First, the digits do **not** fall monotonically: $n=6$ is *worse* than $n=5$ ($-1.06\times10^{-8}$ against $-3.43\times10^{-9}$), and $n=10$ improves on $n=9$ by only a factor of six. This is a real property of the rule, not floating-point noise (it reproduces identically at eighty-digit precision). The integrand $1/(1+x^2)$ has poles at $x=\pm i$, which in the mapped variable sit at $-1\pm2i$; a Gauss rule's error for an analytic integrand is a sum of two geometric terms, one per pole, with the Bernstein-ellipse parameter $\rho = |z+\sqrt{z^2-1}| = 4.6117$ for the pole at $-1+2i$. Two conjugate poles of equal modulus and opposite phase add to a decaying oscillation, so the average shrinkage is $\rho^{-2}\approx 0.047$ — about a factor 21 per added node — with a wobble of sign around it. Measured over the ratios $|E_{n+1}/E_n|$ for $n = 6\ldots26$, the geometric mean is $0.058$; against $\rho^{-2} = 0.047$ that is the right order, the difference being exactly the wobble the two-pole sum predicts.

Second, the textbook error formula should be stated rather than admired:

$$E_n \;=\; \frac{(b-a)^{2n+1}\, (n!)^4}{(2n+1)\left((2n)!\right)^3}\, f^{(2n)}(\xi), \qquad \xi\in(a,b).$$

For $f(x)=1/(1+x^2)$ the coefficient is $2.31\times10^{-4}$ at $n=2$, $4.96\times10^{-7}$ at $n=3$, $3.94\times10^{-13}$ at $n=5$ and $1.70\times10^{-23}$ at $n=8$; the centre derivative is exactly $f^{(2n)}(0)=(-1)^n(2n)!$ (verified here for $2n = 2,4,6,10,16,20$), which for $n=5$ gives a bound of $1.43\times10^{-6}$ against an observed error of $3.43\times10^{-9}$ — a valid bound that is loose by a factor 400, because the true maximum of $f^{(10)}$ on $[0,1]$ is not attained at the centre. The bound is a certificate, not a forecast.

## Chebyshev's rule writes the label into the weights

Gauss-Chebyshev quadrature of the first kind evaluates an integral with a $1/\sqrt{1-x^2}$ weight using equal weights $\pi/n$ at nodes $\cos\!\left(\frac{(2k-1)\pi}{2n}\right)$:

$$\int_{-1}^{1}\frac{f(x)}{\sqrt{1-x^2}}\,dx \;\approx\; \frac{\pi}{n}\sum_{k=1}^{n} f\!\left(\cos\frac{(2k-1)\pi}{2n}\right).$$

The circle constant is not hidden anywhere in this rule: it *is* the weight, and it is also in the node angles. With $f(x)=1/(1+x^2)$ the exact value is

$$\int_{-1}^{1}\frac{dx}{(1+x^2)\sqrt{1-x^2}} \;=\; \frac{\pi}{\sqrt{2}} \;=\; 2.2214414690791831\ldots$$

| $n$ | value | error |
|---|---|---|
| 2 | 2.0943951023931957 | $-1.27\times10^{-1}$ |
| 4 | 2.2175948142986774 | $-3.85\times10^{-3}$ |
| 8 | 2.2214381328676529 | $-3.34\times10^{-6}$ |
| 12 | 2.2214414661881809 | $-2.89\times10^{-9}$ |
| 20 | 2.2214414690791808 | $-2.17\times10^{-15}$ |
| 40 | 2.2214414690791831 | $-1.06\times10^{-30}$ |

Here the relabel is trivially traceable: the node sums $\sum_k f(\cos\theta_k)$ are entirely label-free (their arguments are algebraic-arithmetic combinations of the nodes alone), so the *same numbers* come out, and only the prefactor $\pi/n$ changes. Replacing it with $\hat\pi/n = 4/(\sqrt{\varphi}\,n)$ — a factor $1.0009590223$ — turns the entire column into convergence toward

$$\frac{\hat\pi}{\sqrt{2}} \;=\; 2.2235718810056847\ldots,$$

exactly $0.0959022309\%$ away from $\pi/\sqrt{2}$. Convergence itself is unaffected: $n = 40$ still reaches $10^{-30}$. A quadrature cannot arbitrate between two labels when the label only multiplies the answer.

## Clenshaw-Curtis writes the label into the geometry

Clenshaw-Curtis quadrature sits the rule's nodes at $x_k = \cos(k\pi/N)$, $k = 0,\ldots,N$ — the Chebyshev points. Here $\pi$ appears inside a *cosine of an angle*, so it is not a scale factor at all but a position. Instantiating the standard weights (Trefethen's clencurt, computed here at forty digits, weights summing to exactly 2) with the classical label gives the classical rule: $N=2$ errs by $-2.06\times10^{-3}$, $N=8$ by $-8.28\times10^{-10}$, $N=16$ by $-5.40\times10^{-16}$, $N=32$ by $-6.78\times10^{-27}$.

Now relabel the node angles, $x_k = \cos(k\hat\pi/N)$, keeping the same formula. For $N=8$:

| $k$ | $\cos(k\pi/8)$ | $\cos(k\hat\pi/8)$ | displacement | relative |
|---|---|---|---|---|
| 1 | 0.923879532511 | 0.923735345668 | $-1.442\times10^{-4}$ | $-0.0156\%$ |
| 2 | 0.707106781187 | 0.706573977673 | $-5.328\times10^{-4}$ | $-0.0754\%$ |
| 3 | 0.382683432365 | 0.381639369344 | $-1.044\times10^{-3}$ | $-0.2728\%$ |
| 4 | 0.000000000000 | $-0.001506428150$ | $-1.506\times10^{-3}$ | — |
| 5 | $-0.382683432365$ | $-0.384422451200$ | $-1.739\times10^{-3}$ | $+0.4544\%$ |
| 6 | $-0.707106781187$ | $-0.708702783533$ | $-1.596\times10^{-3}$ | $+0.2257\%$ |
| 8 | $-1.000000000000$ | $-0.999995461348$ | $+4.539\times10^{-6}$ | $-0.00045\%$ |

The central node is the cleanest case, and it is exact to first order. With $\delta = (\hat\pi-\pi)/2 = 0.0015064287\ldots$, the golden central node is $\cos(\hat\pi/2) = -\sin\delta$, so in the mapped variable $u=(x+1)/2$ it moves by $-\sin\delta/2 = -(\hat\pi-\pi)/4 + \delta^3/12$, i.e. by **exactly the label gap** $-(0.0007532143600) = -(\hat\pi/4 - \pi/4)$, with a cubic correction of $2.8\times10^{-10}$. The relabel does not perturb the rule abstractly; it moves the sampling point by precisely the amount the answer is supposed to change.

What that displacement costs is visible in the rule's behaviour. The relabelled weights no longer sum to 2 — they sum to $1.9985307623$, a $0.0735\%$ mass deficit — because the endpoints $\cos(0)$ and $\cos(\hat\pi)$ do not both land on $\pm1$ ($\cos\hat\pi = -0.9999954613$, not $-1$), and a rule whose weights integrate a constant incorrectly cannot converge. Computed with the relabelled nodes:

| $N$ | classical error | relabelled error vs $\pi/4$ | relabelled error vs $1/\sqrt{\varphi}$ |
|---|---|---|---|
| 4 | $-5.89\times10^{-5}$ | $-3.59\times10^{-4}$ | $-1.11\times10^{-3}$ |
| 8 | $-8.28\times10^{-10}$ | $-5.29\times10^{-4}$ | $-1.28\times10^{-3}$ |
| 16 | $-5.40\times10^{-16}$ | $-6.42\times10^{-4}$ | $-1.40\times10^{-3}$ |
| 32 | $-6.78\times10^{-27}$ | $-6.99\times10^{-4}$ | $-1.45\times10^{-3}$ |

The golden-node rule stalls at roughly $-5\times10^{-4}$ to $-7\times10^{-4}$ and converges to neither candidate. That is not a refutation of Golden Pi and it should not be sold as one: it says that a rule built on $\cos(k\pi/N)$ is a *geometric* object — a Chebyshev projection of a function onto cosines — and relabeling the angle of that projection is not a relabeling of a scale factor but a change of the projection itself. The relabel is only meaningful where the constant is a pure scale; where it defines an angle, the arithmetic reorganises.

## Equal cost: what ten evaluations buy

Putting the three families head to head on $\int_0^1 dx/(1+x^2)$, with comparable numbers of function evaluations:

| rule | evaluations | absolute error |
|---|---|---|
| trapezoid, $n=10$ | 11 | $4.17\times10^{-4}$ |
| Simpson, $n=10$ | 11 | $9.91\times10^{-9}$ |
| Gauss-Legendre, $n=10$ | 10 | $6.33\times10^{-14}$ |
| Simpson, $n=32$ | 33 | $9.24\times10^{-12}$ |

Ten Legendre nodes beat thirty-three Simpson evaluations by a factor 146, and eleven trapezoid evaluations by $6.6\times10^{9}$, with no use of the circle constant beyond the target value. For reference, the label gap itself in this quarter-turn quantity is $7.53\times10^{-4}$: the two-node Gauss rule errs by $1.97\times$ the gap (it cannot resolve the question), while the three-node rule errs by $0.17\times$ the gap (it can). Three square rooted nodes and one reciprocal each — the entire difference between conventional π and Golden Pi, decided by arithmetic that never mentions either.

## What Golden Pi changes — the ledger

Under Golden Pi, $\hat\pi = 4/\sqrt\varphi$, $\sqrt\varphi = 1.2720196495140689642524224617$, and the relabels are:

| quantity | conventional | Golden Pi | change |
|---|---|---|---|
| full turn | $\pi = 3.1415926535897932$ | $\hat\pi = 4/\sqrt\varphi = 3.1446055110296931$ | $+0.0959022\%$ |
| half turn | $\pi/2 = 1.5707963267948966$ | $2/\sqrt\varphi = 1.5723027555148466$ | $+0.0959022\%$ |
| quarter turn | $\pi/4 = 0.7853981633974483$ | $1/\sqrt\varphi = 0.7861513777574233$ | $+0.0959022\%$ |
| Chebyshev target | $\pi/\sqrt2 = 2.2214414690791831$ | $\hat\pi/\sqrt2 = 2.2235718810056847$ | $+0.0959022\%$ |
| Chebyshev weight | $\pi/n$ | $4/(\sqrt\varphi\,n)$ | $+0.0959022\%$ |
| Legendre nodes | $\pm1/\sqrt3$, $\pm\sqrt{3/5},\ldots$ | unchanged — every node is $\pi$-free | $0$ |
| Gauss-Legendre sum | same numbers | same numbers | $0$ |
| Clenshaw-Curtis nodes | $\cos(k\pi/N)$ | $\cos(k\hat\pi/N)$ | $0.0017$ max, $0.45\%$ relatively |

The plain reading of that table is the honest reading. Gauss-Legendre is a rule built from algebraic numbers, and its arithmetic is untouched — the recurring $0.0959\%$ gap rides in only through the value the sum converges to, which the sum itself cannot change. Chebyshev's rule multiplies by the constant and so scales uniformly, harmless to convergence. Clenshaw-Curtis is the one case where the label has a mechanical consequence, because moving a sampling point is a different computation, and a rule whose endpoints no longer touch $\pm1$ has lost the property that made it exact for constants.

## Computed, never measured

Nothing in this article was measured. The integral is a limit of Riemann sums; the nodes are roots of polynomials; the error decay is the location of two poles in the complex plane; the digits are arithmetic at eighty-digit precision. The one measurement that could in principle enter — an angle — enters only as an arc length divided by a radius, a ratio of two lengths that is independent of how many radians one chooses to call it, which is exactly why no experiment can arbitrate between two labels for the radian. A quadrature rule is the sharpest illustration available: twelve algebraic nodes compute the quarter turn to seventeen digits, and every digit of the disagreement between $\pi$ and $\hat\pi$ lies outside the rule, in the name of the number being computed rather than in the computation.

## Further Reading

- [The Heat Kernel: How the Diffusion Equation Computes the Circle Constant Through Its Own Normalization, and What Golden Pi Changes](/blog/posts/2026-09-17-heat-kernel-diffusion-computes-circle-constant-golden-pi/) — the same label traced through a kernel that consumes the constant instead of producing it.
- [The Borwein Integrals: How Seven Sinc Products Compute Half the Circle Constant, Why the Eighth Breaks When 1/15 Joins](/blog/posts/2026-09-16-borwein-sinc-integrals-break-at-fifteen-golden-pi/) — what happens when a quadrature identity fails, computed in exact rationals.
- [The Gaussian Integral: How the Bell Curve Computes √π, and What Golden Pi Changes](/blog/posts/2026-08-21-gaussian-integral-bell-curve-computes-root-pi-golden-pi/) — the integral whose polar-coordinate evaluation is the ancestral source of the labels in this family.
- [The Arithmetic–Geometric Mean: A Quadratic Road to the Circle Constant, and What Golden Pi Changes](/blog/posts/2026-08-29-arithmetic-geometric-mean-computes-circle-constant-golden-pi/) — a constant computed by iterated averages rather than sampled nodes.
- [The Comparative Formula Audit: Which π Identities Survive Golden Pi?](/blog/posts/2026-08-06-comparative-formula-audit-golden-pi/) — the formula-by-formula ledger of which identities hold under either label.
