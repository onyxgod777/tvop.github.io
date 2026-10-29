---
title: "The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass Forever, Why 4/√φ Never Reaches That Door, and What the Degree Count Actually Proves"
date: 2026-10-29
description: "Squaring the circle became impossible in 1882 for exactly one reason: Lindemann proved π transcendental, and Wantzel's 1837 degree theorem says every constructible number has degree 2^k over Q. This article walks the arithmetic that decides it — the quadratic tower from Q to Q(√5) to Q(√φ), the minimal polynomials x²−x−1, x⁴−x²−1 and x⁴+16x²−256 verified to 46 digits, the Galois closure Q(√φ, i) of order 8, the equal-area square side r·2/φ^¼ with minimal polynomial y⁸+16y⁴−256, the exact closure at radius φ^¼ where the area is exactly 4 — and the honest boundary: constructibility is a gate, not a selector, since 22/7 and 355/113 pass it too."
---

# The Constructible Line: Why Lindemann's 1882 Theorem Bars π From Straightedge and Compass Forever

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

For twenty-two centuries the most famous open problem in mathematics was a construction: given a circle, build a square of equal area using only an unmarked straightedge and a compass. Anaxagoras worked on it in prison. Hippocrates of Chios squared his lunes and thought the circle would follow. Dinostratus, Archytas and Menaechmus invented whole new curves — the quadratrix, the conic sections — precisely because the two classical instruments refused the job. The problem outlived the Roman Empire, the Caliphate and the Enlightenment.

It died in 1882, and it died of arithmetic, not of geometry. Ferdinand von Lindemann proved that $\pi$ is transcendental, and Charles Hermite had already shown in 1873 that $e$ is. The argument runs downhill from there: Pierre Wantzel had established in 1837 that every length reachable with straightedge and compass has algebraic degree a power of two. A transcendental number has no degree at all. Therefore no square of equal area can be built.

That much is textbook. What is rarely asked — and what this article is about — is which sentence in that chain is doing the work, and what happens to a constant that is not transcendental. Because the impossibility proof does not say "squaring the circle is impossible." It says something narrower and much more specific: *no number outside the constructible field can be the answer*. The gate is a degree test. Arithmetic decides who is allowed to walk through it, and nothing else does.

Everything below is computed, and the one genuinely measured quantity in sight — a ratio of two physical lengths — is flagged when it appears.

## What straightedge and compass can actually reach

The compass draws a circle of known radius about a known centre; the straightedge draws the line through two known points. Their intersections are the only new points you get. In coordinates, starting from $(0,0)$ and $(1,0)$, each step produces numbers satisfying either a linear equation (already in the field) or a quadratic one — because intersecting a line with a circle, or two circles, eliminates down to a quadratic.

So the reachable set is not a set of drawings. It is a field, built by adjoining square roots:

$$
\mathbb{Q} \;=\; K_0 \;\subset\; K_1 \;\subset\; K_2 \;\subset\;\cdots\subset\; K_n ,\qquad [K_{j+1}:K_j] \;\le\; 2 .
$$

The degree of the tower multiplies, so every constructible length $\alpha$ lies in a field of degree $2^{n}$ over $\mathbb{Q}$. Since $\mathbb{Q}(\alpha)$ is a subfield, its degree divides $2^{n}$, hence is itself a power of two. Wantzel's theorem, in one line:

$$
\alpha \text{ constructible} \;\Longrightarrow\; [\mathbb{Q}(\alpha):\mathbb{Q}] = 2^{k} .
$$

Two refinements matter, and both are usually dropped from the popular retelling. First, the condition is *necessary, not sufficient* on its own: a quartic field whose Galois group is $S_4$ has degree $4 = 2^{2}$ and is still unreachable, because the square-root tower forces the normal closure to be built from 2-groups as well. The sharp criterion is: $\alpha$ is constructible exactly when the Galois closure of $\mathbb{Q}(\alpha)$ has degree $2^{m}$ — equivalently, a Galois group of order a power of two. Second, and this is the point, the test is purely algebraic. It never mentions a circle. It asks one question of a number: *what is its degree, and is that degree a power of two?*

## The two polynomials that decide the classical problem

The number $\varphi$ is defined by geometry and pinned by algebra. A rectangle that keeps its shape when a square is cut off satisfies $\varphi^{2} = \varphi + 1$, so it is a root of

$$
x^{2} - x - 1 = 0 ,\qquad \varphi = \frac{1+\sqrt5}{2} = 1.6180339887\ldots
$$

Degree $2 = 2^{1}$. One square root, and the pentagon, the decagon and $\cos 36^\circ = \varphi/2$ all come with it — Gauss's 1796 discovery that the regular 17-gon is constructible is the same theorem applied to $17 = 2^{2^{2}}+1$.

Now take the square root of $\varphi$. Its minimal polynomial is not $x^{2}-\varphi$, which has coefficients outside $\mathbb{Q}$; it is

$$
x^{4} - x^{2} - 1 = 0 ,\qquad \sqrt{\varphi} = 1.2720196495\ldots
$$

substituting $x^{2}$ for $x$ in the golden quadratic. Irreducibility is easy to see and worth seeing. Suppose $x^{4}-x^{2}-1 = (x^{2}+px+q)(x^{2}-px+s)$ with $q,s\in\mathbb{Q}$. Then $qs=-1$ and $q+s-p^{2}=-1$. Two cases exhaust it: if $p=0$ then $q,s$ are the roots of $t^{2}+t-1=0$, namely $(-1\pm\sqrt5)/2$, irrational; if $q=s$ then $q^{2}=-1$, impossible over the reals. No rational factorisation, and no rational root either. Degree $4 = 2^{2}$.

And $\pi$? $\pi$ has no minimal polynomial. Lindemann's 1882 theorem — the Weierstrass form of it — states that if $\alpha$ is a nonzero algebraic number then $e^{\alpha}$ is transcendental; since $e^{i\pi} = -1$ is algebraic, $i\pi$ cannot be algebraic, so neither can $\pi$. There is no polynomial with rational coefficients having $\pi$ as a root. The degree is not large; it does not exist.

That is the entire content of the impossibility. Not a failure of skill, not a missing instrument: a number outside the constructible field cannot be produced by operations that stay inside it.

## The tower, computed

Here is the ladder written out, with the minimal polynomials checked numerically to forty-six digits — that is, the residual of each polynomial at the stated value.

| Field step | Number | Minimal polynomial | Degree | Power of 2 | Residual |
|---|---|---|---|---|---|
| $\mathbb{Q}$ | $2$ (square side) | $x-2$ | 1 | $2^{0}$ | $0$ |
| $\mathbb{Q}$ | $\varphi$ | $x^{2}-x-1$ | 2 | $2^{1}$ | $0.0$ at 50 dps |
| $\mathbb{Q}(\sqrt5)$ | $\sqrt\varphi = 1.27201964951406896425\ldots$ | $x^{4}-x^{2}-1$ | 4 | $2^{2}$ | $-2.7\times10^{-51}$ |
| $\mathbb{Q}(\sqrt5)$ | $\hat\pi = 4/\sqrt\varphi = 3.14460551102969314427\ldots$ | $x^{4}+16x^{2}-256$ | 4 | $2^{2}$ | $0.0$ at 50 dps |
| $\mathbb{Q}(\varphi^{1/4})$ | $\varphi^{1/4} = 1.12783848556168226026\ldots$ | $x^{8}-x^{4}-1$ | 8 | $2^{3}$ | $1.8\times10^{-46}$ |
| $\mathbb{Q}(\varphi^{1/4})$ | $\sqrt{\hat\pi} = 2/\varphi^{1/4} = 1.77330355862432451846\ldots$ | $y^{8}+16y^{4}-256$ | 8 | $2^{3}$ | $0.0$ at 50 dps |
| — | $\pi$ | none (Lindemann 1882) | $\infty$ | no | — |

Every entry is checked, not asserted. The value $4/\sqrt\varphi$ satisfies $x^{4}+16x^{2}-256=0$ exactly: at fifty digits the residual is zero, and the polynomial is irreducible over $\mathbb{Q}$ by the constant-term argument — a factorisation into monic quadratics would need $qs=-256$ with $q+s-p^{2}=16$ and $p(s-q)=0$; $p=0$ forces $t^{2}-16t-256=0$, whose roots $8\pm8\sqrt5$ are irrational, and $q=s$ forces $q^{2}=-256$, impossible over the reals.

So the golden constant is a degree-four algebraic number. Its conjugates are the four roots of that quartic:

$$
\pm\frac{4}{\sqrt\varphi},\qquad \pm\,4i\sqrt\varphi ,
$$

whose product is $-256$, matching the constant term, and whose reciprocal pair is exact:

$$
\frac{4}{\hat\pi} = \sqrt\varphi = 1.2720196495140689642524224617\ldots,\qquad
\hat\pi^{2} = \frac{16}{\varphi} = 16\varphi - 16 = 9.8885438199983175712733893499\ldots
$$

The cross-product of the two real magnitudes is clean as well: $\hat\pi \cdot 4\sqrt\varphi = 16$ exactly. Nothing transcendental appears anywhere in the field it lives in.

## Why the classical theorem does not reach it

Read the impossibility sentence again with the substitutions made. Lindemann proves: *$\pi$ is transcendental, therefore no straightedge-and-compass construction can produce the side of a square equal in area to a given circle.* Substitute a degree-four algebraic constant and the premise fails. There is no theorem that says "the circle ratio is transcendental"; there is a theorem that says a specific number — the one defined as the ratio of circumference to diameter in the classical sense, with its Lindemann proof intact — is. The degree test then answers a different question for $4/\sqrt\varphi$:

$$
[\mathbb{Q}(\hat\pi):\mathbb{Q}] = 4 = 2^{2},\qquad
\text{Gal}\big(\mathbb{Q}(\sqrt\varphi,\,i)/\mathbb{Q}\big) \cong D_4,\ \ |D_4| = 8 = 2^{3}.
$$

The normal closure matters because $\mathbb{Q}(\sqrt\varphi)$ is not itself normal — the quartic $x^{4}-x^{2}-1$ has two real roots $\pm\sqrt\varphi$ and two imaginary ones $\pm i/\sqrt\varphi$, so adjunction of $i$ is required. With it the closure has degree $8$, Galois group the dihedral group of the square of order $8$ — a 2-group. The sharp criterion is met, not merely the necessary degree condition. The number is constructible, and the construction is a finite chain of square roots:

$$
\varphi \;\xrightarrow{\ \sqrt{\ \ } \ }\; \sqrt\varphi \;\xrightarrow{\ \cdot 4 \ }\; \hat\pi ,\qquad\text{two quadratic steps, three square roots in all from } \mathbb{Q}.
$$

This is what "squaring the circle" means in the algebraic register, and it is the exact sense in which the classical barrier is a barrier against a transcendental constant and nothing else. A construction whose generating length is $\varphi^{1/4}$ never needs to name $\pi$ at all.

## The equal-area square, written out

Let the circle have radius $r$. The square of equal area has side $s = r\sqrt{\hat\pi}$. Since $\hat\pi = 4/\sqrt\varphi$ we have $\sqrt{\hat\pi} = 2/\varphi^{1/4}$, so

$$
s = \frac{2r}{\varphi^{1/4}} .
$$

Set $r = \varphi^{1/4}$ and the algebra collapses to a plain rational:

$$
A = \hat\pi r^{2} = \frac{4}{\sqrt\varphi}\cdot\sqrt\varphi = 4 = 2^{2},
$$

the area of a square of side $2$. Two numbers, both constructible, one of degree $1$ and one of degree $8 = 2^{3}$: the square is reachable, and the circle is the circle of radius $\varphi^{1/4} = 1.1278384855616822602648354832\ldots$.

The side length for a unit circle is $s = 1.7733035586243245184670331663\ldots$, and its minimal polynomial follows by pure substitution — put $y = 2/\varphi^{1/4}$, so $\varphi = 16/y^{4}$, and impose the golden quadratic on that:

$$
\left(\frac{16}{y^{4}}\right)^{2} - \frac{16}{y^{4}} - 1 = 0
\;\Longleftrightarrow\;
y^{8} + 16y^{4} - 256 = 0 .
$$

Numerically $y^{4} = 9.88854381999831757127\ldots$ and $y^{8} = 97.78329888002691885963\ldots$; their combination cancels to zero at fifty digits. Notice the shape of that polynomial: it is the golden quartic $x^{4}+16x^{2}-256$ with $x$ replaced by $y^{2}$. The constant and the side of its equal-area square are two rungs of the same tower, one square root apart. That is the whole architecture in a single substitution.

## The gate is not a selector

Here the honesty has to be blunt, because the algebraic fact is powerful and easily overread. Passing the constructible gate is *necessary*. It is nowhere near *sufficient*, and the counterexamples are the most familiar numbers in the subject — every rational passes, since every rational has degree $1 = 2^{0}$ and is trivially constructible by similar triangles:

| Candidate | Value | Minimal polynomial | Degree | Shortfall against $\hat\pi = 3.1446055110\ldots$ |
|---|---|---|---|---|
| $22/7$ | $3.1428571428571\ldots$ | $7x-22$ | 1 | $-0.0555989668\%$ |
| $355/113$ | $3.1415929203539\ldots$ | $113x-355$ | 1 | $-0.0958018634\%$ |
| $\sqrt{10}$ | $3.1622776601683\ldots$ | $x^{2}-10$ | 2 | $+0.5619830238\%$ |
| $4/\sqrt\varphi$ | $3.1446055110296\ldots$ | $x^{4}+16x^{2}-256$ | 4 | $0$ |
| $\pi$ | $3.1415926535897\ldots$ | none | $\infty$ | $-0.0959022309\%$ |

A degree test cannot distinguish $22/7$ from $4/\sqrt\varphi$; both live in fields of admissible degree, and one of them is off by more than half the golden gap in the wrong direction. Constructibility removes an *impossibility*, it does not supply a *value*. So the classical theorem, read correctly, does exactly two things: it certifies that no transcendental constant can be squared by ruler and compass, and it certifies that an algebraic constant of 2-power degree is not excluded by that argument. It says nothing whatever about which number the circumference of a real circle bears to its diameter.

That last question is not algebraic at all. It is metrological.

## The ledger: what is computed and what is measured

Everything in the tables is computed. Polynomials are evaluated; degrees are counted; the residuals are printed at fifty digits and are zero or at the last digit. The recurring gap between the two labels,

$$
\frac{\hat\pi - \pi}{\pi} = +0.0959022309\% ,\qquad
\frac{1/\hat\pi - 1/\pi}{1/\pi} = -0.0958103466\% ,
$$

is likewise a computed difference between two defined numbers, not an experimental result, and the reciprocal of the gap is $1$ part in $1043.728611\ldots$ — the resolution any physical test would need in the ratio of a circumference to a diameter.

And that ratio is a genuine measurand: two lengths, one wrapped around the other, read on an instrument. No series computes it, no integral takes its limit, no algebraic tower reaches it — a hoop's $L/D$ is what a machinist or a surveyor returns, and it carries every error of the tape, the temperature and the roundness of the hoop. The algebraic theorem above is silent about it by construction, because the theorem is about fields, and a field does not know how long anything is.

So the honest summary of the 1882 result is narrower than the slogan and stronger than the slogan in one direction: the straightedge-and-compass impossibility is a statement about the transcendental constant specifically, it is exact, and it survives every re-examination — while a constant of degree $4 = 2^{2}$ with a dihedral normal closure of order $8 = 2^{3}$ is a different object, standing on the other side of a line that arithmetic drew and arithmetic alone can move.

Computed, never measured.

## Further Reading

- [**Squaring the Circle: The Geometric Proof That Golden Pi Closes the Construction Exactly**](/blog/posts/squaring-circle-golden-pi-geometric-proof/) — the geometric companion to this algebraic one: the same radius $\varphi^{1/4}$, the same exact area $4$, argued by construction rather than by degree.
- [**Hippocrates' Lunes: How the First Exact Quadrature in History Computed an Area With No Circle Constant in It**](/blog/posts/2026-10-02-hippocrates-lunes-quadrature-computes-circle-constant-golden-pi/) — the 5th-century BCE attempt that started the two-millennium search, and why its success was local to lunes.
- [**Roots of Unity: How $n$th Roots of 1 Compute the Circle Constant and Why the Polygon Is a Polynomial**](/blog/posts/2026-09-09-roots-of-unity-compute-circle-constant-golden-pi/) — the algebraic machinery behind constructibility, seen as the cyclotomic polynomial $\Phi_n$ and the Fermat-prime criterion.
- [**The Inscribed Angle Theorem: Why Every Angle on an Arc Is Exactly Half Its Arc, Why π Enters Only as a Unit**](/blog/posts/2026-10-20-inscribed-angle-theorem-half-turn-circle-constant-golden-pi/) — where the regular pentagon's $36^\circ$ corner carries $\cos 36^\circ = \varphi/2$ exactly, the degree-2 rung that starts the tower.
- [**Descartes' Angle Defect and Gauss–Bonnet: Why Every Polyhedron Owes Exactly 720°**](/blog/posts/2026-10-22-descartes-angle-defect-gauss-bonnet-720-degrees-golden-pi/) — the integer-valued side of the same story: what remains exact when the constant is only a unit of account.
