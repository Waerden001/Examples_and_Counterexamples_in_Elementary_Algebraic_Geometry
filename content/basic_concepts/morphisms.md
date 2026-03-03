---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/morphisms.tex
---

## Morphisms
### \'{Etale  related}

### Example: An \'{e}tale morphism, Hartshorne $\mathrm{III}.10.6$ {#ecag-0158}

**Statement:** Let $k$ be an algebraically closed field with $\operatorname{char}(k) \neq 2$. There exists a degree $2$ etale morphism from a disjoint union of two copies of $\mathbb{A}_k^1$ to the nodal cubic curve $Y = \operatorname{Spec}(k[x,y]/(y^2 - x^2(x+1)))$.

**Construction/Proof:** Define the morphism

$$
f: X = \operatorname{Spec}(k[s,t]/(t^2 - (s^2 - 1)^2)) \rightarrow \operatorname{Spec}(k[x,y]/(y^2 - x^2(x+1))) = Y

$$

by the ring map $x \mapsto s^2 - 1$, $y \mapsto st$.

**Step 1 (Well-definedness):** We must verify that the relations in $\mathcal{O}(Y)$ are preserved. We check $y^2 - x^2(x+1)$: under the map, $y^2 = s^2 t^2$ and $x^2(x+1) = (s^2-1)^2 \cdot s^2$. So $y^2 - x^2(x+1) = s^2 t^2 - s^2(s^2-1)^2 = s^2(t^2 - (s^2-1)^2)$, which vanishes in $\mathcal{O}(X)$.

**Step 2 (Fibre over the node):** The node of $Y$ is the origin $(x,y)$. The fibre over this point is

$$
X_0 = X \times_Y \operatorname{Spec}(k) = \operatorname{Spec}\left( k[s,t]/(t^2 - (s^2-1)^2) \otimes_{k[x,y]/(y^2 - x^2(x+1))} k[x,y]/(x,y) \right).

$$

Setting $x = s^2 - 1 = 0$ and $y = st = 0$ in $\mathcal{O}(X)$ gives the conditions $s^2 = 1$ and $st = 0$. Since $s = \pm 1 \neq 0$, we must have $t = 0$. Thus

$$
X_0 = \operatorname{Spec}(k[s,t]/(t, s^2 - 1)) = \operatorname{Spec}(k[s]/(s^2 - 1)) \cong \operatorname{Spec}(k) \sqcup \operatorname{Spec}(k),

$$

which consists of two reduced points (here we use $\operatorname{char}(k) \neq 2$).

**Step 3 (Flatness):** Each fibre of $f$ over a closed point of $Y$ consists of exactly two points (counted with multiplicity), and in fact all fibres are reduced of degree $2$. Since the domain and target are both integral schemes and $f$ is a finite morphism of constant fibre degree, $f$ is flat. More precisely, $\mathcal{O}(X)$ is a free $\mathcal{O}(Y)$-module of rank $2$.

**Step 4 (Etaleness):** The morphism $f$ is of finite presentation (it is finite). To verify smoothness, we check that the map on differentials $f^* \Omega_{Y/k} \rightarrow \Omega_{X/k}$ is an isomorphism. Since $X$ and $Y$ are both curves (of dimension $1$), this means $f$ is smooth of relative dimension $0$. A smooth morphism of relative dimension $0$ is etale. Equivalently, $f$ is flat and unramified: at each point $q \in X$ mapping to $p \in Y$, the induced map on residue fields is a separable extension, and $\mathfrak{m}_p \cdot \mathcal{O}_{X,q} = \mathfrak{m}_q$. Both conditions are satisfied since every fibre is reduced and consists of $k$-rational points. Therefore $f$ is a degree $2$ etale morphism.

**Key Insight:** The nodal cubic admits an etale cover by a smooth curve precisely because the node is an ordinary double point. The two branches of the node are "separated" in the cover, with each preimage point lying on a distinct branch. This illustrates that etale morphisms can resolve the topology (but not the singularity) of nodal curves.

**Prerequisites:** Etale morphisms, flatness criteria, Kahler differentials, nodal curves, fibre products of schemes

<!-- BENCHMARK_PROBLEM: Let $k$ be an algebraically closed field with $\operatorname{char}(k) \neq 2$, and let $Y = \operatorname{Spec}(k[x,y]/(y^2 - x^2(x+1)))$ be the nodal cubic. Consider the morphism $f: X = \operatorname{Spec}(k[s,t]/(t^2 - (s^2-1)^2)) \to Y$ defined by $x \mapsto s^2 - 1$, $y \mapsto st$. Compute the scheme-theoretic fibre $f^{-1}((x,y))$ over the node and determine whether $f$ is etale. Justify your answer by verifying flatness and unramifiedness. -->

### Remark {#ecag-0159}

One may ask whether there is a more direct way to verify the flatness of the morphism $f$ from the previous example using localization. Let $\mathfrak{p} = (x,y) \subset k[x,y]/(y^2 - x^2(x+1))$ be the prime ideal corresponding to the node, and let $\mathfrak{q}_1 = (s-1, t)$ and $\mathfrak{q}_2 = (s+1, t)$ be the two primes of $\mathcal{O}(X)$ lying over $\mathfrak{p}$. One approach is to localize the ring extension $\mathcal{O}(Y) \hookrightarrow \mathcal{O}(X)$ at $\mathfrak{p}$ and verify that $\mathcal{O}(X)_{\mathfrak{q}_i}$ is a flat (equivalently, free) module over $\mathcal{O}(Y)_{\mathfrak{p}}$ for $i = 1, 2$. Since $\mathcal{O}(Y)_{\mathfrak{p}}$ is a one-dimensional local ring and each $\mathcal{O}(X)_{\mathfrak{q}_i}$ is a one-dimensional local domain, flatness can be checked by verifying that the maximal ideal $\mathfrak{m}_{\mathfrak{p}}$ generates $\mathfrak{m}_{\mathfrak{q}_i}$ (unramifiedness) and that there is no torsion. Alternatively, for a finite morphism between integral Noetherian schemes, flatness is equivalent to constancy of the fibre degree (by Grothendieck's generic flatness combined with the local criterion of flatness). This provides a more computational approach than the differential criterion used above.

### Different Frobenius actions

Let $X$ be a scheme over $k = \mathbb{F}_p$, where $p$ is a prime, and let $\overline{X} = X \times_{\operatorname{Spec}(k)} \operatorname{Spec}(\overline{k})$ be the base change to the algebraic closure. There are four distinct Frobenius morphisms associated to this situation:

- **Global (absolute) Frobenius** $F_{\overline{X}}$: This is the morphism $\overline{X} \to \overline{X}$ that acts on the structure sheaf by $f \mapsto f^p$, raising every section to its $p$-th power. Over $k = \mathbb{F}_p$, this is a $k$-linear morphism since $a^p = a$ for all $a \in \mathbb{F}_p$. This $k$-linearity fails over $\mathbb{F}_q$ for $q = p^r$ with $r > 1$.

- **Relative Frobenius** $F_{X/k}$: This is defined as $F_{X/k} = 1_{\operatorname{Spec}(\overline{k})} \times_k F_X$, where $F_X: X \to X$ is the absolute Frobenius of $X$. It is a morphism $\overline{X} \to \overline{X}^{(p)}$ (or $\overline{X} \to \overline{X}$ when $k = \mathbb{F}_p$ since $X^{(p)} \cong X$ in that case). The relative Frobenius is an $\overline{k}$-linear map because $a^p = a$ for $a \in \mathbb{F}_p$ on the coefficient side. Over $\mathbb{F}_q$ with $q \neq p$, one must distinguish between $X$ and $X^{(p)}$, since the Frobenius twist is nontrivial.

- **Arithmetic Frobenius**: This is the morphism $F_{\overline{k}} \times_k 1_X: \overline{X} \to \overline{X}$, which acts by applying the Frobenius $a \mapsto a^p$ to the geometric fibre (i.e., to the $\overline{k}$-coefficients) while fixing the $X$-structure.

- **Geometric Frobenius**: This is the morphism $F_{\overline{k}}^{-1} \times_k 1_X: \overline{X} \to \overline{X}$, which acts by applying the inverse Frobenius $a \mapsto a^{1/p}$ to the $\overline{k}$-coefficients. The geometric Frobenius is the one that acts naturally on etale cohomology and appears in the Grothendieck--Lefschetz trace formula.

**Explicit description for affine space.** In the case $X = \operatorname{Spec}(\mathbb{F}_p[x_1, \ldots, x_n])$, writing elements as polynomials $\sum a_I x^I$ with $a_I \in \overline{k}$:
- The global Frobenius sends $\sum a_I x^I \mapsto \sum a_I^p x^{pI}$ (raises everything to the $p$-th power).
- The relative Frobenius sends $\sum a_I x^I \mapsto \sum a_I x^{pI}$ (raises variables to the $p$-th power, fixes coefficients).
- The arithmetic Frobenius sends $\sum a_I x^I \mapsto \sum a_I^p x^I$ (raises coefficients to the $p$-th power, fixes variables).
- The geometric Frobenius sends $\sum a_I x^I \mapsto \sum a_I^{1/p} x^I$ (takes $p$-th roots of coefficients, fixes variables).

Note the fundamental relation: $F_{\overline{X}} = F_{X/k} \circ (\text{arithmetic Frobenius})$, i.e., the absolute Frobenius factors as the composition of the relative and arithmetic Frobenius morphisms. On $\overline{k}$-points, the global Frobenius is the identity map (since it is a morphism of $\overline{k}$-schemes that equals the identity on topological spaces), while the relative and geometric Frobenius both act as the map $(a_1, \ldots, a_n) \mapsto (a_1^p, \ldots, a_n^p)$ on $\overline{k}$-points.

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{F}_p[x])$ and $\overline{X} = X \times_{\operatorname{Spec}(\mathbb{F}_p)} \operatorname{Spec}(\overline{\mathbb{F}_p})$. For the polynomial $f = \alpha x^2 + \beta x + \gamma \in \overline{\mathbb{F}_p}[x]$ where $\alpha, \beta, \gamma \in \overline{\mathbb{F}_p}$, write down explicitly the image of $f$ under each of the four Frobenius morphisms (global, relative, arithmetic, geometric). Verify that the global Frobenius equals the composition of the relative and arithmetic Frobenius. -->

### Remark {#ecag-0160}

For a detailed treatment of the interplay between the various Frobenius morphisms and the Lefschetz trace formula in etale cohomology, see [Some remarks on Frobenius and Lefschetz in etale cohomology](http://www.math.mcgill.ca/goren/SeminarOnCohomology/Frobenius.pdf) by E. Goren. In particular, that reference clarifies the role of the geometric Frobenius (rather than the arithmetic Frobenius) as the natural operator on $\ell$-adic cohomology $H^i_{\text{et}}(\overline{X}, \mathbb{Q}_\ell)$, since its eigenvalues satisfy the weight bounds predicted by the Weil conjectures (proved by Deligne). The key point is that on $\overline{\mathbb{F}_q}$-points, the geometric Frobenius acts as $(x_1, \ldots, x_n) \mapsto (x_1^q, \ldots, x_n^q)$, and its fixed points are precisely the $\mathbb{F}_q$-rational points of $X$, which connects the Grothendieck--Lefschetz trace formula to point counting.

## Global L-functions of zero-dimensional schemes
Let $X \rightarrow \operatorname{Spec}(\mathbb{Z})$ be a $0$-dimensional scheme over $\mathbb{Z}$. Since zero-dimensional schemes do not have the complication of bad reduction in the usual sense, the global zeta function of $X$ can be defined as

$$
\zeta(X, s) := \prod_{p} Z(X_p, p^{-s}),

$$

where $X_p = X \times_{\operatorname{Spec}(\mathbb{Z})} \operatorname{Spec}(\mathbb{F}_p)$ is the reduction of $X$ modulo $p$, and $Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{\# X_p(\mathbb{F}_{p^n})}{n} t^n \right)$ is the local zeta function.

### Example: Empty scheme {#ecag-0161}

**Statement:** The global zeta function of the empty scheme $X = \emptyset$ over $\operatorname{Spec}(\mathbb{Z})$ equals $1$.

**Construction/Proof:** Let $X = \emptyset = \operatorname{Spec}(0) \to \operatorname{Spec}(\mathbb{Z})$, where $0$ denotes the zero ring. For any prime $p$, the reduction modulo $p$ is

$$
X_p = \operatorname{Spec}(0 \otimes_{\mathbb{Z}} \mathbb{F}_p) = \operatorname{Spec}(0) = \emptyset.

$$

Since $X_p$ is empty, it has no points over any field extension: $\# X_p(\mathbb{F}_{p^n}) = 0$ for all $n \geq 1$. Therefore the local zeta function is

$$
Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{0}{n} t^n\right) = \exp(0) = 1.

$$

The global zeta function is then

$$
\zeta(\emptyset, s) = \prod_p Z(X_p, p^{-s}) = \prod_p 1 = 1.

$$

**Key Insight:** The empty scheme serves as the identity element for the zeta function under disjoint union of schemes, since $\zeta(X \sqcup \emptyset, s) = \zeta(X, s) \cdot \zeta(\emptyset, s) = \zeta(X, s)$. This is consistent with the fact that the empty product equals $1$.

**Prerequisites:** Local zeta function, global zeta function, base change of schemes

<!-- BENCHMARK_PROBLEM: Let $X = \emptyset$ be the empty scheme over $\operatorname{Spec}(\mathbb{Z})$. Compute the local zeta function $Z(X_p, t)$ for every prime $p$ and the global zeta function $\zeta(X, s)$. Express your answers in closed form. -->

### Example {#ecag-0162}

**Statement:** The global zeta function of $X = \operatorname{Spec}(\mathbb{Z})$ over itself equals the Riemann zeta function $\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$.

**Construction/Proof:** Let $X = \operatorname{Spec}(\mathbb{Z}) \to \operatorname{Spec}(\mathbb{Z})$ be the identity morphism. For each prime $p$, the fibre is

$$
X_p = \operatorname{Spec}(\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{F}_p) = \operatorname{Spec}(\mathbb{F}_p),

$$

which is a single closed point with residue field $\mathbb{F}_p$. For every $n \geq 1$, there is exactly one $\mathbb{F}_p$-algebra homomorphism $\mathbb{F}_p \to \mathbb{F}_{p^n}$ (the inclusion), so $\# X_p(\mathbb{F}_{p^n}) = 1$.

The local zeta function is therefore

$$
Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{1}{n} t^n\right) = \exp(-\ln(1 - t)) = \frac{1}{1 - t}.

$$

Here we used the Taylor series $-\ln(1 - t) = \sum_{n=1}^{\infty} \frac{t^n}{n}$ for $|t| < 1$. The global zeta function is

$$
\zeta(X, s) = \prod_p Z(X_p, p^{-s}) = \prod_p \frac{1}{1 - p^{-s}}.

$$

By the Euler product formula, this equals the Riemann zeta function:

$$
\prod_p \frac{1}{1 - p^{-s}} = \sum_{n=1}^{\infty} \frac{1}{n^s} = \zeta(s),

$$

which converges for $\operatorname{Re}(s) > 1$.

**Key Insight:** The scheme $\operatorname{Spec}(\mathbb{Z})$ is the terminal object in the category of schemes, and its zeta function recovers the most fundamental object of analytic number theory. This example illustrates that the scheme-theoretic zeta function is a vast generalization of the Riemann zeta function: for any scheme $X$ of finite type over $\mathbb{Z}$, the zeta function $\zeta(X, s)$ encodes arithmetic information about the reductions of $X$ modulo all primes.

**Prerequisites:** Euler product formula, Riemann zeta function, local zeta function, base change

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{Z})$. Compute the local zeta function $Z(X_p, t)$ for each prime $p$ by first determining $\# X_p(\mathbb{F}_{p^n})$ for all $n \geq 1$, and then show that the global zeta function $\zeta(X, s) = \prod_p Z(X_p, p^{-s})$ equals the Riemann zeta function $\sum_{n=1}^{\infty} n^{-s}$. -->

### Example: Two points {#ecag-0163}

**Statement:** The global zeta function of $X = \operatorname{Spec}(\mathbb{Z}[x]/(x(x-1)))$, the disjoint union of two copies of $\operatorname{Spec}(\mathbb{Z})$, equals $\zeta(s)^2$, the square of the Riemann zeta function.

**Construction/Proof:** The ring $\mathbb{Z}[x]/(x(x-1)) \cong \mathbb{Z}[x]/(x) \times \mathbb{Z}[x]/(x-1) \cong \mathbb{Z} \times \mathbb{Z}$ by the Chinese Remainder Theorem (since $x$ and $x - 1$ are coprime). Therefore

$$
X = \operatorname{Spec}(\mathbb{Z} \times \mathbb{Z}) \cong \operatorname{Spec}(\mathbb{Z}) \sqcup \operatorname{Spec}(\mathbb{Z}).

$$

For any prime $p$, reducing modulo $p$:

$$
X_p = \operatorname{Spec}(\mathbb{F}_p[x]/(x(x-1))) \cong \operatorname{Spec}(\mathbb{F}_p) \sqcup \operatorname{Spec}(\mathbb{F}_p),

$$

since $x$ and $x - 1$ remain coprime in $\mathbb{F}_p[x]$ for all primes $p$ (note $0 \neq 1$ in $\mathbb{F}_p$ for every prime $p$). Thus $\# X_p(\mathbb{F}_{p^n}) = 2$ for all $n \geq 1$.

The local zeta function is

$$
Z(X_p, t) = \exp\left(\sum_{n=1}^{\infty} \frac{2}{n} t^n\right) = \exp(-2\ln(1-t)) = \frac{1}{(1-t)^2}.

$$

The global zeta function is

$$
\zeta(X, s) = \prod_p \frac{1}{(1-p^{-s})^2} = \left(\prod_p \frac{1}{1-p^{-s}}\right)^2 = \zeta(s)^2.

$$

**Key Insight:** The zeta function is multiplicative under disjoint union: $\zeta(X \sqcup Y, s) = \zeta(X, s) \cdot \zeta(Y, s)$, since the point counts and hence the local zeta functions factor accordingly. This example is the simplest nontrivial instance of this principle.

**Prerequisites:** Chinese Remainder Theorem, Riemann zeta function, local zeta function, Euler product

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{Z}[x]/(x(x-1)))$ viewed as a scheme over $\operatorname{Spec}(\mathbb{Z})$. Compute $\# X_p(\mathbb{F}_{p^n})$ for all primes $p$ and all $n \geq 1$, determine the local zeta function $Z(X_p, t)$, and express the global zeta function $\zeta(X, s)$ in terms of the Riemann zeta function. -->

### Example {#ecag-0164}

**Statement:** The global zeta function of $X = \operatorname{Spec}(\mathbb{Z}[x]/(x^2 - x - 1))$ equals $\zeta(s) \cdot L(\chi, s)$, where $\zeta(s)$ is the Riemann zeta function and $L(\chi, s)$ is the Dirichlet $L$-function for the Legendre symbol character $\chi = \left(\frac{\cdot}{5}\right)$, the quadratic character modulo $5$.

**Construction/Proof:** The polynomial $x^2 - x - 1$ has discriminant $\Delta = 1 + 4 = 5$. Its splitting field is $\mathbb{Q}(\sqrt{5})$, and $\mathbb{Z}[x]/(x^2 - x - 1) \cong \mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$ is the ring of integers of $\mathbb{Q}(\sqrt{5})$.

**Step 1 (Splitting behavior by quadratic reciprocity):** The behavior of $X_p$ is governed by the splitting of $p$ in $\mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$, which depends on the Legendre symbol $\left(\frac{5}{p}\right) = \left(\frac{p}{5}\right)$ (by quadratic reciprocity, since $5 \equiv 1 \pmod{4}$):

- If $p = 5$ (ramified): $x^2 - x - 1 \equiv (x - 3)^2 \pmod{5}$, so $X_5 = \operatorname{Spec}(\mathbb{F}_5[x]/(x-3)^2)$, a fat point.
- If $\left(\frac{p}{5}\right) = 1$, i.e., $p \equiv 1, 4 \pmod{5}$ (split): $x^2 - x - 1$ factors into two distinct linear factors in $\mathbb{F}_p[x]$, so $X_p \cong \operatorname{Spec}(\mathbb{F}_p) \sqcup \operatorname{Spec}(\mathbb{F}_p)$.
- If $\left(\frac{p}{5}\right) = -1$, i.e., $p \equiv 2, 3 \pmod{5}$ (inert): $x^2 - x - 1$ is irreducible over $\mathbb{F}_p$, so $X_p \cong \operatorname{Spec}(\mathbb{F}_{p^2})$, a single closed point with residue field $\mathbb{F}_{p^2}$.

**Step 2 (Local zeta functions):**

*Case $p = 5$:* The scheme $\operatorname{Spec}(\mathbb{F}_5[x]/(x-3)^2)$ has the same $\mathbb{F}_{p^n}$-points as $\operatorname{Spec}(\mathbb{F}_5[x]/(x-3)) = \operatorname{Spec}(\mathbb{F}_5)$ for any field extension, since a ring homomorphism $\mathbb{F}_5[x]/(x-3)^2 \to \mathbb{F}_{5^n}$ is determined by the image of $x$, which must satisfy $(x-3)^2 = 0$, hence $x = 3$ (as $\mathbb{F}_{5^n}$ is reduced). Thus $\# X_5(\mathbb{F}_{5^n}) = 1$ and

$$
Z(X_5, t) = \frac{1}{1 - t}.

$$

*Case $p \equiv 1, 4 \pmod{5}$ (split):* Here $X_p$ consists of two $\mathbb{F}_p$-rational points, so $\# X_p(\mathbb{F}_{p^n}) = 2$ for all $n \geq 1$, giving

$$
Z(X_p, t) = \frac{1}{(1-t)^2}.

$$

*Case $p \equiv 2, 3 \pmod{5}$ (inert):* Here $X_p = \operatorname{Spec}(\mathbb{F}_{p^2})$. An $\mathbb{F}_{p^n}$-point corresponds to a ring homomorphism $\mathbb{F}_{p^2} \to \mathbb{F}_{p^n}$, which exists if and only if $2 \mid n$ (since $\mathbb{F}_{p^2} \hookrightarrow \mathbb{F}_{p^n}$ if and only if $2 \mid n$). When it exists, it is unique as a point of the spectrum (there are $\operatorname{Gal}(\mathbb{F}_{p^2}/\mathbb{F}_p)$-conjugate embeddings, but they give the same closed point). Thus $\# X_p(\mathbb{F}_{p^n}) = 0$ if $n$ is odd and $\# X_p(\mathbb{F}_{p^n}) = 1$ if $n$ is even, giving

$$
Z(X_p, t) = \exp\left(\sum_{m=1}^{\infty} \frac{t^{2m}}{m}\right) = \exp(-\ln(1 - t^2)) = \frac{1}{1 - t^2}.

$$

**Step 3 (Global zeta function):** Assembling the Euler product:

$$
\begin{aligned}
\zeta(X, s) &= Z(X_5, 5^{-s}) \cdot \prod_{p \equiv 1,4 \pmod{5}} \frac{1}{(1 - p^{-s})^2} \cdot \prod_{p \equiv 2,3 \pmod{5}} \frac{1}{1 - p^{-2s}} \\
&= \frac{1}{1 - 5^{-s}} \cdot \prod_{p \equiv 1,4 \pmod{5}} \frac{1}{(1 - p^{-s})^2} \cdot \prod_{p \equiv 2,3 \pmod{5}} \frac{1}{(1 - p^{-s})(1 + p^{-s})}.
\end{aligned}

$$

Now observe that for split primes $\left(\frac{p}{5}\right) = 1$, we have $\frac{1}{(1-p^{-s})^2} = \frac{1}{1-p^{-s}} \cdot \frac{1}{1-\left(\frac{p}{5}\right)p^{-s}}$, and for inert primes $\left(\frac{p}{5}\right) = -1$, we have $\frac{1}{1-p^{-2s}} = \frac{1}{1-p^{-s}} \cdot \frac{1}{1+p^{-s}} = \frac{1}{1-p^{-s}} \cdot \frac{1}{1-\left(\frac{p}{5}\right)p^{-s}}$. Therefore:

$$
\begin{aligned}
\zeta(X, s) &= \prod_p \frac{1}{1 - p^{-s}} \cdot \prod_{p \neq 5} \frac{1}{1 - \left(\frac{p}{5}\right) p^{-s}} \\
&= \zeta(s) \cdot L(\chi, s),
\end{aligned}

$$

where $\chi: (\mathbb{Z}/5\mathbb{Z})^\times \to \mathbb{C}^\times$ is the Legendre symbol character $\chi(n) = \left(\frac{n}{5}\right)$, and

$$
L(\chi, s) := \prod_{p \neq 5} \frac{1}{1 - \chi(p) p^{-s}} = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}

$$

is the Dirichlet $L$-function associated to $\chi$ (where by convention $\chi(5) = 0$, so the factor at $p = 5$ is absorbed).

**Key Insight:** This is the simplest nontrivial instance of the Dedekind zeta function factorization: for a number field $K/\mathbb{Q}$ of degree $d$, the Dedekind zeta function $\zeta_K(s)$ equals the zeta function of $\operatorname{Spec}(\mathcal{O}_K)$ and factors as a product of the Riemann zeta function and Artin $L$-functions. For the quadratic field $\mathbb{Q}(\sqrt{5})$, one gets $\zeta_K(s) = \zeta(s) \cdot L(\chi, s)$. The splitting behavior of primes in the ring of integers is completely governed by the Legendre symbol, connecting algebraic geometry over $\operatorname{Spec}(\mathbb{Z})$ to classical analytic number theory.

**Prerequisites:** Dedekind zeta function, quadratic reciprocity, Legendre symbol, Dirichlet $L$-functions, splitting of primes in number fields, local zeta function

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Spec}(\mathbb{Z}[x]/(x^2 - x - 1))$ over $\operatorname{Spec}(\mathbb{Z})$. (a) Determine the structure of the fibre $X_p$ for $p = 2, 3, 5, 7, 11$, specifying whether $p$ is split, inert, or ramified in $\mathbb{Q}(\sqrt{5})$. (b) Compute the local zeta function $Z(X_p, t)$ for each of these primes. (c) Show that the global zeta function satisfies $\zeta(X, s) = \zeta(s) \cdot L(\chi, s)$ where $\chi$ is the quadratic character modulo $5$. -->
