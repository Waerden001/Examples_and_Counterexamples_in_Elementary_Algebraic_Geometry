---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/monad.tex
---

## Monad on Hirzebruch surfaces
Let $\pi: \Sigma_{n}=\mathbf{P}(\mathcal{E}^{\vee})=\mathbf{P}(\mathcal{O}\oplus \mathcal{O}(-n))\rightarrow \mathbf{P}^1$ be the $n$-th Hirzebruch surfaces.  Let $H=c_{1}(\mathcal{O}_{\Sigma_{n}}(1))$, $E$ be the class of $\mathbf{P}(\mathcal{O}(-n))$, its self-intersection equals to $-n$, $F$ be a fiber class of $\pi$. We have $E=H-nF$. The Chow ring of $\Sigma_{n}$ is given by $A(\Sigma_{n})=A[\mathbf{P}^1][H]/(H^{2}-nFH)=\mathbf{Z}[F, H]/(F^2, H^{2}-nFH)$, naturally one has $\operatorname{Pic}(\Sigma_{n})=\mathbf{Z} H\oplus \mathbf{Z} F$. From now on, we denote $\mathcal{E}(p,q)=\mathcal{E}\otimes\mathcal{O}_{\Sigma_{n}}(pH+qF)$ for any sheaf of $\mathcal{O}_{\Sigma_{n}}$-modules. Recall that the relative Euler sequence computes the relative canonical sheaf

$$0\rightarrow \mathcal{O}_{\Sigma_{n}}(-1, 0)\rightarrow \pi^{*}(\mathcal{E}^{\vee})\rightarrow T_{\Sigma_{n}/\mathbf{P}^1}(-1,0)\rightarrow 0.$$

\begin{align*}\Omega_{\Sigma_{n}/\mathbf{P}^1}&=\mathcal{O}_{\Sigma_{n}}(-2, 0)\otimes \pi^{*}(\det \mathcal{E})=\mathcal{O}_{\Sigma_{n}}(-2,n)\\
T_{\Sigma_{n}/\mathbf{P}^1}&=\mathcal{O}_{\Sigma_{n}}(2,-n)\\
\omega_{\Sigma_{n}}&=\mathcal{O}_{\Sigma_{n}}(-2, n-2).\end{align*}
For later computations, we need the following lemmata.

### Lemma {#ecag-0240}

The cohomology of any line bundle $\mathcal{O}_{\Sigma_n}(p,q)$ on the Hirzebruch surface $\Sigma_n$ is completely determined by the integers $p$, $q$, and $n$ through the projection $\pi:\Sigma_n\to\mathbf{P}^1$. Since $\Sigma_n = \mathbf{P}(\mathcal{O}\oplus\mathcal{O}(-n))$, the higher direct images of $\mathcal{O}_{\Sigma_n}(p)$ along fibers of $\pi$ reduce the problem to cohomology on $\mathbf{P}^1$.

**Direct image computation.** For $p \geq 0$, the projection formula gives

$$
\pi_*\mathcal{O}_{\Sigma_n}(p,q) = \operatorname{Sym}^p(\mathcal{O}\oplus\mathcal{O}(-n))\otimes\mathcal{O}_{\mathbf{P}^1}(q) = \bigoplus_{j=0}^{p}\mathcal{O}_{\mathbf{P}^1}(q-jn),

$$

while $\pi_*\mathcal{O}_{\Sigma_n}(p,q) = 0$ for $p < 0$ and $R^1\pi_*\mathcal{O}_{\Sigma_n}(p,q) = 0$ for $p \geq -1$.

**$\mathrm{H}^0$ criterion.** By the Leray spectral sequence, $\mathrm{H}^0(\Sigma_n, \mathcal{O}(p,q)) = \mathrm{H}^0(\mathbf{P}^1, \pi_*\mathcal{O}(p,q))$. This is nonzero precisely when $p \geq 0$ and at least one summand $\mathcal{O}_{\mathbf{P}^1}(q - jn)$ has nonnegative degree for some $0 \leq j \leq p$, which amounts to $np + q \geq 0$. Hence

$$
\mathrm{H}^{0}(\mathcal{O}_{\Sigma_{n}}(p, q))\neq 0 \quad\text{if and only if}\quad p\geq 0 \;\text{ and }\; np+q\geq 0.

$$

**$\mathrm{H}^2$ by Serre duality.** Since $\omega_{\Sigma_n} = \mathcal{O}(-2, n-2)$, Serre duality gives $\mathrm{H}^2(\mathcal{O}(p,q)) = \mathrm{H}^0(\mathcal{O}(-p-2, n-2-q))^{\vee}$. Applying the $\mathrm{H}^0$ criterion to the dual: $-p-2 \geq 0$ and $n(-p-2) + (n-2-q) \geq 0$, i.e.,

$$
\mathrm{H}^{2}(\mathcal{O}_{\Sigma_{n}}(p, q))\neq 0 \quad\text{if and only if}\quad p\leq -2 \;\text{ and }\; np+q\leq -(n+2).

$$

**$\mathrm{H}^1$ by exclusion.** The Euler characteristic from Riemann--Roch on $\Sigma_n$ is $\chi(\mathcal{O}(p,q)) = \tfrac{1}{2}(p+1)(np+2q+2)$. Since $\mathrm{H}^1$ is determined by $\chi - h^0 + h^2$, the region where $\mathrm{H}^1 \neq 0$ consists of exactly two disjoint components:

$$
\mathrm{H}^{1}(\mathcal{O}_{\Sigma_{n}}(p, q))\neq 0 \quad\text{if and only if}\quad \begin{cases}p\geq 0,\; q\leq -2\end{cases} \;\text{ or }\; \begin{cases}p\leq -2,\; q\geq n.\end{cases}

$$

The first region corresponds to contributions from $R^0\pi_*$ summands of negative degree on $\mathbf{P}^1$ (specifically $\mathrm{H}^1(\mathbf{P}^1, \mathcal{O}(q-jn))$ for $j$ with $q - jn \leq -2$). The second region comes from $R^1\pi_*$ when $p \leq -2$, which by relative Serre duality contributes $\mathrm{H}^0$ of a bundle on $\mathbf{P}^1$ of sufficiently positive degree.

<!-- BENCHMARK_PROBLEM: On the Hirzebruch surface $\Sigma_2$, determine all pairs $(p,q)\in\mathbf{Z}^2$ with $-3\leq p\leq 3$ and $-5\leq q\leq 5$ for which $\mathrm{H}^1(\mathcal{O}_{\Sigma_2}(p,q))\neq 0$. -->

The classical Beilinson spectral sequence is a way to describe torsion-free sheaves on $\mathbf{P}^2$ as the cohomology of certain three-term complexes---the so-called monad. With the isomorphism between the Hilbert scheme of points on $\mathbf{C}^2$ and the moduli space of rank $1$ torsion-free sheaves on $\mathbf{P}^2$ which are trivial over infinity, the Hilbert scheme can be realized as the quiver variety with one vertex and one loop, see \cite[Theorem 2.1]{Nakajima}. The essential part of the construction is a resolution of the diagonal in $\mathbf{P}^2\times \mathbf{P}^2$. For Hirzebruch surfaces, the diagonal can also be resolved(for references to the details of the construction , we refer to [\cite{Buchdahl1987}] or [\cite{Aprodu09}]). We first briefly recall the Beilinson-type spectral sequence on $\Sigma_{n}$, following the approach in [\cite{Nakajima}] we give a monad description of $\operatorname{Hilb}(T^*\mathbf{P}^1)$ as a Nakajima quiver variety of type $A_{1}^{(1)}$, and we show that the two tautological bundles corresponding to the two vertices are exactly $\mathcal{O}_{X}(1)^{[n]}$ and $\mathcal{O}_{X}^{[n]}$.
.
We denote $p_{i}:\Sigma_{n}\times \Sigma_{n}$ be the projections to the two factors, $p: X\times X\rightarrow \mathbf{P}^1\times \mathbf{P}^1$ be the product of the ruling $\pi$. Let $\Delta_{\mathbf{P}^1}\subset \mathbf{P}^1\times \mathbf{P}^1$ be the diagonal divisor on $\mathbf{P}^1\times \mathbf{P}^1$ and $\Delta$ be the diagonal divisor on $\Sigma_{n}\times \Sigma_{n}$, $L= \mathcal{O}_{\mathbf{P}^1\times \mathbf{P}^1}(\Delta_{\mathbf{P}^1})$. Consider the line bundle

$$\mathcal{F} = p_{1}^{*}(T_{\Sigma_{n}/\mathbf{P}^1}(-1, 0))\otimes p_{2}^{*}(\mathcal{O}_{\Sigma_{n}}(1, 0))=\mathcal{O}_{\Sigma_{n}}(1,-n)\boxtimes \mathcal{O}_{\Sigma_{n}}(1, 0).$$

A rank $2$ locally free sheaf $\mathcal{G}$ is defined by an extension

$$0\rightarrow \mathcal{F}\rightarrow \mathcal{G}\rightarrow p^{*}(L)\rightarrow 0.$$

Note that $p^{*}(L)=\mathcal{O}_{\Sigma_{n}}(0,1)\boxtimes \mathcal{O}_{\Sigma_{n}}(0,1)$.
Buchdahl proved that[\cite{Buchdahl1987}] the diagonal $\Delta$ can be realized as the zero locus of a global section $s$ of $\mathcal{G}$, then the Koszul complex of $s$ gives us the resolution of the diagonal $C^{\bullet}\twoheadrightarrow\mathcal{O}_{\Delta}$:

$$0\rightarrow \wedge^{2}\mathcal{G}^{\vee}\rightarrow \mathcal{G}^{\vee}\xrightarrow{s} \mathcal{O}_{\Sigma_{n}\times \Sigma_{n}}\rightarrow \mathcal{O}_{\Delta}\rightarrow 0.$$

Then the Beilinson spectral sequences comes from different ways of computing the image of $p_{1}^{*}\mathcal{E}$ under the composite functor $p_{2*}(\mathcal{O}_{\Delta}\otimes -)$ . On the one hand, we trivially have $p_{2*}(\mathcal{O}_{\Delta}\otimes p_{1}^{*}\mathcal{E})=\mathcal{E}$. If we take the cohomology of $C^{\bullet}$ first in the double complex for the hyper direct image $\mathbf{R}^{\bullet}p_{2*}(C^{\bullet}\otimes p_{1}^{*}\mathcal{E})$, the trivial identity tells us exactly that the corresponding spectral sequence degenerate at the $E_{2}$ page, namely
$$E_{2}^{p,q}=R^{q}p_{2*}(\mathrm{H}^{p}(C^{\bullet}\otimes p_{1}^{*}\mathcal{E}))=\begin{cases}\mathcal{E} &  (p,q)=(0,0)\\
0 & \text{otherwise }\end{cases}.$$
On the other hand, we can also take the direct image first, then we get the so-called Beilinson spectral sequence for $\Sigma_{n}$.

### Theorem: Buchdahl {#ecag-0241}

For any torsion-free sheaf $\mathcal{E}$ on the Hirzebruch surface $\Sigma_n$, the two spectral sequences of the double complex $\mathbf{R}p_{2*}(C^\bullet \otimes p_1^*\mathcal{E})$ produce a Beilinson-type spectral sequence

$$
E_{1}^{p,q} = R^{q}p_{2*}(\wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}) \Rightarrow \begin{cases}\mathcal{E} & p+q=0\\ 0 & \text{otherwise}\end{cases},

$$

where $\mathcal{G}$ is the rank-$2$ bundle on $\Sigma_n \times \Sigma_n$ constructed from Buchdahl's resolution of the diagonal, and $p_1, p_2$ are the two projections.

The argument is a direct application of the two filtrations of a double complex. Buchdahl's resolution provides a Koszul complex $C^\bullet \to \mathcal{O}_\Delta$ on $\Sigma_n \times \Sigma_n$, which when tensored with $p_1^*\mathcal{E}$ (exact since the Koszul terms are locally free) gives a double complex $C^\bullet \otimes p_1^*\mathcal{E}$. The first filtration --- taking cohomology of $C^\bullet$ first --- sees only $\mathcal{O}_\Delta \otimes p_1^*\mathcal{E}$ in degree $0$, whose pushforward under $p_2$ is $\mathcal{E}$ itself, so this spectral sequence degenerates immediately at $E_2$ with abutment $\mathcal{E}$ in bidegree $(0,0)$. The second filtration --- taking $Rp_{2*}$ first --- produces the $E_1$-page $E_1^{p,q} = R^q p_{2*}(\wedge^{-p}\mathcal{G}^\vee \otimes p_1^*\mathcal{E})$, supported in the range $-2 \leq p \leq 0$ and $0 \leq q \leq 2$ (since $\mathcal{G}$ has rank $2$ and $\Sigma_n$ is a surface). Both spectral sequences converge to the same abutment, establishing the theorem.

The $E_1$-page has three columns: $p = 0$ corresponds to $\wedge^0 \mathcal{G}^\vee = \mathcal{O}$, $p = -1$ to $\mathcal{G}^\vee$, and $p = -2$ to $\wedge^2 \mathcal{G}^\vee = \det(\mathcal{G}^\vee)$.

<!-- BENCHMARK_PROBLEM: For the Beilinson spectral sequence on $\Sigma_n$, the $E_1$-page has entries $E_1^{p,q}$ for $-2\leq p\leq 0$ and $0\leq q\leq 2$. Explain why the spectral sequence is supported in this range, and identify which exterior power $\wedge^{-p}\mathcal{G}^\vee$ contributes to each column $p\in\{-2,-1,0\}$. -->

### Remark {#ecag-0242}

Buchdahl originally stated the spectral sequence for locally free sheaves, but the same argument extends to torsion-free sheaves without modification: tensoring with $p_1^*\mathcal{E}$ preserves exactness of the Koszul complex because its terms are locally free on $\Sigma_n \times \Sigma_n$, so no flatness assumption on $\mathcal{E}$ is needed.

There is also an asymmetry in the construction. One may use either $p_{1*}(p_2^*\mathcal{E} \otimes \mathcal{O}_\Delta)$ or $p_{2*}(p_1^*\mathcal{E} \otimes \mathcal{O}_\Delta)$ to produce the spectral sequence, and these two choices generally yield different $E_1$-pages. The convention above (using $p_{2*}$ and $p_1^*\mathcal{E}$) is preferred because the bundle $\mathcal{G}$ involves $T_{\Sigma_n/\mathbf{P}^1}(-1,0)$ pulled back from the first factor, which interacts favorably with the cohomology vanishing from the line bundle lemma to produce better vanishing on the $E_1$-page.

To compute the $E_1$-terms explicitly, take the exterior powers of the dual of the defining sequence of $\mathcal{G}$ and tensor with $p_1^*\mathcal{E}$. Since $\mathcal{E}$ is torsion-free, $-\otimes p_1^*\mathcal{E}$ is exact, giving

$$0\rightarrow \wedge^{-p-1}\mathcal{F}^{\vee}\otimes p^{*}(L^{\vee})\otimes p_{1}^{*}\mathcal{E}\rightarrow \wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}\rightarrow \wedge^{-p}\mathcal{F}^{\vee}\otimes p_{1}^{*}\mathcal{E}\rightarrow 0.$$

For $p = 0$, the first sheaf vanishes and $\wedge^0\mathcal{G}^\vee \otimes p_1^*\mathcal{E} = p_1^*\mathcal{E}$. For $p = -2$, the last sheaf vanishes and $\wedge^2\mathcal{G}^\vee \otimes p_1^*\mathcal{E} = \mathcal{E}(-1,n-1) \boxtimes \mathcal{O}_{\Sigma_n}(-1,-1)$. Taking the associated long exact sequences in higher direct images yields

\begin{align}
&E_{1}^{0,q}= \mathrm{H}^{q}(\mathcal{E})\otimes \mathcal{O}_{\Sigma_{n}}(0,0)\\
\dots\rightarrow \mathrm{H}^{q}(\mathcal{E}(0, -1))\otimes \mathcal{O}_{\Sigma_{n}}(0, -1)\rightarrow &E_{1}^{-1, q}\rightarrow \mathrm{H}^{q}(\mathcal{E}(-1, n))\otimes \mathcal{O}_{\Sigma_{n}}(-1, 0)\rightarrow \dots \\
&E_{1}^{-2, q}= \mathrm{H}^{q}(\mathcal{E}(-1, n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1).
\end{align}

<!-- BENCHMARK_PROBLEM: On $\Sigma_n$, explain why using $p_{2*}(p_1^*\mathcal{E}\otimes\mathcal{O}_\Delta)$ rather than $p_{1*}(p_2^*\mathcal{E}\otimes\mathcal{O}_\Delta)$ gives better vanishing on the $E_1$-page of the Beilinson spectral sequence. Which specific cohomology groups vanish in one convention but not necessarily in the other? -->

### Lemma {#ecag-0243}

Let $\mathcal{E}$ be a torsion-free sheaf on $\Sigma_n$ that is trivial at infinity, meaning $\mathcal{E}|_E \cong \mathcal{O}_E^{\oplus r}$ where $E$ is the negative section. The triviality condition controls the fiberwise splitting type and forces cohomological vanishing in two complementary ranges:

$$
\mathrm{H}^{0}(\mathcal{E}(p,q))=0 \quad \text{for } np+q\leq -1,

$$

$$
\mathrm{H}^{2}(\mathcal{E}(p,q))=0 \quad \text{for } np+q\geq -(n+1).

$$

For the $\mathrm{H}^0$ vanishing, restrict to a general fiber $F \cong \mathbf{P}^1$ of $\pi$. On each fiber, the restriction $\mathcal{E}(p,q)|_F$ has degree $np + q$ (since $H \cdot F = 1$ and $F \cdot F = 0$). Since $\mathcal{E}$ is trivial at infinity, the splitting type on each fiber is nonnegative, so $\mathcal{E}|_F \cong \bigoplus \mathcal{O}_{\mathbf{P}^1}(a_i)$ with each $a_i \geq 0$. When $np + q \leq -1$, the total degree is negative, so every summand $\mathcal{O}_{\mathbf{P}^1}(a_i + np + q)$ has $a_i + np + q \leq a_i - 1$, and for generic fibers $a_i = 0$, giving degree $\leq -1$. Thus any global section restricts to zero on every fiber, and $\pi_*\mathcal{E}(p,q) = 0$ forces $\mathrm{H}^0(\mathcal{E}(p,q)) = 0$.

For the $\mathrm{H}^2$ vanishing, Serre duality gives $\mathrm{H}^2(\mathcal{E}(p,q)) = \mathrm{H}^0(\mathcal{E}^\vee(-p-2, n-2-q))^\vee$ using $\omega_{\Sigma_n} = \mathcal{O}(-2,n-2)$. The dual $\mathcal{E}^\vee$ is also trivial at infinity, so the $\mathrm{H}^0$ vanishing applies to $\mathcal{E}^\vee$: we need $n(-p-2) + (n-2-q) \leq -1$, which rearranges to $np + q \geq -(n+1)$.

<!-- BENCHMARK_PROBLEM: Let $\mathcal{E}$ be a rank $2$ torsion-free sheaf on $\Sigma_2$ that is trivial at infinity. For the twist $\mathcal{E}(-1,1)$, verify directly from the vanishing lemma that $\mathrm{H}^0(\mathcal{E}(-1,1))=0$ and $\mathrm{H}^2(\mathcal{E}(-1,1))=0$, and explain why $\mathrm{H}^1(\mathcal{E}(-1,1))$ may be nonzero. -->

### Proposition {#ecag-0244}

A torsion-free sheaf $\mathcal{E}$ on $\Sigma_n$ that is trivial at infinity admits a monad description: it is the cohomology of a three-term complex

$$
0\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(0, -1)\rightarrow E_{1}^{-1, 1}\otimes\mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow  \mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow 0,

$$

where the middle term fits in a split short exact sequence

$$
0 \rightarrow \mathrm{H}^{1}(\mathcal{E}(-1, -1))\otimes\mathcal{O}_{\Sigma_n}(1, -1)\rightarrow E_{1}^{-1, 1}\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2, n))\otimes \mathcal{O}_{\Sigma_{n}}(0, 0)\rightarrow 0.

$$

**Vanishing on the $E_1$-page.** The key step is to apply the Beilinson spectral sequence not to $\mathcal{E}$ but to the twist $\mathcal{E}(-1,0)$. The $E_1$-page for $\mathcal{E}(-1,0)$ is a $3 \times 3$ grid:

| $q\backslash p$ | $p=-2$ | $p=-1$ | $p=0$ |
|---|---|---|---|
| $q=2$ | $\mathrm{H}^{2}(\mathcal{E}(-2,n-1))\otimes\mathcal{O}(-1, -1)$ | $E_{1}^{-1,2}$ | $\mathrm{H}^2(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$ |
| $q=1$ | $\mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1)$ | $E_{1}^{-1,1}$ | $\mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$ |
| $q=0$ | $\mathrm{H}^{0}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1)$ | $E_{1}^{-1,0}$ | $\mathrm{H}^{0}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$ |

We use the vanishing lemma to kill the four corner entries. For $\mathrm{H}^0$: the fiberwise degree of $\mathcal{E}(-2,n-1)$ is $n(-2) + (n-1) = -(n+1) \leq -1$, so $\mathrm{H}^0 = 0$; for $\mathcal{E}(-1,0)$, the fiberwise degree is $-n \leq -1$, so $\mathrm{H}^0 = 0$. For $\mathrm{H}^2$: the fiberwise degree of $\mathcal{E}(-2,n-1)$ is $-(n+1) \geq -(n+1)$, so $\mathrm{H}^2 = 0$; for $\mathcal{E}(-1,0)$, the fiberwise degree is $-n \geq -(n+1)$, so $\mathrm{H}^2 = 0$.

**Degeneration to a monad.** With all four corner entries vanishing, convergence of the spectral sequence forces $E_1^{-1,2} = 0$ and $E_1^{-1,0} = 0$ as well, since these would contribute to total degrees $1$ and $-1$ respectively with no surviving terms to cancel them. Only the $q = 1$ row survives, and the spectral sequence degenerates at $E_1$, expressing $\mathcal{E}(-1,0)$ as the cohomology of

$$
0\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1, -1)\rightarrow E_{1}^{-1, 1}\rightarrow  \mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}\rightarrow 0.

$$

Tensoring with $\mathcal{O}_{\Sigma_n}(1,0)$ yields the first statement.

**Splitting of the middle term.** The vanishing lemma also gives $\mathrm{H}^0(\mathcal{E}(-1,-1)) = 0$ (fiberwise degree $-(n+1) \leq -1$) and $\mathrm{H}^2(\mathcal{E}(-1,-1)) = 0$ (fiberwise degree $-(n+1)$, boundary). The long exact sequence from the exterior power filtration then degenerates to the claimed short exact sequence for $E_1^{-1,1} \otimes \mathcal{O}_{\Sigma_n}(1,0)$. This sequence splits because the relevant Ext group vanishes: $\operatorname{Ext}^1(\mathcal{O}_{\Sigma_n}, \mathcal{O}_{\Sigma_n}(1,-1)) = \mathrm{H}^1(\mathcal{O}_{\Sigma_n}(1,-1))$, and by the line bundle cohomology lemma, $\mathrm{H}^1(\mathcal{O}_{\Sigma_n}(1,-1))$ requires either $\{p \geq 0, q \leq -2\}$ or $\{p \leq -2, q \geq n\}$. With $p = 1$ and $q = -1$, neither condition holds, so the Ext group vanishes and the sequence splits.

The essential point is that the twist by $\mathcal{O}(-1,0)$ is precisely what makes all four corner entries of the $E_1$-page vanish simultaneously, forcing the spectral sequence to collapse to a single row and producing the monad.

<!-- BENCHMARK_PROBLEM: In the monad description for a torsion-free sheaf $\mathcal{E}$ on $\Sigma_n$ trivial at infinity, the middle term splits as $\mathrm{H}^1(\mathcal{E}(-1,-1))\otimes\mathcal{O}_{\Sigma_n}(1,-1)\oplus\mathrm{H}^1(\mathcal{E}(-2,n))\otimes\mathcal{O}_{\Sigma_n}$. Verify the splitting by computing $\operatorname{Ext}^1(\mathcal{O}_{\Sigma_n}, \mathcal{O}_{\Sigma_n}(1,-1))$ using the cohomology of line bundles on $\Sigma_n$, and identify for which values of $n$ this Ext group vanishes. -->
