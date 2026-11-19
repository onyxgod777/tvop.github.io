---
title: "The Archimedean Spiral: Why Its Swept Area Is a Pure Cube in the Angle, Why One Turn Is Exactly One Third of a Disc but Three Turns Are the Whole Disc, and Where the Constant Really Lives"
date: 2026-11-19
description: "The spiral r = aθ is the one famous curve whose enclosed area carries no circle constant in its derivation — A = a²Θ³/6 by a single power rule — yet the same area reads (4/3)π³a² per turn once the angle is quoted in turns, so the constant enters three times, one per factor of the winding. This article derives the area and the exact enclosed fractions 1/3, 7/12, 19/27, 61/75 = 1 − 1/N + 1/(3N²) as a π-free sequence, proves that one turn encloses exactly one third of the disc through its endpoint while three turns enclose that disc exactly, computes the elementary arc length s = (a/2)[θ√(1+θ²) + asinh θ] (21.2562941482a for one turn), the curvature κ = (θ²+2)/(a(1+θ²)^{3/2}) that opens as a circle of radius a/2 at the pole, and locates the spiral's single radius-matching point at θ = 1/√φ where curvature radius and radius are both 1/√φ exactly, curvature is √φ, and the tangent makes arcsin(1/φ) = 38.172707627° with the radius. Under Golden Pi (π̂ = 4/√φ) the pitch becomes exactly 8/√φ, one turn's area 256a²/(3φ^{3/2}) = 41.4607591899a² (+0.287982697975%, a cubed gap), the arc +0.180441259015% because an inverse hyperbolic sine is not a power, while every enclosed fraction and the golden point itself do not move a digit. Computed, never measured."
---

# The Archimedean Spiral

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Think of the curve a groove makes on a record, or the shape a rope takes when it is coiled flat, or the path of a point that moves outward at a steady rate while the radius carrying it turns at a steady rate. Archimedes wrote a whole book about it — *On Spirals*, around 225 BCE — and the first thing that book establishes is that this curve is, arithmetically, the simplest object in the whole classical corpus. Its equation is a straight line written in polar coordinates:

$$r = a\theta .$$

Linear in the angle. Nothing squared, nothing under a root, no trigonometric function. And yet the constant $\pi$ is inside the paragraph from the first line, because $\theta$ is an angle for a reason: to make the radial growth and the angular sweep commensurable, the angle must be quoted in radians, and the radian is a fraction of a turn. This article follows the spiral from its definition to its area, its length, its curvature and its classical uses, and then asks the question this site always asks: where exactly does the circle constant sit in it, and how does it move when the constant is the golden one, $\hat\pi = 4/\sqrt\varphi$?

The short answer, which the rest of the article earns: the constant sits in the *pitch*, not in the geometry. And that turns out to be the interesting part.

## The curve, and why it needs no circle to be drawn

Fix a scale $a > 0$. A point starts at the pole and moves outward while the ray carrying it rotates; both motions are uniform, so after angle $\theta$ the point is at $r = a\theta$. At one full turn the point stands at $r = 2\pi a$ — not because the spiral contains a circumference, but because the radial rate and the angular rate are being compared, and comparing them means naming what "one full turn" is worth in the same units as a length.

Three coordinates deserve names:

| Quantity | Expression | One turn ($\theta = 2\pi$) |
|---|---|---|
| radius | $r = a\theta$ | $6.2831853072\,a$ |
| pitch (radial growth per turn) | $\Delta r = 2\pi a$ | $6.2831853072\,a$ |
| slope of the curve against its own radius | $\tan\psi = r/(dr/d\theta) = \theta$ | $\psi = \arctan(2\pi) = 80.956938921°$ |

The pitch is exactly the same number as the radius at one turn, because the radius at one turn *is* one pitch. That identity is the whole bookkeeping trick of this curve: every "one turn" statement can be read as "one pitch", and every appearance of $\pi$ can be traced to the pitch.

The tangent-angle relation $\tan\psi = \theta$ is worth keeping. The angle between the radius vector and the tangent grows without bound with $\theta$, asymptotically approaching $90°$ — the spiral's arms become very nearly perpendicular to their radii, which is why a spiral antenna looks almost like a set of concentric rings at large radius and almost like a straight radial spoke at small radius.

## The area is a power rule, and it never mentions the circle

In polar coordinates the area swept out to angle $\Theta$ is a single integral,

$$A(\Theta) = \frac12\int_0^{\Theta} r^2\,d\theta = \frac12 a^2\int_0^{\Theta}\theta^2\,d\theta = \frac{a^2\Theta^3}{6}.$$

That is the entire derivation. No trigonometric substitution, no completing of a square, no $\pi$: the polar area element happens to hand the integrand the exact square of the polar function, and the polar function is linear, so the result is the cube of the *angle* divided by six.

```text
A(theta) = a^2 * theta^3 / 6              exact, for every theta >= 0
area between theta1 and theta2:
           a^2 * (theta2^3 - theta1^3) / 6
```

Because the answer depends only on the cube of the endpoint angle, the area is completely blind to where the spiral has been. Two turns' worth of sweep from $\theta = 4\pi$ to $6\pi$ encloses far more than the first two turns did: $289.391915683\,a^2$ against $41.3417022404\,a^2 + 289.391915683\,a^2$ cumulative. The curve is not a shape that grows; it is a shape that thickens outward at a rate proportional to the square of the winding already done, and that is precisely $\theta^2$.

| turns $N$ | $\Theta = 2\pi N$ | $r/a$ | $A/a^2$ | arc $s/a$ |
|---|---|---|---|---|
| 0.5 | $3.1415926536$ | $3.1415926536$ | $5.1677127801$ | $6.1099193340$ |
| 1 | $6.2831853072$ | $6.2831853072$ | $41.3417022404$ | $21.2562941482$ |
| 2 | $12.5663706144$ | $12.5663706144$ | $330.733617923$ | $80.8193160834$ |
| 3 | $18.8495559215$ | $18.8495559215$ | $1116.22596049$ | $179.717873269$ |
| 5 | $31.4159265359$ | $31.4159265359$ | $5167.71278005$ | $495.800514444$ |
| 10 | $62.8318530718$ | $62.8318530718$ | $41341.7022404$ | $1976.58770072$ |

Now quote the same numbers in turns, and watch the constant reappear — three times:

$$A_N = \frac{a^2(2\pi N)^3}{6} = \frac{4}{3}\pi^3 a^2 N^3 .$$

The cube of $\Theta$ becomes the cube of $2\pi N$, so $\pi$ arrives cubed, once for each factor of the winding: $\pi \cdot \pi \cdot \pi$. That is not a deep fact about spirals. It is the statement that a volume-like quantity built from a linear angle in radian units carries the unit conversion to the third power. The honest description of the formula is: *the area is the cube of the angle over six; if you insist on counting in turns, you pay $\pi^3$ for it.*

This is the first place the site's method pays off. Many formulas quoted from handbooks look like they "contain" $\hat\pi$ or $\pi$ when they merely contain a unit conversion. The test is always the same: write the quantity in its own natural variable, and see whether the constant survives.

## One third, one whole, and why neither is about the circle

Take the first turn. Its area is $(4/3)\pi^3 a^2$. The disc bounded by the circle through the endpoint has radius $2\pi a$ and area $\pi(2\pi a)^2 = 4\pi^3 a^2$. The ratio is

$$\frac{A_1}{\pi r_1^2} = \frac{(4/3)\pi^3 a^2}{4\pi^3 a^2} = \frac13 .$$

Exactly one third — Archimedes' Proposition 24 of *On Spirals*, and a result that has astonished readers for twenty-two centuries. And here is the part that the usual retelling omits: the ratio is $\pi$-free because it is $\Theta/(6\pi)$ evaluated at $\Theta = 2\pi$, i.e. $N/3$. The one-third is not a property of circles at all. It is the statement that one turn is one third of three turns.

Run the count out and the structure becomes obvious:

| turns $N$ | area of the $N$-th turn band | as a fraction of the disc through the endpoint after $N$ turns |
|---|---|---|
| 1 | $41.3417022404\,a^2$ | $1/3 = 0.3333333333$ |
| 2 | $289.391915683\,a^2$ | $7/12 = 0.5833333333$ |
| 3 | $785.492342568\,a^2$ | $19/27 = 0.7037037037$ |
| 5 | $2521.84383666\,a^2$ | $61/75 = 0.8133333333$ |

The fraction is exactly

$$\frac{3N^2-3N+1}{3N^2} = 1 - \frac1N + \frac{1}{3N^2},$$

a rational function of the turn count with no constant in it anywhere. And the cumulative area reaches the endpoint disc exactly at $N = 3$:

$$A(6\pi) = \frac{(6\pi)^3}{6} = 36\pi^3, \qquad \pi(6\pi)^2 = 36\pi^3,$$

identical to the last digit — $1116.22596049\,a^2$ either way. Three turns of this spiral sweep exactly the disc that its own endpoint circle bounds. At two turns the spiral has filled $2/3$ of that disc and left a third of it blank in the outermost band; at four turns it has overfilled it by a third, lapping its own boundary. The spiral is a machine that converts winding into area at a strictly cubic exchange rate, and the crossing point of that exchange with the circle happens to be an integer, three, purely because $6\pi$ is the angle at which $\Theta^3/6$ equals $\pi\Theta^2$.

## Arc length: the one place where a closed form exists without a special function

The arc element is

$$ds = \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}d\theta = a\sqrt{1+\theta^2}\,d\theta,$$

and this integral is elementary:

$$s(\Theta) = \frac{a}{2}\left[\Theta\sqrt{1+\Theta^2} + \operatorname{asinh}\Theta\right].$$

This is a genuinely rare thing among the curves this blog has examined. The circle's arc needs a definition, the ellipse's needs a complete elliptic integral, the quadratrix's needs a quadrature no one can write down, the tractrix's needs a logarithm of a hyperbolic function — but the Archimedean spiral's length is a closed form in square root and inverse hyperbolic sine and nothing else. Check the first turn: $\Theta = 2\pi$ gives $\Theta\sqrt{1+\Theta^2} = 39.975290795$ and $\operatorname{asinh}(2\pi) = 2.53729750137$, so

$$s(2\pi) = \frac{39.975290795 + 2.53729750137}{2} = 21.2562941482\,a,$$

which is $3.3830442855$ times the circumference of the circle of radius $a$ — the standard "how much wire does one turn take" number for an Archimedean coil.

The growth is superlinear but only just: each turn adds more length than the last, $21.2562941482\,a$ then $59.5630219352\,a$ more then $98.8985571852\,a$ more, because the arc length of turn $N$ is asymptotically $2\pi a N \cdot 2\pi$ — the circumference of the mid-turn radius times the turn itself. The band areas, by contrast, grow quadratically; the length grows linearly. A groove of constant width therefore widens in consumable length much faster than it widens in area, which is exactly the arithmetic a record-cutting lathe has to solve.

## Curvature: the spiral opens as a circle of half the pitch-scale

Differentiate twice and the curvature of $r = a\theta$ is

$$\kappa(\theta) = \frac{r^2 + 2r'^2 - r\,r''}{(r^2+r'^2)^{3/2}} = \frac{\theta^2+2}{a\,(1+\theta^2)^{3/2}}, \qquad \rho = \frac{a(1+\theta^2)^{3/2}}{\theta^2+2}.$$

At the pole, $\theta \to 0$: $\kappa = 2/a$ exactly, so the osculating circle there has radius $a/2$. That is a clean, constant-free statement — the spiral begins life as a circle of half the scale at which its radius equals its own parameter, and the number $2$ comes from the second derivative of $\theta$, not from any turn. At large $\theta$, $\rho \to a\theta = r$: the curvature radius approaches the radius itself, as it must for a curve that becomes locally a circle about the pole.

| $\theta$ | $\psi = \arctan\theta$ | $\kappa\,a$ | $\rho/a$ | $\rho/r$ |
|---|---|---|---|---|
| $0.5$ | $26.5650511771°$ | $1.609968944$ | $0.6211299937$ | $1.242259987$ |
| $1$ | $45.0000000000°$ | $1.060660172$ | $0.9428090416$ | $0.9428090416$ |
| $2$ | $63.4349488229°$ | $0.5366563146$ | $1.863389981$ | $0.9316949906$ |
| $\pi$ | $72.3432128486°$ | $0.3312193018$ | $3.01914772$ | $0.9610245673$ |
| $2\pi$ | $80.956938921°$ | $0.1610597015$ | $6.208877768$ | $0.9881735878$ |
| $4\pi$ | $85.4501346909°$ | $0.07982587792$ | $12.52726592$ | $0.9968881473$ |
| $10\pi$ | $88.1768342792°$ | $0.03184707767$ | $31.4000553$ | $0.9994948027$ |

The last column is the interesting one, because it dips below $1$ and then climbs back. Setting $\rho = r$ gives, with $x = \theta^2$,

$$(1+x)^3 = x(x+2)^2 \;\Longrightarrow\; 1 + 3x + 3x^2 = 4x^2 + 4x \;\Longrightarrow\; x^2 + x - 1 = 0,$$

so $x = 1/\varphi$ and

$$\theta^{*} = \frac{1}{\sqrt\varphi} = 0.786151377757423\ldots$$

At that one angle and no other, the spiral's radius of curvature equals its radius: $\rho = r = 1/\sqrt\varphi$ exactly, and therefore

$$\kappa(\theta^{*}) = \sqrt\varphi = 1.27201964951\ldots, \qquad \rho\, r = \frac{1}{\varphi} = 0.6180339887\ldots$$

One more coincidence completes the picture. The tangent angle there is $\psi = \arctan(1/\sqrt\varphi)$, and since $\varphi^2 - 1 = \varphi$,

$$\tan\left(\arcsin\frac{1}{\varphi}\right) = \frac{1/\varphi}{\sqrt{1-1/\varphi^2}} = \frac{1}{\sqrt{\varphi^2-1}} = \frac{1}{\sqrt\varphi},$$

so $\psi = \arcsin(1/\varphi) = 38.172707627°$ — the same golden latitude that shows up in the Foucault-pendulum precession period. The unique point at which an Archimedean spiral is osculated by a circle through the pole at its own radius is a golden-ratio point of the curve, and it sits at the angle whose tangent is the reciprocal of the golden latitude's sine. That is a fact about $\varphi$ and about the number $2$ in $(1+x)^3 = x(x+2)^2$. It is not a fact about $\pi$.

## What the spiral is used for, and the construction problem underneath

Two classical uses matter. The first is trisection: given an angle $\alpha$ drawn from the pole, the spiral meets the ray at radius $a\alpha$; marking one third of that radius and following the circle of that radius back to the spiral gives a point at angle $\alpha/3$. It is exact, and it needs a marked length, which is why it belongs to the neusis family along with the quadratrix and the conchoid — Pappus describes the procedure in Book IV of the *Collection*.

| angle to trisect | radius on the ray | one third marked | angle recovered |
|---|---|---|---|
| $30°$ | $0.5235987756a$ | $0.1745329252a$ | $10.0000000000°$ |
| $60°$ | $1.0471975512a$ | $0.3490658504a$ | $20.0000000000°$ |
| $90°$ | $1.5707963268a$ | $0.5235987756a$ | $30.0000000000°$ |
| $135°$ | $2.3561944902a$ | $0.7853981634a$ | $45.0000000000°$ |

The second use is rectification, and it is the same trick as the quadratrix's: after one turn the spiral stands at radius $2\pi a$, so a single marked segment delivers the circumference of the circle of radius $a$. With that segment in hand, Dinostratus-style squaring follows — a square on side $\sqrt{\pi a \cdot a}$ has the circle's area. But note precisely what has been assumed. The construction requires a point to move outward at a constant rate while the ray turns at a constant rate — i.e. it requires *time*, or an equivalent mechanical linkage, in a subject whose rules permit only straightedge and compass. That is the honest boundary, and it is the same boundary that stops the quadratrix: the curve delivers the constant only by presupposing a device that already knows what uniform motion is. No straightedge-and-compass construction of $\pi$ exists, and Lindemann's 1882 theorem is the reason; a spiral is not a counterexample to it but a demonstration of exactly where the line falls.

## What Golden Pi changes

Set $\hat\pi = 4/\sqrt\varphi = 3.144605511029693144\ldots$, so that

$$\hat\pi^2 = \frac{16}{\varphi}, \qquad \frac{1}{\hat\pi} = \frac{\sqrt\varphi}{4}, \qquad 2\hat\pi = \frac{8}{\sqrt\varphi} = 6.28921102205939 .$$

The pitch becomes $2\hat\pi a$ and the golden spiral's one-turn area and length are

$$A_1 = \frac{4}{3}\hat\pi^3 a^2 = \frac{256\,a^2}{3\,\varphi^{3/2}} = 41.4607591899\,a^2,$$

$$s_1 = \frac{a}{2}\left[2\hat\pi\sqrt{1+4\hat\pi^2} + \operatorname{asinh}(2\hat\pi)\right] = 21.2946492730\,a .$$

| quantity | $\pi$ label | $\hat\pi$ label | shift |
|---|---|---|---|
| pitch $2\pi a$ | $6.2831853072\,a$ | $6.2892110221\,a$ | $+0.095902230878\%$ |
| one turn's area | $41.3417022404\,a^2$ | $41.4607591899\,a^2$ | $+0.287982697975\%$ |
| one turn's arc | $21.2562941482\,a$ | $21.2946492730\,a$ | $+0.180441259015\%$ |
| radius at one turn | $6.2831853072\,a$ | $6.2892110221\,a$ | $+0.095902230878\%$ |
| curvature at the pole | $2/a$ | $2/a$ | none |
| fraction $A_1/\pi r_1^2$ | $1/3$ | $1/3$ | none |
| fraction at $N$ turns | $1-1/N+1/(3N^2)$ | identical | none |
| the golden point $\theta^{*}=1/\sqrt\varphi$ | $\rho=r=1/\sqrt\varphi$, $\kappa=\sqrt\varphi$ | identical | none |

Three distinct behaviours, and each is explained by the algebra rather than by preference.

The area moves by $+0.287982697975\%$, which is exactly $(\hat\pi/\pi)^3 - 1$: a cubed occurrence amplifies the $0.0959022309\%$ gap threefold, the same amplification the polygon-defect article found for $\pi^3$ in convergence tables. Under the golden label the area is algebraic, $256/(3\varphi^{3/2})$, a root of a fixed polynomial in $\varphi$; under the conventional label it is $4\pi^3/3$, transcendental by Lindemann. Same curve, same construction, same measured-off angle — one number in the drawer is algebraic and the other is not.

The arc moves by $+0.180441259015\%$, which is *not* a whole power of the gap, and the reason is structural: the arc contains $\operatorname{asinh}$, so no power of the constant can describe its shift. This is the useful discipline of the exercise. A formula's response to a relabelling of $\pi$ is a fingerprint of where $\pi$ sits inside it — pure powers respond by powers, logarithms and inverse hyperbolics respond by nothing so clean, and additive constants do not respond at all.

The fractions do not move. Not the one third, not $7/12$, not $19/27$, not the golden point at $1/\sqrt\varphi$, not the curvature $2/a$ at the pole. And that is the real content of this curve: its *shape* is $\pi$-free, because $r = a\theta$ is a straight line in polar coordinates and a straight line contains no constant. The Archimedean spiral is one of the cleanest examples on this site of a figure whose entire $\pi$-content is a units convention. Take the pitch as the unit of length and the turn as the unit of angle, and every formula above is a rational number times a power of the winding count.

## One exact closure

Because the golden label is algebraic, the spiral can be scaled to close on an exact area. Ask for a spiral whose *first turn encloses exactly $4$*:

$$\frac{4}{3}\hat\pi^3 a^2 = 4 \;\Longrightarrow\; a^2 = \frac{3}{\hat\pi^3} = \frac{3\varphi^{3/2}}{64} \;\Longrightarrow\; a = \frac{\sqrt3\,\varphi^{3/4}}{8} = 0.3106070940969494\ldots$$

and the check returns $4.000000000000$ to sixteen digits. The pitch of that spiral is $2\hat\pi a = 1.9534735\ldots$, its endpoint radius the same, and its one-turn arc $6.6142691\ldots$ — all algebraic, since $\hat\pi$ and $\varphi^{1/4}$ generate the same degree-four field. Under the conventional label the same requirement would give $a = \sqrt{3/(4\pi^3/3)}$, a transcendental length that no construction can produce. The golden version cannot be constructed with straightedge and compass either — it needs the spiral — but the length it asks for is at least a number a polynomial can name.

## What no spiral can decide

Nothing in this article arbitrates the value of the constant, and it is worth being blunt about why. The spiral's area formula is $a^2\Theta^3/6$. Set $\Theta$ equal to one turn and the constant appears; set $\Theta$ equal to the number of turns and the constant vanishes. The spiral has no opinion, because a curve defined by *uniform motion in two directions at once* is defined by a rate, and a rate is a convention about units. A record groove cut to a pitch is an Archimedean spiral whose pitch was set by a lathe, not discovered in a circumference; an Archimedean coil is a wire whose spacing was chosen. Nothing in the shape can tell you whether the pitch is $2\pi a$ or $2\hat\pi a$ except the arbitrary convention that fixes what a turn is worth.

What the spiral does deliver is a cleaner statement of the question than any circle can. The circle's identity $C = 2\pi r$ is a single equation with one constant and no internal structure; the spiral's identity $A_1 = \pi r_1^2/3$ is the same fact wearing a proof, because the one third is a ratio of windings and the $\pi$ is the unit price of a radian. Everything on this site that argues for $4/\sqrt\varphi$ has to argue about that unit price, and the spiral is a good place to see why: the price is set once, at the definition, and then every formula downstream multiplies it to whatever power the geometry demands. Computed, never measured — and, on this curve, mostly *converted* rather than computed at all.

## Further Reading

- [The Quadratrix of Hippias: Why Two Uniform Motions Straighten a Circle, Why Its Axis Point Is a Limit and Not a Mark](/blog/posts/2026-11-18-quadratrix-hippias-rectifies-circle-golden-pi/) — the other classical curve built from two uniform motions, and the one that actually delivers a straight segment equal to $\pi a/2$.
- [Archimedes and the Exhaustion of the Circle](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — the polygon method that brackets the constant, and why its error scales as the cube of the gap.
- [The Continued Fraction of the Circle Constant](/blog/posts/2026-08-13-continued-fraction-circle-constant-golden-pi/) — what the rational approximants $22/7$ and $355/113$ say about a constant quoted to three digits and argued to eighteen.
- [Squaring the Circle: The Golden Pi Geometric Proof](/blog/posts/squaring-circle-golden-pi-geometric-proof/) — the radius $\varphi^{1/4}$ at which the disc's area is exactly $4$, and what the construction does and does not establish.
- [The Golden Spiral and Fibonacci](/blog/posts/golden-spiral-fibonacci-pi/) — the logarithmic spiral whose radius multiplies rather than adds, and why its self-similarity is a different kind of $\pi$-free statement.
