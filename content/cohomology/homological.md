---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/homological.tex
---

## Homological algebra

### Example: $\mathrm{Hom}, \mathscr{H}om, \operatorname{Ext}^{i}_{A}(-,-), \mathscr{E}xt^{i}_{-}(-,-), \operatorname{Tor}^{i}_{-}(-,-)$ with Macaulay2 {#ecag-0227}

**Statement:** We illustrate the computation of the fundamental homological functors $\mathrm{Hom}$, $\mathscr{H}om$, $\operatorname{Ext}^{i}$, $\mathscr{E}xt^{i}$, and $\operatorname{Tor}_{i}$ using the computer algebra system Macaulay2. In particular, we compute $\mathscr{E}xt^{i}(\mathcal{O}_{L_1}, \mathcal{O}_{L_2})$ for two lines $L_1, L_2$ in $\mathbb{P}^3$.

**Construction/Proof:** Recall the key distinctions among these functors:

1. *Global Hom vs. sheaf Hom.* For an $A$-module $M$ and $N$, $\mathrm{Hom}_A(M, N)$ is the $A$-module of module homomorphisms. For sheaves $\mathscr{F}, \mathscr{G}$ on a scheme $X$, the sheaf $\mathscr{H}om(\mathscr{F}, \mathscr{G})$ is defined by $U \mapsto \operatorname{Hom}_{\mathcal{O}_X|_U}(\mathscr{F}|_U, \mathscr{G}|_U)$. One has $\Gamma(X, \mathscr{H}om(\mathscr{F}, \mathscr{G})) = \operatorname{Hom}_{\mathcal{O}_X}(\mathscr{F}, \mathscr{G})$.

2. *Ext as derived functor.* $\operatorname{Ext}^i_A(M, N)$ is the $i$-th right derived functor of $\mathrm{Hom}_A(M, -)$ (equivalently, of $\mathrm{Hom}_A(-, N)$). In Macaulay2, given a ring $R$, modules $M, N$, one computes $\operatorname{Ext}^i(M, N)$ via `Ext^i(M, N)`.

3. *Sheaf Ext.* $\mathscr{E}xt^i(\mathscr{F}, \mathscr{G})$ is the sheafification of the presheaf $U \mapsto \operatorname{Ext}^i_{\mathcal{O}_X(U)}(\mathscr{F}(U), \mathscr{G}(U))$. For coherent sheaves on projective space, Macaulay2 computes this via the module $\operatorname{Ext}^i_S(M, N)$ over the homogeneous coordinate ring $S$, then sheafifying.

4. *Tor.* $\operatorname{Tor}_i^A(M, N)$ is the $i$-th left derived functor of $M \otimes_A -$. In Macaulay2, one computes it via `Tor_i(M, N)`.

5. *Concrete example:* Let $L_1, L_2 \subset \mathbb{P}^3$ be two skew lines. In Macaulay2, set $S = k[x_0, x_1, x_2, x_3]$ and define ideals $I_1, I_2$ cutting out $L_1, L_2$. Then $\mathscr{E}xt^1(\mathcal{O}_{L_1}, \mathcal{O}_{L_2}) = 0$ (since the lines are disjoint), while $\mathscr{E}xt^2(\mathcal{O}_{L_1}, \mathcal{O}_{L_2})$ is computed from the module $\operatorname{Ext}^2_S(S/I_1, S/I_2)$. If the lines meet at a point $p$, then $\mathscr{E}xt^1(\mathcal{O}_{L_1}, \mathcal{O}_{L_2})$ is supported at $p$.

**References:**

- [Computing with sheaves and sheaf cohomology in algebraic geometry (Stillman, SWC 2006)](http://swc.math.arizona.edu/aws/2006/06StillmanNotes.pdf)
- [Computing with sheaves and sheaf cohomology in algebraic geometry (Stillman, Osaka 2015)](http://www.math.sci.osaka-u.ac.jp/~msj-si-2015/school_slides/stillman-day2.pdf)
- [$\mathscr{E}xt^{i}(\mathcal{O}_{L_{1}},\mathcal{O}_{L_{2}})$ for two lines $L_{1}, L_{2}$ in $\mathbb{P}^{3}$ (Math StackExchange)](https://math.stackexchange.com/questions/1550511/mathcalexti-mathcalo-l-1-mathcalo-l-2-and-textexti-mathc?rq=1)

**Key Insight:** The distinction between the global functor $\operatorname{Ext}^i$ and the sheaf functor $\mathscr{E}xt^i$ is crucial: $\operatorname{Ext}^i$ captures global extension classes while $\mathscr{E}xt^i$ captures local information and is itself a sheaf. Macaulay2 makes these abstract constructions computationally accessible, allowing explicit verification of vanishing and support conditions.

**Prerequisites:** Derived functors, Hom and tensor product of modules, coherent sheaves on projective space, Macaulay2 basics

<!-- BENCHMARK_PROBLEM: Let $L_1$ and $L_2$ be two disjoint lines in $\mathbb{P}^3_k$ over an algebraically closed field $k$. Show that $\mathscr{E}xt^1(\mathcal{O}_{L_1}, \mathcal{O}_{L_2}) = 0$. What is the support of $\mathscr{E}xt^1(\mathcal{O}_{L_1}, \mathcal{O}_{L_2})$ when $L_1$ and $L_2$ meet at a single point? -->

### Example: $\operatorname{Ext}^{1}$ and extension of vector bundles {#ecag-0228}

**Statement:** We classify extensions of line bundles on $\mathbb{P}^1$ via $\operatorname{Ext}^1$. Specifically, elements of $\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1}(-2), \mathcal{O}_{\mathbb{P}^1}(2))$ parametrize isomorphism classes of short exact sequences of vector bundles on $\mathbb{P}^1$.

**Construction/Proof:**

1. *Setup.* Let $X = \mathbb{P}^1_k$. Consider the Ext group

$$
\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1}(-2), \mathcal{O}_{\mathbb{P}^1}(2)).

$$

By the standard adjunction and Serre duality computation, we have

$$
\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1}(-2), \mathcal{O}_{\mathbb{P}^1}(2)) \cong H^1(\mathbb{P}^1, \mathcal{O}_{\mathbb{P}^1}(4)).

$$

Since $\deg(\mathcal{O}(4)) = 4 \geq 0$, by the standard cohomology of line bundles on $\mathbb{P}^1$ we get $H^1(\mathbb{P}^1, \mathcal{O}(4)) = 0$. Therefore

$$
\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1}(-2), \mathcal{O}_{\mathbb{P}^1}(2)) = 0.

$$

This means every short exact sequence $0 \to \mathcal{O}(2) \to \mathscr{E} \to \mathcal{O}(-2) \to 0$ splits, so $\mathscr{E} \cong \mathcal{O}(2) \oplus \mathcal{O}(-2)$.

2. *A nontrivial case.* Now consider

$$
\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1}(2), \mathcal{O}_{\mathbb{P}^1}(-2)) \cong H^1(\mathbb{P}^1, \mathcal{O}_{\mathbb{P}^1}(-4)).

$$

By Serre duality, $H^1(\mathbb{P}^1, \mathcal{O}(-4)) \cong H^0(\mathbb{P}^1, \mathcal{O}(2))^{\vee}$, which has dimension $3$. So there is a $3$-dimensional family of extensions

$$
0 \to \mathcal{O}(-2) \to \mathscr{E} \to \mathcal{O}(2) \to 0.

$$

By Grothendieck's theorem, every vector bundle on $\mathbb{P}^1$ splits as a direct sum of line bundles, so $\mathscr{E} \cong \mathcal{O}(a) \oplus \mathcal{O}(b)$ with $a + b = 0$. For the zero element in $\operatorname{Ext}^1$, we get the split extension $\mathscr{E} \cong \mathcal{O}(2) \oplus \mathcal{O}(-2)$. For a nonzero element, one can show $\mathscr{E} \cong \mathcal{O} \oplus \mathcal{O}$ or $\mathscr{E} \cong \mathcal{O}(1) \oplus \mathcal{O}(-1)$, depending on the specific extension class.

3. *Birkhoff-Grothendieck classification.* By Grothendieck's theorem, the middle term $\mathscr{E}$ of any extension on $\mathbb{P}^1$ must split. The constraint $\det(\mathscr{E}) = \mathcal{O}(a+b) = \mathcal{O}(-2+2) = \mathcal{O}$ forces $a + b = 0$. The possible bundles are $\mathcal{O}(n) \oplus \mathcal{O}(-n)$ for $n \geq 0$, subject to the constraint that $\mathscr{E}$ admits a surjection onto $\mathcal{O}(2)$, which forces $n \leq 2$.

**References:**

- [Vector bundles in $\operatorname{Ext}^{1}(\mathcal{O}_{\mathbb{P}^{1}}(-2), \mathcal{O}_{\mathbb{P}^{1}}(2))$ (Math StackExchange)](https://math.stackexchange.com/questions/1529355/vector-bundles-in-textext1-mathcalo-mathbbp12-mathcalo-math?rq=1)
- [Extensions of vector bundles on $\mathbb{P}^{1}$ (Math StackExchange)](https://math.stackexchange.com/questions/1601588/extension-of-vector-bundles-on-mathbbcp1?rq=1)

**Key Insight:** On $\mathbb{P}^1$, Grothendieck's splitting theorem rigidly constrains the middle terms of extensions. The vanishing or non-vanishing of $\operatorname{Ext}^1$ between line bundles is governed entirely by the cohomology of twist sheaves $\mathcal{O}(n)$, making $\mathbb{P}^1$ an ideal testing ground for extension computations.

**Prerequisites:** Cohomology of line bundles on $\mathbb{P}^1$, Serre duality, Grothendieck's splitting theorem, Ext groups as derived functors

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1}(a), \mathcal{O}_{\mathbb{P}^1}(b))$ as a function of $a, b \in \mathbb{Z}$. For which values of $a, b$ is this group nonzero? When it is nonzero, give its dimension over $k$. -->

### Remark {#ecag-0229}

This remark collects computations of $\operatorname{Ext}^1_{\mathbf{Z}}(A, B)$ for various abelian groups $A, B$, illustrating two key vanishing principles and the use of free resolutions.

**Vanishing principles.** $\operatorname{Ext}^1_{\mathbf{Z}}(A, B) = 0$ for any $B$ if $A$ is a free abelian group (since free modules are projective, so $\operatorname{Ext}^i$ vanishes for $i \geq 1$). Similarly, $\operatorname{Ext}^1_{\mathbf{Z}}(A, B) = 0$ for any $A$ if $B$ is divisible (i.e., $\forall b \in B$, $0 \neq n \in \mathbf{Z}$, $\exists b' \in B$ such that $nb' = b$), since divisible abelian groups are injective. Thus:

$$
\operatorname{Ext}^1(\mathbf{Z}, \mathbf{Z}) = 0, \quad \operatorname{Ext}^1(\mathbf{Z}, \mathbf{Q}) = 0

$$

$$
\operatorname{Ext}^1(\mathbf{Z}/n\mathbf{Z}, \mathbf{Q}) = 0, \quad \operatorname{Ext}^1(\mathbf{Q}, \mathbf{Q}) = 0.

$$

**Computation via free resolutions.** For $\mathbf{Z}/n\mathbf{Z}$, we have the free resolution

$$
0 \to \mathbf{Z} \xrightarrow{\cdot n} \mathbf{Z} \to \mathbf{Z}/n\mathbf{Z} \to 0.

$$

Applying $\operatorname{Hom}(-, \mathbf{Z})$ gives $0 \to \mathbf{Z} \xrightarrow{\cdot n} \mathbf{Z}$, whose cokernel is $\mathbf{Z}/n\mathbf{Z}$. Applying $\operatorname{Hom}(-, \mathbf{Z}/m\mathbf{Z})$ gives $0 \to \mathbf{Z}/m\mathbf{Z} \xrightarrow{\cdot n} \mathbf{Z}/m\mathbf{Z}$, whose cokernel is $\mathbf{Z}/\gcd(m,n)\mathbf{Z}$. Therefore:

$$
\operatorname{Ext}^1(\mathbf{Z}/n\mathbf{Z}, \mathbf{Z}) = \mathbf{Z}/n\mathbf{Z}, \quad \operatorname{Ext}^1(\mathbf{Z}/m\mathbf{Z}, \mathbf{Z}/n\mathbf{Z}) = \mathbf{Z}/\gcd(m,n)\mathbf{Z}.

$$

**Torsion-versus-divisibility argument.** To show $\operatorname{Ext}^1(\mathbf{Q}, \mathbf{Z}/m\mathbf{Z}) = 0$: take any free resolution of $\mathbf{Q}$ and apply $\operatorname{Hom}(-, \mathbf{Z}/m\mathbf{Z})$. Since $\mathbf{Z}/m\mathbf{Z}$ is $m$-torsion, $\operatorname{Ext}^1(\mathbf{Q}, \mathbf{Z}/m\mathbf{Z})$ is $m$-torsion. On the other hand, $\mathbf{Q}$ is a $\mathbf{Q}$-module, so the scalar multiplication by any nonzero integer $n$ on $\mathbf{Q}$ is an isomorphism. This induces an isomorphism on $\operatorname{Ext}^1(\mathbf{Q}, \mathbf{Z}/m\mathbf{Z})$ via functoriality, giving it a $\mathbf{Q}$-vector space structure. An abelian group that is simultaneously $m$-torsion and a $\mathbf{Q}$-vector space must be zero. Hence:

$$
\operatorname{Ext}^1(\mathbf{Q}, \mathbf{Z}/m\mathbf{Z}) = 0.

$$

Note: the computation of $\operatorname{Ext}^1(\mathbf{Q}, \mathbf{Z})$ is considerably more subtle. One can show $\operatorname{Ext}^1_{\mathbf{Z}}(\mathbf{Q}, \mathbf{Z}) \cong \widehat{\mathbf{Z}} / \mathbf{Z}$, where $\widehat{\mathbf{Z}} = \prod_p \mathbf{Z}_p$ is the profinite completion of $\mathbf{Z}$. This is a large, uncountable, torsion-free, divisible group.

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{Ext}^1_{\mathbf{Z}}(\mathbf{Z}/m\mathbf{Z}, \mathbf{Z}/n\mathbf{Z})$ for arbitrary positive integers $m, n$. Express your answer in terms of $m$ and $n$. -->
