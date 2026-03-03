#!/usr/bin/env python3
"""Select a stratified random subset of ECAG-Bench for pilot evaluation.

Stratification ensures proportional representation across:
  - chapter (basic_concepts, cohomology, computations, moduli)
  - difficulty (1, 2, 3)
  - question_type (example, counterexample, computation, proof)

With a minimum of 12 counterexample problems to ensure statistical power
for the example-vs-counterexample comparison.
"""

import argparse
import json
import random
from collections import Counter, defaultdict


def stratified_sample(data, n=50, min_counterexamples=12, seed=42):
    """Select n problems with stratified sampling, ensuring min counterexamples."""
    rng = random.Random(seed)

    # Separate counterexamples and others
    counterexamples = [d for d in data if d['question_type'] == 'counterexample']
    others = [d for d in data if d['question_type'] != 'counterexample']

    # Sample counterexamples first
    n_counter = min(min_counterexamples, len(counterexamples))
    selected_counter = rng.sample(counterexamples, n_counter)

    # For remaining slots, stratify by (chapter, difficulty)
    n_remaining = n - n_counter
    strata = defaultdict(list)
    for d in others:
        key = (d['chapter'], d['difficulty'])
        strata[key].append(d)

    # Calculate proportional allocation
    total_others = len(others)
    selected_others = []
    for key, items in sorted(strata.items()):
        k = max(1, round(len(items) / total_others * n_remaining))
        k = min(k, len(items))
        selected_others.extend(rng.sample(items, k))

    # Trim or pad to exact count
    if len(selected_others) > n_remaining:
        selected_others = rng.sample(selected_others, n_remaining)
    elif len(selected_others) < n_remaining:
        pool = [d for d in others if d not in selected_others]
        extra = rng.sample(pool, min(n_remaining - len(selected_others), len(pool)))
        selected_others.extend(extra)

    selected = selected_counter + selected_others
    # Sort by ID for reproducibility
    selected.sort(key=lambda d: d['id'])
    return selected


def print_stats(subset):
    """Print distribution statistics for the selected subset."""
    print(f"Total selected: {len(subset)}")
    print(f"\nBy chapter:")
    for k, v in sorted(Counter(d['chapter'] for d in subset).items()):
        print(f"  {k}: {v}")
    print(f"\nBy difficulty:")
    for k, v in sorted(Counter(d['difficulty'] for d in subset).items()):
        print(f"  Level {k}: {v}")
    print(f"\nBy question_type:")
    for k, v in sorted(Counter(d['question_type'] for d in subset).items()):
        print(f"  {k}: {v}")
    print(f"\nBy verification_strategy:")
    for k, v in sorted(Counter(d['verification_strategy'] for d in subset).items()):
        print(f"  {k}: {v}")


def main():
    parser = argparse.ArgumentParser(description='Select stratified subset for pilot evaluation')
    parser.add_argument('--input', default='benchmark/data/ecag_bench.jsonl',
                        help='Path to benchmark JSONL file')
    parser.add_argument('--output', default='eval/results/pilot_subset.jsonl',
                        help='Path to output subset JSONL')
    parser.add_argument('--n', type=int, default=50, help='Number of problems to select')
    parser.add_argument('--min-counterexamples', type=int, default=12,
                        help='Minimum number of counterexample problems')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()

    with open(args.input) as f:
        data = [json.loads(line) for line in f]

    subset = stratified_sample(data, n=args.n,
                                min_counterexamples=args.min_counterexamples,
                                seed=args.seed)

    import os
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    with open(args.output, 'w') as f:
        for d in subset:
            f.write(json.dumps(d) + '\n')

    print(f"Selected {len(subset)} problems -> {args.output}")
    print_stats(subset)


if __name__ == '__main__':
    main()
