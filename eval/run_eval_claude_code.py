#!/usr/bin/env python3
"""Evaluate ECAG-Bench problems using Claude Code CLI (claude -p).

Uses subprocess to call `claude -p` for each problem, collecting responses
into a JSONL file. Supports resume from partial runs.

Usage:
    python eval/run_eval_claude_code.py \
        --input eval/results/pilot_100.jsonl \
        --output eval/results/pilot_100_responses.jsonl \
        --concurrency 3
"""

import argparse
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path


def load_prompt_template(path='eval/prompt_template.txt'):
    """Load the evaluation prompt template."""
    with open(path) as f:
        return f.read()


def evaluate_single(entry, prompt_template, model_flag=None):
    """Evaluate a single problem using claude -p.

    Returns the entry dict augmented with model_response and metadata.
    """
    problem_text = entry['problem']
    prompt = prompt_template.replace('{problem}', problem_text)

    cmd = ['claude', '-p', '--output-format', 'json']
    if model_flag:
        cmd.extend(['--model', model_flag])

    # Remove CLAUDECODE env var to allow nested invocation
    env = os.environ.copy()
    env.pop('CLAUDECODE', None)

    start = time.time()
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=600,  # 10 minute timeout per problem
            env=env,
        )
        elapsed = time.time() - start

        if result.returncode != 0:
            return {
                **entry,
                'model_response': None,
                'error': result.stderr.strip(),
                'elapsed_seconds': elapsed,
                'timestamp': datetime.now().isoformat(),
            }

        # Parse JSON output from claude
        try:
            output = json.loads(result.stdout)
            response_text = output.get('result', result.stdout)
        except json.JSONDecodeError:
            response_text = result.stdout.strip()

        return {
            **entry,
            'model_response': response_text,
            'error': None,
            'elapsed_seconds': elapsed,
            'timestamp': datetime.now().isoformat(),
        }

    except subprocess.TimeoutExpired:
        return {
            **entry,
            'model_response': None,
            'error': 'timeout_600s',
            'elapsed_seconds': 600,
            'timestamp': datetime.now().isoformat(),
        }
    except Exception as e:
        return {
            **entry,
            'model_response': None,
            'error': str(e),
            'elapsed_seconds': time.time() - start,
            'timestamp': datetime.now().isoformat(),
        }


def main():
    parser = argparse.ArgumentParser(
        description='Evaluate ECAG-Bench using Claude Code CLI')
    parser.add_argument('--input', default='eval/results/pilot_100.jsonl',
                        help='Input JSONL with problems')
    parser.add_argument('--output', default='eval/results/pilot_100_responses.jsonl',
                        help='Output JSONL with responses')
    parser.add_argument('--prompt-template', default='eval/prompt_template.txt',
                        help='Path to prompt template')
    parser.add_argument('--concurrency', type=int, default=3,
                        help='Number of concurrent evaluations')
    parser.add_argument('--model', default=None,
                        help='Model flag to pass to claude -p')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from partial output file')
    args = parser.parse_args()

    # Load problems
    with open(args.input) as f:
        problems = [json.loads(line) for line in f]

    prompt_template = load_prompt_template(args.prompt_template)

    # Check for resume
    completed_ids = set()
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    completed_ids.add(entry['id'])
                except (json.JSONDecodeError, KeyError):
                    continue
        print(f"Resuming: {len(completed_ids)} already completed")

    remaining = [p for p in problems if p['id'] not in completed_ids]
    print(f"Problems to evaluate: {len(remaining)} / {len(problems)}")

    if not remaining:
        print("All problems already evaluated!")
        return

    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

    # Open output file in append mode
    mode = 'a' if args.resume and completed_ids else 'w'
    completed = len(completed_ids)
    total = len(problems)
    errors = 0

    with open(args.output, mode) as out_f:
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            futures = {
                executor.submit(
                    evaluate_single, entry, prompt_template, args.model
                ): entry
                for entry in remaining
            }

            for future in as_completed(futures):
                entry = futures[future]
                try:
                    result = future.result()
                    out_f.write(json.dumps(result) + '\n')
                    out_f.flush()
                    completed += 1

                    status = 'OK' if result.get('error') is None else f"ERR: {result['error'][:50]}"
                    if result.get('error'):
                        errors += 1
                    elapsed = result.get('elapsed_seconds', 0)
                    print(f"[{completed}/{total}] {entry['id']} - {status} ({elapsed:.1f}s)")

                except Exception as e:
                    errors += 1
                    completed += 1
                    print(f"[{completed}/{total}] {entry['id']} - EXCEPTION: {e}")

    print(f"\nDone! {completed} evaluated, {errors} errors")
    print(f"Output: {args.output}")


if __name__ == '__main__':
    main()
