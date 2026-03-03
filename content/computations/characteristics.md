---
chapter: computations
source: /home/waerden/GitHub/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/latex/Computations/characteristics.tex
---

## Characteristic classes and numbers

### Example: Horrocks–Mumford bundle {#ecag-0230}

The Horrocks–Mumford bundle $\mathscr{F}$ is a rank-2 vector bundle on $\mathbb{P}^4$ with Chern classes $c_1(\mathscr{F}) = 5h$ and $c_2(\mathscr{F}) = 10h^2$, where $h$ is the hyperplane class. It is the unique (up to twist and automorphisms) indecomposable rank-2 bundle on $\mathbb{P}^n$ for $n \geq 3$.

We compute $\chi(\mathscr{F}(n-5))$ via the Hirzebruch–Riemann–Roch theorem:
$$
\chi(\mathscr{F}(n-5)) = \int_{\mathbb{P}^4} \operatorname{ch}(\mathscr{F}(n-5)) \cdot \operatorname{td}(\mathbb{P}^4).
$$

**Chern character of $\mathscr{F}(t)$ with $t = n-5$.** The twisted bundle has $c_1(\mathscr{F}(t)) = (2t + 5)h$ and $c_2(\mathscr{F}(t)) = (t^2 + 5t + 10)h^2$. For a rank-2 bundle, the Chern character components are determined by Newton's identities:

- $\operatorname{ch}_0 = 2$
- $\operatorname{ch}_1 = c_1 = (2t+5)h$
- $\operatorname{ch}_2 = \frac{c_1^2 - 2c_2}{2} = \frac{(2t+5)^2 - 2(t^2+5t+10)}{2} = \frac{2t^2+10t+5}{2}\; h^2$
- $\operatorname{ch}_3 = \frac{c_1^3 - 3c_1 c_2}{6}$. We have $(2t+5)^3 = 8t^3+60t^2+150t+125$ and $3(2t+5)(t^2+5t+10) = 6t^3+45t^2+135t+150$, so $\operatorname{ch}_3 = \frac{2t^3+15t^2+15t-25}{6}\; h^3$.
- $\operatorname{ch}_4 = \frac{c_1^4 - 4c_1^2 c_2 + 2c_2^2}{24}$. Computing the three terms:
  - $(2t+5)^4 = 16t^4+160t^3+600t^2+1000t+625$
  - $4(2t+5)^2(t^2+5t+10) = 16t^4+160t^3+660t^2+1300t+1000$
  - $2(t^2+5t+10)^2 = 2t^4+20t^3+90t^2+200t+200$

  So $\operatorname{ch}_4 = \frac{2t^4+20t^3+30t^2-100t-175}{24}\; h^4$.

**Todd class of $\mathbb{P}^4$.** The tangent bundle $T_{\mathbb{P}^4}$ has $c_i = \binom{5}{i} h^i$ from the Euler sequence $0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus 5} \to T_{\mathbb{P}^4} \to 0$. The Todd class components are:

- $\operatorname{td}_0 = 1$
- $\operatorname{td}_1 = \frac{c_1}{2} = \frac{5}{2}$
- $\operatorname{td}_2 = \frac{c_1^2 + c_2}{12} = \frac{25+10}{12} = \frac{35}{12}$
- $\operatorname{td}_3 = \frac{c_1 c_2}{24} = \frac{50}{24} = \frac{25}{12}$
- $\operatorname{td}_4 = \frac{-c_1^4 + 4c_1^2 c_2 + 3c_2^2 + c_1 c_3 - c_4}{720} = \frac{720}{720} = 1$

**The Euler characteristic.** We extract the degree-4 component $\chi = \sum_{i+j=4} \operatorname{ch}_i \cdot \operatorname{td}_j$. Writing each term over the common denominator 24:

| Term | Expression | Over 24 |
|------|-----------|---------|
| $\operatorname{ch}_0 \cdot \operatorname{td}_4$ | $2 \cdot 1$ | $48$ |
| $\operatorname{ch}_1 \cdot \operatorname{td}_3$ | $(2t+5) \cdot \frac{25}{12}$ | $100t + 250$ |
| $\operatorname{ch}_2 \cdot \operatorname{td}_2$ | $\frac{2t^2+10t+5}{2} \cdot \frac{35}{12}$ | $70t^2 + 350t + 175$ |
| $\operatorname{ch}_3 \cdot \operatorname{td}_1$ | $\frac{2t^3+15t^2+15t-25}{6} \cdot \frac{5}{2}$ | $20t^3 + 150t^2 + 150t - 250$ |
| $\operatorname{ch}_4 \cdot \operatorname{td}_0$ | $\frac{2t^4+20t^3+30t^2-100t-175}{24}$ | $2t^4 + 20t^3 + 30t^2 - 100t - 175$ |

Collecting by degree: $2t^4 + 40t^3 + 250t^2 + 500t + 48$. So
$$
\chi(\mathscr{F}(t)) = \frac{2t^4 + 40t^3 + 250t^2 + 500t + 48}{24} = \frac{t^4+20t^3+125t^2+250t+24}{12}.
$$

**Substituting $t = n - 5$.** We expand and collect:

| Power | $(n-5)^4$ | $20(n-5)^3$ | $125(n-5)^2$ | $250(n-5)$ | $+24$ | Total |
|-------|-----------|-------------|--------------|------------|-------|-------|
| $n^4$ | $1$ | | | | | $1$ |
| $n^3$ | $-20$ | $20$ | | | | $0$ |
| $n^2$ | $150$ | $-300$ | $125$ | | | $-25$ |
| $n^1$ | $-500$ | $1500$ | $-1250$ | $250$ | | $0$ |
| $n^0$ | $625$ | $-2500$ | $3125$ | $-1250$ | $24$ | $24$ |

The vanishing of the $n^3$ and $n^1$ coefficients reflects Serre duality: since $\omega_{\mathbb{P}^4} = \mathcal{O}(-5)$ and $c_1(\mathscr{F}) = 5$, we have $\mathscr{F}^{\vee} \cong \mathscr{F}(-5)$, so $\chi(\mathscr{F}(t)) = \chi(\mathscr{F}(-t-5))$ by Serre duality, which forces the polynomial in $n = t+5$ to be even. Hence
$$
\chi(\mathscr{F}(n-5)) = \frac{n^4 - 25n^2 + 24}{12} = \frac{(n^2-1)(n^2-24)}{12} = \frac{(n-1)(n+1)(n^2-24)}{12}.
$$

**Verification.**

- $n = 5$ (i.e., $\mathscr{F}$ itself): $\chi = \frac{24 \cdot 1}{12} = 2$. This matches the known cohomology $h^0(\mathscr{F}) = 4$, $h^1(\mathscr{F}) = 2$, $h^i(\mathscr{F}) = 0$ for $i \geq 2$, giving $\chi = 4 - 2 = 2$. ✓
- $n = 0$ (i.e., $\mathscr{F}(-5) \cong \mathscr{F}^{\vee}$): $\chi = \frac{24}{12} = 2 = \chi(\mathscr{F})$ by Serre duality. ✓
- $n = \pm 1$: $\chi = 0$. Indeed, $\mathscr{F}(-4)$ and $\mathscr{F}(-6)$ have all cohomology groups vanishing, which can be verified from the monad description $0 \to \mathcal{O}(-1)^5 \to \Omega^2(2)^2 \to \mathcal{O}(1)^5 \to 0$.

<!-- BENCHMARK_PROBLEM: Let $\mathscr{F}$ be the Horrocks–Mumford bundle on $\mathbb{P}^4$ with $c_1(\mathscr{F}) = 5h$ and $c_2(\mathscr{F}) = 10h^2$. Using the Hirzebruch–Riemann–Roch theorem, compute $\chi(\mathscr{F}(n-5))$ as a closed-form rational function of $n$, and verify your answer at $n = 5$ using the known cohomology $h^0(\mathscr{F}) = 4$, $h^1(\mathscr{F}) = 2$, $h^i(\mathscr{F}) = 0$ for $i \geq 2$. -->
