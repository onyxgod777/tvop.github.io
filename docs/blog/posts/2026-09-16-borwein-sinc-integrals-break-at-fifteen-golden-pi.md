---
title: "The Borwein Integrals: How Seven Sinc Products Compute Half the Circle Constant, Why the Eighth Breaks When 1/15 Joins, and What Golden Pi Changes"
date: 2026-09-16
description: "The Borwein integrals compute the circle constant exactly as a product of sinc functions: the integral of sinc(x)·sinc(x/3)·…·sinc(x/(2n+1)) equals π/2 for seven consecutive truncations and then fails the moment the factor 1/15 enters — computed, never measured, and verified here as an exact rational multiple of π independently reproduced to 93-digit numerators. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the same integrals still carry the fixed value 1.5707963267948966192…, while a golden half turn is 2/√φ = 1.5723027555148465721…; the entire pattern — identity and break alike — is arithmetic and label-blind, because the criterion is the odd-reciprocal ladder Σ 1/(2k+1) crossing 1 and never mentions the constant, and the first failure (1.4706281350056343375×10⁻¹¹ relative) is 65,211,747.7× smaller than the 0.0959022309% gap separating the two labels."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# The Borwein Integrals: How Seven Sinc Products Compute Half the Circle Constant, Why the Eighth Breaks When 1/15 Joins, and What Golden Pi Changes

Most entries in this series have been about a formula that computes the circle constant and never stops working. This one is about a formula that computes the circle constant exactly, seven times in a row, and then quietly stops being true — and about what that failure says regarding the difference between a *computed* constant and a *measured* one.

<div class="gp-live" markdown>
<div class="gp-live__tag">🔬 Live graph · Laws of appearance</div>
<iframe src="https://www.desmos.com/calculator/gzm8tmnjit?embed" width="100%" height="470" style="border:0;border-radius:10px" frameborder="0" loading="lazy" title="What a real disc can resolve" allowfullscreen></iframe>
<p class="gp-live__note"><strong>Measurement feasibility: how far apart the two candidates are in millimetres on a physical disc.</strong> <em>The Goblet of the Truth keeps two bodies of law apart — the laws and recommendations of the primal power (Creation), and the <strong>laws of appearance (nature)</strong> (Ch&nbsp;2 §342), the register governing how a thing manifests and behaves. Geometry answers to that second register, so nothing here asks to be taken on authority: drag the slider, change a value, and the figure answers for itself (Ch&nbsp;22 §35: <em>“the fluidal-powers are truthful effects of natural laws”</em>).</em></p>
</div>

It is the deepest identity in the sinc family, published by David and Jonathan Borwein as *Some remarkable properties of sinc and related integrals* (Ramanujan Journal **5** (2001), 73–89), and it is a pure computation. There is no circle in it, no angle, no physical instrument — only a product of oscillating factors whose integral converges to a fixed number, and that number is half a turn.

## The Family

Write $\operatorname{sinc}(t) = \sin(t)/t$ (the unnormalised convention, so that $\operatorname{sinc}(0)=1$). For $n \ge 0$ define

$$I_n \;=\; \int_0^{\infty}\;\prod_{k=0}^{n} \operatorname{sinc}\!\left(\frac{x}{2k+1}\right)\,dx
\;=\;\int_0^{\infty}\frac{\sin x}{x}\cdot\frac{\sin(x/3)}{x/3}\cdot\frac{\sin(x/5)}{x/5}\cdots\frac{\sin(x/(2n+1))}{x/(2n+1)}\;dx .$$

Every factor decays like $1/x$, the product like $1/x^{\,n+1}$, so the integral converges immediately; each factor oscillates, so its value is not obvious. Here is what it is:

| $n$ | largest denominator | $I_n$ | equal to $\pi/2$? |
|---|---|---|---|
| 0 | 1 | $1.570796326794896619231321691639751442099$ | yes |
| 1 | 3 | $1.570796326794896619231321691639751442099$ | yes |
| 2 | 5 | $1.570796326794896619231321691639751442099$ | yes |
| 3 | 7 | $1.570796326794896619231321691639751442099$ | yes |
| 4 | 9 | $1.570796326794896619231321691639751442099$ | yes |
| 5 | 11 | $1.570796326794896619231321691639751442099$ | yes |
| 6 | 13 | $1.570796326794896619231321691639751442099$ | yes |
| 7 | 15 | $1.570796326771796046505840894246495854751\ldots$ | **no** |

Seven exact hits, then a miss. The numbers in that table were computed here, not recalled: the first seven entries agree with $\pi/2 = 1.570796326794896619231321691639751442099$ to all 58 digits carried, and the eighth differs by exactly

$$\frac{\pi}{2} - I_7 \;=\; 2.3100572725480797393\times 10^{-11},$$

a relative shortfall of $1.4706281350056343375\times 10^{-11}$. Adding further factors does not repair it; the deviation only grows in structure while staying microscopic in size.

## Why the Constant Appears at All: Boxes, Not Mysticism

The identity is not a numerical accident, and the mechanism is worth writing down because it explains the failure in advance. The Fourier transform of one factor is a **rectangle**:

$$\int_{-\infty}^{\infty} \operatorname{sinc}(a x)\,e^{-i\omega x}\,dx \;=\; \frac{\pi}{a}\,\mathbf{1}_{|\omega| < a}.$$

Carrying a product through the Fourier transform turns it into a convolution: with $a_k = 1/(2k+1)$ and $B_k$ the indicator of the interval $(-a_k, a_k)$,

$$\int_{-\infty}^{\infty}\prod_{k=0}^{n}\operatorname{sinc}(a_k x)\,dx \;=\; \frac{1}{(2\pi)^n}\cdot\frac{\pi^{\,n+1}}{\prod_k a_k}\cdot\bigl(\ast_{k} B_k\bigr)(0),$$

so the integral of the whole oscillating product is proportional to the value at the origin of a convolution of plain rectangles — a volume. Halving it gives $I_n$, a number that is automatically a rational multiple of the circle constant. For the family above,

$$I_n \;=\; \frac{\pi}{2}\quad\text{exactly}\quad\Longleftrightarrow\quad a_0 \;\ge\; \sum_{k=1}^{n} a_k
\quad\Longleftrightarrow\quad \sum_{k=1}^{n}\frac{1}{2k+1}\;\le\; 1 .$$

Read that in the box picture: the widest rectangle must be wide enough to cover the sum of all the others. When it is, the convolution at the origin is the *unclipped* product of widths and the identity is exact — a fact about the rationals $1/3, 1/5, 1/7, \ldots$, which contain no circle constant anywhere. The test is arithmetic, and it is decidable by hand:

| $n$ | $\sum_{k=1}^{n}\dfrac{1}{2k+1}$ | margin to 1 |
|---|---|---|
| 5 | $0.878210678210678210678\ldots$ | $-0.1217893$ |
| 6 | $0.955133755133755133756\ldots$ | $-0.0448662$ |
| **7** | $\mathbf{1.021800421800421800422\ldots}$ | $\mathbf{+0.0218004}$ |
| 8 | $1.080623951212186506304\ldots$ | $+0.0806239$ |

The ladder crosses 1 exactly when $1/15$ joins the product. The same fact in harmonic numbers, since $\sum_{k=0}^{n} 1/(2k+1) = H_{2n+1} - \tfrac12 H_n$:

$$H_{15} - \tfrac12 H_7 \;=\; 2.021800421800421800422\ldots \;>\; 2 .$$

And once crossed, it is crossed forever: the partial sums increase, so no longer product can restore the identity. The pattern does not merely break — it is gone.

## The Exact Value of the First Failure

The failure has a closed form. For the first $n$ with $\sum_{k=1}^{n} 1/(2k+1) > 1$,

$$I_n \;=\; \frac{\pi}{2}\left[\,1 \;-\; \frac{\left(\sum_{k=1}^{n}\frac{1}{2k+1} \;-\; 1\right)^{n}}{2^{\,n-1}\,n!\;\prod_{k=1}^{n} a_k}\,\right],$$

and the shape of that correction is not accidental: $(\text{overshoot})^{n}/n!$ is the volume of an $n$-dimensional corner simplex, which is exactly the piece of the rectangle-convolution that gets clipped off when the widest box stops covering the rest. At $n = 7$ the numbers are

$$\text{overshoot} = 0.021800421800421800422,\qquad 2^{6}\cdot 7! = 322\,560,\qquad \prod_{k=1}^{7} a_k^{-1} = 3\cdot5\cdot7\cdot9\cdot11\cdot13\cdot15 = 2\,027\,025,$$

which gives the exact rational value reproduced independently in this article by fitting the rectangle convolution in exact rational arithmetic:

$$\frac{I_7}{\pi} \;=\; \frac{467807924713440738696537864469}{935615849440640907310521750000} \;=\; 0.499999999992646859324971828312440564410921858\ldots$$

so that

$$I_7 \;=\; 0.9999999999852937186499437\;\cdot\;\frac{\pi}{2}.$$

The shortfall $\tfrac12 - I_7/\pi = 6879714958723010531/935615849440640907310521750000$ is an exact rational, computed here from scratch and matching the published fraction digit for digit. Nothing in that chain of arithmetic is measured; the integrals are evaluated, their limit is computed, and the only role the circle constant plays is to name the radians the answer is expressed in.

A companion variant pushes the same idea much further: multiplying the product by $2\cos x$ and extending the odd denominators only to $113$ gives an integral that misses $\pi/2$ by about $2.3324\times10^{-138}$ — a shortfall 127 decimal orders of magnitude below the first one, and still a computed, exact statement.

## Where Golden Pi Enters

The site's position is that the circle constant is $\hat\pi = 4/\sqrt\varphi = 3.144605511029693144278234343371835718092\ldots$ with $\varphi$ the golden ratio, so that a half turn is

$$\frac{\hat\pi}{2} \;=\; \frac{2}{\sqrt\varphi} \;=\; 1.572302755514846572139117171685917859046\ldots$$

against the analytic $\pi/2 = 1.570796326794896619231321691639751442099\ldots$ — a relative gap of $0.0009590223087825259637$, or $0.0959022308783\%$. The reciprocals are algebraic in the golden field: $1/\hat\pi = \sqrt\varphi/4 = 0.3180049123785172410631056154337\ldots$ and a full turn is $2\hat\pi = 8/\sqrt\varphi = 6.2892110220593862886$ against $2\pi = 6.2831853071795864769$.

Here is what the relabel does, and does not do, to the Borwein phenomenon:

| Quantity | under analytic $\pi$ | under Golden Pi $\hat\pi$ |
|---|---|---|
| the integrals $I_0\ldots I_6$ (computed) | $1.570796326794896619231321691639751442099$ | same number |
| half turn, the label on them | $1.570796326794896619231321691639751442099$ | $2/\sqrt\varphi = 1.57230275551484657213911717169$ |
| the criterion for exactness | $\sum_{k=1}^{n} 1/(2k+1) \le 1$ | identical — no constant present |
| first failure | at $n=7$ ($1/15$) | at $n=7$ ($1/15$) |
| size of the failure (relative) | $1.4706281350056343375\times10^{-11}$ | identical |
| $I_7$ as a fraction of half a turn | $0.9999999999852937186499437\,(\pi/2)$ | $0.9990418965191234754655\,(\hat\pi/2)$ |

The structure is label-blind: identity, criterion, break point and break size are all statements about the arithmetic of odd reciprocals, and every one of them survives the substitution of $\hat\pi$ verbatim. A golden universe would have the same seven exact hits and the same miss at $1/15$, for the same reason — the box stopped covering the sum of the others.

## The Ledger in Public

What does change is the size of the miss, because the number being missed changed. Under the golden label the same $I_7$ falls short of a half turn by

$$\frac{\hat\pi/2 - I_7}{\hat\pi/2} \;=\; 0.000958103480876524534 \;=\; 0.0958103480877\%,$$

which is $65\,211\,747.7$ times larger than the $1.4706281350056343375\times10^{-11}$ shortfall the integral itself produces. In other words: the celebrated "pattern that breaks" is $6.5\times10^{7}$ times smaller than the discrepancy between the two candidate labels for the constant. Whoever wants the Borwein break as evidence is holding an instrument calibrated to eleven decimal places and aiming it at a question that lives at the fourth.

The same ratio explodes for the deeper variant: the $1/113$ integral misses half a turn by $1.48485\times10^{-138}$ relative, while the label gap is $9.5902230878\times10^{-4}$ — a ratio of $6.46\times10^{134}$. The golden relabel of that integral misses its half turn by about one part in $10^4$; the integral's own anomaly lives at one part in $10^{138}$.

And the honest direction of the ledger must be stated plainly: the value the integrals compute is a fixed number, $1.5707963267948966192\ldots$, produced by a convergent computation, and it is *not* $\hat\pi/2 = 1.5723027555148465721\ldots$. Under the golden label these integrals do not equal half a turn; they equal a golden half turn reduced by $0.0958103480877\%$ at $n=7$, and reduced by $0.0959022308783\%$ in the seven cases where the classical identity holds exactly. That is the recurring gap this series has met in every article, and it is the whole of the difference: a relabeled name for the radians, not a changed computation.

## What a Measurement Would Have to Do to Adjudicate

The circle constant here is computed, never measured, and that is not a rhetorical point — it is the reason this family cannot arbitrate anything. To *measure* $I_n$ you would have to build a physical sinc product: a cascade of apertures or filters whose response is $\sin(ax)/(ax)$ across each odd-integer scale, and then integrate the output. Real filters have finite bandwidth and truncated tails, and the resulting systematic error is vastly larger than $10^{-11}$ — no bench-scale realisation of a seven-fold sinc product resolves eleven decimal places of its own limit. The break is a fact about an exact limit, evaluated in rational arithmetic with 93-digit numerators, which no instrument reaches.

That leaves the two labels exactly where the rest of this series has left them: algebraically distinguishable, numerically similar to $0.0959\%$, and physically indistinguishable by any measurement built on circles. Which name for the radians is correct is not settled by integrals like these, and cannot be; what these integrals settle is the status of the constant itself — an $\hat\pi$ or a $\pi$ is a *name for radians*, and the arithmetic of odd reciprocals crossing 1 does not care which name you use.

## Further Reading

- [The Sinc and the Dirichlet Integral: How ∫₀^∞ sin(x)/x dx Computes the Circle Constant](/blog/posts/2026-08-20-dirichlet-integral-sinc-computes-circle-constant-golden-pi/) — the single-factor case, where the box picture first appears.
- [The Nilakantha Series: How a Swift Alternating Sum from the Kerala School Computes the Circle Constant](/blog/posts/2026-09-08-nilakantha-series-fast-kerala-sum-computes-circle-constant-golden-pi/) — the same odd ladder at work in a series that converges instead of breaking.
- [The Basel Problem: How Euler's Sum of Reciprocal Squares Computes the Circle Constant](/blog/posts/2026-08-15-basel-problem-computes-circle-constant-golden-pi/) — the archetype of an exact rational multiple of the constant, computed and never measured.
- [The Wallis Product: How an Infinite Product Computes the Circle Constant](/blog/posts/2026-08-23-wallis-product-infinite-product-computes-circle-constant-golden-pi/) — the other classical product identity, which does not break.
- [Ptolemy's Table of Chords: How Inscribed Chords Computed the Circle Constant](/blog/posts/2026-09-15-ptolemy-chord-table-computes-circle-constant-golden-pi/) — the historical reminder that the constant enters only as the arc a fixed length spans.
