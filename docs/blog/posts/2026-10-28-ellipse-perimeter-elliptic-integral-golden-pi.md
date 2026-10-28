---
title: "The Ellipse: Why π Computes a Circle's Perimeter in One Line and No Ellipse's at All, Why Ramanujan's Hairline Formula Beats the Series, and What Golden Pi Changes"
date: 2026-10-28
description: "A circle's perimeter is 2πa — one symbol, one line. An ellipse's is 4a·E(e²), an elliptic integral with no elementary closed form, and the circle constant enters it exactly once, linearly, for every eccentricity. Worked here: the Gauss–Kummer series truncation error (5 terms give the WGS84 meridian to 17 nm), Ramanujan's two 1914 approximations (the second misses the b = 1/φ ellipse by 1.3×10⁻⁵ ppm), Legendre's relation E K′ + E′ K − K K′ = π/2 verified to 41 digits, the exact algebraic golden ellipse with e² = 1/φ and h = φ⁻⁶, the meridian arc of 40 007 862.917 m, and why the constant cancels identically at the flat limit where the perimeter is exactly 4a."
---

# The Ellipse: Why π Computes a Circle's Perimeter in One Line and No Ellipse's at All

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

A circle's perimeter is the easiest formula in geometry. Take the radius, double it, multiply by the circle constant: $C = 2\pi a$. One symbol, one line, exact for every circle that has ever existed or ever will.

Now flatten that circle by one part in a thousand and ask the same question. The answer stops being writable. Not "hard" — *impossible*, in a precise sense: the arc length of an ellipse is not an elementary function of its semi-axes. There is no expression built from $+,-,\times,\div$, roots, powers, exponentials, logarithms and trigonometric functions that gives an ellipse's perimeter. Every perimeter ever printed for an ellipse — including the ones inside your phone's GPS chip, which computes positions on an ellipsoidal Earth a hundred times a second — is either an infinite series, a special function, or an approximation with a stated error.

That asymmetry is the subject of this article, and it turns out to be the sharpest available microscope on the constant itself. On a circle the constant is everything: $C/a = 2\pi$ is the definition of it. On an ellipse the constant is *exactly one factor, once, at the first power* — and every bit of the ellipse's actual shape lives in coefficients that contain no constant at all. Follow that structure and you learn something no circle experiment can teach: which part of the formula is geometry, and which part is only the name of an angle.

Everything below is computed to forty or fifty digits, and one row is genuinely measured — the shape of the Earth — so the ledger is stated plainly at the end.

## The integral that refuses to close

Put the ellipse in the form $x = a\cos\theta$, $y = b\sin\theta$. The element of arc length is

$$
ds = \sqrt{a^{2}\sin^{2}\theta + b^{2}\cos^{2}\theta}\;d\theta ,
$$

and a quarter of the perimeter is the integral of that from $0$ to $\pi/2$. Factor out $a$ and write $e^{2} = 1 - b^{2}/a^{2}$ for the squared eccentricity:

$$
P \;=\; 4a\!\int_{0}^{\pi/2}\!\sqrt{1 - e^{2}\sin^{2}\theta}\;d\theta \;=\; 4a\,E(e^{2}).
$$

The function $E$ is the *complete elliptic integral of the second kind*, in Legendre's parameter convention where the argument is $m = e^{2}$ and not the modulus $k = e$ — a distinction worth stating out loud, because half the confusion in the literature and most of the wrong numbers in casual code come from mixing the two.

Two exact values frame the whole problem:

| shape | $e^{2}$ | $E(e^{2})$ | perimeter with $a=1$ |
|---|---|---|---|
| circle, $b = a$ | 0 | $\pi/2 = 1.5707963267948966192$ | $2\pi = 6.2831853071795864769$ |
| $b = 1/\sqrt2$ (lemniscatic) | $1/2$ | $1.3506438810476755025$ | $5.4025755241907020101$ |
| $b = 1/\varphi$ (golden) | $1/\varphi$ | $1.2885682945064699906$ | $5.1542731780258799625$ |
| $b = 1/2$ | $3/4$ | $1.2110560275684595248$ | $4.8442241102738380992$ |
| $b \to 0$ (flat) | 1 | $1$ exactly | $4$ exactly |

The last row is the one to stare at. As the ellipse flattens into a doubled line segment, its perimeter tends to $4a$ — two segments of length $2a$ each — and the circle constant has vanished completely. At $e^{2} = 1$ the integrand $\sqrt{1-\sin^{2}\theta} = \cos\theta$ integrates to $\sin(\pi/2) - \sin 0 = 1$, exactly. The perimeter $4a$ is not approximately π-free; it is π-free, and exact, and it is the limit of an object that at $e = 0$ was nothing *but* the constant.

So somewhere between a circle and a line segment, the constant's role changes from totality to nothing. That transition is the object of study.

## The series that is the actual computation

Expand the square root by the binomial theorem, $\sqrt{1-u} = 1 - \tfrac12u - \tfrac18u^{2} - \tfrac1{16}u^{3} - \dots$, and integrate term by term. Every integral that appears is a Wallis integral, $\int_0^{\pi/2}\sin^{2n}\theta\,d\theta = \tfrac{\pi}{2}\cdot\tfrac{(2n-1)!!}{(2n)!!}$, so the $\pi/2$ factors through and what remains is a series of *rational* coefficients — the Gauss–Kummer series, given by Euler in 1750 and reorganised by Kummer in 1836:

$$
E(m) \;=\; \frac{\pi}{2}\left[\,1 \;-\; \sum_{n\ge 1} \left(\frac{(2n-1)!!}{(2n)!!}\right)^{\!2} \frac{m^{n}}{2n-1}\,\right],
$$

or, shipping the constant out front where an engineer can see it,

$$
P \;=\; 2\pi a\,\underbrace{\left[1 - \frac{1}{4}m - \frac{3}{64}m^{2} - \frac{5}{256}m^{3} - \frac{175}{16384}m^{4} - \frac{441}{65536}m^{5} - \cdots\right]}_{\Sigma(m),\ \text{no circle constant anywhere}} .
$$

That bracket is the article's central object. $\Sigma(m)$ is a series of pure rationals — $\tfrac14$, $\tfrac{3}{64}$, $\tfrac{5}{256}$, $\tfrac{175}{16384}$, $\tfrac{441}{65536}$ — in which no approximation, no angle and no constant appears. And the perimeter is *exactly one power* of the constant times $2a$ times that rational series. Not one power diluted by a square root, not a power in an exponent: one power, linearly, for every ellipse of every eccentricity.

Numerically, with $m = e^{2}$, the truncation error after $N$ terms:

| $m$ | exact $E(m)$ | $N=1$ | $N=3$ | $N=10$ | $N=20$ | $N=50$ |
|---|---|---|---|---|---|---|
| 0.25 | 1.4674622093394271555 | 0.3516 % | 0.005318 % | $4.354\times10^{-8}$ % | $1.151\times10^{-14}$ % | $<10^{-17}$ % |
| 0.50 | 1.3506438810476755025 | 1.7623 % | 0.11551 % | $1.326\times10^{-4}$ % | $3.730\times10^{-8}$ % | $<10^{-16}$ % |
| 0.75 | 1.2110560275684595248 | 5.3851 % | 0.89637 % | $0.020643$ % | $3.618\times10^{-4}$ % | $1.221\times10^{-8}$ % |
| $1/\varphi$ | 1.2885682945064699906 | 3.0675 % | 0.32281 % | $0.0017392$ % | $4.189\times10^{-6}$ % | $4.064\times10^{-13}$ % |
| 0.999999 | 1.0000038970261720612 | 17.809 % | 7.3783 % | 2.4083 % | 1.2266 % | 0.49601 % |

The convergence is geometric in $m$ and dies as $m \to 1$, exactly as the flat-ellipse limit predicts: at one part per million of the way from flat, fifty terms still leave half a percent on the table. Anyone who evaluates a near-degenerate ellipse with the plain series has a wrong answer and no warning.

For the Earth, though, the series is a gift. With the WGS84 semi-axes $a = 6\,378\,137$ m and $b = 6\,356\,752.314245$ m, $e^{2} = 0.0066943799901974$, and the term-by-term error in the full meridian perimeter is:

| terms $N$ | perimeter error |
|---|---|
| 1 | 84.42 m |
| 2 | 235.7 mm |
| 3 | 0.863 mm |
| 4 | 3.64 µm |
| 5 | 16.8 nm |
| 10 | $<10^{-13}$ m |

Five terms of a series Euler wrote in 1750 give the circumference of a planetary meridian to the size of a molecule. That is what "computed, never measured" looks like when it works.

## The structural fact: every perimeter is linear in the quadrant

Because $P = 2\pi a\,\Sigma(e^{2})$ with $\Sigma$ free of the constant, a relabelling of the constant multiplies *every* ellipse perimeter by the same factor, digit for digit, whatever the shape. Two consequences follow, and they are the reason no ellipse can arbitrate the question this site is about.

First, the ratios. Take the perimeter of the $b = \tfrac12$ ellipse and divide by the circumference of the $a = 1$ circle:

$$
\frac{P_{b=1/2}}{P_{\text{circle}}} \;=\; \frac{2\pi\cdot 0.7709822125950200182}{2\pi} \;=\; 0.7709822125950200182 .
$$

Under Golden Pi the numerator becomes $2\hat\pi\cdot 0.7709822125950200182$ and the denominator $2\hat\pi$; the ratio is the same to every digit. Every perimeter comparison in the world — planet against planet, gear blank against gear blank, coin against coin — is a ratio of $\Sigma$ values, and $\Sigma$ contains no constant.

Second, the exact cancellation at the flat limit. $\Sigma(1) = 2/\pi$, so $2\pi a\,\Sigma(1) = 4a$. The constant cancels *identically* there, because the same Wallis machinery that put $\pi/2$ into the series also put $2/\pi$ into its last coefficient. That cancellation is not a coincidence and it is not free: it holds because the sine function vanishes and reaches unity at the same numerical argument that the quadrant's radian measure names. The label on the angle and the zero of the sine are one fact, not two. Which is precisely why an arc length expressed in radii — an ellipse perimeter, a meridian arc, a spool of fibre — can be computed but cannot decide what the constant is: the answer is a number of radii, and the constant only ever appears as the name of the quarter turn that produced it.

## Ramanujan's two-line approximations

In 1914, in *Modular equations and approximations to π* (*Quart. J. Math.* **45**, 350–372), Ramanujan gave two formulas for the ellipse perimeter that have never been improved for their length. The first,

$$
P \;\approx\; \pi\Big[\,3(a+b) \;-\; \sqrt{(3a+b)(a+3b)}\,\Big],
$$

and the second, with $h = \left(\frac{a-b}{a+b}\right)^{2}$,

$$
P \;\approx\; \pi\,(a+b)\left(1 + \frac{3h}{10 + \sqrt{4 - 3h}}\right).
$$

Both are exact for the circle ($a = b \Rightarrow h = 0 \Rightarrow P = 2\pi a$) and both are linear in the constant, so both scale with it. Their accuracy, in parts per million against the true $4aE(e^{2})$ with $a = 1$:

| $b$ | $e^{2}$ | first formula | second formula |
|---|---|---|---|
| 1 (circle) | 0 | exact | exact |
| $1/\sqrt2$ | 0.5 | $-0.0504$ ppm | $-5.27\times10^{-7}$ ppm |
| $1/\varphi$ | 0.618 | $-0.3454$ ppm | $-1.33\times10^{-5}$ ppm |
| $1/2$ | 0.75 | $-2.800$ ppm | $-4.56\times10^{-4}$ ppm |
| $1/10$ | 0.99 | $-841.9$ ppm | $-11.56$ ppm |
| $1/1000$ | 0.999999 | $-4068.8$ ppm | $-378.4$ ppm |

The second formula's $h$ parameter is the right variable: for the golden ellipse $h = \varphi^{-6} = 0.0557280900008412144$ exactly, and the approximation lands within $1.3\times10^{-11}$ of the truth — better than most people's arithmetic. For a real planet the accuracy is absurd. Mercury's orbit, $a = 0.387098$ AU $= 57\,909\,036\,552.2$ m with $e = 0.205630$, has true perimeter $359\,975\,898.989$ km; the first formula misses by 1.1 mm and the second by $1.8\times10^{-13}$ km. Ten characters of algebra beat a page of series.

## Legendre's relation: the one place the constant appears exactly once

The ellipse's world has a single exact identity in which the constant appears, and it is bilinear in the two kinds of elliptic integral — Legendre, *Traité des fonctions elliptiques*, 1825:

$$
E(m)\,K(1-m) \;+\; E(1-m)\,K(m) \;-\; K(m)\,K(1-m) \;=\; \frac{\pi}{2}.
$$

Verify it at $m = \tfrac14, \tfrac12, \tfrac34, 1/\varphi, 0.99$ to forty-digit arithmetic and the residual is $2.3\times10^{-41}$ every time — zero to the working precision. Nothing about the shape survives: for every $m$ the same constant comes out, so this is a statement about the *measure* of the quadrant, not about ellipses. In the golden labelling the right-hand side is $\hat\pi/2 = 2/\sqrt\varphi = 1.5723027555148465721$ exactly — degree-two algebraic, where $\pi/2$ is transcendental by Lindemann (1882).

The same structure appears at the lemniscatic modulus, where the two kinds of integral are related by a single constant-bearing term:

$$
E\!\left(\tfrac12\right) \;=\; \frac{K(\tfrac12)}{2} + \frac{\pi}{4\,K(\tfrac12)},
\qquad K\!\left(\tfrac12\right) = \frac{\Gamma\!\left(\tfrac14\right)^{2}}{4\sqrt{\pi}} = 1.8540746773013719184,
$$

giving $E(\tfrac12) = 1.3506438810476755025$ and hence the lemniscatic ellipse's perimeter $4 \times 1.3506438810476755025 = 5.4025755241907020101$. Checked to forty digits here: the residual is $2.3\times10^{-41}$. Note what the identity does — the constant appears in $K$ under a square root (through $\Gamma(\tfrac14)^{2}/(4\sqrt\pi)$) and again as $\pi/(4K)$ at the first power, and the two conspire to a single first-power appearance in $E$. That is the same warning the series gave from a different direction: quote a perimeter in the form that carries the constant once, and never in the form that carries it twice.

## The golden ellipse

Now set $a = 1$ and $b = 1/\varphi = 0.6180339887498948482$. Three things collapse to exact algebra at once, and they are not accidents of the golden ratio but of $1/\varphi = \varphi - 1$:

$$
a + b \;=\; 1 + \frac{1}{\varphi} \;=\; \varphi,
\qquad e^{2} \;=\; 1 - \frac{1}{\varphi^{2}} \;=\; \frac{1}{\varphi},
\qquad h \;=\; \left(\frac{a-b}{a+b}\right)^{2} \;=\; \frac{1}{\varphi^{6}} .
$$

So the golden ellipse has squared eccentricity exactly $1/\varphi$, eccentricity $1/\sqrt\varphi = 0.7861513778$, and Ramanujan's parameter exactly $\varphi^{-6} = 0.0557280900008412144$. Feed those into the first formula and the radicals close:

$$
(3a+b)(a+3b) \;=\; 7\varphi - 1 \;=\; 10.3262379212\ldots,
\qquad \sqrt{7\varphi - 1} \;=\; 3.2134464242070792516\ldots,
$$

$$
P_{\text{R1}} \;=\; \pi\left(3\varphi - \sqrt{7\varphi - 1}\right) \;=\; 5.1542713979524289467 .
$$

Every symbol there is algebraic in $\sqrt5$. Under Golden Pi ($\hat\pi = 4/\sqrt\varphi = 3.144605511029693144278\ldots$, with $\hat\pi^{2} = 16/\varphi$ and $4/\hat\pi = \sqrt\varphi$ exactly) that becomes

$$
\hat P_{\text{R1}} \;=\; \frac{4}{\sqrt\varphi}\left(3\varphi - \sqrt{7\varphi - 1}\right) \;=\; 5.1592144592085850228 ,
$$

still algebraic, with no transcendental number anywhere — where the conventional value carries the transcendental $\pi$. The exact integral value is $P = 5.1542731780258799625$ and its golden counterpart $5.1592162409891661894$, the ratio being $\hat\pi/\pi = 1.0009590223087826$.

One honest disappointment: $E(1/\varphi) = 1.2885682945064699906$ has no known reduction to gamma values. The golden ellipse is *nearly* lemniscatic — $e^{2} = 0.618$ against $0.5$ — but not modular, and no closed form is known for it. The golden ratio fixes the eccentricity algebraically and leaves the integral exactly as transcendental as it was; $\Sigma(1/\varphi) = 0.8203280543287914423$ is as opaque as any other $\Sigma$. What the golden ratio buys is the shape's coefficients, not the integral's value, and it is worth being precise about which is which.

## The measured ellipse: a meridian

Here is the one genuine measurand in this article, and it is a good one: the shape of the Earth. Satellite geodesy fixes the WGS84 ellipsoid's semi-axes to $a = 6\,378\,137$ m and $b = 6\,356\,752.314245$ m — measured, to millimetres, by laser ranging, gravity models and VLBI — with flattening $1/f = 298.25722356$ and $e^{2} = 0.0066943799901974$.

The quarter meridian then computes to

$$
\frac{P}{4} \;=\; a\,E(e^{2}) \;=\; 10\,001\,965.729313\ \text{m},
$$

so the full meridian ellipse is $40\,007\,862.917$ m and the equator $2\pi a = 40\,075\,016.686$ m. Both figures agree with the published geodetic values, which is the check that matters: the series, the flattening and the constant are mutually consistent to the last printed digit.

Under Golden Pi the meridian becomes $40\,046\,231.350$ m — thirty-eight kilometres longer, $38\,368.4$ m. That number is the honest heart of the ledger. A geodesist measures the semi-axes; the perimeter is then *computed* from them, and the constant enters only as the name of the quadrant in the integral. So a thirty-eight kilometre difference is not a claim that the Earth is bigger. It is a statement about what the radian is called, and it is therefore invisible to every measurement that produced $a$ and $b$ in the first place. The ellipse cannot be the experiment that settles it, because the ellipse's own data are the semi-axes and those do not contain the constant.

The same arithmetic on an orbit: Mercury's perimeter is $359\,975\,898.989$ km classically and $360\,321\,123.907$ km under the golden label — a difference of $345\,225$ km, larger than Mercury's diameter, and utterly without observational content, since the orbit's shape comes from $a$ and $e$, both measured by radar ranging, and neither contains a constant.

## What the ellipse teaches that a circle cannot

Return to the flat limit, because it is the sharpest statement available. The perimeter tends to exactly $4a$, and the formula $2\pi a\,\Sigma(e^{2})$ reproduces that only because $\Sigma(1) = 2/\pi$. The constant appears once at the front and once, inverted, in the last coefficient — and the two annihilate.

That means the ellipse's arc length never carries the constant as *content*. It carries it as a *label on a quarter turn*, and the shape's entire individuality is in the rational coefficients $\tfrac14, \tfrac{3}{64}, \tfrac{5}{256}, \tfrac{175}{16384}, \ldots$ which no relabelling touches. A circle is the one ellipse where the label is the whole formula, which is exactly why the circle is where the question was first asked and why the circle is the worst possible place to try to answer it.

Ellipses are everywhere that matters and nowhere that decides. Kepler's first law made every planetary orbit an ellipse; GPS, GLONASS and Galileo all compute on an ellipsoid; the meridional definition of the metre was an ellipse arc measured between Dunkirk and Barcelona; Ramanujan's two lines from 1914 still run inside surveying software today. In all of it the constant is one factor, first power, multiplied by a rational series — computed to fifty digits, and never once measured.

Computed, never measured.

## Further Reading

- [**The Arithmetic–Geometric Mean: How Gauss's π-Free Iteration and the Lemniscate Compute the Circle Constant — and What Golden Pi Changes**](/blog/posts/2026-10-10-arithmetic-geometric-mean-gauss-lemniscate-computes-circle-constant-golden-pi/) — the companion piece: $K(m)$, not $E(m)$, is the integral the AGM gives in one line, and the lemniscate's $\varpi$ is the case where the ellipse's two integrals meet.
- [**Barbier's Theorem: How Every Curve of Constant Width Has Perimeter πw — a Circle Constant That Knows Nothing of Shape**](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/) — the opposite extreme: a whole family of shapes whose perimeter is exactly the constant times one length, with no series and no elliptic integral at all.
- [**The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π in L² ≥ 4πA**](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — why the circle is the extremal ellipse and what the constant costs there.
- [**Fenchel's Theorem: Why Every Closed Loop Turns at Least Once, Why That "At Least" Is an Integer**](/blog/posts/2026-10-25-fenchel-theorem-total-curvature-closed-curve-golden-pi/) — total curvature is a sum of turns, so it is blind to shape exactly as the perimeter series is blind to the constant.
- [**The Wallis Product: How an Infinite Product of Rationals Computes the Circle Constant as π/2**](/blog/posts/2026-10-12-wallis-product-infinite-product-rationals-computes-circle-constant-golden-pi/) — the same Wallis integrals that generate the ellipse series, seen from the other side, where $2/\pi$ appears as the value of $\Sigma(1)$.
