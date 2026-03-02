---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/hodge.tex
---

## Hodge numbers

### Example: Hodge numbers of a blow-up {#ecag-0231}

We give several computations of the hodge number of $Bl_{C}(\mathbb{P}^{3})$(over $\mathbb{C}$), where $C$ is the twisted cubic parametrized by $[u^{3}, u^{2}v, uv^{2}, v^{3}]$.

- $\chi^{p,q}=(-1)^{p+q}h^{p,q}$ is additive. Then we know 
$$\chi^{p,q}(Bl_{C}(\mathbb{P}^{3}))=\chi^{p,q}(\mathbb{P}^{1}\times \mathbb{P}^{1})+\chi^{p,q}(\mathbb{P}^{3})-\chi^{p,q}(C)$$
Then we know the Hodge diamond is given by 
$$\begin{pmatrix} & & & 1& & & \\
 & & 0& &0 & &\\
  & 0& & 2& &0 &\\
   0& & 0 & &0 & &0\\
    & 0& & 2& &0 &\\
     & & 0& &0 & &\\
      & & & 1& & &\end{pmatrix}$$
For computations of each terms, see the reference below.
- Mixed Hodge structure.
- Decomposition theorem.
- Computer algebra. Macaulay2. See [here](http://www2.macaulay2.com/Macaulay2/doc/Macaulay2-1.10/share/doc/Macaulay2/Schubert2/html/_blowup.html).

### Remark: refenrence {#ecag-0232}

[Computations of some Hodge numbers](http://www.math.purdue.edu/~dvb/preprints/book-chap17.pdf)
