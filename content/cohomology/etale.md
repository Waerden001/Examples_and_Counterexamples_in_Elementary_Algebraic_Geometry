---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/etale.tex
---

## Etale cohomology

### Example: Etale cohomology of curves {#ecag-0225}

Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field $k$, and let $\ell$ be a prime with $\ell \neq \operatorname{char}(k)$. The $\ell$-adic cohomology groups of $C$ are

$$
H^i_{\text{ét}}(C, \mathbb{Q}_\ell) \cong \begin{cases} \mathbb{Q}_\ell & \text{if } i = 0, \\ \mathbb{Q}_\ell^{2g} & \text{if } i = 1, \\ \mathbb{Q}_\ell & \text{if } i = 2, \\ 0 & \text{if } i \geq 3. \end{cases}

$$

The $\ell$-adic Euler characteristic is $\chi(C) = 1 - 2g + 1 = 2 - 2g$.

**Degrees 0 and 2.** Since $C$ is connected, $H^0_{\text{ét}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell$. For $H^2$, Poincaré duality for a smooth projective variety of dimension $d$ over an algebraically closed field gives $H^{2d}_{\text{ét}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-d)$. With $d = 1$, this is $H^2_{\text{ét}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-1)$, which as a $\mathbb{Q}_\ell$-vector space has dimension 1 (the Tate twist records the Galois action but does not affect the underlying dimension).

The vanishing $H^i = 0$ for $i > 2$ follows from the general bound: a smooth variety of dimension $d$ over an algebraically closed field has étale cohomological dimension $2d$.

**Degree 1 via the Jacobian.** The identification of $H^1$ proceeds through the Jacobian variety $J(C)$. The étale fundamental group $\pi_1^{\text{ét}}(C)$ classifies finite étale covers, and for abelian covers there is a canonical identification

$$
H^1_{\text{ét}}(C, \mathbb{Z}/\ell^n\mathbb{Z}) \cong \operatorname{Hom}(\pi_1^{\text{ét}}(C)^{\text{ab}}, \mathbb{Z}/\ell^n\mathbb{Z}).

$$

The abelianized fundamental group $\pi_1^{\text{ét}}(C)^{\text{ab}}$ is in turn identified with the Tate module of the Jacobian via the theory of abelian étale covers: every connected abelian étale cover of $C$ arises as a pullback of an isogeny $J(C) \to J(C)$. This yields

$$
H^1_{\text{ét}}(C, \mathbb{Z}/\ell^n\mathbb{Z}) \cong J(C)[\ell^n]^{\vee}.

$$

Since $J(C)$ is an abelian variety of dimension $g$ over the algebraically closed field $k$ with $\ell \neq \operatorname{char}(k)$, the $\ell^n$-torsion subgroup is $J(C)[\ell^n] \cong (\mathbb{Z}/\ell^n\mathbb{Z})^{2g}$. Passing to the inverse limit over $n$ and tensoring with $\mathbb{Q}_\ell$ defines the $\ell$-adic cohomology:

$$
H^1_{\text{ét}}(C, \mathbb{Q}_\ell) = \left(\varprojlim_n H^1_{\text{ét}}(C, \mathbb{Z}/\ell^n\mathbb{Z})\right) \otimes_{\mathbb{Z}_\ell} \mathbb{Q}_\ell \cong T_\ell(J(C))^{\vee} \otimes_{\mathbb{Z}_\ell} \mathbb{Q}_\ell \cong \mathbb{Q}_\ell^{2g},

$$

where $T_\ell(J(C)) = \varprojlim_n J(C)[\ell^n] \cong \mathbb{Z}_\ell^{2g}$ is the $\ell$-adic Tate module.

**Comparison with topology.** When $k = \mathbb{C}$, the Artin comparison theorem provides a canonical isomorphism

$$
H^i_{\text{ét}}(C, \mathbb{Q}_\ell) \cong H^i_{\text{sing}}(C(\mathbb{C}), \mathbb{Q}) \otimes_{\mathbb{Q}} \mathbb{Q}_\ell.

$$

The analytification $C(\mathbb{C})$ is a compact Riemann surface of genus $g$, a closed orientable surface with singular cohomology $H^0 = H^2 = \mathbb{Q}$ and $H^1 = \mathbb{Q}^{2g}$. The comparison theorem confirms that étale cohomology recovers these Betti numbers over any algebraically closed field (of appropriate characteristic), even in positive characteristic where no underlying topological space of the "correct" homotopy type exists.

**Summary table.**

| $i$ | $\dim_{\mathbb{Q}_\ell} H^i_{\text{ét}}(C, \mathbb{Q}_\ell)$ | Source |
|-----|---------------------------------------------------------------|--------|
| $0$ | $1$ | Connectedness |
| $1$ | $2g$ | $T_\ell(J(C))^{\vee} \otimes \mathbb{Q}_\ell$ |
| $2$ | $1$ | Poincaré duality |
| $\geq 3$ | $0$ | Cohomological dimension bound |

<!-- BENCHMARK_PROBLEM: Let C be a smooth projective curve of genus 3 over an algebraically closed field k with char(k) != l. Compute the dimensions of H^i_et(C, Q_l) for all i >= 0. What is the l-adic Euler characteristic? -->

### Example: Etale cohomology of curves -- explicit computations {#ecag-0226}

We compute the étale cohomology for three specific curves, illustrating how the genus determines the Betti numbers while the Galois action on $H^1$ carries additional arithmetic content.

**The projective line $\mathbb{P}^1$ (genus $g = 0$).** The projective line over an algebraically closed field is simply connected: $\pi_1^{\text{ét}}(\mathbb{P}^1_{\bar{k}}) = 0$. (Every finite étale cover of $\mathbb{P}^1$ over an algebraically closed field is trivial, by the Riemann--Hurwitz formula: a connected étale cover $f : C \to \mathbb{P}^1$ of degree $d$ satisfies $2g(C) - 2 = d(2 \cdot 0 - 2) = -2d$, so $g(C) = 0$ and $d = 1$, using $\ell \neq \operatorname{char}(k)$ for tameness.) Therefore $H^1_{\text{ét}}(\mathbb{P}^1, \mathbb{Q}_\ell) = 0$, and

$$
\dim H^i_{\text{ét}}(\mathbb{P}^1, \mathbb{Q}_\ell) = \begin{cases} 1 & i = 0, 2, \\ 0 & \text{otherwise.} \end{cases}

$$

The Euler characteristic is $\chi(\mathbb{P}^1) = 1 - 0 + 1 = 2 = 2 - 2(0)$.

**An elliptic curve $E$ (genus $g = 1$).** An elliptic curve is isomorphic to its own Jacobian: $J(E) \cong E$. The $\ell^n$-torsion group $E[\ell^n] \cong (\mathbb{Z}/\ell^n\mathbb{Z})^2$ yields

$$
H^1_{\text{ét}}(E, \mathbb{Q}_\ell) \cong T_\ell(E) \otimes_{\mathbb{Z}_\ell} \mathbb{Q}_\ell \cong \mathbb{Q}_\ell^2.

$$

The Euler characteristic is $\chi(E) = 1 - 2 + 1 = 0$, reflecting the fact that $E$ admits a nowhere-vanishing 1-form (a differential of the first kind), which over $\mathbb{C}$ corresponds to the fact that the universal cover is $\mathbb{C}$ with deck group $\Lambda \cong \mathbb{Z}^2$.

When $E$ is defined over a number field $K$, the Galois representation

$$
\rho_\ell : \operatorname{Gal}(\overline{K}/K) \longrightarrow \operatorname{GL}(H^1_{\text{ét}}(E_{\bar{K}}, \mathbb{Q}_\ell)) \cong \operatorname{GL}_2(\mathbb{Q}_\ell)

$$

encodes the arithmetic of $E$. The $L$-function $L(E, s)$ is determined by the characteristic polynomials of Frobenius elements under $\rho_\ell$ at the primes of good reduction.

**A genus-2 curve.** Let $C$ be a smooth projective curve of genus 2, for instance the smooth projective completion of the affine curve $y^2 = f(x)$ where $f \in k[x]$ is separable of degree 5 or 6. The Jacobian $J(C)$ is a 2-dimensional abelian variety (an abelian surface), and

$$
H^1_{\text{ét}}(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell^4.

$$

The Euler characteristic is $\chi(C) = 1 - 4 + 1 = -2 = 2 - 2(2)$.

| Curve | $g$ | $\dim H^0$ | $\dim H^1$ | $\dim H^2$ | $\chi$ |
|-------|-----|-----------|-----------|-----------|--------|
| $\mathbb{P}^1$ | $0$ | $1$ | $0$ | $1$ | $2$ |
| Elliptic $E$ | $1$ | $1$ | $2$ | $1$ | $0$ |
| Genus-2 | $2$ | $1$ | $4$ | $1$ | $-2$ |

**Frobenius action in positive characteristic.** When $C$ is defined over $\mathbb{F}_q$, the geometric Frobenius $\operatorname{Frob}_q$ acts on $H^1_{\text{ét}}(C_{\overline{\mathbb{F}_q}}, \mathbb{Q}_\ell)$ as a $\mathbb{Q}_\ell$-linear endomorphism. The Grothendieck--Lefschetz trace formula expresses the number of rational points in terms of this action:

$$
|C(\mathbb{F}_q)| = \sum_{i=0}^{2} (-1)^i \operatorname{tr}(\operatorname{Frob}_q \mid H^i_{\text{ét}}).

$$

Since $\operatorname{Frob}_q$ acts as the identity on $H^0$ and as multiplication by $q$ on $H^2 \cong \mathbb{Q}_\ell(-1)$, this gives

$$
|C(\mathbb{F}_q)| = 1 - \operatorname{tr}(\operatorname{Frob}_q \mid H^1) + q = q + 1 - \sum_{i=1}^{2g} \alpha_i,

$$

where $\alpha_1, \ldots, \alpha_{2g}$ are the eigenvalues of $\operatorname{Frob}_q$ on $H^1$.

The Weil conjectures for curves (proved by Weil, 1948) assert that $|\alpha_i| = q^{1/2}$ for all $i$, yielding the Hasse--Weil bound $||C(\mathbb{F}_q)| - q - 1| \leq 2g\sqrt{q}$. The zeta function takes the form

$$
Z(C/\mathbb{F}_q, t) = \frac{\det(1 - t \cdot \operatorname{Frob}_q \mid H^1)}{(1 - t)(1 - qt)} = \frac{P_1(t)}{(1-t)(1-qt)},

$$

where $P_1(t) = \prod_{i=1}^{2g}(1 - \alpha_i t)$ is a polynomial of degree $2g$ with integer coefficients. The functional equation $P_1(t) = q^g t^{2g} P_1(1/qt)$ reflects Poincaré duality.

For an elliptic curve $E/\mathbb{F}_q$ with $P_1(t) = 1 - a_q t + qt^2$, the point count becomes $|E(\mathbb{F}_q)| = q + 1 - a_q$, and the Riemann hypothesis gives $|a_q| \leq 2\sqrt{q}$.

<!-- BENCHMARK_PROBLEM: Let E be an elliptic curve over a finite field F_q with q = p^r, p != l. The characteristic polynomial of Frobenius on H^1_et(E, Q_l) is t^2 - a_q t + q. Express |E(F_q)| in terms of a_q and q. What constraint does the Riemann hypothesis for curves place on a_q? -->
