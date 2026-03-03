#!/usr/bin/env python3
"""Score ECAG-Bench model responses using Claude Code CLI (claude -p).

Two-stage scoring:
  1. Automatic scoring via Claude (claude -p) for initial assessment
  2. Human review for edge cases (score=0.5, counterexamples, L3)

Usage:
    python eval/score_responses.py \
        --input eval/results/pilot_100_responses.jsonl \
        --output eval/results/pilot_100_scored.jsonl \
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


SCORING_PROMPT = """You are an expert algebraic geometer grading a student's response to a constructive mathematics problem.

## PROBLEM
{problem}

## KNOWN SOLUTION
{solution}

## MODEL RESPONSE
{response}

## GRADING CRITERIA

Score the response on a scale of 0, 0.5, or 1:

- **1.0 (Correct)**: The response provides a valid, concrete mathematical object that satisfies all required properties. The verification is rigorous and the object is non-trivial.
- **0.5 (Partial)**: The response provides a valid mathematical object but either:
  - Fails to verify all required properties
  - Provides an incomplete verification
  - Uses a trivially degenerate example when a non-trivial one is expected
- **0.0 (Incorrect)**: The response either:
  - Provides an invalid or non-existent object
  - Confuses the required properties (claims the object has properties it doesn't)
  - Contains critical mathematical errors
  - Fails to address the problem

## FAILURE MODES (if score < 1.0)
Classify the primary failure mode:
- F1: Fabricated objects - The object doesn't exist or isn't well-defined
- F2: Property confusion - Valid object but wrong properties claimed/verified
- F3: Computational errors - Correct strategy but arithmetic/algebraic mistakes
- F4: Trivial/degenerate - Technically correct but trivially degenerate
- F5: Hallucinated theorems - Invokes non-existent theorems or results
- F6: Incomplete verification - Plausible object but fails to verify all properties

## OUTPUT FORMAT
Respond in EXACTLY this JSON format (no other text):
{{"score": <0 or 0.5 or 1>, "failure_mode": <"F1"|"F2"|"F3"|"F4"|"F5"|"F6"|null>, "reasoning": "<brief explanation of your grading>"}}
"""


def score_single(entry, env):
    """Score a single response using claude -p."""
    if entry.get('model_response') is None:
        return {
            **entry,
            'score': 0.0,
            'failure_mode': None,
            'scoring_reasoning': 'No model response (error/timeout)',
            'scoring_error': entry.get('error', 'no_response'),
        }

    prompt = SCORING_PROMPT.format(
        problem=entry['problem'],
        solution=entry.get('solution', 'No solution provided'),
        response=entry['model_response'],
    )

    cmd = ['claude', '-p', '--output-format', 'json']

    start = time.time()
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=300,
            env=env,
        )
        elapsed = time.time() - start

        if result.returncode != 0:
            return {
                **entry,
                'score': None,
                'failure_mode': None,
                'scoring_reasoning': None,
                'scoring_error': result.stderr.strip(),
            }

        # Parse claude output
        try:
            claude_output = json.loads(result.stdout)
            response_text = claude_output.get('result', result.stdout)
        except json.JSONDecodeError:
            response_text = result.stdout.strip()

        # Parse the scoring JSON from the response
        try:
            # Try to find JSON in the response
            scoring = extract_json(response_text)
            return {
                **entry,
                'score': scoring.get('score', None),
                'failure_mode': scoring.get('failure_mode', None),
                'scoring_reasoning': scoring.get('reasoning', ''),
                'scoring_error': None,
            }
        except (json.JSONDecodeError, ValueError):
            return {
                **entry,
                'score': None,
                'failure_mode': None,
                'scoring_reasoning': response_text[:500],
                'scoring_error': 'json_parse_error',
            }

    except subprocess.TimeoutExpired:
        return {
            **entry,
            'score': None,
            'failure_mode': None,
            'scoring_reasoning': None,
            'scoring_error': 'scoring_timeout_300s',
        }
    except Exception as e:
        return {
            **entry,
            'score': None,
            'failure_mode': None,
            'scoring_reasoning': None,
            'scoring_error': str(e),
        }


def extract_json(text):
    """Extract JSON object from text that may contain markdown or other content."""
    import re
    # Try direct parse first
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # Try to find JSON in code blocks
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if match:
        return json.loads(match.group(1))

    # Try to find bare JSON object
    match = re.search(r'\{[^{}]*"score"[^{}]*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group(0))

    raise ValueError("No JSON found in response")


def print_summary(scored):
    """Print scoring summary statistics."""
    valid = [s for s in scored if s.get('score') is not None]
    errors = [s for s in scored if s.get('scoring_error')]

    print(f"\n{'='*60}")
    print(f"SCORING SUMMARY")
    print(f"{'='*60}")
    print(f"Total: {len(scored)}")
    print(f"Successfully scored: {len(valid)}")
    print(f"Errors: {len(errors)}")

    if not valid:
        return

    scores = [s['score'] for s in valid]
    print(f"\nScore distribution:")
    for sv in [1.0, 0.5, 0.0]:
        cnt = scores.count(sv)
        print(f"  {sv}: {cnt} ({cnt/len(scores)*100:.1f}%)")

    avg = sum(scores) / len(scores)
    print(f"\nOverall accuracy (score=1.0): {scores.count(1.0)/len(scores)*100:.1f}%")
    print(f"With partial credit: {avg*100:.1f}%")

    # By difficulty
    print(f"\nBy difficulty:")
    for level in [1, 2, 3]:
        level_scores = [s['score'] for s in valid if s.get('difficulty') == level]
        if level_scores:
            acc = level_scores.count(1.0) / len(level_scores) * 100
            print(f"  Level {level}: {acc:.1f}% ({level_scores.count(1.0)}/{len(level_scores)})")

    # By question type
    print(f"\nBy question type:")
    from collections import Counter
    qtypes = set(s.get('question_type', 'unknown') for s in valid)
    for qt in sorted(qtypes):
        qt_scores = [s['score'] for s in valid if s.get('question_type') == qt]
        if qt_scores:
            acc = qt_scores.count(1.0) / len(qt_scores) * 100
            print(f"  {qt}: {acc:.1f}% ({qt_scores.count(1.0)}/{len(qt_scores)})")

    # By chapter
    print(f"\nBy chapter:")
    chapters = set(s.get('chapter', 'unknown') for s in valid)
    for ch in sorted(chapters):
        ch_scores = [s['score'] for s in valid if s.get('chapter') == ch]
        if ch_scores:
            acc = ch_scores.count(1.0) / len(ch_scores) * 100
            print(f"  {ch}: {acc:.1f}% ({ch_scores.count(1.0)}/{len(ch_scores)})")

    # Failure mode distribution
    failures = [s for s in valid if s['score'] < 1.0 and s.get('failure_mode')]
    if failures:
        print(f"\nFailure mode distribution (n={len(failures)}):")
        fm_counts = Counter(s['failure_mode'] for s in failures)
        for fm, cnt in sorted(fm_counts.items()):
            print(f"  {fm}: {cnt} ({cnt/len(failures)*100:.1f}%)")


def main():
    parser = argparse.ArgumentParser(
        description='Score ECAG-Bench responses using Claude Code CLI')
    parser.add_argument('--input', default='eval/results/pilot_100_responses.jsonl',
                        help='Input JSONL with responses')
    parser.add_argument('--output', default='eval/results/pilot_100_scored.jsonl',
                        help='Output JSONL with scores')
    parser.add_argument('--concurrency', type=int, default=3,
                        help='Number of concurrent scoring calls')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from partial output')
    args = parser.parse_args()

    # Load responses
    with open(args.input) as f:
        responses = [json.loads(line) for line in f]

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
        print(f"Resuming: {len(completed_ids)} already scored")

    remaining = [r for r in responses if r['id'] not in completed_ids]
    print(f"Responses to score: {len(remaining)} / {len(responses)}")

    if not remaining:
        print("All responses already scored!")
        # Still print summary
        with open(args.output) as f:
            scored = [json.loads(line) for line in f]
        print_summary(scored)
        return

    env = os.environ.copy()
    env.pop('CLAUDECODE', None)

    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    mode = 'a' if args.resume and completed_ids else 'w'
    completed = len(completed_ids)
    total = len(responses)

    scored_results = []

    with open(args.output, mode) as out_f:
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            futures = {
                executor.submit(score_single, entry, env): entry
                for entry in remaining
            }

            for future in as_completed(futures):
                entry = futures[future]
                try:
                    result = future.result()
                    out_f.write(json.dumps(result) + '\n')
                    out_f.flush()
                    scored_results.append(result)
                    completed += 1

                    score = result.get('score', '?')
                    fm = result.get('failure_mode', '')
                    err = result.get('scoring_error', '')
                    status = f"score={score}" + (f" {fm}" if fm else '') + (f" ERR:{err[:30]}" if err else '')
                    print(f"[{completed}/{total}] {entry['id']} - {status}")

                except Exception as e:
                    completed += 1
                    print(f"[{completed}/{total}] {entry['id']} - EXCEPTION: {e}")

    # Load all scored for summary (including previously completed)
    with open(args.output) as f:
        all_scored = [json.loads(line) for line in f]
    print_summary(all_scored)


if __name__ == '__main__':
    main()
