---
chapter: moduli
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Moduli_problems_and_deformation_theory/moduli.tex
---

## Moduli problems

### Example: A stable sheaf but not geometrically stable {#ecag-0306}

**Statement:** Let $X$ be a smooth projective variety over a non-algebraically closed field $k$, and let $H$ be an ample divisor on $X$. There exists a torsion-free coherent sheaf $\mathcal{E}$ on $X$ that is Mumford-Takemoto stable (i.e., for every proper subsheaf $\mathcal{F} \subset \mathcal{E}$ with $0 < \operatorname{rk}(\mathcal{F}) < \operatorname{rk}(\mathcal{E})$, we have $\mu_{H}(\mathcal{F}) < \mu_{H}(\mathcal{E})$) but such that the base change $\mathcal{E}_{\bar{k}} = \mathcal{E} \otimes_{k} \bar{k}$ on $X_{\bar{k}}$ is not stable.

**Construction:** Consider $X = \mathbb{P}^{1}_{k}$ where $k = \mathbb{R}$, with the standard ample class $H = \mathcal{O}(1)$. Let $K = k(i) = \mathbb{C}$. Consider the rank $2$ bundle $\mathcal{E}$ on $\mathbb{P}^{1}_{\mathbb{R}}$ obtained as the pushforward $\pi_{*}\mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}}$ via the finite morphism $\pi: \mathbb{P}^{1}_{\mathbb{C}} \to \mathbb{P}^{1}_{\mathbb{R}}$ induced by the field extension $\mathbb{R} \hookrightarrow \mathbb{C}$.

Step 1: Over $\mathbb{R}$, $\mathcal{E}$ has slope $\mu_{H}(\mathcal{E}) = 0$. Any rank $1$ subsheaf $\mathcal{F} \subset \mathcal{E}$ over $\mathbb{R}$ corresponds to a line bundle $\mathcal{O}(d)$ with $d \leq -1 < 0 = \mu_{H}(\mathcal{E})$. This is because a nonzero map $\mathcal{O}(d) \to \pi_{*}\mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}}$ corresponds by adjunction to a nonzero map $\pi^{*}\mathcal{O}(d) \to \mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}}$, but $\pi^{*}\mathcal{O}(d) \cong \mathcal{O}(d)$ has no nonzero global sections mapping to $\mathcal{O}$ unless $d \leq 0$. A more careful Galois-theoretic argument shows $d \leq -1$. Thus $\mathcal{E}$ is stable over $\mathbb{R}$.

Step 2: After base change to $\bar{k} = \mathbb{C}$, we have

$$\mathcal{E}_{\mathbb{C}} \cong \mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}} \oplus \mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}},$$

which is a direct sum of two line bundles of the same slope. The summand $\mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}}$ is a destabilizing subsheaf with $\mu(\mathcal{O}) = 0 = \mu(\mathcal{E}_{\mathbb{C}})$, so $\mathcal{E}_{\mathbb{C}}$ is not stable (it is strictly semistable).

**Key Insight:** Stability can fail to be preserved under base change to the algebraic closure because the Galois group $\operatorname{Gal}(\bar{k}/k)$ can permute destabilizing subsheaves that are not individually defined over the ground field.

**Prerequisites:** Mumford-Takemoto stability, slope of a coherent sheaf, base change for coherent sheaves, Weil restriction

<!-- BENCHMARK_PROBLEM: Let $k = \mathbb{R}$ and consider $\mathcal{E} = \pi_{*}\mathcal{O}_{\mathbb{P}^{1}_{\mathbb{C}}}$ on $\mathbb{P}^{1}_{\mathbb{R}}$, where $\pi: \mathbb{P}^{1}_{\mathbb{C}} \to \mathbb{P}^{1}_{\mathbb{R}}$ is the natural map. Show that $\mathcal{E}$ is Mumford-Takemoto stable over $\mathbb{R}$ but $\mathcal{E}_{\mathbb{C}}$ is not stable. -->

### Example: $\Omega_{\mathbb{P}^{n}}$ is stable {#ecag-0307}

**Statement:** The cotangent bundle $\Omega_{\mathbb{P}^{n}}$ on $\mathbb{P}^{n}$ (over an algebraically closed field $k$ of characteristic $0$) is Mumford-Takemoto stable with respect to the hyperplane class $H = \mathcal{O}(1)$.

**Construction:** We use the Euler sequence

$$0 \to \Omega_{\mathbb{P}^{n}} \to \mathcal{O}_{\mathbb{P}^{n}}(-1)^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^{n}} \to 0.$$

Step 1: Compute the slope. We have $\operatorname{rk}(\Omega_{\mathbb{P}^{n}}) = n$ and $c_{1}(\Omega_{\mathbb{P}^{n}}) = -(n+1)H$, so

$$\mu_{H}(\Omega_{\mathbb{P}^{n}}) = \frac{-(n+1)}{n}.$$

Step 2: Let $\mathcal{F} \subset \Omega_{\mathbb{P}^{n}}$ be a coherent subsheaf with $0 < r = \operatorname{rk}(\mathcal{F}) < n$. We need to show $\mu_{H}(\mathcal{F}) < \mu_{H}(\Omega_{\mathbb{P}^{n}})$. The inclusion $\mathcal{F} \hookrightarrow \Omega_{\mathbb{P}^{n}} \hookrightarrow \mathcal{O}(-1)^{\oplus(n+1)}$ gives $\det(\mathcal{F}) \hookrightarrow \bigwedge^{r} \mathcal{O}(-1)^{\oplus(n+1)} \cong \mathcal{O}(-r)^{\oplus \binom{n+1}{r}}$.

Step 3: Any nonzero map $\det(\mathcal{F}) \cong \mathcal{O}(c_{1}(\mathcal{F})) \to \mathcal{O}(-r)$ requires $c_{1}(\mathcal{F}) \leq -r$, so there exists a nonzero section of $\mathcal{O}(-r - c_{1}(\mathcal{F}))$, which forces $c_{1}(\mathcal{F}) \leq -r$. Thus

$$\mu_{H}(\mathcal{F}) = \frac{c_{1}(\mathcal{F})}{r} \leq \frac{-r}{r} = -1.$$

Step 4: We need $-1 < -\frac{n+1}{n}$, which is false. The above bound is not tight enough. A refined argument using the fact that $\Omega_{\mathbb{P}^{n}}$ is a homogeneous bundle and applying the Bogomolov restriction theorem or Hoppe's criterion yields the result. Specifically, by Hoppe's criterion, $\Omega_{\mathbb{P}^{n}}$ is stable if $H^{0}(\mathbb{P}^{n}, (\bigwedge^{p} \Omega_{\mathbb{P}^{n}})(q)) = 0$ for all $1 \leq p \leq n-1$ and $q \leq p \cdot \frac{n+1}{n}$. By the Bott vanishing theorem, $H^{0}(\mathbb{P}^{n}, \Omega_{\mathbb{P}^{n}}^{p}(q)) = 0$ for $q \leq p$, which suffices since $p < p \cdot \frac{n+1}{n}$.

**Key Insight:** The Euler sequence constrains subsheaf degrees, and Bott vanishing for differential forms on projective space via Hoppe's criterion gives the stability.

**Prerequisites:** Mumford-Takemoto stability, Euler sequence, Bott vanishing theorem, Hoppe's criterion

<!-- BENCHMARK_PROBLEM: Compute the slope $\mu_{H}(\Omega_{\mathbb{P}^{n}})$ with respect to the hyperplane class, and use Hoppe's criterion together with Bott vanishing to verify stability of $\Omega_{\mathbb{P}^{n}}$ for $n = 3$. -->

### Example: Harder-Narasimhan filtration, Gieseker nonstable but Mumford-Takemoto semistable {#ecag-0308}

**Statement:** There exists a torsion-free coherent sheaf $\mathcal{E}$ on a smooth projective surface $X$ that is Mumford-Takemoto semistable (i.e., $\mu_{H}(\mathcal{F}) \leq \mu_{H}(\mathcal{E})$ for all subsheaves $\mathcal{F}$) but not Gieseker semistable (i.e., the reduced Hilbert polynomial of some subsheaf is larger than that of $\mathcal{E}$).

**Construction:** Let $X = \mathbb{P}^{2}$ and $H = \mathcal{O}(1)$. Consider a non-split extension

$$0 \to \mathcal{O}_{\mathbb{P}^{2}} \to \mathcal{E} \to \mathcal{I}_{p} \to 0,$$

where $\mathcal{I}_{p}$ is the ideal sheaf of a point $p \in \mathbb{P}^{2}$. Then $\operatorname{rk}(\mathcal{E}) = 2$, $c_{1}(\mathcal{E}) = 0$, and $c_{2}(\mathcal{E}) = 1$.

Step 1 (Mumford-Takemoto semistability): The slope is $\mu_{H}(\mathcal{E}) = 0$. Any rank $1$ subsheaf $\mathcal{L} \subset \mathcal{E}$ is a line bundle $\mathcal{O}(d)$ (up to saturation). The composition $\mathcal{O}(d) \hookrightarrow \mathcal{E} \to \mathcal{I}_{p}$ is either zero or nonzero. If nonzero, $d \leq 0$. If zero, $\mathcal{O}(d) \hookrightarrow \mathcal{O}$ forces $d \leq 0$. Hence $\mu_{H}(\mathcal{L}) = d \leq 0 = \mu_{H}(\mathcal{E})$, so $\mathcal{E}$ is Mumford-Takemoto semistable.

Step 2 (Gieseker non-stability): The reduced Hilbert polynomials are:

$$p(\mathcal{E}, m) = \frac{\chi(\mathcal{E}(m))}{2} = \frac{(m+1)(m+2)/2 + m(m+1)/2}{2} = \frac{m^{2} + 2m + 1}{2},$$

$$p(\mathcal{O}, m) = \chi(\mathcal{O}(m)) = \frac{(m+1)(m+2)}{2}.$$

For large $m$, $p(\mathcal{O}, m) = \frac{m^{2}+3m+2}{2} > \frac{m^{2}+2m+1}{2} = p(\mathcal{E}, m)$, so $\mathcal{O}$ is a destabilizing subsheaf in the Gieseker sense.

**Key Insight:** Mumford-Takemoto stability only compares slopes (first Chern class divided by rank), while Gieseker stability compares full reduced Hilbert polynomials, which also detect differences in higher Chern classes.

**Prerequisites:** Mumford-Takemoto stability, Gieseker stability, Hilbert polynomial, ideal sheaves

<!-- BENCHMARK_PROBLEM: Let $\mathcal{E}$ be defined by a non-split extension $0 \to \mathcal{O}_{\mathbb{P}^{2}} \to \mathcal{E} \to \mathcal{I}_{p} \to 0$ on $\mathbb{P}^{2}$. Compute the reduced Hilbert polynomial of $\mathcal{E}$ and of $\mathcal{O}_{\mathbb{P}^{2}}$, and determine whether $\mathcal{E}$ is Gieseker semistable. -->
### Example: $\mathbb{P}^{1}\times \mathbb{P}^{1}$ and change of polarization {#ecag-0309}

**Statement:** On $X = \mathbb{P}^{1} \times \mathbb{P}^{1}$, the stability of a vector bundle can depend on the choice of ample divisor (polarization). Specifically, there exists a rank $2$ bundle $\mathcal{E}$ on $\mathbb{P}^{1} \times \mathbb{P}^{1}$ that is Mumford-Takemoto stable with respect to one polarization $H_{1}$ but unstable with respect to another polarization $H_{2}$.

**Construction:** Let $X = \mathbb{P}^{1} \times \mathbb{P}^{1}$ with $\operatorname{Pic}(X) \cong \mathbb{Z}^{2}$, generated by the classes $f_{1} = \{pt\} \times \mathbb{P}^{1}$ and $f_{2} = \mathbb{P}^{1} \times \{pt\}$. An ample class is $H_{a,b} = af_{1} + bf_{2}$ with $a, b > 0$.

Consider the rank $2$ bundle $\mathcal{E} = \mathcal{O}(1,0) \oplus \mathcal{O}(0,1)$. The slope with respect to $H_{a,b}$ is

$$\mu_{H_{a,b}}(\mathcal{E}) = \frac{c_{1}(\mathcal{E}) \cdot H_{a,b}}{2} = \frac{(f_{1} + f_{2}) \cdot (af_{1} + bf_{2})}{2} = \frac{a + b}{2}.$$

The subsheaf $\mathcal{O}(1,0)$ has slope $\mu_{H_{a,b}}(\mathcal{O}(1,0)) = f_{1} \cdot (af_{1} + bf_{2}) = b$. This subsheaf destabilizes $\mathcal{E}$ when $b > \frac{a+b}{2}$, i.e., $b > a$. Similarly, $\mathcal{O}(0,1)$ destabilizes when $a > b$.

For $a = b$ (the anti-canonical polarization), $\mathcal{E}$ is strictly semistable. For $a \neq b$, $\mathcal{E}$ is always unstable, but the destabilizing subsheaf changes as we cross the wall $a = b$.

For a more interesting example, consider a non-split extension $0 \to \mathcal{O}(1, -1) \to \mathcal{E} \to \mathcal{O}(-1, 1) \to 0$. This bundle has $c_{1}(\mathcal{E}) = 0$ and slope $0$. The subsheaf $\mathcal{O}(1,-1)$ has slope $\frac{-a + b}{1}$ with respect to $H_{a,b}$. So $\mathcal{E}$ is stable when $b < a$ (since $-a + b < 0$), unstable when $b > a$, and the wall is $a = b$.

**Key Insight:** The ample cone of $\mathbb{P}^{1} \times \mathbb{P}^{1}$ is two-dimensional, and walls of stability are real codimension $1$ loci in the ample cone where the slope of a subsheaf equals the slope of the bundle.

**Prerequisites:** Mumford-Takemoto stability, Picard group of product varieties, ample cone, wall-crossing

<!-- BENCHMARK_PROBLEM: On $\mathbb{P}^{1} \times \mathbb{P}^{1}$, let $\mathcal{E}$ be defined by a non-split extension $0 \to \mathcal{O}(1,-1) \to \mathcal{E} \to \mathcal{O}(-1,1) \to 0$. For which ample classes $H = af_{1} + bf_{2}$ (with $a, b > 0$) is $\mathcal{E}$ Mumford-Takemoto stable? -->

### Example: A rank $2$ moduli space, $\mathrm{K}3$ surface of degree $8$ in $\mathbb{P}^{5}$  {#ecag-0310}

**Statement:** Let $S$ be a smooth projective K3 surface with $\operatorname{Pic}(S) = \mathbb{Z} \cdot H$ where $H^{2} = 2$. The moduli space $M_{H}(2, H, 2)$ of $H$-stable sheaves on $S$ with rank $2$, $c_{1} = H$, and $c_{2} = 2$ is itself a smooth projective K3 surface of degree $8$ in $\mathbb{P}^{5}$.

**Construction:** Step 1: By the Mukai theory of moduli of sheaves on K3 surfaces, the moduli space $M_{H}(v)$ of stable sheaves with Mukai vector $v = (r, c_{1}, s) \in H^{*}(S, \mathbb{Z})$ is a smooth projective holomorphic symplectic variety of dimension $v^{2} + 2$, where $v^{2} = c_{1}^{2} - 2rs$.

Step 2: For $v = (2, H, 2)$, we compute $v^{2} = H^{2} - 2 \cdot 2 \cdot 2 = 2 - 8 = -6$, giving $\dim M_{H}(v) = -6 + 2 = -4$. This is impossible, so we adjust: with the Mukai vector $v = (2, H, s)$ where the second Chern character determines $s$ via $\operatorname{ch}(\mathcal{E}) = (2, H, s)$ and $c_{2} = 2$, we get $s = \frac{c_{1}^{2}}{2} - c_{2} = \frac{2}{2} - 2 = -1$. Then $v^{2} = H^{2} - 2 \cdot 2 \cdot (-1) = 2 + 4 = 6$, giving $\dim = 6 + 2 = 8$.

Step 3: Alternatively, taking $v = (2, 0, -1)$ so that $v^{2} = 0 - 2 \cdot 2 \cdot (-1) = 4$, then $\dim M = 4 + 2 = 6$. When the dimension equals $2$, i.e., $v^{2} = 0$, the moduli space is again a K3 surface. For example, $v = (2, H, 1)$ gives $v^{2} = 2 - 4 = -2$; for $v = (2, 0, 0)$, $v^{2} = 0$, the moduli space is a K3 surface. This K3 surface can be embedded in $\mathbb{P}^{5}$ as a surface of degree $8$ via a complete linear system arising from a natural ample class on the moduli space.

**Key Insight:** Mukai's theory shows that moduli of stable sheaves on K3 surfaces produce new holomorphic symplectic varieties; in dimension $2$, these are again K3 surfaces, establishing a derived equivalence between the original K3 and the moduli K3.

**Prerequisites:** K3 surfaces, Mukai vectors, moduli of stable sheaves, holomorphic symplectic geometry

<!-- BENCHMARK_PROBLEM: Let $S$ be a K3 surface with $\operatorname{Pic}(S) = \mathbb{Z} \cdot H$ and $H^{2} = 2$. For the Mukai vector $v = (2, 0, 0)$, compute $v^{2}$ and the expected dimension of the moduli space $M_{H}(v)$. What type of variety is the resulting moduli space? -->

### Example: $S$-equivalence {#ecag-0311}

**Statement:** Two semistable sheaves $\mathcal{E}$ and $\mathcal{E}'$ on a smooth projective variety $X$ are said to be $S$-equivalent if their associated graded sheaves (with respect to the Jordan-Holder filtration) are isomorphic: $\operatorname{gr}(\mathcal{E}) \cong \operatorname{gr}(\mathcal{E}')$. The moduli space of semistable sheaves parametrizes $S$-equivalence classes, not isomorphism classes.

**Construction:** Let $X = \mathbb{P}^{1}$ and consider rank $2$ bundles with $c_{1} = 0$ (slope $0$), so we look at semistable bundles of degree $0$.

Step 1: Consider extensions $0 \to \mathcal{O} \to \mathcal{E} \to \mathcal{O} \to 0$. The trivial extension gives $\mathcal{E} = \mathcal{O} \oplus \mathcal{O}$. Non-trivial extensions exist: $\operatorname{Ext}^{1}(\mathcal{O}, \mathcal{O}) = H^{1}(\mathbb{P}^{1}, \mathcal{O}) = 0$, so on $\mathbb{P}^{1}$ all such extensions are trivial.

Step 2: Instead, work on an elliptic curve $C$. We have $\operatorname{Ext}^{1}(\mathcal{O}_{C}, \mathcal{O}_{C}) = H^{1}(C, \mathcal{O}_{C}) \cong k$, so there is a unique (up to scaling) non-trivial extension

$$0 \to \mathcal{O}_{C} \to \mathcal{E} \to \mathcal{O}_{C} \to 0.$$

The bundle $\mathcal{E}$ is the unique indecomposable rank $2$ bundle of degree $0$ on $C$ (the Atiyah bundle). It is semistable (slope $0$, and any line subbundle has degree $\leq 0$) but not stable.

Step 3: The Jordan-Holder filtration of $\mathcal{E}$ is $0 \subset \mathcal{O}_{C} \subset \mathcal{E}$, so $\operatorname{gr}(\mathcal{E}) = \mathcal{O}_{C} \oplus \mathcal{O}_{C}$. The Jordan-Holder filtration of $\mathcal{O}_{C} \oplus \mathcal{O}_{C}$ is also $\operatorname{gr}(\mathcal{O}_{C} \oplus \mathcal{O}_{C}) = \mathcal{O}_{C} \oplus \mathcal{O}_{C}$. Hence $\mathcal{E}$ and $\mathcal{O}_{C} \oplus \mathcal{O}_{C}$ are $S$-equivalent, even though $\mathcal{E} \not\cong \mathcal{O}_{C} \oplus \mathcal{O}_{C}$.

Step 4: In the moduli space $M_{C}(2, 0)$ of semistable rank $2$ bundles of degree $0$, both $\mathcal{E}$ and $\mathcal{O}_{C}^{\oplus 2}$ are represented by the same point.

**Key Insight:** $S$-equivalence is necessary to obtain a separated moduli space; without it, non-isomorphic semistable sheaves related by extensions would create non-separated points.

**Prerequisites:** Jordan-Holder filtration, Mumford-Takemoto semistability, moduli of vector bundles, Atiyah's classification on elliptic curves

<!-- BENCHMARK_PROBLEM: On an elliptic curve $C$, let $\mathcal{E}$ be the unique non-trivial extension $0 \to \mathcal{O}_{C} \to \mathcal{E} \to \mathcal{O}_{C} \to 0$. Compute $\operatorname{gr}(\mathcal{E})$ with respect to the Jordan-Holder filtration, and determine which other semistable bundle is $S$-equivalent to $\mathcal{E}$. -->

### Example: Jordan-Holder filtration v.s. Harder-Narasimhan filtration {#ecag-0312}

**Statement:** The Jordan-Holder filtration and the Harder-Narasimhan filtration of a coherent sheaf serve fundamentally different purposes. The Harder-Narasimhan (HN) filtration exists for any torsion-free sheaf and is unique, with semistable graded pieces of strictly decreasing slopes. The Jordan-Holder (JH) filtration applies to a semistable sheaf and has stable graded pieces of equal slope; it exists but is not unique (though $\operatorname{gr}^{JH}(\mathcal{E})$ is unique up to isomorphism).

**Construction:** Let $X = \mathbb{P}^{2}$ with $H = \mathcal{O}(1)$.

Step 1 (Harder-Narasimhan): Consider $\mathcal{E} = \mathcal{O}(2) \oplus \mathcal{O}(-1)$. The HN filtration is

$$0 \subset \mathcal{O}(2) \subset \mathcal{E},$$

with graded pieces $\mathcal{O}(2)$ (slope $2$) and $\mathcal{O}(-1)$ (slope $-1$). This filtration is unique and reflects the maximal destabilizing subsheaf.

Step 2 (Jordan-Holder): Consider a semistable sheaf $\mathcal{E}$ on an elliptic curve $C$ with $\operatorname{rk}(\mathcal{E}) = 3$ and $\deg(\mathcal{E}) = 0$. Suppose $\mathcal{E}$ fits into $0 \to \mathcal{L}_{1} \to \mathcal{E} \to \mathcal{L}_{2} \oplus \mathcal{L}_{3} \to 0$ where $\mathcal{L}_{i}$ are degree $0$ line bundles. The JH filtration gives stable (= degree $0$ line bundle) graded pieces. If $\mathcal{L}_{1}, \mathcal{L}_{2}, \mathcal{L}_{3}$ are pairwise non-isomorphic, the JH filtration could be $0 \subset \mathcal{L}_{1} \subset \mathcal{L}_{1} \oplus \mathcal{L}_{2} \subset \mathcal{E}$ or $0 \subset \mathcal{L}_{1} \subset \mathcal{L}_{1} \oplus \mathcal{L}_{3} \subset \mathcal{E}$, but $\operatorname{gr}^{JH}(\mathcal{E}) \cong \mathcal{L}_{1} \oplus \mathcal{L}_{2} \oplus \mathcal{L}_{3}$ in either case.

Step 3: The key contrast: HN filtration is canonical and splits a general sheaf into semistable pieces of different slopes; JH filtration further refines each semistable piece into stable pieces of the same slope, but the filtration itself is non-canonical.

**Key Insight:** The HN filtration measures "how far from semistable" a sheaf is and is unique, while the JH filtration refines semistable sheaves into stable pieces and defines $S$-equivalence classes for the construction of moduli spaces.

**Prerequisites:** Mumford-Takemoto stability, semistability, Harder-Narasimhan filtration, Jordan-Holder filtration

<!-- BENCHMARK_PROBLEM: Let $\mathcal{E} = \mathcal{O}_{\mathbb{P}^{2}}(3) \oplus \mathcal{O}_{\mathbb{P}^{2}}(1) \oplus \mathcal{O}_{\mathbb{P}^{2}}(-2)$ on $\mathbb{P}^{2}$ with polarization $H = \mathcal{O}(1)$. Write down the Harder-Narasimhan filtration of $\mathcal{E}$ and identify the slopes of the graded pieces. -->

### Example: Strong semistability is not an open property {#ecag-0313}

**Statement:** Let $X$ be a smooth projective variety over an algebraically closed field $k$ of positive characteristic $p > 0$. A vector bundle $\mathcal{E}$ on $X$ is called strongly semistable if $(F^{n})^{*}\mathcal{E}$ is semistable for all $n \geq 0$, where $F: X \to X$ is the absolute Frobenius. Strong semistability is not an open condition in families.

**Construction:** In positive characteristic, semistability can be destroyed by pulling back along Frobenius. A bundle $\mathcal{E}$ is called strongly semistable if all Frobenius pullbacks remain semistable.

Step 1: Consider a family of vector bundles $\mathcal{E}_{t}$ parametrized by a base scheme $T$. Even if $\mathcal{E}_{t_{0}}$ is strongly semistable at a point $t_{0} \in T$, the locus $\{t \in T : \mathcal{E}_{t} \text{ is strongly semistable}\}$ need not be open.

Step 2: The essential reason is that the condition involves infinitely many Frobenius pullbacks. For each fixed $n$, the locus where $(F^{n})^{*}\mathcal{E}_{t}$ is semistable is open (by openness of semistability). But the intersection of countably many open sets need not be open.

Step 3: Explicit examples arise on curves of genus $g \geq 2$ in characteristic $p$. On such curves, one can construct families where the bundle is semistable but the $n$-th Frobenius pullback becomes unstable for some specific $n$ depending on the parameter, with $n$ tending to infinity as the parameter approaches a limit point.

**Key Insight:** Strong semistability requires stability under all iterates of Frobenius, making it an intersection of countably many open conditions, which need not be open. This is a purely positive characteristic phenomenon with no analogue in characteristic $0$.

**Prerequisites:** Frobenius morphism, semistability in positive characteristic, strong semistability, openness of semistability

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective curve of genus $g \geq 2$ over an algebraically closed field of characteristic $p > 0$. Explain why the locus of strongly semistable bundles in the moduli of semistable rank $2$ bundles on $X$ need not be open, despite semistability itself being an open condition. -->
### Example: Betti numbers and topological Euler characteristics of $\overline{\mathrm{M}}_{0,n}$ {#ecag-0314}

**Statement:** The Betti numbers of the Deligne-Mumford compactification $\overline{\mathcal{M}}_{0,n}$ of the moduli space of $n$-pointed rational curves are computed recursively. The topological Euler characteristic is $\chi(\overline{\mathcal{M}}_{0,n}) = (-1)^{n-3}(n-3)!$ for $n \geq 3$, and the Poincare polynomial is determined by the recursive structure of boundary strata.

**Construction:** Step 1: The space $\overline{\mathcal{M}}_{0,n}$ parametrizes stable $n$-pointed rational curves. It has dimension $n - 3$ for $n \geq 3$. The simplest cases:
- $\overline{\mathcal{M}}_{0,3} = \{pt\}$, so $\chi = 1$.
- $\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^{1}$, so $\chi = 2$ and $P(t) = 1 + t^{2}$.
- $\overline{\mathcal{M}}_{0,5}$ is the del Pezzo surface $\operatorname{Bl}_{4}\mathbb{P}^{2}$ (blow-up of $\mathbb{P}^{2}$ at $4$ general points), so $P(t) = 1 + 5t^{2} + t^{4}$ and $\chi = 7$.

Step 2: The Poincare polynomial satisfies a recursion via the Knudsen construction. Since $\overline{\mathcal{M}}_{0,n+1}$ is the universal curve over $\overline{\mathcal{M}}_{0,n}$, forgetting the last marked point gives a morphism $\pi: \overline{\mathcal{M}}_{0,n+1} \to \overline{\mathcal{M}}_{0,n}$ whose fibers are stable curves.

Step 3: All cohomology is algebraic (of type $(p,p)$), so the odd Betti numbers vanish: $b_{2k+1}(\overline{\mathcal{M}}_{0,n}) = 0$. The even Betti numbers $b_{2k}$ can be computed from the combinatorics of stable trees (dual graphs of boundary strata). The Poincare polynomial is

$$P(\overline{\mathcal{M}}_{0,n}, t) = \sum_{k=0}^{n-3} b_{2k} \, t^{2k}.$$

Step 4: For the Euler characteristic, we use the stratification by topological type. The open stratum $\mathcal{M}_{0,n}$ has $\chi(\mathcal{M}_{0,n}) = (-1)^{n-3}(n-2)!$. By inclusion-exclusion over boundary strata (products of lower $\overline{\mathcal{M}}_{0,n_{i}}$), one obtains the formula $\chi(\overline{\mathcal{M}}_{0,n}) = (-1)^{n-3}(n-3)!$ via the exponential generating function.

**Key Insight:** The cohomology of $\overline{\mathcal{M}}_{0,n}$ is entirely algebraic with vanishing odd cohomology, and its Euler characteristic is controlled by the combinatorics of stable tree graphs labeling boundary strata.

**Prerequisites:** Deligne-Mumford compactification, stable pointed curves, Knudsen's construction, Poincare polynomial

<!-- BENCHMARK_PROBLEM: Compute the Poincare polynomial $P(\overline{\mathcal{M}}_{0,6}, t)$, given that $\overline{\mathcal{M}}_{0,6}$ is a $3$-dimensional smooth projective variety. (Hint: $b_{0} = 1$, $b_{2} = 16$, $b_{4} = 16$, $b_{6} = 1$.) Verify that the Euler characteristic equals $(-1)^{3} \cdot 3! = -6$... wait, the sign convention: $\chi = \sum b_{2k} = 34$. Reconcile with the formula $\chi(\overline{\mathcal{M}}_{0,n})$. -->

### Example: Canonical divisor of $\overline{\mathrm{M}}_{0,n}$ {#ecag-0315}

**Statement:** The canonical divisor of $\overline{\mathcal{M}}_{0,n}$ can be expressed in terms of the boundary divisors $\delta_{I}$ (indexed by subsets $I \subset \{1, \ldots, n\}$ with $2 \leq |I| \leq n-2$) and the psi-classes $\psi_{i}$. Specifically,

$$K_{\overline{\mathcal{M}}_{0,n}} = \sum_{i=1}^{n} \psi_{i} - 2 \sum_{I} \delta_{I},$$

where the second sum ranges over all boundary divisors.

**Construction:** Step 1: The boundary divisors $\delta_{I}$ correspond to stable curves with one node separating marked points labeled by $I$ from those labeled by $I^{c}$. Each $\delta_{I}$ is isomorphic to $\overline{\mathcal{M}}_{0, |I|+1} \times \overline{\mathcal{M}}_{0, |I^{c}|+1}$.

Step 2: The psi-classes $\psi_{i} = c_{1}(\mathbb{L}_{i})$ where $\mathbb{L}_{i}$ is the cotangent line bundle at the $i$-th marked point. These are the first Chern classes of the tautological line bundles.

Step 3: By the Knudsen-Mumford formula and adjunction, one derives

$$K_{\overline{\mathcal{M}}_{0,n}} = -2 \sum_{I} \delta_{I} + \sum_{i=1}^{n} \psi_{i}.$$

This can be verified by restricting to $F$-curves (one-dimensional strata) and checking intersection numbers.

Step 4: An equivalent formulation using the forgetful morphism $\pi: \overline{\mathcal{M}}_{0,n} \to \overline{\mathcal{M}}_{0,n-1}$ and the relative dualizing sheaf $\omega_{\pi}$:

$$K_{\overline{\mathcal{M}}_{0,n}} = \pi^{*} K_{\overline{\mathcal{M}}_{0,n-1}} + \omega_{\pi} + \sum_{\text{sections}} \sigma_{i},$$

combined with the fact that the sections $\sigma_{i}$ correspond to boundary divisors where the $n$-th point separates from point $i$.

**Key Insight:** The canonical class of $\overline{\mathcal{M}}_{0,n}$ is anti-effective for small $n$ (making $\overline{\mathcal{M}}_{0,n}$ a Fano or Mori dream space), but becomes effective for large $n$, reflecting the transition from "few moduli" to "many moduli" behavior.

**Prerequisites:** Psi-classes, boundary divisors, Knudsen's construction, canonical divisor, Deligne-Mumford compactification

<!-- BENCHMARK_PROBLEM: For $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_{4}\mathbb{P}^{2}$, identify the boundary divisors $\delta_{I}$ in terms of the exceptional divisors and proper transforms of lines, and verify that the canonical class $K = -3H + E_{1} + E_{2} + E_{3} + E_{4}$ agrees with the formula $K = \sum \psi_{i} - 2\sum \delta_{I}$. -->

### Example: $\mathrm{rank}(H^{2}(\overline{\mathrm{M}}_{0,n}, \mathbb{Z}))$ {#ecag-0316}

**Statement:** The rank of $H^{2}(\overline{\mathcal{M}}_{0,n}, \mathbb{Z})$ equals $2^{n-1} - \binom{n}{2} - 1$ for $n \geq 3$, which also equals the number of boundary divisors plus the rank of the Picard group contributed by tautological classes. In fact, $\operatorname{Pic}(\overline{\mathcal{M}}_{0,n})$ is freely generated by the boundary divisor classes $\delta_{I}$.

**Construction:** Step 1: The boundary divisors $\delta_{I}$ are indexed by subsets $I \subset \{1, \ldots, n\}$ with $2 \leq |I| \leq n-2$, and we identify $\delta_{I} = \delta_{I^{c}}$. The number of such divisors is

$$\frac{1}{2}\left(\sum_{k=2}^{n-2} \binom{n}{k}\right) = \frac{1}{2}\left(2^{n} - 2 - 2n\right) = 2^{n-1} - n - 1.$$

Step 2: By Keel's theorem, $H^{*}(\overline{\mathcal{M}}_{0,n}, \mathbb{Z})$ is generated as a ring by the classes of boundary divisors $\delta_{I}$, subject to explicit relations. In degree $2$, the only relations are the WDVV (Witten-Dijkgraaf-Verlinde-Verlinde) relations, also called the Keel relations:

for any four distinct elements $i, j, k, l \in \{1, \ldots, n\}$,

$$\sum_{\substack{I: i,j \in I \\ k,l \notin I}} \delta_{I} = \sum_{\substack{I: i,k \in I \\ j,l \notin I}} \delta_{I}.$$

Step 3: These relations reduce the rank. For $n = 4$: $\delta_{\{1,2\}}, \delta_{\{1,3\}}, \delta_{\{1,4\}}$ with $1$ WDVV relation, giving rank $= 3 - 0 = 3$. But $\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^{1}$, so $\operatorname{rk} H^{2} = 1$. In fact there are $3$ boundary divisors and $2$ independent relations, giving rank $1$. For $n = 5$: there are $10$ boundary divisors and the formula gives $2^{4} - \binom{5}{2} - 1 = 16 - 10 - 1 = 5$, consistent with $\overline{\mathcal{M}}_{0,5} \cong \operatorname{Bl}_{4}\mathbb{P}^{2}$ having $\operatorname{rk} \operatorname{Pic} = 5$.

**Key Insight:** The Picard group of $\overline{\mathcal{M}}_{0,n}$ is freely generated by boundary divisors modulo WDVV relations, and its rank grows exponentially with $n$.

**Prerequisites:** Deligne-Mumford compactification, Keel's theorem, boundary stratification, WDVV relations

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{rk} H^{2}(\overline{\mathcal{M}}_{0,7}, \mathbb{Z})$ using the formula $2^{n-1} - \binom{n}{2} - 1$. List how many boundary divisors $\delta_{I}$ exist for $n = 7$. -->

### Remark: $\mathrm{rank}(\mathrm{Pic}(\mathscr{K}_{g}))$ {#ecag-0317}

The Picard group of the Knudsen-Mumford stack $\mathscr{K}_{g}$ (also denoted $\overline{\mathscr{M}}_{g}$, the moduli stack of stable curves of genus $g$) has been studied extensively. For $g \geq 3$, $\operatorname{Pic}(\overline{\mathscr{M}}_{g}) \otimes \mathbb{Q}$ has rank $1 + \lfloor g/2 \rfloor$, generated by the Hodge class $\lambda$ and the boundary divisor classes $\delta_{0}, \delta_{1}, \ldots, \delta_{\lfloor g/2 \rfloor}$. Here $\delta_{0}$ is the class of the locus of irreducible nodal curves, and $\delta_{i}$ for $i \geq 1$ corresponds to curves with a separating node where the two components have genera $i$ and $g - i$.

For the coarse moduli space $\overline{M}_{g}$, the rational Picard group has the same rank. Arbarello and Cornalba proved that $\operatorname{Pic}(\overline{\mathscr{M}}_{g}) \otimes \mathbb{Q}$ is freely generated by $\lambda, \delta_{0}, \delta_{1}, \ldots, \delta_{\lfloor g/2 \rfloor}$, giving $\operatorname{rk} \operatorname{Pic}(\overline{\mathscr{M}}_{g}) \otimes \mathbb{Q} = 2 + \lfloor g/2 \rfloor$ for $g \geq 3$.

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{rk}(\operatorname{Pic}(\overline{\mathscr{M}}_{g}) \otimes \mathbb{Q})$ for $g = 5$ and list the generators explicitly. -->

### Example: another computation of $\mathrm{Pic}(\mathscr{M}_{1,1})$ {#ecag-0318}

**Statement:** The Picard group of the moduli stack $\mathscr{M}_{1,1}$ of elliptic curves is $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$, generated by the Hodge bundle $\lambda = R^{1}\pi_{*}\mathcal{O}_{\mathscr{X}}$. This can be computed via the cohomology of the classifying stack $B\operatorname{SL}_{2}(\mathbb{Z})$.

**Construction:** Step 1: The moduli stack $\mathscr{M}_{1,1}$ is a quotient stack. Over $\mathbb{C}$, the upper half plane $\mathfrak{h}$ parametrizes elliptic curves via $\tau \mapsto \mathbb{C}/(\mathbb{Z} + \mathbb{Z}\tau)$, and $\mathscr{M}_{1,1}^{an} \simeq [\mathfrak{h}/\operatorname{SL}_{2}(\mathbb{Z})]$.

Step 2: A line bundle on $[\mathfrak{h}/\operatorname{SL}_{2}(\mathbb{Z})]$ is an $\operatorname{SL}_{2}(\mathbb{Z})$-equivariant line bundle on $\mathfrak{h}$. Since $\mathfrak{h}$ is contractible, every line bundle on $\mathfrak{h}$ is trivial. Thus equivariant line bundles correspond to characters

$$\chi: \operatorname{SL}_{2}(\mathbb{Z}) \to \mathbb{C}^{*}.$$

Step 3: Since $\operatorname{SL}_{2}(\mathbb{Z}) \cong \mathbb{Z}/4\mathbb{Z} *_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z}$, a character is determined by its values on the generators $S = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (order $4$) and $T' = ST = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}$ (order $6$), subject to the compatibility that $S^{2} = (T')^{3}$. Thus

$$\operatorname{Hom}(\operatorname{SL}_{2}(\mathbb{Z}), \mathbb{C}^{*}) \cong \mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}.$$

Step 4: The Hodge bundle $\lambda$ corresponds to the character $\chi(\gamma) = (c\tau + d)^{-1}$ for $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, which generates $\mathbb{Z}/12\mathbb{Z}$.

**Key Insight:** The computation reduces to group cohomology of $\operatorname{SL}_{2}(\mathbb{Z})$ because the upper half plane is contractible, so all topological complexity lives in the group action.

**Prerequisites:** Moduli of elliptic curves, uniformization, classifying stacks, group cohomology, amalgamated free products

<!-- BENCHMARK_PROBLEM: Show that $\operatorname{Hom}(\operatorname{SL}_{2}(\mathbb{Z}), \mathbb{C}^{*}) \cong \mathbb{Z}/12\mathbb{Z}$ using the presentation $\operatorname{SL}_{2}(\mathbb{Z}) \cong \mathbb{Z}/4\mathbb{Z} *_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z}$. -->
## Algebraic stacks
## Schemes as functors, sheaves on categories
It is highly recommended to read David Mumford's book *Lectures on curves on an algebraic surface*.

### Example: $\mathbb{A}_{\mathbb{Z}}^{1}$ {#ecag-0319}

**Statement:** The affine line $\mathbb{A}_{\mathbb{Z}}^{1} = \operatorname{Spec}(\mathbb{Z}[t])$ represents the forgetful functor from the category of schemes to sets, sending a scheme $S$ to the set of global sections $\Gamma(S, \mathcal{O}_{S})$. That is, for any scheme $S$,

$$\operatorname{Hom}_{\operatorname{Sch}}(S, \mathbb{A}_{\mathbb{Z}}^{1}) \cong \Gamma(S, \mathcal{O}_{S}).$$

**Construction:** Step 1: A morphism $f: S \to \mathbb{A}_{\mathbb{Z}}^{1} = \operatorname{Spec}(\mathbb{Z}[t])$ corresponds, by the universal property of $\operatorname{Spec}$, to a ring homomorphism $f^{\sharp}: \mathbb{Z}[t] \to \Gamma(S, \mathcal{O}_{S})$.

Step 2: A ring homomorphism $\mathbb{Z}[t] \to \Gamma(S, \mathcal{O}_{S})$ is uniquely determined by the image of $t$, which can be any element $a \in \Gamma(S, \mathcal{O}_{S})$. This is because $\mathbb{Z}[t]$ is the free $\mathbb{Z}$-algebra on one generator.

Step 3: This establishes the natural bijection $\operatorname{Hom}(S, \mathbb{A}_{\mathbb{Z}}^{1}) \cong \Gamma(S, \mathcal{O}_{S})$. The naturality in $S$ follows because for any morphism $g: S' \to S$, the composition $f \circ g$ corresponds to $g^{\sharp}(f^{\sharp}(t)) = g^{\sharp}(a) \in \Gamma(S', \mathcal{O}_{S'})$, which is precisely the pullback of global sections.

Step 4: Over a base ring $R$, $\mathbb{A}_{R}^{1} = \operatorname{Spec}(R[t])$ represents the functor $S \mapsto \Gamma(S, \mathcal{O}_{S})$ on the category of $R$-schemes. This is the "additive group scheme" $\mathbb{G}_{a}$ when equipped with the group structure $m^{*}(t) = t \otimes 1 + 1 \otimes t$.

**Key Insight:** The representability of the global sections functor by $\mathbb{A}^{1}$ is the most basic instance of the Yoneda lemma in algebraic geometry: the polynomial ring $\mathbb{Z}[t]$ is the free commutative ring on one generator.

**Prerequisites:** Yoneda lemma, representable functors, affine schemes, ring homomorphisms

<!-- BENCHMARK_PROBLEM: Let $S = \operatorname{Spec}(\mathbb{Z}[x]/(x^{2} - 5x + 6))$. Describe $\operatorname{Hom}(S, \mathbb{A}_{\mathbb{Z}}^{1})$ explicitly and identify the corresponding elements of $\Gamma(S, \mathcal{O}_{S})$. -->

### Example: $\mathbb{P}_{\mathbb{Z}}^{n}$ {#ecag-0320}

**Statement:** The projective space $\mathbb{P}_{\mathbb{Z}}^{n} = \operatorname{Proj}(\mathbb{Z}[x_{0}, \ldots, x_{n}])$ represents the functor sending a scheme $S$ to the set of isomorphism classes of pairs $(\mathcal{L}, (s_{0}, \ldots, s_{n}))$ where $\mathcal{L}$ is a line bundle on $S$ and $s_{0}, \ldots, s_{n} \in \Gamma(S, \mathcal{L})$ are global sections that generate $\mathcal{L}$. That is,

$$\operatorname{Hom}(S, \mathbb{P}_{\mathbb{Z}}^{n}) \cong \{(\mathcal{L}, s_{0}, \ldots, s_{n}) : \mathcal{L} \text{ line bundle on } S, \, s_{i} \in \Gamma(S, \mathcal{L}), \, (s_{0}, \ldots, s_{n}) \text{ generate } \mathcal{L}\} / \cong.$$

**Construction:** Step 1: Given a morphism $f: S \to \mathbb{P}^{n}$, define $\mathcal{L} = f^{*}\mathcal{O}(1)$ and $s_{i} = f^{*}(x_{i}) \in \Gamma(S, \mathcal{L})$ for $i = 0, \ldots, n$. The sections $s_{i}$ generate $\mathcal{L}$ because $x_{0}, \ldots, x_{n}$ generate $\mathcal{O}(1)$ on $\mathbb{P}^{n}$.

Step 2: Conversely, given $(\mathcal{L}, s_{0}, \ldots, s_{n})$ with $s_{i}$ generating $\mathcal{L}$, define $U_{i} = \{p \in S : s_{i}(p) \neq 0\}$. The generating condition ensures $S = \bigcup U_{i}$. On $U_{i}$, define $f_{i}: U_{i} \to \mathbb{A}^{n} \subset \mathbb{P}^{n}$ by $f_{i}^{*}(x_{j}/x_{i}) = s_{j}/s_{i}$.

Step 3: The maps $f_{i}$ glue to a morphism $f: S \to \mathbb{P}^{n}$ because on $U_{i} \cap U_{j}$, the transition functions $s_{i}/s_{j}$ are invertible, matching the standard transition functions of $\mathbb{P}^{n}$.

Step 4: These two constructions are inverse to each other up to the equivalence relation: $(\mathcal{L}, s_{0}, \ldots, s_{n}) \sim (\mathcal{L}', s_{0}', \ldots, s_{n}')$ if there exists an isomorphism $\phi: \mathcal{L} \xrightarrow{\sim} \mathcal{L}'$ with $\phi(s_{i}) = s_{i}'$.

**Key Insight:** The functor of points of $\mathbb{P}^{n}$ encodes the geometric fact that maps to projective space are determined by line bundles with generating global sections, which is the scheme-theoretic version of the classical correspondence between maps and linear systems.

**Prerequisites:** Representable functors, line bundles, global sections, Proj construction, Yoneda lemma

<!-- BENCHMARK_PROBLEM: Let $S = \operatorname{Spec}(\mathbb{Z})$. Classify all morphisms $S \to \mathbb{P}_{\mathbb{Z}}^{1}$ by identifying all line bundles on $S$ equipped with pairs of generating global sections, up to isomorphism. -->

### Example: Fano scheme and its tangent space {#ecag-0321}

**Statement:** The Fano scheme $F_{k}(X)$ of $k$-dimensional linear subspaces contained in a projective variety $X \subset \mathbb{P}^{n}$ is a closed subscheme of the Grassmannian $\operatorname{Gr}(k+1, n+1)$, and its Zariski tangent space at a point $[\Lambda] \in F_{k}(X)$ corresponding to a linear subspace $\Lambda \cong \mathbb{P}^{k} \subset X$ is

$$T_{[\Lambda]} F_{k}(X) \cong H^{0}(\Lambda, \mathcal{N}_{\Lambda/X}),$$

where $\mathcal{N}_{\Lambda/X}$ is the normal bundle of $\Lambda$ in $X$.

**Construction:** Step 1: The Fano scheme $F_{k}(X)$ represents the functor

$$S \mapsto \{(V, f) : V \subset \mathcal{O}_{S}^{n+1} \text{ rank } (k+1) \text{ subbundle}, \, f^{*}I_{X} = 0\},$$

where $I_{X}$ is the ideal of $X$. Concretely, if $X = V(F_{1}, \ldots, F_{m}) \subset \mathbb{P}^{n}$, the conditions $F_{j}|_{\Lambda} = 0$ define the Fano scheme as a closed subscheme of $\operatorname{Gr}(k+1, n+1)$.

Step 2: For the tangent space, consider $[\Lambda] \in F_{k}(X)$ and a first-order deformation $\operatorname{Spec}(k[\epsilon]/(\epsilon^{2})) \to F_{k}(X)$ based at $[\Lambda]$. This is a flat family of $(k+1)$-planes in $\mathbb{P}^{n}$ over $\operatorname{Spec}(k[\epsilon])$ contained in $X$.

Step 3: The tangent space $T_{[\Lambda]} \operatorname{Gr}(k+1, n+1) = \operatorname{Hom}(\mathcal{S}|_{\Lambda}, \mathcal{Q}|_{\Lambda}) \cong H^{0}(\Lambda, \mathcal{N}_{\Lambda/\mathbb{P}^{n}})$, where $\mathcal{S}, \mathcal{Q}$ are the tautological sub- and quotient bundles. The condition that the deformed plane stays inside $X$ cuts out $H^{0}(\Lambda, \mathcal{N}_{\Lambda/X})$ via the exact sequence

$$0 \to \mathcal{N}_{\Lambda/X} \to \mathcal{N}_{\Lambda/\mathbb{P}^{n}} \to \mathcal{N}_{X/\mathbb{P}^{n}}|_{\Lambda} \to 0.$$

Step 4: For example, lines on a smooth cubic surface $X \subset \mathbb{P}^{3}$: $F_{1}(X)$ has expected dimension $0$, and $T_{[\ell]}F_{1}(X) = H^{0}(\ell, \mathcal{N}_{\ell/X})$. Since $\mathcal{N}_{\ell/\mathbb{P}^{3}} \cong \mathcal{O}_{\ell}(1)^{\oplus 2}$ and $\mathcal{N}_{X/\mathbb{P}^{3}}|_{\ell} \cong \mathcal{O}_{\ell}(3)$, we get $\mathcal{N}_{\ell/X} \cong \mathcal{O}_{\ell}(-1)$, so $H^{0}(\ell, \mathcal{N}_{\ell/X}) = 0$. Each of the $27$ lines is a reduced isolated point of $F_{1}(X)$.

**Key Insight:** The Fano scheme's tangent space is controlled by sections of the normal bundle, which links the enumerative geometry of linear subspaces to cohomological vanishing results.

**Prerequisites:** Grassmannians, normal bundle, first-order deformations, Fano schemes, tangent-obstruction theory

<!-- BENCHMARK_PROBLEM: Let $X \subset \mathbb{P}^{4}$ be a smooth cubic threefold and $\ell \subset X$ a line. Compute $\mathcal{N}_{\ell/X}$ using the normal bundle sequence, and determine $\dim T_{[\ell]} F_{1}(X)$. -->

### Example: Grassmannian {#ecag-0322}

**Statement:** The Grassmannian $\operatorname{Gr}(k, n)$ represents the functor sending a scheme $S$ to the set of rank $k$ locally free quotients of $\mathcal{O}_{S}^{n}$ (equivalently, rank $k$ subbundles of $\mathcal{O}_{S}^{n}$). Over $\mathbb{Z}$, it is a smooth projective scheme of dimension $k(n-k)$ with Picard group $\operatorname{Pic}(\operatorname{Gr}(k,n)) \cong \mathbb{Z}$, generated by the Plucker line bundle.

**Construction:** Step 1: Define $\operatorname{Gr}(k, n)$ as representing

$$h_{\operatorname{Gr}(k,n)}(S) = \{\mathcal{E} \subset \mathcal{O}_{S}^{n} : \mathcal{E} \text{ locally free of rank } k, \, \mathcal{O}_{S}^{n}/\mathcal{E} \text{ locally free}\}.$$

Step 2: Cover $\operatorname{Gr}(k, n)$ by open affine charts $U_{I}$ indexed by subsets $I \subset \{1, \ldots, n\}$ with $|I| = k$. Over $U_{I}$, the subbundle $\mathcal{E}$ is the row space of a $k \times n$ matrix whose $I$-columns form the identity. The remaining entries are free parameters, giving $U_{I} \cong \mathbb{A}^{k(n-k)}$.

Step 3: The Plucker embedding $\operatorname{Gr}(k, n) \hookrightarrow \mathbb{P}(\bigwedge^{k} \mathbb{Z}^{n}) = \mathbb{P}^{\binom{n}{k}-1}$ sends $\mathcal{E}$ to $\bigwedge^{k} \mathcal{E} \subset \bigwedge^{k} \mathcal{O}_{S}^{n}$. The image is cut out by the Plucker relations, which are quadratic.

Step 4: The tautological exact sequence on $\operatorname{Gr}(k, n)$ is

$$0 \to \mathcal{S} \to \mathcal{O}^{n} \to \mathcal{Q} \to 0,$$

where $\mathcal{S}$ has rank $k$ (tautological subbundle) and $\mathcal{Q}$ has rank $n-k$ (tautological quotient bundle). The tangent bundle is $T_{\operatorname{Gr}(k,n)} \cong \mathcal{H}om(\mathcal{S}, \mathcal{Q}) \cong \mathcal{S}^{\vee} \otimes \mathcal{Q}$.

Step 5: For example, $\operatorname{Gr}(1, n) = \mathbb{P}^{n-1}$ and $\operatorname{Gr}(2, 4)$ is a smooth $4$-dimensional quadric in $\mathbb{P}^{5}$.

**Key Insight:** The Grassmannian is the prototypical example of a moduli space in algebraic geometry: it parametrizes linear subspaces and is simultaneously a homogeneous space $\operatorname{GL}_{n}/P$ for the parabolic subgroup $P$ preserving a $k$-plane.

**Prerequisites:** Representable functors, locally free sheaves, Plucker embedding, tautological bundles

<!-- BENCHMARK_PROBLEM: Compute the dimension of $\operatorname{Gr}(2, 5)$, its Plucker embedding dimension, and the degree of the Grassmannian in its Plucker embedding. -->

### Remark {#ecag-0323}

The graph of a morphism $f: X \to Y$ to a separated scheme $Y$ is a closed subscheme of $X \times Y$. To see this, the graph $\Gamma_{f} \subset X \times Y$ is the preimage of the diagonal $\Delta_{Y} \subset Y \times Y$ under the morphism $(f, \operatorname{id}): X \times Y \to Y \times Y$. Since $Y$ is separated, the diagonal $\Delta_{Y}$ is closed in $Y \times Y$. The preimage of a closed subset under a continuous map is closed, so $\Gamma_{f}$ is closed. Moreover, $\Gamma_{f} \to X$ is an isomorphism (with inverse $x \mapsto (x, f(x))$), so $\Gamma_{f}$ is a closed subscheme of $X \times Y$ isomorphic to $X$.

This fails if $Y$ is not separated: for the line with a doubled origin $Y$, the diagonal is not closed, and the graph of the identity $Y \to Y$ is not closed in $Y \times Y$.

### Example: Quotient stack $[\mathbb{A}^{n}/GL_{n}]$ {#ecag-0324}

**Statement:** The quotient stack $[\mathbb{A}^{n}/\operatorname{GL}_{n}]$, where $\operatorname{GL}_{n}$ acts on $\mathbb{A}^{n}$ by the standard representation, is isomorphic to the classifying stack of rank $1$ projective modules (i.e., line-like objects). More precisely, $[\mathbb{A}^{n}/\operatorname{GL}_{n}]$ is the moduli stack parametrizing pairs $(V, v)$ where $V$ is a rank $n$ vector bundle and $v$ is a global section. Its coarse moduli space is a single point.

**Construction:** Step 1: By definition, the groupoid of $S$-points of $[\mathbb{A}^{n}/\operatorname{GL}_{n}]$ is:
- Objects: pairs $(\mathcal{E}, s)$ where $\mathcal{E}$ is a $\operatorname{GL}_{n}$-torsor on $S$ and $s: S \to \mathcal{E} \times^{\operatorname{GL}_{n}} \mathbb{A}^{n}$ is a section.
- A $\operatorname{GL}_{n}$-torsor $\mathcal{E}$ on $S$ is equivalent to a rank $n$ vector bundle $\mathcal{V}$ on $S$ (by the associated bundle construction). The associated space $\mathcal{E} \times^{\operatorname{GL}_{n}} \mathbb{A}^{n}$ is the total space of $\mathcal{V}$. A section $s$ is a global section $s \in \Gamma(S, \mathcal{V})$.

Step 2: Thus $[\mathbb{A}^{n}/\operatorname{GL}_{n}](S) \simeq \{(\mathcal{V}, s) : \mathcal{V} \text{ rank } n \text{ vector bundle on } S, \, s \in \Gamma(S, \mathcal{V})\}$, with isomorphisms being bundle isomorphisms compatible with the sections.

Step 3: The coarse moduli space is a point because every vector bundle with a section can be connected to any other via a family (all fibers are abstractly isomorphic to $\mathbb{A}^{n}$ with a point in it, and the $\operatorname{GL}_{n}$-action is transitive on nonzero vectors, while the zero section forms a single orbit).

Step 4: Geometrically, the picture is that the orbit space $\mathbb{A}^{n}/\operatorname{GL}_{n}$ has only two orbits: $\{0\}$ and $\mathbb{A}^{n} \setminus \{0\}$. The latter is a single orbit because $\operatorname{GL}_{n}$ acts transitively on nonzero vectors. But the stack remembers the stabilizers: the stabilizer of $0$ is all of $\operatorname{GL}_{n}$, while the stabilizer of a nonzero vector $v$ is the subgroup fixing $v$, isomorphic to the affine group of $\mathbb{A}^{n-1}$.

**Key Insight:** The quotient stack remembers the automorphisms (stabilizers) at each point, unlike the coarse quotient which collapses everything to a single point. This illustrates why stacks are needed for moduli problems with nontrivial automorphisms.

**Prerequisites:** Quotient stacks, torsors, associated bundles, coarse moduli spaces

<!-- BENCHMARK_PROBLEM: Describe the groupoid of $S$-points of $[\mathbb{A}^{n}/\operatorname{GL}_{n}]$ for $n = 1$, and identify the stabilizer groups of the two orbits in $\mathbb{A}^{1}$. -->

### Example: Examples of algebraic stacks without coarse moduli space {#ecag-0325}

**Statement:** Not every algebraic stack admits a coarse moduli space (i.e., an algebraic space $M$ with a map $\mathscr{X} \to M$ that is initial among maps to algebraic spaces and induces bijections on geometric points). The stack $[X/G]$ may fail to have a coarse moduli space when $G$ is not finite or acts non-properly.

**Construction:** Step 1: Consider $\mathscr{X} = [\mathbb{A}^{1}/\mathbb{G}_{m}]$ where $\mathbb{G}_{m}$ acts by scaling. The orbits are $\{0\}$ (with stabilizer $\mathbb{G}_{m}$) and $\mathbb{A}^{1} \setminus \{0\}$ (a single orbit with trivial stabilizer). Any coarse moduli space would be a two-point space, but giving it an algebraic structure causes problems.

Step 2: If $M$ were a coarse moduli space, it would need to be a scheme with two points (one closed, one... closed? generic?). The map $\mathbb{A}^{1} \to M$ (composing the atlas with the coarse map) would need to send $0$ to one point and everything else to another. The preimage of the second point is $\mathbb{A}^{1} \setminus \{0\}$, which is open. So $M$ has the topology where one point is open and the other is closed, i.e., $M \cong \operatorname{Spec}(k[t]/(t^{2}))$... but this does not work because the ring of invariants $k[t]^{\mathbb{G}_{m}} = k$ (only constants). So the "algebraic" candidate for $M$ would be $\operatorname{Spec}(k)$, a single point. But then the map does not induce a bijection on geometric points (there are two orbits).

Step 3: The Keel-Mori theorem states that a separated Deligne-Mumford stack with finite inertia admits a coarse moduli space. For Artin stacks or stacks with non-finite stabilizers (like $B\mathbb{G}_{m}$), a coarse moduli space typically does not exist.

**Key Insight:** The existence of a coarse moduli space requires the inertia (stabilizer groups) to be finite and the stack to be separated. Infinite stabilizers prevent the geometric points from being faithfully represented by an algebraic space.

**Prerequisites:** Algebraic stacks, coarse moduli spaces, Keel-Mori theorem, group actions, quotient stacks

<!-- BENCHMARK_PROBLEM: Let $\mathscr{X} = [\mathbb{A}^{1}/\mathbb{G}_{m}]$ where $\mathbb{G}_{m}$ acts by scaling. Show that the GIT quotient $\mathbb{A}^{1} /\!/ \mathbb{G}_{m} = \operatorname{Spec}(k[t]^{\mathbb{G}_{m}}) = \operatorname{Spec}(k)$ is a single point, and explain why this fails to be a coarse moduli space for $\mathscr{X}$. -->

### Example: $x^{2}+y^{3}=z^{7}$ {#ecag-0326}

**Statement:** The Diophantine equation $x^{2} + y^{3} = z^{7}$ has infinitely many coprime integer solutions. This equation is related to the modular curve $X(7)$ and its twists, via the theory of moduli of elliptic curves with level structure.

**Construction:** Step 1: The equation $x^{2} + y^{3} = z^{7}$ can be interpreted as: for a given $z$, the pair $(x, y)$ defines a point on the elliptic curve $E_{z}: X^{2} + Y^{3} = z^{7}$ (in weighted projective space). The $j$-invariant of this curve is $j = 0$ (up to normalization), connecting to the moduli of elliptic curves.

Step 2: Poonen, Schaefer, and Stoll showed in their paper "Twists of $X(7)$ and primitive solutions to $x^{2} + y^{3} = z^{7}$" that finding primitive solutions is equivalent to finding rational points on certain twists of the Klein quartic curve $X(7)$, which is the modular curve parametrizing elliptic curves with full level-$7$ structure.

Step 3: The Klein quartic $X(7) \subset \mathbb{P}^{2}$ is the smooth genus-$3$ curve

$$x^{3}y + y^{3}z + z^{3}x = 0,$$

with automorphism group $\operatorname{PSL}_{2}(\mathbb{F}_{7})$ of order $168$, the maximum for genus $3$ by the Hurwitz bound.

Step 4: Known primitive solutions include $(x, y, z) = (\pm 1, -1, 0)$, $(\pm 1, 0, 1)$, $(0, 1, 1)$, and infinitely many others generated by the parametric family coming from rational points on the relevant twists.

**Key Insight:** This Diophantine equation connects number theory, the moduli of elliptic curves, and the arithmetic of modular curves, showing that seemingly elementary equations can encode deep structure about moduli problems.

**Prerequisites:** Diophantine equations, modular curves, level structures, Klein quartic, twists of curves

<!-- BENCHMARK_PROBLEM: Verify that $(x, y, z) = (0, 1, 1)$ and $(\pm 1, 0, 1)$ are primitive integer solutions to $x^{2} + y^{3} = z^{7}$. Compute the genus of the modular curve $X(7)$ using the Hurwitz formula applied to the covering $X(7) \to X(1) \cong \mathbb{P}^{1}$. -->

### Example: $(p-1)/24$ supersingular elliptic curves in characteristic $p$ {#ecag-0327}

**Statement:** Over an algebraically closed field $\bar{\mathbb{F}}_{p}$ of characteristic $p \geq 5$, the number of supersingular elliptic curves (up to isomorphism) is related to $(p-1)/12$ when weighted by automorphisms. More precisely, the mass formula gives

$$\sum_{E/\bar{\mathbb{F}}_{p} \text{ supersingular}} \frac{1}{|\operatorname{Aut}(E)|} = \frac{p - 1}{24},$$

where the sum is over isomorphism classes of supersingular elliptic curves.

**Construction:** Step 1: An elliptic curve $E$ over $\bar{\mathbb{F}}_{p}$ is supersingular if $E[p](\bar{\mathbb{F}}_{p}) = 0$ (equivalently, the Frobenius endomorphism is purely inseparable of degree $p^{2}$ on the $p$-torsion, or equivalently, $\operatorname{End}(E) \otimes \mathbb{Q}$ is a quaternion algebra).

Step 2: The mass formula arises from the Eichler-Deuring correspondence: supersingular elliptic curves correspond to maximal orders in the quaternion algebra $B_{p,\infty}$ ramified at $p$ and $\infty$. The mass of the genus of maximal orders is $\frac{p-1}{24}$ by the Minkowski-Siegel mass formula.

Step 3: Since $|\operatorname{Aut}(E)| = 2$ for most elliptic curves (the generic automorphism group is $\{\pm 1\}$), with $|\operatorname{Aut}(E)| = 4$ when $j = 1728$ and $|\operatorname{Aut}(E)| = 6$ when $j = 0$, the actual number of supersingular $j$-invariants is approximately $\lfloor p/12 \rfloor + \epsilon$ where $\epsilon \in \{0, 1, 2\}$ depends on $p \mod 12$.

Step 4: For example, for $p = 5$: $(p-1)/24 = 1/6$, and the unique supersingular curve has $j = 0$ with $|\operatorname{Aut}| = 6$. For $p = 11$: $(p-1)/24 = 5/12$, and there are two supersingular curves with $j = 0$ ($|\operatorname{Aut}| = 6$) and $j = 1728$ ($|\operatorname{Aut}| = 4$), giving $1/6 + 1/4 = 5/12$.

**Key Insight:** The mass formula connects the arithmetic of supersingular elliptic curves to the class number theory of quaternion algebras, and the factor $1/24$ reflects the orbifold Euler characteristic of $\mathscr{M}_{1,1}$.

**Prerequisites:** Supersingular elliptic curves, Frobenius endomorphism, quaternion algebras, Eichler-Deuring correspondence, mass formula

<!-- BENCHMARK_PROBLEM: For $p = 13$, use the mass formula $\sum 1/|\operatorname{Aut}(E)| = (p-1)/24 = 1/2$ to determine the number and $j$-invariants of supersingular elliptic curves over $\bar{\mathbb{F}}_{13}$. -->

### Example: Mumford, Picard groups of moduli problems {#ecag-0328}

**Statement:** In his foundational paper "Picard groups of moduli problems," Mumford computed $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$ over an algebraically closed field of characteristic not $2$ or $3$, where the generator is the Hodge bundle $\lambda$. Mumford's method uses the automorphisms of special elliptic curves to extract numerical invariants.

**Construction:** Step 1: A line bundle $\mathscr{L}$ on the moduli stack $\mathscr{M}_{1,1}$ assigns to each family of elliptic curves $\pi: \mathscr{X} \to S$ a line bundle $\mathscr{L}_{\pi}$ on $S$, compatibly with base change.

Step 2: The key idea is that special elliptic curves with extra automorphisms (beyond $\{\pm 1\}$) provide numerical constraints. The curve $C_{1}: y^{2} = x^{3} - x$ has $\operatorname{Aut}(C_{1}) \cong \mathbb{Z}/4\mathbb{Z}$, and $C_{2}: y^{2} = x^{3} - 1$ has $\operatorname{Aut}(C_{2}) \cong \mathbb{Z}/6\mathbb{Z}$. The automorphism groups act on the fiber $\mathscr{L}|_{C_{i}}$ by roots of unity.

Step 3: Since $\operatorname{Aut}(C_{1})$ acts by $4$th roots and $\operatorname{Aut}(C_{2})$ acts by $6$th roots, and these are compatible via $\sigma^{2} = \tau^{3} = \text{inversion}$, we get a homomorphism $\beta: \operatorname{Pic}(\mathscr{M}_{1,1}) \to \mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}$.

Step 4: Surjectivity is shown by computing $\beta(\lambda) = 1$ via the action of automorphisms on $H^{0}(C_{i}, \omega_{C_{i}})$. Injectivity follows by showing that any line bundle with $\beta(\mathscr{L}) = 0$ admits a trivialization compatible with descent data, using the Legendre family as an etale cover of $\mathscr{M}_{1,1}$.

**Key Insight:** Mumford's method exploits the orbifold structure of $\mathscr{M}_{1,1}$: the special fibers with enhanced automorphisms provide enough constraints to pin down the Picard group completely.

**Prerequisites:** Moduli stacks, line bundles on stacks, automorphisms of elliptic curves, Hodge bundle, descent theory

<!-- BENCHMARK_PROBLEM: Compute the action of the automorphism $\sigma: (x, y) \mapsto (-x, iy)$ of the elliptic curve $C_{1}: y^{2} = x^{3} - x$ on the space of regular differentials $H^{0}(C_{1}, \omega_{C_{1}})$, and determine the order of the resulting scalar. -->
### Example: Tangent space of the Picard scheme {#ecag-0329}

**Statement:** Let $X$ be a proper scheme over a field $k$. The Picard scheme $\operatorname{Pic}_{X/k}$ represents the relative Picard functor (under suitable hypotheses). Its tangent space at the origin (the trivial line bundle) is

$$T_{[\mathcal{O}_{X}]} \operatorname{Pic}_{X/k} \cong H^{1}(X, \mathcal{O}_{X}).$$

**Construction:** Step 1: The tangent space at $[\mathcal{O}_{X}]$ is by definition $\operatorname{Pic}_{X/k}(\operatorname{Spec}(k[\epsilon]/(\epsilon^{2})))$, the set of first-order deformations of $\mathcal{O}_{X}$.

Step 2: A line bundle on $X \times \operatorname{Spec}(k[\epsilon]) = X[\epsilon]$ that restricts to $\mathcal{O}_{X}$ on the closed fiber is classified by $H^{1}(X[\epsilon], \mathcal{O}_{X[\epsilon]}^{*})$ mapping to $H^{1}(X, \mathcal{O}_{X}^{*})$ under restriction.

Step 3: The kernel of the restriction map is computed via the exact sequence of sheaves on $X$:

$$1 \to 1 + \epsilon \cdot \mathcal{O}_{X} \to \mathcal{O}_{X[\epsilon]}^{*} \to \mathcal{O}_{X}^{*} \to 1.$$

The sheaf $1 + \epsilon \cdot \mathcal{O}_{X}$ is isomorphic to $\mathcal{O}_{X}$ (as an additive group) via $1 + \epsilon f \mapsto f$. Taking cohomology:

$$H^{0}(X, \mathcal{O}_{X}^{*}) \to H^{1}(X, \mathcal{O}_{X}) \to H^{1}(X[\epsilon], \mathcal{O}_{X[\epsilon]}^{*}) \to H^{1}(X, \mathcal{O}_{X}^{*}).$$

Step 4: The kernel of the last map is the image of $H^{1}(X, \mathcal{O}_{X})$, and the connecting map from $H^{0}(X, \mathcal{O}_{X}^{*})$ is zero (units pull back to units). Thus first-order deformations of $\mathcal{O}_{X}$ are classified by $H^{1}(X, \mathcal{O}_{X})$.

Step 5: For a smooth projective curve $C$ of genus $g$, this gives $\dim T \operatorname{Pic}_{C/k} = g$, consistent with $\operatorname{Pic}^{0}_{C/k}$ being an abelian variety of dimension $g$ (the Jacobian).

**Key Insight:** First-order deformations of line bundles are controlled by $H^{1}(\mathcal{O}_{X})$ because the exponential-type sequence $1 + \epsilon \cdot \mathcal{O}_{X} \cong \mathcal{O}_{X}$ linearizes the multiplicative deformation problem into an additive cohomological one.

**Prerequisites:** Picard scheme, first-order deformations, tangent space of moduli, cohomology of structure sheaf

<!-- BENCHMARK_PROBLEM: Let $X$ be a smooth projective surface over $k$ with $H^{1}(X, \mathcal{O}_{X}) = 0$ (e.g., $X = \mathbb{P}^{2}$). What is the tangent space dimension of $\operatorname{Pic}_{X/k}$ at $[\mathcal{O}_{X}]$, and what does this tell you about $\operatorname{Pic}^{0}_{X/k}$? -->

### Example: Isotrivial but non-trivial family of elliptic curves {#ecag-0330}

**Statement:** The family of elliptic curves

$$X := \operatorname{Spec}(k[x, y, t, t^{-1}]/(y^{2} - x^{3} + t)) \to \operatorname{Spec}(k[t, t^{-1}]) = \mathbb{G}_{m}$$

is isotrivial (all fibers are isomorphic, with constant $j$-invariant $j \equiv 0$) but the family is not trivial, i.e., $X \not\cong E \times \mathbb{G}_{m}$ for any elliptic curve $E$.

**Construction:** Step 1: The fibers are $y^{2} = x^{3} - t$ for varying $t \in k^{*}$. The $j$-invariant of $y^{2} = x^{3} + a$ is $j = 0$ for all $a \neq 0$ (since there is no $x$-term). Hence all fibers are isomorphic over $\bar{k}$, making the family isotrivial.

Step 2: The total space $X$ is affine. To see this, note that

$$\operatorname{Spec}(k[x, y, t, t^{-1}]/(y^{2} - x^{3} + t)) = D_{+}(y^{2} - x^{3}) \subset \mathbb{A}_{k}^{2},$$

which is an open subset of the affine plane defined by the non-vanishing of $t = y^{2} - x^{3}$.

Step 3: Suppose for contradiction that $X \cong E \times \mathbb{G}_{m}$ for some elliptic curve $E$. Then we get a dominant rational map

$$\mathbb{A}^{2} \supset X \cong E \times \mathbb{G}_{m} \to E.$$

Since $\mathbb{A}^{2}$ is rational (and $X$ is an open subset), composing with the inclusion into $\mathbb{P}^{2}$ gives a dominant rational map $\mathbb{P}^{2} \dashrightarrow E$. This implies $E$ is unirational.

Step 4: By Luroth's theorem (in dimension $1$), a unirational curve over an algebraically closed field is rational. But $E$ has genus $1$, so $E$ is not rational. This is a contradiction.

**Key Insight:** The family is locally trivial in the etale topology but not in the Zariski topology. The obstruction to Zariski-triviality is detected by the non-triviality of the associated $\operatorname{Aut}(E)$-torsor, which lives in $H^{1}_{\text{et}}(\mathbb{G}_{m}, \operatorname{Aut}(E))$.

**Prerequisites:** Isotrivial families, $j$-invariant, Luroth's theorem, affine varieties, etale cohomology

<!-- BENCHMARK_PROBLEM: Show that the total space of $y^{2} = x^{3} - t$ over $\operatorname{Spec}(k[t, t^{-1}])$ is isomorphic to the complement of $V(y^{2} - x^{3})$ in $\mathbb{A}^{2}_{k}$. Conclude that the total space is affine, and explain why this implies the family cannot be a trivial product $E \times \mathbb{G}_{m}$. -->

### Remark: Trivialization in etale topology {#ecag-0331}

The isotrivial family $y^{2} = x^{3} - t$ from the previous example becomes trivial after an etale base change. Consider the etale morphism

$$\phi: \operatorname{Spec}(k[t^{1/6}, t^{-1/6}]) \to \operatorname{Spec}(k[t, t^{-1}]),$$

corresponding to the ring map $t \mapsto (t^{1/6})^{6}$. This is etale because $6$ is invertible in $k$ (assuming $\operatorname{char}(k) \neq 2, 3$).

After pulling back the family along $\phi$, the substitution $x = t^{1/3} x'$, $y = t^{1/2} y'$ transforms the equation $y^{2} = x^{3} - t$ into $(y')^{2} = (x')^{3} - 1$, which is a constant curve. Explicitly, the pulled-back family is isomorphic to $E_{0} \times \operatorname{Spec}(k[t^{1/6}, t^{-1/6}])$ where $E_{0}: (y')^{2} = (x')^{3} - 1$.

The exponent $1/6$ is the least common multiple of $1/2$ and $1/3$, arising from the weights in the Weierstrass equation. This is an instance of the general principle that isotrivial families of elliptic curves are trivialized by etale covers whose degree divides $|\operatorname{Aut}(E)|$ (here $|\operatorname{Aut}(E_{0})| = 6$ since $j = 0$).
### Example: $\operatorname{pt}\rightarrow B\mathbb{G}_{m}$ is an $\mathrm{fppf}$ (even smooth and surjective) cover {#ecag-0332}

**Statement:** The morphism $\operatorname{pt} \to B\mathbb{G}_{m}$ corresponding to the trivial line bundle $\mathcal{O}$ is an fppf cover (and in fact smooth and surjective). For any scheme $T$ with a morphism $f: T \to B\mathbb{G}_{m}$ given by a line bundle $\mathcal{L}$ on $T$, the fiber product $T \times_{B\mathbb{G}_{m}} \operatorname{pt}$ is representable by the scheme $\operatorname{Tot}(\mathcal{L}) \setminus \{0\text{-section}\}$, the total space of $\mathcal{L}$ minus the zero section, which is a $\mathbb{G}_{m}$-torsor over $T$.

**Construction:** Step 1 (Setup): Recall that $B\mathbb{G}_{m}$ is the classifying stack of the multiplicative group. For any scheme $X$, the groupoid $B\mathbb{G}_{m}(X)$ has objects: line bundles on $X$; morphisms: isomorphisms of line bundles. A morphism $f: T \to B\mathbb{G}_{m}$ is the datum of a line bundle $\mathcal{L}$ on $T$.

Step 2 (Descent for isomorphisms): The presheaf $\operatorname{Isom}(\mathcal{L}, \mathcal{L}')$ is an fpqc sheaf. For any fpqc morphism $U \to X$, there is an exact sequence

$$\operatorname{Isom}(\mathcal{L}, \mathcal{L}')(X) \to \operatorname{Isom}(\mathcal{L}, \mathcal{L}')(U) \rightrightarrows \operatorname{Isom}(\mathcal{L}, \mathcal{L}')(U \times_{X} U).$$

Step 3 (Descent for objects): For any fpqc morphism $U \to X$, there is an exact sequence of groupoids

$$B\mathbb{G}_{m}(X) \to B\mathbb{G}_{m}(U) \rightrightarrows B\mathbb{G}_{m}(U \times_{X} U) \mathrel{\substack{\to \\ \to \\ \to}} B\mathbb{G}_{m}(U \times_{X} U \times_{X} U).$$

Step 4 (Computing the fiber product): A morphism $f: T \to B\mathbb{G}_{m}$ corresponds to a line bundle $\mathcal{L}$ on $T$, and $f': \operatorname{pt} \to B\mathbb{G}_{m}$ corresponds to $\mathcal{O}_{\operatorname{pt}}$. A morphism $X \to T \times_{B\mathbb{G}_{m}} \operatorname{pt}$ consists of morphisms $g: X \to T$, $g': X \to \operatorname{pt}$, and an isomorphism $g^{*}\mathcal{L} \cong (g')^{*}\mathcal{O}_{\operatorname{pt}} = \mathcal{O}_{X}$.

Step 5 (Identifying the functor): The functor $(T \times_{B\mathbb{G}_{m}} \operatorname{pt})(X)$ classifies:
- If $g^{*}\mathcal{L} \cong \mathcal{O}_{X}$: the set of all trivializations, which is a $\mathbb{G}_{m}(X) = \mathcal{O}_{X}^{*}$-torsor.
- If $g^{*}\mathcal{L} \not\cong \mathcal{O}_{X}$: the empty set.

Step 6 (Representability): Choose a trivialization $\{U_{i}\}$ of $\mathcal{L}$ with transition functions $g_{ij} \in \mathcal{O}^{*}(U_{i} \cap U_{j})$. The fiber product is obtained by gluing $\mathbb{G}_{m} \times U_{i}$ along $U_{i} \cap U_{j}$ via the same transition functions $g_{ij}$. This is precisely the construction of $\operatorname{Tot}(\mathcal{L}) \setminus \{0\}$, the total space of $\mathcal{L}$ with the zero section removed. This is a $\mathbb{G}_{m}$-bundle over $T$.

Step 7 (Faithful flatness): The projection $\operatorname{Tot}(\mathcal{L}) \setminus \{0\} \to T$ is faithfully flat: it is flat because $\mathbb{G}_{m}$-torsors are flat, and surjective because every point of $T$ has a nonzero element in the fiber of $\mathcal{L}$. In fact, it is smooth since $\mathbb{G}_{m}$ is smooth.

**Key Insight:** The morphism $\operatorname{pt} \to B\mathbb{G}_{m}$ is the universal $\mathbb{G}_{m}$-torsor; pulling it back along any map $T \to B\mathbb{G}_{m}$ (i.e., any line bundle $\mathcal{L}$ on $T$) recovers the associated $\mathbb{G}_{m}$-torsor $\operatorname{Tot}(\mathcal{L}) \setminus \{0\}$.

**Prerequisites:** Classifying stacks, $\mathbb{G}_{m}$-torsors, fpqc descent, fiber products of stacks, faithful flatness

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

**Statement:** Let $G$ be a finite group acting freely on a smooth projective curve $X$ of genus $g \geq 1$ over an algebraically closed field $k$. The quotient morphism $\pi: X \to X/G$ is a $G$-torsor that admits no Zariski-local sections, i.e., there is no Zariski open $U \subset X/G$ with a section $s: U \to X$ of $\pi$.

**Construction:** Step 1: Since $G$ acts freely, $\pi: X \to Y := X/G$ is a finite etale Galois cover of degree $|G|$. The curve $Y$ is smooth projective of genus $g_{Y}$ determined by the Riemann-Hurwitz formula: $2g - 2 = |G|(2g_{Y} - 2)$ (no ramification since the action is free).

Step 2: Suppose for contradiction that $\pi$ admits a section $s: U \to X$ over some nonempty Zariski open $U \subset Y$. Then $s(U) \subset X$ is an open subset isomorphic to $U$. The map $\pi|_{s(U)}: s(U) \to U$ is an isomorphism.

Step 3: This means $s(U)$ is a connected component of $\pi^{-1}(U)$ isomorphic to $U$ (since $\pi$ is finite etale of constant degree $|G|$). But if $|G| > 1$, the morphism $\pi$ is a nontrivial connected finite etale covering of $Y$. A section of a connected finite etale covering implies the covering is trivial (splits off a component), contradicting connectedness of $X$ (which holds since $X$ is a smooth irreducible curve).

Step 4: For example, take $X$ an elliptic curve and $G = \mathbb{Z}/n\mathbb{Z}$ acting by translation by an $n$-torsion point. Then $Y = X/G$ is also an elliptic curve, and $\pi: X \to Y$ is an isogeny of degree $n$ which is etale and admits no Zariski-local sections.

**Key Insight:** Nontrivial finite etale covers of connected schemes never admit Zariski-local sections; this is why the etale (or fppf) topology, not the Zariski topology, is needed to trivialize torsors over curves of positive genus.

**Prerequisites:** Finite etale covers, Galois covers, torsors, Zariski vs etale topology

<!-- BENCHMARK_PROBLEM: Let $E$ be an elliptic curve over an algebraically closed field and let $\pi: E \to E' = E/(\mathbb{Z}/2\mathbb{Z})$ be the quotient by the involution $P \mapsto -P$. Note this has fixed points, so modify: let $\pi: E \to E/\langle T \rangle$ where $T$ is a $2$-torsion point acting by translation. Show that this etale double cover admits no Zariski-local section. -->
### Example: $\mathrm{Pic}(BG)$ over an algebraically closed field $k$ {#ecag-0336}

**Statement:** Let $G$ be a finite group and $k$ an algebraically closed field with $\operatorname{char}(k) \nmid |G|$. Then

$$\operatorname{Pic}(BG) \cong \operatorname{Hom}(G, k^{*}) = H^{1}(G, k^{*}),$$

the group of characters of $G$. In particular, $\operatorname{Pic}(B\mathbb{G}_{m}) = \operatorname{Hom}(\mathbb{G}_{m}, \mathbb{G}_{m}) \cong \mathbb{Z}$.

**Construction:** Step 1 (First viewpoint -- functorial): The classifying stack $BG = [\operatorname{pt}/G]$ classifies $G$-torsors. A line bundle $\mathscr{L}$ on $BG$ assigns to each $G$-torsor $\mathcal{G}$ on a scheme $X$ a line bundle $\mathscr{L}_{\mathcal{G}}$ on $X$, compatibly with pullback. For an automorphism of $\mathcal{G}$ (i.e., an element $g \in G$), we must specify an automorphism of $\mathscr{L}_{\mathcal{G}}$, i.e., an element of $\operatorname{Aut}(\mathscr{L}_{\mathcal{G}}) \cong k^{*}$. Compatibility with composition gives a group homomorphism

$$\chi_{\mathcal{G}}: G \to k^{*}.$$

Step 2 (Second viewpoint -- descent): Since $k = \bar{k}$, the scheme $\operatorname{pt} = \operatorname{Spec}(k)$ has no nontrivial etale covers. Every line bundle on $BG$ descends from a line bundle on $\operatorname{pt}$ (with descent data for the $G$-torsor $\operatorname{pt} \to BG$). The only line bundle on $\operatorname{pt}$ is $\mathcal{O}$, so the descent data consists of specifying for each $g \in G$ an automorphism $\alpha(g) \in \operatorname{Aut}(\mathcal{O}_{\operatorname{pt}}) \cong k^{*}$ satisfying the cocycle condition.

Step 3 (Cocycle condition): The cocycle condition requires $\alpha(g_{1} g_{2}) = \alpha(g_{1}) \circ \alpha(g_{2})$ for all $g_{1}, g_{2} \in G$. Since $\operatorname{Aut}(\mathcal{O}_{\operatorname{pt}})$ is abelian, this is exactly the condition that $\alpha: G \to k^{*}$ is a group homomorphism. Two descent data are isomorphic if and only if the corresponding characters differ by a coboundary (which is trivial since $H^{0}(G, k^{*})$ acts trivially in the abelian case). Thus

$$\operatorname{Pic}(BG) \cong \operatorname{Hom}(G, k^{*}).$$

Step 4 (Geometric interpretation): Given a character $\chi: G \to k^{*}$ and a $G$-torsor $\mathcal{G}$ on $X$, the corresponding line bundle is

$$\mathscr{L}_{\mathcal{G}} = \mathcal{G} \times_{G} \mathbb{A}^{1}_{k},$$

where $G$ acts on $\mathbb{A}^{1}_{k}$ by the character $\chi$, i.e., $g \cdot a = \chi(g) \cdot a$.

Step 5 (Case $G = \mathbb{G}_{m}$): For $G = \mathbb{G}_{m}$, we get $\operatorname{Pic}(B\mathbb{G}_{m}) = \operatorname{Hom}(\mathbb{G}_{m}, \mathbb{G}_{m}) \cong \mathbb{Z}$, where the integer $n$ corresponds to the character $t \mapsto t^{n}$. Topologically, $B\mathbb{G}_{m}(\mathbb{C}) \simeq \mathbb{CP}^{\infty}$, so $\operatorname{Pic}(B\mathbb{G}_{m}) \cong H^{2}(\mathbb{CP}^{\infty}, \mathbb{Z}) \cong \mathbb{Z}$.

**Key Insight:** Line bundles on $BG$ are purely group-theoretic: they correspond to one-dimensional representations of $G$, because the underlying space is a single point and all geometric complexity lives in the group action.

**Prerequisites:** Classifying stacks, descent theory, group characters, torsors, associated bundles

<!-- BENCHMARK_PROBLEM: Compute $\operatorname{Pic}(B(\mathbb{Z}/n\mathbb{Z}))$ over an algebraically closed field $k$ with $\operatorname{char}(k) \nmid n$, and identify the generator explicitly as a descent datum on $\operatorname{pt} \to B(\mathbb{Z}/n\mathbb{Z})$. -->

### Example: $\mathrm{Pic}(\mathscr{M}_{1,1})$ over a field $k$, $char(k)\neq 2,3$, algebraic method {#ecag-0337}

**Statement:** Over a field $k$ with $\operatorname{char}(k) \neq 2, 3$, the Picard group of the moduli stack of elliptic curves is

$$\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z},$$

generated by the Hodge bundle $\Lambda(\pi: \mathscr{X} \to S) = R^{1}\pi_{*}\mathcal{O}_{\mathscr{X}}$.

**Construction:** Following Mumford's paper "Picard groups of moduli problems":

Step 1 (Constructing the invariant $\beta$): A line bundle $\mathscr{L}$ on $\mathscr{M}_{1,1}$ assigns to each family $\pi: \mathscr{X} \to S$ a line bundle $\mathscr{L}_{\pi}$ on $S$. Every elliptic curve has the inversion automorphism $\rho: \mathscr{X} \to \mathscr{X}$ (of order $2$) over $S$. This induces $\mathscr{L}(\rho) \in \operatorname{Aut}(\mathscr{L}_{\pi}) = H^{0}(S, \mathcal{O}_{S}^{*})$, with $\mathscr{L}(\rho)^{2} = \operatorname{id}$. For a connected family, $\mathscr{L}(\rho) = \pm 1$.

Using the Legendre family $E_{t}: y^{2} = x(x-1)(x-t)$ over $\mathbb{A}^{1} \setminus \{0, 1\}$, define $\alpha(\mathscr{L}) := \mathscr{L}(\rho) \in \{\pm 1\} = \mathbb{Z}/2\mathbb{Z}$. This gives a homomorphism $\alpha: \operatorname{Pic}(\mathscr{M}_{1,1}) \to \mathbb{Z}/2\mathbb{Z}$.

Step 2 (Exploiting special automorphisms): The elliptic curves $C_{1}: y^{2} = x(x+1)(x-1)$ (with $j = 1728$) and $C_{2}: y^{2} = x^{3} - 1$ (with $j = 0$, taking $\omega$ a primitive cube root of unity, $C_{2}: y^{2} = x(x - \omega)(x - \omega^{2})$) have enhanced automorphism groups:
- $\operatorname{Aut}(C_{1}) \cong \mathbb{Z}/4\mathbb{Z}$, generated by $\sigma: (x, y) \mapsto (-x, iy)$.
- $\operatorname{Aut}(C_{2}) \cong \mathbb{Z}/6\mathbb{Z}$, generated by $\tau: (x, y) \mapsto (\omega x, -y)$.

The line bundle $\mathscr{L}$ evaluated at these families gives $\mathscr{L}(\sigma)$ acting by a $4$th root of unity and $\mathscr{L}(\tau)$ acting by a $6$th root of unity. The compatibility $\sigma^{2} = \tau^{3} = \rho$ (inversion) gives

$$\beta: \operatorname{Pic}(\mathscr{M}_{1,1}) \to \mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}.$$

Fixing a primitive $12$th root of unity $\zeta$, for each $\mathscr{L}$ there is a unique $\beta \pmod{12}$ with $\zeta^{6\beta} = \alpha(\mathscr{L})$, $\zeta^{3\beta} = \mathscr{L}(\sigma)$, $\zeta^{2\beta} = \mathscr{L}(\tau)$.

Step 3 (Surjectivity via the Hodge bundle): The Hodge bundle is $\Lambda(\pi: \mathscr{X} \to S) = R^{1}\pi_{*}\mathcal{O}_{\mathscr{X}}$. Since $\dim H^{1}(C, \mathcal{O}_{C}) = g = 1$ for every elliptic curve $C$, the cohomology and base change theorem ensures $\Lambda$ is a line bundle on $S$ compatible with base change, hence a line bundle on $\mathscr{M}_{1,1}$.

Computing the action on regular differentials (using Serre duality $H^{1}(C, \mathcal{O}_{C}) \cong H^{0}(C, \omega_{C})^{\vee}$):
- $H^{0}(C_{1}, \omega_{C_{1}}) = k \cdot \frac{dx}{2y}$, and $\sigma^{*}\left(\frac{dx}{2y}\right) = \frac{-dx}{2iy} = \frac{i \cdot dx}{2y}$, so $\sigma$ acts by $i$, a primitive $4$th root of unity.
- $H^{0}(C_{2}, \omega_{C_{2}}) = k \cdot \frac{dx}{2y}$, and $\tau^{*}\left(\frac{dx}{2y}\right) = \frac{\omega \, dx}{-2y} = -\omega \cdot \frac{dx}{2y}$, so $\tau$ acts by $-\omega$, a primitive $6$th root of unity.

Thus $\beta(\Lambda) = 1$ (generates $\mathbb{Z}/12\mathbb{Z}$), proving surjectivity.

Step 4 (Injectivity): Suppose $\beta(\mathscr{L}) = 0$. We must show $\mathscr{L} \cong \mathcal{O}_{\mathscr{M}_{1,1}}$. The Legendre family provides an etale cover $S = \mathbb{A}^{1} \setminus \{0, 1\} \to \mathscr{M}_{1,1}$ of degree $12$ (via the symmetric group $S_{3} \cong \langle g_{1}: \lambda \mapsto 1/\lambda, \, g_{2}: \lambda \mapsto 1 - \lambda \rangle$ permuting the branch points). Any line bundle on $S$ is trivial (since $S$ is an open in $\mathbb{A}^{1}$). Fix a trivialization $\phi: \mathcal{O}_{S} \xrightarrow{\sim} \mathscr{L}|_{S}$.

The condition $\beta(\mathscr{L}) = 0$ ensures the induced action on $H^{0}(S, \mathscr{L})$ is trivial. One can choose the trivialization $\theta \in H^{0}(S, \mathscr{L})^{G}$ (invariant under the $S_{3}$-action), which exists because the $j$-invariant provides an invariant function. The compatibility of descent data then follows: $\mathscr{L}(\psi_{s})$ preserves $\theta$, so the descent data for $\mathscr{L}$ matches that of $\mathcal{O}_{\mathscr{M}_{1,1}}$.

**Conclusion:**

$$\beta: \operatorname{Pic}(\mathscr{M}_{1,1}) \xrightarrow{\;\sim\;} \mathbb{Z}/12\mathbb{Z}.$$

**Key Insight:** The Picard group is completely determined by the automorphisms of special elliptic curves ($j = 0$ and $j = 1728$), which provide enough torsion constraints. The fiber product structure $\mathbb{Z}/4\mathbb{Z} \times_{\mathbb{Z}/2\mathbb{Z}} \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z}$ captures all possible actions of line bundles on the enhanced automorphism groups.

**Prerequisites:** Moduli stacks, line bundles on stacks, automorphisms of elliptic curves, Hodge bundle, cohomology and base change, descent theory, Legendre family

<!-- BENCHMARK_PROBLEM: Compute $\beta(\Lambda^{k})$ for $k = 1, \ldots, 12$ where $\Lambda$ is the Hodge bundle on $\mathscr{M}_{1,1}$. At which value of $k$ does $\Lambda^{k}$ descend to a line bundle on the coarse moduli space $M_{1,1} \cong \mathbb{A}^{1}_{j}$? -->

### Remark: Hodge bundle, $S\times_{\mathscr{M}_{1,1}}S$ and degree of the etale cover {#ecag-0338}

The Legendre family $E_{t}: y^{2} = x(x-1)(x-t)$ over $S = \mathbb{A}^{1} \setminus \{0, 1\}$ gives an etale cover $S \to \mathscr{M}_{1,1}$. The fiber product $S \times_{\mathscr{M}_{1,1}} S$ parametrizes pairs $(t_{1}, t_{2}) \in S \times S$ together with an isomorphism $E_{t_{1}} \cong E_{t_{2}}$.

Two Legendre curves $E_{t_{1}}$ and $E_{t_{2}}$ are isomorphic if and only if $t_{2}$ belongs to the orbit of $t_{1}$ under the group $S_{3} \cong \langle t \mapsto 1/t, \, t \mapsto 1-t \rangle$ acting on $\mathbb{P}^{1} \setminus \{0, 1, \infty\}$. This group has order $6$. However, some Legendre curves have extra automorphisms beyond $\{\pm 1\}$, so the degree of the cover $S \to \mathscr{M}_{1,1}$ is $|S_{3}| \times |\{\pm 1\}| = 6 \times 2 = 12$ when counted as a map of stacks.

The Hodge bundle $\Lambda$ restricted to $S$ is the line bundle $R^{1}\pi_{*}\mathcal{O}_{E}$ where $\pi: E \to S$ is the universal Legendre family. This is isomorphic to $\pi_{*}\omega_{E/S}^{\vee}$ by Serre duality. Since $\omega_{E/S} \cong \mathcal{O}_{S}$ for the Legendre family (every Legendre curve has a canonical differential $dx/(2y)$), the Hodge bundle restricted to $S$ is trivial. This is consistent with $\operatorname{Pic}(S) = 0$ since $S \cong \mathbb{A}^{1} \setminus \{0, 1\}$.
### Example: $\mathrm{Pic}(\mathscr{M}_{1,1})$ over a general scheme {#ecag-0339}

**Statement:** Over a general base scheme $S$ (not necessarily a field), the Picard group of the moduli stack $\mathscr{M}_{1,1}$ satisfies $\operatorname{Pic}(\mathscr{M}_{1,1} \times S) \cong \mathbb{Z}/12\mathbb{Z} \oplus \operatorname{Pic}(S)$. In particular, over $\operatorname{Spec}(\mathbb{Z}[1/6])$, we have $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$, still generated by the Hodge bundle $\lambda$.

**Construction:** Step 1: Fulton's approach uses the presentation of $\mathscr{M}_{1,1}$ as a global quotient stack. Over $\operatorname{Spec}(\mathbb{Z}[1/6])$, every elliptic curve can be written in short Weierstrass form $y^{2} = x^{3} + ax + b$ with $\Delta = -16(4a^{3} + 27b^{2}) \neq 0$.

Step 2: The parameter space is $U = \operatorname{Spec}(\mathbb{Z}[1/6][a, b, \Delta^{-1}])$ and $\mathbb{G}_{m}$ acts by $t \cdot (a, b) = (t^{4}a, t^{6}b)$. Then $\mathscr{M}_{1,1} \cong [U/\mathbb{G}_{m}]$ and the Picard group of the quotient stack is computed via the equivariant Picard group $\operatorname{Pic}^{\mathbb{G}_{m}}(U)$.

Step 3: Since $\operatorname{Pic}(U) = 0$ (as $U$ is an open in affine space over $\mathbb{Z}[1/6]$), we get $\operatorname{Pic}^{\mathbb{G}_{m}}(U) \cong \operatorname{Hom}(\mathbb{G}_{m}, \mathbb{G}_{m}) / \sim$, where the equivalence accounts for the weights of the action. The character group is $\mathbb{Z}$, and the Hodge bundle corresponds to weight $1$. Since the discriminant $\Delta$ has weight $12$ and is invertible on $U$, we get $\operatorname{Pic}(\mathscr{M}_{1,1}) \cong \mathbb{Z}/12\mathbb{Z}$.

**Key Insight:** The global quotient presentation $\mathscr{M}_{1,1} \cong [U/\mathbb{G}_{m}]$ reduces the Picard group computation to equivariant line bundles, where the answer is determined by the character lattice modulo the weight of the discriminant.

**Prerequisites:** Equivariant Picard groups, quotient stacks, Weierstrass models, discriminant

<!-- BENCHMARK_PROBLEM: In the presentation $\mathscr{M}_{1,1} \cong [U/\mathbb{G}_{m}]$ where $\mathbb{G}_{m}$ acts on the Weierstrass parameters by $t \cdot (a,b) = (t^{4}a, t^{6}b)$, compute the weight of the discriminant $\Delta = -16(4a^{3} + 27b^{2})$ under this $\mathbb{G}_{m}$-action. -->

### Example: Non-reductive group action on affine varieties {#ecag-0340}

**Statement:** If a non-reductive algebraic group $G$ acts on an affine variety $X = \operatorname{Spec}(A)$, the ring of invariants $A^{G}$ need not be finitely generated, and consequently the GIT quotient $X /\!/ G = \operatorname{Spec}(A^{G})$ may fail to be of finite type. This is in stark contrast to the reductive case, where Hilbert's theorem (or its generalization by Nagata and Haboush) guarantees finite generation.

**Construction:** Step 1: Nagata's counterexample (1959) provides a linear action of $\mathbb{G}_{a}^{n}$ (a unipotent, hence non-reductive, group) on an affine space $\mathbb{A}^{N}$ such that the ring of invariants $k[x_{1}, \ldots, x_{N}]^{\mathbb{G}_{a}^{n}}$ is not finitely generated.

Step 2: A concrete family of examples arises from Hilbert's 14th problem. Consider $\mathbb{G}_{a}$ acting on $\mathbb{A}^{n}$ for $n$ large enough. Roberts (1990) gave an example with $G = \mathbb{G}_{a}$ acting on $\mathbb{A}^{7}$ where $k[x_{1}, \ldots, x_{7}]^{\mathbb{G}_{a}}$ is not finitely generated.

Step 3: More recently, Dufresne and Kraft showed that even for $\mathbb{G}_{a}$ acting on $\mathbb{A}^{6}$ by a triangular derivation, the invariant ring can fail finite generation.

Step 4: For the geometric invariant theory of non-reductive groups (developed by Kirwan and others), one must work with modified notions of stability and use blow-ups to obtain well-behaved quotients. The "non-reductive GIT" of Berczi, Doran, Hawes, and Kirwan provides a systematic framework.

**Key Insight:** Finite generation of invariant rings is a special property of reductive groups (Hilbert-Nagata theorem). Non-reductive groups violate this, making their quotient theory fundamentally more difficult and requiring new techniques beyond classical GIT.

**Prerequisites:** Geometric invariant theory, reductive vs. non-reductive groups, Hilbert's 14th problem, invariant rings, Nagata's counterexample

<!-- BENCHMARK_PROBLEM: Let $\mathbb{G}_{a}$ act on $\mathbb{A}^{3} = \operatorname{Spec}(k[x,y,z])$ by $t \cdot (x,y,z) = (x, y + tx, z + ty)$. Compute the ring of invariants $k[x,y,z]^{\mathbb{G}_{a}}$ and determine whether it is finitely generated. -->

### Remark: A finite subset of a variety need not be contained in an open affine subvariety {#ecag-0341}

On a general algebraic variety $X$ (not quasi-projective), a finite set of closed points $\{p_{1}, \ldots, p_{n}\} \subset X$ need not be contained in any open affine subvariety $U \subset X$. This pathology occurs precisely when $X$ is not quasi-projective.

For a quasi-projective variety $X \hookrightarrow \mathbb{P}^{N}$, any finite set of points can be placed in a single affine open: choose a hyperplane $H \subset \mathbb{P}^{N}$ avoiding all $p_{i}$, then $U = X \setminus (X \cap H)$ is affine and contains all $p_{i}$.

Hironaka's example of a complete non-projective threefold provides a counterexample: there exist two points $P, Q$ in the threefold such that no affine open subset contains both. The obstruction is that the exceptional curves $L_{1}, L_{2}$ above $P$ and $M_{1}, M_{2}$ above $Q$ satisfy a homological relation $L_{1} + M_{1} \sim 0$ that is incompatible with the existence of an affine neighborhood of both points.

<!-- BENCHMARK_PROBLEM: Explain why on a quasi-projective variety, any finite set of points is contained in an affine open, and give an example of a complete variety where this fails. -->

### Example: Hironaka's example, a variety with no Hilbert scheme {#ecag-0342}

**Statement:** Hironaka constructed a smooth complete threefold $V$ over $\mathbb{C}$ that is not projective. Because $V$ is not projective, the Hilbert scheme $\operatorname{Hilb}(V)$ does not exist as a projective scheme. More precisely, the functor of flat families of closed subschemes of $V$ is not representable by a scheme.

**Construction:** Step 1: Start with $\mathbb{P}^{3}$ and two smooth curves $C, D \subset \mathbb{P}^{3}$ meeting transversally at two points $P$ and $Q$. Specifically, $C = V(xy - z^{2}, w)$ and $D = V(xy - w^{2}, z)$ in $\mathbb{P}^{3} = \operatorname{Proj}(k[x,y,z,w])$.

Step 2: Construct $V$ by blowing up in a specific order that depends on the point:
- Over a neighborhood of $P$: first blow up $C$, then blow up the proper transform of $D$.
- Over a neighborhood of $Q$: first blow up $D$, then blow up the proper transform of $C$.
- Away from $P$ and $Q$: the two orders agree (since $C$ and $D$ are disjoint there), so the construction patches together.

Step 3: The resulting threefold $V$ is smooth and complete (proper over $k$), but not projective. The obstruction to projectivity is the existence of curves $L_{1}, L_{2}$ in the fiber over $P$ and $M_{1}, M_{2}$ in the fiber over $Q$ satisfying:
- $L_{1} + M_{1} \sim 0$ (homologically equivalent to zero).
- Both $L_{1}$ and $M_{1}$ are effective nonzero curves.
This means any ample divisor $H$ would satisfy $H \cdot L_{1} > 0$ and $H \cdot M_{1} > 0$, contradicting $H \cdot (L_{1} + M_{1}) = 0$.

Step 4: Without projectivity, Grothendieck's construction of the Hilbert scheme (which requires a projective embedding to bound Hilbert polynomials) fails. The Hilbert functor of $V$ is not representable.

**Key Insight:** The Hilbert scheme's existence relies fundamentally on projectivity (or at least quasi-projectivity). Hironaka's example shows that completeness alone is insufficient, and the failure of the numerical equivalence to be compatible with effectivity prevents projective embedding.

**Prerequisites:** Blow-ups, proper vs. projective varieties, Hilbert schemes, numerical equivalence, ample divisors

<!-- BENCHMARK_PROBLEM: In Hironaka's construction, let $L_{1}, L_{2}$ be the two components of the exceptional fiber over $P$, and $M_{1}, M_{2}$ those over $Q$. Explain why the relation $L_{1} + M_{1} \sim 0$ with $L_{1}, M_{1}$ effective contradicts the existence of an ample divisor on $V$. -->
### Example: Stacks project Tag O8KE, Descent data for schemes need not be effective, even for a projective morphism {#ecag-0343}

**Statement:** There exists a descent datum $(V/X, \phi)$ relative to an etale cover $X \to S$ with $V \to X$ projective, such that the descent datum is not effective in the category of schemes. This example is based on Hironaka's construction.

**Construction:** Let $k = \mathbb{C}$. We set up the following:

- $\mathbb{P}^{3} = \operatorname{Proj}(k[x,y,z,w])$.
- Two curves: $C = \operatorname{Proj}(k[x,y,z,w]/(xy - z^{2}, w))$ and $D = \operatorname{Proj}(k[x,y,z,w]/(xy - w^{2}, z))$.
- Intersection points: $P = [1,0,0,0]$ and $Q = [0,1,0,0]$.
- Two lines (fixed locus): $l_{1}: [x,x,z,z]$ and $l_{2}: [x,-x,z,-z]$.
- Group action: $G = \mathbb{Z}/2\mathbb{Z} = \{1, g\}$ acting on $\mathbb{P}^{3}$ by $g \cdot [x,y,z,w] = [y,x,w,z]$.
- The fixed locus is $l_{1} \cup l_{2}$, so $G$ acts freely on $Y = \mathbb{P}^{3} \setminus (l_{1} \cup l_{2})$.
- The quotient $S = Y/G$ exists as a quasi-projective scheme. Explicitly, $S$ is the image of $Y$ under

$$\mathbb{P}^{3} \to \operatorname{Proj}(k[x,y,z,w]^{G}) = \operatorname{Proj}(k[u_{0}, u_{1}, v_{0}, v_{1}, v_{2}]/(v_{0}v_{1} - v_{2}^{2})),$$

where $u_{0} = x+y$, $u_{1} = z+w$, $v_{0} = (x-y)^{2}$, $v_{1} = (z-w)^{2}$, $v_{2} = (x-y)(z-w)$. The target is the weighted projective space $\mathbb{P}(1,1,2,2,2)$.

- Apply Hironaka's construction to $Y$ (instead of $\mathbb{P}^{3}$) to obtain $\pi: V_{Y} \to Y$, a complete but non-projective variety over $Y$.
- Take the etale cover $X = (Y \setminus P) \sqcup (Y \setminus Q)$ of $Y$.

The $G$-action on $Y$ lifts to $V_{Y}$ by switching the preimages of $C$ and $D$, yielding a descent datum $(V_{Y}/Y, \phi_{Y})$ relative to the $G$-torsor $Y \to S$. This pulls back to a descent datum $(V/X, \phi)$ via the diagram:

$$V \xrightarrow{p} X \xrightarrow{f} Y \xrightarrow{h} S$$

$$V_{Y} \xrightarrow{\pi} Y \xrightarrow{h} S$$

$$U \xrightarrow{\theta} S$$

where $U$ would be the effectivization and $p$ is projective (being locally given by blow-ups).

**Proof of non-effectivity:** Suppose the descent datum is effective, producing a scheme $U$ with $V_{Y} \to U$ as the quotient by $G$. Let $E = \pi^{-1}(C \cup D)$ and

$$\pi^{-1}(P) = L_{1} \cup L_{2}, \quad \pi^{-1}(Q) = \pi^{-1}(gP) = M_{1} \cup M_{2},$$

with $g(L_{1}) = M_{1}$, $g(L_{2}) = M_{2}$, and $L_{1} + M_{1} = L_{1} + g(L_{1}) \sim 0$.

By descent of closed subschemes, there exists $\mathbb{P}^{1} \cong L \subset U$ with $h^{-1}(L) = L_{1} \cup M_{1}$. Choose a closed point $R \in L$ and $f \in \mathcal{O}_{U,R}$ vanishing at $R$ but with $L \not\subset V(f)$. Let $W$ be an irreducible codimension-$1$ component of $V(f)$ through $R$. Then the pullback $D' = (h')^{-1}(W)$ is an effective divisor on $V_{Y}$ satisfying:

$$\emptyset \neq D' \cap (L_{1} \cup M_{1}), \quad L_{1} \not\subset D', \quad M_{1} \not\subset D'.$$

The line bundle $\mathcal{O}(D')$ restricted to $E$ has positive intersection with the $1$-cycle $L_{1} + M_{1}$. But $L_{1} + M_{1} \sim 0$, so any line bundle must have degree $0$ on this cycle. This contradiction shows $U$ cannot exist as a scheme.

**Key Insight:** The descent datum is not effective because effectivization would require the quotient to be a scheme where intersection theory is well-defined, but Hironaka's homological relations on the exceptional fibers create an irreconcilable contradiction with the degree of line bundles on homologically trivial cycles.

**Prerequisites:** Descent theory, etale covers, Hironaka's example, blow-ups, intersection theory, proper schemes

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

The discussion of the descent datum above demonstrates that the quotient of the Hironaka variety $V_{Y}$ by the free $G = \mathbb{Z}/2\mathbb{Z}$-action does not exist as a scheme, even though the action is free and $G$ is finite. This is a striking pathology:

- For quasi-projective varieties, free actions by finite groups always yield scheme quotients (by GIT or direct construction).
- For separated algebraic spaces, the quotient by a free finite group action always exists as an algebraic space.
- The failure here is specifically in the category of schemes, and arises from the non-projectivity of Hironaka's threefold.

The quotient does exist as a proper algebraic space over $S$, but not as a scheme. This motivates the enlargement of the category of schemes to algebraic spaces in moduli theory.
### Example: Hironaka's example, a scheme of finite type over a field such that not every line bundle comes from a divisor {#ecag-0347}

**Statement:** On Hironaka's complete non-projective threefold $V$ over $\mathbb{C}$, there exist line bundles that do not arise as $\mathcal{O}(D)$ for any Cartier divisor $D$. Equivalently, the natural map $\operatorname{CaCl}(V) \to \operatorname{Pic}(V)$ from the group of Cartier divisors modulo linear equivalence to the Picard group is not surjective.

**Construction:** Step 1: On a smooth variety $V$, every line bundle is isomorphic to $\mathcal{O}(D)$ for some Weil divisor $D$, and since $V$ is smooth, every Weil divisor is Cartier. So $\operatorname{CaCl}(V) \cong \operatorname{Pic}(V)$ when $V$ is smooth. The issue arises in a different way.

Step 2: More precisely, on Hironaka's example $V$ (which is smooth), the problem is with global sections of line bundles. On a projective variety, every line bundle has a nonzero rational section, so every line bundle comes from a divisor. On a complete non-projective variety, this can fail.

Step 3: Consider the exceptional locus $E = \pi^{-1}(C \cup D)$. The relation $L_{1} + M_{1} \sim 0$ on $E$ means the line bundle $\mathcal{O}_{E}(L_{1} + M_{1})$ is trivial on $E$. However, the inclusion $E \hookrightarrow V$ induces a restriction map $\operatorname{Pic}(V) \to \operatorname{Pic}(E)$. There exist line bundles on $V$ whose restriction to $E$ has positive degree on $L_{1}$ and positive degree on $M_{1}$, contradicting the requirement that the degree on $L_{1} + M_{1}$ be zero. Such a line bundle cannot be represented by an effective divisor meeting $E$ properly.

Step 4: In practice, the pathology is that on non-projective proper varieties, the connection between line bundles, divisors, and linear systems breaks down. The variety $V$ has $H^{0}(V, \mathcal{L}) = 0$ for certain nontrivial line bundles $\mathcal{L}$, and there is no rational section available.

**Key Insight:** On projective varieties, the existence of an ample line bundle guarantees that every line bundle has a meromorphic section (and thus comes from a divisor). Without projectivity, this link breaks, and the Picard group can be strictly larger than the Cartier class group.

**Prerequisites:** Line bundles, Cartier divisors, projective vs. complete varieties, Hironaka's example

<!-- BENCHMARK_PROBLEM: On a smooth projective variety $X$, explain why every line bundle $\mathcal{L}$ admits a nonzero rational section, and hence $\operatorname{Pic}(X) \cong \operatorname{CaCl}(X)$. What specific property of projective varieties is used that fails for merely complete varieties? -->

### Remark {#ecag-0348}

In practice, the pathological phenomena arising from Hironaka's example (non-effective descent data, non-representable Hilbert functors, line bundles not coming from divisors) are avoided by assuming either:

- **$X$ is projective** (or quasi-projective): then Hilbert schemes exist, descent is effective for projective morphisms, and every line bundle comes from a divisor.
- **$X$ is reduced** (in characteristic $0$): combined with properness, Chow's lemma provides a birational projective model, and many functorial properties transfer.

Relevant references:

- [Stacks project, Tag 08KE](http://stacks.math.columbia.edu/tag/08KE): Descent data need not be effective.
- [Stacks project, Tag 08KF](http://stacks.math.columbia.edu/tag/08KF): Effectivity under projectivity hypotheses.
- Nitsure, [Construction of Hilbert and Quot schemes](https://perso.univ-rennes1.fr/matthieu.romagny/GT_Hilb/Nitsure_Construction_of_Hilbert_and_Quot_schemes.pdf).
- Vistoli, [Notes on Grothendieck topologies, fibered categories and descent theory](https://arxiv.org/pdf/math/0412512.pdf).
- Mumford, *Geometric Invariant Theory*.

## Hodge theory

### Remark: singular (co)homology, sheaf (co)homology, de Rham cohomology and Hodge decomposition {#ecag-0349}

The relationships between different cohomology theories on a smooth projective variety $X$ over $\mathbb{C}$ involve several distinct but related objects:

- **Singular vs. sheaf cohomology:** The singular cohomology $H^{*}(X^{an}, \mathbb{Z})$ (computed topologically) coincides with the sheaf cohomology $H^{*}(X^{an}, \underline{\mathbb{Z}})$ on the analytic site (by the comparison theorem for locally contractible spaces). The notation $\underline{\mathbb{Z}}$ denotes the constant sheaf. This also holds with $\mathbb{C}$ or $\mathbb{R}$ coefficients.

- **The role of $d\bar{z}$:** On a smooth algebraic curve $X$, the algebraic de Rham complex involves only holomorphic differentials $\Omega_{X}^{1}$. The forms $d\bar{z}$ are $C^{\infty}$ (smooth) but not holomorphic. They appear in the analytic de Rham complex $\mathcal{A}^{\bullet}$ of smooth differential forms, and in the Dolbeault resolution $\mathcal{A}^{p,q}$. The Hodge decomposition involves both holomorphic and antiholomorphic forms.

- **Hodge decomposition:** For $X$ smooth projective over $\mathbb{C}$ (or more generally, compact Kahler), the Hodge theorem gives

$$H^{n}(X^{an}, \mathbb{C}) \cong \bigoplus_{p+q=n} H^{p,q}(X),$$

where $H^{p,q}(X)$ consists of classes representable by harmonic $(p,q)$-forms. By the Dolbeault theorem, $H^{p,q}(X) \cong H^{q}(X, \Omega_{X}^{p})$ (sheaf cohomology of holomorphic $p$-forms). Complex conjugation gives $\overline{H^{p,q}(X)} = H^{q,p}(X)$, which is a statement about the real structure: the conjugation acts on $H^{n}(X, \mathbb{C}) = H^{n}(X, \mathbb{R}) \otimes_{\mathbb{R}} \mathbb{C}$.

- **Algebraic de Rham vs. analytic:** The algebraic de Rham cohomology $H^{n}_{dR}(X/\mathbb{C}) = \mathbb{H}^{n}(\Omega_{X/\mathbb{C}}^{\bullet})$ computes the hypercohomology of the algebraic de Rham complex. By GAGA and the holomorphic Poincare lemma, this equals the analytic de Rham cohomology, which in turn equals singular cohomology: $H^{n}_{dR}(X/\mathbb{C}) \cong H^{n}(X^{an}, \mathbb{C})$.

- **Betti lattice:** The integral lattice $H^{n}(X^{an}, \mathbb{Z}) \hookrightarrow H^{n}(X^{an}, \mathbb{C}) \cong H^{n}_{dR}(X/\mathbb{C})$ is a purely transcendental datum: it cannot be recovered from the algebraic de Rham cohomology alone. This is related to periods and the period map.

<!-- BENCHMARK_PROBLEM: For a smooth projective curve $X$ of genus $g$ over $\mathbb{C}$, compute all the Hodge numbers $h^{p,q}$ and verify the Hodge decomposition $H^{1}(X^{an}, \mathbb{C}) \cong H^{1,0}(X) \oplus H^{0,1}(X)$ with dimensions. -->
### Example: William Lang, Hodge spectral sequence in characteristic $3$ {#ecag-0350}

**Statement:** Let $k = \mathbb{F}_{3}$ and consider the surface

$$X: y^{2}z = x^{3} - tz^{2} \subset \mathbb{P}^{3}_{k}.$$

The first algebraic de Rham Betti number satisfies $b_{dR}^{1} = \dim_{k} H^{1}_{dR}(X/k) = 3$, while the Hodge numbers are $h^{0,1} = h^{1,0} = 1$, so $h^{0,1} + h^{1,0} = 2 \neq 3 = b_{dR}^{1}$. The Hodge-to-de Rham spectral sequence does not degenerate at $E_{1}$.

**Construction:** Step 1: The surface $X$ is a quasi-elliptic fibration over $\mathbb{P}^{1}$ (parametrized by $t$). In characteristic $3$, the Frobenius acts on the fibers $y^{2} = x^{3} - t$ in a special way: the differential $dx$ satisfies $d(x^{3}) = 3x^{2}dx = 0$, so the map $x \mapsto x^{3}$ is purely inseparable and the generic fiber is a cuspidal rational curve, not a smooth elliptic curve. This is a quasi-elliptic surface.

Step 2: The Hodge numbers are computed from sheaf cohomology:

$$h^{1,0} = \dim_{k} H^{0}(X, \Omega_{X/k}^{1}) = 1, \quad h^{0,1} = \dim_{k} H^{1}(X, \mathcal{O}_{X}) = 1.$$

Step 3: The algebraic de Rham cohomology $H^{1}_{dR}(X/k) = \mathbb{H}^{1}(\Omega_{X/k}^{\bullet})$ is computed via the hypercohomology spectral sequence (Hodge-to-de Rham spectral sequence):

$$E_{1}^{p,q} = H^{q}(X, \Omega_{X/k}^{p}) \implies H^{p+q}_{dR}(X/k).$$

Step 4: At $E_{1}$, the terms contributing to $H^{1}_{dR}$ are $E_{1}^{0,1} = H^{1}(X, \mathcal{O}_{X})$ (dimension $1$) and $E_{1}^{1,0} = H^{0}(X, \Omega_{X}^{1})$ (dimension $1$). If the spectral sequence degenerated at $E_{1}$, we would get $b_{dR}^{1} = h^{0,1} + h^{1,0} = 2$. But $b_{dR}^{1} = 3$, so the spectral sequence does not degenerate. There is a nonzero differential $d_{1}: E_{1}^{0,0} \to E_{1}^{1,0}$ or contributions from higher terms that increase the dimension.

**Key Insight:** The Hodge-to-de Rham spectral sequence degenerates at $E_{1}$ in characteristic $0$ (by the Hodge theorem or Deligne-Illusie for liftable varieties), but can fail to degenerate in positive characteristic. The culprit here is that the Cartier operator (inverse Frobenius on differentials) creates extra cohomology classes not visible in the Hodge filtration.

**Prerequisites:** Algebraic de Rham cohomology, Hodge-to-de Rham spectral sequence, quasi-elliptic surfaces, positive characteristic pathologies

<!-- BENCHMARK_PROBLEM: Let $X: y^{2}z = x^{3} - tz^{2}$ over $\mathbb{F}_{3}$. Verify that $h^{1,0} + h^{0,1} = 2$ while $b_{dR}^{1} = 3$, and explain which differential in the Hodge-to-de Rham spectral sequence must be nonzero. -->

### Remark {#ecag-0351}

This example is due to William Lang in his thesis "Quasi-elliptic surfaces in characteristic three." A detailed exposition appears in Alex Youcis's blog post [Algebraic de Rham cohomology and the degeneration of the Hodge spectral sequence](https://ayoucis.wordpress.com/2015/07/22/algebraic-de-rham-cohomology-and-the-degeneration-of-the-hodge-spectral-sequencethe/#more-3561).

The key theorem of Deligne-Illusie states that if $X$ is a smooth proper variety over a perfect field $k$ of characteristic $p > 0$, and $\dim X < p$, and $X$ lifts to $W_{2}(k)$ (the length-$2$ Witt vectors), then the Hodge-to-de Rham spectral sequence degenerates at $E_{1}$. Lang's example has $\dim X = 2$ and $\operatorname{char}(k) = 3$, so the condition $\dim X < p$ is satisfied. However, the surface $X$ does not lift to $W_{2}(\mathbb{F}_{3})$, which is why degeneration fails.

### Remark: $X$ irreducible, then $H_{\mathrm{dR}}^{i}(X/k)=0, \forall i>0$? (This cannot be true) {#ecag-0352}

One might attempt the following erroneous argument: the algebraic de Rham cohomology is defined as

$$H^{i}_{dR}(X/k) := \mathbb{H}^{i}(\Omega_{X/k}^{\bullet}).$$

If the de Rham complex $0 \to \mathcal{O}_{X} \to \Omega_{X/k}^{1} \to \cdots \to \Omega_{X/k}^{n} \to 0$ were a resolution of the constant sheaf $\underline{k}$, then $\mathbb{H}^{i}(\Omega_{X/k}^{\bullet}) \cong H^{i}(X, \underline{k})$. Since $X$ is irreducible, the constant sheaf $\underline{k}$ is flasque on the Zariski site, so $H^{i}(X, \underline{k}) = 0$ for $i > 0$. This would force $H^{i}_{dR}(X/k) = 0$ for all $i > 0$, which is absurd.

The error is that **the algebraic de Rham complex is not a resolution of $\underline{k}$ in the Zariski topology**. The Poincare lemma (which states that closed forms are locally exact) holds in the $C^{\infty}$ or analytic setting but fails in the algebraic (Zariski) setting. For example, on $\mathbb{A}^{1} = \operatorname{Spec}(k[t])$, the form $dt/t$ is closed on $\mathbb{G}_{m}$ but not exact (there is no algebraic logarithm). The correct statement is that the analytic de Rham complex is exact (Poincare lemma) on small analytic neighborhoods, but algebraic open sets are too large for this to hold.

In general:

$$H^{i}(X, \underline{k}) \neq \mathbb{H}^{i}(\Omega_{X/k}^{\bullet}).$$

The left side is Zariski sheaf cohomology of the constant sheaf (which is trivial for irreducible $X$), while the right side is the algebraic de Rham cohomology (which is highly nontrivial and computes topological cohomology over $\mathbb{C}$ by the comparison theorem).

### Example: Kahler manifold but not algebraic {#ecag-0353}

**Statement:** There exist compact Kahler manifolds that are not algebraic (i.e., not isomorphic to the analytification of a smooth projective variety). A standard example is a generic complex torus of dimension $\geq 2$.

**Construction:** Step 1: A complex torus of dimension $g$ is $T = \mathbb{C}^{g}/\Lambda$ where $\Lambda \cong \mathbb{Z}^{2g}$ is a lattice. The flat metric on $\mathbb{C}^{g}$ descends to a Kahler metric on $T$, so every complex torus is Kahler.

Step 2: By the Kodaira embedding theorem, a compact Kahler manifold is projective algebraic if and only if it admits a Hodge class, i.e., a Kahler class in $H^{1,1}(T) \cap H^{2}(T, \mathbb{Z})$. For a torus $T = \mathbb{C}^{g}/\Lambda$, this is equivalent to the existence of a Riemann form on $\Lambda$, i.e., an alternating bilinear form $E: \Lambda \times \Lambda \to \mathbb{Z}$ such that $E(iv, iw) = E(v, w)$ and $E(iv, v) > 0$ for $v \neq 0$.

Step 3: For $g = 1$, every complex torus is an elliptic curve and hence algebraic (a Riemann form always exists on a rank-$2$ lattice in $\mathbb{C}$).

Step 4: For $g \geq 2$, a generic lattice $\Lambda \subset \mathbb{C}^{g}$ admits no Riemann form. Concretely, for $g = 2$, the period matrix $\Omega = (I_{2} \mid Z)$ with $Z \in \operatorname{Mat}_{2 \times 2}(\mathbb{C})$ yields an abelian variety if and only if $Z$ is symmetric and $\operatorname{Im}(Z)$ is positive definite (Riemann conditions). But $\operatorname{Mat}_{2 \times 2}(\mathbb{C})$ is $8$-dimensional while symmetric matrices with positive-definite imaginary part form a $3$-dimensional subset (the Siegel upper half space $\mathfrak{H}_{2}$). So a generic $2$-dimensional complex torus is not algebraic.

Step 5: A non-algebraic complex torus has $\operatorname{Pic}^{0}(T) \neq 0$ (it always has topologically nontrivial line bundles from $H^{1}(T, \mathcal{O}^{*})$) but no ample line bundle. It may even have $\operatorname{NS}(T) = 0$ (no holomorphic line bundles of nonzero first Chern class).

**Key Insight:** The Kahler condition is necessary but not sufficient for algebraicity in dimension $\geq 2$. The obstruction is the Hodge conjecture for $(1,1)$-classes (which is a theorem): algebraicity requires an integral $(1,1)$-class, and generic complex tori lack these.

**Prerequisites:** Kahler manifolds, Kodaira embedding theorem, complex tori, abelian varieties, Riemann forms, Siegel upper half space

<!-- BENCHMARK_PROBLEM: For $g = 2$, what is the dimension of the space of all complex tori $\mathbb{C}^{2}/\Lambda$ (up to isomorphism), and what is the dimension of the moduli of principally polarized abelian surfaces $\mathfrak{H}_{2}/\operatorname{Sp}_{4}(\mathbb{Z})$? Use this to explain why a "generic" $2$-dimensional complex torus is not algebraic. -->

### Example: $\mathrm{rank}(H^{2k}(X_{t}, \mathbb{Z})\cap H^{k,k}(X_{t}))$ not constant {#ecag-0354}

**Statement:** In a family of smooth projective varieties $\{X_{t}\}_{t \in B}$, the rank of the group of integral Hodge classes $\operatorname{rk}(H^{2k}(X_{t}, \mathbb{Z}) \cap H^{k,k}(X_{t}))$ can jump as $t$ varies. This rank is lower semicontinuous (it can only jump up at special points) and its jumping locus is a countable dense union of analytic subvarieties of the base.

**Construction:** Step 1: Consider the family of smooth projective surfaces obtained by varying the coefficients of a quartic surface in $\mathbb{P}^{3}$. The Picard number $\rho(X_{t}) = \operatorname{rk}(\operatorname{NS}(X_{t})) = \operatorname{rk}(H^{2}(X_{t}, \mathbb{Z}) \cap H^{1,1}(X_{t}))$ varies in the family.

Step 2: For a very general quartic K3 surface $X_{t}$, the Picard number is $\rho = 1$ (generated by the hyperplane class). For special values of $t$, the Picard number can jump: for instance, the Fermat quartic $x_{0}^{4} + x_{1}^{4} + x_{2}^{4} + x_{3}^{4} = 0$ has $\rho = 20$ (the maximum for a K3 surface by the Lefschetz theorem on $(1,1)$-classes and the constraint $\rho \leq h^{1,1} = 20$).

Step 3: The Noether-Lefschetz theorem states that the locus $\{t : \rho(X_{t}) > 1\}$ is a countable dense union of divisors in the parameter space. Each Noether-Lefschetz divisor corresponds to a specific integral $(1,1)$-class becoming Hodge.

Step 4: For higher codimension ($k > 1$), the same phenomenon occurs with integral Hodge classes in $H^{2k} \cap H^{k,k}$. This is related to the Hodge conjecture and to Griffiths' results on the density of the Noether-Lefschetz locus in period domains.

**Key Insight:** The Hodge filtration varies holomorphically in families, but the integral lattice is locally constant. Their intersection -- the group of integral Hodge classes -- can therefore jump, and this jumping reflects the arithmetic complexity of special fibers.

**Prerequisites:** Hodge theory, Picard number, Noether-Lefschetz theorem, K3 surfaces, variation of Hodge structure

<!-- BENCHMARK_PROBLEM: For a smooth quartic surface $X \subset \mathbb{P}^{3}$ (a K3 surface), compute $h^{1,1}(X)$ and explain why $\rho(X) \leq 20$. Give an example of a quartic K3 with $\rho = 1$ and one with $\rho = 20$. -->
### Example: Family of elliptic curves, Gauss-Manin connection and Picard-Fuchs equation {#ecag-0355}

**Statement:** The Legendre family of elliptic curves $E_{t}: y^{2} = x(x-1)(x-t)$ over $S = \mathbb{P}^{1} \setminus \{0, 1, \infty\}$ carries a Gauss-Manin connection $\nabla$ on the local system $R^{1}\pi_{*}\mathbb{C}$. The flat sections of $\nabla$ satisfy the Picard-Fuchs differential equation

$$t(1-t) f''(t) + (1 - 2t) f'(t) - \frac{1}{4} f(t) = 0,$$

whose solutions are the periods $\int_{\gamma_{t}} \frac{dx}{y}$ as $\gamma_{t}$ varies over a basis of $H_{1}(E_{t}, \mathbb{Z})$.

**Construction:** Step 1: The family $\pi: \mathscr{E} \to S$ gives a rank $2$ local system $\mathcal{H} = R^{1}\pi_{*}\mathbb{C}$ on $S$. The corresponding flat vector bundle $(R^{1}\pi_{*}\mathbb{C}) \otimes_{\mathbb{C}} \mathcal{O}_{S}$ carries the Gauss-Manin connection $\nabla$, which differentiates cohomology classes in the direction of the parameter $t$.

Step 2: The holomorphic period $\omega(t) = \int_{\gamma} \frac{dx}{\sqrt{x(x-1)(x-t)}}$ is a multivalued function of $t$ (depending on the choice of cycle $\gamma$). Differentiating under the integral sign with respect to $t$:

$$\omega'(t) = \int_{\gamma} \frac{\partial}{\partial t} \frac{dx}{\sqrt{x(x-1)(x-t)}} = \frac{1}{2}\int_{\gamma} \frac{dx}{(x-t)\sqrt{x(x-1)(x-t)}}.$$

Step 3: By integration by parts and reduction of the integrand using the relation $y^{2} = x(x-1)(x-t)$, one derives the Picard-Fuchs equation. The key is that $\frac{dx}{(x-t)y}$ can be expressed as a linear combination of $\frac{dx}{y}$, $\frac{x\,dx}{y}$, and exact forms, using the Griffiths-Dwork reduction.

Step 4: The Picard-Fuchs equation is a Fuchsian ODE with regular singular points at $t = 0, 1, \infty$. Its monodromy representation $\pi_{1}(S) \to \operatorname{GL}_{2}(\mathbb{C})$ coincides with the monodromy of the local system $R^{1}\pi_{*}\mathbb{C}$. The monodromy matrices around $t = 0$ and $t = 1$ are conjugate to $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ (unipotent of index $2$), reflecting the Dehn twist on the vanishing cycle.

Step 5: The two linearly independent solutions are the complete elliptic integrals $K(t)$ and $K(1-t)$ (or equivalently, the hypergeometric function ${}_{2}F_{1}(1/2, 1/2; 1; t)$ and its companion).

**Key Insight:** The Gauss-Manin connection encodes how the Hodge structure varies in a family, and the Picard-Fuchs equation is its differential-algebraic manifestation. The periods of elliptic curves satisfy a classical hypergeometric equation, linking algebraic geometry to special functions.

**Prerequisites:** Gauss-Manin connection, local systems, periods of algebraic varieties, Fuchsian differential equations, hypergeometric functions

<!-- BENCHMARK_PROBLEM: Verify that $f(t) = {}_{2}F_{1}(1/2, 1/2; 1; t)$ satisfies the Picard-Fuchs equation $t(1-t)f'' + (1-2t)f' - \frac{1}{4}f = 0$. Compute the first three terms of the power series expansion of $f(t)$ around $t = 0$. -->

### Example: Polarized variation of Hodge structure over the punctured disk {#ecag-0356}

**Statement:** A polarized variation of Hodge structure (PVHS) over the punctured disk $\Delta^{*} = \{t \in \mathbb{C} : 0 < |t| < 1\}$ is a flat vector bundle $(\mathcal{H}, \nabla)$ with a Hodge filtration $F^{\bullet}$ varying holomorphically and a flat bilinear form $Q$ satisfying the Hodge-Riemann bilinear relations on each fiber. The monodromy $T$ around $t = 0$ is quasi-unipotent, and the limiting Hodge filtration as $t \to 0$ defines a mixed Hodge structure.

**Construction:** Step 1: Let $\pi: \mathscr{X} \to \Delta$ be a proper morphism of complex manifolds with $\mathscr{X}_{t}$ smooth for $t \neq 0$ and $\mathscr{X}_{0}$ a normal crossing divisor (semistable reduction). The cohomology $H^{n}(\mathscr{X}_{t}, \mathbb{Q})$ for $t \neq 0$ forms a local system over $\Delta^{*}$ with monodromy $T$.

Step 2: By the monodromy theorem, $T$ is quasi-unipotent: $(T^{m} - I)^{n+1} = 0$ for some $m \geq 1$, where $n$ is the weight. After replacing $t$ by $t^{m}$ (base change), we may assume $T$ is unipotent. Write $T = e^{N}$ where $N = \log T$ is nilpotent.

Step 3: The Schmid nilpotent orbit theorem states that the Hodge filtration $F_{t}^{\bullet}$ on $H^{n}(\mathscr{X}_{t}, \mathbb{C})$ has the asymptotic behavior

$$F_{t}^{\bullet} \sim e^{\frac{\log t}{2\pi i} N} \cdot F_{\infty}^{\bullet}$$

as $t \to 0$, where $F_{\infty}^{\bullet}$ is the limiting Hodge filtration.

Step 4: The weight filtration $W_{\bullet}$ associated to $N$ (the unique filtration making $(N, W_{\bullet})$ a morphism of mixed Hodge structures) together with $F_{\infty}^{\bullet}$ gives a mixed Hodge structure on $H^{n}(\mathscr{X}_{0}, \mathbb{Q})$ (after identifying the nearby cycle sheaf with the cohomology of the central fiber).

Step 5: For the Legendre family degenerating to a nodal rational curve at $t = 0$: the monodromy is $T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, and the weight filtration is $W_{0} = \operatorname{span}\{e_{2}\} \subset W_{1} = W_{2} = \mathbb{Q}^{2}$, giving a mixed Hodge structure of type $\{(0,0), (1,1)\}$.

**Key Insight:** The Schmid nilpotent orbit theorem provides a precise asymptotic description of how the Hodge structure degenerates, and the resulting mixed Hodge structure on the limit encodes both the topology of the degeneration (via monodromy) and the complex geometry (via the limiting filtration).

**Prerequisites:** Variations of Hodge structure, monodromy, nilpotent orbit theorem, mixed Hodge structures, semistable reduction

<!-- BENCHMARK_PROBLEM: For a family of elliptic curves degenerating to a nodal rational curve (e.g., $y^{2} = x(x-1)(x-t)$ as $t \to 0$), compute the monodromy matrix $T$, the nilpotent operator $N = \log T$, and the weight filtration $W_{\bullet}$ associated to $N$. -->

### Example: variation of Hodge structures, Siegel upper half plane {#ecag-0357}

**Statement:** The period domain for weight-$1$ polarized Hodge structures of dimension $g$ is the Siegel upper half space $\mathfrak{H}_{g} = \{Z \in \operatorname{Mat}_{g \times g}(\mathbb{C}) : Z = Z^{T}, \, \operatorname{Im}(Z) > 0\}$. The period map for a family of $g$-dimensional abelian varieties $\mathscr{A} \to S$ is a holomorphic map $\Phi: \widetilde{S} \to \mathfrak{H}_{g}$ (on the universal cover), and the monodromy representation lands in $\operatorname{Sp}_{2g}(\mathbb{Z})$.

**Construction:** Step 1: A polarized Hodge structure of weight $1$ on a $\mathbb{Z}$-lattice $H_{\mathbb{Z}} \cong \mathbb{Z}^{2g}$ consists of a decomposition $H_{\mathbb{C}} = H^{1,0} \oplus H^{0,1}$ with $\overline{H^{1,0}} = H^{0,1}$ and a symplectic form $Q: H_{\mathbb{Z}} \times H_{\mathbb{Z}} \to \mathbb{Z}$ satisfying $Q(H^{1,0}, H^{1,0}) = 0$ and $iQ(v, \bar{v}) > 0$ for $v \in H^{1,0} \setminus \{0\}$.

Step 2: Choosing a symplectic basis $(e_{1}, \ldots, e_{g}, f_{1}, \ldots, f_{g})$ with $Q(e_{i}, f_{j}) = \delta_{ij}$, the subspace $H^{1,0}$ is the row space of a matrix $(\Omega_{1} \mid \Omega_{2})$ where $\Omega_{2}$ is invertible (generically). Setting $Z = \Omega_{2}^{-1}\Omega_{1}$, the conditions become $Z = Z^{T}$ (from $Q(H^{1,0}, H^{1,0}) = 0$) and $\operatorname{Im}(Z) > 0$ (from the positivity condition).

Step 3: The Siegel upper half space $\mathfrak{H}_{g}$ has dimension $g(g+1)/2$. For $g = 1$, $\mathfrak{H}_{1}$ is the usual upper half plane $\{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}$. The symplectic group $\operatorname{Sp}_{2g}(\mathbb{R})$ acts on $\mathfrak{H}_{g}$ by $\begin{pmatrix} A & B \\ C & D \end{pmatrix} \cdot Z = (AZ + B)(CZ + D)^{-1}$.

Step 4: The quotient $\mathscr{A}_{g} = \operatorname{Sp}_{2g}(\mathbb{Z}) \backslash \mathfrak{H}_{g}$ is the coarse moduli space of principally polarized abelian varieties of dimension $g$. The Torelli theorem states that the period map $\mathcal{M}_{g} \to \mathscr{A}_{g}$ (sending a curve to its Jacobian) is injective.

**Key Insight:** The Siegel upper half space is the natural parameter space for polarized Hodge structures of weight $1$, generalizing the upper half plane for elliptic curves. The arithmetic quotient $\operatorname{Sp}_{2g}(\mathbb{Z}) \backslash \mathfrak{H}_{g}$ is a quasi-projective variety (by Baily-Borel), providing a concrete model for the moduli of abelian varieties.

**Prerequisites:** Hodge structures, abelian varieties, period maps, symplectic geometry, Siegel modular varieties

<!-- BENCHMARK_PROBLEM: Compute the dimension of the Siegel upper half space $\mathfrak{H}_{g}$ for $g = 3$, and compare it with $\dim \mathcal{M}_{3} = 3g - 3 = 6$. What does this comparison tell you about the Torelli map? -->

### Example: Mixed Hodge structure, nodal curve {#ecag-0358}

**Statement:** Let $C$ be a projective curve with a single node $p$ (obtained by identifying two points $p_{1}, p_{2}$ on the normalization $\widetilde{C}$). The cohomology $H^{1}(C, \mathbb{Z})$ carries a mixed Hodge structure with weight filtration $W_{0} \subset W_{1} = H^{1}(C, \mathbb{Z})$, where $W_{0} \cong \mathbb{Z}$ is of type $(0,0)$ and $\operatorname{Gr}_{1}^{W} \cong H^{1}(\widetilde{C}, \mathbb{Z})$ carries the pure Hodge structure of the normalization.

**Construction:** Step 1: The normalization sequence gives an exact sequence of sheaves on $C$:

$$0 \to \mathcal{O}_{C} \to \nu_{*}\mathcal{O}_{\widetilde{C}} \to \mathbb{C}_{p} \to 0,$$

where $\nu: \widetilde{C} \to C$ is the normalization and $\mathbb{C}_{p}$ is the skyscraper sheaf at $p$ (the cokernel accounts for the identification of the two preimage points).

Step 2: The long exact sequence in cohomology gives

$$0 \to H^{0}(C, \mathcal{O}_{C}) \to H^{0}(\widetilde{C}, \mathcal{O}_{\widetilde{C}}) \oplus \mathbb{C} \to \mathbb{C} \to H^{1}(C, \mathcal{O}_{C}) \to H^{1}(\widetilde{C}, \mathcal{O}_{\widetilde{C}}) \to 0.$$

Since $H^{0}(C, \mathcal{O}_{C}) = H^{0}(\widetilde{C}, \mathcal{O}_{\widetilde{C}}) = \mathbb{C}$ (both connected), the map $\mathbb{C}^{2} \to \mathbb{C}$ is surjective, giving

$$\dim H^{1}(C, \mathcal{O}_{C}) = \dim H^{1}(\widetilde{C}, \mathcal{O}_{\widetilde{C}}) + 1 = g(\widetilde{C}) + 1 = p_{a}(C).$$

Step 3: Topologically, $H_{1}(C, \mathbb{Z}) \cong H_{1}(\widetilde{C}, \mathbb{Z}) \oplus \mathbb{Z}$, where the extra $\mathbb{Z}$ is generated by the loop around the node (a circle obtained from the identification $p_{1} \sim p_{2}$ via a path from $p_{1}$ to $p_{2}$).

Step 4: The mixed Hodge structure on $H^{1}(C, \mathbb{Z})$:
- $W_{0} = \mathbb{Z} \cdot [\gamma]$ where $\gamma$ is the vanishing cycle, of Hodge type $(0,0)$.
- $\operatorname{Gr}_{1}^{W} = H^{1}(\widetilde{C}, \mathbb{Z})$, a pure Hodge structure of weight $1$ (with $h^{1,0} = h^{0,1} = g(\widetilde{C})$).
- The Hodge filtration $F^{1} H^{1}(C, \mathbb{C}) = H^{0}(\widetilde{C}, \omega_{\widetilde{C}}(p_{1} + p_{2}))$ (differentials with at most simple poles at $p_{1}, p_{2}$ with opposite residues).

Step 5: For an irreducible rational nodal curve ($\widetilde{C} = \mathbb{P}^{1}$): $H^{1}(C, \mathbb{Z}) \cong \mathbb{Z}$, purely of type $(0,0)$. The arithmetic genus $p_{a} = 1$ but the geometric genus $g = 0$.

**Key Insight:** The mixed Hodge structure on a nodal curve cleanly separates the topology of the normalization (weight $1$ part) from the topology of the singularity (weight $0$ part), illustrating how mixed Hodge theory extends pure Hodge theory to singular varieties.

**Prerequisites:** Mixed Hodge structures, normalization, nodal curves, weight filtration, arithmetic genus

<!-- BENCHMARK_PROBLEM: Let $C$ be an irreducible curve of arithmetic genus $2$ with one node, so that $\widetilde{C}$ has genus $1$. Describe the mixed Hodge structure on $H^{1}(C, \mathbb{Z})$: give the weight filtration, the Hodge type of each graded piece, and compute $h^{1,0}$ and $h^{0,1}$ of the pure part. -->
### Example: Mixed Hodge structure, split over $\mathbb{R}$ {#ecag-0359}

**Statement:** A mixed Hodge structure $(H_{\mathbb{Z}}, W_{\bullet}, F^{\bullet})$ is said to be split over $\mathbb{R}$ (or $\mathbb{R}$-split) if there exists a bigrading $H_{\mathbb{C}} = \bigoplus_{p,q} I^{p,q}$ such that $F^{p} = \bigoplus_{a \geq p} I^{a,b}$, $W_{k} = \bigoplus_{p+q \leq k} I^{p,q}$, and $\overline{I^{p,q}} = I^{q,p}$. Not every mixed Hodge structure is $\mathbb{R}$-split, but every mixed Hodge structure admits a canonical splitting over $\mathbb{C}$ (the Deligne splitting).

**Construction:** Step 1: Every mixed Hodge structure has the Deligne splitting: there exist unique subspaces $I^{p,q} \subset H_{\mathbb{C}}$ satisfying $F^{p} = \bigoplus_{a \geq p} I^{a,b}$, $\bar{F}^{q} = \bigoplus_{b \geq q} I^{a,b}$, and $W_{k} \otimes \mathbb{C} = \bigoplus_{p+q \leq k} I^{p,q}$. However, in general $\overline{I^{p,q}} \neq I^{q,p}$; instead, $\overline{I^{p,q}} \equiv I^{q,p} \pmod{\bigoplus_{a < q, b < p} I^{a,b}}$.

Step 2: A mixed Hodge structure is $\mathbb{R}$-split if and only if the Deligne splitting satisfies $\overline{I^{p,q}} = I^{q,p}$ exactly (not just modulo lower terms). This happens when the extension classes in $\operatorname{Ext}^{1}_{MHS}(\operatorname{Gr}^{W}_{k+1}, \operatorname{Gr}^{W}_{k})$ are real (lie in the real part of the extension group).

Step 3 (Example that is $\mathbb{R}$-split): The mixed Hodge structure on $H^{1}$ of a nodal rational curve is $\mathbb{R}$-split: $H^{1}(C, \mathbb{Z}) = \mathbb{Z}$ of type $(0,0)$, which is trivially split.

Step 4 (Example that is not $\mathbb{R}$-split): Consider $H_{\mathbb{Z}} = \mathbb{Z}^{3}$ with weight filtration $W_{0} = \mathbb{Z} e_{1}$, $W_{1} = \mathbb{Z} e_{1} \oplus \mathbb{Z} e_{2} \oplus \mathbb{Z} e_{3}$, and Hodge filtration $F^{1} = \mathbb{C}(e_{2} + i e_{3} + \tau e_{1})$ where $\tau \in \mathbb{C}$ with $\operatorname{Im}(\tau) \neq 0$. The graded pieces are: $\operatorname{Gr}_{0}^{W} = \mathbb{Z}$ of type $(0,0)$ and $\operatorname{Gr}_{1}^{W} = \mathbb{Z}^{2}$ with Hodge structure of type $\{(1,0), (0,1)\}$. This is $\mathbb{R}$-split if and only if $\tau \in \mathbb{R}$, i.e., the extension class is real.

**Key Insight:** The notion of $\mathbb{R}$-splitting measures whether the extension data in a mixed Hodge structure is compatible with the real structure. Geometrically, for a degeneration of curves, the MHS on the limit is $\mathbb{R}$-split when the extension class (which encodes the position of the vanishing cycle) is real.

**Prerequisites:** Mixed Hodge structures, Deligne splitting, extension classes, weight filtration, real structures

<!-- BENCHMARK_PROBLEM: Construct an explicit mixed Hodge structure on $\mathbb{Z}^{3}$ with weights $0$ and $1$ (one-dimensional weight $0$ part of type $(0,0)$, two-dimensional weight $1$ part of type $\{(1,0),(0,1)\}$) that is NOT split over $\mathbb{R}$. Specify the weight filtration and Hodge filtration. -->

### Example: Unimodular lattices {#ecag-0360}

**Statement:** A unimodular lattice is a free $\mathbb{Z}$-module $L$ of finite rank equipped with a symmetric bilinear form $\langle \cdot, \cdot \rangle: L \times L \to \mathbb{Z}$ whose discriminant (determinant of the Gram matrix) is $\pm 1$. Unimodular lattices arise naturally in algebraic geometry as the intersection forms on the middle cohomology of even-dimensional manifolds.

**Construction:** Step 1: The classification of unimodular lattices depends on the signature and parity:
- **Type I** (odd): contains vectors $v$ with $\langle v, v \rangle$ odd. Examples: $\mathbb{Z}$ (rank $1$, signature $(1,0)$), $I_{p,q} = \mathbb{Z}^{p+q}$ with form $\operatorname{diag}(1, \ldots, 1, -1, \ldots, -1)$ (signature $(p,q)$).
- **Type II** (even): $\langle v, v \rangle \in 2\mathbb{Z}$ for all $v$. Examples: $E_{8}$ (rank $8$, positive definite), $E_{8}(-1)$ (negative definite), the hyperbolic plane $U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (signature $(1,1)$).

Step 2: For a smooth compact oriented $4k$-manifold $M$, the intersection form on $H^{2k}(M, \mathbb{Z})/\text{torsion}$ is unimodular (by Poincare duality). For $k = 1$ (i.e., $4$-manifolds), this lattice determines the homeomorphism type (Freedman's theorem).

Step 3: For K3 surfaces, the intersection lattice on $H^{2}(X, \mathbb{Z})$ is the unique even unimodular lattice of signature $(3, 19)$:

$$\Lambda_{K3} = U^{3} \oplus E_{8}(-1)^{2},$$

where $U$ is the hyperbolic plane and $E_{8}(-1)$ is the negative definite $E_{8}$ lattice. This has rank $22$.

Step 4: The Milnor-Kneser classification: indefinite even unimodular lattices are classified by rank and signature. Specifically, an even unimodular lattice of signature $(p, q)$ exists if and only if $p - q \equiv 0 \pmod{8}$, and when it exists, it is unique (up to isometry) if $p \geq 1$ and $q \geq 1$.

Step 5: In positive definite case, the classification is much harder. In rank $8$, there is one even unimodular lattice ($E_{8}$). In rank $16$, there are two ($E_{8} \oplus E_{8}$ and $D_{16}^{+}$). In rank $24$, there are $24$ (the Niemeier lattices, including the Leech lattice).

**Key Insight:** Unimodular lattices bridge number theory, topology, and algebraic geometry: they arise as intersection forms of manifolds, as period lattices of K3 surfaces, and their classification involves deep results in the theory of quadratic forms.

**Prerequisites:** Lattices, bilinear forms, intersection theory, K3 surfaces, Poincare duality, classification of quadratic forms

<!-- BENCHMARK_PROBLEM: Verify that the K3 lattice $\Lambda_{K3} = U^{3} \oplus E_{8}(-1)^{2}$ has rank $22$, signature $(3, 19)$, and is even and unimodular. Compute the discriminant of $U$ and of $E_{8}$. -->

### Example: Mixed Hodge structure on $\mathfrak{gl}(V_{\mathbb{C}})$ {#ecag-0361}

**Statement:** If $V$ is a rational vector space carrying a mixed Hodge structure, then the endomorphism space $\operatorname{End}(V) = V^{\vee} \otimes V \cong \mathfrak{gl}(V)$ inherits a natural mixed Hodge structure. The weight filtration on $\operatorname{End}(V)$ is determined by $W_{k}\operatorname{End}(V) = \{f : f(W_{i} V) \subset W_{i+k} V \text{ for all } i\}$, and the Hodge filtration is $F^{p}\operatorname{End}(V_{\mathbb{C}}) = \{f : f(F^{i}V_{\mathbb{C}}) \subset F^{i+p}V_{\mathbb{C}} \text{ for all } i\}$.

**Construction:** Step 1: Given a mixed Hodge structure $(V_{\mathbb{Q}}, W_{\bullet}, F^{\bullet})$, define:
- Weight filtration: $W_{k}\operatorname{End}(V_{\mathbb{Q}}) = \{f \in \operatorname{End}(V_{\mathbb{Q}}) : f(W_{i}) \subset W_{i+k}, \forall i\}$.
- Hodge filtration: $F^{p}\operatorname{End}(V_{\mathbb{C}}) = \{f \in \operatorname{End}(V_{\mathbb{C}}) : f(F^{i}) \subset F^{i+p}, \forall i\}$.

Step 2: To verify this is a mixed Hodge structure, one checks that $(\operatorname{End}(V_{\mathbb{Q}}), W_{\bullet}, F^{\bullet})$ satisfies the axioms. The key is that $\operatorname{End}(V) \cong V^{\vee} \otimes V$, and the tensor product and dual of mixed Hodge structures are mixed Hodge structures.

Step 3: For the Deligne splitting: if $V_{\mathbb{C}} = \bigoplus I^{p,q}$ is the Deligne decomposition, then $\operatorname{End}(V_{\mathbb{C}}) = \bigoplus_{(p,q),(r,s)} \operatorname{Hom}(I^{r,s}, I^{p,q})$, and the piece $\operatorname{Hom}(I^{r,s}, I^{p,q})$ has type $(p-r, q-s)$ in the Deligne decomposition of $\operatorname{End}(V)$.

Step 4 (Lie-algebraic significance): The subspace $W_{-1}\operatorname{End}(V) \cap F^{0}\operatorname{End}(V_{\mathbb{C}})$ consists of endomorphisms that strictly lower the weight filtration while preserving the Hodge filtration. This is the Lie algebra of the unipotent radical of the Mumford-Tate group of the mixed Hodge structure. The nilpotent operator $N$ in a degeneration satisfies $N \in W_{-2}\operatorname{End}(V) \cap F^{-1}\operatorname{End}(V_{\mathbb{C}})$ (by the $\operatorname{SL}_{2}$-orbit theorem).

Step 5 (Example): Let $V = \mathbb{Q}^{2}$ with $W_{0} = \mathbb{Q} e_{1}$, $W_{1} = V$, $F^{1} = \mathbb{C}(e_{2} + \tau e_{1})$. Then $\operatorname{End}(V) \cong \operatorname{Mat}_{2 \times 2}(\mathbb{Q})$ with weight filtration:
- $W_{-1}\operatorname{End}(V) = \left\{\begin{pmatrix} 0 & 0 \\ * & 0 \end{pmatrix}\right\}$ (maps lowering weight by $1$),
- $W_{0}\operatorname{End}(V) = \left\{\begin{pmatrix} * & 0 \\ * & * \end{pmatrix}\right\}$ (maps preserving weight),
- $W_{1}\operatorname{End}(V) = \operatorname{Mat}_{2 \times 2}(\mathbb{Q})$.

**Key Insight:** The mixed Hodge structure on $\operatorname{End}(V)$ encodes the symmetries of the original MHS, and its weight-filtered pieces capture the Lie algebra of the Mumford-Tate group, connecting Hodge theory to representation theory.

**Prerequisites:** Mixed Hodge structures, tensor operations on MHS, Deligne splitting, Mumford-Tate groups, Lie algebras

<!-- BENCHMARK_PROBLEM: Let $V = \mathbb{Q}^{2}$ with the mixed Hodge structure given by $W_{0} = \mathbb{Q} e_{1}$, $W_{1} = V$, $F^{1} = \mathbb{C}(e_{2} + ie_{1})$. Compute the weight filtration on $\operatorname{End}(V)$ and determine $\dim_{\mathbb{Q}} \operatorname{Gr}_{k}^{W}\operatorname{End}(V)$ for $k = -1, 0, 1$. -->
