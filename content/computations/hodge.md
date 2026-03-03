---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/hodge.tex
---

## Hodge numbers

### Example: Hodge numbers of a blow-up {#ecag-0231}

Let $C \subset \mathbb{P}^3$ be the twisted cubic curve, parametrized by $[s,t] \mapsto [s^3, s^2 t, s t^2, t^3]$. As a smooth rational curve, $C \cong \mathbb{P}^1$. We compute the Hodge diamond of the blow-up $X = \operatorname{Bl}_C(\mathbb{P}^3)$ over $\mathbb{C}$.

**The blow-up formula for Hodge numbers.** For a smooth variety $X$ of dimension $d$ blown up along a smooth subvariety $Z$ of codimension $c \geq 2$, the Hodge numbers satisfy

$$
h^{p,q}(\operatorname{Bl}_Z(X)) = h^{p,q}(X) + \sum_{i=1}^{c-1} h^{p-i,q-i}(Z).

$$

Here $Z = C \cong \mathbb{P}^1$ has codimension $c = 2$ in $\mathbb{P}^3$. The formula gives

$$
h^{p,q}(\operatorname{Bl}_C(\mathbb{P}^3)) = h^{p,q}(\mathbb{P}^3) + h^{p-1,q-1}(\mathbb{P}^1).

$$

**Hodge numbers of the ingredients.** For projective spaces, $h^{p,p}(\mathbb{P}^n) = 1$ for $0 \le p \le n$ and all other Hodge numbers vanish. In tabular form:

| $(p,q)$ | $h^{p,q}(\mathbb{P}^3)$ | $h^{p-1,q-1}(\mathbb{P}^1)$ | $h^{p,q}(\operatorname{Bl}_C(\mathbb{P}^3))$ |
|---------|-------------------------|------------------------------|----------------------------------------------|
| $(0,0)$ | $1$ | $0$ | $1$ |
| $(1,1)$ | $1$ | $1$ | $2$ |
| $(2,2)$ | $1$ | $1$ | $2$ |
| $(3,3)$ | $1$ | $0$ | $1$ |
| all other | $0$ | $0$ | $0$ |

The entry $h^{p-1,q-1}(\mathbb{P}^1)$ contributes when $(p-1,q-1) \in \{(0,0),(1,1)\}$, i.e., at $(p,q) = (1,1)$ and $(2,2)$. For $p \neq q$, both summands vanish since $\mathbb{P}^3$ and $\mathbb{P}^1$ have $h^{p,q} = 0$ for $p \neq q$.

**The Hodge diamond of $\operatorname{Bl}_C(\mathbb{P}^3)$.** Assembling the results:

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

The Betti numbers are $b_0 = b_6 = 1$, $b_1 = b_5 = 0$, $b_2 = b_4 = 2$, $b_3 = 0$, giving Euler characteristic $\chi = 1 + 2 + 2 + 1 = 6$.

**The exceptional divisor.** The exceptional divisor $E = \mathbb{P}(N_{C/\mathbb{P}^3})$ is the projectivization of the normal bundle of $C$ in $\mathbb{P}^3$. For the twisted cubic, the normal bundle is $N_{C/\mathbb{P}^3} \cong \mathcal{O}_{\mathbb{P}^1}(5) \oplus \mathcal{O}_{\mathbb{P}^1}(1)$, which can be computed from the conormal exact sequence

$$
0 \to N_{C/\mathbb{P}^3}^{\vee} \to \Omega_{\mathbb{P}^3}|_C \to \Omega_C \to 0

$$

using $\Omega_C \cong \mathcal{O}_{\mathbb{P}^1}(-2)$ and $c_1(\Omega_{\mathbb{P}^3}|_C) = -4 \cdot 3 = -12$ (restricting $\mathcal{O}(-4)$ along the degree 3 embedding), so $\deg(N_{C/\mathbb{P}^3}^{\vee}) = -12 + 2 = -10$ and $\deg(N_{C/\mathbb{P}^3}) = 10 - 4 = 6$. The splitting type $\mathcal{O}(5) \oplus \mathcal{O}(1)$ is determined by the fact that $H^0(N_{C/\mathbb{P}^3}(-2))$ is nonzero (from the deformation theory of the twisted cubic), forcing the minimum summand degree to be at least 1. Since $5 + 1 = 6$, this determines the splitting.

The surface $E = \mathbb{P}(\mathcal{O}(5) \oplus \mathcal{O}(1))$ is the Hirzebruch surface $\mathbb{F}_4$. All Hirzebruch surfaces have the same Hodge numbers: $h^{0,0} = h^{2,2} = 1$, $h^{1,1} = 2$, and all other $h^{p,q} = 0$.

**Verification via $\chi^{p,q}$-additivity.** The Hodge--Euler numbers $\chi^{p,q} = (-1)^{p+q} h^{p,q}$ satisfy the additivity relation

$$
\chi^{p,q}(\operatorname{Bl}_Z(X)) = \chi^{p,q}(X) + \chi^{p,q}(E) - \chi^{p,q}(Z)

$$

for a blow-up with exceptional divisor $E$ lying over center $Z$. Checking at $(p,q) = (1,1)$: $\chi^{1,1} = h^{1,1}$, and the formula gives $1 + 2 - 1 = 2$, consistent with the direct computation. At $(p,q) = (2,2)$: $1 + 1 - 0 = 2$ (since $\mathbb{P}^1$ has no $(2,2)$-class but $\mathbb{P}^3$ contributes $h^{2,2} = 1$ and $E \cong \mathbb{F}_4$ contributes $h^{2,2} = 1$), also consistent.

**Geometric interpretation.** The increase of $h^{1,1}$ from 1 to 2 reflects the new algebraic cycle class $[E] \in H^{1,1}(\operatorname{Bl}_C(\mathbb{P}^3))$ contributed by the exceptional divisor. Since $C$ is rational, no new odd-dimensional cohomology is introduced, and the Hodge structure remains pure of type $(p,p)$.

<!-- BENCHMARK_PROBLEM: Let C be the twisted cubic in P^3 over the complex numbers. Compute h^{1,1} of the blow-up Bl_C(P^3). Show your work using the blow-up formula for Hodge numbers, identifying the codimension of C and the Hodge numbers of the ingredients. -->

### Remark: Reference {#ecag-0232}

The computations in this section follow the methods detailed in Donu Arapura's notes, [Computations of some Hodge numbers](http://www.math.purdue.edu/~dvb/preprints/book-chap17.pdf), which provide a systematic treatment of Hodge number calculations for blow-ups, fibrations, and related constructions. In particular, Chapter 17 of those notes covers the additivity of Hodge--Euler characteristics and the blow-up formula for Hodge numbers. See also Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Section 7.3.3, for the general blow-up formula.

<!-- BENCHMARK_PROBLEM: State the blow-up formula for Hodge numbers: if X is a smooth projective variety of dimension d and Z is a smooth subvariety of codimension c >= 2, express h^{p,q}(Bl_Z(X)) in terms of h^{p,q}(X) and h^{*,*}(Z). -->
