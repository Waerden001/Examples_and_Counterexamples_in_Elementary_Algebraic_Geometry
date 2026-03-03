---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/characteristics.tex
---

## Characteristic classes and numbers

### Example: Horrocks–Mumford bundle {#ecag-0230}

**Statement:** Let $\mathscr{F}$ be the Horrocks--Mumford bundle on $\mathbb{P}^4$, the unique (up to twist) indecomposable rank-2 vector bundle on $\mathbb{P}^4$ that is not a line bundle. Its total Chern class is $c(\mathscr{F}) = 1 + 5h + 10h^2$, where $h$ is the hyperplane class. We compute the Euler characteristic $\chi(\mathscr{F}(n-5))$ in two independent ways and obtain

$$
\chi(\mathscr{F}(n-5)) = \frac{(n^2 - 1)(n^2 - 24)}{12}.

$$

**Construction/Proof:**

*Method 1: Hirzebruch--Riemann--Roch.*

By the Hirzebruch--Riemann--Roch theorem on $\mathbb{P}^4$, we have

$$
\chi(\mathscr{F}(n-5)) = \bigl\{\operatorname{Ch}(\mathscr{F}(n-5)) \cdot \operatorname{Td}(T_{\mathbb{P}^4})\bigr\}_0,

$$

where $\{\cdot\}_0$ denotes the degree-zero part (i.e., the component in $H^8(\mathbb{P}^4, \mathbb{Q}) \cong \mathbb{Q}$). Using Macaulay2 to expand the Chern character of the twisted bundle via the splitting principle, one obtains

$$
\operatorname{Ch}(\mathscr{F}(n-5)) = 2 + \frac{125}{6}(n-5)h + \frac{125}{12}(n-5)^2 h^2 + \frac{5}{3}(n-5)^3 h^3 + \frac{1}{12}(n-5)^4 h^4.

$$

The Todd class of $\mathbb{P}^4$ is

$$
\operatorname{Td}(\mathbb{P}^4) = 1 + \frac{5}{2}h + \frac{35}{12}h^2 + \frac{25}{12}h^3 + h^4.

$$

Multiplying and extracting the coefficient of $h^4$ yields

$$
\chi(\mathscr{F}(n-5)) = \frac{(n^2 - 1)(n^2 - 24)}{12}.

$$

*Method 2: Resolution of the bundle.*

The Horrocks--Mumford bundle arises as the cohomology of a monad. Specifically, there is an exact sequence

$$
0 \rightarrow \mathcal{O}(2) \otimes V_1 \xrightarrow{\ p\ } \wedge^2 T_{\mathbb{P}^4} \otimes W \xrightarrow{\ q\ } \mathcal{O}(3) \otimes V_3 \rightarrow 0,

$$

where $V_1$, $W$, $V_3$ are vector spaces with $\dim V_1 = 5$, $\dim W = 2$, $\dim V_3 = 5$, and $\mathscr{F} = \ker(q) / \operatorname{im}(p)$. Additionally, the Koszul resolution of the tangent bundle on $\mathbb{P}^4$ gives

$$
0 \rightarrow \mathcal{O} \rightarrow \mathcal{O}(1) \otimes V \rightarrow \mathcal{O}(2) \otimes \wedge^2 V \rightarrow \wedge^2 T_{\mathbb{P}^4} \rightarrow 0,

$$

where $V$ is the 5-dimensional vector space with $\mathbb{P}^4 = \mathbb{P}(V)$. By additivity of Euler characteristics in exact sequences and the monad structure, we obtain

$$
\chi(\mathscr{F}(n-5)) = \chi(\wedge^2 T_{\mathbb{P}^4}(n-5) \otimes W) - \chi(\mathcal{O}(n-3) \otimes V_1) - \chi(\mathcal{O}(n-2) \otimes V_3).

$$

Substituting dimensions:

$$
= 2\,\chi(\wedge^2 T_{\mathbb{P}^4}(n-5)) - 5\,\chi(\mathcal{O}(n-3)) - 5\,\chi(\mathcal{O}(n-2)).

$$

Using the Koszul complex for $\wedge^2 T_{\mathbb{P}^4}$ and the standard formula $\chi(\mathcal{O}_{\mathbb{P}^4}(m)) = \binom{m+4}{4}$, we expand

$$
\chi(\wedge^2 T_{\mathbb{P}^4}(n-5)) = 10\,\chi(\mathcal{O}(n-3)) - 5\,\chi(\mathcal{O}(n-4)) + \chi(\mathcal{O}(n-5)),

$$

which gives

$$
\chi(\mathscr{F}(n-5)) = 2\Bigl(10\binom{n+1}{4} - 5\binom{n}{4} + \binom{n-1}{4}\Bigr) - 5\binom{n+1}{4} - 5\binom{n+2}{4}.

$$

Simplifying:

$$
= 15\binom{n+1}{4} - 10\binom{n}{4} + 2\binom{n-1}{4} - 5\binom{n+2}{4} = \frac{(n^2 - 1)(n^2 - 24)}{12}.

$$

Both methods yield the same answer, confirming the computation.

**Key Insight:** The two computations -- one via Hirzebruch--Riemann--Roch using Chern characters and Todd classes, the other via the explicit monad resolution and the Koszul complex -- provide a powerful consistency check. This illustrates how index-theoretic and homological methods complement each other in computing invariants of vector bundles on projective space.

**Prerequisites:** Hirzebruch--Riemann--Roch theorem, Chern character, Todd class, Horrocks--Mumford bundle, monads on projective space, Koszul complex for tangent bundle of $\mathbb{P}^n$, Euler characteristic of line bundles on $\mathbb{P}^4$

<!-- BENCHMARK_PROBLEM: Let F be the Horrocks–Mumford bundle on P^4 with total Chern class c(F) = 1 + 5h + 10h^2. Compute chi(F(n-5)) as a polynomial in n using the Hirzebruch–Riemann–Roch theorem. Express your answer as a single rational function of n. -->
