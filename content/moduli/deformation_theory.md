---
chapter: moduli
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Moduli_problems_and_deformation_theory/deformation_theory.tex
---

## Deformation theory

### Example: Hartsshorne $\mathrm{III}.9.9$, a rigid $k$-algebra {#ecag-0299}

Consider $$X=\mathrm{Spec}(k[x,y,z,w]/((x,y)\cap(z,w)))$$

### Remark: infinitesimal deformation corresponding to $H^{1}(X,T_{X})$ {#ecag-0300}

Thus we know projective spaces $\mathbb{P}_{k}^{n}$ are rigid.

### Example: $T_{id}(\mathrm{Aut}(X))\cong \mathrm{Hom}(\Omega_{X}, \mathcal{O}_{X})$ {#ecag-0301}

We assume $X$ is a scheme of finite type over $k=\overline{k}, char(k)=0$. A tangent vector of $\mathrm{Aut}(X)$ at the identity map is given by a morphism $$\mathrm{Spec}(k[\epsilon]/(\epsilon^{2}))\rightarrow \mathrm{Aut}(X).$$
In other words, an isomorphism over $k[\epsilon]/(\epsilon^{2})$
$$\mathcal{O}_{X[\epsilon]}\rightarrow \mathcal{O}_{X[\epsilon]}.$$
Locally, this is given by a $k[\epsilon]/(\epsilon^{2})$-algbra isomorphism
$$x_{i}\mapsto x_{i}+\epsilon f_{i}.$$
This is the same as given a morphism $d: \mathcal{O}_{X}\rightarrow \mathcal{O}_{X}$ such that 
$$d(x_{i}x_{j})=x_{i}f_{j}+x_{j}f_{i}=x_{i}d(f_{j})+x_{j}d(x_{i}).$$
In other words, a tangent vector is the same as a derivative $d: \mathcal{O}_{X}\rightarrow \mathcal{O}_{X}$. By the universal property of $\Omega_{X}$, we get an isomorphism 
$$T_{id}(\mathrm{Aut}(X))\cong \mathrm{Hom}(\Omega_{X}, \mathcal{O}_{X}).$$
If $X$ is smooth, we have 
$$T_{id}(\mathrm{Aut}(X))\cong H^{0}(X, T_{X}).$$

Let $X$ be a $k$-scheme. For a line bundle $\mathcal{L}\in \pic(X)$, we define the deformation functor 
$$\widehat{\pic}_{X, \mathcal{L}}:\cat{Art}/k\rightarrow \cat{Set},   A\mapsto \{\text{line bundle } \mathcal{L}' \text{ on } X_{A}, \phi: \mathcal{L}'|_{X}\cong \mathcal{L} \}/\sim.$$
To get the tangent-obstruction theory of $\widehat{\pic}_{X, \mathcal{L}}$, we consider a small extension $0\rightarrow M\rightarrow B\rightarrow A\rightarrow 0$ in $\cat{Art}/k$. The map $\iota: X_{A}\hookrightarrow X_{B}$ is given by the ideal sheaf $\mathcal{I}=\pi^{*}M$, where $\pi: X_{B}\rightarrow \operatorname{Spec\,}(B)$ is the natural projection. We have an exact sequence of sheaves
$$1\rightarrow 1+\mathcal{I}\rightarrow \mathcal{O}^{\times}_{X_{B}}\rightarrow \mathcal{O}^{\times}_{X_{A}}\rightarrow 1.$$
Note that $1+\mathcal{I}\cong \mathcal{I}=\pi^{*}M$. Take the associated long exact sequence, we have 
$$\mathrm{H}^{1}(X, \pi^{*}M)\rightarrow \pic(X_{B})\xrightarrow{\iota^{*}}\pic(X_{A})\rightarrow \mathrm{H}^{2}(X, \pi^{*}M).$$ Note that locally the sheaf structure of $\pi^{*}M$ is just $\mathcal{O}_{X}\otimes_{k} M\cong \mathcal{O}_{X}^{\oplus \dim_{k}M}$. Thus we know
$$\mathrm{H}^{i}(X, \pi^{*}M)=\mathrm{H}^{i}(X, \mathcal{O}_{X})^{\oplus \dim_{k}M}=\mathrm{H}^{i}(X, \mathcal{O}_{X})\otimes_{k} M.$$
Assume that $X$ is proper. Then $T_{1}=\mathrm{H}^{1}(X, \mathcal{O}_{X})$ and $T_{2}=\mathrm{H}^{2}(X, \mathcal{O}_{X})$ are finite-dimension and form a tangent-obstruction theory. If $\pic(X)$ is representable, then we know the tangent space $T_{[\mathcal{L}]}\pic(X)=\mathrm{H}^{1}(X, \mathcal{O}_{X}).$
## Deformation of mapping spaces
## Deformation of automorphisms
## Deformation of torsors
## Deformation of coherent sheaves
Let $X$ be a smooth projective variety. $E$ be a coherent sheaf of $\mathcal{O}_{X}$-module. We denote the ring of dual numbers by $k[\epsilon]$, $\operatorname{Spec\,}(k[\epsilon])$ by $D$ and $X\otimes_{k}\operatorname{Spec\,}(k[\epsilon])$ by $X_{D}$. Consider the deformation functor 
$$ \mathcal{M}: \cat{Art}/k \rightarrow \cat{Set}, A \mapsto \{A\text{-flat coherent sheaf } E'\in \cat{Coh}(X_{A}), \phi:E'|_{X}\cong E\}/\sim.
$$

### Theorem {#ecag-0302}

There's a natural bijection between $\mathcal{M}(D)$ and $\mathrm{Ext}^{1}(E, E)$.

\begin{proof}
We have an short exact sequence 
$$0\rightarrow (\epsilon)\rightarrow k[\epsilon]\rightarrow k\rightarrow 0.$$
Note that as $k[\epsilon]$-modules, $(\epsilon)\cong k$. Pull the sequence back along the map $\pi:X_{D}\rightarrow D$, we get an exact sequence of $\mathcal{O}_{X_{D}}$-modules 
$$0\rightarrow \epsilon\mathcal{O}_{X}\rightarrow \mathcal{O}_{X_{D}}\rightarrow \mathcal{O}_{X}\rightarrow 0.$$
Let $E'$ be a deformation of $E$ over $D$. Since $E'$ is $D$-flat, applying $-\otimes E$ to the second sequence above, we get 
$$0\rightarrow \epsilon E\rightarrow E'\rightarrow E\rightarrow 0.$$
This gives us an element in $\mathrm{Ext}^{1}_{\mathcal{O}_{X_{D}}}(\epsilon E, E)$, via the embedding $\mathcal{O}_{X}\rightarrow \pi_{*}\mathcal{O}_{X_{D}}=\mathcal{O}_{X}\oplus \epsilon\mathcal{O}_{X}$, it also gives us an element in $\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(E,E)$. Conversely, given an element $E'\in \mathrm{Ext}^{1}_{\mathcal{O}_{X}}(E, E)$, we have to give $E'$ an $\mathcal{O}_{X_{D}}$-module structure and prove it's $D$-flat. For the first requirement, we just define the action of $\epsilon$ on $E'$ by the composition of $E'\rightarrow E$ and $E\rightarrow E'$, clearly we have $\epsilon^{2}=0$. To prove it's flat over $D$, we simply point out the $E'|_{X}=E$ which is flat over $\operatorname{Spec\,}(k)$ and $(\epsilon)\otimes_{\mathcal{O}_{X_{D}}} E'=E\rightarrow E'$ is an injection by our difinition of the $\epsilon$-action. Finally it's straightforward to check that 
$$\mathcal{M}(D)=\mathrm{Ext}^{1}(E, E).$$
\end{proof}

### Theorem {#ecag-0303}

Let $$0\rightarrow I\rightarrow B\xrightarrow{\sigma}A\rightarrow 0$$
be a small extension and $E$ be a coherent sheaf on $X$ satisfying $\hom(E,E)\cong \mathbf{C}$(e.g stable sheaves). Then we have a tangent-obstruction theory given by 
$$\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(E, E)\otimes I\rightarrow \mathcal{M}(B)\rightarrow \mathcal{M}(A)\xrightarrow{ob} \mathrm{Ext}^{2}_{\mathcal{O}_{X}}(E, E)\otimes I .$$
In other words, 
 
1. The non-trivial fibre of $\mathcal{M}(\sigma)$ is an $\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(E, E)\otimes_{k}I$-torsor.
2. There is an obstruction map $\mathrm{ob}:\mathcal{M}(A)\rightarrow \mathrm{Ext}^{2}_{\mathcal{O}_{X}}(E, E)\otimes_{k}I$. The image of $\mathcal{M}(\sigma)$ is exactly the kernel of the obstruction map. Furthermore,
3. The image of $\mathrm{ob}$ is in the traceless part $\mathrm{Ext}^{2}_{0}(E, E)\otimes_{k}I$, which is the kernel of the trace map $\mathrm{Ext}^{1}(E, E)\otimes I\rightarrow \mathrm{H}^{2}(\mathcal{O}_{X})\otimes_{k} I$.

\begin{proof}
We list the steps, when we have time, we'll write down the proof.

- We first show that given $E_{A}\in \mathcal{M}(A)$. Deformations of $E_{A}$ to $B$ form a $\mathrm{Ext}^{1}_{\mathcal{O}_{X_{A}}}(I\otimes_{\mathcal{O}_{X_{A}}}E_{A}, E_{A})$-torsor.
- Then we use some homological algebra to construct the obstruction map.
- Finally,we apply some version of the cohomology and base change theorem to prove that $$\mathrm{Ext}^{1}_{\mathcal{O}_{X_{A}}}(I\otimes_{\mathcal{O}_{X_{A}}}E_{A}, E_{A})=\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(E,E)\otimes_{k}I.$$

 
\end{proof}

### Remark {#ecag-0304}

From this example, we can actually see a deformation-obstruction theory has several layers. First, for any given geometric object $E$, we might discuss about its deformations even without a moduli space.  Secondly, with a fine moduli space, then we know $T_{[E]}M= \mathcal{M}(\operatorname{Spec\,}(k[\epsilon]/(\epsilon^{2})))$, where $\mathcal{M}$ is the moduli functor and $M$ is the moduli space. Thirdly, if we only have a coarse moduli space, then $T_{[E]}M\neq \mathcal{M}(\operatorname{Spec\,}(k[\epsilon]/(\epsilon^{2})))$ in general. Then you have to be careful what do you mean by `tangent space'.

## Deformation of quotient sheaves
Let $X$ be a scheme over $k$. $\mathcal{F}$ be a coherent sheaf on $X$, $\mathcal{S}_{0}$ be a coherent subsheaf of $\mathcal{F}$, $\qQ_{0}$ be the quotient. Define the deformation functor
$$D:=D_{[\mathcal{F}\rightarrow \qQ_{0}\rightarrow 0]}: \cat{Art}/k\rightarrow \cat{Set}$$
$$A\mapsto \{ \text{exact sequences of } A\text{-flat sheaves } 0\rightarrow \mathcal{S}\rightarrow \mathcal{F}\otimes_{k}A\rightarrow \qQ\rightarrow 0 \text{ on } X_{A},  \mathcal{S}\otimes_{A}k\cong \mathcal{S}_{0} \}/\sim.$$
By definition, $[0\rightarrow \mathcal{S}'\rightarrow \mathcal{F}\otimes_{k}B\rightarrow \qQ'\rightarrow 0]\in D(B)$ is a deformation of $[0\rightarrow \mathcal{S}\rightarrow \mathcal{F}\otimes_{k}A\rightarrow \qQ\rightarrow 0]\in D(A)$ if and only if we have 

- $\mathcal{S}'\otimes_{B}A=\mathcal{S}$
- $\mathcal{S}'$ is flat over $B$. We know $\mathcal{S}'\otimes_{B}A=\mathcal{S}$ is flat over $A$, thus we only need $\mathcal{S}'\otimes_{B} M=\mathcal{S}\otimes_{B}A\otimes_{A}M=\mathcal{S}\otimes_{A}M \rightarrow \mathcal{S}'$ is an injection. In other words, flatness is equivalent to the existence of the short exact sequence
$$0\rightarrow \mathcal{S}\otimes_{A}M\rightarrow \mathcal{S}'\rightarrow \mathcal{S}\rightarrow 0.$$

In other words, an extension exists if and only if we can find a subsheaf $\mathcal{E}$ of  $\mathcal{F}\otimes_{k}B/S\otimes_{A}M=\mathcal{F}\otimes_{k}B/\im(\alpha)$ whose image in $\mathcal{F}\otimes_{k}A$ is exactly $\mathcal{S}$. Because the image lies in $\mathcal{S}$, we only need to find a subsheaf of $\ker(\beta)/\im(\alpha)$ has this property. In other words, we need the following sequence to split
$$0\rightarrow \ker\rightarrow \ker(\beta)/\im(\alpha)\rightarrow \mathcal{S}\rightarrow 0.$$
We can check that $\ker=\mathcal{F}\otimes_{k}M/\mathcal{S}\otimes_{A}M=\qQ\otimes_{A}M$. That is, the obstruction is given by 
$$ob=[0\rightarrow \qQ\otimes_{A}M\rightarrow \ker(\beta)/\im(\alpha)\rightarrow \mathcal{S}\rightarrow 0]\in \mathrm{Ext}^{1}_{\mathcal{O}_{X_{B}}}(\mathcal{S}, \qQ\otimes_{A}M).$$
Moreover, all flat deformations of the given element is bijective to 
$$\mathrm{Ext}^{0}_{\mathcal{O}_{X_{B}}}(\mathcal{S}, \qQ\otimes_{A}M)=\hom(\mathcal{S}, \qQ\otimes_{A}M).$$ 
$$<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
& 0\arrow{d} & & 0 \arrow{d}\\
& \mathcal{S}\otimes_{A}M\arrow{d}\arrow[dashrightarrow]{dr}{\alpha}& & \mathcal{S}\arrow{d}\\ 
0\arrow{r} & \mathcal{F}\otimes_{k}M\arrow{r}\arrow{d}& \mathcal{F}\otimes_{k}B\arrow[dashrightarrow]{dr}{\beta}\arrow{r}& \mathcal{F}\otimes_{k}A\arrow{r}\arrow{d} & 0\\
&\qQ\otimes_{A}M\arrow{d} & &Q\arrow{d}\\
& 0 & &0
\end{tikzcd}
```
$$
There's still one more issue, these two $\mathrm{Ext}$ groups still depend on $B$. We claim that  the $M(\ker(\beta)/\im(\alpha))=0$. Indeed if $\gamma=\sum f_{i}\otimes_{k}b_{i}\in \ker(\beta)$, then we have $\sum f_{i}\otimes_{k}a_{i}\in \mathcal{S}$, where $a_{i}=b_{i}\pmod M$. Then $m\gamma =\sum f_{i}\otimes mb_{i}=\sum f_{i}\otimes ma_{i}$, the last identity comes from the fact that $M^{2}=0$, thus $ma_{i}$ is well defined. Then $m\gamma=m(\sum f_{i}\otimes_{k}a_{i})\in \im(\alpha)$. 
Apply $\otimes_{A}k$ to 
$$0\rightarrow \ker\rightarrow \ker(\beta)/\im(\alpha)\rightarrow \mathcal{S}\rightarrow 0.$$
We still get an exact sequence by the $A$-flatness of $\mathcal{S}$
$$0\rightarrow \qQ\otimes_{A}M\rightarrow \ker(\beta)/\im(\alpha)\otimes_{A}k\rightarrow \mathcal{S}\otimes_{A}k\rightarrow 0.$$
We can check that we have the following commutative diagram. If we just consider small extensions, we have $\qQ\otimes_{A}M\otimes_{A}k=\qQ\otimes_{A}M$ because $m_{A}M=0$.
$$
<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
& & 0\arrow{d}& 0\arrow{d}&\\
 & & \mathcal{S}\otimes_{A}m_{A}\arrow{d}\arrow[r, equal]&  \mathcal{S}\otimes_{A}m_{A}\arrow{d}&\\
 0\arrow{r}&\qQ\otimes_{A}M \arrow{r}\arrow[d,equal]& \ker(\beta)/\im(\alpha)\arrow{r}\arrow{d}&  \mathcal{S}\arrow{d}\arrow{r}& 0\\
 0\arrow{r}&\qQ\otimes_{A}M \arrow{r}& \ker(\beta)/\im(\alpha)\otimes_{A}k\arrow{r}\arrow{d}&\mathcal{S}\otimes_{A}k \arrow{d}\arrow{r}&0\\
 & & 0& 0& \\
\end{tikzcd}
```
$$
In conclusion, we have
$$\hom_{X_{A}}(\mathcal{S},\qQ\otimes_{A}M)=\hom_{X}(\mathcal{S}\otimes_{A}k,\qQ\otimes_{A}M)=\hom_{X}(\mathcal{S}_{0}, \qQ_{0})\otimes_{k}M$$
$$\mathrm{Ext}^{1}_{X_{A}}(\mathcal{S}, \qQ\otimes_{A}M)=\mathrm{Ext}^{1}_{X}(\mathcal{S}\otimes_{A}k, \qQ\otimes_{A}M)=\mathrm{Ext}^{1}_{X}(\mathcal{S}_{0}, \qQ_{0})\otimes_{k} M.$$
Because $m_{A}M=0$, any element in $\hom_{X_{A}}(\mathcal{S}, \qQ\otimes_{A}M)$ factors through the geometric fibre. And we can take out $M$ because of the projection formula, $M$ is simply viewed as a vector space. As a special case, the tangent-obstruction theory of the Hilbert scheme functor $H_{Z,X}$ is given by $T_{1}=\hom_{\mathcal{O}_{X}}(I_{Z}, \mathcal{O}_{Z}), T_{2}=\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(I_{Z}, \mathcal{O}_{Z})$.

### Remark {#ecag-0305}

We actually have many slightly different ways to describe the tangent space at a point on a Hilbert scheme of $n$ points on a $k$-dimensional smooth quasi-projective variety $X$.
\begin{align*}T_{Z}\mathrm{Hilb}^{n}(X)&=\hom_{\mathcal{O}_{X}}(\mathcal{I}_{Z}, \mathcal{O}_{Z})\\
&=\mathrm{Ext}^1_{\mathcal{O}_{X}}(\mathcal{O}_{Z},\mathcal{O}_{Z})\\
&=\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(\mathcal{I}_{Z}, \mathcal{I}_{Z}).
\end{align*}
$\hom_{\mathcal{O}_{X}}(\mathcal{I}_{Z}, \mathcal{O}_{Z})=\mathrm{Ext}^1_{\mathcal{O}_{X}}(\mathcal{O}_{Z},\mathcal{O}_{Z})$ can be seen by applying $\hom(-, \mathcal{O}_{Z})$ to the short exact sequence 
$$0\rightarrow \mathcal{I}_{Z}\rightarrow \mathcal{O}_{X}\rightarrow \mathcal{O}_{Z}\rightarrow 0.$$
For the last identity, maybe there's a much easier proof. The one we know is that we realize $\mathrm{Hilb}^{n}(X)$ as the rank $1$ instanton moduli space $\mathcal{M}(n,1)$(see the subsection about the deformation theory of $\mathcal{M}(n,r)$). The tangent space of $\mathcal{M}(n,1)$ at $[\mathcal{I}_{Z}]$ is given by $\mathrm{Ext}^{1}_{\mathcal{O}_{X}}(I_{Z}, I_{Z})$.

## Deformation theory the instanton moduli space
The instanton moduli space $\mathcal{M}(n,r)$ is defined to be moduli of rank $2$ torsion-free sheaves on $\mathbf{P}^{2}$ framed at infinity.
## Deformation of Hilbert schemes
## Hilbert schemes of points on surfaces
## Deformation of Calabi-Yau varieties

## Deformation of varieties
## Deformation of nodes
