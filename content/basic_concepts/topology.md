---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/topology.tex
---

## Topology
### \'{Etale  related}

### Example: \'{E}tale fundamental group of the nodal curve $y^{2}=x^{2}(x+1)$ {#ecag-0179}

Let $C \subset \mathbb{A}^2_k$ be the cubic curve defined by $y^2 = x^2(x+1)$ over an algebraically closed field $k$ with $\operatorname{char} k \neq 2$. This curve has an ordinary double point (node) at the origin: the polynomial $f = x^2(x+1) - y^2$ satisfies $f(0,0) = 0$, and both partial derivatives vanish there since $\partial f/\partial x = 3x^2 + 2x$ and $\partial f/\partial y = -2y$. The Hessian at the origin is $\begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$, which has two distinct eigenvalues (here $\operatorname{char} k \neq 2$ is essential), confirming the singularity is an ordinary node with two distinct tangent directions $y = \pm x$.

We will show that $\pi_1^{\text{\'et}}(C, \bar{c}) \cong \widehat{\mathbb{Z}}$, the profinite completion of $\mathbb{Z}$, when $\operatorname{char} k = 0$.

The normalization $\nu: \widetilde{C} \to C$ resolves the node. To compute it explicitly, substitute $y = tx$ into the defining equation to get $t^2 x^2 = x^2(x+1)$, so $x = t^2 - 1$ and $y = t(t^2 - 1)$ for points away from the origin. This defines a morphism $\mathbb{A}^1_k \to C$ sending $t \mapsto (t^2-1, \, t(t^2-1))$, which is birational and finite, hence is the normalization. The preimage of the node $(0,0)$ consists of the two points $t = 1$ and $t = -1$, since $t^2 - 1 = 0$ has exactly these roots.

Scheme-theoretically, $C$ is the pushout of the diagram $\{1, -1\} \hookrightarrow \mathbb{A}^1_k$: we obtain $C$ from $\widetilde{C} \cong \mathbb{A}^1_k$ by gluing the points $t = 1$ and $t = -1$ together. By the van Kampen theorem for étale fundamental groups (SGA 1, Exposé IX), the fundamental group of $C$ fits into a sequence determined by the fundamental groups of $\widetilde{C}$ and the gluing data. Over an algebraically closed field of characteristic zero, $\pi_1^{\text{\'et}}(\mathbb{A}^1_k) = 0$ (the affine line is simply connected), so the only source of non-trivial covering data is the identification of the two preimage points.

Concretely, every connected finite étale cover of $C$ of degree $n$ corresponds to a trivial cover of $\mathbb{A}^1_k$ (since $\pi_1^{\text{\'et}}(\mathbb{A}^1_k) = 0$, there are no non-trivial connected étale covers) together with a gluing datum at the node. The trivial cover of degree $n$ is $\coprod_{i=1}^{n} \mathbb{A}^1_k$, and the gluing must identify the $n$ points lying over $t = 1$ with the $n$ points lying over $t = -1$. A connected cover arises precisely when this identification is a cyclic permutation, i.e., an element of order $n$ in $S_n$. The isomorphism classes of such covers are classified by $\mathbb{Z}/n\mathbb{Z}$, and passing to the inverse limit over all $n$ gives
$$
\pi_1^{\text{\'et}}(C, \bar{c}) \cong \varprojlim_n \mathbb{Z}/n\mathbb{Z} = \widehat{\mathbb{Z}}.
$$

This result has a transparent topological analogy. Over $\mathbb{C}$, the analytification $C^{\text{an}}$ is homeomorphic to a pinched torus: the normalization $\widetilde{C}^{\text{an}} \cong \mathbb{C}$ is contractible, and identifying two distinct points creates a space homotopy equivalent to $S^1$. The topological fundamental group is $\pi_1(S^1) = \mathbb{Z}$, and profinite completion gives $\widehat{\mathbb{Z}}$, consistent with our computation.

In positive characteristic $p \neq 2$, the affine line $\mathbb{A}^1_k$ is no longer simply connected (see {#ecag-0181}), so the normalization $\widetilde{C}$ contributes additional covers via Artin--Schreier extensions. The tame fundamental group (classifying covers of degree prime to $p$) remains $\widehat{\mathbb{Z}}^{(p')} = \prod_{\ell \neq p} \mathbb{Z}_\ell$, but the full wild fundamental group acquires a large pro-$p$ part from the Artin--Schreier covers of $\mathbb{A}^1_k$.

<!-- BENCHMARK_PROBLEM: Let $C$ be the nodal cubic $y^2 = x^2(x+1)$ over $\overline{\mathbb{Q}}$. Compute $\pi_1^{\text{\'et}}(C, \bar{c})$ by analyzing the normalization $\widetilde{C} \to C$, the preimage of the node, and the resulting classification of finite étale covers. Explain what changes if the base field has characteristic $p > 2$. -->

### Example: Hartshorne $\mathrm{III}.10.5$, \'{e}tale locally free implies Zariski locally free {#ecag-0180}

Let $X$ be a Noetherian scheme and $\mathscr{F}$ a coherent sheaf on $X$. If there exists a faithfully flat étale morphism $f: U \to X$ such that $f^*\mathscr{F} \cong \mathcal{O}_U^r$, then $\mathscr{F}$ is locally free of rank $r$ in the Zariski topology.

The argument proceeds by constructing a local trivialization of $\mathscr{F}$ at each point $x \in X$ and then using faithful flatness to descend. Fix $x \in X$. Since $f^*\mathscr{F}$ has constant rank $r$, the sheaf $\mathscr{F}$ itself has rank $r$ at every point (rank is preserved under flat pullback). By Nakayama's lemma, we can choose sections $s_1, \ldots, s_r \in \mathscr{F}(V)$ on some Zariski neighborhood $V$ of $x$ that generate the fiber $\mathscr{F}_x / \mathfrak{m}_x \mathscr{F}_x \cong k(x)^r$. These sections define a surjection
$$
\varphi: \mathcal{O}_V^r \twoheadrightarrow \mathscr{F}|_V
$$

(surjectivity at $x$ by construction, and surjectivity extends to a Zariski neighborhood by coherence). Let $K = \ker(\varphi)$, so we have the exact sequence
$$
0 \to K \to \mathcal{O}_V^r \xrightarrow{\varphi} \mathscr{F}|_V \to 0.
$$

Since $f$ is flat, pullback preserves exactness:
$$
0 \to f^*K \to \mathcal{O}_{f^{-1}(V)}^r \xrightarrow{f^*\varphi} f^*\mathscr{F}|_{f^{-1}(V)} \to 0.
$$

By hypothesis $f^*\mathscr{F} \cong \mathcal{O}_U^r$, so $f^*\varphi$ is a surjection $\mathcal{O}_{f^{-1}(V)}^r \twoheadrightarrow \mathcal{O}_{f^{-1}(V)}^r$ between free sheaves of the same rank. At any point $u \in f^{-1}(V)$, tensoring with the residue field $k(u)$ gives a surjective linear map $k(u)^r \to k(u)^r$, which is necessarily an isomorphism by dimension counting. Therefore $(f^*K) \otimes k(u) = 0$, and by Nakayama's lemma applied to the finitely generated $\mathcal{O}_{U,u}$-module $(f^*K)_u$, we conclude $(f^*K)_u = 0$.

Since this holds at every point $u \in f^{-1}(V)$, we have $f^*K = 0$. Now faithful flatness enters: because $f$ is faithfully flat (étale and surjective), the functor $f^*$ reflects zero objects, so $f^*K = 0$ implies $K = 0$. Therefore $\varphi: \mathcal{O}_V^r \xrightarrow{\sim} \mathscr{F}|_V$ is an isomorphism, and $\mathscr{F}$ is free of rank $r$ on the Zariski open set $V$.

Since $x$ was arbitrary, $\mathscr{F}$ is Zariski locally free of rank $r$.

It is worth isolating exactly what the proof requires of $f$. The étale hypothesis is used in two ways: flatness (to pull back exact sequences) and surjectivity (to ensure faithful flatness for the descent step $f^*K = 0 \Rightarrow K = 0$). The proof works verbatim for any faithfully flat morphism $f: U \to X$ of finite presentation, not just étale ones. In particular, it applies to fppf covers. The key point is that Nakayama's lemma is a purely local argument on $U$, requiring no special structure of $f$ beyond flatness. Only the final descent step requires faithful flatness (= flat + surjective). The word "étale" could be replaced by "faithfully flat and quasi-compact" throughout.

<!-- BENCHMARK_PROBLEM: In the proof that étale locally free implies Zariski locally free (Hartshorne III.10.5), identify exactly where Nakayama's lemma is applied and where faithful flatness is used. Determine the minimal hypothesis on $f: U \to X$: is the full étale condition necessary, or does the proof work for any faithfully flat morphism of finite presentation? -->

### Example: $\mathbb{A}^{1}$ is not algebraically simply connected {#ecag-0181}

Over an algebraically closed field $k$ of characteristic $p > 0$, the affine line $\mathbb{A}^1_k$ admits non-trivial connected finite étale covers, so $\pi_1^{\text{\'et}}(\mathbb{A}^1_k, \bar{a}) \neq 0$. The simplest example is the Artin--Schreier morphism
$$
\varphi: \mathbb{A}^1_k \to \mathbb{A}^1_k, \quad t \mapsto t^p - t.
$$

On coordinate rings, $\varphi$ corresponds to $k[x] \hookrightarrow k[t]$ via $x \mapsto t^p - t$, making $k[t]$ a free $k[x]$-module of rank $p$.

The morphism $\varphi$ is étale because the derivative of $t^p - t$ with respect to $t$ is $pt^{p-1} - 1 = -1$ (since $\operatorname{char} k = p$), which is a unit everywhere. Equivalently, the extension $k(t)/k(t^p - t)$ is separable of degree $p$, and the module of relative differentials $\Omega_{k[t]/k[x]}$ vanishes since $dt = d(t^p - t) \cdot (-1)^{-1}$, confirming étaleness.

The fiber over any closed point $x = a \in k$ consists of the roots of $t^p - t - a = 0$. If $t_0$ is one root, then $t_0 + c$ is also a root for every $c \in \mathbb{F}_p$, since
$$
(t_0 + c)^p - (t_0 + c) = t_0^p + c^p - t_0 - c = (t_0^p - t_0) + (c^p - c) = a + 0 = a,
$$

where we used $c^p = c$ for $c \in \mathbb{F}_p$. Since the polynomial $t^p - t - a$ has $p$ distinct roots $\{t_0, t_0 + 1, \ldots, t_0 + (p-1)\}$ (distinctness follows from separability, or directly from the fact that the differences $c \in \mathbb{F}_p$ are distinct), every fiber has exactly $p$ geometric points. Combined with étaleness, this confirms $\varphi$ is a finite étale cover of degree $p$.

The cover is connected because $k[t]$ is a domain (equivalently, $t^p - t - x$ is irreducible over $k(x)$ by the Artin--Schreier criterion: a polynomial $T^p - T - \alpha$ over a field of characteristic $p$ is either irreducible or splits completely, and it splits completely only if $\alpha = \beta^p - \beta$ for some $\beta$ in the field, which fails for $\alpha = x \in k(x)$). The Galois group is $\mathbb{Z}/p\mathbb{Z}$ acting by translations $t \mapsto t + c$ for $c \in \mathbb{F}_p$.

| Property | Verification |
|----------|-------------|
| Finite | $k[t]$ is a free $k[x]$-module of rank $p$ (basis: $1, t, t^2, \ldots, t^{p-1}$) |
| Étale | $\frac{d}{dt}(t^p - t) = -1 \neq 0$ everywhere |
| Connected | $t^p - t - x$ is irreducible over $k(x)$ by Artin--Schreier theory |
| Galois | $\operatorname{Gal}(k(t)/k(x)) \cong \mathbb{Z}/p\mathbb{Z}$ via $t \mapsto t + 1$ |
| Non-trivial | Degree $p > 1$ |

The existence of this cover shows $\pi_1^{\text{\'et}}(\mathbb{A}^1_k) \neq 0$, in stark contrast to characteristic zero where $\pi_1^{\text{\'et}}(\mathbb{A}^1_k) = 0$. The full structure of $\pi_1^{\text{\'et}}(\mathbb{A}^1_k)$ in characteristic $p$ is far richer: by Abhyankar's conjecture (proved by Raynaud for the affine line in 1994 and Harbater in general), a finite group $G$ is a quotient of $\pi_1^{\text{\'et}}(\mathbb{A}^1_k)$ if and only if $G$ is quasi-$p$, meaning $G$ is generated by its $p$-Sylow subgroups (equivalently, $G$ has no non-trivial quotient of order prime to $p$). For instance, when $p = 2$, the groups $S_n$, $A_n$, $\operatorname{GL}_n(\mathbb{F}_{2^m})$, and all simple groups of Lie type in characteristic 2 are quotients of $\pi_1^{\text{\'et}}(\mathbb{A}^1_k)$.

<!-- BENCHMARK_PROBLEM: Prove that the Artin--Schreier map $\varphi: \mathbb{A}^1_k \to \mathbb{A}^1_k$ given by $t \mapsto t^p - t$ (where $k$ is algebraically closed of characteristic $p > 0$) is a connected finite étale Galois cover with group $\mathbb{Z}/p\mathbb{Z}$. Verify étaleness by computing the derivative, prove connectedness using the Artin--Schreier irreducibility criterion, and explicitly describe the Galois action on fibers. -->

### Remark: $\mathbb{P}_{K}^{1}$ is algebraically simply connected {#ecag-0182}

Over a separably closed field $K$, the projective line $\mathbb{P}^1_K$ is algebraically simply connected: $\pi_1^{\text{\'et}}(\mathbb{P}^1_K, \bar{x}) = 0$. This follows from the Riemann--Hurwitz formula by a genus argument.

Suppose $f: C \to \mathbb{P}^1_K$ is a connected finite étale cover of degree $d$, where $C$ is a smooth projective curve over $K$ (smoothness and projectivity follow from $f$ being finite étale over a smooth projective base). The Riemann--Hurwitz formula gives
$$
2g(C) - 2 = d \cdot (2g(\mathbb{P}^1) - 2) + \deg R = d \cdot (-2) + \deg R,
$$

where $R$ is the ramification divisor. Since $f$ is étale, there is no ramification, so $\deg R = 0$ and
$$
2g(C) - 2 = -2d, \quad \text{hence} \quad g(C) = 1 - d.
$$

Since $g(C) \geq 0$ for any smooth projective curve, we must have $d \leq 1$. But $d \geq 1$ as $f$ is a cover, so $d = 1$ and $f$ is an isomorphism. Since every connected finite étale cover of $\mathbb{P}^1_K$ is trivial, $\pi_1^{\text{\'et}}(\mathbb{P}^1_K, \bar{x}) = 0$.

Note that this argument applies in all characteristics, including characteristic $p > 0$: the Riemann--Hurwitz formula for étale covers (where the ramification term vanishes) requires no characteristic hypothesis. The contrast with $\mathbb{A}^1_k$ in characteristic $p$ is instructive. The Artin--Schreier cover $t \mapsto t^p - t$ on $\mathbb{A}^1_k$ is étale, but it does not extend to an étale cover of $\mathbb{P}^1_k$. Indeed, the map extends to a morphism $\mathbb{P}^1 \to \mathbb{P}^1$ of degree $p$, but it ramifies (wildly) at the point at infinity: in the coordinate $s = 1/t$, the map becomes $s \mapsto s^p/(1 - s^{p-1})$, which has a critical point at $s = 0$. So the Riemann--Hurwitz obstruction forces any finite cover of $\mathbb{P}^1$ to ramify somewhere, preventing non-trivial étale covers, while the affine line evades this constraint by allowing ramification "at infinity."

The hypothesis that $K$ is separably closed is essential. Over a field $K$ that is not separably closed, there can be non-trivial finite étale covers of $\mathbb{P}^1_K$ arising from the arithmetic fundamental group. The étale fundamental group fits into the exact sequence
$$
1 \to \pi_1^{\text{\'et}}(\mathbb{P}^1_{\bar{K}}) \to \pi_1^{\text{\'et}}(\mathbb{P}^1_K) \to \operatorname{Gal}(K^{\text{sep}}/K) \to 1.
$$

Since $\pi_1^{\text{\'et}}(\mathbb{P}^1_{\bar{K}}) = 0$ (the geometric fundamental group vanishes by the argument above), this collapses to
$$
\pi_1^{\text{\'et}}(\mathbb{P}^1_K) \cong \operatorname{Gal}(K^{\text{sep}}/K),
$$

which is highly non-trivial for, say, a number field $K$. In this case, the non-trivial étale covers of $\mathbb{P}^1_K$ are forms: they are curves $C$ over $K$ that become isomorphic to $\mathbb{P}^1$ over $\bar{K}$ but are not isomorphic to $\mathbb{P}^1$ over $K$ itself (e.g., smooth conics without a $K$-rational point).

<!-- BENCHMARK_PROBLEM: Using the Riemann--Hurwitz formula, prove that $\mathbb{P}^1_K$ has no non-trivial connected finite étale covers when $K$ is separably closed. Then explain why the Artin--Schreier cover of $\mathbb{A}^1_k$ in characteristic $p > 0$ does not contradict this: show explicitly that it ramifies at infinity when extended to $\mathbb{P}^1_k$. -->

### Remark: Sheaf cohomology, Zariski topology,  étale topology {#ecag-0183}

The choice of Grothendieck topology on a scheme profoundly affects sheaf cohomology, and the simplest example already exhibits a dramatic divergence: for $\mathbb{P}^1$ over an algebraically closed field $k$ of characteristic zero and the constant sheaf $\underline{\mathbb{Z}/\ell\mathbb{Z}}$ (with $\ell$ invertible in $k$), we have
$$
H^2_{\operatorname{Zar}}(\mathbb{P}^1, \underline{\mathbb{Z}/\ell\mathbb{Z}}) = 0 \quad \text{but} \quad H^2_{\text{\'et}}(\mathbb{P}^1, \underline{\mathbb{Z}/\ell\mathbb{Z}}) \cong \mathbb{Z}/\ell\mathbb{Z}.
$$

The Zariski vanishing follows from Grothendieck's vanishing theorem: for a Noetherian topological space $X$ of dimension $n$, $H^i_{\operatorname{Zar}}(X, \mathscr{F}) = 0$ for all $i > n$ and any sheaf of abelian groups $\mathscr{F}$. Since $\mathbb{P}^1$ has Zariski dimension 1, all $H^i_{\operatorname{Zar}}$ vanish for $i \geq 2$, regardless of the coefficient sheaf. This theorem rests on the fact that any Zariski open cover of $X$ can be refined to one with at most $n+1$ elements (by the combinatorial structure of the Zariski topology on a Noetherian space of dimension $n$), which bounds the cohomological dimension.

The étale non-vanishing arises because the Grothendieck vanishing theorem does not apply to the étale site. The étale topology is not a topology on the underlying topological space of $X$; rather, it is a Grothendieck topology on the category of étale $X$-schemes, and the notion of "dimension" relevant for cohomological vanishing is the étale cohomological dimension $\operatorname{cd}_\ell(X)$. For a smooth projective variety $X$ of dimension $n$ over an algebraically closed field, $\operatorname{cd}_\ell(X) = 2n$ (by the étale Poincaré duality theorem), so $\mathbb{P}^1$ has étale cohomological dimension 2 with respect to $\ell$-torsion sheaves. More precisely, the étale cohomology of $\mathbb{P}^1$ with $\ell$-torsion coefficients is

| $i$ | $H^i_{\text{\'et}}(\mathbb{P}^1, \mathbb{Z}/\ell\mathbb{Z})$ | Analogy with $S^2$ |
|-----|----------------------------------------------|---------------------|
| 0 | $\mathbb{Z}/\ell\mathbb{Z}$ | $H^0(S^2, \mathbb{Z}) \cong \mathbb{Z}$ |
| 1 | $0$ | $H^1(S^2, \mathbb{Z}) = 0$ |
| 2 | $\mathbb{Z}/\ell\mathbb{Z}$ | $H^2(S^2, \mathbb{Z}) \cong \mathbb{Z}$ |

This matches the singular cohomology of $\mathbb{P}^1(\mathbb{C}) \cong S^2$ via the Artin comparison theorem, which asserts that for a smooth variety $X$ over $\mathbb{C}$ and a finite abelian group $\Lambda$, there is a canonical isomorphism $H^i_{\text{\'et}}(X, \underline{\Lambda}) \cong H^i_{\text{sing}}(X(\mathbb{C}), \Lambda)$.

The Čech-theoretic perspective further illuminates the divergence. For quasi-coherent sheaves on separated schemes, Čech cohomology with respect to an affine open cover computes the correct sheaf cohomology in the Zariski topology (Leray's theorem / Serre's criterion). The standard cover $\mathbb{P}^1 = U_0 \cup U_1$ with $U_i \cong \mathbb{A}^1$ gives the familiar computation $H^1_{\operatorname{Zar}}(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$ via the Čech complex. But the constant sheaf $\underline{\mathbb{Z}/\ell\mathbb{Z}}$ is not quasi-coherent, and Leray's theorem does not apply to it. In fact, on a connected scheme $X$, every Zariski open subset $U$ is also connected (for irreducible $X$), so $\Gamma(U, \underline{\mathbb{Z}/\ell\mathbb{Z}}) = \mathbb{Z}/\ell\mathbb{Z}$ for every non-empty Zariski open $U$, and the Čech complex for any Zariski cover collapses to give trivial higher cohomology. The Zariski topology is simply too coarse -- its open sets are too large and too connected -- to detect the "topological" cohomology captured by the étale topology.

In the étale topology, the relevant covers are surjective étale morphisms $U \to X$, and the Čech-to-derived-functor spectral sequence
$$
\check{H}^p(\mathfrak{U}, \mathscr{H}^q(\mathscr{F})) \Rightarrow H^{p+q}_{\text{\'et}}(X, \mathscr{F})
$$

(where $\mathscr{H}^q(\mathscr{F})$ denotes the presheaf $V \mapsto H^q_{\text{\'et}}(V, \mathscr{F}|_V)$) can be used to compute étale cohomology. For torsion sheaves on Noetherian schemes, Čech cohomology agrees with derived-functor cohomology in the étale topology under mild hypotheses (Artin's theorem), but the covers involved are genuine étale covers, not merely Zariski opens. It is through these finer covers that the étale topology accesses the "topological" information of the underlying variety.

<!-- BENCHMARK_PROBLEM: Explain why $H^2_{\operatorname{Zar}}(\mathbb{P}^1, \underline{\mathbb{Z}/\ell\mathbb{Z}}) = 0$ (citing the Grothendieck vanishing theorem and the Zariski dimension of $\mathbb{P}^1$) while $H^2_{\text{\'et}}(\mathbb{P}^1, \underline{\mathbb{Z}/\ell\mathbb{Z}}) \cong \mathbb{Z}/\ell\mathbb{Z}$ for $\ell$ invertible in an algebraically closed base field. Why does the Grothendieck vanishing theorem fail in the étale setting, and what is the correct cohomological dimension bound for étale cohomology of smooth projective varieties? -->
