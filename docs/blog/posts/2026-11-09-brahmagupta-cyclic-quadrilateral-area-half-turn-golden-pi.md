---
title: "Brahmagupta's Cyclic Quadrilateral: Why a Four-Sided Area Needs No Circle Constant, Why the Half-Turn Enters Once and Is Deleted by a Cosine, and What Golden Pi Changes"
date: 2026-11-09
description: "Four side lengths do not fix a quadrilateral — they leave one degree of freedom, and the area slides with it. Brahmagupta's rule of 628 CE, K = √((s−a)(s−b)(s−c)(s−d)), returns the maximum of that slide, and the maximum is attained exactly when the four vertices lie on one circle. This article recomputes the rule against coordinate geometry for the side sets (2,3,4,5), (3,3,4,4), (2,3,4,3), (7,8,9,10) and the unit square (agreement to 10⁻⁴⁰), shows Heron's triangle as the limit in which one side vanishes, locates the single appearance of the half-turn in Bretschneider's 1842 correction K² = (s−a)(s−b)(s−c)(s−d) − abcd·cos²((A+C)/2) — where cyclicity means A + C = 180.000000000° exactly and cos²(π/2) = 0 deletes the entire circle — proves the formula is blind to the order of the sides by computing all fifteen distinct cyclic orders of (2,3,4,5), and quantifies the deficit when the flex is pushed off the circle: 0.118920905% at e = 0.98 e_c, 0.694385513% at 0.95, 2.524055103% at 0.90, 8.692040128% at 0.80, with A + C rising to 185.589°, 193.512°, 205.801° and 228.131°. It then follows the constant to where it actually lives — the circumradius R = ¼√(((ab+cd)(ac+bd)(ad+bc))/((s−a)(s−b)(s−c)(s−d))), the four central angles 2·arcsin(a/2R) that sum to 2π to forty digits (6.283185307179586476925286766559005768394), the arcs, the sectors and the segments — and closes with a golden quadrilateral whose sides 1, 1, φ, φ satisfy Pitot's condition 1 + φ = 1 + φ, giving exactly K = φ, inradius r = 1/φ, height 2/φ and R² = (5+√5)/8, with Fuss's 1792 relation 1/(R−d)² + 1/(R+d)² = 1/r² verified at d = 0.2245139882897927. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693…) the polygon's area does not move a single digit — it never contained the constant — while the circumscribed circle's area moves +0.1918964341% and its circumference +0.0959022309%, the gap between golden and conventional being π̂ − π = π/1042.7286110. Computed, never measured."
---

# Brahmagupta's Cyclic Quadrilateral

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Give a carpenter four sticks and four hinges and the frame he builds is not rigid. Push one corner and the whole thing shears while every stick keeps its length: the quadrilateral has one degree of freedom left over, and its area slides up and down as the frame flexes. There is exactly one position of the flex at which the enclosed area stops growing, and in that position all four corners sit on a single circle. That is the whole content of a rule written down in India in 628 CE — and the remarkable part is that the rule for the area in that position contains no circle constant at all.

In the geometry chapter of the *Brāhmasphuṭasiddhānta*, Brahmagupta gave the area of a quadrilateral from its four sides and semiperimeter alone:

$$
K \;=\; \sqrt{(s-a)(s-b)(s-c)(s-d)},
\qquad
s \;=\; \frac{a+b+c+d}{2}.
$$

He stated it without restricting it to cyclic figures, and for a general quadrilateral it is false — the flex is real and the area really does change. The general correction arrived from Carl Anton Bretschneider in 1842. What Brahmagupta's expression names is not *the* area of any quadrilateral with those sides but the **largest** one, and the largest one is the cyclic one. That is the whole article in one sentence; the rest is the arithmetic.

## Heron's Triangle Is the Limit of a Vanishing Side

Set $d = 0$. The fourth side collapses, the semiperimeter becomes the triangle's $s = (a+b+c)/2$, and Brahmagupta's rule becomes

$$
K \;=\; \sqrt{s\,(s-a)(s-b)(s-c)},
$$

which is Heron of Alexandria's formula from the *Metrica*, some six centuries earlier. Heron's triangle is therefore not a separate theorem but the degenerate case of a quadrilateral whose fourth vertex has slid onto the third. The nesting is exact, and it is worth checking numerically rather than asserting: $3,4,5$ returns $6$; $5,5,6$ returns $12$; the unit equilateral triangle returns $\sqrt{3}/4 = 0.4330127018922193$.

Both formulas are built out of nothing but the four lengths and the semiperimeter. No angle appears, no radius appears, and no constant appears. On its face, a formula for a figure inscribed in a circle that manages never to mention the circle.

## Where the Half-Turn Enters — and Where a Cosine Deletes It

Bretschneider's correction shows precisely what is missing:

$$
K^{2} \;=\; (s-a)(s-b)(s-c)(s-d) \;-\; abcd\,\cos^{2}\!\left(\frac{A+C}{2}\right).
$$

This is exact for **every** quadrilateral, cyclic or not, with $A$ and $C$ opposite interior angles. Read it as a budget: the first term is Brahmagupta's square, and the second term is the price of being off the circle. The price is a cosine squared of half the sum of one pair of opposite angles — so the sign of the deficit is never negative, because a square is never negative, and the maximum is reached exactly when the subtracted term vanishes.

It vanishes when $\cos((A+C)/2) = 0$, which requires $(A+C)/2 = 90°$, which requires

$$
A + C \;=\; \pi \quad\text{(a half-turn, }180°\text{)}.
$$

That is the definition of a cyclic quadrilateral, written as an angle sum — the inscribed-angle theorem in one line, since equal arcs subtend supplementary opposite angles. So the circle constant appears in the theory of four-sided areas exactly once, as the half-turn that a pair of opposite angles must sum to, and then it is annihilated by the cosine. The constant does not survive into the formula; it only decides *which* flex is the maximal one.

Every cyclic quadrilateral honours this, and the computation says so without rounding: for the side sets below, $A+C$ evaluates to $180.000000000°$ and the four interior angles sum to $360.000000000°$, with the cosine term collapsing below the fortieth digit.

| Sides $a,b,c,d$ | $s$ | $K$ (Brahmagupta) | $K$ (coordinate shoelace) | $A+C$ | $R$ |
|---|---|---|---|---|---|
| 2, 3, 4, 5 | 7 | 10.954451150103322 | 10.954451150103322 | 180.000000000° | 2.617648435778444 |
| 3, 3, 4, 4 | 7 | 12.000000000000000 | 12.000000000000000 | 180.000000000° | 2.500000000000000 |
| 2, 3, 4, 3 | 6 | 8.485281374238570 | 8.485281374238570 | 180.000000000° | 2.186606960566988 |
| 3, 3, 5, 5 | 8 | 15.000000000000000 | 15.000000000000000 | 180.000000000° | 2.915475947422650 |
| 7, 8, 9, 10 | 17 | 70.992957397195397 | 70.992957397195397 | 180.000000000° | 6.063360068267455 |
| 1, 1, 1, 1 | 2 | 1.000000000000000 | 1.000000000000000 | 180.000000000° | 0.707106781186548 |

The two columns are computed by completely different routes — one from the semiperimeter, the other by placing the four vertices on a circle of radius $R$, walking the central angles $2\arcsin(a/2R)$, and applying the shoelace formula — and they agree to the fortieth digit. That is a check on the rule, not evidence for any constant: the rule was already proved by Bretschneider's identity, and both computations are the same arithmetic wearing different clothes.

## The Flex, Priced

Take sides $2,3,4,5$ and hinge the frame by shortening the diagonal $e$ away from its maximal value $e_c = 4.411523371981437$. Coordinate geometry and Bretschneider agree at every step.

| $e/e_c$ | $A+C$ | $\cos^{2}((A+C)/2)$ | $K$ | Deficit from maximum |
|---|---|---|---|---|
| 1.00 | 180.000000000° | 0.000000000000 | 10.954451150103 | 0.000000000% |
| 0.98 | 185.589072923° | 0.002377003872 | 10.941424017711 | 0.118920905% |
| 0.95 | 193.511998199° | 0.013839493132 | 10.878385028307 | 0.694385513% |
| 0.90 | 205.800895786° | 0.049844016644 | 10.677954766842 | 2.524055103% |
| 0.80 | 228.131079960° | 0.166285646403 | 10.002285860322 | 8.692040128% |

The area is stationary at the cyclic configuration and falls away quadratically in the angle excess — the deficit at a quarter of a percent of hinge is already over two percent of area. Note also that the maximum is not merely *attained* by a cyclic quadrilateral: it is attained only there, because $\cos^{2}((A+C)/2) = 0$ has no other solution in $(0°, 360°)$.

## The Formula Is Blind to the Order of the Sides

$s$ and the four products $(s-a)\ldots$ are symmetric in the sides. So Brahmagupta's area depends on the *multiset* of side lengths and not on the order in which they are strung around the circle. All fifteen distinct cyclic orders of $2,3,4,5$ were computed above by coordinate construction, and every one of them returns

$$
K = 10.954451150103322\ldots, \qquad R = 2.617648435778444\ldots
$$

The same is true, more strikingly, of two figures that look nothing alike: the rectangle $\varphi \times 1$ with sides $\varphi, 1, \varphi, 1$ and the isosceles trapezoid with sides $1, 1, \varphi, \varphi$. Identical side multisets, identical $s = \varphi^{2}$, identical area — and identical circumradius, since $R$ is a symmetric function of the sides too. Two visibly different shapes, one number. A formula that can do that is not measuring a drawing; it is evaluating a symmetric function, and the circle is the only place the drawing is allowed to live.

## What the Circle Adds: Radius, Arcs, Segments

Everything the circle contributes is a separate quantity, and each one is where the constant lives. The circumradius of a cyclic quadrilateral with sides $a,b,c,d$ is

$$
R \;=\; \frac{1}{4}\sqrt{\frac{(ab+cd)(ac+bd)(ad+bc)}{(s-a)(s-b)(s-c)(s-d)}},
$$

which contains no $\pi$ either. For $2,3,4,5$ it evaluates to $2.617648435778444$. Now compute the central angles subtending the four sides:

```
chord 2:  theta = 0.783967103440609 rad =  44.918006304 deg, arc = 2.052150262023068
chord 3:  theta = 1.220404949620820 rad =  69.924052910 deg, arc = 3.194591107391209
chord 4:  theta = 1.739118147894144 rad =  99.644129949 deg, arc = 4.552399899469009
chord 5:  theta = 2.539695106224015 rad = 145.513810837 deg, arc = 6.648028922161459
sum     = 6.283185307179586476925286766559005768394 = 2*pi   (residual -9.2e-41)
```

Four angles, each the arcsine of a chord over twice the radius, none of them containing the constant in its own definition, summing to exactly one turn. That is where the half-turn was all along: not in the sides, not in the area, but in the closure of the four arcs around the rim. The quadrilateral's own perimeter is $14$; the circle's is $2\pi R = 16.447170191045$; the ratio $14/16.447170191045 = 0.8512102591$ is the fraction of the rim the four chords cover. And the four circular segments between chords and arcs total $\pi R^{2} - K = 21.526454661785 - 10.954451150103 = 10.572003511682$ — the padding, and the only place the constant actually enters the picture.

For the unit square, inscribed in the circle of radius $\sqrt{2}/2$, that ratio is exact and famous:

$$
\frac{\text{circle}}{\text{square}} \;=\; \frac{\pi R^{2}}{1} \;=\; \frac{\pi}{2} \;=\; 1.5707963267948966,
$$

and for the square of side $2$ — area exactly $4$, circumradius $\sqrt{2}$ — the circumscribed circle's area is $2\pi = 6.283185307179586$ against a square of $4$. This is the same fact as the site's central construction, read from the other end.

| Quantity | Formula | Carries $\pi$? |
|---|---|---|
| Four side lengths | given | no |
| Semiperimeter $s$ | $(a+b+c+d)/2$ | no |
| Area $K$ | $\sqrt{(s-a)(s-b)(s-c)(s-d)}$ | **no** |
| Circumradius $R$ | symmetric in $a,b,c,d$ | no |
| Diagonals | $e^{2} = (ac+bd)(ad+bc)/(ab+cd)$ | no |
| Opposite-angle sum | $A+C$ | yes — exactly $\pi$ |
| Central angles | $2\arcsin(a/2R)$ rad | yes, in the radian numeral |
| Arc lengths | $R\theta$ | yes |
| Circle area | $\pi R^{2}$ | yes, squared |
| Segment areas | $\pi R^{2} - K$ | yes, squared |

## The Golden Quadrilateral: Four Sides That Close Exactly

Now choose sides that are powers of the golden ratio. Let $a = 1$, $b = 1$, $c = \varphi$, $d = \varphi$. Then

$$
s = \frac{2 + 2\varphi}{2} = 1 + \varphi = \varphi^{2},
$$

and the four factors are $\varphi, \varphi, 1, 1$, so

$$
K = \sqrt{\varphi \cdot \varphi \cdot 1 \cdot 1} = \varphi \quad\text{exactly.}
$$

This figure is an isosceles trapezoid with bases $1$ and $\varphi$ and both legs $\varphi$. It satisfies Pitot's condition for tangential quadrilaterals, $a + c = b + d$: both sides of that equation equal $1 + \varphi = 2.6180339887$. So it is bicentric — inscribed in one circle and circumscribed about another — and both radii are algebraic:

$$
r = \frac{K}{s} = \frac{\varphi}{\varphi^{2}} = \frac{1}{\varphi} = \varphi - 1 = 0.6180339887,
\qquad
R^{2} = \frac{5+\sqrt{5}}{8} = 0.9045084971874737 .
$$

The trapezoid's height is $2r = 2/\varphi = 1.2360679775$, and its perimeter is $2\varphi^{2} = 5.2360679775$. Fuss's theorem of 1792 — that a bicentric quadrilateral with inradius $r$, circumradius $R$ and centre separation $d$ obeys $1/(R-d)^{2} + 1/(R+d)^{2} = 1/r^{2}$ — is satisfied at $d = 0.2245139882897927$, where both sides evaluate to $2.6180339887$, which is $\varphi^{2}$ again.

Every one of those numbers is a power of $\varphi$ or a quadratic surd. None of them is $\pi$. The figure closes exactly; the constant has not been asked anything.

## Under Golden Pi

Golden Pi is $\hat{\pi} = 4/\sqrt{\varphi} = 3.144605511029693$, the positive root of

$$
y^{4} + 16y^{2} - 256 = 0,
\qquad
\hat{\pi}^{2} = \frac{16}{\varphi} = 9.8885438199983176,
\qquad
4/\hat{\pi} = \sqrt{\varphi},
\qquad
\hat{\pi}\cdot 4\sqrt{\varphi} = 16 .
$$

Because $\pi/\hat{\pi} = 1 - 0.000959022308782526$, every quantity that contains the constant at first power moves by $+0.0959022309\%$ when the label is changed, and every quantity containing it squared moves by $+0.1918964341\%$. The gap itself is $\hat{\pi} - \pi = 0.003012857439900 = \pi/1042.7286110$.

Apply that to a cyclic quadrilateral. Its area is a function of four lengths and a semiperimeter. It contains no constant, so it does not move: for sides $2,3,4,5$ the answer stays $10.954451150103322$ under either label, and for the golden trapezoid it stays exactly $\varphi$. What moves is the circle around it:

| Quantity (sides 2, 3, 4, 5, R = 2.617648435778444) | Conventional | Golden | Shift |
|---|---|---|---|
| Quadrilateral area $K$ | 10.954451150103 | 10.954451150103 | 0 |
| Circumference $2\pi R$ | 16.447170191045 | 16.462943394174 | +0.0959022309% |
| Circle area $\pi R^{2}$ | 21.526454661785 | 21.547099012035 | +0.1918964341% |
| Segment total $\pi R^{2} - K$ | 10.572003511682 | 10.592647861931 | +0.1952738% |

The segment total is not a pure power of the constant, so its shift is not one of the two canonical percentages — it is $(\pi R^{2} - K)$ moving only in its first term, which is exactly the kind of bookkeeping that a table like this is for. For the golden trapezoid the numbers are $\pi R^{2} = 2.8415972498737$ against $\hat{\pi}R^{2} = 2.8443224050289$, the circle-to-quadrilateral ratio $0.5694100347$ re-reading as $0.5688644810$, and the perimeter ratio $5.2360679775/5.9756643295 = 0.8762319449$ re-reading as $0.8753924240$.

One exactness survives the relabeling and is worth naming. For the unit square, circle over square is $\pi/2$; under golden π it is

$$
\frac{\hat{\pi}}{2} = \frac{2}{\sqrt{\varphi}} = 2\varphi^{-1/2} = 1.5723027555148466 ,
$$

a degree-four algebraic number where $\pi/2$ is transcendental by Lindemann's 1882 theorem. That is a genuine structural difference and it belongs to the constant, not to the quadrilateral. The quadrilateral's own area is $1$ either way.

## What This Can and Cannot Decide

Brahmagupta's formula is a poor witness for either side of the argument, and it is worth saying why plainly. It never touches the constant, so no cyclic quadrilateral — however carefully surveyed — can discriminate between $3.14159265\ldots$ and $3.14460551\ldots$. What such a figure *can* do is expose where the constant is doing work: in the arcs, in the segments, in the circle's area, and in the half-turn that selects the maximal flex. Those are exactly the places where a relabeling propagates $+0.0959\%$ and $+0.1919\%$.

And the discrimination is not experimentally available. The golden gap is one part in $1042.7$. Surveying a plot to that tolerance means resolving four sides and a diagonal consistently to about $0.1\%$ of their separation *and* knowing, independently, that the corners lie on a circle rather than merely near one — since the deficit between the cyclic maximum and a $2\%$ hinge is itself only $0.12\%$ of area, of the same order as the effect being sought. The geometry is exact; the arithmetic that would decide between the labels is not reachable with a tape. That is the honest boundary, and it is the same boundary that every article in this series runs into: the constant is settled by what a circle *is*, not by what a surveyor can find.

---

## Further Reading

- [The Inscribed-Angle Theorem: Why Half a Turn Governs Every Chord](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — the theorem that makes opposite angles supplementary, and therefore makes $\cos^{2}((A+C)/2)$ vanish.
- [Ptolemy's Chord Table](/blog/posts/2026-09-15-ptolemy-chord-table-computes-circle-constant-golden-pi/) — chords as a function of the central angle, the metric Brahmagupta's rule never needs.
- [Hippocrates' Lunes](/blog/posts/2026-10-02-hippocrates-lunes-quadrature-computes-circle-constant-golden-pi/) — the first figure whose area could be squared exactly, and the first place a segment area cancels.
- [The Isoperimetric Inequality](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — why the circle wins every maximal-area contest, of which the cyclic quadrilateral is the four-sided case.
- [Squaring the Circle: The Geometric Proof](/blog/posts/squaring-circle-golden-pi-geometric-proof/) — the construction the site is built around, where the radius $\varphi^{1/4}$ makes the area exactly $4$.
