# Contributing to ECAG

Thank you for your interest in contributing! This project thrives on community input — whether you're fixing errors, improving existing content, or adding new examples.

## Quality Standards

Every example in this collection should be a **self-contained mathematical narrative** — not a template or checklist, but a natural exposition that a reader can follow from statement to conclusion. Specifically:

1. **Natural mathematical prose.** Write as you would in a good textbook or survey article. Avoid bullet-point-heavy formats; instead, let the argument flow logically from one step to the next.
2. **Complete constructions.** If the example involves constructing an object, include all the computational details needed for a reader to verify the construction independently. Don't just state the answer — show *why* it works.
3. **Logical completeness.** Every claim should be justified, either by a direct argument or by a precise reference. If a result is "well-known," cite where it can be found.
4. **Key insight.** Each example should make clear *what* the reader should take away — the surprising phenomenon, the instructive failure, or the essential technique.

### Reference Example

See [`content/computations/characteristics.md`](content/computations/characteristics.md), entry **ecag-0230** (Chern classes of the Horrocks–Mumford bundle) for a model of the quality and depth we aim for.

## Content Format

Each example in `content/` follows this structure:

```markdown
### Example: Your descriptive title here {#ecag-XXXX}

A natural mathematical exposition of the example, flowing from the problem
statement through the construction or proof to the key insight.

The construction proceeds as follows. Let $X$ be a smooth projective variety...

$$
\operatorname{Pic}(X) \cong \mathbb{Z}
$$

This result is surprising because...

<!-- BENCHMARK_PROBLEM: {"problem": "Compute Pic(X) for ...", "answer": "Z", "answer_type": "closed_form", "difficulty": 2, "tags": ["picard-group"], "verification_strategy": "cas"} -->
```

## Formatting Rules

### BENCHMARK_PROBLEM

Each example must end with a `<!-- BENCHMARK_PROBLEM: {...} -->` HTML comment containing a JSON object. This is extracted automatically by `scripts/build_benchmark.py` to generate the benchmark dataset.

### Display Math

Display math (`$$`) must follow these rules:

- `$$` must appear on its own line (no inline text on the same line)
- There must be a blank line before the opening `$$` and after the closing `$$`
- No blank lines inside the `$$...$$` block (MathJax interprets blank lines as paragraph breaks)

**Correct:**

```markdown
The Picard group is computed as follows.

$$
\operatorname{Pic}(X) \cong \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}
$$

This shows that...
```

**Incorrect:**

```markdown
The Picard group is $$\operatorname{Pic}(X) \cong \mathbb{Z}$$
```

### LaTeX Conventions

- **Use standard LaTeX** — write `\operatorname{Spec}` not `\Spec`, write `\mathcal{O}` not `\O`, write `\mathbf{P}` not `\P`. Custom macros from `mystyle.sty` are only for the LaTeX source in `latex/`.
- **Aligned environments:** Inside MathJax, use `\begin{aligned}...\end{aligned}` (not `\begin{align}` or `\begin{align*}`).
- **Operator names:** Always use `\operatorname{Name}` for operator-style names (Spec, Proj, Pic, Hom, Ext, etc.).

### ECAG IDs

- For new entries, use a placeholder `{#ecag-NEW}` and the maintainer will assign the real ID.
- Existing IDs must not be changed or reused.

## Ways to Contribute

### 1. Improve existing examples

If an example's exposition could be clearer, more complete, or better motivated, submit a PR. This is the most valuable form of contribution.

### 2. Fix mathematical errors

If you find an error, open an issue using the **Error Report** template, or submit a PR directly.

### 3. Add new examples or counterexamples

Create a new entry in the appropriate `content/` file following the format above. Include the `BENCHMARK_PROBLEM` comment.

### 4. Improve the benchmark

Refine `problem` formulations, add better `tags`, `prerequisites`, or `msc_codes`.

## LaTeX Source

The original LaTeX is in `latex/`. If you edit LaTeX files:

- Use existing macros from `mystyle.sty`
- Follow the `\documentclass[../main.tex]{subfiles}` pattern
- Verify compilation: `cd latex && pdflatex main.tex`

## Pull Request Checklist

- [ ] Content in `content/` uses standard LaTeX (no custom macros)
- [ ] Display math follows the `$$`-on-its-own-line rule with blank lines before/after
- [ ] Each example includes a `<!-- BENCHMARK_PROBLEM: ... -->` comment
- [ ] `python scripts/validate_benchmark.py benchmark/data/ecag_bench.jsonl benchmark/schema.json` passes
- [ ] If LaTeX edited, `pdflatex main.tex` compiles
- [ ] ECAG ID is assigned or placeholder `{#ecag-NEW}` is used

## Code of Conduct

Be respectful and constructive. Mathematical disagreements should be resolved with references and proofs, not arguments.

## License

By contributing, you agree that your contributions will be licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
