---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/algebraic_groups.tex
---

## Algebraic groups and group schemes

### Example: Zariski closure of an algebraic group, not even a group {#ecag-0001}

The Zariski closure of an algebraic group inside an ambient variety need not be an algebraic group. The nodal cubic $C : y^2 = x^2(x+1)$ over a field $k$ provides a clean illustration: its smooth locus is isomorphic to $\mathbb{G}_m$, yet $C$ itself cannot carry any algebraic group structure because it is singular. This contrasts with the closure theorem for algebraic groups, which guarantees that the Zariski closure of an abstract subgroup $H \leq G$ inside an algebraic group $G$ is again a subgroup of $G$.

**The nodal cubic and its singular point.** Consider the affine plane curve

$$
C : y^2 = x^2(x+1) \subset \mathbb{A}^2_k.

$$

Writing $f(x,y) = x^3 + x^2 - y^2$, the partial derivatives are $\partial f/\partial x = 3x^2 + 2x$ and $\partial f/\partial y = -2y$. Both vanish at the origin, so $(0,0)$ is a singular point. The tangent cone there is cut out by the lowest-degree homogeneous part of $f$, namely $x^2 - y^2 = (x-y)(x+y)$, which consists of two distinct lines (assuming $\operatorname{char}(k) \neq 2$). This confirms that $(0,0)$ is an ordinary node.

**The smooth locus is $\mathbb{G}_m$.** Away from the node, introduce the parameter $t = y/x$. Then $t^2 = x + 1$, giving $x = t^2 - 1$ and $y = tx = t(t^2 - 1) = t^3 - t$. When $t \neq \pm 1$ (corresponding to $(x,y) \neq (0,0)$), this substitution is invertible. The map

$$
\varphi : \mathbb{G}_m \to C \setminus \{(0,0)\}, \qquad t \mapsto (t^2 - 1, \; t^3 - t)

$$

is an isomorphism of varieties. On the level of coordinate rings, $\mathcal{O}(C \setminus \{(0,0)\})$ is the localization of $k[x,y]/(y^2 - x^2(x+1))$ at the maximal ideal of the origin. Under $\varphi^*$, this ring is identified with $k[t, t^{-1}]$: the inverse map sends $t \mapsto y/x$, $t^{-1} \mapsto x(x+1)/y$ (using $y^2 = x^2(x+1)$ to verify $t \cdot t^{-1} = 1$). Under this identification, the group law on $\mathbb{G}_m$ corresponds to multiplication of the parameter $t$.

**The closure is not a group.** The Zariski closure of $C \setminus \{(0,0)\}$ in $\mathbb{A}^2_k$ is the full curve $C$, since removing a closed point from an irreducible curve leaves a dense open subset. Since $C$ has a singular point at the origin, it cannot carry the structure of an algebraic group: over any field, an algebraic group is smooth. (The multiplication map $\mu : G \times G \to G$ and the existence of a rational point imply that $G$ is geometrically reduced; then generic smoothness plus homogeneity under translation forces smoothness everywhere.)

**Why no contradiction with the closure theorem.** The closure theorem states: if $G$ is an algebraic group and $H \leq G(k)$ is a Zariski-dense subset that is also an abstract subgroup, then $\overline{H} \leq G$ is a closed subgroup scheme. Crucially, the ambient space must itself be an algebraic group. In our example, $\mathbb{G}_m$ is embedded as an open subvariety of the singular curve $C$, not as a subgroup of an algebraic group. The closure is taken inside $\mathbb{A}^2_k$, which has no group structure compatible with the embedding.

**Application: Zariski density of $\operatorname{SL}(2,\mathbb{Z})$ in $\operatorname{SL}(2,\mathbb{C})$.** The closure theorem gives a powerful method for proving density results. We show that $\overline{\operatorname{SL}(2,\mathbb{Z})}^{\mathrm{Zar}} = \operatorname{SL}(2,\mathbb{C})$ using the Bruhat decomposition.

By the closure theorem, $\overline{\operatorname{SL}(2,\mathbb{Z})}$ is a closed subgroup of $\operatorname{SL}(2,\mathbb{C})$. We identify generators that lie in this closure. The matrices $\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ for $n \in \mathbb{Z}$ lie in $\operatorname{SL}(2,\mathbb{Z})$. Any polynomial $f(a)$ vanishing on all these matrices satisfies $f(n) = 0$ for all $n \in \mathbb{Z}$, hence $f = 0$. Therefore their Zariski closure is the full upper unipotent subgroup

$$
U_+ = \left\{ \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} : a \in \mathbb{C} \right\}.

$$

By the closure theorem (since $\overline{\operatorname{SL}(2,\mathbb{Z})}$ is a group), $U_+ \subset \overline{\operatorname{SL}(2,\mathbb{Z})}$. The same argument with $\begin{pmatrix} 1 & 0 \\ n & 1 \end{pmatrix}$ gives $U_- \subset \overline{\operatorname{SL}(2,\mathbb{Z})}$.

To show the maximal torus $T = \left\{ \begin{pmatrix} t & 0 \\ 0 & t^{-1} \end{pmatrix} : t \in \mathbb{C}^\times \right\}$ lies in $\overline{\operatorname{SL}(2,\mathbb{Z})}$, let $s = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in \operatorname{SL}(2,\mathbb{Z})$ and compute, for any $a \in \mathbb{C}$ with $a \neq 0$:

$$
\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -a^{-1} & 1 \end{pmatrix} \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & a \\ -a^{-1} & 1 \end{pmatrix} \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & a \\ -a^{-1} & 0 \end{pmatrix}.

$$

(The intermediate product has $(1,1)$-entry $1 + a(-a^{-1}) = 0$; the final $(2,2)$-entry is $(-a^{-1})(a) + 1 \cdot 1 = 0$.) This triple product lies in $\overline{\operatorname{SL}(2,\mathbb{Z})}$ since each factor belongs to $U_+$ or $U_-$. Now observe that

$$
s^{-1} \begin{pmatrix} 0 & a \\ -a^{-1} & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} 0 & a \\ -a^{-1} & 0 \end{pmatrix} = \begin{pmatrix} -a^{-1} & 0 \\ 0 & -a \end{pmatrix} = (-I) \begin{pmatrix} a^{-1} & 0 \\ 0 & a \end{pmatrix}.

$$

Since $s, -I \in \operatorname{SL}(2,\mathbb{Z})$ and $\overline{\operatorname{SL}(2,\mathbb{Z})}$ is a group, we conclude $\begin{pmatrix} a^{-1} & 0 \\ 0 & a \end{pmatrix} \in \overline{\operatorname{SL}(2,\mathbb{Z})}$ for all $a \neq 0$, i.e., $T \subset \overline{\operatorname{SL}(2,\mathbb{Z})}$.

With $U_+$, $U_-$, and $T$ all contained in $\overline{\operatorname{SL}(2,\mathbb{Z})}$, the Bruhat decomposition completes the argument:

$$
\operatorname{SL}(2,\mathbb{C}) = B w_0 B \sqcup B

$$

where $B = TU_+$ is the upper Borel subgroup and $w_0 = s$ is the nontrivial Weyl group element. Since $T$ and $U_+$ both lie in $\overline{\operatorname{SL}(2,\mathbb{Z})}$, so does $B = TU_+$. The two Bruhat cells $BsB$ and $B$ are then both contained in $\overline{\operatorname{SL}(2,\mathbb{Z})}$ (using $s \in \operatorname{SL}(2,\mathbb{Z})$ and the fact that $\overline{\operatorname{SL}(2,\mathbb{Z})}$ is closed under multiplication), giving $\overline{\operatorname{SL}(2,\mathbb{Z})} = \operatorname{SL}(2,\mathbb{C})$.

<!-- BENCHMARK_PROBLEM: Let $C : y^2 = x^2(x+1)$ be the nodal cubic over an algebraically closed field $k$ with $\operatorname{char}(k) \neq 2$. Show that $C \setminus \{(0,0)\} \cong \mathbb{G}_m$ by exhibiting an explicit isomorphism with inverse, and explain precisely which property of algebraic groups fails for $C$ that prevents it from being an algebraic group. Then use the Bruhat decomposition for $\operatorname{SL}_2$ to prove that $\operatorname{SL}(2,\mathbb{Z})$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{C})$. -->

### Example: $SL(2,\mathbb{Z}$ is Zariski-dense in $SL(2,\mathbb{C})$, another proof, Sam {#ecag-0002}

There is an alternative proof that $\operatorname{SL}(2,\mathbb{Z})$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{C})$, using $p$-adic methods and the density of $\mathbb{Q}(i)$-points rather than the Bruhat decomposition. The argument proceeds through a chain of density statements, each in a different topology.

**Strong approximation gives $p$-adic density.** The algebraic group $\operatorname{SL}_2$ is simply connected (its fundamental group as an algebraic group is trivial; equivalently, $\operatorname{SL}_2$ has no nontrivial connected finite etale covers). The strong approximation theorem for simply connected semisimple groups over $\mathbb{Q}$ states that $\operatorname{SL}(2,\mathbb{Z})$ is dense in $\operatorname{SL}(2,\mathbb{Z}_p)$ in the $p$-adic topology for every prime $p$. We fix $p = 5$ for a reason that will become clear shortly.

**From $p$-adic density to Zariski density over $\mathbb{Q}_5$.** Since $\operatorname{SL}(2,\mathbb{Z})$ is $5$-adically dense in $\operatorname{SL}(2,\mathbb{Z}_5)$, and the Zariski topology on $\operatorname{SL}(2,\mathbb{Q}_5)$ is coarser than the $5$-adic topology (a Zariski-closed set is defined by polynomial equations, which are continuous in the $5$-adic topology, so the zero locus is $5$-adically closed), any Zariski-closed set containing $\operatorname{SL}(2,\mathbb{Z})$ also contains $\operatorname{SL}(2,\mathbb{Z}_5)$.

Moreover, $\operatorname{SL}(2,\mathbb{Z}_5)$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{Q}_5)$. To see this, note that $\operatorname{SL}(2,\mathbb{Z}_5)$ is open in $\operatorname{SL}(2,\mathbb{Q}_5)$ in the $5$-adic topology. A nonzero polynomial on $\operatorname{SL}_2$ restricts to a nonzero analytic function on the $5$-adic manifold $\operatorname{SL}(2,\mathbb{Q}_5)$; by the $p$-adic identity theorem, such a function cannot vanish on the open set $\operatorname{SL}(2,\mathbb{Z}_5)$ without vanishing identically. Combining, $\operatorname{SL}(2,\mathbb{Z})$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{Q}_5)$.

**Why $p = 5$: the field $\mathbb{Q}_5$ contains $i$.** The polynomial $x^2 + 1$ factors modulo $5$ as $(x-2)(x-3)$ since $2^2 = 4 \equiv -1 \pmod{5}$. By Hensel's lemma (the derivative $2x$ is nonzero at $x \equiv 2$ since $\operatorname{char}(\mathbb{Q}_5) = 0$), the root lifts to $\mathbb{Z}_5$, giving a square root of $-1$ in $\mathbb{Q}_5$. Therefore $\mathbb{Q}(i) \hookrightarrow \mathbb{Q}_5$, and consequently $\operatorname{SL}(2,\mathbb{Q}(i)) \subset \operatorname{SL}(2,\mathbb{Q}_5)$.

Any prime $p \equiv 1 \pmod{4}$ would work equally well, since $-1$ is a quadratic residue mod $p$ precisely when $p \equiv 1 \pmod{4}$ (by the first supplement to quadratic reciprocity). The choice $p = 5$ is simply the smallest such prime.

**An open chart on $\operatorname{SL}_2$.** The map

$$
\psi : (\mathbb{A}^1 \setminus \{0\})^2 \times \mathbb{A}^1 \hookrightarrow \operatorname{SL}_2, \qquad (x, y, z) \mapsto \begin{pmatrix} x & y \\ z & \frac{1 + yz}{x} \end{pmatrix}

$$

is well-defined since the determinant equals $x \cdot \frac{1+yz}{x} - yz = 1$. Its image is the open subset $\{a_{11} \neq 0\} \cap \{a_{12} \neq 0\} \subset \operatorname{SL}_2$, which is Zariski-dense because $\operatorname{SL}_2$ is irreducible of dimension 3.

**Density of $\mathbb{Q}(i)$-points completes the proof.** The field $\mathbb{Q}(i)$ is dense in $\mathbb{C}$ in the Euclidean topology, since both $\mathbb{Q}$ is dense in $\mathbb{R}$ and every complex number $a + bi$ can be approximated by $(a' + b'i)$ with $a', b' \in \mathbb{Q}$. It follows that $(\mathbb{Q}(i) \setminus \{0\})^2 \times \mathbb{Q}(i)$ is Euclidean-dense in $(\mathbb{C} \setminus \{0\})^2 \times \mathbb{C}$, and via $\psi$, the $\mathbb{Q}(i)$-points of the open chart are Euclidean-dense in the $\mathbb{C}$-points of the chart.

Now we chain the density statements. Euclidean density implies Zariski density (a polynomial vanishing on a Euclidean-dense set vanishes identically), so $\operatorname{SL}(2,\mathbb{Q}(i))$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{C})$. Since $\mathbb{Q}(i) \subset \mathbb{Q}_5$ and $\operatorname{SL}(2,\mathbb{Z})$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{Q}_5)$, any polynomial vanishing on $\operatorname{SL}(2,\mathbb{Z})$ vanishes on $\operatorname{SL}(2,\mathbb{Q}_5)$, hence on $\operatorname{SL}(2,\mathbb{Q}(i))$, hence on $\operatorname{SL}(2,\mathbb{C})$. Therefore $\overline{\operatorname{SL}(2,\mathbb{Z})}^{\mathrm{Zar}} = \operatorname{SL}(2,\mathbb{C})$.

**Verification.** We check the chain of inclusions is correct:

$$
\operatorname{SL}(2,\mathbb{Z}) \hookrightarrow \operatorname{SL}(2,\mathbb{Z}_5) \hookrightarrow \operatorname{SL}(2,\mathbb{Q}_5) \hookleftarrow \operatorname{SL}(2,\mathbb{Q}(i)) \hookrightarrow \operatorname{SL}(2,\mathbb{C}).

$$

The argument uses "Zariski-dense in" at each stage: the first two arrows are from strong approximation plus $p$-adic density, and the rightmost arrow is from Euclidean density of $\mathbb{Q}(i)$ in $\mathbb{C}$. The backward arrow $\operatorname{SL}(2,\mathbb{Q}(i)) \hookrightarrow \operatorname{SL}(2,\mathbb{Q}_5)$ uses that $\mathbb{Q}(i) \subset \mathbb{Q}_5$; the key subtlety is that we use Zariski density of $\operatorname{SL}(2,\mathbb{Z})$ in $\operatorname{SL}(2,\mathbb{Q}_5)$ to conclude vanishing of polynomials on $\operatorname{SL}(2,\mathbb{Q}(i))$ (since $\mathbb{Q}(i)$-points are a subset of $\mathbb{Q}_5$-points), and then Zariski density of $\operatorname{SL}(2,\mathbb{Q}(i))$ in $\operatorname{SL}(2,\mathbb{C})$ extends the vanishing to all of $\operatorname{SL}(2,\mathbb{C})$.

<!-- BENCHMARK_PROBLEM: Explain why $\mathbb{Q}_5$ contains a primitive 4th root of unity (using Hensel's lemma and the factorization of $x^2 + 1$ modulo 5). Then, using the open embedding $(x,y,z) \mapsto \begin{pmatrix} x & y \\ z & (1+yz)/x \end{pmatrix}$ of $(\mathbb{A}^1 \setminus \{0\})^2 \times \mathbb{A}^1$ into $\operatorname{SL}_2$, show that if $F \subset K$ are fields with $F$ dense in $K$ in the Euclidean topology, then $\operatorname{SL}(2,F)$ is Zariski-dense in $\operatorname{SL}(2,K)$. Combine this with strong approximation to give a proof that $\operatorname{SL}(2,\mathbb{Z})$ is Zariski-dense in $\operatorname{SL}(2,\mathbb{C})$. -->

### Remark: Non-reduced group schemes in characteristic $p$ {#ecag-0003}

In characteristic $p > 0$, the scheme $\operatorname{Spec}(k[x]/(x^p))$ underlies two fundamentally different group scheme structures. These arise as the kernels of the Frobenius endomorphism on $\mathbb{G}_m$ and $\mathbb{G}_a$ respectively, and they are distinguished entirely by their Hopf algebra structures.

**The group schemes $\mu_p$ and $\alpha_p$.** Over a field $k$ of characteristic $p$, the Frobenius endomorphism $x \mapsto x^p$ is an endomorphism of both the multiplicative group $\mathbb{G}_m = \operatorname{Spec}(k[x, x^{-1}])$ and the additive group $\mathbb{G}_a = \operatorname{Spec}(k[x])$. Their kernels fit into exact sequences of group schemes:

$$
0 \to \mu_p \to \mathbb{G}_m \xrightarrow{x \mapsto x^p} \mathbb{G}_m \to 0,

$$

$$
0 \to \alpha_p \to \mathbb{G}_a \xrightarrow{x \mapsto x^p} \mathbb{G}_a \to 0.

$$

As functors on $k$-algebras, $\mu_p(S) = \{ s \in S^\times : s^p = 1 \}$ (the $p$-th roots of unity in $S$) and $\alpha_p(S) = \{ s \in S : s^p = 0 \}$ (the $p$-nilpotent elements of $S$). These are represented by $\operatorname{Spec}(k[x]/(x^p - 1))$ and $\operatorname{Spec}(k[x]/(x^p))$ respectively.

**Isomorphism of underlying schemes.** In characteristic $p$, the binomial theorem gives $x^p - 1 = (x-1)^p$, so the substitution $u = x - 1$ yields

$$
k[x]/(x^p - 1) \cong k[u]/(u^p).

$$

Thus $\mu_p$ and $\alpha_p$ have isomorphic underlying schemes --- both are $\operatorname{Spec}$ of a truncated polynomial ring of length $p$. As topological spaces, both consist of a single point (the unique prime ideal $(u)$), with structure sheaf $k[u]/(u^p)$.

**The Hopf algebra structures.** A group scheme structure on $\operatorname{Spec}(A)$ is equivalent to a Hopf algebra structure on $A$: a comultiplication $\Delta : A \to A \otimes_k A$ (encoding the group law), a counit $\varepsilon : A \to k$ (encoding the identity element), and an antipode $S : A \to A$ (encoding inversion). The two group schemes have the following structures:

| | $\mu_p$: $A = k[x]/(x^p - 1)$ | $\alpha_p$: $A = k[x]/(x^p)$ |
|---|---|---|
| Group law | Multiplication: $(s,t) \mapsto st$ | Addition: $(s,t) \mapsto s + t$ |
| $\Delta(x)$ | $x \otimes x$ | $x \otimes 1 + 1 \otimes x$ |
| $\varepsilon(x)$ | $1$ | $0$ |
| $S(x)$ | $x^{-1} = x^{p-1}$ | $-x$ |

One verifies that these are well-defined. For $\mu_p$: $\Delta(x)^p = x^p \otimes x^p = 1 \otimes 1$ in $A \otimes A$, so $\Delta$ factors through $A \otimes A$. For $\alpha_p$: $\Delta(x)^p = (x \otimes 1 + 1 \otimes x)^p = x^p \otimes 1 + 1 \otimes x^p = 0$ (the cross terms vanish since $\binom{p}{i} \equiv 0 \pmod{p}$ for $0 < i < p$), so $\Delta$ is well-defined on $k[x]/(x^p)$.

**Non-isomorphism as group schemes.** To show $\mu_p \not\cong \alpha_p$, we prove that no $k$-algebra isomorphism $\varphi : k[u]/(u^p) \to k[u]/(u^p)$ can intertwine the two comultiplications. Under the substitution $u = x - 1$, the comultiplication of $\mu_p$ becomes

$$
\Delta_\mu(u) = \Delta_\mu(x) - 1 = x \otimes x - 1 \otimes 1 = (u+1) \otimes (u+1) - 1 = u \otimes 1 + 1 \otimes u + u \otimes u.

$$

For $\alpha_p$, the comultiplication is $\Delta_\alpha(u) = u \otimes 1 + 1 \otimes u$. So $\Delta_\mu$ and $\Delta_\alpha$ differ by the term $u \otimes u$.

Any $k$-algebra automorphism of $k[u]/(u^p)$ has the form $\varphi(u) = a_1 u + a_2 u^2 + \cdots + a_{p-1} u^{p-1}$ with $a_1 \neq 0$ (since $\varphi$ must map the maximal ideal $(u)$ to itself and be an isomorphism). If $\varphi$ intertwined $\Delta_\mu$ with $\Delta_\alpha$, we would need

$$
(\varphi \otimes \varphi)(\Delta_\mu(u)) = \Delta_\alpha(\varphi(u)),

$$

i.e., $\varphi(u) \otimes 1 + 1 \otimes \varphi(u) + \varphi(u) \otimes \varphi(u) = \varphi(u) \otimes 1 + 1 \otimes \varphi(u)$, which forces $\varphi(u) \otimes \varphi(u) = 0$ in $k[u]/(u^p) \otimes k[u]/(u^p)$. But $\varphi(u) = a_1 u + \text{higher}$ with $a_1 \neq 0$, so $\varphi(u) \otimes \varphi(u)$ has leading term $a_1^2 (u \otimes u) \neq 0$. This is a contradiction.

Alternatively, one can distinguish $\mu_p$ from $\alpha_p$ by their Cartier duals: the Cartier dual of $\mu_p$ is the constant group scheme $\mathbb{Z}/p\mathbb{Z}$, while the Cartier dual of $\alpha_p$ is $\alpha_p$ itself (it is self-dual). Since $\mathbb{Z}/p\mathbb{Z}$ is etale and $\alpha_p$ is not (it has a single point), these are visibly non-isomorphic, hence so are $\mu_p$ and $\alpha_p$.

<!-- BENCHMARK_PROBLEM: Let $k$ be a field of characteristic $p > 0$. Write down explicitly the Hopf algebra structures (comultiplication, counit, antipode) on $k[x]/(x^p - 1)$ for $\mu_p$ and on $k[x]/(x^p)$ for $\alpha_p$. Using the substitution $u = x - 1$ to identify the underlying algebras as $k[u]/(u^p)$, show that the comultiplication of $\mu_p$ becomes $\Delta_\mu(u) = u \otimes 1 + 1 \otimes u + u \otimes u$, and prove that no $k$-algebra automorphism of $k[u]/(u^p)$ can intertwine $\Delta_\mu$ with $\Delta_\alpha(u) = u \otimes 1 + 1 \otimes u$, thereby showing $\mu_p \not\cong \alpha_p$ as group schemes. -->

### Example: A group scheme that is not smooth over a nonperfect field of characteristic $p$ {#ecag-0004}

Over a nonperfect field $k$ of characteristic $p > 0$, the closed subgroup scheme $G = V(x^p + \alpha y^p) \subset \mathbb{G}_{a,k}^2$ (where $\alpha \in k \setminus k^p$) is reduced and irreducible but nowhere smooth and not normal. This demonstrates that in positive characteristic, the implications "algebraic group $\Rightarrow$ smooth" and "reduced $\Rightarrow$ generically smooth" can both fail for group schemes over non-perfect base fields.

**Setup and the subgroup scheme structure.** Let $k$ be a field of characteristic $p > 0$ with an element $\alpha \in k \setminus k^p$, and consider $\mathbb{G}_{a,k}^2 = \operatorname{Spec}(k[x,y])$ with the additive group law $(x,y) \mapsto (x_1 + x_2, \, y_1 + y_2)$. The comultiplication is $\Delta(x) = x \otimes 1 + 1 \otimes x$ and $\Delta(y) = y \otimes 1 + 1 \otimes y$. Define

$$
G = V(x^p + \alpha y^p) = \operatorname{Spec}\bigl(k[x,y]/(x^p + \alpha y^p)\bigr).

$$

To verify that $G$ is a closed subgroup scheme, we must check that the ideal $I = (x^p + \alpha y^p)$ is a Hopf ideal: it must be preserved by the comultiplication, counit, and antipode. For the comultiplication:

$$
\Delta(x^p + \alpha y^p) = (x \otimes 1 + 1 \otimes x)^p + \alpha(y \otimes 1 + 1 \otimes y)^p.

$$

In characteristic $p$, the Frobenius identity $(a + b)^p = a^p + b^p$ holds in any commutative ring (since $\binom{p}{i} \equiv 0 \pmod{p}$ for $0 < i < p$). Therefore

$$
\Delta(x^p + \alpha y^p) = (x^p + \alpha y^p) \otimes 1 + 1 \otimes (x^p + \alpha y^p),

$$

which lies in $I \otimes A + A \otimes I$ where $A = k[x,y]$. The counit sends $x, y \mapsto 0$, giving $\varepsilon(x^p + \alpha y^p) = 0$. The antipode sends $(x,y) \mapsto (-x,-y)$, giving $S(x^p + \alpha y^p) = (-x)^p + \alpha(-y)^p = -(x^p + \alpha y^p)$ (since $(-1)^p = -1$ in characteristic $p$, where $p$ is odd; for $p = 2$, $(-1)^2 = 1$ and $-(x^2 + \alpha y^2) = x^2 + \alpha y^2$ in characteristic 2, so the ideal is still preserved). Thus $G$ is a closed subgroup scheme of $\mathbb{G}_{a,k}^2$.

**Irreducibility over $k$.** The polynomial $f(x,y) = x^p + \alpha y^p$ is irreducible in $k[x,y]$. To prove this, suppose for contradiction that $f = gh$ with $g, h \in k[x,y]$ both of positive degree. Over the algebraic closure $\overline{k}$, we have $\alpha^{1/p} \in \overline{k}$ and $f = (x + \alpha^{1/p} y)^p$, so $\overline{k}[x,y]$ being a UFD forces $g = c(x + \alpha^{1/p}y)^a$ and $h = c'(x + \alpha^{1/p}y)^b$ for some $c, c' \in \overline{k}^\times$ and $a + b = p$ with $a, b \geq 1$.

Now $g \in k[x,y]$ has degree $a$. The coefficient of $y^a$ in $g$ is $c(\alpha^{1/p})^a = c \cdot \alpha^{a/p}$. The coefficient of $x^a$ in $g$ is $c$. Both lie in $k$, so $c \in k^\times$ and $c \cdot \alpha^{a/p} \in k$, giving $\alpha^{a/p} \in k$. Since $0 < a < p$ and $p$ is prime, $\gcd(a,p) = 1$, so there exist integers $r, s$ with $ra + sp = 1$. Then $\alpha^{1/p} = \alpha^{(ra + sp)/p} = (\alpha^{a/p})^r \cdot \alpha^s \in k$, contradicting $\alpha \notin k^p$.

Since $f$ is irreducible, the ideal $(f)$ is prime, and $G$ is integral (in particular, reduced and irreducible).

**$G$ is nowhere smooth.** The Jacobian matrix of the single defining equation $f = x^p + \alpha y^p$ is

$$
\left(\frac{\partial f}{\partial x}, \; \frac{\partial f}{\partial y}\right) = \left(px^{p-1}, \; \alpha p y^{p-1}\right) = (0, \; 0)

$$

since $\operatorname{char}(k) = p$. The Jacobian vanishes identically on all of $\mathbb{A}^2_k$, not just on $G$. For a hypersurface $V(f) \subset \mathbb{A}^n$ to be smooth at a point, the Jacobian must have rank 1 at that point. Since it has rank 0 everywhere, $G$ is singular at every point, i.e., nowhere smooth over $k$.

This is a purely inseparable phenomenon. Over a perfect field, the Frobenius is surjective, so $\alpha = \beta^p$ for some $\beta \in k$, and $x^p + \alpha y^p = (x + \beta y)^p$ is no longer irreducible --- the reduced scheme $V(x + \beta y)$ is a smooth line. The pathology arises precisely because $\alpha \notin k^p$.

**$G$ is not normal.** In the fraction field $K = \operatorname{Frac}(k[x,y]/(x^p + \alpha y^p))$, consider the element $\xi = x/y$. This satisfies the monic polynomial equation

$$
\xi^p = \frac{x^p}{y^p} = \frac{-\alpha y^p}{y^p} = -\alpha \in k \subset k[x,y]/(f).

$$

So $\xi$ is integral over the coordinate ring $k[x,y]/(f)$ (it is a root of $T^p + \alpha \in k[T]$). However, $\xi = x/y$ does not lie in $k[x,y]/(f)$ itself: in $k[x,y]/(f)$, the element $y$ is not a unit (it vanishes at the origin of $G$), and $x$ is not divisible by $y$ (since $x$ and $y$ are algebraically independent modulo the relation $x^p = -\alpha y^p$, and no polynomial relation $x = y \cdot q(x,y)$ can hold modulo $f$ for degree reasons). Therefore the integral closure of $k[x,y]/(f)$ strictly contains $k[x,y]/(f)$, so $G$ is not normal.

More explicitly, the normalization of $G$ is $\operatorname{Spec}(k[\xi])$ where $\xi^p = -\alpha$. The field $k(\xi) = k[T]/(T^p + \alpha)$ is a purely inseparable extension of $k$ of degree $p$, and $k[\xi]$ is a DVR (since $k[\xi]$ is a PID and $\xi$ generates the maximal ideal). The normalization map $\operatorname{Spec}(k[\xi]) \to G$ is a bijection on points but not an isomorphism of schemes --- it is a universal homeomorphism, another characteristically positive-characteristic phenomenon.

**Contrast with characteristic zero.** Over a field of characteristic zero, every algebraic group is smooth (Cartier's theorem). The proof uses the fact that the local ring at the identity has no nilpotents in the tangent space when the characteristic does not divide the order of the group scheme. More precisely, in characteristic zero, the category of finite group schemes is equivalent to the category of finite etale group schemes, and all connected group schemes are smooth. The example $G = V(x^p + \alpha y^p)$ shows that all of these results are specific to characteristic zero (or more precisely, to perfect fields).

<!-- BENCHMARK_PROBLEM: Let $k$ be a field of characteristic $p > 0$ with $\alpha \in k \setminus k^p$. Prove that the polynomial $f(x,y) = x^p + \alpha y^p$ is irreducible in $k[x,y]$ by analyzing its factorization over $\overline{k}$ and using the fact that $\gcd(a,p) = 1$ for $0 < a < p$. Show that the Jacobian matrix of $f$ vanishes identically in characteristic $p$, so that $V(f) \subset \mathbb{A}^2_k$ is an integral scheme that is nowhere smooth. Finally, prove that $V(f)$ is not normal by exhibiting the element $x/y$ in the fraction field that is integral over the coordinate ring but does not belong to it. -->
