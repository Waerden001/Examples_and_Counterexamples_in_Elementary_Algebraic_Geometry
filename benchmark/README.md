---
language:
  - en
license: cc-by-4.0
task_categories:
  - question-answering
  - text-generation
tags:
  - mathematics
  - algebraic-geometry
  - benchmark
  - examples
  - counterexamples
  - construction
pretty_name: "ECAG-Bench"
size_categories:
  - n<1K
---

# ECAG-Bench: Examples and Counterexamples in Algebraic Geometry Benchmark

## Overview

**ECAG-Bench** evaluates whether large language models can construct concrete mathematical objects in algebraic geometry that satisfy given properties. Unlike theorem-proving benchmarks, ECAG-Bench tests *constructive* mathematical reasoning: given a set of constraints, can the model produce a specific example, counterexample, or compute an invariant?

This is a fundamentally different capability from proof verification — answers are typically **not unique**, and evaluation relies on **property verification** rather than answer matching.

## Dataset Description

- **Source:** Curated from *Examples and Counterexamples in Elementary Algebraic Geometry* by Waerden
- **Repository:** [GitHub](https://github.com/Waerden001/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry)
- **Website:** [GitHub Pages](https://waerden001.github.io/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/)
- **License:** CC-BY-4.0
- **Format:** JSONL (one JSON object per line)

## Statistics

| Metric | Count |
|--------|-------|
| Total entries | 332 |
| Substantive (with solution) | 332 |
| Stubs (title only) | 0 |

### By Chapter

| Chapter | Count |
|---------|-------|
| Basic Concepts | 162 |
| Computations | 66 |
| Moduli & Deformation | 58 |
| Cohomology | 46 |

### By Difficulty

| Level | Description | Count |
|-------|-------------|-------|
| 1 | Routine: directly from definitions | 77 |
| 2 | Requires applying a non-trivial theorem | 237 |
| 3 | Deep: combining multiple results or unexpected | 18 |

### By Question Type

| Type | Count |
|------|-------|
| Example | 243 |
| Counterexample | 66 |
| Computation | 14 |
| Proof | 9 |

### By Verification Strategy

| Strategy | Count | Description |
|----------|-------|-------------|
| CAS (SageMath/Macaulay2) | 309 | Automated property verification |
| Exact match | 14 | Unique numeric/symbolic answer |
| Rubric | 9 | Human/LLM-judge with structured rubric |

## Schema

Each entry contains:

```json
{
  "id": "ecag-0042",
  "problem": "Give an example of a smooth complete nonprojective surface.",
  "solution": "Consider the twisted family of P^1...",
  "answer": null,
  "answer_type": "example",
  "difficulty": 3,
  "chapter": "computations",
  "topic": "invariants",
  "subtopic": "picard_group",
  "question_type": "example",
  "tags": ["projective", "complete", "surface"],
  "source": "Hartshorne II.7.13",
  "prerequisites": ["Picard group", "cuspidal curves"],
  "msc_codes": ["14A15"],
  "verification_strategy": "cas",
  "verification_script": null,
  "accepts_multiple": true,
  "is_stub": false,
  "latex_source": "latex/Computations/picard.tex"
}
```

## Evaluation Methodology

Since constructions in algebraic geometry are non-unique, ECAG-Bench uses a **four-layer verification pipeline**:

1. **Parsing** (Regex/SymPy): Is the output a well-formed mathematical expression?
2. **CAS Verification** (SageMath/Singular/Macaulay2): Does the constructed object satisfy the required properties? (genus, smoothness, dimension, etc.)
3. **LLM-Assisted Judgment** (with rubric): Is the reasoning valid? Is the answer non-trivial?
4. **Human Expert Sampling**: Gold-standard calibration on a random subset.

**Layer 2 is the core innovation**: we verify *properties* of mathematical objects, not answer equivalence.

### Verification Strategies

- **Strategy A (Exact):** Constrained problems with unique numeric answers — verified by exact match.
- **Strategy B (CAS):** LLM outputs a mathematical object; SageMath verifies its properties deterministically.
- **Strategy C (Rubric):** Structured scoring on correctness (C1), completeness (C2), non-triviality (C3), and reasoning validity (C4).

## Usage

```python
import json

with open("benchmark/data/ecag_bench.jsonl") as f:
    entries = [json.loads(line) for line in f]

# Filter by difficulty
hard = [e for e in entries if e["difficulty"] == 3]

# Filter substantive (non-stub) entries
substantive = [e for e in entries if not e["is_stub"]]
```

### Validation

```bash
python scripts/validate_benchmark.py benchmark/data/ecag_bench.jsonl benchmark/schema.json
```

## Topics Covered

- **Schemes & morphisms:** affineness, flatness, smoothness, etale maps, base change, dimension
- **Sheaves & bundles:** coherent sheaves, locally free sheaves, normal bundles, pushforward/pullback
- **Curves:** genus, inflection points, automorphisms, Hasse principle, hyperelliptic curves
- **Cohomology:** local duality, Borel-Moore, derived categories, Fourier-Mukai, perverse sheaves
- **Computations:** Picard/class groups, intersection theory, Hodge theory, weight filtrations, Morse theory
- **Moduli & deformation:** stability, moduli stacks, Pic(M_{1,1}), deformation of sheaves, Hilbert schemes

## Citation

```bibtex
@misc{wang2026ecagbench,
  title={ECAG-Bench: A Benchmark for Constructive Algebraic Geometry Reasoning in Large Language Models},
  author={Waerden},
  year={2026},
  url={https://github.com/Waerden001/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry},
  note={Examples and Counterexamples in Elementary Algebraic Geometry}
}
```

## Related Work

- [FrontierMath](https://epoch.ai/benchmarks/frontiermath) (Epoch AI, 2024) — Research-level math with custom verification scripts
- [AMBER](https://arxiv.org/abs/2602.01291) (2025) — Construction-verification benchmark in Lean 4
- [PutnamBench](https://arxiv.org/abs/2407.11214) (2024) — Putnam problems formalized in Lean/Isabelle/Coq
- [GHOSTS](https://arxiv.org/abs/2301.13867) (NeurIPS 2023) — Graduate-level math evaluation with rubrics
- [MathArena](https://matharena.ai/) (ETH, 2025) — Competition math with dual grading
