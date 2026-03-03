---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/weight.tex
---

## Weights, nearby and vanishing cycles

### Example: $X=\mathbb{C}^{\times}\hookrightarrow\mathbb{P}_{\mathbb{C}}^{1}=\overline{X}$, weight filtration {#ecag-0278}

Let $X = \mathbb{C}^{\times}$ embedded in $\overline{X} = \mathbb{P}^{1}_{\mathbb{C}}$ as the complement of two points. The boundary divisor is $D = \overline{X} \setminus X = \{0, \infty\}$, a union of two points. Since $D$ is already a normal crossing divisor (vacuously, since $\dim \overline{X} = 1$), we may apply the weight spectral sequence directly with $D^{(0)} = \overline{X} = \mathbb{P}^{1}$ and $D^{(1)} = \{0, \infty\}$.

The $E_1$-page of the weight spectral sequence, with formula $E_1^{-p,q} = H^{q-2p}(D^{(p)}; \mathbb{Q})$, is:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $H^0(D^{(1)}) = \mathbb{Q}^2$ | $H^2(\mathbb{P}^1) = \mathbb{Q}$ |
| $1$ | $0$ | $H^1(\mathbb{P}^1) = 0$ |
| $0$ | $0$ | $H^0(\mathbb{P}^1) = \mathbb{Q}$ |

The sole nontrivial differential is $d_1 : E_1^{-1,2} \to E_1^{0,2}$, the Gysin map $H^0(D^{(1)}) \to H^2(\overline{X})$. Each point class maps to the fundamental class of $\mathbb{P}^1$, so this is the map $\mathbb{Q}^2 \to \mathbb{Q}$ sending $(a,b) \mapsto a + b$, which is surjective with kernel $\mathbb{Q} \cdot (1, -1)$.

Surjectivity also follows from convergence: the spectral sequence converges to $H^{p+q}(X; \mathbb{Q})$, and $X = \mathbb{C}^{\times} \simeq S^1$ has $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}$, $H^k(X) = 0$ for $k \geq 2$. Vanishing of $H^2(X)$ forces $d_1$ to kill all of $E_1^{0,2}$.

The $E_2$-page is therefore:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $\mathbb{Q}$ | $0$ |
| $1$ | $0$ | $0$ |
| $0$ | $0$ | $\mathbb{Q}$ |

The spectral sequence degenerates at $E_2$, and the position $(-1, 2)$ contributes to $H^{-1+2}(X) = H^1(X)$. The weight filtration on $H^1(X; \mathbb{Q})$ reads

$$
0 = W_0 H^1(X; \mathbb{Q}) = W_1 H^1(X; \mathbb{Q}) \subset W_2 H^1(X; \mathbb{Q}) = H^1(X; \mathbb{Q}) = \mathbb{Q},

$$

so $\operatorname{Gr}_2^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}$. The generator of $H^1(\mathbb{C}^{\times})$ has pure weight 2, not weight 1, because it arises from the boundary $D$ via the Gysin map rather than from the compact part $\overline{X}$. This is characteristic of non-compact smooth varieties: the missing compactness shifts the weight upward.

<!-- BENCHMARK_PROBLEM: Let X = C^* embedded in P^1_C as the complement of {0, infty}. Compute the weight filtration on H^1(X; Q). What is Gr_2^W H^1(X; Q)? -->

### Remark: Weight filtration, [reference, Joana Cirici](http://userpage.fu-berlin.de/jcirici/computeweight.pdf) {#ecag-0279}

Let $X$ be a smooth complex variety of dimension $n$. Choose a smooth compactification $j : X \hookrightarrow \overline{X}$ such that $D = \overline{X} \setminus X$ is a normal crossing divisor with irreducible components $D = \bigcup_{i=1}^{N} D_i$. Define $D^{(0)} = \overline{X}$ and, for $p \geq 1$,

$$
D^{(p)} = \coprod_{\{i_1, \dots, i_p\} \subset \{1, 2, \dots, N\}} D_{i_1} \cap \cdots \cap D_{i_p}.

$$

Since $D$ is normal crossing, each connected component of $D^{(p)}$ is a smooth projective variety of dimension $n - p$.

The weight spectral sequence takes the form

$$
E_1^{-p,q} = H^{q-2p}(D^{(p)}; \mathbb{Q}) \Rightarrow H^{q-p}(X; \mathbb{Q}),

$$

with $E_1$-differential $d_1 : E_1^{-p,q} \to E_1^{-p+1,q}$ given by the alternating sum of Gysin maps

$$
i_* : H^{q-2p}(D_{i_1} \cap \cdots \cap D_{i_p}) \to H^{q-2p+2}(D_{i_1} \cap \cdots \cap \widehat{D_{i_k}} \cap \cdots \cap D_{i_p}),

$$

where $\widehat{D_{i_k}}$ denotes omission of the $k$-th component.

The spectral sequence degenerates at $E_2$ (a theorem of Deligne), yielding the weight filtration

$$
0 = W_{n-1} H^n(X; \mathbb{Q}) \subset W_n H^n(X; \mathbb{Q}) \subset \cdots \subset W_{2n} H^n(X; \mathbb{Q}) = H^n(X; \mathbb{Q}),

$$

with graded pieces $\operatorname{Gr}_q^W H^{q-p}(X; \mathbb{Q}) = E_2^{-p,q}$.

For concreteness, the $E_1$-page for a surface ($n = 2$) is:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $5$ | $H^1(D^{(2)})$ | $H^3(D^{(1)})$ | $H^5(\overline{X})$ |
| $4$ | $H^0(D^{(2)})$ | $H^2(D^{(1)})$ | $H^4(\overline{X})$ |
| $3$ | $0$ | $H^1(D^{(1)})$ | $H^3(\overline{X})$ |
| $2$ | $0$ | $H^0(D^{(1)})$ | $H^2(\overline{X})$ |
| $1$ | $0$ | $0$ | $H^1(\overline{X})$ |
| $0$ | $0$ | $0$ | $H^0(\overline{X})$ |

The $E_2$-page reads off the graded pieces of the weight filtration: the entry at position $(-p, q)$ gives $\operatorname{Gr}_q^W H^{q-p}(X; \mathbb{Q})$:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $5$ | $\operatorname{Gr}_5^W H^3$ | $\operatorname{Gr}_5^W H^4$ | $\operatorname{Gr}_5^W H^5$ |
| $4$ | $\operatorname{Gr}_4^W H^2$ | $\operatorname{Gr}_4^W H^3$ | $\operatorname{Gr}_4^W H^4$ |
| $3$ | $0$ | $\operatorname{Gr}_3^W H^2$ | $\operatorname{Gr}_3^W H^3$ |
| $2$ | $0$ | $\operatorname{Gr}_2^W H^1$ | $\operatorname{Gr}_2^W H^2$ |
| $1$ | $0$ | $0$ | $\operatorname{Gr}_1^W H^1$ |
| $0$ | $0$ | $0$ | $\operatorname{Gr}_0^W H^0$ |

Each anti-diagonal (entries with $q - p = n$ constant) assembles into the weight filtration of $H^n(X; \mathbb{Q})$. The key constraint is that for a smooth variety of dimension $n$, the weights on $H^m(X; \mathbb{Q})$ range from $\max(0, m)$ to $\min(2m, 2n)$, with the lower bound $m$ realized by the compact part $H^m(\overline{X})$ and the upper bound achieved by the deepest boundary stratum contributions.

<!-- BENCHMARK_PROBLEM: For a smooth complex variety X of dimension n with smooth compactification j: X -> X_bar where D = X_bar \ X is a normal crossing divisor, what is the range of the weight filtration on H^n(X; Q)? That is, what are the smallest and largest indices k such that W_k H^n(X; Q) can be nontrivial? -->

### Remark: Gysin map {#ecag-0280}

Let $i : Z \hookrightarrow X$ be a closed embedding of smooth complex varieties with $Z$ of codimension $c$ in $X$. The Gysin map (or pushforward in cohomology) is

$$
i_* : H^k(Z; \mathbb{Q}) \to H^{k+2c}(X; \mathbb{Q}),

$$

defined as the composition

$$
H^k(Z; \mathbb{Q}) \xrightarrow{\;\sim\;} H^{k+2c}_Z(X; \mathbb{Q}) \to H^{k+2c}(X; \mathbb{Q}),

$$

where the first map is the Thom isomorphism (using the orientation of the normal bundle $\mathcal{N}_{Z/X}$) and the second is the forgetful map from cohomology with supports to ordinary cohomology.

The essential properties are:

1. **Degree shift.** The map $i_*$ shifts cohomological degree by $2c$, where $c = \operatorname{codim}(Z, X)$.
2. **Projection formula.** For $\alpha \in H^*(X)$ and $\beta \in H^*(Z)$, we have $i_*(i^*(\alpha) \cup \beta) = \alpha \cup i_*(\beta)$.
3. **Functoriality.** For composable closed embeddings $Z \xrightarrow{j} Y \xrightarrow{i} X$ of smooth varieties, $(i \circ j)_* = i_* \circ j_*$.
4. **Self-intersection.** $i^* \circ i_*(1_Z) = c_c(\mathcal{N}_{Z/X})$, the top Chern class of the normal bundle.

In the weight spectral sequence, the $d_1$ differentials $E_1^{-p,q} \to E_1^{-p+1,q}$ are alternating sums of Gysin maps $i_* : H^{q-2p}(D^{(p)}) \to H^{q-2p+2}(D^{(p-1)})$, connecting the cohomology of deeper boundary strata to shallower ones. The degree shift of $2$ per step in depth accounts for the codimension-1 nature of each boundary component.

<!-- BENCHMARK_PROBLEM: Let i: Z -> X be a closed embedding of smooth complex varieties where Z has codimension c in X. By how many degrees does the Gysin map i_* shift cohomological degree? -->

### Example: punctured Riemann surface {#ecag-0281}

Let $\overline{X}$ be a compact Riemann surface of genus $g$, and let $D$ consist of $p$ distinct points. Set $X = \overline{X} \setminus D$. We compute the weight filtration on $H^*(X; \mathbb{Q})$.

The boundary strata are $D^{(0)} = \overline{X}$ (a smooth projective curve of genus $g$) and $D^{(1)} = D$ (a disjoint union of $p$ points). The $E_1$-page is:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $H^0(D^{(1)}) = \mathbb{Q}^p$ | $H^2(\overline{X}) = \mathbb{Q}$ |
| $1$ | $0$ | $H^1(\overline{X}) = \mathbb{Q}^{2g}$ |
| $0$ | $0$ | $H^0(\overline{X}) = \mathbb{Q}$ |

The only nontrivial differential is $d_1 : E_1^{-1,2} = \mathbb{Q}^p \to E_1^{0,2} = \mathbb{Q}$, the Gysin map sending each point class to the fundamental class of $\overline{X}$. This is the map $(a_1, \ldots, a_p) \mapsto a_1 + \cdots + a_p$, which is surjective with $(p-1)$-dimensional kernel.

Surjectivity also follows from convergence. Topologically, $X$ is a genus-$g$ surface with $p$ punctures, hence homotopy equivalent to a wedge of $2g + p - 1$ circles, so $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}^{2g+p-1}$, and $H^k(X) = 0$ for $k \geq 2$. The vanishing of $H^2(X)$ forces $d_1$ to be surjective.

The $E_2$-page is:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $\mathbb{Q}^{p-1}$ | $0$ |
| $1$ | $0$ | $\mathbb{Q}^{2g}$ |
| $0$ | $0$ | $\mathbb{Q}$ |

Reading off the weight filtration on $H^1(X; \mathbb{Q})$ from the anti-diagonal $q - p = 1$:

$$
0 = W_0 H^1(X; \mathbb{Q}) \subset W_1 H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{2g} \subset W_2 H^1(X; \mathbb{Q}) = H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{2g + p - 1},

$$

with graded pieces

$$
\operatorname{Gr}_1^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{2g}, \quad \operatorname{Gr}_2^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{p-1}.

$$

The weight-1 part $W_1 H^1(X) \cong \mathbb{Q}^{2g}$ is the image of $H^1(\overline{X})$, carrying a pure Hodge structure of weight 1 from the compact surface. The weight-2 part $\operatorname{Gr}_2^W H^1(X) \cong \mathbb{Q}^{p-1}$ arises from the boundary and has dimension $p-1$ (not $p$) because the sum of all puncture classes vanishes in $H^2(\overline{X})/\operatorname{im}(d_1)$.

**Verification.** For $g = 0$, $p = 2$: this recovers the case $X = \mathbb{C}^{\times}$ from the previous example, with $\operatorname{Gr}_1^W = 0$ and $\operatorname{Gr}_2^W = \mathbb{Q}$.

<!-- BENCHMARK_PROBLEM: Let X be a Riemann surface of genus 3 with 5 punctures. What is the dimension of Gr_1^W H^1(X; Q) and of Gr_2^W H^1(X; Q)? -->

### Example: complement of three intersecting lines in $\mathbb{P}^{2}$ {#ecag-0282}

Let $\overline{X} = \mathbb{P}^2$ and let $D$ be the union of three lines $L_1, L_2, L_3$ in general position (pairwise intersections are three distinct points). Set $X = \mathbb{P}^2 \setminus D$. The three lines form a normal crossing divisor, so we apply the weight spectral sequence directly.

The boundary strata are $D^{(0)} = \mathbb{P}^2$, $D^{(1)} = L_1 \sqcup L_2 \sqcup L_3 \cong (\mathbb{P}^1)^{\sqcup 3}$, and $D^{(2)} = \{P_1, P_2, P_3\}$ (the three pairwise intersection points). The $E_1$-page is:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $H^0(D^{(2)}) = \mathbb{Q}^3$ | $H^2(D^{(1)}) = \mathbb{Q}^3$ | $H^4(\mathbb{P}^2) = \mathbb{Q}$ |
| $3$ | $0$ | $H^1(D^{(1)}) = 0$ | $H^3(\mathbb{P}^2) = 0$ |
| $2$ | $0$ | $H^0(D^{(1)}) = \mathbb{Q}^3$ | $H^2(\mathbb{P}^2) = \mathbb{Q}$ |
| $1$ | $0$ | $0$ | $H^1(\mathbb{P}^2) = 0$ |
| $0$ | $0$ | $0$ | $H^0(\mathbb{P}^2) = \mathbb{Q}$ |

To determine the $E_2$-page, we identify the topology of $X$. Removing one line from $\mathbb{P}^2$ yields $\mathbb{C}^2$; the remaining two lines become two lines in $\mathbb{C}^2$ intersecting in one point. After a linear change of coordinates, these are the coordinate axes, so

$$
X \simeq \mathbb{C}^2 \setminus \{\text{two lines through origin}\} \cong (\mathbb{C} \setminus \{0\}) \times (\mathbb{C} \setminus \{0\}) \simeq S^1 \times S^1 = T^2.

$$

Hence $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}^2$, $H^2(X) = \mathbb{Q}$, and $H^k(X) = 0$ for $k \geq 3$.

**The differentials at row $q = 2$.** The map $d_1 : E_1^{-1,2} = \mathbb{Q}^3 \to E_1^{0,2} = \mathbb{Q}$ sends each line class $[L_i]$ to the hyperplane class in $H^2(\mathbb{P}^2)$. This is the map $(a_1, a_2, a_3) \mapsto a_1 + a_2 + a_3$, surjective with 2-dimensional kernel.

**The differentials at row $q = 4$.** The map $d_1 : E_1^{-2,4} = \mathbb{Q}^3 \to E_1^{-1,4} = \mathbb{Q}^3$ sends the class of each intersection point $P_k = L_i \cap L_j$ to the fundamental classes of the two lines it lies on, with appropriate signs. The subsequent map $d_1 : E_1^{-1,4} = \mathbb{Q}^3 \to E_1^{0,4} = \mathbb{Q}$ sends each $[L_i] \in H^2(L_i)$ to $[\mathbb{P}^2] \in H^4(\mathbb{P}^2)$. Convergence to $H^*(X)$ forces the $E_2$-page to be:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $\mathbb{Q}$ | $0$ | $0$ |
| $3$ | $0$ | $0$ | $0$ |
| $2$ | $0$ | $\mathbb{Q}^2$ | $0$ |
| $1$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $0$ | $\mathbb{Q}$ |

The weight filtration is therefore:

- $H^0(X) = \mathbb{Q}$, pure of weight 0.
- $H^1(X) = \mathbb{Q}^2$, pure of weight 2: $\operatorname{Gr}_2^W H^1(X) = \mathbb{Q}^2$.
- $H^2(X) = \mathbb{Q}$, pure of weight 4: $\operatorname{Gr}_4^W H^2(X) = \mathbb{Q}$.

Although $X \simeq T^2$ as a topological space, the weight filtration reveals that all cohomology classes originate from the boundary strata. In particular, $H^1(X)$ is pure of weight 2 rather than weight 1. This distinguishes the algebraic structure of the complement from a genuine compact torus, whose $H^1$ would be pure of weight 1.

<!-- BENCHMARK_PROBLEM: Let X = P^2 \ D where D is the union of three lines in general position in P^2_C. What is the weight of H^1(X; Q)? That is, for which k is Gr_k^W H^1(X; Q) nonzero? -->

### Example: complement of three concurrent lines in $\mathbb{P}^{2}$ {#ecag-0283}

Let $D$ be the union of three concurrent lines in $\mathbb{P}^2$, all passing through a single point $p$. Set $X = \mathbb{P}^2 \setminus D$. Since three concurrent lines fail to form a normal crossing divisor (they share a triple point), we must resolve the singularity before applying the weight spectral sequence.

**Resolution.** Blow up $\mathbb{P}^2$ at $p$ to obtain $\overline{X} = \operatorname{Bl}_p(\mathbb{P}^2)$ with exceptional divisor $E \cong \mathbb{P}^1$. The strict transforms $\widetilde{L}_1, \widetilde{L}_2, \widetilde{L}_3$ of the three lines are disjoint from each other (they only met at $p$, which has been separated by the blow-up), and each meets $E$ transversally in one point. The divisor $D' = \widetilde{L}_1 \cup \widetilde{L}_2 \cup \widetilde{L}_3 \cup E$ is normal crossing in $\overline{X}$, and $\overline{X} \setminus D' \cong X$.

The boundary strata are $D'^{(0)} = \overline{X}$ with $H^*(\overline{X}) = H^*(\mathbb{P}^2) \oplus \mathbb{Q}[-2]$ (the blow-up adds a class in degree 2 from $E$, so $H^2(\overline{X}) = \mathbb{Q}^2$), $D'^{(1)} = \widetilde{L}_1 \sqcup \widetilde{L}_2 \sqcup \widetilde{L}_3 \sqcup E$ (four copies of $\mathbb{P}^1$), and $D'^{(2)} = \{Q_1, Q_2, Q_3\}$ (three points, one on each $\widetilde{L}_i \cap E$). The $E_1$-page is:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $\mathbb{Q}^3$ | $\mathbb{Q}^4$ | $\mathbb{Q}$ |
| $3$ | $0$ | $0$ | $0$ |
| $2$ | $0$ | $\mathbb{Q}^4$ | $\mathbb{Q}^2$ |
| $1$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $0$ | $\mathbb{Q}$ |

**Topology of $X$.** Removing one line from $\mathbb{P}^2$ gives $\mathbb{C}^2$. The remaining two lines pass through the origin in $\mathbb{C}^2$ and are distinct. Removing them yields $\mathbb{C}^2 \setminus \{\text{two lines through } 0\}$, which retracts onto $S^3 \setminus \{\text{two circles}\}$ (each complex line through the origin meets $S^3 \subset \mathbb{C}^2$ in a great circle). The complement of two disjoint circles in $S^3$ is homotopy equivalent to $S^1 \vee S^1$. Therefore $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}^2$, $H^k(X) = 0$ for $k \geq 2$.

Using convergence, the $E_2$-page must be:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $0$ | $0$ | $0$ |
| $3$ | $0$ | $0$ | $0$ |
| $2$ | $0$ | $\mathbb{Q}^2$ | $0$ |
| $1$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $0$ | $\mathbb{Q}$ |

The weight filtration gives $H^1(X; \mathbb{Q}) \cong \mathbb{Q}^2$ pure of weight 2:

$$
\operatorname{Gr}_2^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}^2.

$$

The extra generator in $H^2(\overline{X})$ from the exceptional divisor $E$ (compared to $H^2(\mathbb{P}^2) = \mathbb{Q}$) changes the rank of the $d_1$ differentials. Concretely, $d_1 : \mathbb{Q}^4 \to \mathbb{Q}^2$ at row $q = 2$ has kernel of dimension 2 (contributing to $\operatorname{Gr}_2^W H^1$), and the maps at row $q = 4$ are exact (killing all of $H^2(X)$).

Comparing with the general-position case (ecag-0282): both complements have $H^1$ pure of weight 2 and of dimension 2, but the topologies differ -- $T^2$ for general position versus $S^1 \vee S^1$ for concurrent lines. The difference is visible in $H^2$: the general-position complement has $H^2 = \mathbb{Q}$ (from the cup product on the torus), while the concurrent complement has $H^2 = 0$ (the wedge has no top-dimensional cohomology).

<!-- BENCHMARK_PROBLEM: Let X = P^2_C minus three concurrent lines. What is the homotopy type of X, and what is the dimension of H^1(X; Q)? -->

### Remark: $X=\mathbb{C}^{2}\setminus\{0\}\subset \mathbb{P}^{2}$ {#ecag-0284}

Consider $X = \mathbb{C}^2 \setminus \{0\}$. The standard embedding $\mathbb{C}^2 \subset \mathbb{P}^2$ has boundary $\mathbb{P}^2 \setminus \mathbb{C}^2 = \mathbb{P}^1_\infty$ (the line at infinity), but $X$ also excludes the origin, which lies in the interior. The complement $\mathbb{P}^2 \setminus X$ consists of $\mathbb{P}^1_\infty$ together with the point $0 \in \mathbb{C}^2$, and this is not a normal crossing divisor.

To resolve, blow up $\mathbb{P}^2$ at the origin. Let $\overline{X} = \operatorname{Bl}_0(\mathbb{P}^2)$ with exceptional divisor $E \cong \mathbb{P}^1$ and strict transform $L_\infty$ of the line at infinity. Since $0 \notin \mathbb{P}^1_\infty$, the divisors $E$ and $L_\infty$ are disjoint, so $D = E \cup L_\infty$ is a normal crossing divisor in $\overline{X}$ with $\overline{X} \setminus D \cong X$.

The boundary strata are $D^{(1)} = E \sqcup L_\infty$ (two disjoint copies of $\mathbb{P}^1$) and $D^{(2)} = \emptyset$ (since $E \cap L_\infty = \emptyset$). Topologically, $X = \mathbb{C}^2 \setminus \{0\} \simeq S^3$, so $H^0(X) = \mathbb{Q}$, $H^3(X) = \mathbb{Q}$, and all other cohomology vanishes.

The $E_1$-page (for a surface, $n=2$) has entries only in columns $p = -1$ and $p = 0$. Row $q=2$ gives $d_1 : H^0(D^{(1)}) = \mathbb{Q}^2 \to H^2(\overline{X}) = \mathbb{Q}^2$, and the other differentials are determined by the known cohomology of $X$. After degenerating at $E_2$, the weight filtration gives:

- $H^0(X) = \mathbb{Q}$, pure of weight 0.
- $H^3(X) = \mathbb{Q}$, pure of weight 4: $\operatorname{Gr}_4^W H^3(X) = \mathbb{Q}$.

The appearance of weight 4 on $H^3$ (rather than weight 3, which would occur for a smooth compact 3-fold) reflects the codimension-2 nature of the removed point: deleting a codimension-$c$ subvariety creates cohomology shifted by $2c$ in weight. Here $c = 2$ (a point in a surface), and the weight shift $2c = 4$ accounts for the gap between the cohomological degree 3 and the weight 4.

<!-- BENCHMARK_PROBLEM: What is the homotopy type of C^2 \ {0}? Using this, determine H^k(C^2 \ {0}; Q) for all k. -->

### Example: cubical hyperresolution, It's our guess, we didn't check the precise definition carefully!!!!!! {#ecag-0285}

A cubical hyperresolution of a singular variety $X$ is a proper augmented cubical diagram of smooth varieties that resolves $X$ in a cohomological sense, enabling the construction of mixed Hodge structures even when $X$ is singular.

For a variety $X$ with singular locus $Y \subset X$, the simplest case is a 1-cubical hyperresolution (a square diagram). Let $f : \widetilde{X} \to X$ be a resolution of singularities, and let $\widetilde{Y} = f^{-1}(Y)$ be the preimage of the singular locus. The resolution square is:

$$
\begin{array}{ccc}
\widetilde{Y} & \longrightarrow & \widetilde{X} \\
\downarrow & & \downarrow \, f \\
Y & \longrightarrow & X
\end{array}

$$

All four corners are varieties, but the upper row consists of smooth varieties: $\widetilde{X}$ is smooth by construction of the resolution, and $\widetilde{Y}$ can be arranged to be smooth (after further blow-ups if necessary). The horizontal maps are closed embeddings, and the vertical maps are proper and surjective.

For a concrete instance, consider a nodal curve $X$ with a single node at $Y = \{p\}$. Taking the normalization $\widetilde{X} = X^{\nu}$ (a smooth curve), the preimage is $\widetilde{Y} = f^{-1}(p) = \{q_1, q_2\}$ (the two branches above the node). The square becomes:

$$
\begin{array}{ccc}
\{q_1, q_2\} & \longrightarrow & X^{\nu} \\
\downarrow & & \downarrow \\
\{p\} & \longrightarrow & X
\end{array}

$$

The cohomology of $X$ is then recovered from the Mayer--Vietoris-type exact sequence associated to this square:

$$
\cdots \to H^k(X) \to H^k(\widetilde{X}) \oplus H^k(Y) \to H^k(\widetilde{Y}) \to H^{k+1}(X) \to \cdots

$$

For deeper singularities (e.g., a variety whose singular locus is itself singular), one iterates: resolve $Y$, form the fiber product, resolve its singular locus, and so on. This produces a cubical diagram indexed by subsets of $\{0, 1, \ldots, d\}$ where $d$ is the depth of the stratification. The general construction, due to Guillen--Navarro Aznar--Pascual-Gainza--Puerta, ensures that at each vertex the variety is smooth, and the resulting weight spectral sequence is independent of the choices made.

<!-- BENCHMARK_PROBLEM: In a 1-cubical hyperresolution of a singular variety X with singular locus Y, what are the four terms of the square diagram? Describe them in terms of X, Y, and a resolution of singularities. -->

### Example: Nodal curve {#ecag-0286}

Consider the nodal cubic $X = \{(x:y:z) \in \mathbb{P}^2 \mid y^2 z = x^2(x+z)\}$, which has a single node at $P = (0:0:1)$. We compute the mixed Hodge structure on $H^*(X; \mathbb{Q})$ using the normalization as a cubical hyperresolution.

The normalization $f : \widetilde{X} \to X$ satisfies $\widetilde{X} \cong \mathbb{P}^1$ (since $X$ is a rational curve with one node). The preimage of the node consists of two points: $\widetilde{Y} = f^{-1}(P) = \{Q_1, Q_2\}$. Setting $Y = \{P\}$, the resolution square is:

$$
\begin{array}{ccc}
\{Q_1, Q_2\} & \longrightarrow & \mathbb{P}^1 \\
\downarrow & & \downarrow \, f \\
\{P\} & \longrightarrow & X
\end{array}

$$

The associated Mayer--Vietoris exact sequence is

$$
0 \to H^0(X) \to H^0(\widetilde{X}) \oplus H^0(Y) \to H^0(\widetilde{Y}) \to H^1(X) \to H^1(\widetilde{X}) \oplus H^1(Y) \to \cdots

$$

Substituting the known cohomology groups:

| Space | $H^0$ | $H^1$ | $H^2$ |
|---|---|---|---|
| $\widetilde{X} = \mathbb{P}^1$ | $\mathbb{Q}$ | $0$ | $\mathbb{Q}$ |
| $Y = \{P\}$ | $\mathbb{Q}$ | $0$ | $0$ |
| $\widetilde{Y} = \{Q_1, Q_2\}$ | $\mathbb{Q}^2$ | $0$ | $0$ |

The exact sequence becomes

$$
0 \to H^0(X) \to \mathbb{Q}^2 \xrightarrow{\;\delta\;} \mathbb{Q}^2 \to H^1(X) \to 0 \to 0 \to H^2(X) \to \mathbb{Q} \to 0.

$$

The map $\delta : H^0(\widetilde{X}) \oplus H^0(Y) \to H^0(\widetilde{Y})$ sends $(a, b) \mapsto (a - b, \, a - b)$, since both points $Q_1, Q_2$ lie over $P$ and both map to the same connected component of $\widetilde{X}$. This map has kernel $\{a = b\} \cong \mathbb{Q}$ and cokernel $\mathbb{Q}$.

Therefore: $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}$, $H^2(X) = \mathbb{Q}$.

The generator of $H^1(X) \cong \mathbb{Q}$ comes from the cokernel of $\delta$, which involves only $H^0$ groups -- all of which carry pure Hodge structures of weight 0. Hence $H^1(X)$ carries weight 0:

$$
\operatorname{Gr}_0^W H^1(X; \mathbb{Q}) = \mathbb{Q}.

$$

This is markedly different from a smooth projective curve of genus 1, where $H^1$ is pure of weight 1. The node "pinches" a handle, creating a loop that arises from the failure of the normalization map to be injective (it identifies $Q_1$ with $Q_2$), and this purely topological origin places the resulting class at weight 0 rather than weight 1.

**Verification.** The nodal cubic has geometric genus $p_g = 0$ (it is rational) and arithmetic genus $p_a = 1$ (by the degree-genus formula). The discrepancy $p_a - p_g = 1$ accounts for the extra $H^1$ class. If we smooth the node (deforming to an elliptic curve), the weight-0 class in $H^1$ would be "promoted" to weight 1, recovering the pure Hodge structure of a smooth genus-1 curve.

<!-- BENCHMARK_PROBLEM: Consider the nodal cubic X = {y^2 z = x^2(x+z)} in P^2. What is H^1(X; Q), and what is its weight in the mixed Hodge structure? Compare with the case of a smooth elliptic curve. -->

### Remark: weight spectral sequence for singular varieties {#ecag-0287}

For singular varieties, the weight spectral sequence is constructed via cubical hyperresolutions rather than smooth compactifications with normal crossing boundary. Given a singular variety $X$, one chooses a cubical hyperresolution $a_\bullet : X_\bullet \to X$, where each $X_I$ (indexed by subsets $I$ of a finite set) is a smooth variety. The weight spectral sequence takes the form

$$
E_1^{p,q} = \bigoplus_{|I|=p} H^q(X_I; \mathbb{Q}) \Rightarrow H^{p+q}(X; \mathbb{Q}).

$$

The fundamental results, due to Deligne in the smooth case and extended by Guillen--Navarro Aznar--Pascual-Gainza--Puerta to the singular case via cubical methods, are:

1. The resulting mixed Hodge structure on $H^n(X; \mathbb{Q})$ is independent of the choice of cubical hyperresolution.
2. The weight filtration on $H^n(X; \mathbb{Q})$ satisfies $W_{-1} H^n = 0$ and $W_{2n} H^n = H^n$.

The weight ranges depend on the geometric nature of $X$:

| Type of $X$ | Weights on $H^n(X)$ |
|---|---|
| Smooth projective | pure weight $n$ |
| Smooth, not necessarily proper | $n \leq k \leq 2n$ |
| Projective, not necessarily smooth | $0 \leq k \leq n$ |
| General (singular, non-proper) | $0 \leq k \leq 2n$ |

The smooth non-compact and singular projective cases are dual: removing a boundary divisor pushes weights up (toward $2n$), while introducing singularities pushes weights down (toward $0$). For a general variety that is both singular and non-compact, the full range $0$ to $2n$ is possible.

<!-- BENCHMARK_PROBLEM: For a singular projective variety X, what is the range of weights that can appear in the mixed Hodge structure on H^n(X; Q)? How does this differ from a smooth projective variety? -->

### Remark: Mayer-Vietoris exact sequence {#ecag-0288}

In the context of cubical hyperresolutions and mixed Hodge theory, the Mayer--Vietoris exact sequence serves as the primary computational tool. For the simplest cubical hyperresolution (the normalization square of a singular variety), the associated long exact sequence is

$$
\cdots \to H^k(X) \to H^k(\widetilde{X}) \oplus H^k(Y) \to H^k(\widetilde{Y}) \to H^{k+1}(X) \to \cdots

$$

where $\widetilde{X} \to X$ is the resolution, $Y$ is the singular locus, and $\widetilde{Y} = \widetilde{X} \times_X Y$.

More generally, for a variety $X = U \cup V$ covered by two open subvarieties, the classical Mayer--Vietoris sequence

$$
\cdots \to H^k(X) \to H^k(U) \oplus H^k(V) \to H^k(U \cap V) \to H^{k+1}(X) \to \cdots

$$

is a morphism of mixed Hodge structures. The crucial consequence is **strictness**: every map in the sequence is strict with respect to the weight filtration, meaning $f(W_k) = f(\text{source}) \cap W_k(\text{target})$ for each $k$. Strictness implies that the long exact sequence splits into short exact sequences on each graded piece:

$$
\cdots \to \operatorname{Gr}_m^W H^k(X) \to \operatorname{Gr}_m^W H^k(U) \oplus \operatorname{Gr}_m^W H^k(V) \to \operatorname{Gr}_m^W H^k(U \cap V) \to \operatorname{Gr}_m^W H^{k+1}(X) \to \cdots

$$

This is an exact sequence of pure Hodge structures (each $\operatorname{Gr}_m^W$ carries a pure Hodge structure of weight $m$), reducing mixed Hodge theory computations to manipulations of pure Hodge structures at each weight level. Without strictness, one could not separately track the weight-$m$ contributions through the exact sequence, and the bookkeeping would become intractable.

<!-- BENCHMARK_PROBLEM: In the Mayer-Vietoris sequence for mixed Hodge structures, what special property do the maps have with respect to the weight filtration, and why is this property useful for computations? -->

### Remark: cubical hyperresolution {#ecag-0289}

A cubical hyperresolution of a variety $X$ is a proper augmented cubical variety $a_\bullet : X_\bullet \to X$, indexed by the partially ordered set of subsets of $\{0, 1, \ldots, n\}$, satisfying:

1. Each $X_I$ is a smooth variety.
2. The augmentation $X_\emptyset \to X$ is a proper surjective map (typically a resolution of singularities).
3. For each $I$ and $i \in I$, the induced map $X_I \to X_{I \setminus \{i\}}$ is proper.
4. The diagram computes the correct cohomology of $X$: the augmented complex is acyclic (i.e., the natural map from $H^*(X)$ to the cohomological descent spectral sequence of the diagram is an isomorphism).

The existence of cubical hyperresolutions in characteristic zero follows from Hironaka's resolution of singularities. The construction is inductive: starting from a resolution $\widetilde{X} \to X$ with exceptional locus mapping to the singular locus $Y$, one resolves $Y$ and the fiber product $\widetilde{Y} = \widetilde{X} \times_X Y$ to produce the 1-cube. If $\widetilde{Y}$ is still singular, one repeats to obtain a 2-cube, and so on. For a variety with a stratification of depth $d$, a $d$-cubical hyperresolution suffices.

The advantage of cubical hyperresolutions over simplicial ones is economy: a $d$-cubical hyperresolution has $2^{d+1} - 1$ terms (indexed by nonempty subsets of $\{0, \ldots, d\}$), compared to the potentially larger number of terms in a simplicial resolution. The cubical structure is also more natural for iterated fiber products.

References: Guillen--Navarro Aznar--Pascual-Gainza--Puerta, *Hyperresolutions cubiques et descente cohomologique* (Springer LNM 1335); see also the expository notes by [Schwede](https://www.math.utah.edu/~schwede/Notes/NotesOnCubicalHyperresolutions.pdf) and [Steenbrink](https://link.springer.com/content/pdf/10.1007/978-3-319-28829-1_15.pdf).

<!-- BENCHMARK_PROBLEM: What is the key property that each term X_I in a cubical hyperresolution must satisfy, and what foundational result guarantees the existence of cubical hyperresolutions in characteristic zero? -->

### Example: cuspidal singularity {#ecag-0290}

Consider the cuspidal cubic $X = \{(x:y:z) \in \mathbb{P}^2 \mid y^2 z = x^3\}$, which has a cusp at $P = (0:0:1)$. Unlike the node, the cusp is a unibranch singularity: the normalization $f : \widetilde{X} \to X$ satisfies $\widetilde{X} \cong \mathbb{P}^1$, and the preimage of the cusp is a single point $\widetilde{Y} = f^{-1}(P) = \{Q\}$. Setting $Y = \{P\}$, the resolution square is:

$$
\begin{array}{ccc}
\{Q\} & \longrightarrow & \mathbb{P}^1 \\
\downarrow & & \downarrow \, f \\
\{P\} & \longrightarrow & X
\end{array}

$$

The Mayer--Vietoris exact sequence gives

$$
0 \to H^0(X) \to H^0(\mathbb{P}^1) \oplus H^0(\{P\}) \to H^0(\{Q\}) \to H^1(X) \to H^1(\mathbb{P}^1) \to \cdots

$$

$$
0 \to H^0(X) \to \mathbb{Q}^2 \xrightarrow{\;\delta\;} \mathbb{Q} \to H^1(X) \to 0 \to 0 \to H^2(X) \to \mathbb{Q} \to 0.

$$

The map $\delta : (a, b) \mapsto a - b$ is surjective (from $\mathbb{Q}^2$ to $\mathbb{Q}$). Therefore: $H^0(X) = \mathbb{Q}$ (kernel of $\delta$ restricted to the image of $H^0(X) \to \mathbb{Q}^2$, which is the diagonal), $H^1(X) = 0$ (cokernel of $\delta$ is zero), and $H^2(X) = \mathbb{Q}$.

The cuspidal cubic thus has the same Betti numbers as $\mathbb{P}^1$: this is no coincidence, since the normalization $f$ is a homeomorphism for a unibranch singularity. The cusp is topologically a continuous bijection that fails to be an isomorphism of varieties only because the local ring at the cusp is not integrally closed. On the level of underlying topological spaces, no new loop is created.

The mixed Hodge structure is: $H^0(X) = \mathbb{Q}$ pure of weight 0, and $H^2(X) = \mathbb{Q}$ pure of weight 2.

**Comparison with the nodal cubic.** The following table summarizes the contrast:

| | Nodal cubic ($y^2z = x^2(x+z)$) | Cuspidal cubic ($y^2z = x^3$) |
|---|---|---|
| Singularity type | node (two branches) | cusp (one branch) |
| Normalization preimage | $\{Q_1, Q_2\}$ | $\{Q\}$ |
| $H^1(X; \mathbb{Q})$ | $\mathbb{Q}$, weight 0 | $0$ |
| Topological effect | pinched handle creates loop | no new topology |

The node creates a weight-0 class in $H^1$ because the normalization identifies two distinct points, forming a topological loop. The cusp, being unibranch, identifies nothing, and $H^1$ vanishes.

<!-- BENCHMARK_PROBLEM: Compare the mixed Hodge structures of the nodal cubic y^2z = x^2(x+z) and the cuspidal cubic y^2z = x^3 in P^2. In particular, what is H^1 for each, and why do they differ? -->

### Example: de Rham-Witt complex {#ecag-0291}

Let $X$ be a smooth variety over a perfect field $k$ of characteristic $p > 0$. The de Rham--Witt complex $W_n \Omega^*_X$, introduced by Bloch and developed systematically by Illusie, is a sheaf of differential graded algebras on $X$ that provides a purely algebraic construction of crystalline cohomology.

For each $n \geq 1$, the complex $W_n \Omega^*_X$ is equipped with four structural maps:

- **Restriction** $R : W_{n+1} \Omega^q_X \to W_n \Omega^q_X$ (surjective, truncates the "top Witt component").
- **Frobenius** $F : W_{n+1} \Omega^q_X \to W_n \Omega^q_X$ (the Frobenius lift).
- **Verschiebung** $V : W_n \Omega^q_X \to W_{n+1} \Omega^q_X$ (the "shift" or transfer map).
- **Differential** $d : W_n \Omega^q_X \to W_n \Omega^{q+1}_X$ (extending the de Rham differential).

These satisfy the fundamental relations $FV = p$ (multiplication by $p$), $FdV = d$, and $Fd[a] = [a]^{p-1} d[a]$ for a Teichmuller representative $[a] \in W_n \mathcal{O}_X$.

In low degrees: $W_n \Omega^0_X = W_n \mathcal{O}_X$ is the sheaf of length-$n$ Witt vectors, and $W_n \Omega^1_X$ is generated over $W_n \mathcal{O}_X$ by symbols $d[a]$ and $V^i(d[b])$ subject to the relations above.

The inverse limit $W\Omega^*_X = \varprojlim_n W_n \Omega^*_X$ computes crystalline cohomology:

$$
H^n_{\operatorname{cris}}(X/W(k)) \cong \mathbb{H}^n(X, W\Omega^*_X),

$$

where $W(k) = \varprojlim_n W_n(k)$ is the ring of $p$-typical Witt vectors of $k$. This is a $p$-adic cohomology theory: for $k = \mathbb{F}_p$, $W(k) = \mathbb{Z}_p$, and crystalline cohomology is a free $\mathbb{Z}_p$-module whose rank equals the corresponding Betti number (for "good" varieties, i.e., those that lift to characteristic 0).

**Examples.**

- $X = \operatorname{Spec}(k)$: $W_n \Omega^0 = W_n(k)$ and all higher forms vanish. For $k = \mathbb{F}_p$, $W(\mathbb{F}_p) = \mathbb{Z}_p$.
- $X = \mathbb{A}^1_k$: $W_n \Omega^0 = W_n(k[t])$ and $W_n \Omega^1$ is generated by $d[t], V(d[t]), V^2(d[t]), \ldots$ The relation $Fd[t] = [t]^{p-1} d[t]$ encodes how the Frobenius interacts with the differential.

The operators $F$, $V$, and $R$ encode the arithmetic structure (Frobenius action, $p$-divisibility) that is invisible in ordinary de Rham cohomology, making the de Rham--Witt complex the natural home for $p$-adic Hodge-theoretic information in positive characteristic.

Reference: [Davis, Notes on the de Rham--Witt complex](https://www3.nd.edu/~mbehren1/TAGS/Davis_notes.pdf).

<!-- BENCHMARK_PROBLEM: What cohomology theory does the hypercohomology of the de Rham-Witt complex W Omega^*_X compute for a smooth variety X over a perfect field k of characteristic p > 0? -->

## Nearby cycles

### Example: Tate twist {#ecag-0292}

The Tate twist $\mathbb{Z}(n)$ is a fundamental bookkeeping device in cohomology that accounts for the discrepancy between cohomological degree and motivic weight. Its definition varies by context.

**Betti cohomology.** Over $\mathbb{C}$, set $\mathbb{Z}(1) = 2\pi i \cdot \mathbb{Z} \subset \mathbb{C}$ and $\mathbb{Z}(n) = (2\pi i)^n \cdot \mathbb{Z}$. As an abelian group, $\mathbb{Q}(n) \cong \mathbb{Q}$, but as a Hodge structure it is pure of type $(-n, -n)$. The Tate twist $\mathbb{Q}(n)$ shifts the Hodge filtration: if $V$ is a pure Hodge structure of weight $k$, then $V(n) = V \otimes \mathbb{Q}(n)$ is pure of weight $k - 2n$, with $F^p V(n) = F^{p+n} V$.

**Etale cohomology.** For a scheme over a field $k$ with $\ell$ invertible in $k$, set $\mathbb{Z}/\ell^n(1) = \mu_{\ell^n}$ (the sheaf of $\ell^n$-th roots of unity) and

$$
\mathbb{Z}_\ell(1) = \varprojlim_n \mu_{\ell^n}, \qquad \mathbb{Z}_\ell(m) = \mathbb{Z}_\ell(1)^{\otimes m}.

$$

The absolute Galois group $\operatorname{Gal}(\overline{k}/k)$ acts on $\mathbb{Z}_\ell(1)$ via the cyclotomic character $\chi_\ell : \operatorname{Gal}(\overline{k}/k) \to \mathbb{Z}_\ell^{\times}$. For $k = \mathbb{F}_q$, the geometric Frobenius acts on $\mathbb{Z}_\ell(1)$ as multiplication by $q^{-1}$, so tensoring with $\mathbb{Q}_\ell(n)$ multiplies all Frobenius eigenvalues by $q^{-n}$.

**$p$-adic cohomology.** The $p$-adic Tate twist $\mathbb{Z}_p(n)$ in mixed characteristic $(0,p)$ is more subtle. Constructions by Sato and others produce sheaves $\mathbb{Z}/p^r(n)$ on the etale site related to logarithmic de Rham--Witt sheaves $W_r \Omega^n_{\log}$.

**Role in nearby cycles.** For a family $f : X \to S$ degenerating over $0 \in S$, the monodromy operator on nearby cycles satisfies

$$
N : \operatorname{Gr}_k^W R^n \Psi \mathbb{Q} \to \operatorname{Gr}_{k-2}^W R^n \Psi \mathbb{Q}(-1).

$$

The Tate twist $(-1)$ accounts for the weight shift of $-2$: since $\mathbb{Q}(-1)$ has weight $2$, tensoring with it compensates, making $N$ a morphism between objects of the same weight. Without the Tate twist, the graded pieces of the weight filtration would not carry pure Hodge structures of the correct weight, and the formalism of mixed Hodge modules would break down.

<!-- BENCHMARK_PROBLEM: In etale cohomology with l-adic coefficients, how is the Tate twist Z_l(1) defined? What Galois representation does it correspond to? -->

### Example: inertia group {#ecag-0293}

Let $K$ be a complete discretely valued field with valuation ring $\mathcal{O}_K$, maximal ideal $\mathfrak{m}$, and residue field $k = \mathcal{O}_K / \mathfrak{m}$. Fix an algebraic closure $\overline{K}$ and let $\overline{k}$ be the corresponding residue field. The **inertia group** $I$ is defined as the kernel

$$
1 \to I \to \operatorname{Gal}(\overline{K}/K) \to \operatorname{Gal}(\overline{k}/k) \to 1,

$$

so $I$ consists of those automorphisms of $\overline{K}$ that act trivially on the residue field.

The inertia group admits a further filtration by ramification. The **wild inertia** (or **$p$-part**) $P \subset I$ is the pro-$p$-Sylow subgroup, where $p = \operatorname{char}(k)$. The **tame inertia** is the quotient $I^t = I/P$, which is a profinite group isomorphic to $\prod_{\ell \neq p} \mathbb{Z}_\ell$. When $\operatorname{char}(k) = 0$, there is no wild ramification and $I = I^t$.

In the complex-analytic setting ($K = \mathbb{C}(\!(t)\!)$, $k = \mathbb{C}$), the absolute Galois group is the profinite completion $\widehat{\mathbb{Z}}$ of $\pi_1(D^*) \cong \mathbb{Z}$, and the inertia group is all of $\operatorname{Gal}(\overline{K}/K) \cong \widehat{\mathbb{Z}}$ (since $\operatorname{Gal}(\overline{\mathbb{C}}/\mathbb{C}) = 1$). The monodromy transformation $T$ is the image of the topological generator.

**Role in nearby cycles.** For a proper family $f : X \to \operatorname{Spec}(\mathcal{O}_K)$, the nearby cycles functor $R\Psi$ produces sheaves on the special fiber $X_s$ equipped with a continuous action of $\operatorname{Gal}(\overline{K}/K)$. The structure theorems are:

1. **Grothendieck's monodromy theorem.** The action of $I$ on $R^n \Psi \mathbb{Q}_\ell$ is quasi-unipotent: after a finite extension of $K$ (i.e., passing to a finite-index subgroup of $I$), the action becomes unipotent.
2. **Tame quotient.** The tame inertia $I^t \cong \prod_{\ell \neq p} \mathbb{Z}_\ell$ acts through a single topological generator, whose action gives the monodromy operator.
3. **Wild part.** The wild inertia $P$ acts through a finite quotient on $R^n \Psi \mathbb{Q}_\ell$ (this is the content of quasi-unipotence restricted to the $p$-part).

The inertia group thus captures the "local monodromy" at a place of bad reduction, and its structure (tame vs. wild) dictates the complexity of the degeneration.

<!-- BENCHMARK_PROBLEM: Define the inertia group I for a complete discretely valued field K with residue field k. What is the relationship between I and the Galois groups of K and k? -->

### Example: Frobenius morphisms {#ecag-0294}

Let $X$ be a scheme over $\mathbb{F}_p$.

**Absolute Frobenius.** The absolute Frobenius $F_{\mathrm{abs}} : X \to X$ is the identity on the underlying topological space and the $p$-th power map $a \mapsto a^p$ on $\mathcal{O}_X$. It is functorial in $X$ but is not a morphism of $\mathbb{F}_p$-schemes (it does not commute with the structure map to $\operatorname{Spec}(\mathbb{F}_p)$ unless $X = \operatorname{Spec}(\mathbb{F}_p)$).

**Relative Frobenius.** If $X$ is an $S$-scheme with $S$ an $\mathbb{F}_p$-scheme, define the Frobenius twist $X^{(p)} = X \times_{S, F_S} S$. The relative Frobenius $F_{X/S} : X \to X^{(p)}$ is the unique morphism making the diagram

$$
\begin{array}{ccc}
X & \xrightarrow{F_{X/S}} & X^{(p)} \\
& \searrow & \downarrow \\
& & S
\end{array}

$$

commute, where $X \to S$ is the structure map and $X^{(p)} \to S$ is the base-changed structure map. The relative Frobenius is a morphism of $S$-schemes and is a purely inseparable morphism of degree $p^{\dim X}$.

**Arithmetic and geometric Frobenius.** For $X$ over $\mathbb{F}_q$ (with $q = p^r$), the arithmetic Frobenius $\operatorname{Frob}_q \in \operatorname{Gal}(\overline{\mathbb{F}_q}/\mathbb{F}_q)$ acts by $x \mapsto x^q$. It acts on $\ell$-adic cohomology $H^n_{\mathrm{et}}(X_{\overline{\mathbb{F}_q}}, \mathbb{Q}_\ell)$ by functoriality. The geometric Frobenius $\operatorname{Frob}_q^{-1}$ is its inverse. Deligne's theorem (the Weil conjectures) states: for $X$ smooth and projective over $\mathbb{F}_q$, the eigenvalues $\alpha$ of geometric Frobenius on $H^n_{\mathrm{et}}(X_{\overline{\mathbb{F}_q}}, \mathbb{Q}_\ell)$ are algebraic numbers satisfying

$$
|\alpha| = q^{n/2}

$$

under every complex embedding. This is the "Riemann hypothesis over finite fields."

**Interaction with nearby cycles.** For a family $f : X \to S$ over a trait $S = \operatorname{Spec}(\mathcal{O}_K)$ with residue characteristic $p$, the nearby cycles $R\Psi$ carry commuting actions of the inertia group $I$ (monodromy) and the Frobenius on the special fiber. The **weight-monodromy conjecture** asserts that the monodromy filtration $M_\bullet$ and the weight filtration $W_\bullet$ (defined via Frobenius eigenvalues) are related by $M_k = W_{k+n}$ on $R^n \Psi \mathbb{Q}_\ell$. This conjecture, proved by Deligne for $\ell$-adic cohomology over equal-characteristic local fields, unifies the arithmetic notion of weight (Frobenius eigenvalue magnitude) with the geometric notion (the weight filtration from mixed Hodge theory).

<!-- BENCHMARK_PROBLEM: For a smooth projective variety X over F_q, what does the Weil conjecture (Riemann hypothesis, proved by Deligne) say about the eigenvalues of geometric Frobenius acting on H^n_et(X_{F_q-bar}, Q_l)? -->

### Example: monodromy operators {#ecag-0295}

Let $f : X \to D$ be a proper morphism from a smooth variety to a disk $D$ with smooth generic fiber. The fundamental group $\pi_1(D^*) \cong \mathbb{Z}$ of the punctured disk acts on the cohomology of the generic fiber $X_t$, producing the monodromy transformation $T \in \operatorname{Aut}(H^n(X_t; \mathbb{Q}))$.

By the monodromy theorem, $T$ is quasi-unipotent: there exist positive integers $m$ and $k$ such that $(T^m - \operatorname{Id})^k = 0$. After the base change $s \mapsto s^m$ (which replaces $T$ by $T^m$), we may assume $T$ is unipotent: $(T - \operatorname{Id})^k = 0$ for some $k$. The **monodromy operator** (or **log monodromy**) is the nilpotent endomorphism

$$
N = \log(T) = \sum_{j=1}^{k-1} \frac{(-1)^{j+1}}{j}(T - \operatorname{Id})^j,

$$

which is a finite sum since $T$ is unipotent.

The operator $N$ determines a unique increasing filtration $M_\bullet$ on $H^n(X_t; \mathbb{Q})$, called the **monodromy filtration**, characterized by two properties:

1. $N(M_j) \subset M_{j-2}$ (the operator $N$ shifts the filtration by $-2$).
2. $N^j : \operatorname{Gr}_j^M \xrightarrow{\;\sim\;} \operatorname{Gr}_{-j}^M$ is an isomorphism for all $j \geq 0$.

These two conditions determine $M_\bullet$ uniquely from $N$. Concretely, the filtration is built from the kernels and images of powers of $N$:

$$
M_j = \sum_{i \geq 0} \ker(N^{i+1}) \cap \operatorname{im}(N^{\max(i-j, 0)}).

$$

The **monodromy weight conjecture** (or weight-monodromy conjecture) asserts that the monodromy filtration $M_\bullet$, centered at weight $n$, coincides with the weight filtration from mixed Hodge theory. That is, on $H^n(X_t; \mathbb{Q})$:

$$
W_{n+j} = M_j.

$$

This has been proved in several important cases (by Deligne in equal characteristic, by Scholze for complete intersections in toric varieties).

At the sheaf level, $N$ acts as $N : R^n \Psi \mathbb{Q} \to R^n \Psi \mathbb{Q}(-1)$, where the Tate twist $(-1)$ accounts for the weight shift: $N$ maps weight $k$ to weight $k - 2$, and tensoring with $\mathbb{Q}(-1)$ (which has weight 2) restores the balance.

<!-- BENCHMARK_PROBLEM: Given a unipotent monodromy transformation T acting on H^n(X_t; Q), define the monodromy operator N. What are the two defining properties of the monodromy filtration M_* associated to N? -->

### Example: Milnor fibration, nearby cycles of a family $X\rightarrow D$, [reference](http://achinger.impan.pl/thesis.pdf) {#ecag-0296}

Consider the family $f : X \to D$ defined by $X = \{(x_1, x_2, t) \in \mathbb{C}^2 \times D \mid x_1 x_2 = t\}$ with projection $(x_1, x_2, t) \mapsto t$. The special fiber $X_0 = \{x_1 x_2 = 0\}$ consists of the two coordinate axes meeting at the origin, and each generic fiber $X_t \cong \{x_1 x_2 = t\} \cong \mathbb{C}^{\times}$ for $t \neq 0$ is a smooth hyperbola.

**Milnor fiber at the singular point.** The Milnor fiber $F_{\mathrm{pt}}$ at the origin $(0,0,0) \in X_0$ captures the local topology of the degeneration. Concretely, $F_{\mathrm{pt}}$ is the intersection of the generic fiber $\{x_1 x_2 = \epsilon\}$ with a small ball around the origin. For small $\epsilon \neq 0$, this set $\{(a, \epsilon/a) : a \in \mathbb{C}^{\times},\, |a|^2 + |\epsilon/a|^2 < r^2\}$ retracts onto the circle $|a| = |\epsilon|^{1/2}$. Therefore

$$
F_{\mathrm{pt}} \simeq S^1.

$$

**Milnor fiber at smooth points.** At any point $q \in X_0$ away from the origin, the family $f$ is a submersion (the singular locus of $f$ is precisely the origin), so the Milnor fiber is contractible: $F_q \simeq \{*\}$.

**Nearby cycles sheaves.** The stalk of $R^k \Psi \mathbb{Z}$ at a point $q \in X_0$ is $H^k(F_q; \mathbb{Z})$. This gives:

| Point $q \in X_0$ | $F_q$ | $(R^0\Psi\mathbb{Z})_q$ | $(R^1\Psi\mathbb{Z})_q$ |
|---|---|---|---|
| smooth point | $\{*\}$ | $\mathbb{Z}$ | $0$ |
| origin | $S^1$ | $\mathbb{Z}$ | $\mathbb{Z}$ |

As sheaves on $X_0$:

$$
R^0 \Psi \mathbb{Z} \cong \mathbb{Z}_{X_0}, \qquad R^1 \Psi \mathbb{Z} \cong \mathbb{Z}_{\mathrm{pt}},

$$

where $\mathbb{Z}_{X_0}$ is the constant sheaf and $\mathbb{Z}_{\mathrm{pt}}$ is the skyscraper sheaf supported at the origin.

The single nontrivial cycle in $H^1(F_{\mathrm{pt}}) = H^1(S^1) = \mathbb{Z}$ is the **vanishing cycle**: it is the homology class in the generic fiber that collapses to a point as $t \to 0$. This is the prototypical example of the Picard--Lefschetz theory of vanishing cycles for ordinary double points (nodes of type $A_1$).

<!-- BENCHMARK_PROBLEM: For the family x_1 x_2 = t over a disk, what is the Milnor fiber over the singular point (0,0,0)? What are the nearby cycles sheaves R^0 Psi Z and R^1 Psi Z on the special fiber? -->

### Example: Dwork family of elliptic curves, need 'monodromy formula' {#ecag-0297}

We compute the monodromy action on $H^1(X_t; \mathbb{Z})$ for the Dwork family

$$
f : X = \{(\epsilon, [x:y:z]) \in D \times \mathbb{P}^2 \mid \epsilon(x^3 + y^3 + z^3) = 3xyz\} \to D, \quad (\epsilon, [x:y:z]) \mapsto \epsilon.

$$

**The special fiber.** At $\epsilon = 0$, the equation becomes $3xyz = 0$, giving the union of three coordinate lines $L_1 = \{x=0\}$, $L_2 = \{y=0\}$, $L_3 = \{z=0\}$ in $\mathbb{P}^2$. These form a triangle with vertices

$$
P_1 = [1:0:0], \quad P_2 = [0:1:0], \quad P_3 = [0:0:1].

$$

For generic $\epsilon \neq 0$, the fiber $X_\epsilon$ is a smooth elliptic curve with $H^1(X_\epsilon; \mathbb{Z}) \cong \mathbb{Z}^2$.

**Step 1: Nearby cycles sheaves.** At each vertex $P_i$, the singularity of $f$ is locally of the form $x_1 x_2 = t$ (an ordinary double point), so the Milnor fiber is $S^1$ and $R^1 \Psi \mathbb{Z}$ has stalk $\mathbb{Z}$ at each $P_i$. At smooth points of $X_0$, the family is locally trivial. Therefore:

$$
R^0 \Psi \mathbb{Z} \cong \mathbb{Z}_{X_0}, \qquad R^1 \Psi \mathbb{Z} \cong \bigoplus_{i=1}^{3} \mathbb{Z}_{P_i}.

$$

**Step 2: The nearby cycles spectral sequence.** The $E_2$-page of $H^p(X_0, R^q \Psi \mathbb{Z}) \Rightarrow H^{p+q}(X_t; \mathbb{Z})$ is:

| $q \setminus p$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $1$ | $\mathbb{Z}^3$ | $0$ | $0$ |
| $0$ | $\mathbb{Z}$ | $\mathbb{Z}$ | $\mathbb{Z}^3$ |

Here $H^1(X_0, \mathbb{Z}) = \mathbb{Z}$: the triangle of three $\mathbb{P}^1$'s has first homology generated by the loop around the triangle. And $H^2(X_0, \mathbb{Z}) = \mathbb{Z}^3$: each irreducible component $L_i \cong \mathbb{P}^1$ contributes a fundamental class.

The differential $d_2 : E_2^{0,1} = \mathbb{Z}^3 \to E_2^{2,0} = \mathbb{Z}^3$ must be compatible with convergence to $H^*(X_t)$ with $H^0 = \mathbb{Z}$, $H^1 = \mathbb{Z}^2$, $H^2 = \mathbb{Z}$. The resulting exact sequence is:

$$
0 \to H^1(X_0, \mathbb{Z}) \xrightarrow{\;i\;} H^1(X_t, \mathbb{Z}) \xrightarrow{\;p\;} H^0(X_0, R^1\Psi\mathbb{Z}) \xrightarrow{\;d_2\;} H^2(X_0, \mathbb{Z}) \to H^2(X_t, \mathbb{Z}) \to 0,

$$

$$
0 \to \mathbb{Z} \xrightarrow{\;i\;} \mathbb{Z}^2 \xrightarrow{\;p\;} \mathbb{Z}^3 \xrightarrow{\;d_2\;} \mathbb{Z}^3 \to \mathbb{Z} \to 0.

$$

Since $\operatorname{im}(p) = \ker(d_2)$ has rank $2 - 1 = 1$, the map $d_2$ has rank 2.

**Step 3: Monodromy form.** Choose a basis $\{e_1, e_2\}$ of $H^1(X_t; \mathbb{Z})$ where $e_1 = i(\text{generator of } H^1(X_0))$ and $e_2$ maps to a generator of $\ker(d_2) \subset H^0(X_0, R^1 \Psi \mathbb{Z})$. The monodromy $T$ acts trivially on $H^1(X_0)$ and on the stalks of $R^1 \Psi \mathbb{Z}$, so it has the form

$$
T = \begin{pmatrix} 1 & m \\ 0 & 1 \end{pmatrix}

$$

for some integer $m$.

**Step 4: The monodromy formula.** There is a commutative diagram relating the two filtration steps of $H^1(X_t)$:

$$
\begin{array}{ccc}
H^1(X_t, \mathbb{Z}) & \xrightarrow{\;p\;} & H^0(X_0, R^1\Psi\mathbb{Z}) \\
\downarrow\, {1-T} & & \downarrow\, \overline{\alpha} \\
H^1(X_t, \mathbb{Z}) & \xleftarrow{\;i\;} & H^1(X_0, \mathbb{Z})
\end{array}

$$

where $\overline{\alpha}$ is the connecting homomorphism from the short exact sequence

$$
0 \to \mathbb{Z}_{X_0} \to \bigoplus_{i=1}^{3} \mathbb{Z}_{L_i} \to \bigoplus_{i=1}^{3} \mathbb{Z}_{P_i} \to 0.

$$

A Cech cohomology computation shows $\overline{\alpha}([P_i])$ equals the generator of $H^1(X_0, \mathbb{Z}) = \mathbb{Z}$ for each $i$.

**Step 5: Exploiting the $\mathbb{Z}/3\mathbb{Z}$-symmetry.** The cyclic permutation $(x,y,z) \mapsto (y,z,x)$ acts on the Dwork family, permuting $P_1, P_2, P_3$ cyclically. Since $p$ is equivariant and $\operatorname{coker}(p) \cong \mathbb{Z}^2$ is torsion-free, the image $\operatorname{im}(p) \subset \mathbb{Z}^3$ is generated by the invariant element $[P_1] + [P_2] + [P_3]$. Therefore:

$$
\overline{\alpha}([P_1] + [P_2] + [P_3]) = 3 \in H^1(X_0, \mathbb{Z}) \cong \mathbb{Z}.

$$

From the commutative diagram, $(1-T)(e_2) = i(\overline{\alpha}(p(e_2))) = \pm 3 \cdot e_1$. Fixing orientations, the monodromy matrix is:

$$
T = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}.

$$

The monodromy index $m = 3$ equals the number of nodes in the special fiber. This is a general phenomenon for semistable degenerations of elliptic curves: the monodromy is unipotent with $m$ equal to the number of irreducible components in the Neron polygon of the special fiber.

<!-- BENCHMARK_PROBLEM: For the Dwork family of elliptic curves epsilon(x^3+y^3+z^3) = 3xyz, what is the monodromy matrix T acting on H^1(X_t; Z) with respect to a suitable basis? What integer m appears in the upper-right entry? -->

### Remark {#ecag-0298}

Every irreducible complex representation of an abelian group is 1-dimensional. This follows from Schur's lemma: if $\rho : G \to \operatorname{GL}(V)$ is an irreducible representation and $G$ is abelian, then $\rho(g)$ commutes with $\rho(h)$ for all $g, h \in G$, hence every $\rho(g)$ is an intertwining operator for $\rho$. Schur's lemma then forces $\rho(g)$ to be a scalar multiple of the identity, so every subspace of $V$ is $G$-invariant. Irreducibility then requires $\dim V = 1$.

However, representations of abelian groups need not be semisimple (i.e., decompose as direct sums of irreducibles) unless the group is compact. The key example is $G = \mathbb{Z}$ with the representation

$$
\rho : \mathbb{Z} \to \operatorname{GL}_2(\mathbb{C}), \qquad 1 \mapsto \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.

$$

The subspace $\mathbb{C} \cdot \binom{1}{0}$ is invariant, but there is no complementary invariant subspace: if $\binom{a}{b}$ with $b \neq 0$ spanned a second invariant line, then $\rho(1) \binom{a}{b} = \binom{a+b}{b}$ would need to be a scalar multiple of $\binom{a}{b}$, forcing $b = 0$. So $\rho$ is indecomposable but reducible.

This is precisely the situation encountered with monodromy. The monodromy representation of $\pi_1(D^*) \cong \mathbb{Z}$ on $H^n(X_t; \mathbb{Q})$ is typically not semisimple when the special fiber is singular. The Jordan block structure of the monodromy transformation $T$ is encoded by the nilpotent operator $N = \log(T)$, and the monodromy filtration extracts this structure in a canonical way.

For compact groups the situation is different: every continuous finite-dimensional representation is semisimple, by Maschke's theorem (finite groups) or the Peter--Weyl theorem (compact groups). The existence of a Haar measure on compact groups allows averaging to construct invariant complements, which fails for $\mathbb{Z}$ or other non-compact groups. This algebraic distinction -- semisimple vs. non-semisimple monodromy -- is the representation-theoretic core of the theory of degenerations.

<!-- BENCHMARK_PROBLEM: Give an example of a 2-dimensional representation of Z over C that is indecomposable but not irreducible. Why does this not contradict the fact that every irreducible representation of an abelian group is 1-dimensional? -->
