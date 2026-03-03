---
chapter: moduli
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Moduli_problems_and_deformation_theory/deformation_theory.tex
---

## Deformation theory

### Example: Hartshorne III.9.9, a rigid $k$-algebra {#ecag-0299}

The union of two coordinate planes in $\mathbb{A}^4_k$ meeting at the origin provides a singular scheme that is nonetheless rigid. Set $R = k[x,y,z,w]/(xz, xw, yz, yw)$, so $X = \operatorname{Spec}(R)$ is the subscheme defined by the ideal $I = (x,y) \cap (z,w) = (xz, xw, yz, yw)$.

The first-order deformations of $R$ as a $k$-algebra are classified by the $T^1$ functor. Writing $R = S/I$ with $S = k[x,y,z,w]$, the relevant exact sequence is

$$
\operatorname{Hom}_R(\Omega_{S/k} \otimes_S R,\, R) \xrightarrow{\;\delta\;} \operatorname{Hom}_R(I/I^2,\, R) \to T^1(R/k) \to 0.
$$

The map $\delta$ sends a $k$-derivation $D: S \to R$ to the restriction $D|_I: I/I^2 \to R$. A homomorphism $\phi \in \operatorname{Hom}_R(I/I^2, R)$ is determined by the images $\phi(xz)$, $\phi(xw)$, $\phi(yz)$, $\phi(yw)$, subject to the relations in $I/I^2$ coming from syzygies. The key syzygies are:

- $w \cdot (xz) - z \cdot (xw) = 0$, giving $w \cdot \phi(xz) = z \cdot \phi(xw)$ in $R$,
- $w \cdot (yz) - z \cdot (yw) = 0$, giving $w \cdot \phi(yz) = z \cdot \phi(yw)$,
- $y \cdot (xz) - x \cdot (yz) = 0$, giving $y \cdot \phi(xz) = x \cdot \phi(yz)$,
- $y \cdot (xw) - x \cdot (yw) = 0$, giving $y \cdot \phi(xw) = x \cdot \phi(yw)$.

In $R$, the ring splits as a fiber product: $R \cong k[x,y] \times_k k[z,w]$ (the two planes share only the origin). Every element of $R$ can be written uniquely as $f(x,y) + g(z,w) - g(0,0)$. Using this decomposition, one checks that the syzygy constraints force the images $\phi(xz)$, $\phi(xw)$, $\phi(yz)$, $\phi(yw)$ to lie in the image of $\delta$. Concretely, if $D$ is the derivation with $D(x) = a$, $D(y) = b$, $D(z) = c$, $D(w) = d$ for $a, b, c, d \in R$, then $D(xz) = xc + az$, and similar expressions for the other generators. The explicit verification (Hartshorne III.9.9) shows that every $\phi$ satisfying the syzygy relations arises from such a $D$, so $\delta$ is surjective and $T^1(R/k) = 0$.

Thus $X$ is rigid despite being singular. This is a counterexample to the expectation that rigidity requires smoothness. The geometric explanation is that the two components of $X$ cannot be "moved apart" even infinitesimally --- the embedding in $\mathbb{A}^4$ is too constrained by the syzygy structure.

<!-- BENCHMARK_PROBLEM: Let $R = k[x,y,z,w]/(xz, xw, yz, yw)$ for an algebraically closed field $k$. Compute $T^1(R/k)$, the module of first-order deformations of $R$ as a $k$-algebra. Is $R$ rigid? -->

### Remark: infinitesimal deformations and $H^1(X, T_X)$ {#ecag-0300}

For a smooth projective variety $X$ over $k$, the Kodaira--Spencer correspondence identifies first-order deformations of $X$ (flat families over $\operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ with special fiber $X$, up to isomorphism) with $H^1(X, T_X)$.

As a basic application, projective space $\mathbb{P}^n_k$ is rigid for all $n \geq 1$. The Euler sequence

$$
0 \to \mathcal{O}_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus(n+1)} \to T_{\mathbb{P}^n} \to 0
$$

induces a long exact sequence in cohomology. Since $H^1(\mathbb{P}^n, \mathcal{O}(1)) = 0$ (by direct computation or Serre vanishing for $n \geq 1$) and $H^2(\mathbb{P}^n, \mathcal{O}) = 0$ (for $n \geq 2$; for $n = 1$, $H^1$ of the two-term sequence suffices), the connecting map gives $H^1(\mathbb{P}^n, T_{\mathbb{P}^n}) = 0$. So $\mathbb{P}^n$ admits no nontrivial first-order deformations.

More generally, obstructions to extending a first-order deformation to higher order lie in $H^2(X, T_X)$. When $H^2(X, T_X) = 0$, every first-order deformation extends to a formal deformation, and the Kuranishi space (the base of the versal deformation) is smooth of dimension $h^1(X, T_X)$. For instance, smooth curves of genus $g \geq 2$ have $H^2(C, T_C) = 0$ (since $\dim C = 1$), so their deformation space is smooth of dimension $h^1(C, T_C) = 3g - 3$.

<!-- BENCHMARK_PROBLEM: Using the Euler sequence on $\mathbb{P}^n_k$ (with $n \geq 2$ and $k$ algebraically closed of characteristic zero), compute $H^1(\mathbb{P}^n_k, T_{\mathbb{P}^n_k})$ and determine whether $\mathbb{P}^n_k$ is rigid. -->

### Example: $T_{\operatorname{id}}(\operatorname{Aut}(X)) \cong \operatorname{Hom}(\Omega_X, \mathcal{O}_X)$ {#ecag-0301}

**Infinitesimal automorphisms.** A tangent vector to $\operatorname{Aut}(X)$ at the identity is a morphism $\operatorname{Spec}(k[\epsilon]/(\epsilon^2)) \to \operatorname{Aut}(X)$, which corresponds to an automorphism of the trivial deformation $X[\epsilon] = X \times_k \operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ reducing to the identity modulo $\epsilon$. Locally, such an automorphism takes the form $x_i \mapsto x_i + \epsilon f_i$ with $f_i \in \mathcal{O}_X$. The condition that this be a ring homomorphism forces the map $d: x_i \mapsto f_i$ to satisfy the Leibniz rule $d(x_i x_j) = x_i d(x_j) + x_j d(x_i)$, making $d$ a $k$-derivation of $\mathcal{O}_X$. By the universal property of Kahler differentials, such a derivation corresponds to an $\mathcal{O}_X$-module map $\Omega_{X/k} \to \mathcal{O}_X$. Hence

$$
T_{\operatorname{id}}(\operatorname{Aut}(X)) \cong \operatorname{Hom}_{\mathcal{O}_X}(\Omega_{X/k}, \mathcal{O}_X).
$$

When $X$ is smooth, $\Omega_{X/k}$ is locally free and $\mathcal{H}om(\Omega_{X/k}, \mathcal{O}_X) = T_X$, so $T_{\operatorname{id}}(\operatorname{Aut}(X)) \cong H^0(X, T_X)$.

**Picard deformation functor.** For a proper $k$-scheme $X$ and a line bundle $\mathcal{L} \in \operatorname{Pic}(X)$, the deformation functor

$$
\widehat{\operatorname{Pic}}_{X, \mathcal{L}} : \mathbf{Art}/k \to \mathbf{Set}, \quad A \mapsto \{\mathcal{L}' \text{ on } X_A \;:\; \mathcal{L}'|_X \cong \mathcal{L}\}/\sim
$$

has tangent space $T_1 = H^1(X, \mathcal{O}_X)$ and obstruction space $T_2 = H^2(X, \mathcal{O}_X)$.

To see this, consider a small extension $0 \to M \to B \to A \to 0$ in $\mathbf{Art}/k$. The closed immersion $\iota: X_A \hookrightarrow X_B$ has ideal sheaf $\mathcal{I} = \pi^*M$ with $\mathcal{I}^2 = 0$. The exponential exact sequence on $X_B$,

$$
1 \to 1 + \mathcal{I} \to \mathcal{O}_{X_B}^\times \to \mathcal{O}_{X_A}^\times \to 1,
$$

identifies $1 + \mathcal{I} \cong \mathcal{I} \cong \mathcal{O}_X \otimes_k M$ (via $s \mapsto 1 + s$, using $\mathcal{I}^2 = 0$). The long exact sequence in cohomology gives

$$
H^1(X, \mathcal{O}_X) \otimes_k M \to \operatorname{Pic}(X_B) \xrightarrow{\iota^*} \operatorname{Pic}(X_A) \to H^2(X, \mathcal{O}_X) \otimes_k M.
$$

The tangent space (take $A = k$, $B = k[\epsilon]$, $M = k$) is $H^1(X, \mathcal{O}_X)$, and the obstruction to lifting a line bundle from $X_A$ to $X_B$ lies in $H^2(X, \mathcal{O}_X) \otimes_k M$.

**Example: curves.** For a smooth projective curve $C$ of genus $g$, we have $T_{\operatorname{id}}(\operatorname{Aut}(C)) = H^0(C, T_C)$ with $\dim = 3$ for $g = 0$ (corresponding to $\operatorname{PGL}_2$), $\dim = 1$ for $g = 1$ (translations on the elliptic curve), and $\dim = 0$ for $g \geq 2$ (finite automorphism group). The Picard tangent space is $H^1(C, \mathcal{O}_C) = g$ for all $g$, with no obstructions since $H^2(C, \mathcal{O}_C) = 0$.

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective curve of genus $g$ over an algebraically closed field $k$ of characteristic zero. Compute $\dim_k T_{\operatorname{id}}(\operatorname{Aut}(X))$ and $\dim_k T_{[\mathcal{L}]}\operatorname{Pic}(X)$ in terms of $g$, and determine for which values of $g$ the automorphism group is finite. -->

## Deformation of mapping spaces
## Deformation of automorphisms
## Deformation of torsors
## Deformation of coherent sheaves
Let $X$ be a smooth projective variety. $E$ be a coherent sheaf of $\mathcal{O}_{X}$-module. We denote the ring of dual numbers by $k[\epsilon]$, $\operatorname{Spec}(k[\epsilon])$ by $D$ and $X\otimes_{k}\operatorname{Spec}(k[\epsilon])$ by $X_{D}$. Consider the deformation functor

$$
 \mathcal{M}: \mathbf{Art}/k \rightarrow \mathbf{Set}, \quad A \mapsto \{A\text{-flat coherent sheaf } E'\in \mathbf{Coh}(X_{A}), \phi:E'|_{X}\cong E\}/\sim.
$$

### Theorem {#ecag-0302}

First-order deformations of a coherent sheaf $E$ on a smooth projective variety $X$ are classified by $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$. Precisely, there is a natural bijection $\mathcal{M}(D) \cong \operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$, where $D = \operatorname{Spec}(k[\epsilon]/(\epsilon^2))$.

**From deformations to extensions.** The structure sheaf sequence $0 \to (\epsilon) \to k[\epsilon] \to k \to 0$ with $(\epsilon) \cong k$ pulls back to

$$
0 \to \mathcal{O}_X \to \mathcal{O}_{X_D} \to \mathcal{O}_X \to 0.
$$

Given a deformation $E'$ of $E$ over $D$ (a coherent $\mathcal{O}_{X_D}$-module, flat over $D$, with $E'|_X \cong E$), flatness over $D$ ensures that tensoring preserves exactness, yielding

$$
0 \to \epsilon E \to E' \to E \to 0,
$$

where $\epsilon E \cong E$ as $\mathcal{O}_X$-modules (since $\epsilon^2 = 0$, the $\mathcal{O}_{X_D}$-structure on $\epsilon E$ factors through $\mathcal{O}_X$). This short exact sequence defines a class in $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$.

**From extensions to deformations.** Conversely, given a class in $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$ represented by

$$
0 \to E \xrightarrow{\iota} E' \xrightarrow{p} E \to 0,
$$

define an $\mathcal{O}_{X_D}$-module structure on $E'$ by letting $\epsilon$ act as $\iota \circ p$. Since $(p \circ \iota) = 0$ by exactness, we have $\epsilon^2 = \iota \circ p \circ \iota \circ p = 0$, giving a well-defined $k[\epsilon]$-module structure.

**Flatness.** The deformation $E'$ is flat over $D$ because: (a) $E'/\epsilon E' = E$ is flat over $k$ (automatic), and (b) the multiplication map $(\epsilon) \otimes_{k[\epsilon]} E' \to E'$ is injective, which amounts to the injectivity of $\iota: E \to E'$ given by exactness.

These two constructions are inverse to each other: isomorphic deformations yield the same extension class, and equivalent extensions produce isomorphic deformations. The essential observation is that flatness over the dual numbers is equivalent to the extension sequence being short exact, which is precisely the data captured by $\operatorname{Ext}^1$.

**Verification for line bundles on $\mathbb{P}^1$.** For $E = \mathcal{O}_{\mathbb{P}^1}(n)$, we have $\operatorname{Ext}^1(\mathcal{O}(n), \mathcal{O}(n)) = H^1(\mathbb{P}^1, \mathcal{O}) = 0$, so line bundles on $\mathbb{P}^1$ admit no nontrivial deformations. This is consistent with the fact that $\operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z}$ is discrete.

<!-- BENCHMARK_PROBLEM: Let $X = \mathbb{P}^1_k$ over an algebraically closed field $k$, and let $E = \mathcal{O}_{\mathbb{P}^1}(n)$ for an integer $n$. Compute $\operatorname{Ext}^1_{\mathcal{O}_X}(E, E)$ and determine the dimension of the space of first-order deformations of $E$. -->

### Theorem {#ecag-0303}

For a coherent sheaf $E$ on a smooth projective variety $X$ with $\operatorname{Hom}(E, E) \cong k$ (e.g., a stable sheaf), the deformation functor $\mathcal{M}$ of $E$ admits a tangent-obstruction theory governed by the Ext groups of $E$. Given a small extension $0 \to I \to B \xrightarrow{\sigma} A \to 0$ in $\mathbf{Art}/k$ (with $\mathfrak{m}_A \cdot I = 0$):

$$
\operatorname{Ext}^1_{\mathcal{O}_X}(E, E) \otimes_k I \to \mathcal{M}(B) \to \mathcal{M}(A) \xrightarrow{\operatorname{ob}} \operatorname{Ext}^2_{\mathcal{O}_X}(E, E) \otimes_k I.
$$

The three structural properties are: (1) if $E_A \in \mathcal{M}(A)$ lifts to $\mathcal{M}(B)$, the set of lifts is an $\operatorname{Ext}^1(E,E) \otimes_k I$-torsor; (2) $E_A$ lifts if and only if $\operatorname{ob}(E_A) = 0$; and (3) the obstruction lies in the traceless part $\operatorname{Ext}^2_0(E,E) \otimes_k I = \ker(\operatorname{tr}: \operatorname{Ext}^2(E,E) \to H^2(X, \mathcal{O}_X)) \otimes_k I$.

**Torsor structure.** Given two lifts $E_B, E'_B$ of $E_A$, the closed immersion $X_A \hookrightarrow X_B$ has ideal sheaf $\mathcal{I} = \mathcal{O}_{X_B} \otimes_B I$ with $\mathcal{I}^2 = 0$ (since $\mathfrak{m}_A \cdot I = 0$). Both lifts restrict to $E_A$ on $X_A$, so their difference defines a class in $\operatorname{Ext}^1_{\mathcal{O}_{X_A}}(E_A, I \otimes E_A)$. Using $\mathfrak{m}_A \cdot I = 0$ and the simplicity $\operatorname{Hom}(E,E) \cong k$, base change gives $\operatorname{Ext}^1_{\mathcal{O}_{X_A}}(E_A, I \otimes E_A) = \operatorname{Ext}^1_{\mathcal{O}_X}(E,E) \otimes_k I$.

**Obstruction map.** Given $E_A \in \mathcal{M}(A)$, local lifts $\{E_{B,\alpha}\}$ always exist on an open cover $\{U_\alpha\}$ (local Ext computations). On overlaps $U_{\alpha\beta}$, the differences assemble into a Cech $2$-cocycle whose class

$$
\operatorname{ob}(E_A) \in \operatorname{Ext}^2_{\mathcal{O}_X}(E, E) \otimes_k I
$$

is the obstruction. It vanishes if and only if the local lifts patch globally.

**Tracelessness.** The trace map $\operatorname{tr}: \mathcal{E}nd(E) \to \mathcal{O}_X$ induces $\operatorname{tr}: \operatorname{Ext}^2(E,E) \to H^2(X, \mathcal{O}_X)$. The trace component of the obstruction governs deformations of $\det(E)$ in $\operatorname{Pic}(X)$, which is unobstructed when $H^2(X, \mathcal{O}_X) = 0$. Under the simplicity assumption $\operatorname{Hom}(E,E) \cong k$, the obstruction to deforming $E$ itself (with fixed determinant) lies in $\ker(\operatorname{tr}) \otimes_k I$.

The simplicity condition is essential: it ensures the automorphism group of $E$ is $k^*$ (scalars only), making the deformation functor well-behaved. Without it, the fibers of the lifting map are merely acted on by a group, rather than being torsors.

**Application: smoothness of moduli.** If $X$ is a smooth projective surface with $H^2(X, \mathcal{O}_X) = 0$ and $E$ is a stable bundle of rank $r$, then $\operatorname{Ext}^2_0(E,E) = \operatorname{Ext}^2(E,E)$ (the trace map targets $0$), so the moduli space is smooth at $[E]$ if and only if $\operatorname{Ext}^2(E,E) = 0$. When $E$ is a locally free sheaf on a surface, Serre duality gives $\operatorname{Ext}^2(E,E) = \operatorname{Hom}(E, E \otimes K_X)^\vee$, so the moduli space is smooth at $[E]$ when $\operatorname{Hom}(E, E \otimes K_X) = 0$.

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective surface over $\mathbb{C}$ with $H^2(X, \mathcal{O}_X) = 0$, and let $E$ be a stable vector bundle of rank $r$ on $X$. Using the tangent-obstruction theory, prove that the moduli space of stable sheaves is smooth at $[E]$ and compute its dimension in terms of $r$, $c_1(E)$, $c_2(E)$, and invariants of $X$. -->

### Remark {#ecag-0304}

The deformation-obstruction theory of a geometric object operates at several distinct levels that should not be conflated.

At the most fundamental level, the deformation functor $\mathcal{M}: \mathbf{Art}/k \to \mathbf{Set}$ is defined purely in terms of the object $E$ and its base extensions, without reference to any moduli space. The tangent space $\mathcal{M}(k[\epsilon]/(\epsilon^2))$ and obstruction spaces exist intrinsically.

When a fine moduli space $M$ exists (carrying a universal family), the functor $\mathcal{M}$ is pro-representable by the formal completion $\widehat{M}_{[E]}$, and there is a canonical identification

$$
T_{[E]} M = \mathcal{M}(\operatorname{Spec}(k[\epsilon]/(\epsilon^2))).
$$

However, when only a coarse moduli space $M$ exists, this identification fails in general. The coarse moduli map $\mathcal{M} \to h_M$ need not be an isomorphism on tangent spaces. If $E$ has nontrivial automorphisms, first-order deformations modulo automorphisms may differ from the Zariski tangent space. This is particularly important for the moduli of semistable sheaves: the moduli functor is typically not representable, and the coarse moduli space (constructed via GIT) can have tangent spaces at properly semistable points that differ from $\operatorname{Ext}^1(E,E)$.

A concrete instance: if $E = E_1 \oplus E_2$ is a direct sum of two non-isomorphic stable sheaves of the same slope (a properly $S$-equivalent point), then $\operatorname{Ext}^1(E,E) = \operatorname{Ext}^1(E_1,E_1) \oplus \operatorname{Ext}^1(E_1,E_2) \oplus \operatorname{Ext}^1(E_2,E_1) \oplus \operatorname{Ext}^1(E_2,E_2)$, but the tangent space to the coarse moduli space at $[E]$ sees only the diagonal deformations $\operatorname{Ext}^1(E_1,E_1) \oplus \operatorname{Ext}^1(E_2,E_2)$, since the off-diagonal terms correspond to deformations that are identified under $S$-equivalence.

<!-- BENCHMARK_PROBLEM: Give an example of a coherent sheaf $E$ on a smooth projective variety $X$ such that the coarse moduli space $M$ of semistable sheaves exists, but $T_{[E]} M \neq \operatorname{Ext}^1(E, E)$. Explain why the identification fails. -->

## Deformation of quotient sheaves
Let $X$ be a scheme over $k$. $\mathcal{F}$ be a coherent sheaf on $X$, $\mathcal{S}_{0}$ be a coherent subsheaf of $\mathcal{F}$, $\mathcal{Q}_{0}$ be the quotient. Define the deformation functor

$$
D:=D_{[\mathcal{F}\rightarrow \mathcal{Q}_{0}\rightarrow 0]}: \mathbf{Art}/k\rightarrow \mathbf{Set}
$$

$$
A\mapsto \{ \text{exact sequences of } A\text{-flat sheaves } 0\rightarrow \mathcal{S}\rightarrow \mathcal{F}\otimes_{k}A\rightarrow \mathcal{Q}\rightarrow 0 \text{ on } X_{A},  \mathcal{S}\otimes_{A}k\cong \mathcal{S}_{0} \}/\sim.
$$

By definition, $[0\rightarrow \mathcal{S}'\rightarrow \mathcal{F}\otimes_{k}B\rightarrow \mathcal{Q}'\rightarrow 0]\in D(B)$ is a deformation of $[0\rightarrow \mathcal{S}\rightarrow \mathcal{F}\otimes_{k}A\rightarrow \mathcal{Q}\rightarrow 0]\in D(A)$ if and only if we have

- $\mathcal{S}'\otimes_{B}A=\mathcal{S}$
- $\mathcal{S}'$ is flat over $B$. We know $\mathcal{S}'\otimes_{B}A=\mathcal{S}$ is flat over $A$, thus we only need $\mathcal{S}'\otimes_{B} M=\mathcal{S}\otimes_{B}A\otimes_{A}M=\mathcal{S}\otimes_{A}M \rightarrow \mathcal{S}'$ is an injection. In other words, flatness is equivalent to the existence of the short exact sequence

$$
0\rightarrow \mathcal{S}\otimes_{A}M\rightarrow \mathcal{S}'\rightarrow \mathcal{S}\rightarrow 0.
$$

In other words, an extension exists if and only if we can find a subsheaf $\mathcal{E}$ of  $\mathcal{F}\otimes_{k}B/\mathcal{S}\otimes_{A}M=\mathcal{F}\otimes_{k}B/\operatorname{im}(\alpha)$ whose image in $\mathcal{F}\otimes_{k}A$ is exactly $\mathcal{S}$. Because the image lies in $\mathcal{S}$, we only need to find a subsheaf of $\ker(\beta)/\operatorname{im}(\alpha)$ has this property. In other words, we need the following sequence to split

$$
0\rightarrow \ker\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\rightarrow \mathcal{S}\rightarrow 0.
$$

We can check that $\ker=\mathcal{F}\otimes_{k}M/\mathcal{S}\otimes_{A}M=\mathcal{Q}\otimes_{A}M$. That is, the obstruction is given by

$$
\operatorname{ob}=[0\rightarrow \mathcal{Q}\otimes_{A}M\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\rightarrow \mathcal{S}\rightarrow 0]\in \operatorname{Ext}^{1}_{\mathcal{O}_{X_{B}}}(\mathcal{S}, \mathcal{Q}\otimes_{A}M).
$$

Moreover, all flat deformations of the given element is bijective to

$$
\operatorname{Ext}^{0}_{\mathcal{O}_{X_{B}}}(\mathcal{S}, \mathcal{Q}\otimes_{A}M)=\operatorname{Hom}(\mathcal{S}, \mathcal{Q}\otimes_{A}M).
$$

<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
& 0\arrow{d} & & 0 \arrow{d}\\
& \mathcal{S}\otimes_{A}M\arrow{d}\arrow[dashrightarrow]{dr}{\alpha}& & \mathcal{S}\arrow{d}\\
0\arrow{r} & \mathcal{F}\otimes_{k}M\arrow{r}\arrow{d}& \mathcal{F}\otimes_{k}B\arrow[dashrightarrow]{dr}{\beta}\arrow{r}& \mathcal{F}\otimes_{k}A\arrow{r}\arrow{d} & 0\\
&\mathcal{Q}\otimes_{A}M\arrow{d} & &\mathcal{Q}\arrow{d}\\
& 0 & &0
\end{tikzcd}
```

There's still one more issue, these two $\operatorname{Ext}$ groups still depend on $B$. We claim that  the $M(\ker(\beta)/\operatorname{im}(\alpha))=0$. Indeed if $\gamma=\sum f_{i}\otimes_{k}b_{i}\in \ker(\beta)$, then we have $\sum f_{i}\otimes_{k}a_{i}\in \mathcal{S}$, where $a_{i}=b_{i}\pmod M$. Then $m\gamma =\sum f_{i}\otimes mb_{i}=\sum f_{i}\otimes ma_{i}$, the last identity comes from the fact that $M^{2}=0$, thus $ma_{i}$ is well defined. Then $m\gamma=m(\sum f_{i}\otimes_{k}a_{i})\in \operatorname{im}(\alpha)$.
Apply $\otimes_{A}k$ to

$$
0\rightarrow \ker\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\rightarrow \mathcal{S}\rightarrow 0.
$$

We still get an exact sequence by the $A$-flatness of $\mathcal{S}$

$$
0\rightarrow \mathcal{Q}\otimes_{A}M\rightarrow \ker(\beta)/\operatorname{im}(\alpha)\otimes_{A}k\rightarrow \mathcal{S}\otimes_{A}k\rightarrow 0.
$$

We can check that we have the following commutative diagram. If we just consider small extensions, we have $\mathcal{Q}\otimes_{A}M\otimes_{A}k=\mathcal{Q}\otimes_{A}M$ because $m_{A}M=0$.
<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
& & 0\arrow{d}& 0\arrow{d}&\\
 & & \mathcal{S}\otimes_{A}m_{A}\arrow{d}\arrow[r, equal]&  \mathcal{S}\otimes_{A}m_{A}\arrow{d}&\\
 0\arrow{r}&\mathcal{Q}\otimes_{A}M \arrow{r}\arrow[d,equal]& \ker(\beta)/\operatorname{im}(\alpha)\arrow{r}\arrow{d}&  \mathcal{S}\arrow{d}\arrow{r}& 0\\
 0\arrow{r}&\mathcal{Q}\otimes_{A}M \arrow{r}& \ker(\beta)/\operatorname{im}(\alpha)\otimes_{A}k\arrow{r}\arrow{d}&\mathcal{S}\otimes_{A}k \arrow{d}\arrow{r}&0\\
 & & 0& 0& \\
\end{tikzcd}
```

In conclusion, we have

$$
\operatorname{Hom}_{X_{A}}(\mathcal{S},\mathcal{Q}\otimes_{A}M)=\operatorname{Hom}_{X}(\mathcal{S}\otimes_{A}k,\mathcal{Q}\otimes_{A}M)=\operatorname{Hom}_{X}(\mathcal{S}_{0}, \mathcal{Q}_{0})\otimes_{k}M
$$

$$
\operatorname{Ext}^{1}_{X_{A}}(\mathcal{S}, \mathcal{Q}\otimes_{A}M)=\operatorname{Ext}^{1}_{X}(\mathcal{S}\otimes_{A}k, \mathcal{Q}\otimes_{A}M)=\operatorname{Ext}^{1}_{X}(\mathcal{S}_{0}, \mathcal{Q}_{0})\otimes_{k} M.
$$

Because $m_{A}M=0$, any element in $\operatorname{Hom}_{X_{A}}(\mathcal{S}, \mathcal{Q}\otimes_{A}M)$ factors through the geometric fibre. And we can take out $M$ because of the projection formula, $M$ is simply viewed as a vector space. As a special case, the tangent-obstruction theory of the Hilbert scheme functor $H_{Z,X}$ is given by $T_{1}=\operatorname{Hom}_{\mathcal{O}_{X}}(I_{Z}, \mathcal{O}_{Z}), T_{2}=\operatorname{Ext}^{1}_{\mathcal{O}_{X}}(I_{Z}, \mathcal{O}_{Z})$.

### Remark {#ecag-0305}

The tangent space at a point $[Z]$ on the Hilbert scheme $\operatorname{Hilb}^n(X)$ of $n$ points on a smooth quasi-projective variety $X$ admits three canonical descriptions, all naturally isomorphic:

$$
T_Z \operatorname{Hilb}^n(X) \;=\; \operatorname{Hom}_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{O}_Z) \;=\; \operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{O}_Z, \mathcal{O}_Z) \;=\; \operatorname{Ext}^1_{\mathcal{O}_X}(\mathcal{I}_Z, \mathcal{I}_Z).
$$

**First isomorphism: $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \cong \operatorname{Ext}^1(\mathcal{O}_Z, \mathcal{O}_Z)$.** Apply $\operatorname{Hom}(-, \mathcal{O}_Z)$ to the short exact sequence $0 \to \mathcal{I}_Z \to \mathcal{O}_X \to \mathcal{O}_Z \to 0$. The long exact sequence begins

$$
0 \to \operatorname{Hom}(\mathcal{O}_Z, \mathcal{O}_Z) \to \operatorname{Hom}(\mathcal{O}_X, \mathcal{O}_Z) \to \operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \to \operatorname{Ext}^1(\mathcal{O}_Z, \mathcal{O}_Z) \to \operatorname{Ext}^1(\mathcal{O}_X, \mathcal{O}_Z) \to \cdots
$$

The first map is an isomorphism (both terms equal $\operatorname{Hom}(\mathcal{O}_Z, \mathcal{O}_Z)$ via restriction from $\mathcal{O}_X$ to $\mathcal{O}_Z$), and $\operatorname{Ext}^1(\mathcal{O}_X, \mathcal{O}_Z) = H^1(X, \mathcal{O}_Z) = 0$ since $\mathcal{O}_Z$ is supported on a zero-dimensional subscheme. So the connecting map gives the isomorphism.

**Second isomorphism: $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \cong \operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{I}_Z)$.** Apply $\operatorname{Hom}(\mathcal{I}_Z, -)$ to the same sequence:

$$
\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_X) \to \operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z) \to \operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{I}_Z) \to \operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{O}_X).
$$

When $X$ is smooth, $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_X) \cong H^0(X, \mathcal{O}_X)$ (any map $\mathcal{I}_Z \to \mathcal{O}_X$ extends to $\mathcal{O}_X \to \mathcal{O}_X$ by normality, hence is multiplication by a global function). This first map sends $1 \in H^0(\mathcal{O}_X)$ to the inclusion $\mathcal{I}_Z \hookrightarrow \mathcal{O}_X \twoheadrightarrow \mathcal{O}_Z$, which is the zero map in $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z)$ only when $Z = \emptyset$. For the term $\operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{O}_X)$: from the sequence $0 \to \mathcal{I}_Z \to \mathcal{O}_X \to \mathcal{O}_Z \to 0$ and $\mathcal{E}xt^i(\mathcal{O}_X, \mathcal{O}_X) = 0$ for $i > 0$, one obtains $\mathcal{E}xt^1(\mathcal{I}_Z, \mathcal{O}_X) \cong \mathcal{E}xt^2(\mathcal{O}_Z, \mathcal{O}_X)$, and the vanishing conditions (depending on $\dim X$) yield the desired isomorphism.

Alternatively, the last isomorphism follows from viewing $\operatorname{Hilb}^n(X)$ as the moduli space of rank-$1$ torsion-free sheaves: the ideal sheaf $\mathcal{I}_Z$ is a rank-$1$ torsion-free sheaf, and the deformation theory of coherent sheaves (Theorem ecag-0302) identifies the tangent space with $\operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{I}_Z)$.

**Verification for a single point.** Let $X$ be a smooth surface and $Z$ a single reduced point. Then $\mathcal{I}_Z = \mathfrak{m}_Z$ (the maximal ideal sheaf) and $\mathcal{O}_Z = k$. We have $\operatorname{Hom}(\mathfrak{m}_Z, k) = (\mathfrak{m}_Z / \mathfrak{m}_Z^2)^* \cong k^2$ (the Zariski cotangent space), so $\dim T_Z \operatorname{Hilb}^1(X) = 2 = \dim X$. This is consistent with $\operatorname{Hilb}^1(X) \cong X$.

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective surface over $\mathbb{C}$, and let $Z \subset X$ consist of a single reduced point. Compute $\dim_k T_Z \operatorname{Hilb}^1(X)$ using each of the three descriptions $\operatorname{Hom}(\mathcal{I}_Z, \mathcal{O}_Z)$, $\operatorname{Ext}^1(\mathcal{O}_Z, \mathcal{O}_Z)$, and $\operatorname{Ext}^1(\mathcal{I}_Z, \mathcal{I}_Z)$, and verify they agree. -->

## Deformation theory the instanton moduli space
The instanton moduli space $\mathcal{M}(n,r)$ is defined to be moduli of rank $2$ torsion-free sheaves on $\mathbf{P}^{2}$ framed at infinity.
## Deformation of Hilbert schemes
## Hilbert schemes of points on surfaces
## Deformation of Calabi-Yau varieties

## Deformation of varieties
## Deformation of nodes
