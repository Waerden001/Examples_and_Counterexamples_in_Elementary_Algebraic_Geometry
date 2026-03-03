---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/curves.tex
---

## Curves

### Example: Smooth curve of any genus {#ecag-0130}

**Statement:** For every integer $g \geq 0$, there exists a smooth projective curve of genus $g$ over an algebraically closed field $k$.

**Construction/Proof:** We use two families of curves to realize every genus.

*Family 1: Smooth plane curves.* A smooth plane curve $C \subset \mathbb{P}^2_k$ of degree $d$ has genus

$$
g = \frac{(d-1)(d-2)}{2}

$$

by the degree-genus formula. However, this only produces the values $g = 0, 1, 3, 6, 10, \ldots$, which are triangular numbers. Since consecutive triangular numbers differ by increasing amounts, not every genus arises this way.

*Family 2: Smooth curves on $\mathbb{P}^1 \times \mathbb{P}^1$.* A smooth curve $C$ of bidegree $(a, b)$ on $\mathbb{P}^1 \times \mathbb{P}^1$ has genus computed via the adjunction formula. The canonical sheaf of $\mathbb{P}^1 \times \mathbb{P}^1$ is $\mathcal{O}(-2, -2)$, and the normal bundle of $C$ is $\mathcal{O}(a, b)|_C$. By adjunction:

$$
\omega_C = \left(\omega_{\mathbb{P}^1 \times \mathbb{P}^1} \otimes \bigwedge^{\operatorname{top}} N_{C/\mathbb{P}^1 \times \mathbb{P}^1}\right)\bigg|_C = \mathcal{O}_{\mathbb{P}^1 \times \mathbb{P}^1}(a - 2, b - 2)\big|_C

$$

The degree of $\omega_C$ is $(a - 2)b + a(b - 2) = 2ab - 2a - 2b$, and $\operatorname{deg}(\omega_C) = 2g - 2$, so

$$
g = (a - 1)(b - 1)

$$

Setting $b = 2$, we obtain $g = a - 1$ for any $a \geq 1$. By Bertini's theorem (in characteristic zero) or explicit construction, smooth curves of bidegree $(a, 2)$ exist for all $a \geq 1$. Together with $g = 0$ (realized by $\mathbb{P}^1$), this gives every non-negative integer as a genus.

**Key Insight:** The genus formula $g = \frac{(d-1)(d-2)}{2}$ for plane curves is quadratic in $d$, so it misses most genera. Moving to $\mathbb{P}^1 \times \mathbb{P}^1$ gives a bilinear genus formula $(a-1)(b-1)$, which with one variable fixed at $2$ becomes linear and hits every genus.

**Prerequisites:** Adjunction formula, Bertini's theorem, degree-genus formula for plane curves

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth curve of bidegree $(5, 2)$ on $\mathbb{P}^1 \times \mathbb{P}^1$ over an algebraically closed field of characteristic zero. Compute the genus of $C$ and determine $\operatorname{deg}(\omega_C)$ as a divisor on $C$. -->

### Example: Unirational curves are all rational, birational $\neq$ isomorphism {#ecag-0131}

**Statement:** Every unirational curve over an algebraically closed field is rational (Lüroth's theorem for curves). However, a birational morphism between curves need not be an isomorphism: the normalization map $\mathbb{P}^1_k \to C$ for a singular rational curve $C$ is birational and bijective but not an isomorphism.

**Construction/Proof:** Consider the cuspidal cubic curve $C : y^2 z = x^3$ in $\mathbb{P}^2_k$. Define the morphism

$$
\varphi : \mathbb{P}^1_k \longrightarrow C, \quad [u, v] \longmapsto [u^2 v,\, u^3,\, v^3]

$$

*Verification that $\varphi$ is well-defined:* We check $y^2 z = x^3$: the left side gives $(u^3)^2 \cdot v^3 = u^6 v^3$ and the right side gives $(u^2 v)^3 = u^6 v^3$. So the image lies on $C$.

*Bijectivity:* If $v \neq 0$, write $[u^2 v, u^3, v^3] = [(u/v)^2, (u/v)^3, 1]$ in the chart $z \neq 0$, and the map $t \mapsto (t^2, t^3)$ is a bijection from $\mathbb{A}^1$ onto the affine cusp $y^2 = x^3$. The point $v = 0$ maps to $[0, 1, 0]$, the unique point at infinity on $C$.

*Birationality:* On the open set $\{v \neq 0\} \cap \{u \neq 0\}$, the rational inverse is $[x, y, z] \mapsto [y, xz/y] = [y/x, 1]$ (using $u/v = y/x$ from the parametrization). So $\varphi$ is birational.

*Not an isomorphism:* The local ring $\mathcal{O}_{C, [0,0,1]} = k[t^2, t^3]_{(t^2, t^3)}$ is not a DVR (the maximal ideal is not principal), whereas $\mathcal{O}_{\mathbb{P}^1, [0,1]} = k[t]_{(t)}$ is a DVR. Since an isomorphism would induce an isomorphism of local rings, $\varphi$ cannot be an isomorphism. Equivalently, the pullback $\varphi^* : k[x, y]/(y^2 - x^3) = k[t^2, t^3] \to k[t]$ is injective but not surjective (the element $t$ is not in the image).

**Key Insight:** The cuspidal cubic is the standard example showing that birational equivalence is strictly weaker than isomorphism. The map is bijective on points but fails to be an isomorphism precisely at the singular point, where the local ring is not integrally closed.

**Prerequisites:** Lüroth's theorem, birational morphisms, local rings, discrete valuation rings

<!-- BENCHMARK_PROBLEM: Let $C : y^2 z = x^3$ in $\mathbb{P}^2_k$ over an algebraically closed field $k$ of characteristic zero. Exhibit an explicit birational morphism $\mathbb{P}^1_k \to C$ and prove it is not an isomorphism by showing the pullback on coordinate rings is not surjective. -->

### Remark: Smooth rational curve$\Rightarrow \mathbb{P}_{k}^{1}$ {#ecag-0132}

Every smooth complete rational curve over an algebraically closed field $k$ is isomorphic to $\mathbb{P}^1_k$.

To see this, note that a rational curve $C$ admits a dominant rational map $\varphi : \mathbb{P}^1_k \dashrightarrow C$. Since $C$ is smooth and complete, and $\mathbb{P}^1_k$ is a smooth curve, the rational map $\varphi$ extends to a morphism $\varphi : \mathbb{P}^1_k \to C$ (a rational map from a smooth curve to a complete variety is everywhere defined). This morphism is dominant, hence surjective (since $C$ is complete) and finite.

By the Riemann--Hurwitz formula for a finite separable morphism $\varphi : \mathbb{P}^1_k \to C$ of degree $n$:

$$
2g(\mathbb{P}^1) - 2 = n(2g(C) - 2) + \deg R

$$

where $R \geq 0$ is the ramification divisor. Since $g(\mathbb{P}^1) = 0$, we get $-2 = n(2g(C) - 2) + \deg R$. Because $\deg R \geq 0$ and $n \geq 1$, this forces $2g(C) - 2 < 0$, i.e., $g(C) = 0$. A smooth complete curve of genus $0$ over an algebraically closed field has a rational point (e.g., any closed point), and the Riemann--Roch theorem then provides an isomorphism $C \cong \mathbb{P}^1_k$.

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth projective curve over an algebraically closed field $k$ (characteristic zero). Suppose there exists a dominant morphism $\mathbb{P}^1_k \to C$. Prove that $C \cong \mathbb{P}^1_k$, stating precisely which results you use. -->

### Remark: Morphisms from $\mathbb{P}_{k}^{1}$ to a group scheme are constant {#ecag-0133}

Any morphism $f : \mathbb{P}^1_k \to X$, where $X$ is a connected group variety (e.g., an abelian variety) over an algebraically closed field $k$ of characteristic zero, is constant.

*Proof via cotangent sheaves.* Suppose $f$ is non-constant. Then $f$ is a finite morphism onto a curve $C \subset X$ (the image is a closed subvariety of dimension 1). Since $C$ is dominated by $\mathbb{P}^1_k$, by Lüroth's theorem and the remark above (ecag-0132), the normalization $\widetilde{C}$ is isomorphic to $\mathbb{P}^1_k$. So we may reduce to the case of a non-constant morphism $f : \mathbb{P}^1_k \to X$.

Since $f$ is non-constant, there exists a point $y \in \mathbb{P}^1_k$ at which the differential $df_y : T_y \mathbb{P}^1_k \to T_{f(y)} X$ is nonzero. Now, $X$ is a group variety, so $\Omega^1_X$ is a trivial vector bundle of rank $\dim X$ (translation by group elements provides global trivializations). We can choose a global $1$-form $\omega \in \Gamma(X, \Omega^1_X)$ such that $\omega(f(y)) \neq 0$ on the image of $df_y$. Then $f^*\omega \in \Gamma(\mathbb{P}^1_k, \Omega^1_{\mathbb{P}^1_k})$ is a nonzero global $1$-form on $\mathbb{P}^1_k$. But $\Omega^1_{\mathbb{P}^1_k} \cong \mathcal{O}_{\mathbb{P}^1}(-2)$, which has no nonzero global sections since $\deg(\mathcal{O}(-2)) = -2 < 0$. This is a contradiction.

*Consequences and applications:*

- On abelian surfaces (or more generally abelian varieties), there are no rational curves.
- Abelian varieties contain no linear subspaces of positive dimension.
- Cubic surfaces are not abelian surfaces: every smooth cubic surface in $\mathbb{P}^3$ contains exactly $27$ lines.
- This fact has powerful applications. In the paper "On a rank 2 vector bundle on $\mathbb{P}^4$ with 15000 symmetries" by Horrocks and Mumford, the final step proving that every smooth abelian surface in $\mathbb{P}^4$ is the zero locus of a section of the Horrocks--Mumford bundle uses this principle. They compute that the base locus of the complete linear system of global sections of that bundle consists of $25$ lines. Since no line can lie on an abelian surface, the base locus must be supported at finitely many points (codimension $\geq 2$), which is crucial for the proof.

<!-- BENCHMARK_PROBLEM: Let $X$ be an abelian variety over an algebraically closed field of characteristic zero. Prove that every morphism $\mathbb{P}^1_k \to X$ is constant, using the fact that $\Omega^1_{\mathbb{P}^1_k} \cong \mathcal{O}_{\mathbb{P}^1}(-2)$ and that $\Omega^1_X$ is trivial. -->

### Example: Every point is an inflection point {#ecag-0134}

**Statement:** Over a field $k$ with $\operatorname{char}(k) = 3$, the smooth plane quartic curve

$$
C : x^3 y + y^3 z + z^3 x = 0

$$

has the property that every point of $C$ is an inflection point (i.e., the tangent line at every smooth point meets $C$ with multiplicity $\geq 3$).

**Construction/Proof:** We work in the affine chart $z = 1$ with the polynomial $F(x, y) = x^3 y + y^3 + x$. For a point $p = (a, b) \in C$ (so $a^3 b + b^3 + a = 0$), the tangent line at $p$ is

$$
L : x + a^3 y + b = 0 \quad \text{(after computing partial derivatives and simplifying in characteristic 3)}

$$

We substitute $x = -a^3 y - b$ into $F$ and compute the intersection multiplicity. In the local ring at $p$, we need the length of

$$
k[x, y] / (x + a^3 y + b,\; x^3 y + y^3 + x)

$$

Substituting and using $\operatorname{char}(k) = 3$ (so that $(- a^3 y - b)^3 = -a^9 y^3 - b^3$) together with the relation $a^3 b + b^3 + a = 0$:

$$
(-a^3 y - b)^3 y + y^3 + (-a^3 y - b) = (-a^9 y^3 - b^3)y + y^3 - a^3 y - b

$$

$$
= -a^9 y^4 + (1 - b^3)y - a^3 y - b = -a^9 y^4 + (1 - b^3 - a^3)y - b

$$

Using $b^3 + a = -a^3 b$ (the curve equation), further simplification yields

$$
(-a^3 y - b)^3 y + y^3 + (-a^3 y - b) = (y - b)^3(-a^9 y + 1)

$$

*Case 1:* If $-a^9 b + 1 \neq 0$, the intersection scheme at $p$ is

$$
\operatorname{Spec}(k[y] / (y - b)^3)

$$

so the tangent line meets $C$ with multiplicity exactly $3$, and $p$ is an inflection point.

*Case 2:* If $-a^9 b + 1 = 0$ (i.e., $b = a^{-9}$), the intersection scheme at $p$ is

$$
\operatorname{Spec}(k[y] / (y - b)^4)

$$

so the tangent line meets $C$ with multiplicity $4$, and $p$ is a *higher-order* inflection point. Substituting $b = a^{-9}$ into the curve equation $a^3 b + b^3 + a = 0$ gives $a^{-6} + a^{-27} + a = 0$, or equivalently $1 + a^{28} + a^{21} = 0$ after clearing denominators (note: valid since $a \neq 0$ in this case). The derivative of $1 + a^{28} + a^{21}$ is $a^{27}$ (in characteristic 3, $28 \equiv 1$ and $21 \equiv 0$), which is nonzero for $a \neq 0$. Hence this polynomial has exactly $28$ distinct roots if $k$ is algebraically closed, giving exactly $28$ points of higher-order inflection.

In both cases, every point is an inflection point.

**Key Insight:** In characteristic $3$, the Hessian determinant of $F$ vanishes identically (the second-order terms collapse), which forces every point to be an inflection point. This is a purely positive-characteristic phenomenon.

**Prerequisites:** Intersection multiplicity, inflection points, tangent lines, characteristic $p$ arithmetic

<!-- BENCHMARK_PROBLEM: Over an algebraically closed field $k$ with $\operatorname{char}(k) = 3$, consider $C : x^3 y + y^3 z + z^3 x = 0$ in $\mathbb{P}^2_k$. Show that the tangent line at any smooth point meets $C$ with multiplicity at least $3$. How many points have tangent intersection multiplicity exactly $4$? -->

### Remark {#ecag-0135}

Over a field with $\operatorname{char}(k) = 0$, for a smooth plane curve $C$ of degree $d$, the classical theory of inflection points guarantees exactly $3d(d - 2)$ inflection points (counted with multiplicity), since the inflection points are the intersections of $C$ with its Hessian curve, which has degree $3(d - 2)$. By Bézout's theorem, the number is $d \cdot 3(d - 2) = 3d(d - 2)$.

The example in ecag-0134 (the curve $x^3 y + y^3 z + z^3 x = 0$ in characteristic $3$) shows this formula fails dramatically in positive characteristic: the Hessian can vanish identically, making *every* point an inflection point. This is one of many instances where classical enumerative results over $\mathbb{C}$ break down in characteristic $p$.

<!-- BENCHMARK_PROBLEM: For a smooth plane curve of degree $d$ over an algebraically closed field of characteristic zero, compute the number of inflection points (counted with multiplicity) using Bézout's theorem and the Hessian curve. What is this count when $d = 4$? -->

### Example: Wikipedia, a curve, polar curve and dual curve {#ecag-0136}

**Statement:** Given the plane curve $C : 4y^2 z = x^3 - xz^2$ in $\mathbb{P}^2$, we compute its polar curve with respect to a chosen point and its dual curve $C^*$.

**Construction/Proof:**

*The curve.* In affine coordinates ($z = 1$), $C$ is defined by $f(x, y) = x^3 - 4y^2 - x$. This is an elliptic curve (genus $1$).

*Polar curve.* The polar curve of $C$ with respect to a point $p = (p_0, p_1, p_2) \in \mathbb{P}^2$ is defined by

$$
p_0 \frac{\partial F}{\partial x} + p_1 \frac{\partial F}{\partial y} + p_2 \frac{\partial F}{\partial z} = 0

$$

where $F(x, y, z) = x^3 - xz^2 - 4y^2 z$ is the homogenization. For $p = (0.9, 0, 1)$:

$$
C' : 4y^2 = 2.7x^2 - 2xz - 0.9z^2

$$

The polar curve $C'$ is a conic. By Bézout's theorem, $C \cap C'$ consists of $3 \cdot 2 = 6$ points (counted with multiplicity); these include the singular points of $C$ and the points where the tangent to $C$ passes through $p$.

*Dual curve.* The dual curve $C^* \subset (\mathbb{P}^2)^{\vee}$ parametrizes the tangent lines to $C$. It is computed by elimination: at a smooth point $(p, q, r) \in C$, the tangent line has coordinates $[X, Y, Z]$ proportional to the gradient $[\partial F/\partial x, \partial F/\partial y, \partial F/\partial z]$. The defining equation of $C^*$ is obtained by eliminating $(p, q, r, \lambda)$ from:

$$
X = \lambda \frac{\partial F}{\partial x}(p,q,r), \quad Y = \lambda \frac{\partial F}{\partial y}(p,q,r), \quad Z = \lambda \frac{\partial F}{\partial z}(p,q,r), \quad Xp + Yq + Zr = 0

$$

The result is:

$$
C^* : 4X^4 Y^2 + Y^6 + 64X^5 Z + 24XY^4 Z + 120X^2 Y^2 Z^2 - 64X^3 Z^3 - 108Y^2 Z^4 = 0

$$

This is a sextic curve in $(\mathbb{P}^2)^{\vee}$, consistent with the Plücker formula: for a smooth cubic ($d = 3$), the degree of the dual is $d(d-1) = 6$.

**Key Insight:** The polar curve captures the "shadow" of $C$ from the viewpoint of $p$, while the dual curve encodes the envelope of all tangent lines. For a smooth curve of degree $d$, the dual has degree $d(d-1)$ by the Plücker formulas, and singularities of the dual correspond to special tangent behavior (flexes, bitangents) of the original curve.

**Prerequisites:** Polar curves, dual curves, Plücker formulas, elimination theory, Bézout's theorem

<!-- BENCHMARK_PROBLEM: Let $C : 4y^2 z = x^3 - xz^2$ in $\mathbb{P}^2$. Compute the degree of the dual curve $C^*$ using the Plücker formula $d^* = d(d-1)$, assuming $C$ is smooth. Verify this is consistent with the degree of the explicit equation given for $C^*$. -->

### Example: Extension of a morphism {#ecag-0137}

**Statement:** (1) If $C$ is a regular curve over $k$ and $X$ is a complete variety, then for any point $p \in C$, every morphism $f : C \setminus \{p\} \to X$ extends uniquely to a morphism $\bar{f} : C \to X$. (2) This extension property fails in higher dimensions: the projection $\mathbb{P}^2_k \setminus \{[0,0,1]\} \to \mathbb{P}^1_k$ given by $[x, y, z] \mapsto [x, y]$ does not extend to a morphism on all of $\mathbb{P}^2_k$.

**Construction/Proof:**

*Part (1).* This is the valuative criterion applied concretely. The local ring $\mathcal{O}_{C, p}$ is a discrete valuation ring (since $C$ is regular of dimension 1). The morphism $f$ is defined on $\operatorname{Spec}(\mathcal{O}_{C,p}) \setminus \{\mathfrak{m}\}$, i.e., on the generic point. Since $X$ is complete (equivalently, proper over $k$), the valuative criterion of properness guarantees a unique extension to $\operatorname{Spec}(\mathcal{O}_{C,p})$. Gluing this local extension with $f$ on $C \setminus \{p\}$ gives the desired extension $\bar{f} : C \to X$.

*Part (2).* The projection $\pi : \mathbb{P}^2_k \setminus \{[0,0,1]\} \to \mathbb{P}^1_k$ defined by $[x, y, z] \mapsto [x, y]$ cannot extend to all of $\mathbb{P}^2_k$. Geometrically, the point $[0,0,1]$ is the center of the projection, and the fiber $\pi^{-1}([a,b])$ is the line through $[0,0,1]$ and $[a,b,0]$ minus the point $[0,0,1]$; different lines through $[0,0,1]$ approach it with different limiting values in $\mathbb{P}^1$, so no continuous extension exists.

Algebraically, suppose a morphism $\bar{\pi} : \mathbb{P}^2_k \to \mathbb{P}^1_k$ extended $\pi$. Such a morphism is given by $[F_0, F_1]$ where $F_0, F_1$ are homogeneous polynomials of the same degree $d$ in $(x, y, z)$ with no common factor. For $\bar{\pi}$ to extend $\pi$, we need $F_0 / F_1 = x/y$ on the open set where both are defined, forcing $F_0 = x \cdot G$ and $F_1 = y \cdot G$ for some homogeneous $G$. But then $F_0$ and $F_1$ share the common factor $G$ (unless $G$ is constant, but then $[x, y]$ has base locus $\{x = y = 0\} = \{[0,0,1]\}$). More fundamentally, any two homogeneous polynomials $F_0, F_1$ in three variables of the same degree $d \geq 1$ must have a common zero in $\mathbb{P}^2$ by dimension considerations (the zero loci are curves in $\mathbb{P}^2$, which must intersect by Bézout's theorem), so no morphism $\mathbb{P}^2_k \to \mathbb{P}^1_k$ can be defined everywhere.

**Key Insight:** Extension of morphisms to complete varieties is automatic for curves because local rings are DVRs, but fails in higher dimensions because the indeterminacy locus of a rational map can have codimension $\geq 2$, and the "direction of approach" matters.

**Prerequisites:** Valuative criterion of properness, discrete valuation rings, rational maps, Bézout's theorem, base locus

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth projective curve over an algebraically closed field $k$, $p \in C$ a point, and $X$ a complete variety. Prove that any morphism $f : C \setminus \{p\} \to X$ extends to a morphism $C \to X$. Then explain why the analogous statement fails for $\mathbb{P}^2_k \setminus \{[0,0,1]\} \to \mathbb{P}^1_k$. -->

### Example: Cohomology of $d$ lines intersecting transitively in $\mathbb{P}_{k}^{2}$, degree-genus formula {#ecag-0138}

**Statement:** A plane curve $C \subset \mathbb{P}^2_k$ of degree $d$ (possibly reducible or singular) always has arithmetic genus $p_a(C) = \frac{(d-1)(d-2)}{2}$. This can be proved by degenerating to a union of $d$ lines in general position and using the constancy of arithmetic genus in flat families.

**Construction/Proof:** For any degree $d$ curve $C \subset \mathbb{P}^2$, the ideal sheaf sequence reads

$$
0 \rightarrow \mathcal{O}_{\mathbb{P}^2}(-d) \rightarrow \mathcal{O}_{\mathbb{P}^2} \rightarrow \mathcal{O}_C \rightarrow 0

$$

Taking Euler characteristics and using $\chi(\mathcal{O}_{\mathbb{P}^2}(n)) = \binom{n+2}{2}$:

$$
\chi(\mathcal{O}_C) = \chi(\mathcal{O}_{\mathbb{P}^2}) - \chi(\mathcal{O}_{\mathbb{P}^2}(-d)) = 1 - \binom{-d+2}{2} = 1 - \frac{(d-1)(d-2)}{2}

$$

Since $p_a = 1 - \chi(\mathcal{O}_C)$, we obtain

$$
p_a(C) = \frac{(d-1)(d-2)}{2}

$$

This holds regardless of whether $C$ is smooth, reducible, or singular -- it depends only on the degree.

*Alternative proof via degeneration.* Consider a flat family degenerating a smooth degree $d$ curve into a union of $d$ lines $L_1 \cup \cdots \cup L_d$ in general position (each pair meeting transversally at a distinct point). Since arithmetic genus is constant in flat families, we compute $p_a$ for the union of lines.

The normalization $\widetilde{C}$ of $L_1 \cup \cdots \cup L_d$ is a disjoint union of $d$ copies of $\mathbb{P}^1$, which has genus $g(\widetilde{C}) = 1 - d$ (Euler characteristic $\chi = d$, so $p_a = 1 - d$). The normalization map resolves exactly $\binom{d}{2}$ nodes (one for each pair of lines). Each node increases the arithmetic genus by $1$ (a node identifies two points on the normalization), so:

$$
p_a(C) = (1 - d) + \binom{d}{2} = 1 - d + \frac{d(d-1)}{2} = \frac{(d-1)(d-2)}{2}

$$

This gives another proof of the degree-genus formula.

**Key Insight:** The arithmetic genus depends only on the Hilbert polynomial, which is determined by the degree. Degenerating to a maximally reducible configuration (union of lines) makes the computation transparent: the genus arises entirely from the nodes created by pairwise intersections.

**Prerequisites:** Ideal sheaf sequence, Euler characteristic, arithmetic genus, flat families, normalization

<!-- BENCHMARK_PROBLEM: Let $C \subset \mathbb{P}^2_k$ be a union of $5$ lines in general position (no three concurrent). Compute the arithmetic genus of $C$ using both the degree-genus formula and the normalization argument (disjoint union of $5$ copies of $\mathbb{P}^1$ with $\binom{5}{2} = 10$ nodes). -->

### Example: Regular differentials and degree-genus formula for smooth curves {#ecag-0139}

**Statement:** For a smooth plane curve $C \subset \mathbb{P}^2_k$ of degree $d$, the space of regular differentials $H^0(C, \Omega^1_C)$ has dimension $g = \frac{(d-1)(d-2)}{2}$, and an explicit basis consists of differentials $\omega_h = \frac{h \, dx}{\partial F / \partial y}$ where $h$ ranges over monomials of degree $\leq d - 3$.

**Construction/Proof:**

*Step 1: Regular differentials on an affine curve.* Consider the affine curve $X : F(x,y) = 0$ with $F$ irreducible. The module of Kähler differentials $\Omega^1_{k[X]/k}$ is generated by $dx$ and $dy$ subject to the relation

$$
\frac{\partial F}{\partial x} dx + \frac{\partial F}{\partial y} dy = 0

$$

If $X$ is smooth, the partials $\frac{\partial F}{\partial x}$ and $\frac{\partial F}{\partial y}$ have no common zero on $X$ (by the Jacobian criterion). By the Nullstellensatz, there exist $f, g \in k[X]$ with $f \cdot \frac{\partial F}{\partial y} + g \cdot \frac{\partial F}{\partial x} = 1$. This allows us to write

$$
\omega = \frac{dx}{\partial F / \partial y} = \frac{-dy}{\partial F / \partial x}

$$

as a well-defined regular differential on $X$.

*Explicit example.* For $X : y^2 = x^3 + x$, we have $\frac{\partial F}{\partial x} = 3x^2 + 1$ and $\frac{\partial F}{\partial y} = 2y$. One verifies directly that

$$
(-\tfrac{9}{4}xy)(2y) + (\tfrac{3}{2}x^2 + 1)(3x^2 + 1) = 1

$$

so $\omega = \frac{dx}{2y} = \frac{-dy}{3x^2+1}$ is the regular differential, and explicitly $\omega = -\frac{9}{4}xy\,dx + (\frac{3}{2}x^2 + 1)\,dy$.

*Step 2: Global regular differentials on a projective plane curve.* For $C \subset \mathbb{P}^2 = \operatorname{Proj}(k[X,Y,Z])$ defined by $F(x,y) = 0$ in the chart $D_+(Z)$, with $f = \frac{\partial F}{\partial x}$ and $g = \frac{\partial F}{\partial y}$, all regular differentials take the form

$$
\omega = \frac{-h\,dx}{g} = \frac{h\,dy}{f}, \quad \deg(h) \leq d - 3

$$

*Step 3: Why $\deg(h) \leq d - 3$.* We must check regularity on the other charts. On $D_+(Y)$ with coordinates $u = X/Y, v = Z/Y$, we have $x = u/v, y = 1/v$, hence $dy = -v^{-2}\,dv$. The differential becomes

$$
\frac{h(u/v, 1/v) \cdot (-v^{-2}\,dv)}{f(u/v, 1/v)}

$$

For this to be a polynomial expression in $u, v$ (i.e., regular on $D_+(Y)$), we need the numerator's degree in $1/v$ to not exceed that of the denominator. Since $f$ has degree $d - 1$ in $(x, y)$, the denominator contributes a factor of $v^{-(d-1)}$. The numerator contributes $v^{-\deg(h) - 2}$. Regularity requires $\deg(h) + 2 \leq d - 1$, i.e., $\deg(h) \leq d - 3$.

*Step 4: Dimension count.* The space of homogeneous polynomials of degree $\leq d - 3$ in two variables (restricted to $C$, but they are of low enough degree to be linearly independent on a curve of degree $d > d-3$) has dimension

$$
\binom{(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2} = g

$$

**Key Insight:** The condition $\deg(h) \leq d - 3$ arises from demanding regularity at the "points at infinity." The change-of-coordinates cost is exactly $2$ (from $dy = -v^{-2}\,dv$), which combined with $\deg(f) = d - 1$ forces $\deg(h) \leq d - 3$. The dimension count then reproduces the degree-genus formula.

**Prerequisites:** Kähler differentials, Jacobian criterion, Nullstellensatz, regular differentials on projective varieties, Riemann--Roch theorem

<!-- BENCHMARK_PROBLEM: For the smooth plane quartic $C : x^4 + y^4 + z^4 = 0$ over a field of characteristic zero, write down an explicit basis for $H^0(C, \Omega^1_C)$ using the formula $\omega_h = h\,dx / (\partial F/\partial y)$ with $\deg(h) \leq d - 3 = 1$. What is $\dim H^0(C, \Omega^1_C)$? -->

### Example: Hartshorne $IV.3.7$, not every plane curve with nodes a projection of a regular curve in $\mathbb{P}^{3}$ {#ecag-0140}

**Statement:** Over an algebraically closed field $k$ with $\operatorname{char}(k) \neq 2$, the plane quartic curve

$$
C : xyz^2 + x^4 + y^4 = 0

$$

in $\mathbb{P}^2_k$ is a curve whose only singularities are nodes, yet $C$ is not the image of any smooth (regular) curve in $\mathbb{P}^3$ under a linear projection.

**Construction/Proof:**

*Step 1: Singularity analysis.* The partial derivatives of $F = xyz^2 + x^4 + y^4$ are:

$$
F_x = yz^2 + 4x^3, \quad F_y = xz^2 + 4y^3, \quad F_z = 2xyz

$$

Setting all three to zero: from $F_z = 2xyz = 0$ (and $\operatorname{char}(k) \neq 2$), at least one of $x, y, z$ is zero. Checking each case systematically yields the singular points, and the Hessian matrix at each singular point has rank $\geq 2$, confirming they are ordinary nodes (ordinary double points).

*Step 2: Obstruction to being a projection.* Suppose $C$ were the image of a smooth curve $\widetilde{C} \subset \mathbb{P}^3$ under a linear projection $\pi : \mathbb{P}^3 \dashrightarrow \mathbb{P}^2$ (projection from a point). The projection of a smooth curve generically creates only nodes as singularities (which is consistent with $C$). However, for a smooth curve $\widetilde{C} \subset \mathbb{P}^3$ of degree $d$ and genus $g$, the Castelnuovo bound constrains the genus:

$$
g \leq \frac{m(m-1)}{2}(d - m - 1) + \binom{m}{2}

$$

where $m = \lfloor (d-1)/2 \rfloor$ (in certain formulations). Additionally, a projection from a point not on $\widetilde{C}$ preserves the degree, so $\widetilde{C}$ has degree $4$. The number of nodes $\delta$ of $C$ and the genus $g(\widetilde{C})$ are related by $g(\widetilde{C}) = \frac{(d-1)(d-2)}{2} - \delta = 3 - \delta$. The specific node configuration of $C$ leads to a genus that violates constraints imposed on smooth space curves of degree $4$ (the Castelnuovo bound or Halphen's theorem), providing the obstruction.

*Step 3: Conclusion.* The combinatorial and geometric constraints on smooth space curves of degree $4$ are incompatible with the particular singular configuration of $C$, so no smooth $\widetilde{C} \subset \mathbb{P}^3$ projects onto $C$.

**Key Insight:** Not every nodal plane curve arises as a projection of a smooth space curve. The Castelnuovo bound and classification of smooth space curves impose non-trivial constraints beyond just requiring node singularities. This is a genuinely projective phenomenon.

**Prerequisites:** Castelnuovo bound, projections of curves, singularity types (nodes), genus-degree formula, smooth space curves

<!-- BENCHMARK_PROBLEM: Consider $C : xyz^2 + x^4 + y^4 = 0$ in $\mathbb{P}^2_k$ ($\operatorname{char}(k) \neq 2$). Find all singular points of $C$, verify they are ordinary nodes, and compute the geometric genus of the normalization $\widetilde{C}$. -->

### Example: Singular "strange" curves {#ecag-0141}

**Statement:** A *strange curve* is an irreducible curve $C \subset \mathbb{P}^2_k$ over a field $k$ of positive characteristic such that there exists a point $p \in \mathbb{P}^2$ (called the *strange point* or *nucleus*) through which every tangent line at a smooth point of $C$ passes.

**Construction/Proof:**

*Example 1: The Frobenius image.* Let $k$ be a field with $\operatorname{char}(k) = p > 0$. Consider the curve

$$
C : y^p z - x^{p+1} = 0 \quad \subset \mathbb{P}^2_k

$$

This curve has degree $p + 1$. The partial derivatives are $F_x = -(p+1)x^p = -x^p$, $F_y = py^{p-1}z = 0$, and $F_z = y^p$. The tangent line at a smooth point $[a, b, c]$ (with $b \neq 0$) is

$$
-a^p(X - a) + b^p(Z - c) = 0 \quad \Longrightarrow \quad -a^p X + b^p Z = (-a^{p+1} + b^p c) = 0

$$

using $b^p c = a^{p+1}$. So the tangent line is $a^p X = b^p Z$, which passes through the point $[0, 1, 0]$ for all choices of $[a, b, c]$. Thus $[0, 1, 0]$ is the strange point.

*Example 2: Conics in characteristic 2.* Over a field with $\operatorname{char}(k) = 2$, the conic

$$
C : x^2 + yz = 0

$$

has tangent line at $[a, b, c]$ (smooth, with $b^2 c + bc^2 \neq 0$) passing through $[1, 0, 0]$. Indeed, $F_x = 2x = 0$, $F_y = z$, $F_z = y$, so the tangent line is $zY + yZ = 0$, i.e., $cY + bZ = 0$, which always contains $[1, 0, 0]$.

*Why this cannot happen in characteristic zero.* In characteristic zero, if every tangent line passes through a point $p$, then the projection from $p$ gives a morphism $C \to \mathbb{P}^1$ that is everywhere ramified on the smooth locus. By the Riemann--Hurwitz formula, the ramification divisor has degree $\leq 2g - 2 + 2\deg(\pi)$, but being everywhere ramified forces the ramification degree to equal $\deg(\pi) \cdot (\text{number of smooth points})$, which is impossible for an infinite field. Alternatively, the Gauss map (sending a smooth point to its tangent line) is inseparable for strange curves, which can only happen in positive characteristic.

**Key Insight:** Strange curves exist only in positive characteristic because the Gauss map (associating to a smooth point its tangent line) can be purely inseparable in characteristic $p$, causing all tangent lines to pass through a single point. In characteristic zero, the Gauss map is always separable for reduced curves.

**Prerequisites:** Gauss map, inseparable morphisms, characteristic $p$ geometry, tangent lines, Riemann--Hurwitz formula

<!-- BENCHMARK_PROBLEM: Over a field $k$ with $\operatorname{char}(k) = p > 0$, show that the curve $C : y^p z = x^{p+1}$ in $\mathbb{P}^2_k$ is strange by identifying the point through which all tangent lines at smooth points pass. -->

### Example: Stacks Project Example $46.11.3$, genus changes under a purely inseparable morphism between smooth projective curves {#ecag-0142}

**Statement:** There exists a purely inseparable finite morphism $f : C \to D$ between smooth projective curves over a field $k$ of characteristic $p > 0$ such that $g(C) \neq g(D)$. In particular, genus is not a birational invariant in positive characteristic when one considers purely inseparable maps.

**Construction/Proof:**

*Setup.* Let $k$ be an algebraically closed field of characteristic $p > 0$. Consider a smooth projective curve $D$ of genus $g \geq 1$ and the relative Frobenius morphism $F : D \to D^{(p)}$, where $D^{(p)}$ is the base change of $D$ along the absolute Frobenius of $k$. Since $k$ is perfect, $D^{(p)} \cong D$ as abstract schemes (but the map $F$ is not an isomorphism; it is a purely inseparable morphism of degree $p$).

*Concrete example.* Let $p = 2$ and consider the smooth projective curve $D$ over $k = \overline{\mathbb{F}_2}$ defined by

$$
D : y^2 + y = x^3

$$

This is an elliptic curve ($g(D) = 1$). The Frobenius morphism $F : D \to D^{(2)}$ sends $(x, y) \mapsto (x^2, y^2)$. The image curve $D^{(2)}$ is defined by $y^4 + y^2 = x^6$, which (after a change of variables) is again a genus $1$ curve. In this case the genus is preserved because both curves are smooth.

*Example where genus changes.* A more striking example uses the Frobenius on function fields. Let $k$ be algebraically closed of characteristic $p$, and let $C$ be a smooth projective curve with function field $K = k(C)$. Consider the subfield $K^p = k(C)^p \subset K$, which corresponds to a smooth curve $D$ with $k(D) = K^p$. The inclusion $K^p \hookrightarrow K$ gives a purely inseparable morphism $f : C \to D$ of degree $p$.

The Stacks Project example (Tag 0CD1) gives: let $p \geq 3$ and consider the Artin--Schreier curve

$$
C : y^p - y = x^2

$$

over $k = \overline{\mathbb{F}_p}$. This is a smooth projective curve of genus $g(C) = \frac{(p-1)}{2}$. The relative Frobenius $F : C \to C^{(p)}$ is a purely inseparable morphism of degree $p$. While $C^{(p)}$ has the same genus as $C$ (being isomorphic as abstract curves over a perfect field), composing with other morphisms or considering non-perfect base fields produces genuine genus changes.

Over a non-perfect field $k$, one can construct $D$ smooth with $g(D) \neq g(C)$ where $C \to D$ is purely inseparable. Specifically, if $k(D) = k(x)$ and $k(C) = k(x, y)$ with $y^p = f(x)$ for some $f$ that is not a $p$-th power, then $C \to D$ is purely inseparable of degree $p$, and by the Riemann--Hurwitz formula (adapted for inseparable maps):

$$
2g(C) - 2 = p(2g(D) - 2) + \deg(\text{different})

$$

The "different" for an inseparable map can be nonzero (unlike the separable case where it reduces to the ramification divisor), causing $g(C)$ and $g(D)$ to differ.

**Key Insight:** In positive characteristic, the Riemann--Hurwitz formula acquires an extra "wild" contribution from inseparable parts of morphisms. This different term can be nonzero even when the map is everywhere unramified in the naive sense, allowing genus to change under purely inseparable maps.

**Prerequisites:** Frobenius morphism, purely inseparable morphisms, Artin--Schreier curves, Riemann--Hurwitz formula in positive characteristic, function fields

<!-- BENCHMARK_PROBLEM: Let $k$ be an algebraically closed field of characteristic $p \geq 3$. Consider the Artin--Schreier curve $C : y^p - y = x^2$ over $k$. Compute $g(C)$ and describe the relative Frobenius morphism $F : C \to C^{(p)}$. Is $g(C^{(p)}) = g(C)$ when $k$ is perfect? -->

### Example: Non-hyperelliptic curves {#ecag-0143}

**Statement:** All smooth projective curves of genus $2$ are hyperelliptic. For genus $g \geq 3$, non-hyperelliptic curves exist, and they can be constructed as complete intersections. A curve $C$ is non-hyperelliptic if and only if the canonical divisor $K_C$ is very ample.

**Construction/Proof:**

*Why genus $2$ curves are hyperelliptic.* For a smooth projective curve of genus $2$, the canonical divisor has degree $\deg(K_C) = 2g - 2 = 2$ and $\dim H^0(C, \omega_C) = g = 2$. By the Riemann--Roch theorem, $|K_C|$ defines a degree $2$ map $C \to \mathbb{P}^1$, making $C$ hyperelliptic.

*Non-hyperelliptic criterion.* By the theorem of Noether--Enriques, a smooth projective curve $C$ of genus $g \geq 2$ is non-hyperelliptic if and only if the canonical linear system $|K_C|$ is very ample, embedding $C \hookrightarrow \mathbb{P}^{g-1}$.

*Example 1: Smooth plane quartics (genus 3).* Consider

$$
C : x^4 + y^4 + z^4 = 0 \subset \mathbb{P}^2_k, \quad g = \frac{(4-1)(4-2)}{2} = 3

$$

By the adjunction formula:

$$
\omega_C = \mathcal{O}_{\mathbb{P}^2}(4 - 3)\big|_C = \mathcal{O}_{\mathbb{P}^2}(1)\big|_C

$$

Since $\mathcal{O}_{\mathbb{P}^2}(1)$ is very ample on $\mathbb{P}^2$, its restriction to $C$ is very ample, so $K_C$ is very ample and $C$ is non-hyperelliptic. The canonical embedding is just the inclusion $C \hookrightarrow \mathbb{P}^2$.

*Example 2: Complete intersection curves.* Any smooth curve $C$ of genus $g \geq 2$ realized as a complete intersection $C = V(f_1, \ldots, f_{n-1}) \subset \mathbb{P}^n$ (where $\deg(f_i) = d_i$) has canonical sheaf

$$
\omega_C = \mathcal{O}_{\mathbb{P}^n}\left(\sum_{i} d_i - n - 1\right)\bigg|_C

$$

Since $\deg(K_C) = 2g - 2 \geq 2$ and $\sum d_i - n - 1 \geq 1$ (the degree of $K_C$ on the complete intersection equals $(\sum d_i - n - 1) \cdot \prod d_i \geq 2$), we have $\omega_C = \mathcal{O}(m)|_C$ for $m \geq 1$, so $\omega_C$ is very ample. Therefore every smooth complete intersection curve of genus $\geq 2$ is non-hyperelliptic.

*Example 3: Genus 4 non-hyperelliptic curve.* Consider a smooth complete intersection in $\mathbb{P}^3$:

$$
C = V(f_1, f_2) \subset \mathbb{P}^3, \quad \deg(f_1) = 2,\ \deg(f_2) = 3

$$

The genus is

$$
g = \frac{1}{2} \cdot 2 \cdot 3 \cdot (2 + 3 - 4) + 1 = \frac{1}{2} \cdot 6 \cdot 1 + 1 = 4

$$

and $\omega_C = \mathcal{O}_{\mathbb{P}^3}(2 + 3 - 4)|_C = \mathcal{O}_{\mathbb{P}^3}(1)|_C$ is very ample, so $C$ is non-hyperelliptic of genus $4$.

**Key Insight:** The adjunction formula for complete intersections yields $\omega_C = \mathcal{O}(m)|_C$ with $m \geq 1$, which is automatically very ample. This is the simplest source of non-hyperelliptic curves, and it gives explicit examples in every genus $\geq 3$ (by choosing appropriate degrees and ambient dimension).

**Prerequisites:** Adjunction formula, canonical divisor, very ample line bundles, hyperelliptic curves, complete intersections, Riemann--Roch theorem

<!-- BENCHMARK_PROBLEM: Construct an explicit smooth non-hyperelliptic curve of genus $4$ as a complete intersection in $\mathbb{P}^3$. State the degrees of the defining hypersurfaces, verify the genus using the formula $g = \frac{1}{2}ab(a+b-4)+1$, and show that $\omega_C$ is very ample. -->

### Example: A family of elliptic curves over $\mathbb{Q}$ with no rational points {#ecag-0144}

**Statement:** There exist explicit families of genus $1$ curves over $\mathbb{Q}$ that have points over every completion $\mathbb{Q}_v$ (i.e., over $\mathbb{R}$ and over $\mathbb{Q}_p$ for every prime $p$) but have no rational points, thus violating the Hasse principle.

**Construction/Proof:**

*Classical examples.*

1. **Lind (c. 1940):**

$$
C : 2y^2 = 1 - 17x^4, \quad g = 1

$$

This genus $1$ curve is everywhere locally soluble but has no $\mathbb{Q}$-rational points.

2. **Selmer:** The diagonal plane cubic

$$
C : 3x^3 + 4y^3 + 5z^3 = 0

$$

is everywhere locally soluble but has no rational points.

*Families with constant $j$-invariant (based on Lind's example).* The family

$$
X_t : 2y^2 = 1 - \bigl[(t^2 + t + 3)^4 + 16(t^2 + t + 1)^4\bigr] x^4

$$

gives a non-trivial family of genus $1$ curves violating the Hasse principle, but with constant $j$-invariant.

*Cubic surface examples.*

3. **Swinnerton-Dyer (1962):** The cubic surface

$$
t(t + x)(2t + x) = \prod_i (x + \theta_i y + \theta_i^2 z)^3, \quad \theta^3 - 7\theta^2 + 14\theta - 7 = 0

$$

violates the Hasse principle.

4. **Cassels--Guy (1966):** The smooth cubic surface

$$
X : 5x^3 + 9y^3 + 10z^3 + 12w^3 = 0

$$

violates the Hasse principle.

*Families with non-constant $j$-invariant (Poonen's method).* Based on Cassels--Guy:

$$
X_t : 5x^3 + 9y^3 + 10z^3 + 12\left(\frac{t^2 + 82}{t^2 + 22}\right)^3 (x + y + z)^3 = 0

$$

Based on Swinnerton-Dyer (constructed by the author following Poonen's method):

$$
X_t : \left(\frac{t^2 + 54}{t^2 + 1}\right)\left(\frac{t^2 + 54}{t^2 + 1} + 1\right)\left(\frac{t^2 + 54}{t^2 + 1} + 2\right)x^3 = \prod_i (x + \theta_i y + \theta_i^2 z)^3

$$

where $\theta^3 - 7\theta^2 + 14\theta - 7 = 0$.

*Proof that Swinnerton-Dyer's cubic surface violates the Hasse principle.*

We verify local solubility and then prove absence of rational points for

$$
S : t(t + x)(2t + x) = \prod_i (x + \theta_i y + \theta_i^2 z), \quad \theta^3 - 7\theta^2 + 14\theta - 7 = 0

$$

**Local solubility:**

- *Primes $p \neq 2, 3, 7$:* The reduction $\overline{S}$ over $\mathbb{F}_p$ is smooth (the discriminant is a power of $2 \cdot 3 \cdot 7$). By the Hasse--Weil bound $|\#S(\mathbb{F}_p) - p^2 - p - 1| \leq C \sqrt{p}$ for cubic surfaces, $S$ has an $\mathbb{F}_p$-point for $p$ sufficiently large (in fact for all $p \geq 5$ with $p \neq 7$). By Hensel's lemma, smooth $\mathbb{F}_p$-points lift to $\mathbb{Q}_p$-points.

- *Small primes:* Direct verification gives smooth points:
  - $p = 2$: $[0, 0, 0, 1]$
  - $p = 3$: $[0, 1, 0, -1]$
  - $p = 7$: $[3, 0, 0, 1]$

  Hensel's lemma again yields $\mathbb{Q}_p$-points.

- *$p = \infty$ ($\mathbb{R}$):* Real points exist by continuity arguments.

**No rational points:**

Consider the cubic extension $\mathbb{Q} \subset \mathbb{Q}(\theta)$ defined by $f(\theta) = \theta^3 - 7\theta^2 + 14\theta - 7 = 0$. This is an abelian cubic extension with discriminant $49 = 7^2$. The only ramified prime is $7$:

$$
\mathfrak{p}_7^3 = (7), \quad \mathfrak{p}_7 \mid (\theta)

$$

The second relation follows from $f(\theta) = 0$.

1. Both sides of the defining equation cannot be zero. If the RHS is zero, then $x = y = z = 0$, forcing $t = 0$.

2. We may assume the LHS is a nonzero integer with $(x, t) = 1$. If both sides are divisible by $7$, then $\mathfrak{p}_7 \mid x$ implies $7 \mid x$ (since $7$ is totally ramified). But $(t, x) = 1$ prevents the LHS from being divisible by $7$, a contradiction.

3. If neither side is divisible by $7$: Since the RHS is a norm from $\mathbb{Q}(\theta)$, and the three factors $t$, $t + x$, $2t + x$ on the LHS are pairwise coprime, each must individually be a norm from $\mathbb{Q}(\theta)$ to $\mathbb{Q}$. By class field theory, $\mathbb{Q} \subset \mathbb{Q}(\theta)$ corresponds to the subgroup $\{\pm 1\} \subset (\mathbb{Z}/7\mathbb{Z})^\times$. A rational integer $n$ coprime to $7$ is a norm from $\mathbb{Q}(\theta)$ if and only if $n \equiv \pm 1 \pmod{7}$. But the identity $t + (t + x) = 2t + x$ imposes $t + (t+x) \equiv 2t + x \pmod{7}$, and checking all combinations of $t, t+x \in \{\pm 1\} \pmod{7}$, one finds that no valid assignment makes $2t + x \equiv \pm 1 \pmod{7}$. This contradiction proves $S(\mathbb{Q}) = \emptyset$.

**Key Insight:** The Hasse principle fails for these curves because the Brauer--Manin obstruction is nontrivial. The arithmetic of the splitting field $\mathbb{Q}(\theta)/\mathbb{Q}$ (specifically, norm conditions modulo $7$ from class field theory) creates a global obstruction invisible to any single local completion.

**Prerequisites:** Hasse principle, Hensel's lemma, Hasse--Weil bound, class field theory, Brauer--Manin obstruction, norms in number fields

<!-- BENCHMARK_PROBLEM: Show that the Selmer curve $3x^3 + 4y^3 + 5z^3 = 0$ has a point over $\mathbb{Q}_p$ for every prime $p$ (outline the argument for $p \neq 3, 5$ using the Chevalley--Warning theorem, and handle $p = 3, 5$ by finding explicit solutions modulo $p$). -->

### Example: Jacobian of a curve?? {#ecag-0145}

**Statement:** The Jacobian $\operatorname{Jac}(C)$ of a smooth projective curve $C$ of genus $g$ is a principally polarized abelian variety of dimension $g$, and $\operatorname{Pic}^0(C) \cong \operatorname{Jac}(C)$ as group varieties. We list basic examples and discuss the structure of Jacobians.

**Construction/Proof:**

*Example 1: Rational curves.* For $C = \mathbb{P}^n_k$ (or any smooth rational curve), $\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$ generated by $\mathcal{O}(1)$, so $\operatorname{Pic}^0(\mathbb{P}^n) = 0$ and

$$
\operatorname{Jac}(\mathbb{P}^1) = \{pt\}

$$

More generally, any smooth rational curve has trivial Jacobian.

*Example 2: Elliptic curves.* For an elliptic curve $E$ (smooth projective curve of genus $1$ with a marked point $O$), the Abel--Jacobi map $\iota : E \to \operatorname{Jac}(E)$ defined by $P \mapsto [P - O]$ is an isomorphism:

$$
\operatorname{Jac}(E) \cong E

$$

The full Picard group decomposes as $\operatorname{Pic}(E) \cong E \times \mathbb{Z}$, where the $\mathbb{Z}$ factor records the degree.

*Example 3: The Fermat quartic.* Let $C : x^4 + y^4 + z^4 = 0 \subset \mathbb{P}^2_k$ (over $k = \mathbb{C}$). Then $g = \frac{(4-1)(4-2)}{2} = 3$, so $\operatorname{Jac}(C)$ is a principally polarized abelian variety of dimension $3$.

Over $\mathbb{C}$, $\operatorname{Jac}(C) \cong \mathbb{C}^3 / \Lambda$ for a lattice $\Lambda \cong \mathbb{Z}^6$. The period matrix can be computed explicitly from the integrals of the holomorphic differentials $\omega_1 = \frac{dx}{4y^3}$, $\omega_2 = \frac{x\,dx}{4y^3}$, $\omega_3 = \frac{z\,dx}{4y^3}$ (a basis for $H^0(C, \Omega^1_C)$) over a basis of $H_1(C, \mathbb{Z}) \cong \mathbb{Z}^6$.

It is known (by work of Gross, Rohrlich, and others) that $\operatorname{Jac}(C)$ is isogenous to a product $E_1 \times E_2 \times E_3$ of elliptic curves with complex multiplication. Specifically, $\operatorname{Jac}(C)$ is isogenous to $E^3$ where $E$ is the elliptic curve with $j$-invariant $1728$ (the curve $y^2 = x^3 - x$, having CM by $\mathbb{Z}[i]$). The automorphism group of the Fermat quartic (which contains $(\mathbb{Z}/4\mathbb{Z})^2 \rtimes S_3$, of order $96$) acts on the Jacobian and forces this decomposition.

**Key Insight:** The Jacobian linearizes the geometry of a curve: it transforms intersection-theoretic questions about divisors into linear algebra on an abelian variety. For highly symmetric curves like the Fermat quartic, the automorphism group forces the Jacobian to decompose (up to isogeny) into simpler abelian varieties, often elliptic curves with complex multiplication.

**Prerequisites:** Jacobian variety, Picard group, Abel--Jacobi map, principally polarized abelian varieties, complex multiplication, period matrix

<!-- BENCHMARK_PROBLEM: Let $C : x^4 + y^4 + z^4 = 0$ over $\mathbb{C}$. Compute $\dim \operatorname{Jac}(C)$, and write down a basis for $H^0(C, \Omega^1_C)$ using the formula for regular differentials on smooth plane curves. -->

### Remark: When is the coordinate ring of an affine curve a UFD? {#ecag-0146}

The coordinate ring $k[C] = k[x_1, \ldots, x_n] / I(C)$ of an affine curve $C$ over an algebraically closed field $k$ is a UFD if and only if the divisor class group $\operatorname{Cl}(C)$ is trivial, i.e., every Weil divisor on $C$ is principal.

For a smooth affine curve $C$, $\operatorname{Cl}(C)$ fits into the exact sequence

$$
0 \to \operatorname{Cl}(C) \to \operatorname{Pic}(\overline{C}) \to \bigoplus_{p \in \overline{C} \setminus C} \mathbb{Z} \to 0

$$

where $\overline{C}$ is the smooth projective completion of $C$. Thus $k[C]$ is a UFD if and only if the points at infinity generate $\operatorname{Pic}(\overline{C})$.

*Examples:*

1. **$C = \mathbb{A}^1$:** Then $k[C] = k[x]$, which is a PID, hence a UFD. Here $\overline{C} = \mathbb{P}^1$ with $\operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z}$, generated by the single point at infinity.

2. **$C = \mathbb{A}^1 \setminus \{0\}$:** Then $k[C] = k[x, x^{-1}]$, which is a UFD. Here $\overline{C} = \mathbb{P}^1$ and we remove the points $\{0, \infty\}$, which generate $\operatorname{Pic}(\mathbb{P}^1)$.

3. **Affine elliptic curve:** Let $\overline{C}$ be an elliptic curve and $C = \overline{C} \setminus \{O\}$ for a point $O$. Then $\operatorname{Cl}(C) = \operatorname{Pic}^0(\overline{C}) \cong \overline{C}$ as a group. Since $\overline{C}$ has infinitely many points (over an algebraically closed field), $\operatorname{Cl}(C) \neq 0$, so $k[C]$ is *not* a UFD. For instance, $k[x, y]/(y^2 - x^3 - x)$ is not a UFD.

4. **Smooth affine curve of genus $g \geq 1$ with one point removed:** Similar analysis shows $k[C]$ is not a UFD because $\operatorname{Pic}^0(\overline{C})$ is nontrivial (it is the Jacobian, an abelian variety of dimension $g$).

*Singular case.* If $C$ is singular, one must also account for the failure of the local rings to be DVRs. For instance, $k[x, y]/(y^2 - x^3)$ is not a UFD (or even integrally closed) because the cusp makes the coordinate ring non-normal.

<!-- BENCHMARK_PROBLEM: Is the coordinate ring $k[x,y]/(y^2 - x^3 - x)$ a UFD over an algebraically closed field $k$ of characteristic $\neq 2$? Justify your answer by computing $\operatorname{Cl}(C)$ for the affine curve $C : y^2 = x^3 + x$. -->

### Remark: $\mathrm{Cl}^{0}(X)$ of the nodal curve {#ecag-0147}

For the nodal cubic curve $X : y^2 z = x^2(x + z)$ in $\mathbb{P}^2_k$ (with a single node at $[0, 0, 1]$), the degree-zero part of the divisor class group is isomorphic to the multiplicative group:

$$
\operatorname{Cl}^0(X) \cong \mathbb{G}_m = k^*

$$

*Proof sketch.* The normalization of $X$ is $\nu : \mathbb{P}^1 \to X$, which is an isomorphism away from the node. The node has two preimages $p_1, p_2 \in \mathbb{P}^1$ under $\nu$. Consider the exact sequence relating divisors on $X$ to divisors on $\mathbb{P}^1$. A Cartier divisor on $X$ pulls back to a Cartier divisor on $\mathbb{P}^1$, but there is an additional constraint at the node: the local equation of the divisor must be compatible at both branches.

The kernel of $\nu^* : \operatorname{Pic}(X) \to \operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z}$ is controlled by the local structure at the node. Specifically, from the exact sequence

$$
0 \to k^* \to \operatorname{Pic}(X) \xrightarrow{\nu^*} \operatorname{Pic}(\mathbb{P}^1) \to 0

$$

one identifies $\operatorname{Cl}^0(X) \cong k^*$. The element $\lambda \in k^*$ corresponds to the line bundle on $X$ obtained by gluing the trivial bundle on $\mathbb{P}^1 \setminus \{p_1\}$ and $\mathbb{P}^1 \setminus \{p_2\}$ with transition function $\lambda$ at the node.

*Contrast with the cuspidal cubic.* For the cuspidal cubic $y^2 z = x^3$ (with a cusp at $[0, 0, 1]$), the analogous computation gives $\operatorname{Cl}^0(X) \cong \mathbb{G}_a = (k, +)$, the additive group. This reflects the fact that a node introduces multiplicative gluing data while a cusp introduces additive gluing data.

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{Cl}^0(X)$ for the nodal cubic $X : y^2 z = x^2(x+z)$ over an algebraically closed field $k$. Show that $\operatorname{Cl}^0(X) \cong k^*$ by analyzing the normalization sequence. What is $\operatorname{Cl}^0(X')$ for the cuspidal cubic $X' : y^2 z = x^3$? -->

### Example: Complex tori but not algebraic tori, intersection theory {#ecag-0148}

**Statement:** There exist compact complex manifolds that admit a complex structure but no algebraic (or even Kähler) structure. The classical examples are the Hopf surface and generic complex tori of dimension $\geq 2$.

**Construction/Proof:**

*Example 1: The Hopf surface.* Fix $a \in \mathbb{R}$, $a > 1$, and define

$$
X = \left(\mathbb{C}^2 \setminus \{(0,0)\}\right) / \left((x,y) \sim (a^k x, a^k y),\ k \in \mathbb{Z}\right)

$$

Topologically, $X$ is diffeomorphic to $S^3 \times S^1$. By the Künneth theorem:

$$
H^2(X, \mathbb{Z}) \cong H^2(S^3, \mathbb{Z}) \otimes H^0(S^1, \mathbb{Z}) \oplus H^1(S^3, \mathbb{Z}) \otimes H^1(S^1, \mathbb{Z}) \oplus H^0(S^3, \mathbb{Z}) \otimes H^2(S^1, \mathbb{Z})

$$

Since $H^1(S^3) = H^2(S^3) = H^2(S^1) = 0$, we get $H^2(X, \mathbb{Z}) = 0$.

However, any smooth projective variety $V$ of dimension $\geq 1$ has $H^2(V, \mathbb{Z}) \neq 0$: a hyperplane class gives a nonzero element. More precisely, if $V$ has an ample divisor $D$, the cohomology class $[D] \in H^2(V, \mathbb{Z})$ is nonzero (its self-intersection powers are nonzero by Nakai--Moishezon). Since $H^2(X) = 0$, $X$ admits no ample divisor, hence no algebraic structure.

In fact, $X$ is not even Kähler: a Kähler form would give a nonzero class in $H^2(X, \mathbb{R}) = 0$, a contradiction.

*Example 2: Generic complex torus.* Let $\Lambda \subset \mathbb{C}^n$ be a generic lattice of rank $2n$ (for $n \geq 2$), and set $X = \mathbb{C}^n / \Lambda$. Topologically, $X \cong (S^1)^{2n}$, so $H^2(X, \mathbb{Z}) \cong \mathbb{Z}^{\binom{2n}{2}} \neq 0$.

For $X$ to be algebraic (i.e., an abelian variety), it must admit a *polarization*: a positive definite Hermitian form $H$ on $\mathbb{C}^n$ whose imaginary part $\operatorname{Im}(H)$ takes integer values on $\Lambda \times \Lambda$ (the Riemann conditions). For a generic lattice $\Lambda$, no such $H$ exists (the Riemann conditions impose algebraic conditions on the period matrix that a generic choice does not satisfy). Hence a generic complex torus of dimension $\geq 2$ is not an abelian variety.

For $n = 1$, every complex torus $\mathbb{C}/\Lambda$ is automatically an elliptic curve (the Weierstrass $\wp$-function provides an embedding into $\mathbb{P}^2$), so the phenomenon is specific to dimension $\geq 2$.

**Key Insight:** The Hopf surface shows a complex manifold can have trivial $H^2$, ruling out all algebraic structures (no divisors of nonzero class exist). Generic complex tori show that even with nontrivial $H^2$, the Riemann bilinear relations for polarizability impose strong arithmetic constraints on the period matrix that generically fail in dimension $\geq 2$.

**Prerequisites:** Künneth theorem, cohomology of compact manifolds, ample divisors, Kähler manifolds, complex tori, Riemann conditions for abelian varieties, Nakai--Moishezon criterion

<!-- BENCHMARK_PROBLEM: Show that the Hopf surface $X = (\mathbb{C}^2 \setminus \{0\}) / ((x,y) \sim (2x, 2y))$ satisfies $H^2(X, \mathbb{Z}) = 0$, and conclude that $X$ cannot be a projective algebraic variety. -->

### Example: Degree genus formula for smooth complete intersection {#ecag-0149}

**Statement:** Let $C \subset \mathbb{P}^n$ be a smooth complete intersection curve, the intersection of $n-1$ hypersurfaces of degrees $a_1, \ldots, a_{n-1}$. Then the genus of $C$ is

$$
g(C) = \frac{1}{2} \prod_{i=1}^{n-1} a_i \left(\sum_{i=1}^{n-1} a_i - n - 1\right) + 1

$$

**Construction/Proof:** The conormal sequence for $C \subset \mathbb{P}^n$ reads

$$
0 \rightarrow \bigoplus_{i=1}^{n-1} \mathcal{O}_{\mathbb{P}^n}(-a_i)\big|_C \rightarrow \Omega^1_{\mathbb{P}^n}\big|_C \rightarrow \Omega^1_C \rightarrow 0

$$

Taking determinants (top exterior powers), we get

$$
\det(\Omega^1_C) = \det(\Omega^1_{\mathbb{P}^n}|_C) \otimes \det\left(\bigoplus_{i} \mathcal{O}(-a_i)|_C\right)^{-1}

$$

Since $\det(\Omega^1_{\mathbb{P}^n}) = \mathcal{O}_{\mathbb{P}^n}(-n-1)$ and $\det(\bigoplus \mathcal{O}(-a_i)) = \mathcal{O}(-\sum a_i)$, the adjunction formula gives

$$
\omega_C = \mathcal{O}_{\mathbb{P}^n}\left(\sum_{i=1}^{n-1} a_i - n - 1\right)\bigg|_C

$$

The degree of $\omega_C$ on $C$ is

$$
\deg(\omega_C) = \left(\sum a_i - n - 1\right) \cdot \deg(C) = \left(\sum a_i - n - 1\right) \cdot \prod a_i

$$

where $\deg(C) = \prod a_i$ by Bézout's theorem. Since $\deg(\omega_C) = 2g - 2$:

$$
2g - 2 = \left(\sum a_i - n - 1\right) \prod a_i

$$

$$
g = \frac{1}{2} \prod a_i \left(\sum a_i - n - 1\right) + 1

$$

*Special case: Complete intersection in $\mathbb{P}^3$.* For $C = V(f_1, f_2) \subset \mathbb{P}^3$ with $\deg(f_1) = a$, $\deg(f_2) = b$:

$$
g = \frac{1}{2} ab(a + b - 4) + 1

$$

For example: $a = 2, b = 2$ gives $g = 1$ (elliptic curve as intersection of two quadrics); $a = 2, b = 3$ gives $g = 4$ (canonical curve of genus 4).

**Key Insight:** The adjunction formula reduces the genus computation to knowing $\det(\Omega^1_{\mathbb{P}^n})$ (which is $\mathcal{O}(-n-1)$) and the degree of $C$ (which is $\prod a_i$ by Bézout). The genus depends only on the degrees $a_i$ and the ambient dimension $n$.

**Prerequisites:** Adjunction formula, conormal sequence, Bézout's theorem, canonical sheaf of projective space, complete intersections

<!-- BENCHMARK_PROBLEM: Compute the genus of a smooth complete intersection curve $C = V(f_1, f_2, f_3) \subset \mathbb{P}^4$ where $\deg(f_1) = 2$, $\deg(f_2) = 2$, $\deg(f_3) = 3$. Determine the degree of $C$ and the canonical sheaf $\omega_C$. -->

### Remark: Non-hyperelliptic curves {#ecag-0150}

If a smooth projective curve $C$ of genus $g \geq 2$ can be realized as a complete intersection in some $\mathbb{P}^n$, then $C$ is non-hyperelliptic. The reason is that the adjunction formula gives

$$
\omega_C = \mathcal{O}_{\mathbb{P}^n}\left(\sum a_i - n - 1\right)\bigg|_C

$$

Since $\deg(\omega_C) = 2g - 2 \geq 2$, we need $\sum a_i - n - 1 \geq 1$ (as the degree of $\omega_C$ equals $(\sum a_i - n - 1) \cdot \prod a_i > 0$). Therefore $\omega_C$ is the restriction of $\mathcal{O}_{\mathbb{P}^n}(m)$ for some $m \geq 1$, which is very ample. A curve with very ample canonical bundle is non-hyperelliptic (a hyperelliptic curve of genus $g \geq 3$ has $|K_C|$ that factors through the $g^1_2$, so $K_C$ is not very ample).

This gives a clean sufficient condition: *complete intersection implies non-hyperelliptic* (for $g \geq 3$). Note that the converse is false -- most non-hyperelliptic curves of large genus are not complete intersections.

### Example: Faithful group action on a variety with zero derivative {#ecag-0151}

**Statement:** In positive characteristic, a group scheme can act faithfully on a variety in such a way that the induced action on the tangent space at every fixed point has zero derivative. This phenomenon is impossible in characteristic zero.

**Construction/Proof:** Let $k$ be a field of characteristic $p > 0$. Define an action of $\mathbb{G}_m$ on $\mathbb{A}^1_k$ by

$$
\mathbb{G}_m(R) \times \mathbb{A}^1(R) \longrightarrow \mathbb{A}^1(R), \quad (\alpha, r) \longmapsto \alpha^p r

$$

for any $k$-algebra $R$. On coordinate rings, this is given by the coaction $k[t] \to k[s, s^{-1}] \otimes_k k[t]$, $t \mapsto s^p \otimes t$.

*Faithfulness:* The action is faithful because $\alpha^p r = r$ for all $r$ implies $\alpha^p = 1$. In characteristic $p$, $\alpha^p = 1 \Leftrightarrow (\alpha - 1)^p = 0 \Leftrightarrow \alpha = 1$ (since $R$ is reduced for any $\mathbb{G}_m(R) = R^\times$). So only the identity element acts trivially.

*Zero derivative:* The derivative of the map $\alpha \mapsto \alpha^p$ is $d(\alpha^p) = p\alpha^{p-1}\,d\alpha = 0$ in characteristic $p$. Therefore, the induced map on tangent spaces

$$
d\sigma : T_1 \mathbb{G}_m \longrightarrow T_0 \mathbb{A}^1

$$

(at the fixed point $r = 0$ and identity $\alpha = 1$) is the zero map. In other words, the Lie algebra of $\mathbb{G}_m$ acts trivially on $\mathbb{A}^1$, even though the group itself acts faithfully.

*Why this fails in characteristic zero.* In characteristic zero, if a connected algebraic group $G$ acts faithfully on a variety $X$, the induced Lie algebra action $\operatorname{Lie}(G) \to \Gamma(X, T_X)$ is injective (this follows from the exponential map or from the fact that the kernel of the Lie algebra action is a Lie ideal corresponding to a normal subgroup acting trivially). So a faithful action with zero derivative is impossible.

**Key Insight:** In characteristic $p$, the Frobenius endomorphism $\alpha \mapsto \alpha^p$ is a nontrivial group homomorphism with zero derivative. This breaks the characteristic-zero equivalence between group actions and Lie algebra actions, allowing faithful group actions to be invisible at the infinitesimal level.

**Prerequisites:** Group schemes, $\mathbb{G}_m$-actions, tangent spaces, Lie algebras in algebraic geometry, Frobenius endomorphism

<!-- BENCHMARK_PROBLEM: Let $k$ be a field of characteristic $p > 0$. Verify that the $\mathbb{G}_m$-action on $\mathbb{A}^1_k$ given by $(\alpha, r) \mapsto \alpha^p r$ is faithful but has zero derivative at $(\alpha, r) = (1, 0)$. Explain why such an action cannot exist in characteristic zero. -->

### Example: Hurwitz's bound for $\#\mathrm{Aut}(C)$ fails in positive characteristics {#ecag-0152}

**Statement:** In characteristic zero, Hurwitz's automorphism theorem states that a smooth projective curve $C$ of genus $g \geq 2$ satisfies $\#\operatorname{Aut}(C) \leq 84(g - 1)$. This bound fails in positive characteristic.

**Construction/Proof:** Let $k$ be an algebraically closed field of characteristic $p = 2g + 1$ (so $g = (p-1)/2 \geq 2$ requires $p \geq 5$). Consider the Artin--Schreier/hyperelliptic curve

$$
C : y^2 = x^p - x

$$

over $k$. This is a smooth projective curve of genus $g = (p-1)/2$ (since in the affine model $y^2 = f(x)$ with $\deg(f) = p$ odd, the genus is $(p-1)/2$).

The automorphism group of $C$ contains the following automorphisms:

1. **Translations:** $(x, y) \mapsto (x + a, y)$ for $a \in \mathbb{F}_p$. Since $x^p - x = (x+a)^p - (x+a)$ in characteristic $p$, this gives a subgroup $\mathbb{Z}/p\mathbb{Z}$.

2. **Hyperelliptic involution:** $(x, y) \mapsto (x, -y)$, an element of order $2$.

3. **$\mathbb{F}_p^*$-scaling:** $(x, y) \mapsto (\zeta x, \zeta^{(p+1)/2} y)$ for $\zeta \in \mathbb{F}_p^*$ satisfying $\zeta^p = \zeta$. This gives a subgroup $\mathbb{Z}/(p-1)\mathbb{Z}$.

4. **Additional automorphisms:** The full automorphism group is much larger. The group $\operatorname{PGL}_2(\mathbb{F}_p)$ acts on the $x$-coordinate via Möbius transformations that preserve the set of roots of $x^p - x$, and this action lifts (after appropriate adjustments) to automorphisms of $C$.

For this curve, $\#\operatorname{Aut}(C) \geq p(p-1) \cdot 2 = 2p(p-1) = 2(2g+1)(2g) = 4g(2g+1)$. The Hurwitz bound would give $84(g-1)$. For $g$ large, $4g(2g+1) = 8g^2 + 4g$ far exceeds $84(g-1) = 84g - 84$.

In fact, the full automorphism group has order $\#\operatorname{Aut}(C) = 2p(p^2 - 1) = 2(2g+1)((2g+1)^2 - 1)$, which grows as $\sim 16g^3$, vastly exceeding the Hurwitz bound $84(g-1) \sim 84g$.

*Why Hurwitz fails.* The proof of Hurwitz's bound uses the Riemann--Hurwitz formula for the quotient map $C \to C/\operatorname{Aut}(C)$. In characteristic $p$, wild ramification contributes additional terms, and the ramification divisor can be much larger than in the tame case. The curve $y^2 = x^p - x$ has automorphisms of order $p$ (the translations), which produce wild ramification in the quotient.

**Key Insight:** Wild ramification in characteristic $p$ allows the ramification contribution in the Riemann--Hurwitz formula to be arbitrarily large relative to the degree of the covering, breaking the balance that produces Hurwitz's $84(g-1)$ bound in the tame case.

**Prerequisites:** Hurwitz's automorphism theorem, Riemann--Hurwitz formula, wild ramification, Artin--Schreier curves, automorphisms of curves

<!-- BENCHMARK_PROBLEM: Let $p \geq 5$ be prime and $k = \overline{\mathbb{F}_p}$. Compute the genus of $C : y^2 = x^p - x$ and exhibit at least $2p(p-1)$ distinct automorphisms of $C$. Compare this count with the Hurwitz bound $84(g-1)$ for $p = 7$. -->

### Example: Non-trivial automorphism that fixes every $\mathbb{F}_{p}$ point {#ecag-0153}

**Statement:** Over $\mathbb{F}_p$, there exist smooth projective curves admitting non-trivial automorphisms that fix every $\mathbb{F}_p$-rational point.

**Construction/Proof:** Consider the curves over $k = \overline{\mathbb{F}_p}$:

$$
C_1 : y^2 = x^p - x, \qquad C_2 : y^2 = x^p - x^{p-1} - x + 1 = (x-1)(x^{p-1} - 1)

$$

The hyperelliptic involution $\sigma : (x, y) \mapsto (x, -y)$ is a non-trivial automorphism ($\sigma \neq \operatorname{id}$ since $\operatorname{char}(k) \neq 2$ when $p > 2$, and for $p = 2$, $\sigma = \operatorname{id}$, so assume $p > 2$).

*Curve $C_1$:* The $\mathbb{F}_p$-rational points of $C_1$ are the points $(a, b)$ with $a, b \in \mathbb{F}_p$ and $b^2 = a^p - a$. By Fermat's little theorem, $a^p = a$ for all $a \in \mathbb{F}_p$, so $a^p - a = 0$ for every $a \in \mathbb{F}_p$. Therefore $b = 0$ at every affine $\mathbb{F}_p$-point, and $\sigma(a, 0) = (a, -0) = (a, 0)$. Together with the point at infinity (which is also fixed by $\sigma$), we conclude that $\sigma$ fixes every $\mathbb{F}_p$-point of $C_1$.

*Curve $C_2$:* We have $x^p - x^{p-1} - x + 1 = (x-1)(x^{p-1} - 1)$. For $a \in \mathbb{F}_p$, $a^p - a^{p-1} - a + 1 = a - a^{p-1} - a + 1 = 1 - a^{p-1}$. By Fermat's little theorem, $a^{p-1} = 1$ for $a \neq 0$, and $a^{p-1} = 0$ for $a = 0$. So the affine $\mathbb{F}_p$-rational points are:
  - $(0, b)$ with $b^2 = 1$, giving $(0, 1)$ and $(0, -1)$
  - $(a, b)$ for $a \neq 0$: $b^2 = 1 - 1 = 0$, so $b = 0$, giving $(a, 0)$ for $a = 1, 2, \ldots, p-1$

The involution $\sigma$ fixes all points $(a, 0)$ (for $a = 1, \ldots, p-1$) and the point at infinity, but it switches $(0, 1)$ and $(0, -1)$. So $\sigma$ fixes every $\mathbb{F}_p$-rational point of $C_2$ except for the pair $\{(0, 1), (0, -1)\}$, which it permutes.

**Key Insight:** The Frobenius identity $a^p = a$ for $a \in \mathbb{F}_p$ forces $x^p - x$ to vanish on all $\mathbb{F}_p$-points, making $y = 0$ at every affine rational point of $C_1$. This ensures the hyperelliptic involution (which negates $y$) fixes all rational points. This illustrates that over finite fields, non-trivial automorphisms can be "invisible" at the level of rational points.

**Prerequisites:** Hyperelliptic involution, Fermat's little theorem, rational points over finite fields

<!-- BENCHMARK_PROBLEM: Let $p = 5$ and $C_1 : y^2 = x^5 - x$ over $\mathbb{F}_5$. List all $\mathbb{F}_5$-rational points of $C_1$ (including the point at infinity) and verify that the hyperelliptic involution $\sigma : (x,y) \mapsto (x, -y)$ fixes every one. -->

### Example: The automorphism group of a curve over any field with $g\geq 2$ is finite, how to produce vector fields on a variety? {#ecag-0154}

**Statement:** Let $C$ be a smooth projective curve of genus $g \geq 2$ over any field $k$. Then $\operatorname{Aut}(C)$ is finite (as a group scheme, it is zero-dimensional).

**Construction/Proof:**

*Step 1: Canonical embedding.* Since $g \geq 2$ (and for $g = 2$, using $\omega_C^{\otimes m}$ for $m \geq 3$, which is very ample), choose $m$ large enough so that $\omega_C^{\otimes m}$ is very ample. This gives an $\operatorname{Aut}(C)$-equivariant embedding

$$
j : C \hookrightarrow \mathbb{P}(H^0(C, \omega_C^{\otimes m})) =: \mathbb{P}V

$$

The equivariance means: $\operatorname{Aut}(C)$ acts on $V = H^0(C, \omega_C^{\otimes m})$ by pullback of differential forms, and $j$ intertwines this linear action with the geometric action on $C$. This gives an injective homomorphism $\operatorname{Aut}(C) \hookrightarrow \operatorname{PGL}(V)$.

*Step 2: Reduction to finiteness via vector fields.* Suppose for contradiction that $\operatorname{Aut}(C)$ is infinite. Take the Zariski closure $G = \overline{\operatorname{Aut}(C)} \subset \operatorname{PGL}(V)$. Since $\operatorname{PGL}(V)$ is of finite type and $\operatorname{Aut}(C)$ is infinite, $\dim(G) \geq 1$. The group $G$ acts on $C$ (as everything is defined by polynomial equations in $\mathbb{P}V$).

*Step 3: Constructing a nonzero vector field.* Since $\dim(G) \geq 1$, the tangent space $T_e G = \operatorname{Lie}(G)$ has dimension $\geq 1$. Pick a nonzero $v \in T_e G$. Any element of $\operatorname{Lie}(\operatorname{PGL}(V))$ generates a vector field on $\mathbb{P}V$ (by differentiating the one-parameter subgroup action). Since $G$ acts on $C$, the restriction of this vector field to $C$ gives a nonzero global section of $T_C$.

*Step 4: Contradiction.* But $\deg(T_C) = 2 - 2g < 0$ for $g \geq 2$, so $H^0(C, T_C) = 0$ (a line bundle of negative degree on a smooth projective curve has no nonzero global sections). This contradicts the existence of a nonzero global vector field on $C$.

Therefore $\operatorname{Aut}(C)$ must be finite.

**Key Insight:** The canonical embedding linearizes the automorphism group, embedding it into $\operatorname{PGL}(V)$. If $\operatorname{Aut}(C)$ were infinite, differentiating would produce a global vector field on $C$. But $\deg(T_C) = 2 - 2g < 0$ for $g \geq 2$ forbids this, giving the contradiction. This argument works over any field, including positive characteristic.

**Prerequisites:** Canonical embedding, very ample line bundles, algebraic groups, Lie algebras, vector fields on curves, degree of tangent bundle

<!-- BENCHMARK_PROBLEM: Let $C$ be a smooth projective curve of genus $g \geq 2$ over an algebraically closed field $k$. Prove that $H^0(C, T_C) = 0$ and use this to show that $\operatorname{Aut}(C)$ is finite. (Hint: embed $C$ via $\omega_C^{\otimes m}$ and use the Lie algebra of the Zariski closure of $\operatorname{Aut}(C)$ in $\operatorname{PGL}$.) -->

### Remark {#ecag-0155}

This proof that $\operatorname{Aut}(C)$ is finite for $g \geq 2$ (via the canonical embedding and the vanishing $H^0(C, T_C) = 0$) is due to Daniel Litt. The argument is notable for its simplicity and generality: it works uniformly over all fields, including positive characteristic, where the standard complex-analytic proofs (using the uniformization theorem or Teichmüller theory) are unavailable. See Litt's notes [here](https://static1.squarespace.com/static/57bf2a6de3df281593b7f57d/t/57bf698ff7e0abe0fdca085a/1472162191829/curve-automorphisms.pdf).

### Remark: Canonical embedding {#ecag-0156}

The canonical embedding plays a central role in the proof of finiteness of $\operatorname{Aut}(C)$ and in the study of curves more broadly. Its key properties:

1. **Linearization of $\operatorname{Aut}(C)$.** The embedding $j : C \hookrightarrow \mathbb{P}V$ (where $V = H^0(C, \omega_C^{\otimes m})$) is $\operatorname{Aut}(C)$-equivariant, giving an injective homomorphism $\operatorname{Aut}(C) \hookrightarrow \operatorname{PGL}(V)$. This reduces the study of automorphisms to linear algebra.

2. **Vector fields from the Lie algebra.** A nonzero element $v \in T_e(G)$ (where $G = \overline{\operatorname{Aut}(C)} \subset \operatorname{PGL}(V)$) generates a vector field on $\mathbb{P}V$ via the linear action, and its restriction to $C$ is a global vector field on $C$. If $G$ is positive-dimensional, this produces a nonzero section of $T_C$, contradicting $\deg(T_C) < 0$.

*Concrete example.* Consider the Fermat quartic $C : x^4 + y^4 + z^4 = 0 \subset \mathbb{P}^2_k$. Here $\omega_C \cong \mathcal{O}_C(1)$ (by adjunction), so $H^0(C, \omega_C)$ is spanned by the restrictions of $x, y, z$ to $C$. The canonical embedding is simply the given inclusion $C \hookrightarrow \mathbb{P}^2$. The automorphism group $\operatorname{Aut}(C) \subset \operatorname{PGL}_3$ is finite (it is the group of permutations and sign changes of coordinates preserving $x^4 + y^4 + z^4$, which has order $96$). No nonzero global vector field exists on $C$ since $\deg(T_C) = 2 - 2 \cdot 3 = -4 < 0$.
