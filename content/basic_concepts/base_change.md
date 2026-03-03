---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/base_change.tex
---

## Base-change

### Example: Reduced scheme but not geometrically reduced {#ecag-0005}

**Statement:** Let $k = \mathbf{F}_p(T)$ and $K = \mathbf{F}_p(T^{1/p})$. Then $\operatorname{Spec}(K)$ is a reduced $k$-scheme, but it is not geometrically reduced: the base change $\operatorname{Spec}(K \otimes_k K)$ is not reduced.

**Construction/Proof:** The field extension $K/k$ is purely inseparable of degree $p$, since $T^{1/p}$ satisfies the minimal polynomial $X^p - T \in k[X]$, which is irreducible over $k$ (by Eisenstein's criterion at the prime $T$ in $\mathbf{F}_p[T]$, then passing to the fraction field). In particular, $K$ is a field, so $\operatorname{Spec}(K)$ is a single reduced point.

Now consider the tensor product $K \otimes_k K$. We have

$$
K \otimes_k K \cong K[X]/(X^p - T) \cong K[X]/((X - T^{1/p})^p)

$$

since $X^p - T = (X - T^{1/p})^p$ in $K[X]$ (we are in characteristic $p$). The element

$$
\alpha = 1 \otimes T^{1/p} - T^{1/p} \otimes 1

$$

corresponds to the residue class of $X - T^{1/p}$ in $K[X]/((X - T^{1/p})^p)$. This element is nonzero (it is not the zero class since $X - T^{1/p}$ is not divisible by $(X - T^{1/p})^p$), but

$$
\alpha^p = (1 \otimes T^{1/p} - T^{1/p} \otimes 1)^p = 1 \otimes T - T \otimes 1 = 0

$$

since $T \in k$ and $1 \otimes t = t \otimes 1$ for all $t \in k$. Therefore $\alpha$ is a nonzero nilpotent element in $K \otimes_k K$, so $\operatorname{Spec}(K \otimes_k K)$ is not reduced.

**Key Insight:** A scheme over an imperfect field $k$ can be reduced without being geometrically reduced. The obstruction is precisely that $k^{1/p} \not\subseteq k$, so purely inseparable extensions create nilpotents upon base change.

**Prerequisites:** Purely inseparable field extensions, tensor products of algebras, geometric reducedness, Frobenius endomorphism in characteristic $p$

<!-- BENCHMARK_PROBLEM: Let $k = \mathbf{F}_p(T)$ and $K = \mathbf{F}_p(T^{1/p})$. Explicitly exhibit a nonzero nilpotent element in $K \otimes_k K$ and prove that its $p$-th power is zero. What is the nilpotency index of this element? -->

## Push-forward and pull-back

### Example: Hartshorne $\operatorname{III}.12.4$ {#ecag-0006}

**Statement:** Let $Y$ be an integral scheme of finite type over an algebraically closed field $k$, and let $f : X \to Y$ be a flat projective morphism whose fibres are integral schemes. Let $L, M$ be line bundles on $X$ such that $L_y \cong M_y$ on each fibre $X_y$. Then there exists a line bundle $N$ on $Y$ such that

$$
L \cong M \otimes f^* N.

$$

**Construction/Proof:** Define $\mathscr{F} = L \otimes M^{-1}$. By hypothesis, $\mathscr{F}_y \cong \mathcal{O}_{X_y}$ for every $y \in Y$, so $h^0(X_y, \mathscr{F}_y) = 1$ for all $y$.

Step 1: By Grauert's theorem (Hartshorne III.12.9), since $f$ is a flat projective morphism between Noetherian schemes and $\mathscr{F}$ is a coherent sheaf flat over $Y$, and the function $y \mapsto h^0(X_y, \mathscr{F}_y) = 1$ is constant, the direct image $f_* \mathscr{F}$ is a locally free sheaf of rank $h^0(X_y, \mathscr{F}_y) = 1$. Since each fibre $X_y$ is integral (hence connected), a section of a trivial line bundle on a connected scheme that generates a rank-1 space must generate the bundle. Thus $f_* \mathscr{F}$ is a line bundle. Set $N = f_* \mathscr{F}$.

Step 2: The base change map

$$
f_* \mathscr{F} \otimes k(y) \to H^0(X_y, \mathscr{F}_y)

$$

is an isomorphism by cohomology and base change (since $h^0$ is constant and $Y$ is integral). Since $\mathscr{F}_y \cong \mathcal{O}_{X_y}$, the fibre $\mathscr{F}_y$ is globally generated. This means the evaluation map

$$
f^* f_* \mathscr{F} \to \mathscr{F}

$$

is surjective on each fibre. But $f^* f_* \mathscr{F}$ and $\mathscr{F}$ are both line bundles on $X$ (since $f^* N$ is a line bundle when $N$ is), so a surjection between line bundles is an isomorphism. Therefore

$$
\mathscr{F} \cong f^* N = f^* f_* \mathscr{F},

$$

which gives $L \otimes M^{-1} \cong f^* N$, i.e., $L \cong M \otimes f^* N$.

**Key Insight:** The connectedness of fibres guarantees that the push-forward has rank exactly 1 (rather than higher rank), reducing the problem to showing that a surjection between line bundles is an isomorphism.

**Prerequisites:** Grauert's theorem, cohomology and base change, flat projective morphisms, line bundles, integral schemes

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a flat projective morphism with integral fibres over an integral scheme $Y$ of finite type over an algebraically closed field. If $L$ and $M$ are line bundles on $X$ with $L_y \cong M_y$ for all $y \in Y$, prove that $L \cong M \otimes f^* N$ for some line bundle $N$ on $Y$. Where exactly does the integrality of the fibres enter the proof? -->

### Remark: $f_*\mathcal{O}_{X}\cong \mathcal{O}_{Y}$ {#ecag-0007}

Under the hypotheses of the previous example (flat projective morphism $f : X \to Y$ with integral fibres, $Y$ integral of finite type over an algebraically closed field $k$), we have $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

To see this, apply the same method with $\mathscr{F} = \mathcal{O}_X$. Since each fibre $X_y$ is integral, $H^0(X_y, \mathcal{O}_{X_y}) \cong k(y)$ (the fibre is connected and reduced). By Grauert's theorem, $f_* \mathcal{O}_X$ is locally free of rank 1. On the stalk level at $y \in Y$, the natural map

$$
\mathcal{O}_{Y,y} \to (f_* \mathcal{O}_X)_y

$$

is injective (since $f_* \mathcal{O}_X$ is locally free and $f^\# : \mathcal{O}_Y \to f_* \mathcal{O}_X$ is a ring map sending $1$ to $1$). Since both sides are free $\mathcal{O}_{Y,y}$-modules of rank 1, this injection is an isomorphism. Therefore $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a flat projective morphism with integral fibres, $Y$ an integral scheme of finite type over an algebraically closed field. Prove that $f_* \mathcal{O}_X \cong \mathcal{O}_Y$. Which specific property of the fibres guarantees the rank is exactly 1? -->

### Example: Fibres being integral is necessary, actually flatness matters {#ecag-0008}

**Statement:** The conclusion $f_* \mathcal{O}_X \cong \mathcal{O}_Y$ can fail if the morphism is not flat, even when $X$ is reduced and fibres are connected. Specifically, consider the morphism

$$
f : X = \operatorname{Spec}(k[x,y]/(x^2, xy)) \to Y = \operatorname{Spec}(k[y])

$$

induced by $k[y] \to k[x,y]/(x^2, xy)$, $y \mapsto y$. Then $f_* \mathcal{O}_X \not\cong \mathcal{O}_Y$.

**Construction/Proof:** The ring $A = k[x,y]/(x^2, xy)$ has $x$ as a zero divisor (since $x \cdot x = x^2 = 0$ and $x \cdot y = xy = 0$). The morphism is finite (hence projective) and $Y$ is a regular Noetherian scheme.

Flatness fails: As a $k[y]$-module, $A \cong k[y] \oplus k \cdot x$, where $y$ acts on $x$ by $y \cdot x = 0$. The element $x \in A$ is annihilated by $y \in k[y]$, so $A$ is not torsion-free over $k[y]$. Since $k[y]$ is a PID, torsion-free is equivalent to flat, so $f$ is not flat.

We have $f_* \mathcal{O}_X = \widetilde{A}$ as a quasi-coherent sheaf on $Y = \operatorname{Spec}(k[y])$. The global sections are $\Gamma(Y, f_* \mathcal{O}_X) = A = k[y] \oplus k \cdot x$. This is a rank-2 $k[y]$-module (not free, since it has torsion), so $f_* \mathcal{O}_X \not\cong \mathcal{O}_Y$.

The contrast with the previous results is instructive: conditions (1) $X$ reduced with connected fibres, versus (2) $f$ flat projective with integral fibres. Condition (2) implies $f_* \mathcal{O}_X \cong \mathcal{O}_Y$, but condition (1) does not suffice.

**Key Insight:** Flatness is essential for Grauert's theorem and cohomology-and-base-change to apply. A non-flat morphism can have connected fibres yet still fail to satisfy $f_* \mathcal{O}_X \cong \mathcal{O}_Y$ because the push-forward sheaf can carry torsion.

**Prerequisites:** Flatness of modules over a PID, finite morphisms, structure sheaf push-forward, Grauert's theorem hypotheses

<!-- BENCHMARK_PROBLEM: Show that the morphism $\operatorname{Spec}(k[x,y]/(x^2, xy)) \to \operatorname{Spec}(k[y])$ given by $y \mapsto y$ is not flat, and compute $f_* \mathcal{O}_X$ explicitly as a $k[y]$-module. Is it locally free? -->

### Example: Push-forward of a coherent sheaf might not be coherent {#ecag-0009}

**Statement:** Let $f : X = \operatorname{Spec}(k(x)) \to Y = \operatorname{Spec}(k)$ be the morphism induced by the inclusion $k \hookrightarrow k(x)$. Then $f_* \mathcal{O}_X$ is not a coherent sheaf on $Y$.

**Construction/Proof:** The push-forward $f_* \mathcal{O}_X$ is the quasi-coherent sheaf on $\operatorname{Spec}(k)$ associated to the $k$-module $k(x)$. A coherent sheaf on $\operatorname{Spec}(k)$ corresponds to a finite-dimensional $k$-vector space. However, $k(x)$ is infinite-dimensional over $k$ (the elements $1, x, x^2, \ldots$ are linearly independent). Therefore $f_* \mathcal{O}_X$ is not coherent.

Note that the morphism $f$ is not proper: $\operatorname{Spec}(k(x))$ is not proper over $\operatorname{Spec}(k)$. By the proper direct image theorem (EGA III), if $f$ were proper, the push-forward of any coherent sheaf would be coherent. This example shows that properness is a necessary hypothesis.

**Key Insight:** The push-forward $f_*$ preserves coherence only under properness assumptions. For a non-proper morphism, even the push-forward of the structure sheaf can fail to be coherent, since global sections can form an infinite-dimensional vector space.

**Prerequisites:** Coherent sheaves, proper morphisms, proper direct image theorem

<!-- BENCHMARK_PROBLEM: Let $k$ be a field and $f : \operatorname{Spec}(k(x)) \to \operatorname{Spec}(k)$ the natural morphism. Prove that $f_* \mathcal{O}_X$ is not coherent on $\operatorname{Spec}(k)$, and identify which hypothesis of the proper direct image theorem fails. -->

### Example: Push-forward of a quasi-coherent sheaf might not be quasi-coherent {#ecag-0010}

**Statement:** Let $f : X = \coprod_{i=1}^{\infty} \operatorname{Spec}(\mathbb{Z}) \to S = \operatorname{Spec}(\mathbb{Z})$ be the morphism given by the identity on each component. Then $f_* \mathcal{O}_X$ is not a quasi-coherent sheaf on $S$.

**Construction/Proof:** For any open set $U \subseteq S$, we have

$$
f_* \mathcal{O}_X(U) = \mathcal{O}_X(f^{-1}(U)) = \prod_{i=1}^{\infty} \mathcal{O}_S(U).

$$

For a quasi-coherent sheaf $\mathscr{F}$ on $S = \operatorname{Spec}(\mathbb{Z})$, one must have $\mathscr{F}(D(a)) \cong \mathscr{F}(S) \otimes_{\mathbb{Z}} \mathbb{Z}[1/a]$ for every basic open $D(a)$. We check this fails for $a = 2$.

We have $f_* \mathcal{O}_X(S) = \prod_{i=1}^{\infty} \mathbb{Z}$ and $f_* \mathcal{O}_X(D(2)) = \prod_{i=1}^{\infty} \mathbb{Z}[1/2]$. If $f_* \mathcal{O}_X$ were quasi-coherent, the natural map

$$
\left(\prod_{i=1}^{\infty} \mathbb{Z}\right) \otimes_{\mathbb{Z}} \mathbb{Z}[1/2] \to \prod_{i=1}^{\infty} \mathbb{Z}[1/2]

$$

would be an isomorphism. However, the image of the left-hand side consists of sequences of elements in $\mathbb{Z}[1/2]$ with a uniform bound on the power of $2$ in the denominator: each element of $\left(\prod_i \mathbb{Z}\right) \otimes_{\mathbb{Z}} \mathbb{Z}[1/2]$ can be written as $(a_i)_i \otimes 1/2^M$ for some fixed $M$, giving entries $a_i / 2^M$. But the right-hand side contains sequences like $(1/2, 1/4, 1/8, \ldots, 1/2^n, \ldots)$ where the denominators grow without bound. Such a sequence is not in the image, so the map is not surjective. Hence $f_* \mathcal{O}_X$ is not quasi-coherent.

As a second, simpler example of a non-quasi-coherent sheaf: on $\mathbb{A}_k^1 = \operatorname{Spec}(k[t])$, define a presheaf by

$$
\mathscr{F}(U) = \begin{cases} \mathcal{O}_X(U) & \text{if } 0 \notin U, \\ 0 & \text{if } 0 \in U. \end{cases}

$$

This is a sheaf (restriction maps and gluing are easily verified). We have $\mathscr{F}(\mathbb{A}_k^1) = 0$ since $0 \in \mathbb{A}_k^1$, but $\mathscr{F}$ is not the zero sheaf (it has nonzero sections on opens not containing $0$). A quasi-coherent sheaf with zero global sections on an affine scheme must be the zero sheaf, so $\mathscr{F}$ is not quasi-coherent.

**Key Insight:** Quasi-coherence of $f_* \mathscr{F}$ requires conditions on $f$: for instance, $f$ quasi-compact and quasi-separated suffices. The infinite coproduct morphism fails quasi-compactness, and the resulting infinite product of rings does not commute with localization.

**Prerequisites:** Quasi-coherent sheaves, localization and tensor products, quasi-compact and quasi-separated morphisms, infinite products of rings

<!-- BENCHMARK_PROBLEM: Let $f : \coprod_{i=1}^{\infty} \operatorname{Spec}(\mathbb{Z}) \to \operatorname{Spec}(\mathbb{Z})$ be the fold map. Exhibit an explicit element of $\prod_{i=1}^{\infty} \mathbb{Z}[1/2]$ that is not in the image of $\left(\prod_{i=1}^{\infty} \mathbb{Z}\right) \otimes_{\mathbb{Z}} \mathbb{Z}[1/2]$, and explain why this shows $f_* \mathcal{O}_X$ is not quasi-coherent. -->

### Example: Push-forward might have different cohomology {#ecag-0011}

**Statement:** Let $f : \mathbb{P}_k^1 \to \operatorname{Spec}(k)$ be the structure morphism. Then for $\mathscr{F} = \mathcal{O}_{\mathbb{P}_k^1}(-2)$, we have

$$
H^1(\operatorname{Spec}(k), f_* \mathscr{F}) = 0, \quad \text{but} \quad H^1(\mathbb{P}_k^1, \mathscr{F}) \neq 0.

$$

In particular, $H^i(X, \mathscr{F}) \neq H^i(Y, f_* \mathscr{F})$ in general when $f$ is not affine.

**Construction/Proof:** Step 1: Compute $f_* \mathcal{O}_{\mathbb{P}_k^1}(-2)$. Since $H^0(\mathbb{P}_k^1, \mathcal{O}(-2)) = 0$ (a line bundle of negative degree on $\mathbb{P}^1$ has no nonzero global sections), and $f_*$ on a morphism to $\operatorname{Spec}(k)$ just takes global sections, we get $f_* \mathcal{O}_{\mathbb{P}_k^1}(-2) = 0$ as a sheaf on $\operatorname{Spec}(k)$. Therefore

$$
H^1(\operatorname{Spec}(k), f_* \mathcal{O}_{\mathbb{P}_k^1}(-2)) = 0.

$$

Step 2: Compute $H^1(\mathbb{P}_k^1, \mathcal{O}(-2))$. By Serre duality on $\mathbb{P}_k^1$, with $\omega_{\mathbb{P}^1} \cong \mathcal{O}(-2)$, we have

$$
H^1(\mathbb{P}_k^1, \mathcal{O}(-2)) \cong H^0(\mathbb{P}_k^1, \mathcal{O})^\vee \cong k^\vee \cong k \neq 0.

$$

Alternatively, using the standard Cech computation with the cover $U_0 = D_+(x)$, $U_1 = D_+(y)$, one can identify $H^1(\mathbb{P}_k^1, \mathcal{O}(-2))$ with the $k$-vector space spanned by $x^{-1} y^{-1}$, which is 1-dimensional.

Step 3: This discrepancy arises because $f$ is not affine. For an affine morphism $f : X \to Y$, the Leray spectral sequence degenerates and gives $H^i(X, \mathscr{F}) \cong H^i(Y, f_* \mathscr{F})$ for all $i$. The structure morphism $\mathbb{P}_k^1 \to \operatorname{Spec}(k)$ is projective but not affine, so this identity can fail.

**Key Insight:** The isomorphism $H^i(X, \mathscr{F}) \cong H^i(Y, f_* \mathscr{F})$ holds when $f$ is affine (by degeneration of the Leray spectral sequence at $E_2$), but fails for non-affine morphisms because higher direct images $R^i f_* \mathscr{F}$ can be nonzero.

**Prerequisites:** Cohomology of line bundles on $\mathbb{P}^1$, Serre duality, Leray spectral sequence, affine morphisms

<!-- BENCHMARK_PROBLEM: Let $f : \mathbb{P}_k^1 \to \operatorname{Spec}(k)$ be the structure morphism. Compute $H^1(\operatorname{Spec}(k), f_* \mathcal{O}_{\mathbb{P}_k^1}(-2))$ and $H^1(\mathbb{P}_k^1, \mathcal{O}_{\mathbb{P}_k^1}(-2))$ separately, and explain why they differ. What property of $f$ would guarantee they are equal? -->

### Remark: Push-forward from a noetherian scheme {#ecag-0012}

If $f : X \to Y$ is a morphism with $X$ Noetherian, then the push-forward of a quasi-coherent sheaf is quasi-coherent. More precisely:

- If $f : X \to Y$ is a morphism of schemes with $X$ Noetherian (or more generally, $f$ quasi-compact and quasi-separated), then for any quasi-coherent sheaf $\mathscr{F}$ on $X$, the direct image $f_* \mathscr{F}$ is quasi-coherent on $Y$.

- If moreover $X$ is separated and Noetherian, then Cech cohomology agrees with derived functor cohomology: for any quasi-coherent sheaf $\mathscr{F}$ on $X$ and any open affine cover $\mathfrak{U}$ of $X$,

$$
\check{H}^p(\mathfrak{U}, \mathscr{F}) = H^p(X, \mathscr{F})

$$

for all $p \geq 0$. This follows from Leray's theorem: on a separated Noetherian scheme, intersections of affine opens are affine, so affine opens form a Leray cover for quasi-coherent sheaves.

<!-- BENCHMARK_PROBLEM: Let $X$ be a separated Noetherian scheme and $\mathscr{F}$ a quasi-coherent sheaf on $X$. Why does Cech cohomology with respect to an affine cover compute the derived functor cohomology? State the precise hypotheses needed. -->

### Example: Proper push-forward v.s. finite flat push-forward {#ecag-0013}

**Statement:** Several fundamental results govern when direct images preserve finiteness properties. This example collects key facts and contrasting cases:

(a) (EGA III / Proper direct image theorem) If $f : X \to Y$ is a proper morphism of Noetherian schemes and $\mathscr{F}$ is a coherent sheaf on $X$, then all higher direct images $R^i f_* \mathscr{F}$ are coherent on $Y$.

(b) Properness is essential: the morphism $\operatorname{Spec}(k(x)) \to \operatorname{Spec}(k)$ maps a point to a point topologically, but $f_* \mathcal{O}_X = k(x)$ is infinite-dimensional over $k$, hence not coherent. The morphism fails to be proper.

(c) If $f : X \to Y$ is a finite morphism, then $f_* \mathcal{O}_X$ is locally free if and only if $f$ is flat.

(d) Any surjective morphism $f : X \to Y$ with $Y$ a regular one-dimensional scheme (e.g., a smooth curve) is automatically flat.

(e) (Miracle flatness theorem) If $f : X \to Y$ is a morphism of finite type between Noetherian local rings with $Y$ regular, $X$ Cohen--Macaulay, and $\dim X = \dim Y + \dim(\text{fibre})$, then $f$ is flat.

**Construction/Proof:** For (a), the key input is the cohomological finiteness for proper morphisms, proved using Chow's lemma to reduce to the projective case, then using the computation of cohomology of coherent sheaves on projective space.

For (b), $\operatorname{Spec}(k(x))$ is not of finite type over $k$ (the ring $k(x)$ is not a finitely generated $k$-algebra), hence certainly not proper.

For (c), the forward direction: if $f$ is flat and finite, then $f_* \mathcal{O}_X$ is a coherent $\mathcal{O}_Y$-module (by (a), since finite implies proper) that is flat, hence locally free (a coherent flat module over a Noetherian local ring is free). The converse: if $f_* \mathcal{O}_X$ is locally free, then it is flat as an $\mathcal{O}_Y$-module, and $f$ being affine means flatness of $f$ is equivalent to flatness of $f_* \mathcal{O}_X$.

For (d), over a regular one-dimensional local ring (i.e., a DVR), every torsion-free module is flat. A surjective morphism to an integral curve has torsion-free push-forward (the generic fibre is nonempty by surjectivity), hence $f_* \mathcal{O}_X$ is flat.

For (e), this is a consequence of the dimension formula and the local criterion for flatness.

**Key Insight:** Properness, flatness, and finiteness interact in subtle ways to control when push-forwards behave well. The miracle flatness theorem provides a powerful criterion: correct fiber dimension plus Cohen--Macaulayness automatically implies flatness over a regular base.

**Prerequisites:** Proper direct image theorem, finite morphisms, flatness, Cohen--Macaulay rings, miracle flatness theorem, DVRs

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a finite morphism of Noetherian schemes. Prove that $f_* \mathcal{O}_X$ is locally free if and only if $f$ is flat. Where does the finiteness of $f$ enter each direction of the proof? -->

### Example: Push-forward of a trivial bundle might not be trivial {#ecag-0014}

**Statement:** Let $f : \mathbb{P}^1 \to \mathbb{P}^1$ be the degree-2 map $[x, y] \mapsto [x^2, y^2]$. Then $f_* \mathcal{O}_{\mathbb{P}^1}$ is a rank-2 vector bundle on $\mathbb{P}^1$ that is not trivial. Specifically,

$$
f_* \mathcal{O}_{\mathbb{P}^1} \cong \mathcal{O}_{\mathbb{P}^1} \oplus \mathcal{O}_{\mathbb{P}^1}(-1).

$$

**Construction/Proof:** The morphism $f$ is finite and flat of degree 2, so $f_* \mathcal{O}_{\mathbb{P}^1}$ is a locally free sheaf of rank 2 on $\mathbb{P}^1$. By Grothendieck's theorem, every vector bundle on $\mathbb{P}^1$ splits as a direct sum of line bundles:

$$
f_* \mathcal{O}_{\mathbb{P}^1} \cong \mathcal{O}_{\mathbb{P}^1}(a) \oplus \mathcal{O}_{\mathbb{P}^1}(b)

$$

for some $a, b \in \mathbb{Z}$. We determine $a$ and $b$ using the projection formula. For any $n \in \mathbb{Z}$:

$$
H^0(\mathbb{P}^1, \mathcal{O}(n) \otimes f_* \mathcal{O}_{\mathbb{P}^1}) \cong H^0(\mathbb{P}^1, f^* \mathcal{O}(n) \otimes \mathcal{O}_{\mathbb{P}^1}) = H^0(\mathbb{P}^1, \mathcal{O}(2n))

$$

since $f^* \mathcal{O}(1) \cong \mathcal{O}(2)$ (pulling back along a degree-2 map doubles the degree). The left-hand side equals $h^0(\mathcal{O}(n+a)) + h^0(\mathcal{O}(n+b))$, and the right-hand side is $h^0(\mathcal{O}(2n)) = \max(2n+1, 0)$.

For $n = 0$: $h^0(\mathcal{O}(a)) + h^0(\mathcal{O}(b)) = h^0(\mathcal{O}(0)) = 1$.
For $n = -1$: $h^0(\mathcal{O}(a-1)) + h^0(\mathcal{O}(b-1)) = h^0(\mathcal{O}(-2)) = 0$.

From $n = -1$, both $a - 1 < 0$ and $b - 1 < 0$, so $a \leq 0$ and $b \leq 0$. From $n = 0$, exactly one of $h^0(\mathcal{O}(a)), h^0(\mathcal{O}(b))$ is nonzero, so exactly one of $a, b$ is $\geq 0$. Combined with $a, b \leq 0$, one must be $0$ and the other must satisfy $h^0(\mathcal{O}(b)) = 0$, i.e., $b < 0$.

For $n = 1$: $h^0(\mathcal{O}(1)) + h^0(\mathcal{O}(1+b)) = h^0(\mathcal{O}(2)) = 3$, giving $2 + h^0(\mathcal{O}(1+b)) = 3$, so $h^0(\mathcal{O}(1+b)) = 1$, hence $b = -1$.

Therefore $f_* \mathcal{O}_{\mathbb{P}^1} \cong \mathcal{O}_{\mathbb{P}^1} \oplus \mathcal{O}_{\mathbb{P}^1}(-1)$.

**Key Insight:** Even though $\mathcal{O}_{\mathbb{P}^1}$ is the trivial bundle, its push-forward under a finite map need not be trivial. Grothendieck's splitting theorem reduces the problem to computing dimensions of global sections, which the projection formula translates to cohomology computations on the source.

**Prerequisites:** Grothendieck's splitting theorem for vector bundles on $\mathbb{P}^1$, projection formula, finite flat morphisms, cohomology of line bundles on $\mathbb{P}^1$

<!-- BENCHMARK_PROBLEM: Let $f : \mathbb{P}^1 \to \mathbb{P}^1$ be the map $[x,y] \mapsto [x^2, y^2]$. Using the projection formula and Grothendieck's splitting theorem, determine $f_* \mathcal{O}_{\mathbb{P}^1}$ as a direct sum of line bundles. -->

### Remark: Good things happen sometimes {#ecag-0015}

In some special but important situations, the push-forward of a skyscraper-type sheaf decomposes simply. Specifically, let $k$ be algebraically closed and $f : X \to Y$ a finite morphism between smooth projective curves. For an effective divisor $D = \sum n_i p_i$ on $X$, define $f_* D = \sum n_i f(p_i)$ as a divisor on $Y$. Then

$$
f_* \mathcal{O}_D \cong \mathcal{O}_{f_* D}.

$$

Here $\mathcal{O}_D = \mathcal{O}_X / \mathcal{O}_X(-D)$ is the structure sheaf of the subscheme defined by $D$. This is a skyscraper sheaf supported on the points $p_i$. Since $f$ is finite, $f_*$ on skyscraper sheaves simply relocates the stalks: the stalk of $f_* \mathcal{O}_D$ at $q \in Y$ is the direct sum of the stalks of $\mathcal{O}_D$ at the points $p_i$ mapping to $q$. Each such stalk is $\mathcal{O}_{X, p_i} / \mathfrak{m}_{p_i}^{n_i} \cong k[t]/(t^{n_i})$, which is the same as the stalk of $\mathcal{O}_{f_* D}$ at $f(p_i)$. Over an algebraically closed field, distinct points do not interact, giving the direct sum decomposition.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a finite morphism of smooth projective curves over an algebraically closed field, and let $D = p_1 + p_2$ be a reduced divisor on $X$ with $f(p_1) \neq f(p_2)$. Verify explicitly that $f_* \mathcal{O}_D \cong \mathcal{O}_{f(p_1)} \oplus \mathcal{O}_{f(p_2)}$. -->

### Example: $f^{*}f_{*}\mathscr{F}$ and $f_{*}f^{*}\mathscr{G}$ {#ecag-0016}

**Statement:** For a morphism $f : X \to Y$ and sheaves $\mathscr{F}$ on $X$, $\mathscr{G}$ on $Y$, there are natural adjunction maps

$$
\varepsilon : f^* f_* \mathscr{F} \to \mathscr{F} \quad \text{(counit)}

$$

$$
\eta : \mathscr{G} \to f_* f^* \mathscr{G} \quad \text{(unit)}

$$

These maps are made explicit in the affine case and in the case $Y = \operatorname{Spec}(k)$.

**Construction/Proof:**

*Affine case.* Let $f : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ correspond to a ring map $\varphi : B \to A$. Let $M$ be an $A$-module and $N$ a $B$-module. Denote by $M_B$ the $B$-module obtained from $M$ by restriction of scalars via $\varphi$.

Then $f_* \widetilde{M} = \widetilde{M_B}$ and $f^* f_* \widetilde{M} = \widetilde{A \otimes_B M_B}$. The counit is induced by the $A$-module map

$$
A \otimes_B M_B \to M, \quad a \otimes m \mapsto a \cdot m.

$$

This is the multiplication map. It is surjective if $M$ is generated by the image of $M_B$ (which is all of $M$ as a set), so the counit is always surjective when $A$ is generated by $1$ over $B$ (i.e., $\varphi$ is surjective). In general it need not be injective: the tensor product is over $B$, not over $A$, so elements $a_1 \otimes m_1 + a_2 \otimes m_2$ may collapse non-trivially.

For the unit: $f^* \widetilde{N} = \widetilde{A \otimes_B N}$ and $f_* f^* \widetilde{N} = \widetilde{(A \otimes_B N)_B}$. The unit is

$$
N \to (A \otimes_B N)_B, \quad n \mapsto 1 \otimes n.

$$

This is injective if $\varphi : B \to A$ is faithfully flat (since then $B \to A$ detects zero).

*Degenerate case: $Y = \operatorname{Spec}(k)$.* Let $\mathscr{F}$ be a coherent sheaf on $X$.

Then $f_* \mathscr{F} = H^0(X, \mathscr{F})$ (a $k$-vector space), and

$$
f^* f_* \mathscr{F} = \mathcal{O}_X \otimes_k H^0(X, \mathscr{F}) \cong \mathcal{O}_X^{\oplus h^0(X, \mathscr{F})}.

$$

The counit $\mathcal{O}_X \otimes_k H^0(X, \mathscr{F}) \to \mathscr{F}$ is the evaluation map: it sends $g \otimes s$ to $g \cdot s$ where $s$ is a global section of $\mathscr{F}$ and $g$ is a local function. This map is surjective precisely when $\mathscr{F}$ is globally generated.

For a finite-dimensional $k$-vector space $V$ (i.e., a coherent sheaf on $\operatorname{Spec}(k)$):

$$
f^* V = V \otimes_k \mathcal{O}_X, \quad f_* f^* V = (V \otimes_k \mathcal{O}_X)(X) = V \otimes_k \mathcal{O}_X(X).

$$

The unit is $V \to V \otimes_k \mathcal{O}_X(X)$, $v \mapsto v \otimes 1$. If $X$ is of finite type, one can think of this concretely as $V \hookrightarrow V \otimes_k k[x_1, \ldots, x_n]$, identifying $V$ with the "constant" elements.

**Key Insight:** The adjunction $(f^*, f_*)$ encodes how restriction of scalars and extension of scalars interact. The counit measures how far $\mathscr{F}$ is from being generated by its push-forward, while the unit measures how far $\mathscr{G}$ is from being determined by its pull-back.

**Prerequisites:** Adjoint functors, tensor products and restriction of scalars, global generation of sheaves, flat base change

<!-- BENCHMARK_PROBLEM: Let $f : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ be induced by $\varphi : B \to A$, and let $M$ be an $A$-module. Write down the counit map $A \otimes_B M_B \to M$ explicitly. Give an example where it is not injective. -->

### Remark: Decomposition of $f^{*}f_{*}\mathscr{F}$ and $f_{*}f^{*}\mathscr{G}$ {#ecag-0017}

When $f : X \to Y$ is a finite etale Galois cover with Galois group $G$ (so $G$ acts on $X$ over $Y$ and $Y \cong X/G$), there are decomposition formulas:

For a coherent sheaf $\mathscr{F}$ on $X$:

$$
f^* f_* \mathscr{F} \cong \bigoplus_{g \in G} g^* \mathscr{F}.

$$

This follows from the fact that $X \times_Y X \cong \coprod_{g \in G} X$ (the fibre product of a Galois cover with itself decomposes as a disjoint union indexed by the group), so

$$
f^* f_* \mathscr{F} \cong \operatorname{pr}_{1,*}(\operatorname{pr}_2^* \mathscr{F}) \cong \bigoplus_{g \in G} g^* \mathscr{F}

$$

by flat base change.

For a coherent sheaf $\mathscr{G}$ on $Y$:

$$
f_* f^* \mathscr{G} \cong \mathscr{G}^{\oplus \deg(f)} = \mathscr{G}^{\oplus |G|}.

$$

This follows from the projection formula: $f_* f^* \mathscr{G} \cong \mathscr{G} \otimes f_* \mathcal{O}_X$, and for an etale Galois cover, $f_* \mathcal{O}_X$ is a locally free $\mathcal{O}_Y$-module of rank $|G|$ that decomposes (after passing to representations) according to the regular representation of $G$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a finite etale Galois cover with group $G$. Using the isomorphism $X \times_Y X \cong \coprod_{g \in G} X$, derive the formula $f^* f_* \mathscr{F} \cong \bigoplus_{g \in G} g^* \mathscr{F}$ for a coherent sheaf $\mathscr{F}$ on $X$. -->

### Example: Push-forward... {#ecag-0018}

**Statement:** Push-forward sheaves behave very differently depending on the class of the morphism $f : X \to Y$. The following four cases are the most important in practice, with progressively weaker hypotheses and correspondingly weaker conclusions:

(1) **Finite flat morphism**: $f_* \mathcal{O}_X$ is locally free of rank $\deg(f)$. All higher direct images vanish: $R^i f_* \mathscr{F} = 0$ for $i > 0$ and any quasi-coherent $\mathscr{F}$, since finite morphisms are affine. The projection formula holds: $f_*(\mathscr{F} \otimes f^* \mathscr{G}) \cong f_* \mathscr{F} \otimes \mathscr{G}$.

(2) **Finite morphism** (not necessarily flat): $f_*$ is exact (since $f$ is affine), so $R^i f_* = 0$ for $i > 0$. However, $f_* \mathcal{O}_X$ need not be locally free; it is locally free if and only if $f$ is flat.

(3) **Flat projective morphism**: Grauert's theorem and cohomology-and-base-change apply. The sheaves $R^i f_* \mathscr{F}$ are coherent when $\mathscr{F}$ is coherent. If $h^i(X_y, \mathscr{F}_y)$ is constant in $y$, then $R^i f_* \mathscr{F}$ is locally free with formation commuting with base change.

(4) **Proper birational morphism**: The push-forward satisfies $f_* \mathcal{O}_X = \mathcal{O}_Y$ when $Y$ is normal (Zariski's main theorem). Higher direct images $R^i f_*$ encode information about the exceptional locus and are used in the study of resolutions of singularities.

**Construction/Proof:** These results follow from the general theory:

For (1) and (2), finiteness implies affineness, so the higher direct image vanishing is a consequence of the general fact that affine morphisms have trivial higher direct images (Serre's criterion: $f$ is affine if and only if $R^i f_* \mathscr{F} = 0$ for all quasi-coherent $\mathscr{F}$ and all $i > 0$).

For (3), Grauert's theorem (EGA III, Hartshorne III.12) requires flatness to ensure that cohomology of fibres varies semicontinuously and that constancy implies local freeness.

For (4), the equality $f_* \mathcal{O}_X = \mathcal{O}_Y$ for a proper birational morphism to a normal target follows from the fact that a regular function on $X$ restricts to a regular function on the open set where $f$ is an isomorphism, and normality ensures this extends uniquely to all of $Y$.

**Key Insight:** The hierarchy finite flat $\subset$ finite $\subset$ proper reflects decreasing control over push-forwards: flatness ensures local freeness, finiteness ensures exactness, and properness ensures only coherence.

**Prerequisites:** Finite morphisms, flat morphisms, proper morphisms, Grauert's theorem, Zariski's main theorem, higher direct images

<!-- BENCHMARK_PROBLEM: For each of the four classes of morphisms (finite flat, finite, flat projective, proper birational), state whether $R^i f_* \mathscr{F} = 0$ for $i > 0$ and whether $f_* \mathcal{O}_X$ is necessarily locally free. Justify each answer. -->

### Example: What prevents $f_{*}\mathcal{O}_{X}$ to be $\mathcal{O}_{Y}$ ? {#ecag-0019}

**Statement:** There are two important situations in which $f_* \mathcal{O}_X \cong \mathcal{O}_Y$:

(a) If $f_* \mathcal{O}_X$ is an invertible sheaf (line bundle) on $Y$, then necessarily $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

(b) If $f : X \to Y$ is a proper birational morphism and $Y$ is normal, then $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

**Construction/Proof:** For (a): The structure map $f^\# : \mathcal{O}_Y \to f_* \mathcal{O}_X$ is a morphism of $\mathcal{O}_Y$-modules. If $f_* \mathcal{O}_X$ is invertible, then locally $f^\#$ is a map $\mathcal{O}_{Y,y} \to \mathcal{O}_{Y,y}$ (after choosing a local trivialization), which is determined by the image of $1$, a unit-times-generator. Since $f^\#(1) = 1$ (ring map), this forces $f^\#$ to be surjective locally, hence an isomorphism of line bundles (an injective map of line bundles whose image contains a generator is an isomorphism).

For (b): Let $U \subseteq Y$ be the dense open subset over which $f$ is an isomorphism (which exists since $f$ is birational). For any open $V \subseteq Y$, the map $\mathcal{O}_Y(V) \to f_* \mathcal{O}_X(V) = \mathcal{O}_X(f^{-1}(V))$ is injective (since it is an isomorphism over $V \cap U$, which is dense). For surjectivity: a section $s \in \mathcal{O}_X(f^{-1}(V))$ restricts to a regular function on $f^{-1}(V \cap U) \cong V \cap U$, giving a rational function on $V$ that is regular on the dense open $V \cap U$. Since $Y$ is normal, regular functions on a dense open of a normal scheme extend to the whole scheme (by the algebraic Hartogs' lemma / S2 condition). Therefore $s$ extends to an element of $\mathcal{O}_Y(V)$.

**Key Insight:** For (a), the ring structure ($1 \mapsto 1$) rigidly constrains maps into line bundles. For (b), normality provides the S2 condition (algebraic Hartogs), which forces rational functions that are regular in codimension 1 to extend everywhere.

**Prerequisites:** Line bundles, proper birational morphisms, normal schemes, algebraic Hartogs' lemma (S2 condition), Zariski's main theorem

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a proper birational morphism with $Y$ normal. Prove that $f_* \mathcal{O}_X \cong \mathcal{O}_Y$. Which property of normal schemes is used to extend sections? -->

### Example: Pullback is a locally free sheaf, but not a locally free sheaf itself {#ecag-0020}

**Statement:** Consider $f : X = \operatorname{Spec}(\mathbb{Q}) \to Y = \operatorname{Spec}(\mathbb{Z})$ and the $\mathbb{Z}$-module $M = \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$, defining a coherent sheaf $\mathscr{F} = \widetilde{M}$ on $Y$. Then $f^* \mathscr{F} \cong \widetilde{\mathbb{Q}}$ is free of rank 1 on $X$, but $\mathscr{F}$ itself is not locally free on $Y$.

**Construction/Proof:** The pullback is computed as

$$
f^* \mathscr{F} = \widetilde{M \otimes_{\mathbb{Z}} \mathbb{Q}} = \widetilde{(\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}) \otimes_{\mathbb{Z}} \mathbb{Q}}.

$$

Now $\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Q} \cong \mathbb{Q}$ and $\mathbb{Z}/2\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Q} = 0$ (since every element $\bar{a} \otimes q = \bar{a} \otimes 2 \cdot (q/2) = 2\bar{a} \otimes (q/2) = 0$; torsion modules tensor to zero with $\mathbb{Q}$). Therefore $f^* \mathscr{F} \cong \widetilde{\mathbb{Q}}$, which is free of rank 1 on $\operatorname{Spec}(\mathbb{Q})$.

However, $\mathscr{F} = \widetilde{M}$ is not locally free on $\operatorname{Spec}(\mathbb{Z})$. At the prime $(2)$, the stalk is $M_{(2)} = \mathbb{Z}_{(2)} \oplus \mathbb{Z}/2\mathbb{Z}$, which is not a free $\mathbb{Z}_{(2)}$-module (it has torsion). A locally free sheaf on $\operatorname{Spec}(\mathbb{Z})$ would have torsion-free stalks, so $\mathscr{F}$ is not locally free.

This demonstrates that $f^*$ does not reflect the property of being locally free: one cannot conclude that $\mathscr{F}$ is locally free from the fact that $f^* \mathscr{F}$ is locally free, unless $f$ is faithfully flat. The morphism $\operatorname{Spec}(\mathbb{Q}) \to \operatorname{Spec}(\mathbb{Z})$ is flat but not faithfully flat (it is not surjective: the closed points $(p)$ for primes $p$ are not in the image).

**Key Insight:** Pullback along a flat (but not faithfully flat) morphism can kill torsion, making a non-free module appear free. Faithful flatness is needed to descend properties like local freeness from the pullback to the original sheaf.

**Prerequisites:** Tensor products, torsion modules, flat descent, faithful flatness, locally free sheaves

<!-- BENCHMARK_PROBLEM: Let $f : \operatorname{Spec}(\mathbb{Q}) \to \operatorname{Spec}(\mathbb{Z})$ and $M = \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$. Compute $f^* \widetilde{M}$ and show it is locally free, while $\widetilde{M}$ is not locally free on $\operatorname{Spec}(\mathbb{Z})$. Why does faithful flatness of $f$ matter for descending local freeness? -->

### Example: push-forward a vector bundle along a projective morphism might not be a vector bundle, even if cohomology groups of fibres are constant {#ecag-0021}

**Statement:** Let $Y = \operatorname{Spec}(k[x]/(x^2))$ (the dual numbers) and $f : X = \mathbb{P}^1_Y \to Y$ the projection. There exists a vector bundle $E$ on $X$, flat over $Y$, such that $f_* E$ is not locally free on $Y$, even though the function $y \mapsto h^0(X_y, E_y)$ is constant. The hypothesis that $Y$ is integral in the cohomology-and-base-change theorem is essential.

**Construction/Proof:** Consider the Euler exact sequence on $\mathbb{P}^1_Y$:

$$
0 \to \mathcal{O}_{\mathbb{P}^1_Y}(-2) \to \mathcal{O}_{\mathbb{P}^1_Y}(-1)^{\oplus 2} \to \mathcal{O}_{\mathbb{P}^1_Y} \to 0.

$$

We compute the extension group:

$$
\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1_Y}, \mathcal{O}_{\mathbb{P}^1_Y}(-2)) = H^1(\mathbb{P}^1_Y, \mathcal{O}_{\mathbb{P}^1_Y}(-2)) \cong k[x]/(x^2).

$$

Choose the extension class corresponding to $x \in k[x]/(x^2)$ (a nonzero non-unit). This gives an exact sequence

$$
0 \to \mathcal{O}_{\mathbb{P}^1_Y}(-2) \to E \to \mathcal{O}_{\mathbb{P}^1_Y} \to 0.

$$

The sheaf $E$ is a vector bundle on $\mathbb{P}^1_Y$ (locally free of rank 2) and is flat over $Y$ (since it is locally free on $X$ and $X$ is flat over $Y$).

To compute $f_* E = H^0(X, E)$, apply $f_*$ to the exact sequence. The connecting map in the long exact cohomology sequence is

$$
\delta : H^0(X, \mathcal{O}_{\mathbb{P}^1_Y}) \to H^1(X, \mathcal{O}_{\mathbb{P}^1_Y}(-2))

$$

which is multiplication by the extension class $x$. We have $H^0(X, \mathcal{O}_{\mathbb{P}^1_Y}) \cong k[x]/(x^2)$ and $H^1(X, \mathcal{O}_{\mathbb{P}^1_Y}(-2)) \cong k[x]/(x^2)$, and the map $\delta$ is multiplication by $x$:

$$
\delta : k[x]/(x^2) \xrightarrow{\cdot x} k[x]/(x^2).

$$

Therefore $H^0(X, E) = \ker(\delta) = (x) \subseteq k[x]/(x^2)$, the ideal generated by $x$. As a $k[x]/(x^2)$-module, $(x) \cong k$ (since $x \cdot x = 0$). This is a $k[x]/(x^2)$-module of length 1, but it is not free: a free module of rank 1 would be $k[x]/(x^2)$ itself, which has length 2. Therefore $f_* E$ is not locally free.

Note that the unique point $y$ of $Y$ has fibre $X_y = \mathbb{P}^1_k$, and $E_y$ fits into $0 \to \mathcal{O}(-2) \to E_y \to \mathcal{O} \to 0$ where the extension class becomes $0$ (since $x = 0$ in $k$), so $E_y \cong \mathcal{O} \oplus \mathcal{O}(-2)$ and $h^0(X_y, E_y) = 1$. The function $h^0$ is "constant" (there is only one point), yet $f_* E$ is not free.

**Key Insight:** The cohomology-and-base-change theorem (in its form guaranteeing local freeness from constancy of $h^i$) requires $Y$ to be integral (or at least reduced). Over a non-reduced base like $\operatorname{Spec}(k[x]/(x^2))$, the extension class can be nilpotent but nonzero, creating a non-split extension that has the same fibre as the split one but different global sections.

**Prerequisites:** Cohomology and base change, Ext groups, extensions of sheaves, dual numbers, Euler sequence on $\mathbb{P}^1$

<!-- BENCHMARK_PROBLEM: Let $Y = \operatorname{Spec}(k[x]/(x^2))$ and $f : \mathbb{P}^1_Y \to Y$. Construct a vector bundle $E$ on $\mathbb{P}^1_Y$ such that $f_* E$ is not locally free, by choosing an appropriate extension class in $\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1_Y}, \mathcal{O}_{\mathbb{P}^1_Y}(-2))$. Compute $H^0(\mathbb{P}^1_Y, E)$ as a $k[x]/(x^2)$-module. -->

### Remark: $\operatorname{Ext}^{1}$ and maps in the corresponding extension {#ecag-0022}

Given an exact sequence of coherent sheaves on a scheme $X$:

$$
0 \to \mathscr{F} \to \mathscr{E} \to \mathscr{G} \to 0,

$$

the extension class $e \in \operatorname{Ext}^1(\mathscr{G}, \mathscr{F})$ governs the connecting homomorphisms in the associated long exact cohomology sequences. Specifically:

1. **Connecting map in cohomology.** The connecting homomorphism $\delta^i : H^i(X, \mathscr{G}) \to H^{i+1}(X, \mathscr{F})$ is given by the Yoneda product (cup product) with the extension class $e$. That is, for $\alpha \in H^i(X, \mathscr{G})$:

$$
\delta^i(\alpha) = e \cup \alpha \in H^{i+1}(X, \mathscr{F}).

$$

In particular, when $i = 0$, the map $\delta^0 : H^0(X, \mathscr{G}) \to H^1(X, \mathscr{F})$ sends a global section $s$ of $\mathscr{G}$ to the obstruction class for lifting $s$ to a global section of $\mathscr{E}$.

2. **Functoriality.** The association of an extension class to a short exact sequence is functorial: given a morphism $\varphi : \mathscr{F} \to \mathscr{F}'$, the pushout extension has class $\varphi_*(e) \in \operatorname{Ext}^1(\mathscr{G}, \mathscr{F}')$. Similarly for pullbacks along morphisms $\psi : \mathscr{G}' \to \mathscr{G}$.

3. **Splitting criterion.** The extension splits (i.e., $\mathscr{E} \cong \mathscr{F} \oplus \mathscr{G}$) if and only if $e = 0$ in $\operatorname{Ext}^1(\mathscr{G}, \mathscr{F})$.

This machinery is used heavily in the previous example (ecag-0021), where the connecting map $\delta^0$ was multiplication by the extension class $x \in \operatorname{Ext}^1(\mathcal{O}, \mathcal{O}(-2)) \cong k[x]/(x^2)$, and the kernel of $\delta^0$ determined $H^0(X, E)$.

<!-- BENCHMARK_PROBLEM: Let $0 \to \mathscr{F} \to \mathscr{E} \to \mathscr{G} \to 0$ be an exact sequence of coherent sheaves on a projective scheme $X$ with extension class $e \in \operatorname{Ext}^1(\mathscr{G}, \mathscr{F})$. Show that the connecting homomorphism $\delta^0 : H^0(X, \mathscr{G}) \to H^1(X, \mathscr{F})$ is given by cup product with $e$. When is $\delta^0 = 0$? -->

### Example: Pull-back a bundle along an isomorphism might not get an isomorphic bundle {#ecag-0023}

**Statement:** Let $E$ be an elliptic curve over an algebraically closed field $k$ with origin $O$. For a point $a \in E$, let $\tau_a : E \to E$ denote translation by $a$. Then for any point $p \in E$:

$$
\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p + a)

$$

and $\mathcal{O}_E(p) \cong \mathcal{O}_E(p + a)$ if and only if $a = O$ (the identity element of $E$). In particular, pulling back a line bundle along a non-trivial automorphism can produce a non-isomorphic line bundle.

**Construction/Proof:** Step 1: The isomorphism $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p + a)$. The divisor of $\mathcal{O}_E(p)$ is the point $p$. Pulling back along $\tau_a$ replaces $p$ by $\tau_a^{-1}(p) = p - a$ in the group law... but we must be careful: $\tau_a^* \mathcal{O}_E(p)$ corresponds to the divisor $\tau_a^{-1}(p) = p - a$, so $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p - a)$. Equivalently, $\tau_{-a}^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p + a)$. In either formulation, pulling back along a nontrivial translation changes the line bundle.

Step 2: $\mathcal{O}_E(p) \cong \mathcal{O}_E(q)$ if and only if $p = q$. Two degree-1 line bundles $\mathcal{O}_E(p)$ and $\mathcal{O}_E(q)$ on an elliptic curve are isomorphic if and only if $p$ and $q$ are linearly equivalent. On an elliptic curve, $p \sim q$ if and only if $p = q$ (since $h^0(\mathcal{O}_E(p)) = 1$ by Riemann--Roch, so $|p|$ consists of the single effective divisor $p$). Therefore $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p)$ implies $a = O$.

Step 3: For a smooth variety $X$ with a finite automorphism group $G$, the group of $G$-linearized line bundles is

$$
\operatorname{Pic}^G(X) \cong \frac{\{G\text{-equivariant Weil divisors}\}}{\operatorname{div}\{G\text{-invariant rational functions}\}}.

$$

By Hilbert's Theorem 90, $H^1(G, \mathcal{O}(X)^*) = 0$, which implies that the forgetful map $\operatorname{Pic}^G(X) \hookrightarrow \operatorname{Pic}(X)$ is injective. One can also define an averaging map

$$
\phi : \operatorname{Pic}(X) \to \operatorname{Pic}^G(X), \quad D + \operatorname{div}(f) \mapsto \frac{1}{|G|} \sum_{g \in G} g^* D + \operatorname{div}\left(\frac{1}{|G|} \sum_{g \in G} g^* f\right)

$$

which provides a section (up to torsion issues) of the forgetful map, showing that $\operatorname{Pic}^G(X)$ captures the $G$-invariant part of the Picard group.

**Key Insight:** Unlike topological bundles, algebraic line bundles are sensitive to the precise algebraic structure of automorphisms. On an elliptic curve, the Abel--Jacobi map identifies degree-1 line bundles with points of the curve, so translation acts nontrivially on the Picard group.

**Prerequisites:** Elliptic curves, Picard group, linear equivalence, Riemann--Roch for curves, equivariant sheaves, Hilbert's Theorem 90

<!-- BENCHMARK_PROBLEM: Let $E$ be an elliptic curve with origin $O$ and $\tau_a$ translation by $a \in E$. Prove that $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p)$ for all $p$ if and only if $a = O$. Use the fact that on an elliptic curve, $\mathcal{O}(p) \cong \mathcal{O}(q)$ iff $p = q$. -->
