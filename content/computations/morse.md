---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/morse.tex
---

## Morse theory

### Example: Morse theory on Grassmannians {#ecag-0245}

The Grassmannian $\operatorname{Gr}(k,n)$ of $k$-planes in $\mathbb{C}^n$ has Poincare polynomial given by the Gaussian binomial coefficient:

$$
P_t(\operatorname{Gr}(k,n)) = \frac{\prod_{i=1}^{n}(1-t^{2i})}{\prod_{i=1}^{k}(1-t^{2i})\cdot\prod_{i=1}^{n-k}(1-t^{2i})}.
$$

We compute this via the torus action and Morse theory.

**Torus action and fixed points.** The torus $T = (\mathbb{C}^*)^n$ acts on $\operatorname{Gr}(k,n)$ by scaling columns: for $t = \operatorname{diag}(t_1,\dots,t_n)$ and a $k \times n$ matrix representative $A$ of $[W] \in \operatorname{Gr}(k,n)$, the action is $A \mapsto A \cdot t$. A point $[W]$ is $T$-fixed if and only if $W$ is spanned by coordinate vectors, so the fixed points correspond to $k$-element subsets $J = \{j_1 < j_2 < \dots < j_k\} \subset \{1,\dots,n\}$. There are $\binom{n}{k}$ such fixed points, one for each Plucker coordinate $x_J$.

**Tangent weights and Morse index.** At the fixed point corresponding to $J$, the tangent space $T_{[W]}\operatorname{Gr}(k,n) \cong \operatorname{Hom}(W, \mathbb{C}^n/W)$ decomposes into one-dimensional $T$-weight spaces:

$$
T_{[W]}\operatorname{Gr}(k,n) \cong \bigoplus_{\substack{i \in J \\ j \notin J}} V(i,j), \quad \text{weight}(V(i,j)) = t_j t_i^{-1}.
$$

For a generic moment map $\mu([W]) = \sum_{i \in J} \lambda_i$ with $\lambda_1 > \lambda_2 > \dots > \lambda_n$, the Morse index at $x_J$ is twice the number of pairs $(i,j)$ with $i \in J$, $j \notin J$, $j > i$:

$$
d_J = 2\,\#\{(i,j) : i\in J,\, j\notin J,\, j>i\}.
$$

Since all Morse indices are even --- a consequence of $\operatorname{Gr}(k,n)$ being a complex manifold with moment map from a torus action --- the Morse inequalities are equalities and $P_t(\operatorname{Gr}(k,n)) = \sum_J t^{d_J}$.

**Partition interpretation.** The data of a $k$-element subset $J = \{j_1 < \dots < j_k\} \subset \{1,\dots,n\}$ is equivalent to a partition $\lambda = (j_k - k, \dots, j_1 - 1)$ fitting inside a $k \times (n-k)$ rectangle. Under this bijection, $d_J/2 = |\lambda|$, the size of the partition. Thus

$$
P_t(\operatorname{Gr}(k,n)) = \sum_{\lambda \subset k \times (n-k)} t^{2|\lambda|},
$$

and the Poincare polynomial is symmetric in $t^2$ by the involution $\lambda \mapsto \lambda^c$ (complementary partition in the rectangle).

**Recursion and closed form.** Partitioning according to whether $j_k = n$ (the partition has a full bottom row of length $n - k$) or $j_k < n$ gives the recursion

$$
P_t(k,n) = P_t(k, n-1) + t^{2(n-k)} P_t(k-1, n-1),
$$

which solves to the Gaussian binomial coefficient. The base cases are $P_t(0,n) = P_t(n,n) = 1$.

**Verification for $\operatorname{Gr}(2,4)$.** The six subsets $J \subset \{1,2,3,4\}$ of size $2$ give:

| $J$ | Pairs $(i \in J,\, j \notin J,\, j > i)$ | $d_J$ |
|-----|-------------------------------------------|-------|
| $\{1,2\}$ | $(1,3),(1,4),(2,3),(2,4)$ | $8$ |
| $\{1,3\}$ | $(1,2)$ is excluded since $2 \notin J$ but $2 < 3$; actual: $(1,4),(3,4)$ plus $(1,2)$? No: $(1,4),(3,4)$ and we also need $j > i$: $(1,2)$ has $j=2 \notin J$ and $2>1$ so yes. Pairs: $(1,2),(1,4),(3,4)$ | $6$ |

Let us redo this systematically. For $J = \{j_1,j_2\}$, we count pairs $(i,j)$ with $i \in J$, $j \notin J$, $j > i$:

| $J$ | $d_J/2$ | $d_J$ |
|-----|---------|-------|
| $\{1,2\}$ | $|\{(1,3),(1,4),(2,3),(2,4)\}| = 4$ | $8$ |
| $\{1,3\}$ | $|\{(1,2),(1,4),(3,4)\}| = 3$ | $6$ |
| $\{1,4\}$ | $|\{(1,2),(1,3)\}| = 2$ | $4$ |
| $\{2,3\}$ | $|\{(2,4),(3,4)\}| = 2$ | $4$ |
| $\{2,4\}$ | $|\{(2,3)\}| = 1$ | $2$ |
| $\{3,4\}$ | $|\{\}| = 0$ | $0$ |

So $P_t(\operatorname{Gr}(2,4)) = 1 + t^2 + 2t^4 + t^6 + t^8$, which agrees with the Gaussian binomial $\binom{4}{2}_{t^2} = \frac{(1-t^2)(1-t^4)(1-t^6)(1-t^8)}{(1-t^2)^2(1-t^4)^2}$.

For $\mathbb{P}^n = \operatorname{Gr}(1,n+1)$, the fixed points $J = \{j\}$ have $d_J = 2(n+1-j)$ for $j = 1,\dots,n+1$, giving $P_t(\mathbb{P}^n) = 1 + t^2 + \dots + t^{2n}$.

<!-- BENCHMARK_PROBLEM: Compute the Poincare polynomial $P_t(\operatorname{Gr}(2,5))$ by enumerating all $\binom{5}{2}=10$ fixed points of the torus action, computing the Morse index $d_J$ for each subset $J\subset\{1,2,3,4,5\}$ of size $2$, and verify the result equals $\frac{(1-t^2)(1-t^4)(1-t^6)(1-t^8)(1-t^{10})}{(1-t^2)(1-t^4)(1-t^2)(1-t^4)(1-t^6)}$. -->

### Remark: Nakajima's operators {#ecag-0246}

The Poincare polynomials $P_t(\operatorname{Gr}(k,n))$ admit a representation-theoretic interpretation through the Boson--Fermion correspondence. The generating function

$$
\sum_{n \geq k \geq 0} q^n z^k P_t(\operatorname{Gr}(k,n))
$$

is related to the trace over a Fock space representation of the Heisenberg algebra. Nakajima's construction provides a geometric realization: creation and annihilation operators $\mathfrak{q}_n$ on $\bigoplus_m \mathrm{H}^*(\operatorname{Hilb}^m(S))$ act by correspondences, and the character of this representation recovers the product formula for Poincare polynomials.

For Grassmannians specifically, the relevant operators come from Hecke correspondences

$$
\operatorname{Gr}(k,n) \leftarrow \operatorname{Fl}(k,k+1;n) \rightarrow \operatorname{Gr}(k+1,n),
$$

which intertwine the cohomology groups and give rise to an action of a quantum group or affine Lie algebra. The Poincare polynomial generating function thus reflects the graded dimension of an irreducible representation.

As a consistency check, setting $t = 1$ in $P_t(\operatorname{Gr}(k,n))$ gives $\binom{n}{k}$ (the number of $k$-element subsets, since each partition contributes $1$), and so $\sum_{k=0}^n z^k P_1(\operatorname{Gr}(k,n)) = (1+z)^n$.

<!-- BENCHMARK_PROBLEM: Compute $\sum_{k=0}^{n} z^k P_t(\operatorname{Gr}(k,n))$ for $n=4$ and express the result as a product formula. Verify that setting $t=1$ and $z=1$ gives $2^4 = 16$, the total number of subsets of a $4$-element set. -->

### Example: Moment maps on $\operatorname{Hilb}^n(\mathbb{C}^2)$ {#ecag-0247}

The Hilbert scheme of $n$ points $\operatorname{Hilb}^n(\mathbb{C}^2)$ is a smooth variety of dimension $2n$ (Fogarty's theorem) carrying a natural $T = (\mathbb{C}^*)^2$-action induced from $(t_1,t_2) \cdot (x,y) = (t_1 x, t_2 y)$ on $\mathbb{C}^2$. The $T$-fixed points are monomial ideals, parametrized by partitions of $n$: the partition $\lambda \vdash n$ corresponds to the monomial ideal $I_\lambda \subset \mathbb{C}[x,y]$ whose complement $\{x^a y^b : (a,b) \in \lambda\}$ forms a basis of $\mathbb{C}[x,y]/I_\lambda$.

**Tangent weights.** The tangent space $T_{I_\lambda}\operatorname{Hilb}^n(\mathbb{C}^2) \cong \operatorname{Hom}_{\mathbb{C}[x,y]}(I_\lambda, \mathbb{C}[x,y]/I_\lambda)$ decomposes into $T$-weight spaces. For each cell $s = (i,j)$ in the Young diagram of $\lambda$, there are two contributing weights:

$$
t_1^{-l(s)-1}\, t_2^{a(s)} \quad\text{and}\quad t_1^{l(s)}\, t_2^{-a(s)-1},
$$

where $a(s) = \lambda_i - j - 1$ is the arm length and $l(s) = \lambda'_j - i - 1$ is the leg length. This gives $2n$ weights in total, matching $\dim T_{I_\lambda}\operatorname{Hilb}^n(\mathbb{C}^2) = 2n$.

**Morse index.** Choose a generic one-parameter subgroup $\rho: \mathbb{C}^* \to T$ given by $t \mapsto (t^{m_1}, t^{m_2})$ with $m_1, m_2 > 0$ generic. The composition with the moment map gives a perfect Morse function with isolated critical points at the monomial ideals. The Morse index at $I_\lambda$ is twice the number of negative weights under $\rho$, which equals $2(n(\lambda) + n(\lambda'))$, where $n(\lambda) = \sum_i (i-1)\lambda_i$.

Since all Morse indices are even (isolated critical points on a smooth complex manifold), the Morse inequalities are equalities:

$$
P_t(\operatorname{Hilb}^n(\mathbb{C}^2)) = \sum_{\lambda \vdash n} t^{2(n(\lambda)+n(\lambda'))}.
$$

**Verification for $n = 3$.** The three partitions of $3$ and their invariants:

| $\lambda$ | $\lambda'$ | $n(\lambda) = \sum(i-1)\lambda_i$ | $n(\lambda')$ | Morse index |
|-----------|-----------|-----------------------------------|---------------|-------------|
| $(3)$ | $(1,1,1)$ | $0$ | $0+1+2 = 3$ | $6$ |
| $(2,1)$ | $(2,1)$ | $0 \cdot 2 + 1 \cdot 1 = 1$ | $0 \cdot 2 + 1 \cdot 1 = 1$ | $4$ |
| $(1,1,1)$ | $(3)$ | $0+1+2 = 3$ | $0$ | $6$ |

So $P_t(\operatorname{Hilb}^3(\mathbb{C}^2)) = t^6 + t^4 + t^6 = 2t^6 + t^4$. But this gives the wrong answer; let us recompute more carefully.

For $\lambda = (3)$: cells are $(1,1),(1,2),(1,3)$. We have $n(\lambda) = (1-1) \cdot 3 = 0$. The conjugate is $\lambda' = (1,1,1)$, so $n(\lambda') = (1-1)\cdot 1 + (2-1)\cdot 1 + (3-1)\cdot 1 = 0 + 1 + 2 = 3$. Index $= 2(0+3) = 6$.

For $\lambda = (2,1)$: $n(\lambda) = 0 \cdot 2 + 1 \cdot 1 = 1$. Conjugate $\lambda' = (2,1)$, so $n(\lambda') = 0 \cdot 2 + 1 \cdot 1 = 1$. Index $= 2(1+1) = 4$.

For $\lambda = (1,1,1)$: $n(\lambda) = 0 + 1 + 2 = 3$. Conjugate $\lambda' = (3)$, so $n(\lambda') = 0$. Index $= 2(3+0) = 6$.

This gives $P_t = t^6 + t^4 + t^6 = 2t^6 + t^4$, but the correct answer is $P_t(\operatorname{Hilb}^3(\mathbb{C}^2)) = 1 + t^2 + 2t^4 + t^6$. The discrepancy arises because the Morse index should be computed from negative weights for a specific choice of generic $\rho$, not directly from $n(\lambda) + n(\lambda')$. Indeed, the Betti numbers of $\operatorname{Hilb}^n(\mathbb{C}^2)$ are given by the number of partitions of $n$ with a given value of $n(\lambda)$ alone (not $n(\lambda) + n(\lambda')$), since by the Ellingsrud--Stromme/Goettsche result the Poincare polynomial satisfies

$$
\sum_{n=0}^{\infty} P_t(\operatorname{Hilb}^n(\mathbb{C}^2))\, q^n = \prod_{k=1}^{\infty} \frac{1}{1-q^k t^{2(k-1)}}.
$$

Expanding through $n = 3$: the coefficient of $q^3$ in $\prod_{k \geq 1}(1 - q^k t^{2(k-1)})^{-1}$ is obtained from $q^3 \cdot 1$ (partition $(1,1,1)$, contributing $t^0 \cdot t^2 \cdot t^4 = t^6$... let us use the standard expansion). The factors are $\frac{1}{1-q} \cdot \frac{1}{1-q^2 t^2} \cdot \frac{1}{1-q^3 t^4} \cdots$. Expanding:

- $\lambda = (1,1,1)$: three parts of size $1$, contributing $t^{0+0+0} = 1$ (each part of size $k$ contributes $t^{2(k-1)}$, so size-$1$ parts contribute $t^0$). Total: $t^0 = 1$.
- $\lambda = (2,1)$: one part of size $2$ and one of size $1$, contributing $t^{2} \cdot t^0 = t^2$.
- $\lambda = (3)$: one part of size $3$, contributing $t^{4}$.

So $P_t(\operatorname{Hilb}^3(\mathbb{C}^2)) = 1 + t^2 + t^4$, which has $p(3) = 3$ terms. This is the correct answer: $b_0 = 1$, $b_2 = 1$, $b_4 = 1$, all other Betti numbers zero.

The Goettsche formula shows that $\operatorname{Hilb}^n(\mathbb{C}^2)$ has no odd cohomology, and each partition $\lambda \vdash n$ contributes a single cell of dimension $2\sum_{i}(k_i - 1)$ where $k_i$ are the part sizes --- equivalently, $2n(\lambda)$ where $n(\lambda) = \sum_i \binom{\lambda'_i}{2}$ (the sum of $\binom{\text{column height}}{2}$).

<!-- BENCHMARK_PROBLEM: For $n=3$, enumerate all partitions $\lambda$ of $3$, namely $(3)$, $(2,1)$, and $(1,1,1)$. For each partition, compute $n(\lambda)=\sum_i(i-1)\lambda_i$ and $n(\lambda')$ where $\lambda'$ is the conjugate partition. Then compute the Morse index $2(n(\lambda)+n(\lambda'))$ at each fixed point and verify that $P_t(\operatorname{Hilb}^3(\mathbb{C}^2))=1+t^2+2t^4+t^6$. -->

### Example: Moment maps on smooth nested Hilbert schemes {#ecag-0248}

The nested Hilbert scheme $(\mathbb{C}^2)^{[n,n+1]}$ parametrizes pairs of ideals $(I_1, I_2)$ with $I_2 \subset I_1 \subset \mathbb{C}[x,y]$ and $\operatorname{colength}(I_k) = n_k$, or equivalently flags of zero-dimensional subschemes $Z_n \subset Z_{n+1} \subset \mathbb{C}^2$ with $\operatorname{length}(Z_k) = k$. When $n_2 = n_1 + 1$, the nested Hilbert scheme is smooth of dimension $2(n+1)$.

**Relation to the universal family.** The scheme $(\mathbb{C}^2)^{[n,n+1]}$ is isomorphic to the universal family $\mathcal{Z}_{n+1}$ over $\operatorname{Hilb}^{n+1}(\mathbb{C}^2)$: a point $(Z_n \subset Z_{n+1})$ determines $Z_{n+1}$ together with the reduced point $Z_{n+1} \setminus Z_n$. More precisely, the forgetful map $(\mathbb{C}^2)^{[n,n+1]} \to \operatorname{Hilb}^{n+1}(\mathbb{C}^2)$ sending $(Z_n \subset Z_{n+1}) \mapsto Z_{n+1}$ is a flat family whose fiber over $[Z_{n+1}]$ is $Z_{n+1}$ itself (as a scheme). Smoothness follows from Fogarty's theorem combined with the identification as a Nakajima quiver variety.

**$T$-fixed points.** The $T = (\mathbb{C}^*)^2$-action on $\mathbb{C}^2$ induces an action on $(\mathbb{C}^2)^{[n,n+1]}$. The fixed points are pairs of monomial ideals $(I_\lambda, I_\mu)$ with $I_\mu \subset I_\lambda$, corresponding to pairs of partitions $(\lambda, \mu)$ where $\mu \vdash (n+1)$ and $\lambda$ is obtained from $\mu$ by removing a single box. The number of such pairs equals $\sum_{\mu \vdash (n+1)} r(\mu)$, where $r(\mu)$ is the number of removable corners of $\mu$.

**Tangent weights and Morse theory.** The tangent space at $(I_\lambda, I_\mu)$ decomposes under $T$ as

$$
T_{(I_\lambda, I_\mu)} (\mathbb{C}^2)^{[n,n+1]} \cong \operatorname{Hom}(I_\mu, \mathbb{C}[x,y]/I_\mu) \oplus \operatorname{Hom}(I_\mu/I_\lambda, \mathbb{C}[x,y]/I_\lambda),
$$

with appropriate corrections from the tangent-obstruction theory. Since the nested Hilbert scheme is smooth with isolated fixed points and all Morse indices are even, the Poincare polynomial is

$$
P_t((\mathbb{C}^2)^{[n,n+1]}) = \sum_{\substack{\mu \vdash (n+1) \\ s \in \mu \text{ removable}}} t^{2\,\operatorname{ind}(\mu, s)},
$$

where $\operatorname{ind}(\mu, s)$ is the Morse index at the fixed point $(\mu \setminus s, \mu)$.

**Enumeration for $n = 2$.** The partitions of $3$ and their removable corners:

| $\mu \vdash 3$ | Removable corners $s$ | Pairs $(\lambda, \mu)$ |
|----------------|----------------------|------------------------|
| $(3)$ | $(1,3)$ | $((2), (3))$ |
| $(2,1)$ | $(1,2)$ and $(2,1)$ | $((1,1),(2,1))$ and $((2),(2,1))$ |
| $(1,1,1)$ | $(3,1)$ | $((1,1),(1,1,1))$ |

Total: $1 + 2 + 1 = 4$ fixed points, confirming $\sum_{\mu \vdash 3} r(\mu) = 4$.

<!-- BENCHMARK_PROBLEM: For $n=2$, enumerate all fixed points of $(\mathbb{C}^2)^{[2,3]}$ by listing all partitions $\mu$ of $3$ together with their removable boxes, and count the total number of fixed points. Verify this equals $\sum_{\mu\vdash 3} r(\mu)$ where $r(\mu)$ is the number of removable corners of $\mu$. -->

### Remark: Coadjoint orbits, symplectic forms, and moment maps {#ecag-0249}

Coadjoint orbits of a compact Lie group $G$ provide the fundamental examples connecting symplectic geometry, representation theory, and Morse theory.

For a compact Lie group $G$ with Lie algebra $\mathfrak{g}$, the coadjoint orbit $\mathcal{O}_\xi = G \cdot \xi \subset \mathfrak{g}^*$ through $\xi \in \mathfrak{g}^*$ carries the Kirillov--Kostant--Souriau symplectic form: for tangent vectors $X^\sharp_\eta, Y^\sharp_\eta$ at $\eta \in \mathcal{O}_\xi$ generated by $X, Y \in \mathfrak{g}$,

$$
\omega_\eta(X^\sharp_\eta, Y^\sharp_\eta) = \langle \eta, [X,Y] \rangle.
$$

This $2$-form is $G$-invariant and nondegenerate (the kernel of $X \mapsto X^\sharp_\eta$ is precisely the stabilizer $\mathfrak{g}_\eta$, which is the annihilator of $T_\eta \mathcal{O}_\xi$ under the pairing). The inclusion $\mu: \mathcal{O}_\xi \hookrightarrow \mathfrak{g}^*$ is itself a moment map for the $G$-action.

**Flag manifolds from $U(n)$.** For $G = U(n)$, the coadjoint representation is identified with the adjoint representation via the invariant inner product $\langle A, B \rangle = \operatorname{tr}(A^*B)$, so coadjoint orbits are conjugacy classes of Hermitian matrices. The orbit through $\xi = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ is a flag manifold whose type depends on the multiplicities among the $\lambda_i$. The maximal torus $T \subset U(n)$ of diagonal matrices acts in a Hamiltonian fashion, and the moment map $\mu_T: \mathcal{O}_\xi \to \mathfrak{t}^*$ is the projection onto diagonal entries. By the Atiyah--Guillemin--Sternberg convexity theorem, the image $\mu_T(\mathcal{O}_\xi)$ is the convex hull of the Weyl group orbit $W \cdot \xi = S_n \cdot (\lambda_1, \dots, \lambda_n)$.

**Grassmannians as coadjoint orbits.** The Grassmannian $\operatorname{Gr}(k,n)$ is the orbit through $\xi = \operatorname{diag}(\underbrace{1,\dots,1}_k, \underbrace{0,\dots,0}_{n-k})$, which has exactly two distinct eigenvalues. The moment map for the maximal torus is $\mu_T([W]) = \operatorname{diag}(\|e_1^W\|^2, \dots, \|e_n^W\|^2)$, where $e_i^W$ is the orthogonal projection of the $i$-th standard basis vector onto $W$. A generic linear functional $f = \sum a_i x_i$ on $\mathfrak{t}^*$ composed with $\mu_T$ gives a Morse function whose critical points are the $T$-fixed points $x_J$ and whose Morse indices recover the computation of the previous example. The moment polytope is the convex hull of the $\binom{n}{k}$ vertices obtained by permuting $(\underbrace{1,\dots,1}_k, \underbrace{0,\dots,0}_{n-k})$, which is a hypersimplex $\Delta(k,n)$.

**Full flags from generic orbits.** For $G = U(3)$ and $\xi = \operatorname{diag}(2,1,0)$ (three distinct eigenvalues), the orbit is the complete flag manifold $\operatorname{Fl}(1,2;3)$, which has real dimension $2 \cdot 3 = 6$. The $T$-fixed points correspond to the $3! = 6$ permutations of $(2,1,0)$, and their images under the moment map are the six vertices of a regular hexagon in the plane $x_1 + x_2 + x_3 = 3$ inside $\mathfrak{t}^* \cong \mathbb{R}^3$. The convexity theorem guarantees the moment image is this hexagon.

<!-- BENCHMARK_PROBLEM: For $G=U(3)$ and the coadjoint orbit through $\operatorname{diag}(2,1,0)$, identify the resulting flag manifold, compute its dimension as a real manifold, determine the number of $T$-fixed points (where $T$ is the maximal torus of diagonal matrices), and verify that the convex hull of their images under the moment map is a hexagon in $\mathfrak{t}^*\cong\mathbb{R}^3$. -->
