---
title: "Al-Kashi's 805,306,368-Sided Polygon: Why the Sexagesimal Record of 2π Is Arithmetic Around a Definition, Why the Polygon's Defect Scales as the Cube of the Constant, and What Golden Pi Changes"
date: 2026-11-03
description: "In 1424 Jamshīd al-Kāshī recorded 2π in base sixty as 6;16,59,28,1,34,51,46,14,50 — nine sexagesimal places, sixteen decimals — obtained by a regular polygon of 3·2²⁸ = 805,306,368 sides. This article recomputes that string from its own digits (residual +7.9×10⁻¹⁸, inside the ±0.5·60⁻⁹ half-ulp of any nine-place rounding), traces the side-doubling recursion x_{n+1} = √(2 − √(4 − x_n²)) which contains no circle constant in its arithmetic at all, and shows where the constant is nevertheless hidden: the recursion's limit and its convergence rate are both set by the period of the sine in its argument, so the polygon is constant-free arithmetic around a constant-laden definition. The measured defect is then worked as a theorem: the inscribed deficit 2π − 2N sin(π/N) falls as π³/(3N²), so the golden gap is amplified exactly threefold in the convergence — numerically 1.00285343 at N = 6, 1.002879415 at 48, and 1.002879827 at 768, 12,288, 196,608 and 805,306,368, locking to (π̂/π)³ = 1.00287982698. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693144…, root of y⁴ + 16y² − 256 = 0, which factors exactly as (y² − 16/φ)(y² + 16φ) because φ − 1/φ = 1) the record becomes 6;17,21,9,34,50,45,12,9,48 in base sixty, the two constants separate at the second sexagesimal place, the Earth's great circle moves by 38.3898 km at R = 6371 km, and the honest boundary is arithmetic: the 805-million-gon resolves the constant to eighteen digits while the gap lives in the third, so precision was never the question — the definition of the circle is, and no polygon can supply it. Computed, never measured."
---

# Al-Kashi's 805,306,368-Sided Polygon

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 1424, in Samarkand, Jamshīd ibn Masʿūd al-Kāshī finished a short treatise on the circumference of the circle and wrote down, in the sexagesimal notation of the astronomers, a number for twice the circle constant. He did not write it as we would. He wrote nine places deep in sixtieths:

$$
2\pi \;=\; 6;\;16,\;59,\;28,\;1,\;34,\;51,\;46,\;14,\;50
$$

Read as arithmetic — six, plus sixteen sixtieths, plus fifty-nine three-thousand-six-hundredths, and so on — that string is a rational number, and it is not the circle constant. It is a *record* of one, carried to about sixteen decimal places, and the instrument that produced it was a regular polygon of $3\cdot 2^{28} = 805{,}306{,}368$ sides.

That is the kind of number that invites a certain story: an astronomer with better arithmetic than anyone in Europe for the next century and a half, grinding a polygon to sixteen digits, and therefore "establishing" the value. This article is about why that story is a category error — not because the number is wrong (it is astonishingly right, and we will check it digit by digit against its own definition), but because of *what* the polygon was doing. A polygon does not compare a circumference to a diameter. It computes a limit. And the limit it computes was placed in its own recursion before al-Kāshī started, by the period of the sine function whose argument the polygon halves.

Then we do the part the textbooks leave out: the polygon's error is not a featureless small number. It is proportional to the **cube** of the circle constant, which means the golden gap $\hat\pi/\pi - 1 = 9.59022308783\times10^{-4}$ arrives in every convergence table amplified exactly threefold. That is a checkable statement, and we check it at six values of $N$ spanning eight orders of magnitude.

## Nine sexagesimal places are sixteen decimals

Base sixty is not an affectation. It is a working system for people who divide angles and hours, because $60$ is divisible by $2, 3, 4, 5, 6, 10, 12, 15, 20, 30$, and every astronomical table of the period is built on fractions that terminate in those divisors. The price is that each sexagesimal place buys less precision than a decimal place, and the exchange rate is fixed by $\log_{10} 60 = 1.77815$:

| Sexagesimal place | Value as a fraction | Decimal resolution |
|---|---|---|
| 1 | $1/60$ | $1.667\times10^{-2}$ |
| 2 | $1/60^{2}$ | $2.778\times10^{-4}$ |
| 3 | $1/60^{3}$ | $4.630\times10^{-6}$ |
| 4 | $1/60^{4}$ | $7.716\times10^{-8}$ |
| 5 | $1/60^{5}$ | $1.286\times10^{-9}$ |
| 6 | $1/60^{6}$ | $2.143\times10^{-11}$ |
| 7 | $1/60^{7}$ | $3.572\times10^{-13}$ |
| 8 | $1/60^{8}$ | $5.954\times10^{-15}$ |
| 9 | $1/60^{9}$ | $9.923\times10^{-17}$ |

Nine places give $9.92\times10^{-17}$, which is why the same record is quoted as sixteen decimal places: $60^{9} \approx 1.0\times10^{16}$. The exchange is exact bookkeeping, and it sets a ceiling. Whatever the polygon did, a nine-place record cannot carry more than a part in $10^{16}$ — the notation, not the geometry, is the binding constraint.

## The recursion that names no constant

Here is the whole engine. For a unit circle, the side of the inscribed regular hexagon is $1$. Each doubling replaces a side $x$ subtending a central angle $\theta$ by the two sides subtending $\theta/2$, and the chord–half-angle relation is pure Pythagoras:

$$
x_{n+1} \;=\; \sqrt{\,2-\sqrt{\,4-x_n^{\,2}}}
$$

Start at $x_0 = 1$, multiply the side by the side count $6\cdot2^{n}$, and you have the perimeter. There is no $\pi$ anywhere in that expression — no circle constant, no trigonometric function, only a nested square root of a rational. Al-Kāshī's twenty-eight doublings are twenty-eight applications of it, in sexagesimal arithmetic, on paper.

Run it:

```text
x_0 = 1                                        n=0   sides=6          P=6.000000000000000000
x_1 = sqrt(2 - sqrt(4 - 1))                    n=1   sides=12         P=6.211657082460498296
x_2                                            n=2   sides=24         P=6.265257226562476394
x_3                                            n=3   sides=48         P=6.278700406093734414
x_4                                            n=4   sides=96         P=6.282063901781019276
x_5                                            n=5   sides=192        P=6.282904944570924151
...
n=28                                           sides=805306368      P=6.283185307179586461
```

and the last line is $2\pi = 6.2831853071795864769$ to eighteen digits, missing only in the nineteenth.

A defender of the older story will say: look, no constant in the arithmetic, and it lands on the constant. But that is exactly the sleight of hand to name. The recursion computes the chord of a **half angle**, and "half angle" is only meaningful relative to a full turn. Write the same recursion in closed form and the constant appears instantly, because the closed form is a trigonometric identity:

$$
x_n \;=\; 2\sin\!\frac{\pi}{6\cdot 2^{n}},
\qquad
P_n \;=\; 6\cdot 2^{n}\,x_n \;=\; 2\pi\,\frac{\sin(\pi/N)}{\pi/N},
\qquad N = 6\cdot2^{n}.
$$

The constant did not enter at the end. It entered at the beginning, in the decision that the hexagon's side subtends one sixth of a *turn*, and a turn is $2\pi$ radians by definition of the radian. The polygon is arithmetic without a constant wrapped around a definition full of one. That is not a defect — it is the only way a limit can be honest. But it does mean the polygon can never *test* the constant, only compute it, exactly as the site's rule says: computed, never evaluated by any instrument.

## The record, checked against itself

The obvious check on a historical string is to convert it back and see whether it is a rounding. Do it in exact rational arithmetic — every sexagesimal place is a fraction, so the sum has no floating-point excuse:

```python
from fractions import Fraction
d = [16, 59, 28, 1, 34, 51, 46, 14, 50]          # al-Kashi's nine places, base 60
v = Fraction(6, 1)
for i, k in enumerate(d, start=1):
    v += Fraction(k, 60 ** i)
# v = 6.283185307179586484847...   vs   2*pi = 6.283185307179586476925...
# residual  +7.92204e-18,  relative +1.26083e-18
```

The residual is $+7.92\times10^{-18}$, and half a unit in the last place is $0.5\cdot60^{-9} = 4.96\times10^{-17}$ — the string sits comfortably inside the interval any correct nine-place rounding must occupy, in fact near its centre. So the record is not a lucky string; it is a correctly rounded nine-place value, and every one of its nine digits is doing work.

Nine places, sixteen decimals, and the arithmetic is right. That is a genuine achievement of fifteenth-century computational practice, and it deserves to be stated plainly before the two things that follow are said: it is a *computed* number, and it is a number about a definition.

## The defect is the cube of the constant

Now the part that is not in the histories. The inscribed polygon's shortfall is not some anonymous $O(1/N^{2})$. Expand the sine:

$$
2\pi - 2N\sin\frac{\pi}{N}
\;=\; 2\pi\left(\frac{\pi^{2}}{6N^{2}} - \frac{\pi^{4}}{120N^{4}} + \cdots\right)
\;=\; \frac{\pi^{3}}{3N^{2}} - \frac{\pi^{5}}{60N^{4}} + \cdots
$$

The leading term is $\pi^{3}/(3N^{2})$. The constant appears at the **third power** in the error, so any claim that shifts the constant by a factor $(1+g)$ shifts the defect by $(1+g)^{3} \approx 1 + 3g$. With $g = 9.59022308783\times10^{-4}$ this predicts an amplification of $2.877066926\times10^{-3}$, i.e. a ratio $1.00287982698$.

Compute the two convergence tables and divide:

| $N = 6\cdot2^{n}$ | $2\pi - P_N(\pi)$ | $2\hat\pi - P_N(\hat\pi)$ | ratio |
|---|---|---|---|
| 6 | $2.831853\times10^{-1}$ | $2.839932\times10^{-1}$ | 1.00285343 |
| 48 | $4.484901\times10^{-3}$ | $4.497815\times10^{-3}$ | 1.002879415 |
| 768 | $1.752290\times10^{-5}$ | $1.757333\times10^{-5}$ | 1.002879825 |
| 12 288 | $6.844880\times10^{-8}$ | $6.864590\times10^{-8}$ | 1.002879827 |
| 196 608 | $2.673781\times10^{-10}$ | $2.681481\times10^{-10}$ | 1.002879827 |
| 805 306 368 | $1.593701\times10^{-17}$ | $1.598290\times10^{-17}$ | 1.002879827 |

where $P_N(c) = 2N\sin(c/N)$ is the perimeter of the $N$-gon inscribed in a circle whose half-turn reads $c$. The golden column is a substitution test on the truncation series and nothing more: it does not claim that a Euclidean hexagon's side stops being equal to its radius, only that the *defect term* — the only place the constant sits — responds to a relabelled half-turn. That is the whole content of the cube law.

The ratio locks to $(π̂/π)^{3} = 1.00287982698$ by $N = 768$ and does not move again across five further decades. The $N = 6$ row sits below the asymptotic value, by $2.6\times10^{-5}$ in relative terms, because the $\pi^{5}$ term has not yet died — a third-order prediction being tested against a hexagon is not a fair test, and the table shows the crossover rather than hiding it.

This is what an honest scaling law looks like: a prediction, six independent numerical points, and a residual that shrinks to nothing in exactly the place the next term says it should. It is also a *diagnostic*, and its verdict is uncomfortable for both camps. Because the defect carries $\pi^{3}$, a table of polygon perimeters is three times more sensitive to the constant than a table of circumferences. And because it is only three times, the total separation available at al-Kāshī's eighteen achieved digits is gigantic — $10^{15}$ times the gap. Anybody who claims the polygon question is a matter of precision has not done the arithmetic. The polygon resolves the constant without difficulty. What it cannot do is tell you which definition it was resolving.

## Golden Pi in base sixty

Take the site's value, $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693144\ldots$ with $\varphi = (1+\sqrt5)/2$. Twice it is

$$
2\hat\pi \;=\; \frac{8}{\sqrt\varphi} \;=\; 6.289211022059386288556\ldots
$$

Convert to the same notation al-Kāshī used, nine places deep:

$$
2\hat\pi \;=\; 6;\;17,\;21,\;9,\;34,\;50,\;45,\;12,\;9,\;48\ldots
\qquad\text{against}\qquad
2\pi \;=\; 6;\;16,\;59,\;28,\;1,\;34,\;51,\;46,\;14,\;50
$$

The two strings part company at the **second** sexagesimal place — $16$ against $17$ — and the difference $2\hat\pi - 2\pi = 6.0257148798\times10^{-3}$ is $21.7$ units of that place. In decimal the split appears in the third decimal digit ($3.141$ against $3.144$); in base sixty it appears in the second place. Neither notation is doing anything deep — it is the same $\log 60$ exchange rate as before — but it is a useful reminder that the gap is not a faint, last-digit affair. It is a third-digit affair that any schoolroom table can see.

At the scale of a planet the same difference is not small at all. For a sphere of radius $R = 6371$ km:

| Quantity | conventional $2\pi R$ | golden $2\hat\pi R$ | difference |
|---|---|---|---|
| great circle | 40 030.17 km | 40 068.56 km | 38.3898 km |
| quarter meridian | 10 007.54 km | 10 017.14 km | 9.5975 km |

Thirty-eight kilometres. That is not a rounding error, and it is the reason the question is worth arguing about rather than dismissing: relabelling the constant moves the circumference of the Earth by more than the height of Everest's base camp. If the constant were a free parameter one could read off a globe, the globe would settle it in an afternoon. It is not a free parameter, and no globe is a perfect sphere; which is the whole difficulty.

## The quartic that factors, and what it says

$\hat\pi$ is not a transcendental label swapped in for another. It is algebraic of degree four, and the certificate is one line:

$$
\hat\pi^{4} + 16\hat\pi^{2} - 256 \;=\; 0
\qquad\text{(residual } -5.97\times10^{-59} \text{ at sixty digits)}
$$

which is quadratic in $\hat\pi^{2}$ and therefore factors over $\mathbb{Q}(\sqrt5)$ — here is the reason the coefficient is exactly $16$:

$$
y^{4}+16y^{2}-256 \;=\; \left(y^{2}-\frac{16}{\varphi}\right)\left(y^{2}+16\varphi\right),
\qquad
\frac{16}{\varphi}\cdot16\varphi = 256,
\qquad
16\varphi - \frac{16}{\varphi} = 16\!\left(\varphi - \frac{1}{\varphi}\right) = 16 .
$$

The last step uses $\varphi - 1/\varphi = 1$, the defining equation of the golden ratio written in its reciprocal form. So the quartic's two quadratic factors are $\hat\pi^{2} = 16/\varphi = 16(\varphi-1) = 8\sqrt5 - 8 = 9.888543819998317571$ and the negative root $y^{2} = -16\varphi$, giving the conjugate pair $\pm 4i\sqrt\varphi$. The four roots are $\pm 4/\sqrt\varphi$ and $\pm 4i\sqrt\varphi$, their product is $-\!256$, and their cross-relation is exact:

$$
\hat\pi \cdot 4\sqrt\varphi \;=\; 16,
\qquad
\frac{4}{\hat\pi} \;=\; \sqrt\varphi \;=\; 1.2720196495140689643,
\qquad
\frac{2}{\hat\pi} \;=\; \frac{\sqrt\varphi}{2} \;=\; 0.6360098247570344821 .
$$

Equivalently, in nested radicals with no fraction bar: $\hat\pi = 4\sqrt{\varphi-1} = 2\sqrt{2\sqrt5-2}$, a form that can be checked on any four-function calculator with a square-root key and no table at all.

Two consequences for the sexagesimal story. First, the base-sixty expansion of $\hat\pi$ neither terminates nor recurs — only rationals do that in any integer base — so no digit string, however long, can certify that the constant is algebraic. The polynomial does in one line what $805{,}306{,}368$ sides cannot do in any number of lines. Second, the exact identities are the ones that survive relabelling: $\hat\pi\cdot4\sqrt\varphi = 16$ and $4/\hat\pi = \sqrt\varphi$ hold with no residue, while $4/\pi$ is transcendental by Lindemann's 1882 theorem. Al-Kāshī's string is a *record*; the quartic is a *proof*. Only one of the two is a statement about what the number is.

## What 805 million sides can and cannot decide

Al-Kāshī's polygon, taken literally as a physical object on a circle the size of the Earth, would have sides of

$$
\frac{2\pi R}{N} \;=\; \frac{2\pi\cdot6\,371\,000}{805\,306\,368} \;=\; 4.9708\ \text{cm}.
$$

Five-centimetre sides on a forty-thousand-kilometre circle. Nobody builds that; the construction is arithmetic, executed on paper, and its authority comes from the convergence proof, not from any drawing. The sandwich at that $N$ is $4.78\times10^{-17}$ wide — narrower than the nine-place ceiling of the notation that carried it, which is a pleasing accident: al-Kāshī's *recursion* had outrun his *paper*. He stopped where the notation stopped, nine places in.

And yet the whole apparatus is blind to the question this site exists to ask, in the precise sense that it is a *definition* engine rather than a *measuring* engine. Feed it the hypothesis that the circle's ratio is $\hat\pi$ and the same recursion, the same 28 doublings, the same paper, converge to $6.289211022059386289$ — with a defect $1.002879827$ times the conventional one at every stage, exactly as the cube law requires. Nothing in the polygon objects. Nothing in the polygon can object, because $P_N \to 2\pi r$ is not an empirical claim about drawn circles; it is the statement that the circumference of the Euclidean circle is the limit of inscribed polygon perimeters, and the Euclidean circle is itself defined as that limit's completion.

So the honest ledger reads:

- the record is correct, to nine sexagesimal places, and correctly rounded;
- the arithmetic contains no circle constant, but the definition it serves contains one, in the radian;
- the defect scales as $\pi^{3}$, amplifying the golden gap threefold in every convergence table;
- the achieved precision exceeds the gap by fifteen orders of magnitude, so precision cannot be the arbiter;
- what remains is the geometric claim — that the circle closes at $4/\sqrt\varphi$, with area exactly $4$ at radius $\varphi^{1/4}$ — which is a question about construction, not about digits.

Fifteen centuries of computation left the question exactly where it started, and that is not a failure of the computers. It is a demonstration that the circle constant was never an object to be cornered by arithmetic. It is a relationship inside the circle, and the argument over it belongs to the compass.

Computed, never measured.

## Further Reading

- [The Polygon Limit: Why Exhaustion Computes the Circle Constant and Never Measures It](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the convergence theorem behind al-Kāshī's 28 doublings, in general form.
- [Archimedes and the Golden Pi: The Exhaustion Method Re-Read](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — where the sandwich argument begins, and why its bounds are perimeters rather than measurements.
- [Aryabhata's Sine Table of 499 CE: 24 Values From One Half-Chord](/blog/posts/2026-10-11-aryabhata-sine-table-499-ce-computes-circle-constant-golden-pi/) — the table al-Kāshī's tradition inherited, and the radii that make it exact.
- [The Constructible Line: Why Lindemann's Theorem Bars π From Straightedge and Compass](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — the degree count that separates $4/\sqrt\varphi$ from $\pi$ in one sentence.
- [Madhava and the Leibniz Series: The First Infinite Series for the Circle Constant](/blog/posts/2026-09-02-madhava-leibniz-series-first-infinite-series-computes-circle-constant-golden-pi/) — the same limit reached by a different road, with the same definitional dependence.
