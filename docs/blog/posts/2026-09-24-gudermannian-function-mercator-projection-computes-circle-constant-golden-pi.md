---
title: "The Gudermannian Function and Mercator's Projection: How a Conformal Map Carries the Circle Constant as a Pure Offset, and What Golden Pi Changes"
date: 2026-09-24
description: "Mercator's 1569 world map is a log-tangent, and the Gudermannian function turns its ordinate back into a latitude via a π/2 offset. Every number in the map is computed, never measured — and here the golden label changes nothing except that one offset."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

There is a chart on the wall of every navigator's education that looks like an ordinary rectangle and is, in fact, an exponential. Gerardus Mercator published it in 1569, and it has been the standard way of drawing the globe ever since, not because it shows areas honestly — it does not — but because it preserves *angles*: a straight line drawn on a Mercator chart is a curve of constant compass bearing. That single property is what made long-range navigation possible, and it is bought with a formula that contains the circle constant in exactly one place.

This article follows that constant through the map. The surprising result is the opposite of what most posts in this series have found: here the circle constant is *bookkeeping*. The map's arithmetic — every ordinate, every scale factor, every bearing, every length in metres — is computed from pure algebra and touches no circle constant at all. Golden Pi (π̂ = 4/√φ = 3.144605511…) changes exactly one number in this whole subject, and that number is not a length. It is an offset. Everything below is computed, never measured.

## The map that stretches latitude

Mercator's construction is simple to state. Keep longitude as it is — the horizontal axis is just λ, the longitudes spread evenly. Stretch the vertical axis by a factor that grows with latitude. The stretch is chosen so that the local distortion is the same in both directions, which is what makes the map conformal (angle-preserving). A degree of latitude is already a fixed length on the sphere, so the horizontal must be stretched to match it: the east–west scale of the map relative to the sphere is exactly \(\sec\phi\), the secant of the latitude.

The ordinate \(y\) that results from integrating that stretch is the log-tangent:

\[
y(\phi) \;=\; \int_0^{\phi} \frac{d\phi'}{\cos\phi'} \;=\; \ln\tan\!\left(\frac{\pi}{4} + \frac{\phi}{2}\right)
\;=\; \operatorname{artanh}(\sin\phi)
\]

The third form is the one worth staring at. \(\operatorname{artanh}(\sin\phi)\) is the inverse hyperbolic tangent of the *sine of the latitude* — pure algebra applied to a ratio of triangle sides. It mentions no circle constant. There is no circle anywhere in it. The second form, \(\ln\tan(\pi/4 + \phi/2)\), appears to contain \(\pi/4\), but \(\pi/4\) rad is simply 45°, a fixed angle of the construction, not a value being computed. Numerically the two forms agree to every digit printed in this article; the table below was produced by evaluating both independently and subtracting.

| latitude φ | ordinate y = artanh(sin φ) | map scale sec φ |
|---|---|---|
| 0° | 0 | 1 |
| 15° | 0.26484224776104581867 | 1.035276180410083 |
| 30° | 0.5493061443340548457 | 1.154700538379252 |
| 38.1727076270° | 0.7218177375894051712466 | **1.2720196495140689643** |
| 45° | 0.88137358701954302523 | 1.4142135623730950488 |
| 51.8272923730° | 1.0612750619025575194 | **1.6180339887498948482** |
| 60° | 1.3169578969248167086 | 2 |
| 75° | 2.0275894218001318691 | 3.863703305156273 |
| 85° | 3.1313013314716450054 | 11.47371324566986 |
| 89.9° | 7.0439589847469062661 | 572.9580860191353 |

The two bold rows are not accidents and are the heart of this post; they are discussed in their own section. First, notice the last row: as the latitude approaches the pole, the ordinate grows without bound. Mercator's map has no top edge. The pole is at infinity on the chart, which is why every Mercator world map is truncated somewhere around 83–85° and why Greenland looks the way it does.

Note also the middle of the chart: 45° of latitude occupies an ordinate of 0.8814, while 45° of longitude occupies 0.7854. The ratio is 1.1221997046783602543. A square drawn around the equator is not a square on the map, and no amount of care in drawing fixes it — the stretch is the point.

## The Gudermannian: where the circle constant enters as an offset

If the ordinate \(y\) is an integral, its inverse is a function, and it has a name. The Gudermannian function \(\operatorname{gd}\) returns the latitude whose Mercator ordinate is \(y\):

\[
\operatorname{gd}(x) \;=\; \arcsin(\tanh x) \;=\; \arctan(\sinh x) \;=\; 2\arctan(e^{x}) - \frac{\pi}{2}
\]

All three forms were evaluated independently at ten values of \(x\) for this article and agreed to 26 significant digits each time — for example \(\operatorname{gd}(1) = 0.865769483239658624289602\) by all three routes, which is 49.604937420854700378° of latitude for a chart ordinate of exactly 1 radian.

Look at where the circle constant sits in those three forms. It is absent from the first two. \(\arcsin(\tanh x)\) and \(\arctan(\sinh x)\) are built from the hyperbolic and inverse-trigonometric functions alone. The constant appears only in the third form, as a subtractive offset \(-\pi/2\), and that offset exists for a single reason: \(\arctan(e^x) \to \pi/2\) as \(x \to \infty\), so subtracting \(\pi/2\) re-centres the function on zero at the origin. The constant is a *convention of the vertical origin*, not a measured property of any curve.

Here is the same statement as an integral, which is where the constant is genuinely computed:

\[
\int_0^{\infty} \operatorname{sech} x \, dx \;=\; \big[ \operatorname{gd}(x) \big]_0^{\infty} \;=\; \frac{\pi}{2} \;=\; 1.57079632679489661923132169164\ldots
\]

This is a convergent limit — an area under a curve that flattens exponentially. Quadrature of \(\operatorname{sech}\) from 0 to \(\infty\) returns \(1.57079632679489661923132169164\), matching \(\pi/2\) to every printed digit. Nothing is measured; the integral evaluates to the constant, and the constant is what the integral evaluates to. That is the only sense in which \(\pi/2\) "is" in this subject.

The approach is slow, which is worth knowing before trusting any finite chart: the integral from 0 to 1 is \(0.865769483239658624289602\) (short of \(\pi/2\) by 0.705026843555), from 0 to 5 it is \(1.55732063672605102218242\) (short by 0.0134756900688), and from 0 to 10 it is still short by \(9.07998594626\times10^{-5}\). Correspondingly \(\operatorname{gd}(10) = 1.570705526935434033681299\), i.e. 89.994797551° — four decimal places of latitude are still missing at an ordinate of ten.

## The golden latitude: where the map's stretch is exactly √φ

Two latitudes in the table are printed in bold, and both are exact.

Ask for the latitude at which the map's stretch factor \(\sec\phi\) equals \(\sqrt{\varphi}\). Then \(\cos\phi = 1/\sqrt{\varphi} = 0.78615137775742328607\), and since \(\varphi\) satisfies \(\varphi^2 = \varphi + 1\), the sine of that angle is cleanly algebraic:

\[
\sin\phi_g = \sqrt{1 - \tfrac{1}{\varphi}} = \sqrt{\tfrac{1}{\varphi^2}} = \frac{1}{\varphi}
\]

So the latitude is \(\phi_g = \arcsin(1/\varphi) = 0.66623943249251525510\) rad \(= 38.17270762701224749347°\), and there the map stretch is \(\sqrt{\varphi} = 1.2720196495140689643\) exactly, not approximately. Its complement, \(\arccos(1/\varphi) = 51.827292372987752507°\), is where the stretch is \(\varphi = 1.6180339887498948482\) exactly.

The ordinate at the golden latitude is just as clean. With \(\sin\phi_g = 1/\varphi\),

\[
y_g = \operatorname{artanh}\!\left(\frac{1}{\varphi}\right) = \frac{3}{2}\ln\varphi = \frac{3}{2}\operatorname{arcsinh}\!\left(\frac{1}{2}\right) = 0.7218177375894051712466\ldots
\]

computed here by both routes to 25 digits. And \(\ln\varphi = \operatorname{arcsinh}(1/2) = 0.481211825059603447497759\) — the golden ratio's logarithm is the inverse hyperbolic sine of a half, a fact with no circle constant in it.

This is the honest place to say what has and has not been shown. The map's stretch reaches \(\sqrt{\varphi}\) exactly at 38.1727°, and it reaches \(\varphi\) exactly at 51.8273°. Those are real, exact, algebraic statements about the golden ratio. They are *not* statements about the circle constant. The circle constant never appears in the stretch factor \(\sec\phi\); it does not appear in the ordinate \(\operatorname{artanh}(\sin\phi)\); and it does not appear in the latitudes \(\arcsin(1/\varphi)\). The golden ratio's appearance in Mercator's scale is a fact about triangles, and a good one.

## The rhumb line: a straight line on a conformal map

The payoff of the construction is that a line of constant bearing — a rhumb line, or loxodrome — is a straight line on the chart. On the sphere the relationship between the constant bearing α and the two axis increments is exact and \(\pi\)-free:

\[
\Delta\lambda = \tan\alpha \cdot \Delta\psi, \qquad
\Delta\psi = \operatorname{artanh}(\sin\phi_2) - \operatorname{artanh}(\sin\phi_1)
\]

and the length along such a rhumb is \(L = R\,\Delta\phi / \cos\alpha\) on a sphere of radius \(R\). Take the rhumb from \(0°\)N \(0°\)E to \(45°\)N \(45°\)E with \(R = 6371\) km:

- ordinate increment \(\Delta\psi = 0.881373587019543025232609\)
- longitude increment \(\Delta\lambda = 0.785398163397448309615661\)
- ratio \(\Delta\lambda/\Delta\psi = 0.891106989095684555887207\), so the constant bearing is \(41.70445505716406626°\)
- rhumb length \(L = 6702.199948935228\) km
- great-circle length between the same two points \(= 6671.695598673524\) km
- difference \(30.504350\) km, ratio \(1.004572203544144\)

Every one of those numbers came out of artanh, arctan and ratios. The constant-bearing curve is longer than the great circle, as it must be — the great circle is the shortest path on a sphere — and the 30.5 km penalty is the price of holding a compass heading. Nothing in the computation needed to know what the circle constant is.

## What Golden Pi changes — and what it does not

This is the point in a post where this series usually has to report a percentage shift. Not here. Take the golden label, \(\hat{\pi} = 4/\sqrt{\varphi} = 3.144605511029693144278234343371835718092\), and ask where it enters Mercator's subject.

It enters in exactly one term, the offset in the third form of the Gudermannian:

\[
\operatorname{gd}(x) = 2\arctan(e^{x}) - \frac{\pi}{2}
\qquad\longrightarrow\qquad
2\arctan(e^{x}) - \frac{\hat{\pi}}{2}
\]

with \(\hat{\pi}/2 = 2/\sqrt{\varphi} = 1.5723027555148465721391171716859\) against \(\pi/2 = 1.57079632679489661923132169164\). The difference is \((\hat{\pi}-\pi)/2 = 0.0015064287199499529078\) rad, which is \(0.0863120077904273367°\) — and the relative gap is the site's recurring \(0.09590223087825259637\%\), unsoftened, because the constant sits to the first power.

What that does to a chart is easy to state and easy to get wrong. The pole, where \(\operatorname{gd}(x)\) converges, would be assigned an ordinate of \(\hat{\pi}/2 = 1.5723027555\); read as ordinary degrees that is \(90.0863120078°\), i.e. **9.597 km past the pole** at \(R = 6371\) km (9.608 km at the equatorial radius 6378.137 km, 9.576 km at the polar radius 6356.752 km). A table built on the golden label would put every tabulated latitude \(0.0863°\) too high. Conversely, the golden latitude \(38.1727076270°\), re-expressed against a golden half-turn, reads \(38.1361342235°\) — a shift of \(0.0365734034910815716°\), about \(4.067\) km at the same radius.

But notice precisely what did and did not move. The ordinate table, the scale factors \(\sec\phi\), the constant bearing \(41.70445506°\), the rhumb length \(6702.1999\) km, the great-circle length \(6671.6956\) km, the golden latitudes \(38.1727°\) and \(51.8273°\), the stretch values \(\sqrt{\varphi}\) and \(\varphi\) — none of these is a function of the circle constant at all. They are functions of angles and of hyperbolic logarithms. A relabelling of a symbol cannot move them, and the honest statement is that on this subject the golden label changes *nothing measurable and nothing geometric* except the number a tabulated latitude carries when it is written in radians and folded into a chart ordinate.

That is a result worth publishing even though it contains no shift in metres. It is the first place in this series where the constant's role is purely a convention of the vertical origin, and where the correct outcome of the golden question is "the map is label-blind". The 0.0959% gap does not vanish; it applies to the constant, and the constant simply is not in the map.

The one physical hook is the pole itself. The value \(\pi/2\) rad is a computed limit — the total length of the quarter meridian divided by the radius — and it is what it is because a circle's circumference is not being measured but evaluated. Under ordinary \(\pi\) the quarter-turn is \(1.57079632679489661923132169164\); under the golden label it is \(1.57230275551484657213911717169\); and the difference, \(0.0863120078°\) of latitude, is \(9.597\) km on the ground. Nothing on Earth is surveyed to that precision as an angle, but that is not the reason to prefer one number over the other. The reason is that the quarter-turn is computed from the analytic circle constant, and the analytic constant is \(3.14159265358979323846\ldots\) — the limit of the sech integral and of every series on this site, computed and never measured.

## The honest ledger

| quantity | computed value | depends on the circle constant? | under Golden Pi (π̂ = 4/√φ) |
|---|---|---|---|
| Mercator ordinate \(y(\phi) = \operatorname{artanh}(\sin\phi)\) | e.g. 0.88137358701954302523 at 45° | no | unchanged |
| map scale \(\sec\phi\) | 1.2720196495140689643 at 38.1727076270° | no | unchanged (= √φ exactly) |
| golden latitude \(\arcsin(1/\varphi)\) | 38.17270762701224749347° | no | unchanged |
| complement latitude \(\arccos(1/\varphi)\) | 51.827292372987752507° | no | unchanged (scale = φ exactly) |
| constant bearing, 0°N0°E → 45°N45°E | 41.70445505716406626° | no | unchanged |
| rhumb length, R = 6371 km | 6702.199948935228 km | no | unchanged |
| great-circle length, same points | 6671.695598673524 km | no | unchanged |
| sech integral \(\int_0^\infty \operatorname{sech} x\,dx\) | 1.57079632679489661923132169164 | yes — it *is* π/2 | → 2/√φ = 1.57230275551484657213912 (+0.0959022309%) |
| Gudermannian offset \(-\pi/2\) | −1.57079632679489661923132169164 | yes | → −1.57230275551484657213912; pole reads 90.0863120078°, +9.597 km |
| golden latitude vs golden half-turn | 38.1727076270° | yes (frame conversion only) | reads 38.1361342235°, −0.0365734035° |

Read the table down the third column: eight rows say no. The map is a log-tangent, and log-tangents do not care what a full turn is worth.

## Further Reading

- [The Haversine Formula: How Spherical Trigonometry Computes the Circle Constant on the Globe](/blog/posts/2026-09-20-haversine-formula-navigation-computes-circle-constant-golden-pi/) — the great-circle distance that the rhumb line trades 30.5 km against.
- [Ptolemy's Table of Chords: How Inscribed Chords Computed the Circle Constant](/blog/posts/2026-09-15-ptolemy-chord-table-computes-circle-constant-golden-pi/) — the first circle geometry done as pure lengths, before the constant had a name.
- [The Gauss–Bonnet Theorem: How Curvature and Topology Compute the Circle Constant](/blog/posts/2026-09-01-gauss-bonnet-theorem-curvature-topology-computes-circle-constant-golden-pi/) — the geometry that makes conformal distortion a curvature question rather than a tape measure.
- [Squaring the Circle: Why Golden Pi Is Constructible](/blog/posts/2026-07-26-squaring-circle-golden-pi-constructible/) — the site's core geometric claim, and the sense in which π̂ is exact.
- [Euler's Identity: How e^(iπ) + 1 = 0 Computes the Circle Constant](/blog/posts/2026-09-19-euler-identity-computes-circle-constant-golden-pi/) — where the offset angle of this post's Gudermannian does the same job in a different uniform.
