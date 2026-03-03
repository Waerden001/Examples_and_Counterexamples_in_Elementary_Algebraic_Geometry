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

\begin{align*}
\mathrm{H}^{0}(\mathcal{O}_{\Sigma_{n}}(p, q))&\neq 0 \text{ if and only if }\begin{cases}p\geq 0\\ np+q\geq 0\end{cases}\\
\mathrm{H}^{1}(\mathcal{O}_{\Sigma_{n}}(p, q))&\neq 0  \text{ if and only if }  \begin{cases}p\geq 0\\ q\leq -2\end{cases} \text{ or }  \begin{cases}p\leq -2\\q\geq n\end{cases}\\
\mathrm{H}^{2}(\mathcal{O}_{\Sigma_{n}}(p, q))&\neq 0 \text{ if and only if }\begin{cases}p\geq -2\\ np+q\leq -(n+2)\end{cases}.
\end{align*}

\begin{proof}
See \cite[Lemma 3.1]{Monad15}
\end{proof}
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

### Theorem: [\cite{Buchdahl1987} {#ecag-0241}

]
For any torsion free sheaf $\mathcal{E}$ on $\Sigma_{n}$, there exists a spectral sequence, depending on $\mathcal{E}$:
$$E_{1}^{p,q}=R^{q}p_{2*}(\wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E})\Rightarrow \begin{cases}\mathcal{E} & p+q=0\\
0 & \text{otherwise}\end{cases}.$$

### Remark {#ecag-0242}

It's originally stated for locally free sheaves, the same argument works for torsion free sheaves with very little modification. Also notice that we can use either $p_{1*}(p_{2}^{*}\mathcal{E}\otimes \mathcal{O}_{\Delta})$ or $p_{2*}(p_{1}^{*}\mathcal{E}\otimes \mathcal{O}_{\Delta})$. In general the two spectral sequences are different. We chose the one above simply because we can get better vanishing control on the $E_{1}$-page.

Take the exterior powers of the dual of the defining sequence of $\mathcal{G}$ and tensor with $p_{1}^{*}\mathcal{E}$, Since $\mathcal{E}$ is torsion-free, $-\otimes p_{1}^{*}\mathcal{E}$ is an exact functor. We have

$$0\rightarrow \wedge^{-p-1}\mathcal{F}^{\vee}\otimes p^{*}(L^{\vee})\otimes p_{1}^{*}\mathcal{E}\rightarrow \wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}\rightarrow \wedge^{-p}\mathcal{F}^{\vee}\otimes p_{1}^{*}\mathcal{E}\rightarrow 0.$$

If $p=0$, the first sheaf in the sequence above vanishes, $\wedge^{-p}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}=p_{1}^{*}\mathcal{E}$, if $p=-2$, the last sheaf in the sequence above vanishes, $\wedge^{-2}\mathcal{G}^{\vee}\otimes p_{1}^{*}\mathcal{E}=\mathcal{F}^{\vee}\otimes p^{*}(L^{\vee})\otimes p_{1}^{*}\mathcal{E}=\mathcal{E}(-1, n-1)\boxtimes \mathcal{O}_{\Sigma_{n}}(-1, -1)$. Take the associated long exact sequence one has 
\begin{align}
&E_{1}^{0,q}= \mathrm{H}^{q}(\mathcal{E})\otimes \mathcal{O}_{\Sigma_{n}}(0,0)\\
\dots\rightarrow \mathrm{H}^{q}(\mathcal{E}(0, -1))\otimes \mathcal{O}_{\Sigma_{n}}(0, -1)\rightarrow &E_{1}^{-1, q}\rightarrow \mathrm{H}^{q}(\mathcal{E}(-1, n))\otimes \mathcal{O}_{\Sigma_{n}}(-1, 0)\rightarrow \dots \\
&E_{1}^{-2, q}= \mathrm{H}^{q}(\mathcal{E}(-1, n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1).
\end{align}

### Lemma {#ecag-0243}

Let $\mathcal{E}$ be a torsion-free sheaf on $\Sigma_{n}$, trivial at infinity. We have
\begin{align*}
\mathrm{H}^{0}(\mathcal{E}(p,q))=0 & \text{ for } np+q\leq -1\\
\mathrm{H}^{2}(\mathcal{E}(p,q))=0 & \text{ for } np+q\geq -(n+1).
\end{align*}

### Proposition {#ecag-0244}

For any torsion free sheaf $\mathcal{E}$ on $\Sigma_{n}$ can be realized as a monad:

$$0\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(0, -1)\rightarrow E_{1}^{-1, 1}\otimes\mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow  \mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow 0.$$

where the $E_{1}^{-1, 1}\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)$-term can be computed from 

$$0 \rightarrow \mathrm{H}^{1}(\mathcal{E}(-1, -1))\otimes\mathcal{O}_{\Sigma}(1, -1)\rightarrow E_{1}^{-1, 1}\otimes \mathcal{O}_{\Sigma_{n}}(1, 0)\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2, n))\otimes \mathcal{O}_{\Sigma_{n}}(0, 0)\rightarrow 0.$$

Moreover, the second sequence splits.

\begin{proof}
The trick here is that $\mathcal{E}$ can't be realized as a monad just from the spectral sequence. However, for $\mathcal{E}(-1, 0)$, the Beilinson spectral sequence becomes
\begin{center}
\begin{tabular}{|p{5.5cm}|p{1cm}|p{3.5cm}|p{0.5cm}| }
 \hline
 $\mathrm{H}^{2}(\mathcal{E}(-2,n-1))\otimes\mathcal{O}(-1, -1)$&$E_{1}^{-1,2}$& $\mathrm{H}^2(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$\\
 \hline
$\mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1)$&$E_{1}^{-1,1}$&$\mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$\\
 \hline
 $\mathrm{H}^{0}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1,-1)$&$E_{1}^{-1,0}$& $\mathrm{H}^{0}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}$\\
 \hline
\end{tabular}
\end{center}
By Lemma Vanshing lemma, all the four corner terms vanish. Then Theorem Limit forces $E_{1}^{-1,2}$ and $E_{1}^{-1, 0}$ to be zeros. Thus only the $q=1$ terms in the spectral sequence survive and the spectral sequence degenerates at the $E_{1}$-page. This proves that $\mathcal{E}(-1, 0)$ is the cohomology of 

$$0\rightarrow \mathrm{H}^{1}(\mathcal{E}(-2,n-1))\otimes \mathcal{O}_{\Sigma_{n}}(-1, -1)\rightarrow E_{1}^{-1, 1}\rightarrow  \mathrm{H}^{1}(\mathcal{E}(-1, 0))\otimes \mathcal{O}_{\Sigma_{n}}\rightarrow 0.$$

Tensoring it with $\mathcal{O}_{\Sigma_{n}}(1, 0)$ gives the first statement. To compute $E_{1}^{-1,1}\otimes\mathcal{O}_{\Sigma_{n}}(1, 0)$, Lemma Vanshing lemma shows that $\mathrm{H}^{0}(\mathcal{E}(-1, -1))=0$ and $\mathrm{H}^{2}(\mathcal{E}(-1,-1))=0$ for any $\Sigma_{n}$. Sequence terms in the spectral sequence degenerates to the second statement in the proposition. It splits because  $\operatorname{Ext}^{1}(\mathcal{O}_{\Sigma_{n}}(1, -1), \mathcal{O}_{\Sigma_{n}}) =\mathrm{H}^1(\mathcal{O}_{\Sigma_{n}}(-1, 1))=0$, the last equality comes from Lemma Cohomology on the surface.
\end{proof}
