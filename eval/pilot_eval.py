#!/usr/bin/env python3
"""Run pilot evaluation of ECAG-Bench using the Anthropic API.

This script evaluates a subset of ECAG-Bench problems using Claude,
saving responses and metadata for human scoring.

Usage:
    python eval/pilot_eval.py --input eval/results/pilot_subset.jsonl \
                              --output eval/results/pilot_claude.jsonl \
                              --model claude-opus-4-20250514

Requires: ANTHROPIC_API_KEY environment variable.
"""

import argparse
import json
import os
import time
from pathlib import Path


def load_prompt_template(path='eval/prompt_template.txt'):
    """Load the evaluation prompt template."""
    with open(path) as f:
        return f.read()


def evaluate_problem(client, model, prompt_template, problem_entry):
    """Evaluate a single problem and return the response."""
    prompt = prompt_template.replace('{problem}', problem_entry['problem'])

    try:
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )
        return {
            'id': problem_entry['id'],
            'model': model,
            'problem': problem_entry['problem'],
            'question_type': problem_entry['question_type'],
            'difficulty': problem_entry['difficulty'],
            'chapter': problem_entry['chapter'],
            'response': response.content[0].text,
            'input_tokens': response.usage.input_tokens,
            'output_tokens': response.usage.output_tokens,
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            # Human scoring fields (to be filled manually)
            'score': None,  # 0.0, 0.5, or 1.0
            'failure_mode': None,  # F1-F6 or null
            'notes': None,
        }
    except Exception as e:
        return {
            'id': problem_entry['id'],
            'model': model,
            'error': str(e),
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'score': None,
            'failure_mode': None,
            'notes': None,
        }


def main():
    parser = argparse.ArgumentParser(description='Run pilot evaluation on ECAG-Bench')
    parser.add_argument('--input', required=True, help='Path to pilot subset JSONL')
    parser.add_argument('--output', required=True, help='Path to output results JSONL')
    parser.add_argument('--model', default='claude-opus-4-20250514',
                        help='Model ID to evaluate')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from existing output file')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay between API calls (seconds)')
    args = parser.parse_args()

    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package required. Install with: pip install anthropic")
        return

    client = anthropic.Anthropic()
    prompt_template = load_prompt_template()

    # Load problems
    with open(args.input) as f:
        problems = [json.loads(line) for line in f]

    # Load existing results if resuming
    done_ids = set()
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            for line in f:
                result = json.loads(line)
                done_ids.add(result['id'])
        print(f"Resuming: {len(done_ids)} already completed")

    # Evaluate
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    mode = 'a' if args.resume else 'w'
    with open(args.output, mode) as f:
        for i, problem in enumerate(problems):
            if problem['id'] in done_ids:
                continue

            print(f"[{i+1}/{len(problems)}] Evaluating {problem['id']} "
                  f"({problem['question_type']}, L{problem['difficulty']})...")

            result = evaluate_problem(client, args.model, prompt_template, problem)
            f.write(json.dumps(result) + '\n')
            f.flush()

            if 'error' in result:
                print(f"  ERROR: {result['error']}")
            else:
                print(f"  OK ({result['output_tokens']} tokens)")

            time.sleep(args.delay)

    print(f"\nDone. Results saved to {args.output}")
    print(f"Next step: manually score each response (score: 0/0.5/1, failure_mode: F1-F6)")


if __name__ == '__main__':
    main()
