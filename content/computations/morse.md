---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/morse.tex
---

## Morse theory

### Example: Morse theory on Grassmannian {#ecag-0245}

**Statement:** Let $\operatorname{Gr}(k,n)$ denote the Grassmannian of $k$-planes in $\mathbb{C}^n$. The Poincare polynomial of $\operatorname{Gr}(k,n)$ is given by the Gaussian binomial coefficient:

$$
P_t(\operatorname{Gr}(k,n)) = \frac{\prod_{i=1}^{n}(1-t^{2i})}{\prod_{i=1}^{k}(1-t^{2i})\cdot\prod_{i=1}^{n-k}(1-t^{2i})}.

$$

This is computed via two approaches: (1) torus localization and the moment map, and (2) explicit Morse--Smale dynamics.

**Construction/Proof:**

*Approach 1: Torus localization.*

Step 1. Define a torus action on $\operatorname{Gr}(k,n)$ by right multiplication: for $t = \operatorname{diag}(t_1, \dots, t_n) \in T = (\mathbb{C}^*)^n$ and a $k\times n$ matrix representative $A$ of a point $[W]\in\operatorname{Gr}(k,n)$, the action is $A\mapsto A\cdot t$, which scales the $j$-th column of $A$ by $t_j$.

Step 2. Identify the fixed points. A point $[W]$ is fixed by $T$ if and only if $W$ is spanned by coordinate vectors. In the standard open covering of $\operatorname{Gr}(k,n)$, these correspond to $k\times n$ matrices in reduced row echelon form with the identity block in columns indexed by $J=\{j_1<j_2<\dots<j_k\}\subset\{1,\dots,n\}$ and all other entries zero. There are exactly $\binom{n}{k}$ such fixed points, corresponding to the Plucker coordinates $\{x_J\}$.

Step 3. Compute the tangent space representation at each fixed point. For a fixed point $[W]$ corresponding to the subset $J$, the tangent space $T_{[W]}\operatorname{Gr}(k,n)\cong\operatorname{Hom}(W, \mathbb{C}^n/W)$ decomposes into $T$-weight spaces:

$$
T_{[W]}\operatorname{Gr}(k,n)\cong \bigoplus_{j\notin J,\, i\in J} V(i,j), \quad \text{weight}(V(i,j))=t_j t_i^{-1},

$$

where $V(i,j)$ is the one-dimensional weight space at position $(i,j)$ in the matrix.

Step 4. Compute the Morse index. For a generic choice of moment map $\mu:{\operatorname{Gr}(k,n)}\to\mathfrak{t}^*$ (e.g., $\mu([W])=\sum_{i\in J}\lambda_i$ for generic real $\lambda_1>\lambda_2>\dots>\lambda_n$), the Morse index at the fixed point $x_J$ equals twice the number of negative weights, i.e., twice the number of pairs $(i,j)$ with $i\in J$, $j\notin J$, $j>i$. Explicitly:

$$
d_J = 2\#\{(i,j) : i\in J,\, j\notin J,\, j>i\} = 2\left[(n-k)k + \frac{k(k+1)}{2} - \sum_{\alpha=1}^k j_\alpha\right].

$$

Step 5. By Morse theory (specifically, since all critical points have even index, the Morse inequalities are equalities), the Poincare polynomial is:

$$
P_t(\operatorname{Gr}(k,n)) = \sum_{J} t^{d_J}.

$$

For $\mathbb{P}^n_{\mathbb{C}} = \operatorname{Gr}(1,n+1)$, the fixed points have indices $0, 2, 4, \dots, 2n$, each occurring once, so:

$$
P_t(\mathbb{P}^n_{\mathbb{C}}) = 1 + t^2 + t^4 + \dots + t^{2n}.

$$

Step 6. Interpret $d_J$ combinatorially. The sequence $0\leq (j_1 - 1)\leq (j_2 - 2)\leq\dots\leq(j_k - k)\leq n-k$ defines a partition $\lambda$ inside a $k\times(n-k)$ rectangle. The quantity $d_J/2$ equals the size of the complementary partition $|\lambda^c| = k(n-k) - |\lambda|$. By symmetry of partitions in the rectangle, $\sum_J t^{d_J}$ is a symmetric polynomial in $t^2$, and we may write:

$$
P_t(\operatorname{Gr}(k,n)) = \sum_{\lambda\subset k\times(n-k)} t^{2|\lambda|}.

$$

Step 7. Derive the recursive formula. Partitioning according to whether $j_k = n$ (the last row of the partition fills the entire row) or $j_k < n$:

$$
P_t(k,n) = P_t(k, n-1) + t^{2(n-k)} P_t(k-1, n-1).

$$

Step 8. Solve the recursion to obtain the closed form as a Gaussian binomial coefficient:

$$
P_t(\operatorname{Gr}(k,n)) = \frac{\prod_{i=1}^{n}(1-t^{2i})}{\prod_{i=1}^{k}(1-t^{2i})\cdot\prod_{i=1}^{n-k}(1-t^{2i})}.

$$

**Key Insight:** All Morse indices are even (because the Grassmannian is a complex manifold and the Morse function comes from a torus moment map), so the Morse inequalities become equalities and the Betti numbers are simply the number of critical points of each index --- equivalently, the number of partitions of each size fitting in a $k\times(n-k)$ box.

**Prerequisites:** Grassmannian varieties, torus actions, moment maps, Morse theory, Plucker embedding, Gaussian binomial coefficients

<!-- BENCHMARK_PROBLEM: Compute the Poincare polynomial $P_t(\operatorname{Gr}(2,5))$ by enumerating all $\binom{5}{2}=10$ fixed points of the torus action, computing the Morse index $d_J$ for each subset $J\subset\{1,2,3,4,5\}$ of size $2$, and verify the result equals $\frac{(1-t^2)(1-t^4)(1-t^6)(1-t^8)(1-t^{10})}{(1-t^2)(1-t^4)(1-t^2)(1-t^4)(1-t^6)}$. -->

Now we consider a more familiar version of the Morse theory on Grassmannians, which means, we construct a Morse function explicitly(in the localization method, the Morse function is given by the moment map of the torus action, but we don't need to write it down, since we know critical points are just those fixed points of the torus action, for more details, see Nakajima's book on Hilbert schemes, Chapter $5$).

<!-- %% -->

### Remark: Nakajima's operators {#ecag-0246}

The Poincare polynomials $P_t(\operatorname{Gr}(k,n))$ admit a natural representation-theoretic interpretation. The generating function

$$
\sum_{n\geq k\geq 0} q^n z^k P_t(\operatorname{Gr}(k,n))

$$

can be expressed in terms of characters of representations of infinite-dimensional algebras. Specifically, through the Boson--Fermion correspondence, the generating function of Gaussian binomial coefficients is related to the trace over a Fock space representation. Nakajima's construction of Heisenberg algebra actions on the cohomology of Hilbert schemes provides a geometric realization: the creation and annihilation operators $\mathfrak{q}_n$ on $\bigoplus_m \mathrm{H}^*(\operatorname{Hilb}^m(S))$ act by correspondences, and the character of this representation recovers the product formula for the generating function of Poincare polynomials. For Grassmannians, the analogous operators come from Hecke correspondences

$$
\operatorname{Gr}(k,n) \leftarrow \operatorname{Fl}(k,k+1;n) \rightarrow \operatorname{Gr}(k+1,n),

$$

which intertwine the cohomology groups and give rise to an action of a quantum group or affine Lie algebra. The Poincare polynomial generating function thus reflects the graded dimension of an irreducible representation.

<!-- BENCHMARK_PROBLEM: Compute $\sum_{k=0}^{n} z^k P_t(\operatorname{Gr}(k,n))$ for $n=4$ and express the result as a product formula. Verify that setting $t=1$ and $z=1$ gives $2^4 = 16$, the total number of subsets of a $4$-element set. -->

### Example: Moment maps on $\mathrm{Hilb}^{n}(\mathbb{C}^{2})$ {#ecag-0247}

**Statement:** The Hilbert scheme of $n$ points $\operatorname{Hilb}^n(\mathbb{C}^2)$ carries a natural hyperkahler structure and a Hamiltonian torus action by $T = (\mathbb{C}^*)^2$, induced from the standard action on $\mathbb{C}^2$. The associated moment map $\mu: \operatorname{Hilb}^n(\mathbb{C}^2) \to \mathfrak{t}^*$ is a perfect Morse--Bott function whose critical set consists of isolated fixed points indexed by partitions $\lambda$ of $n$. The Morse index at the fixed point $I_\lambda$ is $2\sum_{s\in\lambda}(a(s) + l(s) + 1) - 2n = 2(n(\lambda) + n(\lambda'))$ where $a(s)$ and $l(s)$ are the arm and leg lengths of the cell $s$ in the Young diagram of $\lambda$, and $n(\lambda) = \sum_i (i-1)\lambda_i$. Consequently, the Poincare polynomial is:

$$
P_t(\operatorname{Hilb}^n(\mathbb{C}^2)) = \sum_{\lambda\vdash n} t^{2(n(\lambda)+n(\lambda'))}.

$$

This equals $\sum_{\lambda\vdash n} t^{2n(\lambda)} \cdot t^{2n(\lambda')}$, and the generating function satisfies Goettsche's formula:

$$
\sum_{n=0}^{\infty} P_t(\operatorname{Hilb}^n(\mathbb{C}^2))\, q^n = \prod_{k=1}^{\infty} \frac{1}{1-q^k t^{2(k-1)}} \cdot \frac{1}{1-q^k t^{2k}} \cdot \frac{1}{1- q^k}.

$$

In fact, by a result of Ellingsrud--Stromme and Goettsche, $\operatorname{Hilb}^n(\mathbb{C}^2)$ has no odd-dimensional cohomology and

$$
\sum_{n=0}^{\infty} P_t(\operatorname{Hilb}^n(\mathbb{C}^2))\, q^n = \prod_{k=1}^{\infty} \frac{1}{1-q^k t^{2(k-1)}}.

$$

**Construction/Proof:**

Step 1. Identify the torus action. The $2$-dimensional torus $T=(\mathbb{C}^*)^2$ acts on $\mathbb{C}^2$ by $(t_1,t_2)\cdot(x,y)=(t_1 x, t_2 y)$. This induces an action on ideals $I\subset\mathbb{C}[x,y]$ of colength $n$, hence on $\operatorname{Hilb}^n(\mathbb{C}^2)$.

Step 2. Identify fixed points. A monomial ideal $I_\lambda = (x^{\lambda_1}, x^{\lambda_2}y, \dots, y^k, \dots)$ is $T$-fixed if and only if it is generated by monomials. Such ideals are in bijection with partitions $\lambda$ of $n$: the monomials $\{x^a y^b : (a,b)\notin\lambda\}$ form a basis for $\mathbb{C}[x,y]/I_\lambda$.

Step 3. Compute the tangent space weights. The tangent space $T_{I_\lambda}\operatorname{Hilb}^n(\mathbb{C}^2) \cong \operatorname{Hom}_{\mathbb{C}[x,y]}(I_\lambda, \mathbb{C}[x,y]/I_\lambda)$ decomposes into $T$-weight spaces. For each cell $s=(i,j)$ in the Young diagram of $\lambda$, there are two contributing weights:

$$
t_1^{-l(s)-1} t_2^{a(s)} \quad \text{and} \quad t_1^{l(s)} t_2^{-a(s)-1},

$$

where $a(s) = \lambda_i - j - 1$ is the arm length and $l(s) = \lambda'_j - i - 1$ is the leg length.

Step 4. Choose a generic one-parameter subgroup $\rho:\mathbb{C}^*\to T$ given by $t\mapsto (t^{m_1}, t^{m_2})$ with $m_1, m_2 > 0$ generic. The moment map $\mu = m_1|z_1|^2 + m_2|z_2|^2$ restricted to the fixed-point set gives a Morse function. The Morse index at $I_\lambda$ is twice the number of negative weights under $\rho$, which equals $2n(\lambda) + 2n(\lambda')$ for appropriate generic choice.

Step 5. Since all Morse indices are even (the critical points are isolated and the space is smooth of dimension $2n$), the Morse inequalities are equalities. The Poincare polynomial is the sum over partitions of $n$ of $t$ raised to the corresponding Morse index.

Step 6. The generating function follows from the bijection between partitions and sequences of non-negative integers via the conjugate partition, and standard $q$-series identities.

**Key Insight:** The torus fixed points on $\operatorname{Hilb}^n(\mathbb{C}^2)$ are monomial ideals, parametrized by partitions of $n$. The combinatorics of arm and leg lengths in Young diagrams directly encode the Morse-theoretic data, converting the topological computation into partition enumeration.

**Prerequisites:** Hilbert scheme of points, torus actions, moment maps, Morse--Bott theory, Young diagrams and partitions, Goettsche's formula

<!-- BENCHMARK_PROBLEM: For $n=3$, enumerate all partitions $\lambda$ of $3$, namely $(3)$, $(2,1)$, and $(1,1,1)$. For each partition, compute $n(\lambda)=\sum_i(i-1)\lambda_i$ and $n(\lambda')$ where $\lambda'$ is the conjugate partition. Then compute the Morse index $2(n(\lambda)+n(\lambda'))$ at each fixed point and verify that $P_t(\operatorname{Hilb}^3(\mathbb{C}^2))=1+t^2+2t^4+t^6$. -->

### Example: Moment maps on smooth nested Hilbert schemes {#ecag-0248}

**Statement:** Let $S$ be a smooth quasi-projective surface (e.g., $S = \mathbb{C}^2$). The nested Hilbert scheme $S^{[n_1, n_2]}$ for $n_1 \leq n_2$ parametrizes pairs of ideals $(I_1, I_2)$ with $I_2 \subset I_1 \subset \mathcal{O}_S$ and $\operatorname{colength}(I_k) = n_k$. Equivalently, $S^{[n_1,n_2]}$ parametrizes flags of $0$-dimensional subschemes $Z_1 \subset Z_2 \subset S$ with $\operatorname{length}(Z_k) = n_k$. When $S = \mathbb{C}^2$ and $n_2 = n_1 + 1$, the nested Hilbert scheme $(\mathbb{C}^2)^{[n, n+1]}$ is smooth of dimension $2(n+1)$ and admits a Hamiltonian $T=(\mathbb{C}^*)^2$-action. The fixed points are indexed by pairs of partitions $(\lambda, \mu)$ where $\lambda \vdash n$, $\mu \vdash (n+1)$, and the Young diagram of $\lambda$ is obtained from that of $\mu$ by removing a single box. The Poincare polynomial can be computed via localization:

$$
P_t((\mathbb{C}^2)^{[n,n+1]}) = \sum_{\substack{\mu\vdash(n+1) \\ s\in\mu}} t^{2\, \operatorname{ind}(\mu, s)},

$$

where the sum is over all partitions $\mu$ of $n+1$ and all removable boxes $s$ of $\mu$, and $\operatorname{ind}(\mu, s)$ is the Morse index at the corresponding fixed point.

**Construction/Proof:**

Step 1. The nested Hilbert scheme $S^{[n,n+1]}$ is isomorphic to the universal family over $\operatorname{Hilb}^{n+1}(S)$: a point of $S^{[n,n+1]}$ is a pair $(Z_n \subset Z_{n+1})$ where $Z_{n+1}$ has length $n+1$ and $Z_n$ has length $n$. The inclusion $Z_n\subset Z_{n+1}$ means $Z_{n+1}\setminus Z_n$ is a single reduced point, so $S^{[n,n+1]}$ fibers over $\operatorname{Hilb}^{n+1}(S)$ with fiber over $[Z_{n+1}]$ being the support of $Z_{n+1}$ (with multiplicity).

Step 2. For $S = \mathbb{C}^2$, smoothness of $(\mathbb{C}^2)^{[n,n+1]}$ follows from the smoothness of $\operatorname{Hilb}^m(\mathbb{C}^2)$ for all $m$ (Fogarty's theorem) and the fact that $(\mathbb{C}^2)^{[n,n+1]}$ is the blowup of $\operatorname{Hilb}^{n+1}(\mathbb{C}^2)$ along a natural subscheme, or alternatively from its identification with a Nakajima quiver variety.

Step 3. The $T$-fixed points of $(\mathbb{C}^2)^{[n,n+1]}$ are pairs of monomial ideals $(I_\lambda, I_\mu)$ with $I_\mu\subset I_\lambda$, corresponding to pairs $(\lambda,\mu)$ where $\mu\vdash(n+1)$ and $\lambda$ is obtained from $\mu$ by removing one box. The number of such pairs equals $\sum_{\mu\vdash(n+1)} r(\mu)$ where $r(\mu)$ is the number of removable corners of $\mu$.

Step 4. The tangent weights at each fixed point $(\lambda,\mu)$ can be computed from the tangent-obstruction theory. The tangent space decomposes as

$$
T_{(I_\lambda, I_\mu)} S^{[n,n+1]} \cong \operatorname{Hom}(I_\mu, \mathbb{C}[x,y]/I_\mu) \oplus \operatorname{Hom}(I_\mu/I_\lambda, \mathbb{C}[x,y]/I_\lambda),

$$

with appropriate corrections. The Morse index is computed from the number of negative weights under a generic one-parameter subgroup.

Step 5. Since the nested Hilbert scheme is smooth and all fixed points are isolated with even Morse indices, Morse theory gives exact Betti numbers and the Poincare polynomial is the sum stated above.

**Key Insight:** The nested Hilbert scheme $(\mathbb{C}^2)^{[n,n+1]}$ inherits its torus action from $\mathbb{C}^2$ and its fixed-point combinatorics reduces to pairs of partitions differing by one box, connecting the topology of these moduli spaces directly to the combinatorics of Young's lattice.

**Prerequisites:** Hilbert schemes of points, nested Hilbert schemes, torus localization, Fogarty's theorem, Nakajima quiver varieties, Young diagrams

<!-- BENCHMARK_PROBLEM: For $n=2$, enumerate all fixed points of $(\mathbb{C}^2)^{[2,3]}$ by listing all partitions $\mu$ of $3$ together with their removable boxes, and count the total number of fixed points. Verify this equals $\sum_{\mu\vdash 3} r(\mu)$ where $r(\mu)$ is the number of removable corners of $\mu$. -->

### Remark: Adjoint orbit, symplectic form, moment maps {#ecag-0249}

Coadjoint orbits of a compact Lie group $G$ carry natural symplectic structures (the Kirillov--Kostant--Souriau symplectic form) and serve as fundamental examples in symplectic geometry and geometric quantization.

Let $G$ be a compact Lie group with Lie algebra $\mathfrak{g}$, and let $\mathfrak{g}^*$ denote its dual. For $\xi\in\mathfrak{g}^*$, the coadjoint orbit $\mathcal{O}_\xi = G\cdot\xi\subset\mathfrak{g}^*$ carries the KKS symplectic form: for $X,Y\in\mathfrak{g}$ and the corresponding tangent vectors $X^\sharp_\eta, Y^\sharp_\eta$ at $\eta\in\mathcal{O}_\xi$,

$$
\omega_\eta(X^\sharp_\eta, Y^\sharp_\eta) = \langle\eta, [X,Y]\rangle.

$$

This $2$-form is $G$-invariant and nondegenerate (since the kernel of the map $X\mapsto X^\sharp_\eta$ is exactly the stabilizer $\mathfrak{g}_\eta$). The inclusion $\mu:\mathcal{O}_\xi\hookrightarrow\mathfrak{g}^*$ is itself a moment map for the $G$-action on $(\mathcal{O}_\xi, \omega)$.

For $G = U(n)$, the coadjoint orbits through diagonal matrices $\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ are flag manifolds. The maximal torus $T\subset U(n)$ of diagonal matrices acts in a Hamiltonian fashion, and the moment map $\mu_T:\mathcal{O}_\xi\to\mathfrak{t}^*$ is the projection of the inclusion onto $\mathfrak{t}^*$. The image $\mu_T(\mathcal{O}_\xi)$ is the convex hull of the Weyl group orbit $W\cdot\xi$ (Atiyah--Guillemin--Sternberg convexity theorem). The components of $\mu_T$ provide a family of Morse--Bott functions on $\mathcal{O}_\xi$, with critical submanifolds given by subtori fixed-point sets.

In the context of this section, the Grassmannian $\operatorname{Gr}(k,n)$ is the coadjoint orbit of $U(n)$ through $\operatorname{diag}(\underbrace{1,\dots,1}_k,\underbrace{0,\dots,0}_{n-k})$. The moment map for the maximal torus action is $\mu_T([W]) = \operatorname{diag}(\|e_1^W\|^2,\dots,\|e_n^W\|^2)$ where $e_i^W$ denotes the orthogonal projection of the $i$-th standard basis vector onto $W$. A generic linear functional $f=\sum a_i x_i$ on $\mathfrak{t}^*$ composed with $\mu_T$ gives a Morse function on $\operatorname{Gr}(k,n)$, recovering the Morse-theoretic computation of the Poincare polynomial from the example above.

<!-- BENCHMARK_PROBLEM: For $G=U(3)$ and the coadjoint orbit through $\operatorname{diag}(2,1,0)$, identify the resulting flag manifold, compute its dimension as a real manifold, determine the number of $T$-fixed points (where $T$ is the maximal torus of diagonal matrices), and verify that the convex hull of their images under the moment map is a hexagon in $\mathfrak{t}^*\cong\mathbb{R}^3$. -->
