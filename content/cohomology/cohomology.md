---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/cohomology.tex
---

## Cohomology and homological algebra

### Example: Serre's computation of sheaf cohomology on projective space {#ecag-0184}

Let $X = \mathbb{P}^n_k$ and consider the standard affine cover $\mathfrak{U} = \{U_i = D_+(x_i)\}_{i=0}^{n}$. Since each finite intersection $U_{i_0} \cap \cdots \cap U_{i_p} = \operatorname{Spec}(k[x_0/x_{i_0}, \ldots, x_n/x_{i_0}]_{x_{i_1}/x_{i_0} \cdots x_{i_p}/x_{i_0}})$ is affine, and higher sheaf cohomology of quasi-coherent sheaves on affine schemes vanishes, the Leray theorem for acyclic covers gives

$$
\check{H}^i(\mathfrak{U}, \mathcal{F}) \cong H^i(X, \mathcal{F})
$$

for any quasi-coherent sheaf $\mathcal{F}$ on $\mathbb{P}^n_k$.

For $\mathcal{F} = \mathcal{O}(m)$, the Cech complex on this cover is

$$
0 \rightarrow \bigoplus_{i} (S_{x_i})_m \rightarrow \bigoplus_{i < j} (S_{x_i x_j})_m \rightarrow \cdots \rightarrow (S_{x_0 x_1 \cdots x_n})_m \rightarrow 0
$$

where $S = k[x_0, \ldots, x_n]$ and the subscript $m$ denotes the degree-$m$ graded piece. Computing the cohomology of this complex yields Serre's result:

$$
H^i(\mathbb{P}^n_k, \mathcal{O}(m)) = \begin{cases} S_m & \text{if } i = 0, \\ 0 & \text{if } 0 < i < n, \\ S_{-m-n-1}^{\vee} & \text{if } i = n. \end{cases}
$$

**$H^0$: global sections.** A degree-$m$ element of $S_{x_i}$ is a fraction $f/x_i^N$ with $\deg f = m + N$. An element lies in $\bigcap_i (S_{x_i})_m$ if and only if it is a polynomial of degree $m$ (no denominators needed), so $H^0 = S_m$. For $m < 0$, no monomial of negative degree exists, giving $H^0 = 0$.

**$H^n$: top cohomology.** An element of $(S_{x_0 \cdots x_n})_m$ is a Laurent monomial $x_0^{a_0} \cdots x_n^{a_n}$ with $\sum a_i = m$ and each $a_i \in \mathbb{Z}$. A monomial lies in the image of the Cech differential if and only if at least one exponent $a_i \geq 0$. Therefore $H^n$ is spanned by monomials with all $a_i \leq -1$. The substitution $a_i = -1 - b_i$ with $b_i \geq 0$ gives $\sum b_i = -m - n - 1$, so $H^n \cong (S_{-m-n-1})^\vee$. This vanishes when $-m - n - 1 < 0$, i.e., $m > -n - 1$.

**Dimensions.** In particular, $\dim_k H^0(\mathbb{P}^n, \mathcal{O}(m)) = \binom{m+n}{n}$ for $m \geq 0$ and $\dim_k H^n(\mathbb{P}^n, \mathcal{O}(m)) = \binom{-m-1}{n}$ for $m \leq -n-1$.

**Verification on $\mathbb{P}^2$.** For $\mathcal{O}(2)$: $h^0 = \binom{4}{2} = 6$, with basis $\{x_0^2, x_0 x_1, x_0 x_2, x_1^2, x_1 x_2, x_2^2\}$. For $\mathcal{O}(-4)$: $h^2 = \binom{3}{2} = 3$, with basis $\{x_0^{-1}x_1^{-1}x_2^{-2}, x_0^{-1}x_1^{-2}x_2^{-1}, x_0^{-2}x_1^{-1}x_2^{-1}\}$ in the Cech picture. These are consistent with the Euler characteristic $\chi(\mathcal{O}(m)) = \binom{m+n}{n}$.

<!-- BENCHMARK_PROBLEM: Let $X = \mathbb{P}^2_k$ with the standard affine cover $\{U_0, U_1, U_2\}$. Using the Cech complex, compute $H^0(\mathbb{P}^2, \mathcal{O}(2))$ and $H^2(\mathbb{P}^2, \mathcal{O}(-4))$ as $k$-vector spaces, giving explicit bases in terms of monomials. What are their dimensions? -->

### Example: Serre vanishing for coherent sheaves on projective schemes {#ecag-0185}

Let $X$ be a projective scheme over a noetherian ring $A$, let $\mathcal{O}_X(1)$ be a very ample invertible sheaf on $X$ over $\operatorname{Spec}(A)$, and let $\mathscr{F}$ be a coherent sheaf on $X$. Serre's theorem asserts:

1. For all $i \geq 0$, $H^i(X, \mathscr{F})$ is a finitely generated $A$-module.
2. For all $i \geq 1$, there exists $n_0 = n_0(i, \mathscr{F})$ such that $H^i(X, \mathscr{F}(n)) = 0$ for all $n \geq n_0$.

The mechanism is transparent from the explicit computation on projective space. Consider $H^n(\mathbb{P}^n, \mathcal{O}(m))$: this is spanned by Laurent monomials $x_0^{a_0} \cdots x_n^{a_n}$ of total degree $m$ with all $a_i \leq -1$. For such a monomial to exist, we need $\sum a_i = m$ with each $a_i \leq -1$, forcing $m \leq -n-1$. Hence $H^n(\mathbb{P}^n, \mathcal{O}(m)) = 0$ for all $m \geq -n$. Twisting by $\mathcal{O}(n)$ shifts $m \mapsto m + n$, so sufficiently large twist eliminates the top cohomology.

**Application to base change.** One important consequence is the simplification of derived pushforwards. For a proper morphism $f: X \to Y$ and a coherent sheaf $\mathscr{F}$, the derived pushforward $\mathbf{R}f_*\mathscr{F}$ involves all $R^i f_*\mathscr{F}$. After sufficient twist, only $f_*\mathscr{F}(n)$ survives, reducing the derived pushforward to an ordinary pushforward. Concretely, for a morphism $\phi: T \to S$ of noetherian schemes, $\mathscr{F}$ coherent on $\mathbb{P}^n_S$, and projections $\pi_S, \pi_T$, there exists $r_0$ such that the base-change homomorphism

$$
\phi^* \pi_{S,*}\mathscr{F}(r) \xrightarrow{\;\sim\;} \pi_{T,*}\mathscr{F}_T(r)
$$

is an isomorphism for all $r \geq r_0$. Without twisting, the correct statement involves derived categories: $L\phi^* \mathbf{R}\pi_{S,*}\mathscr{F} \xrightarrow{\sim} \mathbf{R}\pi_{T,*}\mathscr{F}_T$ under appropriate flatness hypotheses (flat base change theorem).

<!-- BENCHMARK_PROBLEM: Let $\mathcal{F} = \mathcal{O}(m)$ on $\mathbb{P}^n_k$. Determine precisely for which values of $m$ the group $H^n(\mathbb{P}^n, \mathcal{O}(m))$ vanishes. Express your answer as an inequality in $m$ and $n$, and explain why the result follows from the Laurent monomial description of the Cech cohomology. -->

### Example: Local cohomology and regularity for $k[x,y]/(x^2, xy)$ {#ecag-0186}

Let $S = k[x, y]$ with irrelevant ideal $\mathfrak{m} = (x, y)$, and let $R = S/(x^2, xy)$. We compute the local cohomology modules $H^i_{\mathfrak{m}}(R)$, the Hilbert polynomial, and the Castelnuovo--Mumford regularity of $R$.

**The module $R$ as a graded vector space.** A $k$-basis of $R$ is $\{1, x, y, y^2, y^3, \ldots\}$. The element $x$ satisfies $x^2 = xy = 0$ in $R$, so $x$ spans a 1-dimensional submodule annihilated by $\mathfrak{m}$.

**The Cech complex.** Local cohomology is computed by the Cech complex on the generators $x, y$ of $\mathfrak{m}$:

$$
0 \rightarrow R \xrightarrow{\binom{1}{1}} R[x^{-1}] \oplus R[y^{-1}] \rightarrow R[x^{-1}y^{-1}] \rightarrow 0.
$$

Since $x^2 = 0$ in $R$, the localization $R[x^{-1}]$ contains $1 = x^2 \cdot x^{-2} = 0$, so $R[x^{-1}] = 0$. Similarly $R[x^{-1}y^{-1}] = 0$ (localizing at $x$ already kills everything). The complex collapses to

$$
0 \rightarrow R \xrightarrow{\iota} R[y^{-1}] \rightarrow 0.
$$

**$H^0_{\mathfrak{m}}(R)$.** This is $\ker(\iota) = \{r \in R \mid y^N r = 0 \text{ for some } N\}$. Since $xy = 0$ and $y^n \cdot 1 = y^n \neq 0$ for all $n$, we have $H^0_{\mathfrak{m}}(R) = (x) \cong k$, concentrated in graded degree 1.

**$H^1_{\mathfrak{m}}(R)$.** In $R[y^{-1}]$, the element $x$ vanishes: $x = xy \cdot y^{-1} = 0$. So $R[y^{-1}] \cong k[y, y^{-1}]$. The cokernel of $\iota$ is $k[y, y^{-1}] / k[y] \cong \bigoplus_{j \geq 1} k \cdot y^{-j}$, giving $H^1_{\mathfrak{m}}(R) \cong k[y^{-1}] \cdot y^{-1}$ with nonzero graded pieces in degrees $\leq -1$.

**Hilbert function and polynomial.** We have $\dim_k R_d = 1$ for $d = 0$, $\dim_k R_d = 2$ for $d = 1$ (spanned by $x, y$), and $\dim_k R_d = 1$ for $d \geq 2$ (spanned by $y^d$). Thus the Hilbert polynomial is $\chi_R(t) = 1$ for $t \gg 0$.

**Castelnuovo--Mumford regularity.** By definition, $\operatorname{reg}(R) = \max\{d + i \mid H^i_{\mathfrak{m}}(R)_d \neq 0\}$. From the computation above:

| Module | Nonzero degrees $d$ | Contributing $d + i$ |
|--------|--------------------|-----------------------|
| $H^0_{\mathfrak{m}}(R)$ ($i = 0$) | $d = 1$ | $1$ |
| $H^1_{\mathfrak{m}}(R)$ ($i = 1$) | $d = -1, -2, \ldots$ | $0, -1, \ldots$ |

Therefore $\operatorname{reg}(R) = 1$.

**Verification via local duality.** With $S = k[x,y]$ of Krull dimension 2, local duality gives $H^i_{\mathfrak{m}}(R) \cong (\operatorname{Ext}_S^{2-i}(R, S(-2)))^\vee$. For $i = 0$: $\operatorname{Ext}^2_S(R, S(-2))^\vee \cong k^\vee = k$, consistent with $H^0_{\mathfrak{m}}(R) \cong k$. For $i = 1$: $\operatorname{Ext}^1_S(R, S(-2))^\vee$ can be computed from the free resolution $0 \to S(-3) \xrightarrow{\binom{y}{-x}} S(-2)^2 \xrightarrow{(x^2, xy)} S \to R \to 0$, confirming the result.

<!-- BENCHMARK_PROBLEM: Let $S = k[x,y]$, $\mathfrak{m} = (x,y)$, and $R = S/(x^2, xy)$. Compute $H^0_{\mathfrak{m}}(R)$ and $H^1_{\mathfrak{m}}(R)$ as graded $k$-vector spaces by analyzing the Cech complex. Determine the Castelnuovo--Mumford regularity $\operatorname{reg}(R)$. -->

### Remark: Local duality theorem {#ecag-0187}

The preceding example illustrates the local duality theorem in its general form (cf. Eisenbud, *The Geometry of Syzygies*, Springer 2005). For a polynomial ring $S = k[x_0, \ldots, x_r]$ with irrelevant ideal $\mathfrak{m}$ and a finitely generated graded $S$-module $M$, there is a natural isomorphism of graded modules

$$
H^i_{\mathfrak{m}}(M) \cong \left(\operatorname{Ext}_S^{r+1-i}(M, S(-r-1))\right)^{\vee}
$$

where $(-)^\vee$ denotes the graded $k$-dual. This is a graded local analogue of Serre duality: the local cohomology at the irrelevant ideal plays the role of sheaf cohomology, and $S(-r-1)$ plays the role of the dualizing module $\omega_S$.

<!-- BENCHMARK_PROBLEM: State the local duality theorem for a polynomial ring $S = k[x_0, \ldots, x_r]$ with irrelevant ideal $\mathfrak{m}$, and verify it for the module $M = S/(x_0)$ by computing both $H^i_{\mathfrak{m}}(M)$ and $\operatorname{Ext}_S^{r+1-i}(M, S(-r-1))$. -->

### Example: Projective normality and the integral closure of $S(X)$ {#ecag-0188}

Let $X$ be a connected, normal closed subscheme of $\mathbb{P}^r_A$, where $A$ is a finitely generated $k$-algebra. Write $S = S(X) = A[x_0, \ldots, x_r]/I$ for the homogeneous coordinate ring and $\Gamma = \Gamma_*(X, \mathcal{O}_X) = \bigoplus_{n \geq 0} \Gamma(X, \mathcal{O}_X(n))$ for the saturated graded ring of global sections. The main assertions (Hartshorne II.5.14) are:

1. $\Gamma$ is integral over $S$.
2. $\Gamma$ is integrally closed.
3. $\Gamma_d = S_d$ for $d \gg 0$.
4. The Veronese subring $S^{(d)} = \bigoplus_{n \geq 0} S_{nd}$ is integrally closed for all $d$; in particular, the $d$-uple embedding is projectively normal for $d \gg 0$.

**Proof of (1).** Since $X$ is integral (connected and normal implies irreducible), $S$ is a domain. We have $\Gamma = \bigcap_{i=0}^r S_{x_i}$, where each $S_{x_i}$ is a localization of $S$. For any $y \in \Gamma$, there exists $N$ such that $x_i^N y \in S$ for all $i$, so $y$ is integral over $S$ (it lies in the finitely generated $S$-module $S \cdot x_i^{-N}$).

**Proof of (2).** The degree-zero part $S_{((x_i))}$ of $S_{x_i}$ is the coordinate ring of the affine open $X \cap D_+(x_i)$, which is normal since $X$ is. Setting $\Gamma^{(i)} = \{z \in S_{x_i} \mid \deg(z) \geq 0\} \cong S_{((x_i))}[x_i]$, we get $\Gamma = \bigcap_i \Gamma^{(i)}$. Since each $S_{((x_i))}$ is integrally closed, so is the polynomial ring $\Gamma^{(i)}$, and an intersection of integrally closed subrings of a common fraction field is integrally closed. Therefore $\Gamma$ is the integral closure of $S$.

**Proof of (3).** Since $S$ is a finitely generated domain over a field, its integral closure $\Gamma$ is a finite $S$-module. Let $y_1, \ldots, y_m$ generate $\Gamma$ over $S$. For each $y_j$ there exists $N_j$ with $x_i^{N_j} y_j \in S$ for all $i$, so $\Gamma_d \subset S_d$ for $d \geq \max_j \deg(y_j) + \max_j N_j$. Combined with $S \subset \Gamma$, this gives $S_d = \Gamma_d$ for $d \gg 0$.

**Proof of (4).** If $y \in \operatorname{Frac}(\Gamma^{(d)})$ is integral over $\Gamma^{(d)}$, then $y \in \Gamma$ since $\Gamma$ is integrally closed. The degree of $y$ must be divisible by $d$ (it lies in $\operatorname{Frac}(\Gamma^{(d)})$), so $y \in \Gamma^{(d)}$. For $d \gg 0$, $S^{(d)} = \Gamma^{(d)}$ by (3), so $S^{(d)}$ is integrally closed.

As a consequence, $X$ is projectively normal if and only if $\Gamma(X, \mathcal{O}_X(n)) = S(X)_n$ for all $n \geq 0$, equivalently, the restriction map $H^0(\mathbb{P}^r_A, \mathcal{O}(n)) \to H^0(X, \mathcal{O}_X(n))$ is surjective for all $n$. Any nonsingular hypersurface in $\mathbb{P}^r$ is projectively normal (the ideal sheaf sequence and the vanishing $H^1(\mathbb{P}^r, \mathcal{O}(n-d)) = 0$ for $n \geq d$ give the surjectivity).

<!-- BENCHMARK_PROBLEM: Let $X$ be a normal projective variety over a field $k$ embedded in $\mathbb{P}^r$. Prove that the Veronese $d$-uple embedding of $X$ is projectively normal for $d$ sufficiently large. Identify the key algebraic fact that guarantees $\Gamma_d = S(X)_d$ for large $d$. -->

### Example: The rational quartic and failure of projective normality {#ecag-0189}

Consider the map $\varphi: \mathbb{P}^1 \to \mathbb{P}^3$ defined by

$$
[u, v] \mapsto [u^4,\; u^3 v,\; uv^3,\; v^4].
$$

Let $C = \varphi(\mathbb{P}^1)$, a rational quartic curve. The linear system used is the span of $\{u^4, u^3v, uv^3, v^4\} \subset H^0(\mathbb{P}^1, \mathcal{O}(4))$, which is incomplete: the monomial $u^2v^2$ is missing.

Since $\mathcal{O}_C(1) \cong \varphi^*\mathcal{O}_{\mathbb{P}^3}(1) \cong \mathcal{O}_{\mathbb{P}^1}(4)$, we have $h^0(C, \mathcal{O}_C(1)) = h^0(\mathbb{P}^1, \mathcal{O}(4)) = 5$. On the other hand, $h^0(\mathbb{P}^3, \mathcal{O}(1)) = 4$. The restriction map $H^0(\mathbb{P}^3, \mathcal{O}(1)) \to H^0(C, \mathcal{O}_C(1))$ has image spanned by the four coordinate monomials, with $u^2v^2$ generating the 1-dimensional cokernel.

**The section $u^2v^2$ is regular on each affine open.** Writing $[x, y, z, w]$ for coordinates on $\mathbb{P}^3$:

| Affine open | Expression for $u^2v^2$ |
|-------------|------------------------|
| $D_+(x)$ | $(y/x)^2 \cdot x$ |
| $D_+(y)$ | $(x/y)(z/y) \cdot y$ |
| $D_+(z)$ | $(y/z)(w/z) \cdot z$ |
| $D_+(w)$ | $(z/w)^2 \cdot w$ |

Each expression is a regular function times a degree-1 element, confirming $u^2v^2 \in \Gamma(C, \mathcal{O}_C(1)) \setminus S(C)_1$.

From the ideal sheaf sequence $0 \to \mathscr{I}_C \to \mathcal{O}_{\mathbb{P}^3} \to \mathcal{O}_C \to 0$ twisted by $\mathcal{O}(1)$, the non-surjectivity of the restriction map gives $H^1(\mathbb{P}^3, \mathscr{I}_C(1)) \cong k$. Thus $C$ is not projectively normal, and $\Gamma_*(C, \mathcal{O}_C) \supsetneq S(C)$.

<!-- BENCHMARK_PROBLEM: Let $C$ be the image of the map $\mathbb{P}^1 \to \mathbb{P}^3$ given by $[u,v] \mapsto [u^4, u^3v, uv^3, v^4]$. Compute $h^0(C, \mathcal{O}_C(1))$ and $h^0(\mathbb{P}^3, \mathcal{O}(1))$, identify the missing section explicitly, and explain why $C$ is not projectively normal. -->

### Remark: $S(X)$ versus $\Gamma_*(X, \mathcal{O}_X)$ {#ecag-0190}

For a projective scheme $X = \operatorname{Proj}(S)$, several related but distinct objects must be carefully distinguished:

- The scheme $X$ does not determine $S$ uniquely. Different graded rings can give isomorphic $\operatorname{Proj}$'s; for instance $\operatorname{Proj}(S) \cong \operatorname{Proj}(S^{(d)})$ for any $d \geq 1$.

- The homogeneous coordinate ring $S(X)$ depends on the specific embedding $X \hookrightarrow \mathbb{P}^r$, not just the abstract scheme $X$.

- The saturated ring $\Gamma_*(X, \mathcal{O}_X) = \bigoplus_{n \geq 0} H^0(X, \mathcal{O}_X(n))$ is an intrinsic invariant of the pair $(X, \mathcal{O}_X(1))$. There is always a natural map $S(X) \to \Gamma_*(X, \mathcal{O}_X)$, which is an isomorphism in large degrees (by the finiteness of the integral closure), but it can fail to be surjective in small degrees (as the rational quartic example shows).

- The associated sheaves $\widetilde{S}$ and $\widetilde{\Gamma_*}$ are isomorphic on $X$; the distinction lives entirely in graded module theory, not in sheaf theory.

- An isomorphism $X \cong Y$ of abstract schemes does not imply $\mathcal{O}_X(1) \cong f^*\mathcal{O}_Y(1)$, since $\mathcal{O}(1)$ depends on the embedding.

<!-- BENCHMARK_PROBLEM: Give an example of two non-isomorphic graded rings $S$ and $S'$ with $\operatorname{Proj}(S) \cong \operatorname{Proj}(S')$, and explain why $\operatorname{Proj}$ does not determine the graded ring. -->

### Remark: Local cohomology, Cech complex, and Castelnuovo--Mumford regularity {#ecag-0191}

For a noetherian ring $R$ and an ideal $Q = (x_1, \ldots, x_t)$, the local cohomology $H^i_Q(M)$ of an $R$-module $M$ is the $i$-th right derived functor of the $Q$-torsion functor $\Gamma_Q(M) = \{m \in M \mid Q^d m = 0 \text{ for some } d \geq 1\}$. It can be computed as the $i$-th cohomology of the Cech complex

$$
C(x_1, \ldots, x_t; M): \quad 0 \to M \xrightarrow{d} \bigoplus_{i=1}^{t} M[x_i^{-1}] \xrightarrow{d} \cdots \to \bigoplus_{|J|=k} M[x_J^{-1}] \to \cdots \to M[x_{1 \cdots t}^{-1}] \to 0
$$

with differential $d(m_J) = \sum_{k \notin J} (-1)^{|\{i \in J : i < k\}|} m_{J \cup \{k\}}$, where $m_{J \cup \{k\}}$ denotes the natural image of $m_J$ under localization.

For the polynomial ring $S = k[x_0, \ldots, x_r]$ with $\mathfrak{m} = (x_0, \ldots, x_r)$, the **Castelnuovo--Mumford regularity** of a finitely generated graded $S$-module $M$ is

$$
\operatorname{reg}(M) = \max\{d + i \mid H^i_{\mathfrak{m}}(M)_d \neq 0\}.
$$

This invariant controls the degree from which the Hilbert function agrees with the Hilbert polynomial, and it bounds the degrees of generators and syzygies of $M$.

<!-- BENCHMARK_PROBLEM: Let $S = k[x,y,z]$, $\mathfrak{m} = (x,y,z)$, and $M = S/(x,y)$. Compute $H^i_{\mathfrak{m}}(M)$ for all $i$ using the Cech complex on $x, y, z$, and determine $\operatorname{reg}(M)$. -->

### Example: Regularity cannot be bounded by Hilbert polynomial for arbitrary sheaves {#ecag-0192}

Let $\mathscr{F} = \mathcal{O}_{\mathbb{P}^1}(k) \oplus \mathcal{O}_{\mathbb{P}^1}(-k)$ for $k \geq 0$. The Hilbert polynomial of $\mathscr{F}$ is independent of $k$, yet its Castelnuovo--Mumford regularity grows without bound.

**Euler characteristic.** By additivity,

$$
\chi(\mathscr{F}(m)) = \chi(\mathcal{O}(m+k)) + \chi(\mathcal{O}(m-k)) = (m+k+1) + (m-k+1) = 2m + 2.
$$

The Hilbert polynomial $2m + 2 = 2\binom{m+1}{1}$ is independent of $k$.

**Regularity.** The sheaf $\mathscr{F}$ is $m$-regular if $H^1(\mathbb{P}^1, \mathscr{F}(m-1)) = 0$. We have

$$
H^1(\mathbb{P}^1, \mathscr{F}(m-1)) = H^1(\mathcal{O}(m-1+k)) \oplus H^1(\mathcal{O}(m-1-k)).
$$

Since $H^1(\mathbb{P}^1, \mathcal{O}(j)) = 0$ if and only if $j \geq -1$ (by Serre duality, $H^1(\mathcal{O}(j)) \cong H^0(\mathcal{O}(-j-2))^\vee$), the second summand vanishes if and only if $m - 1 - k \geq -1$, i.e., $m \geq k$. The first summand vanishes for all $m \geq 0$. Therefore $\operatorname{reg}(\mathscr{F}) = k$.

Since the Hilbert polynomial is $2m + 2$ regardless of $k$, no function of the Hilbert polynomial coefficients can bound $\operatorname{reg}(\mathscr{F})$. This contrasts with Mumford's theorem for ideal sheaves $\mathscr{I}_X \subset \mathcal{O}_{\mathbb{P}^n}$, where the regularity is bounded by a function of the Hilbert polynomial.

<!-- BENCHMARK_PROBLEM: Let $\mathscr{F} = \mathcal{O}_{\mathbb{P}^1}(k) \oplus \mathcal{O}_{\mathbb{P}^1}(-k)$ for $k \geq 0$. Show that $\operatorname{reg}(\mathscr{F}) = k$ while the Hilbert polynomial of $\mathscr{F}$ is $2m + 2$, independent of $k$. What does this imply about bounding regularity solely in terms of Hilbert polynomial coefficients for arbitrary coherent sheaves? -->

### Remark: Mumford's regularity theorem for ideal sheaves {#ecag-0193}

Mumford proved (in *Lectures on Curves on an Algebraic Surface*, Annals of Mathematics Studies No. 59, Lectures 14--15) that for an ideal sheaf $\mathscr{I}_X$ of a subvariety $X \subset \mathbb{P}^n$, the Castelnuovo--Mumford regularity can be bounded in terms of the Hilbert polynomial of $X$. The preceding example shows this bound fails for arbitrary coherent sheaves: the family $\mathcal{O}(k) \oplus \mathcal{O}(-k)$ on $\mathbb{P}^1$ has constant Hilbert polynomial but unbounded regularity.

<!-- BENCHMARK_PROBLEM: State the distinction between Mumford's regularity theorem for ideal sheaves and the behavior of regularity for arbitrary coherent sheaves. Give an explicit family of sheaves on $\mathbb{P}^1$ demonstrating the failure. -->

### Example: Relations between (co)homology theories {#ecag-0194}

Three fundamental isomorphisms relate Borel--Moore homology to singular and relative homology:

**(1)** $H_i^{BM}(X) \cong H_i(\hat{X}, \{*\})$, where $\hat{X} = X \cup \{*\}$ is the one-point compactification of the locally compact Hausdorff space $X$. Borel--Moore homology uses locally finite chains; a locally finite chain on $X$ extends to a chain on $\hat{X}$ by declaring it to be finite relative to $*$, and this identification is exact.

**(2)** $H_i^{BM}(X) \cong H_i(\overline{X}, \overline{X} \setminus X)$ for any compactification $\overline{X}$ of $X$. By excision, $H_i(\overline{X}, \overline{X} \setminus X) \cong H_i(\hat{X}, \{*\})$, since collapsing the complement $\overline{X} \setminus X$ to a point recovers the one-point compactification (up to homotopy equivalence of pairs).

**(3)** $H_i(X, A) \cong \widetilde{H}_i(X/A)$ whenever $(X, A)$ is a good pair, meaning $A$ is a closed subspace that is a deformation retract of some open neighborhood in $X$. This is the standard excision/quotient theorem: the quotient map $(X, A) \to (X/A, A/A)$ induces an isomorphism on relative homology, and $H_i(X/A, A/A) = \widetilde{H}_i(X/A)$ by definition.

<!-- BENCHMARK_PROBLEM: Compute $H_i^{BM}(\mathbb{R}^n)$ for all $i$ using the one-point compactification $(\mathbb{R}^n)^+ = S^n$ and the isomorphism $H_i^{BM}(X) \cong \widetilde{H}_i(\hat{X})$. Express your answer in terms of $n$. -->

### Example: Borel--Moore homology of $\mathbb{R}$ and $\mathbb{R}^2 \setminus \{0\}$ {#ecag-0195}

**Computation for $\mathbb{R}$.** The one-point compactification of $\mathbb{R}$ is $S^1$, so

$$
H_i^{BM}(\mathbb{R}) = H_i(S^1, \{*\}) = \widetilde{H}_i(S^1) = \begin{cases} \mathbb{Z} & i = 1, \\ 0 & \text{otherwise.} \end{cases}
$$

**Computation for $\mathbb{R}^2 \setminus \{0\}$.** Take the compactification $\overline{X} = S^2$ (the one-point compactification of $\mathbb{R}^2$). The complement $S^2 \setminus (\mathbb{R}^2 \setminus \{0\}) = \{0, \infty\}$ consists of two points, so

$$
H_i^{BM}(\mathbb{R}^2 \setminus \{0\}) = H_i(S^2, \{0, \infty\}) \cong \widetilde{H}_i(S^2 / \{0, \infty\}).
$$

Identifying the north and south poles of $S^2$ produces the wedge $S^2 \vee S^1$ (a sphere with a circle attached at the identified point). Hence

$$
H_i^{BM}(\mathbb{R}^2 \setminus \{0\}) = \widetilde{H}_i(S^2 \vee S^1) = \begin{cases} \mathbb{Z} & i = 1, 2, \\ 0 & \text{otherwise.} \end{cases}
$$

**Comparison with ordinary homology.** The ordinary homology $H_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$ is generated by a circle around the origin. In the Borel--Moore setting, this circle bounds the locally finite 2-chain given by either half-plane it separates, so it maps to zero in $H_1^{BM}$. Instead, $H_1^{BM}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$ is generated by a ray from $0$ to $\infty$ -- a locally finite 1-chain that has no compact analogue. Thus the natural map $H_i(\mathbb{R}^2 \setminus \{0\}) \to H_i^{BM}(\mathbb{R}^2 \setminus \{0\})$ is the zero map for all $i$.

<!-- BENCHMARK_PROBLEM: Compute $H_i^{BM}(\mathbb{R}^2 \setminus \{0\})$ for all $i$ using a compactification argument. Identify a generator of $H_1^{BM}$ as a locally finite chain, and explain why the circle generating $H_1(\mathbb{R}^2 \setminus \{0\})$ maps to zero in Borel--Moore homology. -->

### Remark: Properties and pathologies of Borel--Moore homology {#ecag-0196}

Borel--Moore homology differs from ordinary singular homology in several important ways:

**Not homotopy invariant.** We have $H_1^{BM}(\mathbb{R}) \cong \mathbb{Z}$ but $H_1^{BM}(\{pt\}) = 0$, even though $\mathbb{R}$ is contractible.

**Poincare duality for non-compact manifolds.** For an oriented $n$-manifold $M$, the correct duality is $H_i^{BM}(M) \cong H^{n-i}(M)$, not $H_i(M) \cong H^{n-i}(M)$ (which fails for non-compact $M$).

**Proper pushforward only.** A continuous map $f: X \to Y$ does not generally induce $f_*: H_i^{BM}(X) \to H_i^{BM}(Y)$, because images of locally finite chains need not be locally finite. For example, the inclusion $\mathbb{R} \setminus \{0\} \hookrightarrow \mathbb{R}$ sends the locally finite chain $\sum_{j \geq 0} [2^{-j-1}, 2^{-j}]$ (locally finite on $\mathbb{R} \setminus \{0\}$) to a chain that is not locally finite at $0 \in \mathbb{R}$. Proper maps do induce pushforwards.

**Localization sequence.** For $Y \subset X$ closed in a locally compact space and $U = X \setminus Y$, there is a long exact sequence

$$
\cdots \to H_k^{BM}(Y) \to H_k^{BM}(X) \to H_k^{BM}(U) \to H_{k-1}^{BM}(Y) \to \cdots
$$

arising from the long exact sequence of the pair $(\overline{X}, \overline{X} \setminus U)$.

<!-- BENCHMARK_PROBLEM: Using the localization long exact sequence for Borel--Moore homology applied to $Y = \{0\} \subset X = \mathbb{R}$ with $U = \mathbb{R} \setminus \{0\}$, compute $H_i^{BM}(\mathbb{R} \setminus \{0\})$ for all $i$. -->

### Example: Poincare duality and Poincare--Lefschetz duality {#ecag-0197}

**Poincare--Lefschetz duality.** Let $X$ be a closed subset of a smooth oriented manifold $M$ of real dimension $n$. Then

$$
H_i^{BM}(X) \cong H^{n-i}(M, M \setminus X).
$$

The isomorphism is given by the cap product with the fundamental class. When $X = M$ is compact, $H_i^{BM}(M) = H_i(M)$ and $M \setminus M = \varnothing$, recovering classical Poincare duality $H_i(M) \cong H^{n-i}(M)$.

When $X$ is open in $M$ (so $M$ is a compactification of $X$), combining Poincare--Lefschetz duality with the Borel--Moore definition $H_i^{BM}(X) = H_i(M, M \setminus X)$ gives the self-duality $H^{n-i}(M, M \setminus X) \cong H_i(M, M \setminus X)$.

**Lefschetz duality for manifolds with boundary.** For a compact oriented $n$-manifold $M$ with boundary $\partial M$:

$$
H^k(M, \partial M) \cong H_{n-k}(M), \qquad H_k(M) \cong H^{n-k}(M, \partial M).
$$

The proof uses the fundamental class $[M, \partial M] \in H_n(M, \partial M)$ and the cap product. This differs from the Borel--Moore setting: here $\partial M$ is closed in $M$, whereas Borel--Moore theory involves the complement $M \setminus X$, which is open.

<!-- BENCHMARK_PROBLEM: Let $M$ be a smooth compact oriented $n$-manifold without boundary, and let $X = M \setminus \{p\}$ for a point $p$. Using Poincare--Lefschetz duality $H_i^{BM}(X) \cong H^{n-i}(M, M \setminus X)$, compute $H_i^{BM}(M \setminus \{p\})$ in terms of the cohomology of $M$ and the local cohomology at $p$. -->

### Remark: Intersection homology reference {#ecag-0198}

A comprehensive treatment of intersection homology, including the construction of allowable chains with perversity conditions and the proof of generalized Poincare duality for singular spaces, is given in Maxim's lecture notes (*Intersection Homology*, University of Wisconsin). Intersection homology, introduced by Goresky and MacPherson (1980), recovers Poincare duality for singular algebraic varieties by restricting chains according to a perversity function that controls how chains interact with the singular strata.

<!-- BENCHMARK_PROBLEM: State the perversity condition for a chain to be $\overline{p}$-allowable in intersection homology, and explain why the middle perversity is the unique self-dual perversity for even-dimensional strata. -->

### Example: Perverse sheaves {#ecag-0199}

A perverse sheaf on a complex algebraic variety $X$ (with a fixed stratification $X = \bigsqcup_\alpha S_\alpha$) is an object $\mathcal{F}^\bullet \in D^b_c(X, \mathbb{Q})$ satisfying:

- **(Support)** $\dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathcal{F}^\bullet) \leq -j$ for all $j$.
- **(Cosupport)** $\dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathbb{D}\mathcal{F}^\bullet) \leq -j$ for all $j$, where $\mathbb{D}$ is Verdier duality.

The category $\operatorname{Perv}(X)$ of perverse sheaves is the heart of the perverse $t$-structure on $D^b_c(X)$, defined by

$$
{}^p D^{\leq 0} = \{\mathcal{F}^\bullet \mid \dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathcal{F}^\bullet) \leq -j \;\forall\; j\}, \quad {}^p D^{\geq 0} = \{\mathcal{F}^\bullet \mid \dim_\mathbb{C} \operatorname{supp} \mathcal{H}^j(\mathbb{D}\mathcal{F}^\bullet) \leq -j \;\forall\; j\}.
$$

Despite the name, perverse sheaves are not sheaves but complexes of sheaves satisfying these dimensional conditions.

**Fundamental example: shifted local systems.** If $X$ is smooth of pure dimension $d$ and $\mathcal{L}$ is a local system on $X$, then $\mathcal{L}[d]$ is a perverse sheaf. The support condition is satisfied because $\mathcal{H}^j(\mathcal{L}[d]) = 0$ for $j \neq -d$, and $\operatorname{supp} \mathcal{H}^{-d}(\mathcal{L}[d]) = X$ has dimension $d = -(-d)$. The cosupport condition follows by Verdier duality: $\mathbb{D}(\mathcal{L}[d]) \cong \mathcal{L}^\vee[d]$ (up to twist), and the same dimension count applies.

**Intersection cohomology complex.** For a singular variety with smooth locus $j: U \hookrightarrow X$ and a local system $\mathcal{L}$ on $U$, the intersection cohomology complex $\operatorname{IC}(X, \mathcal{L})$ is the unique extension of $\mathcal{L}[\dim X]$ to a perverse sheaf on $X$ having no nontrivial sub-objects or quotient-objects supported on $X \setminus U$.

The perverse cohomology functors ${}^p H^i: D^b_c(X) \to \operatorname{Perv}(X)$ are the cohomology functors of the perverse $t$-structure, analogous to ordinary cohomology sheaves $\mathcal{H}^i$ for the standard $t$-structure.

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth complex variety of dimension $d$ and $\mathcal{L}$ a local system on $X$. Verify that $\mathcal{L}[d]$ satisfies the support and cosupport conditions to be a perverse sheaf. Determine ${}^p H^0(\mathcal{L}[d])$. -->

### Example: Intersection cohomology via the IC complex {#ecag-0200}

Let $X$ be a (possibly singular) complex algebraic variety of pure dimension $n$, and let $\mathcal{L}$ be a local system on a smooth dense open $U \subset X$. The intersection cohomology groups are

$$
IH^k(X, \mathcal{L}) := H^{k-n}(X, \operatorname{IC}(X, \mathcal{L}))
$$

where $\operatorname{IC}(X, \mathcal{L})$ is the intersection cohomology complex extending $\mathcal{L}[n]$. The shift ensures that when $X$ is smooth and $\mathcal{L}$ is constant, $IH^k(X, \mathbb{Q}) = H^k(X, \mathbb{Q})$.

**Construction of IC by iterated truncation.** Fix a Whitney stratification $X = \bigsqcup_\alpha S_\alpha$ with open stratum $U = S_0$. Let $U_k = \bigsqcup_{\dim S_\alpha \geq n-k} S_\alpha$ with inclusions $j_k: U_k \hookrightarrow U_{k+1}$. Then

$$
\operatorname{IC}(X, \mathcal{L}) = \tau_{\leq -1} R(j_{n-1})_* \cdots \tau_{\leq -n+1} R(j_1)_* (\mathcal{L}[n]).
$$

Each truncation enforces the support condition stratum by stratum. The result is independent of the stratification and is Verdier self-dual (up to twist by $\mathcal{L}^\vee$), yielding generalized Poincare duality:

$$
IH^k(X, \mathcal{L}) \cong IH^{2n-k}(X, \mathcal{L}^\vee)^\vee.
$$

**Concrete example: nodal curve.** Let $X$ be a curve with a single node $p$, and set $U = X \setminus \{p\}$, $\mathcal{L} = \mathbb{Q}_U$. The constant sheaf $\mathbb{Q}_X[1]$ fails to be a perverse sheaf at $p$ because the stalk $\mathcal{H}^0(\mathbb{Q}_X[1])_p = 0$ but the cosupport condition is violated (the local $H^0$ of the Verdier dual is too large). The IC complex corrects this: $\mathcal{H}^{-1}(\operatorname{IC}(X))_p \cong \mathbb{Q}$ and $\mathcal{H}^0(\operatorname{IC}(X))_p = 0$. In terms of the Cech picture, the vanishing cycle at the node is killed by the truncation.

<!-- BENCHMARK_PROBLEM: Let $X$ be a projective curve with a single node $p$, and let $U = X \setminus \{p\}$. Describe the stalk cohomology $\mathcal{H}^j(\operatorname{IC}(X, \mathbb{Q}))_p$ at the node for all $j$, and explain how it differs from $\mathcal{H}^j(\mathbb{Q}_X[1])_p$. -->

### Example: Intersection cohomology and the decomposition theorem {#ecag-0201}

For a complex variety $Y$ of pure dimension $n$ with smooth dense open $U \subset Y$ carrying a local system $L$, the intersection cohomology groups

$$
IH^{n+k}(Y, L) := H^k(Y, \operatorname{IC}(Y, L))
$$

are defined so that $\operatorname{IC}(Y, L)$, which lives in cohomological degrees $[-n, 0]$, normalizes the indexing: for smooth $Y$ with $L$ constant, $IH^k(Y, \mathbb{Q}) = H^k(Y, \mathbb{Q})$. The key structural results are:

**Poincare duality.** $IH^k(Y, L) \cong IH^{2n-k}(Y, L^\vee)^\vee$.

**Hard Lefschetz.** If $Y$ is projective with hyperplane class $\eta$, then $\eta^j: IH^{n-j}(Y) \xrightarrow{\sim} IH^{n+j}(Y)$ for all $j \geq 0$.

**Decomposition theorem** (Beilinson--Bernstein--Deligne--Gabber). For a proper morphism $f: X \to Y$ with $X$ smooth of dimension $n$, the derived pushforward $\mathbf{R}f_*\mathbb{Q}_X[n]$ decomposes in $D^b_c(Y)$ as a direct sum of shifted IC complexes of semisimple local systems on strata of $Y$:

$$
\mathbf{R}f_*\mathbb{Q}_X[n] \cong \bigoplus_{i} \operatorname{IC}(\overline{S_i}, \mathcal{L}_i)[n_i]
$$

where each $\mathcal{L}_i$ is a semisimple local system on a stratum $S_i$ of $Y$. This is one of the deepest results in the theory, subsuming Deligne's degeneration theorem and the semisimplicity of monodromy for algebraic families.

<!-- BENCHMARK_PROBLEM: Let $Y$ be a projective variety of dimension $n$ with a single isolated singularity $p$, smooth elsewhere. If the link of $p$ is a rational homology sphere, show that $IH^k(Y, \mathbb{Q}) \cong H^k(Y, \mathbb{Q})$ for all $k$. -->

### Example: Catalog of (co)homology theories related to perverse sheaves {#ecag-0202}

The following theories arise naturally in the study of the decomposition theorem and perverse sheaves. We list their definitions and interrelationships.

1. **Ordinary cohomology** $H^i(X, \mathbb{Z})$: singular cohomology, computed as $H^i(\mathbf{R}\Gamma(X, \mathbb{Z}_X))$.

2. **Cohomology with support** $H^i_Y(X, \mathscr{F})$: for $Y \subset X$ closed, $H^i_Y = R^i\Gamma_Y$ where $\Gamma_Y$ is sections supported in $Y$. Fits into the exact sequence $\cdots \to H^i_Y(X, \mathscr{F}) \to H^i(X, \mathscr{F}) \to H^i(X \setminus Y, \mathscr{F}) \to \cdots$.

3. **Borel--Moore homology** $H_i^{BM}(X)$: homology via locally finite chains. For an oriented $n$-manifold, $H_i^{BM}(X) \cong H^{n-i}(X)$. For complex varieties, $H_i^{BM}(X) \cong H_c^{2n-i}(X)^\vee$.

4. **Compactly supported cohomology** $H^i_c(X, \mathscr{L})$: defined as $H^i(\overline{X}, j_!\mathscr{L})$ for any compactification $j: X \hookrightarrow \overline{X}$. Satisfies $H^i_c(X) \cong H^{2n-i}(X)^\vee$ for smooth $X$ of complex dimension $n$.

5. **Stalk cohomology** $\mathcal{H}^i_x(A^\bullet) = H^i(A^\bullet_x)$: the local invariant controlling support and cosupport conditions for perverse sheaves.

6. **Cohomology sheaf** $\mathcal{H}^i(A^\bullet)$: sheafification of $U \mapsto H^i(\Gamma(U, A^\bullet))$, always constructible for constructible complexes.

7. **Hypercohomology** $\mathbb{H}^i(X, A^\bullet) = H^i(\mathbf{R}\Gamma(X, A^\bullet))$: derived functor cohomology of a complex of sheaves.

8. **Perverse cohomology** ${}^p H^i(A^\bullet)$: cohomology functors of the perverse $t$-structure. These are perverse sheaves, not classical sheaves.

9. **Intersection homology** $IH_i^{\overline{p}}(X)$: homology using only $\overline{p}$-allowable chains, where the perversity controls interaction with singular strata. The middle perversity $\overline{m}$ gives $\operatorname{IC}(X)$.

10. **Local intersection homology** $IH_i^{\overline{p}}(X, X \setminus \{x\}; \mathscr{L})$: computes the stalk of IC and is determined by the topology of the link of $x$.

These form a hierarchy: stalk cohomology is the local invariant, cohomology sheaves assemble stalks into a global sheaf, hypercohomology globalizes further, and perverse cohomology replaces the standard $t$-structure with one adapted to singularities.

<!-- BENCHMARK_PROBLEM: For a smooth complex variety $X$ of dimension $n$, express $H^i_c(X, \mathbb{Q})$, $H_i^{BM}(X, \mathbb{Q})$, and $IH^i(X, \mathbb{Q})$ in terms of ordinary cohomology $H^j(X, \mathbb{Q})$. Which of these theories are homotopy invariant? -->

### Example: Operations in the theory of perverse sheaves {#ecag-0203}

The theory of perverse sheaves requires several key constructions, which we catalog with precise definitions.

**Perversity.** A perversity is a function $\overline{p}: \{2, 3, \ldots\} \to \mathbb{Z}_{\geq 0}$ with $\overline{p}(2) = 0$ and $\overline{p}(k+1) \in \{\overline{p}(k), \overline{p}(k)+1\}$. The middle perversity is $\overline{m}(2s) = \overline{m}(2s+1) = s-1$. In the BBD (Beilinson--Bernstein--Deligne) convention, the perversity is absorbed into the $t$-structure definition.

**Mapping cone.** For $f: A^\bullet \to B^\bullet$ in $D^b(X)$, the mapping cone $\operatorname{Cone}(f)$ fits in a distinguished triangle $A^\bullet \xrightarrow{f} B^\bullet \to \operatorname{Cone}(f) \xrightarrow{[1]} A^\bullet[1]$.

**Link.** For a point $x$ in a stratified space $X$ belonging to a stratum $S_\alpha$ of dimension $d$, the link $L_x$ is the boundary of a small normal slice to $S_\alpha$ through $x$. The local topology is modeled on $\operatorname{cone}(L_x) \times \mathbb{R}^d$.

**Perverse truncation.** The functors ${}^p\tau_{\leq n}, {}^p\tau_{\geq n}$ are the truncation functors for the perverse $t$-structure. For $A^\bullet \in D^b_c(X)$, there is a distinguished triangle ${}^p\tau_{\leq n} A^\bullet \to A^\bullet \to {}^p\tau_{\geq n+1} A^\bullet \xrightarrow{[1]}$, and ${}^p H^n(A^\bullet) = {}^p\tau_{\leq n}\, {}^p\tau_{\geq n} A^\bullet$.

**Derived pushforward.** For $j: U \hookrightarrow X$ open and $\mathscr{L}$ a local system on $U$, the stalk cohomology of $Rj_*\mathscr{L}$ at $x \in X \setminus U$ computes $H^*(L_x, \mathscr{L})$, the cohomology of the local system restricted to the link.

**Intermediate extension.** For $\mathcal{F} \in \operatorname{Perv}(U)$, the intermediate extension is $j_{!*}\mathcal{F} = \operatorname{Im}({}^p H^0(j_!\mathcal{F}) \to {}^p H^0(Rj_*\mathcal{F}))$. The IC complex is $\operatorname{IC}(X, \mathscr{L}) = j_{!*}(\mathscr{L}[\dim X])$, characterized as the unique perverse extension with no sub- or quotient-objects supported on $X \setminus U$.

<!-- BENCHMARK_PROBLEM: Let $j: U \to X$ be the inclusion of the smooth locus of a variety $X$. Define the intermediate extension functor $j_{!*}$ and prove that $\operatorname{IC}(X, \mathcal{L}) = j_{!*}(\mathcal{L}[\dim X])$ has no nontrivial sub-objects or quotient-objects supported on $X \setminus U$ in $\operatorname{Perv}(X)$. -->

### Example: The functors $j_*$ and $j_!$ across categorical contexts {#ecag-0204}

The functors $j_*$ (direct image) and $j_!$ (extension by zero / proper direct image) appear in several settings with related but distinct meanings.

**Ordinary sheaf theory.** For an open immersion $j: U \hookrightarrow X$:

- $j_*\mathscr{F}$ is the direct image: $(j_*\mathscr{F})(V) = \mathscr{F}(V \cap U)$.
- $j_!\mathscr{F}$ is extension by zero: $(j_!\mathscr{F})(V) = \{s \in \mathscr{F}(V \cap U) \mid \operatorname{supp}(s) \text{ is closed in } V\}$.
- There is a natural inclusion $j_!\mathscr{F} \hookrightarrow j_*\mathscr{F}$.

**Higher derived functors.** $R^k j_*\mathscr{F}$ is the sheafification of $V \mapsto H^k(V \cap U, \mathscr{F})$. Since $j_!$ is exact for open immersions, $R^k j_! = 0$ for $k > 0$.

**Derived category.** For $A^\bullet \in D^b_c(U)$, $Rj_*$ and $j_! = Rj_!$ (for open $j$) are related by Verdier duality: $\mathbb{D}(Rj_* A^\bullet) \cong j_!(\mathbb{D}A^\bullet)$.

**Recollement triangles.** For $j: U \hookrightarrow X$ open with closed complement $i: Z \hookrightarrow X$, any sheaf $\mathscr{F}$ on $X$ fits in the short exact sequence $0 \to j_!j^*\mathscr{F} \to \mathscr{F} \to i_*i^*\mathscr{F} \to 0$. In the derived category, the corresponding distinguished triangles are:

$$
j_! j^* A^\bullet \to A^\bullet \to Ri_* i^* A^\bullet \xrightarrow{[1]}
$$

$$
i_* i^! A^\bullet \to A^\bullet \to Rj_* j^* A^\bullet \xrightarrow{[1]}.
$$

These are dual to each other under Verdier duality: applying $\mathbb{D}$ to the first yields the second (using $\mathbb{D} \circ j_! \cong Rj_* \circ \mathbb{D}$ and $\mathbb{D} \circ i_* \cong i_* \circ \mathbb{D}$, $i^! \cong \mathbb{D} \circ i^* \circ \mathbb{D}$).

**$K$-theory.** For a proper morphism $f: X \to Y$, the $K$-theoretic pushforward $f_!: K_0(X) \to K_0(Y)$ is $f_!([\mathscr{F}]) = \sum_i (-1)^i [R^i f_*\mathscr{F}]$. Properness ensures the higher direct images are coherent.

<!-- BENCHMARK_PROBLEM: Let $j: U \to X$ be an open immersion with closed complement $i: Z \to X$. Write down the two distinguished triangles relating $j_!, j^*, Rj_*, i_*, i^*, Ri_*, i^!$ in $D^b_c(X)$, and verify they are interchanged by Verdier duality. -->

### Example: Non-degeneration of the Leray spectral sequence {#ecag-0205}

The Leray spectral sequence $E_2^{p,q} = H^p(Y, R^q f_*\mathbb{Q}) \Rightarrow H^{p+q}(X, \mathbb{Q})$ for a smooth proper morphism $f: X \to Y$ does not always degenerate at $E_2$, contrary to what one might expect from the algebraic setting.

**The Hopf surface.** Let $X = (\mathbb{C}^2 \setminus \{0\})/\langle z \mapsto 2z \rangle$. This compact complex surface fibers over $\mathbb{P}^1$ via $f: X \to \mathbb{P}^1$, with elliptic curve fibers. The fundamental group is $\pi_1(X) \cong \mathbb{Z}$ (generated by the contracting loop), so $b_1(X) = 1$.

Since $b_1$ is odd, $X$ cannot be Kahler (for compact Kahler manifolds, $b_1$ is even by the Hodge decomposition $H^1 \cong H^{1,0} \oplus H^{0,1}$ with $h^{1,0} = h^{0,1}$).

If the Leray spectral sequence for $f$ degenerated at $E_2$, then $H^1(X, \mathbb{Q})$ would be a quotient of $E_2^{1,0} \oplus E_2^{0,1} = H^1(\mathbb{P}^1, f_*\mathbb{Q}) \oplus H^0(\mathbb{P}^1, R^1 f_*\mathbb{Q})$. We have $H^1(\mathbb{P}^1, \mathbb{Q}) \cong \mathbb{Q}^2$ and $R^1 f_*\mathbb{Q}$ is a local system of rank 2 on $\mathbb{P}^1$. The dimension count from degeneration is incompatible with $b_1(X) = 1$.

The essential point is that Deligne's degeneration theorem requires the morphism to be algebraic (or at least that the total space admits a Kahler metric). The Hopf surface is a purely holomorphic, non-algebraic example where degeneration fails.

<!-- BENCHMARK_PROBLEM: The Hopf surface $X = (\mathbb{C}^2 \setminus \{0\})/\langle z \mapsto 2z \rangle$ fibers over $\mathbb{P}^1$ with elliptic curve fibers. Compute $b_1(X)$, explain why $X$ is not Kahler, and use this to argue that the Leray spectral sequence for $f: X \to \mathbb{P}^1$ does not degenerate at $E_2$. -->

### Remark: Deligne's degeneration theorem {#ecag-0206}

Deligne's theorem (1968) states that for a smooth projective morphism $f: X \to Y$ of algebraic varieties over $\mathbb{C}$, the Leray spectral sequence

$$
E_2^{p,q} = H^p(Y, R^q f_*\mathbb{Q}) \Rightarrow H^{p+q}(X, \mathbb{Q})
$$

degenerates at $E_2$. The proof uses the Hard Lefschetz theorem on the fibers: a relative ample class $\eta \in H^2(X, \mathbb{Q})$ acts on $R^q f_*\mathbb{Q}$ via the Lefschetz operator, and the resulting decomposition into primitive parts gives a splitting of the spectral sequence. This was vastly generalized by the decomposition theorem of Beilinson--Bernstein--Deligne--Gabber (1982), which handles arbitrary proper morphisms (allowing singular fibers) using perverse sheaves and intersection cohomology.

<!-- BENCHMARK_PROBLEM: State Deligne's degeneration theorem for smooth projective morphisms. Explain the role of the Hard Lefschetz theorem on fibers in the proof, and state how the BBDG decomposition theorem generalizes it to proper morphisms with singular fibers. -->

### Example: Pathologies of non-abelian categories {#ecag-0207}

Several basic properties of abelian categories fail in additive categories that are not abelian. Three illustrative pathologies:

**Kernels may not exist.** In the category of finitely generated modules over $R = k[x_1, x_2, \ldots]$ (polynomial ring in infinitely many variables), the projection $\pi: R \to k = R/(x_1, x_2, \ldots)$ has kernel $(x_1, x_2, \ldots)$, which is not finitely generated. So $\ker(\pi)$ does not exist in the category of finitely generated $R$-modules.

**Cokernels may not exist.** In the category of free abelian groups, the map $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$ has cokernel $\mathbb{Z}/2\mathbb{Z}$ in $\operatorname{Ab}$, but $\mathbb{Z}/2\mathbb{Z}$ is not free. No free abelian group satisfies the universal property: if $G$ is free and $\varphi: \mathbb{Z} \to G$ satisfies $\varphi(2n) = 0$ for all $n$, then $2\varphi(1) = 0$, forcing $\varphi(1) = 0$ since $G$ is torsion-free. So the only map $\mathbb{Z} \to G$ annihilating the image of $\times 2$ is zero, but the zero group fails the universal property (the quotient map $\mathbb{Z} \to \mathbb{Z}/2$ is nonzero).

**Zero kernel and cokernel do not imply isomorphism.** In the category of filtered vector spaces, let $V = k$ with $F^0 V = V, F^1 V = 0$, and $W = k$ with $F^0 W = W, F^1 W = W$. The identity map $\operatorname{id}: V \to W$ has trivial kernel and cokernel (as filtered spaces), but it is not an isomorphism: its inverse $W \to V$ does not preserve the filtration (it would need $F^1 V \supseteq F^1 W = W$, but $F^1 V = 0$).

These pathologies show why the axioms of an abelian category -- existence of all kernels and cokernels, and the condition that every monic is a kernel and every epic is a cokernel -- are precisely what is needed for homological algebra.

<!-- BENCHMARK_PROBLEM: In the category of free abelian groups, prove that the map $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$ has no cokernel by showing that no free abelian group satisfies the universal property. -->

### Example: Exactness in sheaves versus presheaves {#ecag-0208}

The Euler sequence on $\mathbb{P}^1$, twisted by $\mathcal{O}(-1)$:

$$
0 \to \mathcal{O}(-2) \to \mathcal{O}(-1) \oplus \mathcal{O}(-1) \to \mathcal{O} \to 0
$$

is exact as a sequence of sheaves (checked on stalks) but not exact as a sequence of presheaves.

For presheaf exactness, the sequence of sections over every open set $U$ would need to be exact. Taking $U = \mathbb{P}^1$:

| Sheaf | $H^0(\mathbb{P}^1, -)$ |
|-------|------------------------|
| $\mathcal{O}(-2)$ | $0$ |
| $\mathcal{O}(-1) \oplus \mathcal{O}(-1)$ | $0$ |
| $\mathcal{O}$ | $k$ |

The global sections sequence $0 \to 0 \to 0 \to k \to 0$ fails to be exact at the last nonzero term: the surjection $\mathcal{O}(-1)^2 \to \mathcal{O}$ induces the zero map $0 \to k$ on global sections, which is not surjective.

The discrepancy is resolved by sheafification: the map $\mathcal{O}(-1)^2 \to \mathcal{O}$ is surjective on stalks (equivalently, every point has a neighborhood where the map is surjective), but global surjectivity fails because $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k \neq 0$. The long exact sequence in cohomology gives $H^0(\mathcal{O}(-1)^2) \to H^0(\mathcal{O}) \to H^1(\mathcal{O}(-2)) \to \cdots$, and the obstruction to surjectivity on global sections is precisely $H^1$ of the kernel.

<!-- BENCHMARK_PROBLEM: Show that the surjection $\mathcal{O}(-1)^2 \to \mathcal{O}$ on $\mathbb{P}^1$ is not surjective as a map of presheaves by computing global sections. Identify the cohomological obstruction to global surjectivity using the long exact sequence. -->

### Example: Derived functors and derived categories {#ecag-0209}

The derived category $D^b(\mathcal{A})$ of an abelian category $\mathcal{A}$ is constructed in two steps: first, form the homotopy category $K^b(\mathcal{A})$ by identifying chain-homotopic morphisms; second, formally invert quasi-isomorphisms.

A left-exact functor $F: \mathcal{A} \to \mathcal{B}$ (with $\mathcal{A}$ having enough injectives) has a total right derived functor $\mathbf{R}F: D^+(\mathcal{A}) \to D^+(\mathcal{B})$, computed by replacing an object by an injective resolution and applying $F$ termwise. The classical derived functors are recovered as $R^i F(A) = H^i(\mathbf{R}F(A))$.

**Example: sheaf cohomology.** For the global sections functor $\Gamma(X, -)$, the derived functor $\mathbf{R}\Gamma(X, \mathcal{F})$ is a complex whose $i$-th cohomology is $H^i(X, \mathcal{F})$.

**Tilting and derived equivalence.** For a finite-dimensional algebra $A$ and a tilting module $T$ (i.e., $\operatorname{pd}(T) \leq 1$, $\operatorname{Ext}^1_A(T, T) = 0$, and $T$ generates $K^b(\operatorname{proj}(A))$), the tilting theorem gives an equivalence $D^b(\operatorname{mod}(A)) \cong D^b(\operatorname{mod}(\operatorname{End}_A(T)))$. This provides explicit equivalences between derived categories of different abelian categories, showing that the derived category retains strictly less information than the abelian category.

<!-- BENCHMARK_PROBLEM: Let $A = k[x]/(x^2)$. Describe the bounded derived category $D^b(\operatorname{mod}(A))$ by listing the indecomposable objects (up to shift) and the morphism spaces between them. -->

### Example: Non-isomorphic abelian categories with equivalent derived categories {#ecag-0210}

**Quiver example.** Let $A$ be the path algebra of $1 \to 2$ over $k$. The category $\operatorname{mod}(A)$ has two simple modules $S_1, S_2$ and one non-simple indecomposable $P_1 = \begin{smallmatrix} k \\ \downarrow \\ k \end{smallmatrix}$ (the projective cover of $S_1$). Let $B$ be the path algebra of the opposite quiver $2 \to 1$.

The module $T = S_2 \oplus P_1$ is a tilting module for $A$: it has projective dimension $\leq 1$ (since $S_2$ has a projective resolution $0 \to P_1 \to P_2 \to S_2 \to 0$), $\operatorname{Ext}^1_A(T, T) = 0$, and the number of non-isomorphic indecomposable summands equals the number of simples. One verifies $\operatorname{End}_A(T) \cong B$. The Rickard--Happel theorem then gives $D^b(\operatorname{mod}(A)) \cong D^b(\operatorname{mod}(B))$, even though $\operatorname{mod}(A) \not\cong \operatorname{mod}(B)$ as abelian categories (their Auslander--Reiten quivers differ).

**Geometric example.** Mukai showed that for an abelian variety $A$ over $\mathbb{C}$, there is an equivalence $D^b(\operatorname{Coh}(A)) \cong D^b(\operatorname{Coh}(\hat{A}))$, where $\hat{A} = \operatorname{Pic}^0(A)$ is the dual abelian variety. The equivalence is given by the Fourier--Mukai transform with kernel the Poincare line bundle $\mathcal{P}$ on $A \times \hat{A}$:

$$
\Phi_\mathcal{P}: D^b(\operatorname{Coh}(A)) \xrightarrow{\sim} D^b(\operatorname{Coh}(\hat{A})), \quad \mathscr{F} \mapsto \mathbf{R}p_{2,*}(p_1^*\mathscr{F} \otimes^L \mathcal{P}).
$$

For a generic abelian variety, $A \not\cong \hat{A}$, so $\operatorname{Coh}(A) \not\cong \operatorname{Coh}(\hat{A})$, yet the derived categories are equivalent. This shows that derived equivalence is strictly weaker than equivalence of abelian categories.

<!-- BENCHMARK_PROBLEM: Let $A$ be the path algebra of $1 \to 2$ over a field $k$. Construct a tilting module $T \in \operatorname{mod}(A)$ with $\operatorname{End}_A(T)$ isomorphic to the path algebra $B$ of $2 \to 1$. Verify that $T$ satisfies the three conditions for a tilting module. -->

### Example: Derived global sections and derived pushforward {#ecag-0211}

The two fundamental derived functors in sheaf theory are derived global sections $\mathbf{R}\Gamma$ and derived pushforward $\mathbf{R}f_*$.

**For a single sheaf $\mathscr{F}$ on $X$:** choose an injective resolution $\mathscr{F} \xrightarrow{\sim} I^\bullet$. Then $\mathbf{R}\Gamma(X, \mathscr{F}) = \Gamma(X, I^\bullet)$ with $H^i(\mathbf{R}\Gamma(X, \mathscr{F})) = H^i(X, \mathscr{F})$.

**For a complex $A^\bullet \in D^b(X)$:** replace by an injective complex $A^\bullet \xrightarrow{\sim} I^\bullet$ (via Cartan--Eilenberg resolution). Then $\mathbf{R}\Gamma(X, A^\bullet) = \Gamma(X, I^\bullet)$ with $H^i(\mathbf{R}\Gamma(X, A^\bullet)) = \mathbb{H}^i(X, A^\bullet)$ (hypercohomology).

**Derived pushforward:** for $f: X \to Y$ and $\mathscr{F}$ on $X$, $\mathbf{R}f_*\mathscr{F} = f_*(I^\bullet)$ with cohomology sheaves $\mathcal{H}^i(\mathbf{R}f_*\mathscr{F}) = R^i f_*\mathscr{F}$.

**Composition and the Leray spectral sequence.** The isomorphism $\mathbf{R}\Gamma(Y, -) \circ \mathbf{R}f_* \cong \mathbf{R}\Gamma(X, -)$ recovers the Leray spectral sequence $E_2^{p,q} = H^p(Y, R^q f_*\mathscr{F}) \Rightarrow H^{p+q}(X, \mathscr{F})$ upon passage to cohomology.

**Projection formula.** For $f: X \to Y$ proper, $\mathscr{F} \in D^b(X)$, $\mathscr{G} \in D^b(Y)$:

$$
\mathbf{R}f_*(\mathscr{F} \otimes^L f^*\mathscr{G}) \cong \mathbf{R}f_*\mathscr{F} \otimes^L \mathscr{G}.
$$

**Base change.** For $f: X \to Y$ proper with $\mathscr{F}$ on $X$ flat over $Y$, the base change map $(R^i f_*\mathscr{F})_y \otimes k(y) \to H^i(X_y, \mathscr{F}|_{X_y})$ is an isomorphism when $R^i f_*\mathscr{F}$ is locally free, or more generally when $h^i(X_y, \mathscr{F}|_{X_y})$ is constant as a function of $y$.

<!-- BENCHMARK_PROBLEM: Let $f: X \to Y$ be a proper morphism of smooth projective varieties and $\mathscr{F}$ a coherent sheaf on $X$ flat over $Y$. State the base change theorem relating $(R^i f_*\mathscr{F})_y$ to $H^i(X_y, \mathscr{F}|_{X_y})$, and give a sufficient condition for the base change map to be an isomorphism. -->

### Remark: Derived functors, spectral sequences, and hypercohomology {#ecag-0212}

Given a left-exact functor $F: \mathcal{A} \to \mathcal{B}$ (with $\mathcal{A}$ having enough injectives), the derived functor $\mathbf{R}F: D^+(\mathcal{A}) \to D^+(\mathcal{B})$ produces a complex in $D^+(\mathcal{B})$. The classical derived functors are $R^i F(A) = H^i(\mathbf{R}F(A))$.

When applied to a complex $A^\bullet$ rather than a single object, two spectral sequences arise:

$$
{}^{I}E_2^{p,q} = R^p F(\mathcal{H}^q(A^\bullet)) \Rightarrow H^{p+q}(\mathbf{R}F(A^\bullet))
$$

$$
{}^{II}E_2^{p,q} = \mathcal{H}^p(\mathbf{R}F(A^q)) \Rightarrow H^{p+q}(\mathbf{R}F(A^\bullet))
$$

The target $H^n(\mathbf{R}F(A^\bullet))$ is the **hypercohomology** $\mathbb{H}^n(A^\bullet)$ when $F = \Gamma(X, -)$. The first spectral sequence is the Grothendieck spectral sequence for composition of derived functors; the second comes from the double complex obtained by applying $F$ to an injective Cartan--Eilenberg resolution of $A^\bullet$.

<!-- BENCHMARK_PROBLEM: Let $A^\bullet = [\mathscr{F} \xrightarrow{d} \mathscr{G}]$ be a two-term complex of coherent sheaves on a projective variety $X$ (with $\mathscr{F}$ in degree 0). Write out the first spectral sequence converging to $\mathbb{H}^n(X, A^\bullet)$, identifying the $E_2$ terms in terms of $H^i(X, \ker d)$, $H^i(X, \operatorname{im} d)$, and $H^i(X, \operatorname{coker} d)$. -->

### Example: Perverse truncation on smooth and two-stratum varieties {#ecag-0213}

**Smooth case.** On a smooth variety $X$ of dimension $d$, a constructible complex $A^\bullet$ lies in ${}^p D^{\leq 0}$ if and only if $\mathcal{H}^j(A^\bullet) = 0$ for $j > -d$, i.e., $A^\bullet[-d] \in D^{\leq 0}$ in the standard $t$-structure. Thus the perverse $t$-structure is the standard $t$-structure shifted by $\dim X$, and perverse sheaves on a smooth variety are simply local systems placed in degree $-d$.

**Two-stratum case.** Let $X = U \sqcup Z$ with $j: U \hookrightarrow X$ open of dimension $n$ and $i: Z \hookrightarrow X$ closed of dimension $m$. The perverse $t$-structure is obtained by gluing the shifted standard $t$-structures on each stratum: $A^\bullet \in {}^p D^{\leq 0}$ if and only if

- $\mathcal{H}^k(j^* A^\bullet) = 0$ for $k > -n$, and
- $\mathcal{H}^k(i^* A^\bullet) = 0$ for $k > -m$.

The perverse truncation ${}^p\tau_{\leq 0} A^\bullet$ is constructed via the distinguished triangle ${}^p\tau_{\leq 0} A^\bullet \to A^\bullet \to {}^p\tau_{\geq 1} A^\bullet \xrightarrow{[1]}$. In the two-stratum setting, this can be computed explicitly: first take the standard truncation $\tau_{\leq -n}(j^* A^\bullet)$ on $U$, then glue with the appropriate truncation on $Z$ using the recollement formalism.

The perverse cohomology ${}^p H^0(A^\bullet) = {}^p\tau_{\leq 0}\, {}^p\tau_{\geq 0} A^\bullet$ is a perverse sheaf encoding how the cohomology of $A^\bullet|_U$ extends across $Z$.

<!-- BENCHMARK_PROBLEM: Let $X$ be a variety with stratification $X = U \cup Z$ where $U$ is smooth open of dimension 2 and $Z$ is a smooth closed point. For the constant sheaf complex $\mathbb{Q}_X[2]$, check whether it satisfies the support and cosupport conditions. Is $\mathbb{Q}_X[2]$ a perverse sheaf? Compute ${}^p H^0(\mathbb{Q}_X[2])$. -->

### Example: Normal sheaf versus restricted normal sheaf {#ecag-0214}

For a closed subscheme $Z \subset X$ with ideal sheaf $\mathcal{I}_Z$, the normal sheaf $\mathcal{N}_{Z/X} = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{I}_Z/\mathcal{I}_Z^2, \mathcal{O}_X)$ and the restricted normal sheaf $\mathcal{N}_{Z/X}|_Z = \mathcal{H}om_{\mathcal{O}_Z}(\mathcal{I}_Z/\mathcal{I}_Z^2, \mathcal{O}_Z)$ can have very different global sections. The latter computes the Zariski tangent space to the Hilbert scheme.

**Basic example.** Let $R = \mathbb{C}[x]$ and $I = (x)$, so $Z = \{0\} \subset \mathbb{A}^1$. Then $I/I^2 \cong R/I \cong \mathbb{C}$ as an $R$-module (generated by $\bar{x}$). For any $f \in \operatorname{Hom}_R(I/I^2, R)$, the element $f(\bar{x}) \in R$ must satisfy $xf(\bar{x}) = f(x\bar{x}) = f(\overline{x^2}) = 0$ (since $x^2 \in I^2$). Since $R$ is a domain, $f(\bar{x}) = 0$. Therefore

$$
\operatorname{Hom}_R(I/I^2, R) = 0.
$$

However, restricting to $R/I$:

$$
\operatorname{Hom}_{R/I}(I/I^2, R/I) = \operatorname{Hom}_\mathbb{C}(\mathbb{C}, \mathbb{C}) \cong \mathbb{C}.
$$

**Hilbert scheme tangent space.** The Zariski tangent space to $\operatorname{Hilb}(X)$ at $[Z]$ is

$$
T_{[Z]} \operatorname{Hilb}(X) = \operatorname{Hom}_{\mathcal{O}_Z}(\mathcal{I}_Z/\mathcal{I}_Z^2, \mathcal{O}_Z) = H^0(\mathcal{N}_{Z/X}|_Z)
$$

-- note the $\operatorname{Hom}$ is over $\mathcal{O}_Z$, not $\mathcal{O}_X$.

**Torus action on $\operatorname{Hilb}^n(\mathbb{C})$.** For $I = (x^n) \subset \mathbb{C}[x]$, the module $I/I^2 \cong \mathbb{C}[x]/(x^n)$ has $\operatorname{Hom}_{\mathbb{C}[x]/(x^n)}(I/I^2, \mathbb{C}[x]/(x^n)) \cong \mathbb{C}[x]/(x^n)$ as a vector space. Under the $\mathbb{C}^*$-action $x \mapsto tx$, the tangent space decomposes as

$$
T_{(x^n)} \operatorname{Hilb}^n(\mathbb{C}) = t \oplus t^2 \oplus \cdots \oplus t^n
$$

as a representation of $\mathbb{C}^*$. This matches the global coordinates on $\operatorname{Hilb}^n(\mathbb{C}) \cong \mathbb{C}^n$: each ideal $I = (f)$ with $f = x^n + a_1 x^{n-1} + \cdots + a_n$ is parametrized by $(a_1, \ldots, a_n)$, and the weight of $a_i$ under $x \mapsto tx$ is $t^i$.

<!-- BENCHMARK_PROBLEM: Let $R = \mathbb{C}[x]$ and $I = (x^n)$. Compute $\operatorname{Hom}_R(I/I^2, R)$ and $\operatorname{Hom}_{R/I}(I/I^2, R/I)$. Use the latter to determine $\dim T_{(x^n)} \operatorname{Hilb}^n(\mathbb{C})$, and describe the $\mathbb{C}^*$-weight decomposition of the tangent space. -->
