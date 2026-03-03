---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/weight.tex
---

## Weights, nearby and vanishing cycles

### Example: $X=\mathbb{C}^{\times}\hookrightarrow\mathbb{P}_{\mathbb{C}}^{1}=\overline{X}$, weight filtration {#ecag-0278}

**Statement:** Let $X = \mathbb{C}^{\times}$ embedded in $\overline{X} = \mathbb{P}^{1}_{\mathbb{C}}$ as the complement of two points. Compute the weight spectral sequence and the weight filtration on the cohomology of $X$.

**Construction/Proof:** The boundary divisor is $D = \overline{X} \setminus X = \{0, \infty\}$, which consists of two points. Using the weight spectral sequence framework with $D^{(0)} = \overline{X} = \mathbb{P}^{1}$ and $D^{(1)} = \{0, \infty\}$, the $E_1$-page is:

$$
E_1^{-p,q} = H^{q-2p}(D^{(p)}; \mathbb{Q})

$$

Laying this out (rows indexed by $q$, columns by $p$):

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $H^0(D^{(1)}) = \mathbb{Q}^2$ | $H^2(\mathbb{P}^1) = \mathbb{Q}$ |
| $1$ | $0$ | $H^1(\mathbb{P}^1) = 0$ |
| $0$ | $0$ | $H^0(\mathbb{P}^1) = \mathbb{Q}$ |

The differential $d_1 : E_1^{-1,2} \to E_1^{0,2}$ is the Gysin map $H^0(D^{(1)}) \to H^2(\overline{X})$, which sends each point class to the fundamental class of $\mathbb{P}^1$. Since both points map to the same generator of $H^2(\mathbb{P}^1) \cong \mathbb{Q}$, this map $\mathbb{Q}^2 \to \mathbb{Q}$ is surjective with kernel $\mathbb{Q}$.

We can verify surjectivity independently: the spectral sequence converges to $H^{p+q}(X; \mathbb{Q})$, and since $X = \mathbb{C}^{\times} \simeq S^1$ is homotopy equivalent to a circle, we have $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}$, and $H^k(X) = 0$ for $k \geq 2$. This forces $d_1$ to be surjective.

The $E_2$-page is therefore:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $\mathbb{Q}$ | $0$ |
| $1$ | $0$ | $0$ |
| $0$ | $0$ | $\mathbb{Q}$ |

This gives the weight filtration on $H^1(X; \mathbb{Q})$:

$$
0 = W_0 H^1(X; \mathbb{Q}) \subset W_1 H^1(X; \mathbb{Q}) = 0 \subset W_2 H^1(X; \mathbb{Q}) = H^1(X; \mathbb{Q}) = \mathbb{Q}.

$$

Thus $\operatorname{Gr}_2^W H^1(X; \mathbb{Q}) = W_2 H^1(X; \mathbb{Q}) / W_1 H^1(X; \mathbb{Q}) \cong \mathbb{Q}$, reflecting the fact that the nontrivial cohomology in degree 1 comes entirely from the boundary divisor (weight 2), consistent with $X$ being affine.

**Key Insight:** The generator of $H^1(\mathbb{C}^{\times})$ has pure weight 2, not weight 1, because it arises from the boundary $D$ via the Gysin map rather than from the compact part $\overline{X}$. This is a hallmark of non-compact smooth varieties.

**Prerequisites:** Weight spectral sequence, Gysin maps, cohomology of $\mathbb{P}^1$, homotopy type of $\mathbb{C}^{\times}$

<!-- BENCHMARK_PROBLEM: Let X = C^* embedded in P^1_C as the complement of {0, infty}. Compute the weight filtration on H^1(X; Q). What is Gr_2^W H^1(X; Q)? -->

### Remark: Weight filtration, [reference, Joana Cirici](http://userpage.fu-berlin.de/jcirici/computeweight.pdf) {#ecag-0279}

Let $X$ be a smooth complex variety of dimension $n$. Let $j : X \hookrightarrow \overline{X}$ be a smooth compactification of $X$ such that $D = \overline{X} \setminus X$ is a normal crossing divisor. Write $D = \bigcup_{i=1}^{N} D_i$ for the decomposition of $D$ into irreducible components. Define $D^{(0)} = \overline{X}$ and for $p \geq 1$,

$$
D^{(p)} = \coprod_{\{i_1, \dots, i_p\} \subset \{1, 2, \dots, N\}} D_{i_1} \cap \cdots \cap D_{i_p}.

$$

Since $D$ is a normal crossing divisor, each connected component of $D^{(p)}$ is a smooth projective variety of dimension $n - p$.

The weight spectral sequence is given by

$$
E_1^{-p,q} = H^{q-2p}(D^{(p)}; \mathbb{Q}) \Rightarrow H^{q-p}(X; \mathbb{Q}).

$$

The differential on the $E_1$-page is

$$
d_1 : E_1^{-p,q} \to E_1^{-p+1,q},

$$

given by the alternating sum of Gysin maps

$$
i_*(j) : H^{q-2p}(D_{i_1} \cap \cdots \cap D_{i_p}) \to H^{q-2p+2}(D_{i_1} \cap \cdots \cap \widehat{D_{i_k}} \cap \cdots \cap D_{i_p}),

$$

where $i$ is the natural closed embedding and $\widehat{D_{i_k}}$ denotes omission.

The weight spectral sequence degenerates at $E_2$, yielding a filtration

$$
0 = W_{n-1} H^n(X; \mathbb{Q}) \subset W_n H^n(X; \mathbb{Q}) \subset \cdots \subset W_{2n} H^n(X; \mathbb{Q}) = H^n(X; \mathbb{Q}),

$$

where $\operatorname{Gr}_q^W H^{p+q} = E_2^{p,q}$ and $W_{k+1} H^n(X; \mathbb{Q}) / W_k H^n(X; \mathbb{Q}) = \operatorname{Gr}_{k+1}^W H^n(X; \mathbb{Q})$.

The $E_1$-page for a surface ($n = 2$) has the following layout (rows indexed by $q$, columns by $-p$):

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $5$ | $H^1(D^{(2)})$ | $H^3(D^{(1)})$ | $H^5(\overline{X})$ |
| $4$ | $H^0(D^{(2)})$ | $H^2(D^{(1)})$ | $H^4(\overline{X})$ |
| $3$ | $0$ | $H^1(D^{(1)})$ | $H^3(\overline{X})$ |
| $2$ | $0$ | $H^0(D^{(1)})$ | $H^2(\overline{X})$ |
| $1$ | $0$ | $0$ | $H^1(\overline{X})$ |
| $0$ | $0$ | $0$ | $H^0(\overline{X})$ |

with differentials $d_1$ going from column $-p$ to column $-p+1$.

The $E_2$-page then reads off the graded pieces of the weight filtration: the entry at position $(-p, q)$ gives $\operatorname{Gr}_q^W H^{q-p}(X; \mathbb{Q})$. The diagonal entries corresponding to $H^n(X)$ are:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $5$ | $\operatorname{Gr}_5^W H^3$ | $\operatorname{Gr}_5^W H^4$ | $\operatorname{Gr}_5^W H^5$ |
| $4$ | $\operatorname{Gr}_4^W H^2$ | $\operatorname{Gr}_4^W H^3$ | $\operatorname{Gr}_4^W H^4$ |
| $3$ | $0$ | $\operatorname{Gr}_3^W H^2$ | $\operatorname{Gr}_3^W H^3$ |
| $2$ | $0$ | $\operatorname{Gr}_2^W H^1$ | $\operatorname{Gr}_2^W H^2$ |
| $1$ | $0$ | $0$ | $\operatorname{Gr}_1^W H^1$ |
| $0$ | $0$ | $0$ | $\operatorname{Gr}_0^W H^0$ |

where each anti-diagonal (entries with $q - p = n$) assembles into the weight filtration of $H^n(X; \mathbb{Q})$.

<!-- BENCHMARK_PROBLEM: For a smooth complex variety X of dimension n with smooth compactification j: X -> X_bar where D = X_bar \ X is a normal crossing divisor, what is the range of the weight filtration on H^n(X; Q)? That is, what are the smallest and largest indices k such that W_k H^n(X; Q) can be nontrivial? -->

### Remark: Gysin map {#ecag-0280}

Let $i : Z \hookrightarrow X$ be a closed embedding of smooth complex varieties with $Z$ of codimension $c$ in $X$. The **Gysin map** (or pushforward in cohomology) is the map

$$
i_* : H^k(Z; \mathbb{Q}) \to H^{k+2c}(X; \mathbb{Q})

$$

defined as the Poincare dual of the pullback in homology, or equivalently via the Thom isomorphism and the natural map from cohomology with support to ordinary cohomology. Concretely, the Gysin map is the composition

$$
H^k(Z; \mathbb{Q}) \xrightarrow{\sim} H^{k+2c}_Z(X; \mathbb{Q}) \to H^{k+2c}(X; \mathbb{Q}),

$$

where the first map is the Thom isomorphism and the second is the forgetful map from cohomology with supports.

Key properties of the Gysin map:

1. **Degree shift:** $i_*$ shifts cohomological degree by $2c$, where $c = \operatorname{codim}(Z, X)$.
2. **Projection formula:** For $\alpha \in H^*(X)$ and $\beta \in H^*(Z)$, we have $i_*(i^*(\alpha) \cup \beta) = \alpha \cup i_*(\beta)$.
3. **Functoriality:** $(i \circ j)_* = i_* \circ j_*$ for composable closed embeddings.
4. **Self-intersection:** $i^* \circ i_*(1) = c_c(\mathcal{N}_{Z/X})$, the top Chern class of the normal bundle.

In the weight spectral sequence, the Gysin maps $i_* : H^{q-2p}(D^{(p)}) \to H^{q-2p+2}(D^{(p-1)})$ provide the $d_1$ differentials, connecting the cohomology of deeper strata of the boundary divisor to shallower ones.

<!-- BENCHMARK_PROBLEM: Let i: Z -> X be a closed embedding of smooth complex varieties where Z has codimension c in X. By how many degrees does the Gysin map i_* shift cohomological degree? -->

### Example: punctured Riemann surface {#ecag-0281}

**Statement:** Let $\overline{X}$ be a compact Riemann surface of genus $g$, and let $D$ consist of $p$ distinct points. Set $X = \overline{X} \setminus D$. Compute the weight spectral sequence and the weight filtration on $H^*(X; \mathbb{Q})$.

**Construction/Proof:** We have $D^{(0)} = \overline{X}$ (a smooth projective curve of genus $g$) and $D^{(1)} = D$ (a disjoint union of $p$ points). The $E_1$-page of the weight spectral sequence is:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $H^0(D^{(1)}) = \mathbb{Q}^p$ | $H^2(\overline{X}) = \mathbb{Q}$ |
| $1$ | $0$ | $H^1(\overline{X}) = \mathbb{Q}^{2g}$ |
| $0$ | $0$ | $H^0(\overline{X}) = \mathbb{Q}$ |

The only nontrivial differential is $d_1 : E_1^{-1,2} = \mathbb{Q}^p \to E_1^{0,2} = \mathbb{Q}$, which is the Gysin map sending each point class to the fundamental class of $\overline{X}$.

To determine the $E_2$-page, observe that $X$ is an open Riemann surface with $p$ punctures. Topologically, $X$ is homotopy equivalent to a wedge of $2g + p - 1$ circles (obtained from the genus-$g$ surface by removing $p$ disks and retracting), so $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}^{2g + p - 1}$, and $H^k(X) = 0$ for $k \geq 2$. Since the spectral sequence converges to $H^*(X)$, the vanishing of $H^2(X)$ forces $d_1$ to be surjective.

The $E_2$-page is therefore:

| $q \setminus p$ | $-1$ | $0$ |
|---|---|---|
| $2$ | $\mathbb{Q}^{p-1}$ | $0$ |
| $1$ | $0$ | $\mathbb{Q}^{2g}$ |
| $0$ | $0$ | $\mathbb{Q}$ |

The weight filtration on $H^1(X; \mathbb{Q})$ is:

$$
0 = W_0 H^1(X; \mathbb{Q}) \subset W_1 H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{2g} \subset W_2 H^1(X; \mathbb{Q}) = H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{2g + p - 1}.

$$

The graded pieces are:

$$
\operatorname{Gr}_1^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{2g}, \quad \operatorname{Gr}_2^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}^{p-1}.

$$

The weight-1 part $W_1 H^1(X) \cong \mathbb{Q}^{2g}$ comes from the compact part $H^1(\overline{X})$ and carries a pure Hodge structure of weight 1. The weight-2 part $\operatorname{Gr}_2^W H^1(X) \cong \mathbb{Q}^{p-1}$ arises from the boundary and reflects the "extra" cycles created by removing points.

**Key Insight:** The weight filtration cleanly separates $H^1(X)$ into the "compact" contribution (weight 1, from the genus) and the "boundary" contribution (weight 2, from the punctures). The weight-2 piece has dimension $p - 1$ rather than $p$ because the sum of all puncture classes is cohomologically trivial.

**Prerequisites:** Weight spectral sequence, Gysin maps, topology of Riemann surfaces, cohomology of compact curves

<!-- BENCHMARK_PROBLEM: Let X be a Riemann surface of genus 3 with 5 punctures. What is the dimension of Gr_1^W H^1(X; Q) and of Gr_2^W H^1(X; Q)? -->

### Example: complement of three intersecting lines in $\mathbb{P}^{2}$ {#ecag-0282}

**Statement:** Let $\overline{X} = \mathbb{P}^2$ and let $D$ be the union of three lines in general position (intersecting pairwise at 3 distinct points). Compute the weight spectral sequence and weight filtration for $X = \overline{X} \setminus D$.

**Construction/Proof:** The three lines in general position form a normal crossing divisor. We have $D^{(0)} = \mathbb{P}^2$, $D^{(1)} = \mathbb{P}^1 \sqcup \mathbb{P}^1 \sqcup \mathbb{P}^1$ (three copies of $\mathbb{P}^1$), and $D^{(2)} = \{P_1, P_2, P_3\}$ (three intersection points). The $E_1$-page is:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $H^0(D^{(2)}) = \mathbb{Q}^3$ | $H^2(D^{(1)}) = \mathbb{Q}^3$ | $H^4(\mathbb{P}^2) = \mathbb{Q}$ |
| $3$ | $0$ | $H^1(D^{(1)}) = 0$ | $H^3(\mathbb{P}^2) = 0$ |
| $2$ | $0$ | $H^0(D^{(1)}) = \mathbb{Q}^3$ | $H^2(\mathbb{P}^2) = \mathbb{Q}$ |
| $1$ | $0$ | $0$ | $H^1(\mathbb{P}^2) = 0$ |
| $0$ | $0$ | $0$ | $H^0(\mathbb{P}^2) = \mathbb{Q}$ |

with differentials $d_1$ going rightward.

To determine the $E_2$-page, we identify the topology of $X$. Removing one line from $\mathbb{P}^2$ gives $\mathbb{C}^2 \cong \mathbb{R}^4$. Removing two more lines from $\mathbb{C}^2$ (which intersect in a single point) gives a space homotopy equivalent to $(\mathbb{C} \setminus \{0\}) \times (\mathbb{C} \setminus \{0\}) \simeq S^1 \times S^1 = T^2$. Therefore $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}^2$, $H^2(X) = \mathbb{Q}$, and $H^k(X) = 0$ for $k \geq 3$.

Using the convergence $E_2 \Rightarrow H^*(X)$, the $E_2$-page must be:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $\mathbb{Q}$ | $0$ | $0$ |
| $3$ | $0$ | $0$ | $0$ |
| $2$ | $0$ | $\mathbb{Q}^2$ | $0$ |
| $1$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $0$ | $\mathbb{Q}$ |

The weight filtration on cohomology gives:
- $H^0(X) = \mathbb{Q}$ is pure of weight 0.
- $H^1(X) = \mathbb{Q}^2$ is pure of weight 2, i.e., $\operatorname{Gr}_2^W H^1(X) = \mathbb{Q}^2$.
- $H^2(X) = \mathbb{Q}$ is pure of weight 4, i.e., $\operatorname{Gr}_4^W H^2(X) = \mathbb{Q}$.

**Key Insight:** Although $X \simeq T^2$ topologically, the weight filtration reveals that the cohomology classes all come from the boundary strata, so $H^1(X)$ is pure of weight 2 (not weight 1 as it would be for a compact torus). This distinguishes the algebraic structure of the complement from a genuine compact torus.

**Prerequisites:** Weight spectral sequence, cohomology of $\mathbb{P}^n$, normal crossing divisors, topology of hyperplane complements

<!-- BENCHMARK_PROBLEM: Let X = P^2 \ D where D is the union of three lines in general position in P^2_C. What is the weight of H^1(X; Q)? That is, for which k is Gr_k^W H^1(X; Q) nonzero? -->

### Example: complement of three concurrent lines in $\mathbb{P}^{2}$ {#ecag-0283}

**Statement:** Let $D$ be the union of three concurrent lines in $\mathbb{P}^2$ (all passing through a single point). Compute the weight filtration on $H^*(X; \mathbb{Q})$ where $X = \mathbb{P}^2 \setminus D$.

**Construction/Proof:** Three concurrent lines do not form a normal crossing divisor since they all meet at one point. To apply the weight spectral sequence, we blow up $\mathbb{P}^2$ at the common intersection point $p$. Let $\overline{X} = \operatorname{Bl}_p(\mathbb{P}^2)$ with exceptional divisor $E \cong \mathbb{P}^1$. The strict transforms $L_1, L_2, L_3$ of the three lines together with $E$ form a normal crossing divisor $D' = L_1 \cup L_2 \cup L_3 \cup E$ in $\overline{X}$, and $\overline{X} \setminus D' \cong \mathbb{P}^2 \setminus D = X$.

Now $D'^{(0)} = \overline{X}$, and $D'^{(1)} = L_1 \sqcup L_2 \sqcup L_3 \sqcup E$, which is four copies of $\mathbb{P}^1$. For $D'^{(2)}$, each strict transform $L_i$ meets $E$ in one point (and the strict transforms are now disjoint from each other since they only met at $p$), so $D'^{(2)} = \{Q_1, Q_2, Q_3\}$, three points.

Note that $H^2(\overline{X}) = \mathbb{Q}^2$ (generated by the hyperplane class and $E$), while $H^0(\overline{X}) = \mathbb{Q}$ and all other odd cohomology vanishes.

The $E_1$-page is:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $H^0(D'^{(2)}) = \mathbb{Q}^3$ | $H^2(D'^{(1)}) = \mathbb{Q}^4$ | $H^4(\overline{X}) = \mathbb{Q}$ |
| $3$ | $0$ | $0$ | $0$ |
| $2$ | $0$ | $H^0(D'^{(1)}) = \mathbb{Q}^4$ | $H^2(\overline{X}) = \mathbb{Q}^2$ |
| $1$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $0$ | $H^0(\overline{X}) = \mathbb{Q}$ |

Topologically, $X = \mathbb{P}^2 \setminus (\text{three concurrent lines})$. Removing one line gives $\mathbb{C}^2$. The remaining two lines pass through the origin in $\mathbb{C}^2$ and are distinct, so removing them gives $\mathbb{C}^2 \setminus (\text{two lines through origin})$. This retracts onto $S^3 \setminus (\text{two points}) \simeq S^1 \vee S^1$ (since each complex line through the origin meets $S^3$ in a circle, and two distinct such circles form a Hopf link). Therefore $X \simeq S^1 \vee S^1$, giving $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}^2$, and $H^k(X) = 0$ for $k \geq 2$.

Using convergence, the $E_2$-page is:

| $q \setminus p$ | $-2$ | $-1$ | $0$ |
|---|---|---|---|
| $4$ | $0$ | $0$ | $0$ |
| $3$ | $0$ | $0$ | $0$ |
| $2$ | $0$ | $\mathbb{Q}^2$ | $0$ |
| $1$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $0$ | $\mathbb{Q}$ |

The weight filtration on $H^1(X; \mathbb{Q}) \cong \mathbb{Q}^2$ is:

$$
\operatorname{Gr}_2^W H^1(X; \mathbb{Q}) \cong \mathbb{Q}^2,

$$

so $H^1(X)$ is pure of weight 2.

The extra generator in $H^2(\overline{X})$ (coming from the exceptional divisor $E$) compared to $H^2(\mathbb{P}^2)$ is what changes the numerics from the general position case. In particular, the map $d_1 : \mathbb{Q}^4 \to \mathbb{Q}^2$ at the $(q=2)$ level has a 2-dimensional kernel contributing to $\operatorname{Gr}_2^W H^1(X)$, while all of $H^2(X)$ vanishes since the map $d_1 : \mathbb{Q}^3 \to \mathbb{Q}^4 \to \mathbb{Q}$ at the $(q=4)$ level is exact.

**Key Insight:** Even though three concurrent lines fail to be a normal crossing divisor, blowing up the common point resolves this while preserving the complement. The blow-up introduces an extra $\mathbb{P}^1$ in both $D'^{(1)}$ and $H^2(\overline{X})$, which changes the spectral sequence but ultimately yields $H^1(X)$ pure of weight 2, just as in the general position case -- though the topology changes from $T^2$ to $S^1 \vee S^1$.

**Prerequisites:** Blow-ups, exceptional divisors, normal crossing divisors, weight spectral sequence, topology of line complements

<!-- BENCHMARK_PROBLEM: Let X = P^2_C minus three concurrent lines. What is the homotopy type of X, and what is the dimension of H^1(X; Q)? -->

### Remark: $X=\mathbb{C}^{2}\setminus\{0\}\subset \mathbb{P}^{2}$ {#ecag-0284}

Consider $X = \mathbb{C}^2 \setminus \{0\}$, which we wish to compactify inside $\mathbb{P}^2$. The complement $\mathbb{P}^2 \setminus \mathbb{C}^2 = \mathbb{P}^1_\infty$ is a line at infinity, and removing the origin from $\mathbb{C}^2$ creates a singularity of the boundary.

To apply the weight spectral sequence, blow up $\mathbb{P}^2$ at the origin. Let $\overline{X} = \operatorname{Bl}_0(\mathbb{P}^2)$ with exceptional divisor $E \cong \mathbb{P}^1$ and strict transform $L_\infty$ of the line at infinity. Then $D = E \cup L_\infty$ is a normal crossing divisor in $\overline{X}$ (the two components are disjoint since the origin is not on the line at infinity), and $\overline{X} \setminus D \cong \mathbb{C}^2 \setminus \{0\} = X$.

We have $D^{(1)} = E \sqcup L_\infty$ (two disjoint copies of $\mathbb{P}^1$), and $D^{(2)} = \emptyset$ (since $E$ and $L_\infty$ do not intersect). Topologically, $X = \mathbb{C}^2 \setminus \{0\} \simeq S^3$, so $H^0(X) = \mathbb{Q}$, $H^3(X) = \mathbb{Q}$, and all other cohomology vanishes.

The weight spectral sequence gives:
- $H^0(X) = \mathbb{Q}$, pure of weight 0.
- $H^3(X) = \mathbb{Q}$, pure of weight 4 (coming from the boundary divisor via $\operatorname{Gr}_4^W H^3(X) = \mathbb{Q}$).

This illustrates how the weight filtration detects the "missing" codimension-2 stratum: removing a point from $\mathbb{C}^2$ creates cohomology only in degree 3 with weight 4, consistent with the general principle that boundary contributions increase weight.

<!-- BENCHMARK_PROBLEM: What is the homotopy type of C^2 \ {0}? Using this, determine H^k(C^2 \ {0}; Q) for all k. -->

### Example: cubical hyperresolution, It's our guess, we didn't check the precise definition carefully!!!!!! {#ecag-0285}

**Statement:** Illustrate the structure of a cubical hyperresolution for a singular variety $X$ with a singular subvariety $Y$, using a concrete small-dimensional example.

**Construction/Proof:** A cubical hyperresolution of a singular variety $X$ is a diagram of smooth varieties indexed by the vertices of a cube (or more generally, a truncated cube), together with proper maps assembling into a resolution of singularities in a homotopical sense. For a variety $X$ with singular locus $Y \subset X$, the simplest cubical hyperresolution is a square (1-cubical hyperresolution):

Consider $X$ with singular subvariety $Y$. Let $\widetilde{X} \to X$ be a resolution of singularities, and let $\widetilde{Y} = \widetilde{X} \times_X Y$ be the fiber product (the preimage of $Y$ in $\widetilde{X}$). Then the cubical hyperresolution diagram is:

$$
\widetilde{Y} \to \widetilde{X}

$$

$$
\downarrow \qquad \downarrow

$$

$$
Y \to X

$$

For a more elaborate example, consider $X$ a nodal curve with a node at $Y = \{*\}$. Let $\widetilde{X} = C'$ be the normalization (a smooth curve), and $\widetilde{Y} = \{*, *\}$ the preimage of the node. Then the resolution $\mathbb{P}^1$ appears as an intermediate term. The full 2-cubical hyperresolution takes the form of a cube:

The front face resolves the pair $(Y, X)$, the back face resolves the pair $(\widetilde{Y}, C')$, and the maps between them encode the resolution data. Specifically:
- The bottom face connects $Y = \{*\}$ and its further resolution.
- The top face connects $\widetilde{Y} = \{*, *\}$ with the exceptional geometry.
- The vertical maps are the resolution maps.

The weight spectral sequence for a singular variety is constructed from the cohomology of the terms in such a cubical hyperresolution, generalizing the smooth case where the normal crossing divisor strata play the role of resolution terms.

**Key Insight:** Cubical hyperresolutions replace the role of smooth compactifications with normal crossing divisors (used for smooth varieties) by providing a functorial diagram of smooth varieties that resolves singularities in a cohomological sense, enabling the construction of mixed Hodge structures on singular varieties.

**Prerequisites:** Resolution of singularities, fiber products, mixed Hodge theory, simplicial and cubical diagrams

<!-- BENCHMARK_PROBLEM: In a 1-cubical hyperresolution of a singular variety X with singular locus Y, what are the four terms of the square diagram? Describe them in terms of X, Y, and a resolution of singularities. -->

### Example: Nodal curve {#ecag-0286}

**Statement:** Compute the resolution diagram and mixed Hodge structure for the nodal cubic curve $X = \{(x : y : z) \in \mathbb{P}^2 \mid y^2 z = x^2(x + z)\}$.

**Construction/Proof:** The curve $X$ has a single node at $P = (0 : 0 : 1)$. The normalization provides the standard resolution: let $f : \widetilde{X} \to X$ be the normalization map. Since $X$ is a rational curve with one node, $\widetilde{X} \cong \mathbb{P}^1$. The preimage of the node consists of two points: $\widetilde{Y} = f^{-1}(P) = \{Q_1, Q_2\}$. Setting $Y = \{P\}$, we obtain the resolution square:

$$
\widetilde{Y} = \{Q_1, Q_2\} \to \widetilde{X} \cong \mathbb{P}^1

$$

$$
\downarrow \qquad\qquad\qquad \downarrow f

$$

$$
Y = \{P\} \qquad\to\qquad X

$$

From this diagram, the mixed Hodge structure on $H^*(X)$ can be computed via the Mayer-Vietoris-type exact sequence associated to the cubical hyperresolution:

$$
0 \to H^0(X) \to H^0(\widetilde{X}) \oplus H^0(Y) \to H^0(\widetilde{Y}) \to H^1(X) \to H^1(\widetilde{X}) \oplus H^1(Y) \to H^1(\widetilde{Y}) \to \cdots

$$

Substituting: $H^0(\widetilde{X}) = \mathbb{Q}$, $H^0(Y) = \mathbb{Q}$, $H^0(\widetilde{Y}) = \mathbb{Q}^2$, $H^1(\widetilde{X}) = 0$, $H^1(Y) = 0$, $H^1(\widetilde{Y}) = 0$, $H^2(\widetilde{X}) = \mathbb{Q}$. The exact sequence gives:

$$
0 \to H^0(X) \to \mathbb{Q}^2 \to \mathbb{Q}^2 \to H^1(X) \to 0 \to 0 \to H^2(X) \to \mathbb{Q} \to 0.

$$

The map $\mathbb{Q}^2 \to \mathbb{Q}^2$ sends $(a, b) \mapsto (a - b, a - b)$ (both points of $\widetilde{Y}$ map to the same point $P$), so its kernel is $\mathbb{Q}$ (the diagonal) and cokernel is $\mathbb{Q}$.

Therefore: $H^0(X) = \mathbb{Q}$, $H^1(X) = \mathbb{Q}$, $H^2(X) = \mathbb{Q}$.

The generator of $H^1(X) \cong \mathbb{Q}$ comes from the cokernel of $H^0(\widetilde{X}) \oplus H^0(Y) \to H^0(\widetilde{Y})$, which involves only weight-0 terms. Hence $H^1(X)$ carries weight 0, i.e.,

$$
\operatorname{Gr}_0^W H^1(X; \mathbb{Q}) = \mathbb{Q}.

$$

This is in contrast to a smooth projective curve, where $H^1$ is pure of weight 1.

**Key Insight:** The node creates a cycle in $H^1(X)$ of weight 0 (below the expected weight 1 for a smooth curve), reflecting the topological fact that the node "pinches" a handle, producing a loop that comes from the resolution's $H^0$ rather than from $H^1$ of a smooth curve.

**Prerequisites:** Normalization of curves, cubical hyperresolutions, mixed Hodge structures, Mayer-Vietoris sequence

<!-- BENCHMARK_PROBLEM: Consider the nodal cubic X = {y^2 z = x^2(x+z)} in P^2. What is H^1(X; Q), and what is its weight in the mixed Hodge structure? Compare with the case of a smooth elliptic curve. -->

### Remark: weight spectral sequence for singular varieties {#ecag-0287}

For singular varieties, the weight spectral sequence is constructed via cubical hyperresolutions rather than smooth compactifications with normal crossing boundary. Given a singular variety $X$, one chooses a cubical hyperresolution $a_\bullet : X_\bullet \to X$, where each $X_I$ (indexed by subsets $I$ of a finite set) is a smooth variety. The weight spectral sequence then takes the form

$$
E_1^{p,q} = \bigoplus_{|I|=p} H^q(X_I; \mathbb{Q}) \Rightarrow H^{p+q}(X; \mathbb{Q}).

$$

The key theorem (due to Deligne, with the cubical approach developed by Guillen, Navarro Aznar, Pascual-Gainza, and Puerta) states that:

1. The resulting mixed Hodge structure on $H^n(X; \mathbb{Q})$ is independent of the choice of cubical hyperresolution.
2. The weight filtration satisfies $W_k H^n(X; \mathbb{Q}) = 0$ for $k < 0$ and $W_k H^n(X; \mathbb{Q}) = H^n(X; \mathbb{Q})$ for $k \geq 2n$, but for singular projective varieties the weights on $H^n$ range from $0$ to $n$ (i.e., $\operatorname{Gr}_k^W H^n = 0$ for $k > n$).

This last point is dual to the smooth non-compact case, where weights on $H^n$ range from $n$ to $2n$. For a general (possibly singular, possibly non-compact) variety, the weights on $H^n$ can range from $0$ to $2n$.

<!-- BENCHMARK_PROBLEM: For a singular projective variety X, what is the range of weights that can appear in the mixed Hodge structure on H^n(X; Q)? How does this differ from a smooth projective variety? -->

### Remark: Mayer-Vietoris exact sequence {#ecag-0288}

In the context of cubical hyperresolutions and mixed Hodge theory, the Mayer-Vietoris exact sequence provides a computational tool for the cohomology of singular varieties. For the simplest cubical hyperresolution (the normalization square of a nodal curve), the associated long exact sequence takes the form:

$$
\cdots \to H^k(X) \to H^k(\widetilde{X}) \oplus H^k(Y) \to H^k(\widetilde{Y}) \to H^{k+1}(X) \to \cdots

$$

where $\widetilde{X} \to X$ is the resolution, $Y$ is the singular locus, and $\widetilde{Y} = \widetilde{X} \times_X Y$.

More generally, for a variety $X = U \cup V$ covered by two open subvarieties, the classical Mayer-Vietoris sequence

$$
\cdots \to H^k(X) \to H^k(U) \oplus H^k(V) \to H^k(U \cap V) \to H^{k+1}(X) \to \cdots

$$

is a morphism of mixed Hodge structures. This means every map in the sequence is strict with respect to the weight filtration, so one can read off weight information by tracking how classes propagate through the sequence.

The strictness property is crucial: it implies that the Mayer-Vietoris sequence splits into short exact sequences on each graded piece $\operatorname{Gr}_k^W$, greatly simplifying computations.

<!-- BENCHMARK_PROBLEM: In the Mayer-Vietoris sequence for mixed Hodge structures, what special property do the maps have with respect to the weight filtration, and why is this property useful for computations? -->

### Remark: cubical hyperresolution {#ecag-0289}

A **cubical hyperresolution** of a variety $X$ is a proper augmented cubical variety $a_\bullet : X_\bullet \to X$ (indexed by the partially ordered set of subsets of $\{0, 1, \dots, n\}$) satisfying:

1. Each $X_I$ is a smooth variety.
2. The augmentation $X_\emptyset \to X$ is a proper surjective map (typically a resolution of singularities).
3. For each $I$, the induced map $X_I \to X_{I \setminus \{i\}}$ is proper.
4. The diagram is "acyclic" in the sense that it computes the correct cohomology of $X$.

The existence of cubical hyperresolutions follows from Hironaka's resolution of singularities (in characteristic zero). The construction is inductive: at each stage, one resolves the singular locus of the previous stage and takes fiber products.

References for detailed constructions:
- [Notes on Cubical Hyperresolutions (Schwede)](https://www.math.utah.edu/~schwede/Notes/NotesOnCubicalHyperresolutions.pdf)
- [Some Remarks on Hyperresolutions (Steenbrink)](https://link.springer.com/content/pdf/10.1007/978-3-319-28829-1_15.pdf)

The advantage of cubical hyperresolutions over simplicial ones is that cubical diagrams require fewer terms and are more natural for iterated fiber products. For a variety with a stratification of depth $d$, a $d$-cubical hyperresolution suffices.

<!-- BENCHMARK_PROBLEM: What is the key property that each term X_I in a cubical hyperresolution must satisfy, and what foundational result guarantees the existence of cubical hyperresolutions in characteristic zero? -->

### Example: cuspidal singularity {#ecag-0290}

**Statement:** Compute the mixed Hodge structure on the cohomology of the cuspidal cubic $X = \{(x : y : z) \in \mathbb{P}^2 \mid y^2 z = x^3\}$.

**Construction/Proof:** The curve $X$ has a cusp at $P = (0 : 0 : 1)$. Unlike the node, the cusp is a unibranch singularity: the normalization $f : \widetilde{X} \to X$ satisfies $\widetilde{X} \cong \mathbb{P}^1$, and the preimage of the cusp is a single point: $\widetilde{Y} = f^{-1}(P) = \{Q\}$. Setting $Y = \{P\}$, the resolution square is:

$$
\widetilde{Y} = \{Q\} \to \widetilde{X} \cong \mathbb{P}^1

$$

$$
\downarrow \qquad\qquad\quad \downarrow f

$$

$$
Y = \{P\} \quad\to\quad X

$$

The associated long exact sequence is:

$$
0 \to H^0(X) \to H^0(\widetilde{X}) \oplus H^0(Y) \to H^0(\widetilde{Y}) \to H^1(X) \to H^1(\widetilde{X}) \to H^1(\widetilde{Y}) \to H^2(X) \to H^2(\widetilde{X}) \to 0.

$$

Substituting: $H^0(\widetilde{X}) = \mathbb{Q}$, $H^0(Y) = \mathbb{Q}$, $H^0(\widetilde{Y}) = \mathbb{Q}$, $H^1(\widetilde{X}) = 0$, $H^1(\widetilde{Y}) = 0$, $H^2(\widetilde{X}) = \mathbb{Q}$.

The map $H^0(\widetilde{X}) \oplus H^0(Y) \to H^0(\widetilde{Y})$ sends $(a, b) \mapsto a - b$, which is surjective from $\mathbb{Q}^2$ to $\mathbb{Q}$.

Therefore: $H^0(X) = \mathbb{Q}$, $H^1(X) = 0$, $H^2(X) = \mathbb{Q}$.

The cuspidal cubic has the same Betti numbers as $\mathbb{P}^1$, which reflects the fact that the normalization is a homeomorphism (the cusp is unibranch). In particular, $H^1(X) = 0$: unlike the nodal cubic, the cusp does not create any new $H^1$ class because no topological loop is formed.

The mixed Hodge structure is: $H^0(X) = \mathbb{Q}$ pure of weight 0, and $H^2(X) = \mathbb{Q}$ pure of weight 2.

**Key Insight:** The cusp, being a unibranch singularity, does not create any extra topology (unlike the node which creates a loop). The normalization map for a cusp is a bijection on points, so it is a homeomorphism, and the cohomology of the cuspidal cubic equals that of its normalization $\mathbb{P}^1$.

**Prerequisites:** Normalization of curves, unibranch singularities, cubical hyperresolutions, mixed Hodge structures

<!-- BENCHMARK_PROBLEM: Compare the mixed Hodge structures of the nodal cubic y^2z = x^2(x+z) and the cuspidal cubic y^2z = x^3 in P^2. In particular, what is H^1 for each, and why do they differ? -->

### Example: de Rham-Witt complex {#ecag-0291}

**Statement:** Describe the de Rham-Witt complex $W\Omega^*_X$ and its role in $p$-adic cohomology, with explicit low-degree terms for a smooth variety over a perfect field of characteristic $p > 0$.

**Construction/Proof:** Let $X$ be a smooth variety over a perfect field $k$ of characteristic $p > 0$. The de Rham-Witt complex $W_n \Omega^*_X$ is a sheaf of differential graded algebras on $X$ that generalizes both the de Rham complex and the Witt vectors. It was introduced by Bloch and further developed by Illusie.

For each $n \geq 1$, the de Rham-Witt complex $W_n \Omega^*_X$ comes equipped with:

1. **Restriction:** $R : W_{n+1} \Omega^q_X \to W_n \Omega^q_X$ (surjective).
2. **Frobenius:** $F : W_{n+1} \Omega^q_X \to W_n \Omega^q_X$.
3. **Verschiebung:** $V : W_n \Omega^q_X \to W_{n+1} \Omega^q_X$.
4. **Differential:** $d : W_n \Omega^q_X \to W_n \Omega^{q+1}_X$.

These satisfy the relations $FV = p$, $FdV = d$, and $F d[a] = [a]^{p-1} d[a]$ for a Teichmuller lift $[a]$.

In degree 0, $W_n \Omega^0_X = W_n \mathcal{O}_X$ is the sheaf of length-$n$ Witt vectors. In degree 1, $W_n \Omega^1_X$ is generated over $W_n \mathcal{O}_X$ by elements $d[a]$ and $V^{i}(d[b])$ subject to the above relations.

The inverse limit $W\Omega^*_X = \varprojlim_n W_n \Omega^*_X$ computes crystalline cohomology:

$$
H^n_{\operatorname{cris}}(X/W(k)) \cong \mathbb{H}^n(X, W\Omega^*_X),

$$

where $W(k)$ denotes the ring of $p$-typical Witt vectors of $k$. This provides a $p$-adic cohomology theory for varieties in characteristic $p$ analogous to de Rham cohomology in characteristic 0.

For $X = \operatorname{Spec}(k)$ a point, $W_n \Omega^0 = W_n(k)$ (the length-$n$ Witt vectors of $k$), and all higher forms vanish.

For $X = \mathbb{A}^1_k$, the de Rham-Witt complex in degree 0 is $W_n(k[t])$ and in degree 1 is generated by $d[t]$, $V d[t]$, $V^2 d[t]$, etc.

Reference: [Davis, Notes on the de Rham-Witt complex](https://www3.nd.edu/~mbehren1/TAGS/Davis_notes.pdf)

**Key Insight:** The de Rham-Witt complex provides a purely algebraic construction of crystalline cohomology that avoids the need to lift $X$ to characteristic 0. The operators $F$, $V$, and $R$ encode the arithmetic structure (Frobenius action, $p$-divisibility) that is invisible in ordinary de Rham cohomology.

**Prerequisites:** Witt vectors, crystalline cohomology, sheaves of differential graded algebras, smooth varieties in positive characteristic

<!-- BENCHMARK_PROBLEM: What cohomology theory does the hypercohomology of the de Rham-Witt complex W Omega^*_X compute for a smooth variety X over a perfect field k of characteristic p > 0? -->

## Nearby cycles

### Example: Tate twist {#ecag-0292}

**Statement:** Define the Tate twist $\mathbb{Z}(n)$ in various cohomological contexts and explain its role in the theory of nearby cycles.

**Construction/Proof:** The Tate twist is a fundamental bookkeeping device in cohomology that accounts for the difference between cohomological degree and motivic weight.

**In singular/Betti cohomology:** The Tate twist $\mathbb{Z}(1)$ is defined as the group $2\pi i \cdot \mathbb{Z} \subset \mathbb{C}$. More generally, $\mathbb{Z}(n) = (2\pi i)^n \cdot \mathbb{Z}$. For rational coefficients, $\mathbb{Q}(n) \cong \mathbb{Q}$ as an abelian group, but carries a pure Hodge structure of type $(-n, -n)$.

**In etale cohomology:** For a scheme $X$ over a field and a prime $\ell$ invertible in the base, $\mathbb{Z}/\ell^n(1) = \mu_{\ell^n}$, the sheaf of $\ell^n$-th roots of unity. Then $\mathbb{Z}_\ell(1) = \varprojlim_n \mu_{\ell^n}$ and $\mathbb{Z}_\ell(m) = \mathbb{Z}_\ell(1)^{\otimes m}$. The Galois group acts on $\mathbb{Z}_\ell(1)$ via the cyclotomic character $\chi : \operatorname{Gal}(\overline{k}/k) \to \mathbb{Z}_\ell^{\times}$.

**In $p$-adic cohomology:** The $p$-adic Tate twist $\mathbb{Z}_p(n)$ over a base of mixed characteristic $(0, p)$ is more subtle. Sato and others have constructed sheaves $\mathbb{Z}/p^r(n)$ on the etale site that serve as the $p$-adic analogue, related to logarithmic de Rham-Witt sheaves $W_r \Omega^n_{\log}$.

The Tate twist appears in nearby cycles through the monodromy action: if $f : X \to S$ is a family over a punctured disk, the monodromy operator $N$ on the nearby cycles $R\Psi$ shifts weight by $-2$ and involves a Tate twist, reflecting the fact that the monodromy logarithm $N = \log(T_u)$ (where $T_u$ is the unipotent part of monodromy) satisfies

$$
N : \operatorname{Gr}_k^W R^n \Psi \mathbb{Q} \to \operatorname{Gr}_{k-2}^W R^n \Psi \mathbb{Q}(-1).

$$

Reference: [Sato, $p$-adic Tate twist](http://www.math.sci.hiroshima-u.ac.jp/algebra/agsympo/documents/Sato.pdf)

**Key Insight:** The Tate twist ensures that cohomological operations such as Gysin maps, cup products with fundamental classes, and monodromy operators are compatible with weight filtrations. Without it, the graded pieces of the weight filtration would not carry pure Hodge structures of the correct weight.

**Prerequisites:** Etale cohomology, roots of unity, cyclotomic character, Hodge structures, monodromy

<!-- BENCHMARK_PROBLEM: In etale cohomology with l-adic coefficients, how is the Tate twist Z_l(1) defined? What Galois representation does it correspond to? -->

### Example: inertia group {#ecag-0293}

**Statement:** Define the inertia group in the context of ramification theory and explain its role in the theory of nearby cycles.

**Construction/Proof:** Let $K$ be a complete discretely valued field with residue field $k$ and let $\overline{K}$ be an algebraic closure. The **inertia group** $I$ is the kernel of the surjection

$$
\operatorname{Gal}(\overline{K}/K) \twoheadrightarrow \operatorname{Gal}(\overline{k}/k),

$$

i.e., $I$ consists of those automorphisms of $\overline{K}$ that act trivially on the residue field. There is an exact sequence

$$
1 \to I \to \operatorname{Gal}(\overline{K}/K) \to \operatorname{Gal}(\overline{k}/k) \to 1.

$$

The inertia group itself has a filtration by **ramification subgroups**: the wild inertia (or $p$-part) $P \subset I$ is the pro-$p$-Sylow subgroup (where $p = \operatorname{char}(k)$), and the tame inertia $I^t = I/P$ is the tame quotient. When $\operatorname{char}(k) = 0$, there is no wild ramification and $I = I^t$.

For a family $f : X \to S$ where $S = \operatorname{Spec}(\mathcal{O}_K)$, the nearby cycles functor $R\Psi$ produces sheaves on the special fiber $X_s$ equipped with a continuous action of $\operatorname{Gal}(\overline{K}/K)$. The key structure theorem states:

1. The action of $I$ on $R^n \Psi \mathbb{Q}_\ell$ is quasi-unipotent (Grothendieck's monodromy theorem).
2. After a finite extension of $K$ (corresponding to passing to a finite-index subgroup of $I$), the action becomes unipotent.
3. The tame inertia $I^t \cong \prod_{\ell \neq p} \mathbb{Z}_\ell$ acts through a single topological generator, whose action gives the monodromy operator.

In the complex-analytic setting, the inertia group corresponds to $\pi_1(D^*) \cong \mathbb{Z}$, the fundamental group of a punctured disk, whose generator gives the classical monodromy transformation.

Reference: [Ramification group (Wikipedia)](https://en.wikipedia.org/wiki/Ramification_group)

**Key Insight:** The inertia group captures the "local" Galois symmetry at a place of bad reduction. Its action on nearby cycles encodes monodromy, and Grothendieck's quasi-unipotence theorem ensures this action is always controlled enough to define a monodromy operator and weight filtration.

**Prerequisites:** Galois theory, discrete valuation rings, ramification theory, nearby cycles functor, $\ell$-adic sheaves

<!-- BENCHMARK_PROBLEM: Define the inertia group I for a complete discretely valued field K with residue field k. What is the relationship between I and the Galois groups of K and k? -->

### Example: Frobenius morphisms {#ecag-0294}

**Statement:** Define the Frobenius morphism in its various forms (absolute, relative, arithmetic, geometric) and describe its interaction with nearby cycles and weight filtrations.

**Construction/Proof:** Let $X$ be a scheme over $\mathbb{F}_q$ (or more generally over $\mathbb{F}_p$).

**Absolute Frobenius:** The absolute Frobenius $F_{\operatorname{abs}} : X \to X$ acts as the identity on the underlying topological space and as the $p$-th power map $a \mapsto a^p$ on the structure sheaf $\mathcal{O}_X$.

**Relative Frobenius:** If $X$ is an $S$-scheme where $S$ is an $\mathbb{F}_p$-scheme, the relative Frobenius $F_{X/S} : X \to X^{(p)}$ is defined by the Cartesian diagram

$$
X \xrightarrow{F_{X/S}} X^{(p)} \to X

$$

$$
\downarrow \qquad\qquad \downarrow \qquad \downarrow

$$

$$
S \xrightarrow{F_S} S = S

$$

where $X^{(p)} = X \times_{S, F_S} S$ is the base change of $X$ along the Frobenius of $S$.

**Arithmetic Frobenius:** For $X$ over $\mathbb{F}_q$, the arithmetic Frobenius $\operatorname{Frob}_q$ is the element of $\operatorname{Gal}(\overline{\mathbb{F}_q}/\mathbb{F}_q)$ given by $x \mapsto x^q$. It acts on etale cohomology $H^n_{\operatorname{et}}(X_{\overline{\mathbb{F}_q}}, \mathbb{Q}_\ell)$.

**Geometric Frobenius:** The geometric Frobenius is $\operatorname{Frob}_q^{-1}$, the inverse of the arithmetic Frobenius. The Weil conjectures (proved by Deligne) state that the eigenvalues of geometric Frobenius on $H^n_{\operatorname{et}}(X_{\overline{\mathbb{F}_q}}, \mathbb{Q}_\ell)$ for smooth projective $X$ are algebraic numbers with absolute value $q^{n/2}$ under every complex embedding (purity).

**Interaction with nearby cycles:** For a family $f : X \to S$ over a trait $S = \operatorname{Spec}(\mathcal{O}_K)$ with $K$ a local field of residue characteristic $p$, the nearby cycles $R\Psi$ carry commuting actions of:
1. The inertia group $I$ (monodromy).
2. The Frobenius $\operatorname{Frob}$ on the special fiber (from the Galois action on the geometric generic fiber).

The weight-monodromy conjecture (proved by Deligne for $\ell$-adic cohomology over equal characteristic local fields) asserts that the monodromy filtration and the weight filtration (defined via Frobenius eigenvalues) coincide up to a shift.

**Key Insight:** The Frobenius morphism provides an intrinsic "weight" measurement in positive characteristic: the absolute values of its eigenvalues on cohomology determine the weights, bridging arithmetic (eigenvalue magnitudes) and geometry (the weight filtration from the spectral sequence).

**Prerequisites:** Schemes over finite fields, etale cohomology, Weil conjectures, $\ell$-adic sheaves, nearby cycles

<!-- BENCHMARK_PROBLEM: For a smooth projective variety X over F_q, what does the Weil conjecture (Riemann hypothesis, proved by Deligne) say about the eigenvalues of geometric Frobenius acting on H^n_et(X_{F_q-bar}, Q_l)? -->

### Example: monodromy operators {#ecag-0295}

**Statement:** Define the monodromy operator $N$ in the context of nearby cycles and describe its interaction with the weight filtration.

**Construction/Proof:** Let $f : X \to D$ be a proper morphism from a smooth variety to a disk $D$ with smooth generic fiber. Let $D^* = D \setminus \{0\}$ be the punctured disk. The monodromy transformation $T$ is the automorphism of $H^n(X_t; \mathbb{Q})$ (for $t \in D^*$) induced by the generator of $\pi_1(D^*) \cong \mathbb{Z}$.

By the monodromy theorem, $T$ is quasi-unipotent: there exist positive integers $m$ and $k$ such that $(T^m - \operatorname{Id})^k = 0$. After a base change $s \mapsto s^m$, we may assume $T$ is unipotent. The **monodromy operator** (or **log monodromy**) is then

$$
N = \log(T) = (T - \operatorname{Id}) - \frac{1}{2}(T - \operatorname{Id})^2 + \frac{1}{3}(T - \operatorname{Id})^3 - \cdots,

$$

which is a well-defined nilpotent operator since $T$ is unipotent.

The monodromy operator $N$ determines a unique increasing filtration $M_\bullet$ on $H^n(X_t; \mathbb{Q})$, called the **monodromy filtration**, characterized by:
1. $N(M_k) \subset M_{k-2}$ (i.e., $N$ shifts the filtration by $-2$).
2. $N^k : \operatorname{Gr}_k^M \xrightarrow{\sim} \operatorname{Gr}_{-k}^M$ is an isomorphism for all $k \geq 0$.

The **monodromy weight conjecture** (proved in some cases) states that, when centered appropriately, this filtration coincides with the weight filtration coming from mixed Hodge theory.

At the level of nearby cycles sheaves, $N$ acts as a morphism $N : R^n \Psi \mathbb{Q} \to R^n \Psi \mathbb{Q}(-1)$ (with a Tate twist reflecting the weight shift).

Reference: [Achinger, Thesis, p.14](http://achinger.impan.pl/thesis.pdf)

**Key Insight:** The monodromy operator $N$ is the infinitesimal generator of the monodromy action and encodes how cycles in the generic fiber degenerate as they approach the special fiber. Its nilpotency order measures the "depth" of the degeneration, and the monodromy filtration it determines is the fundamental invariant of the singularity of the family.

**Prerequisites:** Monodromy theorem, nilpotent operators, nearby cycles, mixed Hodge structures, weight filtration

<!-- BENCHMARK_PROBLEM: Given a unipotent monodromy transformation T acting on H^n(X_t; Q), define the monodromy operator N. What are the two defining properties of the monodromy filtration M_* associated to N? -->

### Example: Milnor fibration, nearby cycles of a family $X\rightarrow D$, [reference](http://achinger.impan.pl/thesis.pdf) {#ecag-0296}

**Statement:** Compute the Milnor fiber and the nearby cycles sheaves for the family $X = \{(x_1, x_2, t) \mid x_1 x_2 = t, |t| < 1\} \to D$ given by $(x_1, x_2, t) \mapsto t$.

**Construction/Proof:** The definition of the Milnor fiber captures the idea of the "generic fiber near a singular point." For a family $f : X \to D$ and a point $x \in X_0$ (the special fiber), the Milnor fiber $F_x$ is the fiber of $f$ restricted to a small ball around $x$, taken over a nearby regular value. Equivalently, one can define it via base change to the universal covering $\widetilde{D^*} \to D^*$ of the punctured disk (see [Achinger, p.3](http://achinger.impan.pl/thesis.pdf)), which makes the construction canonical.

For the family $X = \{(x_1, x_2, t) \mid x_1 x_2 = t\} \to D$ mapping $(x_1, x_2, t) \mapsto t$:

The special fiber $X_0 = \{x_1 x_2 = 0\}$ consists of the two coordinate axes, meeting at the origin. The generic fiber $X_t$ for $t \neq 0$ is $\{x_1 x_2 = t\}$, which is a smooth hyperbola isomorphic to $\mathbb{C}^{\times}$.

By the intuition of nearby cycles, the Milnor fiber over the singular point $\operatorname{pt} = (0, 0, 0)$ is the generic fiber near that point: $\{x_1 x_2 = \epsilon\}$ for small $\epsilon \neq 0$, which is $\{(a, \epsilon/a) \mid a \in \mathbb{C}^{\times}\} \cong \mathbb{C}^{\times} \simeq S^1$.

This can be verified using the formal definition: the Milnor fiber over $\operatorname{pt}$ is

$$
F_{\operatorname{pt}} = \{(x_1, x_2, u) \mid |x_1|^2 + |x_2|^2 + |x_1 x_2|^2 < \epsilon, \ \exp(u) = x_1 x_2\}.

$$

The domain of $u$ is contractible (a half-plane in $\mathbb{C}$), so $F_{\operatorname{pt}}$ is a trivial $S^1$-fibration over a contractible base. Therefore

$$
F_{\operatorname{pt}} \simeq S^1.

$$

The nearby cycles sheaves $R^k \Psi \mathbb{Z}$ on $X_0$ are computed from the cohomology of the Milnor fibers at each point of $X_0$:

- At smooth points of $X_0$ (away from the origin), the family is locally trivial, so the Milnor fiber is a point and $R^k \Psi \mathbb{Z}$ has stalk $\mathbb{Z}$ for $k = 0$ and $0$ for $k > 0$.
- At the singular point $\operatorname{pt} = (0,0,0)$, the Milnor fiber is $S^1$, contributing $H^0(S^1) = \mathbb{Z}$ and $H^1(S^1) = \mathbb{Z}$.

Therefore the nearby cycles sheaves are:

$$
R^0 \Psi \mathbb{Z} \cong \mathbb{Z}_{X_0}, \qquad R^1 \Psi \mathbb{Z} \cong \mathbb{Z}_{\operatorname{pt}},

$$

where $\mathbb{Z}_{X_0}$ is the constant sheaf and $\mathbb{Z}_{\operatorname{pt}}$ is the skyscraper sheaf supported at the singular point.

**Key Insight:** The Milnor fiber detects the local topology of a degeneration: at smooth points of the special fiber the Milnor fiber is contractible (nothing interesting happens), while at singular points the Milnor fiber captures the vanishing cycle. For the ordinary double point $x_1 x_2 = t$, the Milnor fiber is $S^1$, and the single nontrivial cycle in $H^1(S^1)$ is the vanishing cycle that collapses as $t \to 0$.

**Prerequisites:** Milnor fibration, nearby cycles functor, skyscraper sheaves, vanishing cycles, ordinary double points

<!-- BENCHMARK_PROBLEM: For the family x_1 x_2 = t over a disk, what is the Milnor fiber over the singular point (0,0,0)? What are the nearby cycles sheaves R^0 Psi Z and R^1 Psi Z on the special fiber? -->

### Example: Dwork family of elliptic curves, need 'monodromy formula' {#ecag-0297}

**Statement:** Compute the monodromy action on $H^1(X_t; \mathbb{Z})$ for the Dwork family of elliptic curves

$$
f : X = \{(\epsilon, [x : y : z]) \in D \times \mathbb{P}^2_{\mathbb{C}} \mid \epsilon(x^3 + y^3 + z^3) = 3xyz\} \to D.

$$

**Construction/Proof:** The special fiber $X_0$ is defined by $3xyz = 0$, which is the union of the three coordinate lines $\{x = 0\}$, $\{y = 0\}$, $\{z = 0\}$ in $\mathbb{P}^2$. These three lines intersect pairwise at three distinct points:

$$
P_1 = [1 : 0 : 0], \quad P_2 = [0 : 1 : 0], \quad P_3 = [0 : 0 : 1].

$$

For generic $\epsilon \neq 0$, the fiber $X_\epsilon$ is a smooth elliptic curve with $H^1(X_\epsilon; \mathbb{Z}) \cong \mathbb{Z}^2$.

**Step 1: Nearby cycles sheaves.** At smooth points of $X_0$ (away from the $P_i$), the family is locally trivial, so $R^0 \Psi \mathbb{Z} \cong \mathbb{Z}$. At each node $P_i$, the singularity is locally an ordinary double point $x_1 x_2 = t$, so the Milnor fiber is $S^1$ and $R^1 \Psi \mathbb{Z}$ has stalk $\mathbb{Z}$ at $P_i$. Therefore:

$$
R^0 \Psi \mathbb{Z} \cong \mathbb{Z}_{X_0}, \qquad R^1 \Psi \mathbb{Z} \cong \bigoplus_{i=1}^{3} \mathbb{Z}_{P_i}.

$$

Higher nearby cycles vanish since $R^1 \Psi \mathbb{Z}$ is locally of rank at most 1.

**Step 2: Nearby cycles spectral sequence.** The $E_2$-page of the spectral sequence $H^p(X_0, R^q \Psi \mathbb{Z}) \Rightarrow H^{p+q}(X_t; \mathbb{Z})$ is:

| $q \setminus p$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $1$ | $H^0(X_0, R^1\Psi) = \mathbb{Z}^3$ | $0$ | $0$ |
| $0$ | $H^0(X_0, \mathbb{Z}) = \mathbb{Z}$ | $H^1(X_0, \mathbb{Z}) = \mathbb{Z}$ | $H^2(X_0, \mathbb{Z}) = \mathbb{Z}^3$ |

Here $H^1(X_0, \mathbb{Z}) = \mathbb{Z}$ (computed from the triangle of three $\mathbb{P}^1$'s: the cycle around the triangle generates $H^1$), and $H^2(X_0, \mathbb{Z}) = \mathbb{Z}^3$ (each $\mathbb{P}^1$ component contributes a fundamental class).

The only potentially nonzero differential is $d_2 : H^0(X_0, R^1 \Psi \mathbb{Z}) \to H^2(X_0, \mathbb{Z})$, i.e., $d_2 : \mathbb{Z}^3 \to \mathbb{Z}^3$.

Since the spectral sequence converges to $H^*(X_t; \mathbb{Z})$ with $H^0 = \mathbb{Z}$, $H^1 = \mathbb{Z}^2$, $H^2 = \mathbb{Z}$, we get the exact sequence:

$$
0 \to H^1(X_0, \mathbb{Z}) \xrightarrow{i} H^1(X_t, \mathbb{Z}) \xrightarrow{p} H^0(X_0, R^1\Psi\mathbb{Z}) \xrightarrow{d_2} H^2(X_0, \mathbb{Z}) \to H^2(X_t, \mathbb{Z}) \to 0

$$

$$
0 \to \mathbb{Z} \xrightarrow{i} \mathbb{Z}^2 \xrightarrow{p} \mathbb{Z}^3 \xrightarrow{d_2} \mathbb{Z}^3 \to \mathbb{Z} \to 0.

$$

From this, $\ker(d_2)$ has rank 1 (since $\operatorname{im}(p) = \ker(d_2)$ and $H^1(X_t)/\operatorname{im}(i) \cong \ker(d_2)$, which has rank $2 - 1 = 1$).

**Step 3: Monodromy computation.** The monodromy action of $\pi_1(D^*)$ on $R^k \Psi \mathbb{Z}$ is trivial for $k \geq 1$ (by the construction in [Achinger's thesis](http://achinger.impan.pl/thesis.pdf)). Choose a basis $\{e_1, e_2\}$ of $H^1(X_t; \mathbb{Z})$ where $e_1 = i(\text{generator of } H^1(X_0))$ and $e_2$ maps to a generator of $\ker(d_2) \subset H^0(X_0, R^1\Psi\mathbb{Z})$. Since monodromy acts trivially on $H^1(X_0)$ and on $R^1\Psi\mathbb{Z}$, the monodromy matrix has the form

$$
T = \begin{pmatrix} 1 & m \\ 0 & 1 \end{pmatrix}

$$

for some integer $m$ to be determined.

**Step 4: The monodromy formula.** By the monodromy formula ([Achinger](http://achinger.impan.pl/thesis.pdf)), there is a commutative diagram (up to sign):

$$
H^1(X_t, \mathbb{Z}) \xrightarrow{p} H^0(X_0, R^1\Psi\mathbb{Z})

$$

$$
\downarrow{1-T} \qquad\qquad\qquad \downarrow{\overline{\alpha}}

$$

$$
H^1(X_t, \mathbb{Z}) \xleftarrow{\quad i \quad} H^1(X_0, \mathbb{Z})

$$

where $\overline{\alpha}$ is the connecting homomorphism from the long exact sequence associated to

$$
0 \to \mathbb{Z}_{X_0} \to \bigoplus_{i=1}^{3} \mathbb{Z}_{L_i} \to R^1 \Psi \mathbb{Z} \cong \bigoplus_{i=1}^{3} \mathbb{Z}_{P_i} \to 0.

$$

Using Cech cohomology, one computes $\overline{\alpha} : H^0(X_0, R^1\Psi\mathbb{Z}) \to H^1(X_0, \mathbb{Z})$ and finds that $\overline{\alpha}([P_i]) = 1$ (the generator of $H^1(X_0, \mathbb{Z}) = \mathbb{Z}$) for each $i$.

**Step 5: Exploiting symmetry.** The $\mathbb{Z}/3\mathbb{Z}$-action on $X$ by cyclic permutation of coordinates preserves all the structures. The map $p$ is equivariant, so $\ker(d_2) = \operatorname{im}(p)$ is $\mathbb{Z}/3\mathbb{Z}$-invariant. Since $\operatorname{coker}(p) \cong \mathbb{Z}^2$ is torsion-free, the image $\operatorname{im}(p)$ is generated by the invariant element $[P_1] + [P_2] + [P_3]$. Therefore:

$$
\overline{\alpha}([P_1] + [P_2] + [P_3]) = 3 \in H^1(X_0, \mathbb{Z}) \cong \mathbb{Z}.

$$

From the commutative diagram, $(1-T)(e_2) = \pm m \cdot e_1$ and $\overline{\alpha}(p(e_2)) = 3 \cdot e_1$, giving $m = \pm 3$. Fixing orientations, the monodromy action is:

$$
T = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}.

$$

**Key Insight:** The monodromy index $m = 3$ reflects the three nodes of the special fiber. The $\mathbb{Z}/3\mathbb{Z}$-symmetry of the Dwork family constrains the image of $p$ to be generated by the symmetric combination $[P_1] + [P_2] + [P_3]$, which makes the monodromy computation tractable without explicitly constructing the vanishing cycles.

**Prerequisites:** Nearby cycles spectral sequence, monodromy formula, Cech cohomology, ordinary double points, Dwork families

<!-- BENCHMARK_PROBLEM: For the Dwork family of elliptic curves epsilon(x^3+y^3+z^3) = 3xyz, what is the monodromy matrix T acting on H^1(X_t; Z) with respect to a suitable basis? What integer m appears in the upper-right entry? -->

### Remark {#ecag-0298}

Every irreducible complex representation of an abelian group is 1-dimensional. This is a direct consequence of Schur's lemma: if $\rho : G \to \operatorname{GL}(V)$ is irreducible and $G$ is abelian, then every $\rho(g)$ commutes with all of $\rho(G)$, hence by Schur's lemma $\rho(g)$ is a scalar for each $g$. Thus every subspace of $V$ is invariant, forcing $\dim V = 1$.

However, if the group is not compact (e.g., $\mathbb{Z}$, or an infinite discrete group), then representations need not be semisimple (i.e., need not decompose as a direct sum of irreducibles). For example, the representation $\mathbb{Z} \to \operatorname{GL}_2(\mathbb{C})$ given by

$$
1 \mapsto \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}

$$

is indecomposable but not irreducible: it has an invariant subspace spanned by $(1, 0)^T$ but does not split as a direct sum of 1-dimensional representations.

This is precisely the situation encountered with monodromy: the monodromy representation of $\pi_1(D^*) \cong \mathbb{Z}$ on $H^n(X_t; \mathbb{Q})$ is typically not semisimple when the special fiber is singular. The failure of semisimplicity is measured by the monodromy operator $N = \log(T)$, and the monodromy filtration encodes the Jordan block structure of $T$.

For compact groups (including finite groups), every representation is semisimple by Maschke's theorem (finite case) or the Peter-Weyl theorem (compact case), so this phenomenon does not arise.

<!-- BENCHMARK_PROBLEM: Give an example of a 2-dimensional representation of Z over C that is indecomposable but not irreducible. Why does this not contradict the fact that every irreducible representation of an abelian group is 1-dimensional? -->
