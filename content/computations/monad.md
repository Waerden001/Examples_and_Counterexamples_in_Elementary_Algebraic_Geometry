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

**Statement:** Let $\Sigma_n$ be the $n$-th Hirzebruch surface with $\operatorname{Pic}(\Sigma_n)=\mathbf{Z}H\oplus\mathbf{Z}F$. Then the cohomology of line bundles $\mathcal{O}_{\Sigma_n}(p,q)$ is determined as follows:

$$
\mathrm{H}^{0}(\mathcal{O}_{\Sigma_{n}}(p, q))\neq 0 \text{ if and only if }\begin{cases}p\geq 0\\ np+q\geq 0\end{cases}

$$

$$
\mathrm{H}^{1}(\mathcal{O}_{\Sigma_{n}}(p, q))\neq 0  \text{ if and only if }  \begin{cases}p\geq 0\\ q\leq -2\end{cases} \text{ or }  \begin{cases}p\leq -2\\q\geq n\end{cases}

$$

$$
\mathrm{H}^{2}(\mathcal{O}_{\Sigma_{n}}(p, q))\neq 0 \text{ if and only if }\begin{cases}p\geq -2\\ np+q\leq -(n+2)\end{cases}.

$$

**Construction/Proof:** The proof proceeds by reducing to computations on $\mathbf{P}^1$ via the projection $\pi:\Sigma_n\to\mathbf{P}^1$.

Step 1. Since $\Sigma_n=\mathbf{P}(\mathcal{O}\oplus\mathcal{O}(-n))$, the projection formula and the relative cohomology of $\mathcal{O}(p)$ on the fibers of $\pi$ give:

$$
\pi_*\mathcal{O}_{\Sigma_n}(p,q)=\operatorname{Sym}^p(\mathcal{O}\oplus\mathcal{O}(-n))\otimes\mathcal{O}_{\mathbf{P}^1}(q)=\bigoplus_{j=0}^{p}\mathcal{O}_{\mathbf{P}^1}(q-jn)

$$

for $p\geq 0$, and $\pi_*\mathcal{O}_{\Sigma_n}(p,q)=0$ for $p<0$, while $R^1\pi_*\mathcal{O}_{\Sigma_n}(p,q)=0$ for $p\geq -1$.

Step 2. For $\mathrm{H}^0$: by the Leray spectral sequence, $\mathrm{H}^0(\Sigma_n,\mathcal{O}(p,q))=\mathrm{H}^0(\mathbf{P}^1,\pi_*\mathcal{O}(p,q))$. This is nonzero precisely when $p\geq 0$ and at least one summand $\mathcal{O}_{\mathbf{P}^1}(q-jn)$ has $q-jn\geq 0$ for some $0\leq j\leq p$, which amounts to $q\geq 0$ (take $j=0$) or more generally $np+q\geq 0$.

Step 3. For $\mathrm{H}^2$: Serre duality on the surface gives $\mathrm{H}^2(\mathcal{O}(p,q))=\mathrm{H}^0(\omega_{\Sigma_n}\otimes\mathcal{O}(-p,-q))^{\vee}=\mathrm{H}^0(\mathcal{O}(-p-2,n-2-q))^{\vee}$. By the criterion for $\mathrm{H}^0$, this is nonzero iff $-p-2\geq 0$ and $n(-p-2)+(n-2-q)\geq 0$, i.e., $p\leq -2$ and $np+q\leq -(n+2)$.

Step 4. For $\mathrm{H}^1$: by the Euler characteristic $\chi(\mathcal{O}(p,q))=\frac{1}{2}(p+1)(np+2q+2)$ (from Riemann--Roch on $\Sigma_n$), the region where $\mathrm{H}^1\neq 0$ is determined by exclusion: it occurs precisely in the two disjoint regions stated, where both $\mathrm{H}^0=0$ and $\mathrm{H}^2=0$ yet $\chi<0$, or where there is a genuine contribution from $R^1\pi_*$.

**Key Insight:** The geometry of $\Sigma_n$ as a $\mathbf{P}^1$-bundle over $\mathbf{P}^1$ reduces all cohomology computations to line bundles on $\mathbf{P}^1$ via the Leray spectral sequence and Serre duality.

**Prerequisites:** Hirzebruch surfaces, Leray spectral sequence, Serre duality, cohomology of line bundles on $\mathbf{P}^1$

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

**Statement:** (Buchdahl) For any torsion-free sheaf $\mathcal{E}$ on the Hirzebruch surface $\Sigma_{n}$, there exists a spectral sequence:

$$
E_{1}^{p,q}=R^{q}p_{2*}(\wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E})\Rightarrow \begin{cases}\mathcal{E} & p+q=0\\
0 & \text{otherwise}\end{cases}.

$$

Here $\mathcal{G}$ is the rank $2$ locally free sheaf on $\Sigma_n\times\Sigma_n$ constructed from the resolution of the diagonal, and $p_1,p_2$ are the two projections.

**Construction/Proof:** The proof is a standard application of the two spectral sequences associated to a double complex.

Step 1. Begin with Buchdahl's resolution of the diagonal: the diagonal $\Delta\subset\Sigma_n\times\Sigma_n$ is the zero locus of a section $s\in\mathrm{H}^0(\mathcal{G})$, yielding the Koszul resolution

$$
0\rightarrow \wedge^{2}\mathcal{G}^{\vee}\rightarrow \mathcal{G}^{\vee}\xrightarrow{s} \mathcal{O}_{\Sigma_{n}\times \Sigma_{n}}\rightarrow \mathcal{O}_{\Delta}\rightarrow 0.

$$

Step 2. For any torsion-free sheaf $\mathcal{E}$ on $\Sigma_n$, tensor the resolution with $p_1^*\mathcal{E}$ (exact since $\mathcal{E}$ is torsion-free and the terms of the Koszul complex are locally free on $\Sigma_n\times\Sigma_n$). This produces a complex $C^\bullet\otimes p_1^*\mathcal{E}$.

Step 3. Compute $\mathbf{R}p_{2*}(C^\bullet\otimes p_1^*\mathcal{E})$ via two different filtrations of the resulting double complex:

- **First filtration** (take cohomology of $C^\bullet$ first): Since $C^\bullet$ is a resolution of $\mathcal{O}_\Delta$, the only nonzero cohomology sheaf is $\mathcal{O}_\Delta\otimes p_1^*\mathcal{E}$ in degree $0$. Its direct image under $p_2$ is simply $\mathcal{E}$, concentrated in bidegree $(0,0)$.

- **Second filtration** (take $Rp_{2*}$ first): This produces the $E_1$-page $E_1^{p,q}=R^qp_{2*}(\wedge^{-p}\mathcal{G}^\vee\otimes p_1^*\mathcal{E})$.

Step 4. Since both spectral sequences converge to the same abutment, the second spectral sequence converges to $\mathcal{E}$ in total degree $0$ and to $0$ in all other total degrees.

**Key Insight:** The Beilinson spectral sequence on $\Sigma_n$ arises from resolving the diagonal via the Koszul complex of a carefully constructed rank $2$ bundle, then exploiting the two filtrations of the associated double complex --- one giving the identity functor, the other giving computable $E_1$-terms.

**Prerequisites:** Koszul complex, Beilinson spectral sequence, resolution of the diagonal, derived pushforward, Hirzebruch surfaces

<!-- BENCHMARK_PROBLEM: For the Beilinson spectral sequence on $\Sigma_n$, the $E_1$-page has entries $E_1^{p,q}$ for $-2\leq p\leq 0$ and $0\leq q\leq 2$. Explain why the spectral sequence is supported in this range, and identify which exterior power $\wedge^{-p}\mathcal{G}^\vee$ contributes to each column $p\in\{-2,-1,0\}$. -->

### Remark {#ecag-0242}

The Beilinson spectral sequence in the theorem above was originally stated by Buchdahl for locally free sheaves, but the same argument extends to torsion-free sheaves with only minor modification: the key point is that tensoring with $p_1^*\mathcal{E}$ preserves exactness of the Koszul complex because the terms of the complex are locally free on $\Sigma_n\times\Sigma_n$, so no flatness assumption on $\mathcal{E}$ is needed for this step.

There is also a choice in the construction: one may use either $p_{1*}(p_{2}^{*}\mathcal{E}\otimes \mathcal{O}_{\Delta})$ or $p_{2*}(p_{1}^{*}\mathcal{E}\otimes \mathcal{O}_{\Delta})$ to produce the spectral sequence. In general these two spectral sequences are different. The convention above (using $p_{2*}$ and $p_1^*\mathcal{E}$) is chosen because it yields better vanishing control on the $E_1$-page, as the asymmetry in the bundle $\mathcal{G}$ (which involves $T_{\Sigma_n/\mathbf{P}^1}(-1,0)$ pulled back from the first factor) interacts more favorably with the cohomology vanishing results from the Lemma on cohomology of line bundles.

<!-- BENCHMARK_PROBLEM: On $\Sigma_n$, explain why using $p_{2*}(p_1^*\mathcal{E}\otimes\mathcal{O}_\Delta)$ rather than $p_{1*}(p_2^*\mathcal{E}\otimes\mathcal{O}_\Delta)$ gives better vanishing on the $E_1$-page of the Beilinson spectral sequence. Which specific cohomology groups vanish in one convention but not necessarily in the other? -->

Take the exterior powers of the dual of the defining sequence of $\mathcal{G}$ and tensor with $p_{1}^{*}\mathcal{E}$, Since $\mathcal{E}$ is torsion-free, $-\otimes p_{1}^{*}\mathcal{E}$ is an exact functor. We have

$$0\rightarrow \wedge^{-p-1}\mathcal{F}^{\vee}\otimes p^{*}(L^{\vee})\otimes p_{1}^{*}\mathcal{E}\rightarrow \wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}\rightarrow \wedge^{-p}\mathcal{F}^{\vee}\otimes p_{1}^{*}\mathcal{E}\rightarrow 0.$$

If $p=0$, the first sheaf in the sequence above vanishes, $\wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}=p_{1}^{*}\mathcal{E}$, if $p=-2$, the last sheaf in the sequence above vanishes, $\wedge^{-2}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}=\mathcal{F}^{\vee}\otimes p^{*}(L^{\vee})\otimes p_{1}^{*}\mathcal{E}=\mathcal{E}(-1, n-1)\boxtimes \mathcal{O}_{\Sigma_{n}}(-1, -1)$. Take the associated long exact sequence one has
\begin{align}
&E_{1}^{0,q}= \mathrm{H}^{q}(\mathcal{E})\otimes \mathcal{O}_{\Sigma_{n}}(0,0)\\
\dots\rightarrow \mathrm{H}^{q}(\mathcal{E}(0, -1))\otimes \mathcal{O}_{\Sigma_{n}}(0, -1)\rightarrow &E_{1}^{-1, q}\rightarrow \mathrm{H}^{q}(\mathcal{E}(-1, n))\otimes \mathcal{O}_{\Sigma_{n}}(-1, 0)\rightarrow \dots \\
&E_{1}^{-2, q}= \mathrm{H}^{q}(\mathcal{E}(-1, n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1).
\end{align}

### Lemma {#ecag-0243}

**Statement:** Let $\mathcal{E}$ be a torsion-free sheaf on $\Sigma_{n}$ that is trivial at infinity (i.e., $\mathcal{E}|_E\cong\mathcal{O}_E^{\oplus r}$ where $E$ is the negative section at infinity). Then:

$$
\mathrm{H}^{0}(\mathcal{E}(p,q))=0 \quad \text{for } np+q\leq -1,

$$

$$
\mathrm{H}^{2}(\mathcal{E}(p,q))=0 \quad \text{for } np+q\geq -(n+1).

$$

**Construction/Proof:**

Step 1. For the $\mathrm{H}^0$ vanishing: Restrict to a general fiber $F\cong\mathbf{P}^1$ of $\pi$. Since $\mathcal{E}$ is trivial at infinity, along the section at infinity $E$ we have $\mathcal{E}|_E\cong\mathcal{O}_E^{\oplus r}$. On each fiber $F$, the restriction $\mathcal{E}(p,q)|_F$ has degree $np+q$ (since $H\cdot F=1$ and $F\cdot F=0$). When $np+q\leq -1$, the degree is negative, so any global section of $\mathcal{E}(p,q)$ restricts to zero on every fiber. Since $\pi$ is proper with connected fibers and $\pi_*$ of a sheaf with no sections on fibers is zero, we obtain $\mathrm{H}^0(\mathcal{E}(p,q))=0$.

Step 2. For the $\mathrm{H}^2$ vanishing: By Serre duality, $\mathrm{H}^2(\mathcal{E}(p,q))=\mathrm{H}^0(\mathcal{E}^{\vee}(-p-2,n-2-q))^{\vee}$ (using $\omega_{\Sigma_n}=\mathcal{O}(-2,n-2)$). The triviality of $\mathcal{E}$ at infinity implies $\mathcal{E}^{\vee}$ is also trivial at infinity, so by the $\mathrm{H}^0$ vanishing applied to $\mathcal{E}^{\vee}$, we need $n(-p-2)+(n-2-q)\leq -1$, i.e., $-np-2n+n-2-q\leq -1$, which gives $np+q\geq -(n+1)$ after rearranging. Thus $\mathrm{H}^2(\mathcal{E}(p,q))=0$ in this range.

**Key Insight:** The triviality-at-infinity condition controls the splitting type of $\mathcal{E}$ on fibers, turning the fiberwise degree computation into a global vanishing statement via the Leray spectral sequence and Serre duality.

**Prerequisites:** Serre duality on surfaces, Leray spectral sequence, splitting of bundles on $\mathbf{P}^1$, torsion-free sheaves on Hirzebruch surfaces

<!-- BENCHMARK_PROBLEM: Let $\mathcal{E}$ be a rank $2$ torsion-free sheaf on $\Sigma_2$ that is trivial at infinity. For the twist $\mathcal{E}(-1,1)$, verify directly from the vanishing lemma that $\mathrm{H}^0(\mathcal{E}(-1,1))=0$ and $\mathrm{H}^2(\mathcal{E}(-1,1))=0$, and explain why $\mathrm{H}^1(\mathcal{E}(-1,1))$ may be nonzero. -->

### Proposition {#ecag-0244}

**Statement:** Let $\mathcal{E}$ be a torsion-free sheaf on $\Sigma_n$ that is trivial at infinity. Then $\mathcal{E}$ can be realized as the cohomology of a monad (three-term complex):

$$
0\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(0, -1)\rightarrow E_{1}^{-1, 1}\otimes\mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow  \mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow 0.

$$

The middle term $E_{1}^{-1, 1}\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)$ fits in a short exact sequence

$$
0 \rightarrow \mathrm{H}^{1}(\mathcal{E}(-1, -1))\otimes\mathcal{O}_{\Sigma_n}(1, -1)\rightarrow E_{1}^{-1, 1}\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2, n))\otimes \mathcal{O}_{\Sigma_{n}}(0, 0)\rightarrow 0.

$$

Moreover, this second sequence splits.

**Construction/Proof:**

Step 1. Apply the Beilinson spectral sequence (Theorem ecag-0241) not to $\mathcal{E}$ directly but to the twist $\mathcal{E}(-1,0)$. The $E_1$-page for $\mathcal{E}(-1,0)$ is a $3\times 3$ grid:

| $q\backslash p$ | $p=-2$ | $p=-1$ | $p=0$ |
|---|---|---|---|
| $q=2$ | $\mathrm{H}^{2}(\mathcal{E}(-2,n-1))\otimes\mathcal{O}(-1, -1)$ | $E_{1}^{-1,2}$ | $\mathrm{H}^2(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$ |
| $q=1$ | $\mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1)$ | $E_{1}^{-1,1}$ | $\mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$ |
| $q=0$ | $\mathrm{H}^{0}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1)$ | $E_{1}^{-1,0}$ | $\mathrm{H}^{0}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$ |

Step 2. Apply the vanishing lemma (ecag-0243) to eliminate corner terms. For $\mathrm{H}^0$: we need $np+q\leq -1$. For $\mathcal{E}(-2,n-1)$, the fiberwise degree is $n(-2)+(n-1)=-(n+1)\leq -1$, so $\mathrm{H}^0(\mathcal{E}(-2,n-1))=0$. For $\mathcal{E}(-1,0)$, the fiberwise degree is $-n\leq -1$, so $\mathrm{H}^0(\mathcal{E}(-1,0))=0$.

For $\mathrm{H}^2$: we need $np+q\geq -(n+1)$. For $\mathcal{E}(-2,n-1)$, the fiberwise degree is $-(n+1)$, which is the boundary case; in fact $\mathrm{H}^2(\mathcal{E}(-2,n-1))=0$ since the inequality is not strict. For $\mathcal{E}(-1,0)$, the fiberwise degree is $-n\geq -(n+1)$, so $\mathrm{H}^2(\mathcal{E}(-1,0))=0$.

Step 3. With all four corner terms vanishing, the convergence of the spectral sequence forces $E_1^{-1,2}=0$ and $E_1^{-1,0}=0$ as well (since the spectral sequence converges to $\mathcal{E}(-1,0)$ in total degree $0$ and to $0$ elsewhere, and these terms would contribute to total degrees $1$ and $-1$ respectively with no other terms to cancel them).

Step 4. Only the $q=1$ row survives, and the spectral sequence degenerates at $E_1$, expressing $\mathcal{E}(-1,0)$ as the cohomology of the monad

$$
0\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1, -1)\rightarrow E_{1}^{-1, 1}\rightarrow  \mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}\rightarrow 0.

$$

Tensoring with $\mathcal{O}_{\Sigma_n}(1,0)$ yields the first statement.

Step 5. To compute $E_1^{-1,1}\otimes\mathcal{O}_{\Sigma_n}(1,0)$: apply the vanishing lemma to check $\mathrm{H}^0(\mathcal{E}(-1,-1))=0$ (fiberwise degree $-(n+1)\leq -1$) and $\mathrm{H}^2(\mathcal{E}(-1,-1))=0$ (fiberwise degree $-(n+1)$, boundary). The long exact sequence from the exterior power filtration then degenerates to the claimed short exact sequence.

Step 6. Splitting: The second sequence splits because $\operatorname{Ext}^{1}(\mathcal{O}_{\Sigma_{n}}(0,0), \mathcal{O}_{\Sigma_{n}}(1, -1)) =\mathrm{H}^1(\mathcal{O}_{\Sigma_{n}}(1, -1))$. By the cohomology lemma (ecag-0240), $\mathrm{H}^1(\mathcal{O}_{\Sigma_n}(1,-1))$ requires either $\{p\geq 0, q\leq -2\}$ or $\{p\leq -2, q\geq n\}$. With $p=1$ and $q=-1$, neither condition is satisfied, so $\operatorname{Ext}^1=0$ and the sequence splits.

**Key Insight:** The monad description arises not from the Beilinson spectral sequence applied directly to $\mathcal{E}$, but to the twist $\mathcal{E}(-1,0)$; this shift is precisely what makes the four corner terms of the $E_1$-page vanish, forcing degeneration and producing a clean three-term complex.

**Prerequisites:** Beilinson spectral sequence on $\Sigma_n$, vanishing for torsion-free sheaves trivial at infinity, Ext computations on Hirzebruch surfaces, spectral sequence degeneration

<!-- BENCHMARK_PROBLEM: In the monad description for a torsion-free sheaf $\mathcal{E}$ on $\Sigma_n$ trivial at infinity, the middle term splits as $\mathrm{H}^1(\mathcal{E}(-1,-1))\otimes\mathcal{O}_{\Sigma_n}(1,-1)\oplus\mathrm{H}^1(\mathcal{E}(-2,n))\otimes\mathcal{O}_{\Sigma_n}$. Verify the splitting by computing $\operatorname{Ext}^1(\mathcal{O}_{\Sigma_n}, \mathcal{O}_{\Sigma_n}(1,-1))$ using the cohomology of line bundles on $\Sigma_n$, and identify for which values of $n$ this Ext group vanishes. -->
