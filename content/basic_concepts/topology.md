---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/topology.tex
---

## Topology
### \'{Etale  related}

### Example: \'{E}tale fundamental group of the nodal curve $y^{2}=x^{2}(x+1)$ {#ecag-0179}

> **Status:** Stub — content needed.

### Example: Hartshorne $\mathrm{III}.10.5$, \'{e}tale locally free implies Zariski locally free {#ecag-0180}

The proof is not hard, but let me ask 

- why do we need the \'{e}tale condition?
- where do we need to use the Nakayama's lemma?

For the first question, the answer is we can get a short exact sequence 
$$0\rightarrow f^{*}\mathrm{kernel}\rightarrow \mathcal{O}_{U}^{r}\rightarrow \mathscr{F}\rightarrow 0$$
so you know we actually only need the flatness. For the second question , we have
$$0\rightarrow f^{*}\mathrm{kernel} \otimes k(x)\rightarrow \mathcal{O}_{U,x}^{r}\otimes k(x)\rightarrow f^{*}\mathscr{F}\otimes k(x)\rightarrow 0.$$
And use Nakayama's theorem, and the freeness of $f^{*}\mathscr{F}$, we know $f^{*}\mathrm{kernel} \otimes k(x)=0$. Then we get $f^{*}\mathrm{kernel} =0$, if $f$ is faithfully flat, we can get $\mathrm{kernel}=0$ directly, but here we don't need it, because firbre, we know $\mathcal{O}_{U,x}^{r}\rightarrow f^{*}\mathscr{F}$ is an isomorphism, so actually the original $\mathcal{O}_{X}^{r}\rightarrow \mathscr{F}\rightarrow 0$ is an isomorphism fibrewise. Then we know $f^{*}\mathscr{F}$ is locally free.

### Example: $\mathbb{A}^{1}$ is not algebraically simply connected {#ecag-0181}

Consider the Artin–Schreier map.

### Remark: $\mathbb{P}_{K}^{1}$ is algebraically simply connected {#ecag-0182}

Note that we need conditions like $K$ is separably closed. See for example [Galois theory for schemes](http://websites.math.leidenuniv.nl/algebra/GSchemes.pdf).

### Remark: Sheaf cohomology, Zariski topology,  étale topology {#ecag-0183}

Note the following facts
 
- Grothendieck vanishing theorem is true for Noetherian topological spaces(in Zariski topology) and sheaves of abelian groups. 
 $$H^{2}_{Zar}(\mathbb{P}^{1},\underline{k})=0, H^{2}_{ét}(\mathbb{P}^{1}, \underline{k})\cong k.$$
- Čech cohomology also relies on the topology. For example, $\mathbb{P}^{1}=U_{0}\cap U_{1}$. If we want to compute the Čech cohomology, we have two difficulties
 
- this cover is not fine, no matter in Zariski topology or étale topology. This is not an issue, because we can use spectral sequence to compute $H^{2}(X,\underline{k})$
