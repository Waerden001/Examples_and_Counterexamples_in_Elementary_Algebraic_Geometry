---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/morphisms.tex
---

## Morphisms
### \'{Etale  related}

### Example: An \'{e}tale morphism, Hartshorne $\mathrm{III}.10.6$ {#ecag-0158}

Let $k$ be an algebraically closed field with $\operatorname{char}(k) \neq 2$, and let $Y = \operatorname{Spec}(k[x,y]/(y^2 - x^2(x+1)))$ be the nodal cubic. We construct a degree-2 etale morphism onto $Y$ from a smooth source by defining

$$
f: X = \operatorname{Spec}(k[s,t]/(t^2 - (s^2 - 1)^2)) \longrightarrow Y

$$

via the ring homomorphism $\varphi: k[x,y]/(y^2 - x^2(x+1)) \to k[s,t]/(t^2 - (s^2-1)^2)$ given by $x \mapsto s^2 - 1$ and $y \mapsto st$.

**Well-definedness.** The map $\varphi$ must send the defining relation of $\mathcal{O}(Y)$ to zero in $\mathcal{O}(X)$. We compute $\varphi(y^2 - x^2(x+1)) = s^2 t^2 - (s^2-1)^2 \cdot s^2 = s^2(t^2 - (s^2-1)^2)$, which vanishes in $\mathcal{O}(X)$ as required.

**The source scheme $X$.** The defining equation $t^2 = (s^2 - 1)^2$ factors as $(t - (s^2-1))(t + (s^2-1)) = 0$, so

$$
X \cong \operatorname{Spec}(k[s,t]/(t - s^2 + 1)) \sqcup \operatorname{Spec}(k[s,t]/(t + s^2 - 1)) \cong \mathbb{A}^1_k \sqcup \mathbb{A}^1_k,

$$

a disjoint union of two copies of the affine line, each parametrized by $s$. In particular, $X$ is smooth.

**Fibre over the node.** The node of $Y$ is the origin, corresponding to the maximal ideal $(x,y) \subset \mathcal{O}(Y)$. Setting $x = s^2 - 1 = 0$ and $y = st = 0$ in $\mathcal{O}(X)$ gives $s = \pm 1$ (using $\operatorname{char}(k) \neq 2$) and, since $s \neq 0$, forces $t = 0$. The scheme-theoretic fibre is therefore

$$
f^{-1}((0,0)) = \operatorname{Spec}(k[s]/(s^2 - 1)) \cong \operatorname{Spec}(k) \sqcup \operatorname{Spec}(k),

$$

consisting of two reduced $k$-rational points at $s = 1$ and $s = -1$.

**Flatness.** Since $f$ is a finite morphism between integral schemes and every fibre has the same degree 2 (two reduced points over every closed point of $Y$, as one verifies by examining generic and special fibres), $f$ is flat by the local criterion: for a finite morphism of Noetherian integral schemes, flatness is equivalent to constancy of the fibre degree.

**Etaleness.** A morphism is etale if and only if it is flat and unramified. Flatness was established above. For unramifiedness at a point $q \in X$ lying over $p \in Y$, we need two conditions: the residue field extension $k(p) \hookrightarrow k(q)$ is separable, and $\mathfrak{m}_p \cdot \mathcal{O}_{X,q} = \mathfrak{m}_q$. Both hold at every point: the residue fields are all $k$ (since $k$ is algebraically closed and all fibres consist of $k$-rational points), so the extension is trivially separable, and the fibre at each point is reduced, which gives $\mathfrak{m}_p \cdot \mathcal{O}_{X,q} = \mathfrak{m}_q$. Therefore $f$ is a degree-2 etale morphism.

The nodal cubic admits this etale cover by a smooth curve precisely because its singularity is an ordinary double point. The two branches of the node are separated in the cover, with each preimage point lying on a distinct component of $X$. This illustrates that etale morphisms capture the local topology (the two branches) without resolving the singularity in the algebro-geometric sense.

<!-- BENCHMARK_PROBLEM: Let $k$ be an algebraically closed field with $\operatorname{char}(k) \neq 2$, and let $Y = \operatorname{Spec}(k[x,y]/(y^2 - x^2(x+1)))$ be the nodal cubic. Consider the morphism $f: X = \operatorname{Spec}(k[s,t]/(t^2 - (s^2-1)^2)) \to Y$ defined by $x \mapsto s^2 - 1$, $y \mapsto st$. Compute the scheme-theoretic fibre $f^{-1}((x,y))$ over the node and determine whether $f$ is etale. Justify your answer by verifying flatness and unramifiedness. -->

### Remark {#ecag-0159}

The flatness of the morphism $f$ in the previous example can also be verified directly by localization. Let $\mathfrak{p} = (x,y) \subset \mathcal{O}(Y)$ be the prime corresponding to the node, and let $\mathfrak{q}_1 = (s-1, t)$ and $\mathfrak{q}_2 = (s+1, t)$ be the two primes of $\mathcal{O}(X)$ lying over $\mathfrak{p}$. One localizes the ring extension $\mathcal{O}(Y) \hookrightarrow \mathcal{O}(X)$ at $\mathfrak{p}$ and checks that each $\mathcal{O}(X)_{\mathfrak{q}_i}$ is a flat (equivalently, free) module over $\mathcal{O}(Y)_{\mathfrak{p}}$.

Since $\mathcal{O}(Y)_{\mathfrak{p}}$ is a one-dimensional local ring and each $\mathcal{O}(X)_{\mathfrak{q}_i}$ is a one-dimensional local domain, flatness reduces to two checkable conditions: the maximal ideal $\mathfrak{m}_{\mathfrak{p}}$ generates $\mathfrak{m}_{\mathfrak{q}_i}$ (which is precisely unramifiedness), and the module has no torsion (which holds automatically since $\mathcal{O}(X)_{\mathfrak{q}_i}$ is a domain and $\mathcal{O}(Y)_{\mathfrak{p}}$ is an integral domain).

More generally, for a finite morphism between integral Noetherian schemes, flatness is equivalent to constancy of the fibre degree. This follows from Grothendieck's generic flatness theorem (which gives flatness on a dense open) combined with the local criterion of flatness (which promotes generic flatness to global flatness when the fibre degree is constant). This algebraic criterion is often more practical than the differential approach via Kahler differentials.

<!-- BENCHMARK_PROBLEM: Let $f: X \to Y$ be the degree-2 morphism from the etale cover of the nodal cubic constructed in ecag-0158. Let $\mathfrak{p} = (x,y) \subset \mathcal{O}(Y)$ be the node, and let $\mathfrak{q}_1 = (s-1,t)$, $\mathfrak{q}_2 = (s+1,t) \subset \mathcal{O}(X)$ be the primes lying over $\mathfrak{p}$. Verify flatness of $f$ at $\mathfrak{q}_1$ by showing that $\mathcal{O}(X)_{\mathfrak{q}_1}$ is a free module over $\mathcal{O}(Y)_{\mathfrak{p}}$. -->

### Different Frobenius actions

Let $X$ be a scheme over $k = \mathbb{F}_p$ for a prime $p$, and let $\overline{X} = X \times_{\operatorname{Spec}(k)} \operatorname{Spec}(\overline{k})$ be the base change to the algebraic closure. There are four distinct Frobenius morphisms associated to this situation, each playing a different role in arithmetic geometry.

The **absolute (global) Frobenius** $F_{\overline{X}}: \overline{X} \to \overline{X}$ acts on the structure sheaf by $f \mapsto f^p$, raising every section to its $p$-th power. Over $k = \mathbb{F}_p$, this is $k$-linear since $a^p = a$ for all $a \in \mathbb{F}_p$ by Fermat's little theorem. This $k$-linearity fails over $\mathbb{F}_q$ for $q = p^r$ with $r > 1$.

The **relative Frobenius** $F_{X/k}: \overline{X} \to \overline{X}^{(p)}$ is defined as $F_{X/k} = 1_{\operatorname{Spec}(\overline{k})} \times_k F_X$, where $F_X: X \to X$ is the absolute Frobenius of $X$. When $k = \mathbb{F}_p$, we have $X^{(p)} \cong X$ (since the Frobenius twist is trivial on $\mathbb{F}_p$-schemes), so $F_{X/k}$ can be viewed as an endomorphism of $\overline{X}$. It is $\overline{k}$-linear because $a^p = a$ for $a \in \mathbb{F}_p$ on the structure side. Over $\mathbb{F}_q$ with $q \neq p$, the Frobenius twist $X^{(p)}$ is genuinely different from $X$.

The **arithmetic Frobenius** is $F_{\overline{k}} \times_k 1_X: \overline{X} \to \overline{X}$, which applies $a \mapsto a^p$ to the $\overline{k}$-coefficients while fixing the $X$-structure. The **geometric Frobenius** is $F_{\overline{k}}^{-1} \times_k 1_X: \overline{X} \to \overline{X}$, applying the inverse Frobenius $a \mapsto a^{1/p}$ to the $\overline{k}$-coefficients. The geometric Frobenius is the natural operator on etale cohomology and appears in the Grothendieck--Lefschetz trace formula.

**Explicit formulas for $X = \mathbb{A}^n_{\mathbb{F}_p}$.** Writing elements of $\mathcal{O}(\overline{X}) = \overline{k}[x_1, \ldots, x_n]$ as polynomials $\sum a_I x^I$ with $a_I \in \overline{k}$:

| Frobenius | Action on $\sum a_I x^I$ | Effect on coefficients | Effect on variables |
|-----------|--------------------------|----------------------|-------------------|
| Absolute | $\sum a_I^p x^{pI}$ | $a_I \mapsto a_I^p$ | $x_i \mapsto x_i^p$ |
| Relative | $\sum a_I x^{pI}$ | unchanged | $x_i \mapsto x_i^p$ |
| Arithmetic | $\sum a_I^p x^I$ | $a_I \mapsto a_I^p$ | unchanged |
| Geometric | $\sum a_I^{1/p} x^I$ | $a_I \mapsto a_I^{1/p}$ | unchanged |

The fundamental factorization is $F_{\overline{X}} = F_{X/k} \circ (\text{arithmetic Frobenius})$: the absolute Frobenius decomposes as the relative Frobenius followed by the arithmetic Frobenius. This is immediate from the table: raising both coefficients and variables to the $p$-th power is the same as first raising coefficients, then raising variables.

On $\overline{k}$-points, the absolute Frobenius acts as the identity on the underlying topological space (it is a morphism of locally ringed spaces that is a homeomorphism). The relative and geometric Frobenius both act as $(a_1, \ldots, a_n) \mapsto (a_1^p, \ldots, a_n^p)$ on $\overline{k}$-valued points. This is why the geometric Frobenius, rather than the arithmetic one, plays the central role in the Weil conjectures: its fixed points on $\overline{X}(\overline{k})$ are precisely the $\mathbb{F}_p$-rational points of $X$.

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{F}_p[x])$ and $\overline{X} = X \times_{\operatorname{Spec}(\mathbb{F}_p)} \operatorname{Spec}(\overline{\mathbb{F}_p})$. For the polynomial $f = \alpha x^2 + \beta x + \gamma \in \overline{\mathbb{F}_p}[x]$ where $\alpha, \beta, \gamma \in \overline{\mathbb{F}_p}$, write down explicitly the image of $f$ under each of the four Frobenius morphisms (absolute, relative, arithmetic, geometric). Verify that the absolute Frobenius equals the composition of the relative and arithmetic Frobenius. -->

### Remark {#ecag-0160}

The geometric Frobenius, rather than the arithmetic Frobenius, is the natural operator on $\ell$-adic cohomology $H^i_{\text{et}}(\overline{X}, \mathbb{Q}_\ell)$. Its eigenvalues satisfy the weight bounds predicted by the Weil conjectures (proved by Deligne): on $H^i_{\text{et}}(\overline{X}, \mathbb{Q}_\ell)$ for a smooth projective variety $X$ of dimension $d$ over $\mathbb{F}_q$, the eigenvalues of the geometric Frobenius are algebraic numbers of absolute value $q^{i/2}$ under every complex embedding.

The connection to point counting is through the Grothendieck--Lefschetz trace formula:

$$
\# X(\mathbb{F}_{q^n}) = \sum_{i=0}^{2d} (-1)^i \operatorname{Tr}(\operatorname{Frob}_q^n \mid H^i_{\text{et}}(\overline{X}, \mathbb{Q}_\ell)),

$$

where $\operatorname{Frob}_q$ denotes the geometric Frobenius. On $\overline{\mathbb{F}_q}$-points, the geometric Frobenius acts as $(x_1, \ldots, x_n) \mapsto (x_1^q, \ldots, x_n^q)$, and its fixed points are precisely the $\mathbb{F}_q$-rational points of $X$. This is the scheme-theoretic formulation of Weil's original insight connecting point counts to cohomological data. For a detailed treatment, see Goren, *Some remarks on Frobenius and Lefschetz in etale cohomology*.

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective curve of genus $g$ over $\mathbb{F}_q$. Using the Grothendieck--Lefschetz trace formula, express $\# X(\mathbb{F}_{q^n})$ in terms of the eigenvalues of the geometric Frobenius on $H^i_{\text{et}}(\overline{X}, \mathbb{Q}_\ell)$ for $i = 0, 1, 2$. State the Riemann hypothesis for curves (Weil's theorem) as a constraint on these eigenvalues. -->

## Global L-functions of zero-dimensional schemes
Let $X \rightarrow \operatorname{Spec}(\mathbb{Z})$ be a $0$-dimensional scheme over $\mathbb{Z}$. Since zero-dimensional schemes do not have the complication of bad reduction in the usual sense, the global zeta function of $X$ can be defined as

$$
\zeta(X, s) := \prod_{p} Z(X_p, p^{-s}),

$$

where $X_p = X \times_{\operatorname{Spec}(\mathbb{Z})} \operatorname{Spec}(\mathbb{F}_p)$ is the reduction of $X$ modulo $p$, and $Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{\# X_p(\mathbb{F}_{p^n})}{n} t^n \right)$ is the local zeta function.

### Example: Empty scheme {#ecag-0161}

The empty scheme $X = \emptyset = \operatorname{Spec}(0)$ over $\operatorname{Spec}(\mathbb{Z})$ has the simplest possible zeta function. For any prime $p$, the reduction modulo $p$ is

$$
X_p = \operatorname{Spec}(0 \otimes_{\mathbb{Z}} \mathbb{F}_p) = \operatorname{Spec}(0) = \emptyset,

$$

which has no points over any field extension: $\# X_p(\mathbb{F}_{p^n}) = 0$ for all $n \geq 1$. The local zeta function is therefore

$$
Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{0}{n} t^n\right) = e^0 = 1,

$$

and the global zeta function is

$$
\zeta(\emptyset, s) = \prod_p 1 = 1.

$$

This is consistent with the multiplicativity of the zeta function under disjoint union: $\zeta(X \sqcup \emptyset, s) = \zeta(X, s) \cdot \zeta(\emptyset, s) = \zeta(X, s)$. The empty scheme is the identity element for the monoid of isomorphism classes of schemes over $\operatorname{Spec}(\mathbb{Z})$ under disjoint union, and $\zeta(\emptyset, s) = 1$ is the corresponding identity in the multiplicative group of Dirichlet series.

<!-- BENCHMARK_PROBLEM: Let $X = \emptyset$ be the empty scheme over $\operatorname{Spec}(\mathbb{Z})$. Compute the local zeta function $Z(X_p, t)$ for every prime $p$ and the global zeta function $\zeta(X, s)$. Express your answers in closed form. -->

### Example {#ecag-0162}

The scheme $X = \operatorname{Spec}(\mathbb{Z})$ over itself (via the identity morphism) has zeta function equal to the Riemann zeta function. For each prime $p$, the fibre is

$$
X_p = \operatorname{Spec}(\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{F}_p) = \operatorname{Spec}(\mathbb{F}_p),

$$

a single closed point with residue field $\mathbb{F}_p$. For every $n \geq 1$, there is exactly one $\mathbb{F}_p$-algebra homomorphism $\mathbb{F}_p \to \mathbb{F}_{p^n}$ (the canonical inclusion), so $\# X_p(\mathbb{F}_{p^n}) = 1$.

The local zeta function is

$$
Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{t^n}{n}\right) = \exp(-\ln(1 - t)) = \frac{1}{1 - t},

$$

using the Taylor series $-\ln(1 - t) = \sum_{n=1}^{\infty} t^n/n$ for $|t| < 1$. The global zeta function is

$$
\zeta(X, s) = \prod_p \frac{1}{1 - p^{-s}}.

$$

By the Euler product formula, this equals the Riemann zeta function:

$$
\prod_p \frac{1}{1 - p^{-s}} = \sum_{n=1}^{\infty} \frac{1}{n^s} = \zeta(s),

$$

converging for $\operatorname{Re}(s) > 1$. The Euler product identity follows from unique factorization in $\mathbb{Z}$: expanding each geometric series $\frac{1}{1-p^{-s}} = \sum_{k=0}^{\infty} p^{-ks}$ and multiplying over all primes recovers every positive integer $n = \prod p_i^{k_i}$ exactly once.

The scheme $\operatorname{Spec}(\mathbb{Z})$ is the terminal object in the category of schemes, and the fact that its zeta function recovers the Riemann zeta function shows that the scheme-theoretic zeta function is a direct generalization of the most fundamental object of analytic number theory.

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{Z})$. Compute the local zeta function $Z(X_p, t)$ for each prime $p$ by first determining $\# X_p(\mathbb{F}_{p^n})$ for all $n \geq 1$, and then show that the global zeta function $\zeta(X, s) = \prod_p Z(X_p, p^{-s})$ equals the Riemann zeta function $\sum_{n=1}^{\infty} n^{-s}$. -->

### Example: Two points {#ecag-0163}

Consider $X = \operatorname{Spec}(\mathbb{Z}[x]/(x(x-1)))$, which by the Chinese Remainder Theorem decomposes as

$$
X = \operatorname{Spec}(\mathbb{Z}[x]/(x) \times \mathbb{Z}[x]/(x-1)) \cong \operatorname{Spec}(\mathbb{Z}) \sqcup \operatorname{Spec}(\mathbb{Z}),

$$

a disjoint union of two copies of $\operatorname{Spec}(\mathbb{Z})$. (The CRT applies because $x$ and $x - 1$ generate the unit ideal in $\mathbb{Z}[x]$: they satisfy $1 = x - (x-1)$.)

For any prime $p$, the elements $0$ and $1$ remain distinct in $\mathbb{F}_p$, so $x$ and $x-1$ remain coprime in $\mathbb{F}_p[x]$, giving

$$
X_p = \operatorname{Spec}(\mathbb{F}_p[x]/(x(x-1))) \cong \operatorname{Spec}(\mathbb{F}_p) \sqcup \operatorname{Spec}(\mathbb{F}_p).

$$

Each component contributes one point over every extension, so $\# X_p(\mathbb{F}_{p^n}) = 2$ for all $n \geq 1$. The local zeta function is

$$
Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{2}{n} t^n\right) = \exp(-2\ln(1-t)) = \frac{1}{(1-t)^2}.

$$

The global zeta function is therefore

$$
\zeta(X, s) = \prod_p \frac{1}{(1-p^{-s})^2} = \left(\prod_p \frac{1}{1-p^{-s}}\right)^2 = \zeta(s)^2.

$$

This illustrates the multiplicativity of the zeta function under disjoint union: since $X \cong \operatorname{Spec}(\mathbb{Z}) \sqcup \operatorname{Spec}(\mathbb{Z})$, we get $\zeta(X, s) = \zeta(\operatorname{Spec}(\mathbb{Z}), s)^2 = \zeta(s)^2$. Point counts add under disjoint union, exponents in the local zeta function add, and the global zeta function multiplies.

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{Z}[x]/(x(x-1)))$ viewed as a scheme over $\operatorname{Spec}(\mathbb{Z})$. Compute $\# X_p(\mathbb{F}_{p^n})$ for all primes $p$ and all $n \geq 1$, determine the local zeta function $Z(X_p, t)$, and express the global zeta function $\zeta(X, s)$ in terms of the Riemann zeta function. -->

### Example {#ecag-0164}

The scheme $X = \operatorname{Spec}(\mathbb{Z}[x]/(x^2 - x - 1))$ provides the simplest nontrivial instance of the Dedekind zeta function factorization. The polynomial $x^2 - x - 1$ has discriminant $\Delta = 1 + 4 = 5$, its splitting field is $\mathbb{Q}(\sqrt{5})$, and $\mathbb{Z}[x]/(x^2 - x - 1) \cong \mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right] = \mathcal{O}_{\mathbb{Q}(\sqrt{5})}$ is the ring of integers of $\mathbb{Q}(\sqrt{5})$.

**Splitting behavior of primes.** The structure of the fibre $X_p$ is governed by the factorization of $x^2 - x - 1$ modulo $p$. By quadratic reciprocity (applicable since $5 \equiv 1 \pmod{4}$, so $\left(\frac{5}{p}\right) = \left(\frac{p}{5}\right)$), there are three cases:

- **Ramified** ($p = 5$): We have $x^2 - x - 1 \equiv (x - 3)^2 \pmod{5}$, so $X_5 = \operatorname{Spec}(\mathbb{F}_5[x]/(x-3)^2)$, a fat point supported at $x = 3$.

- **Split** ($\left(\frac{p}{5}\right) = 1$, i.e., $p \equiv \pm 1 \pmod{5}$): The polynomial $x^2 - x - 1$ has two distinct roots in $\mathbb{F}_p$, so $X_p \cong \operatorname{Spec}(\mathbb{F}_p) \sqcup \operatorname{Spec}(\mathbb{F}_p)$.

- **Inert** ($\left(\frac{p}{5}\right) = -1$, i.e., $p \equiv \pm 2 \pmod{5}$): The polynomial $x^2 - x - 1$ is irreducible over $\mathbb{F}_p$, so $X_p \cong \operatorname{Spec}(\mathbb{F}_{p^2})$, a single closed point with residue field $\mathbb{F}_{p^2}$.

**Local zeta functions.** For $p = 5$: a ring homomorphism $\mathbb{F}_5[x]/(x-3)^2 \to \mathbb{F}_{5^n}$ must send $x$ to an element satisfying $(x-3)^2 = 0$; since $\mathbb{F}_{5^n}$ is reduced, this forces $x = 3$, so $\# X_5(\mathbb{F}_{5^n}) = 1$ and $Z(X_5, t) = \frac{1}{1 - t}$.

For split primes: $\# X_p(\mathbb{F}_{p^n}) = 2$ for all $n \geq 1$, giving $Z(X_p, t) = \frac{1}{(1-t)^2}$.

For inert primes: an $\mathbb{F}_{p^n}$-point of $\operatorname{Spec}(\mathbb{F}_{p^2})$ is a homomorphism $\mathbb{F}_{p^2} \to \mathbb{F}_{p^n}$, which exists if and only if $2 \mid n$. So $\# X_p(\mathbb{F}_{p^n}) = 1$ if $2 \mid n$ and $0$ otherwise, giving

$$
Z(X_p, t) = \exp\left(\sum_{m=1}^{\infty} \frac{t^{2m}}{m}\right) = \frac{1}{1 - t^2} = \frac{1}{(1-t)(1+t)}.

$$

**Global zeta function.** Assembling the Euler product:

$$
\zeta(X, s) = \frac{1}{1 - 5^{-s}} \cdot \prod_{\substack{p \neq 5 \\ \left(\frac{p}{5}\right) = 1}} \frac{1}{(1 - p^{-s})^2} \cdot \prod_{\substack{p \neq 5 \\ \left(\frac{p}{5}\right) = -1}} \frac{1}{(1 - p^{-s})(1 + p^{-s})}.

$$

Each local factor can be rewritten uniformly. For split primes, $\frac{1}{(1-p^{-s})^2} = \frac{1}{1-p^{-s}} \cdot \frac{1}{1-\left(\frac{p}{5}\right)p^{-s}}$ since $\left(\frac{p}{5}\right) = 1$. For inert primes, $\frac{1}{(1-p^{-s})(1+p^{-s})} = \frac{1}{1-p^{-s}} \cdot \frac{1}{1-\left(\frac{p}{5}\right)p^{-s}}$ since $\left(\frac{p}{5}\right) = -1$. Therefore

$$
\zeta(X, s) = \prod_p \frac{1}{1 - p^{-s}} \cdot \prod_{p \neq 5} \frac{1}{1 - \left(\frac{p}{5}\right) p^{-s}} = \zeta(s) \cdot L(\chi, s),

$$

where $\chi = \left(\frac{\cdot}{5}\right)$ is the Legendre symbol character modulo 5, and

$$
L(\chi, s) = \prod_{p \neq 5} \frac{1}{1 - \chi(p) p^{-s}} = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}

$$

is the associated Dirichlet $L$-function (with the convention $\chi(5) = 0$, so the factor at $p = 5$ is absorbed).

**Verification.** We check the first few primes:

| $p$ | $p \bmod 5$ | $\left(\frac{p}{5}\right)$ | Type | $X_p$ | $Z(X_p, t)$ |
|-----|------------|----------------------------|------|--------|-------------|
| $2$ | $2$ | $-1$ | inert | $\operatorname{Spec}(\mathbb{F}_4)$ | $\frac{1}{1-t^2}$ |
| $3$ | $3$ | $-1$ | inert | $\operatorname{Spec}(\mathbb{F}_9)$ | $\frac{1}{1-t^2}$ |
| $5$ | $0$ | $0$ | ramified | $\operatorname{Spec}(\mathbb{F}_5[x]/(x-3)^2)$ | $\frac{1}{1-t}$ |
| $7$ | $2$ | $-1$ | inert | $\operatorname{Spec}(\mathbb{F}_{49})$ | $\frac{1}{1-t^2}$ |
| $11$ | $1$ | $1$ | split | $\operatorname{Spec}(\mathbb{F}_{11})^{\sqcup 2}$ | $\frac{1}{(1-t)^2}$ |

For $p = 11$: we verify that $x^2 - x - 1 \equiv 0 \pmod{11}$ has roots $x = \frac{1 \pm \sqrt{5}}{2}$. Since $4 \cdot 5 = 20 \equiv 9 \pmod{11}$ and $\sqrt{9} = \pm 3$ in $\mathbb{F}_{11}$, the discriminant $\sqrt{5}$ equals $\pm 3 \cdot 2^{-1} \cdot 2 = \pm 3$ (more directly, $4^2 = 16 \equiv 5$, so $\sqrt{5} = \pm 4$), giving roots $x = \frac{1 \pm 4}{2} \equiv \frac{5}{2}, \frac{-3}{2} \equiv 8, 4 \pmod{11}$. Indeed $8^2 - 8 - 1 = 55 \equiv 0$ and $4^2 - 4 - 1 = 11 \equiv 0 \pmod{11}$.

This factorization $\zeta_{\mathbb{Q}(\sqrt{5})}(s) = \zeta(s) \cdot L(\chi, s)$ is a special case of the general result that the Dedekind zeta function of an abelian extension $K/\mathbb{Q}$ factors as a product of Dirichlet $L$-functions, one for each character of $\operatorname{Gal}(K/\mathbb{Q})$.

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{Z}[x]/(x^2 - x - 1))$ over $\operatorname{Spec}(\mathbb{Z})$. (a) Determine the structure of the fibre $X_p$ for $p = 2, 3, 5, 7, 11$, specifying whether $p$ is split, inert, or ramified in $\mathbb{Q}(\sqrt{5})$. (b) Compute the local zeta function $Z(X_p, t)$ for each of these primes. (c) Show that the global zeta function satisfies $\zeta(X, s) = \zeta(s) \cdot L(\chi, s)$ where $\chi$ is the quadratic character modulo $5$. -->
