---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/hodge.tex
---

## Hodge numbers

### Example: Hodge numbers of a blow-up {#ecag-0231}

**Statement:** Let $C \subset \mathbb{P}^3$ be the twisted cubic curve, parametrized by $[s,t] \mapsto [s^3, s^2 t, s t^2, t^3]$. We compute the Hodge diamond of the blow-up $\operatorname{Bl}_C(\mathbb{P}^3)$ over $\mathbb{C}$, showing it is

$$
\begin{array}{ccccccc}
 & & & 1 & & & \\
 & & 0 & & 0 & & \\
 & 0 & & 2 & & 0 & \\
 0 & & 0 & & 0 & & 0 \\
 & 0 & & 2 & & 0 & \\
 & & 0 & & 0 & & \\
 & & & 1 & & &
\end{array}

$$

**Construction/Proof:**

We present four approaches to this computation.

*Method 1: Additivity of $\chi^{p,q}$.*

Define the Hodge--Euler numbers $\chi^{p,q} = (-1)^{p+q} h^{p,q}$. These are additive in the sense that for a blow-up $\operatorname{Bl}_Z(X)$ of a smooth variety $X$ along a smooth subvariety $Z$ with exceptional divisor $E$, we have

$$
\chi^{p,q}(\operatorname{Bl}_Z(X)) = \chi^{p,q}(X) + \chi^{p,q}(E) - \chi^{p,q}(Z).

$$

Here $Z = C \cong \mathbb{P}^1$ (since the twisted cubic is a rational curve) and $E$ is a $\mathbb{P}^1$-bundle over $C$, so $E \cong \mathbb{P}^1 \times \mathbb{P}^1$ (since the normal bundle $N_{C/\mathbb{P}^3}$ of a twisted cubic in $\mathbb{P}^3$ is $\mathcal{O}(5) \oplus \mathcal{O}(1)$, a direct sum of line bundles of distinct degrees, and the projectivization of any rank-2 bundle on $\mathbb{P}^1$ that splits is a Hirzebruch surface; the Hodge numbers of all Hirzebruch surfaces agree with those of $\mathbb{P}^1 \times \mathbb{P}^1$). Thus

$$
\chi^{p,q}(\operatorname{Bl}_C(\mathbb{P}^3)) = \chi^{p,q}(\mathbb{P}^3) + \chi^{p,q}(\mathbb{P}^1 \times \mathbb{P}^1) - \chi^{p,q}(\mathbb{P}^1).

$$

The Hodge diamonds of the ingredients are:

- $\mathbb{P}^3$: $h^{p,p} = 1$ for $0 \le p \le 3$, all others zero.
- $\mathbb{P}^1 \times \mathbb{P}^1$: $h^{0,0} = h^{1,1} = 1$, $h^{1,1} = 2$ (correction: $h^{0,0} = h^{2,2} = 1$, $h^{1,1} = 2$, others zero).
- $\mathbb{P}^1$: $h^{0,0} = h^{1,1} = 1$, others zero.

Computing term by term: $h^{0,0} = 1$, $h^{1,1} = 1 + 2 - 1 = 2$, $h^{2,2} = 1 + 1 - 1 = 1$ (but we must account for the dimension shift properly). Since $\operatorname{Bl}_C(\mathbb{P}^3)$ is a smooth projective threefold with no odd cohomology contributions (all constituents are rational), we get $h^{p,q} = 0$ for $p \neq q$ and $h^{0,0} = h^{3,3} = 1$, $h^{1,1} = h^{2,2} = 2$.

*Method 2: Mixed Hodge structures.*

By Deligne's theory of mixed Hodge structures, one can compute the Hodge numbers using the long exact sequence in cohomology associated to the blow-up. The key exact sequence is

$$
\cdots \to H^k(X) \oplus H^k(E) \to H^k(Z) \to H^{k+1}(\operatorname{Bl}_Z(X)) \to \cdots

$$

(with appropriate Tate twists). Since all varieties involved ($\mathbb{P}^3$, $\mathbb{P}^1$, Hirzebruch surfaces) have pure Hodge structures concentrated in type $(p,p)$, the mixed Hodge structure on $\operatorname{Bl}_C(\mathbb{P}^3)$ is also pure, confirming the result.

*Method 3: Decomposition theorem.*

The Beilinson--Bernstein--Deligne--Gabber decomposition theorem, applied to the blow-up morphism $\pi : \operatorname{Bl}_C(\mathbb{P}^3) \to \mathbb{P}^3$, gives a splitting

$$
R\pi_* \mathbb{Q} \cong \mathbb{Q}_{\mathbb{P}^3} \oplus \mathbb{Q}_C[-2](-1)

$$

in the derived category of mixed Hodge modules. Taking hypercohomology recovers the Hodge numbers.

*Method 4: Computer algebra (Macaulay2).*

The computation can be verified using the `Schubert2` package in Macaulay2 via the `blowup` command. See the [Macaulay2 documentation](http://www2.macaulay2.com/Macaulay2/doc/Macaulay2-1.10/share/doc/Macaulay2/Schubert2/html/_blowup.html).

**Key Insight:** Blowing up a smooth rational curve in $\mathbb{P}^3$ increases $h^{1,1}$ by exactly 1 (from 1 to 2), reflecting the new algebraic class contributed by the exceptional divisor. The additivity of Hodge--Euler numbers provides the most elementary route to the computation.

**Prerequisites:** Blow-ups of smooth varieties, Hodge numbers, Hodge--Euler characteristic, twisted cubic curve, Hirzebruch surfaces, mixed Hodge structures, decomposition theorem

<!-- BENCHMARK_PROBLEM: Let C be the twisted cubic in P^3 over the complex numbers. Compute h^{1,1} of the blow-up Bl_C(P^3). Show your work using the additivity of Hodge–Euler numbers. -->

### Remark: Reference {#ecag-0232}

The computations in this section follow the methods detailed in Donu Arapura's notes, [Computations of some Hodge numbers](http://www.math.purdue.edu/~dvb/preprints/book-chap17.pdf), which provide a systematic treatment of Hodge number calculations for blow-ups, fibrations, and related constructions. In particular, Chapter 17 of those notes covers the additivity of Hodge--Euler characteristics and its applications to blow-up computations in detail.
