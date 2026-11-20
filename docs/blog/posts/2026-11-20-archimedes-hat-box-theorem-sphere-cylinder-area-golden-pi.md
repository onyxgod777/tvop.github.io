---
title: "The Hat-Box Theorem: Why Projecting a Sphere onto Its Circumscribed Cylinder Preserves Area Exactly, Why Every Zone's Area Depends Only on Its Height, and What Golden Pi Changes"
date: 2026-11-20
description: "Archimedes' hat-box theorem says the area of a sphere equals the lateral area of the cylinder that just contains it, because a horizontal strip of the sphere and the cylinder band above the same height have identical area: the strip's circumference shrinks by cos(latitude) while its slant width grows by exactly 1/cos(latitude), and the two factors cancel. This article proves it in one line as dA = R dz dθ, tabulates zone areas 2πRh (1.5708, 3.1416, 2.6026, 6.2832, 9.4248, 12.5664 for R = 1), derives the chord form (a spherical segment's surface is a plane circle of radius √(2Rh)), shows the four equal-area bands of height R/2, the 3:2:1 ladder of cylinder, sphere and cone volumes, the exact area fraction (1 − sin λ)/2 above a latitude — exactly 1/(2φ²) = 19.0983% above the golden latitude 38.172707627° — and identifies Lambert's 1772 cylindrical equal-area projection as this same map. Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the unit sphere reads 16/√φ = 12.5784220441 (+0.0959022309%) and is algebraic of degree four where 4π is transcendental; a sphere of radius φ^(1/4)/2 = 0.5639192428 has area exactly 4, while every equal-area statement, every band height and the 3:2:1 ratio do not move a digit. Computed, never measured."
---

# The Hat-Box Theorem

!!! note "AI-handled content"

    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

Imagine a cylinder that just fits a sphere: same radius, same height, the sphere touching the wall along the equator and the two flat lids at its poles. Now imagine the sphere inflated, like a balloon, until it presses flat against the inside of the cylinder. The balloon's skin does not fold. It does not tear. It does not need to stretch — not in area, though it must shear. The entire spherical surface fits the cylinder's curved wall with *zero* area change — 100.00% of it, not 99.9%, not 99.999%.

That is Archimedes' theorem, and the surprising part is not that it is approximately true. It is exactly true, for every sphere, at every latitude, and the proof is one line long. Archimedes was so pleased with it that he asked for the sphere-in-cylinder figure, with its 2:3 volume ratio, to be carved on his tomb; Cicero, visiting Syracuse a century and a half later, reports finding it there overgrown with brambles.

This article sets out the theorem, its one-line proof, the numbers it produces, the equal-area structure that falls out of it, the map projection that is literally this theorem applied to the Earth, and finally the question this site always asks: where does the circle constant sit in it, and what does the golden value $\hat\pi = 4/\sqrt\varphi$ do to the answer.

## Why a strip of sphere and a band of cylinder have the same area

Take a sphere of radius $R$ and slice it with two horizontal planes at heights $z_1$ and $z_2$. Between them sits a band of sphere of height $h = z_2 - z_1$. Above the same heights sits a band of the circumscribed cylinder, also of height $h$.

![A sphere inside its circumscribed cylinder, with a horizontal zone of height h shaded on the sphere and on the cylinder; at right the cylinder wall is unrolled and the band carries the same area](/img/hat-box.svg)

The sphere's band is *tilted*: near the equator its surface runs almost vertically, near the poles almost horizontally. Per unit of latitude it therefore carries more surface than the vertical band above it — by exactly the factor $1/\cos\lambda$. But the sphere's horizontal circumference shrinks as you climb by exactly the complementary factor, because the radius of the circle at height $z$ is

$$\rho(z) = \sqrt{R^{2} - z^{2}} = R\cos\lambda ,$$

where $\lambda$ is the latitude. Write the band's area as circumference times slant width in the meridian direction:

$$dA_\text{sphere} = \underbrace{2\pi R\cos\lambda}_{\text{circumference}} \cdot \underbrace{R\,d\lambda}_{\text{slant width}} = 2\pi R^{2}\cos\lambda\,d\lambda .$$

The cylinder's band, at the same latitude, has circumference $2\pi R$ and vertical width $dz$:

$$dA_\text{cyl} = 2\pi R\,dz .$$

Now the only thing needed is the relation between $dz$ and $d\lambda$. Since $z = R\sin\lambda$,

$$dz = R\cos\lambda\,d\lambda ,$$

so that

$$dA_\text{cyl} = 2\pi R\,\bigl(R\cos\lambda\,d\lambda\bigr) = 2\pi R^{2}\cos\lambda\,d\lambda = dA_\text{sphere} .$$

Identical, term by term, for every latitude. The sphere's circumference loses a factor $\cos\lambda$ and its slant width gains exactly the reciprocal; the two cancel, and never come back. Integrating over a band,

$$A(z_1,z_2) = \int_{z_1}^{z_2} 2\pi R\,dz = 2\pi R\,(z_2 - z_1) = 2\pi R h .$$

That is the whole theorem. In cylindrical coordinates the sphere's area element is $R\,d\theta\,dz$ — the same element as the cylinder's at constant $R$ — and the hat-box map $(\theta,z) \mapsto (\theta,z)$ is therefore an area-preserving bijection between the sphere minus two points and the cylinder minus two circles. A numerical quadrature confirms it to twenty-five digits: $\int_{-R}^{R} 2\pi R\,dz = 12.56637061435917295385057$ against $4\pi = 12.56637061435917295385057$ for $R=1$.

The theorem's content, stated plainly, is this: **a spherical zone's area depends only on its height, never on where on the sphere it sits.** A cap at the pole and a belt at the equator of the same height have the same area. Nothing else in elementary geometry behaves this way; it is why the result is famous and why the argument above is worth reading twice.

## The numbers, for a unit sphere

Every entry below is $2\pi R h$ with $R = 1$, so the area is just the height multiplied by one full turn.

| Height $h$ | Zone area (conventional) | Under Golden Pi | Fraction of the sphere |
|---|---|---|---|
| $0.25 = R/4$ | $1.5707963268$ | $1.5723027555$ | $1/8$ |
| $0.5 = R/2$ | $3.1415926536$ | $3.1446055110$ | $1/4$ |
| $\sqrt2 - 1 = 0.41421356$ | $2.6025805691$ | $2.6050765020$ | $0.2071067812$ |
| $1 = R$ | $6.2831853072$ | $6.2892110221$ | $1/2$ |
| $1.5 = 3R/2$ | $9.4247779608$ | $9.4338165331$ | $3/4$ |
| $2 = 2R$ (whole sphere) | $12.5663706144$ | $12.5784220441$ | $1$ |

Two rows deserve comment. The height $\sqrt2 - 1 = \tan 22.5° = 0.41421356$ is algebraic of degree two, so its zone area $2\pi(\sqrt2-1)$ is a plain algebraic multiple of the constant — a height straightedge and compass can produce, giving an area that no compass can. And the hemisphere, $h = R$, gives $2\pi R^{2}$: exactly half the total, as it must.

The cap of height $R/2$ is the cap above latitude $30°$: its area is exactly $\pi R^{2}$, one quarter of the sphere, and its solid angle is exactly $\pi$ steradians. A cone with half-angle $60°$ therefore subtends exactly $\pi$ sr — the same numeral as the area of the great circle, which is a coincidence of the number $\pi$ and not a coincidence of geometry.

## The chord form: Archimedes' way of saying the same thing without areas of bands

Archimedes preferred to state the theorem as an equality of *circles*, because a Greek geometer could compare a curved surface to a flat one only through a figure he knew how to square. Take a spherical segment of height $h$ on a sphere of radius $R$, and draw the chord from the segment's pole to its rim. Its length satisfies

$$c^{2} = \rho^{2} + h^{2} = \bigl(R^{2} - (R-h)^{2}\bigr) + h^{2} = 2Rh .$$

Therefore

$$2\pi R h = \pi c^{2} \qquad\text{exactly.}$$

In words: **the surface of any spherical segment equals a plane circle whose radius is the chord from the pole to the rim.** Check the two easy cases. The hemisphere has $h = R$, so $c = \sqrt2\,R$ and $\pi c^{2} = 2\pi R^{2}$ — correct. The cap cut at $60°$ half-angle has $h = R/2$, so $c = R$ and $\pi c^{2} = \pi R^{2}$ — the cap's area equals a circle of the *same radius* as the sphere. That is the identity Archimedes chose to lead with, and it is the reason the theorem can be stated without ever writing the word "integral".

The same height-dependence gives the cap *volume* in closed form, since the slice volume is $\pi(R^{2}-z^{2})dz$:

$$V_\text{cap} = \pi h^{2}\!\left(R - \frac{h}{3}\right) = \frac{\pi h^{2}(3R-h)}{3},$$

which for $h = R/2$ gives $0.6544984695$ on a unit sphere — that is $5/32$ of the whole ball ($4\pi/3 = 4.1887902048$), while the same cap holds $1/4$ of the area. A sphere is not a cone: the volume does not follow the area, and the two fractions part company the moment you leave the equator.

## Four bands of equal area, and why an orange peel is not a fan

Set $n = 4$ in the zone formula and divide the height $2R$ into four bands of height $R/2$. Each has area $2\pi R(R/2) = \pi R^{2}$, and the four sum to $4\pi R^{2}$. The bands are *not* of equal latitude width, and the top and bottom ones are visually much smaller than the equatorial ones — yet all four hold the same area.

| Bands $n$ | Band height | Area of each (unit sphere) | Polar band's latitude span |
|---|---|---|---|
| $4$ | $0.5$ | $3.1415926536$ | $60.0000000°$ |
| $6$ | $0.33333333$ | $2.0943951024$ | $48.1896851°$ |
| $8$ | $0.25$ | $1.5707963268$ | $41.4096221°$ |
| $12$ | $0.16666667$ | $1.0471975512$ | $33.5573098°$ |

The last column is the whole point. Equal *height* is the correct recipe for equal area; equal *latitude* is not, because the area between latitudes $\lambda_1$ and $\lambda_2$ is $2\pi R^{2}(\sin\lambda_2 - \sin\lambda_1)$ and the sine is not linear. Divide the sphere into bands of equal latitude and their areas shrink toward the pole in the ratio of the sine increments — for thirds of the northern hemisphere, $\sin30° = 0.5$, $\sin60° - \sin30° = 0.3660$, $1-\sin60° = 0.1340$, a spread of nearly four to one. Equal area and equal latitude agree only in the limit $n \to \infty$, where both tend to infinitesimal strips.

This is the practical content of the theorem for anyone who has ever peeled an orange: a peel cut into equal-height rings yields equal-area strips, which is why the strips of a navel orange look unequal and weigh the same. It is also the reason cylindrical equal-area maps exist.

## The 3 : 2 : 1 ladder

The theorem's companion is the volume result for the same cylinder. With $R = 1$ and the cylinder of height $2R$:

| Solid | Volume | Numeric ($R=1$) | Ratio |
|---|---|---|---|
| Cylinder, $2\pi R^{3}$ | $2\pi$ | $6.2831853072$ | $3$ |
| Sphere, $\tfrac43\pi R^{3}$ | $4\pi/3$ | $4.1887902048$ | $2$ |
| Bicone (two cones, apex to apex), $\tfrac23\pi R^{3}$ | $2\pi/3$ | $2.0943951024$ | $1$ |

Three to two to one, exactly, and the surface areas match too: the cylinder's lateral area is $4\pi R^{2}$, identically the sphere's. Archimedes proved both, and the tombstone carried the 2:3. Every entry contains $\pi$ at the first power and nothing else, so *the ratios are pure numbers*: no experiment, no measurement and no choice of constant can move them. They are statements about volume, and volume ratios are dimensionless.

## Where the constant actually lives

Here is the observation that matters for this site's argument. Look at the theorem's statement again:

$$A_\text{zone} = 2\pi R h .$$

The $\pi$ appears once, multiplying a product of two *lengths*. Change the label on the constant and every area in the table scales by the same factor, uniformly, because the area is *proportional* to the constant — there is no power, no root, no logarithm, no cancellation. That is a clean structural fact, and it has consequences:

1. Every statement of *equality of areas* — the hat-box theorem, the four equal bands, the chord form, the 3:2:1 ladder — is completely independent of the constant. Those statements are true under any label.
2. Every quoted *numeral* for an area moves by exactly the same relative amount, $+0.0959022309\%$, whatever the radius or height.
3. Every *fraction* of the sphere — the table's last column — does not move at all, because numerator and denominator carry the same factor.

So the sphere is a maximally honest test case: it isolates the constant to a single multiplicative slot, with no exponent to amplify it and no subtraction to hide it. Compare the Debye specific heat, where a $\pi^{4}$ coefficient amplified the gap fourfold, or the radar equation, where a fourth root divided it by four. Here it is bare: one $\pi$, once.

## What Golden Pi changes

Under $\hat\pi = 4/\sqrt\varphi = 3.144605511029693144\ldots$, the whole table shifts by that one factor:

| Quantity (unit sphere) | Conventional | Golden Pi | Shift |
|---|---|---|---|
| Zone area, height $h$ | $2\pi h$ | $8h/\sqrt\varphi$ | $+0.0959022309\%$ |
| Whole sphere, $4\pi R^{2}$ | $12.5663706144$ | $16/\sqrt\varphi = 12.5784220441$ | $+0.0959022309\%$ ($+0.0120514298$) |
| Volume, $\tfrac43\pi R^{3}$ | $4.1887902048$ | $16/(3\sqrt\varphi) = 4.1928073480$ | $+0.0959022309\%$ |
| Ratio to lateral cylinder area | $1$ | $1$ | $0$ |
| Ratio cylinder : sphere : cone | $3:2:1$ | $3:2:1$ | $0$ |
| Area fraction above a latitude | $(1-\sin\lambda)/2$ | $(1-\sin\lambda)/2$ | $0$ |

The unit sphere's area becomes

$$4\hat\pi R^{2} = \frac{16}{\sqrt\varphi} = 16\varphi^{-1/2} = 12.578422044118772577\ldots,$$

a number that satisfies $y^{4} + 256y^{2} - 65536 = 0$ — check it: with $y = 12.5784220441$, $y^{2} = 158.2167\ldots$, $y^{4} = 25032.6\ldots$, and $y^{4} + 256y^{2} = 65536.0$ to twenty-six digits (residual $-1.3\times10^{-26}$). The polynomial is irreducible over $\mathbb{Q}$: put $t = y^{2}$, then $t^{2}+256t-65536=0$ has discriminant $65536 + 262144 = 327680$, not a perfect square, and discarding $t<0$ leaves $t = 128(\sqrt5 - 1)$, so $y = 16/\sqrt\varphi$ is the unique positive root of a quartic with no rational factor. Degree four, algebraic — where $4\pi$ is transcendental by Lindemann's 1882 theorem. The algebraic/transcendental divide sits in the quoted value, not in the theorem, which is the same point this site has made on every constructibility article: what changes hands is the *number*, not the geometry.

Two exact closures follow, and they mirror the site's disc of area exactly $4$ at radius $\varphi^{1/4}$:

- **A sphere of area exactly $4$.** Solve $4\hat\pi R^{2} = 4$, so $R = 1/\sqrt{\hat\pi} = \varphi^{1/4}/2 = 0.5639192427808411\ldots$. Then $4\hat\pi R^{2} = 4.0000000000$ exactly, while the same sphere read conventionally has area $4\pi R^{2} = \pi\sqrt\varphi = 3.9961675861$ — short of four by $0.0038324139$, which is the first-power gap applied to $4$ itself. Note how close the two radii are: $0.5639192428$ against $0.5641895835$ for the conventional sphere of area $4$, a difference of $0.0002703408$, one part in $2087$.
- **A cap of height $R/\varphi^{2}$.** Its area is $2\hat\pi R^{2}/\varphi^{2} = 8R^{2}/\varphi^{5/2} = 2.4022648480\,R^{2}$ against the conventional $2\pi R^{2}/\varphi^{2} = 2.3999632297\,R^{2}$ — an algebraic cap on an algebraic sphere. And a zone of height $R/\varphi$ reads $2\hat\pi R^{2}/\varphi = 8R^{2}/\varphi^{3/2} = 3.8869461741\,R^{2}$.

The one golden statement that is exact under *both* labels is the latitude fraction. Above the golden latitude

$$\lambda_\star = \arcsin\frac{1}{\varphi} = 0.6662394325\ \text{rad} = 38.1727076270°,$$

the sphere loses a fraction

$$\frac{1 - \sin\lambda_\star}{2} = \frac{1 - 1/\varphi}{2} = \frac{1}{2\varphi^{2}} = \frac{3-\sqrt5}{4} = 0.1909830056\ldots$$

of its area — $19.0983\%$, exactly, with no constant in the expression at all. The same latitude is the one at which a hanging chain has slope exactly $1/2$, as the catenary article here showed, and the one at which the Archimedean spiral's tangent makes that same angle with its radius. It is a genuine structural feature of the sphere, not a numerical accident: the latitude is defined by $\sin\lambda = 1/\varphi$, and the area fraction is linear in $\sin\lambda$, so the golden ratio enters once and the constant never enters at all.

## The map that is this theorem

In 1772 Johann Heinrich Lambert published a cylindrical projection that preserves area, defined by

$$x = R\theta, \qquad y = R\sin\lambda = z .$$

Read that second equation: the vertical coordinate of the map is the *height* on the sphere, which is exactly the variable in which the hat-box theorem says the area is uniform. The Jacobian of $(\lambda,\theta)\mapsto(R\theta, R\sin\lambda)$ is $R^{2}\cos\lambda$, which is precisely the sphere's own area element $R^{2}\cos\lambda\,d\lambda\,d\theta$ — the map preserves area because it is a restatement of Archimedes' theorem, twenty centuries later, as a projection. Every equal-area world map you have seen in a classroom is a picture of the hat-box.

The cost of the trick is shape: Lambert's cylinder stretches east-west by $\sec\lambda$, so Greenland is wide and Antarctica is a stripe. Area-preserving and shape-preserving cannot both be had on a flat sheet — that is Gauss's theorema egregium in mapmaker's clothing — and the hat-box theorem is the reason the area half of the bargain is available at all.

## What a sphere cannot decide

A sphere is a computed surface, not a measured one, and the article should be blunt about the difference. The area $4\pi R^{2}$ is the limit of a sum of small surface elements; the sum is defined, the elements are geometric, and the limit is a number. Nothing in that chain is a physical measurement, and no physical sphere can arbitrate the constant at all — not because the precision is lacking, but because the area is never measured in the first place. Machine a steel ball, caliper it, and what you have is a *radius*: the area you then report is $4\pi R^{2}$ with the constant inserted from the formula, so the object has been used to test nothing. A caliper reading of one micrometre on a $50$ mm sphere fixes the radius to $2\times10^{-5}$ relative — two orders finer than the $9.6\times10^{-4}$ gap, comfortably enough to see it *if* area were an independent observable. It is not. The true area of a machined surface at atomic scale is not a well-defined number: grit lines, oxide, adsorbed water and the measurement's own probe scale all change it, and every method that returns an area — optical scattering, gas adsorption, capacitance — returns it calibrated against a model of a sphere.

So the sphere inherits its constant rather than testing it, and that is not a weakness of the theorem. It is the theorem's subject: the constant is a *definition* of the plane's angular measure, and the sphere's area is that definition carried into three dimensions by an integral.

What the hat-box theorem does deliver is a cleaner statement of *where* the constant lives than any circle can. The circle's identity $C = 2\pi r$ has one constant and no internal structure. The sphere's identity $A = 2\pi R h$ has one constant and a theorem attached: the height, not the latitude, sets the area, and that fact holds in every label. Change $\pi$ to $\hat\pi$ and you have changed nothing about geometry and everything about one numeral. Computed, never measured — and, on this surface, computed once and then multiplied.

## Further Reading

- [The Witch of Agnesi: Why a Curve Traced by Straight Lines Encloses Exactly Four Times the Generating Circle](/blog/posts/2026-11-17-witch-of-agnesi-exact-quadrature-golden-pi/) — the other classical result where an exact multiple of a circle's area falls out of a construction with no integration.
- [The Pseudosphere: Why Sweeping a Tractrix Around Its Axis Reproduces the Sphere's Area Exactly](/blog/posts/2026-11-15-pseudosphere-tractrix-constant-curvature-golden-pi/) — the same $4\pi R^{2}$ arriving from a surface of constant negative curvature, and why the coincidence is not one.
- [Pappus's Centroid Theorem: Why Sweeping an Area Through One Turn Gives V = 2πR·A](/blog/posts/2026-10-30-pappus-centroid-theorem-torus-swept-area-golden-pi/) — the bookkeeping rule for how many powers of the constant a swept solid carries.
- [Archimedes and the Exhaustion of the Circle](/blog/posts/2026-07-25-archimedes-golden-pi-exhaustion/) — the method that produced both theorems, and the cube-law by which its error shrinks.
- [Squaring the Circle: The Golden Pi Geometric Proof](/blog/posts/squaring-circle-golden-pi-geometric-proof/) — the radius $\varphi^{1/4}$ at which a disc's area is exactly $4$, and the sphere of radius $\varphi^{1/4}/2$ that does the same in three dimensions.
