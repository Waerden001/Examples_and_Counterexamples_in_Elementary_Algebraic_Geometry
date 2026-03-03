# Contributing to ECAG

Thank you for your interest in contributing! This project thrives on community input — whether you're fixing errors, filling stubs, or adding entirely new examples.

## Ways to Contribute

### 1. Fix errors in existing examples

If you find a mathematical error:

1. Open an issue using the **Error Report** template
2. Or submit a PR directly editing the relevant file in `content/`

### 2. Fill in stubs

Many examples have titles but no content (marked **Stub** in the website). These are open for contribution. Search for `> **Status:** Stub` in `content/` files to find them.

### 3. Add new examples or counterexamples

Create a new entry in the appropriate `content/` file following the format below.

### 4. Improve the benchmark

Add `tags`, `prerequisites`, `msc_codes`, or improve `problem` formulations in `benchmark/data/ecag_bench.jsonl`.

## Content Format

Each example in `content/` follows this structure:

```markdown
### Example: Your descriptive title here {#ecag-XXXX}

Your mathematical content here. Use standard LaTeX in math mode:

$$\operatorname{Pic}(X) \cong \mathbb{Z}$$

Inline math: $X$ is a smooth projective curve of genus $g$.
```

**Rules:**

- **Use standard LaTeX only** — write `\operatorname{Spec}` not `\Spec`, write `\mathcal{O}` not `\O`, write `\mathbf{P}` not `\P`. Custom macros from `mystyle.sty` are only for the LaTeX source in `latex/`.
- **ECAG ID** — for new entries, use a placeholder `{#ecag-NEW}` and the maintainer will assign the real ID.
- **Stub entries** — if you can only provide a title and rough statement, that's still valuable. Mark the body with `> **Status:** Stub — content needed.`
- **References** — link to Stacks Project tags, Hartshorne exercises, or other sources where applicable.
- **Diagrams** — commutative diagrams using `tikzcd` should be wrapped in a fenced code block with a comment: `<!-- tikzcd diagram: manual conversion needed -->`.

## Benchmark Entries

If you edit `benchmark/data/ecag_bench.jsonl`, ensure:

1. All math uses standard LaTeX (no custom macros)
2. `id` follows the `ecag-XXXX` pattern
3. Run validation before committing:
   ```bash
   python scripts/validate_benchmark.py benchmark/data/ecag_bench.jsonl benchmark/schema.json
   ```

## LaTeX Source

The original LaTeX is in `latex/`. If you edit LaTeX files:

- Use existing macros from `mystyle.sty`
- Follow the `\documentclass[../main.tex]{subfiles}` pattern
- Verify compilation: `cd latex && pdflatex main.tex`

## Pull Request Checklist

- [ ] Content in `content/` uses standard LaTeX (no custom macros)
- [ ] If benchmark edited, `validate_benchmark.py` passes
- [ ] If LaTeX edited, `pdflatex main.tex` compiles
- [ ] ECAG ID is assigned or placeholder `{#ecag-NEW}` is used

## Code of Conduct

Be respectful and constructive. Mathematical disagreements should be resolved with references and proofs, not arguments.

## License

By contributing, you agree that your contributions will be licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
