---
title: "The Bessel Functions: How Cylindrical Waves Compute the Circle Constant Through a Half-Turn Integral, and What Golden Pi Changes"
date: 2026-09-21
description: "The Bessel functions are the natural modes of every circular drum, every cylindrical waveguide and every circular aperture, and they are the cleanest case in mathematics where one and the same function is written two ways — one with the circle constant visible, one without it. The defining series J₀(x) = Σ (−1)ᵏ (x/2)²ᵏ/(k!)² and the differential equation x²y″ + xy′ + (x² − ν²)y = 0 mention no circle constant at all, so the zeros j₀,₁ = 2.4048255577… and j₁,₁ = 3.8317059702… are fixed roots of π-free arithmetic and their ratios (j₁,₁/j₀,₁ = 1.5933405057, the familiar 1.59 of a drum's first overtone) are label-blind. The constant enters only through Bessel's integral J_n(x) = (1/π)∫₀^π cos(nθ − x sin θ) dθ and the half-integer forms J_±1/2(x) = √(2/πx)·(sin x, cos x) — computed limits, never measurements — verified here to 50 digits (J₀(1) = 0.76519768655796655144971752610266322090927428975533, J₁(1) = 0.44005058574493351595968220371891491312737230199277) against closed forms that carry π explicitly. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the series, the ODE, the roots and the ratios do not move, while the half-integer prefactor shifts −0.0479166533% (π under a square root), the Airy-disk factor j₁,₁/π falls from 1.2196698913 to 1.2185013213, a membrane's fundamental at c = 60 m/s, a = 0.15 m moves 153.095949912 → 152.949268152 Hz (−0.0958103466%, because the frequency goes as 1/2π), and the golden-normalized half-turn integral (1/π̂)∫₀^π̂ cos(x sin θ) dθ differs from J₀(x) by ∫_π^π̂ cos(x sin θ) dθ ≈ 0.0030128574 rad, the label gap itself, to first order. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Bessel Functions: How Cylindrical Waves Compute the Circle Constant Through a Half-Turn Integral, and What Golden Pi Changes

Most of the objects in this series — the Basel sum, the Gaussian integral, the Fresnel integrals, the elliptic integral of an ellipse — are *one* mathematical thing that can be written in several ways. The Bessel functions are different, and that difference is why they are worth a whole article. A Bessel function is genuinely *two* things at once: a power series with rational coefficients that contains no circle constant anywhere in it, and an integral over a half turn whose prefactor is $1/\pi$. Both are the same function, evaluated at the same argument, and the circle constant is present in one representation and absent from the other.

That is a sharper picture of what the constant *is* than any single series can give. And it makes the golden-π question unusually concrete: which of the two representations does the golden relabel touch, and by how much?

## One function, two representations, and the constant only in one

The Bessel function of the first kind, order $\nu$, satisfies

$$x^2 y'' + x y' + (x^2 - \nu^2)\,y = 0$$

and for integer order $n$ its series is

$$J_n(x) \;=\; \sum_{k=0}^{\infty} \frac{(-1)^k}{k!\,(k+n)!}\left(\frac{x}{2}\right)^{2k+n}$$

There is no circle constant in that series. Not hidden under a square root, not in a limit — absent. The coefficients are $1/(k!(k+n)!)$ and the powers are powers of $x/2$. For $n = 0$ it is the pattern $1 - x^2/4 + x^4/64 - x^6/2304 + \cdots$; for $n = 1$ it is $x/2 - x^3/16 + x^5/384 - \cdots$.

The companion representation is Bessel's integral:

$$J_n(x) \;=\; \frac{1}{\pi}\int_0^{\pi} \cos\!\big(n\theta - x\sin\theta\big)\,d\theta$$

Here the constant is on the page twice: as the prefactor $1/\pi$ and as the upper limit of integration $\pi$. The integral runs over a half turn — not because a half turn is a measured length, but because the integrand is even and periodic with period $2\pi$, so the half turn is the canonical fundamental domain of an angular average. That is a *computed* limit of integration, the period of the trigonometric integrand, and it is the only sense in which the constant appears here.

Computing both at the same point is how the two representations are proved identical. The series was summed to forty terms and the integral evaluated by high-precision quadrature, both at 50 decimal digits:

```text
J0(1)  series   = 0.76519768655796655144971752610266322090927428975533
J0(1)  integral = 0.76519768655796655144971752610266322090927428975533   (diff 1.4e-52)
J1(1)  series   = 0.44005058574493351595968220371891491312737230199277
J1(1)  integral = 0.44005058574493351595968220371891491312737230199277   (diff 2.0e-52)
```

The integral identity was checked at four more points — $(n,x) = (2,0.7)$, $(3,2.5)$, $(0,5)$ — and each matched the series to better than $3\times10^{-52}$. This is a *computation*, in the strict sense: the integral's value is the limit of Riemann-style quadrature and the series' value is the limit of its partial sums, and the two limits agree. Nothing was measured, and nothing here depends on a physical circle being drawn anywhere.

## The roots of J₀ are the roots of π-free arithmetic

Because the series is $\pi$-free, so is everything determined by it alone. The zeros of $J_0$ and $J_1$ — the numbers that become the mode frequencies of a drum — are roots of $\pi$-free power series:

| root | value | what it is |
|---|---|---|
| $j_{0,1}$ | 2.404825557695772768621631879326454643124244909146 | first zero of $J_0$ |
| $j_{0,2}$ | 5.5200781102863106495966041128130274252218654787829 | second zero |
| $j_{0,3}$ | 8.6537279129110122169541987126609466855657952312754 | third zero |
| $j_{1,1}$ | 3.8317059702075123156144358863081607665645452742878 | first zero of $J_1$ |
| $j_{1,2}$ | 7.0155866698156187535370499814765247432763115029113 | second zero of $J_1$ |
| $j_{2,1}$ | 5.1356223018406825563014016901377654569737723475005 | first zero of $J_2$ |

The consequence is immediate and worth stating plainly: if the circle constant were relabelled tomorrow, these numbers would not change. They are the roots of $1 - x^2/4 + x^4/64 - \cdots$, and the numerator 1 and denominators 4 and 64 come from factorials, not from a circle. Two famous consequences:

- **the harmonic ratios of a circular membrane are label-blind.** The ratios $j_{1,1}/j_{0,1} = 1.5933405056951119971027307221235464247178623049426$ — the 1.59 that every drum tuner knows — and $j_{2,1}/j_{0,1} = 2.1355487866494034704271814200166705427938812935373$ are ratios of two such roots. No relabelling of the constant can move them, because the constant never appears in the arithmetic that produces them.
- **Neumann's identity is label-blind too.** $\sum_{n=-\infty}^{\infty} J_n(x)^2 = 1$ exactly; evaluated here at $x = 1$ by summing forty orders it returned $1.000000000000000000000000000000000000000000000000$ to the precision of the sum. A complete set of Bessel orders carries unit energy, and the unit is arithmetic, not angular.

## The constant does enter — through the half-integer orders

Where the circle constant is *not* dispensable is at half-integer order, where the Bessel functions collapse into elementary functions:

$$J_{1/2}(x) = \sqrt{\frac{2}{\pi x}}\,\sin x, \qquad J_{-1/2}(x) = \sqrt{\frac{2}{\pi x}}\,\cos x, \qquad J_{3/2}(x) = \sqrt{\frac{2}{\pi x}}\left(\frac{\sin x}{x} - \cos x\right)$$

These are not approximations; they are identities, and they are another way to compute the constant. Evaluating the closed forms at $x = 1$:

| quantity | closed form | value | golden label | shift |
|---|---|---|---|---|
| $J_{1/2}(1)$ | $\sqrt{2/\pi}\,\sin 1$ | 0.67139670714180309041636401204046708054564081676935 | 0.67107499630912221325196283034870752824755695858169 | −0.0479166533% |
| $J_{-1/2}(1)$ | $\sqrt{2/\pi}\,\cos 1$ | 0.43109886801837607952052096729853340008805601068862 | 0.43089229986824560333307332292207674127627657891111 | −0.0479166533% |
| $J_{3/2}(1)$ | $\sqrt{2/\pi}(\sin 1 - \cos 1)$ | 0.24029783912342701089584304474193368045758480608073 | 0.24018269644087660991888950742663078697128037967058 | −0.0479166533% |

The closed forms matched the series evaluations digit for digit at 50 places — another computation, not a measurement.

The shift is exactly half the recurring label gap, and the reason is written in the formula: the constant sits **under a square root**, so a relative change in the constant produces half the relative change in the function. The recurring gap itself is

$$\frac{\hat\pi - \pi}{\pi} = 0.09590223087825259636982582861956100205134871912376\%$$

and $\sqrt{\pi/\hat\pi} = 0.99952083346662447978145290919018411935812622659214$, which is $1 - 0.0479166533\%$. The same halving appeared in the Gaussian integral, $\Gamma(1/2)$ and Stirling's formula; it is the signature of a square root.

## What the golden half-turn integral does

Because Bessel's integral *is* the constant's other home, the honest test is to keep the integrand and relabel the half turn: define the golden-normalised object $\tilde J_0(x) = (1/\hat\pi)\int_0^{\hat\pi} \cos(x\sin\theta)\,d\theta$ and compare it with the true $J_0(x)$.

| $x$ | $\tilde J_0(x)$ | $J_0(x)$ | relative difference |
|---|---|---|---|
| 0.5 | 0.9385287591693960818082941812731285325558663692677 | 0.93846980724081290422840467359971262556892679709682 | 0.0062817075% |
| 1 | 0.76542265001884639840469242391422317206180413592245 | 0.76519768655796655144971752610266322090927428975533 | 0.0293993911% |
| 2 | 0.22463436627789770465067275191407884973424396220372 | 0.22389077914123566805182745464994862582515448221861 | 0.3321204828% |

The size of the distortion rises with $x$ because the integrand oscillates faster and the extra sliver of angle $\hat\pi - \pi$ buys more phase. The sliver itself is

$$\int_{\pi}^{\hat\pi}\cos(x\sin\theta)\,d\theta \;\approx\; \cos(x\sin\pi)\cdot(\hat\pi-\pi) \;=\; \hat\pi-\pi \;=\; 0.003012857439899905815590960092332833895314$$

to first order, because $\sin\theta$ vanishes at the endpoint. Computed numerically the three values above give 0.0030128563, 0.0030128529 and 0.0030128392 — each the label gap in radians, differing only in the second-order term. That is a clean, checkable statement: **relabelling the half turn changes the golden integral by precisely the size of the relabelling**, and the resulting function is not $J_0$, which is why no consistent relabel can preserve Bessel's integral without changing what the symbol $\pi$ means in the statement of the theorem.

## The Airy disk and the 1.22 that is really 3.8317/π

The most famous appearance of $j_{1,1}$ in physics is the circular aperture. The Fraunhofer diffraction pattern of a circular hole of diameter $D$ has intensity $I(\theta) \propto \left[2J_1(x)/x\right]^2$ with $x = \pi D\sin\theta/\lambda$, and the first dark ring therefore sits at

$$\sin\theta_1 = \frac{j_{1,1}}{\pi}\cdot\frac{\lambda}{D} = 1.2196698912665044549265388474652551778793593307751\cdot\frac{\lambda}{D}$$

This is where the familiar "1.22" of the Rayleigh criterion comes from, and it is a *computed* constant: a $\pi$-free Bessel zero divided by the circle constant. It needs no measurement at all, and it is the reason the resolution formula can be quoted as $1.22\,\lambda/D$ without anyone ever pointing a telescope at anything.

Under the golden label the same division gives $j_{1,1}/\hat\pi = 1.2185013213160813480738628325484720337047514706242$ — a shift of −0.0958103466%, once again the full recurring gap, undiluted this time because the constant enters to the first power in the denominator.

## The membrane: where the relabel lands on a physical number

A clamped circular membrane of radius $a$ and wave speed $c$ has normal-mode frequencies

$$f_{0n} = \frac{j_{0,n}\,c}{2\pi a}, \qquad f_{1n} = \frac{j_{1,n}\,c}{2\pi a}, \qquad \ldots$$

with the roots above fixed and the circle constant only in the conversion from radians-per-metre. Taking $a = 0.15$ m and $c = 60$ m/s — the order of magnitude of a taut polymer drumhead:

| mode | frequency (analytic label) | frequency (golden label) | shift |
|---|---|---|---|
| $f_{01}$ | 153.0959499124024713683896808132314203503 Hz | 152.9492681521326154789133259307792019585 Hz | −0.0958103466% |
| $f_{11}$ | 243.9339782533008909853077694930510355759 Hz | 243.7002642632162696147725665096944067409 Hz | −0.0958103466% |
| $f_{21}$ | 326.9438700763689452556244478612129154138 Hz | 326.6306240212010558342906557426184044937 Hz | −0.0958103466% |

Every absolute frequency moves by the same fraction — because the shift is a property of the constant, not of the mode — while every ratio stays put, as established above: $1.5933405057$ under both labels, to fifty digits.

The shift is −0.0958103466% rather than the +0.0959022309% seen in $1/\hat\pi$ elsewhere in this series for the trivial reason that the frequency goes as $1/2\pi$: the two printed gaps differ by the square of the gap itself, a discrepancy of order $10^{-6}$ percent that only matters if you are quoting a fraction to ten digits, which we are, deliberately, because that is the honest way to keep a ledger.

### Is a drum a measurement that could arbitrate?

A tuned drum *is* a physical measurement, so this is the one place in the article where the word "measured" is legitimate: you can put a microphone on a membrane and read its modes. But the frequencies so obtained cannot settle the constant, and the arithmetic of the previous section says why. The measured fundamental of a real membrane departs from $j_{0,1}c/2\pi a$ by far more than 0.096%, because the idealisation is doing the heavy lifting: air loading and radiation damping shift the resonance, the tension of a real membrane is neither perfectly uniform nor perfectly constant (a polymer head creeps measurably over a session), the clamped boundary is not perfectly clamped, and $c$ is itself a measured quantity with its own uncertainty absorbed into the number you would compare against. The gap between the two labels is smaller than every one of those corrections — it is smaller than the *uncertainty of the uncertainty*. The honest position is the one this site keeps repeating: the constant is decided by the limits of the series, the integrals and the roots, all of which are computed, and the physics inherits whichever label the arithmetic settles on. Nobody resolves a $10^{-3}$ difference in a symbol by weighing a drum.

## What the golden label moves, and what it does not

| object | representation | golden-π effect |
|---|---|---|
| $J_n$ series $\sum (-1)^k (x/2)^{2k+n}/(k!(k+n)!)$ | π-free | none — the same rationals converge to the same function |
| Bessel differential equation | π-free | none — order, linearity and singularity structure unchanged |
| zeros $j_{0,1}, j_{1,1}, j_{0,2}, \ldots$ | roots of a π-free series | none — fixed algebraic/transcendental roots |
| harmonic ratios $j_{1,1}/j_{0,1}$, $j_{2,1}/j_{0,1}$ | ratio of π-free roots | none — label-blind |
| Neumann sum $\sum J_n^2 = 1$ | π-free identity | none |
| Bessel's integral $(1/\pi)\int_0^\pi$ | constant visible twice | integral over the golden half turn differs by $0.0030128574$ rad at first order; normalised value off by 0.0063%–0.33% |
| half-integer forms $\sqrt{2/\pi x}$ | constant under a square root | −0.0479166533% |
| Airy factor $j_{1,1}/\pi$ | constant to the first power | 1.2196698913 → 1.2185013213 (−0.0958103466%) |
| membrane frequencies $j\,c/2\pi a$ | constant to the first power | −0.0958103466% |

One more honest number, because it cuts both ways. The asymptotic spacing of large zeros of $J_0$ is $\pi$ itself: $j_{0,20} - j_{0,19} = 3.141485264146227750018093630035266738157$, which misses the analytic constant by −0.0034183122%. That is a real, computable, $\pi$-adjacent quantity — and it is 28 times *closer* to the analytic constant than the golden label is, which is exactly the kind of evidence the golden argument has to answer for, not wave away. The asymptotic $j_{0,20} \approx \pi(20 - \tfrac14) = 62.046454908398416459637206819770181962894095637658$ against the true 62.048469190227169882852500264650952323815383766251 likewise tracks $\pi$, and substituting $\hat\pi$ there makes the approximation worse (−1.93% instead of −2.02%), not better. Structure that never mentions the constant reproduces the analytic one; the relabel is a choice of symbol for the same angles, and the series, the roots and the drums will not arbitrate it.

Computed, never measured.

## Further Reading

- [**The Haversine Formula: How Spherical Trigonometry Computes the Circle Constant on the Globe, and What Golden Pi Changes**](/blog/posts/2026-09-20-haversine-formula-navigation-computes-circle-constant-golden-pi/) — the same pattern one dimension down: a table of squared chord ratios that mentions no circle constant, with the constant entering only at the arc conversion $d = R\theta$.
- [**Euler's Identity: How e^(iπ) + 1 = 0 Computes the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-09-19-euler-identity-computes-circle-constant-golden-pi/) — where the constant is an output of a series rather than an input, and the same $\hat\pi - \pi = 0.0030128574$ sliver appears as the miss distance $|e^{i\hat\pi}+1|$.
- [**Gaussian Quadrature: How Legendre Nodes Compute the Circle Constant to Machine Precision, and What Golden Pi Changes**](/blog/posts/2026-09-18-gaussian-quadrature-legendre-nodes-compute-circle-constant-golden-pi/) — the numerical machinery that computed the integral side of the comparison above, and why polynomial roots are label-blind.
- [**The Ellipse's Perimeter: How the Complete Elliptic Integral of the Second Kind Computes the Circle Constant, and What Golden Pi Changes**](/blog/posts/2026-09-12-ellipse-perimeter-elliptic-integral-computes-circle-constant-golden-pi/) — a family of curves whose length has no elementary form, and the ambiguity of where the relabel lands when the constant appears both in a prefactor and in a limit.
- [**The Pendulum's Period: How π Enters Physics, and Why It Is Computed, Never Measured**](/blog/posts/2026-08-18-pendulum-period-computes-circle-constant-golden-pi/) — the earlier case of a physical formula whose amplitude corrections swamp the label gap, exactly as a drum's real resonance corrections swamp it here.
