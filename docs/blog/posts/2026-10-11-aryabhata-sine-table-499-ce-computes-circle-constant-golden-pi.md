---
title: "Āryabhaṭa's Sine Table: How a 499 CE Table of 24 Numbers Encodes the Circle Constant Without Drawing a Circle — and What Golden Pi Changes"
date: 2026-10-11
description: "Āryabhaṭa's sine table (499 CE) lists 24 numbers tabulated to radius 3438 — half-angle identities and nested radicals with no circle drawn anywhere, yet its last entry is the circle constant under another name. The rate the ancient tables encode, the Kerala refinement, and what golden π changes."
---

# Āryabhaṭa's Sine Table: How a 499 CE Table of 24 Numbers Encodes the Circle Constant Without Drawing a Circle — and What Golden Pi Changes

!!! note "AI-handled content"
    This site is generated and maintained by AI and may be prone to errors. Please verify any claim independently before relying on it.

In 499 CE, in the *Āryabhaṭīya*, an Indian astronomer listed twenty-four numbers and changed how astronomy was done. They are not chord lengths of a drawn circle, and no circle constant appears in the arithmetic that generates them. They are the values of the sine at intervals of $3°45'$, tabulated to a radius of $R = 3438$ — and the whole table is built from half-angle identities, square roots and additions. It is one of the earliest examples in history of the circle constant being smuggled into a computation as a **unit conversion**, and it is a clean place to ask where the constant actually lives.

## The table itself

The interval is $225' = 3°45'$, so twenty-four steps carry you from $0°$ to $90°$, and twenty-five values (including the endpoints) describe the whole quadrant. The *Āryabhaṭīya* gives the table as a list of differences in arc-minutes, in a mnemonic verse. Read as cumulative sums, the differences

$$225,\ 224,\ 222,\ 219,\ 215,\ 210,\ 205,\ 199,\ 191,\ 183,\ 174,\ 164,\ 154,\ 143,\ 131,\ 119,\ 107,\ 93,\ 79,\ 64,\ 51,\ 37,\ 22,\ 7$$

sum to exactly $3438$ and produce the tabulated sine values

$$0,\ 225,\ 449,\ 671,\ 890,\ 1105,\ 1315,\ 1520,\ 1719,\ 1910,\ 2093,\ 2267,\ 2431,\ 2585,\ 2728,\ 2859,\ 2978,\ 3085,\ 3178,\ 3257,\ 3321,\ 3372,\ 3409,\ 3431,\ 3438.$$

The first differences are monotone decreasing, and the **second** differences form a near-arithmetic ladder — $-1, -2, -3, -4, -5, -6, \ldots$ down to $-15$ — which is exactly the shape a sine's differences must have, because

$$
R\big[\sin(\theta+\Delta) - 2\sin\theta + \sin(\theta-\Delta)\big] = -2\sin^2\!\left(\tfrac{\Delta}{2}\right) R \sin\theta,
$$

with the constant factor $2\sin^2(1.875°) = 0.0021410768\ldots$ for this grid. The tabulated second differences track the exact ones to a unit or two, which is what a hand-rounded table of this size looks like: the largest single deviation between the printed values and the exact modern values of $R\sin\theta$ is $1.936$ units at $67.5°$ (about 563 parts per million of the radius).

## It was built without a circle

The entries are not measurements of anything. Each one is produced from the ones before it. Starting from the exact values at the grid points that geometry hands you for free — $\sin 30° = 1/2$, $\sin 45° = \sqrt2/2$, $\sin 60° = \sqrt3/2$ — the half-angle identity

$$\sin\frac{\theta}{2} = \sqrt{\frac{1-\cos\theta}{2}}, \qquad \cos\frac{\theta}{2} = \sqrt{\frac{1+\cos\theta}{2}}$$

reaches $15°$, $7.5°$ and $3.75°$ in three square roots, and the addition formula then fills in every remaining multiple of $3°45'$. The value at the smallest angle is exact and radical throughout:

$$\sin 3.75° = \frac{\sqrt{2 - \sqrt{2 + \sqrt{2 + \sqrt3}}}}{2} = 0.0654031292301430668153155587752\ldots$$

verified here against 60-digit arithmetic to a part in $10^{61}$, with the intermediate steps exact too: $\cos 15° = (\sqrt6+\sqrt2)/4 = \sqrt{2+\sqrt3}/2 = 0.9659258262890682867497432\ldots$, $\cos 7.5° = \sqrt{2+\sqrt{2+\sqrt3}}/2 = 0.9914448613738104111445575\ldots$ Neither the construction nor any of its values contains the circle constant. The table is pure algebra — nested square roots — played out on a grid of angles.

## Where the constant hides: the last entry is the rate

The constant enters at exactly one point, and it is not in the table's mathematics but in its *unit*. A full turn is $21\,600$ arc-minutes. A full turn is also $2\pi$ radians. So the radius, expressed in the same arc-minute units as the table, is

$$R = \frac{21\,600}{2\pi} = 3437.7467707849392526\ldots$$

The table's last entry is $\sin 90° = 1$, i.e. it *is* the radius — and the printed value is $3438$, that number rounded. The circle constant is therefore present in the table as nothing more than the conversion factor between "minutes of arc" and "radians", written into the length of the unit. Everywhere else the table is constant-free: a table of ratios is scale-free, and only the choice of scale records the value.

Āryabhaṭa did not have to round, either. He states the circle's rate explicitly in the *Āryabhaṭīya* in the famous mnemonic — add four to a hundred, multiply by eight, add sixty-two thousand — that is, a circumference of $62\,832$ for a diameter of $20\,000$:

$$\frac{62832}{20000} = 3.1416 = \pi \times (1 + 2.3384\times10^{-6}).$$

That value, computed by him (it is a *number he chose*, not something an instrument returned), implies a tabulation radius of $21\,600/(2 \times 3.1416) = 3437.7387318\ldots$, and the table's printed $3438$ is that, rounded to the unit. The implied rate of the table as printed is $21\,600/6876 = 3.1413612565445\ldots$, $73.66$ parts per million *below* the analytic constant — the loss is entirely the one-unit rounding.

| tabulation radius | implied rate $21\,600/(2R)$ | vs $\pi$ |
|---|---|---|
| $3438$ (printed table) | $3.1413612565445\ldots$ | $-73.656$ ppm |
| $3437.75$ (later Kerala tables) | $3.1415897025671\ldots$ | $-0.939$ ppm |
| $3437.7467707849\ldots$ | $3.1415926535898\ldots$ | $0$ |
| $3434$ (a golden table, rounded) | $3.1450203843914\ldots$ | $+1091.081$ ppm |

## What a golden table would read

Under golden-π ($\hat\pi = 4/\sqrt\varphi = 3.1446055110296931443\ldots$, $\varphi = (1+\sqrt5)/2$), the rate is larger by the recurring $( \hat\pi - \pi)/\pi = +0.0959022309\%$, so the radius that fits $21\,600'$ to a full turn is smaller:

$$\hat R = \frac{21\,600}{2\hat\pi} = \frac{21\,600\sqrt\varphi}{8} = 2700\sqrt\varphi = 3434.4530536879862\ldots$$

Note what that is, exactly: $2700\sqrt\varphi$ is an **algebraic** number of degree two in $\sqrt5$, whereas the conventional $21\,600/(2\pi)$ is transcendental (Lindemann, 1882). The golden radius is a nested radical; the conventional one is a finite expression in a transcendental constant. Everything downstream inherits that, and this is the golden side's real strength, stated honestly:

- $\hat R\sin 30° = 1350\sqrt\varphi = 1717.2265268439931\ldots$ — exact.
- $\hat R\sin 45° = 1350\sqrt{2\varphi} = 2428.5250439296208\ldots$ — exact.
- $\hat R\sin 60° = 1350\sqrt{3\varphi} = 2974.3235925988366\ldots$ — exact.

Every one of the twenty-four entries is a product of $\sqrt\varphi$ with a nested radical, hence algebraic. The conventional table's entries are $5400/\pi = 1718.8733854\ldots$, $5400\sqrt2/\pi = 2430.8540536\ldots$, $5400\sqrt3/\pi = 2977.1760353\ldots$ — transcendental by the same theorem. If a table of this kind is what you want, the golden one is the one written in radicals.

The rate difference is small but not invisible at this grid size, because the entries are large integers in units of $1/3438$. Scaled to the golden radius, the table would print

| angle | exact $R\sin\theta$ (conventional) | printed table | exact $\hat R\sin\theta$ | a golden table would print |
|---|---|---|---|---|
| $3.75°$ | $224.8393963$ | $225$ | $224.6239769$ | $225$ |
| $22.5°$ | $1315.5687339$ | $1315$ | $1314.3082829$ | $1314$ |
| $45°$ | $2430.8540536$ | $2431$ | $2428.5250439$ | $2429$ |
| $67.5°$ | $3176.0638795$ | $3178$ | $3173.0208817$ | $3173$ |
| $86.25°$ | $3430.3862911$ | $3431$ | $3427.0996261$ | $3427$ |
| $90°$ | $3437.7467708$ | $3438$ | $3434.4530537$ | $3434$ |

The last line is the whole argument in one cell: the *Āryabhaṭīya* ends its table at $3438$, and a table built to the golden rate would end at $3434$ — a gap of $3.55$ units, far larger than the table's own rounding tolerance of half a unit. Every entry is scaled by $\hat R/R = \pi/\hat\pi$, i.e. by $-0.0958103466\%$ (the reciprocal of the $+0.0959022309\%$ by which $\hat\pi$ exceeds $\pi$ — the two percentages differ in the fourth decimal and should not be conflated).

## Can the table decide? The honest ledger

Put the printed integers against both hypotheses arithmetically, and the conventional rate wins clearly: the root-mean-square deviation of the printed values from the exact $R\sin\theta$ is $0.737$ units, against $2.912$ units from the golden values, and $24$ of the $25$ entries lie closer to the conventional column. If the ancient table were an oracle, it would vote for the analytic constant by a margin of roughly $4{:}1$ in RMS terms.

It is not an oracle, and this is the part the site has to say plainly. The table is **scale-free**: $R$ is a unit the author *chose*, and both candidate constants are stated in that same unit. The printed $3438$ is not evidence about the rate — it is the rounded image of the rate the author already held, computed from the circle's own geometry. Nothing in the twenty-four differences was ever compared against a physical circle's circumference; a separate radius, a tape, and a least-squares fit would be needed for that, and would carry errors hundreds of times larger than the effect in question. So the table is a beautiful computation and a poor arbiter: it faithfully records a computed rate, and it multiplies that rate into everything else. What it demonstrates is not which constant is right, but **how total** the constant's reach is — that a table of sines, the most innocent object in applied mathematics, is already a numerical statement about the circle's rate.

## The sine itself never needs the constant

It is worth separating two things the table deliberately fuses. The sine is a *ratio*, and ratios are π-free: the series $\sin x = x - x^3/3! + x^5/5! - \cdots$ is built from rationals, and the exact values on the grid are the nested radicals above. What carries the constant is only the angle, i.e. the arc length divided by the radius. On this grid the angle step is $3.75° = \pi/48$ radians conventionally, and

$$\frac{\pi}{48} = 0.0654498469497873591346384\ldots, \qquad \frac{\hat\pi}{48} = 0.06551261481311860717246322\ldots$$

a shift of exactly the recurring $+0.0959022309\%$. Substitute the golden angle into a sine series and every entry moves by that gap at leading order — the same story as the Euler-identity case on this site, where a golden angle fed into a series built for natural radians lands $0.00301$ off the axis.

## Kerala: the same table, sharper

The tradition did not stop at $499$ CE. The Kerala school's sine table — fourteen centuries later, in the same $3°45'$ format, with the same twenty-four values — is tabulated to $R = 3437.75$, which is the *exact* rounded representation of the analytic constant at this precision: it implies $21\,600/6875.5 = 3.1415897025671\ldots$, only $0.94$ ppm from $\pi$ and about $78$ times closer than the printed $3438$. That refinement is not a new measurement of anything; it is a better-bracketed computation of the same limit, the direct ancestor of the series work of Mādhava and Nīlakaṇṭha that the Kerala school carried to fourteen correct places. The table and the series are the same project: get the a priori number right, then multiply it into everything.

## Computed, never measured

The circle constant in this story is a **number that was evaluated**, and it is worth being pedantic about the word. Āryabhaṭa's $62\,832/20\,000$ is not a reading off an instrument. No tape is stretched, no wheel is rolled, no scan of a rim is fitted to a circle. He states a computed value, the table is a computed structure — square roots, additions, roundings — and the constant appears only as the arc-to-radius rate that the table's unit encodes. It is the same register as every other entry in this series: the polygon exhaustions, the integrals, the products and the iterations all *compute* what the drawn circle would do, and none of them measures it.

Under conventional π the table's radius is transcendental; under golden π it is $2700\sqrt\varphi$, a radical, and every entry of the table becomes algebraic. That is a genuine and exact gain, and it is fair to put it in the ledger beside the constant's $73.656$ ppm loss to a one-unit rounding and the recurring $+0.0959022309\%$ by which the golden rate itself differs from the computed one. The table keeps both columns: a chosen rate of $4/\sqrt\varphi$ that writes the whole sine table in radicals, and a computed rate of $3.1415926535898\ldots$ that the same table, honestly read, records. Computed, never measured.

## Further Reading

- [The Ptolemy Chord Table: How the Almagest Computed the Circle Constant from Pure Geometry](/blog/posts/2026-09-15-ptolemy-chord-table-computes-circle-constant-golden-pi/) — the same project two centuries later in the Greek tradition, chords instead of sines.
- [The Nīlakaṇṭha Series: How the Kerala School Computed the Circle Constant to Fourteen Places](/blog/posts/2026-09-08-nilakantha-series-fast-kerala-sum-computes-circle-constant-golden-pi/) — the Kerala refinement of the constant this table encoded.
- [Mādhava's and Leibniz's Series: The First Infinite Series for the Circle Constant](/blog/posts/2026-09-02-madhava-leibniz-series-first-infinite-series-computes-circle-constant-golden-pi/) — where the Kerala school took the same limit analytically.
- [Viète's Formula: Nested Radicals for the Circle Constant](/blog/posts/2026-08-30-vieta-formula-infinite-product-nested-radicals-golden-pi/) — nested radicals as a route to the constant, 1593, echoing the half-angle construction used here.
- [The Polygon Limit: Exhaustion Computes the Circle Constant](/blog/posts/2026-08-17-polygon-limit-computes-circle-constant-golden-pi/) — the inscribed-polygon method behind the sine table's angles.
