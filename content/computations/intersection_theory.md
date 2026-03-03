---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/intersection_theory.tex
---

## Chow rings

### Example: Chow ring of $\overline{\mathrm{M}}_{0,n}$ {#ecag-0233}

**Statement:** The Chow ring of $\overline{\mathrm{M}}_{0,n}$ can be computed explicitly for small $n$ using Keel's presentation. For $n = 4$, we have $\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,4}) \cong \mathbb{Z}[\delta]/(\delta^{2})$. For $n = 5$, the Picard group has rank $5$, and the full Chow ring is isomorphic to $\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,5}) \cong \mathbb{Z}[H, E_{1}, E_{2}, E_{3}, E_{4}]/(H^{2} - 1, HE_{i}, E_{i}^{2} + 1, E_{i}E_{j})$, arising from the identification $\overline{\mathrm{M}}_{0,5} \cong \operatorname{Bl}_{4\text{pts}}(\mathbb{P}^{2})$.

**Construction/Proof:**

*Step 1: The case $n = 4$.* We have $\overline{\mathrm{M}}_{0,4} \cong \mathbb{P}^{1}$. In Keel's description, the boundary divisors satisfy $\delta_{1,2} = \delta_{1,3} = \delta_{1,4}$ and $\delta_{1,2}\delta_{1,3} = 0$. Hence

$$
\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,4}) \cong \operatorname{CH}^{*}(\mathbb{P}^{1}) \cong \mathbb{Z}[\delta]/(\delta^{2}).

$$

*Step 2: The case $n = 5$, generators and relations.* We have $\binom{5}{2} = 10$ generators $\delta_{i,j}$. Keel's relations give, for distinct $i, j, k, l$:

$$
\delta_{i,j} + \delta_{k,l} = \delta_{i,k} + \delta_{j,l} = \delta_{i,l} + \delta_{j,k}.

$$

Multiplying these equations by $\delta_{i,j}$ and applying the disjointness relation in Keel's description yields the product relations:

$$
\delta_{i,j}^{2} = \delta_{k,l}^{2} = -\delta_{a,b}\delta_{c,d},

$$

where $a, b, c, d$ are any four distinct elements of $\{1, 2, 3, 4, 5\}$. All triple products and higher vanish by a dimension argument since $\dim \overline{\mathrm{M}}_{0,5} = 2$.

*Step 3: Computing the rank of the Picard group.* Labeling the ten divisors $\{\delta_{1,2}, \delta_{1,3}, \ldots, \delta_{4,5}\}$ lexicographically as $\{e_{1}, \ldots, e_{10}\}$, the linear relations among them are encoded in a matrix whose row reduction reveals:

$$
\operatorname{rank}(\operatorname{Pic}(\overline{\mathrm{M}}_{0,5})) = 5.

$$

Explicitly, the dependent generators can be expressed in terms of the five free generators $\delta_{1,5}, \delta_{2,5}, \delta_{3,4}, \delta_{3,5}, \delta_{4,5}$:

$$
\delta_{1,2} = \delta_{1,3} + \delta_{2,4} - \delta_{3,4},

$$

$$
\delta_{1,3} = \delta_{1,4} + \delta_{2,3} - \delta_{2,4},

$$

$$
\delta_{1,4} = \delta_{1,5} + \delta_{3,4} - \delta_{3,5},

$$

$$
\delta_{2,3} = \delta_{2,5} + \delta_{3,4} - \delta_{4,5},

$$

$$
\delta_{2,4} = \delta_{2,5} + \delta_{3,4} - \delta_{3,5}.

$$

*Step 4: Geometric identification via blow-ups.* The space $\overline{\mathrm{M}}_{0,5}$ admits a geometric description as a blow-up. The universal curve diagram specializes to show that $\overline{\mathrm{M}}_{0,5} \cong \operatorname{Bl}_{(0,0),(1,1),(\infty,\infty)}(\mathbb{P}^{1} \times \mathbb{P}^{1})$, where the three blown-up points lie on the diagonal.

Now, $\operatorname{Bl}_{2\text{pts}}(\mathbb{P}^{2})$ is isomorphic to $\operatorname{Bl}_{1\text{pt}}(\mathbb{P}^{1} \times \mathbb{P}^{1})$. To see this, observe that $\operatorname{Bl}_{2\text{pts}}(\mathbb{P}^{2})$ contains three $(-1)$-divisors: $E_{1}$, $E_{2}$, and $H - E_{1} - E_{2}$ (the strict transform of the line through the two points). Consider the ample divisor $2H - E_{1} - E_{2}$, which corresponds to conics passing through the two points. This embeds the surface as a degree $2$ smooth surface in $\mathbb{P}^{3}$, which over an algebraically closed field is isomorphic to $\mathbb{P}^{1} \times \mathbb{P}^{1}$. The embedding precisely contracts the strict transform $H - E_{1} - E_{2}$.

Combining, we obtain $\overline{\mathrm{M}}_{0,5} \cong \operatorname{Bl}_{4\text{pts}}(\mathbb{P}^{2})$, where the four points are in general position. The Chow ring is therefore:

$$
\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,5}) \cong \mathbb{Z}[H, E_{1}, E_{2}, E_{3}, E_{4}]/(H^{2} - 1, HE_{i}, E_{i}^{2} + 1, E_{i}E_{j}).

$$

An open question from this computation: what are the boundary divisors $\delta_{i,j}$ expressed in terms of $H, E_{1}, E_{2}, E_{3}, E_{4}$?

**Key Insight:** The moduli space $\overline{\mathrm{M}}_{0,5}$ is a del Pezzo surface of degree $5$. Recognizing it as a blow-up of $\mathbb{P}^{2}$ at four general points immediately gives the Chow ring from the blow-up formula, bypassing the complexity of Keel's abstract generators-and-relations presentation.

**Prerequisites:** Chow rings, blow-up formula for Chow rings, Keel's theorem on $\overline{\mathrm{M}}_{0,n}$, del Pezzo surfaces, Hirzebruch surfaces

<!-- BENCHMARK_PROBLEM: Compute the rank of $\operatorname{Pic}(\overline{\mathrm{M}}_{0,5})$ using Keel's presentation by boundary divisors $\delta_{S}$. Express the answer as a single integer. -->

### Remark: Keel, Chow ring of $\overline{\mathrm{M}}_{0,n}$ {#ecag-0234}

Sean Keel computed $\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,n})$ in the paper *Intersection theory of moduli space of stable $n$-pointed curves of genus $0$*. The result states that $\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,n})$ is generated by boundary divisors $\{\delta_{S} \mid S \subset \{1, 2, \ldots, n\},\; \#S \geq 2,\; \#S^{c} \geq 2\}$ subject to the following relations:

1. **Symmetry:** $\delta_{S} = \delta_{S^{c}}$.

2. **Linear equivalences:** For any four distinct elements $i, j, k, l \in \{1, 2, \ldots, n\}$,

$$
\sum_{\substack{i,j \in S \\ k,l \in S^{c}}} \delta_{S} = \sum_{\substack{i,k \in S \\ j,l \in S^{c}}} \delta_{S} = \sum_{\substack{i,l \in S \\ j,k \in S^{c}}} \delta_{S}.

$$

3. **Disjointness:** $\delta_{S} \cdot \delta_{T} = 0$ unless one of the four containments $S \subset T$, $S \subset T^{c}$, $S^{c} \subset T$, or $S^{c} \subset T^{c}$ holds.

These relations are complete: they generate the full ideal of relations in $\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,n})$. The linear equivalences (relation 2) arise from pulling back the relation $[0] = [1] = [\infty]$ in $\operatorname{CH}^{1}(\mathbb{P}^{1})$ via the forgetful morphisms $\overline{\mathrm{M}}_{0,n} \to \overline{\mathrm{M}}_{0,4} \cong \mathbb{P}^{1}$. The disjointness relation (relation 3) reflects the fact that two boundary divisors corresponding to non-nested partitions have empty intersection.

<!-- BENCHMARK_PROBLEM: In Keel's presentation of $\operatorname{CH}^{*}(\overline{\mathrm{M}}_{0,6})$, how many distinct boundary divisor generators $\delta_{S}$ are there (after identifying $\delta_{S} = \delta_{S^{c}}$)? Express the answer as a single integer. -->

### Remark: Blow-ups of $\mathbb{P}^{2}$ {#ecag-0235}

Several subtle distinctions arise when comparing blow-ups of $\mathbb{P}^{2}$ and $\mathbb{P}^{1} \times \mathbb{P}^{1}$. One must be careful about the positions of the blown-up points.

**Key facts:**

- $\operatorname{Bl}_{2\text{pts}}(\mathbb{P}^{2}) \cong \operatorname{Bl}_{1\text{pt}}(\mathbb{P}^{1} \times \mathbb{P}^{1})$: Both are the Hirzebruch surface $\mathbb{F}_{1}$ blown up once, equivalently a del Pezzo surface of degree $7$. However, $\mathbb{F}_{1} := \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(1)) \cong \operatorname{Bl}_{1\text{pt}}(\mathbb{P}^{2}) \not\cong \mathbb{P}^{1} \times \mathbb{P}^{1}$, since $\mathbb{P}^{1} \times \mathbb{P}^{1}$ contains no $(-1)$-curve while $\mathbb{F}_{1}$ does. This also shows $\mathbb{F}_{1}$ is not minimal, whereas all other Hirzebruch surfaces $\mathbb{F}_{n}$ ($n \neq 1$) are minimal.

- $\operatorname{Bl}_{\text{3 distinct pts on } \Delta}(\mathbb{P}^{1} \times \mathbb{P}^{1}) \cong \operatorname{Bl}_{\text{4 general pts}}(\mathbb{P}^{2})$: This follows from the identification $\operatorname{Bl}_{2\text{pts}}(\mathbb{P}^{2}) \cong \operatorname{Bl}_{1\text{pt}}(\mathbb{P}^{1} \times \mathbb{P}^{1})$ applied iteratively.

- $\operatorname{Bl}_{\text{3 general pts}}(\mathbb{P}^{1} \times \mathbb{P}^{1}) \cong \operatorname{Bl}_{\text{3 distinct pts on } \Delta}(\mathbb{P}^{1} \times \mathbb{P}^{1})$: In $\mathbb{P}^{1} \times \mathbb{P}^{1}$, any three distinct points can be moved to the diagonal by an automorphism of $\mathbb{P}^{1} \times \mathbb{P}^{1}$ (as long as no two share a row or column fiber).

- $\operatorname{Bl}_{\text{4 general pts}}(\mathbb{P}^{2}) \not\cong \operatorname{Bl}_{\text{4 pts, 3 on a line}}(\mathbb{P}^{2})$: If three of the four blown-up points lie on a line $L$ in $\mathbb{P}^{2}$, the strict transform $L'$ has class $H - E_{1} - E_{2} - E_{3}$, so $L'^{2} = 1 - 3 = -2$. This produces a $(-2)$-curve, which does not exist when the four points are in general position (where all $(-1)$-curves have self-intersection exactly $-1$).

<!-- BENCHMARK_PROBLEM: Let $X = \operatorname{Bl}_{p_1, p_2, p_3, p_4}(\mathbb{P}^2)$ where $p_1, p_2, p_3$ are collinear and $p_4$ is in general position. Compute the self-intersection number of the strict transform of the line through $p_1, p_2, p_3$. Express the answer as a single integer. -->

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
## Five conics problems via fundamental class
Excess intersection theory or intersection theory on the space of complete conics (i.e Blow up of the degree $2$ Veronese surface in $\mathbf{P}(\mathrm{H}^{0}(\mathcal{O}_{\mathbf{P}^{2}}(2)))\cong \mathbf{P}^{5}$) shows that $3264$ smooth conics tangent to $5$ generic conics. Here we want to interpret the the computations in excess intersection theory in term of the construction of the fundamental class of a moduli problem. We know the locus of conics that are tangent to a given conic is a degree $6$ hypersurface in $\mathbf{P}^{5}$. We have to consider the intersection $\mathcal{M}=\bigcap_{i=1}^{5}Z_{i}$ degree $6$ hypersurfaces of this form, each with defining equation $f_{i}$. We view them as sections of $\mathcal{O}_{\mathbf{P}^{5}}(6)$. The universal property of $\mathcal{M}$ comes from the fact that it's a fibre product. $\mathcal{M}$ is not a complete intersection, the construction of the fundamental class in this case is just that we scaling the images all those global sections $f_{i}\rightarrow tf_{i}$. When $t\rightarrow +\infty$, we end up with the normal cone $C_{\mathcal{M}/\mathbf{P}^{5}}$ of $\mathcal{M}$ in $\mathbf{P}^{5}$, which lives in $E:=\bigoplus_{i=1}^{5}\mathcal{O}_{\mathbf{P}^{5}}(6)$, and the support of it is just $\mathcal{M}$.  Although the cone is not a global section of $E|_{\mathcal{M}}$. The principle of fundamental classes is just that we view it as a global section. Then $[\mathcal{M}]^{\mathrm{vir}}$ is defined to be $[C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}}]\cap \mathcal{M}$, this intersection is well-defined because we have the Gysin isomorphism $0^{!}: A_{k}(E)\rightarrow A_{k-\operatorname{rk}{E}}(\mathcal{M})$. In other words, we're in the following situation: the normal cone $C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}}$ embeds into the vector bundle $E = \mathcal{O}^{\oplus 5}_{\mathbf{P}^{5}}(6)$ over $\mathcal{M} \hookrightarrow \mathbf{P}^{5}$.

The computation of $[\mathcal{M}]^{\mathrm{vir}}$ boils down to the computation of the Gysin map. We have the closed embeddings $\mathcal{M} \hookrightarrow C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}} \hookrightarrow E|_{\mathcal{M}}$. In this situation (see for example Ravi Vakil's notes), we have

$$
[C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}}]\cap [\mathcal{M}]=\{c(E|_{\mathcal{M}})s(\mathcal{M}, C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}})\}_{0}.

$$

The normal cone is just the normal bundle, but one subtle thing here is that although set-theoretically the $2$-dimensional component $T$ of $\mathcal{M}$ is just the degree $2$ Veronese surface $S$, scheme-theoretically, it's not. The multiplicity of $Z_{i}$ along $S$ is $2$ (see for example Eisenbud and Harris, *3264 and All That*, p. 463). Then we know the degree $k$ piece of the Segre class $s(\mathcal{M}, C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}})$ is given by

$$
s_{k}(\mathcal{M}, C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}})=2^{k+3}s(S, N_{S/\mathbf{P}^{5}})+s_{k}(\text{zero dimensional components of } \mathcal{M}).

$$

Now we compute

$$
c(E|_{\mathcal{M}})=(1+6H)^{5}|_{\mathcal{M}}=(1+12h)^{5}.

$$

$$
c(N_{S/\mathbf{P}^{5}})=\frac{(1+H)^{6}|_{S}}{(1+h)^{3}}=1+9h+30h^{2}.

$$

Which implies

$$
s(S, N_{S/\mathbf{P}^{5}})=1-9h+51h^{2}.

$$

Thus

$$
s_{k}(\mathcal{M}, C_{\mathcal{M}/\mathbf{P}^{5}}|_{\mathcal{M}})=8-144h+1632h^{2}+s_{k}(\text{zero dimensional components of } \mathcal{M}).

$$

Finally, we get

$$
[\mathcal{M}]^{\mathrm{vir}}=\deg((1+12h)^{5}(8-144h+1632h^{2}))+\text{zero dimensional components of } \mathcal{M}

$$

$$
=4512[\text{pt on } T]+\text{zero dimensional components of } \mathcal{M}.

$$

Now use the fact that

$$
i_{*}[\mathcal{M}]^{\mathrm{vir}}=c_{\mathrm{top}}(E)=7776[\text{pt on } \mathbf{P}^{5}]

$$

We get

$$
\text{number of zero dimensional components of } \mathcal{M}=7776-4512=3264.

$$

However, from the point of view of fundamental classes, the important thing is not the solution $3264$ of the five conics problem, it's the fact that $[\mathcal{M}]^{\mathrm{vir}}$ is given by $4512$ points on the non-reduced Veronese surface plus all zero dimensional components of $\mathcal{M}$.
## Quantum cohomology of projective spaces We apply basic Schubert calculus to prove that

$$
QH^{*}(\mathbf{P}^{n}, \mathbf{Z})=\mathbf{Z}[h_{1},q]/(h_{1}^{n+1}-q).

$$

The most annoying part is the notation, we use the following

$$
\begin{tabular}{ |p{3cm}||p{3cm}|p{3cm}|p{3cm}|  }
 \hline
 \multicolumn{4}{|c|}{$\mathbf{P}^{n}$} \\
 \hline
 \text{Algebraic cycles}& $\mathrm{H}_{*}(\mathbf{P}^{n}, \mathbf{Z})$ & $\mathrm{H}^{*}(\mathbf{P}^{n},\mathbf{Z})$ &\text{Differential forms}\\
 \hline
 \text{[pt]}  & $\mathrm{H}_{0}, H^{n}$    & $\mathrm{H}^{0}, h_{0}$ &  \text{constant functions}\\
 \hline
  \text{[$\mathbf{P}^{1}$]}  & $\mathrm{H}_{2}, H^{n-1}$    & $\mathrm{H}^{2}, h_{1}$ &  \text{$(1,1)$-forms}\\
 \hline
 ...&...&...&...\\
 \hline
   \text{[$\mathbf{P}^{n}$]}  & $\mathrm{H}_{2n}, H^{0}$    & $\mathrm{H}^{2n}, h_{n}$ &  \text{$(n,n)$-forms}\\
 \hline
\end{tabular}

$$
Two extra terms for the computation

$$\mathrm{H}_{2}(\mathbf{P}^{n}, \mathbf{Z})=\mathbf{Z} H^{n-1}, q^{rH^{n-1}}\leftrightarrow q^{r}$$

$$\dim \mathcal{M}_{0,3}(\mathbf{P}^{n}, rH^{n-1})=(\dim \mathbf{P}^{n}-3)(1-0)+3+\int_{rH^{n-1}}T_{\mathbf{P}^{n}}=n+r(n+1).$$

The quantum product is defined to be

$$h_{i}\circ h_{j}:=\sum (h_{i}\circ h_{j})_{rH^{n-1}}q^{r}$$

$$=\sum\langle H^{i}|H^{j}|H^{k}\rangle_{rH^{n-1}}h_{k}q^{r}.$$

Since $\operatorname{ev}_{1}^{*}(H^{i})\cup \operatorname{ev}_{2}^{*}(H^{j})\cup \operatorname{ev}^{*}_{3}(H^{k})$ cuts down the dimension of $\mathcal{M}_{0,3}(\mathbf{P}^{n}, rH^{n-1})$ by at most $3n$. Thus $\langle H^{i}|H^{j}|H^{k}\rangle_{rH^{n-1}}\neq 0$ only if $r=0$ or $1$. First we have the classical intersection part
$$\langle H^{i}|H^{j}|H^{k}\rangle_{0}=\begin{cases}1 & i+j+k=n\\
0 & \text{otherwise}.\end{cases}$$
To compute $\langle H^{i}|H^{j}|H^{k}\rangle_{1H^{n-1}}$, we use basic Schubert calculus. The geometric meaning of  $\langle H^{i}|H^{j}|H^{k}\rangle_{1H^{n-1}}$ is that projective lines intersecting with $H^{i}, H^{j}$ and $H^{k}$. In other words, it means $2$-planes in $\mathbf{C}^{n+1}$ intersecting $(n+1-i)$-plane, $(n+1-j)$-plane and $(n+1-k)$-plane nontrivially. In $\operatorname{Gr}(2, n+1)$, the Schubert cycle corresponding to $2$-planes intersecting a $l$-plane nontrivially is exactly $\sigma_{n+1-2-l+1}$. Thus we have to compute

$$\sigma_{i-1}\sigma_{j-1}\sigma_{k-1}\in A^{*}(\operatorname{Gr}(2, n+1)).$$

Luckily, they're all special cycles in the sense that we can apply Pieri's rule. Note that the quantum product only takes the degree $0$ part. Now the question is that how many different ways can we find to add $(j-1)+(k-1)$ boxes (in different columns) to a length $i-1$ row such that we can finally fill up a $2(n-1)$-rectangular? The only possibility is that $(i-1)+(j-1)+(k-1)=2n-2$, that is $i+j+k=2n+1$. And in this case, we have exactly a unique way to fill up the rectangular. In conclusion, we have
$$\langle H^{i}|H^{j}|H^{k}\rangle_{H^{n-1}}=\begin{cases}1 & i+j+k=2n+1\\
0 & \text{otherwise}.\end{cases}$$
All together, we get the desired

$$QH^{*}(\mathbf{P}^{n}, \mathbf{Z})=\mathbf{Z}[h_{1},q]/(h_{1}^{n+1}-q).$$

## Quantum cohomology of the flag variety associated to a unitary group
Consider the flag variety

$$F_{3}=F_{1,2}=\{(L,V)\in \operatorname{Gr}(1, \mathbf{C}^{3})\times \operatorname{Gr}(2,\mathbf{C}^{3})\mid L\subset V\}\cong U_{3}/(U_{1}\times U_{1}\times U_{1}).$$

We have

$$QH^{*}(\mathbf{P}(\mathcal{V}), \mathbf{Z})=\mathbf{Z}[\alpha, \zeta]/(\zeta^{2}-\alpha\zeta+\alpha^{2}-q_{1}-q_{2}, \alpha^{3}-\alpha q_{1}-\zeta q_{1}).$$

First note that $F_{3}$ is nothing but the projectivization of the tautological bundle $\mathcal{V}$ on $\operatorname{Gr}(2, \mathbf{C}^{3})$. We denote it by $\mathbf{P}(\mathcal{V})$. Since the Schubert cells give $\mathbf{P}(\mathcal{V})$ a CW-structure, the cohomology ring is the same as the Chow ring. Let $\zeta=c_{1}(\mathcal{O}_{\mathbf{P}(\mathcal{V})}(1))$, then

$$A^{*}(\mathbf{P}(\mathcal{V}))=A^{*}(\operatorname{Gr}(1, \mathbf{C}^{3}))[\zeta]/(\zeta^{2}+c_{1}(\mathcal{V})\zeta+c_{2}(\mathcal{V})).$$

$$c(\mathcal{V})=1-\sigma_{1}+\sigma_{1,1}=1-[\mathbf{P}^{1}]+[\mathrm{pt}].$$

We have the following

$$
\begin{tabular}{ |p{3cm}||p{3cm}|p{3cm}|p{5cm}|  }
 \hline
 \multicolumn{4}{|c|}{$\mathbf{P}(\mathcal{V})$} \\
 \hline
 \text{Algebraic cycles}& $\mathrm{H}_{*}(\mathbf{P}(\mathcal{V}), \mathbf{Z})$ & $A^{*}(\mathbf{P}(\mathcal{V}),\mathbf{Z})$ &\text{Algebraic cocycles}\\
 \hline
 \text{[pt]}  & $\mathrm{H}_{0}$    & $\mathrm{H}^{0}; 1$ & $[\mathbf{P}(\mathcal{V})]$\\
 \hline
  \text{$\pi^{*}[\mathrm{pt}]$}, \text{$[\mathbf{P}^{1}]$}  & $\mathrm{H}_{2}; F, L $    & $\mathrm{H}^{2}; \zeta, \alpha$ & $[\mathbf{P}^{2}], \pi^{*}[\mathbf{P}^{1}]$\\
 \hline
 \text{$\pi^{*}[\mathbf{P}^{1}]$},$[\mathbf{P}^{2}]$ & $\mathrm{H}_{4}; l,f$    & $\mathrm{H}^{4}; \alpha^{2}, \zeta^{2}$ &  $\pi^{*}[\mathrm{pt}]=[\text{Fibre}], [\mathbf{P}^{1}]$\\
 \hline
   \text{[$\mathbf{P}(\mathcal{V})$]}  & $\mathrm{H}_{6}$    & $\mathrm{H}^{6};\alpha^{2}\zeta= \alpha\zeta^{2} $ &  $[\mathrm{pt}]$\\
 \hline
\end{tabular}

$$
Here by 'algebraic cocycles', we just mean algebraic cycles graded by their codimensions. Here we give different names to the same algebraic cycle depends on we view it as elements in $\mathrm{H}^{*}$ or $\mathrm{H}_{*}$. In this notation, we rewrite

$$A^{*}(\mathbf{P}(\mathcal{V}))=\mathbf{Z}[\alpha,\zeta]/(\zeta^{2}-\alpha\zeta+\alpha^{2}, \alpha^{3}).$$

Two extra terms we need for the computation of the quantum cohomology ring

$$\mathrm{H}_{2}(\mathbf{P}(\mathcal{V}), \mathbf{Z})=\mathbf{Z} F\oplus \mathbf{Z} L, q^{rF+sL}\leftrightarrow q_{1}^{r}q_{2}^{s}$$

$$\dim \mathcal{M}_{0,3}(\mathbf{P}(\mathcal{V}), rF+sL)=(\dim \mathbf{P}(\mathcal{V})-3)(1-0)+3+\int_{rF+sL}c_{1}(T_{\mathbf{P}(\mathcal{V})})=3+2r+2s.$$

Here we used the fact that $c_{1}(T_{\mathbf{P}(\mathcal{V})})=2\zeta+2\alpha$.
As an example, we compute $\alpha\circ \alpha$
\begin{align*}
\alpha\circ \alpha :&=\sum (\alpha\circ \alpha)_{rF+sL}q_{1}^{r}q_{2}^{s} \\
&=\sum_{(r,s)}\sum_{\gamma\in \mathrm{H}_{*}}\langle l|l|\gamma\rangle_{rF+sL}\gamma^{\vee}q_{1}^{r}q_{2}^{s}.
\end{align*}
Now we compute
\begin{align*}
\langle l,l,l\rangle_{(0,0)} &= l^{3}=\alpha^{3}=0, \\
\langle l,l,f\rangle_{(0,0)} &= \alpha^{2}\zeta=[\mathrm{pt}], \deg([\mathrm{pt}])=1.
\end{align*}

$$f^{\vee}=\alpha^{2}.$$

Similarly,
\begin{align*}
\langle l|l|[\mathrm{pt}]\rangle_{(1,0)} &= F, \\
\langle l|l|[\mathrm{pt}]\rangle_{(0,1)} &= \operatorname{Gr}(1, \mathbf{P}^{2}).
\end{align*}
Then we know there's exactly one stable map of degree $1$ intersecting two different $l$. But the moduli space of degree $1$ stable maps to the base $\mathbf{P}^{2}$  has positive dimension, which gives us Gromov-Witten invariant $0$. In other words, we have

$$\alpha\circ \alpha =f^{\vee}+1q^{1}=\alpha^{2}+q_{1}.$$

Similar argument gives us

$$\zeta\circ \zeta=\zeta^{2}+q_{2}$$

Then we finally get the quantum cohomology ring of $\mathbf{P}(\mathcal{V})$

$$QH^{*}(\mathbf{P}(\mathcal{V}), \mathbf{Z})=\mathbf{Z}[\alpha, \zeta]/(\zeta^{2}-\alpha\zeta+\alpha^{2}-q_{1}-q_{2}, \alpha^{3}-\alpha q_{1}-\zeta q_{1}).$$

In Martin A. Guest's book *From cohomology to integrable systems*, Example 2.6, you can find another computation of this quantum cohomology ring, the result is given by

$$QH^{*}(\mathbf{P}(\mathcal{V}), \mathbf{Z})=\frac{\mathbf{Z}[x_{1}, x_{2}, x_{3}, q_{1}, q_{2}, q_{3}]}{(x_{1}+x_{2}+x_{3}, x_{1}x_{2}+x_{1}x_{3}+x_{2}x_{3}+q_{1}+q_{2}+q_{3}, x_{1}x_{2}x_{3}+x_{1}q_{2}+x_{3}q_{1})}.$$

And

$$QH^{*}(\mathbf{P}(\mathcal{V}), \mathbf{Z})=\mathbf{Z}[a,b, q_{1}, q_{2}]/(a^{2}+b^{2}-ab-q_{1}-q_{2}, ab^{2}-a^{2}b-aq_{2}-bq_{1}).$$

Our result is easily seen to be the same as the second one because

$$\alpha(\zeta^{2}-\alpha\zeta+\alpha^{2}-q_{1}-q_{2})-(\alpha^{3}-\alpha q_{1}-\zeta q_{1})=\alpha\zeta^{2}-\alpha^{2}\zeta-\alpha q_{2}+\zeta q_{1}.$$

## Examples of quantum differential equations
## Equivariant cohomology
We view equivariant cohomology as the geometry of a system of varieties and view equivariant Chern classes as information contained in a system of vector bundles. We'll show this with some examples. By the approximation theorem in equivariant cohomology, we know if $\mathbb{E}_{m}$ is a connected space with a free $G$-action and $\mathrm{H}^{i}(\mathbb{E}_{m})=0$ for $0<i<k(m)$, then

$$\mathrm{H}_{G}^{*}(X):=\mathrm{H}^{*}(\mathbb{E}G\times_{G}X)=\mathrm{H}^{*}(\mathbb{E}_{m}\times_{G}X), \forall *<k(m).$$

### Example: $G=(\mathbf{C}^{\times})^{n}, X=\operatorname{pt}$ {#ecag-0236}

**Statement:** For the algebraic torus $G = (\mathbf{C}^{\times})^{n}$ acting on a point, the equivariant cohomology ring is the polynomial ring

$$
\mathrm{H}_{G}^{*}(\operatorname{pt}) = \mathbf{Z}[t_{1}, \ldots, t_{n}],

$$

where $t_{i} = c_{1}(\mathcal{O}_{\mathbf{P}^{\infty}}(1))$ on the $i$-th factor.

**Construction/Proof:** By the approximation theorem, $\mathrm{H}_{G}^{*}(\operatorname{pt})$ is computed as the limit of $\mathrm{H}^{*}(\operatorname{pt} \times_{G} (\mathbf{C}^{m} \setminus \{0\})^{n})$ as $m \to \infty$. Since the torus $(\mathbf{C}^{\times})^{n}$ acts diagonally on $(\mathbf{C}^{m} \setminus \{0\})^{n}$ with each factor acting freely on the corresponding $\mathbf{C}^{m} \setminus \{0\}$, we have the identification

$$
\operatorname{pt} \times_{G} (\mathbf{C}^{m} \setminus \{0\})^{n} = (\mathbf{P}^{m-1})^{n}.

$$

This gives a chain of closed embeddings:

$$
\operatorname{pt} \hookrightarrow (\mathbf{P}^{0})^{n} \hookrightarrow (\mathbf{P}^{1})^{n} \hookrightarrow \cdots \hookrightarrow (\mathbf{P}^{m-1})^{n} \hookrightarrow \cdots

$$

Taking the inverse limit of cohomology along these inclusions, and using the Kunneth formula $\mathrm{H}^{*}((\mathbf{P}^{m-1})^{n}) = \mathbf{Z}[t_{1}, \ldots, t_{n}]/(t_{1}^{m}, \ldots, t_{n}^{m})$, we obtain in the limit:

$$
\mathrm{H}_{G}^{*}(\operatorname{pt}) = \mathrm{H}^{*}((\mathbf{P}^{\infty})^{n}) = \mathbf{Z}[t_{1}, \ldots, t_{n}].

$$

**Key Insight:** The classifying space $BG = B(\mathbf{C}^{\times})^{n} = (\mathbf{P}^{\infty})^{n}$ is approximated by products of finite projective spaces, and the equivariant cohomology of a point is simply the cohomology of the classifying space, which for a torus is a polynomial ring with one generator per circle factor.

**Prerequisites:** Equivariant cohomology, classifying spaces, Borel construction, Kunneth formula, inverse limits in cohomology

<!-- BENCHMARK_PROBLEM: Compute $\mathrm{H}^{*}_{(\mathbf{C}^{\times})^3}(\operatorname{pt})$ as a graded ring. Express the answer as a quotient of a polynomial ring (or a polynomial ring itself). -->

### Example: $G=(\mathbf{C}^{\times})^{n}, X=\operatorname{Gr}(k,n)$ {#ecag-0237}

**Statement:** The $(\mathbf{C}^{\times})^{n}$-equivariant cohomology of the Grassmannian $\operatorname{Gr}(k, n)$ is given by

$$
\mathrm{H}^{*}_{G}(\operatorname{Gr}(k,n)) = \frac{\mathbf{Z}[t_{1}, \ldots, t_{n}][c_{1}, \ldots, c_{k}, c'_{1}, \ldots, c'_{n-k}]}{((1 + c_{1} + \cdots + c_{k})(1 + c'_{1} + \cdots + c'_{n-k}) = c(V))},

$$

where $c(V) = \prod_{i=1}^{n}(1 + t_{i})$ is the total Chern class of the equivariant tautological representation, and $c_{j}$, $c'_{j}$ are the equivariant Chern classes of the tautological and quotient bundles respectively. As a special case, $\mathrm{H}^{*}_{G}(\mathbf{P}^{n-1}) = \mathbf{Z}[t_{1}, \ldots, t_{n}][\zeta] / \prod_{i=1}^{n}(\zeta + t_{i})$.

**Construction/Proof:** The Borel construction gives the chain of varieties $\operatorname{Gr}(k,n) \times_{G} (\mathbf{C}^{m} \setminus \{0\})^{n}$, which we now identify as Grassmannian bundles over products of projective spaces.

*Step 1: Identifying the equivariant vector bundle.* Let $E = \mathbf{C}^{n}$ with the standard torus action, where $(\mathbf{C}^{\times})^{n}$ acts by scaling the $i$-th coordinate by the $i$-th factor. Then the mixed quotient is

$$
V_{m} := E \times_{G} (\mathbf{C}^{m} \setminus \{0\})^{n} = \bigoplus_{i=1}^{n} \mathcal{O}_{i}(-1),

$$

where $\mathcal{O}_{i}(-1)$ denotes the tautological line bundle on the $i$-th $\mathbf{P}^{m-1}$ factor. This identification holds because the fibers of $E$ carry the same weights as the base: the $i$-th coordinate of $E$ transforms under the same character as the $i$-th copy of $\mathbf{C}^{m} \setminus \{0\}$.

*Step 2: Grassmannian bundle structure.* Naturally,

$$
\operatorname{Gr}(k,n) \times_{G} (\mathbf{C}^{m} \setminus \{0\})^{n} = \operatorname{Gr}(V_{m}, k),

$$

i.e., it is the Grassmannian bundle of $k$-planes in the fibers of the rank-$n$ vector bundle $V_{m}$ over $(\mathbf{P}^{m-1})^{n}$.

*Step 3: Taking the limit.* By the standard computation of the cohomology of a Grassmannian bundle (via the splitting principle and the Whitney sum formula), the Chow ring / cohomology ring of $\operatorname{Gr}(V_{m}, k)$ is generated over $\mathrm{H}^{*}((\mathbf{P}^{m-1})^{n})$ by the Chern classes of the tautological and quotient bundles, subject to the Whitney sum relation. Taking the limit $m \to \infty$ yields the stated formula.

*Step 4: The projective space case.* For $k = 1$, the Grassmannian $\operatorname{Gr}(1, n) = \mathbf{P}^{n-1}$. The tautological bundle is a line bundle with $c_{1} = -\zeta$, so the Whitney sum relation becomes $c(V) = (1 - \zeta)(1 + c'_{1} + \cdots + c'_{n-1})$. Eliminating the $c'_{j}$ variables, one obtains a single relation:

$$
\prod_{i=1}^{n}(\zeta + t_{i}) = 0 \quad \text{in } \mathrm{H}^{*}_{G}(\mathbf{P}^{n-1}).

$$

More precisely,

$$
\mathrm{H}^{*}_{G}(\mathbf{P}^{n-1}) = \mathbf{Z}[t_{1}, \ldots, t_{n}][\zeta] / \prod_{i=1}^{n}(\zeta + t_{i}).

$$

**Key Insight:** The Borel construction converts the equivariant Grassmannian into an honest Grassmannian bundle over the classifying space, so equivariant cohomology reduces to the classical cohomology of Grassmannian bundles. The equivariant parameters $t_{i}$ encode the torus weights and appear via the Chern class of the representation $V$.

**Prerequisites:** Equivariant cohomology, Borel construction, Grassmannian bundles, Chern classes, Whitney sum formula, tautological and quotient bundles on Grassmannians

<!-- BENCHMARK_PROBLEM: Write down the equivariant cohomology ring $\mathrm{H}^{*}_{(\mathbf{C}^{\times})^3}(\mathbf{P}^{2})$ explicitly as a quotient of a polynomial ring $\mathbf{Z}[t_1, t_2, t_3][\zeta]$. What is the single defining relation? -->

### Remark: $\mathcal{O}(-1)$ or $\mathcal{O}(1)$? {#ecag-0238}

When performing the Borel construction for a torus action, one must carefully distinguish between $\mathcal{O}(-1)$ and $\mathcal{O}(1)$ on the approximating projective spaces.

The key criterion is: if the action on the fibers of a representation $E$ has the same weights as the standard action on the base $\mathbf{C}^{m} \setminus \{0\}$ (i.e., the $i$-th coordinate of $E$ scales by the same character as the $i$-th copy of $\mathbf{C}^{m} \setminus \{0\}$), then the resulting mixed quotient $E \times_{G} (\mathbf{C}^{m} \setminus \{0\})^{n}$ is the tautological bundle $\mathcal{O}(-1)$ (on $\mathbf{P}^{m-1}$ or on Grassmannians).

The justification is direct: the tautological bundle on $\mathbf{P}^{m-1}$ is the sub-line-bundle of the trivial bundle $\mathbf{C}^{m}$ whose fiber over a point $[\ell]$ is the line $\ell$ itself. This is exactly the bundle obtained by the Borel construction when the fiber and the base carry the same weight. Since the tautological line bundle has no nonzero global sections (a global section would be a linear form vanishing on every line through the origin), it must be $\mathcal{O}(-1)$, not $\mathcal{O}(1)$.

<!-- BENCHMARK_PROBLEM: In the Borel construction for $G = \mathbf{C}^{\times}$ acting on $E = \mathbf{C}$ with weight $1$, is the resulting line bundle on $\mathbf{P}^{m-1} = (\mathbf{C}^m \setminus \{0\})/G$ isomorphic to $\mathcal{O}(-1)$ or $\mathcal{O}(1)$? Justify your answer. -->

### Remark {#ecag-0239}

For a comprehensive introduction to equivariant cohomology in algebraic geometry, including the localization theorem and applications to enumerative geometry, see D. Anderson's introductory notes *Introduction to Equivariant Cohomology in Algebraic Geometry* (available at IMPAN). These notes cover the Borel construction, the approximation theorem, equivariant Chern classes, and the Atiyah-Bott localization formula, with detailed examples on flag varieties and Grassmannians. They provide the foundational material needed for the equivariant computations in this section.
