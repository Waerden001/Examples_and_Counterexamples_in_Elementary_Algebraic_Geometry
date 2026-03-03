---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/etale.tex
---

## Etale cohomology

### Example: Etale cohomology of curves {#ecag-0225}

**Statement:** Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field $k$, and let $\ell$ be a prime different from $\operatorname{char}(k)$. The etale cohomology groups of $C$ with coefficients in $\mathbb{Z}/\ell\mathbb{Z}$ (and more generally $\mathbb{Q}_\ell$) are given by:

$$
H^i_{\text{et}}(C, \mathbb{Q}_\ell) \cong \begin{cases} \mathbb{Q}_\ell & \text{if } i = 0, \\ \mathbb{Q}_\ell^{2g} & \text{if } i = 1, \\ \mathbb{Q}_\ell & \text{if } i = 2, \\ 0 & \text{if } i \geq 3. \end{cases}

$$

In particular, the $\ell$-adic Euler characteristic is $\chi(C) = 2 - 2g$, matching the topological Euler characteristic.

**Construction/Proof:**

The computation proceeds in several steps.

*Step 1: $H^0$ and $H^2$.* Since $C$ is connected, $H^0_{\text{et}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell$. By Poincare duality for smooth projective varieties of dimension $d$ over an algebraically closed field, $H^{2d}_{\text{et}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-d)$. For $d = 1$, this gives $H^2_{\text{et}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-1) \cong \mathbb{Q}_\ell$ (as a vector space, forgetting the Tate twist). The vanishing $H^i = 0$ for $i > 2$ follows from the fact that $C$ has cohomological dimension 2 (it is a variety of dimension 1, and for smooth projective varieties the etale cohomological dimension is $2 \dim$).

*Step 2: $H^1$ via the Jacobian.* The key is identifying $H^1_{\text{et}}(C, \mathbb{Z}/\ell^n\mathbb{Z})$ with the $\ell^n$-torsion of the Jacobian $J(C)$. There is a canonical isomorphism

$$
H^1_{\text{et}}(C, \mathbb{Z}/\ell^n\mathbb{Z}) \cong \operatorname{Hom}(\pi_1^{\text{et}}(C), \mathbb{Z}/\ell^n\mathbb{Z}) \cong J(C)[\ell^n]^\vee,

$$

where the first isomorphism uses that $H^1$ classifies torsors (or equivalently, abelian covers), and the second uses the identification of abelian etale covers of $C$ with isogenies to $J(C)$. Since $J(C)$ is an abelian variety of dimension $g$ over an algebraically closed field with $\ell \neq \operatorname{char}(k)$, we have $J(C)[\ell^n] \cong (\mathbb{Z}/\ell^n\mathbb{Z})^{2g}$. Taking the inverse limit over $n$ and tensoring with $\mathbb{Q}_\ell$:

$$
H^1_{\text{et}}(C, \mathbb{Q}_\ell) = \left(\varprojlim_n H^1_{\text{et}}(C, \mathbb{Z}/\ell^n\mathbb{Z})\right) \otimes_{\mathbb{Z}_\ell} \mathbb{Q}_\ell \cong \mathbb{Q}_\ell^{2g}.

$$

*Step 3: Comparison with topology.* When $k = \mathbb{C}$, the Artin comparison theorem gives a canonical isomorphism $H^i_{\text{et}}(C, \mathbb{Q}_\ell) \cong H^i(C(\mathbb{C}), \mathbb{Q}) \otimes_\mathbb{Q} \mathbb{Q}_\ell$. Since $C(\mathbb{C})$ is a compact Riemann surface of genus $g$ with singular cohomology $H^0 = H^2 = \mathbb{Q}$ and $H^1 = \mathbb{Q}^{2g}$, this confirms the computation.

**Key Insight:** The etale cohomology of a curve is completely controlled by its Jacobian, which provides the bridge between arithmetic (torsion points on abelian varieties) and topology (the first cohomology group). This is the prototypical example of how etale cohomology recovers topological invariants in algebraic geometry over arbitrary fields.

**Prerequisites:** Etale cohomology, $\ell$-adic cohomology, Poincare duality, etale fundamental group, Jacobian variety, torsion points of abelian varieties, Artin comparison theorem

<!-- BENCHMARK_PROBLEM: Let C be a smooth projective curve of genus 3 over an algebraically closed field k with char(k) != l. Compute the dimensions of H^i_et(C, Q_l) for all i >= 0. What is the l-adic Euler characteristic? -->

### Example: Etale cohomology of curves -- explicit computations {#ecag-0226}

**Statement:** We give explicit computations of the etale cohomology groups for specific curves, illustrating the general theory: the projective line $\mathbb{P}^1$ (genus 0), an elliptic curve $E$ (genus 1), and a hyperelliptic curve of genus 2.

**Construction/Proof:**

*Example 1: $\mathbb{P}^1$ (genus $g = 0$).*

The projective line is simply connected: $\pi_1^{\text{et}}(\mathbb{P}^1_{\overline{k}}) = 0$ (over an algebraically closed field). Therefore $H^1_{\text{et}}(\mathbb{P}^1, \mathbb{Q}_\ell) = 0$. Combined with $H^0 \cong \mathbb{Q}_\ell$ and $H^2 \cong \mathbb{Q}_\ell(-1)$, the Euler characteristic is $\chi(\mathbb{P}^1) = 1 - 0 + 1 = 2$, consistent with $2 - 2(0) = 2$.

*Example 2: Elliptic curve $E$ (genus $g = 1$).*

An elliptic curve is its own Jacobian: $J(E) \cong E$. The $\ell^n$-torsion $E[\ell^n] \cong (\mathbb{Z}/\ell^n\mathbb{Z})^2$ gives

$$
H^1_{\text{et}}(E, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell^2.

$$

This is the Tate module $T_\ell(E) \otimes \mathbb{Q}_\ell$. The Galois representation on $H^1_{\text{et}}$ encodes the arithmetic of $E$: for $E$ defined over a number field $K$, the action of $\operatorname{Gal}(\overline{K}/K)$ on $H^1_{\text{et}}(E_{\overline{K}}, \mathbb{Q}_\ell)$ determines the $L$-function $L(E, s)$. The Euler characteristic is $\chi(E) = 1 - 2 + 1 = 0$.

*Example 3: Hyperelliptic curve of genus 2.*

Let $C$ be a smooth projective curve of genus 2, for instance the smooth completion of the affine curve $y^2 = f(x)$ where $f$ is a separable polynomial of degree 5 or 6. Then $J(C)$ is a 2-dimensional abelian variety (an abelian surface), and

$$
H^1_{\text{et}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell^4.

$$

The Euler characteristic is $\chi(C) = 1 - 4 + 1 = -2 = 2 - 2(2)$.

*Frobenius action in positive characteristic.* When $C$ is defined over $\mathbb{F}_q$, the geometric Frobenius $\operatorname{Frob}_q$ acts on $H^1_{\text{et}}(C_{\overline{\mathbb{F}_q}}, \mathbb{Q}_\ell)$, and the Weil conjectures (proved by Weil for curves) assert that the eigenvalues $\alpha_1, \ldots, \alpha_{2g}$ of Frobenius on $H^1$ satisfy $|\alpha_i| = q^{1/2}$. The zeta function of $C/\mathbb{F}_q$ is then

$$
Z(C/\mathbb{F}_q, t) = \frac{\det(1 - t \operatorname{Frob}_q \mid H^1)}{(1 - t)(1 - qt)} = \frac{P_1(t)}{(1-t)(1-qt)},

$$

where $P_1(t)$ is a polynomial of degree $2g$ with integer coefficients and all roots of absolute value $q^{-1/2}$.

**Key Insight:** These explicit examples show that the etale cohomology of curves is entirely determined by the genus, but the Galois action on $H^1$ -- equivalently, the Tate module of the Jacobian -- carries deep arithmetic information. The passage from topology (Betti numbers) to arithmetic (Frobenius eigenvalues) is the central theme of the Weil conjectures.

**Prerequisites:** Etale cohomology of curves, Jacobian varieties, Tate modules, etale fundamental group, Weil conjectures, zeta functions of varieties over finite fields

<!-- BENCHMARK_PROBLEM: Let E be an elliptic curve over a finite field F_q with q = p^r, p != l. The characteristic polynomial of Frobenius on H^1_et(E, Q_l) is t^2 - a_q t + q. Express |E(F_q)| in terms of a_q and q. What constraint does the Riemann hypothesis for curves place on a_q? -->
