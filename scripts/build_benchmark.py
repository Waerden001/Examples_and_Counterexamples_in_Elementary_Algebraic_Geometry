#!/usr/bin/env python3
"""
build_benchmark.py — Build ECAG-Bench JSONL from content/ Markdown files.

Extracts example/remark/theorem environments from Markdown files produced
by tex_to_md.py and generates benchmark entries in JSONL format.

Usage:
    python build_benchmark.py --content-dir content --output benchmark/data/ecag_bench.jsonl
"""

import os
import re
import json
import argparse
import glob
from typing import List, Dict, Any, Optional


def infer_topic_subtopic(title: str, chapter: str) -> tuple:
    """Infer topic and subtopic from the example title and chapter."""
    title_lower = title.lower()

    topic_keywords = {
        'affine': ('schemes', 'affineness'),
        'reduced': ('schemes', 'reduced_separated'),
        'separated': ('schemes', 'reduced_separated'),
        'flat': ('morphisms', 'flatness'),
        'finite type': ('morphisms', 'finiteness'),
        'quasi-finite': ('morphisms', 'finiteness'),
        'proper': ('morphisms', 'properness'),
        'smooth': ('morphisms', 'smoothness'),
        'etale': ('morphisms', 'etale'),
        'étale': ('morphisms', 'etale'),
        'picard': ('invariants', 'picard_group'),
        'pic(': ('invariants', 'picard_group'),
        'class group': ('invariants', 'class_group'),
        'cl(': ('invariants', 'class_group'),
        'genus': ('curves', 'genus'),
        'curve': ('curves', 'general'),
        'elliptic': ('curves', 'elliptic_curves'),
        'ample': ('divisors', 'ampleness'),
        'divisor': ('divisors', 'general'),
        'linear system': ('divisors', 'linear_systems'),
        'normal bundle': ('bundles', 'normal_bundles'),
        'vector bundle': ('bundles', 'vector_bundles'),
        'sheaf': ('sheaves', 'general'),
        'sheaves': ('sheaves', 'general'),
        'coherent': ('sheaves', 'coherent'),
        'locally free': ('sheaves', 'locally_free'),
        'push-forward': ('functors', 'pushforward'),
        'pull-back': ('functors', 'pullback'),
        'base change': ('functors', 'base_change'),
        'cohomology': ('cohomology', 'general'),
        'spectral sequence': ('cohomology', 'spectral_sequences'),
        'derived': ('cohomology', 'derived_categories'),
        'fourier-mukai': ('cohomology', 'fourier_mukai'),
        'moduli': ('moduli', 'general'),
        'stable': ('moduli', 'stability'),
        'deformation': ('moduli', 'deformation_theory'),
        'hilbert': ('moduli', 'hilbert_scheme'),
        'stack': ('moduli', 'stacks'),
        'hironaka': ('schemes', 'hironaka_examples'),
        'intersection': ('computations', 'intersection_theory'),
        'chow': ('computations', 'intersection_theory'),
        'quantum': ('computations', 'quantum_cohomology'),
        'hodge': ('computations', 'hodge_theory'),
        'weight': ('computations', 'weight_filtrations'),
        'morse': ('computations', 'morse_theory'),
        'monad': ('computations', 'monads'),
        'dimension': ('schemes', 'dimension'),
        'frobenius': ('morphisms', 'frobenius'),
        'automorphism': ('groups', 'automorphisms'),
        'group scheme': ('groups', 'group_schemes'),
    }

    for keyword, (topic, subtopic) in topic_keywords.items():
        if keyword in title_lower:
            return topic, subtopic

    # Fallback based on chapter
    chapter_defaults = {
        'basic_concepts': ('basic_concepts', 'general'),
        'cohomology': ('cohomology', 'general'),
        'computations': ('computations', 'general'),
        'moduli': ('moduli', 'general'),
        'relative': ('relative', 'general'),
    }
    return chapter_defaults.get(chapter, ('general', 'general'))


def infer_question_type(env_type: str, title: str) -> str:
    """Infer the question type from environment type and title."""
    title_lower = title.lower()

    if 'not' in title_lower or 'counterexample' in title_lower or 'but' in title_lower:
        return 'counterexample'
    if 'compute' in title_lower or 'calculation' in title_lower:
        return 'computation'
    if env_type in ('theorem', 'lemma', 'proposition', 'corollary'):
        return 'proof'
    if env_type == 'example':
        # Check if title suggests computation
        compute_patterns = [r'cl\(', r'pic\(', r'picard', r'chow ring',
                            r'hodge number', r'euler', r'genus']
        for pat in compute_patterns:
            if re.search(pat, title_lower):
                return 'computation'
        return 'example'
    return 'example'


def infer_difficulty(title: str, body: str, env_type: str) -> int:
    """Heuristic difficulty estimate: 1, 2, or 3."""
    title_lower = title.lower()
    body_len = len(body)

    # Level 3 indicators
    hard_keywords = ['hironaka', 'fourier-mukai', 'quantum cohomology',
                     'monad', 'weight spectral', 'descent data',
                     'isotrivial', 'picard of moduli', 'five conics']
    for kw in hard_keywords:
        if kw in title_lower or kw in body.lower()[:200]:
            return 3

    # Level 1 indicators
    if body_len < 200 or env_type in ('remark', 'definition'):
        return 1

    # Level 2 for everything else with substantial content
    if body_len > 500:
        return 2

    return 1


def title_to_problem(title: str, env_type: str, question_type: str) -> str:
    """Convert an example/remark title to a benchmark problem statement."""
    if not title:
        return ''

    # Clean up LaTeX artifacts in title
    clean = title.strip()

    if question_type == 'counterexample':
        return f'Give a counterexample or example demonstrating: {clean}.'
    elif question_type == 'computation':
        return f'Compute or describe: {clean}.'
    elif question_type == 'proof':
        return f'Prove: {clean}.'
    else:
        return f'Give an example: {clean}.'


def parse_markdown_file(filepath: str) -> List[Dict[str, Any]]:
    """Parse a Markdown file and extract benchmark entries."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []

    # Parse front matter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    chapter = ''
    source_file = ''
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            if line.startswith('chapter:'):
                chapter = line.split(':', 1)[1].strip()
            elif line.startswith('source:'):
                source_file = line.split(':', 1)[1].strip()

    # Find all ### blocks (environments)
    pattern = re.compile(
        r'### (Example|Remark|Theorem|Lemma|Proposition|Corollary|'
        r'Conjecture|Definition|Exercise|Warning)'
        r'(?:: ([^\n{]*))?\s*'  # optional title
        r'\{#(ecag-\d{4})\}\s*\n'  # anchor
        r'(.*?)(?=\n### |\Z)',  # body until next ### or end
        re.DOTALL
    )

    for match in pattern.finditer(content):
        env_type = match.group(1).lower()
        title = (match.group(2) or '').strip()
        ecag_id = match.group(3)
        body = match.group(4).strip()

        # Detect stubs
        is_stub = body.startswith('> **Status:** Stub') or len(body) < 5

        # Skip remarks and definitions for the benchmark — focus on examples
        if env_type in ('remark', 'definition') and not title:
            continue

        # Infer metadata
        question_type = infer_question_type(env_type, title)
        topic, subtopic = infer_topic_subtopic(title, chapter)
        difficulty = infer_difficulty(title, body, env_type)
        problem = title_to_problem(title, env_type, question_type)

        if not problem:
            continue

        # Determine verification strategy
        if question_type == 'computation':
            verification_strategy = 'exact'
        elif question_type in ('example', 'counterexample'):
            verification_strategy = 'cas'
        else:
            verification_strategy = 'rubric'

        entry = {
            'id': ecag_id,
            'problem': problem,
            'solution': body if not is_stub else '',
            'answer': None,
            'answer_type': question_type if question_type != 'computation' else 'closed_form',
            'difficulty': difficulty,
            'chapter': chapter,
            'topic': topic,
            'subtopic': subtopic,
            'question_type': question_type,
            'tags': [],
            'source': 'Original',
            'reference': None,
            'prerequisites': [],
            'msc_codes': [],
            'verification_strategy': verification_strategy,
            'verification_script': None,
            'accepts_multiple': question_type in ('example', 'counterexample'),
            'is_stub': is_stub,
            'latex_source': source_file,
        }
        entries.append(entry)

    return entries


def main():
    parser = argparse.ArgumentParser(description='Build ECAG-Bench JSONL from Markdown')
    parser.add_argument('--content-dir', default='content',
                        help='Path to content/ directory')
    parser.add_argument('--output', '-o', default='benchmark/data/ecag_bench.jsonl',
                        help='Output JSONL file')
    args = parser.parse_args()

    all_entries = []
    md_files = sorted(glob.glob(os.path.join(args.content_dir, '**', '*.md'), recursive=True))

    for md_file in md_files:
        entries = parse_markdown_file(md_file)
        all_entries.append((md_file, entries))

    # Write JSONL
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    total = 0
    with open(args.output, 'w', encoding='utf-8') as f:
        for md_file, entries in all_entries:
            for entry in entries:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
                total += 1

    # Statistics
    stubs = sum(1 for _, entries in all_entries for e in entries if e['is_stub'])
    by_chapter = {}
    by_difficulty = {1: 0, 2: 0, 3: 0}
    by_qtype = {}
    by_vstrategy = {}
    for _, entries in all_entries:
        for e in entries:
            by_chapter[e['chapter']] = by_chapter.get(e['chapter'], 0) + 1
            by_difficulty[e['difficulty']] += 1
            by_qtype[e['question_type']] = by_qtype.get(e['question_type'], 0) + 1
            by_vstrategy[e['verification_strategy']] = by_vstrategy.get(e['verification_strategy'], 0) + 1

    print(f'Written {total} entries to {args.output}')
    print(f'  Stubs: {stubs}')
    print(f'  By chapter: {json.dumps(by_chapter, indent=2)}')
    print(f'  By difficulty: {json.dumps(by_difficulty, indent=2)}')
    print(f'  By question type: {json.dumps(by_qtype, indent=2)}')
    print(f'  By verification: {json.dumps(by_vstrategy, indent=2)}')


if __name__ == '__main__':
    main()
