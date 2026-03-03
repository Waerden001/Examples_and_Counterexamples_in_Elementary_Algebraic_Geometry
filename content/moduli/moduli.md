---
chapter: moduli
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Moduli_problems_and_deformation_theory/moduli.tex
---

## Moduli problems

### Example: A stable sheaf but not geometrically stable {#ecag-0306}

Mumford--Takemoto stability of a coherent sheaf on a smooth projective variety $X$ over a field $k$ depends on the ground field. We construct a rank-2 bundle on $\mathbb{P}^1_{\mathbb{R}}$ that is stable over $\mathbb{R}$ but becomes strictly semistable after base change to $\mathbb{C}$.

Take $k = \mathbb{R}$, $X = \mathbb{P}^1_{\mathbb{R}}$, and $H = \mathcal{O}(1)$. The finite morphism $\pi \colon \mathbb{P}^1_{\mathbb{C}} \to \mathbb{P}^1_{\mathbb{R}}$ induced by $\mathbb{R} \hookrightarrow \mathbb{C}$ gives a rank-2 bundle $\mathcal{E} = \pi_* \mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}$ on $\mathbb{P}^1_{\mathbb{R}}$. Since $\pi$ is finite of degree 2 and $\mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}$ has degree 0, the projection formula gives $\deg(\mathcal{E}) = 0$, so
$$
\mu_H(\mathcal{E}) = \frac{\deg(\mathcal{E})}{\operatorname{rk}(\mathcal{E})} = \frac{0}{2} = 0.
$$

To verify stability over $\mathbb{R}$, let $\mathcal{F} \cong \mathcal{O}(d) \hookrightarrow \mathcal{E}$ be a rank-1 subsheaf. By adjunction for $\pi_*\dashv\pi^*$, a nonzero map $\mathcal{O}(d) \to \pi_* \mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}$ corresponds to a nonzero map $\pi^* \mathcal{O}(d) \cong \mathcal{O}(d) \to \mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}$. For this to be nonzero we need $d \leq 0$. A Galois-theoretic refinement sharpens this: the inclusion $\mathcal{O}(d) \hookrightarrow \mathcal{E}$ defines an $\mathbb{R}$-rational sub-line-bundle. But $\pi_* \mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}$ carries a $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$-action exchanging the two summands that appear after base change (see below), so any $\mathbb{R}$-rational sub-line-bundle must land in the invariant part, forcing $d \leq -1$. Hence $\mu_H(\mathcal{F}) = d \leq -1 < 0 = \mu_H(\mathcal{E})$, and $\mathcal{E}$ is Mumford--Takemoto stable over $\mathbb{R}$.

After base change to $\bar{k} = \mathbb{C}$, the morphism $\pi$ splits: $\mathbb{P}^1_{\mathbb{C}} \times_{\mathbb{P}^1_{\mathbb{R}}} \mathbb{P}^1_{\mathbb{C}} \cong \mathbb{P}^1_{\mathbb{C}} \sqcup \mathbb{P}^1_{\mathbb{C}}$, so
$$
\mathcal{E}_{\mathbb{C}} \cong \mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}} \oplus \mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}.
$$

The summand $\mathcal{O}_{\mathbb{P}^1_{\mathbb{C}}}$ is a subsheaf with $\mu(\mathcal{O}) = 0 = \mu(\mathcal{E}_{\mathbb{C}})$, so $\mathcal{E}_{\mathbb{C}}$ is strictly semistable. The two destabilizing sub-line-bundles are exchanged by $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$, which is why neither is defined over $\mathbb{R}$.

This phenomenon is general: whenever the Galois group $\operatorname{Gal}(\bar{k}/k)$ permutes the destabilizing subsheaves of $\mathcal{E}_{\bar{k}}$ transitively and none is individually defined over $k$, the bundle can be stable over $k$ while failing geometric stability.

<!-- BENCHMARK_PROBLEM: Let $k = \mathbb{R}$ and consider $\mathcal{E} = \pi_{*}\mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}}$ on $\mathbb{P}^{1}_{\mathbb{R}}$, where $\pi: \mathbb{P}^{1}_{\mathbb{C}} \to \mathbb{P}^{1}_{\mathbb{R}}$ is the natural map. Show that $\mathcal{E}$ is Mumford-Takemoto stable over $\mathbb{R}$ but $\mathcal{E}_{\mathbb{C}}$ is not stable. -->

### Example: $\Omega_{\mathbb{P}^{n}}$ is stable {#ecag-0307}

The cotangent bundle $\Omega_{\mathbb{P}^n}$ is Mumford--Takemoto stable with respect to $H = \mathcal{O}(1)$, over any algebraically closed field of characteristic 0. The proof combines a naive slope bound from the Euler sequence with Hoppe's criterion and Bott vanishing.

From the dual Euler sequence
$$
0 \to \Omega_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n} \to 0,
$$

we read off $\operatorname{rk}(\Omega_{\mathbb{P}^n}) = n$ and $c_1(\Omega_{\mathbb{P}^n}) = -(n+1)H$, giving
$$
\mu_H(\Omega_{\mathbb{P}^n}) = \frac{-(n+1)}{n}.
$$

**Naive bound from the Euler sequence.** Let $\mathcal{F} \subset \Omega_{\mathbb{P}^n}$ be a coherent subsheaf of rank $r$ with $0 < r < n$. The composite $\mathcal{F} \hookrightarrow \Omega_{\mathbb{P}^n} \hookrightarrow \mathcal{O}(-1)^{\oplus(n+1)}$ induces a nonzero map $\det(\mathcal{F}) \to \bigwedge^r \mathcal{O}(-1)^{\oplus(n+1)} \cong \mathcal{O}(-r)^{\oplus \binom{n+1}{r}}$, hence a nonzero map $\mathcal{O}(c_1(\mathcal{F})) \to \mathcal{O}(-r)$. Existence of a nonzero global section of $\mathcal{O}(-r - c_1(\mathcal{F}))$ forces $c_1(\mathcal{F}) \leq -r$, so $\mu_H(\mathcal{F}) \leq -1$. This is insufficient: $-1 > -(n+1)/n$ for $n \geq 2$, so the Euler sequence alone does not prove stability.

**Hoppe's criterion and Bott vanishing.** Hoppe's criterion states that a vector bundle $\mathcal{E}$ of rank $n$ on $\mathbb{P}^n$ with $c_1(\mathcal{E})/\operatorname{rk}(\mathcal{E})$ not an integer is stable if
$$
H^0\!\left(\mathbb{P}^n,\, \bigl(\textstyle\bigwedge^p \mathcal{E}\bigr)(q)\right) = 0 \quad \text{for all } 1 \leq p \leq n-1 \text{ and } q = \left\lfloor p \cdot \mu_H(\mathcal{E}) \right\rfloor + 1.
$$

For $\mathcal{E} = \Omega_{\mathbb{P}^n}$ with $\mu = -(n+1)/n$, it suffices to verify $H^0(\mathbb{P}^n, \Omega_{\mathbb{P}^n}^p(q)) = 0$ for $1 \leq p \leq n-1$ and
$$
q \leq \left\lfloor p \cdot \tfrac{n+1}{n} \right\rfloor = p + \left\lfloor \tfrac{p}{n} \right\rfloor = p \quad (\text{since } 1 \leq p \leq n-1).
$$

By the Bott vanishing theorem, $H^0(\mathbb{P}^n, \Omega_{\mathbb{P}^n}^p(q)) = 0$ whenever $0 < q \leq p$. This is exactly the required range, so $\Omega_{\mathbb{P}^n}$ is stable.

**Verification for $n = 3$.** We have $\mu_H(\Omega_{\mathbb{P}^3}) = -4/3$. Hoppe's criterion requires:

| $p$ | Required vanishing | Bott vanishing gives |
|-----|-------------------|---------------------|
| $1$ | $H^0(\Omega^1(1)) = 0$ | $0 < 1 \leq 1$: vanishes |
| $2$ | $H^0(\Omega^2(2)) = 0$ | $0 < 2 \leq 2$: vanishes |

Both conditions hold, confirming stability of $\Omega_{\mathbb{P}^3}$.

<!-- BENCHMARK_PROBLEM: Compute the slope $\mu_{H}(\Omega_{\mathbb{P}^{n}})$ with respect to the hyperplane class, and use Hoppe's criterion together with Bott vanishing to verify stability of $\Omega_{\mathbb{P}^{n}}$ for $n = 3$. -->

### Example: Harder-Narasimhan filtration, Gieseker nonstable but Mumford-Takemoto semistable {#ecag-0308}

Mumford--Takemoto semistability and Gieseker semistability are distinct conditions: the former compares slopes $\mu_H = c_1 \cdot H^{n-1}/\operatorname{rk}$, while the latter compares full reduced Hilbert polynomials. We exhibit a rank-2 sheaf on $\mathbb{P}^2$ that is Mumford--Takemoto semistable but Gieseker unstable.

On $X = \mathbb{P}^2$ with $H = \mathcal{O}(1)$, choose a non-split extension
$$
0 \to \mathcal{O}_{\mathbb{P}^2} \to \mathcal{E} \to \mathcal{I}_p \to 0,
$$

where $\mathcal{I}_p$ is the ideal sheaf of a closed point $p \in \mathbb{P}^2$. Such an extension exists because $\operatorname{Ext}^1(\mathcal{I}_p, \mathcal{O}) \cong \operatorname{Ext}^2(\mathcal{O}_p, \mathcal{O}) \cong k \neq 0$ by local duality. The resulting sheaf has $\operatorname{rk}(\mathcal{E}) = 2$, $c_1(\mathcal{E}) = 0$, and $c_2(\mathcal{E}) = 1$.

**Mumford--Takemoto semistability.** The slope is $\mu_H(\mathcal{E}) = 0$. Let $\mathcal{L} \cong \mathcal{O}(d)$ be a saturated rank-1 subsheaf of $\mathcal{E}$. The composition $\mathcal{O}(d) \hookrightarrow \mathcal{E} \twoheadrightarrow \mathcal{I}_p$ is either zero or nonzero. If nonzero, it gives an injection $\mathcal{O}(d) \hookrightarrow \mathcal{I}_p \subset \mathcal{O}$, forcing $d \leq 0$. If zero, the map factors through $\mathcal{O}(d) \hookrightarrow \mathcal{O}$, again forcing $d \leq 0$. In either case $\mu_H(\mathcal{L}) = d \leq 0 = \mu_H(\mathcal{E})$, confirming Mumford--Takemoto semistability.

**Gieseker instability.** On $\mathbb{P}^2$, $\chi(\mathcal{O}(m)) = \binom{m+2}{2} = \frac{(m+1)(m+2)}{2}$. From $0 \to \mathcal{I}_p \to \mathcal{O} \to \mathcal{O}_p \to 0$ we get $\chi(\mathcal{I}_p(m)) = \frac{(m+1)(m+2)}{2} - 1 = \frac{m^2 + 3m}{2}$. Additivity on the defining extension yields
$$
\chi(\mathcal{E}(m)) = \chi(\mathcal{O}(m)) + \chi(\mathcal{I}_p(m)) = \frac{(m+1)(m+2)}{2} + \frac{m^2 + 3m}{2} = m^2 + 3m + 1.
$$

The reduced Hilbert polynomials are therefore
$$
p(\mathcal{E}, m) = \frac{m^2 + 3m + 1}{2}, \qquad p(\mathcal{O}, m) = \frac{m^2 + 3m + 2}{2}.
$$

Since $p(\mathcal{O}, m) - p(\mathcal{E}, m) = \frac{1}{2} > 0$ for all $m$, the subsheaf $\mathcal{O} \subset \mathcal{E}$ has strictly larger reduced Hilbert polynomial, so $\mathcal{E}$ is not Gieseker semistable. The discrepancy arises because Mumford--Takemoto stability sees only $c_1$ (the leading coefficient), while Gieseker stability detects the constant-term shift caused by $c_2(\mathcal{E}) = 1$.

<!-- BENCHMARK_PROBLEM: Let $\mathcal{E}$ be defined by a non-split extension $0 \to \mathcal{O}_{\mathbb{P}^{2}} \to \mathcal{E} \to \mathcal{I}_{p} \to 0$ on $\mathbb{P}^{2}$. Compute the reduced Hilbert polynomial of $\mathcal{E}$ and of $\mathcal{O}_{\mathbb{P}^{2}}$, and determine whether $\mathcal{E}$ is Gieseker semistable. -->
### Example: $\mathbb{P}^{1}\times \mathbb{P}^{1}$ and change of polarization {#ecag-0309}

On $X = \mathbb{P}^1 \times \mathbb{P}^1$, stability of a vector bundle depends on the choice of polarization. The ample cone is two-dimensional, and walls of stability are codimension-1 loci where the slope of a subsheaf equals the slope of the bundle.

Let $\operatorname{Pic}(X) \cong \mathbb{Z}^2$ be generated by $f_1 = \{pt\} \times \mathbb{P}^1$ and $f_2 = \mathbb{P}^1 \times \{pt\}$, with intersection products $f_1^2 = f_2^2 = 0$ and $f_1 \cdot f_2 = 1$. An ample class is $H_{a,b} = af_1 + bf_2$ with $a, b > 0$.

**A split example.** Consider $\mathcal{E} = \mathcal{O}(1,0) \oplus \mathcal{O}(0,1)$, which has $c_1(\mathcal{E}) = f_1 + f_2$. The slope with respect to $H_{a,b}$ is
$$
\mu_{H_{a,b}}(\mathcal{E}) = \frac{(f_1 + f_2) \cdot (af_1 + bf_2)}{2} = \frac{a + b}{2}.
$$

The subsheaf $\mathcal{O}(1,0)$ has slope $\mu_{H_{a,b}}(\mathcal{O}(1,0)) = f_1 \cdot (af_1 + bf_2) = b$, which exceeds $(a+b)/2$ precisely when $b > a$. Similarly, $\mathcal{O}(0,1)$ destabilizes when $a > b$. For $a = b$, both summands have slope equal to $\mu_H(\mathcal{E})$, so $\mathcal{E}$ is strictly semistable. For $a \neq b$, $\mathcal{E}$ is always unstable, but the destabilizing subsheaf switches as we cross the wall $a = b$.

**A non-split example.** Take a non-split extension
$$
0 \to \mathcal{O}(1,-1) \to \mathcal{E} \to \mathcal{O}(-1,1) \to 0.
$$

Now $c_1(\mathcal{E}) = 0$, so $\mu_{H_{a,b}}(\mathcal{E}) = 0$ for all polarizations. The only potential destabilizing subsheaf (up to saturation) is $\mathcal{O}(1,-1) \subset \mathcal{E}$, with slope
$$
\mu_{H_{a,b}}(\mathcal{O}(1,-1)) = (f_1 - f_2) \cdot (af_1 + bf_2) = b - a.
$$

This slope is negative when $a > b$, zero when $a = b$, and positive when $b > a$. Since the extension is non-split, there is no copy of $\mathcal{O}(-1,1)$ as a sub-line-bundle. Therefore $\mathcal{E}$ is stable when $a > b$, strictly semistable when $a = b$, and unstable when $b > a$. The wall of stability is the ray $a = b$ in the ample cone.

<!-- BENCHMARK_PROBLEM: On $\mathbb{P}^{1} \times \mathbb{P}^{1}$, let $\mathcal{E}$ be defined by a non-split extension $0 \to \mathcal{O}(1,-1) \to \mathcal{E} \to \mathcal{O}(-1,1) \to 0$. For which ample classes $H = af_{1} + bf_{2}$ (with $a, b > 0$) is $\mathcal{E}$ Mumford-Takemoto stable? -->

### Example: A rank $2$ moduli space, $\mathrm{K}3$ surface of degree $8$ in $\mathbb{P}^{5}$  {#ecag-0310}

Let $S$ be a smooth projective K3 surface with $\operatorname{Pic}(S) = \mathbb{Z} \cdot H$ and $H^2 = 2$. Mukai's theory of moduli of sheaves on K3 surfaces produces new holomorphic symplectic varieties; in dimension 2, these are again K3 surfaces.

Recall that the Mukai vector of a sheaf $\mathcal{E}$ on $S$ is $v(\mathcal{E}) = \operatorname{ch}(\mathcal{E}) \cdot \sqrt{\operatorname{td}(S)} = (r, c_1, s) \in H^*(S, \mathbb{Z})$, where $s = r + \frac{c_1^2}{2r} - \frac{c_2}{r}$ (for a rank-$r$ sheaf). The Mukai pairing is $\langle (r, c_1, s), (r, c_1, s) \rangle = c_1^2 - 2rs$, and we write $v^2 = -\langle v, v \rangle = 2rs - c_1^2$. The moduli space $M_H(v)$ of $H$-stable sheaves with Mukai vector $v$ is, when non-empty and when all semistable sheaves are stable, a smooth projective holomorphic symplectic variety of dimension $v^2 + 2$.

**Dimension computation.** For a rank-2 sheaf with $c_1 = H$ and $c_2 = 2$, the Mukai vector is $v = (2, H, s)$ where $s = \frac{c_1^2}{2} - c_2 + r = \frac{2}{2} - 2 + 2 = 1$. (Here $s = \operatorname{ch}_0 + \operatorname{ch}_2 = r + \frac{c_1^2}{2r} - \frac{c_2}{r}$; more precisely for the Mukai vector convention $v = (r, c_1, \frac{c_1^2}{2r} - c_2 + r)$.) Then $v^2 = 2 \cdot 2 \cdot 1 - H^2 = 4 - 2 = 2$, giving $\dim M_H(v) = 2 + 2 = 4$.

**The 2-dimensional case.** To obtain a 2-dimensional moduli space (i.e., another K3 surface), we need $v^2 = 0$. Taking $v = (2, 0, 0)$ gives $v^2 = 2 \cdot 2 \cdot 0 - 0 = 0$, so $\dim M_H(v) = 0 + 2 = 2$. The resulting moduli space is a smooth K3 surface. By a theorem of Mukai, this K3 carries a natural ample class under which it embeds in $\mathbb{P}^5$ as a degree-8 surface (a complete intersection of three quadrics). This establishes a Fourier--Mukai equivalence $D^b(S) \simeq D^b(M_H(v))$ between the derived categories of the original K3 and the moduli K3.

| Mukai vector $v = (r, c_1, s)$ | $v^2 = 2rs - c_1^2$ | $\dim M_H(v)$ | Type |
|-------------------------------|---------------------|---------------|------|
| $(2, 0, 0)$ | $0$ | $2$ | K3 surface |
| $(2, H, 1)$ | $4 - 2 = 2$ | $4$ | Hilb$^2(S')$ type |
| $(2, 0, -1)$ | $-4$ | N/A (empty) | -- |

<!-- BENCHMARK_PROBLEM: Let $S$ be a K3 surface with $\operatorname{Pic}(S) = \mathbb{Z} \cdot H$ and $H^{2} = 2$. For the Mukai vector $v = (2, 0, 0)$, compute $v^{2}$ and the expected dimension of the moduli space $M_{H}(v)$. What type of variety is the resulting moduli space? -->

### Example: $S$-equivalence {#ecag-0311}

Two semistable sheaves $\mathcal{E}$ and $\mathcal{E}'$ are $S$-equivalent if their associated graded objects under the Jordan--Holder filtration are isomorphic: $\operatorname{gr}^{JH}(\mathcal{E}) \cong \operatorname{gr}^{JH}(\mathcal{E}')$. The moduli space of semistable sheaves parametrizes $S$-equivalence classes, not isomorphism classes. This identification is necessary for the moduli space to be separated.

On $\mathbb{P}^1$, the phenomenon is invisible: $\operatorname{Ext}^1(\mathcal{O}, \mathcal{O}) = H^1(\mathbb{P}^1, \mathcal{O}) = 0$, so every extension of $\mathcal{O}$ by $\mathcal{O}$ splits. To see a non-trivial example, work on an elliptic curve $C$. Since $\operatorname{Ext}^1(\mathcal{O}_C, \mathcal{O}_C) = H^1(C, \mathcal{O}_C) \cong k$, there is a unique (up to scaling) non-trivial extension
$$
0 \to \mathcal{O}_C \to \mathcal{E} \to \mathcal{O}_C \to 0.
$$

This $\mathcal{E}$ is the Atiyah bundle: the unique indecomposable rank-2 bundle of degree 0 on $C$. It is semistable (slope 0, and every line subbundle has degree $\leq 0$) but not stable (the subsheaf $\mathcal{O}_C$ achieves the same slope).

The Jordan--Holder filtration of $\mathcal{E}$ is $0 \subset \mathcal{O}_C \subset \mathcal{E}$, with graded pieces $\mathcal{O}_C$ and $\mathcal{O}_C$, so $\operatorname{gr}^{JH}(\mathcal{E}) = \mathcal{O}_C \oplus \mathcal{O}_C$. The split bundle $\mathcal{O}_C \oplus \mathcal{O}_C$ has the same associated graded: $\operatorname{gr}^{JH}(\mathcal{O}_C \oplus \mathcal{O}_C) = \mathcal{O}_C \oplus \mathcal{O}_C$. Therefore $\mathcal{E}$ and $\mathcal{O}_C^{\oplus 2}$ are $S$-equivalent, even though they are not isomorphic as bundles ($\mathcal{E}$ is indecomposable while $\mathcal{O}_C^{\oplus 2}$ is not). In the moduli space $M_C(2, 0)$ of semistable rank-2 degree-0 bundles, both are represented by the same closed point.

Without this identification, one could construct a family over $\mathbb{A}^1$ whose fiber over $t \neq 0$ is $\mathcal{E}$ and whose fiber over $t = 0$ is $\mathcal{O}_C^{\oplus 2}$ (the extension class $t \in \operatorname{Ext}^1(\mathcal{O}_C, \mathcal{O}_C) \cong k$ degenerates to 0), which would give a non-separated moduli space if these were assigned distinct points.

<!-- BENCHMARK_PROBLEM: On an elliptic curve $C$, let $\mathcal{E}$ be the unique non-trivial extension $0 \to \mathcal{O}_{C} \to \mathcal{E} \to \mathcal{O}_{C} \to 0$. Compute $\operatorname{gr}(\mathcal{E})$ with respect to the Jordan-Holder filtration, and determine which other semistable bundle is $S$-equivalent to $\mathcal{E}$. -->

### Example: Jordan-Holder filtration v.s. Harder-Narasimhan filtration {#ecag-0312}

The Harder--Narasimhan (HN) filtration and the Jordan--Holder (JH) filtration serve fundamentally different roles. The HN filtration exists uniquely for any torsion-free sheaf, with semistable graded pieces of strictly decreasing slopes; it measures how far a sheaf is from being semistable. The JH filtration applies only to a semistable sheaf, refining it into stable graded pieces of equal slope; the filtration itself is not unique, but $\operatorname{gr}^{JH}(\mathcal{E})$ is unique up to isomorphism, and this defines $S$-equivalence classes for moduli construction.

**The Harder--Narasimhan filtration.** On $\mathbb{P}^2$ with $H = \mathcal{O}(1)$, consider $\mathcal{E} = \mathcal{O}(3) \oplus \mathcal{O}(1) \oplus \mathcal{O}(-2)$. The slopes of the summands are $3, 1, -2$. The HN filtration is the unique filtration whose successive quotients are semistable with strictly decreasing slopes:
$$
0 \subset \mathcal{O}(3) \subset \mathcal{O}(3) \oplus \mathcal{O}(1) \subset \mathcal{E},
$$

with graded pieces $\mathcal{O}(3)$ (slope 3), $\mathcal{O}(1)$ (slope 1), and $\mathcal{O}(-2)$ (slope $-2$). Each graded piece is a line bundle, hence stable.

**The Jordan--Holder filtration.** On an elliptic curve $C$, consider a semistable rank-3 bundle $\mathcal{E}$ of degree 0 fitting into $0 \to \mathcal{L}_1 \to \mathcal{E} \to \mathcal{L}_2 \oplus \mathcal{L}_3 \to 0$, where $\mathcal{L}_1, \mathcal{L}_2, \mathcal{L}_3$ are pairwise non-isomorphic degree-0 line bundles. On an elliptic curve, degree-0 line bundles are stable, so the JH filtration refines $\mathcal{E}$ into three stable pieces. However, the filtration itself is non-unique: one could take
$$
0 \subset \mathcal{L}_1 \subset \mathcal{L}_1 \oplus \mathcal{L}_2 \subset \mathcal{E} \qquad \text{or} \qquad 0 \subset \mathcal{L}_1 \subset \mathcal{L}_1 \oplus \mathcal{L}_3 \subset \mathcal{E}.
$$

In both cases, $\operatorname{gr}^{JH}(\mathcal{E}) \cong \mathcal{L}_1 \oplus \mathcal{L}_2 \oplus \mathcal{L}_3$, confirming that the associated graded is canonical even though the filtration is not.

| Filtration | Applies to | Unique? | Graded pieces | Purpose |
|-----------|-----------|---------|---------------|---------|
| HN | any torsion-free sheaf | yes | semistable, strictly decreasing slopes | measures instability |
| JH | semistable sheaves only | no (but $\operatorname{gr}$ is) | stable, all same slope | defines $S$-equivalence |

<!-- BENCHMARK_PROBLEM: Let $\mathcal{E} = \mathcal{O}_{\mathbb{P}^{2}}(3) \oplus \mathcal{O}_{\mathbb{P}^{2}}(1) \oplus \mathcal{O}_{\mathbb{P}^{2}}(-2)$ on $\mathbb{P}^{2}$ with polarization $H = \mathcal{O}(1)$. Write down the Harder-Narasimhan filtration of $\mathcal{E}$ and identify the slopes of the graded pieces. -->

### Example: Strong semistability is not an open property {#ecag-0313}

Over an algebraically closed field $k$ of characteristic $p > 0$, a vector bundle $\mathcal{E}$ on a smooth projective variety $X$ is strongly semistable if $(F^n)^*\mathcal{E}$ is semistable for all $n \geq 0$, where $F \colon X \to X$ is the absolute Frobenius. Unlike ordinary semistability, strong semistability is not an open condition in families.

The reason is structural: for each fixed $n$, the locus
$$
U_n = \{t \in T : (F^n)^*\mathcal{E}_t \text{ is semistable}\}
$$

is open in the parameter space $T$ (by the standard openness of semistability). However, strong semistability requires membership in the intersection $\bigcap_{n \geq 0} U_n$, which is a countable intersection of open sets and need not be open.

Explicit examples arise on smooth projective curves $C$ of genus $g \geq 2$ in characteristic $p$. One can construct a family $\{\mathcal{E}_t\}_{t \in T}$ of rank-2 bundles on $C$ such that $\mathcal{E}_t$ is semistable for all $t$, but the smallest $n$ for which $(F^n)^*\mathcal{E}_t$ becomes unstable depends on $t$ and tends to infinity as $t$ approaches a limit point $t_0$. At $t_0$ itself, $(F^n)^*\mathcal{E}_{t_0}$ remains semistable for all $n$, so $\mathcal{E}_{t_0}$ is strongly semistable. But every punctured neighborhood of $t_0$ contains points where strong semistability fails, so the strongly semistable locus is not open.

This phenomenon has no analogue in characteristic 0, where the Frobenius does not exist and semistability automatically implies strong semistability (vacuously).

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective curve of genus $g \geq 2$ over an algebraically closed field of characteristic $p > 0$. Explain why the locus of strongly semistable bundles in the moduli of semistable rank $2$ bundles on $X$ need not be open, despite semistability itself being an open condition. -->
### Example: Betti numbers and topological Euler characteristics of $\overline{\mathrm{M}}_{0,n}$ {#ecag-0314}

The Deligne--Mumford compactification $\overline{\mathcal{M}}_{0,n}$ of the moduli space of $n$-pointed rational curves has dimension $n - 3$ for $n \geq 3$. Its cohomology is entirely algebraic (all of type $(p,p)$), so the odd Betti numbers vanish and the Poincare polynomial takes the form $P(\overline{\mathcal{M}}_{0,n}, t) = \sum_{k=0}^{n-3} b_{2k}\, t^{2k}$.

**Small cases.** The first three non-trivial cases are:

| $n$ | $\overline{\mathcal{M}}_{0,n}$ | $\dim$ | $P(t)$ | $\chi_{\mathrm{top}}$ |
|-----|-------------------------------|--------|---------|------------------|
| $3$ | $\{pt\}$ | $0$ | $1$ | $1$ |
| $4$ | $\mathbb{P}^1$ | $1$ | $1 + t^2$ | $2$ |
| $5$ | $\operatorname{Bl}_4 \mathbb{P}^2$ | $2$ | $1 + 5t^2 + t^4$ | $7$ |
| $6$ | smooth 3-fold | $3$ | $1 + 16t^2 + 16t^4 + t^6$ | $34$ |

The identification $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_4 \mathbb{P}^2$ (the del Pezzo surface of degree 5) gives $b_2 = 5$ since blowing up 4 points adds 4 exceptional classes to $H^2(\mathbb{P}^2)$.

**Recursive structure.** The forgetful morphism $\pi \colon \overline{\mathcal{M}}_{0,n+1} \to \overline{\mathcal{M}}_{0,n}$ (forgetting the last marked point) realizes $\overline{\mathcal{M}}_{0,n+1}$ as the universal curve over $\overline{\mathcal{M}}_{0,n}$. By Keel's theorem, the cohomology ring $H^*(\overline{\mathcal{M}}_{0,n}, \mathbb{Z})$ is generated by boundary divisor classes subject to explicit quadratic relations, enabling recursive computation of Betti numbers.

**Euler characteristic.** The open stratum $\mathcal{M}_{0,n}$ has $\chi(\mathcal{M}_{0,n}) = (-1)^{n-3}(n-2)!$ (since $\mathcal{M}_{0,n} \cong M_{0,n}$ is an iterated fibration with fibers $\mathbb{P}^1$ minus finitely many points). By inclusion-exclusion over boundary strata -- each of which is a product of lower $\overline{\mathcal{M}}_{0,n_i}$ -- one obtains the formula
$$
\chi_{\mathrm{top}}(\overline{\mathcal{M}}_{0,n}) = \sum_{k=0}^{n-3} b_{2k}.
$$

For $n = 6$: $\chi = 1 + 16 + 16 + 1 = 34$.

<!-- BENCHMARK_PROBLEM: Compute the Poincare polynomial $P(\overline{\mathcal{M}}_{0,6}, t)$, given that $\overline{\mathcal{M}}_{0,6}$ is a $3$-dimensional smooth projective variety. (Hint: $b_{0} = 1$, $b_{2} = 16$, $b_{4} = 16$, $b_{6} = 1$.) Verify that the Euler characteristic equals $(-1)^{3} \cdot 3! = -6$... wait, the sign convention: $\chi = \sum b_{2k} = 34$. Reconcile with the formula $\chi(\overline{\mathcal{M}}_{0,n})$. -->

### Example: Canonical divisor of $\overline{\mathrm{M}}_{0,n}$ {#ecag-0315}

The canonical divisor of $\overline{\mathcal{M}}_{0,n}$ admits an expression in terms of boundary divisors and psi-classes. Recall that the boundary divisors $\delta_I$ (indexed by subsets $I \subset \{1, \ldots, n\}$ with $2 \leq |I| \leq n-2$, identifying $\delta_I = \delta_{I^c}$) correspond to stable curves with one node separating marked points labeled by $I$ from those labeled by $I^c$, and each is isomorphic to $\overline{\mathcal{M}}_{0,|I|+1} \times \overline{\mathcal{M}}_{0,|I^c|+1}$. The psi-classes $\psi_i = c_1(\mathbb{L}_i)$ are the first Chern classes of the cotangent line bundles at the $i$-th marked point.

The canonical class is given by the Knudsen--Mumford formula:
$$
K_{\overline{\mathcal{M}}_{0,n}} = \sum_{i=1}^{n} \psi_i - 2 \sum_I \delta_I.
$$

This can be derived from the relative dualizing sheaf of the forgetful morphism $\pi \colon \overline{\mathcal{M}}_{0,n} \to \overline{\mathcal{M}}_{0,n-1}$: one has $K_{\overline{\mathcal{M}}_{0,n}} = \pi^* K_{\overline{\mathcal{M}}_{0,n-1}} + \omega_\pi + \sum \sigma_i$, where $\sigma_i$ are the sections corresponding to boundary divisors where the $n$-th point separates from point $i$. Iterating this and using $K_{\overline{\mathcal{M}}_{0,3}} = 0$ yields the formula above.

**Verification on $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_4 \mathbb{P}^2$.** In this case, $K_{\operatorname{Bl}_4 \mathbb{P}^2} = -3H + E_1 + E_2 + E_3 + E_4$ where $H$ is the pullback of the hyperplane class and $E_i$ are the exceptional divisors. The 10 boundary divisors $\delta_I$ (with $|I| = 2$) correspond to the 4 exceptional divisors and the 6 proper transforms of lines through pairs of blown-up points. The formula $K = \sum \psi_i - 2\sum \delta_I$ can be verified by matching intersection numbers with $F$-curves (one-dimensional boundary strata).

For small $n$, the anti-canonical class $-K$ is ample, making $\overline{\mathcal{M}}_{0,n}$ a Fano variety (and in fact a Mori dream space): $\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^1$ and $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_4 \mathbb{P}^2$ are both Fano. For large $n$, the canonical class becomes effective, reflecting the transition from "few moduli" to "many moduli" behavior.

<!-- BENCHMARK_PROBLEM: For $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_{4}\mathbb{P}^{2}$, identify the boundary divisors $\delta_{I}$ in terms of the exceptional divisors and proper transforms of lines, and verify that the canonical class $K = -3H + E_{1} + E_{2} + E_{3} + E_{4}$ agrees with the formula $K = \sum \psi_{i} - 2\sum \delta_{I}$. -->

### Example: $\mathrm{rank}(H^{2}(\overline{\mathrm{M}}_{0,n}, \mathbb{Z}))$ {#ecag-0316}

The Picard group of $\overline{\mathcal{M}}_{0,n}$ is freely generated by the boundary divisor classes $\delta_I$, and the rank of $H^2(\overline{\mathcal{M}}_{0,n}, \mathbb{Z})$ equals $2^{n-1} - \binom{n}{2} - 1$ for $n \geq 3$.

**Counting boundary divisors.** The boundary divisors $\delta_I$ are indexed by subsets $I \subset \{1, \ldots, n\}$ with $2 \leq |I| \leq n-2$, subject to the identification $\delta_I = \delta_{I^c}$. The number of such divisors is
$$
\frac{1}{2}\sum_{k=2}^{n-2} \binom{n}{k} = \frac{1}{2}(2^n - 2 - 2n) = 2^{n-1} - n - 1.
$$

**The Keel relations.** By Keel's theorem, $H^*(\overline{\mathcal{M}}_{0,n}, \mathbb{Z})$ is generated as a ring by the $\delta_I$, subject to explicit quadratic relations: for any four distinct elements $i, j, k, l \in \{1, \ldots, n\}$,
$$
\sum_{\substack{I:\, i,j \in I \\ k,l \notin I}} \delta_I = \sum_{\substack{I:\, i,k \in I \\ j,l \notin I}} \delta_I.
$$

These WDVV (Witten--Dijkgraaf--Verlinde--Verlinde) relations are the only relations in degree 2, and they reduce the rank from $(2^{n-1} - n - 1)$ to $2^{n-1} - \binom{n}{2} - 1$.

**Verification.**

| $n$ | Boundary divisors | $\operatorname{rk} H^2$ | Geometric check |
|-----|------------------|-------------------------|----------------|
| $4$ | $3$ | $2^3 - 6 - 1 = 1$ | $\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^1$, $\operatorname{rk}\operatorname{Pic} = 1$ |
| $5$ | $10$ | $2^4 - 10 - 1 = 5$ | $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_4 \mathbb{P}^2$, $\operatorname{rk}\operatorname{Pic} = 5$ |
| $6$ | $25$ | $2^5 - 15 - 1 = 16$ | matches known $b_2 = 16$ |
| $7$ | $56$ | $2^6 - 21 - 1 = 42$ | |

The rank grows exponentially with $n$, reflecting the exponential growth of the boundary stratification.

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{rk} H^{2}(\overline{\mathcal{M}}_{0,7}, \mathbb{Z})$ using the formula $2^{n-1} - \binom{n}{2} - 1$. List how many boundary divisors $\delta_{I}$ exist for $n = 7$. -->

### Remark: $\mathrm{rank}(\mathrm{Pic}(\mathscr{K}_{g}))$ {#ecag-0317}

The rational Picard group of the Deligne--Mumford compactification $\overline{\mathscr{M}}_g$ (the moduli stack of stable curves of genus $g$) has rank $2 + \lfloor g/2 \rfloor$ for $g \geq 3$, with explicit generators given by the Hodge class $\lambda$ and the boundary divisor classes $\delta_0, \delta_1, \ldots, \delta_{\lfloor g/2 \rfloor}$. Here $\delta_0$ is the class of the locus of irreducible nodal curves, and $\delta_i$ for $i \geq 1$ corresponds to curves with a separating node where the two components have genera $i$ and $g - i$ (with $\delta_i = \delta_{g-i}$, so the index runs to $\lfloor g/2 \rfloor$).

Arbarello and Cornalba proved that $\operatorname{Pic}(\overline{\mathscr{M}}_g) \otimes \mathbb{Q}$ is freely generated by these classes:
$$
\operatorname{Pic}(\overline{\mathscr{M}}_g) \otimes \mathbb{Q} = \mathbb{Q}\lambda \oplus \mathbb{Q}\delta_0 \oplus \mathbb{Q}\delta_1 \oplus \cdots \oplus \mathbb{Q}\delta_{\lfloor g/2 \rfloor}.
$$

For example, at $g = 5$: $\operatorname{rk}(\operatorname{Pic}(\overline{\mathscr{M}}_5) \otimes \mathbb{Q}) = 2 + 2 = 4$, with generators $\lambda, \delta_0, \delta_1, \delta_2$. The coarse moduli space $\overline{M}_g$ has the same rational Picard rank.

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{rk}(\operatorname{Pic}(\overline{\mathscr{M}}_{g}) \otimes \mathbb{Q})$ for $g = 5$ and list the generators explicitly. -->

### Example: another computation of $\mathrm{Pic}(\mathscr{M}_{1,1})$ {#ecag-0318}

The Picard group of the moduli stack $\mathscr{M}_{1,1}$ of elliptic curves is $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$, generated by the Hodge bundle $\lambda$. This can be computed by reducing the problem to the character group of $\operatorname{SL}_2(\mathbb{Z})$.

Over $\mathbb{C}$, the upper half-plane $\mathfrak{h}$ uniformizes elliptic curves via $\tau \mapsto \mathbb{C}/(\mathbb{Z} + \mathbb{Z}\tau)$, giving $\mathscr{M}_{1,1}^{\mathrm{an}} \simeq [\mathfrak{h}/\operatorname{SL}_2(\mathbb{Z})]$. A line bundle on this quotient stack is an $\operatorname{SL}_2(\mathbb{Z})$-equivariant line bundle on $\mathfrak{h}$. Since $\mathfrak{h}$ is contractible, every line bundle on $\mathfrak{h}$ is trivial, and equivariant structures correspond to characters $\chi \colon \operatorname{SL}_2(\mathbb{Z}) \to \mathbb{C}^*$.

The group $\operatorname{SL}_2(\mathbb{Z})$ has the presentation as an amalgamated free product
$$
\operatorname{SL}_2(\mathbb{Z}) \cong \mathbb{Z}/4\mathbb{Z} \ast_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z},
$$

where the generator $S = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has order 4 and $T' = ST = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}$ has order 6, with $S^2 = (T')^3 = -I$. A character $\chi$ must send $S$ to a 4th root of unity and $T'$ to a 6th root of unity, subject to $\chi(S)^2 = \chi(T')^3$. The set of such pairs forms the fiber product
$$
\operatorname{Hom}(\operatorname{SL}_2(\mathbb{Z}), \mathbb{C}^*) \cong \mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}.
$$

To see this explicitly: $\chi(S) = i^a$ for $a \in \{0,1,2,3\}$ and $\chi(T') = e^{2\pi i b/6}$ for $b \in \{0,1,\ldots,5\}$, with $i^{2a} = e^{2\pi i \cdot 3b/6}$, i.e., $(-1)^a = (-1)^b$, so $a \equiv b \pmod{2}$. There are $2 \cdot 6 = 12$ valid pairs.

The Hodge bundle $\lambda$ corresponds to the character $\chi(\gamma) = (c\tau + d)^{-1}$ for $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, which is a generator of $\mathbb{Z}/12\mathbb{Z}$: we have $\chi(S) = \tau^{-1}|_{\tau = i} = -i = i^3$ (a primitive 4th root) and $\chi(T') = (\tau+1)^{-1}|_{\tau = e^{2\pi i/3}} = e^{-2\pi i/6}$ (a primitive 6th root).

<!-- BENCHMARK_PROBLEM: Show that $\operatorname{Hom}(\operatorname{SL}_{2}(\mathbb{Z}), \mathbb{C}^{*}) \cong \mathbb{Z}/12\mathbb{Z}$ using the presentation $\operatorname{SL}_{2}(\mathbb{Z}) \cong \mathbb{Z}/4\mathbb{Z} *_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z}$. -->
## Algebraic stacks
## Schemes as functors, sheaves on categories
It is highly recommended to read David Mumford's book *Lectures on curves on an algebraic surface*.

### Example: $\mathbb{A}_{\mathbb{Z}}^{1}$ {#ecag-0319}

The affine line $\mathbb{A}_{\mathbb{Z}}^1 = \operatorname{Spec}(\mathbb{Z}[t])$ represents the forgetful functor from schemes to sets sending $S$ to $\Gamma(S, \mathcal{O}_S)$. This is the most basic instance of the Yoneda lemma in algebraic geometry.

For any scheme $S$, a morphism $f \colon S \to \mathbb{A}_{\mathbb{Z}}^1 = \operatorname{Spec}(\mathbb{Z}[t])$ corresponds to a ring homomorphism $f^\sharp \colon \mathbb{Z}[t] \to \Gamma(S, \mathcal{O}_S)$, which is uniquely determined by the image $a = f^\sharp(t) \in \Gamma(S, \mathcal{O}_S)$. This follows from the universal property of the polynomial ring: $\mathbb{Z}[t]$ is the free $\mathbb{Z}$-algebra on one generator. The correspondence
$$
\operatorname{Hom}_{\mathrm{Sch}}(S, \mathbb{A}_{\mathbb{Z}}^1) \xrightarrow{\;\sim\;} \Gamma(S, \mathcal{O}_S), \qquad f \mapsto f^\sharp(t),
$$

is natural in $S$: for any morphism $g \colon S' \to S$, the composition $f \circ g$ corresponds to $g^\sharp(f^\sharp(t)) = g^\sharp(a)$, which is the pullback of the global section $a$ along $g$.

Over a base ring $R$, the scheme $\mathbb{A}_R^1 = \operatorname{Spec}(R[t])$ represents the same functor on $R$-schemes. When equipped with the comultiplication $m^*(t) = t \otimes 1 + 1 \otimes t$ and counit $e^*(t) = 0$, it becomes the additive group scheme $\mathbb{G}_a$ over $R$.

**Explicit example.** Let $S = \operatorname{Spec}(\mathbb{Z}[x]/(x^2 - 5x + 6))$. Then $\Gamma(S, \mathcal{O}_S) = \mathbb{Z}[x]/(x^2 - 5x + 6)$, and $\operatorname{Hom}(S, \mathbb{A}_{\mathbb{Z}}^1)$ is in bijection with elements of this ring. Equivalently, a morphism is determined by a polynomial $p(x) \in \mathbb{Z}[x]$ modulo $x^2 - 5x + 6$, i.e., by a pair $(a, b) \in \mathbb{Z}^2$ representing $a + bx$.

<!-- BENCHMARK_PROBLEM: Let $S = \operatorname{Spec}(\mathbb{Z}[x]/(x^{2} - 5x + 6))$. Describe $\operatorname{Hom}(S, \mathbb{A}_{\mathbb{Z}}^{1})$ explicitly and identify the corresponding elements of $\Gamma(S, \mathcal{O}_{S})$. -->

### Example: $\mathbb{P}_{\mathbb{Z}}^{n}$ {#ecag-0320}

Projective space $\mathbb{P}_{\mathbb{Z}}^n = \operatorname{Proj}(\mathbb{Z}[x_0, \ldots, x_n])$ represents the functor sending a scheme $S$ to the set of isomorphism classes of pairs $(\mathcal{L}, (s_0, \ldots, s_n))$, where $\mathcal{L}$ is a line bundle on $S$ and $s_0, \ldots, s_n \in \Gamma(S, \mathcal{L})$ generate $\mathcal{L}$:
$$
\operatorname{Hom}(S, \mathbb{P}_{\mathbb{Z}}^n) \cong \{(\mathcal{L}, s_0, \ldots, s_n) : s_i \in \Gamma(S, \mathcal{L}),\; (s_0, \ldots, s_n) \text{ generate } \mathcal{L}\}/{\cong}.
$$

**From morphisms to line bundles.** Given $f \colon S \to \mathbb{P}^n$, set $\mathcal{L} = f^*\mathcal{O}(1)$ and $s_i = f^*(x_i)$. The sections generate $\mathcal{L}$ because $x_0, \ldots, x_n$ generate $\mathcal{O}(1)$ on $\mathbb{P}^n$.

**From line bundles to morphisms.** Given $(\mathcal{L}, s_0, \ldots, s_n)$ with the $s_i$ generating $\mathcal{L}$, define $U_i = \{p \in S : s_i(p) \neq 0\}$. The generating condition ensures $S = \bigcup U_i$. On each $U_i$, the ratios $s_j/s_i \in \Gamma(U_i, \mathcal{O}_S)$ are well-defined, and the map $f_i \colon U_i \to \mathbb{A}^n \subset \mathbb{P}^n$ given by $f_i^*(x_j/x_i) = s_j/s_i$ is a morphism. On $U_i \cap U_j$, the transition functions $s_i/s_j$ are invertible and match the standard gluing of $\mathbb{P}^n$, so the $f_i$ glue to a global morphism $f \colon S \to \mathbb{P}^n$.

These constructions are inverse to each other up to the equivalence $(\mathcal{L}, s_0, \ldots, s_n) \sim (\mathcal{L}', s_0', \ldots, s_n')$ whenever there is an isomorphism $\phi \colon \mathcal{L} \xrightarrow{\sim} \mathcal{L}'$ with $\phi(s_i) = s_i'$ for all $i$.

**The case $S = \operatorname{Spec}(\mathbb{Z})$.** Every line bundle on $\operatorname{Spec}(\mathbb{Z})$ is trivial (since $\mathbb{Z}$ is a PID), so a morphism $\operatorname{Spec}(\mathbb{Z}) \to \mathbb{P}_{\mathbb{Z}}^n$ corresponds to $(n+1)$-tuples $(s_0, \ldots, s_n) \in \mathbb{Z}^{n+1}$ generating $\mathbb{Z}$ as an ideal, modulo simultaneous scaling by $\pm 1$. For $n = 1$: the set of morphisms $\operatorname{Spec}(\mathbb{Z}) \to \mathbb{P}_{\mathbb{Z}}^1$ is in bijection with $\{(a, b) \in \mathbb{Z}^2 : \gcd(a, b) = 1\}/\{(a,b) \sim (-a,-b)\}$.

<!-- BENCHMARK_PROBLEM: Let $S = \operatorname{Spec}(\mathbb{Z})$. Classify all morphisms $S \to \mathbb{P}_{\mathbb{Z}}^{1}$ by identifying all line bundles on $S$ equipped with pairs of generating global sections, up to isomorphism. -->

### Example: Fano scheme and its tangent space {#ecag-0321}

The Fano scheme $F_k(X)$ of $k$-dimensional linear subspaces contained in a projective variety $X \subset \mathbb{P}^n$ is a closed subscheme of the Grassmannian $\operatorname{Gr}(k+1, n+1)$. Its Zariski tangent space at a point $[\Lambda]$ corresponding to a $k$-plane $\Lambda \cong \mathbb{P}^k \subset X$ is
$$
T_{[\Lambda]} F_k(X) \cong H^0(\Lambda, \mathcal{N}_{\Lambda/X}),
$$

where $\mathcal{N}_{\Lambda/X}$ is the normal bundle of $\Lambda$ in $X$.

**Representability.** The Fano scheme represents the functor $S \mapsto \{(V, f) : V \subset \mathcal{O}_S^{n+1} \text{ rank-}(k+1) \text{ subbundle},\, f^*I_X = 0\}$. Concretely, if $X = V(F_1, \ldots, F_m) \subset \mathbb{P}^n$, the conditions $F_j|_\Lambda = 0$ cut out $F_k(X)$ as a closed subscheme of $\operatorname{Gr}(k+1, n+1)$.

**Tangent space computation.** A first-order deformation of $[\Lambda]$ in $F_k(X)$ is a flat family of $(k+1)$-planes in $\mathbb{P}^n$ over $\operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ contained in $X$. The tangent space of the Grassmannian at $[\Lambda]$ is $T_{[\Lambda]} \operatorname{Gr}(k+1, n+1) \cong \operatorname{Hom}(\mathcal{S}|_\Lambda, \mathcal{Q}|_\Lambda) \cong H^0(\Lambda, \mathcal{N}_{\Lambda/\mathbb{P}^n})$. The condition that the deformed plane stays inside $X$ is captured by the normal bundle sequence
$$
0 \to \mathcal{N}_{\Lambda/X} \to \mathcal{N}_{\Lambda/\mathbb{P}^n} \to \mathcal{N}_{X/\mathbb{P}^n}|_\Lambda \to 0,
$$

and the tangent space $T_{[\Lambda]} F_k(X)$ is the kernel of the induced map on global sections, which equals $H^0(\Lambda, \mathcal{N}_{\Lambda/X})$.

**Lines on a cubic surface.** Let $X \subset \mathbb{P}^3$ be a smooth cubic surface and $\ell \subset X$ a line. Then $\mathcal{N}_{\ell/\mathbb{P}^3} \cong \mathcal{O}_\ell(1)^{\oplus 2}$ (normal bundle of a line in $\mathbb{P}^3$) and $\mathcal{N}_{X/\mathbb{P}^3}|_\ell \cong \mathcal{O}_\ell(3)$ (restriction of $\mathcal{O}(3)$ to $\ell$). From the exact sequence we get $\mathcal{N}_{\ell/X} \cong \mathcal{O}_\ell(-1)$ (using $\operatorname{rk} = 1$ and $\deg = 1 + 1 - 3 = -1$). Since $H^0(\mathbb{P}^1, \mathcal{O}(-1)) = 0$, each of the 27 lines on $X$ is a reduced isolated point of $F_1(X)$.

**Lines on a cubic threefold.** For a smooth cubic threefold $X \subset \mathbb{P}^4$ and a line $\ell \subset X$: $\mathcal{N}_{\ell/\mathbb{P}^4} \cong \mathcal{O}_\ell(1)^{\oplus 3}$ and $\mathcal{N}_{X/\mathbb{P}^4}|_\ell \cong \mathcal{O}_\ell(3)$. From the normal bundle sequence, $\mathcal{N}_{\ell/X}$ has rank 2 and degree $3 - 3 = 0$. For a general line, $\mathcal{N}_{\ell/X} \cong \mathcal{O}_\ell \oplus \mathcal{O}_\ell$, giving $\dim T_{[\ell]} F_1(X) = h^0(\mathcal{O}^{\oplus 2}) = 2$. This is consistent with $F_1(X)$ being a smooth surface (the famous Fano surface of lines).

<!-- BENCHMARK_PROBLEM: Let $X \subset \mathbb{P}^{4}$ be a smooth cubic threefold and $\ell \subset X$ a line. Compute $\mathcal{N}_{\ell/X}$ using the normal bundle sequence, and determine $\dim T_{[\ell]} F_{1}(X)$. -->

### Example: Grassmannian {#ecag-0322}

The Grassmannian $\operatorname{Gr}(k, n)$ represents the functor sending a scheme $S$ to the set of rank-$k$ locally free quotients of $\mathcal{O}_S^n$ (equivalently, rank-$k$ subbundles of $\mathcal{O}_S^n$):
$$
h_{\operatorname{Gr}(k,n)}(S) = \{\mathcal{E} \subset \mathcal{O}_S^n : \mathcal{E} \text{ locally free of rank } k,\; \mathcal{O}_S^n/\mathcal{E} \text{ locally free}\}.
$$

It is a smooth projective scheme of dimension $k(n-k)$ over $\mathbb{Z}$, with $\operatorname{Pic}(\operatorname{Gr}(k,n)) \cong \mathbb{Z}$ generated by the Plucker line bundle $\det(\mathcal{S}^{\vee})$.

**Affine charts.** The standard open cover is indexed by subsets $I \subset \{1, \ldots, n\}$ with $|I| = k$. Over the chart $U_I$, the subbundle $\mathcal{E}$ is the row space of a $k \times n$ matrix whose $I$-columns form the identity matrix. The remaining $k(n-k)$ entries are free parameters, giving $U_I \cong \mathbb{A}^{k(n-k)}$.

**The Plucker embedding.** The map $\operatorname{Gr}(k, n) \hookrightarrow \mathbb{P}(\bigwedge^k \mathbb{Z}^n) = \mathbb{P}^{\binom{n}{k}-1}$ sends $\mathcal{E}$ to $\bigwedge^k \mathcal{E} \subset \bigwedge^k \mathcal{O}_S^n$. The image is cut out by the quadratic Plucker relations.

**Tautological bundles.** On $\operatorname{Gr}(k, n)$ there is a tautological exact sequence
$$
0 \to \mathcal{S} \to \mathcal{O}^n \to \mathcal{Q} \to 0,
$$

where $\mathcal{S}$ has rank $k$ (tautological subbundle) and $\mathcal{Q}$ has rank $n - k$ (tautological quotient). The tangent bundle is $T_{\operatorname{Gr}(k,n)} \cong \mathcal{S}^{\vee} \otimes \mathcal{Q}$.

**Examples and computations.**

| Grassmannian | $\dim$ | Plucker space | Description |
|-------------|--------|---------------|-------------|
| $\operatorname{Gr}(1, n) = \mathbb{P}^{n-1}$ | $n - 1$ | $\mathbb{P}^{n-1}$ | projective space |
| $\operatorname{Gr}(2, 4)$ | $4$ | $\mathbb{P}^5$ | smooth quadric hypersurface |
| $\operatorname{Gr}(2, 5)$ | $6$ | $\mathbb{P}^9$ | degree 5, codimension 3 |

For $\operatorname{Gr}(2, 5)$: dimension $= 2 \cdot 3 = 6$, Plucker embedding dimension $= \binom{5}{2} - 1 = 9$, and the degree in the Plucker embedding is $\frac{6!}{1! \cdot 2! \cdot 3!} = \frac{720}{12} = 5$ (computed via the formula for the degree of a Grassmannian as a product of hook lengths).

<!-- BENCHMARK_PROBLEM: Compute the dimension of $\operatorname{Gr}(2, 5)$, its Plucker embedding dimension, and the degree of the Grassmannian in its Plucker embedding. -->

### Remark {#ecag-0323}

The graph of a morphism $f \colon X \to Y$ to a separated scheme $Y$ is a closed subscheme of $X \times Y$. To see this, note that $\Gamma_f = (\operatorname{id}_X, f)^{-1}(\Delta_Y)$, where $\Delta_Y \subset Y \times Y$ is the diagonal. Since $Y$ is separated, $\Delta_Y$ is closed, and the preimage of a closed set is closed. Moreover, $\Gamma_f \to X$ (projection to the first factor) is an isomorphism with inverse $x \mapsto (x, f(x))$, so $\Gamma_f$ is a closed subscheme of $X \times Y$ isomorphic to $X$.

Separatedness is essential: for the line with a doubled origin $Y$, the diagonal $\Delta_Y$ is not closed in $Y \times Y$, and the "graph" of the identity $Y \to Y$ is not closed in $Y \times Y$.

<!-- BENCHMARK_PROBLEM: Let $f \colon \mathbb{A}^1 \to \mathbb{P}^1$ be the open inclusion. Show that the graph $\Gamma_f$ is a closed subscheme of $\mathbb{A}^1 \times \mathbb{P}^1$, and describe its ideal sheaf. -->


### Example: Quotient stack $[\mathbb{A}^{n}/GL_{n}]$ {#ecag-0324}

The quotient stack $[\mathbb{A}^n/\operatorname{GL}_n]$, where $\operatorname{GL}_n$ acts on $\mathbb{A}^n$ by the standard representation, is the moduli stack parametrizing pairs $(\mathcal{V}, s)$ where $\mathcal{V}$ is a rank-$n$ vector bundle and $s$ is a global section. Its coarse moduli space is a single point.

**The groupoid of $S$-points.** By definition, the $S$-points of $[\mathbb{A}^n/\operatorname{GL}_n]$ form a groupoid whose objects are pairs $(\mathcal{E}, s)$ where $\mathcal{E}$ is a $\operatorname{GL}_n$-torsor on $S$ and $s \colon S \to \mathcal{E} \times^{\operatorname{GL}_n} \mathbb{A}^n$ is a section. A $\operatorname{GL}_n$-torsor on $S$ is equivalent (via the associated bundle construction) to a rank-$n$ vector bundle $\mathcal{V}$ on $S$, and the associated space $\mathcal{E} \times^{\operatorname{GL}_n} \mathbb{A}^n$ is the total space of $\mathcal{V}$. A section is simply an element $s \in \Gamma(S, \mathcal{V})$. Morphisms in the groupoid are bundle isomorphisms $\phi \colon \mathcal{V} \xrightarrow{\sim} \mathcal{V}'$ with $\phi(s) = s'$.

Thus:
$$
[\mathbb{A}^n/\operatorname{GL}_n](S) \simeq \{(\mathcal{V}, s) : \mathcal{V} \text{ rank-}n \text{ vector bundle on } S,\; s \in \Gamma(S, \mathcal{V})\}.
$$

**Orbit structure.** The orbit space $\mathbb{A}^n/\operatorname{GL}_n$ has exactly two orbits: $\{0\}$ and $\mathbb{A}^n \setminus \{0\}$ (the latter because $\operatorname{GL}_n$ acts transitively on nonzero vectors). Their stabilizers differ dramatically: the stabilizer of $0$ is all of $\operatorname{GL}_n$, while the stabilizer of a nonzero vector $v$ is the subgroup of matrices fixing $v$, isomorphic to the affine group $k^{n-1} \rtimes \operatorname{GL}_{n-1}$.

The coarse moduli space $\operatorname{Spec}(k[\mathbb{A}^n]^{\operatorname{GL}_n}) = \operatorname{Spec}(k)$ is a single point, collapsing both orbits. The stack $[\mathbb{A}^n/\operatorname{GL}_n]$ remembers the stabilizers at each point, which is why stacks are necessary for moduli problems with nontrivial automorphisms.

**The case $n = 1$.** For $[\mathbb{A}^1/\mathbb{G}_m]$, the $S$-points are pairs $(\mathcal{L}, s)$ where $\mathcal{L}$ is a line bundle on $S$ and $s \in \Gamma(S, \mathcal{L})$. The two orbits are $\{0\}$ (stabilizer $\mathbb{G}_m$) and $\mathbb{A}^1 \setminus \{0\}$ (trivial stabilizer). The coarse moduli space is again $\operatorname{Spec}(k)$.

<!-- BENCHMARK_PROBLEM: Describe the groupoid of $S$-points of $[\mathbb{A}^{n}/\operatorname{GL}_{n}]$ for $n = 1$, and identify the stabilizer groups of the two orbits in $\mathbb{A}^{1}$. -->

### Example: Examples of algebraic stacks without coarse moduli space {#ecag-0325}

Not every algebraic stack admits a coarse moduli space. The Keel--Mori theorem guarantees existence for separated Deligne--Mumford stacks with finite inertia, but Artin stacks with infinite stabilizer groups typically have no coarse moduli space.

**The stack $[\mathbb{A}^1/\mathbb{G}_m]$.** Let $\mathbb{G}_m$ act on $\mathbb{A}^1$ by scaling: $t \cdot x = tx$. The orbits are $\{0\}$ (with stabilizer $\mathbb{G}_m$) and $\mathbb{A}^1 \setminus \{0\}$ (a single free orbit). A coarse moduli space $M$ would need to be an algebraic space with a map $\mathscr{X} = [\mathbb{A}^1/\mathbb{G}_m] \to M$ that is initial among maps to algebraic spaces and induces a bijection on geometric points.

Since there are two orbits, $M$ should have two geometric points. However, the GIT quotient is
$$
\mathbb{A}^1 /\!/ \mathbb{G}_m = \operatorname{Spec}(k[x]^{\mathbb{G}_m}) = \operatorname{Spec}(k),
$$

since the only $\mathbb{G}_m$-invariant regular functions on $\mathbb{A}^1$ are constants. This single point cannot induce a bijection on geometric points (two orbits would need to map to distinct points), so $\operatorname{Spec}(k)$ fails the defining property of a coarse moduli space.

Attempting to give $M$ two points as an algebraic space also fails: the map $\mathbb{A}^1 \to M$ (composing the atlas with the coarse map) would need to send $0$ to one point and $\mathbb{A}^1 \setminus \{0\}$ to another. The preimage of the open orbit's image would be $\mathbb{A}^1 \setminus \{0\}$, which is open. But one cannot construct an algebraic space with these properties that satisfies the universal property.

**The classifying stack $B\mathbb{G}_m$.** The classifying stack $B\mathbb{G}_m = [\operatorname{Spec}(k)/\mathbb{G}_m]$ (trivial action) has a single geometric point but stabilizer $\mathbb{G}_m$. Any map to an algebraic space $M$ factors through a point, but $B\mathbb{G}_m$ is not equivalent to a point (it has nontrivial automorphisms). Again, no coarse moduli space exists.

The Keel--Mori theorem precisely identifies the obstruction: a coarse moduli space exists if and only if the inertia stack $I_{\mathscr{X}} \to \mathscr{X}$ is finite. For $[\mathbb{A}^1/\mathbb{G}_m]$, the stabilizer at $0$ is $\mathbb{G}_m$, which is not finite.

<!-- BENCHMARK_PROBLEM: Let $\mathscr{X} = [\mathbb{A}^{1}/\mathbb{G}_{m}]$ where $\mathbb{G}_{m}$ acts by scaling. Show that the GIT quotient $\mathbb{A}^{1} /\!/ \mathbb{G}_{m} = \operatorname{Spec}(k[t]^{\mathbb{G}_{m}}) = \operatorname{Spec}(k)$ is a single point, and explain why this fails to be a coarse moduli space for $\mathscr{X}$. -->

### Example: $x^{2}+y^{3}=z^{7}$ {#ecag-0326}

The Diophantine equation $x^{2} + y^{3} = z^{7}$ has infinitely many coprime integer solutions. The connection to moduli theory runs through the observation that for a given nonzero $z$, the pair $(x, y)$ lies on the curve $Y^{2} = X^{3} - z^{7}$, which is an elliptic curve with $j$-invariant $j = 0$. Varying $z$ produces a family of elliptic curves with constant $j$-invariant, linking the Diophantine problem to the moduli of elliptic curves with enhanced structure.

**Reduction to the Klein quartic.** Poonen, Schaefer, and Stoll showed that finding primitive solutions (i.e., $\gcd(x, y, z) = 1$) is equivalent to finding rational points on certain twists of the modular curve $X(7)$, which parametrizes elliptic curves equipped with full level-$7$ structure. The curve $X(7)$ is realized in $\mathbb{P}^{2}$ as the Klein quartic


$$
x^{3}y + y^{3}z + z^{3}x = 0,
$$

a smooth curve of genus $3$. Its automorphism group is $\operatorname{PSL}_{2}(\mathbb{F}_{7})$, of order $168$. This is the maximum possible for genus $3$, since the Hurwitz bound gives $|\operatorname{Aut}(C)| \leq 84(g - 1) = 84 \cdot 2 = 168$.

**Genus computation via the Hurwitz formula.** The quotient map $X(7) \to X(7)/\operatorname{PSL}_{2}(\mathbb{F}_{7}) \cong X(1) \cong \mathbb{P}^{1}$ has degree $168$. The ramification occurs above three points of $\mathbb{P}^{1}$: above $j = 0$ the stabilizers have order $7$, yielding $168/7 = 24$ branch points each with $e_{P} - 1 = 6$; above $j = 1728$ the stabilizers have order $2$, yielding $84$ points each contributing $1$; and above $j = \infty$ the stabilizers have order $3$, yielding $56$ points each contributing $2$. The Hurwitz formula gives
$$
2g(X(7)) - 2 = 168(2 \cdot 0 - 2) + 24 \cdot 6 + 84 \cdot 1 + 56 \cdot 2 = -336 + 144 + 84 + 112 = 4,
$$

so $g(X(7)) = 3$. This is consistent with the Klein quartic being a smooth plane curve of degree $4$, for which the degree-genus formula gives $(4-1)(4-2)/2 = 3$.

**Primitive solutions.** Direct verification confirms the known primitive solutions:

| $(x, y, z)$ | $x^{2}$ | $y^{3}$ | $z^{7}$ | Check |
|---|---|---|---|---|
| $(0, 1, 1)$ | $0$ | $1$ | $1$ | $0 + 1 = 1$ |
| $(1, 0, 1)$ | $1$ | $0$ | $1$ | $1 + 0 = 1$ |
| $(-1, 0, 1)$ | $1$ | $0$ | $1$ | $1 + 0 = 1$ |
| $(1, -1, 0)$ | $1$ | $-1$ | $0$ | $1 - 1 = 0$ |
| $(-1, -1, 0)$ | $1$ | $-1$ | $0$ | $1 - 1 = 0$ |

All entries have $\gcd(x, y, z) = 1$, confirming they are primitive. The existence of infinitely many further primitive solutions follows from the analysis of rational points on the relevant twists of $X(7)$.

<!-- BENCHMARK_PROBLEM: Verify that $(x, y, z) = (0, 1, 1)$ and $(\pm 1, 0, 1)$ are primitive integer solutions to $x^{2} + y^{3} = z^{7}$. Compute the genus of the modular curve $X(7)$ using the Hurwitz formula applied to the covering $X(7) \to X(1) \cong \mathbb{P}^{1}$. -->

### Example: $(p-1)/24$ supersingular elliptic curves in characteristic $p$ {#ecag-0327}

Over an algebraically closed field $\bar{\mathbb{F}}_{p}$ of characteristic $p \geq 5$, the number of supersingular elliptic curves up to isomorphism, weighted by automorphisms, is governed by the Eichler--Deuring mass formula:

$$\sum_{E/\bar{\mathbb{F}}_{p} \text{ supersingular}} \frac{1}{|\operatorname{Aut}(E)|} = \frac{p - 1}{24},$$

where the sum runs over isomorphism classes of supersingular elliptic curves over $\bar{\mathbb{F}}_{p}$.

An elliptic curve $E$ over $\bar{\mathbb{F}}_{p}$ is supersingular if $E[p](\bar{\mathbb{F}}_{p}) = 0$, or equivalently if $\operatorname{End}(E) \otimes \mathbb{Q}$ is a quaternion algebra (rather than an imaginary quadratic field). The mass formula arises from the Eichler--Deuring correspondence, which identifies isomorphism classes of supersingular elliptic curves with classes of maximal orders in the quaternion algebra $B_{p,\infty}$ ramified at $p$ and $\infty$. The Minkowski--Siegel mass formula for the genus of maximal orders yields the factor $(p-1)/24$.

**Automorphism groups.** For a generic elliptic curve, $\operatorname{Aut}(E) = \{\pm 1\}$ so $|\operatorname{Aut}(E)| = 2$. The exceptions are $|\operatorname{Aut}(E)| = 4$ when $j(E) = 1728$ (provided $p \neq 2$) and $|\operatorname{Aut}(E)| = 6$ when $j(E) = 0$ (provided $p \neq 3$). Whether these special $j$-values are supersingular depends on $p \bmod 12$.

**Verification for small primes.**

| $p$ | $(p-1)/24$ | Supersingular $j$-values | $\lvert\operatorname{Aut}\rvert$ | Mass check |
|---|---|---|---|---|
| $5$ | $1/6$ | $j = 0$ | $6$ | $1/6$ |
| $7$ | $1/4$ | $j = 1728$ | $4$ | $1/4$ |
| $11$ | $5/12$ | $j = 0,\; 1728$ | $6,\; 4$ | $1/6 + 1/4 = 5/12$ |
| $13$ | $1/2$ | $j = 5$ | $2$ | $1/2$ |
| $17$ | $2/3$ | $j = 0,\; 8$ | $6,\; 2$ | $1/6 + 1/2 = 2/3$ |
| $19$ | $3/4$ | $j = 1728,\; 18$ | $4,\; 2$ | $1/4 + 1/2 = 3/4$ |
| $23$ | $11/12$ | $j = 0,\; 1728,\; 19$ | $6,\; 4,\; 2$ | $1/6 + 1/4 + 1/2 = 11/12$ |

For $p = 13$, the unique supersingular $j$-invariant is $j = 5$ (since neither $j = 0$ nor $j = 1728$ is supersingular in characteristic $13$), and $|\operatorname{Aut}(E)| = 2$ since $5 \notin \{0, 1728\}$, giving mass $1/2 = (13-1)/24$. The factor $1/24$ in the mass formula reflects the orbifold Euler characteristic of $\mathscr{M}_{1,1}$: the coarse moduli space $M_{1,1} \cong \mathbb{A}^{1}_{j}$ has Euler characteristic $1$, but the stack $\mathscr{M}_{1,1}$ accounts for the automorphism groups at each point, and the Gauss--Bonnet theorem on this orbifold produces the rational number $(p-1)/24$.

<!-- BENCHMARK_PROBLEM: For $p = 13$, use the mass formula $\sum 1/|\operatorname{Aut}(E)| = (p-1)/24 = 1/2$ to determine the number and $j$-invariants of supersingular elliptic curves over $\bar{\mathbb{F}}_{13}$. -->

### Example: Mumford, Picard groups of moduli problems {#ecag-0328}

In his foundational paper "Picard groups of moduli problems," Mumford computed $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$ over an algebraically closed field of characteristic not $2$ or $3$, generated by the Hodge bundle $\lambda$. The method exploits elliptic curves with enhanced automorphisms to extract numerical invariants that pin down the Picard group.

A line bundle $\mathscr{L}$ on the moduli stack $\mathscr{M}_{1,1}$ assigns to each family $\pi: \mathscr{X} \to S$ a line bundle $\mathscr{L}_{\pi}$ on $S$, compatibly with base change. For a single elliptic curve $C$ over $\operatorname{Spec}(k)$, every automorphism $\alpha \in \operatorname{Aut}(C)$ induces a scalar $\mathscr{L}(\alpha) \in k^{*}$ acting on the one-dimensional fiber $\mathscr{L}|_{C}$.

**The invariant $\beta$.** Consider the two elliptic curves with enhanced automorphisms: $C_{1}: y^{2} = x^{3} - x$ with $j = 1728$ and $\operatorname{Aut}(C_{1}) \cong \mathbb{Z}/4\mathbb{Z}$ generated by $\sigma: (x, y) \mapsto (-x, iy)$; and $C_{2}: y^{2} = x^{3} - 1$ with $j = 0$ and $\operatorname{Aut}(C_{2}) \cong \mathbb{Z}/6\mathbb{Z}$ generated by $\tau: (x, y) \mapsto (\omega x, -y)$ where $\omega = e^{2\pi i/3}$. A line bundle $\mathscr{L}$ determines $\mathscr{L}(\sigma) \in \mu_{4}$ and $\mathscr{L}(\tau) \in \mu_{6}$. The constraint $\sigma^{2} = \tau^{3} = [-1]$ forces $\mathscr{L}(\sigma)^{2} = \mathscr{L}(\tau)^{3}$, yielding
$$
\beta: \operatorname{Pic}(\mathscr{M}_{1,1}) \to \mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}.
$$

**Surjectivity via the Hodge bundle.** The Hodge bundle $\lambda$ assigns to a family $\pi$ the line bundle $\pi_{*}\omega_{\mathscr{X}/S}$, whose fiber over $C$ is $H^{0}(C, \omega_{C})$, spanned by $dx/(2y)$. Computing: $\sigma^{*}(dx/(2y)) = -dx/(2iy) = i \cdot dx/(2y)$, so $\lambda(\sigma) = i$; and $\tau^{*}(dx/(2y)) = \omega \cdot dx/(-2y) = -\omega \cdot dx/(2y)$, so $\lambda(\tau) = -\omega$, a primitive $6$th root. Hence $\beta(\lambda) = 1$, proving surjectivity.

**Injectivity.** If $\beta(\mathscr{L}) = 0$, all automorphisms act trivially on $\mathscr{L}$. Using the Legendre family $y^{2} = x(x-1)(x-t)$ over $S = \mathbb{A}^{1} \setminus \{0,1\}$ as an etale cover of $\mathscr{M}_{1,1}$, note $\operatorname{Pic}(S) = 0$, so $\mathscr{L}|_{S}$ is trivial. The triviality of $\beta(\mathscr{L})$ ensures any trivialization is compatible with descent data, giving $\mathscr{L} \cong \mathcal{O}_{\mathscr{M}_{1,1}}$.

<!-- BENCHMARK_PROBLEM: Compute the action of the automorphism $\sigma: (x, y) \mapsto (-x, iy)$ of the elliptic curve $C_{1}: y^{2} = x^{3} - x$ on the space of regular differentials $H^{0}(C_{1}, \omega_{C_{1}})$, and determine the order of the resulting scalar. -->
### Example: Tangent space of the Picard scheme {#ecag-0329}

Let $X$ be a proper scheme over a field $k$. Under suitable hypotheses (e.g., $X$ geometrically integral), the Picard scheme $\operatorname{Pic}_{X/k}$ represents the relative Picard functor. Its tangent space at the origin $[\mathcal{O}_{X}]$ is
$$
T_{[\mathcal{O}_{X}]} \operatorname{Pic}_{X/k} \cong H^{1}(X, \mathcal{O}_{X}).
$$

By definition, the tangent space is $\operatorname{Pic}_{X/k}(\operatorname{Spec}(k[\epsilon]/(\epsilon^{2})))$, the set of first-order deformations of $\mathcal{O}_{X}$. A line bundle on $X[\epsilon] := X \times \operatorname{Spec}(k[\epsilon])$ restricting to $\mathcal{O}_{X}$ on the closed fiber lies in the kernel of the restriction $H^{1}(X[\epsilon], \mathcal{O}_{X[\epsilon]}^{*}) \to H^{1}(X, \mathcal{O}_{X}^{*})$.

**Computing the kernel.** Consider the exact sequence of sheaves on $X$:
$$
1 \to 1 + \epsilon \cdot \mathcal{O}_{X} \to \mathcal{O}_{X[\epsilon]}^{*} \to \mathcal{O}_{X}^{*} \to 1.
$$

The sheaf $1 + \epsilon \cdot \mathcal{O}_{X}$ is isomorphic to $\mathcal{O}_{X}$ as an additive group via $1 + \epsilon f \mapsto f$. The associated long exact sequence in cohomology reads
$$
H^{0}(X, \mathcal{O}_{X}^{*}) \to H^{1}(X, \mathcal{O}_{X}) \to H^{1}(X[\epsilon], \mathcal{O}_{X[\epsilon]}^{*}) \to H^{1}(X, \mathcal{O}_{X}^{*}).
$$

The connecting map from $H^{0}(X, \mathcal{O}_{X}^{*})$ is zero because global units on $X$ lift to units on $X[\epsilon]$. Therefore the kernel of the restriction map is exactly $H^{1}(X, \mathcal{O}_{X})$, which classifies first-order deformations of $\mathcal{O}_{X}$.

**Examples.** For a smooth projective curve $C$ of genus $g$, we get $\dim T_{[\mathcal{O}_{C}]} \operatorname{Pic}_{C/k} = g$, consistent with $\operatorname{Pic}^{0}_{C/k}$ being an abelian variety of dimension $g$ (the Jacobian). For $X = \mathbb{P}^{2}$, we have $H^{1}(\mathbb{P}^{2}, \mathcal{O}_{\mathbb{P}^{2}}) = 0$, so $\operatorname{Pic}^{0}_{\mathbb{P}^{2}/k}$ is trivial and $\operatorname{Pic}(\mathbb{P}^{2}) \cong \mathbb{Z}$ is discrete. More generally, for any smooth projective surface with $H^{1}(X, \mathcal{O}_{X}) = 0$, the Picard variety is trivial and the Picard group is finitely generated (the Neron--Severi group).

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective surface over $k$ with $H^{1}(X, \mathcal{O}_{X}) = 0$ (e.g., $X = \mathbb{P}^{2}$). What is the tangent space dimension of $\operatorname{Pic}_{X/k}$ at $[\mathcal{O}_{X}]$, and what does this tell you about $\operatorname{Pic}^{0}_{X/k}$? -->

### Example: Isotrivial but non-trivial family of elliptic curves {#ecag-0330}

The family of elliptic curves
$$
X := \operatorname{Spec}(k[x, y, t, t^{-1}]/(y^{2} - x^{3} + t)) \to \operatorname{Spec}(k[t, t^{-1}]) = \mathbb{G}_{m}
$$

is isotrivial but not trivial. The fibers $y^{2} = x^{3} - t$ all have $j$-invariant $j = 0$ (since the Weierstrass form $y^{2} = x^{3} + a$ has $j = 0$ whenever $a \neq 0$), so every fiber is isomorphic to $E_{0}: y^{2} = x^{3} - 1$ over $\bar{k}$. Nevertheless, $X \not\cong E_{0} \times \mathbb{G}_{m}$.

**The total space is affine.** The defining relation $t = y^{2} - x^{3}$ shows that
$$
X \cong \operatorname{Spec}(k[x, y, (y^{2} - x^{3})^{-1}]) = \mathbb{A}^{2}_{k} \setminus V(y^{2} - x^{3}),
$$

an open subscheme of $\mathbb{A}^{2}_{k}$. Since $y^{2} - x^{3}$ is irreducible, this complement is the principal open set $D(y^{2} - x^{3})$, which is affine.

**Non-triviality via Luroth's theorem.** Suppose for contradiction that $X \cong E \times \mathbb{G}_{m}$ for some elliptic curve $E$. Since $X$ is an open subset of $\mathbb{A}^{2}$, composing with the projection gives a dominant rational map $\mathbb{A}^{2} \dashrightarrow E$, which extends to $\mathbb{P}^{2} \dashrightarrow E$. This makes $E$ unirational. By Luroth's theorem, a unirational curve over an algebraically closed field is rational, so $E$ would have genus $0$. But $g(E) = 1$, a contradiction.

The obstruction to Zariski-local triviality is detected by the class of the associated $\operatorname{Aut}(E_{0})$-torsor in $H^{1}_{\text{et}}(\mathbb{G}_{m}, \operatorname{Aut}(E_{0}))$. Since $\operatorname{Aut}(E_{0}) \cong \mu_{6}$ (for $j = 0$), this torsor is nontrivial as a $\mu_{6}$-torsor over $\mathbb{G}_{m}$, corresponding to the class of $t$ in $k[t, t^{-1}]^{*}/(k[t, t^{-1}]^{*})^{6}$.

<!-- BENCHMARK_PROBLEM: Show that the total space of $y^{2} = x^{3} - t$ over $\operatorname{Spec}(k[t, t^{-1}])$ is isomorphic to the complement of $V(y^{2} - x^{3})$ in $\mathbb{A}^{2}_{k}$. Conclude that the total space is affine, and explain why this implies the family cannot be a trivial product $E \times \mathbb{G}_{m}$. -->

### Remark: Trivialization in etale topology {#ecag-0331}

The isotrivial family $y^{2} = x^{3} - t$ from the previous example becomes trivial after an etale base change. Consider the etale morphism

$$\phi: \operatorname{Spec}(k[t^{1/6}, t^{-1/6}]) \to \operatorname{Spec}(k[t, t^{-1}]),$$

corresponding to the ring map $t \mapsto (t^{1/6})^{6}$. This is etale because $6$ is invertible in $k$ (assuming $\operatorname{char}(k) \neq 2, 3$).

After pulling back the family along $\phi$, the substitution $x = t^{1/3} x'$, $y = t^{1/2} y'$ transforms the equation $y^{2} = x^{3} - t$ into $(y')^{2} = (x')^{3} - 1$, which is a constant curve. Explicitly, the pulled-back family is isomorphic to $E_{0} \times \operatorname{Spec}(k[t^{1/6}, t^{-1/6}])$ where $E_{0}: (y')^{2} = (x')^{3} - 1$.

The exponent $1/6$ is the least common multiple of $1/2$ and $1/3$, arising from the weights in the Weierstrass equation. This is an instance of the general principle that isotrivial families of elliptic curves are trivialized by etale covers whose degree divides $|\operatorname{Aut}(E)|$ (here $|\operatorname{Aut}(E_{0})| = 6$ since $j = 0$).
### Example: $\operatorname{pt}\rightarrow B\mathbb{G}_{m}$ is an $\mathrm{fppf}$ (even smooth and surjective) cover {#ecag-0332}

The morphism $\operatorname{pt} \to B\mathbb{G}_{m}$ corresponding to the trivial line bundle $\mathcal{O}$ is an fppf cover -- in fact, it is smooth and surjective. We verify this by computing the fiber product with an arbitrary map from a scheme.

Recall that $B\mathbb{G}_{m}$ is the classifying stack of $\mathbb{G}_{m}$: for any scheme $X$, the groupoid $B\mathbb{G}_{m}(X)$ has line bundles on $X$ as objects and isomorphisms between them as morphisms. A map $f: T \to B\mathbb{G}_{m}$ is the datum of a line bundle $\mathcal{L}$ on $T$.

**Computing the fiber product.** The map $\operatorname{pt} \to B\mathbb{G}_{m}$ corresponds to $\mathcal{O}_{\operatorname{pt}}$. For a test scheme $X$, a map $X \to T \times_{B\mathbb{G}_{m}} \operatorname{pt}$ consists of $g: X \to T$, $g': X \to \operatorname{pt}$, and an isomorphism $g^{*}\mathcal{L} \xrightarrow{\sim} \mathcal{O}_{X}$. When $g^{*}\mathcal{L} \cong \mathcal{O}_{X}$, the set of such trivializations is a $\mathbb{G}_{m}(X)$-torsor (since any two trivializations differ by a unit); otherwise it is empty.

**Representability.** Choose a Zariski trivialization $\{U_{i}\}$ of $\mathcal{L}$ with transition functions $g_{ij} \in \mathcal{O}^{*}(U_{i} \cap U_{j})$. The fiber product is obtained by gluing $\mathbb{G}_{m} \times U_{i}$ along $U_{i} \cap U_{j}$ via the same transition functions $g_{ij}$. This is precisely $\operatorname{Tot}(\mathcal{L}) \setminus \{0\}$, the total space of $\mathcal{L}$ with the zero section removed. Hence
$$
T \times_{B\mathbb{G}_{m}} \operatorname{pt} \cong \operatorname{Tot}(\mathcal{L}) \setminus \{0\text{-section}\},
$$

which is a scheme and a $\mathbb{G}_{m}$-torsor over $T$.

**Faithful flatness and smoothness.** The projection $\operatorname{Tot}(\mathcal{L}) \setminus \{0\} \to T$ is flat (as $\mathbb{G}_{m}$-torsors are flat), surjective (every point of $T$ has a nonzero element in the fiber of $\mathcal{L}$), and smooth (since $\mathbb{G}_{m}$ is smooth). This confirms $\operatorname{pt} \to B\mathbb{G}_{m}$ is a smooth surjective cover.

**Example.** For $T = \mathbb{P}^{1}$ and $\mathcal{L} = \mathcal{O}(1)$, the total space $\operatorname{Tot}(\mathcal{O}(1))$ is the blow-up of $\mathbb{A}^{2}$ at the origin (i.e., $\operatorname{Tot}(\mathcal{O}(1)) \cong \operatorname{Bl}_{0}(\mathbb{A}^{2})$). Removing the zero section (the exceptional divisor) gives $\operatorname{Tot}(\mathcal{O}(1)) \setminus \{0\} \cong \mathbb{A}^{2} \setminus \{0\}$, which is indeed faithfully flat over $\mathbb{P}^{1}$ via the canonical projection $(x, y) \mapsto [x : y]$. This is the universal $\mathbb{G}_{m}$-torsor: pulling $\operatorname{pt} \to B\mathbb{G}_{m}$ back along any map $T \to B\mathbb{G}_{m}$ recovers the associated frame bundle $\operatorname{Tot}(\mathcal{L}) \setminus \{0\}$.

<!-- BENCHMARK_PROBLEM: Let $T = \mathbb{P}^{1}$ and $\mathcal{L} = \mathcal{O}(1)$. Identify the scheme $T \times_{B\mathbb{G}_{m}} \operatorname{pt} = \operatorname{Tot}(\mathcal{O}(1)) \setminus \{0\}$ explicitly as a scheme, and verify that it is faithfully flat over $\mathbb{P}^{1}$. -->

### Remark: $T'\rightarrow B\mathbb{G}_{m}$ representable?(i.e any pull-back along this morphism is a scheme) {#ecag-0333}

Any morphism $T' \to B\mathbb{G}_{m}$ from a scheme $T'$ is representable. To verify this, by the diagonal criterion, it suffices to show that the diagonal $\Delta: B\mathbb{G}_{m} \to B\mathbb{G}_{m} \times B\mathbb{G}_{m}$ is representable. Given a scheme $T$ with a morphism $T \to B\mathbb{G}_{m} \times B\mathbb{G}_{m}$ corresponding to two line bundles $\mathcal{L}_{1}, \mathcal{L}_{2}$ on $T$, the fiber product

$$B\mathbb{G}_{m} \times_{B\mathbb{G}_{m} \times B\mathbb{G}_{m}} T$$

is the functor of isomorphisms $\operatorname{Isom}(\mathcal{L}_{1}, \mathcal{L}_{2})$. An isomorphism $\mathcal{L}_{1} \xrightarrow{\sim} \mathcal{L}_{2}$ is the same as a nowhere-vanishing section of $\mathcal{L}_{2} \otimes \mathcal{L}_{1}^{\vee}$. Thus

$$\operatorname{Isom}(\mathcal{L}_{1}, \mathcal{L}_{2}) \cong \operatorname{Tot}(\mathcal{L}_{2} \otimes \mathcal{L}_{1}^{\vee}) \setminus \{0\},$$

which is a scheme (an open subscheme of the total space of a line bundle). Therefore the diagonal is representable, and consequently any morphism from a scheme to $B\mathbb{G}_{m}$ is representable.

### Remark: `glue' {#ecag-0334}

When working with stacks, the notion of "gluing" is richer than for ordinary sheaves or schemes. For sheaves, gluing means identifying sections on overlaps to produce a global section. For stacks, gluing involves two distinct levels:

- **Descent for isomorphisms** (between two objects): Given two objects $\mathcal{E}, \mathcal{E}'$ over $X$ and isomorphisms $\phi_{i}: \mathcal{E}|_{U_{i}} \xrightarrow{\sim} \mathcal{E}'|_{U_{i}}$ that agree on overlaps, we can descend to a global isomorphism $\mathcal{E} \xrightarrow{\sim} \mathcal{E}'$.

- **Descent for objects** (defining a new object): Given objects $\mathcal{E}_{i}$ on $U_{i}$ with isomorphisms $\phi_{ij}: \mathcal{E}_{i}|_{U_{ij}} \xrightarrow{\sim} \mathcal{E}_{j}|_{U_{ij}}$ satisfying the cocycle condition $\phi_{jk} \circ \phi_{ij} = \phi_{ik}$ on triple overlaps, we can descend to a global object $\mathcal{E}$.

For a quotient stack $[X/G]$, the gluing data has a concrete geometric meaning: points in the same $G$-orbit are connected by isomorphisms ($x \cong gx$ for $g \in G$), and the stabilizer $\operatorname{Stab}(x) = \{g \in G : gx = x\}$ provides the automorphisms at each point. The stack remembers both the orbit structure and the stabilizers, unlike the coarse quotient $X/G$ which only remembers orbits.

### Example: quotient morphism $X\rightarrow X/G$ with no Zariski-local sections {#ecag-0335}

Let $G$ be a finite group acting freely on a smooth projective curve $X$ of genus $g \geq 1$ over an algebraically closed field $k$, with $|G| > 1$. The quotient morphism $\pi: X \to Y := X/G$ is a finite etale Galois cover of degree $|G|$, and it admits no Zariski-local sections.

Since the action is free, the Riemann--Hurwitz formula (with no ramification) gives $2g - 2 = |G|(2g_{Y} - 2)$, where $g_{Y}$ is the genus of $Y$.

**Proof of non-existence of sections.** Suppose for contradiction that $\pi$ admits a section $s: U \to X$ over some nonempty Zariski open $U \subset Y$. Then $s$ is a morphism with $\pi \circ s = \operatorname{id}_{U}$, so $s(U)$ is a locally closed subset of $X$ mapping isomorphically onto $U$. Since $\pi$ is finite etale of constant degree $|G|$, the preimage $\pi^{-1}(U)$ is a disjoint union of $|G|$ copies of $U$ (etale-locally), and the section singles out one component. This means the connected finite etale cover $\pi^{-1}(U) \to U$ splits off a trivial component. But $X$ is a smooth irreducible curve, so $\pi^{-1}(U)$ is connected (being a nonempty open subset of the irreducible $X$). A connected etale cover that admits a section must be trivial (degree $1$), contradicting $|G| > 1$.

**Example.** Let $E$ be an elliptic curve and $G = \mathbb{Z}/n\mathbb{Z}$ acting by translation by an $n$-torsion point $T \in E[n]$. The quotient $\pi: E \to E/G$ is an isogeny of degree $n$, which is etale (translations have no fixed points). By the argument above, $\pi$ admits no Zariski-local section. This illustrates why the etale topology, rather than the Zariski topology, is needed to trivialize torsors over varieties of positive genus.

<!-- BENCHMARK_PROBLEM: Let $E$ be an elliptic curve over an algebraically closed field and let $\pi: E \to E' = E/(\mathbb{Z}/2\mathbb{Z})$ be the quotient by the involution $P \mapsto -P$. Note this has fixed points, so modify: let $\pi: E \to E/\langle T \rangle$ where $T$ is a $2$-torsion point acting by translation. Show that this etale double cover admits no Zariski-local section. -->
### Example: $\mathrm{Pic}(BG)$ over an algebraically closed field $k$ {#ecag-0336}

Let $G$ be a finite group and $k$ an algebraically closed field with $\operatorname{char}(k) \nmid |G|$. Then
$$
\operatorname{Pic}(BG) \cong \operatorname{Hom}(G, k^{*}) = H^{1}(G, k^{*}),
$$

the group of characters of $G$. Line bundles on $BG$ are purely group-theoretic: they correspond to one-dimensional representations of $G$, because the underlying space is a point and all geometric complexity resides in the group action.

**Via descent.** Since $k = \bar{k}$, the $G$-torsor $\operatorname{pt} \to BG$ trivializes everything: every line bundle on $BG$ descends from a line bundle on $\operatorname{pt}$. The only line bundle on $\operatorname{pt}$ is $\mathcal{O}$, so a descent datum consists of specifying, for each $g \in G$, an automorphism $\alpha(g) \in \operatorname{Aut}(\mathcal{O}_{\operatorname{pt}}) \cong k^{*}$. The cocycle condition requires $\alpha(g_{1} g_{2}) = \alpha(g_{1}) \cdot \alpha(g_{2})$, i.e., $\alpha: G \to k^{*}$ is a group homomorphism. Two descent data are isomorphic if and only if they differ by a coboundary; since $\operatorname{Aut}(\mathcal{O})$ is abelian, all coboundaries are trivial. Hence $\operatorname{Pic}(BG) \cong \operatorname{Hom}(G, k^{*})$.

**Geometric realization.** Given a character $\chi: G \to k^{*}$ and a $G$-torsor $\mathcal{G}$ on a scheme $X$, the corresponding line bundle is the associated bundle
$$
\mathscr{L}_{\mathcal{G}} = \mathcal{G} \times_{G} \mathbb{A}^{1}_{k},
$$

where $G$ acts on $\mathbb{A}^{1}_{k}$ via $g \cdot a = \chi(g) \cdot a$.

**Examples.**

| $G$ | $\operatorname{Hom}(G, k^{*})$ | Generator |
|---|---|---|
| $\mathbb{Z}/n\mathbb{Z}$ | $\mathbb{Z}/n\mathbb{Z}$ | $1 \mapsto \zeta_{n}$ (primitive $n$th root) |
| $S_{3}$ | $\mathbb{Z}/2\mathbb{Z}$ | sign character |
| $\mathbb{G}_{m}$ | $\mathbb{Z}$ | $t \mapsto t^{n}$ for $n \in \mathbb{Z}$ |

For $G = \mathbb{G}_{m}$, the isomorphism $\operatorname{Pic}(B\mathbb{G}_{m}) \cong \mathbb{Z}$ is consistent with the topological picture $B\mathbb{G}_{m}(\mathbb{C}) \simeq \mathbb{CP}^{\infty}$, giving $\operatorname{Pic}(B\mathbb{G}_{m}) \cong H^{2}(\mathbb{CP}^{\infty}, \mathbb{Z}) \cong \mathbb{Z}$. For $G = \mathbb{Z}/n\mathbb{Z}$, the generator of $\operatorname{Pic}(B(\mathbb{Z}/n\mathbb{Z})) \cong \mathbb{Z}/n\mathbb{Z}$ is the descent datum $\alpha: 1 \mapsto \zeta_{n}$ on $\operatorname{pt} \to B(\mathbb{Z}/n\mathbb{Z})$.

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{Pic}(B(\mathbb{Z}/n\mathbb{Z}))$ over an algebraically closed field $k$ with $\operatorname{char}(k) \nmid n$, and identify the generator explicitly as a descent datum on $\operatorname{pt} \to B(\mathbb{Z}/n\mathbb{Z})$. -->

### Example: $\mathrm{Pic}(\mathscr{M}_{1,1})$ over a field $k$, $char(k)\neq 2,3$, algebraic method {#ecag-0337}

Over a field $k$ with $\operatorname{char}(k) \neq 2, 3$, the Picard group of the moduli stack of elliptic curves is
$$
\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z},
$$

generated by the Hodge bundle $\Lambda$. This is Mumford's theorem from "Picard groups of moduli problems." The proof below follows Mumford's original algebraic method, constructing an invariant $\beta$ from the automorphism groups of special elliptic curves.

**The inversion invariant $\alpha$.** Every elliptic curve has the inversion automorphism $\rho = [-1]$ of order $2$. A line bundle $\mathscr{L}$ on $\mathscr{M}_{1,1}$ induces $\mathscr{L}(\rho) = \pm 1$ on any connected family. Evaluating on the Legendre family $E_{t}: y^{2} = x(x-1)(x-t)$ over $\mathbb{A}^{1} \setminus \{0, 1\}$ gives a homomorphism $\alpha: \operatorname{Pic}(\mathscr{M}_{1,1}) \to \mathbb{Z}/2\mathbb{Z}$.

**Refining to $\beta$.** The curves $C_{1}: y^{2} = x^{3} - x$ ($j = 1728$) and $C_{2}: y^{2} = x^{3} - 1$ ($j = 0$) have enhanced automorphisms $\sigma: (x,y) \mapsto (-x, iy)$ of order $4$ and $\tau: (x,y) \mapsto (\omega x, -y)$ of order $6$. Since $\sigma^{2} = \tau^{3} = \rho$, the scalars $\mathscr{L}(\sigma) \in \mu_{4}$ and $\mathscr{L}(\tau) \in \mu_{6}$ satisfy $\mathscr{L}(\sigma)^{2} = \mathscr{L}(\tau)^{3} = \alpha(\mathscr{L})$. Fixing a primitive $12$th root $\zeta$, there is a unique $\beta(\mathscr{L}) \in \mathbb{Z}/12\mathbb{Z}$ with $\zeta^{3\beta} = \mathscr{L}(\sigma)$ and $\zeta^{2\beta} = \mathscr{L}(\tau)$. This gives
$$
\beta: \operatorname{Pic}(\mathscr{M}_{1,1}) \to \mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}.
$$

**Surjectivity.** The Hodge bundle $\Lambda$ assigns to each family $\pi: \mathscr{X} \to S$ the line bundle $R^{1}\pi_{*}\mathcal{O}_{\mathscr{X}}$. By cohomology and base change, this is a line bundle on $\mathscr{M}_{1,1}$. Computing the action on $H^{0}(C, \omega_{C}) = k \cdot dx/(2y)$ via Serre duality:

- $\sigma^{*}(dx/(2y)) = -dx/(2iy) = i \cdot dx/(2y)$, so $\Lambda(\sigma) = i$, a primitive $4$th root.
- $\tau^{*}(dx/(2y)) = \omega \, dx/(-2y) = -\omega \cdot dx/(2y)$, so $\Lambda(\tau) = -\omega$, a primitive $6$th root.

Hence $\beta(\Lambda) = 1$, proving surjectivity. The powers of $\Lambda$ give:

| $k$ | $\beta(\Lambda^{k})$ | $\Lambda^{k}(\sigma)$ | $\Lambda^{k}(\tau)$ | Descends to $M_{1,1}$? |
|---|---|---|---|---|
| $1$ | $1$ | $i$ | $-\omega$ | No |
| $2$ | $2$ | $-1$ | $\omega^{2}$ | No |
| $4$ | $4$ | $1$ | $\omega$ | No |
| $6$ | $6$ | $-1$ | $1$ | No |
| $12$ | $0$ | $1$ | $1$ | Yes |

The bundle $\Lambda^{k}$ descends to the coarse moduli space $M_{1,1} \cong \mathbb{A}^{1}_{j}$ if and only if $\beta(\Lambda^{k}) = 0$, i.e., $k \equiv 0 \pmod{12}$.

**Injectivity.** Suppose $\beta(\mathscr{L}) = 0$. The Legendre family gives an etale cover $S = \mathbb{A}^{1} \setminus \{0,1\} \to \mathscr{M}_{1,1}$ with $\operatorname{Pic}(S) = 0$, so $\mathscr{L}|_{S} \cong \mathcal{O}_{S}$. The group $S_{3} \cong \langle \lambda \mapsto 1/\lambda,\; \lambda \mapsto 1 - \lambda \rangle$ permutes branch points, giving degree $6$; combined with $\{\pm 1\}$ this yields a cover of degree $12$ as a map of stacks. The condition $\beta(\mathscr{L}) = 0$ ensures all automorphisms act trivially, so a trivialization of $\mathscr{L}|_{S}$ is automatically compatible with descent data. Hence $\mathscr{L} \cong \mathcal{O}_{\mathscr{M}_{1,1}}$, and $\beta$ is an isomorphism.

<!-- BENCHMARK_PROBLEM: Compute $\beta(\Lambda^{k})$ for $k = 1, \ldots, 12$ where $\Lambda$ is the Hodge bundle on $\mathscr{M}_{1,1}$. At which value of $k$ does $\Lambda^{k}$ descend to a line bundle on the coarse moduli space $M_{1,1} \cong \mathbb{A}^{1}_{j}$? -->

### Remark: Hodge bundle, $S\times_{\mathscr{M}_{1,1}}S$ and degree of the etale cover {#ecag-0338}

The Legendre family $E_{t}: y^{2} = x(x-1)(x-t)$ over $S = \mathbb{A}^{1} \setminus \{0, 1\}$ gives an etale cover $S \to \mathscr{M}_{1,1}$. The fiber product $S \times_{\mathscr{M}_{1,1}} S$ parametrizes pairs $(t_{1}, t_{2}) \in S \times S$ together with an isomorphism $E_{t_{1}} \cong E_{t_{2}}$.

Two Legendre curves $E_{t_{1}}$ and $E_{t_{2}}$ are isomorphic if and only if $t_{2}$ belongs to the orbit of $t_{1}$ under the group $S_{3} \cong \langle t \mapsto 1/t, \, t \mapsto 1-t \rangle$ acting on $\mathbb{P}^{1} \setminus \{0, 1, \infty\}$. This group has order $6$. However, some Legendre curves have extra automorphisms beyond $\{\pm 1\}$, so the degree of the cover $S \to \mathscr{M}_{1,1}$ is $|S_{3}| \times |\{\pm 1\}| = 6 \times 2 = 12$ when counted as a map of stacks.

The Hodge bundle $\Lambda$ restricted to $S$ is the line bundle $R^{1}\pi_{*}\mathcal{O}_{E}$ where $\pi: E \to S$ is the universal Legendre family. This is isomorphic to $\pi_{*}\omega_{E/S}^{\vee}$ by Serre duality. Since $\omega_{E/S} \cong \mathcal{O}_{S}$ for the Legendre family (every Legendre curve has a canonical differential $dx/(2y)$), the Hodge bundle restricted to $S$ is trivial. This is consistent with $\operatorname{Pic}(S) = 0$ since $S \cong \mathbb{A}^{1} \setminus \{0, 1\}$.
### Example: $\mathrm{Pic}(\mathscr{M}_{1,1})$ over a general scheme {#ecag-0339}

Over a general base scheme $S$ (not necessarily a field), $\operatorname{Pic}(\mathscr{M}_{1,1} \times S) \cong \mathbb{Z}/12\mathbb{Z} \oplus \operatorname{Pic}(S)$. In particular, over $\operatorname{Spec}(\mathbb{Z}[1/6])$, the Picard group is $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$, generated by the Hodge bundle $\lambda$. This is proved using a global quotient presentation, which reduces the problem to equivariant line bundles.

**The quotient stack presentation.** Over $\operatorname{Spec}(\mathbb{Z}[1/6])$, every elliptic curve admits a short Weierstrass form $y^{2} = x^{3} + ax + b$ with discriminant $\Delta = -16(4a^{3} + 27b^{2}) \neq 0$. The parameter space is $U = \operatorname{Spec}(\mathbb{Z}[1/6][a, b, \Delta^{-1}])$, and $\mathbb{G}_{m}$ acts by $t \cdot (a, b) = (t^{4}a, t^{6}b)$, corresponding to the substitution $x \mapsto t^{2}x$, $y \mapsto t^{3}y$ in the Weierstrass equation. This gives $\mathscr{M}_{1,1} \cong [U/\mathbb{G}_{m}]$.

**Weight computation.** The discriminant $\Delta = -16(4a^{3} + 27b^{2})$ has weight $\operatorname{wt}(\Delta) = \operatorname{wt}(a^{3}) = 3 \cdot 4 = 12$ (equivalently, $\operatorname{wt}(b^{2}) = 2 \cdot 6 = 12$). An equivariant line bundle on $U$ is determined by a character $n \in \mathbb{Z}$ of $\mathbb{G}_{m}$. Since $\operatorname{Pic}(U) = 0$ ($U$ is an open in affine space), $\operatorname{Pic}^{\mathbb{G}_{m}}(U) \cong \mathbb{Z}$. But $\Delta$ is an invertible function of weight $12$ on $U$, so characters $n$ and $n + 12$ give isomorphic equivariant line bundles. Therefore
$$
\operatorname{Pic}(\mathscr{M}_{1,1}) = \operatorname{Pic}([U/\mathbb{G}_{m}]) \cong \mathbb{Z}/12\mathbb{Z}.
$$

The Hodge bundle corresponds to weight $1$: the differential $dx/(2y)$ transforms as $t^{2}dx/(2t^{3}y) = t^{-1} \cdot dx/(2y)$, but by convention (using $\pi_{*}\omega$ rather than its dual) the Hodge bundle has weight $1$.

<!-- BENCHMARK_PROBLEM: In the presentation $\mathscr{M}_{1,1} \cong [U/\mathbb{G}_{m}]$ where $\mathbb{G}_{m}$ acts on the Weierstrass parameters by $t \cdot (a,b) = (t^{4}a, t^{6}b)$, compute the weight of the discriminant $\Delta = -16(4a^{3} + 27b^{2})$ under this $\mathbb{G}_{m}$-action. -->

### Example: Non-reductive group action on affine varieties {#ecag-0340}

If a non-reductive algebraic group $G$ acts on an affine variety $X = \operatorname{Spec}(A)$, the ring of invariants $A^{G}$ need not be finitely generated, so the GIT quotient $X /\!/ G = \operatorname{Spec}(A^{G})$ may fail to be of finite type. This is the negative answer to Hilbert's 14th problem, in stark contrast to the reductive case where the Hilbert--Nagata theorem guarantees finite generation.

**A concrete example.** Let $\mathbb{G}_{a}$ act on $\mathbb{A}^{3} = \operatorname{Spec}(k[x, y, z])$ by $t \cdot (x, y, z) = (x,\, y + tx,\, z + ty)$. The corresponding derivation is $D = x \partial_{y} + y \partial_{z}$. The invariant ring is computed by solving $Df = 0$:

- $Dx = 0$, so $x \in k[x,y,z]^{\mathbb{G}_{a}}$.
- $D(xz - y^{2}/2)$: we have $D(xz) = x \cdot y$ and $D(y^{2}) = 2y \cdot x$, so $D(xz - y^{2}/2) = xy - xy = 0$.

Setting $u = x$ and $v = 2xz - y^{2}$, one verifies $k[x,y,z]^{\mathbb{G}_{a}} = k[u, v]$, which is finitely generated (a polynomial ring in two variables). This low-dimensional example is deceptively well-behaved.

**Counterexamples to finite generation.** Nagata (1959) constructed a linear action of $\mathbb{G}_{a}^{13}$ on $\mathbb{A}^{32}$ with non-finitely-generated invariant ring. Roberts (1990) simplified this to $\mathbb{G}_{a}$ acting on $\mathbb{A}^{7}$ with non-finitely-generated invariants. Dufresne and Kraft further showed that even $\mathbb{G}_{a}$ acting on $\mathbb{A}^{6}$ by a triangular derivation can produce infinitely generated invariant rings.

The obstruction is fundamentally tied to the non-reductivity of $G$: for a reductive group, the Reynolds operator (averaging over the group) provides a projection $A \to A^{G}$ that splits the inclusion, which suffices for finite generation by Hilbert's basis theorem. No such operator exists for non-reductive groups. The "non-reductive GIT" developed by Berczi, Doran, Hawes, and Kirwan provides modified stability conditions and blow-up procedures to obtain well-behaved quotients in this setting.

<!-- BENCHMARK_PROBLEM: Let $\mathbb{G}_{a}$ act on $\mathbb{A}^{3} = \operatorname{Spec}(k[x,y,z])$ by $t \cdot (x,y,z) = (x, y + tx, z + ty)$. Compute the ring of invariants $k[x,y,z]^{\mathbb{G}_{a}}$ and determine whether it is finitely generated. -->

### Remark: A finite subset of a variety need not be contained in an open affine subvariety {#ecag-0341}

On a general algebraic variety $X$ (not quasi-projective), a finite set of closed points $\{p_{1}, \ldots, p_{n}\} \subset X$ need not be contained in any open affine subvariety $U \subset X$. This pathology occurs precisely when $X$ is not quasi-projective.

For a quasi-projective variety $X \hookrightarrow \mathbb{P}^{N}$, any finite set of points can be placed in a single affine open: choose a hyperplane $H \subset \mathbb{P}^{N}$ avoiding all $p_{i}$, then $U = X \setminus (X \cap H)$ is affine and contains all $p_{i}$.

Hironaka's example of a complete non-projective threefold provides a counterexample: there exist two points $P, Q$ in the threefold such that no affine open subset contains both. The obstruction is that the exceptional curves $L_{1}, L_{2}$ above $P$ and $M_{1}, M_{2}$ above $Q$ satisfy a homological relation $L_{1} + M_{1} \sim 0$ that is incompatible with the existence of an affine neighborhood of both points.

<!-- BENCHMARK_PROBLEM: Explain why on a quasi-projective variety, any finite set of points is contained in an affine open, and give an example of a complete variety where this fails. -->

### Example: Hironaka's example, a variety with no Hilbert scheme {#ecag-0342}

Hironaka constructed a smooth complete threefold $V$ over $\mathbb{C}$ that is not projective. As a consequence, the Hilbert functor of $V$ (parametrizing flat families of closed subschemes) is not representable by a scheme.

**The construction.** Start with $\mathbb{P}^{3}$ and two smooth curves $C = V(xy - z^{2}, w)$ and $D = V(xy - w^{2}, z)$ meeting transversally at two points $P = [1:0:0:0]$ and $Q = [0:1:0:0]$. The threefold $V$ is obtained by blowing up in a position-dependent order:

- Near $P$: blow up $C$ first, then the proper transform of $D$.
- Near $Q$: blow up $D$ first, then the proper transform of $C$.
- Away from $P$ and $Q$: the curves $C$ and $D$ are disjoint, so the two blow-up orders commute and the construction patches together.

The result is smooth and complete (proper over $\mathbb{C}$).

**Non-projectivity.** Let $L_{1}, L_{2}$ denote the two components of the exceptional fiber $\pi^{-1}(P)$ and $M_{1}, M_{2}$ those of $\pi^{-1}(Q)$. The key relation is
$$
L_{1} + M_{1} \sim 0 \quad \text{(numerical equivalence)},
$$

where both $L_{1}$ and $M_{1}$ are effective nonzero curves. If an ample divisor $H$ existed on $V$, we would have $H \cdot L_{1} > 0$ (since $L_{1}$ is an effective curve) and $H \cdot M_{1} > 0$ (likewise), giving $H \cdot (L_{1} + M_{1}) > 0$. But $L_{1} + M_{1} \sim 0$ forces $H \cdot (L_{1} + M_{1}) = 0$, a contradiction. Hence $V$ admits no ample divisor and is not projective.

**Failure of the Hilbert scheme.** Grothendieck's construction of $\operatorname{Hilb}(V)$ requires a projective embedding to bound Hilbert polynomials and apply the Grassmannian embedding. Without projectivity, this argument breaks down entirely. The Hilbert functor of $V$ is not representable by a scheme, though it may be representable as an algebraic space or algebraic stack under weaker hypotheses.

<!-- BENCHMARK_PROBLEM: In Hironaka's construction, let $L_{1}, L_{2}$ be the two components of the exceptional fiber over $P$, and $M_{1}, M_{2}$ those over $Q$. Explain why the relation $L_{1} + M_{1} \sim 0$ with $L_{1}, M_{1}$ effective contradicts the existence of an ample divisor on $V$. -->
### Example: Stacks project Tag O8KE, Descent data for schemes need not be effective, even for a projective morphism {#ecag-0343}

There exists a descent datum $(V/X, \phi)$ relative to an etale cover $X \to S$ with $V \to X$ projective, such that the descent datum is not effective in the category of schemes. This example, based on Hironaka's construction, demonstrates that even projectivity of the morphism $V \to X$ is insufficient to guarantee effectivity of descent.

**Setup.** Work over $k = \mathbb{C}$. Let $G = \mathbb{Z}/2\mathbb{Z} = \{1, g\}$ act on $\mathbb{P}^{3} = \operatorname{Proj}(k[x,y,z,w])$ by $g \cdot [x,y,z,w] = [y,x,w,z]$. The two curves from Hironaka's construction, $C = V(xy - z^{2}, w)$ and $D = V(xy - w^{2}, z)$, are swapped by $g$: since $g$ interchanges $(x,y)$ and $(z,w)$, we have $g \cdot C = D$ and $g \cdot P = Q$ where $P = [1,0,0,0]$ and $Q = [0,1,0,0]$.

The fixed locus of $g$ consists of points $[x,y,z,w]$ with $[y,x,w,z] = [x,y,z,w]$, i.e., $x = y$ and $z = w$ (up to scaling), which gives the two lines $l_{1} = \{[x,x,z,z]\}$ and $l_{2} = \{[x,-x,z,-z]\}$. Setting $Y = \mathbb{P}^{3} \setminus (l_{1} \cup l_{2})$, the action of $G$ on $Y$ is free.

**The invariant ring.** The ring of invariants $k[x,y,z,w]^{G}$ is generated by the symmetric functions $u_{0} = x+y$, $u_{1} = z+w$ and the "anti-symmetric squares" $v_{0} = (x-y)^{2}$, $v_{1} = (z-w)^{2}$, $v_{2} = (x-y)(z-w)$. These satisfy the relation $v_{0}v_{1} = v_{2}^{2}$ (a quadric cone), and the quotient is
$$
S = Y/G \hookrightarrow \operatorname{Proj}(k[u_{0}, u_{1}, v_{0}, v_{1}, v_{2}]/(v_{0}v_{1} - v_{2}^{2})).
$$

**Constructing the descent datum.** Apply Hironaka's blow-up construction to $Y$ to obtain $\pi: V_{Y} \to Y$. The $G$-action on $Y$ lifts to $V_{Y}$ (since $g$ swaps $C$ and $D$, it swaps the blow-up orders at $P$ and $Q$, which is exactly how $V_{Y}$ is constructed). This gives a descent datum $(V_{Y}/Y, \phi)$ relative to the $G$-torsor $Y \to S$. The morphism $V_{Y} \to Y$ is projective (locally given by blow-ups of smooth subvarieties).

**Proof of non-effectivity.** Suppose the descent datum is effective, producing a scheme $U$ with $V_{Y} \to U$ the quotient by $G$. The exceptional fibers are
$$
\pi^{-1}(P) = L_{1} \cup L_{2}, \quad \pi^{-1}(Q) = M_{1} \cup M_{2},
$$

with $g(L_{i}) = M_{i}$ and $L_{1} + M_{1} \sim 0$ (numerically). By descent, the $G$-orbit $L_{1} \cup M_{1}$ descends to a curve $L \cong \mathbb{P}^{1}$ in $U$. Choose a closed point $R \in L$ and $f \in \mathcal{O}_{U,R}$ with $f(R) = 0$ but $L \not\subset V(f)$. An irreducible codimension-$1$ component $W$ of $V(f)$ through $R$ pulls back to an effective divisor $D'$ on $V_{Y}$ meeting $L_{1} \cup M_{1}$ but containing neither. Then $D' \cdot (L_{1} + M_{1}) > 0$, contradicting $L_{1} + M_{1} \sim 0$. Hence no such scheme $U$ exists.

The descended object does exist as an algebraic space, just not as a scheme. The failure is specifically that the local ring $\mathcal{O}_{U,R}$ of a scheme provides enough functions to separate curves from divisors, leading to the intersection-theoretic contradiction.

<!-- BENCHMARK_PROBLEM: In the setup above, verify that $g \cdot P = Q$, $g \cdot C = D$, and that the fixed locus of the $G$-action on $\mathbb{P}^{3}$ is exactly $l_{1} \cup l_{2}$. Compute the invariant ring $k[x,y,z,w]^{G}$ and verify the relation $v_{0}v_{1} = v_{2}^{2}$. -->

### Remark: Descent datum {#ecag-0344}

Basic descent theory involves several key components:

- **Descent for affine morphisms:** If $f: X \to Y$ is an affine morphism, descent data for quasi-coherent sheaves relative to an fpqc cover $Y' \to Y$ are always effective. This is because quasi-coherent sheaves on affine schemes correspond to modules, and module descent is always effective.

- **Relative descent datum and group actions:** For a $G$-torsor $Y \to S$, a descent datum on $V \to Y$ consists of an isomorphism $\phi: g^{*}V \xrightarrow{\sim} V$ satisfying the cocycle condition $\phi_{gh} = \phi_{h} \circ h^{*}\phi_{g}$. This is equivalent to lifting the $G$-action on $Y$ to a $G$-action on $V$ compatible with the structural morphism.

- **Descent datum and quotients:** When the descent datum is effective, the descended object $U$ is the categorical quotient $V/G$, and the morphism $V \to U$ is a $G$-torsor. The Keel-Mori theorem guarantees effectivity for separated Deligne-Mumford stacks with finite inertia, but the example above shows that effectivity can fail for non-separated situations or when working in the category of schemes rather than algebraic spaces.

### Remark: Where do we use the condition that $U$ is a scheme? {#ecag-0345}

In the proof of non-effectivity of the descent datum in the Hironaka example, the key step uses the scheme structure of $U$ in the following way: at a closed point $R$ of $L \cong \mathbb{P}^{1} \subset U$, we need to find $f \in \mathcal{O}_{U,R}$ with $f(R) = 0$ but $L \not\subset V(f)$. This requires that $R$ is not the generic point of $L$, which holds because $R$ is a closed point (a complex point).

More fundamentally, the argument relies on the local ring $\mathcal{O}_{U,R}$ being a local ring of a Noetherian scheme, ensuring that principal divisors near $R$ behave as expected (codimension $1$ subvarieties through $R$ exist that do not contain $L$). If $U$ were merely an algebraic space rather than a scheme, the local ring might not have the same properties, and in fact the descended object does exist as an algebraic space (just not as a scheme).

### Remark: Hironaka's example, the quotient of a scheme by a free action of a finite group need not be a scheme {#ecag-0346}

The descent datum analysis of the preceding sections shows that the quotient of Hironaka's threefold $V_Y$ by the free action of $G = \mathbb{Z}/2\mathbb{Z}$ does not exist as a scheme, despite the action being free and the group finite. To appreciate how unusual this is, recall the contrasting situations where quotients do exist:

1. If $X$ is quasi-projective and $G$ is a finite group acting freely, the quotient $X/G$ exists as a scheme. This follows from geometric invariant theory or, more elementarily, by gluing affine invariant-ring quotients. The key input is that quasi-projective varieties admit ample line bundles, which can be averaged over $G$ to produce a $G$-linearized ample bundle.

2. If $X$ is a separated algebraic space and $G$ is finite acting freely, then $X/G$ exists as an algebraic space. This is a theorem of Deligne (SGA 1, Expose V) that requires no projectivity hypothesis but only works in the larger category of algebraic spaces.

Hironaka's threefold $V_Y$ is proper but not projective, so situation (1) does not apply. The descent datum for the projection $V_Y \to V_Y/G$ is not effective in the category of schemes because the two curves $\ell_1, m_1$ and $\ell_2, m_2$ in the exceptional locus are identified by $G$ in a way that cannot be realized by a scheme morphism -- the local patching would require simultaneously contracting curves that intersect differently on the two sheets.

The quotient $V_Y/G$ does exist as a proper algebraic space over $S$. It is an algebraic space that is not a scheme, providing one of the original motivations for Artin's introduction of algebraic spaces as a necessary enlargement of the category of schemes in moduli theory.

<!-- BENCHMARK_PROBLEM: Let $G = \mathbb{Z}/2\mathbb{Z}$ act freely on a proper threefold $X$ over $\mathbb{C}$. State conditions under which $X/G$ exists as a scheme, and give an example (Hironaka's threefold) where the quotient exists as an algebraic space but not as a scheme. What property of $X$ fails that would guarantee a scheme quotient? -->
### Example: Hironaka's example, a scheme of finite type over a field such that not every line bundle comes from a divisor {#ecag-0347}

On Hironaka's complete non-projective smooth threefold $V$ over $\mathbb{C}$, the natural map $\operatorname{CaCl}(V) \to \operatorname{Pic}(V)$ from Cartier divisor classes to isomorphism classes of line bundles is not surjective. That is, there exist line bundles on $V$ that are not of the form $\mathcal{O}(D)$ for any Cartier divisor $D$.

**Why the naive argument fails.** On any smooth variety, every Weil divisor is Cartier, so the map $\operatorname{CaCl}(V) \to \operatorname{Pic}(V)$ is the same as $\operatorname{Cl}(V) \to \operatorname{Pic}(V)$. On a smooth variety this map is an isomorphism provided every line bundle admits a nonzero rational section (equivalently, a nonzero meromorphic section in the analytic category). On a smooth projective variety $X$, this is guaranteed: if $\mathcal{L}$ is any line bundle and $\mathcal{A}$ is ample, then for $n \gg 0$ the bundle $\mathcal{L} \otimes \mathcal{A}^{\otimes n}$ is generated by global sections. Any nonzero global section of $\mathcal{L} \otimes \mathcal{A}^{\otimes n}$ tensored with a rational section of $\mathcal{A}^{\otimes(-n)}$ gives a rational section of $\mathcal{L}$. On a merely complete variety, no ample bundle exists, and this argument collapses.

**The obstruction on Hironaka's threefold.** Consider the exceptional locus $E = \pi^{-1}(C \cup D)$ of the blow-up constructing $V$, with its irreducible components including the curves $L_1, M_1$. The numerical relation $L_1 + M_1 \sim 0$ on $E$ means $\mathcal{O}_E(L_1 + M_1)$ is trivial. The restriction map $\operatorname{Pic}(V) \to \operatorname{Pic}(E)$ sends any line bundle on $V$ to its restriction on $E$. There exist line bundles $\mathcal{L}$ on $V$ whose restriction to $E$ has strictly positive degree on both $L_1$ and $M_1$; such a bundle cannot be $\mathcal{O}(D)$ for any effective divisor $D$ meeting $E$ properly, since $D \cdot L_1$ and $D \cdot M_1$ would need to be non-negative while $D \cdot (L_1 + M_1) = 0$.

More concretely, the variety $V$ admits nontrivial line bundles $\mathcal{L}$ with $H^0(V, \mathcal{L}) = 0$ and, crucially, with no nonzero rational section at all. This last point distinguishes $V$ from projective varieties: the function field $k(V)$ does not "see" all line bundles. The Picard group $\operatorname{Pic}(V)$ is strictly larger than $\operatorname{CaCl}(V)$.

<!-- BENCHMARK_PROBLEM: On a smooth projective variety $X$, explain why every line bundle $\mathcal{L}$ admits a nonzero rational section, and hence $\operatorname{Pic}(X) \cong \operatorname{CaCl}(X)$. What specific property of projective varieties is used that fails for merely complete varieties? -->

### Remark {#ecag-0348}

The pathologies demonstrated by Hironaka's example -- non-effective descent data, non-representable Hilbert functors, line bundles not arising from divisors -- are all consequences of the absence of projectivity. In practice, standard hypotheses eliminate these phenomena entirely.

The most common assumption is **projectivity** (or quasi-projectivity). For a projective morphism $f\colon X \to S$, descent data are always effective (Grothendieck, EGA IV). The Hilbert functor $\operatorname{Hilb}_{X/S}$ is representable by a scheme when $X \to S$ is projective (Grothendieck). And on a smooth projective variety, every line bundle admits a rational section, so $\operatorname{Pic}(X) \cong \operatorname{CaCl}(X)$.

A weaker but still sufficient assumption in characteristic $0$ is that $X$ is **reduced and proper**. By Chow's lemma, such an $X$ admits a birational projective model $\widetilde{X} \to X$, and many of the functorial properties (representability of moduli, effectivity of descent) can be transferred from $\widetilde{X}$ to $X$ via this map. In positive characteristic, additional care is needed because inseparable morphisms can introduce further pathologies.

The following references contain detailed treatments:

- [Stacks project, Tag 08KE](http://stacks.math.columbia.edu/tag/08KE): Descent data need not be effective.
- [Stacks project, Tag 08KF](http://stacks.math.columbia.edu/tag/08KF): Effectivity under projectivity hypotheses.
- Nitsure, [Construction of Hilbert and Quot schemes](https://perso.univ-rennes1.fr/matthieu.romagny/GT_Hilb/Nitsure_Construction_of_Hilbert_and_Quot_schemes.pdf).
- Vistoli, [Notes on Grothendieck topologies, fibered categories and descent theory](https://arxiv.org/pdf/math/0412512.pdf).
- Mumford, *Geometric Invariant Theory*.

<!-- BENCHMARK_PROBLEM: State the hypotheses under which the Hilbert functor $\operatorname{Hilb}_{X/S}$ is representable by a scheme and descent data for quasi-coherent sheaves are effective. Which of these hypotheses fail for Hironaka's complete non-projective threefold? -->

## Hodge theory

### Remark: singular (co)homology, sheaf (co)homology, de Rham cohomology and Hodge decomposition {#ecag-0349}

Let $X$ be a smooth projective variety over $\mathbb{C}$. Several cohomology theories apply to $X$, and the relationships between them form the backbone of Hodge theory.

**Singular and sheaf cohomology.** The singular cohomology groups $H^n(X^{\mathrm{an}}, \mathbb{Z})$, computed from the underlying topological space of the analytification, coincide with the sheaf cohomology groups $H^n(X^{\mathrm{an}}, \underline{\mathbb{Z}})$ of the constant sheaf $\underline{\mathbb{Z}}$ on the analytic site. This is the comparison theorem for locally contractible spaces, and it holds equally with $\mathbb{R}$ or $\mathbb{C}$ coefficients.

**Holomorphic vs. smooth forms.** The algebraic de Rham complex $\Omega_{X/\mathbb{C}}^{\bullet}$ involves only holomorphic (algebraic) differential forms. Antiholomorphic forms such as $d\bar{z}$ are $C^{\infty}$ but not holomorphic; they appear in the smooth de Rham complex $\mathcal{A}_X^{\bullet}$ and in the Dolbeault resolution $\mathcal{A}_X^{p,q}$, which resolves the sheaf $\Omega_X^p$ of holomorphic $p$-forms. The Hodge decomposition necessarily involves both holomorphic and antiholomorphic contributions.

**The Hodge decomposition.** When $X$ is smooth projective (or more generally compact Kahler), the Hodge theorem gives a canonical decomposition
$$
H^n(X^{\mathrm{an}}, \mathbb{C}) \cong \bigoplus_{p+q=n} H^{p,q}(X),
$$

where $H^{p,q}(X)$ consists of cohomology classes representable by harmonic $(p,q)$-forms. The Dolbeault theorem identifies $H^{p,q}(X) \cong H^q(X, \Omega_X^p)$. Complex conjugation interchanges the summands: $\overline{H^{p,q}(X)} = H^{q,p}(X)$, a statement about the real structure $H^n(X, \mathbb{C}) = H^n(X, \mathbb{R}) \otimes_{\mathbb{R}} \mathbb{C}$.

**Algebraic de Rham cohomology.** The algebraic de Rham cohomology $H^n_{\mathrm{dR}}(X/\mathbb{C}) = \mathbb{H}^n(\Omega_{X/\mathbb{C}}^{\bullet})$ is the hypercohomology of the algebraic de Rham complex. By GAGA (which identifies algebraic and analytic coherent cohomology on proper varieties) and the holomorphic Poincare lemma (which shows the analytic de Rham complex resolves $\underline{\mathbb{C}}$), one obtains the comparison isomorphism
$$
H^n_{\mathrm{dR}}(X/\mathbb{C}) \cong H^n(X^{\mathrm{an}}, \mathbb{C}).
$$

**The Betti lattice.** The integral lattice $H^n(X^{\mathrm{an}}, \mathbb{Z}) \hookrightarrow H^n(X^{\mathrm{an}}, \mathbb{C}) \cong H^n_{\mathrm{dR}}(X/\mathbb{C})$ is a transcendental datum that cannot be recovered from the algebraic de Rham cohomology alone. The entries of the period matrix -- integrals $\int_\gamma \omega$ of algebraic differential forms over topological cycles -- encode this lattice, and the period map records how it varies in families.

<!-- BENCHMARK_PROBLEM: For a smooth projective curve $X$ of genus $g$ over $\mathbb{C}$, compute all the Hodge numbers $h^{p,q}$ and verify the Hodge decomposition $H^{1}(X^{an}, \mathbb{C}) \cong H^{1,0}(X) \oplus H^{0,1}(X)$ with dimensions. -->
### Example: William Lang, Hodge spectral sequence in characteristic $3$ {#ecag-0350}

Over $k = \mathbb{F}_3$, the surface
$$
X\colon y^2 z = x^3 - t z^2 \subset \mathbb{P}^3_k
$$

provides an explicit example where the Hodge-to-de Rham spectral sequence fails to degenerate at $E_1$. The Hodge numbers are $h^{1,0} = h^{0,1} = 1$, so if degeneration held we would have $b_{\mathrm{dR}}^1 = h^{1,0} + h^{0,1} = 2$. In fact $b_{\mathrm{dR}}^1 = \dim_k H^1_{\mathrm{dR}}(X/k) = 3$.

**The quasi-elliptic fibration.** The projection to the coordinate $t$ realizes $X$ as a fibration $\pi\colon X \to \mathbb{P}^1$ whose generic fiber is the curve $y^2 = x^3 - t$ over $k(t)$. In characteristic $3$, the identity $d(x^3) = 3x^2\,dx = 0$ makes the map $x \mapsto x^3$ purely inseparable, so the generic fiber is a cuspidal rational curve rather than a smooth elliptic curve. Such a fibration is called quasi-elliptic.

**Hodge numbers.** The individual Hodge numbers are computed from sheaf cohomology:
$$
h^{1,0} = \dim_k H^0(X, \Omega_{X/k}^1) = 1, \qquad h^{0,1} = \dim_k H^1(X, \mathcal{O}_X) = 1.
$$

**The spectral sequence.** The algebraic de Rham cohomology $H^1_{\mathrm{dR}}(X/k) = \mathbb{H}^1(\Omega_{X/k}^{\bullet})$ is computed via the Hodge-to-de Rham spectral sequence
$$
E_1^{p,q} = H^q(X, \Omega_{X/k}^p) \implies H^{p+q}_{\mathrm{dR}}(X/k).
$$

The $E_1$ terms contributing to $H^1_{\mathrm{dR}}$ are $E_1^{0,1} = H^1(X, \mathcal{O}_X)$ of dimension $1$ and $E_1^{1,0} = H^0(X, \Omega_X^1)$ of dimension $1$. If the spectral sequence degenerated at $E_1$, the total dimension would be $2$. Since $b_{\mathrm{dR}}^1 = 3 > 2$, a nonzero differential at the $E_1$ page must be responsible: the map $d_1\colon E_1^{0,0} = H^0(X, \mathcal{O}_X) \to E_1^{1,0}$ interacts nontrivially with the $E_2$-page terms to produce the extra dimension.

**Why degeneration fails.** In characteristic $0$, the Hodge-to-de Rham spectral sequence always degenerates at $E_1$ for smooth proper varieties, either by the Hodge theorem (analytically) or by the Deligne-Illusie theorem (algebraically, for varieties lifting to $W_2(k)$). In positive characteristic, the Cartier operator can create cohomology classes invisible to the Hodge filtration. Lang's surface does not lift to $W_2(\mathbb{F}_3)$, so Deligne-Illusie does not apply, even though $\dim X = 2 < 3 = \operatorname{char}(k)$.

<!-- BENCHMARK_PROBLEM: Let $X: y^{2}z = x^{3} - tz^{2}$ over $\mathbb{F}_{3}$. Verify that $h^{1,0} + h^{0,1} = 2$ while $b_{dR}^{1} = 3$, and explain which differential in the Hodge-to-de Rham spectral sequence must be nonzero. -->

### Remark {#ecag-0351}

This example is due to William Lang in his thesis *Quasi-elliptic surfaces in characteristic three*. A detailed exposition appears in Alex Youcis's blog post [Algebraic de Rham cohomology and the degeneration of the Hodge spectral sequence](https://ayoucis.wordpress.com/2015/07/22/algebraic-de-rham-cohomology-and-the-degeneration-of-the-hodge-spectral-sequencethe/#more-3561).

The relevant theorem of Deligne-Illusie states: if $X$ is smooth proper over a perfect field $k$ of characteristic $p > 0$, $\dim X < p$, and $X$ lifts to $W_2(k)$ (the ring of length-$2$ Witt vectors), then the Hodge-to-de Rham spectral sequence degenerates at $E_1$. Lang's example satisfies $\dim X = 2 < 3 = p$, so the dimension hypothesis holds. The failure of degeneration therefore implies that $X$ does not lift to $W_2(\mathbb{F}_3)$. This obstruction to lifting is itself an interesting phenomenon, tied to the purely inseparable geometry of the quasi-elliptic fibration.

<!-- BENCHMARK_PROBLEM: State the Deligne-Illusie theorem on the degeneration of the Hodge-to-de Rham spectral sequence. For a smooth proper surface over $\mathbb{F}_3$, which hypothesis of the theorem can fail, and give an example where it does fail. -->

### Remark: $X$ irreducible, then $H_{\mathrm{dR}}^{i}(X/k)=0, \forall i>0$? (This cannot be true) {#ecag-0352}

The following erroneous argument illustrates a common confusion about algebraic de Rham cohomology. Recall that de Rham cohomology is defined as
$$
H^i_{\mathrm{dR}}(X/k) := \mathbb{H}^i(\Omega_{X/k}^{\bullet}).
$$

Suppose the de Rham complex $0 \to \mathcal{O}_X \to \Omega_{X/k}^1 \to \cdots \to \Omega_{X/k}^n \to 0$ were a resolution of the constant sheaf $\underline{k}$ in the Zariski topology. Then $\mathbb{H}^i(\Omega_{X/k}^{\bullet}) \cong H^i(X, \underline{k})$. But for irreducible $X$, the constant sheaf $\underline{k}$ is flasque on the Zariski site (every nonempty open in an irreducible space is dense and connected), so $H^i(X, \underline{k}) = 0$ for $i > 0$. This would force $H^i_{\mathrm{dR}}(X/k) = 0$ for all $i > 0$ -- which is absurd, since for instance a smooth projective curve of genus $g \geq 1$ has $H^1_{\mathrm{dR}} \neq 0$.

The error lies in the premise: **the algebraic de Rham complex is not exact in the Zariski topology**. The Poincare lemma -- the statement that closed forms are locally exact -- holds in the $C^{\infty}$ or analytic setting (where "local" means on a small contractible ball), but fails in the Zariski setting where open sets are far too large. For instance, on $\mathbb{A}^1 = \operatorname{Spec}(k[t])$, the $1$-form $dt/t$ is closed on $\mathbb{G}_m$ but not exact: there is no algebraic logarithm. The Zariski open set $\mathbb{G}_m \subset \mathbb{A}^1$ is not contractible in any relevant sense.

The correct statement is therefore:
$$
H^i(X, \underline{k}) \neq \mathbb{H}^i(\Omega_{X/k}^{\bullet}) \quad \text{in general}.
$$

The left side is Zariski sheaf cohomology of the constant sheaf (trivial for irreducible $X$), while the right side is algebraic de Rham cohomology, which over $\mathbb{C}$ recovers the singular cohomology $H^i(X^{\mathrm{an}}, \mathbb{C})$ via the comparison theorem.

<!-- BENCHMARK_PROBLEM: Explain why the constant sheaf $\underline{k}$ is flasque on an irreducible topological space $X$ with the Zariski topology, and why this does NOT imply $H^i_{\mathrm{dR}}(X/k) = 0$ for $i > 0$. Identify the specific step in the naive argument that fails. -->

### Example: Kahler manifold but not algebraic {#ecag-0353}

A generic complex torus of dimension $g \geq 2$ is a compact Kahler manifold that is not algebraic, providing a clean example of the gap between the Kahler and projective categories.

**Every complex torus is Kahler.** A complex torus of dimension $g$ is a quotient $T = \mathbb{C}^g / \Lambda$ where $\Lambda \cong \mathbb{Z}^{2g}$ is a lattice. The standard flat Hermitian metric on $\mathbb{C}^g$ descends to $T$, giving a Kahler metric with constant Kahler form. Thus every complex torus is Kahler.

**The Kodaira criterion.** By the Kodaira embedding theorem, a compact Kahler manifold $M$ is projective algebraic if and only if it admits a Hodge class: a Kahler class lying in $H^{1,1}(M) \cap H^2(M, \mathbb{Z})$. For $T = \mathbb{C}^g/\Lambda$, this translates to the existence of a Riemann form on $\Lambda$, i.e., an alternating $\mathbb{Z}$-bilinear form $E\colon \Lambda \times \Lambda \to \mathbb{Z}$ satisfying $E(iv, iw) = E(v,w)$ and $E(iv, v) > 0$ for $v \neq 0$. A complex torus admitting such a form is an abelian variety.

**Dimension $1$ vs. dimension $\geq 2$.** For $g = 1$, every lattice $\Lambda \subset \mathbb{C}$ of rank $2$ admits a Riemann form (any alternating form on $\mathbb{Z}^2$ is a scalar multiple of the standard one, and the positivity condition can always be arranged by choosing sign). Thus every $1$-dimensional complex torus is an elliptic curve.

For $g \geq 2$, the situation changes dramatically. A $g$-dimensional complex torus (up to isomorphism) is parametrized by the quotient $\operatorname{GL}_g(\mathbb{C}) \backslash \operatorname{Mat}_{g \times 2g}(\mathbb{C}) / \operatorname{GL}_{2g}(\mathbb{Z})$, which has dimension $g^2$ over $\mathbb{R}$ (after accounting for redundancies). By contrast, the principally polarized abelian varieties form the Siegel modular variety $\mathscr{A}_g = \operatorname{Sp}_{2g}(\mathbb{Z}) \backslash \mathfrak{H}_g$ of dimension $g(g+1)/2$. For $g = 2$: the space of complex tori has real dimension $8$ (the period matrix $\Omega = (I_2 \mid Z)$ with $Z \in \operatorname{Mat}_{2 \times 2}(\mathbb{C})$), while the Siegel upper half space $\mathfrak{H}_2$ has real dimension $6$ (complex dimension $3$). So the abelian varieties form a proper subset.

**Non-algebraic tori.** A non-algebraic complex torus $T$ may have $\operatorname{NS}(T) = 0$, meaning there are no holomorphic line bundles with nonzero first Chern class. Such a torus has $\operatorname{Pic}^0(T) \neq 0$ (topologically nontrivial flat line bundles exist, from $H^1(T, \mathcal{O}^*_T)$), but no ample line bundle and hence no projective embedding.

<!-- BENCHMARK_PROBLEM: For $g = 2$, what is the dimension of the space of all complex tori $\mathbb{C}^{2}/\Lambda$ (up to isomorphism), and what is the dimension of the moduli of principally polarized abelian surfaces $\mathfrak{H}_{2}/\operatorname{Sp}_{4}(\mathbb{Z})$? Use this to explain why a "generic" $2$-dimensional complex torus is not algebraic. -->

### Example: $\mathrm{rank}(H^{2k}(X_{t}, \mathbb{Z})\cap H^{k,k}(X_{t}))$ not constant {#ecag-0354}

In a family of smooth projective varieties $\{X_t\}_{t \in B}$, the rank of the group of integral Hodge classes $\operatorname{rk}(H^{2k}(X_t, \mathbb{Z}) \cap H^{k,k}(X_t))$ can jump as $t$ varies. The Hodge filtration $F^{\bullet}$ varies holomorphically in families, but the integral lattice $H^{2k}(X_t, \mathbb{Z})$ is locally constant (it is carried by the flat connection). Their intersection can therefore change, and the rank is lower semicontinuous: it can only jump up at special points.

**Quartic K3 surfaces.** Consider the universal family of smooth quartic surfaces in $\mathbb{P}^3$. Each fiber $X_t$ is a K3 surface with Hodge numbers $h^{2,0} = h^{0,2} = 1$ and $h^{1,1} = 20$ (computed from $\chi(\mathcal{O}_X) = 2$ and $b_2 = 22$). The Picard number is $\rho(X_t) = \operatorname{rk}(H^2(X_t, \mathbb{Z}) \cap H^{1,1}(X_t))$, which satisfies $1 \leq \rho(X_t) \leq 20$.

For a very general quartic $X_t$, the Picard number is $\rho = 1$, generated by the hyperplane class $h$. At special values of $t$, the Picard number jumps. The most extreme case is the Fermat quartic $x_0^4 + x_1^4 + x_2^4 + x_3^4 = 0$, which has $\rho = 20$, the maximum allowed by $h^{1,1}$.

**The Noether-Lefschetz theorem.** The locus
$$
\mathrm{NL} = \{t \in B : \rho(X_t) > 1\}
$$

is a countable dense union of divisors in the parameter space $B$. Each Noether-Lefschetz divisor corresponds to a specific integral class in $H^2(X_t, \mathbb{Z})$ becoming of type $(1,1)$. The countability follows from the countability of the lattice $H^2(X_t, \mathbb{Z})$, while the density is a consequence of the fact that the period domain for K3 surfaces is a type IV Hermitian symmetric domain and the Hodge locus is dense in it.

**Higher codimension.** For $k > 1$, the same phenomenon occurs with integral Hodge classes in $H^{2k}(X_t, \mathbb{Z}) \cap H^{k,k}(X_t)$. The jumping of these ranks is closely related to the Hodge conjecture and to Griffiths' and Cattani-Deligne-Kaplan's results on the algebraicity of Hodge loci.

<!-- BENCHMARK_PROBLEM: For a smooth quartic surface $X \subset \mathbb{P}^{3}$ (a K3 surface), compute $h^{1,1}(X)$ and explain why $\rho(X) \leq 20$. Give an example of a quartic K3 with $\rho = 1$ and one with $\rho = 20$. -->
### Example: Family of elliptic curves, Gauss-Manin connection and Picard-Fuchs equation {#ecag-0355}

The Legendre family of elliptic curves $E_t\colon y^2 = x(x-1)(x-t)$ over $S = \mathbb{P}^1 \setminus \{0, 1, \infty\}$ provides the most classical example of the Gauss-Manin connection and its associated Picard-Fuchs equation. The periods of the family satisfy
$$
t(1-t)\, f''(t) + (1 - 2t)\, f'(t) - \tfrac{1}{4}\, f(t) = 0.
$$

**The Gauss-Manin connection.** The family $\pi\colon \mathscr{E} \to S$ produces a rank-$2$ local system $\mathcal{H} = R^1\pi_*\mathbb{C}$ on $S$. The associated flat vector bundle $\mathcal{H} \otimes_{\mathbb{C}} \mathcal{O}_S$ carries the Gauss-Manin connection $\nabla$, which differentiates cohomology classes along the parameter $t$.

**Deriving the Picard-Fuchs equation.** The holomorphic period is the multivalued function
$$
\omega(t) = \int_{\gamma} \frac{dx}{\sqrt{x(x-1)(x-t)}},
$$

where $\gamma \in H_1(E_t, \mathbb{Z})$. Differentiating under the integral sign:
$$
\omega'(t) = \frac{1}{2} \int_{\gamma} \frac{dx}{(x-t)\sqrt{x(x-1)(x-t)}}.
$$

By the Griffiths-Dwork reduction, the integrand $\frac{dx}{(x-t)y}$ can be expressed as a $k(t)$-linear combination of $\frac{dx}{y}$ and $\frac{x\,dx}{y}$ plus an exact form. Iterating this reduction for $\omega''(t)$ and eliminating the second basis element yields the Picard-Fuchs ODE above.

**Solutions and monodromy.** The Picard-Fuchs equation is Fuchsian with regular singular points at $t = 0, 1, \infty$. Two linearly independent solutions near $t = 0$ are the complete elliptic integrals $K(t)$ and $K(1-t)$, equivalently the Gauss hypergeometric function
$$
f(t) = {}_2F_1\bigl(\tfrac{1}{2}, \tfrac{1}{2}; 1; t\bigr) = 1 + \frac{1}{4}t + \frac{9}{64}t^2 + \cdots
$$

and its companion obtained by the connection formula. The monodromy representation $\pi_1(S) \to \operatorname{GL}_2(\mathbb{C})$ coincides with the monodromy of the local system $R^1\pi_*\mathbb{C}$. The monodromy matrices around $t = 0$ and $t = 1$ are both conjugate to $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ (unipotent of index $2$), reflecting the Dehn twist around the vanishing cycle as the elliptic curve acquires a node.

The Gauss-Manin connection thus encodes how the Hodge structure varies in the family, and the Picard-Fuchs equation is its differential-algebraic manifestation, linking algebraic geometry to the classical theory of special functions.

<!-- BENCHMARK_PROBLEM: Verify that $f(t) = {}_{2}F_{1}(1/2, 1/2; 1; t)$ satisfies the Picard-Fuchs equation $t(1-t)f'' + (1-2t)f' - \frac{1}{4}f = 0$. Compute the first three terms of the power series expansion of $f(t)$ around $t = 0$. -->

### Example: Polarized variation of Hodge structure over the punctured disk {#ecag-0356}

A polarized variation of Hodge structure (PVHS) over the punctured disk $\Delta^* = \{t \in \mathbb{C} : 0 < |t| < 1\}$ consists of a flat vector bundle $(\mathcal{H}, \nabla)$ equipped with a holomorphically varying Hodge filtration $F^{\bullet}$ and a flat bilinear form $Q$ satisfying the Hodge-Riemann bilinear relations fiberwise. The Schmid nilpotent orbit theorem describes the asymptotic behavior of the Hodge filtration as $t \to 0$ and produces a limiting mixed Hodge structure.

**Setup.** Let $\pi\colon \mathscr{X} \to \Delta$ be a proper morphism with smooth fibers $\mathscr{X}_t$ for $t \neq 0$ and a semistable (normal crossing) central fiber $\mathscr{X}_0$. The cohomology groups $H^n(\mathscr{X}_t, \mathbb{Q})$ assemble into a local system over $\Delta^*$ with monodromy operator $T$ (the action of the generator of $\pi_1(\Delta^*) \cong \mathbb{Z}$).

**The monodromy theorem.** The monodromy $T$ is quasi-unipotent: $(T^m - I)^{n+1} = 0$ for some $m \geq 1$, where $n$ is the weight. After the base change $t \mapsto t^m$ we may assume $T$ is unipotent, and write $T = e^N$ where $N = \log T = (T - I) - \frac{1}{2}(T-I)^2 + \cdots$ is nilpotent.

**Schmid's nilpotent orbit theorem.** The Hodge filtration $F_t^{\bullet}$ on $H^n(\mathscr{X}_t, \mathbb{C})$ satisfies
$$
F_t^{\bullet} \sim e^{\frac{\log t}{2\pi i} N} \cdot F_{\infty}^{\bullet}
$$

as $t \to 0$, where $F_{\infty}^{\bullet}$ is the limiting Hodge filtration. The pair $(W_{\bullet}, F_{\infty}^{\bullet})$ -- where $W_{\bullet}$ is the unique monodromy weight filtration associated to $N$ centered at weight $n$ -- defines a mixed Hodge structure on $H^n(\mathscr{X}_t, \mathbb{Q})$ (identified via the nearby cycle functor).

**Concrete example: degenerating elliptic curves.** For the Legendre family $y^2 = x(x-1)(x-t)$ as $t \to 0$, the fiber degenerates to a nodal rational curve. The monodromy is
$$
T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad N = \log T = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.
$$

The weight filtration associated to $N$ (centered at weight $1$) is $W_0 = \operatorname{span}\{e_2\} \subset W_1 = W_2 = \mathbb{Q}^2$. The resulting mixed Hodge structure has graded pieces $\operatorname{Gr}_0^W \cong \mathbb{Q}$ of type $(0,0)$ (the vanishing cycle) and $\operatorname{Gr}_2^W \cong \mathbb{Q}$ of type $(1,1)$, reflecting the topology of the nodal degeneration.

<!-- BENCHMARK_PROBLEM: For a family of elliptic curves degenerating to a nodal rational curve (e.g., $y^{2} = x(x-1)(x-t)$ as $t \to 0$), compute the monodromy matrix $T$, the nilpotent operator $N = \log T$, and the weight filtration $W_{\bullet}$ associated to $N$. -->

### Example: variation of Hodge structures, Siegel upper half plane {#ecag-0357}

The period domain for weight-$1$ polarized Hodge structures of dimension $g$ is the Siegel upper half space
$$
\mathfrak{H}_g = \{Z \in \operatorname{Mat}_{g \times g}(\mathbb{C}) : Z = Z^T, \; \operatorname{Im}(Z) > 0\}.
$$

This is the natural generalization of the upper half plane $\mathfrak{H}_1 = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}$ that parametrizes elliptic curves.

**From Hodge structures to period matrices.** A polarized Hodge structure of weight $1$ on a lattice $H_{\mathbb{Z}} \cong \mathbb{Z}^{2g}$ consists of a decomposition $H_{\mathbb{C}} = H^{1,0} \oplus H^{0,1}$ with $\overline{H^{1,0}} = H^{0,1}$, together with a symplectic form $Q\colon H_{\mathbb{Z}} \times H_{\mathbb{Z}} \to \mathbb{Z}$ satisfying $Q(H^{1,0}, H^{1,0}) = 0$ and $iQ(v, \bar{v}) > 0$ for $v \in H^{1,0} \setminus \{0\}$.

Choose a symplectic basis $(e_1, \ldots, e_g, f_1, \ldots, f_g)$ with $Q(e_i, f_j) = \delta_{ij}$. The subspace $H^{1,0}$ is the row space of a $(g \times 2g)$-matrix $(\Omega_1 \mid \Omega_2)$ where $\Omega_2$ is invertible. Setting $Z = \Omega_2^{-1} \Omega_1$, the Hodge-Riemann conditions translate to $Z = Z^T$ (from the isotropy condition $Q(H^{1,0}, H^{1,0}) = 0$) and $\operatorname{Im}(Z) > 0$ (from positivity). This identifies the parameter space with $\mathfrak{H}_g$.

**Dimensions and group actions.** The Siegel upper half space $\mathfrak{H}_g$ has complex dimension $g(g+1)/2$. The real symplectic group $\operatorname{Sp}_{2g}(\mathbb{R})$ acts transitively on $\mathfrak{H}_g$ by generalized Mobius transformations:
$$
\begin{pmatrix} A & B \\ C & D \end{pmatrix} \cdot Z = (AZ + B)(CZ + D)^{-1}.
$$

**The moduli space $\mathscr{A}_g$.** The arithmetic quotient $\mathscr{A}_g = \operatorname{Sp}_{2g}(\mathbb{Z}) \backslash \mathfrak{H}_g$ is the coarse moduli space of principally polarized abelian varieties of dimension $g$. By the Baily-Borel theorem, $\mathscr{A}_g$ is a quasi-projective variety of dimension $g(g+1)/2$. The Torelli theorem asserts that the period map $\mathcal{M}_g \to \mathscr{A}_g$, sending a smooth curve $C$ of genus $g$ to its Jacobian $(\operatorname{Jac}(C), \Theta)$, is injective. Since $\dim \mathcal{M}_g = 3g - 3$ and $\dim \mathscr{A}_g = g(g+1)/2$, the Torelli map is an embedding for $g \leq 3$ (where $3g - 3 \leq g(g+1)/2$) and its image has positive codimension for $g \geq 4$ (the Schottky problem: characterizing which principally polarized abelian varieties are Jacobians).

<!-- BENCHMARK_PROBLEM: Compute the dimension of the Siegel upper half space $\mathfrak{H}_{g}$ for $g = 3$, and compare it with $\dim \mathcal{M}_{3} = 3g - 3 = 6$. What does this comparison tell you about the Torelli map? -->

### Example: Mixed Hodge structure, nodal curve {#ecag-0358}

Let $C$ be a projective curve with a single node $p$, obtained by identifying two distinct points $p_1, p_2$ on the smooth normalization $\widetilde{C}$. The first cohomology $H^1(C, \mathbb{Z})$ carries a mixed Hodge structure whose weight filtration cleanly separates the contribution of the singularity from that of the normalization.

**The normalization sequence.** The normalization map $\nu\colon \widetilde{C} \to C$ gives an exact sequence of sheaves on $C$:
$$
0 \to \mathcal{O}_C \to \nu_* \mathcal{O}_{\widetilde{C}} \to \mathbb{C}_p \to 0,
$$

where $\mathbb{C}_p$ is the skyscraper sheaf at the node (the cokernel encodes the identification $f(p_1) = f(p_2)$ imposed on functions). The associated long exact sequence in cohomology yields
$$
0 \to \mathbb{C} \to \mathbb{C} \oplus \mathbb{C} \to \mathbb{C} \to H^1(C, \mathcal{O}_C) \to H^1(\widetilde{C}, \mathcal{O}_{\widetilde{C}}) \to 0.
$$

Since both $C$ and $\widetilde{C}$ are connected, $H^0(C, \mathcal{O}_C) = H^0(\widetilde{C}, \mathcal{O}_{\widetilde{C}}) = \mathbb{C}$. The connecting map $\mathbb{C} \to H^1$ is injective, giving
$$
\dim H^1(C, \mathcal{O}_C) = g(\widetilde{C}) + 1 = p_a(C).
$$

**Topology.** At the level of singular homology, $H_1(C, \mathbb{Z}) \cong H_1(\widetilde{C}, \mathbb{Z}) \oplus \mathbb{Z}$. The extra $\mathbb{Z}$ is generated by the vanishing cycle $\gamma$: the small loop around the node, formed by connecting $p_1$ to $p_2$ via a path on $\widetilde{C}$ and closing up through the identification.

**The mixed Hodge structure.** The weight filtration on $H^1(C, \mathbb{Z})$ is:

- $W_0 = \mathbb{Z} \cdot [\gamma]$, of Hodge type $(0,0)$. This is the part coming from the singularity.
- $\operatorname{Gr}_1^W = H^1(\widetilde{C}, \mathbb{Z})$, a pure Hodge structure of weight $1$ with $h^{1,0} = h^{0,1} = g(\widetilde{C})$.

The Hodge filtration is $F^1 H^1(C, \mathbb{C}) = H^0(\widetilde{C}, \omega_{\widetilde{C}}(p_1 + p_2))$, consisting of meromorphic differentials on $\widetilde{C}$ with at most simple poles at $p_1$ and $p_2$ and opposite residues (so that they descend to regular $1$-forms on $C$ in a generalized sense).

**Special case: rational nodal curve.** When $\widetilde{C} = \mathbb{P}^1$ (so $C$ is an irreducible rational curve with one node), we have $H^1(C, \mathbb{Z}) \cong \mathbb{Z}$, purely of type $(0,0)$. The arithmetic genus is $p_a(C) = 1$ while the geometric genus is $g(\widetilde{C}) = 0$. The mixed Hodge structure is concentrated in weight $0$.

<!-- BENCHMARK_PROBLEM: Let $C$ be an irreducible curve of arithmetic genus $2$ with one node, so that $\widetilde{C}$ has genus $1$. Describe the mixed Hodge structure on $H^{1}(C, \mathbb{Z})$: give the weight filtration, the Hodge type of each graded piece, and compute $h^{1,0}$ and $h^{0,1}$ of the pure part. -->
### Example: Mixed Hodge structure, split over $\mathbb{R}$ {#ecag-0359}

A mixed Hodge structure $(H_{\mathbb{Z}}, W_{\bullet}, F^{\bullet})$ is $\mathbb{R}$-split if there exists a bigrading $H_{\mathbb{C}} = \bigoplus_{p,q} I^{p,q}$ simultaneously compatible with the weight filtration ($W_k \otimes \mathbb{C} = \bigoplus_{p+q \leq k} I^{p,q}$), the Hodge filtration ($F^p = \bigoplus_{a \geq p} I^{a,b}$), and conjugation ($\overline{I^{p,q}} = I^{q,p}$). Not every mixed Hodge structure is $\mathbb{R}$-split, although every one admits a canonical splitting over $\mathbb{C}$.

**The Deligne splitting.** Every mixed Hodge structure possesses unique subspaces $I^{p,q} \subset H_{\mathbb{C}}$ satisfying $F^p = \bigoplus_{a \geq p} I^{a,b}$, $\bar{F}^q = \bigoplus_{b \geq q} I^{a,b}$, and $W_k \otimes \mathbb{C} = \bigoplus_{p+q \leq k} I^{p,q}$. These are the Deligne subspaces. In general, $\overline{I^{p,q}} \neq I^{q,p}$; instead one has only the weaker congruence $\overline{I^{p,q}} \equiv I^{q,p} \pmod{\bigoplus_{a < q,\, b < p} I^{a,b}}$. The mixed Hodge structure is $\mathbb{R}$-split precisely when equality holds: $\overline{I^{p,q}} = I^{q,p}$ on the nose. This is equivalent to requiring that the extension classes in $\operatorname{Ext}^1_{\mathrm{MHS}}(\operatorname{Gr}_{k+1}^W, \operatorname{Gr}_k^W)$ lie in the real part of the extension group.

**An $\mathbb{R}$-split example.** The mixed Hodge structure on $H^1$ of a rational nodal curve is $\mathbb{R}$-split: $H^1(C, \mathbb{Z}) = \mathbb{Z}$ of type $(0,0)$, which is trivially split (there is no nontrivial extension data).

**A non-$\mathbb{R}$-split example.** Take $H_{\mathbb{Z}} = \mathbb{Z}^3$ with basis $\{e_1, e_2, e_3\}$. Define the weight filtration by $W_0 = \mathbb{Z} e_1$ and $W_1 = H_{\mathbb{Z}}$, so $\operatorname{Gr}_0^W \cong \mathbb{Z}$ of type $(0,0)$ and $\operatorname{Gr}_1^W \cong \mathbb{Z}^2$ with Hodge decomposition of type $\{(1,0),(0,1)\}$. Define the Hodge filtration by
$$
F^1 = \mathbb{C} \cdot (e_2 + i e_3 + \tau e_1),
$$

where $\tau \in \mathbb{C}$. One checks that this defines a valid mixed Hodge structure for any $\tau$, and that:

- If $\tau \in \mathbb{R}$, the Deligne splitting satisfies $\overline{I^{p,q}} = I^{q,p}$ and the structure is $\mathbb{R}$-split.
- If $\operatorname{Im}(\tau) \neq 0$, the structure is not $\mathbb{R}$-split: the extension class has a nontrivial imaginary part.

Geometrically, in the context of a degeneration of curves acquiring a node, the parameter $\tau$ records the position of the node relative to the Jacobian of the normalization. The resulting mixed Hodge structure on the limit is $\mathbb{R}$-split precisely when this extension class is real.

<!-- BENCHMARK_PROBLEM: Construct an explicit mixed Hodge structure on $\mathbb{Z}^{3}$ with weights $0$ and $1$ (one-dimensional weight $0$ part of type $(0,0)$, two-dimensional weight $1$ part of type $\{(1,0),(0,1)\}$) that is NOT split over $\mathbb{R}$. Specify the weight filtration and Hodge filtration. -->

### Example: Unimodular lattices {#ecag-0360}

A unimodular lattice is a free $\mathbb{Z}$-module $L$ of finite rank equipped with a symmetric bilinear form $\langle \cdot, \cdot \rangle\colon L \times L \to \mathbb{Z}$ whose Gram matrix has determinant $\pm 1$. Such lattices arise throughout algebraic geometry and topology as intersection forms on the middle cohomology of compact oriented manifolds.

**Classification by type and signature.** Unimodular lattices fall into two classes:

- **Type I (odd):** there exists $v \in L$ with $\langle v, v \rangle$ odd. The standard examples are the diagonal lattices $I_{p,q} = (\mathbb{Z}^{p+q}, \operatorname{diag}(1,\ldots,1,-1,\ldots,-1))$ of signature $(p,q)$.
- **Type II (even):** $\langle v, v \rangle \in 2\mathbb{Z}$ for all $v$. Key examples include the $E_8$ root lattice (rank $8$, positive definite, $\det = 1$), its negative $E_8(-1)$, and the hyperbolic plane $U$ with Gram matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (signature $(1,1)$, $\det = -1$).

**The Milnor-Kneser theorem.** Indefinite even unimodular lattices are classified by rank and signature alone. Such a lattice of signature $(p,q)$ with $p, q \geq 1$ exists if and only if $p - q \equiv 0 \pmod{8}$, and when it exists it is unique up to isometry. In the positive definite case, classification is far more intricate: there is one even unimodular lattice of rank $8$ ($E_8$), two of rank $16$ ($E_8 \oplus E_8$ and $D_{16}^+$), and twenty-four of rank $24$ (the Niemeier lattices, including the Leech lattice).

**Intersection forms of $4k$-manifolds.** For a smooth compact oriented $4k$-manifold $M$, Poincare duality makes the intersection pairing on $H^{2k}(M, \mathbb{Z})/\mathrm{torsion}$ into a unimodular lattice. For simply connected closed $4$-manifolds, Freedman's theorem states that the homeomorphism type is determined by this lattice (together with a $\mathbb{Z}/2$-valued invariant in the odd case).

**The K3 lattice.** For a K3 surface $X$, the intersection form on $H^2(X, \mathbb{Z})$ is the unique even unimodular lattice of signature $(3, 19)$:
$$
\Lambda_{K3} = U^{\oplus 3} \oplus E_8(-1)^{\oplus 2}.
$$

This has rank $3 \cdot 2 + 2 \cdot 8 = 22$. The signature is $(3 \cdot 1 + 2 \cdot 0,\; 3 \cdot 1 + 2 \cdot 8) = (3, 19)$, since each copy of $U$ contributes signature $(1,1)$ and each $E_8(-1)$ contributes $(0,8)$. The discriminant is $(-1)^3 \cdot 1^2 = -1$ (each $U$ has $\det = -1$ and each $E_8(-1)$ has $\det = 1$), confirming unimodularity. The lattice $\Lambda_{K3}$ is even because both $U$ and $E_8(-1)$ are even. By the Milnor-Kneser theorem and $3 - 19 = -16 \equiv 0 \pmod{8}$, this is the unique such lattice.

<!-- BENCHMARK_PROBLEM: Verify that the K3 lattice $\Lambda_{K3} = U^{3} \oplus E_{8}(-1)^{2}$ has rank $22$, signature $(3, 19)$, and is even and unimodular. Compute the discriminant of $U$ and of $E_{8}$. -->

### Example: Mixed Hodge structure on $\mathfrak{gl}(V_{\mathbb{C}})$ {#ecag-0361}

If $(V_{\mathbb{Q}}, W_{\bullet}, F^{\bullet})$ is a mixed Hodge structure, then the endomorphism space $\operatorname{End}(V) \cong V^{\vee} \otimes V \cong \mathfrak{gl}(V)$ inherits a natural mixed Hodge structure. This construction connects Hodge theory to Lie theory: the weight-graded pieces of $\operatorname{End}(V)$ encode the Lie algebra of the Mumford-Tate group.

**The induced filtrations.** The weight and Hodge filtrations on $\operatorname{End}(V)$ are defined by:
$$
W_k \operatorname{End}(V_{\mathbb{Q}}) = \{f \in \operatorname{End}(V_{\mathbb{Q}}) : f(W_i) \subset W_{i+k} \text{ for all } i\},
$$
$$
F^p \operatorname{End}(V_{\mathbb{C}}) = \{f \in \operatorname{End}(V_{\mathbb{C}}) : f(F^i) \subset F^{i+p} \text{ for all } i\}.
$$

That these define a mixed Hodge structure follows from the general fact that $\operatorname{End}(V) \cong V^{\vee} \otimes V$ and the category of mixed Hodge structures is closed under duals and tensor products.

**The Deligne decomposition.** If $V_{\mathbb{C}} = \bigoplus_{p,q} I^{p,q}$ is the Deligne splitting of $V$, then $\operatorname{End}(V_{\mathbb{C}}) = \bigoplus \operatorname{Hom}(I^{r,s}, I^{p,q})$, and the summand $\operatorname{Hom}(I^{r,s}, I^{p,q})$ has Deligne type $(p-r, q-s)$ in $\operatorname{End}(V)$. This makes the bigrading completely explicit.

**Lie-algebraic significance.** The weight-$0$ piece $W_0 \operatorname{End}(V) \cap F^0 \operatorname{End}(V_{\mathbb{C}})$ is the Lie algebra of endomorphisms preserving both filtrations -- this is the Lie algebra of the Mumford-Tate group. The negative-weight piece $W_{-1} \operatorname{End}(V) \cap F^0$ is the Lie algebra of the unipotent radical. For degenerations, the nilpotent operator $N$ satisfies $N \in W_{-2} \operatorname{End}(V) \cap F^{-1} \operatorname{End}(V_{\mathbb{C}})$ by the $\operatorname{SL}_2$-orbit theorem.

**Explicit computation.** Take $V = \mathbb{Q}^2$ with $W_0 = \mathbb{Q} e_1$, $W_1 = V$, and $F^1 = \mathbb{C}(e_2 + \tau e_1)$ for some $\tau \in \mathbb{C}$. In the basis $\{e_1, e_2\}$, $\operatorname{End}(V) \cong \operatorname{Mat}_{2 \times 2}(\mathbb{Q})$. An endomorphism $f$ represented by $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ sends $e_1 \mapsto ae_1 + ce_2$ and $e_2 \mapsto be_1 + de_2$. The condition $f(W_i) \subset W_{i+k}$ gives:

| Weight $k$ | Condition | Matrices | $\dim$ |
|------------|-----------|----------|--------|
| $W_{-1}$ | $f(W_0) = 0$, $f(W_1) \subset W_0$ | $\begin{pmatrix} 0 & b \\ 0 & 0 \end{pmatrix}$ | $1$ |
| $W_0$ | $f(W_0) \subset W_0$, $f(W_1) \subset W_1$ | $\begin{pmatrix} a & b \\ 0 & d \end{pmatrix}$ | $3$ |
| $W_1$ | (all) | $\operatorname{Mat}_{2\times 2}$ | $4$ |

Thus $\operatorname{Gr}_{-1}^W \operatorname{End}(V)$ has dimension $1$, $\operatorname{Gr}_0^W$ has dimension $2$, and $\operatorname{Gr}_1^W$ has dimension $1$. The graded piece $\operatorname{Gr}_{-1}^W$ consists of maps $W_1/W_0 \to W_0$, i.e., $\operatorname{Hom}(\operatorname{Gr}_1^W V, \operatorname{Gr}_0^W V)$, of Hodge type $(-1, -1) + (0,0) = (-1,-1)$... more precisely, its type depends on the Hodge types of the graded pieces. The graded piece $\operatorname{Gr}_1^W$ consists of maps $W_0 \to W_1/W_0$, i.e., $\operatorname{Hom}(\operatorname{Gr}_0^W V, \operatorname{Gr}_1^W V)$.

<!-- BENCHMARK_PROBLEM: Let $V = \mathbb{Q}^{2}$ with the mixed Hodge structure given by $W_{0} = \mathbb{Q} e_{1}$, $W_{1} = V$, $F^{1} = \mathbb{C}(e_{2} + ie_{1})$. Compute the weight filtration on $\operatorname{End}(V)$ and determine $\dim_{\mathbb{Q}} \operatorname{Gr}_{k}^{W}\operatorname{End}(V)$ for $k = -1, 0, 1$. -->
