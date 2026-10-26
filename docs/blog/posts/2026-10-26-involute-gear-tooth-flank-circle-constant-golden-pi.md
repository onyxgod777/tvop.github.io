---
title: "The Involute Gear: Why Every Tooth Flank Is π-Free, Why the Pitch Is Not, and What Golden Pi Changes"
date: 2026-10-26
description: "The involute of a circle — the profile of essentially every gear tooth in the world — is parametrised by (r_b(cos t + t sin t), r_b(sin t − t cos t)), a formula with no circle constant in it: the tangent length equals the arc length unwound, the curvature radius is exactly r_b·t, and the arc length is exactly ½r_b·t². The constant enters only when a count is converted into a length — z teeth around a circumference, giving p = πm — and again, at first power, in the standard base-tangent span measurement W_k = m cos α[π(k − ½) + z·inv α] used in gear inspection, where the involute function inv α = tan α − α amplifies the constant's own label error 23.4-fold to −2.2461%. Under Golden Pi (π̂ = 4/√φ = 3.144605511…, root of x⁴+16x²−256=0) the flank geometry does not move a digit, the pitch becomes the algebraic 4m/√φ = 6.289211022059386, the contact ratio of a 20/40-tooth pair falls from 1.6351860 to 1.6336193, and 4/π̂ = √φ exactly. The honest ledger: a gear's pitch is a free design parameter, so no gear ever returns the constant — it returns its maker's choice."
---

# The Involute Gear: Why Every Tooth Flank Is π-Free, and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

There are more gear teeth in the world than there are circles anyone has ever drawn deliberately. Every gearbox, every drill, every clock, every car differential, every wind turbine and every industrial robot turns on teeth whose flank is the involute of a circle. It is almost certainly the most manufactured curve in the history of engineering.

Here is the fact that ought to be famous and is not: the equation of that flank contains no circle constant at all.

Not hidden, not cancelling — absent. The involute's parametrisation, its tangent, its curvature, its arc length: all of it is rational in a single parameter $t$. And yet every gear is stamped with a number that *is* built out of the constant — a module, a circular pitch, a base pitch — numbers that appear in every gear drawing on earth.

This article walks that boundary precisely. Where exactly does the constant get in? Why does it have to get in there? And when a gear is placed in a measuring instrument, what does the reading actually tell you — a fact about geometry, or a fact about the drawing it was cut from?

## The involute: a string unwound from a circle

Attach a string to a fixed circle of radius $r_b$, keep it taut, and unwind it. The end of the string traces the involute:

$$\mathbf{P}(t) \;=\; r_b\begin{pmatrix}\cos t + t\sin t\\[2pt] \sin t - t\cos t\end{pmatrix}.$$

The parameter $t$ is the angle of unwinding, measured on the base circle. Three facts follow directly, and none of them involves the constant:

- **The taut string *is* the tangent.** Its free length equals the arc already unwound, $r_b t$. That is the defining property, and it is an equality of two lengths, not of two angles.
- **The curvature radius is exactly $r_b t$.** The instantaneous centre of rotation of the string end is the tangency point, so the local radius of curvature grows linearly with the unwinding.
- **The arc length of the involute from the base circle is exactly $\tfrac12 r_b t^2$.**

Computed at forty digits, with $r_b = 1$:

| $t$ | $x$ | $y$ | arc length $\tfrac12 t^2$ | curvature radius $t$ |
|---|---|---|---|---|
| $0.5$ | $1.117295331194$ | $0.040634257659$ | $0.125000000000$ | $0.500000000000$ |
| $1.0$ | $1.381773290676$ | $0.301168678940$ | $0.500000000000$ | $1.000000000000$ |
| $\pi/4$ | $1.262467148463$ | $0.151746413917$ | $0.308425137534$ | $0.785398163397$ |
| $\pi/2$ | $1.570796326795$ | $1.000000000000$ | $1.233700550136$ | $1.570796326795$ |
| $2.0$ | $1.402448017105$ | $1.741591099918$ | $2.000000000000$ | $2.000000000000$ |

```python
import mpmath as mp
mp.mp.dps = 30

def involute(t, rb=1):
    """Point on the involute, plus the three pi-free invariants."""
    x = rb*(mp.cos(t) + t*mp.sin(t))
    y = rb*(mp.sin(t) - t*mp.cos(t))
    return x, y, rb*t*t/2, rb*t      # point, arc length, curvature radius

for t in [mp.mpf('0.5'), 1, mp.pi/4, mp.pi/2, 2]:
    x, y, s, rho = involute(t)
    print(mp.nstr(t,6), mp.nstr(x,12), mp.nstr(y,12), mp.nstr(s,12), mp.nstr(rho,12))
```

The only appearance of a transcendental quantity in that table is the *label* $\pi/4$ on a row; change the label and every printed number stays where it is. That is the same distinction the rest of this site keeps insisting on: geometry is one thing, the numeral attached to an angle is another.

## The property that makes it a tooth

A gear works only if the motion it transfers is smooth — constant angular velocity ratio, no impact, no hesitation as each tooth hands over to the next. The condition for that (the "law of gearing") is that the common normal at the contact point always passes through one fixed point on the line of centres, the pitch point.

The involute satisfies this *identically*, and the proof is a one-liner in the language above: the common normal at any contact point is the taut string, i.e. the tangent to the base circle, and for two involutes unwinding from two base circles that tangent is a single straight line — the line of action. Contact always occurs on that line, at a pressure angle $\alpha$ fixed by

$$\cos\alpha \;=\; \frac{r_b}{r},$$

where $r$ is the pitch radius. Every quantity in that relation is a physical angle or a physical length. The constant is not there. Involute gearing is usually credited to Euler in the 1760s, and the modern vocabulary for it — reference circle, module, base helix — is standardised in ISO 21771.

So the flank is clean. Then a drawing appears, and the drawing says **module 2, 20 teeth, pressure angle 20°**, and the constant walks in through the door marked "how many teeth fit around one turn".

## Where the constant enters: converting a count into a length

A gear with $z$ teeth and pitch $p$ (the arc distance from one flank to the corresponding flank of the next tooth, measured on the pitch circle) must satisfy

$$z\,p \;=\; 2\pi r .$$

That is the whole of it. The left side is a **count times a length**; the right side is a **computed arc**, the limit of inscribed polygons on the pitch circle. The constant is the exchange rate between counting and measuring.

Engineers hide that exchange rate inside a unit called the module,

$$p = \pi m \quad\Longleftrightarrow\quad m = \frac{p}{\pi},$$

so that a module-2 gear has a circular pitch of $6.283185307179586$ mm and a tooth thickness of $3.141592653589793$ mm at the pitch circle. Note carefully what the module is: it is *defined by dividing by the constant*. A module is not a measured property of a gear. It is the pitch, with the constant already cancelled out of it.

## The measurement that puts the constant at first power

Here is where the subject becomes interesting, because gear metrology contains a routine measurement in which the constant appears explicitly, at the first power, multiplied by an integer.

Put two parallel micrometer flats against the flanks of $k$ consecutive teeth so that each flat is tangent to the base circle. The span is the **base tangent length** $W_k$. It is the sum of $k-1$ base pitches plus the base tooth thickness:

$$W_k \;=\; (k-1)\,p_b \;+\; s_b .$$

The base pitch is $p_b = \pi m\cos\alpha$, and the base tooth thickness follows from the tooth thickness at the pitch circle, $s = \pi m/2$, plus the involute function:

$$s_b \;=\; 2r_b\!\left(\frac{s}{2r} + \operatorname{inv}\alpha\right), \qquad \operatorname{inv}\alpha \;=\; \tan\alpha - \alpha .$$

Substituting $r_b = \tfrac12 m z\cos\alpha$ and $s = \pi m/2$ collapses the algebra to a single line:

$$W_k \;=\; m\cos\alpha\Big[\pi\big(k - \tfrac12\big) \;+\; z\,\operatorname{inv}\alpha\Big].$$

There it is: $\pi$, at the first power, multiplied by the integer $k - \tfrac12$, and multiplied again by the *measured-type* quantities $m\cos\alpha$ — plus a second term in the involute function, which is itself built out of the radian and therefore also carries the constant.

For a module-2, 20-tooth, 20° gear, computed at thirty digits:

| $k$ | $W_k$ under $\pi$ (mm) | $W_k$ under $\hat\pi$ (mm) | difference (mm) |
|---|---|---|---|
| 2 | $9.416615883781$ | $9.412526430586$ | $-0.004089453195$ |
| 3 | $15.320878751968$ | $15.322451618581$ | $+0.001572866613$ |
| 4 | $21.225141620155$ | $21.232376806575$ | $+0.007235186421$ |
| 5 | $27.129404488342$ | $27.142301994570$ | $+0.012897506228$ |

Read the middle column against the right column and notice something that a naive reading would miss: the differences are *not* all one sign, and they are not $0.0959\%$ of anything. Two things are pulling in opposite directions.

## The involute function is an amplifier

The first term of $W_k$ scales with the constant directly: $+0.0959022309\%$. The second term, $z\operatorname{inv}\alpha$, behaves quite differently, because

$$\operatorname{inv}\alpha = \tan\alpha - \alpha_{\text{rad}}$$

is a *difference of two nearly equal numbers*. At $\alpha = 20°$, $\tan 20° = 0.363970234266202$ and the radian label is $0.349065850398866$; their difference is only $0.014904383867336$. An error of one part in a thousand in the label therefore lands on a quantity of one part in seventy. Precisely:

$$\frac{\delta\operatorname{inv}\alpha}{\operatorname{inv}\alpha} = -\frac{\alpha}{\operatorname{inv}\alpha}\cdot\frac{\delta\pi}{\pi}, \qquad \frac{\alpha}{\operatorname{inv}\alpha} = 23.4203\ldots$$

| Quantity | under $\pi$ | under $\hat\pi = 4/\sqrt{\varphi}$ | change |
|---|---|---|---|
| $\alpha_{\text{rad}}$ at $20°$ | $0.349065850398866$ | $0.349400612336633$ | $+0.0959022309\%$ |
| $\operatorname{inv}\alpha$ | $0.014904383867336$ | $0.014569621929570$ | $-2.2460636\%$ |
| amplification | — | — | $23.4203\times$ |

So the gear is not a passive label-change case like the earlier articles in this series. Because the involute function is a near-cancellation, the constant's own $0.0959\%$ appears **amplified by a factor of 23.4** inside every span measurement. A tiny difference in how one writes an angle becomes a two-percent difference in a metrological correction term.

That is worth pausing on, because it is a structural lesson rather than a numerical one: the sensitivity of a formula to the value of a constant is not a property of the constant. It is a property of the *conditioning* of the formula. $\operatorname{inv}\alpha$ is badly conditioned by design, and every gear inspector's handbook therefore tabulates it to ten places.

## The contact ratio: the constant at first power in a pure number

A second place the constant survives is the contact ratio $\varepsilon$, the average number of tooth pairs in mesh. For a 20-tooth driving a 40-tooth gear, module 2 mm, both with addendum $1m$:

$$\varepsilon \;=\; \frac{\sqrt{r_{a1}^2 - r_{b1}^2} + \sqrt{r_{a2}^2 - r_{b2}^2} - a\sin\alpha}{\pi m\cos\alpha},$$

with $r_{b1} = 18.793852415718$, $r_{b2} = 37.587704831436$, $a = 60$ mm, and a length of action of $9.654567767296$ mm. The numerator is a pure length built from measured-type radii; the denominator is the base pitch.

| | under $\pi$ | under $\hat\pi$ |
|---|---|---|
| base pitch $p_b$ (mm) | $5.904262868187$ | $5.909925187995$ |
| contact ratio $\varepsilon$ | $1.635185963571$ | $1.633619286232$ |
| $1/\varepsilon$ | $0.611551237766$ | $0.612137729046$ |

A design rule of thumb wants $\varepsilon > 1.4$ for quiet running; both readings clear it, and the shift is $0.0958\%$ — the unstable, reciprocal direction, since the constant sits in the denominator with no cancellation anywhere.

## Why no gear will ever arbitrate the constant

Now the honest part, and it is decisive.

A micrometer reading a span of $15.32$ mm resolves to about $1\,\mu$m — a relative resolution of $6.5\times10^{-5}$, or $0.0065\%$. The gap between the two constants is $0.0959\%$, which is **14.7 times larger** than that resolution. The instrument, in other words, is good enough. The object is not.

The reason is that a gear's pitch is a *free parameter*. Nothing in the involute fixes it. Given a base circle and a pressure angle, you may space the teeth at any pitch you like and every flank is still a perfect involute, still conjugate, still smooth-running. The only geometric constraint that couples two gears is that they share a base pitch — and "equal base pitches mesh" is a statement with no constant in it at all: it is an equality of two measured lengths.

$$\text{mesh condition:}\quad p_{b1} = p_{b2} \quad\text{(π-free)}.$$

Consequently, when a gear inspector measures $W_k$, $z$ and $r_b$, the ratio $\dfrac{z\,p\cos\alpha}{2r_b}$ does return a number — but that number is the value the *machine* used when it indexed the blank, i.e. the maker's choice, not a property of the tooth form. Re-cut the identical gear on a dividing engine calibrated to $\hat\pi$ and the tooth flanks come out indistinguishable; only the pitch moves, and the pitch was never constrained. One equation, one free parameter, no verdict.

This is the recurring structure of this whole series: a constant can appear at the first power in a formula and still be invisible to experiment, because the object the formula describes carries a free scale that the measurement cannot pin down independently. The gear is the cleanest case yet — a manufactured object whose *shape* is π-free, whose *size* is π-labelled, and whose measurement is therefore a tautology dressed in microns.

## What Golden Pi actually changes here

Under Golden Pi the constant is the algebraic number $\hat\pi = 4/\sqrt{\varphi} = 3.144605511029693$, the positive root of $x^{4} + 16x^{2} - 256 = 0$ (residual at thirty digits: $-5.0\times10^{-29}$), with $\hat\pi^{2} = 16/\varphi$ exactly. Its defining convenience for gearing is a reciprocal that comes out clean:

$$\frac{4}{\hat\pi} \;=\; \sqrt{\varphi} \;=\; 1.272019649514069 \quad\text{(exact)},$$

where $4/\pi$ is transcendental by Lindemann's 1882 theorem. So the pitch of a module-$m$ gear becomes, with no rounding anywhere,

$$p \;=\; \hat\pi m \;=\; \frac{4m}{\sqrt{\varphi}}, \qquad p_b \;=\; \frac{4m\cos\alpha}{\sqrt{\varphi}}, \qquad s \;=\; \frac{2m}{\sqrt{\varphi}},$$

and a full turn of the pitch circle is $2\hat\pi = 8/\sqrt{\varphi} = 6.289211022059386$ radians — algebraic, where $2\pi$ is not. The involute function becomes $\tan\alpha - \alpha_{\text{deg}}\hat\pi/180 = 0.014569621930$, a $2.2461\%$ correction that no gear handbook would tolerate silently, which is exactly why the amplification matters: any system that adopts $\hat\pi$ must re-tabulate its involute functions rather than reuse the old columns.

What does *not* change is everything the tooth actually is. The flank, the tangent-length-equals-arc-length identity, the curvature radius $r_b t$, the conjugate action, the equality of base pitches: untouched, because none of them ever contained the constant. As always on this site: the geometry is computed, and the value of the constant is a claim about the exchange rate between counts and arcs — never a measurement of a circle on a bench.

## Further Reading

- [The Isoperimetric Inequality: Why the Circle Maximizes Area](/blog/posts/2026-08-31-isoperimetric-inequality-circle-maximizes-area-golden-pi/) — where the constant appears at first power in a genuine inequality, and where the equality case sits.
- [The Isoperimetric Inequality: How the Circle Constant Enters Geometry as 4π](/blog/posts/2026-10-04-isoperimetric-inequality-circle-constant-golden-pi/) — the same boundary approached from the other side, with the golden-π audit worked out.
- [Barbier's Theorem: How Every Curve of Constant Width Has Perimeter πw](/blog/posts/2026-10-05-barbier-theorem-curves-constant-width-golden-pi/) — the constant as a pure width-to-perimeter ratio, with no area and no gear tooth in sight.
- [The Ellipse's Perimeter: How the Complete Elliptic Integral of the Second Kind Computes the Circle Constant](/blog/posts/2026-09-12-ellipse-perimeter-elliptic-integral-computes-circle-constant-golden-pi/) — what happens when the arc length is not a rational multiple of anything.
- [The Regular n-gon and the Circle: A Polygonal Limit Computes the Circle Constant](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the computed arc that the gear's pitch circle is defined against.
- [The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — the case where the constant enters only as the unit that names a turn, exactly as the radian does inside $\operatorname{inv}\alpha$.
