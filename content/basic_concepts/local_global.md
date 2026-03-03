---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/local_global.tex
---

### Example: Hartshorne, Example $\mathrm{III}.10.0.2$ {#ecag-0157}

Let $f : X \to Y$ be a morphism of schemes with $X$ integral and Noetherian, and let $\Omega_{X/Y}$ denote the sheaf of relative Kähler differentials. The claim is that $\Omega_{X/Y}$ is locally free of rank $n$ if and only if the fiber dimension is constant:

$$
\dim_{k(x)} \Omega_{X/Y} \otimes_{\mathcal{O}_{X,x}} k(x) = n \quad \text{for every } x \in X.
$$

**The forward direction.** If $\Omega_{X/Y} \cong \mathcal{O}_X^{\oplus n}$ locally, then at every point $x \in X$ the fiber $\Omega_{X/Y} \otimes k(x) \cong k(x)^n$ has dimension $n$. This is immediate.

**The converse.** Since $X$ is Noetherian and $f$ is a morphism of schemes, $\Omega_{X/Y}$ is a coherent $\mathcal{O}_X$-module. At each point $x \in X$, the hypothesis $\dim_{k(x)} \Omega_{X/Y} \otimes k(x) = n$ means that $\Omega_{X/Y,x}$ requires exactly $n$ generators as an $\mathcal{O}_{X,x}$-module, by Nakayama's lemma. By choosing lifts of a basis for the fiber, we obtain a surjection $\mathcal{O}_{X,x}^n \twoheadrightarrow \Omega_{X/Y,x}$ in a neighborhood of $x$.

The key input is that $X$ is integral. The generic stalk $\Omega_{X/Y,\eta}$ is a vector space over the function field $K(X)$, and the constant fiber dimension forces $\operatorname{rank}_{K(X)} \Omega_{X/Y,\eta} = n$. At every point $x$, the surjection $\mathcal{O}_{X,x}^n \twoheadrightarrow \Omega_{X/Y,x}$ must then be an isomorphism: its kernel $K_x$ satisfies $K_x \otimes K(X) = 0$ (since the generic rank is already $n$), and on an integral Noetherian scheme a coherent subsheaf of a free module with zero generic stalk is itself zero. This establishes local freeness of rank $n$.

This is a standard and useful fact: a coherent sheaf on an integral Noetherian scheme with constant fiber dimension is locally free. (See, e.g., Hartshorne II, Exercise 5.8 or Vakil, Theorem 13.7.2.)

**Reinterpretation via cohomology and base change.** There is an instructive (if circular) way to recover the same conclusion from the base change machinery. Consider the identity morphism $\operatorname{id} : X \to X$ and the coherent sheaf $\mathscr{F} = \Omega_{X/Y}$. If $\Omega_{X/Y}$ is flat over $\mathcal{O}_X$ (via $\operatorname{id}$, this simply means flat as an $\mathcal{O}_X$-module), then the base change theorem (Hartshorne III.12.11, or Grauert's theorem in the proper case) guarantees that the natural map

$$
\varphi^0(x) : R^0(\operatorname{id})_*(\Omega_{X/Y}) \otimes k(x) \longrightarrow H^0(X_x, \Omega_{X/Y}|_{X_x})
$$

is an isomorphism for all $x$. Since $R^0(\operatorname{id})_* \Omega_{X/Y} = \Omega_{X/Y}$ and the fiber of $\operatorname{id}$ over $x$ is $\operatorname{Spec} k(x)$, the right-hand side is $\Omega_{X/Y} \otimes k(x)$. By the semicontinuity theorem, the constancy of $\dim_{k(x)} \Omega_{X/Y} \otimes k(x)$ then implies that $R^0(\operatorname{id})_*(\Omega_{X/Y}) = \Omega_{X/Y}$ is locally free.

The circularity is worth noting explicitly: on an integral Noetherian scheme, a coherent sheaf is flat if and only if it is locally free. So assuming flatness to deduce local freeness invokes the conclusion as a hypothesis. Nevertheless, this reformulation illustrates how the cohomology and base change theorem subsumes pointwise-to-global upgrade results, and in more general settings (e.g., families over a non-integral base where flatness is a genuine additional hypothesis), the base change approach becomes the essential tool.

<!-- BENCHMARK_PROBLEM: Let X be an integral Noetherian scheme and F a coherent sheaf on X. If dim_{k(x)} F tensor k(x) = n for all x in X, is F necessarily locally free of rank n? Justify your answer, stating clearly what hypotheses on X are needed. -->
