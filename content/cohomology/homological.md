---
chapter: cohomology
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Cohomology_and_homological_algebra/homological.tex
---

## Homological algebra

### Example: $\mathrm{Hom}, \mathscr{H}om, Ext^{i}_{A}(-,-), \mathscr{E}xt^{i}_{-}(-,-), Tor^{i}_{-}(-,-)$ with Macaulay2 {#ecag-0227}

We learned these examples from 
- [Computing with sheaves and sheaf cohomology in algebraic geometry](http://swc.math.arizona.edu/aws/2006/06StillmanNotes.pdf)
- [Computing with sheaves and sheaf cohomology in algebraic geometry](http://www.math.sci.osaka-u.ac.jp/~msj-si-2015/school_slides/stillman-day2.pdf)
- [$\mathscr{E](https://math.stackexchange.com/questions/1550511/mathcalexti-mathcalo-l-1-mathcalo-l-2-and-textexti-mathc?rq=1)xt^{i}(\mathcal{O}_{L_{1}},\mathcal{O}_{L_{2}})$ for two lines $L_{1}, L_{2}$ in $\mathbb{P}^{3}$}

### Example: $\operatorname{Ext}^{1}$ and extension of vector bundles {#ecag-0228}

Consider the following example

- [vector bundles in $Ext^{1](https://math.stackexchange.com/questions/1529355/vector-bundles-in-textext1-mathcalo-mathbbp12-mathcalo-math?rq=1)(\mathcal{O}_{\mathbb{P}^{1}}(-2), \mathcal{O}_{\mathbb{P}^{1}}(2))$}
- [Extensions of vector bundles on $\mathbb{P](https://math.stackexchange.com/questions/1601588/extension-of-vector-bundles-on-mathbbcp1?rq=1)^{1}$}

\begin{example}[Compute $\mathrm{Ext}_{\mathbf{Z}}(\mathbf{Q}, \mathbf{Z})$]

### Remark {#ecag-0229}

$\mathrm{Ext}_{\mathbf{Z}}(A,B)=0$ for any $B$ if $A$ is a free abelian group. $\mathrm{Ext}_{\mathbf{Z}}(A,B)=0$ for any $A$ if $B$ is divisible (i.e  $\forall b\in B, 0\neq n\in \mathbf{Z}, \exists b'\in B$ such that $nb'=b$ ). Thus we have 

$$\mathrm{Ext}(\mathbf{Z},\mathbf{Z})=0, \mathrm{Ext}(\mathbf{Z},\mathbf{Q})=0$$

$$\mathrm{Ext}(\mathbf{Z}/n\mathbf{Z}, \mathbf{Q})=0, \mathrm{Ext}(\mathbf{Q}, \mathbf{Q})=0.$$

For $\mathbf{Z}/n\mathbf{Z}$, we have the free resolution $0\rightarrow \mathbf{Z}\rightarrow \mathbf{Z}\rightarrow \mathbf{Z}/n\mathbf{Z}\rightarrow 0$, apply $\hom(-, \mathbf{Z})$ or $\hom(-,\mathbf{Z}/m\mathbf{Z})$, we can get 

$$\mathrm{Ext}(\mathbf{Z}/m\mathbf{Z}, \mathbf{Z})=\mathbf{Z}/m\mathbf{Z}, \mathrm{Ext}(\mathbf{Z}/m\mathbf{Z}, \mathbf{Z}/m\mathbf{Z})=\mathbf{Z}/(m,n)\mathbf{Z}.$$

Sometimes, we can also use the torsion property of vector space structure for some abelian groups to compute the $\mathrm{Ext}$ groups. For example, $\mathrm{Ext}(\mathbf{Q}, \mathbf{Z}/m\mathbf{Z})$ is $m$-torsion by taking a free resolution of $\mathbf{Q}$ and then apply $\hom(-,\mathbf{Z}/m\mathbf{Z})$. It also has a $\mathbf{Q}$-vector space structure induced from the scalar multiplication of $\mathbf{Q}$. Thus we know

$$\mathrm{Ext}(\mathbf{Q}, \mathbf{Z}/m\mathbf{Z})=0.$$
