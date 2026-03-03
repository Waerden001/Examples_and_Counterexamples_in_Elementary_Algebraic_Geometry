---
chapter: moduli
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Moduli_problems_and_deformation_theory/deformation_theory.tex
---

## Deformation theory

### Example: Hartsshorne $\mathrm{III}.9.9$, a rigid $k$-algebra {#ecag-0299}

**Statement:** Let $k$ be a field. The $k$-algebra

$$
X = \operatorname{Spec}(k[x,y,z,w]/((x,y) \cap (z,w)))

$$

is rigid, meaning it admits no non-trivial first-order infinitesimal deformations. Equivalently, the module $T^1$ of first-order deformations vanishes.

**Construction/Proof:** The ideal $(x,y) \cap (z,w) = (xz, xw, yz, yw)$ defines the union of two coordinate planes in $\mathbb{A}^4_k$ meeting at the origin. Denote $R = k[x,y,z,w]/(xz, xw, yz, yw)$.

Step 1. The cotangent complex controls deformations. For an affine scheme $X = \operatorname{Spec}(R)$ where $R = S/I$ with $S = k[x,y,z,w]$, the first-order deformations of $R$ as a $k$-algebra are classified by

$$
T^1(R/k) = \operatorname{coker}\left(\operatorname{Hom}_R(\Omega_{S/k} \otimes_S R,\, R) \to \operatorname{Hom}_R(I/I^2,\, R)\right).

$$

Step 2. The ideal $I = (xz, xw, yz, yw)$ has four generators. The conormal module $I/I^2$ is a module over $R$. A homomorphism $\phi \in \operatorname{Hom}_R(I/I^2, R)$ is determined by the images of $xz, xw, yz, yw$ subject to the relations in $I/I^2$.

Step 3. The key relations in $I/I^2$ come from the syzygies among the generators. For example, $x \cdot (yw) - y \cdot (xw) = 0$ in $I$, giving $x \cdot \phi(yw) = y \cdot \phi(xw)$ in $R$. Each such homomorphism $\phi$ can be shown to lift to a $k$-derivation of $S$ restricted to $I$, meaning $\phi$ lies in the image of the natural map from $\operatorname{Der}_k(S, R)$.

Step 4. By explicit computation (Hartshorne III.9.9), one verifies $T^1(R/k) = 0$, so $X$ is rigid. This is notable because $X$ is singular (it is the union of two planes meeting at a point), yet it admits no deformations. Smoothness is not required for rigidity.

**Key Insight:** Despite being singular, the scheme $X$ has enough syzygies among its defining equations that every potential first-order deformation is trivial. This provides a counterexample to the naive expectation that only smooth varieties can be rigid.

**Prerequisites:** Cotangent complex, $T^1$ functor, first-order deformations of algebras, Hartshorne Chapter III

<!-- BENCHMARK_PROBLEM: Let $R = k[x,y,z,w]/(xz, xw, yz, yw)$ for an algebraically closed field $k$. Compute $T^1(R/k)$, the module of first-order deformations of $R$ as a $k$-algebra. Is $R$ rigid? -->

### Remark: infinitesimal deformation corresponding to $H^{1}(X,T_{X})$ {#ecag-0300}

For a smooth projective variety $X$ over a field $k$, the first-order infinitesimal deformations of $X$ (i.e., flat families over $\operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ with special fiber $X$, modulo isomorphism) are classified by $H^1(X, T_X)$, where $T_X = \mathcal{H}om(\Omega_{X/k}, \mathcal{O}_X)$ is the tangent sheaf. This is the Kodaira-Spencer correspondence.

For projective space $\mathbb{P}^n_k$, the Euler sequence

$$
0 \to \mathcal{O}_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus(n+1)} \to T_{\mathbb{P}^n} \to 0

$$

together with the vanishing $H^1(\mathbb{P}^n, \mathcal{O}(1)) = 0$ and $H^2(\mathbb{P}^n, \mathcal{O}) = 0$ (for $n \geq 1$), yields $H^1(\mathbb{P}^n_k, T_{\mathbb{P}^n_k}) = 0$ via the associated long exact sequence in cohomology. Thus projective spaces $\mathbb{P}^n_k$ are rigid: they admit no non-trivial first-order deformations.

More generally, obstructions to extending deformations lie in $H^2(X, T_X)$. When $H^2(X, T_X) = 0$, every first-order deformation extends to all higher orders, and the deformation space is smooth of dimension $\dim_k H^1(X, T_X)$.

<!-- BENCHMARK_PROBLEM: Using the Euler sequence on $\mathbb{P}^n_k$ (with $n \geq 2$ and $k$ algebraically closed of characteristic zero), compute $H^1(\mathbb{P}^n_k, T_{\mathbb{P}^n_k})$ and determine whether $\mathbb{P}^n_k$ is rigid. -->

### Example: $T_{id}(\mathrm{Aut}(X))\cong \mathrm{Hom}(\Omega_{X}, \mathcal{O}_{X})$ {#ecag-0301}

**Statement:** Let $X$ be a scheme of finite type over an algebraically closed field $k$ with $\operatorname{char}(k) = 0$. Then the tangent space to the automorphism scheme $\operatorname{Aut}(X)$ at the identity is naturally isomorphic to $\operatorname{Hom}_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X)$. If $X$ is smooth, this equals $H^0(X, T_X)$.

Furthermore, let $X$ be a $k$-scheme and $\mathcal{L} \in \operatorname{Pic}(X)$ a line bundle. The deformation functor of the pair $(X, \mathcal{L})$ restricted to the Picard component,

$$
\widehat{\operatorname{Pic}}_{X, \mathcal{L}} : \mathbf{Art}/k \to \mathbf{Set}, \quad A \mapsto \{\text{line bundle } \mathcal{L}' \text{ on } X_A,\; \phi: \mathcal{L}'|_X \cong \mathcal{L}\}/\sim,

$$

has tangent-obstruction theory with $T_1 = H^1(X, \mathcal{O}_X)$ and $T_2 = H^2(X, \mathcal{O}_X)$ when $X$ is proper.

**Construction/Proof:**

*Part 1: Tangent space of $\operatorname{Aut}(X)$.*

A tangent vector of $\operatorname{Aut}(X)$ at the identity is a morphism

$$
\operatorname{Spec}(k[\epsilon]/(\epsilon^2)) \to \operatorname{Aut}(X),

$$

which corresponds to an automorphism of the trivial deformation $X[\epsilon] = X \times_k \operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ reducing to the identity modulo $\epsilon$. That is, a $k[\epsilon]/(\epsilon^2)$-algebra isomorphism

$$
\mathcal{O}_{X[\epsilon]} \to \mathcal{O}_{X[\epsilon]}.

$$

Locally on an affine chart with coordinates $x_i$, this isomorphism takes the form

$$
x_i \mapsto x_i + \epsilon f_i

$$

for some $f_i \in \mathcal{O}_X$. For this to be a ring homomorphism, the map $d: \mathcal{O}_X \to \mathcal{O}_X$ defined by $d(x_i) = f_i$ must satisfy the Leibniz rule:

$$
d(x_i x_j) = x_i d(x_j) + x_j d(x_i).

$$

This is precisely the condition that $d$ be a $k$-derivation of $\mathcal{O}_X$. By the universal property of the module of Kahler differentials $\Omega_{X/k}$, giving such a derivation is equivalent to giving an $\mathcal{O}_X$-module homomorphism $\Omega_{X/k} \to \mathcal{O}_X$. Hence

$$
T_{\operatorname{id}}(\operatorname{Aut}(X)) \cong \operatorname{Hom}_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X).

$$

When $X$ is smooth, $\Omega_{X/k}$ is locally free, so $\mathcal{H}om(\Omega_{X/k}, \mathcal{O}_X) = T_X$ is the tangent sheaf, and global sections give

$$
T_{\operatorname{id}}(\operatorname{Aut}(X)) \cong H^0(X, T_X).

$$

*Part 2: Tangent-obstruction theory of $\widehat{\operatorname{Pic}}_{X, \mathcal{L}}$.*

Consider a small extension $0 \to M \to B \to A \to 0$ in $\mathbf{Art}/k$. The closed immersion $\iota: X_A \hookrightarrow X_B$ has ideal sheaf $\mathcal{I} = \pi^* M$, where $\pi: X_B \to \operatorname{Spec}(B)$ is the structure map. The exponential exact sequence of sheaves of multiplicative groups on $X_B$ is

$$
1 \to 1 + \mathcal{I} \to \mathcal{O}^{\times}_{X_B} \to \mathcal{O}^{\times}_{X_A} \to 1.

$$

Since $\mathcal{I}^2 = 0$ (small extension), the map $s \mapsto 1 + s$ gives an isomorphism of abelian sheaves $\mathcal{I} \xrightarrow{\sim} 1 + \mathcal{I}$, so $1 + \mathcal{I} \cong \pi^* M$. Taking the long exact sequence in cohomology:

$$
H^1(X, \pi^* M) \to \operatorname{Pic}(X_B) \xrightarrow{\iota^*} \operatorname{Pic}(X_A) \to H^2(X, \pi^* M).

$$

Since $\pi^* M$ is locally isomorphic to $\mathcal{O}_X \otimes_k M \cong \mathcal{O}_X^{\oplus \dim_k M}$, we have

$$
H^i(X, \pi^* M) = H^i(X, \mathcal{O}_X) \otimes_k M.

$$

When $X$ is proper, $T_1 = H^1(X, \mathcal{O}_X)$ and $T_2 = H^2(X, \mathcal{O}_X)$ are finite-dimensional and form a tangent-obstruction theory. If $\operatorname{Pic}(X)$ is representable, then $T_{[\mathcal{L}]}\operatorname{Pic}(X) = H^1(X, \mathcal{O}_X)$.

**Key Insight:** Infinitesimal automorphisms are the same as global derivations, which by the universal property of Kahler differentials correspond to global sections of the tangent sheaf. The Picard deformation theory follows from the multiplicative-to-additive reduction via the exponential sequence $1 + \mathcal{I} \cong \mathcal{I}$ for square-zero ideals.

**Prerequisites:** Kahler differentials, universal property of $\Omega_{X/k}$, tangent sheaf, Picard group, exponential exact sequence, cohomology of sheaves, small extensions in $\mathbf{Art}/k$

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective curve of genus $g$ over an algebraically closed field $k$ of characteristic zero. Compute $\dim_k T_{\operatorname{id}}(\operatorname{Aut}(X))$ and $\dim_k T_{[\mathcal{L}]}\operatorname{Pic}(X)$ in terms of $g$, and determine for which values of $g$ the automorphism group is finite. -->

## Deformation of mapping spaces
## Deformation of automorphisms
## Deformation of torsors
## Deformation of coherent sheaves
Let $X$ be a smooth projective variety. $E$ be a coherent sheaf of $\mathcal{O}_{X}$-module. We denote the ring of dual numbers by $k[\epsilon]$, $\operatorname{Spec}(k[\epsilon])$ by $D$ and $X\otimes_{k}\operatorname{Spec}(k[\epsilon])$ by $X_{D}$. Consider the deformation functor
$$ \mathcal{M}: \mathbf{Art}/k \rightarrow \mathbf{Set}, \quad A \mapsto \{A\text{-flat coherent sheaf } E'\in \mathbf{Coh}(X_{A}), \phi:E'|_{X}\cong E\}/\sim.

$$

### Theorem {#ecag-0302}

**Statement:** Let $X$ be a smooth projective variety over a field $k$, and let $E$ be a coherent sheaf of $\mathcal{O}_X$-modules. Let $D = \operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ denote the spectrum of the ring of dual numbers and $X_D = X \times_k D$. Then there is a natural bijection

$$
\mathcal{M}(D) \cong \operatorname{Ext}^1_{\mathcal{O}_X}(E, E),

$$

where $\mathcal{M}(D)$ is the set of isomorphism classes of first-order deformations of $E$ over $D$.

**Construction/Proof:**

Step 1. *Setup.* We have the short exact sequence of $k[\epsilon]$-modules

$$
0 \to (\epsilon) \to k[\epsilon] \to k \to 0.

$$

As $k[\epsilon]$-modules, $(\epsilon) \cong k$ (via $\epsilon \mapsto 1$). Pulling back along $\pi: X_D \to D$ gives an exact sequence of $\mathcal{O}_{X_D}$-modules

$$
0 \to \epsilon \mathcal{O}_X \to \mathcal{O}_{X_D} \to \mathcal{O}_X \to 0.

$$

Step 2. *From deformations to extensions.* Let $E'$ be a deformation of $E$ over $D$, i.e., $E'$ is a coherent $\mathcal{O}_{X_D}$-module, flat over $D$, with $E'|_X \cong E$. Since $E'$ is flat over $D$, tensoring the above sequence with $E'$ over $\mathcal{O}_{X_D}$ preserves exactness:

$$
0 \to \epsilon E \to E' \to E \to 0.

$$

Here $\epsilon E \cong E$ as $\mathcal{O}_X$-modules (since $\epsilon \cdot \epsilon = 0$, the $\mathcal{O}_{X_D}$-module structure on $\epsilon E$ factors through $\mathcal{O}_X$). This short exact sequence defines an element of $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$ via the identification $\epsilon E \cong E$ and restriction of scalars from $\mathcal{O}_{X_D}$ to $\mathcal{O}_X$.

Step 3. *From extensions to deformations.* Conversely, given a class $[E'] \in \operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$ represented by a short exact sequence

$$
0 \to E \xrightarrow{\iota} E' \xrightarrow{p} E \to 0,

$$

we define an $\mathcal{O}_{X_D}$-module structure on $E'$ by letting $\epsilon$ act as $\iota \circ p: E' \to E \to E'$. Since $p \circ \iota \circ p \circ \iota = 0$ (as $p \circ \iota = 0$ by exactness), we have $\epsilon^2 = 0$, so this is a well-defined $k[\epsilon]$-module structure, hence an $\mathcal{O}_{X_D}$-module structure.

Step 4. *Flatness.* To verify $E'$ is flat over $D = \operatorname{Spec}(k[\epsilon])$, we check two conditions: (a) $E'|_X = E'/\epsilon E' = E$ is flat over $\operatorname{Spec}(k)$ (automatic), and (b) the multiplication map $(\epsilon) \otimes_{k[\epsilon]} E' \to E'$ is injective. The latter amounts to the injectivity of $\iota: E \to E'$, which holds by exactness.

Step 5. *Bijection.* One verifies that these two constructions are inverse to each other: isomorphic deformations give the same extension class, and equivalent extensions yield isomorphic deformations. Therefore

$$
\mathcal{M}(D) = \operatorname{Ext}^1_{\mathcal{O}_X}(E, E).

$$

**Key Insight:** Flatness over the dual numbers is equivalent to the extension sequence being short exact, which is precisely the data of an element in $\operatorname{Ext}^1$. The $\epsilon$-action on the middle term of an extension is forced by the splitting data, connecting the linear algebra of extensions with the geometry of deformations.

**Prerequisites:** Flatness over Artinian rings, $\operatorname{Ext}$ groups, coherent sheaves, deformation functors, dual numbers

<!-- BENCHMARK_PROBLEM: Let $X = \mathbb{P}^1_k$ over an algebraically closed field $k$, and let $E = \mathcal{O}_{\mathbb{P}^1}(n)$ for an integer $n$. Compute $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$ and determine the dimension of the space of first-order deformations of $E$. -->

### Theorem {#ecag-0303}

**Statement:** Let $X$ be a smooth projective variety over $k$, and let $E$ be a coherent sheaf on $X$ satisfying $\operatorname{Hom}(E, E) \cong k$ (e.g., $E$ is a stable sheaf). Let $0 \to I \to B \xrightarrow{\sigma} A \to 0$ be a small extension in $\mathbf{Art}/k$ (so $\mathfrak{m}_A \cdot I = 0$). Then the deformation functor $\mathcal{M}$ of $E$ admits a tangent-obstruction theory:

$$
\operatorname{Ext}^1_{\mathcal{O}_X}(E, E) \otimes_k I \to \mathcal{M}(B) \to \mathcal{M}(A) \xrightarrow{\operatorname{ob}} \operatorname{Ext}^2_{\mathcal{O}_X}(E, E) \otimes_k I.

$$

Specifically:

1. If the fiber $\mathcal{M}(\sigma)^{-1}(E_A)$ over $E_A \in \mathcal{M}(A)$ is non-empty, it is an $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E) \otimes_k I$-torsor.
2. There is an obstruction map $\operatorname{ob}: \mathcal{M}(A) \to \operatorname{Ext}^2_{\mathcal{O}_X}(E, E) \otimes_k I$ such that $E_A$ lifts to $\mathcal{M}(B)$ if and only if $\operatorname{ob}(E_A) = 0$.
3. The obstruction lies in the traceless part: $\operatorname{im}(\operatorname{ob}) \subseteq \operatorname{Ext}^2_0(E, E) \otimes_k I$, where $\operatorname{Ext}^2_0(E, E) = \ker\left(\operatorname{tr}: \operatorname{Ext}^2(E, E) \to H^2(X, \mathcal{O}_X)\right)$.

**Construction/Proof:**

Step 1. *Torsor structure.* Given $E_A \in \mathcal{M}(A)$, suppose $E_B, E'_B$ are two lifts to $\mathcal{M}(B)$. The small extension $0 \to I \to B \to A \to 0$ gives a closed immersion $X_A \hookrightarrow X_B$ with ideal sheaf $\mathcal{I} = \mathcal{O}_{X_B} \otimes_B I$. Since $\mathfrak{m}_A \cdot I = 0$, we have $\mathcal{I}^2 = 0$. Both $E_B$ and $E'_B$ restrict to $E_A$ on $X_A$, so their difference defines an element of $\operatorname{Ext}^1_{\mathcal{O}_{X_A}}(E_A, I \otimes_{\mathcal{O}_{X_A}} E_A)$. By cohomology and base change (using $\mathfrak{m}_A \cdot I = 0$ and the simplicity $\operatorname{Hom}(E,E) \cong k$), this group equals $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E) \otimes_k I$, establishing the torsor structure.

Step 2. *Obstruction map.* Given $E_A \in \mathcal{M}(A)$, choose a local lift $\{E_{B,\alpha}\}$ on an open cover $\{U_\alpha\}$ of $X_B$ (local lifts always exist since $\operatorname{Ext}$ is computed via local-to-global spectral sequences). On overlaps $U_{\alpha\beta}$, the difference of local lifts gives elements in $\operatorname{Ext}^1_{\mathcal{O}_{X_A}}(E_A, I \otimes E_A)|_{U_{\alpha\beta}}$. These assemble into a Cech 2-cocycle, whose class

$$
\operatorname{ob}(E_A) \in \operatorname{Ext}^2_{\mathcal{O}_X}(E, E) \otimes_k I

$$

is the obstruction. It vanishes if and only if the local lifts can be patched into a global lift.

Step 3. *Tracelessness.* The trace map $\operatorname{tr}: \mathcal{E}nd(E) \to \mathcal{O}_X$ induces $\operatorname{tr}: \operatorname{Ext}^2(E, E) \to H^2(X, \mathcal{O}_X)$. Since the obstruction arises from the $\operatorname{Ext}^2$ of the deformation functor, and the trace part of the obstruction is governed by the deformation of $\det(E)$ in $\operatorname{Pic}(X)$, the assumption $\operatorname{Hom}(E, E) \cong k$ ensures the obstruction lies in the traceless part $\operatorname{Ext}^2_0(E, E) \otimes_k I = \ker(\operatorname{tr}) \otimes_k I$.

Step 4. *Base change reduction.* The identification $\operatorname{Ext}^i_{\mathcal{O}_{X_A}}(I \otimes_{\mathcal{O}_{X_A}} E_A, E_A) = \operatorname{Ext}^i_{\mathcal{O}_X}(E, E) \otimes_k I$ uses the fact that $\mathfrak{m}_A \cdot I = 0$, so any $\mathcal{O}_{X_A}$-module map from $I \otimes E_A$ factors through $E_A \otimes_A k = E$. The module $I$ is then just a $k$-vector space, and the projection formula gives the tensor factorization.

**Key Insight:** The condition $\operatorname{Hom}(E,E) \cong k$ (simplicity/stability) is essential: it ensures the automorphism group of $E$ is trivial (up to scalars), which makes the deformation functor well-behaved and forces the fibers of the lifting map to be torsors rather than merely group-acted sets. The tracelessness of the obstruction reflects that the determinant line bundle deforms freely in the Picard scheme.

**Prerequisites:** Small extensions in $\mathbf{Art}/k$, $\operatorname{Ext}$ groups, stable sheaves, torsor structure, trace map on endomorphisms, cohomology and base change

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective surface over $\mathbb{C}$ with $H^2(X, \mathcal{O}_X) = 0$, and let $E$ be a stable vector bundle of rank $r$ on $X$. Using the tangent-obstruction theory, prove that the moduli space of stable sheaves is smooth at $[E]$ and compute its dimension in terms of $r$, $c_1(E)$, $c_2(E)$, and invariants of $X$. -->

### Remark {#ecag-0304}

The deformation-obstruction theory of a geometric object operates at several distinct levels, which should not be conflated:

1. **Intrinsic deformation theory.** For any geometric object $E$ (a sheaf, a scheme, a map, etc.), one can study its deformations over Artinian bases without reference to any moduli space. The deformation functor $\mathcal{M}: \mathbf{Art}/k \to \mathbf{Set}$ is defined purely in terms of the object $E$ and its base extensions. The tangent space $\mathcal{M}(k[\epsilon]/(\epsilon^2))$ and obstruction spaces exist at this level.

2. **Fine moduli spaces.** If a fine moduli space $M$ exists (i.e., there is a universal family), the functor $\mathcal{M}$ is representable by the formal completion $\widehat{M}_{[E]}$, and we have a canonical isomorphism

$$
T_{[E]} M = \mathcal{M}(\operatorname{Spec}(k[\epsilon]/(\epsilon^2))).

$$

In this case, the Zariski tangent space of the moduli space coincides with first-order deformations.

3. **Coarse moduli spaces.** If only a coarse moduli space $M$ exists, the identification $T_{[E]} M = \mathcal{M}(\operatorname{Spec}(k[\epsilon]/(\epsilon^2)))$ fails in general. The coarse moduli map $\mathcal{M} \to h_M$ need not be an isomorphism on tangent spaces. For instance, if $E$ has non-trivial automorphisms, first-order deformations modulo automorphisms may differ from the Zariski tangent space. One must carefully distinguish between the "tangent space to the functor" and the "tangent space to the coarse moduli space."

This distinction is particularly important in moduli of sheaves: the moduli functor of semistable sheaves is typically not representable, and the coarse moduli space (constructed via GIT) has tangent spaces that can differ from $\operatorname{Ext}^1(E, E)$ at points corresponding to properly semistable sheaves.

<!-- BENCHMARK_PROBLEM: Give an example of a coherent sheaf $E$ on a smooth projective variety $X$ such that the coarse moduli space $M$ of semistable sheaves exists, but $T_{[E]} M \neq \operatorname{Ext}^1(E, E)$. Explain why the identification fails. -->

## Deformation of quotient sheaves
Let $X$ be a scheme over $k$. $\mathcal{F}$ be a coherent sheaf on $X$, $\mathcal{S}_{0}$ be a coherent subsheaf of $\mathcal{F}$, $\qQ_{0}$ be the quotient. Define the deformation functor

$$D:=D_{[\mathcal{F}\rightarrow \qQ_{0}\rightarrow 0]}: \mathbf{Art}/k\rightarrow \mathbf{Set}$$

$$A\mapsto \{ \text{exact sequences of } A\text{-flat sheaves } 0\rightarrow \mathcal{S}\rightarrow \mathcal{F}\otimes_{k}A\rightarrow \qQ\rightarrow 0 \text{ on } X_{A},  \mathcal{S}\otimes_{A}k\cong \mathcal{S}_{0} \}/\sim.$$

By definition, $[0\rightarrow \mathcal{S}'\rightarrow \mathcal{F}\otimes_{k}B\rightarrow \qQ'\rightarrow 0]\in D(B)$ is a deformation of $[0\rightarrow \mathcal{S}\rightarrow \mathcal{F}\otimes_{k}A\rightarrow \qQ\rightarrow 0]\in D(A)$ if and only if we have

- $\mathcal{S}'\otimes_{B}A=\mathcal{S}$
- $\mathcal{S}'$ is flat over $B$. We know $\mathcal{S}'\otimes_{B}A=\mathcal{S}$ is flat over $A$, thus we only need $\mathcal{S}'\otimes_{B} M=\mathcal{S}\otimes_{B}A\otimes_{A}M=\mathcal{S}\otimes_{A}M \rightarrow \mathcal{S}'$ is an injection. In other words, flatness is equivalent to the existence of the short exact sequence

$$0\rightarrow \mathcal{S}\otimes_{A}M\rightarrow \mathcal{S}'\rightarrow \mathcal{S}\rightarrow 0.$$

In other words, an extension exists if and only if we can find a subsheaf $\mathcal{E}$ of  $\mathcal{F}\otimes_{k}B/S\otimes_{A}M=\mathcal{F}\otimes_{k}B/\operatorname{im}(\alpha)$ whose image in $\mathcal{F}\otimes_{k}A$ is exactly $\mathcal{S}$. Because the image lies in $\mathcal{S}$, we only need to find a subsheaf of $\ker(\beta)/\operatorname{im}(\alpha)$ has this property. In other words, we need the following sequence to split

$$0\rightarrow \ker\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\rightarrow \mathcal{S}\rightarrow 0.$$

We can check that $\ker=\mathcal{F}\otimes_{k}M/\mathcal{S}\otimes_{A}M=\qQ\otimes_{A}M$. That is, the obstruction is given by

$$\operatorname{ob}=[0\rightarrow \qQ\otimes_{A}M\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\rightarrow \mathcal{S}\rightarrow 0]\in \operatorname{Ext}^{1}_{\mathcal{O}_{X_{B}}}(\mathcal{S}, \qQ\otimes_{A}M).$$

Moreover, all flat deformations of the given element is bijective to

$$\operatorname{Ext}^{0}_{\mathcal{O}_{X_{B}}}(\mathcal{S}, \qQ\otimes_{A}M)=\operatorname{Hom}(\mathcal{S}, \qQ\otimes_{A}M).$$

<!-- tikzcd diagram: manual conversion needed -->
```latex
<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
& 0\arrow{d} & & 0 \arrow{d}\\
& \mathcal{S}\otimes_{A}M\arrow{d}\arrow[dashrightarrow]{dr}{\alpha}& & \mathcal{S}\arrow{d}\\
0\arrow{r} & \mathcal{F}\otimes_{k}M\arrow{r}\arrow{d}& \mathcal{F}\otimes_{k}B\arrow[dashrightarrow]{dr}{\beta}\arrow{r}& \mathcal{F}\otimes_{k}A\arrow{r}\arrow{d} & 0\\
&\qQ\otimes_{A}M\arrow{d} & &Q\arrow{d}\\
& 0 & &0
\end{tikzcd}
```
```
There's still one more issue, these two $\operatorname{Ext}$ groups still depend on $B$. We claim that  the $M(\ker(\beta)/\operatorname{im}(\alpha))=0$. Indeed if $\gamma=\sum f_{i}\otimes_{k}b_{i}\in \ker(\beta)$, then we have $\sum f_{i}\otimes_{k}a_{i}\in \mathcal{S}$, where $a_{i}=b_{i}\pmod M$. Then $m\gamma =\sum f_{i}\otimes mb_{i}=\sum f_{i}\otimes ma_{i}$, the last identity comes from the fact that $M^{2}=0$, thus $ma_{i}$ is well defined. Then $m\gamma=m(\sum f_{i}\otimes_{k}a_{i})\in \operatorname{im}(\alpha)$.
Apply $\otimes_{A}k$ to

$$0\rightarrow \ker\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\rightarrow \mathcal{S}\rightarrow 0.$$

We still get an exact sequence by the $A$-flatness of $\mathcal{S}$

$$0\rightarrow \qQ\otimes_{A}M\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\otimes_{A}k\rightarrow \mathcal{S}\otimes_{A}k\rightarrow 0.$$

We can check that we have the following commutative diagram. If we just consider small extensions, we have $\qQ\otimes_{A}M\otimes_{A}k=\qQ\otimes_{A}M$ because $m_{A}M=0$.
<!-- tikzcd diagram: manual conversion needed -->
```latex
<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
& & 0\arrow{d}& 0\arrow{d}&\\
 & & \mathcal{S}\otimes_{A}m_{A}\arrow{d}\arrow[r, equal]&  \mathcal{S}\otimes_{A}m_{A}\arrow{d}&\\
 0\arrow{r}&\qQ\otimes_{A}M \arrow{r}\arrow[d,equal]& \ker(\beta)/\operatorname{im}(\alpha)\arrow{r}\arrow{d}&  \mathcal{S}\arrow{d}\arrow{r}& 0\\
 0\arrow{r}&\qQ\otimes_{A}M \arrow{r}& \ker(\beta)/\operatorname{im}(\alpha)\otimes_{A}k\arrow{r}\arrow{d}&\mathcal{S}\otimes_{A}k \arrow{d}\arrow{r}&0\\
 & & 0& 0& \\
\end{tikzcd}
```
```
In conclusion, we have

$$\operatorname{Hom}_{X_{A}}(\mathcal{S},\qQ\otimes_{A}M)=\operatorname{Hom}_{X}(\mathcal{S}\otimes_{A}k,\qQ\otimes_{A}M)=\operatorname{Hom}_{X}(\mathcal{S}_{0}, \qQ_{0})\otimes_{k}M$$

$$\operatorname{Ext}^{1}_{X_{A}}(\mathcal{S}, \qQ\otimes_{A}M)=\operatorname{Ext}^{1}_{X}(\mathcal{S}\otimes_{A}k, \qQ\otimes_{A}M)=\operatorname{Ext}^{1}_{X}(\mathcal{S}_{0}, \qQ_{0})\otimes_{k} M.$$

Because $m_{A}M=0$, any element in $\operatorname{Hom}_{X_{A}}(\mathcal{S}, \qQ\otimes_{A}M)$ factors through the geometric fibre. And we can take out $M$ because of the projection formula, $M$ is simply viewed as a vector space. As a special case, the tangent-obstruction theory of the Hilbert scheme functor $H_{Z,X}$ is given by $T_{1}=\operatorname{Hom}_{\mathcal{O}_{X}}(I_{Z}, \mathcal{O}_{Z}), T_{2}=\operatorname{Ext}^{1}_{\mathcal{O}_{X}}(I_{Z}, \mathcal{O}_{Z})$.

### Remark {#ecag-0305}

There are several equivalent descriptions of the tangent space at a point $[Z]$ on the Hilbert scheme $\operatorname{Hilb}^n(X)$ of $n$ points on a smooth quasi-projective variety $X$ of dimension $k$ over an algebraically closed field. All three are canonically isomorphic:

$$
T_Z \operatorname{Hilb}^n(X) = \operatorname{Hom}_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{O}_Z) = \operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{O}_Z, \mathcal{O}_Z) = \operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{I}_Z).

$$

**First isomorphism:** $\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{O}_Z) \cong \operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{O}_Z, \mathcal{O}_Z)$. Apply the functor $\operatorname{Hom}_{\mathcal{O}_X}(-, \mathcal{O}_Z)$ to the short exact sequence

$$
0 \to \mathcal{I}_Z \to \mathcal{O}_X \to \mathcal{O}_Z \to 0.

$$

The resulting long exact sequence begins

$$
0 \to \operatorname{Hom}(\mathcal{O}_Z, \mathcal{O}_Z) \to \operatorname{Hom}(\mathcal{O}_X, \mathcal{O}_Z) \to \operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \to \operatorname{Ext}^1(\mathcal{O}_Z, \mathcal{O}_Z) \to \operatorname{Ext}^1(\mathcal{O}_X, \mathcal{O}_Z) \to \cdots

$$

The first two terms are both isomorphic to $\operatorname{Hom}(\mathcal{O}_Z, \mathcal{O}_Z)$ (since $\operatorname{Hom}(\mathcal{O}_X, \mathcal{O}_Z) \cong H^0(X, \mathcal{O}_Z) \cong \operatorname{Hom}(\mathcal{O}_Z, \mathcal{O}_Z)$ via restriction), and the map between them is the identity. Furthermore, $\operatorname{Ext}^1(\mathcal{O}_X, \mathcal{O}_Z) = H^1(X, \mathcal{O}_Z) = 0$ since $\mathcal{O}_Z$ is supported on a zero-dimensional subscheme. Thus the connecting map gives the isomorphism $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \xrightarrow{\sim} \operatorname{Ext}^1(\mathcal{O}_Z, \mathcal{O}_Z)$.

**Second isomorphism:** $\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{O}_Z) \cong \operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{I}_Z)$. This can be established by realizing $\operatorname{Hilb}^n(X)$ as the rank-1 instanton moduli space $\mathcal{M}(n, 1)$, i.e., the moduli of rank-1 torsion-free sheaves with fixed determinant. The ideal sheaf $\mathcal{I}_Z$ is a rank-1 torsion-free sheaf, and the tangent space to $\mathcal{M}(n,1)$ at $[\mathcal{I}_Z]$ is $\operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{I}_Z)$ by the deformation theory of coherent sheaves (Theorem ecag-0302). Alternatively, apply $\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{I}_Z, -)$ to $0 \to \mathcal{I}_Z \to \mathcal{O}_X \to \mathcal{O}_Z \to 0$:

$$
\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_X) \to \operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \to \operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{I}_Z) \to \operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{O}_X).

$$

When $X$ is smooth, $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_X) \cong H^0(X, \mathcal{O}_X)$ (since $\mathcal{I}_Z \subset \mathcal{O}_X$ and any map $\mathcal{I}_Z \to \mathcal{O}_X$ extends to $\mathcal{O}_X \to \mathcal{O}_X$ by normality), and $\operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{O}_X) \cong \operatorname{Ext}^2(\mathcal{O}_Z, \mathcal{O}_X)$ which, combined with the appropriate vanishing conditions, yields the desired isomorphism.

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective surface over $\mathbb{C}$, and let $Z \subset X$ consist of a single reduced point. Compute $\dim_k T_Z \operatorname{Hilb}^1(X)$ using each of the three descriptions $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z)$, $\operatorname{Ext}^1(\mathcal{O}_Z, \mathcal{O}_Z)$, and $\operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{I}_Z)$, and verify they agree. -->

## Deformation theory the instanton moduli space
The instanton moduli space $\mathcal{M}(n,r)$ is defined to be moduli of rank $2$ torsion-free sheaves on $\mathbf{P}^{2}$ framed at infinity.
## Deformation of Hilbert schemes
## Hilbert schemes of points on surfaces
## Deformation of Calabi-Yau varieties

## Deformation of varieties
## Deformation of nodes
