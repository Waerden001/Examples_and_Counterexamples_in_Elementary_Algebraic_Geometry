#!/usr/bin/env python3
"""
validate_benchmark.py — Validate ECAG-Bench JSONL against schema.

Checks:
  1. Each line is valid JSON
  2. Each entry conforms to benchmark/schema.json
  3. All IDs are unique
  4. No unexpanded custom macros in problem/solution fields
  5. Required fields are non-empty

Usage:
    python validate_benchmark.py benchmark/data/ecag_bench.jsonl benchmark/schema.json
"""

import json
import re
import sys
import argparse
from typing import List, Tuple


# Custom macros that should have been expanded (word-boundary aware patterns)
UNEXPANDED_PATTERNS = [
    (r'\\A(?![a-zA-Z])', r'\A'),
    (r'\\P(?![a-zA-Z])', r'\P'),
    (r'\\C(?![a-zA-Z])', r'\C'),
    (r'\\Q(?![a-zA-Z])', r'\Q'),
    (r'\\Z(?![a-zA-Z])', r'\Z'),
    (r'\\O(?![a-zA-Z])', r'\O'),
    (r'\\F(?![a-zA-Z])', r'\F'),
    (r'\\E(?![a-zA-Z])', r'\E'),
    (r'\\L(?![a-zA-Z])', r'\L'),
    (r'\\cA(?![a-zA-Z])', r'\cA'),
    (r'\\cM(?![a-zA-Z])', r'\cM'),
    (r'\\ol\{', r'\ol{'),
    (r'\\wt\{', r'\wt{'),
    (r'\\mf\{', r'\mf{'),
    (r'\\shuai\{', r'\shuai{'),
    (r'\\reword\{', r'\reword{'),
]


def validate_schema(entry: dict, schema: dict) -> List[str]:
    """Basic schema validation without jsonschema dependency."""
    errors = []

    # Check required fields
    for field in schema.get('required', []):
        if field not in entry:
            errors.append(f'missing required field: {field}')

    props = schema.get('properties', {})
    for field, value in entry.items():
        if field not in props:
            if schema.get('additionalProperties') is False:
                errors.append(f'unknown field: {field}')
            continue

        spec = props[field]

        # Type check
        expected_types = spec.get('type', [])
        if isinstance(expected_types, str):
            expected_types = [expected_types]

        type_ok = False
        for t in expected_types:
            if t == 'string' and isinstance(value, str):
                type_ok = True
            elif t == 'integer' and isinstance(value, int) and not isinstance(value, bool):
                type_ok = True
            elif t == 'boolean' and isinstance(value, bool):
                type_ok = True
            elif t == 'array' and isinstance(value, list):
                type_ok = True
            elif t == 'null' and value is None:
                type_ok = True
            elif t == 'number' and isinstance(value, (int, float)):
                type_ok = True

        if not type_ok and value is not None:
            errors.append(f'{field}: expected type {expected_types}, got {type(value).__name__}')

        # Enum check
        if 'enum' in spec and value is not None:
            if value not in spec['enum']:
                errors.append(f'{field}: {value!r} not in {spec["enum"]}')

        # Pattern check
        if 'pattern' in spec and isinstance(value, str):
            if not re.match(spec['pattern'], value):
                errors.append(f'{field}: {value!r} does not match pattern {spec["pattern"]}')

        # Min/max for integers
        if 'minimum' in spec and isinstance(value, (int, float)):
            if value < spec['minimum']:
                errors.append(f'{field}: {value} < minimum {spec["minimum"]}')
        if 'maximum' in spec and isinstance(value, (int, float)):
            if value > spec['maximum']:
                errors.append(f'{field}: {value} > maximum {spec["maximum"]}')

        # minLength for strings
        if 'minLength' in spec and isinstance(value, str):
            if len(value) < spec['minLength']:
                errors.append(f'{field}: length {len(value)} < minLength {spec["minLength"]}')

    return errors


def check_unexpanded_macros(text: str) -> List[str]:
    """Check for unexpanded custom macros in text."""
    warnings = []
    for pattern, name in UNEXPANDED_PATTERNS:
        matches = re.findall(pattern, text)
        if matches:
            warnings.append(f'unexpanded macro {name} found ({len(matches)} occurrences)')
    return warnings


def validate_jsonl(jsonl_path: str, schema_path: str) -> Tuple[int, int, int]:
    """Validate a JSONL file against a schema.

    Returns (total, errors, warnings).
    """
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    total = 0
    error_count = 0
    warning_count = 0
    seen_ids = set()

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            total += 1

            # Parse JSON
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as e:
                print(f'  ERROR line {line_num}: invalid JSON: {e}')
                error_count += 1
                continue

            entry_id = entry.get('id', f'line-{line_num}')

            # Schema validation
            schema_errors = validate_schema(entry, schema)
            for err in schema_errors:
                print(f'  ERROR {entry_id}: {err}')
                error_count += 1

            # Unique ID check
            if entry_id in seen_ids:
                print(f'  ERROR {entry_id}: duplicate ID')
                error_count += 1
            seen_ids.add(entry_id)

            # Check for unexpanded macros in problem and solution
            for field in ('problem', 'solution'):
                text = entry.get(field, '')
                if text:
                    macro_warnings = check_unexpanded_macros(text)
                    for w in macro_warnings:
                        print(f'  WARN {entry_id}.{field}: {w}')
                        warning_count += 1

    return total, error_count, warning_count


def main():
    parser = argparse.ArgumentParser(description='Validate ECAG-Bench JSONL')
    parser.add_argument('jsonl', help='Path to .jsonl file')
    parser.add_argument('schema', help='Path to schema.json')
    args = parser.parse_args()

    print(f'Validating {args.jsonl} against {args.schema}...')
    total, errors, warnings = validate_jsonl(args.jsonl, args.schema)

    print(f'\nResults: {total} entries, {errors} errors, {warnings} warnings')

    if errors > 0:
        print('VALIDATION FAILED')
        sys.exit(1)
    else:
        print('VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
