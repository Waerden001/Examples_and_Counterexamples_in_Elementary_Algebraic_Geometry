---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/local_global.tex
---

### Example: Hartshorne, Example $\mathrm{III}.10.0.2$ {#ecag-0157}

**Statement:** Let $f : X \to Y$ be a morphism of schemes with $X$ integral and Noetherian, and let $\Omega_{X/Y}$ be the sheaf of relative Kahler differentials. Then $\Omega_{X/Y}$ is locally free of rank $n$ if and only if for every point $x \in X$,

$$
\dim_{k(x)} \Omega_{X/Y} \otimes_{\mathcal{O}_{X,x}} k(x) = n.

$$

Moreover, if $\Omega_{X/Y}$ happens to be flat over $X$, this equivalence can also be deduced from the cohomology and base change theorem applied to the identity morphism $\operatorname{id} : X \to X$.

**Construction/Proof:**

The forward direction is immediate: if $\Omega_{X/Y}$ is locally free of rank $n$, then at every point $x \in X$ the fiber $\Omega_{X/Y} \otimes k(x) \cong k(x)^n$ has dimension $n$.

For the converse, since $X$ is integral and Noetherian, the sheaf $\Omega_{X/Y}$ is coherent. At each point $x \in X$, the assumption $\dim_{k(x)} \Omega_{X/Y} \otimes k(x) = n$ means that $\Omega_{X/Y,x}$ requires exactly $n$ generators as an $\mathcal{O}_{X,x}$-module, by Nakayama's lemma. Since $X$ is integral, the generic rank of $\Omega_{X/Y}$ is constant, and the constancy of fiber dimension $n$ at every point forces $\Omega_{X/Y}$ to be locally free of rank $n$. (This is a standard result: a coherent sheaf on an integral Noetherian scheme with constant fiber dimension is locally free.)

*Alternative viewpoint via cohomology and base change.* Consider the identity morphism $\operatorname{id} : X \to X$ and the sheaf $\mathscr{F} = \Omega_{X/Y}$ on $X$. If $\Omega_{X/Y}$ is flat over $X$ (via $\operatorname{id}$, this simply means flat as an $\mathcal{O}_X$-module), then the cohomology and base change theorem (Hartshorne III.12.11, or Grauert's theorem in the proper case) guarantees that the natural map

$$
\varphi^0(x) : R^0(\operatorname{id})_*(\Omega_{X/Y}) \otimes k(x) \longrightarrow H^0(X_x, \Omega_{X/Y}|_{X_x})

$$

is an isomorphism for all $x$. Since $R^0(\operatorname{id})_* \Omega_{X/Y} = \Omega_{X/Y}$ and the fiber over $x$ under $\operatorname{id}$ is $\operatorname{Spec} k(x)$, this reduces to saying $\Omega_{X/Y} \otimes k(x)$ has constant dimension $n$, which by the base change theorem implies $\Omega_{X/Y}$ is locally free. Note that the flatness assumption on $\Omega_{X/Y}$ is the key additional hypothesis; on an integral Noetherian scheme, flatness of a coherent sheaf is equivalent to local freeness, so this alternative argument is somewhat circular but illustrates the mechanism of the base change theorem.

**Key Insight:** The constancy of fiber dimension characterizes local freeness for coherent sheaves on integral Noetherian schemes. The observation that the cohomology and base change theorem (applied to the identity morphism) recovers this classical fact highlights how the base change machinery subsumes pointwise-to-global upgrade results.

**Prerequisites:** Coherent sheaves, Nakayama's lemma, Kahler differentials, locally free sheaves, cohomology and base change theorem, flatness

<!-- BENCHMARK_PROBLEM: Let X be an integral Noetherian scheme and F a coherent sheaf on X. If dim_{k(x)} F tensor k(x) = n for all x in X, is F necessarily locally free of rank n? Justify your answer, stating clearly what hypotheses on X are needed. -->
