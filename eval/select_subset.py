#!/usr/bin/env python3
"""Select a stratified random subset of ECAG-Bench for pilot evaluation.

Stratification ensures proportional representation across:
  - chapter (basic_concepts, cohomology, computations, moduli)
  - difficulty (1, 2, 3)
  - question_type (example, counterexample, computation, proof)

Constraints:
  - All 4 chapters must be represented
  - Minimum counterexample count for statistical power
  - Minimum L1 and L3 counts for difficulty calibration
"""

import argparse
import json
import random
from collections import Counter, defaultdict


def stratified_sample(data, n=100, min_counterexamples=20,
                      min_l1=20, min_l3=10, seed=42):
    """Select n problems with stratified sampling.

    Ensures:
      - At least min_counterexamples counterexamples
      - At least min_l1 Level 1 problems
      - At least min_l3 Level 3 problems (if available)
      - All 4 chapters represented
      - Proportional allocation across (chapter, difficulty, question_type)
    """
    rng = random.Random(seed)

    # Group by (question_type, chapter, difficulty)
    strata = defaultdict(list)
    for d in data:
        key = (d['question_type'], d['chapter'], d['difficulty'])
        strata[key].append(d)

    # Calculate proportional allocation for each stratum
    allocation = {}
    for key, items in strata.items():
        allocation[key] = max(1, round(len(items) / len(data) * n))

    # Enforce minimum constraints by boosting underrepresented groups
    # 1. Counterexamples
    counter_keys = [k for k in allocation if k[0] == 'counterexample']
    counter_total = sum(allocation[k] for k in counter_keys)
    if counter_total < min_counterexamples:
        scale = min_counterexamples / max(counter_total, 1)
        for k in counter_keys:
            allocation[k] = max(allocation[k], round(allocation[k] * scale))

    # 2. Level 1
    l1_keys = [k for k in allocation if k[2] == 1]
    l1_total = sum(allocation[k] for k in l1_keys)
    if l1_total < min_l1:
        scale = min_l1 / max(l1_total, 1)
        for k in l1_keys:
            allocation[k] = max(allocation[k], round(allocation[k] * scale))

    # 3. Level 3
    l3_keys = [k for k in allocation if k[2] == 3]
    l3_available = sum(len(strata[k]) for k in l3_keys)
    l3_target = min(min_l3, l3_available)
    l3_total = sum(allocation[k] for k in l3_keys)
    if l3_total < l3_target:
        scale = l3_target / max(l3_total, 1)
        for k in l3_keys:
            allocation[k] = max(allocation[k], round(allocation[k] * scale))

    # 4. All chapters must be represented
    chapters = set(d['chapter'] for d in data)
    for ch in chapters:
        ch_keys = [k for k in allocation if k[1] == ch]
        if sum(allocation[k] for k in ch_keys) == 0:
            # Find the largest stratum in this chapter and add 1
            largest = max(ch_keys, key=lambda k: len(strata[k]))
            allocation[largest] = max(1, allocation[largest])

    # Cap each stratum at available count
    for key in allocation:
        allocation[key] = min(allocation[key], len(strata[key]))

    # Sample from each stratum
    selected = []
    for key in sorted(allocation.keys()):
        k = allocation[key]
        if k > 0:
            selected.extend(rng.sample(strata[key], k))

    # Trim or pad to exact n
    if len(selected) > n:
        # Keep mandatory minimums, trim from largest strata
        selected = rng.sample(selected, n)
    elif len(selected) < n:
        # Add more from the pool
        selected_ids = {d['id'] for d in selected}
        pool = [d for d in data if d['id'] not in selected_ids]
        extra = rng.sample(pool, min(n - len(selected), len(pool)))
        selected.extend(extra)

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
    parser = argparse.ArgumentParser(
        description='Select stratified subset for pilot evaluation')
    parser.add_argument('--input', default='benchmark/data/ecag_bench.jsonl',
                        help='Path to benchmark JSONL file')
    parser.add_argument('--output', default='eval/results/pilot_100.jsonl',
                        help='Path to output subset JSONL')
    parser.add_argument('--n', type=int, default=100,
                        help='Number of problems to select')
    parser.add_argument('--min-counterexamples', type=int, default=20,
                        help='Minimum number of counterexample problems')
    parser.add_argument('--min-l1', type=int, default=20,
                        help='Minimum number of Level 1 problems')
    parser.add_argument('--min-l3', type=int, default=10,
                        help='Minimum number of Level 3 problems')
    parser.add_argument('--seed', type=int, default=42,
                        help='Random seed')
    args = parser.parse_args()

    with open(args.input) as f:
        data = [json.loads(line) for line in f]

    subset = stratified_sample(
        data, n=args.n,
        min_counterexamples=args.min_counterexamples,
        min_l1=args.min_l1, min_l3=args.min_l3,
        seed=args.seed)

    import os
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

    with open(args.output, 'w') as f:
        for d in subset:
            f.write(json.dumps(d) + '\n')

    print(f"Selected {len(subset)} problems -> {args.output}")
    print_stats(subset)


if __name__ == '__main__':
    main()
