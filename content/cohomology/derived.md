---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/derived.tex
---

## Derived categories

### Example: Dualizing complex of a projective variety {#ecag-0215}

Consider the projective variety $X$ of a plane intersecting a line in $\mathbf{P}^{3}$

$$X=\operatorname{Proj\,}(k[x,y,z,w]/(x)(y,z))=\operatorname{Proj\,}(k[x,y,z,w]/(xy,xz)).$$

We want to compute the dualizing complex

$$\omega_{X}^{\bullet}=\mathbf{R}\operatorname{Hom}_{\mathcal{O}_{\mathbf{P}^{3}}}(\mathcal{O}_{X},\omega_{\mathbf{P}^{3}}[3]).$$

We have a resolution $\mathcal{L}^{\bullet}\rightarrow \mathcal{O}_{X}$(for any monomial ideals, we can always write down such a resolution easily) of $\mathcal{O}_{X}$ by locally free sheaves. 

$$\mathcal{L}^{\bullet}:0\rightarrow \mathcal{O}(-3)\xrightarrow{ \begin{bmatrix}z \\ -y \end{bmatrix}}\mathcal{O}(-2)\oplus\mathcal{O}(-2)\xrightarrow{\begin{bmatrix}xy & xz \end{bmatrix}} \mathcal{O}_{\mathbf{P}^{3}} \rightarrow \mathcal{O}_{X}\rightarrow 0.$$

Since $\omega_{\mathbf{P}^{3}}=\mathcal{O}_{\mathbf{P}^{3}}(-4)$, we have 

$$\mathbf{R}\operatorname{Hom}(\mathcal{O}_{X},\omega_{\mathbf{P}^{3}}[3])\cong \mathbf{R}\operatorname{Hom}(\mathcal{L}^{\bullet}\tens\mathcal{O}(4)[-3],\mathcal{O}).$$

Thus, we have 

$$\omega_{X}^{\bullet}: [\mathcal{O}(-4)\xrightarrow {\begin{bmatrix}xy \\ xz \end{bmatrix}}\mathcal{O}(-2)\oplus\mathcal{O}(-2)\xrightarrow{\begin{bmatrix}z & -y \end{bmatrix}} \mathcal{O}(-1)][-3].$$

### Example: Complexes have the same homology but not quasi-isomorphic {#ecag-0216}

Consider the following two complexes

$$\mathcal{L}^{\bullet}: \mathbf{C}[x,y]\oplus \mathbf{C}[x,y]\xrightarrow{\begin{bmatrix}x & y \end{bmatrix}} \mathbf{C}[x,y],$$

$$\mathcal{M}^{\bullet}:\mathbf{C}[x,y]\xrightarrow{0}\mathbf{C}.$$

## Derived pushforward and shifted direct sum of higher direct images
Consider the simplest springer resolution 
$$f:X=T^{*}\mathbf{P}^{1}\rightarrow \operatorname{Spec\,}(k[x,y,z]/xy-z^{2})=Y$$. Since $f$ is a semismall map, $\mathbf{R} f_{*}(\mathbf{Q}_{X}[2])$ is a perverse sheaf on $Y$.  
We claim 

$$\mathbf{R} f_{*}(\mathbf{Q}_{X}[2])\neq \mathbf{R}^{0}f_{*}(\mathbf{Q}_{X}[2])\oplus \mathbf{R}^{-1}f_{*}(\mathbf{Q}_{X}[2])[1]\oplus \mathbf{R}^{-2}f_{*}(\mathbf{Q}_{X}[2])[2].$$

### Remark {#ecag-0217}

Let $f:X\rightarrow Y$ be a proper morphism between irreducible varieties, by semi-continuity,

$$Y_{k}:=\{y\in Y|\dim f^{-1}(y)\geq k\}$$

is a closed subset of $Y$. A semismall map has the property that  bigger $Y_{k}$ has small fibres(controlled by the codimension of the fibre). That is 

$$k+\dim Y_{k}\leq \dim X-k.$$

We call $f$ a small map if the inequality is strict.

## Fourier-Mukai transforms on elliptic curves
Let $E$ be an elliptic curve over $\mathbf{C}$. $\mathscr{P}$ be the normalized Poincare bundle on $E\times E$ defined as follows
<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
 & \mathscr{P}=\pi_{1}^{*}\mathcal{O}_{E}(-p_{0})\otimes \pi_{2}^{*}\mathcal{O}_{E}(-p_{0})\otimes \mathcal{O}_{E\times E}(\Delta)\arrow{d}&\\
 &E\times E\arrow{dl}{\pi_{1}}\arrow{dr}{\pi_{2}} &\\
  E& &E
\end{tikzcd}
```.$$
Then we have

$$\mathscr{P}|_{p\times E}=\mathcal{O}_{E}(p-p_{0}), \mathscr{P}|_{E\times p}=\mathcal{O}_{E}(p-p_{0}).$$

We consider the Fourier-Mukai transform

$$\Phi:=\Phi^{\mathscr{P}}_{E\rightarrow E}: \mathrm{D}^{b}(E)\rightarrow \mathrm{D}^{b}(E)$$

$$\mathscr{E}\mapsto \mathbf{R}\pi_{2, *}(\pi_{1}^{*}\mathscr{E}\otimes\mathscr{P} ).$$

Mukai shows us the following theorem.

### Theorem: Mukai {#ecag-0218}

$\Phi\circ\Phi=\iota\circ[-1]$, where $\iota: E\rightarrow E$ is the negation map in the group structure on $E$. Since $\iota\circ [-1]$ is obviously an equivalence, it follows that $\Phi$ is a nontrivial equivalence.

\begin{proof}Note that the Fourier-Mukai kernel of $\Phi\circ \Phi$ is given by $\mathscr{P}\circ \mathscr{P}:=\mathbf{R} \pi_{13, *}(\pi_{12}^{*}\mathscr{P}\otimes \pi_{23}^{*}\mathscr{P})$. To understand this complex, consider the following commutative diagram
<!-- tikzcd diagram: manual conversion needed -->
```latex
\begin{tikzcd}
E\times E\times E\arrow{r}{f}\arrow[swap]{d}{\pi_{13}} & E\times E\arrow{d}{\pi_{1}}\\
E\times E \arrow{r}{m} & E
\end{tikzcd}
```.$$
\begin{align*}f:(x,y,z)&\mapsto (x+z,y)\\
m:(x,y)&\mapsto x+y.\end{align*}
By the second lemma below, we know $\mathbf{R} \pi_{13, *}(\pi_{12}^{*}\mathscr{P}\otimes \pi_{23}^{*}\mathscr{P})=\mathbf{R} \pi_{13, *}(f^{*}\mathscr{P})$. Then the flat base change theorem tells us 

$$\mathbf{R} \pi_{13, *}(f^{*}\mathscr{P})=m^{*}(\mathbf{R}\pi_{1, *}\mathscr{P}).$$

Since $\mathrm{H}^{2}(\mathscr{P}|_{E\times p})=\mathrm{H}^{2}(\mathcal{O}_{E}(p-p_{0}))=0$, we can apply cohomology and base change for $\mathrm{H}^{1}$. Then we know $\mathbf{R}^{1}\pi_{1, *}\mathscr{P}=\mathcal{O}_{p_{0}}$, the skyscraper sheaf supported at $p_{0}$. $\mathbf{R}^{0}\pi_{1, *}\mathscr{P}$ is the sheafification of $\mathrm{H}^{0}(\pi_{1}^{-1}U, \mathscr{P}|_{\pi_{1}^{-1}U})=0$, thus $\mathbf{R}^{0}\pi_{1, *}\mathscr{P}=0$. In other words, we know 

$$\mathbf{R}\pi_{1, *}\mathscr{P}=\mathcal{O}_{p_{0}}[-1].$$

Finally

$$m^{*}(\mathbf{R}\pi_{1, *}\mathscr{P})=m^{*}(\mathcal{O}_{p_{0}}[-1])=\mathcal{O}_{\Gamma_{\iota}}[-1].$$

That is 

$$\Phi\circ \Phi=\iota\circ[-1].$$

\end{proof}
The fact that $\mathbf{R} \pi_{13, *}(\pi_{12}^{*}\mathscr{P}\otimes \pi_{23}^{*}\mathscr{P})=\mathbf{R} \pi_{13, *}(f^{*}\mathscr{P})$ comes from the following two lemmas. First for any closed point $p\in E$, we denote the fibre product  $m^{-1}(p)$ by 

$$D_{p}:=\{(x, y)\in E\times E|x+y=p\}.$$

### Lemma {#ecag-0219}

For any closed point $p\in E$, we have 

$$\mathcal{O}_{E\times E}(D_{p}-D_{p_{0}})=\pi_{1}^{*}\mathcal{O}_{E}(p-p_{0})\otimes \pi_{2}^{*}\mathcal{O}_{E}(p-p_{0}).$$

\begin{proof}It's just a basic application of the see-saw principle. 
\begin{align*}
\pi_{1}^{*}\mathcal{O}_{E}(p-p_{0})\otimes \pi_{2}^{*}\mathcal{O}_{E}(p-p_{0})|_{q\times E}&=\mathcal{O}_{E}(p-p_{0})\\
\mathcal{O}_{E\times E}(D_{p}-D_{p_{0}})|_{q\times E}&=\mathcal{O}_{E}((p-q)-(p_{0}-q))=\mathcal{O}_{E}(p-p_{0}).\\
\pi_{1}^{*}\mathcal{O}_{E}(p-p_{0})\otimes \pi_{2}^{*}\mathcal{O}_{E}(p-p_{0})|_{E\times q}&=\mathcal{O}_{E}(p-p_{0})=\mathcal{O}_{E\times E}(D_{p}-D_{p_{0}})|_{E\times q}.
\end{align*}

We conclude that 

$$\mathcal{O}_{E\times E}(D_{p}-D_{p_{0}})=\pi_{1}^{*}\mathcal{O}_{E}(p-p_{0})\otimes \pi_{2}^{*}\mathcal{O}_{E}(p-p_{0}).$$

\end{proof}

### Lemma {#ecag-0220}

We have an isomorphism of line bundles on $E\times E\times E$

$$\pi_{12}^{*}\mathscr{P}\otimes \pi_{23}^{*}\mathscr{P}=f^{*}\mathscr{P}.$$

\begin{proof}
Another basic application of the see-saw principle. We have
\begin{align*}\pi_{12}^{*}\mathscr{P}|_{E\times p\times E}&=\pi_{1}^{*}\mathcal{O}_{E}(p-p_{0})\\
\pi_{12}^{*}\mathscr{P}|_{E\times p\times E}&=\pi_{2}^{*}\mathcal{O}_{E}(p-p_{0})\\
f^{*}\mathscr{P}|_{E\times p\times E}&=\mathcal{O}_{E\times E}(D_{p}-D_{p_{0}}).
\end{align*}
The last equality holds because we have 
\begin{align*}f^{*}\mathcal{O}_{E\times E}(\Delta)|_{E\times p\times E}&=\mathcal{O}_{E\times E}(D_{p})\\ f^{*}\pi_{1}^{*}\mathcal{O}_{E}(-p_{0})|_{E\times p\times E}&=\mathcal{O}_{E\times E}(-D_{p_{0}})\\ f^{*}\pi_{2}^{*}\mathcal{O}_{E}(-p_{0})|_{E\times p\times E}&=0.
\end{align*}
And the restrictions to $p_{0}\times E\times p_{0}$ of $\pi_{12}^{*}\mathscr{P}$, $\pi_{23}^{*}\mathscr{P}$ and $f^{*}\mathscr{P}$ are all trivial. Based on the lemma above, we conclude that 

$$\pi_{12}^{*}\mathscr{P}\otimes \pi_{23}^{*}\mathscr{P}=f^{*}\mathscr{P}.$$

\end{proof}
We can actually prove that $\Phi$ is an equivalence quite easily by proving $\Phi(\mathcal{O}_{x})=\mathscr{P}_{x}$ maps an orthonormal basis to another orthonormal basis and commutes with the Serre functor, see for example [Andrei Căldăraru's note, p25](http://www.math.wisc.edu/~andreic/publications/lnPoland.pdf). Everything boils down to the following two simple facts

$$\mathrm{Ext}^{i}(\mathcal{O}_{E}(p'-p_{0}), \mathcal{O}_{E}(p-p_{0}))=\mathrm{H}^{i}(\mathcal{O}_{E}(p-p'))=0 \text{ if $p\neq p'$ or $i\neq 0, 1$}$$

$$\mathscr{P}_{x}\otimes \omega_{E}=\mathscr{P}_{x}.$$

## Six functors

### Example: Adjoint functor {#ecag-0221}

Let $i:(\mathbf{Z}, \leq)\hookrightarrow (\mathbf{R}, \leq)$, be the natural embedding. It has a right adjoint functor given by the floor function $\lfloor \rfloor:(\mathbf{R}, \leq)\rightarrow (\mathbf{Z}, \leq)$. We can get a rough idea about why `adjoint functors' are `best approximations' in each other.

### Example: $i_{*},i^{*}, i_{!}, i^{!}, j_{*},j^{*}, j_{!}, j^{!}$ {#ecag-0222}

We just consider the simple example $\mathbf{C}^{\times}\xhookrightarrow{i}\mathbf{C}\xhookleftarrow{j} \mathrm{pt}$. We have 

- $j_{*}=j_{!}$. Closed embedding is proper.
- $i_{*}\neq i_{!}$. Open embedding is not proper.

Proper morphism must have proper fibres, but the inverse is not true, $\mathbf{C}^{\times}\hookrightarrow \mathbf{C}$ is not proper, intuitively because we can find a line in $\mathbf{C}^{\times}$ which is not closed in $\mathbf{C}$. Now we can have a very intuitive understanding of the valuation criteria of properness. It says if we can find a curve in the base most of whose points are images of the map, then we have one (closeness) and only one (separateness). In the world of algebraic geometry, we don't have one-parameter curves, so the spectrum of a discrete valuation ring literally serves as a role of a one-parameter curve. If we understand the universal closeness of a proper morphism in the language of Grothendieck topology, it really means for any 'open' in the base, the intersection with the image is closed. However, this generalized topological point of view teaches us what should really be called an 'intersection'. For example $\mathbb{A}^{1}\times_{\mathrm{Spec(k)}} \mathbb{A}^{1} \rightarrow \mathbb{A}^{1}$ should be viewed as the intersection of $\mathbb{A}^{1}$(first copy) and $\mathbb{A}^{1}$(second copy) in $\mathbb{A}^{1}$(the second copy) all in the 'topology' of $\mathrm{Spec}(k)$. We find the image of $xy=1$ is not closed thus we can say '$\mathbb{A}^{2}$ is not closed in $\mathbb{A}^{1}$'. 

First extent then restrict by different functors kills every sheaf.

- $j^{*}i_{!}=j^{!}i_{*}\mathscr{F}=0$.
- $i^{*}j_{!}\mathscr{F}=i^{!}j_{*}\mathscr{F}=0$

- $i^{*}=i^{!}$.

### Remark {#ecag-0223}

Cohomology and base change theorem is wrong for local systems even if we have a cartesian square satisfies all the conditions. Instead if we consider sheaf of $\mathcal{O}_{X}$-modules, then we have $j^{*}i_{*}\mathcal{O}_{\mathbb{A}^{1}\setminus\{0\}}=0$. This just says $k[t]/t\otimes_{k[t]}k[t, t^{-1}]=0$.

### Remark: Why the difference? {#ecag-0224}

I don't know. My guess is that $\mathcal{O}_{X}$-module is finer (in some sense) than local systems. Or in other words, local systems depend largely on the 'nearby cycles'. We even want to say local system is more about the local information/monodromy around a singular point instead of the fibre over the singular fibre itself. But somehow, $\mathcal{O}_{X}$-modules really takes the structure sheaf of the singular point into consideration, which means it kills what it always kills, it still has a huge impact on the pull back.
