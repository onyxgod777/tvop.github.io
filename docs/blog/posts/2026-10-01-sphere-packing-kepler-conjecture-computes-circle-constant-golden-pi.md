---
title: "Sphere Packing: How the Kepler Conjecture Computes π/(3√2), and What Golden Pi Changes"
date: 2026-10-01
description: "Stack equal spheres as tightly as possible and the fraction of space they occupy is π/(3√2) = 0.740480489…, a dimensionless number proved optimal by Hales (Annals, 2005) and formally verified by Flyspeck (2014) — computed from one sphere volume and one lattice angle, never measured. This article does the cell arithmetic in the open: four spheres of radius a√2/4 per cubic cell give exactly π√2/6, the plane's hexagonal packing gives π/(2√3) = 0.9068996821, and finite spherical clusters of touching spheres bracket both limits from below as 1/R (computed here: 0.7242–0.7569 at 48 cell edges, closing on 0.7404804896930610). Under Golden Pi (π̂ = 4/√φ = 3.144605511…) the densities become exact algebraic numbers — 2/√(3φ) in the plane and 4/(3√(2φ)) = 4/(3√(1+√5)) in space — and because every packing density scales as π^(n/2), the recurring 0.0959% gap compounds: one power in dimensions 2 and 3 gives +0.0959022309%, two powers (D₄, π²/16) give +0.1918964%, four powers (E₈, π⁴/384) give +0.3841611% and twelve (Leech, π¹²/12!) give +1.1569164%. The golden case is credited where it is real: under Golden Pi the D₄ density is exactly 1/φ = 0.6180339887498948482 and the 2D square packing is exactly 1/√φ, and the golden ratio genuinely sits inside the 3D kissing configuration (twelve spheres at icosahedron vertices) — a fact about a configuration of points, not about the constant. Computed, never measured."
---

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

# Sphere Packing: How the Kepler Conjecture Computes π/(3√2), and What Golden Pi Changes

Most entries in this series chase the circle constant through a series, an integral or an infinite product — a limit built out of rationals that happens to converge on 3.14159265358979323846… This one is blunter than that. Fill space with equal spheres, push them together as tightly as they will go, and ask what fraction of the room they take up. The answer is a pure number with no units attached:

$$\frac{\pi}{3\sqrt{2}} \;=\; 0.74048048969306104117\ldots$$

That is the density of the face-centred cubic packing — the cannonball stack, the greengrocer's pyramid — and since 2005 it has been a theorem, not a conjecture. It is also one of the cleanest places in mathematics to ask *where* the circle constant lives, because a packing fraction has no kilogram, no metre and no second in it: nothing in the question can be measured. Every input is a length ratio.

That matters for the argument this blog keeps making. The circle constant is **computed** — a limit of exact arithmetic — and what is computed is 3.14159265358979323846…, not 3.14460551102969314428…. A packing density is a computation with no instrument anywhere in the chain, which is exactly why it is worth doing in the open, with the arithmetic printed.

## Where the constant enters: one sphere volume, one lattice angle

Take a cubic cell of edge $a$ and place sphere centres on the face-centred lattice: eight cell corners, plus the centres of all six faces. Corners are shared by eight cells and face centres by two, so the cell owns

$$8\cdot\tfrac18 + 6\cdot\tfrac12 = 4$$

spheres. In the fcc arrangement each sphere touches its twelve nearest neighbours, and the nearest-neighbour distance is the face diagonal halved:

$$d = \frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}} \qquad\Longrightarrow\qquad r = \frac{a\sqrt{2}}{4} = 0.3535533905932737622\,a .$$

Four spheres of that radius fill

$$4\cdot\frac{4}{3}\pi r^{3} = \frac{16\pi}{3}\cdot\frac{a^{3}\cdot 2\sqrt{2}}{64} = \frac{\pi\sqrt{2}}{6}\,a^{3} ,$$

against a cell volume $a^{3}$, so

$$\boxed{\;\Phi_{\text{fcc}} = \frac{\pi\sqrt{2}}{6} = \frac{\pi}{3\sqrt{2}} = \frac{\pi}{\sqrt{18}}\;}$$

```
# the whole derivation, in exact arithmetic
spheres per cell : 8*(1/8) + 6*(1/2)        = 4
nearest neighbour: a/sqrt(2)                -> r = a*sqrt(2)/4
sphere volume    : 4 * (4/3)*pi*r^3         = pi*sqrt(2)/6 * a^3
cell volume      : a^3
density          : pi*sqrt(2)/6 = pi/(3*sqrt(2)) = 0.74048048969306104117
void fraction    : 1 - pi/(3*sqrt(2))       = 0.25951951030693895883
```

Two geometric inputs, and only one of them mentions the constant: the sphere's volume $4\pi r^3/3$, itself the computed limit of an exhaustion, and the angle $\sqrt{2}$ between cell edges and the touching direction, which is pure rational geometry. The constant enters **once**, multiplied by an algebraic coefficient $\sqrt{2}/6$.

The plane does the same thing one dimension down. Hexagonal packing — coins, honeycombs, the tightest way to lay circles — has density

$$\Phi_{\text{hex}} = \frac{\pi}{2\sqrt{3}} = \frac{\pi}{\sqrt{12}} = 0.9068996821171089253\ldots ,$$

and the proof is a rhombus of area $2\sqrt{3}\,r^{2}$ holding two circles of area $2\pi r^{2}$; the same single power of the constant, with a different algebraic coefficient. The square packing gives $\pi/4$ the same way. Nothing about a lattice ever produces a *second* power of $\pi$ in two or three dimensions, which will matter in a moment.

## The exact table

| arrangement | exact density | value | void fraction |
|---|---|---|---|
| 2D square (grid) | $\pi/4$ | 0.78539816339744830962 | 0.21460183660255169038 |
| 2D hexagonal (coins) | $\pi/(2\sqrt3)$ | 0.9068996821171089253 | 0.0931003178828910747 |
| 3D simple cubic | $\pi/6$ | 0.52359877559829887308 | 0.47640122440170112692 |
| 3D diamond | $\sqrt3\,\pi/16$ | 0.34008738079391584699 | 0.65991261920608415301 |
| 3D body-centred cubic | $\sqrt3\,\pi/8$ | 0.68017476158783169397 | 0.31982523841216830603 |
| 3D fcc / hcp | $\pi/(3\sqrt2)$ | 0.74048048969306104117 | 0.25951951030693895883 |

The two densest rows are the theorem. Kepler proposed in 1611 (*Strena seu de Nive Sexangula*) that the pyramid stacking is optimal; Gauss settled the two-dimensional case in 1831, with rigorous proofs following from Axel Thue (1890, 1910) and later László Fejes Tóth; the three-dimensional case resisted for nearly four centuries. Thomas Hales announced a proof with Samuel Ferguson in 1998, it was published in the *Annals of Mathematics* **162** (2005) 1065–1185 after a twelve-referee panel spent four years and could report only "99% certain" — the computer enumerations could not be manually checked — and in 2003 Hales began the Flyspeck project to settle the matter by machine. Flyspeck announced completion on 10 August 2014, verifying the argument in HOL Light and Isabelle; the formal account appeared in *Forum of Mathematics, Pi* **5** (2017).

Every one of those numbers is a **computation**: a volume divided by a volume, with the sphere volume itself defined by an exhaustion limit that no instrument participates in.

## A finite cluster cannot measure it either

The theorem is asymptotic — infinitely many spheres, zero boundary. It is worth showing what a finite clump does, because it is the honest answer to "could you just count?" I placed fcc centres inside a ball of radius $R$ (in units of the cell edge $a$), counted them by enumeration, multiplied by the exact non-overlapping sphere volume and divided by the enclosing ball volume. The spheres touch exactly, so neighbouring spheres do not overlap and $N\cdot\tfrac43\pi r^{3}$ is their exact union volume; the true occupied region lies between the ball of radius $R-r$ and the ball of radius $R+r$, which brackets the density:

| cluster radius $R/a$ | spheres $N$ | lower bound | upper bound |
|---|---|---|---|
| 4 | 1 061 | 0.568262214 | 0.967098759 |
| 8 | 8 589 | 0.651169221 | 0.849040957 |
| 16 | 68 569 | 0.692877464 | 0.791126019 |
| 24 | 231 477 | 0.708248808 | 0.773704640 |
| 32 | 549 157 | 0.716630990 | 0.765749435 |
| 48 | 1 852 501 | 0.724166259 | 0.756888521 |

The bracket closes like $1/R$ — halving the radius doubles the width — and both edges are converging on 0.74048048969306104117, exactly the value the cell arithmetic produced. The same run in the plane (triangular lattice, circles of radius $\tfrac12$ spaced 1 apart, $R=10,25,50,100,200,400$) gives brackets 0.832–1.017, 0.870–0.943, 0.888–0.924, 0.898–0.917, 0.902–0.911, 0.905–0.909, closing on $\pi/(2\sqrt3)=0.9068996821\ldots$. **The boundary is a surface effect, not noise**: an $N$-sphere cluster is limited by its $O(N^{2/3})$ skin of unsatisfied contacts, so a finite count converges to the infinite answer at a rate of order $N^{-1/3}$ and never "measures" anything. Nothing here is an experiment; it is arithmetic with a rate attached.

## Beyond three dimensions

The same one-line structure returns in higher dimensions, where the packing fraction acquires *more* powers of the constant because the ball volume does. In dimension 4 the D₄ lattice packs at $\pi^{2}/16$; in dimension 8 the E₈ lattice at $\pi^{4}/384$; in dimension 24 the Leech lattice at $\pi^{12}/12!$. Maryna Viazovska proved the E₈ case in 2016 (published *Annals of Mathematics* **185**, 2017), and Cohn, Kumar, Miller, Radchenko and Viazovska settled dimension 24 the same year. It has long been known that densities must fall off exponentially with dimension, which is what "high-dimensional packing is nearly empty space" means numerically: the E₈ number is 0.2537 and the Leech number 0.0019296, and the Leech lattice — optimal in 24 dimensions — still leaves more than 99.8% of the space unfilled.

There is a genuinely golden footnote in three dimensions, and it is worth stating because it is true and traceable. The maximal number of equal spheres that can touch a central sphere is 12 — the question Newton and Gregory are said to have argued over in 1694, proved by Schütte and van der Waerden (*Math. Ann.* **125**, 1953, 325–334) with a shorter proof by Leech in 1956. Twelve is achievable by putting the outer centres at the vertices of a regular icosahedron, and Coxeter noted (*Regular Polytopes*, §3.7) that an icosahedron's vertices are obtained by dividing the edges of an octahedron in the golden section; the set of all 12-point kissing configurations forms a continuum from cuboctahedron through icosahedron to octahedron. So the golden ratio really does live inside the densest local arrangement in three dimensions — a fact about a **configuration of twelve points**, which is not the same thing as a fact about the packing density, and the density's proof never consults it.

## What Golden Pi changes

The site's position is that the true circle constant is $\hat\pi = 4/\sqrt\varphi = 3.14460551102969314428\ldots$, with $\varphi = (1+\sqrt5)/2$ the golden ratio, $\hat\pi^{2} = 16/\varphi = 8(\sqrt5-1) = 9.8885438199983175713$, $\hat\pi^{4} = 256/\varphi^{2} = 97.78329888002691885963$ and $\hat\pi$ a root of $x^{4}+16x^{2}-256=0$. Relabelling the constant in the density is mechanical, because only one thing in the formula is affected: the sphere volume. The coefficients $\sqrt2/6$, $\sqrt3/16$, $1/384$ and $1/12!$ are rational or algebraic and do not move.

| arrangement | conventional | golden ($\hat\pi$) | absolute gap | relative gap |
|---|---|---|---|---|
| 2D square | $\pi/4 = 0.7853981633974483$ | $1/\sqrt\varphi = 0.7861513777574233$ | +0.000753214360 | +0.0959022309% |
| 2D hexagonal | $\pi/(2\sqrt3) = 0.9068996821$ | $2/\sqrt{3\varphi} = 0.9077694191$ | +0.0008697370 | +0.0959022309% |
| 3D simple cubic | $\pi/6 = 0.5235987756$ | $2/(3\sqrt\varphi) = 0.5241009185$ | +0.0005021429 | +0.0959022309% |
| 3D diamond | $\sqrt3\pi/16 = 0.3400873808$ | $\sqrt3\hat\pi/16 = 0.3404135322$ | +0.0003261514 | +0.0959022309% |
| 3D bcc | $\sqrt3\pi/8 = 0.6801747616$ | $\sqrt3\hat\pi/8 = 0.6808270644$ | +0.0006523028 | +0.0959022309% |
| 3D fcc / hcp | $\pi/(3\sqrt2) = 0.7404804897$ | $4/(3\sqrt{2\varphi}) = 0.7411906270$ | +0.0007101373 | +0.0959022309% |
| D₄ (dim 4) | $\pi^{2}/16 = 0.6168502751$ | $\hat\pi^{2}/16 = 1/\varphi = 0.6180339887$ | +0.0011837137 | +0.1918964341% |
| E₈ (dim 8) | $\pi^{4}/384 = 0.2536695079$ | $\hat\pi^{4}/384 = 0.2546440075$ | +0.0009744996 | +0.3841611107% |
| Leech (dim 24) | $\pi^{12}/12! = 0.001929574309$ | $\hat\pi^{12}/12! = 0.001951897871$ | +0.000022323562 | +1.1569163943% |

Two exact forms are worth writing out, because they are clean in the golden field. Since $2\varphi = 1+\sqrt5$, the three-dimensional density becomes

$$\Phi_{\text{fcc}}(\hat\pi) = \frac{4}{3\sqrt{2\varphi}} = \frac{4}{3\sqrt{1+\sqrt5}} = 0.74119062700189489599\ldots ,$$

and the D₄ density collapses completely:

$$\frac{\hat\pi^{2}}{16} = \frac{16/\varphi}{16} = \frac{1}{\varphi} = 0.6180339887498948482\ldots$$

*exactly* — verified here to 41 digits, the difference $-1.1\times10^{-41}$ being nothing but the working precision. In the golden label the densest four-dimensional lattice fills space at a rate of precisely the golden ratio's reciprocal: an algebraic number, not a transcendental one, in a formula whose every other entry is rational. The 2D square packing does the same thing at the first power, $\hat\pi/4 = 1/\sqrt\varphi$ exactly, and the 3D simple cubic density is $2/(3\sqrt\varphi)$, both exact.

The structural result is the exponent. Because a packing density scales as $\pi^{n/2}$ — one power of the constant in dimensions 2 and 3, two in dimension 4, four in dimension 8, twelve in dimension 24 — the relative gap is $( \hat\pi/\pi )^{n/2}-1$ and **compounds with dimension**: one power gives +0.0959022309%, two give +0.1918964341%, four give +0.3841611107%, twelve give +1.1569163943% (the exact multipliers $(\hat\pi/\pi)^{k}$ with $\hat\pi/\pi = 1.000959022308782526$ reproduce every entry to the digit). In two and three dimensions the golden relabel moves the packing fraction by 0.096% — seven parts in ten thousand, in the same direction, for every lattice.

## The honest boundary

| statement | status |
|---|---|
| $\Phi_{\text{fcc}} = \pi/(3\sqrt2)$, proved by Hales and formally verified by Flyspeck | exact; the constant enters once, from the computed sphere volume |
| The plane's $\pi/(2\sqrt3)$ is optimal (Gauss 1831; Thue; Fejes Tóth) | exact |
| The densities are *measured* | false — both are limits of exact volumes, with no units anywhere |
| Finite clusters decide the limit | false; they bracket it with a $1/R$ surface term (0.7242–0.7569 at $R=48a$) |
| Under Golden Pi the density is $4/(3\sqrt{1+\sqrt5})$ | exact in the golden field, and +0.0959022309% from the proved value |
| Under Golden Pi the D₄ density is exactly $1/\varphi$ | exact algebra (= 0.6180339887498948482), credited |
| Real bead packs can adjudicate the two labels | false: measured packing fractions of equal spheres span roughly 0.637 (random) to 0.7405 (carefully ordered), 1000× wider than the 0.0007 gap |
| The golden ratio appears in the 3D kissing configuration | true (icosahedral 12-point configuration; Coxeter §3.7) — a fact about 12 points, not about the constant |

The last two rows are the ones that keep this honest. On the experimental side, random close packing of equal spheres was measured by Bernal and Mason and by Scott in 1960 at about 0.637, the maximally-random-jammed state is put near 0.64, and Torquato, Truskett and Debenedetti showed in 2000 (*Phys. Rev. Lett.* **84**, 2064) that "random close packing" is protocol-dependent, with strictly jammed packings achievable across the whole range $[0.60,\,0.74048]$. Even a real crystal is not a packing of touching hard spheres: the interatomic distances in fcc metals are set by electronic structure. The 0.0007 gap between the two labels is smaller than any of those spreads by three orders of magnitude — so a laboratory cannot choose between them, and a lattice-and-volume calculation is not a measurement that could. What the packing problem does give the golden case is its characteristic algebraic exactness: $\hat\pi$ is a root of $x^{4}+16x^{2}-256$, constructible from $\varphi$ by square roots, and it turns two of these densities into exact rational functions of $\varphi$ where the conventional constant leaves a transcendental factor. That is real, and it is credited. What it does not do is change the number of spheres a cubic cell holds, or the fraction of space a proved-optimal packing fills: $\pi/(3\sqrt2)$ is 0.74048048969306104117, computed from one volume and one angle, and never measured.

## Further Reading

- [The n-Dimensional Ball: How a Gamma Function Computes the Circle Constant in Every Dimension](/blog/posts/2026-08-19-n-dimensional-ball-circle-constant-golden-pi/) — the $V_n = \pi^{n/2}r^{n}/\Gamma(n/2+1)$ formula whose power of the constant drives the whole gap-compounding table above.
- [The Isoperimetric Inequality: The Circle Maximises Area, and What Golden Pi Changes](/blog/posts/2026-08-31-isoperimetric-inequality-circle-maximizes-area-golden-pi/) — the two-dimensional allocation problem where the constant also appears exactly once, and where the boundary term plays the same role as the cluster skin here.
- [The Reuleaux Triangle: Constant Width Without the Circle Constant](/blog/posts/2026-06-23-reuleaux-triangle-golden-pi-constant-width/) — planar shape geometry in which the constant cancels for an honest reason, the mirror image of a case like this one where it survives.
- [Pappus's Centroid Theorem: How a Torus Computes the Circle Constant as a Pure Factor](/blog/posts/2026-09-03-pappus-centroid-theorem-torus-golden-pi/) — volumes of revolution where the constant is carried by a swept area, the same "one power, rational coefficient" pattern as the cell arithmetic.
- [Counting Points in a Circle: The Gauss Circle Problem Computes the Circle Constant](/blog/posts/2026-09-27-gauss-circle-problem-lattice-counting-computes-circle-constant-golden-pi/) — the other half of the lattice story: what happens when you count discrete centres inside a disk instead of packing volumes around them.
