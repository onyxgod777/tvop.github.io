---
title: "Hippocrates' Lunes: The One Curvilinear Figure That Squares Exactly, Why the Circle Constant Cancels Against Pythagoras, and What Golden Pi Changes"
date: 2026-11-10
description: "In the fifth century BCE Hippocrates of Chios squared a figure bounded by circular arcs — the lunes between a semicircle on a chord and the arc it cuts — and the two crescent-shaped areas come out equal to the right triangle underneath them, with no circle constant surviving in the answer. This article rebuilds the figure from its three arcs, computes the isosceles case (semicircles π/4 each, segments π/4 − 1/2, lunes 1/2 in total, 1/4 each, the equal square exactly 1/2 on a side) and the 3-4-5 triangle (leg semicircles 9.8174770424681039 against the big semicircle's identical 9.8174770424681039, lunes 6.000000000000 exactly), proves the cancellation is Pythagoras and not geometry-luck, scans every central angle from 30° to 180° and finds the constant's coefficient π·sin²(θ/2) equal to θ at exactly one non-degenerate angle, 90.0000000000°, and prices the loss when the triangle is not right: the lunes become K + (π/4)·ab·cos C, so the equilateral case carries 0.3926990817 of pure π against a triangle of 0.4330127019. Under Golden Pi (π̂ = 4/√φ = 3.144605511029693…) the right-angle identity does not move a single digit — the same lunes are 1/2 and 6.000000000000 — because the coefficient it multiplies is a² + b² − c² = 0, while the arcs that bound the lune shift +0.0959022309% (2.2214414691 → 2.2235718810 for the semicircle of radius 1/√2), the off-right residual shifts by ab·cos C·(1/√φ − π/4) = 0.0007532143599749765 per unit, and the equilateral lunes move to 0.8260883908 against 0.8257117836. The history is followed honestly: the lunes come to us through Simplicius quoting Eudemus, they were a genuine quadrature of a curvilinear figure and not of the circle, and the circle itself stayed open until Lindemann's 1882 theorem. Computed, never measured."
---

# Hippocrates' Lunes

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Draw a straight line through a circle and you cut off a region with one straight edge and one curved edge — a segment. Draw that same straight line again, this time as the diameter of a second circle built outside the first, and the gap between the new semicircle and the old arc closes into a crescent with two curved sides: a lune. In the fifth century BCE, Hippocrates of Chios looked at that crescent and found something that should not have been possible. He computed its area exactly, in terms of the straight-line figure it sits on, and the circle constant vanished from the answer.

That result is the first recorded quadrature of a curvilinear figure. It is also the reason generations of geometers believed the circle itself might be squareable, which it is not. Both halves of that story are worth recovering with the arithmetic in the open, because the lune is a rare object: a figure whose boundary is nothing but circular arcs, whose area is nevertheless a straight-line area, exactly, with no approximation and no constant left over.

## The Construction

Take a chord $AB$ of a circle of radius $R$, subtending a central angle $\theta$ at the centre $O$. Build a semicircle outward on $AB$ as diameter. The region between that semicircle and the arc $AB$ of the original circle is a lune — two arcs, no straight edges at all.

Its area is the difference of two things that can both be written down: the semicircle, and the circular segment the chord cuts off.

$$
\text{semicircle on } AB \;=\; \frac{\pi}{2}\left(R\sin\frac{\theta}{2}\right)^{2},
\qquad
\text{segment} \;=\; \frac{R^{2}}{2}\left(\theta - \sin\theta\right),
$$

so

$$
A_{\text{lune}}(\theta) \;=\; \frac{R^{2}}{2}\left[\pi\,\sin^{2}\frac{\theta}{2} \;-\; \theta \;+\; \sin\theta\right].
$$

Everything in that bracket is a computed limit: $\pi$ is the value the circumference-to-diameter ratio is *defined* to take in this geometry, $\sin$ is a ratio of lengths. Nothing here is measured.

The classical figure takes $\theta = 90°$, the quarter-circle case, which is exactly the lune drawn on the leg of a right isosceles triangle. Set $R = 1$:

| Quantity | Exact | Decimal |
|---|---|---|
| Semicircle on the chord (radius $1/\sqrt2$) | $\pi/4$ | 0.7853981633974483 |
| Segment cut by the chord ($\theta=\pi/2$) | $\pi/4 - 1/2$ | 0.2853981633974483 |
| Lune | $1/2$ | 0.5000000000000000 |

The brackets collapse: $\tfrac{\pi}{2}\cdot\tfrac12 = \tfrac{\pi}{4}$ appears with a plus sign, $\tfrac{1}{2}\cdot\tfrac{\pi}{2} = \tfrac{\pi}{4}$ appears with a minus sign, and both go. The $\sin\theta = 1$ term leaves $\tfrac12$ behind, and $\tfrac12$ is the area of the right isosceles triangle $AOB$ with legs $R$. The lune equals the triangle. Not approximately, not to some order — identically.

## The Arithmetic: Two Lunes, Three Areas, One Cancellation

The usual presentation uses the full triangle rather than a single chord, and it is more convincing because the bookkeeping is explicit. Take a right triangle with legs $a, a$ and hypotenuse $c = a\sqrt2$, inscribed in a circle with $c$ as diameter. Build semicircles on both legs, outside the triangle.

For $a = 1$:

| Region | Exact | Decimal |
|---|---|---|
| Semicircle on the hypotenuse ($r = c/2$) | $\pi/4$ | 0.7853981633974483 |
| Semicircles on the two legs ($r = 1/2$ each) | $2 \cdot \pi/8 = \pi/4$ | 0.7853981633974483 |
| Two circular segments inside the big semicircle, outside the triangle | $\pi/4 - 1/2$ | 0.2853981633974483 |
| Both lunes = legs − segments | $1/2$ | 0.5000000000000000 |
| Each lune | $1/4$ | 0.2500000000000000 |

The semicircles on the legs together have *exactly* the area of the semicircle on the hypotenuse — the first of the two cancellations, and the one that is easy to miss. Subtract from that sum the two segments (which themselves contain $\pi/4$), and what remains is the triangle's $\tfrac12$. Each lune carries $\tfrac14$, so a square of side $\tfrac12$ has exactly the area of one lune. That square is constructible with straightedge and compass from the original triangle in one step.

The same computation on the 3-4-5 triangle, where nothing is accidentally $\pi/4$:

| Quantity | Decimal |
|---|---|
| Semicircle on hypotenuse ($r = 2.5$) | 9.8174770424681039 |
| Semicircles on legs 3 and 4 ($r = 1.5$, $2$) | 3.5342917352885174 + 6.2831853071795865 = 9.8174770424681039 |
| Segments inside the big semicircle | 3.8174770424681039 |
| Both lunes | 6.0000000000000000 |
| Triangle area (Heron: $s = 6$) | 6.0000000000000000 |

Six against six, to every digit the subtraction carries. The two lunes on the legs of a 3-4-5 triangle enclose exactly the area of the triangle from which they were built.

## The Cause Is Pythagoras, Not Luck

Why did it work? Because the semicircles' areas are proportional to the squares of their diameters, and the diameters are the sides of a right triangle. Writing it generally, for a right triangle with legs $a, b$:

$$
A_{\text{legs}} \;=\; \frac{\pi}{8}\left(a^{2}+b^{2}\right) \;=\; \frac{\pi}{8}c^{2} \;=\; A_{\text{big}},
$$

so the two lunes are

$$
A_{\text{lunes}} \;=\; \frac{\pi}{8}\left(a^{2}+b^{2}-c^{2}\right) + K \;=\; 0 + K,
$$

where $K = ab/2$ is the triangle's area. The entire content of Hippocrates' quadrature is the Pythagorean theorem applied to areas proportional to squared sides. There is no special virtue in the circle; there is a special virtue in the right angle, which is what makes the coefficient of $\pi$ vanish.

That also tells you immediately where the result must fail: drop the right angle and $a^2+b^2-c^2$ stops being zero. It becomes $2ab\cos C$, and the lunes acquire a term in $\pi$ that cannot be removed.

## The Angle Scan: Where Else the Constant Disappears

The chord version makes the same point more sharply, because the parameter is a single angle. The $\pi$-coefficient in $A_{\text{lune}}(\theta)$ is $\tfrac{R^2}{2}\pi\sin^2(\theta/2)$, while the $\pi$-free part is $\tfrac{R^2}{2}(\sin\theta - \theta)$. The lune is constant-free exactly when

$$
\pi\,\sin^{2}\frac{\theta}{2} \;=\; \theta .
$$

Scanning $\theta$ across $(0°, 180°]$ at step $10^{-5}$ rad and bracketing every sign change gives one non-degenerate root:

$$
\theta \;=\; \frac{\pi}{2} \;=\; 90.0000000000°,
$$

with $\theta = \pi$ a second root that is degenerate — the chord has become the diameter, the semicircle has swallowed the arc, and the lune has zero area. Worked at $R = 1$:

| $\theta$ | Lune area | Lune area ÷ $\pi$ | Triangle area | Lune ÷ triangle |
|---|---|---|---|---|
| 30° | 0.0934240140104672 | 0.0297377872665047 | 0.2500000000000000 | 0.373696056041869 |
| 45° | 0.1908921050222020 | 0.0607628442230014 | 0.3535533905932737 | 0.539924407744695 |
| 60° | 0.3021130079926450 | 0.0961655571887813 | 0.4330127018922193 | 0.697700105960964 |
| **90°** | **0.5000000000000000** | **0.1591549430918953** | **0.5000000000000000** | **1.000000000000000** |
| 120° | 0.5639123957917940 | 0.1794988905221150 | 0.4330127018922193 | 1.302299894039040 |
| 150° | 0.4065759859895330 | 0.1294171558253910 | 0.2500000000000000 | 1.626303943958130 |
| 180° | 0.0000000000000000 | 0.0000000000000000 | 0.0000000000000000 | — |

The ratio column is the interesting one. It passes through exactly $1$ at $90°$ and nowhere else — $0.6977$ at $60°$, $1.3023$ at $120°$ — and it rises monotonically to the left of the right angle and falls monotonically to the right of it up to the degenerate diameter. The right angle is not one good case among many; it is the only angle at which the two arcs and the straight chord close the books.

## Off the Right Angle: The Lune That Keeps π

For a general triangle with the side $c$ opposite angle $C$, the same bookkeeping gives

$$
A_{\text{lunes}} \;=\; K \;+\; \frac{\pi}{4}\,ab\,\cos C ,
$$

which is the sentence "the lunes equal the triangle" with the price of a non-right angle written on it. Take $a = b = 1$, $C = 60°$:

| Piece | Decimal |
|---|---|
| Triangle $K = \tfrac12 ab\sin C = \sqrt3/4$ | 0.4330127018922193 |
| $\pi$ term, $\tfrac{\pi}{4}\cdot\tfrac12$ | 0.3926990816987242 |
| Lunes | 0.8257117835909435 |

Almost half the lune's area is now pure $\pi$, and it is not removable — no rearrangement of a 60° triangle's sides will make $\cos C$ vanish. (For $C > 90°$ the term goes negative, which is the arithmetic's way of saying the two "lunes" have overlapped and one of them must be counted with the opposite sign.)

## Golden Pi: The Identity That Does Not Move

Golden Pi is $\hat\pi = 4/\sqrt\varphi = 3.14460551102969314427823434337183571809\ldots$, with $\varphi = (1+\sqrt5)/2$ and the exact closures

$$
\hat\pi^{2} = \frac{16}{\varphi} = 9.88854381999831757127\ldots,
\qquad
\frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4} = 0.31800491237851724106\ldots,
\qquad
\frac{\hat\pi}{4} = \frac{1}{\sqrt\varphi} = 0.78615137775742328607\ldots
$$

and a gap against the conventional label of $+0.0959022309\%$ — one part in $1042.7286110471$, or $\hat\pi - \pi = 0.0030128574398999058$.

Now run the lune computation with $\hat\pi$. The right-angle case returns $1/2$ and $6.000000000000$, exactly as before, on every digit. There is nothing to shift, because the quantity being labelled is $\tfrac{\pi}{8}(a^{2}+b^{2}-c^{2})$, and $a^{2}+b^{2}=c^{2}$ identically for a right triangle: **the constant multiplies zero.** The quadrature is structurally blind to which circle constant is written in it. It cannot arbitrate the constant because it never uses one.

Where the figure does move is where $\pi$ appears alone:

| Quantity | Conventional | Golden | Shift |
|---|---|---|---|
| Lune at $\theta=90°$, $R=1$ | 0.5000000000000000 | 0.5000000000000000 | 0 |
| Two lunes on 3-4-5 legs | 6.0000000000000000 | 6.0000000000000000 | 0 |
| Semicircle on the chord, $\theta=90°$ | 0.7853981633974483 | 0.7861513777574233 | +0.0959022309% |
| Segment, $\theta=90°$ | 0.2853981633974483 | 0.2861513777574233 | +0.2639% of that term |
| Lune perimeter (arcs only), $\theta=90°$ | 3.7922377958740790 | 3.7958746365205280 | +0.0959022309% |
| Lune at $60°$, $R=1$ | 0.3021130079926450 | 0.3024896151726320 | +0.124659% |
| Equilateral lunes, $a=b=1$, $C=60°$ | 0.8257117835909435 | 0.8260883907709310 | +0.0003766072 |
| Gap per unit of $ab\cos C$ | — | $1/\sqrt\varphi - \pi/4 = 0.0007532143599749765$ | — |

Two exact statements come out of the off-right table. First, the golden lunes at $C \ne 90°$ are

$$
A_{\text{lunes}} \;=\; K \;+\; \frac{ab\cos C}{\sqrt\varphi},
$$

because $\hat\pi/4 = 1/\sqrt\varphi$ exactly — algebraic where $\pi/4$ is transcendental by Lindemann's theorem. Second, the *difference* between the two predictions is $\hat\pi/4 - \pi/4 = 1/\sqrt\varphi - \pi/4 = 0.0007532143599749765\ldots$ per unit of $ab\cos C$, and unlike the areas themselves that number has no algebraic closed form at all, because a transcendental term survives subtraction. That is the signature of a real test: where the constant is truly present, no amount of algebraic dressing removes it.

The single-lune scan is equally instructive. Since $\hat\pi/4 = 1/\sqrt\varphi$ and $\sin^2(\theta/2)$ does not depend on any labelling, the condition for the golden lune to be constant-free is $\hat\pi\sin^2(\theta/2) = \theta$ — the same equation with a different coefficient of $\pi$. The root pattern does not change: $90°$ remains the unique non-degenerate angle, because the root is fixed by the *structure* (a semicircle's area against a segment's), not by the size of the constant. The golden lune at $90°$ is $1/2$; at $60°$ it reads $0.3024896152$ where the conventional arithmetic gives $0.3021130080$.

There is one more thing worth naming. Golden Pi squares the circle exactly: a circular area with radius $r = \varphi^{1/4}$ is precisely $4$, because $\hat\pi r^{2} = (4/\sqrt\varphi)\cdot\sqrt\varphi = 4$. The lune says nothing about that, and the lune is not a weaker result for it — it is a different one. A curve-free area can be squared because of a right angle; a disc's area can be squared under Golden Pi because of $\hat\pi^{2}=16/\varphi$. Confusing the two is exactly the mistake the next section is about.

## The History: What Hippocrates Actually Proved

The lunes reach us through Simplicius, writing in the sixth century CE in his commentary on Aristotle's *Physics*, quoting Eudemus of Rhodes' fourth-century-BCE *History of Geometry*. The attribution to Hippocrates of Chios — a contemporary of Socrates, a merchant who reportedly lost his goods to pirates and turned to geometry — is Eudemus', and it is the earliest named piece of Greek quadrature work we have. What Hippocrates squared was a curvilinear figure; the claim that he squared *the circle* is a later accretion, and the historical consensus is that he did not make it, though he is reported to have attempted a quadrature by a related route.

Two facts sit on either side of that report and neither has moved in twenty-four centuries. First: a region bounded entirely by arcs can have exactly the area of a rectilinear figure — $1/2$ and $6.000000000000$ in the two worked cases above — and the square on it can be drawn with straightedge and compass, because $1/4$ has a constructible square root. Second: the same trick fails for the disc, and the failure is not a matter of ingenuity. The disc's area is $\pi r^{2}$; the constant is transcendental (Lindemann, 1882), and Wantzel's 1837 degree criterion admits only lengths algebraic of degree $2^{k}$ into straightedge-and-compass constructions. The lune escapes because the constant cancels *before* the answer; the circle cannot, because the constant *is* the answer.

## What a Lune Can and Cannot Decide

The lune's honesty is its narrowness. It is a theorem about ideal figures whose areas are computed — a semicircle's $\tfrac{\pi}{2}r^{2}$ and a segment's $\tfrac{R^{2}}{2}(\theta-\sin\theta)$ are limits of exhausted polygons, never readings off an object. No physical lune has ever been cut from sheet metal and weighed to test a circle constant, and none could: to know a lune's area you must already know the constant you are testing, which is why the right-angle case is the only one in which the test dissolves into an identity.

So the exact ledger for this figure is short and unglamorous:

- The right-angle quadrature is exact, constant-free, and invariant under any relabelling of $\pi$ — golden, conventional, or otherwise.
- The off-right-angle lune contains $\pi$ at first power, with coefficient $\tfrac14 ab\cos C$, and golden arithmetic moves that term by $ab\cos C(1/\sqrt\varphi - \pi/4)$.
- Neither case can adjudicate between the two labels, because in the first the constant is multiplied by zero and in the second the figure is defined by the constant rather than the other way round.

What the lune does decide — and this is the part that has never been in dispute — is that "curvilinear" does not automatically mean "not squareable". It decided that in the fifth century BCE, with two arcs and a chord, and it has never needed revising.

## Further Reading

- [The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass Forever, Why 4/√φ Never Reaches That Door](/blog/posts/2026-10-29-constructible-numbers-squaring-circle-lindemann-golden-pi/) — the degree argument that closes the circle after the lune opened it.
- [Squaring the Circle: The Golden Pi Geometric Proof](/blog/posts/squaring-circle-golden-pi-geometric-proof/) — the radius $\varphi^{1/4}$ construction that makes a disc's area exactly $4$.
- [The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — the chord-and-arc relations the lune is built from.
- [Brahmagupta's Cyclic Quadrilateral: Why a Four-Sided Area Needs No Circle Constant](/blog/posts/2026-11-09-brahmagupta-cyclic-quadrilateral-area-half-turn-golden-pi/) — another area formula that names a circle and never uses its constant.
- [Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°](/blog/posts/2026-10-22-descartes-angle-defect-gauss-bonnet-720-degrees-golden-pi/) — the same structural blindness, one dimension up.
