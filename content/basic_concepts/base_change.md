---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/base_change.tex
---

## Base-change

### Example: Reduced scheme but not geometrically reduced {#ecag-0005}

Let $k = \mathbf{F}_p(T)$ and $K = \mathbf{F}_p(T^{1/p})$. The scheme $\operatorname{Spec}(K)$ is reduced (it is a single point with no nilpotents), but it is not geometrically reduced: the base change $\operatorname{Spec}(K \otimes_k K)$ carries a nonzero nilpotent.

The extension $K/k$ is purely inseparable of degree $p$: the element $T^{1/p}$ satisfies the minimal polynomial $X^p - T \in k[X]$, which is irreducible over $k$ by Eisenstein's criterion at the prime $T$ in $\mathbf{F}_p[T]$ (then passing to the fraction field).

The tensor product decomposes as

$$
K \otimes_k K \cong K[X]/(X^p - T) \cong K[X]/((X - T^{1/p})^p)

$$

since $X^p - T = (X - T^{1/p})^p$ in characteristic $p$. The element

$$
\alpha = 1 \otimes T^{1/p} - T^{1/p} \otimes 1

$$

corresponds to the residue class of $X - T^{1/p}$ in the quotient. This element is nonzero (since $X - T^{1/p}$ is not divisible by $(X - T^{1/p})^p$), but

$$
\alpha^p = (1 \otimes T^{1/p} - T^{1/p} \otimes 1)^p = 1 \otimes T - T \otimes 1 = 0

$$

because $T \in k$ and $1 \otimes t = t \otimes 1$ for all $t \in k$. So $\alpha$ is a nonzero nilpotent, and $\operatorname{Spec}(K \otimes_k K)$ is not reduced.

The obstruction to geometric reducedness is precisely that $k^{1/p} \not\subseteq k$: purely inseparable extensions, invisible over the ground field, create nilpotents upon self-tensor.

<!-- BENCHMARK_PROBLEM: Let $k = \mathbf{F}_p(T)$ and $K = \mathbf{F}_p(T^{1/p})$. Explicitly exhibit a nonzero nilpotent element in $K \otimes_k K$ and prove that its $p$-th power is zero. What is the nilpotency index of this element? -->

## Push-forward and pull-back

### Example: Hartshorne $\operatorname{III}.12.4$ {#ecag-0006}

Let $Y$ be an integral scheme of finite type over an algebraically closed field $k$, and let $f : X \to Y$ be a flat projective morphism whose fibres are integral schemes. If $L$ and $M$ are line bundles on $X$ with $L_y \cong M_y$ for every $y \in Y$, then there exists a line bundle $N$ on $Y$ such that

$$
L \cong M \otimes f^* N.

$$

Set $\mathscr{F} = L \otimes M^{-1}$. By hypothesis, $\mathscr{F}_y \cong \mathcal{O}_{X_y}$ for every $y \in Y$, so $h^0(X_y, \mathscr{F}_y) = 1$ for all $y$.

**The direct image is a line bundle.** By Grauert's theorem (Hartshorne III.12.9), since $f$ is a flat projective morphism between Noetherian schemes, $\mathscr{F}$ is coherent and flat over $Y$, and $y \mapsto h^0(X_y, \mathscr{F}_y) = 1$ is constant, the direct image $f_* \mathscr{F}$ is locally free of rank $1$. Integrality of the fibres is essential here: since each $X_y$ is connected and reduced, $H^0(X_y, \mathcal{O}_{X_y}) = k(y)$, ensuring the rank is exactly $1$ rather than higher. Set $N = f_* \mathscr{F}$.

**The evaluation map is an isomorphism.** By cohomology and base change (applicable since $h^0$ is constant and $Y$ is integral), the natural map $f_* \mathscr{F} \otimes k(y) \to H^0(X_y, \mathscr{F}_y)$ is an isomorphism for each $y$. Since $\mathscr{F}_y \cong \mathcal{O}_{X_y}$ is globally generated, the evaluation map

$$
f^* f_* \mathscr{F} \to \mathscr{F}

$$

is surjective on each fibre. Both sides are line bundles on $X$ (the left side because $f^* N$ is a line bundle when $N$ is), and a surjection between line bundles is necessarily an isomorphism. Therefore $\mathscr{F} \cong f^* N$, giving $L \cong M \otimes f^* N$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a flat projective morphism with integral fibres over an integral scheme $Y$ of finite type over an algebraically closed field. If $L$ and $M$ are line bundles on $X$ with $L_y \cong M_y$ for all $y \in Y$, prove that $L \cong M \otimes f^* N$ for some line bundle $N$ on $Y$. Where exactly does the integrality of the fibres enter the proof? -->

### Remark: $f_*\mathcal{O}_{X}\cong \mathcal{O}_{Y}$ {#ecag-0007}

Under the same hypotheses -- $f : X \to Y$ flat projective with integral fibres, $Y$ integral of finite type over an algebraically closed field -- we have $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

Apply the preceding argument with $\mathscr{F} = \mathcal{O}_X$. Each fibre $X_y$ is integral, so $H^0(X_y, \mathcal{O}_{X_y}) \cong k(y)$, giving $h^0(X_y, \mathcal{O}_{X_y}) = 1$. By Grauert's theorem, $f_* \mathcal{O}_X$ is locally free of rank 1. The structure map $f^\# : \mathcal{O}_Y \to f_* \mathcal{O}_X$ is a morphism of $\mathcal{O}_Y$-modules sending $1 \mapsto 1$. At each stalk, this is an injection of free rank-1 modules $\mathcal{O}_{Y,y} \hookrightarrow (f_* \mathcal{O}_X)_y$. An injection between free modules of the same rank over a local ring is an isomorphism (the cokernel is finitely generated with zero localization, hence zero by Nakayama). Therefore $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a flat projective morphism with integral fibres, $Y$ an integral scheme of finite type over an algebraically closed field. Prove that $f_* \mathcal{O}_X \cong \mathcal{O}_Y$. Which specific property of the fibres guarantees the rank is exactly 1? -->

### Example: Fibres being integral is necessary; flatness matters {#ecag-0008}

The conclusion $f_* \mathcal{O}_X \cong \mathcal{O}_Y$ can fail without flatness, even when fibres are connected. Consider the morphism

$$
f : X = \operatorname{Spec}(k[x,y]/(x^2, xy)) \to Y = \operatorname{Spec}(k[y])

$$

induced by $k[y] \hookrightarrow k[x,y]/(x^2, xy)$, $y \mapsto y$.

**Structure of $A = k[x,y]/(x^2, xy)$.** As a $k[y]$-module, $A \cong k[y] \oplus k \cdot x$, where $y$ acts on the second summand by $y \cdot x = 0$ (from the relation $xy = 0$). The morphism $f$ is finite (hence projective) with target a regular Noetherian scheme.

**Non-flatness.** The element $x \in A$ is annihilated by $y \in k[y]$, so $A$ has $k[y]$-torsion. Over the PID $k[y]$, torsion-free is equivalent to flat, so $f$ is not flat.

**The push-forward.** We have $f_* \mathcal{O}_X = \widetilde{A}$ on $Y = \operatorname{Spec}(k[y])$. Since $A = k[y] \oplus k \cdot x$ as a $k[y]$-module, the push-forward has rank 2 at the generic point and is not even locally free (it has torsion at $y = 0$). In particular, $f_* \mathcal{O}_X \not\cong \mathcal{O}_Y$.

Flatness is essential for Grauert's theorem and cohomology-and-base-change to apply. A non-flat morphism can have connected fibres yet fail $f_* \mathcal{O}_X \cong \mathcal{O}_Y$ because the push-forward carries torsion.

<!-- BENCHMARK_PROBLEM: Show that the morphism $\operatorname{Spec}(k[x,y]/(x^2, xy)) \to \operatorname{Spec}(k[y])$ given by $y \mapsto y$ is not flat, and compute $f_* \mathcal{O}_X$ explicitly as a $k[y]$-module. Is it locally free? -->

### Example: Push-forward of a coherent sheaf might not be coherent {#ecag-0009}

Let $f : X = \operatorname{Spec}(k(x)) \to Y = \operatorname{Spec}(k)$ be the morphism induced by $k \hookrightarrow k(x)$. Then $f_* \mathcal{O}_X$ is the quasi-coherent sheaf on $\operatorname{Spec}(k)$ associated to the $k$-vector space $k(x)$. A coherent sheaf on $\operatorname{Spec}(k)$ corresponds to a finite-dimensional $k$-vector space, but $k(x)$ is infinite-dimensional over $k$ (the elements $1, x, x^2, \ldots$ are linearly independent). Therefore $f_* \mathcal{O}_X$ is not coherent.

The morphism $f$ is not proper: $\operatorname{Spec}(k(x))$ is not even of finite type over $k$ (the ring $k(x)$ is not a finitely generated $k$-algebra). By the proper direct image theorem (EGA III), if $f : X \to Y$ is proper and $\mathscr{F}$ is coherent on $X$, then $R^i f_* \mathscr{F}$ is coherent on $Y$ for all $i$. This example shows the properness hypothesis is necessary: even $f_* \mathcal{O}_X$ can fail coherence when $f$ is not proper.

<!-- BENCHMARK_PROBLEM: Let $k$ be a field and $f : \operatorname{Spec}(k(x)) \to \operatorname{Spec}(k)$ the natural morphism. Prove that $f_* \mathcal{O}_X$ is not coherent on $\operatorname{Spec}(k)$, and identify which hypothesis of the proper direct image theorem fails. -->

### Example: Push-forward of a quasi-coherent sheaf might not be quasi-coherent {#ecag-0010}

Let $f : X = \coprod_{i=1}^{\infty} \operatorname{Spec}(\mathbb{Z}) \to S = \operatorname{Spec}(\mathbb{Z})$ be the fold map (identity on each component). We show that $f_* \mathcal{O}_X$ is not quasi-coherent on $S$.

For any open $U \subseteq S$, we have $f_* \mathcal{O}_X(U) = \prod_{i=1}^{\infty} \mathcal{O}_S(U)$. Quasi-coherence on $S = \operatorname{Spec}(\mathbb{Z})$ requires $\mathscr{F}(D(a)) \cong \mathscr{F}(S) \otimes_\mathbb{Z} \mathbb{Z}[1/a]$ for every $a$. Testing at $a = 2$: the global sections are $f_* \mathcal{O}_X(S) = \prod_{i=1}^{\infty} \mathbb{Z}$ and the sections over $D(2)$ are $f_* \mathcal{O}_X(D(2)) = \prod_{i=1}^{\infty} \mathbb{Z}[1/2]$. If $f_* \mathcal{O}_X$ were quasi-coherent, the natural map

$$
\left(\prod_{i=1}^{\infty} \mathbb{Z}\right) \otimes_{\mathbb{Z}} \mathbb{Z}[1/2] \to \prod_{i=1}^{\infty} \mathbb{Z}[1/2]

$$

would be an isomorphism. Every element of the left-hand side can be written as $(a_i)_i \otimes 2^{-M}$ for some fixed $M$, giving entries $a_i / 2^M$ with a uniform bound on the power of $2$ in the denominator. But the right-hand side contains sequences like $(1/2, 1/4, 1/8, \ldots, 1/2^n, \ldots)$ where the denominators grow without bound. Such a sequence is not in the image, so the map is not surjective.

**A second example.** On $\mathbb{A}^1_k = \operatorname{Spec}(k[t])$, define a sheaf by

$$
\mathscr{F}(U) = \begin{cases} \mathcal{O}_X(U) & \text{if } 0 \notin U, \\ 0 & \text{if } 0 \in U. \end{cases}

$$

This is a sheaf (restriction maps and gluing are easily verified). The global sections vanish since $0 \in \mathbb{A}^1_k$, yet $\mathscr{F}$ is not the zero sheaf (it has nonzero sections on opens avoiding the origin). A quasi-coherent sheaf with zero global sections on an affine scheme must be zero, so $\mathscr{F}$ is not quasi-coherent.

Quasi-coherence of $f_* \mathscr{F}$ requires conditions on $f$: the standard sufficient condition is that $f$ be quasi-compact and quasi-separated. The infinite coproduct morphism fails quasi-compactness, and the resulting infinite product of rings does not commute with localization.

<!-- BENCHMARK_PROBLEM: Let $f : \coprod_{i=1}^{\infty} \operatorname{Spec}(\mathbb{Z}) \to \operatorname{Spec}(\mathbb{Z})$ be the fold map. Exhibit an explicit element of $\prod_{i=1}^{\infty} \mathbb{Z}[1/2]$ that is not in the image of $\left(\prod_{i=1}^{\infty} \mathbb{Z}\right) \otimes_{\mathbb{Z}} \mathbb{Z}[1/2]$, and explain why this shows $f_* \mathcal{O}_X$ is not quasi-coherent. -->

### Example: Push-forward might have different cohomology {#ecag-0011}

Let $f : \mathbb{P}^1_k \to \operatorname{Spec}(k)$ be the structure morphism and $\mathscr{F} = \mathcal{O}_{\mathbb{P}^1_k}(-2)$. We compute $H^1$ via two different routes and find they disagree.

**Via $f_*$.** Since $H^0(\mathbb{P}^1_k, \mathcal{O}(-2)) = 0$ (a line bundle of negative degree on $\mathbb{P}^1$ has no nonzero global sections), the push-forward is $f_* \mathcal{O}(-2) = 0$ as a sheaf on $\operatorname{Spec}(k)$. Therefore

$$
H^1(\operatorname{Spec}(k),\, f_* \mathcal{O}_{\mathbb{P}^1_k}(-2)) = 0.

$$

**Directly on $\mathbb{P}^1_k$.** The canonical bundle is $\omega_{\mathbb{P}^1} \cong \mathcal{O}(-2)$. By Serre duality,

$$
H^1(\mathbb{P}^1_k, \mathcal{O}(-2)) \cong H^0(\mathbb{P}^1_k, \mathcal{O})^\vee \cong k^\vee \cong k \neq 0.

$$

Alternatively, from the Cech computation with the standard cover $U_0 = D_+(x)$, $U_1 = D_+(y)$: the group $H^1(\mathbb{P}^1_k, \mathcal{O}(-2))$ is the $k$-vector space spanned by the class of $x^{-1}y^{-1}$, which is $1$-dimensional.

**Why the discrepancy.** For an affine morphism $f$, the Leray spectral sequence degenerates and gives $H^i(X, \mathscr{F}) \cong H^i(Y, f_* \mathscr{F})$ for all $i$. The structure morphism $\mathbb{P}^1_k \to \operatorname{Spec}(k)$ is projective but not affine, so the spectral sequence does not degenerate. The higher direct image $R^1 f_* \mathcal{O}(-2) \cong k$ accounts for the discrepancy.

<!-- BENCHMARK_PROBLEM: Let $f : \mathbb{P}_k^1 \to \operatorname{Spec}(k)$ be the structure morphism. Compute $H^1(\operatorname{Spec}(k), f_* \mathcal{O}_{\mathbb{P}_k^1}(-2))$ and $H^1(\mathbb{P}_k^1, \mathcal{O}_{\mathbb{P}_k^1}(-2))$ separately, and explain why they differ. What property of $f$ would guarantee they are equal? -->

### Remark: Push-forward from a Noetherian scheme {#ecag-0012}

Two standard preservation results for quasi-coherent sheaves under push-forward:

If $f : X \to Y$ is a morphism with $X$ Noetherian (or more generally, $f$ quasi-compact and quasi-separated), then $f_* \mathscr{F}$ is quasi-coherent on $Y$ for any quasi-coherent $\mathscr{F}$ on $X$.

If moreover $X$ is separated and Noetherian, then Cech cohomology agrees with derived functor cohomology: for any quasi-coherent sheaf $\mathscr{F}$ on $X$ and any open affine cover $\mathfrak{U}$ of $X$,

$$
\check{H}^p(\mathfrak{U}, \mathscr{F}) = H^p(X, \mathscr{F})

$$

for all $p \geq 0$. The key input is Leray's theorem: on a separated Noetherian scheme, intersections of affine opens are affine (by separatedness), so affine opens form a Leray cover for quasi-coherent sheaves (since quasi-coherent sheaves are acyclic on affine schemes by Serre's theorem).

<!-- BENCHMARK_PROBLEM: Let $X$ be a separated Noetherian scheme and $\mathscr{F}$ a quasi-coherent sheaf on $X$. Why does Cech cohomology with respect to an affine cover compute the derived functor cohomology? State the precise hypotheses needed. -->

### Example: Proper push-forward vs. finite flat push-forward {#ecag-0013}

Several fundamental results govern when direct images preserve finiteness. We state the key facts and the role of each hypothesis.

**(a) Proper direct image theorem** (EGA III). If $f : X \to Y$ is a proper morphism of Noetherian schemes and $\mathscr{F}$ is coherent on $X$, then $R^i f_* \mathscr{F}$ is coherent on $Y$ for all $i \geq 0$. The proof reduces to the projective case via Chow's lemma, then uses the explicit computation of cohomology of coherent sheaves on projective space.

**(b) Properness is essential.** The morphism $\operatorname{Spec}(k(x)) \to \operatorname{Spec}(k)$ is not proper ($k(x)$ is not a finitely generated $k$-algebra), and $f_* \mathcal{O}_X = k(x)$ is infinite-dimensional over $k$, hence not coherent.

**(c) Finite $\Rightarrow$ locally free iff flat.** For a finite morphism $f : X \to Y$ of Noetherian schemes, $f_* \mathcal{O}_X$ is locally free if and only if $f$ is flat. Forward: finiteness implies $f_* \mathcal{O}_X$ is coherent, and a coherent flat module over a Noetherian local ring is free (by the local criterion plus Nakayama). Converse: for an affine morphism, flatness of $f$ is equivalent to flatness of $f_* \mathcal{O}_X$ as an $\mathcal{O}_Y$-module.

**(d) Automatic flatness over regular curves.** Any surjective morphism $f : X \to Y$ with $Y$ a regular one-dimensional scheme is automatically flat. Over a DVR, every torsion-free module is flat, and surjectivity ensures the push-forward has nonzero generic fibre (hence is torsion-free).

**(e) Miracle flatness theorem.** If $f : X \to Y$ is a morphism of finite type between Noetherian local rings with $Y$ regular, $X$ Cohen--Macaulay, and $\dim X = \dim Y + \dim(\text{fibre})$, then $f$ is flat. This provides a powerful geometric criterion: correct fiber dimension plus Cohen--Macaulayness forces flatness over a regular base.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a finite morphism of Noetherian schemes. Prove that $f_* \mathcal{O}_X$ is locally free if and only if $f$ is flat. Where does the finiteness of $f$ enter each direction of the proof? -->

### Example: Push-forward of a trivial bundle might not be trivial {#ecag-0014}

Let $f : \mathbb{P}^1 \to \mathbb{P}^1$ be the degree-2 map $[x : y] \mapsto [x^2 : y^2]$. Since $f$ is finite and flat of degree 2, the push-forward $f_* \mathcal{O}_{\mathbb{P}^1}$ is locally free of rank 2. By Grothendieck's splitting theorem, every vector bundle on $\mathbb{P}^1$ decomposes as a direct sum of line bundles:

$$
f_* \mathcal{O}_{\mathbb{P}^1} \cong \mathcal{O}(a) \oplus \mathcal{O}(b)

$$

for some $a, b \in \mathbb{Z}$. We determine $a$ and $b$ using the projection formula: for any $n \in \mathbb{Z}$,

$$
H^0(\mathbb{P}^1, \mathcal{O}(n) \otimes f_* \mathcal{O}) \cong H^0(\mathbb{P}^1, f^* \mathcal{O}(n)) = H^0(\mathbb{P}^1, \mathcal{O}(2n))

$$

since $f^* \mathcal{O}(1) \cong \mathcal{O}(2)$ (pulling back along a degree-2 map doubles the degree). The left side gives $h^0(\mathcal{O}(n+a)) + h^0(\mathcal{O}(n+b))$.

| $n$ | RHS: $h^0(\mathcal{O}(2n))$ | LHS: $h^0(\mathcal{O}(n+a)) + h^0(\mathcal{O}(n+b))$ | Constraint |
|-----|-----|-----|-----|
| $-1$ | $h^0(\mathcal{O}(-2)) = 0$ | $h^0(\mathcal{O}(a-1)) + h^0(\mathcal{O}(b-1)) = 0$ | $a \leq 0$ and $b \leq 0$ |
| $0$ | $h^0(\mathcal{O}(0)) = 1$ | $h^0(\mathcal{O}(a)) + h^0(\mathcal{O}(b)) = 1$ | Exactly one of $a, b$ is $0$ |
| $1$ | $h^0(\mathcal{O}(2)) = 3$ | $h^0(\mathcal{O}(1+a)) + h^0(\mathcal{O}(1+b)) = 3$ | Determines the other |

From $n = -1$: both $a, b \leq 0$. From $n = 0$: exactly one equals $0$; say $a = 0$, then $h^0(\mathcal{O}(b)) = 0$ forces $b < 0$. From $n = 1$: $2 + h^0(\mathcal{O}(1 + b)) = 3$, so $h^0(\mathcal{O}(1 + b)) = 1$, giving $b = -1$. Therefore

$$
f_* \mathcal{O}_{\mathbb{P}^1} \cong \mathcal{O}_{\mathbb{P}^1} \oplus \mathcal{O}_{\mathbb{P}^1}(-1).

$$

The trivial bundle $\mathcal{O}_{\mathbb{P}^1}$ acquires a nontrivial summand under push-forward. Grothendieck's splitting theorem reduces the identification to a finite computation of global sections, which the projection formula translates to cohomology on the source.

<!-- BENCHMARK_PROBLEM: Let $f : \mathbb{P}^1 \to \mathbb{P}^1$ be the map $[x,y] \mapsto [x^2, y^2]$. Using the projection formula and Grothendieck's splitting theorem, determine $f_* \mathcal{O}_{\mathbb{P}^1}$ as a direct sum of line bundles. -->

### Remark: Good things happen sometimes {#ecag-0015}

In favorable situations, push-forwards of structure sheaves of divisors decompose simply. Let $k$ be algebraically closed, $f : X \to Y$ a finite morphism between smooth projective curves, and $D = \sum n_i p_i$ an effective divisor on $X$. Define $f_* D = \sum n_i f(p_i)$ as a divisor on $Y$. Then

$$
f_* \mathcal{O}_D \cong \mathcal{O}_{f_* D}.

$$

Here $\mathcal{O}_D = \mathcal{O}_X / \mathcal{O}_X(-D)$ is the structure sheaf of the subscheme defined by $D$, a skyscraper sheaf supported at the points $p_i$. Since $f$ is finite, $f_*$ on skyscraper sheaves simply relocates stalks: the stalk of $f_* \mathcal{O}_D$ at $q \in Y$ is $\bigoplus_{f(p_i) = q} \mathcal{O}_{X, p_i} / \mathfrak{m}_{p_i}^{n_i} \cong \bigoplus_{f(p_i) = q} k[t]/(t^{n_i})$. Over an algebraically closed field with distinct image points, this coincides with $\mathcal{O}_{f_* D}$ at $q$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a finite morphism of smooth projective curves over an algebraically closed field, and let $D = p_1 + p_2$ be a reduced divisor on $X$ with $f(p_1) \neq f(p_2)$. Verify explicitly that $f_* \mathcal{O}_D \cong \mathcal{O}_{f(p_1)} \oplus \mathcal{O}_{f(p_2)}$. -->

### Example: $f^{*}f_{*}\mathscr{F}$ and $f_{*}f^{*}\mathscr{G}$ {#ecag-0016}

For a morphism $f : X \to Y$, the functors $(f^*, f_*)$ form an adjoint pair, with natural transformations

$$
\varepsilon : f^* f_* \mathscr{F} \to \mathscr{F} \quad \text{(counit)}, \qquad \eta : \mathscr{G} \to f_* f^* \mathscr{G} \quad \text{(unit)}.

$$

We make these explicit in two settings.

**Affine case.** Let $f : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ correspond to a ring map $\varphi : B \to A$, $M$ an $A$-module, and $N$ a $B$-module. Write $M_B$ for $M$ viewed as a $B$-module via $\varphi$.

The counit is induced by the multiplication map

$$
A \otimes_B M_B \to M, \qquad a \otimes m \mapsto am.

$$

This is surjective (every $m \in M$ equals $1 \otimes m$), but typically not injective: the tensor product is over $B$, not $A$, so distinct simple tensors can collapse. For example, if $A = k[x]$, $B = k$, and $M = k[x]$, then $A \otimes_B M_B = k[x] \otimes_k k[x]$, which has dimension $> \dim_k k[x]$ in each graded piece.

The unit is

$$
N \to (A \otimes_B N)_B, \qquad n \mapsto 1 \otimes n.

$$

This is injective when $\varphi : B \to A$ is faithfully flat.

**Case $Y = \operatorname{Spec}(k)$.** For a coherent sheaf $\mathscr{F}$ on $X$, the push-forward $f_* \mathscr{F} = H^0(X, \mathscr{F})$ is a $k$-vector space, and

$$
f^* f_* \mathscr{F} = \mathcal{O}_X \otimes_k H^0(X, \mathscr{F}) \cong \mathcal{O}_X^{\oplus h^0(X, \mathscr{F})}.

$$

The counit $\mathcal{O}_X \otimes_k H^0(X, \mathscr{F}) \to \mathscr{F}$ is the evaluation map $g \otimes s \mapsto g \cdot s$. This is surjective precisely when $\mathscr{F}$ is globally generated.

For a finite-dimensional $k$-vector space $V$, the unit $V \to V \otimes_k H^0(X, \mathcal{O}_X)$ sends $v \mapsto v \otimes 1$, embedding $V$ as the "constant" elements.

The counit measures how far $\mathscr{F}$ is from being generated by its global sections (pushed forward to the base), while the unit measures how far $\mathscr{G}$ is from being determined by its pullback data.

<!-- BENCHMARK_PROBLEM: Let $f : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ be induced by $\varphi : B \to A$, and let $M$ be an $A$-module. Write down the counit map $A \otimes_B M_B \to M$ explicitly. Give an example where it is not injective. -->

### Remark: Decomposition of $f^{*}f_{*}\mathscr{F}$ and $f_{*}f^{*}\mathscr{G}$ {#ecag-0017}

When $f : X \to Y$ is a finite etale Galois cover with Galois group $G$ (so $G$ acts on $X$ over $Y$ and $Y \cong X/G$), the adjunction maps yield explicit decompositions.

**Pull-back of push-forward.** For a coherent sheaf $\mathscr{F}$ on $X$:

$$
f^* f_* \mathscr{F} \cong \bigoplus_{g \in G} g^* \mathscr{F}.

$$

This follows from the fibre product decomposition $X \times_Y X \cong \coprod_{g \in G} X$ (a defining property of Galois covers) and flat base change:

$$
f^* f_* \mathscr{F} \cong \operatorname{pr}_{1*}(\operatorname{pr}_2^* \mathscr{F}) \cong \bigoplus_{g \in G} g^* \mathscr{F}.

$$

**Push-forward of pull-back.** For a coherent sheaf $\mathscr{G}$ on $Y$:

$$
f_* f^* \mathscr{G} \cong \mathscr{G}^{\oplus |G|}.

$$

By the projection formula, $f_* f^* \mathscr{G} \cong \mathscr{G} \otimes f_* \mathcal{O}_X$. For an etale Galois cover, $f_* \mathcal{O}_X$ is a locally free $\mathcal{O}_Y$-module of rank $|G|$, decomposing (after passage to representations) according to the regular representation of $G$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a finite etale Galois cover with group $G$. Using the isomorphism $X \times_Y X \cong \coprod_{g \in G} X$, derive the formula $f^* f_* \mathscr{F} \cong \bigoplus_{g \in G} g^* \mathscr{F}$ for a coherent sheaf $\mathscr{F}$ on $X$. -->

### Example: Push-forward behavior by class of morphism {#ecag-0018}

Push-forward sheaves behave very differently depending on the class of the morphism. The following hierarchy summarizes the situation, with progressively weaker hypotheses yielding weaker conclusions.

**(1) Finite flat.** The push-forward $f_* \mathcal{O}_X$ is locally free of rank $\deg(f)$. All higher direct images vanish: $R^i f_* \mathscr{F} = 0$ for $i > 0$ and any quasi-coherent $\mathscr{F}$, since finite morphisms are affine and affine morphisms have trivial higher direct images. The projection formula $f_*(\mathscr{F} \otimes f^* \mathscr{G}) \cong f_* \mathscr{F} \otimes \mathscr{G}$ holds.

**(2) Finite (not necessarily flat).** The functor $f_*$ is exact ($R^i f_* = 0$ for $i > 0$) since $f$ is affine. However, $f_* \mathcal{O}_X$ need not be locally free; it is locally free if and only if $f$ is flat.

**(3) Flat projective.** Grauert's theorem and cohomology-and-base-change apply. The sheaves $R^i f_* \mathscr{F}$ are coherent for coherent $\mathscr{F}$. When $h^i(X_y, \mathscr{F}_y)$ is constant in $y$, the sheaf $R^i f_* \mathscr{F}$ is locally free and its formation commutes with base change.

**(4) Proper birational.** If $Y$ is normal, Zariski's main theorem gives $f_* \mathcal{O}_X = \mathcal{O}_Y$. Higher direct images $R^i f_*$ encode information about the exceptional locus and are central to the study of resolutions of singularities.

The hierarchy finite flat $\subset$ finite $\subset$ proper reflects decreasing control: flatness ensures local freeness, finiteness ensures exactness, and properness ensures only coherence. Serre's criterion characterizes the affine case precisely: $f$ is affine if and only if $R^i f_* \mathscr{F} = 0$ for all quasi-coherent $\mathscr{F}$ and all $i > 0$.

<!-- BENCHMARK_PROBLEM: For each of the four classes of morphisms (finite flat, finite, flat projective, proper birational), state whether $R^i f_* \mathscr{F} = 0$ for $i > 0$ and whether $f_* \mathcal{O}_X$ is necessarily locally free. Justify each answer. -->

### Example: What prevents $f_{*}\mathcal{O}_{X}$ from being $\mathcal{O}_{Y}$ {#ecag-0019}

Two important situations guarantee $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

**(a) When $f_* \mathcal{O}_X$ is invertible.** The structure map $f^\# : \mathcal{O}_Y \to f_* \mathcal{O}_X$ is a morphism of $\mathcal{O}_Y$-modules with $f^\#(1) = 1$. If $f_* \mathcal{O}_X$ is invertible, then locally $f^\#$ is a map $\mathcal{O}_{Y,y} \to \mathcal{O}_{Y,y}$ (after trivialization) sending $1$ to $1$, hence $f^\#$ maps the generator to the generator. An injection between free rank-1 modules whose image contains a generator is an isomorphism. Therefore $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

The rigidity here is purely ring-theoretic: the condition $1 \mapsto 1$ pins down the map once the target is known to be rank 1.

**(b) Proper birational morphism to a normal target.** Let $U \subseteq Y$ be the dense open over which $f$ is an isomorphism (existing by birationality). For any open $V \subseteq Y$, the map $\mathcal{O}_Y(V) \to \mathcal{O}_X(f^{-1}(V))$ is injective (it restricts to an isomorphism over the dense open $V \cap U$). For surjectivity: a section $s \in \mathcal{O}_X(f^{-1}(V))$ restricts to a regular function on $f^{-1}(V \cap U) \cong V \cap U$, defining a rational function on $V$ that is regular on the dense open $V \cap U$. Normality of $Y$ provides the S2 condition (algebraic Hartogs' lemma): a rational function on a normal scheme that is regular in codimension 1 extends to a regular function everywhere. Therefore $s$ extends to $\mathcal{O}_Y(V)$, giving $f_* \mathcal{O}_X \cong \mathcal{O}_Y$.

<!-- BENCHMARK_PROBLEM: Let $f : X \to Y$ be a proper birational morphism with $Y$ normal. Prove that $f_* \mathcal{O}_X \cong \mathcal{O}_Y$. Which property of normal schemes is used to extend sections? -->

### Example: Pullback of a locally free sheaf need not reflect local freeness {#ecag-0020}

Consider $f : X = \operatorname{Spec}(\mathbb{Q}) \to Y = \operatorname{Spec}(\mathbb{Z})$ and the $\mathbb{Z}$-module $M = \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$, defining a coherent sheaf $\mathscr{F} = \widetilde{M}$ on $Y$.

**The pullback is free.** We compute

$$
f^* \mathscr{F} = \widetilde{M \otimes_\mathbb{Z} \mathbb{Q}} = \widetilde{(\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}) \otimes_\mathbb{Z} \mathbb{Q}}.

$$

Since $\mathbb{Z} \otimes_\mathbb{Z} \mathbb{Q} \cong \mathbb{Q}$ and $\mathbb{Z}/2\mathbb{Z} \otimes_\mathbb{Z} \mathbb{Q} = 0$ (torsion modules tensor to zero with $\mathbb{Q}$: for any $\bar{a} \otimes q$, we have $\bar{a} \otimes q = \bar{a} \otimes 2 \cdot (q/2) = 2\bar{a} \otimes (q/2) = 0$), we get $f^* \mathscr{F} \cong \widetilde{\mathbb{Q}}$, free of rank 1.

**The original sheaf is not locally free.** At the prime $(2)$, the stalk $M_{(2)} = \mathbb{Z}_{(2)} \oplus \mathbb{Z}/2\mathbb{Z}$ has torsion, so it is not free over $\mathbb{Z}_{(2)}$. A locally free sheaf on $\operatorname{Spec}(\mathbb{Z})$ has torsion-free stalks at every prime, so $\mathscr{F}$ is not locally free.

**The role of faithful flatness.** The morphism $\operatorname{Spec}(\mathbb{Q}) \to \operatorname{Spec}(\mathbb{Z})$ is flat (localization is flat) but not faithfully flat: it is not surjective, since the closed points $(p)$ are not in the image. Faithful flatness is needed to descend properties like local freeness: if $f$ is faithfully flat and $f^* \mathscr{F}$ is locally free, then $\mathscr{F}$ is locally free. Without faithful flatness, the pullback can kill torsion and make a non-free module appear free.

<!-- BENCHMARK_PROBLEM: Let $f : \operatorname{Spec}(\mathbb{Q}) \to \operatorname{Spec}(\mathbb{Z})$ and $M = \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$. Compute $f^* \widetilde{M}$ and show it is locally free, while $\widetilde{M}$ is not locally free on $\operatorname{Spec}(\mathbb{Z})$. Why does faithful flatness of $f$ matter for descending local freeness? -->

### Example: Push-forward of a vector bundle along a projective morphism need not be locally free, even with constant $h^0$ {#ecag-0021}

Let $Y = \operatorname{Spec}(k[x]/(x^2))$ be the spectrum of the dual numbers and $f : X = \mathbb{P}^1_Y \to Y$ the projection. We construct a vector bundle $E$ on $X$, flat over $Y$, such that $f_* E$ is not locally free -- even though $h^0(X_y, E_y)$ is constant. This shows the hypothesis that $Y$ be integral (or at least reduced) in the cohomology-and-base-change theorem is essential.

**Construction via extensions.** The Euler exact sequence on $\mathbb{P}^1_Y$ and Serre duality give

$$
\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1_Y}, \mathcal{O}_{\mathbb{P}^1_Y}(-2)) = H^1(\mathbb{P}^1_Y, \mathcal{O}_{\mathbb{P}^1_Y}(-2)) \cong k[x]/(x^2).

$$

Choose the extension class $x \in k[x]/(x^2)$ (nonzero but nilpotent) to get

$$
0 \to \mathcal{O}_{\mathbb{P}^1_Y}(-2) \to E \to \mathcal{O}_{\mathbb{P}^1_Y} \to 0.

$$

The middle term $E$ is locally free of rank 2 on $\mathbb{P}^1_Y$ (an extension of locally free sheaves on a smooth scheme is locally free) and flat over $Y$.

**Computing $f_* E$.** Apply $f_*$ to the short exact sequence. The relevant portion of the long exact cohomology sequence is

$$
H^0(\mathbb{P}^1_Y, \mathcal{O}) \xrightarrow{\delta} H^1(\mathbb{P}^1_Y, \mathcal{O}(-2)),

$$

where $\delta$ is multiplication by the extension class $x$. Both $H^0$ and $H^1$ are isomorphic to $k[x]/(x^2)$, and the connecting map is

$$
\delta : k[x]/(x^2) \xrightarrow{\cdot\, x} k[x]/(x^2).

$$

Therefore $H^0(\mathbb{P}^1_Y, E) = \ker(\delta) = (x) \subset k[x]/(x^2)$. As a $k[x]/(x^2)$-module, $(x) \cong k$ (since $x \cdot x = 0$). This has length 1, while a free module of rank 1 has length 2. So $f_* E \cong \widetilde{k}$ is not locally free on $Y$.

**Fiber analysis.** The unique point $y$ of $Y$ has fiber $X_y = \mathbb{P}^1_k$, and $E_y$ fits into $0 \to \mathcal{O}(-2) \to E_y \to \mathcal{O} \to 0$ with extension class $x|_{y} = 0 \in k$, so $E_y \cong \mathcal{O} \oplus \mathcal{O}(-2)$ and $h^0(X_y, E_y) = 1$. The function $h^0$ is constant (trivially, as there is one point), yet $f_* E$ is not free.

Over a non-reduced base, the extension class can be nilpotent but nonzero, creating a non-split extension whose fiber over the closed point looks split. The cohomology-and-base-change theorem in its strong form (constancy of $h^i$ implies local freeness) requires integrality or at least reducedness of the base.

<!-- BENCHMARK_PROBLEM: Let $Y = \operatorname{Spec}(k[x]/(x^2))$ and $f : \mathbb{P}^1_Y \to Y$. Construct a vector bundle $E$ on $\mathbb{P}^1_Y$ such that $f_* E$ is not locally free, by choosing an appropriate extension class in $\operatorname{Ext}^1(\mathcal{O}_{\mathbb{P}^1_Y}, \mathcal{O}_{\mathbb{P}^1_Y}(-2))$. Compute $H^0(\mathbb{P}^1_Y, E)$ as a $k[x]/(x^2)$-module. -->

### Remark: $\operatorname{Ext}^{1}$ and connecting maps in extensions {#ecag-0022}

Given an exact sequence of coherent sheaves on a scheme $X$,

$$
0 \to \mathscr{F} \to \mathscr{E} \to \mathscr{G} \to 0,

$$

with extension class $e \in \operatorname{Ext}^1(\mathscr{G}, \mathscr{F})$, the connecting homomorphisms in the long exact cohomology sequence are governed by $e$ via the Yoneda product.

**Connecting map as cup product.** For $\alpha \in H^i(X, \mathscr{G})$, the connecting homomorphism $\delta^i : H^i(X, \mathscr{G}) \to H^{i+1}(X, \mathscr{F})$ is

$$
\delta^i(\alpha) = e \cup \alpha \in H^{i+1}(X, \mathscr{F}).

$$

When $i = 0$, the map $\delta^0 : H^0(X, \mathscr{G}) \to H^1(X, \mathscr{F})$ sends a global section $s$ of $\mathscr{G}$ to the obstruction class for lifting $s$ to a global section of $\mathscr{E}$.

**Functoriality.** The association of extension classes to short exact sequences is functorial in both arguments: a morphism $\varphi : \mathscr{F} \to \mathscr{F}'$ sends $e$ to the pushout class $\varphi_*(e) \in \operatorname{Ext}^1(\mathscr{G}, \mathscr{F}')$, and a morphism $\psi : \mathscr{G}' \to \mathscr{G}$ sends $e$ to the pullback class $\psi^*(e) \in \operatorname{Ext}^1(\mathscr{G}', \mathscr{F})$.

**Splitting criterion.** The extension splits ($\mathscr{E} \cong \mathscr{F} \oplus \mathscr{G}$) if and only if $e = 0$.

In ecag-0021, the connecting map $\delta^0$ was multiplication by the extension class $x \in \operatorname{Ext}^1(\mathcal{O}, \mathcal{O}(-2)) \cong k[x]/(x^2)$, and $\ker(\delta^0)$ determined $H^0(X, E)$.

<!-- BENCHMARK_PROBLEM: Let $0 \to \mathscr{F} \to \mathscr{E} \to \mathscr{G} \to 0$ be an exact sequence of coherent sheaves on a projective scheme $X$ with extension class $e \in \operatorname{Ext}^1(\mathscr{G}, \mathscr{F})$. Show that the connecting homomorphism $\delta^0 : H^0(X, \mathscr{G}) \to H^1(X, \mathscr{F})$ is given by cup product with $e$. When is $\delta^0 = 0$? -->

### Example: Pulling back a line bundle along a translation on an elliptic curve {#ecag-0023}

Let $E$ be an elliptic curve over an algebraically closed field $k$ with origin $O$, and let $\tau_a : E \to E$ denote translation by $a \in E$. For any point $p \in E$,

$$
\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p - a),

$$

and $\mathcal{O}_E(p) \cong \mathcal{O}_E(q)$ if and only if $p = q$. In particular, $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p)$ for all $p$ if and only if $a = O$.

**Pullback shifts the divisor.** The divisor of $\mathcal{O}_E(p)$ is the point $p$. Pulling back along $\tau_a$ replaces $p$ by $\tau_a^{-1}(p) = p - a$ (in the group law of $E$), giving $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p - a)$.

**Degree-1 line bundles classify points.** On an elliptic curve, two degree-1 line bundles $\mathcal{O}_E(p)$ and $\mathcal{O}_E(q)$ are isomorphic if and only if $p \sim q$ (linear equivalence). By Riemann--Roch, $h^0(\mathcal{O}_E(p)) = \deg(p) = 1$ for any point $p$, so the linear system $|p|$ consists of the single effective divisor $p$. Therefore $p \sim q$ implies $p = q$: the Abel--Jacobi map $E \to \operatorname{Pic}^1(E)$, $p \mapsto \mathcal{O}_E(p)$, is injective (and in fact an isomorphism).

It follows that $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p)$ requires $p - a = p$, i.e., $a = O$.

**Equivariant Picard group.** For a smooth variety $X$ with a finite automorphism group $G$, the group $\operatorname{Pic}^G(X)$ of $G$-linearized line bundles embeds into $\operatorname{Pic}(X)$ via the forgetful map. By Hilbert's Theorem 90, $H^1(G, \mathcal{O}(X)^*) = 0$, which guarantees this forgetful map is injective: a $G$-equivariant structure on a line bundle, if it exists, is unique up to isomorphism. One can also construct an averaging map $\operatorname{Pic}(X) \to \operatorname{Pic}^G(X)$ sending $\mathcal{L}$ to $\bigotimes_{g \in G} g^* \mathcal{L}$, which provides a partial inverse (up to torsion issues depending on $|G|$ and the characteristic).

Unlike topological bundles, algebraic line bundles are sensitive to the precise algebraic structure of automorphisms. On an elliptic curve, the Abel--Jacobi map identifies degree-1 line bundles with points of the curve, so translation acts nontrivially on $\operatorname{Pic}^1(E)$.

<!-- BENCHMARK_PROBLEM: Let $E$ be an elliptic curve with origin $O$ and $\tau_a$ translation by $a \in E$. Prove that $\tau_a^* \mathcal{O}_E(p) \cong \mathcal{O}_E(p)$ for all $p$ if and only if $a = O$. Use the fact that on an elliptic curve, $\mathcal{O}(p) \cong \mathcal{O}(q)$ iff $p = q$. -->
