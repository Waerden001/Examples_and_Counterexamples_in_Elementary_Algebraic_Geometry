---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/curves.tex
---

## Curves

### Example: Smooth curve of any genus {#ecag-0130}

For every integer $g \geq 0$, there exists a smooth projective curve of genus $g$ over an algebraically closed field $k$. Two families of curves suffice to realize all genera.

**Plane curves.** A smooth plane curve $C \subset \mathbb{P}^2_k$ of degree $d$ has genus

$$
g = \frac{(d-1)(d-2)}{2}

$$

by the degree-genus formula. The values produced are $g = 0, 1, 3, 6, 10, \ldots$ (triangular numbers), so most genera are missing.

**Curves on $\mathbb{P}^1 \times \mathbb{P}^1$.** A smooth curve $C$ of bidegree $(a, b)$ on $\mathbb{P}^1 \times \mathbb{P}^1$ has genus determined by the adjunction formula. The canonical sheaf of $\mathbb{P}^1 \times \mathbb{P}^1$ is $\mathcal{O}(-2, -2)$, so

$$
\omega_C = \left(\omega_{\mathbb{P}^1 \times \mathbb{P}^1} \otimes \mathcal{O}(a, b)\right)\big|_C = \mathcal{O}(a - 2, b - 2)\big|_C.

$$

The degree of $\omega_C$ on $C$ is $(a-2)b + a(b-2) = 2ab - 2a - 2b$. Since $\deg(\omega_C) = 2g - 2$:

$$
g = (a-1)(b-1).

$$

Setting $b = 2$ gives $g = a - 1$ for any $a \geq 1$. By Bertini's theorem (in characteristic zero) or by explicit construction, smooth curves of bidegree $(a, 2)$ exist for all $a \geq 1$. Together with $g = 0$ (realized by $\mathbb{P}^1$), every non-negative integer arises as a genus.

The underlying reason is that the plane curve genus formula is quadratic in $d$, so it necessarily misses most values. Moving to $\mathbb{P}^1 \times \mathbb{P}^1$ replaces this with the bilinear formula $(a-1)(b-1)$, which with one variable fixed becomes linear and hits every integer.

| Bidegree $(a,2)$ | Genus $g = a-1$ | Degree of $\omega_C$ |
|:-:|:-:|:-:|
| $(1,2)$ | $0$ | $-2$ |
| $(2,2)$ | $1$ | $0$ |
| $(3,2)$ | $2$ | $2$ |
| $(4,2)$ | $3$ | $4$ |
| $(5,2)$ | $4$ | $6$ |

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth curve of bidegree $(5, 2)$ on $\mathbb{P}^1 \times \mathbb{P}^1$ over an algebraically closed field of characteristic zero. Compute the genus of $C$ and determine $\deg(\omega_C)$ as a divisor on $C$. -->

### Example: Unirational curves are all rational, birational $\neq$ isomorphism {#ecag-0131}

Every unirational curve over an algebraically closed field is rational (Luroth's theorem). However, a birational morphism between curves need not be an isomorphism: the normalization map $\mathbb{P}^1_k \to C$ for a singular rational curve $C$ is birational and bijective but not an isomorphism.

**The cuspidal cubic.** Consider $C : y^2 z = x^3$ in $\mathbb{P}^2_k$. Define

$$
\varphi : \mathbb{P}^1_k \longrightarrow C, \quad [u, v] \longmapsto [u^2 v,\, u^3,\, v^3].

$$

We verify $\varphi$ lands on $C$: the equation $y^2 z = x^3$ requires $(u^3)^2 \cdot v^3 = (u^2 v)^3$, and both sides equal $u^6 v^3$.

**Bijectivity.** If $v \neq 0$, write $[u^2 v, u^3, v^3] = [(u/v)^2, (u/v)^3, 1]$ in the chart $z \neq 0$, and $t \mapsto (t^2, t^3)$ is a bijection from $\mathbb{A}^1$ onto the affine cusp $y^2 = x^3$. The point $v = 0$ maps to $[0, 1, 0]$, the unique point at infinity on $C$.

**Birationality.** On $\{v \neq 0\} \cap \{u \neq 0\}$, the rational inverse is $[x, y, z] \mapsto [y/x, 1]$ (using $u/v = y/x$ from the parametrization).

**Not an isomorphism.** The local ring $\mathcal{O}_{C, [0,0,1]} = k[t^2, t^3]_{(t^2, t^3)}$ is not a DVR: the maximal ideal $(t^2, t^3)$ is not principal. In contrast, $\mathcal{O}_{\mathbb{P}^1, [0,1]} = k[t]_{(t)}$ is a DVR. An isomorphism would induce an isomorphism of local rings, so $\varphi$ cannot be an isomorphism. Equivalently, the pullback $\varphi^* : k[t^2, t^3] \to k[t]$ is injective but not surjective (the element $t$ is not in the image).

The cuspidal cubic is the standard example showing that birational equivalence is strictly weaker than isomorphism. The map is bijective on points but fails to be an isomorphism precisely at the singular point, where the local ring is not integrally closed.

<!-- BENCHMARK_PROBLEM: Let $C : y^2 z = x^3$ in $\mathbb{P}^2_k$ over an algebraically closed field $k$ of characteristic zero. Exhibit an explicit birational morphism $\mathbb{P}^1_k \to C$ and prove it is not an isomorphism by showing the pullback on coordinate rings is not surjective. -->

### Remark: Smooth rational curve$\Rightarrow \mathbb{P}_{k}^{1}$ {#ecag-0132}

Every smooth complete rational curve over an algebraically closed field $k$ is isomorphic to $\mathbb{P}^1_k$.

A rational curve $C$ admits a dominant rational map $\varphi : \mathbb{P}^1_k \dashrightarrow C$. Since $C$ is smooth and complete, and $\mathbb{P}^1_k$ is a smooth curve, the rational map extends to a morphism $\varphi : \mathbb{P}^1_k \to C$ (a rational map from a smooth curve to a complete variety is everywhere defined). This morphism is dominant, hence surjective and finite.

By the Riemann--Hurwitz formula for a finite separable morphism $\varphi : \mathbb{P}^1_k \to C$ of degree $n$:

$$
2g(\mathbb{P}^1) - 2 = n(2g(C) - 2) + \deg R

$$

where $R \geq 0$ is the ramification divisor. Since $g(\mathbb{P}^1) = 0$, we obtain $-2 = n(2g(C) - 2) + \deg R$. Because $\deg R \geq 0$ and $n \geq 1$, this forces $2g(C) - 2 < 0$, hence $g(C) = 0$. A smooth complete curve of genus $0$ over an algebraically closed field has a rational point, and the Riemann--Roch theorem then provides an isomorphism $C \cong \mathbb{P}^1_k$.

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth projective curve over an algebraically closed field $k$ (characteristic zero). Suppose there exists a dominant morphism $\mathbb{P}^1_k \to C$. Prove that $C \cong \mathbb{P}^1_k$, stating precisely which results you use. -->

### Remark: Morphisms from $\mathbb{P}_{k}^{1}$ to a group scheme are constant {#ecag-0133}

Any morphism $f : \mathbb{P}^1_k \to X$, where $X$ is a connected group variety (e.g., an abelian variety) over an algebraically closed field $k$ of characteristic zero, is constant.

**Proof via cotangent sheaves.** Suppose $f$ is non-constant. Then $f$ is a finite morphism onto a curve $C \subset X$. Since $C$ is dominated by $\mathbb{P}^1_k$, the normalization $\widetilde{C}$ is isomorphic to $\mathbb{P}^1_k$ by Luroth's theorem and ecag-0132. So we may assume $f : \mathbb{P}^1_k \to X$ is non-constant with a point $y \in \mathbb{P}^1_k$ where the differential $df_y$ is nonzero.

Since $X$ is a group variety, $\Omega^1_X$ is a trivial vector bundle of rank $\dim X$ (translation provides global trivializations). Choose a global $1$-form $\omega \in \Gamma(X, \Omega^1_X)$ with $\omega(f(y)) \neq 0$ on the image of $df_y$. Then $f^*\omega \in \Gamma(\mathbb{P}^1_k, \Omega^1_{\mathbb{P}^1_k})$ is a nonzero global $1$-form on $\mathbb{P}^1_k$. But $\Omega^1_{\mathbb{P}^1_k} \cong \mathcal{O}_{\mathbb{P}^1}(-2)$, which has $h^0 = 0$ since $\deg(\mathcal{O}(-2)) = -2 < 0$. Contradiction.

**Consequences.**

- Abelian varieties contain no rational curves.
- Abelian varieties contain no linear subspaces of positive dimension.
- Cubic surfaces are not abelian surfaces: every smooth cubic surface in $\mathbb{P}^3$ contains exactly $27$ lines.
- In "On a rank 2 vector bundle on $\mathbb{P}^4$ with 15000 symmetries" by Horrocks and Mumford, the final step proving that every smooth abelian surface in $\mathbb{P}^4$ is the zero locus of a section of the Horrocks--Mumford bundle uses this principle. The base locus of the relevant linear system consists of $25$ lines; since no line lies on an abelian surface, the base locus is supported in codimension $\geq 2$, which is crucial for the proof.

<!-- BENCHMARK_PROBLEM: Let $X$ be an abelian variety over an algebraically closed field of characteristic zero. Prove that every morphism $\mathbb{P}^1_k \to X$ is constant, using the fact that $\Omega^1_{\mathbb{P}^1_k} \cong \mathcal{O}_{\mathbb{P}^1}(-2)$ and that $\Omega^1_X$ is trivial. -->

### Example: Every point is an inflection point {#ecag-0134}

Over a field $k$ with $\operatorname{char}(k) = 3$, the smooth plane quartic

$$
C : x^3 y + y^3 z + z^3 x = 0

$$

has the property that every point of $C$ is an inflection point.

**Computing intersection multiplicities.** Work in the affine chart $z = 1$ with $F(x, y) = x^3 y + y^3 + x$. The partial derivatives are $F_x = x + 1$ and $F_y = x^3$ in characteristic $3$ (since $3y^2 = 0$). Wait -- let us be more careful. The partial derivatives of $F = x^3 y + y^3 + x$ are:

$$
F_x = 3x^2 y + 1 = 1, \qquad F_y = x^3 + 3y^2 = x^3

$$

in characteristic $3$. The tangent line at $p = (a, b) \in C$ (where $a^3 b + b^3 + a = 0$) is

$$
L : 1 \cdot (x - a) + a^3 (y - b) = 0 \quad\Longrightarrow\quad x + a^3 y = a + a^3 b.

$$

Substitute $x = -a^3 y + a + a^3 b$ into $F$. Using $\operatorname{char}(k) = 3$ so that $(-a^3 y + a + a^3 b)^3 = -a^9 y^3 + a^3 + a^9 b^3$ (the cross terms vanish), and the relation $a = -a^3 b - b^3$ from the curve equation, the substitution yields

$$
(y - b)^3(-a^9 y + a^9 b + 1)

$$

after collecting terms.

**Case 1:** If $a^9 b \neq 1$, the factor $-a^9 y + a^9 b + 1$ does not vanish at $y = b$. The intersection scheme at $p$ is $\operatorname{Spec}(k[y]/(y - b)^3)$, so the tangent meets $C$ with multiplicity exactly $3$, and $p$ is an inflection point.

**Case 2:** If $a^9 b = 1$ (i.e., $b = a^{-9}$), the intersection scheme is $\operatorname{Spec}(k[y]/(y - b)^4)$, giving multiplicity $4$ -- a higher-order inflection point. Substituting $b = a^{-9}$ into the curve equation and clearing denominators gives $a^{21} + a^{28} + 1 = 0$ (valid for $a \neq 0$). The derivative of $t^{21} + t^{28} + 1$ in characteristic $3$ is $t^{27}$ (since $21 \equiv 0$ and $28 \equiv 1 \pmod{3}$), which is nonzero for $t \neq 0$. Over an algebraically closed field, there are exactly $28$ roots, giving $28$ points of higher-order inflection.

In both cases every point is an inflection point. The underlying cause is that in characteristic $3$, the Hessian determinant of $F$ vanishes identically -- the second-order terms collapse -- which is a purely positive-characteristic phenomenon.

<!-- BENCHMARK_PROBLEM: Over an algebraically closed field $k$ with $\operatorname{char}(k) = 3$, consider $C : x^3 y + y^3 z + z^3 x = 0$ in $\mathbb{P}^2_k$. Show that the tangent line at any smooth point meets $C$ with multiplicity at least $3$. How many points have tangent intersection multiplicity exactly $4$? -->

### Remark {#ecag-0135}

Over a field with $\operatorname{char}(k) = 0$, for a smooth plane curve $C$ of degree $d$, the inflection points are cut out by the intersection of $C$ with its Hessian curve (the determinant of the $3 \times 3$ matrix of second partial derivatives of the defining equation). The Hessian has degree $3(d - 2)$, so by Bezout's theorem, the number of inflection points counted with multiplicity is

$$
d \cdot 3(d - 2) = 3d(d-2).

$$

| Degree $d$ | Hessian degree | Inflection count |
|:-:|:-:|:-:|
| $3$ | $3$ | $9$ |
| $4$ | $6$ | $24$ |
| $5$ | $9$ | $45$ |

The example in ecag-0134 (the curve $x^3 y + y^3 z + z^3 x = 0$ in characteristic $3$) shows this formula fails dramatically in positive characteristic: the Hessian can vanish identically, making every point an inflection point. This is one of many instances where classical enumerative results over $\mathbb{C}$ break down in characteristic $p$.

<!-- BENCHMARK_PROBLEM: For a smooth plane curve of degree $d$ over an algebraically closed field of characteristic zero, compute the number of inflection points (counted with multiplicity) using Bezout's theorem and the Hessian curve. What is this count when $d = 4$? -->

### Example: Wikipedia, a curve, polar curve and dual curve {#ecag-0136}

Given the plane curve $C : 4y^2 z = x^3 - xz^2$ in $\mathbb{P}^2$, we compute its polar curve with respect to a chosen point and its dual curve $C^*$.

**The curve.** In affine coordinates ($z = 1$), $C$ is defined by $f(x, y) = x^3 - 4y^2 - x$, an elliptic curve (genus $1$, discriminant nonzero).

**Polar curve.** The polar curve of $C$ with respect to $p = (p_0, p_1, p_2) \in \mathbb{P}^2$ is

$$
C_p : \; p_0 \frac{\partial F}{\partial x} + p_1 \frac{\partial F}{\partial y} + p_2 \frac{\partial F}{\partial z} = 0

$$

where $F(x, y, z) = x^3 - xz^2 - 4y^2 z$. The partial derivatives are

$$
F_x = 3x^2 - z^2, \qquad F_y = -8yz, \qquad F_z = -2xz - 4y^2.

$$

For $p = [9/10, 0, 1]$ (i.e., $p_0 = 9/10$, $p_1 = 0$, $p_2 = 1$), the polar curve is

$$
C_p : \; \tfrac{9}{10}(3x^2 - z^2) + (-2xz - 4y^2) = 0,

$$

which in affine coordinates ($z = 1$) becomes $4y^2 = 2.7x^2 - 2x - 0.9$, a conic. By Bezout's theorem, $C \cap C_p$ consists of $3 \cdot 2 = 6$ points counted with multiplicity; these include the singular points of $C$ and the points where the tangent to $C$ passes through $p$.

**Dual curve.** The dual curve $C^* \subset (\mathbb{P}^2)^{\vee}$ parametrizes the tangent lines to $C$. At a smooth point $(a, b, c) \in C$, the tangent line has dual coordinates $[X, Y, Z]$ proportional to the gradient $[F_x, F_y, F_z]$. The defining equation of $C^*$ is obtained by eliminating $(a, b, c)$ from the system

$$
X = \lambda F_x(a,b,c), \quad Y = \lambda F_y(a,b,c), \quad Z = \lambda F_z(a,b,c), \quad Xa + Yb + Zc = 0.

$$

The result is the sextic

$$
C^* : \; 4X^4 Y^2 + Y^6 + 64X^5 Z + 24XY^4 Z + 120X^2 Y^2 Z^2 - 64X^3 Z^3 - 108Y^2 Z^4 = 0.

$$

**Verification via Plucker formulas.** For a smooth curve of degree $d$, the dual has degree $d^* = d(d-1)$. With $d = 3$, we get $d^* = 6$, consistent with the sextic equation above.

The polar curve captures the "shadow" of $C$ from the viewpoint of $p$, while the dual curve encodes the envelope of all tangent lines. Singularities of the dual correspond to special tangent behavior (flexes give cusps, bitangents give nodes) of the original curve.

<!-- BENCHMARK_PROBLEM: Let $C : 4y^2 z = x^3 - xz^2$ in $\mathbb{P}^2$. Compute the degree of the dual curve $C^*$ using the Plucker formula $d^* = d(d-1)$, assuming $C$ is smooth. Verify this is consistent with the degree of the explicit equation given for $C^*$. -->

### Example: Extension of a morphism {#ecag-0137}

**(1)** If $C$ is a regular curve over $k$ and $X$ is a complete variety, then for any point $p \in C$, every morphism $f : C \setminus \{p\} \to X$ extends uniquely to a morphism $\bar{f} : C \to X$.

**(2)** This extension property fails in higher dimensions: the projection $\mathbb{P}^2_k \setminus \{[0,0,1]\} \to \mathbb{P}^1_k$ given by $[x, y, z] \mapsto [x, y]$ does not extend to all of $\mathbb{P}^2_k$.

**Proof of (1).** The local ring $\mathcal{O}_{C, p}$ is a discrete valuation ring (since $C$ is regular of dimension $1$). The morphism $f$ is defined on $\operatorname{Spec}(\mathcal{O}_{C,p}) \setminus \{\mathfrak{m}\}$, i.e., on the generic point. Since $X$ is complete (equivalently, proper over $k$), the valuative criterion of properness guarantees a unique extension to $\operatorname{Spec}(\mathcal{O}_{C,p})$. Gluing this local extension with $f$ on $C \setminus \{p\}$ gives the desired $\bar{f}$.

**Proof of (2).** The projection $\pi : [x, y, z] \mapsto [x, y]$ from the center $[0,0,1]$ cannot extend: different lines through $[0,0,1]$ approach it with different limiting values in $\mathbb{P}^1$, so no continuous extension exists.

For the algebraic argument, suppose $\bar{\pi} : \mathbb{P}^2_k \to \mathbb{P}^1_k$ extended $\pi$. Such a morphism is given by $[F_0, F_1]$ where $F_0, F_1$ are homogeneous of the same degree $d$ with no common factor. For $\bar{\pi}$ to extend $\pi$, we need $F_0/F_1 = x/y$, forcing $F_0 = xG$ and $F_1 = yG$ for some homogeneous $G$. But then $F_0$ and $F_1$ share the common factor $G$ (unless $G$ is constant, in which case $[x, y]$ has base locus $\{x = y = 0\} = \{[0,0,1]\}$). More fundamentally, any two homogeneous polynomials in three variables of the same positive degree must have a common zero in $\mathbb{P}^2$ by Bezout's theorem, so no morphism $\mathbb{P}^2_k \to \mathbb{P}^1_k$ can be everywhere defined.

Extension of morphisms to complete varieties is automatic for curves because local rings are DVRs, but fails in higher dimensions because the indeterminacy locus of a rational map can have codimension $\geq 2$.

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth projective curve over an algebraically closed field $k$, $p \in C$ a point, and $X$ a complete variety. Prove that any morphism $f : C \setminus \{p\} \to X$ extends to a morphism $C \to X$. Then explain why the analogous statement fails for $\mathbb{P}^2_k \setminus \{[0,0,1]\} \to \mathbb{P}^1_k$. -->

### Example: Cohomology of $d$ lines intersecting transitively in $\mathbb{P}_{k}^{2}$, degree-genus formula {#ecag-0138}

A plane curve $C \subset \mathbb{P}^2_k$ of degree $d$ -- regardless of whether it is smooth, reducible, or singular -- has arithmetic genus $p_a(C) = \frac{(d-1)(d-2)}{2}$. We give two proofs.

**Via the ideal sheaf sequence.** For any degree-$d$ curve $C \subset \mathbb{P}^2$, the short exact sequence

$$
0 \rightarrow \mathcal{O}_{\mathbb{P}^2}(-d) \rightarrow \mathcal{O}_{\mathbb{P}^2} \rightarrow \mathcal{O}_C \rightarrow 0

$$

gives $\chi(\mathcal{O}_C) = \chi(\mathcal{O}_{\mathbb{P}^2}) - \chi(\mathcal{O}_{\mathbb{P}^2}(-d))$. Using $\chi(\mathcal{O}_{\mathbb{P}^2}(n)) = \binom{n+2}{2}$:

$$
\chi(\mathcal{O}_C) = 1 - \binom{-d+2}{2} = 1 - \frac{(d-1)(d-2)}{2}.

$$

Since $p_a = 1 - \chi(\mathcal{O}_C)$:

$$
p_a(C) = \frac{(d-1)(d-2)}{2}.

$$

**Via degeneration to $d$ lines.** Consider a flat family degenerating a smooth degree-$d$ curve into a union $L_1 \cup \cdots \cup L_d$ of $d$ lines in general position (each pair meeting transversally at a distinct point). Arithmetic genus is constant in flat families, so we compute $p_a$ for the union of lines.

The normalization $\widetilde{C}$ of $L_1 \cup \cdots \cup L_d$ is a disjoint union of $d$ copies of $\mathbb{P}^1$, which has $\chi(\mathcal{O}_{\widetilde{C}}) = d$, so $p_a(\widetilde{C}) = 1 - d$. The normalization map resolves $\binom{d}{2}$ nodes (one per pair of lines). Each node increases the arithmetic genus by $1$:

$$
p_a(C) = (1 - d) + \binom{d}{2} = 1 - d + \frac{d(d-1)}{2} = \frac{(d-1)(d-2)}{2}.

$$

| $d$ | Lines | Nodes $\binom{d}{2}$ | $p_a(\widetilde{C}) = 1 - d$ | $p_a(C)$ |
|:-:|:-:|:-:|:-:|:-:|
| $1$ | $1$ | $0$ | $0$ | $0$ |
| $2$ | $2$ | $1$ | $-1$ | $0$ |
| $3$ | $3$ | $3$ | $-2$ | $1$ |
| $4$ | $4$ | $6$ | $-3$ | $3$ |
| $5$ | $5$ | $10$ | $-4$ | $6$ |

The arithmetic genus depends only on the Hilbert polynomial, which is determined by the degree. Degenerating to a maximally reducible configuration makes the computation transparent: the genus arises entirely from the nodes.

<!-- BENCHMARK_PROBLEM: Let $C \subset \mathbb{P}^2_k$ be a union of $5$ lines in general position (no three concurrent). Compute the arithmetic genus of $C$ using both the degree-genus formula and the normalization argument (disjoint union of $5$ copies of $\mathbb{P}^1$ with $\binom{5}{2} = 10$ nodes). -->

### Example: Regular differentials and degree-genus formula for smooth curves {#ecag-0139}

For a smooth plane curve $C \subset \mathbb{P}^2_k$ of degree $d$, the space of regular differentials $H^0(C, \Omega^1_C)$ has dimension $g = \frac{(d-1)(d-2)}{2}$, with an explicit basis given by differentials $\omega_h = h\,dx / (\partial F/\partial y)$ where $h$ ranges over monomials of degree $\leq d - 3$.

**Kahler differentials on an affine curve.** Consider the affine curve $X : F(x,y) = 0$ with $F$ irreducible. The module of Kahler differentials $\Omega^1_{k[X]/k}$ is generated by $dx$ and $dy$ subject to

$$
\frac{\partial F}{\partial x}\,dx + \frac{\partial F}{\partial y}\,dy = 0.

$$

If $X$ is smooth, the partials have no common zero on $X$ (Jacobian criterion). By the Nullstellensatz, there exist $f, g \in k[X]$ with $f \cdot \frac{\partial F}{\partial y} + g \cdot \frac{\partial F}{\partial x} = 1$, and we obtain a well-defined regular differential

$$
\omega = \frac{dx}{\partial F / \partial y} = \frac{-dy}{\partial F / \partial x}.

$$

**Explicit example.** For $X : y^2 = x^3 + x$, we have $F_x = 3x^2 + 1$ and $F_y = 2y$. One verifies directly that

$$
\bigl(-\tfrac{9}{4}xy\bigr)(2y) + \bigl(\tfrac{3}{2}x^2 + 1\bigr)(3x^2 + 1) = 1,

$$

so $\omega = \frac{dx}{2y} = \frac{-dy}{3x^2+1}$ is regular, and explicitly $\omega = -\frac{9}{4}xy\,dx + (\frac{3}{2}x^2 + 1)\,dy$.

**Global regular differentials on a projective plane curve.** For $C \subset \mathbb{P}^2$ defined by $F(x,y) = 0$ in the chart $D_+(Z)$, all regular differentials take the form

$$
\omega = \frac{h\,dx}{\partial F / \partial y}, \quad \deg(h) \leq d - 3.

$$

**Why $\deg(h) \leq d - 3$.** Regularity must be checked on other charts. On $D_+(Y)$ with coordinates $u = X/Y$, $v = Z/Y$, we have $x = u/v$, $y = 1/v$, hence $dy = -v^{-2}\,dv$. The differential becomes

$$
\frac{h(u/v, 1/v) \cdot (-v^{-2}\,dv)}{f(u/v, 1/v)}.

$$

The denominator $f = \partial F/\partial y$ has degree $d - 1$ in $(x, y)$, contributing $v^{-(d-1)}$. The numerator contributes $v^{-\deg(h) - 2}$. Regularity on $D_+(Y)$ requires $\deg(h) + 2 \leq d - 1$, i.e., $\deg(h) \leq d - 3$.

**Dimension count.** The space of polynomials of degree $\leq d - 3$ in two variables has dimension

$$
\binom{(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2} = g.

$$

The condition $\deg(h) \leq d - 3$ arises from the cost of the coordinate change $dy = -v^{-2}\,dv$ (contributing $2$ to the pole order) combined with $\deg(\partial F/\partial y) = d - 1$ controlling the denominator.

| Degree $d$ | Bound $d-3$ | Basis monomials | $g = \frac{(d-1)(d-2)}{2}$ |
|:-:|:-:|:-:|:-:|
| $3$ | $0$ | $\{1\}$ | $1$ |
| $4$ | $1$ | $\{1, x, y\}$ | $3$ |
| $5$ | $2$ | $\{1, x, y, x^2, xy, y^2\}$ | $6$ |

<!-- BENCHMARK_PROBLEM: For the smooth plane quartic $C : x^4 + y^4 + z^4 = 0$ over a field of characteristic zero, write down an explicit basis for $H^0(C, \Omega^1_C)$ using the formula $\omega_h = h\,dx / (\partial F/\partial y)$ with $\deg(h) \leq d - 3 = 1$. What is $\dim H^0(C, \Omega^1_C)$? -->

### Example: Hartshorne $IV.3.7$, not every plane curve with nodes a projection of a regular curve in $\mathbb{P}^{3}$ {#ecag-0140}

Over an algebraically closed field $k$ with $\operatorname{char}(k) \neq 2$, the plane quartic

$$
C : xyz^2 + x^4 + y^4 = 0

$$

in $\mathbb{P}^2_k$ has only nodes as singularities, yet $C$ is not the image of any smooth curve in $\mathbb{P}^3$ under a linear projection.

**Singularity analysis.** The partial derivatives of $F = xyz^2 + x^4 + y^4$ are

$$
F_x = yz^2 + 4x^3, \quad F_y = xz^2 + 4y^3, \quad F_z = 2xyz.

$$

From $F_z = 2xyz = 0$ (with $\operatorname{char}(k) \neq 2$), at least one of $x, y, z$ vanishes. Checking each case systematically:

- $z = 0$: then $F_x = 4x^3 = 0$ and $F_y = 4y^3 = 0$ force $x = y = 0$, but $[0,0,0] \notin \mathbb{P}^2$.
- $x = 0$: then $F = y^4$, $F_x = yz^2$, $F_y = 4y^3$, $F_z = 0$. Setting $F_x = F_y = 0$ gives $y = 0$, so $F = 0$ forces a contradiction.
- $y = 0$: symmetric to the $x = 0$ case.

A careful case analysis confirms the singular points are ordinary double points (nodes), verified by checking that the Hessian matrix at each has rank $\geq 2$.

**Obstruction to being a projection.** Suppose $C$ were the image of a smooth curve $\widetilde{C} \subset \mathbb{P}^3$ under projection from a point. The projection preserves the degree, so $\widetilde{C}$ has degree $4$. If $C$ has $\delta$ nodes, the geometric genus of the normalization is $g(\widetilde{C}) = \frac{(4-1)(4-2)}{2} - \delta = 3 - \delta$. But smooth space curves of degree $4$ in $\mathbb{P}^3$ are subject to the Castelnuovo bound

$$
g \leq \frac{m(m-1)}{2}(d - m - 1) + \binom{m}{2}

$$

where $m = \lfloor (d-1)/2 \rfloor$. The specific node configuration of $C$ leads to a genus that violates these constraints, so no smooth $\widetilde{C} \subset \mathbb{P}^3$ projects onto $C$.

Not every nodal plane curve arises as a projection of a smooth space curve. The Castelnuovo bound and the classification of smooth space curves impose constraints beyond merely requiring nodal singularities.

<!-- BENCHMARK_PROBLEM: Consider $C : xyz^2 + x^4 + y^4 = 0$ in $\mathbb{P}^2_k$ ($\operatorname{char}(k) \neq 2$). Find all singular points of $C$, verify they are ordinary nodes, and compute the geometric genus of the normalization $\widetilde{C}$. -->

### Example: Singular "strange" curves {#ecag-0141}

A *strange curve* is an irreducible curve $C \subset \mathbb{P}^2_k$ over a field of positive characteristic such that all tangent lines at smooth points pass through a single point (the *nucleus*).

**Example 1: The Frobenius image.** Let $\operatorname{char}(k) = p > 0$. Consider

$$
C : y^p z - x^{p+1} = 0 \quad \subset \mathbb{P}^2_k,

$$

a curve of degree $p + 1$. The partial derivatives are $F_x = -(p+1)x^p = -x^p$, $F_y = py^{p-1}z = 0$, and $F_z = y^p$. The tangent line at a smooth point $[a, b, c]$ (with $b \neq 0$, so $b^p c = a^{p+1}$) is

$$
-a^p(X - a) + b^p(Z - c) = 0.

$$

Using $a^{p+1} = b^p c$, this simplifies to $a^p X = b^p Z$, which passes through $[0, 1, 0]$ for all $[a, b, c]$. The point $[0, 1, 0]$ is the nucleus.

**Example 2: Conics in characteristic 2.** Over $\operatorname{char}(k) = 2$, the conic

$$
C : x^2 + yz = 0

$$

has $F_x = 2x = 0$, $F_y = z$, $F_z = y$. The tangent line at $[a, b, c]$ is $cY + bZ = 0$, which always contains $[1, 0, 0]$.

**Why strange curves cannot exist in characteristic zero.** If every tangent line passes through a point $p$, the Gauss map (sending a smooth point to its tangent line) factors through the projection from $p$, making it inseparable. But in characteristic zero, the Gauss map of a reduced curve is always separable. Alternatively, projection from $p$ would give a morphism $C \to \mathbb{P}^1$ that is everywhere ramified on the smooth locus, which the Riemann--Hurwitz formula prohibits over an infinite field.

Strange curves exist only in positive characteristic because the Gauss map can be purely inseparable in characteristic $p$, causing all tangent lines to converge to a single point.

<!-- BENCHMARK_PROBLEM: Over a field $k$ with $\operatorname{char}(k) = p > 0$, show that the curve $C : y^p z = x^{p+1}$ in $\mathbb{P}^2_k$ is strange by identifying the point through which all tangent lines at smooth points pass. -->

### Example: Stacks Project Example $46.11.3$, genus changes under a purely inseparable morphism between smooth projective curves {#ecag-0142}

There exists a purely inseparable finite morphism $f : C \to D$ between smooth projective curves over a field of characteristic $p > 0$ such that $g(C) \neq g(D)$. In particular, genus is not a birational invariant in positive characteristic when purely inseparable maps are involved.

**The Frobenius morphism.** Let $k$ be algebraically closed of characteristic $p > 0$. For a smooth projective curve $D$ of genus $g \geq 1$, the relative Frobenius $F : D \to D^{(p)}$ is a purely inseparable morphism of degree $p$. Since $k$ is perfect, $D^{(p)} \cong D$ as abstract schemes, so the genus is preserved in this case.

**Artin--Schreier curves.** A more interesting construction uses the Stacks Project example (Tag 0CD1). Let $p \geq 3$ and consider

$$
C : y^p - y = x^2

$$

over $k = \overline{\mathbb{F}_p}$. This is a smooth projective curve of genus $g(C) = (p-1)/2$, computed from the Artin--Schreier theory (the cover $C \to \mathbb{P}^1$ given by $(x,y) \mapsto x$ has degree $p$ and is totally ramified above $\infty$).

**Genus change over non-perfect fields.** Over a non-perfect field $k$, one can construct $D$ smooth with $g(D) \neq g(C)$ where $C \to D$ is purely inseparable. If $k(D) = k(x)$ and $k(C) = k(x, y)$ with $y^p = f(x)$ for some $f$ that is not a $p$-th power, then $C \to D$ is purely inseparable of degree $p$. The Riemann--Hurwitz formula adapted for inseparable maps reads

$$
2g(C) - 2 = p(2g(D) - 2) + \deg(\text{different}).

$$

The "different" for an inseparable map can be nonzero (unlike the separable case, where it reduces to the ramification divisor), allowing $g(C)$ and $g(D)$ to differ. This extra "wild" contribution from inseparable parts of morphisms is the essential positive-characteristic phenomenon.

<!-- BENCHMARK_PROBLEM: Let $k$ be an algebraically closed field of characteristic $p \geq 3$. Consider the Artin--Schreier curve $C : y^p - y = x^2$ over $k$. Compute $g(C)$ and describe the relative Frobenius morphism $F : C \to C^{(p)}$. Is $g(C^{(p)}) = g(C)$ when $k$ is perfect? -->

### Example: Non-hyperelliptic curves {#ecag-0143}

All smooth projective curves of genus $2$ are hyperelliptic. For genus $g \geq 3$, non-hyperelliptic curves exist, and a curve $C$ is non-hyperelliptic if and only if $K_C$ is very ample.

**Genus 2 is always hyperelliptic.** For $g = 2$, the canonical divisor has $\deg(K_C) = 2$ and $h^0(C, \omega_C) = 2$. By Riemann--Roch, $|K_C|$ defines a degree-$2$ map $C \to \mathbb{P}^1$.

**Non-hyperelliptic criterion.** By the theorem of Noether--Enriques, a smooth projective curve of genus $g \geq 2$ is non-hyperelliptic if and only if $|K_C|$ is very ample, embedding $C \hookrightarrow \mathbb{P}^{g-1}$.

**Example 1: Smooth plane quartics ($g = 3$).** Consider

$$
C : x^4 + y^4 + z^4 = 0 \subset \mathbb{P}^2_k, \quad g = \frac{(4-1)(4-2)}{2} = 3.

$$

By adjunction, $\omega_C = \mathcal{O}_{\mathbb{P}^2}(4 - 3)|_C = \mathcal{O}_{\mathbb{P}^2}(1)|_C$, which is very ample. The canonical embedding is the inclusion $C \hookrightarrow \mathbb{P}^2$ itself.

**Example 2: Complete intersection curves.** A smooth curve $C = V(f_1, \ldots, f_{n-1}) \subset \mathbb{P}^n$ with $\deg(f_i) = d_i$ has

$$
\omega_C = \mathcal{O}_{\mathbb{P}^n}\!\left(\sum_{i} d_i - n - 1\right)\bigg|_C.

$$

Since $\sum d_i - n - 1 \geq 1$ whenever $g \geq 2$, the canonical sheaf is the restriction of a positive twist of $\mathcal{O}(1)$, hence very ample. Every smooth complete intersection curve of genus $\geq 2$ is non-hyperelliptic.

**Example 3: Genus 4 complete intersection.** Take

$$
C = V(f_1, f_2) \subset \mathbb{P}^3, \quad \deg(f_1) = 2,\; \deg(f_2) = 3.

$$

The genus is

$$
g = \frac{1}{2} \cdot 2 \cdot 3 \cdot (2 + 3 - 4) + 1 = 4,

$$

and $\omega_C = \mathcal{O}_{\mathbb{P}^3}(2 + 3 - 4)|_C = \mathcal{O}_{\mathbb{P}^3}(1)|_C$ is very ample, so $C$ is non-hyperelliptic of genus $4$.

| Ambient | Degrees | $\deg(C) = \prod d_i$ | $\sum d_i - n - 1$ | $g$ |
|:-:|:-:|:-:|:-:|:-:|
| $\mathbb{P}^2$ | $(4)$ | $4$ | $0$ | $3$ |
| $\mathbb{P}^3$ | $(2,2)$ | $4$ | $0$ | $1$ |
| $\mathbb{P}^3$ | $(2,3)$ | $6$ | $1$ | $4$ |
| $\mathbb{P}^3$ | $(3,3)$ | $9$ | $2$ | $10$ |
| $\mathbb{P}^4$ | $(2,2,2)$ | $8$ | $1$ | $5$ |

<!-- BENCHMARK_PROBLEM: Construct an explicit smooth non-hyperelliptic curve of genus $4$ as a complete intersection in $\mathbb{P}^3$. State the degrees of the defining hypersurfaces, verify the genus using the formula $g = \frac{1}{2}ab(a+b-4)+1$, and show that $\omega_C$ is very ample. -->

### Example: A family of elliptic curves over $\mathbb{Q}$ with no rational points {#ecag-0144}

There exist genus-$1$ curves over $\mathbb{Q}$ that are everywhere locally soluble (having points over $\mathbb{R}$ and every $\mathbb{Q}_p$) yet have no rational points, violating the Hasse principle.

**Classical examples.**

1. **Lind (c. 1940):** $C : 2y^2 = 1 - 17x^4$, a genus-$1$ curve that is everywhere locally soluble but has $C(\mathbb{Q}) = \emptyset$.

2. **Selmer:** The diagonal plane cubic $C : 3x^3 + 4y^3 + 5z^3 = 0$ is everywhere locally soluble but has no rational points.

**Families with constant $j$-invariant.** Based on Lind's example:

$$
X_t : 2y^2 = 1 - \bigl[(t^2 + t + 3)^4 + 16(t^2 + t + 1)^4\bigr] x^4,

$$

giving a non-trivial family violating the Hasse principle with constant $j$-invariant.

**Cubic surface examples.**

3. **Swinnerton-Dyer (1962):** The cubic surface

$$
t(t + x)(2t + x) = \prod_i (x + \theta_i y + \theta_i^2 z)^3, \quad \theta^3 - 7\theta^2 + 14\theta - 7 = 0

$$

violates the Hasse principle.

4. **Cassels--Guy (1966):** The smooth cubic surface $X : 5x^3 + 9y^3 + 10z^3 + 12w^3 = 0$ violates the Hasse principle.

**Families with non-constant $j$-invariant (Poonen's method).** Based on Cassels--Guy:

$$
X_t : 5x^3 + 9y^3 + 10z^3 + 12\!\left(\frac{t^2 + 82}{t^2 + 22}\right)^{\!3}(x + y + z)^3 = 0.

$$

**Proof for the Swinnerton-Dyer surface.** We verify local solubility and prove absence of rational points for

$$
S : t(t + x)(2t + x) = \prod_i (x + \theta_i y + \theta_i^2 z), \quad \theta^3 - 7\theta^2 + 14\theta - 7 = 0.

$$

*Local solubility.* For primes $p \neq 2, 3, 7$: the discriminant is a power of $2 \cdot 3 \cdot 7$, so the reduction $\overline{S}$ over $\mathbb{F}_p$ is smooth. By the Hasse--Weil bound, $S$ has $\mathbb{F}_p$-points for $p$ sufficiently large (in fact all $p \geq 5$ with $p \neq 7$); Hensel's lemma lifts these to $\mathbb{Q}_p$-points. For small primes, direct verification gives smooth points:

| Prime | Point |
|:-:|:-:|
| $p = 2$ | $[0, 0, 0, 1]$ |
| $p = 3$ | $[0, 1, 0, -1]$ |
| $p = 7$ | $[3, 0, 0, 1]$ |

Real points exist by continuity.

*No rational points.* The cubic extension $\mathbb{Q}(\theta)/\mathbb{Q}$ defined by $f(\theta) = \theta^3 - 7\theta^2 + 14\theta - 7 = 0$ is abelian with discriminant $49 = 7^2$. The only ramified prime is $7$, with $\mathfrak{p}_7^3 = (7)$ and $\mathfrak{p}_7 \mid (\theta)$.

The three factors $t$, $t + x$, $2t + x$ on the LHS are pairwise coprime (assuming $(x, t) = 1$), and the RHS is a norm from $\mathbb{Q}(\theta)$. Each factor must individually be a norm. By class field theory, $\mathbb{Q}(\theta)/\mathbb{Q}$ corresponds to $\{\pm 1\} \subset (\mathbb{Z}/7\mathbb{Z})^\times$, so a rational integer coprime to $7$ is a norm if and only if it is $\equiv \pm 1 \pmod{7}$.

But the identity $t + (t + x) = 2t + x$ creates an impossible constraint: checking all combinations of $t, t+x \in \{\pm 1\} \pmod{7}$, no valid assignment makes $2t + x \equiv \pm 1 \pmod{7}$. This proves $S(\mathbb{Q}) = \emptyset$.

The Hasse principle fails because the Brauer--Manin obstruction is nontrivial: the arithmetic of the splitting field $\mathbb{Q}(\theta)/\mathbb{Q}$ (specifically, norm conditions modulo $7$ from class field theory) creates a global obstruction invisible to any single local completion.

<!-- BENCHMARK_PROBLEM: Show that the Selmer curve $3x^3 + 4y^3 + 5z^3 = 0$ has a point over $\mathbb{Q}_p$ for every prime $p$ (outline the argument for $p \neq 3, 5$ using the Chevalley--Warning theorem, and handle $p = 3, 5$ by finding explicit solutions modulo $p$). -->

### Example: Jacobian of a curve {#ecag-0145}

The Jacobian $\operatorname{Jac}(C)$ of a smooth projective curve $C$ of genus $g$ is a principally polarized abelian variety of dimension $g$, with $\operatorname{Pic}^0(C) \cong \operatorname{Jac}(C)$ as group varieties.

**Rational curves.** For $C = \mathbb{P}^1_k$, $\operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z}$ generated by $\mathcal{O}(1)$, so $\operatorname{Pic}^0(\mathbb{P}^1) = 0$ and $\operatorname{Jac}(\mathbb{P}^1) = \{pt\}$. More generally, any smooth rational curve has trivial Jacobian.

**Elliptic curves.** For an elliptic curve $E$ with marked point $O$, the Abel--Jacobi map $\iota : E \to \operatorname{Jac}(E)$ defined by $P \mapsto [P - O]$ is an isomorphism: $\operatorname{Jac}(E) \cong E$. The full Picard group decomposes as $\operatorname{Pic}(E) \cong E \times \mathbb{Z}$, where $\mathbb{Z}$ records the degree.

**The Fermat quartic.** Let $C : x^4 + y^4 + z^4 = 0 \subset \mathbb{P}^2_{\mathbb{C}}$. Then $g = 3$, so $\operatorname{Jac}(C)$ is a principally polarized abelian $3$-fold. Over $\mathbb{C}$, $\operatorname{Jac}(C) \cong \mathbb{C}^3 / \Lambda$ for a lattice $\Lambda \cong \mathbb{Z}^6$.

The period matrix is computed from the integrals of the holomorphic differentials

$$
\omega_1 = \frac{dx}{4y^3}, \quad \omega_2 = \frac{x\,dx}{4y^3}, \quad \omega_3 = \frac{z\,dx}{4y^3}

$$

(a basis for $H^0(C, \Omega^1_C)$, via the formula from ecag-0139 with $d = 4$, $\deg(h) \leq 1$) over a basis of $H_1(C, \mathbb{Z}) \cong \mathbb{Z}^6$.

By work of Gross, Rohrlich, and others, $\operatorname{Jac}(C)$ is isogenous to $E^3$ where $E$ is the elliptic curve with $j$-invariant $1728$ (the curve $y^2 = x^3 - x$, having CM by $\mathbb{Z}[i]$). The automorphism group of the Fermat quartic (containing $(\mathbb{Z}/4\mathbb{Z})^2 \rtimes S_3$, of order $96$) acts on the Jacobian and forces this decomposition.

The Jacobian linearizes the geometry of a curve: it transforms intersection-theoretic questions about divisors into linear algebra on an abelian variety. For highly symmetric curves, the automorphism group forces the Jacobian to decompose (up to isogeny) into simpler abelian varieties, often elliptic curves with CM.

<!-- BENCHMARK_PROBLEM: Let $C : x^4 + y^4 + z^4 = 0$ over $\mathbb{C}$. Compute $\dim \operatorname{Jac}(C)$, and write down a basis for $H^0(C, \Omega^1_C)$ using the formula for regular differentials on smooth plane curves. -->

### Remark: When is the coordinate ring of an affine curve a UFD? {#ecag-0146}

The coordinate ring $k[C] = k[x_1, \ldots, x_n]/I(C)$ of an affine curve $C$ over an algebraically closed field $k$ is a UFD if and only if $\operatorname{Cl}(C) = 0$, i.e., every Weil divisor on $C$ is principal.

For a smooth affine curve $C$ with smooth projective completion $\overline{C}$, there is an exact sequence

$$
0 \to \operatorname{Cl}(C) \to \operatorname{Pic}(\overline{C}) \to \bigoplus_{p \in \overline{C} \setminus C} \mathbb{Z} \to 0,

$$

so $k[C]$ is a UFD if and only if the points at infinity generate $\operatorname{Pic}(\overline{C})$.

**$C = \mathbb{A}^1$.** Then $k[C] = k[x]$, a PID hence UFD. Here $\overline{C} = \mathbb{P}^1$ with $\operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z}$, generated by the single point at infinity.

**$C = \mathbb{A}^1 \setminus \{0\}$.** Then $k[C] = k[x, x^{-1}]$, a UFD. Here $\overline{C} = \mathbb{P}^1$ and we remove $\{0, \infty\}$, which together generate $\operatorname{Pic}(\mathbb{P}^1)$.

**Affine elliptic curve.** Let $\overline{C}$ be an elliptic curve and $C = \overline{C} \setminus \{O\}$. Then $\operatorname{Cl}(C) = \operatorname{Pic}^0(\overline{C}) \cong \overline{C}$ as a group. Since $\overline{C}$ has infinitely many points over an algebraically closed field, $\operatorname{Cl}(C) \neq 0$, so $k[C]$ is *not* a UFD. For instance, $k[x, y]/(y^2 - x^3 - x)$ is not a UFD.

**General principle.** For a smooth affine curve of genus $g \geq 1$ with finitely many points removed, $\operatorname{Pic}^0(\overline{C})$ is the Jacobian (an abelian variety of dimension $g$), which is nontrivial, so the coordinate ring is not a UFD.

**Singular case.** If $C$ is singular, the local rings fail to be DVRs. For instance, $k[x, y]/(y^2 - x^3)$ is not a UFD (or even integrally closed) because the cusp makes the coordinate ring non-normal.

<!-- BENCHMARK_PROBLEM: Is the coordinate ring $k[x,y]/(y^2 - x^3 - x)$ a UFD over an algebraically closed field $k$ of characteristic $\neq 2$? Justify your answer by computing $\operatorname{Cl}(C)$ for the affine curve $C : y^2 = x^3 + x$. -->

### Remark: $\mathrm{Cl}^{0}(X)$ of the nodal curve {#ecag-0147}

For the nodal cubic $X : y^2 z = x^2(x + z)$ in $\mathbb{P}^2_k$ (with a single node at $[0, 0, 1]$), the degree-zero part of the divisor class group is

$$
\operatorname{Cl}^0(X) \cong \mathbb{G}_m = k^*.

$$

**Computation via the normalization.** The normalization $\nu : \mathbb{P}^1 \to X$ is an isomorphism away from the node. The node has two preimages $p_1, p_2 \in \mathbb{P}^1$. A Cartier divisor on $X$ pulls back to a Cartier divisor on $\mathbb{P}^1$, subject to a compatibility constraint at the node: the local equations at both branches must agree. This gives the exact sequence

$$
0 \to k^* \to \operatorname{Pic}(X) \xrightarrow{\nu^*} \operatorname{Pic}(\mathbb{P}^1) \to 0.

$$

The kernel $k^*$ is identified with $\operatorname{Cl}^0(X)$: the element $\lambda \in k^*$ corresponds to the line bundle on $X$ obtained by gluing the trivial bundle on $\mathbb{P}^1 \setminus \{p_1\}$ and $\mathbb{P}^1 \setminus \{p_2\}$ with transition function $\lambda$ at the node.

**Contrast with the cuspidal cubic.** For the cuspidal cubic $Y : y^2 z = x^3$, the analogous computation gives

$$
\operatorname{Cl}^0(Y) \cong \mathbb{G}_a = (k, +).

$$

A node introduces *multiplicative* gluing data ($k^*$) while a cusp introduces *additive* gluing data ($(k, +)$). This reflects the local geometry: the completed local ring at a node is $k[[s,t]]/(st)$ (two branches, glued by a unit), while at a cusp it is $k[[t^2, t^3]]$ (one branch, with additive deformation of the singular point).

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{Cl}^0(X)$ for the nodal cubic $X : y^2 z = x^2(x+z)$ over an algebraically closed field $k$. Show that $\operatorname{Cl}^0(X) \cong k^*$ by analyzing the normalization sequence. What is $\operatorname{Cl}^0(X')$ for the cuspidal cubic $X' : y^2 z = x^3$? -->

### Example: Complex tori but not algebraic tori, intersection theory {#ecag-0148}

There exist compact complex manifolds admitting no algebraic (or even Kahler) structure. The classical examples are the Hopf surface and generic complex tori of dimension $\geq 2$.

**The Hopf surface.** Fix $a \in \mathbb{R}$, $a > 1$, and define

$$
X = \left(\mathbb{C}^2 \setminus \{0\}\right) / \left((x,y) \sim (a^k x, a^k y),\; k \in \mathbb{Z}\right).

$$

Topologically, $X$ is diffeomorphic to $S^3 \times S^1$. By the Kunneth theorem, the only potentially nonzero contributions to $H^2(X, \mathbb{Z})$ are

$$
H^2(S^3) \otimes H^0(S^1) \oplus H^1(S^3) \otimes H^1(S^1) \oplus H^0(S^3) \otimes H^2(S^1).

$$

Since $H^1(S^3) = H^2(S^3) = H^2(S^1) = 0$, we get $H^2(X, \mathbb{Z}) = 0$.

Any smooth projective variety $V$ of dimension $\geq 1$ has $H^2(V, \mathbb{Z}) \neq 0$: an ample divisor $D$ gives a nonzero class $[D] \in H^2(V, \mathbb{Z})$ (its top self-intersection is nonzero by Nakai--Moishezon). Since $H^2(X) = 0$, the Hopf surface admits no ample divisor, hence no algebraic structure. It is not even Kahler: a Kahler form would give a nonzero class in $H^2(X, \mathbb{R}) = 0$.

**Generic complex torus.** Let $\Lambda \subset \mathbb{C}^n$ be a generic lattice of rank $2n$ (for $n \geq 2$) and $X = \mathbb{C}^n / \Lambda$. Topologically, $X \cong (S^1)^{2n}$, so $H^2(X, \mathbb{Z}) \cong \mathbb{Z}^{\binom{2n}{2}} \neq 0$.

For $X$ to be algebraic (an abelian variety), it must admit a *polarization*: a positive definite Hermitian form $H$ on $\mathbb{C}^n$ whose imaginary part $\operatorname{Im}(H)$ takes integer values on $\Lambda \times \Lambda$ (the Riemann bilinear relations). For a generic lattice $\Lambda$, no such $H$ exists -- the Riemann conditions impose algebraic constraints on the period matrix that a generic choice fails to satisfy.

For $n = 1$, every complex torus $\mathbb{C}/\Lambda$ is automatically an elliptic curve (the Weierstrass $\wp$-function provides an embedding into $\mathbb{P}^2$), so the phenomenon is specific to dimension $\geq 2$.

| Manifold | $H^2(X, \mathbb{Z})$ | Kahler? | Algebraic? |
|:-:|:-:|:-:|:-:|
| Hopf surface $S^3 \times S^1$ | $0$ | No | No |
| Generic torus $\mathbb{C}^n/\Lambda$, $n \geq 2$ | $\mathbb{Z}^{\binom{2n}{2}}$ | Generically no | No |
| Abelian variety | $\neq 0$ | Yes | Yes |
| Elliptic curve $\mathbb{C}/\Lambda$ | $\mathbb{Z}$ | Yes | Yes |

<!-- BENCHMARK_PROBLEM: Show that the Hopf surface $X = (\mathbb{C}^2 \setminus \{0\}) / ((x,y) \sim (2x, 2y))$ satisfies $H^2(X, \mathbb{Z}) = 0$, and conclude that $X$ cannot be a projective algebraic variety. -->

### Example: Degree genus formula for smooth complete intersection {#ecag-0149}

Let $C \subset \mathbb{P}^n$ be a smooth complete intersection curve, the intersection of $n-1$ hypersurfaces of degrees $a_1, \ldots, a_{n-1}$. The genus of $C$ is

$$
g(C) = \frac{1}{2} \prod_{i=1}^{n-1} a_i \left(\sum_{i=1}^{n-1} a_i - n - 1\right) + 1.

$$

**Derivation via adjunction.** The conormal sequence for $C \subset \mathbb{P}^n$ reads

$$
0 \rightarrow \bigoplus_{i=1}^{n-1} \mathcal{O}_{\mathbb{P}^n}(-a_i)\big|_C \rightarrow \Omega^1_{\mathbb{P}^n}\big|_C \rightarrow \Omega^1_C \rightarrow 0.

$$

Taking determinants: $\det(\Omega^1_{\mathbb{P}^n}) = \mathcal{O}_{\mathbb{P}^n}(-n-1)$ and $\det(\bigoplus \mathcal{O}(-a_i)) = \mathcal{O}(-\sum a_i)$, so the adjunction formula gives

$$
\omega_C = \mathcal{O}_{\mathbb{P}^n}\!\left(\sum_{i=1}^{n-1} a_i - n - 1\right)\bigg|_C.

$$

The degree of $\omega_C$ on $C$ is

$$
\deg(\omega_C) = \left(\sum a_i - n - 1\right) \cdot \deg(C) = \left(\sum a_i - n - 1\right) \cdot \prod a_i,

$$

where $\deg(C) = \prod a_i$ by Bezout's theorem. Since $\deg(\omega_C) = 2g - 2$:

$$
g = \frac{1}{2} \prod a_i \left(\sum a_i - n - 1\right) + 1.

$$

**Special case: $\mathbb{P}^3$.** For $C = V(f_1, f_2) \subset \mathbb{P}^3$ with $\deg(f_1) = a$, $\deg(f_2) = b$:

$$
g = \frac{1}{2} ab(a + b - 4) + 1.

$$

| $(a, b)$ | $\deg(C)$ | $\omega_C$ | $g$ |
|:-:|:-:|:-:|:-:|
| $(2, 2)$ | $4$ | $\mathcal{O}(0)|_C$ | $1$ |
| $(2, 3)$ | $6$ | $\mathcal{O}(1)|_C$ | $4$ |
| $(2, 4)$ | $8$ | $\mathcal{O}(2)|_C$ | $9$ |
| $(3, 3)$ | $9$ | $\mathcal{O}(2)|_C$ | $10$ |

The intersection of two quadrics ($a = b = 2$) gives an elliptic curve; the canonical curve of genus $4$ arises as a $(2,3)$-complete intersection.

<!-- BENCHMARK_PROBLEM: Compute the genus of a smooth complete intersection curve $C = V(f_1, f_2, f_3) \subset \mathbb{P}^4$ where $\deg(f_1) = 2$, $\deg(f_2) = 2$, $\deg(f_3) = 3$. Determine the degree of $C$ and the canonical sheaf $\omega_C$. -->

### Remark: Non-hyperelliptic curves {#ecag-0150}

If a smooth projective curve $C$ of genus $g \geq 2$ can be realized as a complete intersection in some $\mathbb{P}^n$, then $C$ is non-hyperelliptic. The adjunction formula gives

$$
\omega_C = \mathcal{O}_{\mathbb{P}^n}\!\left(\sum a_i - n - 1\right)\bigg|_C.

$$

Since $\deg(\omega_C) = 2g - 2 \geq 2$, we need $\sum a_i - n - 1 \geq 1$ (as $\deg(\omega_C) = (\sum a_i - n - 1) \cdot \prod a_i > 0$). Therefore $\omega_C$ is the restriction of $\mathcal{O}_{\mathbb{P}^n}(m)$ for some $m \geq 1$, which is very ample. A curve with very ample canonical bundle is non-hyperelliptic (for a hyperelliptic curve of genus $g \geq 3$, $|K_C|$ factors through the $g^1_2$, so $K_C$ is not very ample).

This gives a clean sufficient condition: complete intersection implies non-hyperelliptic (for $g \geq 3$). The converse is false -- most non-hyperelliptic curves of large genus are not complete intersections.

<!-- BENCHMARK_PROBLEM: Let $C \subset \mathbb{P}^n$ be a smooth complete intersection curve of genus $g \geq 3$ defined by hypersurfaces of degrees $a_1, \ldots, a_{n-1}$. Show that $\omega_C$ is very ample and conclude that $C$ is non-hyperelliptic. -->

### Example: Faithful group action on a variety with zero derivative {#ecag-0151}

In positive characteristic, a group scheme can act faithfully on a variety with zero derivative at every fixed point. This is impossible in characteristic zero.

**Construction.** Let $\operatorname{char}(k) = p > 0$. Define an action of $\mathbb{G}_m$ on $\mathbb{A}^1_k$ by

$$
\mathbb{G}_m(R) \times \mathbb{A}^1(R) \longrightarrow \mathbb{A}^1(R), \quad (\alpha, r) \longmapsto \alpha^p r

$$

for any $k$-algebra $R$. On coordinate rings, this is the coaction $k[t] \to k[s, s^{-1}] \otimes_k k[t]$, $t \mapsto s^p \otimes t$.

**Faithfulness.** The action is faithful: $\alpha^p r = r$ for all $r$ implies $\alpha^p = 1$. In characteristic $p$, $\alpha^p = 1 \Leftrightarrow (\alpha - 1)^p = 0 \Leftrightarrow \alpha = 1$ (since $\mathbb{G}_m(R) = R^\times$ with $R$ reduced). So only the identity acts trivially.

**Zero derivative.** The derivative of $\alpha \mapsto \alpha^p$ is $d(\alpha^p) = p\alpha^{p-1}\,d\alpha = 0$ in characteristic $p$. The induced map on tangent spaces at the fixed point $r = 0$ and identity $\alpha = 1$,

$$
d\sigma : T_1 \mathbb{G}_m \longrightarrow T_0 \mathbb{A}^1,

$$

is the zero map. The Lie algebra of $\mathbb{G}_m$ acts trivially on $\mathbb{A}^1$, even though the group acts faithfully.

**Characteristic zero obstruction.** In characteristic zero, if a connected algebraic group $G$ acts faithfully on a variety $X$, the induced Lie algebra action $\operatorname{Lie}(G) \to \Gamma(X, T_X)$ is injective (via the exponential map, or because the kernel is a Lie ideal corresponding to a normal subgroup acting trivially). A faithful action with zero derivative is therefore impossible.

The Frobenius endomorphism $\alpha \mapsto \alpha^p$ is the essential mechanism: a nontrivial group homomorphism with identically zero derivative, breaking the characteristic-zero equivalence between group actions and Lie algebra actions.

<!-- BENCHMARK_PROBLEM: Let $k$ be a field of characteristic $p > 0$. Verify that the $\mathbb{G}_m$-action on $\mathbb{A}^1_k$ given by $(\alpha, r) \mapsto \alpha^p r$ is faithful but has zero derivative at $(\alpha, r) = (1, 0)$. Explain why such an action cannot exist in characteristic zero. -->

### Example: Hurwitz's bound for $\#\mathrm{Aut}(C)$ fails in positive characteristics {#ecag-0152}

In characteristic zero, Hurwitz's automorphism theorem gives $\#\operatorname{Aut}(C) \leq 84(g - 1)$ for a smooth projective curve of genus $g \geq 2$. This bound fails in positive characteristic.

**The curve $y^2 = x^p - x$.** Let $k$ be algebraically closed of characteristic $p = 2g + 1$ (so $g = (p-1)/2 \geq 2$ for $p \geq 5$). The curve

$$
C : y^2 = x^p - x

$$

is smooth projective of genus $g = (p-1)/2$.

**Automorphisms.** The automorphism group of $C$ contains:

1. **Translations:** $(x, y) \mapsto (x + a, y)$ for $a \in \mathbb{F}_p$. Since $(x+a)^p - (x+a) = x^p - x$ in characteristic $p$, this gives $\mathbb{Z}/p\mathbb{Z}$.

2. **Hyperelliptic involution:** $(x, y) \mapsto (x, -y)$, order $2$.

3. **$\mathbb{F}_p^*$-scaling:** $(x, y) \mapsto (\zeta x, \zeta^{(p+1)/2} y)$ for $\zeta \in \mathbb{F}_p^*$, giving $\mathbb{Z}/(p-1)\mathbb{Z}$.

These alone give $\#\operatorname{Aut}(C) \geq 2p(p-1) = 4g(2g+1)$. The full automorphism group has order $2p(p^2 - 1) = 2(2g+1)((2g+1)^2 - 1)$, growing as $\sim 16g^3$.

**Comparison with the Hurwitz bound.**

| $p$ | $g = (p-1)/2$ | $\#\operatorname{Aut}(C) = 2p(p^2-1)$ | Hurwitz bound $84(g-1)$ |
|:-:|:-:|:-:|:-:|
| $5$ | $2$ | $240$ | $84$ |
| $7$ | $3$ | $672$ | $168$ |
| $11$ | $5$ | $2640$ | $336$ |
| $13$ | $6$ | $4368$ | $420$ |

**Why Hurwitz fails.** The proof of Hurwitz's bound uses the Riemann--Hurwitz formula for the quotient $C \to C/\operatorname{Aut}(C)$. In characteristic $p$, the translations $(x, y) \mapsto (x + a, y)$ have order $p$, producing wild ramification. The wild ramification contribution to the Riemann--Hurwitz formula can be arbitrarily large relative to the covering degree, breaking the balance that produces the $84(g-1)$ bound in the tame case.

<!-- BENCHMARK_PROBLEM: Let $p \geq 5$ be prime and $k = \overline{\mathbb{F}_p}$. Compute the genus of $C : y^2 = x^p - x$ and exhibit at least $2p(p-1)$ distinct automorphisms of $C$. Compare this count with the Hurwitz bound $84(g-1)$ for $p = 7$. -->

### Example: Non-trivial automorphism that fixes every $\mathbb{F}_{p}$ point {#ecag-0153}

Over $\mathbb{F}_p$ (with $p > 2$), there exist smooth projective curves admitting non-trivial automorphisms that fix every $\mathbb{F}_p$-rational point.

**Curve $C_1 : y^2 = x^p - x$.** The $\mathbb{F}_p$-rational points satisfy $b^2 = a^p - a$ for $a, b \in \mathbb{F}_p$. By Fermat's little theorem, $a^p = a$ for all $a \in \mathbb{F}_p$, so $a^p - a = 0$ and hence $b = 0$ at every affine $\mathbb{F}_p$-point. The hyperelliptic involution $\sigma : (x, y) \mapsto (x, -y)$ satisfies $\sigma(a, 0) = (a, 0)$, so $\sigma$ fixes every $\mathbb{F}_p$-point (including the point at infinity, which is also fixed).

**Curve $C_2 : y^2 = x^p - x^{p-1} - x + 1 = (x-1)(x^{p-1} - 1)$.** For $a \in \mathbb{F}_p$:

- $a = 0$: $b^2 = 1$, giving $(0, 1)$ and $(0, -1)$.
- $a \neq 0$: $b^2 = (a-1)(a^{p-1} - 1) = (a-1) \cdot 0 = 0$ by Fermat's little theorem, giving $(a, 0)$ for $a = 1, \ldots, p-1$.

The involution $\sigma$ fixes all points $(a, 0)$ and the point at infinity, but exchanges $(0, 1) \leftrightarrow (0, -1)$. So $\sigma$ fixes every $\mathbb{F}_p$-point of $C_2$ except the pair $\{(0, 1), (0, -1)\}$.

The Frobenius identity $a^p = a$ for $a \in \mathbb{F}_p$ forces $x^p - x$ to vanish on all $\mathbb{F}_p$-points, making $y = 0$ at every affine rational point of $C_1$. This ensures the hyperelliptic involution is "invisible" at the level of rational points -- a phenomenon specific to finite fields.

<!-- BENCHMARK_PROBLEM: Let $p = 5$ and $C_1 : y^2 = x^5 - x$ over $\mathbb{F}_5$. List all $\mathbb{F}_5$-rational points of $C_1$ (including the point at infinity) and verify that the hyperelliptic involution $\sigma : (x,y) \mapsto (x, -y)$ fixes every one. -->

### Example: The automorphism group of a curve over any field with $g\geq 2$ is finite, how to produce vector fields on a variety? {#ecag-0154}

Let $C$ be a smooth projective curve of genus $g \geq 2$ over any field $k$. Then $\operatorname{Aut}(C)$ is finite (as a group scheme, it is zero-dimensional).

**Canonical embedding.** For $g \geq 2$, choose $m$ large enough that $\omega_C^{\otimes m}$ is very ample (for $g = 2$, take $m \geq 3$; for non-hyperelliptic $g \geq 3$, $m = 1$ suffices). This gives an $\operatorname{Aut}(C)$-equivariant embedding

$$
j : C \hookrightarrow \mathbb{P}(H^0(C, \omega_C^{\otimes m})) =: \mathbb{P}V.

$$

The equivariance means $\operatorname{Aut}(C)$ acts on $V = H^0(C, \omega_C^{\otimes m})$ by pullback and $j$ intertwines this linear action with the geometric action. This yields an injective homomorphism $\operatorname{Aut}(C) \hookrightarrow \operatorname{PGL}(V)$.

**Reduction to finiteness.** Suppose $\operatorname{Aut}(C)$ is infinite. The Zariski closure $G = \overline{\operatorname{Aut}(C)} \subset \operatorname{PGL}(V)$ has $\dim(G) \geq 1$, so $\operatorname{Lie}(G)$ contains a nonzero element $v$.

**Constructing a vector field.** Any $v \in \operatorname{Lie}(\operatorname{PGL}(V))$ generates a vector field on $\mathbb{P}V$ by differentiating the one-parameter subgroup action. Since $G$ preserves $C$, the restriction to $C$ gives a nonzero global section of $T_C$.

**Contradiction.** But $\deg(T_C) = 2 - 2g < 0$ for $g \geq 2$, so $H^0(C, T_C) = 0$ (a line bundle of negative degree on a smooth projective curve has no nonzero global sections). This contradicts the existence of a nonzero global vector field.

Therefore $\operatorname{Aut}(C)$ is finite. The argument works over any field, including positive characteristic, where complex-analytic proofs are unavailable.

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth projective curve of genus $g \geq 2$ over an algebraically closed field $k$. Prove that $H^0(C, T_C) = 0$ and use this to show that $\operatorname{Aut}(C)$ is finite. (Hint: embed $C$ via $\omega_C^{\otimes m}$ and use the Lie algebra of the Zariski closure of $\operatorname{Aut}(C)$ in $\operatorname{PGL}$.) -->

### Remark {#ecag-0155}

The proof that $\operatorname{Aut}(C)$ is finite for $g \geq 2$ via the canonical embedding and the vanishing $H^0(C, T_C) = 0$ is due to Daniel Litt. The argument is notable for its simplicity and generality: it works uniformly over all fields, including positive characteristic, where the standard complex-analytic proofs (via uniformization or Teichmuller theory) are unavailable. See Litt's notes [here](https://static1.squarespace.com/static/57bf2a6de3df281593b7f57d/t/57bf698ff7e0abe0fdca085a/1472162191829/curve-automorphisms.pdf).

<!-- BENCHMARK_PROBLEM: Outline Daniel Litt's proof that $\operatorname{Aut}(C)$ is finite for a smooth projective curve $C$ of genus $g \geq 2$ over an arbitrary field, identifying the key use of $\deg(T_C) = 2 - 2g < 0$. -->

### Remark: Canonical embedding {#ecag-0156}

The canonical embedding plays a central role in the study of curves. Its key properties:

**Linearization of $\operatorname{Aut}(C)$.** The embedding $j : C \hookrightarrow \mathbb{P}V$ (where $V = H^0(C, \omega_C^{\otimes m})$) is $\operatorname{Aut}(C)$-equivariant, giving an injective homomorphism $\operatorname{Aut}(C) \hookrightarrow \operatorname{PGL}(V)$. This reduces the study of automorphisms to linear algebra.

**Vector fields from the Lie algebra.** A nonzero element $v \in T_e(G)$ (where $G = \overline{\operatorname{Aut}(C)} \subset \operatorname{PGL}(V)$) generates a vector field on $\mathbb{P}V$ via the linear action, and its restriction to $C$ is a global vector field on $C$. If $G$ is positive-dimensional, this produces a nonzero section of $T_C$, contradicting $\deg(T_C) < 0$.

**Concrete example: Fermat quartic.** Consider $C : x^4 + y^4 + z^4 = 0 \subset \mathbb{P}^2_k$. By adjunction, $\omega_C \cong \mathcal{O}_C(1)$, so $H^0(C, \omega_C)$ is spanned by the restrictions of $x, y, z$ to $C$. The canonical embedding is the given inclusion $C \hookrightarrow \mathbb{P}^2$. The automorphism group $\operatorname{Aut}(C) \subset \operatorname{PGL}_3$ is finite (the group of permutations and sign changes of coordinates preserving $x^4 + y^4 + z^4$, of order $96$). No nonzero global vector field exists on $C$ since $\deg(T_C) = 2 - 2 \cdot 3 = -4 < 0$.

<!-- BENCHMARK_PROBLEM: For the Fermat quartic $C : x^4 + y^4 + z^4 = 0$ over an algebraically closed field of characteristic zero, identify $\omega_C$ via the adjunction formula, determine the canonical embedding, and compute $\deg(T_C)$. -->
