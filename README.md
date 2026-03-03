# Examples and Counterexamples in Elementary Algebraic Geometry

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A curated collection of **concrete examples, counterexamples, constructions, and computations** in elementary algebraic geometry. Originally written as supplementary material for learners entering algebraic geometry, now being expanded into a multi-purpose open-source project.

## What's Here

- **`latex/`** — Original LaTeX source, compilable to PDF
- **`content/`** — Markdown version for web browsing (WIP)
- **`benchmark/`** — [ECAG-Bench](https://huggingface.co/datasets/Waerden001/ecag-bench): an LLM benchmark for testing the ability to construct algebraic geometry examples and counterexamples (WIP)
- **`scripts/`** — Tooling for LaTeX-to-Markdown conversion and benchmark generation

## Topics Covered

- **Schemes & morphisms**: affineness, flatness, smoothness, etale maps, base change
- **Sheaves & bundles**: coherent sheaves, locally free sheaves, normal bundles
- **Curves**: genus, inflection points, automorphisms, Hasse principle
- **Cohomology**: local duality, Borel-Moore homology, derived categories, Fourier-Mukai
- **Computations**: Picard/class groups, intersection theory, Hodge theory, weight filtrations
- **Moduli & deformation**: stability, moduli stacks, Pic(M_{1,1}), deformation of sheaves

## Build the PDF

Requires TeX Live 2024 (or later) with `pdflatex`:

```bash
cd latex
pdflatex main.tex && pdflatex main.tex
```

Output: `latex/examples-and-counterexamples.pdf`

## Contributing

We welcome contributions! You can:

- **Fix errors** in existing examples
- **Fill in stubs** (examples with titles but no content)
- **Add new examples and counterexamples**
- **Improve the benchmark** with better problem formulations

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ECAG-Bench

**ECAG-Bench** (Examples & Counterexamples in Algebraic Geometry Benchmark) is an LLM evaluation dataset derived from this collection. It tests whether language models can construct concrete mathematical objects satisfying given properties — a capability distinct from theorem proving.

<!-- Dataset link: https://huggingface.co/datasets/Waerden001/ecag-bench -->

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the material with appropriate attribution.

## Author

**Waerden** — originally written during PhD studies; now maintained as an open community resource.
