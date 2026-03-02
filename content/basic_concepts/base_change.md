---
chapter: basic_concepts
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Basic_concepts/base_change.tex
---

## Base-change

### Example: Reduced scheme but not geometrically reduced {#ecag-0005}

Let $$K=\mathbf{F}_{p}(T^{\frac{1}{p}})$$
$$k=\mathbf{F}_{p}(T).$$
Then $\mathrm{Spec}(K)$ is reduced but $\mathrm{Spec}(K\otimes_{k}K)$ is not, because $1\otimes T^{\frac{1}{p}}-T^{\frac{1}{p}}\otimes 1$ is nilpotent.

## Push-forward and pull-back

### Example: Hartshorne $\mathrm{III}.12.4$ {#ecag-0006}

Let $Y$ be an integral scheme of finite type over an algebraically closed field $k$ and $f:X\rightarrow Y$ be a flat projective morphism whose fibres are integral schemes (hence connected, it's crucial in this problem, so the pushforward of a line bundle is still a line bundle, without this assumption, we know the pushforward is a vector bundle, but not necessarily a line bundle). Let $L,M$ be line bundles on $X$, and assume that $L_{y}\cong M_{y}$ on the fibre $X_{y}$, Then there exists a line bundle $N $on $Y$, such that 
$$L\cong M\otimes f^{*}N.$$
Just use Grauert theorem, we know $f_{*}F:=f_{*}(L\otimes M^{-1})$ is a a vector bundle with rank $h^{0}(X_{t},L_{t}\otimes M^{-1}_{t})$, together with the fact that fibres are all connected, we know it's a line bundle. And 
$$f_{*}F\otimesk(y)\rightarrow H^{0}(X_{y},F_{y})$$
is an isomorphism. But fibrewise $F_{y}$ is globally generated(it's just the trivial bundle in this situation), so this isomorphism just means we have a surjection on the fibres of
$$f^{*}f_{*}F\rightarrow F.$$
But it's also an injection simply because stalks have finite dimensions. Thus we conclude that 
$$f^{*}f_{*}F\cong F$$
now let $N$ be $f_{*}F$, we get the desired property.

### Remark: $f_{*}\mathcal{O}_{X}\cong \mathcal{O}_{Y}$ {#ecag-0007}

Use the same method as above, we get a sequence 
$$\mathcal{O}_{y,Y}\rightarrow k(y)\otimes f_{*}\mathcal{O}_{X}\rightarrow H^{0}(X_{t}, \mathcal{O}_{X_{t}})\cong k.$$
On the stalk level, the first map is an injection simply because $f_{*}\mathcal{O}_{X}$ is locally free. But they both have rank $1$, so it's an isomorphism.

### Example: Fibres being integral is necessary, actually flatness matters {#ecag-0008}

We want to compare the following two conditions

- $X$ is reduced and fibres are connected
- $f:X\rightarrow Y$ is flat projective with integral fibres.

The example is 
$$X=\mathrm{Spec}(k[x,y]/(x^{2},xy))\rightarrow Y=\mathrm{Spec}(k[y])$$
$$k[y]\rightarrow k[x,y]/(x^{2},xy); y\mapsto y.$$
This map is not flat ($x$ is a zero divisor), but it's projective (since finite), $X,Y$ are noetherian schemes and $Y$ is regular. But $f_{*}\mathcal{O}_{X}\neq \mathcal{O}_{Y}$, and $f_{*}\mathcal{O}_{X}$ is not an invertible module over $k[x]$, $x$ is a zero divisor.

### Example: Push-forward of a coherent sheaf might not be coherent {#ecag-0009}

$$f:X=\mathrm{Spec}(k(x))\rightarrow \mathrm{Spec}(k)=Y.$$
Then $f_{*}\mathcal{O}_{X}$ is not coherent over $\mathrm{Spec}(k).$

### Example: Push-forward of a quasi-coherent sheaf might not quasi-coherent {#ecag-0010}

Consider $$f:X=\amalg_{i=1}^{\infty}\mathrm{Spec}(\mathbb{Z})\rightarrow \mathrm{Spec}(\mathbb{Z})=S$$
which is given by the identity map on each component. We claim $f_{*}\mathcal{O}_{X}$ is not quasi-coherent on $S$. Since we know if we have a quasi-coherent sheaf $\mathscr{F}$ on $S$, we must have a bijection
$$\mathscr{F}(S)\otimes_{\mathbb{Z}}\mathcal{O}_{S}(U)\cong \mathscr{F}(U).$$
This is not true in this example, consider $U=D_{+}(2)$, then the corresponding map is
$$(\Pi_{i=1}^{\infty}\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}[\frac{1}{2}]\rightarrow \Pi_{i=1}^{\infty}\mathbb{Z}[\frac{1}{2}].$$
Note that the image of this morphism consists of sequences of rational numbers with a fixed denominator $2^{M}$, however this is not all of the RHS, for example, a sequence of rational numbers with odd numerators and denominators $2^{k_{i}}, k_{i}\rightarrow +\infty$. Thus this map is not surjective, $f_{*}\mathcal{O}_{X}$ is not a quasi-coherent sheaf on $\mathrm{Spec}(\mathbb{Z}).$ At the same time, it's very easy to construct some non-quasi-coherent sheaves, for example on $\mathbb{A}_{k}^{1}$ define a sheaf $\mathscr{F}$ by 
$$\mathscr{F}=\mathcal{O}_{X}(U), 0\notin U;$$
$$\mathscr{F}=0, 0\in U.$$
It's easy to check it's a sheaf, $\mathscr{F}(\mathbb{A}_{k}^{1})=0$, but this sheaf is not zero. Thus it's cannot be a quasi-coherent sheaf.

### Example: Push-forward might have different cohomology {#ecag-0011}

Consider $$f:\mathbb{P}_{k}^{1}\rightarrow \mathrm{Spec}(k).$$
Then $f_{*}\mathcal{O}_{\mathbb{P}_{k}^{1}}(-2)$ is a quasi-coherent sheaf on $\mathrm{Spec}(k)$. $\mathrm{Spec}(k)$ is noetherian affine, then we have $$H^{1}(\mathrm{Spec}(k),f_{*}\mathcal{O}_{\mathbb{P}_{k}^{1}}(-2))=0$$
on the other hand, we have 
$$H^{1}(\mathbb{P}_{k}^{1}, \mathcal{O}_{\mathbb{P}_{k}^{1}}(-2))=kx^{-1}y^{-1}.$$
Thus we see if $f:X\rightarrow Y$ is not affine, even if $X$ has very nice properties(not to say Noetherian, separated), 
$$H^{i}(X,\mathscr{F})\neq H^{i}(Y, f_{*}\mathscr{F}).$$

### Remark: Push-forward from a noetherian scheme {#ecag-0012}

In general we have

- $f:X\rightarrow Y$, where $X$ is noetherian, then the push-forward of a quasi-coherent sheaf is quasi-coherent.
- Moreover, if $X$ is separated, then $$\check{H}^{p}(\mathfrak{U},\mathscr{F})=H^{p}(X,\mathscr{F})$$

### Example: Proper push-forward v.s. finite flat push-forward {#ecag-0013}

Compare the followings

- A theorem from EGA says that if you have a morphism $f:X\rightarrow Y$ between two proper noetherian schemes and let $\mathscr{F}$ be a coherent sheaf on $X$, then all direct images $R^{i}f_{*}\mathscr{F}$ are coherent. Here you really have to be careful, just think about 
$$\mathrm{Spec}(k(x))\rightarrow \mathrm{Spec}(k)$$
again, the pushforward of the structure sheaf is not coherent since $\mathrm{Spec}(k(x))$ is NOT proper over $\mathrm{Spec}(k)$. Although topologically, it's just a map between two points.
- Let $f:X\rightarrow Y$ be a finite morphism, then $f_{*}\mathcal{O}_{X}$ is locally free if and only if $f$ is flat.
- Any surjective morphism to a regular one dimensional scheme (in practice, just means a curve) is automatically flat.
- Miracle flatness theorem.

### Example: Push-forward of a trivial bundle might not be trivial {#ecag-0014}

You can find more information in my notes `bundles'. Here I just want to talk about an easy example. 
$$f:\mathbb{P}^{1}\rightarrow \mathbb{P}^{1};[x,y]\mapsto [x^{2}, y^{2}].$$
Then we know $f_{*}\mathcal{O}_{\mathbb{P}^{1}}$ is a vector bundle on $\mathbb{P}^{1}$, use the push-pull formula to compute 
$$H^{0}(\mathbb{P}^{1}, \mathcal{O}_{\mathbb{P}^{1}}(n)\otimes f_{*}\mathcal{O}_{\mathbb{P}^{1}})$$
we get $$f_{*}\mathcal{O}_{\mathbb{P}^{1}}=\mathcal{O}_{\mathbb{P}^{1}}(-1)\oplus \mathcal{O}_{\mathbb{P}^{1}}.$$

### Remark: Good things happen sometimes {#ecag-0015}

In some special but important situation, we do have some thing like $$f_{*}\mathcal{O}_{D}=\oplus_{i=1}^{n}\mathcal{O}_{f_{*}D}.$$
For example, if $k$ is algebraically closed and $f:X\rightarrow Y$ is a finite morphism between smooth projective curves, $D=\sum n_{i}p_{i}$ and $f_{*}D$ is defined to be $\sum n_{i}f(p_{i})$. This is because $\mathcal{O}_{D}$ is just a skyscraper-type sheaf, just use the definition and the fact that this morphism is finite, we get $f_{*}\mathcal{O}_{D}=\oplus_{i=1}^{n}\mathcal{O}_{f_{*}D}$

### Example: $f^{*}f_{*}\mathscr{F}$ and $f_{*}f^{*}\mathscr{G}$ {#ecag-0016}

In general, it's always enlightening to think about 

- the affine case, or
- the degenerated case, for example $f: X\rightarrow \mathrm{Spec}(k).$

Then we have natural maps 
$$f^{*}f_{*}\mathscr{F}\rightarrow \mathscr{F}.$$
$$\mathscr{G}\rightarrow f_{*}f^{*}\mathscr{G}$$
can be understood and remembered easily. 

- If we're in the affine case, $f:\mathrm{Spec}(A)\rightarrow \mathrm{Spec}(B)$, and $M$ is an $A$-module, and denote $M'$ be the same abelian group as $M$ but with the $B$-module structure induced by the ring map $f^{\#}: B\rightarrow A$. Then $$f_{*}M=M', f^{*}f_{*}M=A\otimes_{B}M'$$
the point is that since the tensor product is over $B$, in general we cannot move $A$ to the right-side, but we do have a natural map
$$A\otimes_{B}M'\rightarrow M; a\otimes m\rightarrow am.$$
If $N$ is a $B$-module, then $$f^{*}N=A\otimes_{B}N, f_{*}f^{*}N=(A\otimes_{B}N)'$$
The last term means view $A\otimes_{B}N$ as a $B$-module by the ring map $f^{\#}$, then we do have 
$$N\rightarrow (A\otimes_{B}N)', n\mapsto 1\otimes n.$$
- In the degenerated case, 
$$f_{*}\mathscr{F}=H^{0}(X,\mathscr{F}), f^{*}f_{*}\mathscr{F}=\mathcal{O}_{X}\otimes_{k}H^{0}(X,\mathscr{F})(=\mathcal{O}_{X}^{h^{0}(X,\mathscr{F})}).$$
We do have a natural map 
$$\mathcal{O}_{X}\otimes_{k}H^{0}(X,\mathscr{F})\rightarrow \mathscr{F}$$
Similarly, a coherent sheaf over $k$ just means a finite dimensional vector space $V$, we have 
$$f_{*}f^{*}V=(V\otimes_{k}\mathcal{O}_{X})'$$
As usual, the last term means we view it as a $k$-module. Then we have a natural map
$$V\rightarrow (V\otimes_{k}\mathcal{O}_{X})'; v\mapsto v\otimes 1.$$
If $f$ is of finite type, you may think about it secretly as 
$$V\rightarrow V\otimes_{k}k[x]; v\mapsto v\otimes 1.$$

### Remark: Decomposition of $f^{*}f_{*}\mathscr{F}$ and $f_{*}f^{*}\mathscr{G}$ {#ecag-0017}

Qirui told me that if you have a nice enough (unramified, finite) morphism $f:X\rightarrow Y$, and a finite group $G$ acts on $X$ and compatible with $f$, $\mathscr{F}$ (resp. $\mathscr{G}$) is a coherent sheaf on $X$(resp. $Y$), then we have something like
$$f^{*}f_{*}\mathscr{F}=\oplus_{g\in G}g^{*}\mathscr{F}$$
$$f_{*}f^{*}\mathscr{G}=\mathscr{G}^{\oplus deg(f)}.$$

### Example: Push-forward... {#ecag-0018}

Typically, we always need to consider push-forward along

- a birational proper morphism.
- a flat projective morphism.
- a finite flat morphism.
- a finite morphism.

### Example: What prevents $f_{*}\mathcal{O}_{X}$ to be $\mathcal{O}_{Y}$ ? {#ecag-0019}

First we have many special situations

- If $f_{*}\mathcal{O}_{X}$ is a line bundle on $Y$, then $f_{*}\mathcal{O}_{X}=\mathcal{O}_{Y}.$
- If $f:X\rightarrow Y$ is a proper birational morphism, $Y$ is normal, then $f_{*}\mathcal{O}_{X}=\mathcal{O}_{Y}$.

### Example: Pullback is a locally free sheaf, but not a locally free sheaf itself {#ecag-0020}

Consider 
$$f:X=\mathrm{Spec}(\mathbb{Q})\rightarrow \mathrm{Spec}(\mathbb{Z})=Y$$
and the module $\mathscr{F}=\mathbb{Z}\oplus \mathbb{Z}/2\mathbb{Z}$ over $Y$, then $f^{*}\mathscr{F}\cong \mathbb{Q}$, it's a free sheaf of rank $1$ over $X$ but itself is obviously not free over $\mathrm{Spec}(\mathbb{Z})$, so in many situations, being faithfully flat is essential.

### Example: push-forward a vector bundle along a projective morphism might not be a vector bundle, even if cohomology groups of fibres are constant {#ecag-0021}

If you want to use cohomologe and base change, make sure $Y$ is integral. Consider the example
$$f:X=\mathbb{P}^{1}_{Y}\rightarrow \mathrm{Spec}(k[x]/(x^{2}))=Y$$
Then it's a projective morphismbetween noetherian schemes. Just consider the `Euler sequence' on $\mathbb{P}_{Y}^{1}$, then we have 
$$0\rightarrow \mathcal{O}_{\mathbb{P}_{Y}^{1}}(-2)\rightarrow \mathcal{O}^{2}_{\mathbb{P}_{Y}^{1}}(-1)\rightarrow \mathcal{O}_{\mathbb{P}_{Y}^{1}}\rightarrow 0$$
This is not what we want, we compute $$Ext^{1}(\mathcal{O}_{\mathbb{P}_{Y}^{1}},\mathcal{O}_{\mathbb{P}_{Y}^{1}}(-2))=H^{1}(\mathbb{P}_{Y}^{1}, \mathcal{O}_{\mathbb{P}_{Y}^{1}}(-2))\cong k[t]/(t^{2}).$$
We consider $t\in Ext^{1}$, then we have 
$$0\rightarrow \mathcal{O}_{\mathbb{P}_{Y}^{1}}(-2)\rightarrow E \rightarrow \mathcal{O}_{\mathbb{P}_{Y}^{1}}\rightarrow 0$$
And note that $H^{0}(X,E)$ is given by the kernel of 
$$H^{0}(X, \mathcal{O}_{\mathbb{P}_{Y}^{1}})\rightarrow H^{1}(X, \mathcal{O}_{\mathbb{P}_{Y}^{1}}(-2))$$
which is just a multiplication by $t$. Thus $H^{0}(X,E)$ is the ideal $(x)$, as a $k[x]/(x^{2})$-module, it's isomorphic to $k[x]/(x^{2})$, then $f_{*}E=H^{0}(X,E)$, it's not free. So we have a projective flat morphism between noetherian schemes, and a sheaf $E$ is flat over $Y$(since it's a vector bundle over $X$ and X is flat over $Y$), but $f_{*}E$ is not a locally free(vector bundle). The only condition missing is that in the cohomology and base-change theorem, we need $Y$ to be an integral scheme.

### Remark: $\mathrm{Ext}^{1}$ and maps in the corresponding extension {#ecag-0022}

> **Status:** Stub — content needed.

### Example: Pull-back a bundle along an isomorphism might not get an isomorphic bundle {#ecag-0023}

Let $E$ be an elliptic curve, then for $p,a\in E$, $\mathcal{O}(p)\cong \mathcal{O}(p+a)$ if and only if $a= 0\in E$. Let $\tau_{a}$ be the translation by $a$. It's an isomorphism of $E$. However
$$\mathcal{O}(p)\neq \mathcal{O}(p+a)=\tau_{a}^{*}(\mathcal{O}(p)).$$
On the other hand, if $X$ is a smooth variety and $G$ the finite automorphism group of $X$. We have 
$$\mathrm{Pic}^{G}(X)\cong \{\text{Equivariant Weil divisor}\}/\mathrm{div}\{\text{G-invariant functions}\}.$$
First by Hilbert 90, we know $H^{1}(G, \mathcal{O}(X)^{*})=0$, this tells us $\mathrm{Pic}^{G}(X)$ is embedded into $\mathrm{Pic}(X)$. Then we define a homomorphism 
$$\phi: \mathrm{Pic}(X)\rightarrow \{\text{Equivariant Weil divisor}\}/\mathrm{div}\{\text{G-invariant functions}\}$$
$$D+\mathrm{div}(f)\mapsto \frac{1}{|G|}\sum g^{*}D+\mathrm{div}(\frac{1}{|G|}\sum g^{*}f) $$
