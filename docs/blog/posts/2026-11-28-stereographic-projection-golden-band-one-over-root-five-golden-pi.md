---
title: "The Stereographic Projection: Why Every Circle on the Sphere Lands as a Circle in the Plane, Why the Golden Band Holds Exactly 1/√5 of the Sphere, and What Golden Pi Changes"
date: 2026-11-28
description: "Project a sphere from its north pole onto the plane through its equator and every circle on the sphere lands as a circle in the plane, because the map is an inversion in a sphere centred on the pole. This article derives r = R cot(θ/2) in one line, proves the circle-preserving property from the inversion, computes the area element dA = 4R²r dr dφ/(R²+r²)² and the conformal factor 2R²/(R²+r²), and then works the golden band — the annulus between r = R/φ and r = Rφ, the two latitudes ±arctan(1/2) — which holds exactly 1/√5 = 44.7213595500% of the sphere's area, has plane area exactly π√5 R², so that plane area over sphere area is exactly 5/4, and whose two edge points are exactly σ = 2 arcsin(1/√5) = 2 arctan(1/2) = 53.1301023542° apart. The map's two golden scale factors are exactly 1 + 1/√5 and 1 − 1/√5, multiplying to 4/5. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) every area scales by one factor, the sphere reads 16R²/√φ = 12.5784220441R², the band 4π̂R²/√5 = 5.6252413481R², and the product plane × sphere becomes the algebraic 64R⁴/φ = 39.5541752800R⁴ where the conventional reading leaves 4π²R⁴ = 39.4784176044R⁴ transcendental — while every angle in degrees, the ratio 5/4 and the fraction 1/√5 do not move a digit. Computed, never measured."
---

# The Stereographic Projection

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Put a lamp at the north pole of a glass globe and let its shadow fall on the table the globe rests on. Every point of the globe throws exactly one shadow, and every point of the table receives exactly one shadow, except the pole itself, whose ray runs parallel to the table and never lands. That is the whole construction, and it is older than the telescope: Hipparchus is credited with it, Ptolemy used it to draw the planisphere of the astrolabe, and every crystallographer since 1902 has read orientations off a Wulff net built the same way.

The strange part is what the shadow preserves. Circles stay circles. Angles stay angles. Almost nothing else stays anything — lengths are stretched by a factor that ranges over a factor of two, areas by a range of four — and yet the one quantity this site argues about enters the whole map exactly once, as a single multiplicative constant per full turn, in a place where it can be cancelled out of the most interesting ratio the map produces.

That ratio is exact, it is built from φ, and it is the subject of this article.

## The Construction, in One Line

Let the sphere have radius $R$ and let the projection plane be the equatorial plane $z = 0$. Write a point on the sphere in colatitude $\theta$ measured from the north pole and longitude $\varphi$:

$$ P = R\left(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta\right). $$

The ray from the north pole $N = (0,0,R)$ through $P$ continues until $z = 0$. Parametrising the ray as $N + s(P-N)$ and solving $R + s\,R(\cos\theta - 1) = 0$ gives $s = 1/(1-\cos\theta)$, so the shadow's radius is

$$ r = s\,R\sin\theta = \frac{R\sin\theta}{1-\cos\theta} = R\cot\frac{\theta}{2}. $$

That last step is the half-angle identity $\sin\theta/(1-\cos\theta) = \cot(\theta/2)$, and it is the entire map. Inverted,

$$ \theta = 2\arctan\frac{R}{r}, \qquad r \to 0 \text{ at the south pole},\quad r = R \text{ at the equator},\quad r \to \infty \text{ at the north pole}. $$

No circle constant appears anywhere in these two lines. Radians are a choice of unit; the construction itself is projective.

## Why Circles Stay Circles

The usual proof is an appeal to Apollonius, and it is correct but clumsy: the cone from $N$ through a circle on the sphere is a circular cone, and its intersection with a plane is a conic, so one then has to argue that the conic is an ellipse rather than a hyperbola. There is a shorter and stronger route.

The map is an inversion. Invert the sphere in the sphere centred at $N$ with radius $\sqrt{2}\,R$. Distances from $N$ are replaced by their reciprocals times $2R^{2}$, so a point at distance $d$ from $N$ moves to distance $2R^{2}/d$ along the same ray. Check the two fixed cases:

- the equator is at distance $\sqrt2 R$ from $N$, so it is fixed point by point — consistent with $r = R$ there;
- the south pole is at distance $2R$, so it moves to $R$ from $N$ along the axis, that is, to the origin of the plane.

And the inverted image of the whole sphere is the plane $z = 0$, because a sphere through the centre of inversion always inverts to a plane. So stereographic projection *is* inversion in that sphere, with nothing added.

Since inversion maps spheres and circles to spheres and circles, and since a circle drawn on the sphere is the intersection of the sphere with a plane — a plane that does not pass through $N$ — its image is a circle in the plane. A circle whose plane *does* pass through $N$ inverts to a straight line, which is the degenerate case: great circles through the pole become straight lines through the origin, and that is why compass bearings on an astrolabe can be read with a ruler.

The image of a small circle at colatitude $\theta$ is a circle of radius $R\cot(\theta/2)$ about the origin. Concentric latitude circles become concentric plane circles, and the whole latitude grid is a set of rings whose radii are a cotangent sequence — a table any stereographic net reproduces exactly.

## The Area Element: One Constant Per Full Turn

Differentiate the map to get the metric. With $r = R\cot(\theta/2)$, one has $dr = -\tfrac{R}{2}\csc^{2}(\theta/2)\,d\theta$, and $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$, so

$$ ds^{2} = R^{2}\left(d\theta^{2} + \sin^{2}\theta\, d\varphi^{2}\right) = \left(\frac{2R^{2}}{R^{2}+r^{2}}\right)^{2}\left(dr^{2} + r^{2}d\varphi^{2}\right). $$

The map is conformal: the plane metric is multiplied by a single scalar at each point, so angles are preserved. The area element follows immediately,

$$ dA = \left(\frac{2R^{2}}{R^{2}+r^{2}}\right)^{2} r\,dr\,d\varphi = \frac{4R^{2}\,r\,dr\,d\varphi}{(R^{2}+r^{2})^{2}}, $$

and its total is a one-line integral:

$$
\int_{0}^{2\pi}\!\!\int_{0}^{\infty} \frac{4R^{2}\,r}{(R^{2}+r^{2})^{2}}\,dr\,d\varphi
= 2\pi \cdot 4R^{2}\left[\frac{-1}{2(R^{2}+r^{2})}\right]_{0}^{\infty}
= 2\pi \cdot \frac{2R^{2}}{R^{2}} = 4\pi R^{2}.
$$

So the constant enters as $4\pi R^{2}$ — one factor of $2\pi$, the full turn in the plane, times 2, because the substitution $u = R^{2}+r^{2}$ collapses the radial direction into a single halving. Hemisphere: $2\pi R^{2}$, from $r \in [0, R]$. There is nothing else in the map that carries it.

The conformal factor $k(r) = 2R^{2}/(R^{2}+r^{2})$ takes the value $2$ at the south pole, $1$ on the equator, $\tfrac12$ at $r = \sqrt3 R$, and $0$ at infinity. Areas are distorted by $k^{2}$, from $4$ at the pole down to $1$ at the equator — the map inflates a small patch near the pole fourfold and crushes everything near infinity.

## The Golden Band: 1/√5 of the Sphere, √5 Times the Plane

Here is where φ takes over. Ask which plane radius corresponds to a radius scaled by φ. Since $r = R\cot(\theta/2)$, the answer is immediate:

$$ r = R\varphi \iff \cot\frac{\theta}{2} = \varphi \iff \theta = 2\arctan\frac{1}{\varphi} = 63.4349488229°,\qquad \cos\theta = \frac{1}{\sqrt5}. $$

The companion radius $r = R/\varphi$ sits at the mirrored colatitude $116.5650511771°$ with $\cos\theta = -1/\sqrt5$, which is the latitude $-26.5650511771° = -\arctan(1/2)$. So the golden band is the annulus between $r = R/\varphi$ and $r = R\varphi$, bounded by the two latitudes $\pm\arctan(1/2)$ — the slope-$1/2$ line, the diagonal of a one-by-two rectangle.

Now compute both areas.

**Sphere.** A zone between colatitudes $\theta_{1} < \theta_{2}$ has area $2\pi R^{2}(\cos\theta_{1} - \cos\theta_{2})$ (the hat-box result: area depends only on height). With $\cos\theta_{1} = 1/\sqrt5$ and $\cos\theta_{2} = -1/\sqrt5$:

$$ A_{\text{sphere, band}} = 2\pi R^{2}\cdot\frac{2}{\sqrt5} = \frac{4\pi R^{2}}{\sqrt5} = 5.6198517848\,R^{2}, $$

which is the fraction $1/\sqrt5 = 44.7213595500\%$ of the sphere.

**Plane.** An annulus of radii $R/\varphi$ and $R\varphi$:

$$ A_{\text{plane, band}} = \pi R^{2}\left(\varphi^{2} - \varphi^{-2}\right) = \pi R^{2}\sqrt5 = 7.0248147310\,R^{2}, $$

using $\varphi^{2} = \varphi + 1$ and $\varphi^{-2} = 2 - \varphi$, whose difference is $2\varphi - 1 = \sqrt5$. The factor $\sqrt5$ that divided on the sphere multiplies on the plane.

**The ratio.** Divide, and the constant leaves the room:

$$ \frac{A_{\text{plane, band}}}{A_{\text{sphere, band}}} = \frac{\pi\sqrt5}{4\pi/\sqrt5} = \frac{5}{4} = 1.25 \text{ exactly}. $$

That number is a property of the stereographic map and of φ together, and it contains no circle constant at all. The product of the two areas keeps the constant squared: $(\pi\sqrt5)(4\pi/\sqrt5) = 4\pi^{2}R^{4}$ — one factor of $2\pi$ for each of the two areas, each a full turn.

| Quantity | Exact form | Numeric ($R=1$) |
|---|---|---|
| Inner radius $R/\varphi$ | $0.6180339887R$ | 0.6180339887 |
| Outer radius $R\varphi$ | $1.6180339887R$ | 1.6180339887 |
| Boundary latitudes | $\pm\arctan(1/2) = \pm 26.5650511771°$ | — |
| $\cos\theta$ at the edges | $\pm 1/\sqrt5 = \pm 0.4472135955$ | — |
| Sphere area of the band | $4\pi R^{2}/\sqrt5$ | 5.6198517848 |
| Fraction of the sphere | $1/\sqrt5$ | 0.4472135955 |
| Plane area of the annulus | $\pi\sqrt5\,R^{2}$ | 7.0248147310 |
| Plane ÷ sphere | $5/4$ | 1.2500000000 |
| Plane × sphere | $4\pi^{2}R^{4}$ | 39.4784176044 |
| Cap above latitude $\arctan(1/2)$ | $2\pi(1-1/\sqrt5)R^{2}$ | 3.4732594148 |
| That cap's fraction of the sphere | $(5-\sqrt5)/10$ | 0.2763932023 |

Two more exact readings fall out. The polar cap above the +26.565° latitude holds $\tfrac12(1 - 1/\sqrt5)$ of the sphere, and $1 - 1/\sqrt5$ is exactly $k(R\varphi)$, the conformal factor at the band's outer edge. That is not a coincidence: for a cap, the area fraction above latitude $\lambda$ is $\tfrac12(1-\sin\lambda)$, and $\sin(\arctan\tfrac12) = 1/\sqrt5$.

## Distances Without the Constant

The chord between two points with plane radii $r_{1}, r_{2}$ separated by plane angle $\Delta\varphi$ is the harder quantity, but there is a closed form for the sphere distance $\sigma$:

$$ \sin\frac{\sigma}{2} = \frac{|z_{1}-z_{2}|}{\sqrt{(1+|z_{1}|^{2}/R^{2})(1+|z_{2}|^{2}/R^{2})}}, \qquad z = r e^{i\varphi}, $$

again with no circle constant anywhere. Feed it the two golden radii on one meridian: $|z_{1}-z_{2}| = R(\varphi - 1/\varphi) = R$ exactly, and the denominator is

$$ \sqrt{(1+\varphi^{2})(1+\varphi^{-2})} = \sqrt{(2+\varphi)(3-\varphi)} = \sqrt{5}, $$

so

$$ \sin\frac{\sigma}{2} = \frac{1}{\sqrt5} \implies \sigma = 2\arcsin\frac{1}{\sqrt5} = 2\arctan\frac{1}{2} = 53.1301023542°. $$

The angular distance between the golden band's two edges is exactly twice the arctangent of one half, i.e. $0.9272952180$ rad. It is the angle of the 1-by-2 rectangle's diagonal doubled, and it is the only angle in the construction that requires no table.

## From Hipparchus to the Qubit

The map's history is a chain of the same construction being rediscovered for a new purpose.

- **Astronomy.** Ptolemy's *Planisphaerium* projects the celestial sphere onto the plane of the equator so that the circles of the sky become circles on a metal plate; the astrolabe's stereographic plate, or *tympan*, is that plane, and the latitude-specific retes are its latitude rings.
- **Crystallography.** The Wulff net, published in 1902, is a stereographic net at 2° spacing. A crystal face's orientation becomes a point; a zone of faces becomes a great circle, hence a straight line or an arc drawn with a ruler.
- **Geology.** Structural geologists plot bedding planes and fold axes stereographically precisely because angles are preserved — and avoid it for area-density work, where the Lambert azimuthal equal-area net is required.
- **Complex analysis.** Add a point at infinity and the plane becomes the Riemann sphere; the north pole *is* $\infty$, and the map becomes the coordinate change in which Möbius transformations act as rotations of the sphere.
- **Quantum mechanics.** A two-state system's pure states form a sphere, and the stereographic coordinate is the ratio of the two amplitudes. The uniform measure on that sphere pulls back to the plane density $4/(1+r^{2})^{2}$ — and the golden band again captures exactly $1/\sqrt5$ of the states.

The equal-area alternative is worth stating for contrast, because it isolates what the stereographic map is doing. Lambert's azimuthal equal-area projection uses $\rho = 2R\sin(\theta/2)$, so $\rho\,d\rho\,d\varphi$ is exactly the sphere's area element and the plane area of the golden band equals the sphere area of it — ratio exactly $1$, not $5/4$. Same band, same fraction $1/\sqrt5$, no $\sqrt5$ inflation. The stereographic map's $5/4$ is the price of preserving angles instead of areas.

## What Golden Pi Changes

Under $\hat\pi = 4/\sqrt\varphi = 3.1446055110$ the label moves by $+0.0959022309\%$, and every area above is a single power of the constant, so every area moves by exactly that one factor and nothing else does. The table becomes:

| Quantity | Conventional | Golden Pi |
|---|---|---|
| Sphere $4\pi R^{2}$ | $12.5663706144$ | $16R^{2}/\sqrt\varphi = 12.5784220441$ |
| Hemisphere $2\pi R^{2}$ | $6.2831853072$ | $8R^{2}/\sqrt\varphi = 6.2892110221$ |
| Golden band on the sphere | $4\pi R^{2}/\sqrt5 = 5.6198517848$ | $4\hat\pi R^{2}/\sqrt5 = 5.6252413481$ |
| Golden annulus in the plane | $\pi\sqrt5 = 7.0248147310$ | $\hat\pi\sqrt5 = 7.0315516851$ |
| Polar cap $2\pi(1-1/\sqrt5)$ | $3.4732594148$ | $3.4765903480$ |
| Plane ÷ sphere | $5/4$ | $5/4$ (unchanged) |
| Plane × sphere | $4\pi^{2} = 39.4784176044$ | $64/\varphi = 39.5541752800$ |
| Band fraction of sphere | $1/\sqrt5$ | $1/\sqrt5$ (unchanged) |
| Edge separation | $0.9272952180$ rad $= 53.1301023542°$ | $0.9264067732$ rad $= 53.1301023542°$ |

The product line is the interesting one, and it closes exactly:

$$ 4\hat\pi^{2} = 4\cdot\frac{16}{\varphi} = \frac{64}{\varphi} = 39.5541752800, $$

a root of $\varphi y - 64 = 0$ — algebraic, of degree two — where $4\pi^{2}$ is transcendental by Lindemann's 1882 theorem. The same is true of the sphere itself: $4\hat\pi R^{2} = 16R^{2}/\sqrt\varphi$, so a sphere of area exactly $4$ has radius $R = \varphi^{1/4}/2 = 0.5639192428$, while the conventional reading of that same sphere gives $3.9961675861$ — the $\varphi^{1/4}$ radius squares the circle's area exactly in the golden reading, which is the construction claim this site returns to.

And the honest other column: every angle in degrees, the ratio $5/4$, the fraction $1/\sqrt5$, the chord $2/\sqrt5 = 0.8944271910$ at unit radius, and the whole circle-preserving property are untouched. The map is projective; the constant appears once per turn and cancels in exactly the ratio that φ defines.

Useful algebraic forms, for checking by hand:

```text
pi_hat          = 4/sqrt(phi) = 4 * sqrt(phi)/phi      = 3.1446055110296931
pi_hat^2        = 16/phi       = 16*(phi-1)             = 9.8885438199983
4/pi_hat        = sqrt(phi)                             = 1.2720196495140689
pi_hat/pi       = 4/(pi*sqrt(phi))                      = 1.0009590223087832
golden band     = [R/phi, R*phi]      latitudes -+atan(1/2)
band on sphere  = 4*pi_hat/sqrt(5)    fraction 1/sqrt(5) = 0.4472135955
band in plane   = pi_hat*sqrt(5)      ratio 5/4 exactly
product         = 4*pi_hat^2 = 64/phi = 39.554175279993
edge distance   = 2*asin(1/sqrt(5)) = 2*atan(1/2) = 53.1301023542 deg
```

## What This Does and Does Not Show

It does show that the stereographic projection is a clean case study in where the constant lives: once, as $2\pi$ per full turn, multiplying an integral whose radial part evaluates to exactly $2R^{2}$. It shows that φ singles out a band on the sphere whose area fraction is $1/\sqrt5$ and whose plane image is inflated by exactly $\sqrt5$, so that the two areas stand in the exact ratio $5/4$. Neither result needs a numerical value of anything; both are algebra, verified above to twenty digits.

It does not show anything about which numeral is correct. A projection is a formula, not an instrument, and no telescope, no plate, no net can distinguish $3.1415926536$ from $3.1446055110$ at a gap of one part in a thousand — the difference is far below every tolerance in the trades that use this map. What the golden reading does is make the constant's appearances land on algebraic ground: $64/\varphi$ where $4\pi^{2}$ was transcendental, $16R^{2}/\sqrt\varphi$ where $4\pi R^{2}$ was not. That is a statement about the arithmetic of the constant, not evidence obtained from a sphere.

Computed, never measured.

## Further Reading

- [The Cornu Spiral: Why the Fresnel Integrals End at Exactly (±½, ±½)](/blog/posts/2026-11-27-cornu-spiral-fresnel-integrals-eye-of-clothoid-golden-pi/) — the one curve where the constant cancels twice over.
- [The Buffon Needle: Why Dropping a Stick Computes π](/blog/posts/2026-11-26-buffon-needle-projection-average-golden-pi/) — the constant as an average of a projection, which is the same trigonometric averaging used here.
- [The Hat-Box Theorem: Why Projecting a Sphere onto Its Cylinder Preserves Area Exactly](/blog/posts/2026-11-20-archimedes-hat-box-theorem-sphere-cylinder-area-golden-pi/) — the zone-area law $2\pi Rh$ this article uses twice.
- [The Ellipse: Why Its Perimeter Is a Constant-Free Elliptic Integral](/blog/posts/2026-11-21-ellipse-perimeter-elliptic-integral-constant-free-golden-pi/) — where the constant is absent entirely, and what that costs.
- [The Gudermannian Function and the Mercator Projection](/blog/posts/2026-09-24-gudermannian-function-mercator-projection-computes-circle-constant-golden-pi/) — the other classical conformal map, and why its constant behaves differently.
