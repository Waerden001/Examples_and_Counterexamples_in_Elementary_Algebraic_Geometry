---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/sheaves_and_bundles.tex
---

## Sheaves and bundles

### Example: Constant sheaf, not quasi-coherent; skyscraper sheaf, not quasi-coherent {#ecag-0165}

**Statement:** Let $k$ be a field. The following hold:

1. The skyscraper sheaf $k$ on $\mathbb{A}^1_k = \operatorname{Spec}(k[T])$, supported at the origin, is a quasi-coherent sheaf (it is the sheaf associated to the module $k[T]/(T)$).
2. The skyscraper sheaf $k(T)$ on $\mathbb{A}^1_k = \operatorname{Spec}(k[T])$, supported at the origin, is **not** a quasi-coherent sheaf.
3. The constant sheaf $\underline{k}$ on $\mathbb{P}^1_k = \operatorname{Proj}(k[x,y])$ is **not** a quasi-coherent sheaf.
4. More generally, the constant sheaf $\underline{k}$ on a scheme $X$ is almost never quasi-coherent.
5. The constant sheaf $\underline{k}$ on any irreducible topological space is always flasque, so for any open cover $\mathfrak{U}$ we have $\check{H}^i(\mathfrak{U}, \underline{k}) = 0$ for all $i \geq 1$.

**Construction/Proof:**

For (1): The skyscraper sheaf supported at the origin with stalk $k$ is isomorphic to $\widetilde{M}$ where $M = k[T]/(T)$, viewed as a $k[T]$-module. This is manifestly quasi-coherent.

For (2): Suppose for contradiction that the skyscraper sheaf $\mathscr{F}$ with stalk $k(T)$ at the origin were quasi-coherent on $\mathbb{A}^1_k = \operatorname{Spec}(k[T])$. Then $\mathscr{F} = \widetilde{M}$ for some $k[T]$-module $M$. We have $M = \Gamma(\mathbb{A}^1_k, \mathscr{F}) = k(T)$ since the only nonempty open set containing the origin is $\mathbb{A}^1_k$ itself among those contributing to global sections. But $\widetilde{k(T)}$ is the constant sheaf with value $k(T)$ on all nonempty open subsets of $\mathbb{A}^1_k$ (since $k(T)$ is a divisible $k[T]$-module, localization does not change it). In particular, $\widetilde{k(T)}$ has stalk $k(T)$ at the generic point, whereas the skyscraper sheaf has stalk $0$ at the generic point. Contradiction.

For (3): On $\mathbb{P}^1_k$, cover by $U_0 = \operatorname{Spec}(k[t])$ and $U_1 = \operatorname{Spec}(k[t^{-1}])$ with $U_0 \cap U_1 = \operatorname{Spec}(k[t, t^{-1}])$. If $\underline{k}$ were quasi-coherent, its sections over $U_0 \cap U_1$ would be determined by its sections over $U_0$ and $U_1$ via localization. But $\underline{k}(U_0) = k$, $\underline{k}(U_1) = k$, and $\underline{k}(U_0 \cap U_1) = k$ (since $U_0 \cap U_1$ is connected in the Zariski topology of $\mathbb{P}^1$). For a quasi-coherent sheaf $\widetilde{M}$ on $U_0$ with $\widetilde{M}(U_0) = k$ as a $k[t]$-module, we would need $\widetilde{M}(U_0 \cap U_1) = k \otimes_{k[t]} k[t, t^{-1}] = k[t,t^{-1}]/(t) = 0$, not $k$. This is a contradiction.

For (5): On an irreducible topological space, every nonempty open set is dense and connected. The constant sheaf $\underline{k}$ assigns $k$ to every nonempty open set. The restriction maps are all the identity $\operatorname{id}_k$. For any inclusion of nonempty open sets $V \subset U$, the restriction $\underline{k}(U) \to \underline{k}(V)$ is surjective, which is precisely the definition of a flasque sheaf. Flasque sheaves are acyclic for the Cech functor.

**Key Insight:** Quasi-coherence is a strong algebraic condition: sections over open subsets are determined by localization. Constant sheaves, whose sections depend only on the topology (connectedness), typically fail this algebraic compatibility.

**Prerequisites:** Quasi-coherent sheaves, skyscraper sheaves, constant sheaves, flasque sheaves, Cech cohomology

<!-- BENCHMARK_PROBLEM: Let $k$ be a field and let $\mathscr{F}$ be the skyscraper sheaf on $\mathbb{A}^1_k = \operatorname{Spec}(k[T])$ with stalk $k(T)$ supported at the origin $(T)$. Prove that $\mathscr{F}$ is not quasi-coherent by showing that no $k[T]$-module $M$ satisfies $\widetilde{M} \cong \mathscr{F}$. -->

### Remark: Sheaf cohomology, Zariski topology, étale topology {#ecag-0166}

The choice of topology fundamentally affects sheaf cohomology, even for simple sheaves on simple spaces. Key observations:

1. **Grothendieck vanishing:** For a Noetherian topological space $X$ of dimension $n$ and any sheaf of abelian groups $\mathscr{F}$ on $X$ (in the Zariski topology), we have $H^i(X, \mathscr{F}) = 0$ for all $i > n$. This applies in the Zariski topology but **not** in the étale topology. Concretely:

$$
H^2_{\mathrm{Zar}}(\mathbb{P}^1, \underline{k}) = 0, \quad H^2_{\text{ét}}(\mathbb{P}^1, \underline{k}) \cong k.

$$

The Zariski vanishing follows from $\dim(\mathbb{P}^1) = 1$ and Grothendieck's theorem. The étale computation reflects the richer topology of the étale site.

2. **Cech cohomology depends on topology:** For $\mathbb{P}^1 = U_0 \cup U_1$ (the standard affine cover), the Cech complex for the constant sheaf $\underline{k}$ involves sections over $U_0$, $U_1$, and $U_0 \cap U_1$. The cover is not fine (i.e., not acyclic for $\underline{k}$) in either Zariski or étale topology. However, the Cech-to-derived-functor spectral sequence

$$
\check{H}^p(\mathfrak{U}, \mathscr{H}^q(\mathscr{F})) \Rightarrow H^{p+q}(X, \mathscr{F})

$$

can still be used to compute the sheaf cohomology from the Cech data, relating the Cech cohomology of the presheaf cohomology groups to the true sheaf cohomology.

<!-- BENCHMARK_PROBLEM: Explain why $H^2_{\mathrm{Zar}}(\mathbb{P}^1_k, \underline{k}) = 0$ using the Grothendieck vanishing theorem, and state the precise hypothesis on $X$ and $\mathscr{F}$ that is required. -->

### Example: Locally free module v.s. locally free sheaf; why we need Noetherian condition {#ecag-0167}

**Statement:** The notions of "locally free module" and "locally free sheaf" do not coincide in general. Precisely:

1. For any ring $R$ and $R$-module $M$, the associated sheaf $\mathscr{F} = \widetilde{M}$ on $\operatorname{Spec}(R)$ is locally free as a sheaf of $\mathcal{O}_{\operatorname{Spec}(R)}$-modules if and only if $M$ is a projective $R$-module.
2. A finitely generated module $M$ over a Noetherian ring $R$ is projective if and only if $M$ is locally free (i.e., $M_{\mathfrak{p}}$ is a free $R_{\mathfrak{p}}$-module for all primes $\mathfrak{p}$).
3. Without the Noetherian hypothesis, a locally free module (in the sense of all localizations being free) need not be projective, hence $\widetilde{M}$ need not be a locally free sheaf.

**Construction/Proof:**

For (1): If $M$ is projective, then $M$ is a direct summand of a free module $F$, so $\widetilde{M}$ is a direct summand of $\widetilde{F}$, which is free. Since projective modules over local rings are free (by Kaplansky's theorem), $\widetilde{M}_{\mathfrak{p}} \cong \widetilde{M_{\mathfrak{p}}}$ is free for each $\mathfrak{p}$, giving local freeness. The converse: if $\widetilde{M}$ is locally free, there exists a cover of $\operatorname{Spec}(R)$ by basic open sets $D(f_i)$ such that $M_{f_i}$ is free over $R_{f_i}$. One can show using the patching property of projective modules that $M$ is projective.

For (2): Over a Noetherian ring, a finitely generated module is projective if and only if it is locally free (Serre's criterion), because the rank function $\mathfrak{p} \mapsto \operatorname{rank}_{R_{\mathfrak{p}}}(M_{\mathfrak{p}})$ is locally constant on $\operatorname{Spec}(R)$, and finite generation plus local freeness give projectivity via Nakayama's lemma and lifting of bases.

For (3): See ecag-0170 for an explicit example of a locally free module that is not projective, demonstrating the necessity of the Noetherian (or at least finite generation) hypothesis.

**Key Insight:** The Noetherian condition ensures that the algebraic notion (locally free stalks) and the geometric notion (locally trivial sheaf on a Zariski cover) agree. Without it, the Zariski topology may be too coarse to detect projectivity from stalk-wise freeness.

**Prerequisites:** Projective modules, locally free modules, Noetherian rings, Nakayama's lemma, Kaplansky's theorem

<!-- BENCHMARK_PROBLEM: Let $R$ be a ring and $M$ an $R$-module. Prove that $\widetilde{M}$ is locally free as a sheaf on $\operatorname{Spec}(R)$ if and only if $M$ is a projective $R$-module. State where the Noetherian hypothesis would be needed if one instead required only that $M_{\mathfrak{p}}$ is free for all $\mathfrak{p} \in \operatorname{Spec}(R)$. -->

### Remark: Coherent sheaf $\Leftrightarrow$ finitely generated module, Hartshorne $\mathrm{II}.5.5$ {#ecag-0168}

A sheaf of $\mathcal{O}_X$-modules $\mathscr{F}$ on a scheme $X$ is **coherent** if it is of finite type and for every open $U \subseteq X$ and every morphism $\mathcal{O}_U^n \to \mathscr{F}|_U$, the kernel is of finite type. On an affine scheme $\operatorname{Spec}(R)$ with $R$ Noetherian, coherent sheaves correspond exactly to finitely generated $R$-modules (Hartshorne II.5.5). What makes this work is the **finite generation of the kernel**: over a Noetherian ring, every submodule of a finitely generated module is finitely generated, so the kernel of any surjection $R^n \twoheadrightarrow M$ is automatically finitely generated. Without the Noetherian condition, finitely generated modules may fail to be coherent because the kernel of a presentation need not be finitely generated. For non-Noetherian rings, the correct replacement is the notion of **finitely presented** modules (those admitting an exact sequence $R^m \to R^n \to M \to 0$), which always give coherent sheaves.

<!-- BENCHMARK_PROBLEM: Give an example of a finitely generated module $M$ over a non-Noetherian ring $R$ such that $\widetilde{M}$ is not a coherent sheaf on $\operatorname{Spec}(R)$. Explain why finite generation of $M$ does not suffice for coherence without the Noetherian hypothesis. -->

### Example: A finitely generated flat module but not finitely presented, not flat {#ecag-0169}

**Statement:** Let $R = \prod_{i=1}^{\infty} \mathbb{F}_2$, the countably infinite product of copies of $\mathbb{F}_2$. Then:

1. $R$ is a von Neumann regular ring (every element $a$ satisfies $a = a^2 b$ for some $b \in R$), hence every finitely generated ideal is a direct summand and every $R$-module is flat.
2. However, $R$ is not Noetherian: the ideal $I = \bigoplus_{i=1}^{\infty} \mathbb{F}_2$ is not finitely generated.
3. The $R$-module $M = R/I$ is finitely generated (it is cyclic) and flat (since every $R$-module is flat over a von Neumann regular ring), but $M$ is **not** finitely presented, because $I = \ker(R \twoheadrightarrow R/I)$ is not finitely generated.

**Construction/Proof:**

To verify von Neumann regularity: for $a = (a_i) \in R$ with each $a_i \in \mathbb{F}_2$, define $b = a$ (since $a_i^2 = a_i$ in $\mathbb{F}_2$). Then $a^2 b = a^3 = a$ (as $a_i^3 = a_i$ in $\mathbb{F}_2$). Over a von Neumann regular ring, every module is flat: this follows because every finitely generated ideal is a direct summand, hence a flat module, and flatness can be tested on finitely generated ideals (by Lazard's criterion, or directly: $M$ is flat iff $\operatorname{Tor}_1^R(R/I, M) = 0$ for all finitely generated ideals $I$, and when $I$ is a direct summand, the Tor automatically vanishes).

The ideal $I = \bigoplus_{i=1}^{\infty} \mathbb{F}_2$ is not finitely generated: any finite subset of $I$ generates an ideal supported on finitely many coordinates, so cannot generate $I$. Thus $R/I$ is finitely generated but not finitely presented.

Note on the title: The phrase "not flat" in the title is a misnomer in this context; the point is that $M$ is flat but not finitely presented, showing that flatness and finite generation together do not imply finite presentation without Noetherian hypotheses.

**Key Insight:** Von Neumann regular rings make every module flat, but infinite products of fields are far from Noetherian, providing a rich source of flat-but-not-finitely-presented modules.

**Prerequisites:** Von Neumann regular rings, flat modules, finitely presented modules, Lazard's criterion

<!-- BENCHMARK_PROBLEM: Let $R = \prod_{i=1}^{\infty} \mathbb{F}_2$ and $I = \bigoplus_{i=1}^{\infty} \mathbb{F}_2 \subset R$. Prove that $R/I$ is a finitely generated flat $R$-module that is not finitely presented. You must verify that $R$ is von Neumann regular and that $I$ is not finitely generated. -->

### Example: Locally free module but not projective {#ecag-0170}

**Statement:** There exists a ring $R$ and an $R$-module $M$ such that $M_{\mathfrak{p}}$ is a free $R_{\mathfrak{p}}$-module for every prime ideal $\mathfrak{p}$ of $R$, yet $M$ is not a projective $R$-module.

**Construction/Proof:**

Let $R = \prod_{i=1}^{\infty} \mathbb{Z}$ (the countable product of copies of $\mathbb{Z}$), and let $M = \bigoplus_{i=1}^{\infty} \mathbb{Z}$, viewed as an $R$-module via the componentwise action (the $i$-th factor of $R$ acts on the $i$-th summand of $M$, and we embed $M \hookrightarrow R$ as the direct sum inside the direct product).

Alternatively, a cleaner classical example: let $R = \mathbb{Z}$ and $M = \mathbb{Q}$. Then $M$ is locally free: for every prime $p$, $M_p = \mathbb{Q} \otimes_{\mathbb{Z}} \mathbb{Z}_{(p)} = \mathbb{Q}$, which is a free $\mathbb{Q}$-module of rank 1 (here $\mathbb{Z}_{(p)}$ is the localization, and $\mathbb{Q}$ is the fraction field). Also $M_{(0)} = \mathbb{Q}$, free of rank 1 over $\mathbb{Q}$. However, $\mathbb{Q}$ is not a projective $\mathbb{Z}$-module: if it were, being torsion-free, it would be free (projective modules over a PID are free), but $\mathbb{Q}$ is not a free $\mathbb{Z}$-module (it is divisible, while a free abelian group on any set is not divisible).

Note: The expression $\mathbb{Z}[\ldots, \frac{1}{p}, \ldots]$ in the original formulation denotes $\mathbb{Q}$ (the ring obtained by inverting all primes), so this coincides with the original intent.

**Key Insight:** Stalk-wise freeness (a local condition at each prime) does not globalize to projectivity without finite generation or Noetherian hypotheses, because there is no uniform Zariski open cover on which the module trivializes.

**Prerequisites:** Projective modules, locally free modules, localization, modules over PIDs

<!-- BENCHMARK_PROBLEM: Prove that $\mathbb{Q}$ is a locally free $\mathbb{Z}$-module (i.e., $\mathbb{Q} \otimes_{\mathbb{Z}} \mathbb{Z}_{\mathfrak{p}}$ is free over $\mathbb{Z}_{\mathfrak{p}}$ for every prime ideal $\mathfrak{p}$ of $\mathbb{Z}$) but is not a projective $\mathbb{Z}$-module. -->

### Example: A (smooth) vector bundle but not a (holomorphic, algebraic) vector bundle, Shizhang & Zijun {#ecag-0171}

**Statement:** Consider the morphism

$$
\pi : X = \mathbb{P}^1 \times \mathbb{P}^1 \setminus \Delta \longrightarrow \mathbb{P}^1, \quad (x,y) \mapsto x,

$$

where $\Delta$ is the diagonal. Then:

1. Over $\mathbb{C}$, the map $\pi$ is a topological line bundle isomorphic to (the topologists') $\mathcal{O}_{\mathbb{P}^1}(-2)$.
2. The map $\pi$ is **not** an algebraic or holomorphic line bundle: it admits no algebraic (or holomorphic) section.
3. The total space $X$ is diffeomorphic to $\operatorname{Tot}(\mathcal{O}_{\mathbb{P}^1}(-2))^{\mathrm{an}}$.

**Construction/Proof:**

*Step 1: $X$ is affine, hence admits no algebraic section.*

The Segre embedding gives

$$
s : \mathbb{P}^1 \times \mathbb{P}^1 \hookrightarrow \mathbb{P}^3, \quad ([x_0, x_1], [y_0, y_1]) \mapsto [x_0 y_0, x_0 y_1, x_1 y_0, x_1 y_1].

$$

Denote coordinates on $\mathbb{P}^3$ by $[X, Y, Z, W]$. The diagonal $\Delta \subset \mathbb{P}^1 \times \mathbb{P}^1$ maps to the locus $\{Y = Z\}$ inside the Segre quadric $\{XW = YZ\}$. The complement $\mathbb{P}^1 \times \mathbb{P}^1 \setminus \Delta$ maps into the complement of the hyperplane $V(Y - Z)$ in $\mathbb{P}^3$, which is affine. Thus $X$ is a closed subvariety of an affine variety, hence affine.

If $\pi$ had an algebraic section $\sigma : \mathbb{P}^1 \to X$, then $\sigma$ would be a morphism from a projective variety to an affine variety. Since $\mathbb{P}^1$ is proper, the image of $\sigma$ would be a proper closed subvariety of $X$. But $\sigma$ composed with $\pi$ is the identity on $\mathbb{P}^1$, which is impossible: the composition $\mathbb{P}^1 \xrightarrow{\sigma} X \hookrightarrow \mathbb{A}^N$ is a non-constant morphism from a projective variety to an affine space, contradicting properness (the image must be a point). Hence no algebraic section exists.

*Step 2: Topological section and degree computation.*

Working over $\mathbb{C}$, we identify $\mathbb{P}^1(\mathbb{C}) \cong S^2$. There exists a continuous (but non-algebraic, non-holomorphic) section:

$$
\sigma : S^2 \to S^2 \times S^2 \setminus \Delta, \quad x \mapsto (x, -x),

$$

where $-x$ denotes the antipodal point. This is well-defined since $x \neq -x$ for the antipodal map (this uses the identification $S^2 \subset \mathbb{R}^3$).

To compute the degree of the topological line bundle, we compute the self-intersection number of the section $\sigma$ via intersection theory in differential topology.

*Step 3: Setting up coordinates.*

Give $S^2$ the standard complex structure via stereographic projection. Near the north pole $N$, use coordinates $(x, y)$; near the south pole $S$, use coordinates $(u, v)$ with transition functions:

$$
u = \frac{x}{x^2 + y^2}, \quad v = \frac{-y}{x^2 + y^2}.

$$

*Step 4: Perturbed section and intersection.*

Define a family of sections by perturbing via rotation about the polar axis by angle $t$:

$$
\sigma_t : S^2 \to S^2 \times S^2 \setminus \Delta, \quad x \mapsto (x, \rho_t(-x)),

$$

where $\rho_t$ is rotation by angle $t$ about the north-south axis. The intersection $\sigma \cap \sigma_t$ consists of two points: $p = (N, S)$ and $q = (S, N)$.

*Step 5: Index computation at $p = (N, S)$.*

Near $p$, in coordinates $(x, y, u, v)$ on $S^2 \times S^2$, the two sections are:

$$
\sigma : (x, y) \mapsto (x, y, -x, y),

$$

$$
\sigma_t : (x, y) \mapsto (x, y, -x \cos t + y \sin t, x \sin t + y \cos t).

$$

The intersection index at $p$ is given by the sign of the determinant of the Jacobian matrix:

$$
A = \begin{pmatrix} 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & -\cos t & \sin t \\ 0 & 1 & \sin t & \cos t \end{pmatrix}.

$$

Computing:

$$
\det(A) = -2 + \sin(2t).

$$

For small $t > 0$, we have $\sin(2t) < 2$, so $\det(A) < 0$. The intersection index at $p$ is $-1$.

*Step 6: Conclusion.*

The same computation at $q = (S, N)$ also gives intersection index $-1$. The total self-intersection number of the zero section is $(-1) + (-1) = -2$. Since the self-intersection number of the zero section of a line bundle $\mathcal{O}(d)$ on $S^2$ equals $d$, we conclude that $\pi : X \to \mathbb{P}^1$ is topologically the line bundle $\mathcal{O}_{\mathbb{P}^1}(-2)$.

**Key Insight:** The complement of the diagonal in $\mathbb{P}^1 \times \mathbb{P}^1$ is algebraically affine (so no projective variety can map non-trivially into it), yet topologically it fibers as a line bundle over $S^2$. The antipodal map provides a topological section that no algebraic or holomorphic map can replicate.

**Prerequisites:** Segre embedding, proper morphisms, topological vector bundles, intersection theory in differential topology, stereographic projection

<!-- BENCHMARK_PROBLEM: Let $X = \mathbb{P}^1_{\mathbb{C}} \times \mathbb{P}^1_{\mathbb{C}} \setminus \Delta$ with the projection $\pi : X \to \mathbb{P}^1_{\mathbb{C}}$ given by $(x,y) \mapsto x$. Prove that $\pi$ admits no algebraic section by showing $X$ is affine via the Segre embedding, and compute the topological degree of the bundle using the self-intersection number of the antipodal section to show it equals $-2$. -->

### Remark {#ecag-0172}

The section $\sigma : (x', y') \mapsto (x', y', -x', y')$ in local coordinates near $(N, S)$ should be read as follows: $(x', y')$ are coordinates on the source $S^2$ near the north pole $N$, and $(x, y, u, v)$ are coordinates on the target $S^2 \times S^2$ near $(N, S)$, where $(x, y)$ correspond to the first factor near $N$ and $(u, v)$ to the second factor near $S$. Thus the section is:

$$
\sigma : x = x', \; y = y', \; u = -x', \; v = y'.

$$

The minus sign in $u = -x'$ and the plus sign in $v = y'$ encode how the antipodal map acts in these particular local coordinates. One could alternatively compute the degree using de Rham cohomology: the Euler class of the bundle $\pi : X \to S^2$ can be computed as the pullback of the Thom class, and integrated over $S^2$ to give $-2$. This provides a coordinate-free verification.

### Remark: index, degree {#ecag-0173}

Several related notions of "index" and "degree" appear across differential topology and algebraic geometry. We collect them here for comparison:

1. **Fixed-point index of an automorphism.** For $f : X \to X$ a smooth map and $p \in \operatorname{Fix}(f)$ an isolated fixed point, the index is:

$$
i(p) := \operatorname{sign} \det(\operatorname{Id} - Df_p),

$$

where $Df_p : T_p X \to T_p X$ is the differential. This measures whether $f$ "repels" or "attracts" near $p$.

2. **Lefschetz number.** For $f : X \to X$ on a compact manifold:

$$
\Lambda(f) = \sum_{k} (-1)^k \operatorname{Tr}(f^* : H^k(X) \to H^k(X)).

$$

The **Lefschetz fixed-point theorem** asserts $\Lambda(f) = \sum_{p \in \operatorname{Fix}(f)} i(p)$ when the fixed points are isolated and nondegenerate.

3. **Index of a vector field.** For a vector field $v$ on a compact manifold $X$ with isolated zeros, the **Poincare-Hopf theorem** states $\sum_{p : v(p) = 0} \operatorname{ind}_p(v) = \chi(X)$, the Euler characteristic.

4. **Intersection index.** For smooth maps $f : X \to Y$ and $g : Z \to Y$ with $\dim X + \dim Z = \dim Y$, the intersection index at a transverse intersection point $p$ is the sign of the determinant of the combined differential.

5. **Degree of a smooth map** $f : X \to Y$ between compact oriented manifolds of the same dimension: $\deg(f) = \sum_{p \in f^{-1}(y)} \operatorname{sign}(\det Df_p)$ for a regular value $y$. In algebraic geometry, the degree of a dominant morphism $f : X \to Y$ of varieties is $[k(X) : k(Y)]$, the degree of the function field extension.

6. **Degree of the top Chern class.** For a rank-$r$ vector bundle $\mathscr{E}$ on a compact complex manifold $X$ of dimension $r$, $\deg(c_r(\mathscr{E})) = \int_X c_r(\mathscr{E})$ counts (with multiplicity) the zeros of a generic section.

7. **Intersection number** in differential topology (signed count of transverse intersections) vs. algebraic geometry ($\chi(\mathcal{O}_Z)$ or via Serre's Tor formula).

The unifying perspective: the degree of a smooth map $f : X \to Y$ equals the intersection index of the cycles $[X \times \{y\}]$ and $[\Gamma_f] = [(x, f(x))]$ in $X \times Y$. In particular, for $f : X \to X$, the Lefschetz number $\Lambda(f)$ equals the intersection number $[\Delta] \cdot [\Gamma_f]$ in $X \times X$.

<!-- BENCHMARK_PROBLEM: Let $f : S^2 \to S^2$ be the antipodal map $f(x) = -x$. Compute the Lefschetz number $\Lambda(f)$ using the cohomological trace formula, and verify it equals the sum of fixed-point indices (noting that $f$ has no fixed points). What does this tell you about the existence of fixed points? -->

### Example: a reflexive sheaf but not locally free {#ecag-0174}

**Statement:** There exist reflexive coherent sheaves that are not locally free. On a normal variety $X$ of dimension $\geq 2$, the pushforward of a line bundle from the smooth locus provides a natural source of such examples.

**Construction/Proof:**

Let $X = \operatorname{Spec}(k[x, y, z]/(xy - z^2))$ be the affine quadric cone over a field $k$ with $\operatorname{char}(k) \neq 2$. Let $\mathfrak{m} = (x, y, z) \subset R = k[x,y,z]/(xy - z^2)$ be the maximal ideal at the vertex (the singular point). Consider the ideal sheaf $\mathscr{I} = \widetilde{\mathfrak{m}}$.

*Step 1: $\mathscr{I}$ is reflexive.* The dual $\mathscr{I}^{\vee} = \mathscr{H}\!om(\mathscr{I}, \mathcal{O}_X)$ can be computed: since $X$ is normal and $\mathscr{I}$ is a rank-1 torsion-free sheaf, the double dual $\mathscr{I}^{\vee\vee}$ is a rank-1 reflexive sheaf. On a normal surface, reflexive rank-1 sheaves correspond to Weil divisor classes. One checks that $\mathfrak{m}^{\vee\vee} \cong \mathfrak{m}$ as $R$-modules (this can be verified by computing $\operatorname{Hom}_R(\mathfrak{m}, R)$ and then dualizing again), so $\mathscr{I}$ is reflexive.

*Step 2: $\mathscr{I}$ is not locally free.* If $\mathscr{I}$ were locally free at the vertex, then $\mathfrak{m}$ would be a free $R_{\mathfrak{m}}$-module, hence principal. But $R_{\mathfrak{m}}$ is a 2-dimensional local ring with singular point (the quadric cone has an $A_1$ singularity at the origin), so its maximal ideal cannot be principal (otherwise $R_{\mathfrak{m}}$ would be regular of dimension 1, contradicting $\dim R_{\mathfrak{m}} = 2$). Hence $\mathscr{I}$ is not locally free.

Alternatively, the class group $\operatorname{Cl}(X) \cong \mathbb{Z}/2\mathbb{Z}$, generated by the class of the Weil divisor corresponding to $\mathfrak{m}$. Since this class is non-trivial in $\operatorname{Cl}(X)$ but becomes trivial in $\operatorname{Pic}(X)$ only if it is Cartier, and the generator has order 2, $\mathfrak{m}$ represents a Weil divisor that is not Cartier, hence $\widetilde{\mathfrak{m}}$ is reflexive but not locally free.

**Key Insight:** On a normal variety, reflexive rank-1 sheaves correspond to Weil divisors, while locally free rank-1 sheaves correspond to Cartier divisors. The gap between the Weil class group $\operatorname{Cl}(X)$ and the Picard group $\operatorname{Pic}(X)$ is precisely the obstruction to reflexive sheaves being locally free.

**Prerequisites:** Reflexive sheaves, Weil divisors, Cartier divisors, class group, normal varieties, quadric cone

<!-- BENCHMARK_PROBLEM: Let $R = k[x,y,z]/(xy - z^2)$ where $\operatorname{char}(k) \neq 2$, and let $\mathfrak{m} = (x,y,z)$. Prove that $\widetilde{\mathfrak{m}}$ is a reflexive sheaf on $\operatorname{Spec}(R)$ that is not locally free by showing $\mathfrak{m}$ corresponds to a Weil divisor that is not Cartier, and that $\operatorname{Cl}(R) \cong \mathbb{Z}/2\mathbb{Z}$. -->

### Example: a coherent sheaf but not a quotient of locally free sheaf {#ecag-0175}

**Statement:** Let $n \geq 2$ and let $X = \overline{\mathbb{A}^n}$ be the affine $n$-space with doubled origin (obtained by gluing two copies of $\mathbb{A}^n_k$ along $\mathbb{A}^n_k \setminus \{0\}$). Then there exists a coherent sheaf on $X$ that is not a quotient of any locally free sheaf. Specifically, the ideal sheaf $\mathscr{I}$ of one of the two origins is coherent but not globally generated.

**Construction/Proof:**

*Step 1: Every locally free sheaf on $X$ is trivial.*

Let $U_0, U_1 \cong \mathbb{A}^n_k$ be the two copies, with $U_0 \cap U_1 = \mathbb{A}^n_k \setminus \{0\}$. By the Quillen-Suslin theorem, every finitely generated projective module over $k[x_1, \ldots, x_n]$ is free, so every locally free sheaf on $\mathbb{A}^n$ is trivial. A locally free sheaf $\mathscr{E}$ on $X$ is given by free sheaves $\mathscr{E}|_{U_0}$ and $\mathscr{E}|_{U_1}$ together with a gluing isomorphism $\varphi$ over $U_0 \cap U_1$. Since $n \geq 2$, the complement of the origin has codimension $\geq 2$, so

$$
\Gamma(\mathbb{A}^n \setminus \{0\}, \mathcal{O}) = \Gamma(\mathbb{A}^n, \mathcal{O}) = k[x_1, \ldots, x_n]

$$

by Hartogs' extension. Therefore $\varphi$ extends to an isomorphism over all of $\mathbb{A}^n$, and $\mathscr{E}$ is trivial.

*Step 2: "Every coherent sheaf is a quotient of locally free" implies $X$ is affine.*

If every coherent sheaf on $X$ were a quotient of a locally free sheaf, then since every locally free sheaf is trivial (hence isomorphic to $\mathcal{O}_X^{\oplus r}$), every coherent sheaf would be globally generated. By Serre's criterion, this would imply $\mathcal{O}_X$ is ample, which forces $H^i(X, \mathscr{F}) = 0$ for $i \geq 1$ and all coherent $\mathscr{F}$ (after twisting). By Serre's affineness criterion, $X$ would be affine. But $X$ is not affine (it is not separated: the two origins cannot be separated by global functions), giving a contradiction.

*Step 3: Explicit non-globally-generated coherent sheaf.*

Denote the two origins by $p \in U_0$ and $q \in U_1$. Consider the ideal sheaf $\mathscr{I}$ of the point $p$:

$$
\mathscr{I}(U_0) = (x_1, \ldots, x_n) \subset k[x_1, \ldots, x_n], \quad \mathscr{I}(U_1) = k[y_1, \ldots, y_n],

$$

with gluing $x_i \mapsto y_i$ on $U_0 \cap U_1$. The stalk $\mathscr{I}_q = \mathcal{O}_{X,q}$, so $1 \in \mathscr{I}_q$. However, any global section of $\mathscr{I}$ must be of the form $(f, f)$ where $f \in (x_1, \ldots, x_n)$ (from the $U_0$ side) and $f$ is the same polynomial on $U_1$ (by Hartogs, global sections on $X$ are pairs that agree on the overlap, and they extend uniquely). Thus every global section of $\mathscr{I}$ vanishes at $q$ as well, so $\mathscr{I}$ is not globally generated at $q$.

**Key Insight:** The doubled origin is not separated and not affine, yet every vector bundle on it is trivial (by Quillen-Suslin plus Hartogs). This creates coherent sheaves that cannot be globally generated, since their global sections cannot distinguish the two origins.

**Prerequisites:** Quillen-Suslin theorem, Hartogs' extension, Serre's affineness criterion, separated schemes, globally generated sheaves

<!-- BENCHMARK_PROBLEM: Let $X$ be the affine plane $\mathbb{A}^2_k$ with doubled origin. Prove that every locally free sheaf on $X$ is trivial by using the Quillen-Suslin theorem and Hartogs' extension, and then exhibit a specific coherent sheaf on $X$ that is not globally generated. -->

### Remark {#ecag-0176}

For well-behaved schemes, coherent sheaves are always quotients of locally free sheaves. Specifically:

- On a **quasi-projective** variety $X$ (over a Noetherian ring), every coherent sheaf is a quotient of a locally free sheaf. This follows because $X$ admits an ample line bundle $\mathcal{O}_X(1)$, and for any coherent $\mathscr{F}$, the twisted sheaf $\mathscr{F}(n)$ is globally generated for $n \gg 0$, giving a surjection $\mathcal{O}_X^{\oplus r} \twoheadrightarrow \mathscr{F}(n)$, hence $\mathcal{O}_X(-n)^{\oplus r} \twoheadrightarrow \mathscr{F}$.

More generally, the **resolution property** (every coherent sheaf is a quotient of a locally free sheaf) holds for quasi-projective schemes, Noetherian regular schemes (by a result of Kleiman), and smooth schemes over a field, but can fail for non-separated or non-quasi-projective schemes, as ecag-0175 demonstrates.

Further discussion can be found in [this MathOverflow thread](https://math.stackexchange.com/questions/849958/is-there-a-coherent-sheaf-which-is-not-a-quotient-of-locally-free-sheaf).

### Example: A universally closed morphism but not a closed embedding {#ecag-0177}

**Statement:** The following morphisms are universally closed (i.e., proper) but not closed embeddings:

1. The $n$-th power map $\mathbb{P}^1_k \to \mathbb{P}^1_k$, $z \mapsto z^n$, for $n \geq 2$.
2. The normalization morphism $\operatorname{Spec}(k[t]) \to \operatorname{Spec}(k[t^2, t^3])$.

**Construction/Proof:**

*Example 1:* The map $f : \mathbb{P}^1_k \to \mathbb{P}^1_k$ given in homogeneous coordinates by $[x : y] \mapsto [x^n : y^n]$ (equivalently, $z \mapsto z^n$ on the affine chart) is a finite morphism of degree $n$ between proper $k$-schemes. Finite morphisms are proper (they are affine and of finite type, and finiteness implies universally closed). For $n \geq 2$, this is not a closed embedding because it is not a monomorphism: the fiber over any point (other than $0$ and $\infty$) consists of $n$ points (the $n$-th roots), so the map is not injective on geometric points.

*Example 2:* The ring map $k[t^2, t^3] \hookrightarrow k[t]$ is an integral extension (since $t$ satisfies $t^2 - t^2 = 0$, i.e., $t$ is integral over $k[t^2, t^3]$), so $f : \operatorname{Spec}(k[t]) \to \operatorname{Spec}(k[t^2, t^3])$ is a finite (hence proper) morphism. It is the normalization of the cuspidal curve $y^2 = x^3$ (parametrized by $x = t^2, y = t^3$). The map is a bijection on points but is not a closed embedding: the corresponding ring map $k[t^2, t^3] \to k[t]$ is not surjective (equivalently, $f$ is not a closed immersion because the induced map on sheaves $\mathcal{O}_{\operatorname{Spec}(k[t^2,t^3])} \to f_* \mathcal{O}_{\operatorname{Spec}(k[t])}$ is not surjective — the element $t$ is not in $k[t^2, t^3]$).

**Key Insight:** Universally closed (properness) is about the topological behavior under base change, while being a closed embedding additionally requires injectivity at the level of structure sheaves. Finite morphisms of degree $> 1$ and non-trivial normalizations are the prototypical examples separating these notions.

**Prerequisites:** Proper morphisms, finite morphisms, closed embeddings, normalization, integral extensions

<!-- BENCHMARK_PROBLEM: Prove that the normalization morphism $\operatorname{Spec}(k[t]) \to \operatorname{Spec}(k[t^2, t^3])$ is universally closed but not a closed embedding. You must show it is finite (hence proper) and that the ring map $k[t^2, t^3] \hookrightarrow k[t]$ is not surjective. -->

### Example: constant fibre $\neq$ locally free {#ecag-0178}

**Statement:** A coherent sheaf $\mathscr{F}$ on a scheme $X$ can have constant fiber dimension $\dim_{k(\mathfrak{p})} \mathscr{F} \otimes k(\mathfrak{p})$ at every point $\mathfrak{p} \in X$ and yet fail to be locally free.

**Construction/Proof:**

Let $R = k[t]/(t^2)$ (the ring of dual numbers) and $X = \operatorname{Spec}(R)$, which is a single point $y = (t)$ with residue field $k(y) = k$. Consider the $R$-module $M = k[t]/(t) = k$, viewed as an $R$-module via the surjection $R \twoheadrightarrow k$.

The fiber dimension at the unique point $y$ is:

$$
\dim_{k(y)} (M \otimes_R k(y)) = \dim_k (k \otimes_{k[t]/(t^2)} k) = \dim_k k = 1,

$$

which is constant (trivially, since $X$ has a single point).

However, $M = k$ is **not** a free $R$-module: a free $R$-module of rank 1 is $R = k[t]/(t^2)$, which has $\dim_k = 2$, while $\dim_k M = 1$. More precisely, $M$ is not even flat over $R$: consider the exact sequence $0 \to (t) \to R \to k \to 0$. Tensoring with $M = k$ gives $(t) \otimes_R k \to k \to k \to 0$. Now $(t) \cong R/(t) = k$ as $R$-modules, so $(t) \otimes_R k \cong k \otimes_R k \cong k$, and the map $k \to k$ is the zero map (since $t$ acts as $0$ on $k$). Thus $\operatorname{Tor}_1^R(k, k) \cong k \neq 0$, so $M$ is not flat.

By Nakayama's lemma, the fiber dimension equals the minimal number of generators of $M_{\mathfrak{p}}$ over $R_{\mathfrak{p}}$. For a finitely generated module to be locally free, one additionally needs the module to be flat (or equivalently, the relations to vanish). The constant fiber dimension condition captures only the generation data, not the relations.

**Key Insight:** Constant fiber dimension guarantees only that the minimal number of generators is constant; local freeness additionally requires that there be no relations among these generators (i.e., flatness). Over non-reduced schemes, the distinction between "generated by $r$ elements" and "free of rank $r$" becomes visible even at a single point.

**Prerequisites:** Nakayama's lemma, flat modules, Tor functor, dual numbers, fiber dimension

<!-- BENCHMARK_PROBLEM: Let $R = k[t]/(t^2)$ and $M = k$ (viewed as an $R$-module via $t \mapsto 0$). Verify that $\dim_{k} (M \otimes_R k) = 1$ but $M$ is not free over $R$. Compute $\operatorname{Tor}_1^R(k, k)$ explicitly to show $M$ is not flat. -->
