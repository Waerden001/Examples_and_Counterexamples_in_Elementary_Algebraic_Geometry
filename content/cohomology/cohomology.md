---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/cohomology.tex
---

### Example: Serre's example {#ecag-0184}

**Statement:** Let $X$ be a projective variety over a field $k$. Serre's fundamental example demonstrates that sheaf cohomology $H^i(X, \mathcal{F})$ for coherent sheaves $\mathcal{F}$ on $X$ can be computed via Cech cohomology when the cover is sufficiently nice (e.g., affine). Specifically, let $X = \mathbb{P}^n_k$ and consider the standard affine cover $\{U_i = D_+(x_i)\}_{i=0}^{n}$. Then for any quasi-coherent sheaf $\mathcal{F}$ on $X$, the Cech cohomology with respect to this cover computes the sheaf cohomology:

$$
\check{H}^i(\{U_j\}, \mathcal{F}) \cong H^i(X, \mathcal{F}).

$$

In particular, Serre showed that for $X = \mathbb{P}^n_k$ and $\mathcal{F} = \mathcal{O}_X(m)$:

$$
H^i(\mathbb{P}^n_k, \mathcal{O}(m)) = \begin{cases} S_m & \text{if } i = 0, \\ 0 & \text{if } 0 < i < n, \\ S_{-m-n-1}^{\vee} & \text{if } i = n, \end{cases}

$$

where $S = k[x_0, \ldots, x_n]$ and $S_d$ denotes the degree $d$ graded piece.

**Construction/Proof:** The proof relies on Serre's vanishing theorem for affine covers. Since each $U_i = \operatorname{Spec}(k[x_0/x_i, \ldots, x_n/x_i])$ is affine, and intersections $U_{i_0} \cap \cdots \cap U_{i_p}$ are also affine (as open subsets of affine schemes defined by inverting elements), the Leray theorem for acyclic covers applies. The Cech complex for $\mathcal{O}(m)$ on the standard cover is:

$$
0 \rightarrow \bigoplus_{i} S_{x_i} \rightarrow \bigoplus_{i < j} S_{x_i x_j} \rightarrow \cdots \rightarrow S_{x_0 x_1 \cdots x_n} \rightarrow 0,

$$

where all modules are taken in degree $m$. The $H^0$ is the intersection $\bigcap_i (S_{x_i})_m = S_m$ for $m \geq 0$ (global sections are polynomials of degree $m$). The $H^n$ consists of Laurent monomials $x_0^{a_0} \cdots x_n^{a_n}$ of degree $m$ with all $a_i < 0$, which by the substitution $a_i \mapsto -1 - b_i$ is dual to degree $-m - n - 1$ polynomials.

**Key Insight:** The computation works because affine schemes have vanishing higher cohomology for quasi-coherent sheaves, so the standard affine open cover of projective space gives an acyclic Cech cover, reducing sheaf cohomology to an explicit combinatorial computation with Laurent polynomials.

**Prerequisites:** Sheaf cohomology, Cech cohomology, projective space, quasi-coherent sheaves, Leray's theorem

<!-- BENCHMARK_PROBLEM: Let X = P^2_k with the standard affine cover {U_0, U_1, U_2}. Compute H^0(P^2, O(2)) and H^2(P^2, O(-4)) as k-vector spaces. What are their dimensions? -->

### Example: Why $H^{i}(X, \mathscr{F}(n))=0$? {#ecag-0185}

**Statement:** Let $X$ be a projective scheme over a noetherian ring $A$, let $\mathcal{O}_{X}(1)$ be a very ample invertible sheaf on $X$ over $\operatorname{Spec}(A)$, and let $\mathscr{F}$ be a coherent sheaf on $X$. Then:

1. For all $i \geq 0$, $H^{i}(X, \mathscr{F})$ is a finitely generated $A$-module.
2. For all $i \geq 1$, there exists $n_0 = n_0(i, \mathscr{F})$ such that $H^{i}(X, \mathscr{F}(n)) = 0$ for all $n \geq n_0$.

**Construction/Proof:** The intuition comes from the explicit computation on projective space. Consider $H^{n}(\mathbb{P}^{n}, \mathcal{O}(m))$: this is the $k$-vector space spanned by Laurent monomials $x_{0}^{a_{0}} \cdots x_{n}^{a_{n}}$ of total degree $m$ with all $a_i \leq -1$. For such a monomial to exist in degree $m$, we need $a_0 + \cdots + a_n = m$ with each $a_i \leq -1$, which forces $m \leq -n - 1$, i.e., $m + n + 1 \leq 0$. So $H^n(\mathbb{P}^n, \mathcal{O}(m)) = 0$ for $m \geq -n$. Twisting by $\mathcal{O}(n)$ corresponds to shifting $m \mapsto m + n$, so for large enough twist the negative-exponent condition cannot be satisfied.

One key application of the vanishing theorem is that it simplifies derived pushforwards. In general, for a proper morphism $f: X \to Y$ and a coherent sheaf $\mathscr{F}$, the derived pushforward $\mathbf{R}f_*\mathscr{F}$ involves all $R^i f_* \mathscr{F}$. However, if we twist $\mathscr{F}$ sufficiently, only $f_* \mathscr{F}(n)$ survives.

For example, by FGA Explained (Lemma 5.4): let $\phi: T \rightarrow S$ be a morphism of noetherian schemes, $\mathscr{F}$ a coherent sheaf on $\mathbb{P}_{S}^{n}$, and $\mathscr{F}_{T}$ its pullback to $\mathbb{P}_{T}^{n}$. Let $\pi_{S}: \mathbb{P}_{S}^{n} \rightarrow S$ and $\pi_{T}: \mathbb{P}_{T}^{n} \rightarrow T$ be the projections. Then there exists $r_0$ such that the base-change homomorphism

$$
\phi^{*}\pi_{S,*}\mathscr{F}(r) \rightarrow \pi_{T,*}\mathscr{F}_{T}(r)

$$

is an isomorphism for all $r \geq r_0$. Without twisting, the correct statement involves derived categories: there is a quasi-isomorphism

$$
L\phi^{*} \mathbf{R}\pi_{S,*}\mathscr{F} \xrightarrow{\sim} \mathbf{R}\pi_{T,*}\mathscr{F}_{T}

$$

under appropriate flatness hypotheses (flat base change theorem).

**Key Insight:** The vanishing of higher cohomology after twisting is ultimately a finiteness phenomenon: the negative-degree Laurent monomials contributing to $H^n$ get pushed into positive degrees by the twist, and eventually no monomials satisfy the required negativity conditions.

**Prerequisites:** Coherent sheaves, sheaf cohomology on projective schemes, Serre vanishing theorem, derived pushforward, base change

<!-- BENCHMARK_PROBLEM: Let F = O(m) on P^n_k. For which values of m is H^n(P^n, O(m)) = 0? Express the answer in terms of n. -->

### Example: Local duality $H^{i}_{\mathfrak{m}}(M)\cong (\mathrm{Ext}^{r+1-i}(M, S(-r-1)))^{\vee}$ {#ecag-0186}

**Statement:** Let $S = k[x, y]$ with the irrelevant maximal ideal $\mathfrak{m} = (x, y)$, and consider the graded $S$-module $R = k[x, y]/(x^2, xy)$. Compute the local cohomology modules $H_{\mathfrak{m}}^{i}(R)$, the Hilbert polynomial $\chi_R(t)$, and the Castelnuovo-Mumford regularity of $R$. The Cech complex for computing local cohomology is:

$$
0 \rightarrow R \xrightarrow{\binom{1}{1}} R[x^{-1}] \oplus R[y^{-1}] \rightarrow R[x^{-1}y^{-1}] \rightarrow 0.

$$

**Construction/Proof:** Step 1: Analyze $R = k[x,y]/(x^2, xy)$. As a $k$-vector space, a basis for $R$ is $\{1, x, y, y^2, y^3, \ldots\}$. The element $x$ is annihilated by both $x$ and $y$ in $R$.

Step 2: Compute the localizations. In $R[x^{-1}]$, since $x^2 = 0$ in $R$, we get $0 = x^2 \cdot x^{-2} = 1$, so $R[x^{-1}] = 0$. Thus the Cech complex simplifies to:

$$
0 \rightarrow R \xrightarrow{\iota} R[y^{-1}] \rightarrow 0.

$$

Step 3: Compute $H^0_{\mathfrak{m}}(R) = \ker(\iota)$. This consists of elements $r \in R$ annihilated by some power of $y$. Since $y^n \cdot x = 0$ for $n \geq 1$ (as $xy = 0$ in $R$) and $y^n \cdot 1 = y^n \neq 0$, we have $H^0_{\mathfrak{m}}(R) = (x) \cong k$ concentrated in degree 1.

Step 4: Compute $H^1_{\mathfrak{m}}(R)$. We have $R[y^{-1}] \cong k[y, y^{-1}]$ (since $x = 0$ in $R[y^{-1}]$ because $x = x \cdot y \cdot y^{-1} = 0$). The cokernel $R[y^{-1}]/R$ is the span of $\{y^{-1}, y^{-2}, \ldots\}$, so $H^1_{\mathfrak{m}}(R) \cong k[y^{-1}] \cdot y^{-1}$.

Step 5: The Hilbert function is $H_R(t) = \dim_k R_t$. We have $R_0 = k$, $R_1 = \langle x, y \rangle \cong k^2$, and $R_t = \langle y^t \rangle \cong k$ for $t \geq 2$. Thus the Hilbert polynomial is $\chi_R(t) = 1$ for $t \gg 0$.

Step 6: For Castelnuovo-Mumford regularity, we need the largest $d$ such that $H^i_{\mathfrak{m}}(R)_{d-i} \neq 0$ for some $i$. We have $H^0_{\mathfrak{m}}(R)$ nonzero only in degree 1 and $H^1_{\mathfrak{m}}(R)$ nonzero in degrees $\leq -1$. So $\operatorname{reg}(R) = \max(1 + 0, -1 + 1) = 1$.

Step 7: Verify by local duality. With $r = 1$ (since $S = k[x,y]$ has Krull dimension 2), local duality gives $H^i_{\mathfrak{m}}(R) \cong (\operatorname{Ext}_S^{2-i}(R, S(-2)))^{\vee}$.

**Key Insight:** The localization $R[x^{-1}]$ vanishes because $x$ is nilpotent in $R$, which dramatically simplifies the Cech complex and makes the local cohomology computation tractable.

**Prerequisites:** Local cohomology, Cech complex, Castelnuovo-Mumford regularity, Hilbert polynomial, local duality theorem

<!-- BENCHMARK_PROBLEM: Let S = k[x,y], m = (x,y), and R = S/(x^2, xy). Compute H^0_m(R) and H^1_m(R) as graded k-vector spaces, and determine the Castelnuovo-Mumford regularity of R. -->

### Remark: Reference {#ecag-0187}

This example and the original local duality theorem can be found in Eisenbud's *The Geometry of Syzygies* (Springer, 2005). The local duality theorem in its general form states that for a polynomial ring $S = k[x_0, \ldots, x_r]$ with irrelevant ideal $\mathfrak{m}$, and a finitely generated graded $S$-module $M$, there is a natural isomorphism of graded modules:

$$
H^i_{\mathfrak{m}}(M) \cong \left(\operatorname{Ext}_S^{r+1-i}(M, S(-r-1))\right)^{\vee}

$$

where $(-)^{\vee}$ denotes the graded $k$-dual. This duality is a graded local version of Serre duality.

### Example: Hartshorne $\mathrm{II}.5.14$ {#ecag-0188}

**Statement:** Let $X$ be a connected, normal closed subscheme of $\mathbb{P}_A^r$, where $A$ is a finitely generated $k$-algebra for a field $k$. Let $S(X) = A[x_0, \ldots, x_r]/I$ be the homogeneous coordinate ring (where $I = \Gamma_*(\mathscr{I}_X)$), and let $\Gamma = \Gamma_*(X, \mathcal{O}_X) = \bigoplus_{n \geq 0} \Gamma(X, \mathcal{O}_X(n))$. Then:

1. $\Gamma$ is integral over $S = S(X)$.
2. $\Gamma$ is integrally closed.
3. $\Gamma_d = S_d$ for $d$ sufficiently large.
4. $S^{(d)} = \bigoplus_{n \geq 0} S_{nd}$ is integrally closed for all $d$. In particular, the $d$-uple embedding is projectively normal for $d \gg 0$.

**Construction/Proof:** We prove each statement in turn.

*Step 1: $\Gamma$ is integral over $S$.* Since $X$ is an integral scheme (connected and normal implies irreducible), $S$ is an integral domain. By definition,

$$
\Gamma = \bigcap_{i=0}^{r} S_{x_i}

$$

where $S_{x_i}$ denotes localization at $x_i$. For any $y \in \Gamma$, we can choose $N$ large enough so that $x_i^N y \in S$ for all $i$. In other words, $y \in S \cdot \frac{1}{x_i^N}$, and since $S \cdot \frac{1}{x_i^N}$ is a finitely generated $S$-module, $y$ is integral over $S$.

*Step 2: $\Gamma$ is integrally closed.* The degree-zero part $S_{((x_i))}$ of $S_{x_i}$ is integrally closed, since it is isomorphic to the affine coordinate ring of $X \cap D_+(x_i)$, which is normal (as $X$ is normal). Define

$$
\Gamma^{(i)} := \{z \in S_{x_i} \mid \deg(z) \geq 0\} \cong S_{((x_i))}[x_i].

$$

Then $\Gamma = \bigcap_{i=0}^{r} \Gamma^{(i)}$. Since $S_{((x_i))}$ is integrally closed, so is the polynomial ring $\Gamma^{(i)} = S_{((x_i))}[x_i]$. An intersection of integrally closed subrings of a common fraction field is integrally closed, so $\Gamma$ is integrally closed. Therefore $\Gamma$ is the integral closure of $S$.

*Step 3: $\Gamma_d = S_d$ for large $d$.* Since $\Gamma$ is the integral closure of $S$ in its fraction field, and $S$ is a finitely generated $k$-algebra that is a domain, the integral closure $\Gamma$ is a finite $S$-module (by the finiteness of integral closure for finitely generated domains over a field). Let $\{y_1, \ldots, y_m\}$ be generators of $\Gamma$ as an $S$-module. For each $y_j$, there exists $N_j$ such that $x_i^{N_j} y_j \in S$. Thus for $d$ large enough, $\Gamma_d \subset S_d$. Combined with $S \subset \Gamma$, we get $S_d = \Gamma_d$ for $d \gg 0$.

*Step 4: $\Gamma^{(d)}$ is integrally closed for all $d$.* Suppose $y \in \operatorname{Frac}(\Gamma^{(d)})$ is integral over $\Gamma^{(d)}$. Then $y \in \Gamma$ (since $\Gamma$ is integrally closed and $\operatorname{Frac}(\Gamma^{(d)}) \subset \operatorname{Frac}(\Gamma)$). Since $y \in \Gamma \cap \operatorname{Frac}(\Gamma^{(d)})$, we can write $y = y'/x_i^{dk_1}$ for some $y' \in \Gamma^{(d)}$, so $\deg(y)$ is divisible by $d$. For large $N$, $x_i^{dN} y^n \in S$ for all $n$, and since $d \mid dN + n\deg(y)$, we have $x_i^{dN} y^n \in \Gamma^{(d)}$ for all $n$, which implies $y$ is integral over $\Gamma^{(d)}$, hence $y \in \Gamma^{(d)}$. Therefore $\Gamma^{(d)}$ is integrally closed for all $d$. For $d \gg 0$, $S^{(d)} = \Gamma^{(d)}$, so $S^{(d)}$ is integrally closed.

*Corollary:* A normal closed subscheme $X \subset \mathbb{P}_A^r$ is projectively normal if and only if the restriction map

$$
\Gamma(\mathbb{P}_A^r, \mathcal{O}_{\mathbb{P}_A^r}(n)) \rightarrow \Gamma(X, \mathcal{O}_X(n))

$$

is surjective for all $n \geq 0$. For instance, nonsingular degree-$d$ hypersurfaces in $\mathbb{P}^r$ are projectively normal.

**Key Insight:** The integral closure of the homogeneous coordinate ring $S(X)$ is always $\Gamma_*(X, \mathcal{O}_X)$ when $X$ is normal, and the two agree in large enough degrees by finiteness of integral closure. This is why the $d$-uple embedding eventually makes any normal variety projectively normal.

**Prerequisites:** Projective schemes, integral closure, normal varieties, homogeneous coordinate ring, Veronese embedding

<!-- BENCHMARK_PROBLEM: Let X be a normal projective variety over a field k embedded in P^r. Prove that the Veronese d-uple embedding of X is projectively normal for d sufficiently large. What is the key algebraic fact that guarantees Gamma_d = S(X)_d for large d? -->

### Example: $\Gamma_{*}(X,\mathcal{O}_{X})\neq S(X)$ {#ecag-0189}

**Statement:** There exist projective schemes $X \subset \mathbb{P}^r$ for which the graded ring of global sections $\Gamma_*(X, \mathcal{O}_X) = \bigoplus_{n \geq 0} \Gamma(X, \mathcal{O}_X(n))$ is strictly larger than the homogeneous coordinate ring $S(X)$. A concrete example is the rational quartic curve in $\mathbb{P}^3$.

**Construction/Proof:** Consider the morphism

$$
C: \mathbb{P}^1 \rightarrow \mathbb{P}^3, \quad [u, v] \mapsto [u^4, u^3 v, uv^3, v^4].

$$

This is the image of $\mathbb{P}^1$ under the incomplete linear system spanned by $\{u^4, u^3v, uv^3, v^4\} \subset H^0(\mathbb{P}^1, \mathcal{O}(4))$. The monomial $u^2 v^2$ is missing from this list, which is the source of the failure of projective normality.

Step 1: Compute cohomology. The ideal sheaf sequence $0 \to \mathscr{I}_C \to \mathcal{O}_{\mathbb{P}^3} \to \mathcal{O}_C \to 0$ twisted by $\mathcal{O}(1)$ gives:

$$
0 \to H^0(\mathbb{P}^3, \mathscr{I}_C(1)) \to H^0(\mathbb{P}^3, \mathcal{O}_{\mathbb{P}^3}(1)) \to H^0(C, \mathcal{O}_C(1)) \to H^1(\mathbb{P}^3, \mathscr{I}_C(1)) \to 0.

$$

We have $H^0(\mathbb{P}^3, \mathscr{I}_C(1)) = 0$ (no linear form vanishes on $C$) and $H^1(\mathbb{P}^3, \mathscr{I}_C(1)) \cong k$. Since $\mathcal{O}_C(1) \cong \mathcal{O}_{\mathbb{P}^1}(4)$, we get $h^0(C, \mathcal{O}_C(1)) = 5$, while $h^0(\mathbb{P}^3, \mathcal{O}(1)) = 4$. The extra section is precisely $u^2 v^2$.

Step 2: Verify that $u^2 v^2$ is a global section. On each standard affine open:

- $D_+(x)$: $u^2 v^2 = (y/x)^2 \cdot x$
- $D_+(y)$: $u^2 v^2 = (x/y)(z/y) \cdot y$
- $D_+(z)$: $u^2 v^2 = (y/z)(w/z) \cdot z$
- $D_+(w)$: $u^2 v^2 = (z/w)^2 \cdot w$

where $x, y, z, w$ are the coordinates on $\mathbb{P}^3$. Each expression is a regular function times a degree-1 element, confirming $u^2 v^2 \in \Gamma(C, \mathcal{O}_C(1))$.

Step 3: Conclude. Since the restriction map $H^0(\mathbb{P}^3, \mathcal{O}(1)) \to H^0(C, \mathcal{O}_C(1))$ is not surjective (it has a 1-dimensional cokernel), $C$ is not projectively normal, and $\Gamma_*(C, \mathcal{O}_C) \neq S(C)$.

**Key Insight:** The curve $C$ is the image of $\mathbb{P}^1$ under an incomplete linear system of degree 4 (missing $u^2v^2$), so the restriction of linear forms on $\mathbb{P}^3$ does not recover all degree-4 monomials on $\mathbb{P}^1$. This gap between $S(X)$ and $\Gamma_*(X, \mathcal{O}_X)$ is detected by $H^1(\mathbb{P}^3, \mathscr{I}_C(1)) \neq 0$.

**Prerequisites:** Projective normality, ideal sheaf sequence, cohomology of line bundles on $\mathbb{P}^1$, Veronese and Segre maps

<!-- BENCHMARK_PROBLEM: Let C be the image of the map P^1 -> P^3 given by [u,v] -> [u^4, u^3v, uv^3, v^4]. Compute h^0(C, O_C(1)) and h^0(P^3, O(1)), and explain why C is not projectively normal. -->

### Remark: Relations between the homogeneous coordinate ring $S(X)$ and $\oplus_{n\geq 0}\mathcal{O}_{X}(n)$ {#ecag-0190}

One must carefully distinguish the following concepts for a projective scheme $X = \operatorname{Proj}(S)$:

- **$X = \operatorname{Proj}(S)$**: The scheme $X$ is defined by the graded ring $S$, but the ring $S$ is not uniquely determined by $X$. Different graded rings can give isomorphic schemes.
- **The homogeneous coordinate ring $S(X)$**: This depends on the specific closed embedding $X \hookrightarrow \mathbb{P}^r$. It is one particular graded ring $S$ such that $X = \operatorname{Proj}(S)$.
- **$\Gamma(X, \mathcal{O}_X) \neq S$**: The ring of global sections is just the degree-zero part of $\Gamma_*(X, \mathcal{O}_X)$, which in general does not equal $S_0$.
- **$\Gamma_*(X, \mathcal{O}_X) = \bigoplus_{n \geq 0} \Gamma(X, \mathcal{O}_X(n))$**: This is the "saturation" of $S$. In general $\Gamma_*(X, \mathcal{O}_X) \neq S$, though $\widetilde{S} \cong \widetilde{\Gamma_*(X, \mathcal{O}_X)}$ as sheaves on $X$.
- **Even if $S$ is a domain**, $\Gamma(X, \mathcal{O}_X)$ equals the degree-0 part of $\Gamma_*(X, \mathcal{O}_X)$, not $S_{(0)}$ (the degree-zero elements of the localization).
- **Isomorphism $X \cong Y$ does not imply $\mathcal{O}_X(n) \cong f^*\mathcal{O}_Y(n)$** in general, since $\mathcal{O}(1)$ depends on the embedding, not just the abstract scheme.

<!-- BENCHMARK_PROBLEM: Give an example of two graded rings S and S' with Proj(S) isomorphic to Proj(S') but S not isomorphic to S' as graded rings. -->

### Remark: Local cohomology, Mumford regularity, Hilbert polynomial {#ecag-0191}

The local cohomology $H_Q^i(-)$ is defined as the $i$-th right derived functor of the $Q$-torsion functor:

$$
H_Q^0(M) := \{m \in M \mid Q^d m = 0 \text{ for some } d \geq 1\}.

$$

When $R$ is a noetherian ring and $Q = (x_1, \ldots, x_t)$, local cohomology can be computed via the Cech complex. For any $R$-module $M$, $H_Q^i(M)$ is the $i$-th cohomology of:

$$
C(x_1, \ldots, x_t; M): 0 \rightarrow M \xrightarrow{d} \bigoplus_{i=1}^{t} M[x_i^{-1}] \xrightarrow{d} \cdots \rightarrow \bigoplus_{\#J = k} M[x_J^{-1}] \rightarrow \cdots \rightarrow M[x_{1,2,\ldots,t}^{-1}] \rightarrow 0.

$$

The differential is given by:

$$
d(m_J \in M[x_J^{-1}]) = \sum_{k \notin J} (-1)^{\#\{i \in J \mid i < k\}} m_{J \cup \{k\}}

$$

where $m_{J \cup \{k\}}$ denotes the image of $m_J$ under the natural localization map $M[x_J^{-1}] \rightarrow M[x_{J \cup \{k\}}^{-1}]$.

The **Castelnuovo-Mumford regularity** of a finitely generated graded $S$-module $M$ (where $S = k[x_0, \ldots, x_r]$) is defined as:

$$
\operatorname{reg}(M) = \max\{d + i \mid H_{\mathfrak{m}}^i(M)_d \neq 0\}

$$

where $\mathfrak{m} = (x_0, \ldots, x_r)$. This invariant controls when the Hilbert function of $M$ agrees with the Hilbert polynomial.

<!-- BENCHMARK_PROBLEM: Let S = k[x,y,z] and M = S/(x,y). Compute H^i_m(M) for all i, where m = (x,y,z), and determine reg(M). -->

### Example: Regularity theorem is false if the sheaf is not an ideal sheaf {#ecag-0192}

**Statement:** Let $\mathscr{F} = \mathcal{O}_{\mathbb{P}^1}(k) \oplus \mathcal{O}_{\mathbb{P}^1}(-k)$ for $k \geq 0$. The Euler characteristic (and hence the Hilbert polynomial) of $\mathscr{F}$ is independent of $k$, yet the Castelnuovo-Mumford regularity of $\mathscr{F}$ depends on $k$ and can be made arbitrarily large. This shows that the regularity of a coherent sheaf cannot be bounded purely in terms of its Hilbert polynomial, unlike the case of ideal sheaves.

**Construction/Proof:** Step 1: Compute the Euler characteristic. We have:

$$
\chi(\mathscr{F}(m)) = \chi(\mathcal{O}(m+k)) + \chi(\mathcal{O}(m-k)) = (m + k + 1) + (m - k + 1) = 2m + 2.

$$

This equals $2\binom{m+1}{1}$ and is independent of $k$.

Step 2: Compute the regularity. The sheaf $\mathscr{F}$ is $m$-regular if $H^1(\mathbb{P}^1, \mathscr{F}(m-1)) = 0$. We have:

$$
H^1(\mathbb{P}^1, \mathscr{F}(m-1)) = H^1(\mathbb{P}^1, \mathcal{O}(m-1+k)) \oplus H^1(\mathbb{P}^1, \mathcal{O}(m-1-k)).

$$

By Serre duality, $H^1(\mathbb{P}^1, \mathcal{O}(j)) = 0$ if and only if $j \geq -1$. So:
- $H^1(\mathbb{P}^1, \mathcal{O}(m-1+k)) = 0$ for $m \geq -k$ (always satisfied for $m \geq 0$).
- $H^1(\mathbb{P}^1, \mathcal{O}(m-1-k)) = 0$ if and only if $m - 1 - k \geq -1$, i.e., $m \geq k$.

Therefore $\operatorname{reg}(\mathscr{F}) = k$.

Step 3: Conclude. If there existed a polynomial $F(a_0, a_1)$ bounding the regularity in terms of the coefficients $a_0, a_1$ of the Hilbert polynomial (here $a_0 = 2, a_1 = 2$), then $\operatorname{reg}(\mathscr{F}) \leq F(2, 2)$, a fixed constant. But $\operatorname{reg}(\mathscr{F}) = k$ is unbounded, a contradiction.

**Key Insight:** The Hilbert polynomial only sees the Euler characteristic, which involves cancellation between $H^0$ and $H^1$. A sheaf can have large higher cohomology that is "hidden" by this cancellation, so the Hilbert polynomial alone cannot control regularity for arbitrary coherent sheaves.

**Prerequisites:** Castelnuovo-Mumford regularity, cohomology of line bundles on $\mathbb{P}^1$, Serre duality, Hilbert polynomial

<!-- BENCHMARK_PROBLEM: Let F = O_{P^1}(k) + O_{P^1}(-k) for k >= 0. Show that reg(F) = k, while the Hilbert polynomial of F is 2m + 2, independent of k. What does this imply about bounding regularity by Hilbert polynomial coefficients? -->

### Remark {#ecag-0193}

This example and the original regularity theorem for ideal sheaves can be found in Mumford's *Lectures on Curves on an Algebraic Surface* (Annals of Mathematics Studies, No. 59), specifically Lectures 14 and 15. Mumford proves that for an ideal sheaf $\mathscr{I}_X$ of a subvariety $X \subset \mathbb{P}^n$, the regularity can be bounded in terms of the Hilbert polynomial of $X$. The example above shows this bound fails for arbitrary coherent sheaves.

### Example: Some relations between (co)homology theories {#ecag-0194}

**Statement:** Several fundamental isomorphisms relate Borel-Moore homology, singular homology, and reduced homology:

1. $H_i^{BM}(X) \cong H_i(\hat{X}, \{*\})$, where $\hat{X} = X^+ = X \cup \{*\}$ is the one-point compactification of $X$.
2. $H_i^{BM}(X) \cong H_i(\overline{X}, \overline{X} \setminus X)$ for any compactification $\overline{X}$ of $X$.
3. $H_i(X, A) \cong \widetilde{H}_i(X/A)$ whenever $A$ is a closed subspace that is a deformation retract of some open neighborhood in $X$ (i.e., $(X, A)$ is a "good pair").

**Construction/Proof:** For (1): Borel-Moore homology of a locally compact space $X$ is defined using locally finite chains. By definition, these are precisely the chains in the one-point compactification $\hat{X}$ that are finite relative to the added point, yielding $H_i^{BM}(X) = H_i(\hat{X}, \{*\})$.

For (2): If $\overline{X}$ is any compactification, excision applied to $\overline{X} \setminus X$ (which is closed) gives $H_i(\overline{X}, \overline{X} \setminus X) \cong H_i(\hat{X}, \{*\})$, since collapsing $\overline{X} \setminus X$ to a point recovers the one-point compactification up to homotopy equivalence of pairs.

For (3): This is the standard excision/quotient theorem. If $A$ is a deformation retract of a neighborhood $U$ in $X$, then the quotient map $(X, A) \to (X/A, A/A)$ induces an isomorphism on relative homology, and $H_i(X/A, A/A) = \widetilde{H}_i(X/A)$ by definition of reduced homology.

**Key Insight:** Borel-Moore homology captures the homology "at infinity" by measuring cycles that are allowed to be non-compact but must be locally finite; the one-point compactification provides a clean way to encode this.

**Prerequisites:** Borel-Moore homology, singular homology, one-point compactification, excision theorem, good pairs

<!-- BENCHMARK_PROBLEM: Compute H_i^{BM}(R^n) for all i using the one-point compactification R^n_+ = S^n. Express the answer in terms of n. -->

### Example: Borel-Moore homology of $\mathbb{R}$ and  $\mathbb{R}^{2}\setminus\{0\}$ {#ecag-0195}

**Statement:** The Borel-Moore homology groups are:

$$
H_i^{BM}(\mathbb{R}^1) = \begin{cases} \mathbb{Z} & \text{if } i = 1, \\ 0 & \text{otherwise.} \end{cases}

$$

$$
H_i^{BM}(\mathbb{R}^2 \setminus \{0\}) = \begin{cases} \mathbb{Z} & \text{if } i = 1, 2, \\ 0 & \text{otherwise.} \end{cases}

$$

Moreover, the natural map $H_i(X) \to H_i^{BM}(X)$ is zero for $X = \mathbb{R}^2 \setminus \{0\}$.

**Construction/Proof:** Step 1: Compute $H_i^{BM}(\mathbb{R}^1)$. The one-point compactification of $\mathbb{R}$ is $S^1$, so:

$$
H_i^{BM}(\mathbb{R}^1) = H_i(S^1, \{*\}) = \widetilde{H}_i(S^1) = \begin{cases} \mathbb{Z} & \text{if } i = 1, \\ 0 & \text{otherwise.} \end{cases}

$$

Step 2: Compute $H_i^{BM}(\mathbb{R}^2 \setminus \{0\})$. The one-point compactification of $\mathbb{R}^2$ is $S^2$. Under the one-point compactification of $\mathbb{R}^2 \setminus \{0\}$, we adjoin a point at infinity $\infty$ to get $(S^2 \setminus \{0\}) \cup \{\infty\}$. However, by the relation $H_i^{BM}(X) = H_i(\overline{X}, \overline{X} \setminus X)$ with $\overline{X} = S^2$ as a compactification (where $S^2 \setminus (\mathbb{R}^2 \setminus \{0\}) = \{0, \infty\}$), we get:

$$
H_i^{BM}(\mathbb{R}^2 \setminus \{0\}) = H_i(S^2, \{0, \infty\}) \cong \widetilde{H}_i(S^2 / \{0, \infty\}).

$$

The space $S^2 / \{0, \infty\}$ is obtained by identifying the north and south poles of $S^2$, giving $S^2 \vee S^1$ (a sphere with a circle attached). Thus:

$$
\widetilde{H}_i(S^2 \vee S^1) = \widetilde{H}_i(S^2) \oplus \widetilde{H}_i(S^1) = \begin{cases} \mathbb{Z} & \text{if } i = 1, 2, \\ 0 & \text{otherwise.} \end{cases}

$$

Step 3: Compare with ordinary homology. The ordinary homology $H_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$, generated by a circle around the origin. In Borel-Moore homology, $H_1^{BM}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$, but a generator is given by a ray from $0$ to $\infty$ (a locally finite 1-chain). The circle that generates $H_1$ is actually a boundary in the Borel-Moore complex (it bounds the locally finite 2-chain consisting of one of the two half-planes it divides). Therefore the natural homomorphism $H_i(\mathbb{R}^2 \setminus \{0\}) \to H_i^{BM}(\mathbb{R}^2 \setminus \{0\})$ is zero for all $i$.

**Key Insight:** Borel-Moore homology detects "non-compact" cycles (like rays to infinity) that are invisible to ordinary homology, while compact cycles (like circles) that are non-trivial in ordinary homology can become boundaries when locally finite chains are allowed.

**Prerequisites:** Borel-Moore homology, one-point compactification, reduced homology, locally finite chains

<!-- BENCHMARK_PROBLEM: Compute H_i^{BM}(R^2 \ {0}) for all i using the one-point compactification method. Identify a generator of H_1^{BM} and explain why the circle generating H_1(R^2 \ {0}) maps to zero in H_1^{BM}. -->

### Remark {#ecag-0196}

Important properties and pathologies of Borel-Moore homology:

- **Not homotopy invariant.** For example, $H_1^{BM}(\mathbb{R}) \cong \mathbb{Z}$ while $H_1^{BM}(\{pt\}) = 0$, even though $\mathbb{R}$ is contractible.
- **No naive Poincare duality.** For non-compact manifolds, the usual Poincare duality $H_i(M) \cong H^{n-i}(M)$ fails. The correct statement involves Borel-Moore homology: $H_i^{BM}(M) \cong H^{n-i}(M)$ for an oriented $n$-manifold.
- **Proper pushforward only.** A continuous map $f: X \to Y$ does not in general induce $f_*: H_i^{BM}(X) \to H_i^{BM}(Y)$, because the image of a locally finite chain need not be locally finite. For example, the inclusion $\mathbb{R} \setminus \{0\} \hookrightarrow \mathbb{R}$ sends the locally finite chain $\sum_{i \geq 0} [1/2^{i+1}, 1/2^i]$, which is locally finite on $\mathbb{R} \setminus \{0\}$, to a chain that is not locally finite at $0 \in \mathbb{R}$. Proper maps do induce pushforwards.
- **Localization long exact sequence.** For a locally compact space $X$, a closed subset $Y \subset X$, and $U = X \setminus Y$, there is a long exact sequence:

$$
\cdots \rightarrow H_k^{BM}(Y) \rightarrow H_k^{BM}(X) \rightarrow H_k^{BM}(U) \rightarrow H_{k-1}^{BM}(Y) \rightarrow \cdots

$$

This follows from the long exact sequence of the triple $(\overline{X}, \overline{X} \setminus U, \overline{X} \setminus X)$ combined with Poincare-Lefschetz duality for Borel-Moore homology.

### Example: Poincar\'{e} duality {#ecag-0197}

**Statement:** Several versions of Poincare duality relate homology and cohomology:

1. **(Poincare-Lefschetz duality)** Let $X$ be a closed subset of a smooth, oriented manifold $M$ with $\dim_{\mathbb{R}}(M) = n$. Then:

$$
H_i^{BM}(X) \cong H^{n-i}(M, M \setminus X).

$$

In particular, for $X = M$:

$$
H_i^{BM}(M) \cong H^{n-i}(M).

$$

2. **(Lefschetz duality for manifolds with boundary)** Let $M$ be an oriented compact $n$-manifold with boundary $\partial M$. Then:

$$
H^k(M, \partial M) \cong H_{n-k}(M), \quad H_k(M) \cong H^{n-k}(M, \partial M).

$$

**Construction/Proof:** For (1): This is proved using the cap product with the fundamental class. The key input is the local computation: for any $x \in M$, the local homology $H_n(M, M \setminus \{x\}) \cong \mathbb{Z}$ by the orientation, and this assembles into a global duality pairing. When $X = M$ is closed and compact, $H_i^{BM}(M) = H_i(M)$, recovering classical Poincare duality.

Note the distinction between Poincare-Lefschetz duality $H_i^{BM}(X) \cong H^{n-i}(M, M \setminus X)$ and the definition $H_i^{BM}(X) = H_i(\overline{X}, \overline{X} \setminus X)$. The former requires $X$ to be embedded in a smooth manifold $M$; the latter is the general definition using any compactification. When $M$ is itself a compactification of $X$ (which implies $X$ is an open submanifold), combining the two gives:

$$
H^{n-i}(M, M \setminus X) \cong H_i(M, M \setminus X).

$$

For (2): Lefschetz duality for manifolds with boundary differs from the Borel-Moore setting. Here $\partial M$ is closed in $M$ (as the boundary), whereas in Borel-Moore theory, $M \setminus X$ is typically open. The proof uses the fundamental class $[M, \partial M] \in H_n(M, \partial M)$ and the cap product.

**Key Insight:** Poincare duality in its various forms converts homological information to cohomological information via the fundamental class; the correct version depends on whether the space is compact, has boundary, or is embedded in an ambient manifold.

**Prerequisites:** Poincare duality, Borel-Moore homology, cap product, fundamental class, manifolds with boundary, Lefschetz duality

<!-- BENCHMARK_PROBLEM: Let M be a smooth compact oriented manifold of dimension n without boundary. State the Poincare duality isomorphism. Then let X = M \ {p} for a point p. Compute H_i^{BM}(X) in terms of the homology of M and the local homology at p, using the Poincare-Lefschetz duality. -->

### Remark {#ecag-0198}

A comprehensive reference for intersection homology, including the construction of intersection homology groups with perversity conditions and the proof of generalized Poincare duality for singular spaces, is Maxim's lecture notes: [Intersection Homology](https://www.math.wisc.edu/~maxim/853notes.pdf). Intersection homology, introduced by Goresky and MacPherson, recovers Poincare duality for singular algebraic varieties by restricting the allowable chains according to a perversity function that controls how chains interact with the singular strata.

### Example: Perverse cohomology, perverse sheaf {#ecag-0199}

**Statement:** A perverse sheaf on a complex algebraic variety $X$ (with a fixed stratification $X = \bigsqcup_\alpha S_\alpha$) is an object $\mathcal{F}^\bullet$ in the bounded derived category $D^b_c(X, \mathbb{Q})$ of constructible sheaves satisfying two conditions:

1. **(Support condition)** $\dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathcal{F}^\bullet) \leq -j$ for all $j$.
2. **(Cosupport condition)** $\dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathbb{D}\mathcal{F}^\bullet) \leq -j$ for all $j$, where $\mathbb{D}$ is the Verdier duality functor.

The category $\operatorname{Perv}(X)$ of perverse sheaves is an abelian subcategory of $D^b_c(X)$, forming the heart of the perverse $t$-structure.

**Construction/Proof:** The perverse $t$-structure on $D^b_c(X)$ is defined by:

$$
{}^p D^{\leq 0} = \{\mathcal{F}^\bullet \mid \dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathcal{F}^\bullet) \leq -j \text{ for all } j\},

$$

$$
{}^p D^{\geq 0} = \{\mathcal{F}^\bullet \mid \dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathbb{D}\mathcal{F}^\bullet) \leq -j \text{ for all } j\}.

$$

The key example: if $X$ is smooth of dimension $d$, then a local system $\mathcal{L}$ on $X$ shifted by $d$ gives a perverse sheaf $\mathcal{L}[d]$. The shift is necessary because the support condition for $\mathcal{H}^j(\mathcal{L}[d])$ requires the stalk cohomology to vanish except in degree $-d$.

For a singular variety with strata $S_\alpha$ of dimension $d_\alpha$, the intersection cohomology complex $\operatorname{IC}(X, \mathcal{L})$ (where $\mathcal{L}$ is a local system on the smooth part) is the fundamental example of a perverse sheaf. It is characterized as the unique extension of $\mathcal{L}[\dim X]$ satisfying both the support and cosupport conditions.

The perverse cohomology functors ${}^p H^i: D^b_c(X) \to \operatorname{Perv}(X)$ are the cohomology functors associated to the perverse $t$-structure, analogous to ordinary cohomology sheaves $\mathcal{H}^i$ for the standard $t$-structure.

**Key Insight:** Perverse sheaves are not sheaves in the classical sense but complexes of sheaves satisfying dimensional conditions that ensure Verdier self-duality; the shift by dimension in the definition compensates for the dimension of the support, making the theory sensitive to the geometry of singularities.

**Prerequisites:** Derived category of constructible sheaves, Verdier duality, $t$-structures, stratifications, local systems, intersection cohomology

<!-- BENCHMARK_PROBLEM: Let X be a smooth complex variety of dimension d and let L be a local system on X. Show that L[d] is a perverse sheaf by verifying the support and cosupport conditions. What is the perverse cohomology {}^p H^0 of L[d]? -->

### Example: Intersection cohomology, Goresky-MacPherson {#ecag-0200}

**Statement:** Let $X$ be a (possibly singular) complex algebraic variety of pure dimension $n$, and let $\mathcal{L}$ be a local system on a smooth dense open subset $U \subset X$. The intersection cohomology groups $IH^k(X, \mathcal{L})$ are defined by:

$$
IH^k(X, \mathcal{L}) := H^{k-n}(X, \operatorname{IC}(X, \mathcal{L}))

$$

where $\operatorname{IC}(X, \mathcal{L})$ is the intersection cohomology complex (a perverse sheaf extending $\mathcal{L}[n]$). These groups satisfy generalized Poincare duality:

$$
IH^k(X, \mathcal{L}) \cong IH^{2n-k}(X, \mathcal{L}^\vee)^\vee.

$$

**Construction/Proof:** The intersection cohomology complex $\operatorname{IC}(X, \mathcal{L})$ is constructed by iterated truncation. Fix a Whitney stratification $X = \bigsqcup_\alpha S_\alpha$ with $U = S_0$ the open stratum. Let $U_k = \bigsqcup_{\dim S_\alpha \geq n - k} S_\alpha$ be the open subsets obtained by successively including strata of decreasing dimension, with inclusions $j_k: U_k \hookrightarrow U_{k+1}$. Then:

$$
\operatorname{IC}(X, \mathcal{L}) = \tau_{\leq -1} R(j_{n-1})_* \cdots \tau_{\leq -n+1} R(j_1)_* (\mathcal{L}[n]).

$$

Each truncation $\tau_{\leq p}$ at each stage enforces the support condition stratum by stratum. The resulting complex is independent of the choice of stratification and is Verdier self-dual (up to a shift and twist by $\mathcal{L}^\vee$), which gives the generalized Poincare duality.

For a concrete example, if $X$ is a curve with a node $p$, $U = X \setminus \{p\}$, and $\mathcal{L} = \mathbb{Q}_U$, then $\operatorname{IC}(X, \mathbb{Q})$ differs from $\mathbb{Q}_X[1]$ precisely at the node, where the stalk cohomology is corrected to restore Poincare duality. Specifically, $\mathcal{H}^{-1}(\operatorname{IC}(X))_p \cong \mathbb{Q}$ and $\mathcal{H}^{0}(\operatorname{IC}(X))_p = 0$ (the vanishing cycle at the node is killed).

**Key Insight:** Intersection cohomology restores Poincare duality on singular spaces by restricting which cycles are "allowable" near singular strata; the perversity condition is encoded algebraically through iterated truncation of the derived pushforward from the smooth part.

**Prerequisites:** Constructible sheaves, derived categories, Whitney stratifications, Verdier duality, truncation functors, local systems

<!-- BENCHMARK_PROBLEM: Let X be a projective curve with a single node p, and let U = X \ {p} be the smooth locus. Describe the stalk cohomology H^j(IC(X, Q))_p at the node for all j, and explain how it differs from the stalk cohomology of Q_X[1] at p. -->

### Example: Intersection cohomology {#ecag-0201}

**Statement:** Given a complex algebraic variety $Y$ of pure dimension $n$ and a local system $L$ on a smooth dense open subset $U \subset Y$, the intersection cohomology groups are defined as:

$$
IH^{n+k}(Y, L) := H^k(Y, \operatorname{IC}(Y, L))

$$

where $\operatorname{IC}(Y, L) \in D^b_c(Y)$ is the intersection cohomology complex, the unique (up to isomorphism) perverse sheaf extending $L[n]$ from $U$ to $Y$.

**Construction/Proof:** The indexing convention $IH^{n+k} = H^k(Y, \operatorname{IC}(Y, L))$ reflects the fact that $\operatorname{IC}(Y, L)$ lives in cohomological degrees $[-n, 0]$. The shift by $n$ ensures that when $Y$ is smooth and $L$ is constant, $IH^k(Y, \mathbb{Q}) = H^k(Y, \mathbb{Q})$ recovers ordinary cohomology. The key properties are:

1. **Poincare duality:** $IH^k(Y, L) \cong IH^{2n-k}(Y, L^\vee)^\vee$.
2. **Hard Lefschetz:** If $Y$ is projective, then cupping with the hyperplane class $\eta$ gives isomorphisms $\eta^j: IH^{n-j}(Y) \xrightarrow{\sim} IH^{n+j}(Y)$.
3. **Decomposition theorem (Beilinson-Bernstein-Deligne-Gabber):** For a proper morphism $f: X \to Y$ with $X$ smooth, $\mathbf{R}f_*\mathbb{Q}_X[n]$ decomposes as a direct sum of shifted intersection cohomology complexes of semisimple local systems on strata of $Y$.

**Key Insight:** The notation $IH^{n+*}$ normalizes intersection cohomology so that the fundamental class lives in the expected degree and Poincare duality takes the familiar form; the intersection cohomology complex $\operatorname{IC}$ is the unique "best" extension of a local system from the smooth locus to the singular variety.

**Prerequisites:** Perverse sheaves, intersection cohomology complex, derived categories, Poincare duality, decomposition theorem

<!-- BENCHMARK_PROBLEM: Let Y be a projective variety of dimension n with a single isolated singular point p, smooth elsewhere. If the link of p is a rational homology sphere, how does IH^k(Y, Q) compare to the ordinary cohomology H^k(Y, Q)? -->

### Example: (co)homology theories related to perverse sheaves {#ecag-0202}

**Statement:** The following (co)homology theories arise naturally in the study of the decomposition theorem and perverse sheaves. We summarize each and explain their interrelationships.

**Construction/Proof:**

1. **Ordinary (co)homology** $H^i(X, \mathbb{Z})$: Singular cohomology, computed via the derived global sections $\mathbf{R}\Gamma(X, \mathbb{Z}_X)$.

2. **Cohomology with support** $H_Y^i(X, \mathscr{F})$: For $Y \subset X$ closed, $H_Y^i(X, \mathscr{F}) = R^i\Gamma_Y(X, \mathscr{F})$ where $\Gamma_Y$ is the sections-with-support-in-$Y$ functor. Fits into the exact sequence $\cdots \to H_Y^i(X, \mathscr{F}) \to H^i(X, \mathscr{F}) \to H^i(X \setminus Y, \mathscr{F}) \to \cdots$.

3. **Borel-Moore homology** $H_i^{BM}(X, \mathbb{Z})$: Homology using locally finite chains. For $X$ an oriented $n$-manifold, $H_i^{BM}(X) \cong H^{n-i}(X)$. Related to compactly supported cohomology by $H_i^{BM}(X) \cong H_c^{2n-i}(X)^\vee$ for complex varieties.

4. **Cohomology with compact support** $H_c^i(X, \mathscr{L})$: Defined as $H^i(\overline{X}, j_!\mathscr{L})$ for any compactification $j: X \hookrightarrow \overline{X}$. Satisfies Poincare duality: $H_c^i(X) \cong H^{2n-i}(X)^\vee$ for smooth $X$ of dimension $n$.

5. **Stalk cohomology** $\mathcal{H}_x^i(A^\bullet) = H^i(A^\bullet_x)$: The cohomology of the stalk complex at $x$. Controls the support and cosupport conditions for perverse sheaves.

6. **Cohomology sheaf** $\mathcal{H}^i(A^\bullet)$: The sheafification of $U \mapsto H^i(\Gamma(U, A^\bullet))$. For constructible complexes, $\mathcal{H}^i(A^\bullet)$ is constructible.

7. **Hypercohomology** $\mathbb{H}^i(X, A^\bullet) = H^i(X, A^\bullet)$: The derived functor cohomology of a complex of sheaves. Computed via injective resolution: replace $A^\bullet$ by a quasi-isomorphic complex of injectives $I^\bullet$ and take $H^i(\Gamma(X, \operatorname{Tot}(I^{\bullet,\bullet})))$.

8. **Perverse cohomology** ${}^p H^i(A^\bullet)$: The cohomology functors of the perverse $t$-structure. For $A^\bullet \in D^b_c(X)$, ${}^p H^i(A^\bullet) \in \operatorname{Perv}(X)$. These are perverse sheaves, not classical sheaves.

9. **Intersection (co)homology** $IH_i^{\overline{p}}(X)$: Homology computed using only $\overline{p}$-allowable chains, where the perversity $\overline{p}$ controls how much a chain can intersect each singular stratum. For the middle perversity $\overline{m}$, this recovers the intersection cohomology complex $\operatorname{IC}(X)$.

10. **Relative intersection homology** $IH_i^{\overline{p}}(X, X \setminus \{x\}; \mathscr{L})$: The local intersection homology at a point $x$, which computes the stalk of the intersection cohomology complex and is determined by the topology of the link of $x$ in $X$.

**Key Insight:** These theories form a hierarchy: stalk cohomology is the local invariant, cohomology sheaves assemble these into a sheaf, hypercohomology globalizes, and perverse cohomology replaces the standard $t$-structure with one adapted to the geometry of singularities.

**Prerequisites:** Derived categories, constructible sheaves, Verdier duality, perverse $t$-structure, intersection homology, Borel-Moore homology

<!-- BENCHMARK_PROBLEM: For a smooth complex variety X of dimension n, express H^i_c(X, Q), H_i^{BM}(X, Q), and IH^i(X, Q) in terms of ordinary cohomology H^j(X, Q). Which of these theories are homotopy invariant? -->

### Example: Operations related to perverse sheaves {#ecag-0203}

**Statement:** The theory of perverse sheaves requires a collection of key operations and constructions. We list the most important ones with precise definitions.

**Construction/Proof:**

1. **Perversity.** A perversity is a function $\overline{p}: \{2, 3, \ldots\} \to \mathbb{Z}_{\geq 0}$ with $\overline{p}(2) = 0$ and $\overline{p}(k+1) \in \{\overline{p}(k), \overline{p}(k)+1\}$. The middle perversity is $\overline{m}(2k) = k-1$, $\overline{m}(2k+1) = k-1$. In the algebraic geometry convention (Beilinson-Bernstein-Deligne), the perversity is absorbed into the definition of the $t$-structure.

2. **Mapping cone.** For a morphism $f: A^\bullet \to B^\bullet$ in $D^b(X)$, the mapping cone $\operatorname{Cone}(f)$ fits in a distinguished triangle $A^\bullet \xrightarrow{f} B^\bullet \to \operatorname{Cone}(f) \xrightarrow{[1]} A^\bullet[1]$.

3. **Link.** For a point $x$ in a stratified space $X$, the link $L_x$ is the boundary of a small normal slice to the stratum through $x$. The local topology of $X$ near $x$ is modeled on $\operatorname{cone}(L_x) \times \mathbb{R}^{d}$ where $d = \dim S_\alpha$.

4. **Injective resolution of a complex.** For $A^\bullet \in D^b(X)$, an injective resolution is a quasi-isomorphism $A^\bullet \xrightarrow{\sim} I^\bullet$ where each $I^k$ is injective. One can use Godement resolutions or flasque resolutions in practice.

5. **Support/cosupport conditions.** $A^\bullet \in {}^pD^{\leq 0}$ iff $\dim \operatorname{supp} \mathcal{H}^j(A^\bullet) \leq -j$ for all $j$. The cosupport condition uses Verdier dual $\mathbb{D}A^\bullet$.

6. **Perverse truncation functors** ${}^p\tau_{\leq n}, {}^p\tau_{\geq n}$: These are the truncation functors for the perverse $t$-structure. For any $A^\bullet \in D^b_c(X)$, there is a distinguished triangle ${}^p\tau_{\leq n} A^\bullet \to A^\bullet \to {}^p\tau_{\geq n+1} A^\bullet \xrightarrow{[1]}$, and ${}^p H^n(A^\bullet) = {}^p\tau_{\leq n} {}^p\tau_{\geq n} A^\bullet$.

7. **Derived pushforward $Rj_*\mathscr{L}$.** For $j: U \hookrightarrow X$ an open inclusion and $\mathscr{L}$ a local system on $U$, $Rj_*\mathscr{L}$ is a complex of sheaves on $X$ whose stalk cohomology at $x \in X \setminus U$ computes $H^*(L_x, \mathscr{L})$.

8. **Perverse functors ${}^p j_*, {}^p j_!$.** These are the intermediate extensions: ${}^p j_{!*}\mathcal{F} = \operatorname{Im}({}^p H^0(j_!\mathcal{F}) \to {}^p H^0(Rj_*\mathcal{F}))$ for $\mathcal{F} \in \operatorname{Perv}(U)$.

9. **Intersection cohomology complex $\operatorname{IC}(X, \mathscr{L})$.** The intermediate extension $j_{!*}(\mathscr{L}[\dim X])$ where $j: U \hookrightarrow X$ is the smooth locus. It is the unique perverse sheaf extending $\mathscr{L}[\dim X]$ with no sub- or quotient-objects supported on $X \setminus U$.

**Key Insight:** The perverse $t$-structure recalibrates the notion of "truncation" to be sensitive to the dimension of supports, so that the resulting heart (perverse sheaves) captures the geometry of singularities in a way that the standard $t$-structure cannot.

**Prerequisites:** Derived categories, $t$-structures, constructible sheaves, Verdier duality, stratified spaces, intermediate extension

<!-- BENCHMARK_PROBLEM: Let j: U -> X be the inclusion of the smooth locus of a variety X. Define the intermediate extension functor j_{!*} and explain why IC(X, L) = j_{!*}(L[dim X]) has no nontrivial sub-objects or quotient-objects supported on X \ U in the category Perv(X). -->

### Example: $j_{*}, j_{!}$ {#ecag-0204}

**Statement:** The functors $j_*$ (direct image) and $j_!$ (extension by zero / proper direct image) appear in several categorical contexts with related but distinct meanings. We catalog the main appearances and their relationships.

**Construction/Proof:**

*In ordinary sheaf theory:* For an open inclusion $j: U \hookrightarrow X$, $j_*\mathscr{F}$ is the direct image sheaf: $(j_*\mathscr{F})(V) = \mathscr{F}(V \cap U)$. The functor $j_!$ is extension by zero: $(j_!\mathscr{F})(V) = \{s \in \mathscr{F}(V \cap U) \mid \operatorname{supp}(s) \text{ is closed in } V\}$. There is a natural inclusion $j_!\mathscr{F} \hookrightarrow j_*\mathscr{F}$.

*Higher derived functors:* $R^k j_*\mathscr{F}$ is the sheafification of $V \mapsto H^k(V \cap U, \mathscr{F})$. For $j$ an open immersion, $j_!$ is exact, so $R^k j_! = 0$ for $k > 0$. The total derived functors $Rj_*$ and $Rj_!$ live in the derived category.

*In the derived category:* For $A^\bullet \in D^b_c(U)$, $Rj_*A^\bullet$ and $j_! A^\bullet$ (which equals $Rj_! A^\bullet$ for open $j$) are related by Verdier duality: $\mathbb{D}(Rj_*A^\bullet) \cong j_!(\mathbb{D}A^\bullet)$.

*Key exact sequences:* For $j: U \hookrightarrow X$ open with complement $i: Z \hookrightarrow X$ closed:

$$
0 \to j_! j^* \mathscr{F} \to \mathscr{F} \to i_* i^* \mathscr{F} \to 0

$$

for any sheaf $\mathscr{F}$ on $X$. In the derived category, there are distinguished triangles:

$$
j_! j^* A^\bullet \to A^\bullet \to Ri_* i^* A^\bullet \xrightarrow{[1]}

$$

$$
i_* i^! A^\bullet \to A^\bullet \to Rj_* j^* A^\bullet \xrightarrow{[1]}.

$$

*In $K$-theory:* For a proper morphism $f$, $f_!: K_0(X) \to K_0(Y)$ is the $K$-theoretic pushforward defined by $f_!([\mathscr{F}]) = \sum (-1)^i [R^i f_*\mathscr{F}]$. This requires properness (or compact support) for well-definedness.

**Key Insight:** The functor $j_!$ is the "minimal" extension (extending by zero outside $U$) while $j_*$ is the "maximal" extension (taking all sections); the intermediate extension $j_{!*}$ in the perverse setting interpolates between them.

**Prerequisites:** Sheaf theory, open/closed immersions, derived categories, Verdier duality, $K$-theory, proper pushforward

<!-- BENCHMARK_PROBLEM: Let j: U -> X be an open immersion with closed complement i: Z -> X. Write down the two distinguished triangles relating j_!, j^*, Rj_*, i_*, i^*, Ri_*, i^! in the derived category. Verify they are compatible with Verdier duality. -->

### Example: Leray spectral sequence doesn't degenerate {#ecag-0205}

**Statement:** The Leray spectral sequence does not always degenerate, even for fibrations. In the holomorphic (non-algebraic) setting, there exist smooth proper morphisms $f: X \to Y$ of complex manifolds for which the Leray spectral sequence

$$
E_2^{p,q} = H^p(Y, R^q f_* \underline{\mathbb{Q}}) \Rightarrow H^{p+q}(X, \underline{\mathbb{Q}})

$$

fails to degenerate at $E_2$.

**Construction/Proof:** Consider the Hopf surface $X = (\mathbb{C}^2 \setminus \{0\}) / \langle z \mapsto 2z \rangle$. This is a compact complex surface that fibers over $\mathbb{P}^1$ via the natural projection $f: X \to \mathbb{P}^1$. The fibers are elliptic curves (tori), but $X$ is not Kahler (it has $b_1 = 1$, which is odd, impossible for a compact Kahler manifold). The Leray spectral sequence for $f$ does not degenerate at $E_2$: we have $H^1(X, \mathbb{Q}) \cong \mathbb{Q}$, but $E_2^{1,0} \oplus E_2^{0,1} = H^1(\mathbb{P}^1, \mathbb{Q}) \oplus H^0(\mathbb{P}^1, R^1 f_* \mathbb{Q})$ would give a different answer if the spectral sequence degenerated.

More generally, the non-degeneracy can occur for any holomorphic fiber bundle where the total space is not Kahler. The crucial point is that Deligne's degeneration theorem requires the morphism to be algebraic (or at least that the total space admits a Kahler metric), not merely holomorphic.

**Key Insight:** Deligne's theorem on degeneration of the Leray spectral sequence for smooth projective morphisms of algebraic varieties is fundamentally an algebraic (or Kahler) result; it relies on the Hard Lefschetz theorem applied fiberwise, which requires a Kahler class and fails in the purely holomorphic setting.

**Prerequisites:** Leray spectral sequence, Hodge theory, Kahler manifolds, Hopf surface, Deligne's degeneration theorem

<!-- BENCHMARK_PROBLEM: The Hopf surface X = (C^2 \ {0}) / <z -> 2z> fibers over P^1 with elliptic curve fibers. Explain why X is not Kahler (compute b_1), and use this to argue that the Leray spectral sequence for f: X -> P^1 cannot degenerate at E_2. -->

### Remark {#ecag-0206}

Deligne's degeneration theorem (1968) states that if $f: X \to Y$ is a smooth projective morphism of algebraic varieties over $\mathbb{C}$, then the Leray spectral sequence degenerates at $E_2$:

$$
E_2^{p,q} = H^p(Y, R^q f_* \underline{\mathbb{Q}}) \Rightarrow H^{p+q}(X, \underline{\mathbb{Q}}).

$$

The proof uses the Hard Lefschetz theorem on the fibers to construct a splitting. More precisely, a relative ample class $\eta \in H^2(X, \mathbb{Q})$ acts on $R^q f_*\mathbb{Q}$ via the Lefschetz operator, and the resulting decomposition $R^q f_*\mathbb{Q} \cong \bigoplus_j \mathcal{L}_j$ into primitive parts gives the splitting of the spectral sequence. This result was later vastly generalized by the decomposition theorem of Beilinson-Bernstein-Deligne-Gabber (1982), which handles arbitrary proper morphisms (allowing singular fibers) using perverse sheaves and intersection cohomology.

### Example: Pathologies of non-abelian categories {#ecag-0207}

**Statement:** Certain basic properties of abelian categories fail in non-abelian (additive but not abelian) categories. The following three pathologies illustrate this.

**Construction/Proof:**

1. **Kernels may not exist.** Consider the category of finitely generated modules over $R = k[x_1, x_2, \ldots]$ (a polynomial ring in infinitely many variables). The kernel of the natural projection $\pi: R \to k = R/(x_1, x_2, \ldots)$ is the ideal $(x_1, x_2, \ldots)$, which is not finitely generated as an $R$-module. Therefore, in the category of finitely generated $R$-modules, $\ker(\pi)$ does not exist.

2. **Cokernels may not exist.** Consider the category of free abelian groups. The map $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$ has cokernel $\mathbb{Z}/2\mathbb{Z}$ in the category of all abelian groups, but $\mathbb{Z}/2\mathbb{Z}$ is not free. No free abelian group satisfies the universal property of the cokernel, so the cokernel does not exist in this subcategory.

3. **Vanishing of kernel and cokernel does not imply isomorphism.** In the category of filtered vector spaces (with morphisms preserving filtrations), a morphism can have zero kernel and zero cokernel without being an isomorphism. For example, let $V = k$ with filtration $F^0 V = V, F^1 V = 0$, and $W = k$ with filtration $F^0 W = W, F^1 W = W$. The identity map $\operatorname{id}: V \to W$ has trivial kernel and cokernel as a map of filtered spaces, but it is not an isomorphism of filtered vector spaces (the inverse does not preserve the filtration).

**Key Insight:** These pathologies show why the axioms of an abelian category (existence of all kernels and cokernels, and the condition that every monomorphism is a kernel and every epimorphism is a cokernel) are precisely what is needed for homological algebra to function.

**Prerequisites:** Abelian categories, kernels and cokernels, finitely generated modules, free abelian groups, filtered vector spaces

<!-- BENCHMARK_PROBLEM: In the category of free abelian groups, show that the multiplication-by-2 map Z -> Z has no cokernel. Prove this by showing that no free abelian group satisfies the universal property of the cokernel. -->

### Example: Exactness depends on the ambient abelian category {#ecag-0208}

**Statement:** The Euler sequence on $\mathbb{P}^1$:

$$
0 \rightarrow \mathcal{O}(-2) \rightarrow \mathcal{O}(-1) \oplus \mathcal{O}(-1) \rightarrow \mathcal{O} \rightarrow 0

$$

is exact in the category of sheaves of $\mathcal{O}_{\mathbb{P}^1}$-modules, but it is not exact in the category of presheaves on $\mathbb{P}^1$.

**Construction/Proof:** The Euler sequence on $\mathbb{P}^n$ is $0 \to \Omega^1_{\mathbb{P}^n}(1) \to \mathcal{O}^{n+1} \to \mathcal{O}(1) \to 0$. For $\mathbb{P}^1$, twisting by $\mathcal{O}(-1)$ gives the sequence above, since $\Omega^1_{\mathbb{P}^1} \cong \mathcal{O}(-2)$.

Exactness as sheaves is checked on stalks: at each point $p \in \mathbb{P}^1$, the stalk sequence is exact. However, exactness as presheaves would require that for every open set $U$, the sequence of sections

$$
0 \to \mathcal{O}(-2)(U) \to (\mathcal{O}(-1) \oplus \mathcal{O}(-1))(U) \to \mathcal{O}(U) \to 0

$$

is exact. Consider $U = \mathbb{P}^1$ itself. Then $\mathcal{O}(-2)(\mathbb{P}^1) = 0$, $(\mathcal{O}(-1) \oplus \mathcal{O}(-1))(\mathbb{P}^1) = 0$, and $\mathcal{O}(\mathbb{P}^1) = k$. So the sequence of global sections is $0 \to 0 \to 0 \to k \to 0$, which is not exact (the map to $k$ is not surjective). Thus the last map in the presheaf sequence is not surjective on global sections.

The discrepancy arises because sheafification is needed: the surjection $\mathcal{O}(-1)^2 \to \mathcal{O}$ is surjective on stalks (equivalently, locally surjective), but not surjective as a presheaf map. Sheafification is an exact functor that turns locally surjective presheaf maps into surjective sheaf maps.

**Key Insight:** Exactness of a sequence of sheaves is a local condition (checked on stalks), while exactness of presheaves is a global condition (checked on sections over every open set). Sheafification bridges the gap, but the two notions of exactness are genuinely different.

**Prerequisites:** Sheaves and presheaves, Euler sequence on projective space, sheafification, cohomology of line bundles on $\mathbb{P}^1$

<!-- BENCHMARK_PROBLEM: Show that the surjection O(-1)^2 -> O on P^1 is not surjective as a map of presheaves by computing global sections of both sides. Explain what property of sheafification resolves this. -->

### Example: Derived functors and derived categories {#ecag-0209}

**Statement:** Derived categories provide a framework for working with derived functors systematically. We illustrate the basic ideas through examples and computations.

**Construction/Proof:** The derived category $D^b(\mathcal{A})$ of a bounded complex of objects in an abelian category $\mathcal{A}$ is constructed in two steps:

Step 1: Form the homotopy category $K^b(\mathcal{A})$ by identifying chain-homotopic morphisms.

Step 2: Formally invert quasi-isomorphisms (maps inducing isomorphisms on cohomology) to obtain $D^b(\mathcal{A})$.

A left-exact functor $F: \mathcal{A} \to \mathcal{B}$ has a right derived functor $\mathbf{R}F: D^+(\mathcal{A}) \to D^+(\mathcal{B})$ computed by replacing an object (or complex) by an injective resolution and applying $F$ termwise. The key property: $R^i F(A) = H^i(\mathbf{R}F(A))$.

Example: For the global sections functor $\Gamma(X, -): \operatorname{Sh}(X) \to \operatorname{Ab}$, the derived functor $\mathbf{R}\Gamma(X, \mathcal{F})$ is the complex whose $i$-th cohomology is $H^i(X, \mathcal{F})$.

For explicit computations of derived categories of finite-dimensional algebras, tilting theory provides a powerful tool. If $\mathcal{A} = \operatorname{mod}(A)$ for a finite-dimensional algebra $A$, and $T$ is a tilting module, then $D^b(\operatorname{mod}(A)) \cong D^b(\operatorname{mod}(\operatorname{End}(T)))$. This gives explicit equivalences between derived categories of different abelian categories.

References: *Explicit Derived Categories* (Utah lecture notes), Cald$\breve{\text{a}}$r$\breve{\text{a}}$ru's *Derived Categories of Sheaves: A Skimming*.

**Key Insight:** The derived category remembers the "higher order" information lost when passing to cohomology, and derived functors are the correct way to extend functors that are only exact on one side to the entire derived category.

**Prerequisites:** Abelian categories, chain complexes, quasi-isomorphisms, injective resolutions, derived functors, tilting theory

<!-- BENCHMARK_PROBLEM: Let A = k[x]/(x^2) and let T = k[x]/(x^2) + k be the direct sum of the regular module and the simple module. Verify that T is a tilting module for A and identify End(T). What does the derived equivalence D^b(mod(A)) = D^b(mod(End(T))) give? -->

### Example: Non-isomorphic abelian categories, isomorphic derived categories {#ecag-0210}

**Statement:** There exist abelian categories $\mathcal{A}$ and $\mathcal{B}$ that are not equivalent as abelian categories, yet whose bounded derived categories $D^b(\mathcal{A}) \cong D^b(\mathcal{B})$ are equivalent as triangulated categories. Such categories are called *derived equivalent*.

**Construction/Proof:** The simplest example comes from tilting theory. Let $A$ be the path algebra of the quiver $1 \to 2$ over a field $k$. Then $\operatorname{mod}(A)$ is the category of representations of $1 \to 2$, which has two simples $S_1, S_2$ and one indecomposable $P_1 = \begin{smallmatrix} 1 \\ 2 \end{smallmatrix}$.

Let $B$ be the path algebra of the quiver $2 \leftarrow 1$ (the opposite quiver). Then $\operatorname{mod}(A) \not\cong \operatorname{mod}(B)$ as abelian categories (the Auslander-Reiten quivers differ), but the tilting module $T = S_2 \oplus P_1$ for $A$ satisfies $\operatorname{End}_A(T) \cong B$, giving an equivalence $D^b(\operatorname{mod}(A)) \cong D^b(\operatorname{mod}(B))$.

A more geometric example: Mukai showed that for an abelian variety $A$ over $\mathbb{C}$, $D^b(\operatorname{Coh}(A)) \cong D^b(\operatorname{Coh}(\hat{A}))$, where $\hat{A}$ is the dual abelian variety. For a generic abelian variety, $A \not\cong \hat{A}$, so $\operatorname{Coh}(A) \not\cong \operatorname{Coh}(\hat{A})$, yet they have equivalent derived categories. The equivalence is given by the Fourier-Mukai transform with kernel the Poincare bundle $\mathcal{P}$ on $A \times \hat{A}$.

**Key Insight:** Derived equivalence is strictly weaker than abelian equivalence; the derived category forgets some of the "abelian" structure (like which sequences are short exact) while retaining enough information for most cohomological computations.

**Prerequisites:** Derived categories, tilting theory, path algebras of quivers, Fourier-Mukai transform, abelian varieties

<!-- BENCHMARK_PROBLEM: Let A be the path algebra of the quiver 1 -> 2 over a field k. Find a tilting module T in mod(A) such that End(T) is isomorphic to the path algebra B of the quiver 2 -> 1 (the opposite quiver). Verify that T has projective dimension at most 1 and generates D^b(mod(A)). -->

### Example: $\mathbf{R}\Gamma(X, \mathscr{F}), \mathbf{R}\Gamma(A^{\bullet}), \mathbf{R}f_{*}(\mathscr{F}), \mathbf{R}f_{*}(A^{\bullet})$ {#ecag-0211}

**Statement:** The derived global sections functor $\mathbf{R}\Gamma$ and the derived pushforward $\mathbf{R}f_*$ are the two fundamental derived functors in sheaf theory. We describe their construction and key properties for both single sheaves and complexes.

**Construction/Proof:**

*Derived global sections of a sheaf:* For $\mathscr{F}$ a sheaf on $X$, choose an injective resolution $\mathscr{F} \xrightarrow{\sim} I^\bullet$. Then $\mathbf{R}\Gamma(X, \mathscr{F}) = \Gamma(X, I^\bullet)$ is a complex of abelian groups with $H^i(\mathbf{R}\Gamma(X, \mathscr{F})) = H^i(X, \mathscr{F})$.

*Derived global sections of a complex:* For $A^\bullet \in D^b(X)$, choose a quasi-isomorphism $A^\bullet \xrightarrow{\sim} I^\bullet$ where $I^\bullet$ is a complex of injectives (using Cartan-Eilenberg resolution or the existence of enough injectives). Then $\mathbf{R}\Gamma(X, A^\bullet) = \Gamma(X, I^\bullet)$, and $H^i(\mathbf{R}\Gamma(X, A^\bullet)) = \mathbb{H}^i(X, A^\bullet)$ is the hypercohomology.

*Derived pushforward of a sheaf:* For $f: X \to Y$ a morphism and $\mathscr{F}$ a sheaf on $X$, $\mathbf{R}f_*\mathscr{F}$ is computed by $f_*(I^\bullet)$ for an injective resolution $\mathscr{F} \to I^\bullet$. The cohomology sheaves are $\mathcal{H}^i(\mathbf{R}f_*\mathscr{F}) = R^i f_*\mathscr{F}$.

*Derived pushforward of a complex:* For $A^\bullet \in D^b(X)$, $\mathbf{R}f_*(A^\bullet)$ is computed via injective replacement, and $\mathcal{H}^i(\mathbf{R}f_* A^\bullet)$ is the sheaf associated to $V \mapsto \mathbb{H}^i(f^{-1}(V), A^\bullet|_{f^{-1}(V)})$.

*Composition:* $\mathbf{R}\Gamma(Y, -) \circ \mathbf{R}f_* \cong \mathbf{R}\Gamma(X, -)$, which at the level of cohomology recovers the Leray spectral sequence $E_2^{p,q} = H^p(Y, R^q f_* \mathscr{F}) \Rightarrow H^{p+q}(X, \mathscr{F})$.

*Projection formula:* For $f: X \to Y$ proper and $\mathscr{F} \in D^b(X)$, $\mathscr{G} \in D^b(Y)$: $\mathbf{R}f_*(\mathscr{F} \otimes^L f^*\mathscr{G}) \cong \mathbf{R}f_*\mathscr{F} \otimes^L \mathscr{G}$.

**Key Insight:** Working with derived functors on complexes (rather than just single sheaves) is essential because many natural constructions (like intersection cohomology complexes or perverse sheaves) are inherently complexes of sheaves, and the derived category provides the correct framework for composition and base change.

**Prerequisites:** Derived categories, injective resolutions, hypercohomology, Leray spectral sequence, projection formula

<!-- BENCHMARK_PROBLEM: Let f: X -> Y be a proper morphism of smooth projective varieties and F a coherent sheaf on X flat over Y. State the base change theorem relating the fiber (R^i f_* F)_y to H^i(X_y, F|_{X_y}), and give a condition under which the base change map is an isomorphism. -->

### Remark: Derived functors(in derived categories, to get a complex), spectral sequence, hypercohomology {#ecag-0212}

The relationship between derived functors, spectral sequences, and hypercohomology is as follows.

Given a left-exact functor $F: \mathcal{A} \to \mathcal{B}$ between abelian categories (with $\mathcal{A}$ having enough injectives), the derived functor $\mathbf{R}F: D^+(\mathcal{A}) \to D^+(\mathcal{B})$ produces a complex in $D^+(\mathcal{B})$, not just a single object. The individual cohomology objects $R^i F(A) = H^i(\mathbf{R}F(A))$ are the classical derived functors.

When applied to a complex $A^\bullet$ (rather than a single object), the derived functor $\mathbf{R}F(A^\bullet)$ gives rise to two spectral sequences:

$$
{}^{I}E_2^{p,q} = R^p F(\mathcal{H}^q(A^\bullet)) \Rightarrow H^{p+q}(\mathbf{R}F(A^\bullet))

$$

$$
{}^{II}E_2^{p,q} = \mathcal{H}^p(\mathbf{R}F(A^q)) \Rightarrow H^{p+q}(\mathbf{R}F(A^\bullet))

$$

The target $H^n(\mathbf{R}F(A^\bullet))$ is called the **hypercohomology** $\mathbb{H}^n(A^\bullet)$ (when $F = \Gamma(X, -)$ is the global sections functor). The first spectral sequence is the Grothendieck spectral sequence for the composition of derived functors, while the second comes from the double complex obtained by applying $F$ to an injective Cartan-Eilenberg resolution of $A^\bullet$.

<!-- BENCHMARK_PROBLEM: Let A^* be a two-term complex F -> G of coherent sheaves on a projective variety X. Write out the first spectral sequence converging to the hypercohomology H^n(X, A^*) and identify the E_2 terms explicitly in terms of H^i(X, F) and H^i(X, G). -->

### Example: Perverse truncation and perverse cohomology {#ecag-0213}

**Statement:** For smooth algebraic varieties over $\mathbb{C}$, the perverse truncation reduces to the ordinary truncation (shifted by dimension). For a variety with two strata $X = U \sqcup Z$ (where $j: U \hookrightarrow X$ is open, $i: Z \hookrightarrow X$ is closed), the perverse truncation can be described explicitly by gluing the standard $t$-structures on $U$ and $Z$.

**Construction/Proof:** Step 1: On a smooth variety $X$ of dimension $d$, a constructible complex $A^\bullet$ is in ${}^p D^{\leq 0}$ if and only if $A^\bullet[-d]$ is in the standard $D^{\leq 0}$, i.e., $\mathcal{H}^j(A^\bullet) = 0$ for $j > -d$. Thus the perverse $t$-structure on a smooth variety is just the standard $t$-structure shifted by $\dim X$, and perverse sheaves on $X$ are just local systems shifted by $d$.

Step 2: For $X = U \sqcup Z$ with $\dim U = n$ and $\dim Z = m$, the perverse $t$-structure on $X$ is obtained by gluing. An object $A^\bullet \in D^b_c(X)$ is in ${}^p D^{\leq 0}$ if and only if:
- $j^* A^\bullet \in D^{\leq -n}(U)$ (i.e., $\mathcal{H}^k(j^* A^\bullet) = 0$ for $k > -n$), and
- $i^* A^\bullet \in D^{\leq -m}(Z)$ (i.e., $\mathcal{H}^k(i^* A^\bullet) = 0$ for $k > -m$).

Step 3: The perverse truncation ${}^p\tau_{\leq 0} A^\bullet$ is constructed via the distinguished triangle:

$$
{}^p\tau_{\leq 0} A^\bullet \to A^\bullet \to {}^p\tau_{\geq 1} A^\bullet \xrightarrow{[1]}

$$

In the two-strata case, this can be computed explicitly. Let $A^\bullet \in D^b_c(X)$. Apply $j^*$ and compute the standard truncation $\tau_{\leq -n}(j^* A^\bullet)$ on $U$. The perverse truncation on $X$ is then obtained by the fiber sequence:

$$
{}^p\tau_{\leq 0} A^\bullet \to \tau_{\leq -m}(A^\bullet) \to i_* \tau_{\leq -m}(i^* \operatorname{Cone}(\tau_{\leq -n} Rj_* j^* A^\bullet \to A^\bullet)).

$$

The perverse cohomology ${}^p H^0(A^\bullet) = {}^p\tau_{\leq 0} {}^p\tau_{\geq 0} A^\bullet$ is a perverse sheaf that, in the two-strata case, encodes how the cohomology of $A^\bullet$ on $U$ extends across $Z$.

**Key Insight:** The perverse $t$-structure is obtained by shifting the standard $t$-structure differently on each stratum (by the dimension of that stratum), then gluing; this dimension-dependent shift is what allows perverse sheaves to detect singularities.

**Prerequisites:** $t$-structures, gluing of $t$-structures, constructible sheaves, stratified spaces, distinguished triangles

<!-- BENCHMARK_PROBLEM: Let X be a variety with stratification X = U ∪ Z where U is smooth open of dimension 2 and Z is a smooth closed point. For the constant sheaf complex Q_X[2], compute the perverse cohomology {}^p H^0(Q_X[2]) by checking the support and cosupport conditions. Is Q_X[2] perverse? -->

### Example: $H^{0}(N_{Z/X})\neq H^{0}(N_{Z/X}|_{Z})$ {#ecag-0214}

**Statement:** The global sections of the normal sheaf $\mathcal{N}_{Z/X} = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{I}_Z/\mathcal{I}_Z^2, \mathcal{O}_X)$, viewed as an $\mathcal{O}_X$-module, can differ dramatically from the global sections of the restricted normal sheaf $\mathcal{N}_{Z/X}|_Z = \mathcal{H}om_{\mathcal{O}_Z}(\mathcal{I}_Z/\mathcal{I}_Z^2, \mathcal{O}_Z)$. The latter is the tangent space to the Hilbert scheme.

**Construction/Proof:** Step 1: A basic example. Let $R = \mathbb{C}[x]$ and $I = (x)$. Then $I/I^2 \cong R/I \cong \mathbb{C}$ as an $R$-module, generated by the class of $x$. We compute:

$$
\operatorname{Hom}_R(I/I^2, R) = 0.

$$

Indeed, for any $f \in \operatorname{Hom}_R(I/I^2, R)$, we have $f(\bar{x}) \in R$ and $x \cdot f(\bar{x}) = f(x \cdot \bar{x}) = f(\bar{x^2}) = f(0) = 0$ (since $x^2 \in I^2$), so $f(\bar{x}) = 0$ because $R$ is a domain. This shows that as an $R$-module, $(I/I^2)^\vee = 0$, even though $\dim_\mathbb{C}(I/I^2) = 1$.

Step 2: However, restricting to $R/I$:

$$
\operatorname{Hom}_{R/I}(I/I^2, R/I) = \operatorname{Hom}_\mathbb{C}(\mathbb{C}, \mathbb{C}) \cong \mathbb{C}.

$$

Step 3: Application to Hilbert schemes. The Zariski tangent space to the Hilbert scheme at a point $[Z] \in \operatorname{Hilb}(X)$ is:

$$
T_Z \operatorname{Hilb}(X) = \operatorname{Hom}_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{O}_Z) = \operatorname{Hom}_{\mathcal{O}_Z}(\mathcal{I}_Z/\mathcal{I}_Z^2, \mathcal{O}_Z) = H^0(\mathcal{N}_{Z/X}|_Z).

$$

Note that this is $\operatorname{Hom}$ over $\mathcal{O}_Z$ (not $\mathcal{O}_X$), which is the restricted normal sheaf.

Step 4: When $X$ is smooth of dimension 1 and $Z$ is a 0-dimensional subscheme, Serre duality gives:

$$
T_Z \operatorname{Hilb}(X) = H^0(\Omega_X^1 \otimes \mathcal{O}_Z)^\vee.

$$

Step 5: For $I = (x^n) \subset \mathbb{C}[x]$, we have $\Omega_X^1 \otimes \mathcal{O}_Z \cong \mathbb{C}[x]/(x^n)$ with basis $\{x, x^2, \ldots, x^n\}$ as a torus representation ($\mathbb{C}^*$ acts by $x \mapsto tx$). Thus:

$$
T_{(x^n)} \operatorname{Hilb}^n(\mathbb{C}) = t + t^2 + \cdots + t^n

$$

as a torus representation. This agrees with the global coordinates on $\operatorname{Hilb}^n(\mathbb{C}) \cong \mathbb{C}^n$ given by $(a_1, \ldots, a_n)$ where:

$$
I = (f), \quad f = x^n + a_1 x^{n-1} + \cdots + a_n.

$$

The weight of $a_i$ under $x \mapsto tx$ is $t^i$, confirming the torus representation.

**Key Insight:** The distinction between $\operatorname{Hom}_{\mathcal{O}_X}$ and $\operatorname{Hom}_{\mathcal{O}_Z}$ is crucial: the former sees the $\mathcal{O}_X$-module structure of the target (where torsion can kill everything), while the latter restricts to $Z$ first and computes the tangent space to the Hilbert scheme.

**Prerequisites:** Normal sheaf, Hilbert scheme, Zariski tangent space, Serre duality, torus representations

<!-- BENCHMARK_PROBLEM: Let R = C[x], I = (x^n). Compute Hom_R(I/I^2, R) and Hom_{R/I}(I/I^2, R/I) as C-vector spaces. What are their dimensions? Use this to find the dimension of the Zariski tangent space T_{(x^n)} Hilb^n(C). -->
