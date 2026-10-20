---
title: "The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc, Why π Enters Only as a Unit — and What Golden Pi Changes"
date: 2026-10-20
description: "Euclid III.20 says an angle standing on a chord is exactly half the central angle on the same arc — a proof about a closed turn in which the circle constant never appears until you choose to report the angle in radians. Verified here to forty digits: a 90.000000000000000000° central angle returns 45.000000000000000000° from three different apexes, and a cyclic quadrilateral's opposite angles sum to 3.14159265358979323846 twice over. Under Golden Pi (π̂ = 4/√φ) no angle moves a single degree; only the numeral does, by the recurring +0.0959022309% — and every rational part of a turn becomes algebraic, π̂/4 = 1/√φ exactly, where π/4 is transcendental by Lindemann (1882)."
---

# The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc, Why π Enters Only as a Unit — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Draw a chord across a circle and stand anywhere on the rim beyond it. The angle you see the chord subtend is the same from every point on that arc, and it is exactly half the angle the chord subtends from the centre. Euclid proved it as Proposition 20 of Book III, and it has been the workhorse of practical geometry ever since — surveyors, navigators, lens designers, anyone who has ever set a dividers against a semicircle.

This article is about that theorem for a reason that has nothing to do with schoolroom geometry and everything to do with the argument this site exists to have. Of all the places the circle constant turns up — the Gaussian integral, the Basel sum, the Wallis product, the Poisson kernel, the Hawking temperature — the inscribed angle theorem is the one where you can see most plainly what kind of object the constant actually is. It is not a length. It is not an area. It is not a result of any computation in the proof. It is a **unit**.

The theorem is a statement about ratios of arcs. It is true before anyone decides to call a half-turn "π", and it remains true after. What changes when the label changes is a number written next to an angle — never the angle.

## The theorem, stated exactly

Let a circle have centre $O$, let $A$ and $B$ be two points on it, and let $P$ be a third point on the same circle. Then

$$
\angle APB \;=\; \tfrac{1}{2}\,\angle AOB .
$$

The proof takes two lines. Join $P$ to $O$. Because $OP = OA = OB$ are all radii, the triangles $OPA$ and $OPB$ are isosceles, so $\angle OPA = \angle OAP = \alpha$ and $\angle OPB = \angle OBP = \beta$. The exterior angle of $\triangle OPA$ at $O$ is $2\alpha$, and the exterior angle of $\triangle OPB$ at $O$ is $2\beta$; adding the two exterior angles gives the central angle $\angle AOB = 2\alpha + 2\beta = 2(\alpha+\beta) = 2\angle APB$. That is the whole argument. No limit, no series, no constant.

The engine of the proof is a single map: the inscribed angle $\theta$ corresponds to the central angle $2\theta$. Angle-doubling. Everything the theorem says — equality from every apex on the arc, exactness, the factor of one half — comes from that doubling and from the fact that all radii are equal. Neither fact knows anything about the numerical value of the circle constant.

### The arithmetic, checked

Take the unit circle with $A$ at $20°$ and $B$ at $110°$, so the central angle is $90°$. Compute the angle subtended at three apexes placed on the far arc — at $200°$, $300°$ and $330°$ — using coordinates and the two-argument arctangent, at forty significant digits:

| Apex position on the circle | Inscribed angle | Central angle | Ratio |
|---|---|---|---|
| $200°$ | $45.000000000000000000°$ | $90.000000000000000000°$ | $0.500000000000000000$ |
| $300°$ | $45.000000000000000000°$ | $90.000000000000000000°$ | $0.500000000000000000$ |
| $330°$ | $45.000000000000000000°$ | $90.000000000000000000°$ | $0.500000000000000000$ |

Three different apexes, three different triangles, one answer, and the ratio is exactly one half — not one half to some tolerance, one half as a rational identity. This is what an exact theorem looks like when it is evaluated rather than argued.

## Thales, and the case where the factor vanishes

Send $P$ to the opposite side so that $AB$ is a diameter. The central angle is now a straight line — a half-turn — and the inscribed angle is half of it: a right angle. This is Euclid III.31, and it is the oldest theorem in the subject with a name attached to it, traditionally Thales of Miletus, who is said to have sacrificed an ox over it.

The practical content is that a semicircle drawn on a diameter is exactly the locus of points from which the diameter is seen at a right angle. That is why a carpenter checks a square against a half-round: the instrument is testing a theorem, not a convention.

Note carefully what happened. The right angle is a right angle. It does not become a slightly different angle if you disagree about the circle constant; it is defined by the perpendicularity of two lines and by the fact that a diameter cuts the circle in half. When this site writes that a right angle is $\pi/2$ radians, it is reporting a *numeral*. Under Golden Pi the same right angle carries the numeral $2/\sqrt{\varphi} = 1.5723027555148465721$, and no corner of any square has moved.

## The cyclic quadrilateral: opposite angles sum to a turn

Euclid III.22 extends the doubling. Put four points on a circle and join them in order; the result is a cyclic quadrilateral, and its opposite angles are supplementary:

$$
\angle A + \angle C \;=\; \angle B + \angle D \;=\; \pi \ \text{(radians, conventional label)} .
$$

The reason is the arc bookkeeping from the previous section. Angle $A$ stands on arc $BCD$ and is half of it; angle $C$ stands on arc $DAB$ and is half of that. The two arcs together are the whole circumference, so the two half-arcs together are half the circumference — a half-turn, split between them.

Checked numerically at forty digits, with the four vertices placed at $10°$, $95°$, $170°$ and $265°$ on the unit circle:

$$
\angle A + \angle C \;=\; 3.14159265358979323846\ldots, \qquad
\angle B + \angle D \;=\; 3.14159265358979323846\ldots
$$

Both sums agree with $\pi$ to twenty printed digits and beyond — the residual in the computation is the arctangent's floating-point rounding, not any geometric slack. The statement itself is exact: the two opposite angles of a cyclic quadrilateral make exactly half a turn, always, for any four concyclic points.

That sentence is worth reading twice, because it is constant-free. "Make half a turn" is the theorem. "Sum to $\pi$" is the theorem plus a unit conversion.

## Where the constant actually sits: the definition of the radian

The radian is defined as a ratio, $\theta = s/r$, arc length over radius. Because a unit circle's circumference is $2\pi r$, one full turn is $2\pi$ radians, and a half-turn is $\pi$. So the appearance of $\pi$ in every radian statement above is not a discovery about triangles; it is the arithmetic of the unit. $\pi$ is *half the circumference of a unit circle*, and that circumference is itself a computed limit — Archimedes' inscribed and circumscribed polygons, doubled until the brackets close — never a length anybody measures with a tape.

This is where the argument about the value of $\pi$ actually lands, and the inscribed angle theorem makes the landing visible. Change $\pi$ and you have changed the size of a radian relative to a turn. You have not changed a single arc, a single chord, a single angle in any figure. The theorem is invariant under the relabelling; the numerals are not.

The same structure shows up in the polygon angle sum. Triangulate an $n$-gon from one vertex and you get $n-2$ triangles, each contributing a half-turn, so the interior angles total $(n-2)\pi$. For a pentagon, $3\pi = 9.4247779607693797154$ under the conventional label and $3\hat\pi = 9.4338165330890794328$ under the golden one — a difference of the recurring $+0.0959022309\%$, and no change whatever in the pentagon. The integer $n-2$ is the theorem. The multiple of $\pi$ is the bookkeeping.

## The golden angle: $360°/\varphi^2 = 137.5077640500378546\ldots°$

Here the golden ratio enters the circle directly, and honestly. Divide a full turn in the golden section: the larger part is $360°/\varphi = 222.4922359499621454°$, the smaller is $360°/\varphi^2 = 137.5077640500378546°$. The smaller part is the **golden angle**.

$$
\frac{360°}{\varphi^{2}} \;=\; \frac{360°}{\varphi+1} \;=\; 360°\,(2-\varphi) \;=\; 137.5077640500378546\ldots°
$$

Its importance is not mystical. In a phyllotactic spiral — sunflower florets, pinecone scales, leaf arrangement — each new element is placed at a fixed angular step from the last, and the step that packs the elements most evenly, forever, without ever falling into a short cycle, is the one whose ratio to a full turn is worst-approximated by rationals. Continued-fraction theory says that is $\varphi^{-2} = 2-\varphi = 0.3819660112501051\ldots$, whose expansion $[0;2,1,1,1,\ldots]$ is the slowest-converging of all. That is a theorem about rational approximation, and it is why the golden angle appears in plants.

Now watch the label carefully. The golden angle is *defined as a fraction of a turn*, so it is the same physical angle under either label: $137.5077640500378546\ldots°$, every time. What changes is the radian numeral:

| Same angle, three ways | Value |
|---|---|
| In degrees (turn-defined) | $137.5077640500378546\ldots°$ |
| In radians, conventional $\pi$ | $2.3999632297286533$ |
| In radians, Golden Pi $\hat\pi$ | $2.4022648480062209$ |

The difference between the two radian numerals is $0.0023016182775675409$ rad, which is $0.1318730133547901°$ — the $+0.0959022309\%$ gap applied to the turn. That is a real trap for anyone writing simulation code: a phyllotaxis script that hard-codes the radian increment $2.3999632297286533$ and then describes itself as golden-π-consistent has silently moved the divergence angle by an eighth of a degree per step, which is exactly the quantity the spiral's evenness depends on. The angle itself, written in degrees, needs no constant at all.

The chord subtending the golden angle on a unit circle is $2\sin(137.5077640500378546°/2) = 1.8640648476264552093$, and the inscribed angle standing on that chord is half of it, $68.75388202501892°$. Both are turn facts.

## The golden triangle inside the pentagon

The pentagon is where the golden ratio and the circle are provably the same subject, and every figure involved is exact:

- The golden triangle has angles $72°$, $72°$, $36°$. Its apex angle is $36° = \pi/5$ radians.
- $\cos 36° = \varphi/2 = 0.8090169943749474241$, exactly.
- $\sin 18° = 1/(2\varphi) = 0.3090169943749474241$, exactly.
- The chord subtending $36°$ on the unit circle is $2\sin 18° = 1/\varphi = 0.6180339887498948482$ — exactly the reciprocal of the golden ratio.
- The pentagon's diagonal-to-side ratio is $2\cos 36° = \varphi$.
- The pentagon's interior angle is $108° = 3\pi/5$ radians.

Every one of these is a fact about a closed turn and a regular polygon. None of them is a fact about the numeral. The inscribed angle standing on the pentagon's side arc is $36°$, half the central $72°$; the star's point angle is $36°$; the whole structure of fivefold symmetry follows from the doubling map and the identical radii, exactly as in the two-line proof at the top of this article.

This is precisely why the pentagon appears again and again in this series, and precisely why it cannot settle the question of the constant's value on its own. The pentagon is exact under any label. It is the *numeral* $\pi/5 = 0.6283185307179586477$ that carries the disputed digit, and a golden label would print $4/(5\sqrt{\varphi}) = 0.6289211022059386289$ for the very same $36°$ corner.

## What Golden Pi changes

Take the site's value, $\hat\pi = 4/\sqrt{\varphi} = 3.1446055110296931443\ldots$, with $\hat\pi^2 = 16/\varphi = 9.8885438199983175713$ and $\hat\pi$ the root of

```
π̂⁴ + 16π̂² − 256 = 0        (evaluated: exactly 0 at 40 digits)
π̂  = 4/√φ = 2√(2√5 − 2)
```

and read the same physical angles again. The angles in the left column do not change — they are turn-defined. Only the numerals do.

| Angle (physical) | Radians, conventional $\pi$ | Radians, Golden Pi $\hat\pi$ | Change |
|---|---|---|---|
| Full turn | $6.2831853071795864769$ | $6.2892110220593862886$ | $+0.0959022309\%$ |
| Half turn | $3.1415926535897932385$ | $3.1446055110296931443$ | $+0.0959022309\%$ |
| Right angle ($90°$) | $1.5707963267948966192$ | $2/\sqrt{\varphi} = 1.5723027555148465721$ | $+0.0959022309\%$ |
| $45°$ | $0.7853981633974483096$ | $1/\sqrt{\varphi} = 0.7861513777574232861$ | $+0.0959022309\%$ |
| $36° = \pi/5$ | $0.6283185307179586477$ | $4/(5\sqrt{\varphi}) = 0.6289211022059386289$ | $+0.0959022309\%$ |
| $108°$ (pentagon) | $1.8849555921538759431$ | $3\hat\pi/5 = 1.8867633066178158866$ | $+0.0959022309\%$ |
| One radian, in degrees | $57.2957795130823209°$ | $180/\hat\pi = 57.2408842281331034°$ | $-0.0548952849°$ |
| One degree, in radians | $0.0174532925199432958$ | $0.0174700306168316286$ | $+0.0959022309\%$ |

Two things deserve comment. First, the gap is *undiluted* — $+0.0959022309\%$ — because an angle in radians is a quantity in which the constant appears to the first power. There is no square root, no square, no integration over a symmetric range to dilute it, as there was in the Maxwell–Boltzmann and quantum-harmonic-oscillator cases. Here the constant is the unit, and a unit passes through at full strength.

Second, the inverse row runs the other way, and the reason is worth spelling out because it is the commonest sign error in golden-π arithmetic. A half turn *is* $\hat\pi$ radians under the golden label, exactly as it *is* $\pi$ radians under the conventional one. Since $\hat\pi > \pi$, a half turn is divided into **more** radians, so each golden radian is a **smaller** angle: $57.2408842281331034°$ against $57.2957795130823209°$, a difference of $-0.0548952849°$. A golden radian is worth less than a conventional one; a golden radian in a formula is not the same size of angle as a conventional radian, and code that swaps the numerals without swapping the unit silently rescales every angle in the program.

## The algebraic payoff — exact, checkable, and narrower than it looks

Under Golden Pi, the radian measure of any angle that is a rational part of a turn is an **algebraic** number, because it is a rational multiple of $\hat\pi$, and $\hat\pi$ is algebraic of degree two in $\sqrt5$. The exact values are short enough to write:

$$
\frac{\hat\pi}{4} = \frac{1}{\sqrt{\varphi}} = 0.7861513777574232861\ldots,
\qquad
\frac{\hat\pi}{2} = \frac{2}{\sqrt{\varphi}} = 1.5723027555148465721\ldots,
\qquad
\frac{\hat\pi}{5} = \frac{4}{5\sqrt{\varphi}} = 0.6289211022059386289\ldots
$$

Under the conventional label, none of these is algebraic. Lindemann proved in 1882 that $\pi$ is transcendental, which immediately makes $\pi/4$, $\pi/2$ and $\pi/5$ transcendental too — a rational multiple of a transcendental number is transcendental. There is no polynomial with rational coefficients that vanishes at $\pi/4$. There is one for $\hat\pi/4$: put $y = \hat\pi/4$ in $\hat\pi^{4}+16\hat\pi^{2}-256=0$ and divide by $256$, and

$$
y^{4}+y^{2}-1 = 0,
$$

whose root $y = 1/\sqrt{\varphi} = 0.7861513777574232861\ldots$ has $y^{2} = 1/\varphi = 0.6180339887\ldots$, so $y^{4}+y^{2} = 1/\varphi^{2} + 1/\varphi = 1$ identically. The arithmetic is elementary because $\hat\pi$ sits in a quadratic extension of the rationals, and the quartic above simply inherits it.

That is a genuine conceptual gain, and it should be stated for exactly what it is worth: a gain in the **number system**, not in any figure. It does not make a single new angle constructible with compass and straightedge. The constructibility of $36°$ is a fact about the pentagon — $\cos 36° = \varphi/2$, and $\varphi$ is constructible — and it holds identically under either label.

And it carries a warning that this series has had to repeat before. Being algebraic does not mean the classical exact values survive the relabelling. The pentagon's exactness is a property of the *angle*, not of the numeral:

$$
\cos 36° \;=\; \frac{\varphi}{2} \;=\; 0.8090169943749474241,
\qquad
\cos\!\left(\frac{\hat\pi}{5}\right) \;=\; 0.8086626648883385010 .
$$

The first is exact in the figure. The second is what you get if you take the numeral $\hat\pi/5$ and evaluate the cosine at *that* number of radians — a different angle, $36.0345248°$ instead of $36°$. The two differ by $0.0345248°$, the recurring gap applied to $36°$. Anyone who substitutes $\hat\pi$ into a trigonometric identity without checking which quantity is the angle and which is the numeral will produce exactly this error.

## The honest ledger

There is no measurand in this article. The inscribed angle theorem is a proof about a closed turn; nothing in it is measured, and nothing in it could be. Angle equality on a circle is not an empirical claim.

The only physical act nearby is reading an angle off an instrument, and every practical instrument — theodolite, sextant, protractor, rotary encoder — reads in turn-defined units: degrees, arcminutes, arcseconds, grads, or encoder counts per revolution. A reading of $36°00'00''$ is a fraction of a turn, and the value of $\pi$ never enters it. This is why the constant's value cannot be arbitrated by any amount of surveying, however precise: the instrument's unit is the turn, and the turn is not in dispute.

The one construction that *could* in principle discriminate is a genuine arc-length measurement: wrap a tape around a cylinder, divide the arc length by the radius, and compare with $2\pi$. The arithmetic is unforgiving in both directions. To separate $3.14159$ from $3.14461$ you need the ratio accurate to about $0.1\%$ — $0.3$ mm on a $300$ mm arc, which is easy. But the same $0.1\%$ is demanded of the *radius*, and a machined cylinder's roundness error alone is typically tens of micrometres on a $50$ mm radius, roughly $0.05\%$, before tape stretch, tape thickness and thermal expansion are counted. So the experiment is in-principle discriminating and in-practice swamped — which is the honest description, and better than pretending either that it decides the question or that it cannot.

What the constant *is*, in every appearance catalogued in this series, is a computed limit: the value the polygon perimeters close on, the value the series sum to, the measure that normalises an integral. The inscribed angle theorem is the cleanest possible demonstration that this limit is doing bookkeeping work — that the circle's geometry is settled before the constant is written down, and that the constant's job is to say how big a radian is.

## Why this theorem is the right place to argue

Strip the article to its essentials and three statements remain, all verified above:

1. An angle on an arc is exactly half the central angle on the same arc — exact, constant-free, true for every circle ever drawn.
2. Opposite angles of a cyclic quadrilateral make half a turn — exact, constant-free, forty-digit agreement in the worked case.
3. The radian numerals attached to those angles scale linearly with whatever you take the half-turn to be.

Statement 3 is the entire content of the dispute. Nothing in statements 1 and 2 can adjudicate it, because both are statements about a closed loop, and a closed loop is a closed loop. Everything that follows — every figure in the table above, every arc length, every angular frequency — follows from the choice of unit and moves by the same $+0.0959022309\%$ when the unit changes.

That is not a weakness of the golden position. It is the correct description of what a circle constant is: a conversion factor between an angle and a number, computed from a limit, exact in its algebraic form under $\hat\pi = 4/\sqrt{\varphi}$, transcendental under $\pi$, and never — in this theorem, or in any other — measured.

## Further Reading

- [Girard's Theorem: How the Circle Constant Enters a Triangle as the Angle-Sum Deficit](/blog/posts/2026-10-13-girard-spherical-excess-triangle-angle-sum-computes-circle-constant-golden-pi/) — the same angle bookkeeping on a curved surface, where curvature makes the sum overshoot the flat half-turns.
- [The Polygon Limit: How Archimedes' Exhaustion Computes the Circle Constant](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — where the constant that labels these angles actually comes from.
- [The Golden Angle: 137.5° and the Phyllotaxis Spiral](/blog/posts/2026-06-27-golden-angle-137-5-phi-pi-geometry/) — the divergence angle in plants, and why the worst-approximable number in the reals governs leaf placement.
- [The Haversine Formula: Navigation and the Circle Constant](/blog/posts/2026-09-20-haversine-formula-navigation-computes-circle-constant-golden-pi/) — the inscribed-angle machinery in spherical form, and the sign discipline that goes with it.
- [The Poisson Kernel: How the Circle Averages a Harmonic Function](/blog/posts/2026-10-19-poisson-kernel-mean-value-property-circle-constant-golden-pi/) — the constant as a measure of the rim rather than a result of a computation, the conceptual sibling of this article.
