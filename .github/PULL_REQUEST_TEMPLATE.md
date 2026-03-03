## Changes

<!-- Brief description of what this PR does -->

## Checklist

- [ ] Content in `content/` uses **standard LaTeX** (no custom macros like `\Spec`, `\O`, etc.)
- [ ] ECAG IDs are correct or placeholder `{#ecag-NEW}` is used for new entries
- [ ] If benchmark data edited: `python scripts/validate_benchmark.py benchmark/data/ecag_bench.jsonl benchmark/schema.json` passes
- [ ] If LaTeX source edited: `cd latex && pdflatex main.tex` compiles successfully
- [ ] Difficulty rating included for new examples

## Type

- [ ] Error fix
- [ ] New example / counterexample
- [ ] Stub filled in
- [ ] Benchmark improvement
- [ ] Other: ___
