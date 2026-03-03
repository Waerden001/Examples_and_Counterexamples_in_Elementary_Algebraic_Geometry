#!/usr/bin/env python3
"""
enhance_examples.py — Enhance content/ Markdown examples via the Anthropic API.

Reads each example/remark/theorem block from content/*.md files, sends them
to the Anthropic API for restructuring into professional, detailed versions,
and writes the enhanced content back.

Features:
  - Resume support: tracks processed IDs in a state file
  - Dry-run mode: print prompts without calling the API
  - Configurable model and concurrency
  - Rate limiting with exponential backoff
  - Post-processing via fix_markdown_math logic
  - Generates improved benchmark problems (BENCHMARK_PROBLEM markers)

Usage:
    # Install dependency first:
    pip install anthropic

    # Enhance all examples:
    python scripts/enhance_examples.py --content-dir content

    # Dry-run (no API calls, print first prompt):
    python scripts/enhance_examples.py --content-dir content --dry-run

    # Resume from where we left off:
    python scripts/enhance_examples.py --content-dir content --resume

    # Process a single file:
    python scripts/enhance_examples.py --content-dir content --file content/basic_concepts/curves.md

    # Use a specific model:
    python scripts/enhance_examples.py --content-dir content --model claude-sonnet-4-20250514
"""

import os
import re
import json
import time
import argparse
import glob
import hashlib
import logging
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple
from pathlib import Path

try:
    import anthropic
except ImportError:
    anthropic = None

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
)
log = logging.getLogger('enhance')

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
DEFAULT_MODEL = 'claude-sonnet-4-20250514'
MAX_TOKENS = 8192
STATE_FILE = '.enhance_state.json'

# Environment types that we enhance
ENHANCEABLE_TYPES = {
    'example', 'remark', 'theorem', 'lemma', 'proposition',
    'corollary', 'conjecture', 'definition', 'exercise', 'warning',
}

# Regex to match ### blocks in content/*.md
# Title may contain LaTeX braces (e.g., $\mathbb{Z}$), so we match everything
# up to the {#ecag-XXXX} anchor at the end of the line.
BLOCK_PATTERN = re.compile(
    r'(### (?:Example|Remark|Theorem|Lemma|Proposition|Corollary|'
    r'Conjecture|Definition|Exercise|Warning)'
    r'(?::.*?)?'
    r'\s*\{#ecag-\d{4}\}\s*\n)'
    r'(.*?)(?=\n### |\Z)',
    re.DOTALL,
)

# More detailed regex for parsing
# Use a non-greedy match for the title, anchored by {#ecag-XXXX} at the end
HEADER_PATTERN = re.compile(
    r'### (Example|Remark|Theorem|Lemma|Proposition|Corollary|'
    r'Conjecture|Definition|Exercise|Warning)'
    r'(?:: (.*?))?\s*'
    r'\{#(ecag-\d{4})\}'
)

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Block:
    """A single ### block from a content Markdown file."""
    env_type: str        # e.g. 'example', 'remark'
    title: str           # Title after the colon (may be empty)
    ecag_id: str         # e.g. 'ecag-0024'
    body: str            # Everything after the header until the next ### or EOF
    header_line: str     # The full ### header line
    is_stub: bool        # Whether the body is empty or a stub marker
    file_path: str       # Source .md file
    start_pos: int       # Character offset in the file
    end_pos: int         # End character offset


@dataclass
class EnhanceResult:
    """Result from enhancing a single block."""
    ecag_id: str
    enhanced_body: str
    benchmark_problem: Optional[str]
    success: bool
    error: Optional[str] = None


@dataclass
class ProcessingState:
    """Tracks which blocks have been processed for resume support."""
    processed: Dict[str, str] = field(default_factory=dict)  # id -> content hash
    errors: Dict[str, str] = field(default_factory=dict)     # id -> error message
    stats: Dict[str, int] = field(default_factory=lambda: {
        'total': 0, 'enhanced': 0, 'stubs_filled': 0, 'skipped': 0, 'errors': 0,
    })


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

ENHANCE_PROMPT = """You are enhancing an algebraic geometry reference work. Given the original example below, produce a restructured, detailed version following this exact format:

**Statement:** [Precise mathematical statement of what this example demonstrates. This should be a clear, self-contained description.]

**Construction/Proof:** [Step-by-step proof or construction with full details. Every non-trivial claim must be justified. Use standard LaTeX only — write \\operatorname{{Spec}} not \\Spec, \\mathcal{{O}} not \\O, \\mathbf{{P}} not \\P, etc.]

**Key Insight:** [1-2 sentences explaining WHY this works and what makes it interesting or instructive.]

**Prerequisites:** [Comma-separated list of concepts needed to understand this example.]

Rules:
- Preserve the mathematical content and theorem/example being demonstrated. Enhance the presentation, do not change what is being proved or shown.
- If the original is a stub (empty or marked as stub), construct the example from scratch based on the title. Make it detailed and complete.
- If the original has errors, unresolved questions, or hedging language ("maybe", "it seems"), resolve them with correct mathematics.
- All math must use standard LaTeX compatible with MathJax 3. NO custom macros.
  - Use \\operatorname{{Spec}} not \\Spec
  - Use \\mathcal{{O}} not \\O
  - Use \\mathbf{{A}} not \\A or \\mathbb{{A}}
  - Use \\mathscr{{E}} not \\cE
  - Use \\overline{{X}} not \\ol{{X}}
  - Use \\widetilde{{X}} not \\wt{{X}}
  - Use \\mathfrak{{m}} not \\mf{{m}}
- Write in English. Use clear, textbook-level mathematical prose.
- Do NOT use \\begin{{theorem}} or other LaTeX environments — use Markdown formatting.
- For display math, use $$ on its own line. Place blank lines before and after display math.
- For inline math, use single $ delimiters.
- Avoid unnecessary verbosity. Be precise and efficient.

Also provide a precise benchmark question for this example. The question should:
- Be self-contained (include all necessary definitions and context)
- Be specific enough that a correct answer requires genuine mathematical knowledge
- Not be trivially answerable by restating the title
- Include constraints where possible to make the answer more precise

Write the benchmark question on a single line starting with "BENCHMARK_PROBLEM:" (no line breaks within it).

---
ENVIRONMENT TYPE: {env_type}
TITLE: {title}
ECAG ID: {ecag_id}
ORIGINAL CONTENT:
{body}
---"""

REMARK_PROMPT = """You are enhancing an algebraic geometry reference work. Given the original remark below, produce a clearer, more precise version.

For remarks, preserve the informal/explanatory nature but make the mathematics precise:

**Remark:** [Clear, precise mathematical statement or observation. Explain the significance and context. Use standard LaTeX only.]

Rules:
- Preserve the mathematical content. Enhance clarity and precision.
- If the original is a stub, write the remark from scratch based on the title.
- All math must use standard LaTeX compatible with MathJax 3 (no custom macros).
- Write in English. Be concise but precise.
- For display math, use $$ on its own line with blank lines before and after.
- Do NOT include BENCHMARK_PROBLEM for pure remarks without mathematical content worth testing.
- If the remark contains a testable mathematical fact, include:

BENCHMARK_PROBLEM: [A specific question testing the key fact in this remark.]

---
ENVIRONMENT TYPE: {env_type}
TITLE: {title}
ECAG ID: {ecag_id}
ORIGINAL CONTENT:
{body}
---"""


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_blocks(filepath: str) -> List[Block]:
    """Parse a Markdown file and extract all ### blocks."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = []
    for match in BLOCK_PATTERN.finditer(content):
        header_line = match.group(1)
        body = match.group(2).strip()

        hm = HEADER_PATTERN.match(header_line.strip())
        if not hm:
            continue

        env_type = hm.group(1).lower()
        title = (hm.group(2) or '').strip()
        ecag_id = hm.group(3)

        is_stub = (
            body.startswith('> **Status:** Stub')
            or len(body.strip()) < 5
        )

        blocks.append(Block(
            env_type=env_type,
            title=title,
            ecag_id=ecag_id,
            body=body,
            header_line=header_line.strip(),
            is_stub=is_stub,
            file_path=filepath,
            start_pos=match.start(),
            end_pos=match.end(),
        ))

    return blocks


def content_hash(block: Block) -> str:
    """Hash of block content for change detection."""
    data = f'{block.ecag_id}:{block.title}:{block.body}'
    return hashlib.md5(data.encode()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# API interaction
# ---------------------------------------------------------------------------

def build_prompt(block: Block) -> str:
    """Build the enhancement prompt for a block."""
    if block.env_type == 'remark' and not block.title:
        template = REMARK_PROMPT
    elif block.env_type in ('remark',):
        template = REMARK_PROMPT
    else:
        template = ENHANCE_PROMPT

    return template.format(
        env_type=block.env_type.capitalize(),
        title=block.title or '(untitled)',
        ecag_id=block.ecag_id,
        body=block.body if block.body and not block.is_stub else '(empty stub — please construct from scratch based on the title)',
    )


def call_api(
    client: 'anthropic.Anthropic',
    prompt: str,
    model: str,
    max_retries: int = 3,
) -> str:
    """Call the Anthropic API with retry and backoff."""
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=MAX_TOKENS,
                messages=[{'role': 'user', 'content': prompt}],
            )
            return response.content[0].text
        except anthropic.RateLimitError:
            wait = 2 ** (attempt + 1)
            log.warning(f'Rate limited, waiting {wait}s (attempt {attempt + 1}/{max_retries})')
            time.sleep(wait)
        except anthropic.APIError as e:
            if attempt == max_retries - 1:
                raise
            wait = 2 ** attempt
            log.warning(f'API error: {e}, retrying in {wait}s')
            time.sleep(wait)
    raise RuntimeError('Max retries exceeded')


def parse_response(response_text: str) -> Tuple[str, Optional[str]]:
    """Parse the API response into enhanced body and optional benchmark problem.

    Returns (enhanced_body, benchmark_problem).
    """
    # Extract BENCHMARK_PROBLEM if present
    benchmark_problem = None
    bm_match = re.search(r'^BENCHMARK_PROBLEM:\s*(.+)$', response_text, re.MULTILINE)
    if bm_match:
        benchmark_problem = bm_match.group(1).strip()
        # Remove the BENCHMARK_PROBLEM line from the body
        response_text = response_text[:bm_match.start()] + response_text[bm_match.end():]

    # Clean up the enhanced body
    body = response_text.strip()

    # Remove any leading/trailing --- markers that might be in the response
    body = re.sub(r'^---\s*$', '', body, flags=re.MULTILINE).strip()

    return body, benchmark_problem


# ---------------------------------------------------------------------------
# Post-processing (inline version of fix_markdown_math logic)
# ---------------------------------------------------------------------------

def fix_display_math_spacing(text: str) -> str:
    """Ensure blank lines surround $$ display math blocks."""
    lines = text.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip code blocks
        if stripped.startswith('```'):
            result.append(line)
            i += 1
            while i < len(lines):
                result.append(lines[i])
                if lines[i].strip().startswith('```') and i > 0:
                    i += 1
                    break
                i += 1
            continue

        # Single-line display math $$...$$
        if re.match(r'^\s*\$\$.*\$\$\s*$', stripped) and stripped != '$$':
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
            i += 1
            continue

        # Opening $$ on its own line
        if stripped == '$$':
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            i += 1
            continue

        result.append(line)
        i += 1

    return '\n'.join(result)


def normalize_blank_lines(text: str) -> str:
    """Collapse 3+ consecutive blank lines to 2."""
    return re.sub(r'\n{4,}', '\n\n\n', text)


def postprocess_body(text: str) -> str:
    """Apply post-processing fixes to enhanced body text."""
    text = fix_display_math_spacing(text)
    text = normalize_blank_lines(text)
    return text.strip()


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_state(state_path: str) -> ProcessingState:
    """Load processing state from file."""
    if os.path.exists(state_path):
        with open(state_path, 'r') as f:
            data = json.load(f)
        state = ProcessingState()
        state.processed = data.get('processed', {})
        state.errors = data.get('errors', {})
        state.stats = data.get('stats', state.stats)
        return state
    return ProcessingState()


def save_state(state: ProcessingState, state_path: str):
    """Save processing state to file."""
    with open(state_path, 'w') as f:
        json.dump(asdict(state), f, indent=2)


# ---------------------------------------------------------------------------
# File rewriting
# ---------------------------------------------------------------------------

def rewrite_file(filepath: str, replacements: Dict[str, Tuple[str, Optional[str]]]):
    """Rewrite a Markdown file, replacing block bodies with enhanced versions.

    replacements: { ecag_id: (enhanced_body, benchmark_problem) }
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process block by block, from last to first (to preserve offsets)
    blocks = list(BLOCK_PATTERN.finditer(content))
    for match in reversed(blocks):
        header_line = match.group(1)
        hm = HEADER_PATTERN.match(header_line.strip())
        if not hm:
            continue
        ecag_id = hm.group(3)

        if ecag_id not in replacements:
            continue

        enhanced_body, benchmark_problem = replacements[ecag_id]

        # Build the new block: header + enhanced body
        # The header_line already includes the trailing newline in group(1)
        new_body = postprocess_body(enhanced_body)

        # If there's a benchmark problem, embed it as an HTML comment
        # so build_benchmark.py can extract it
        if benchmark_problem:
            new_body += f'\n\n<!-- BENCHMARK_PROBLEM: {benchmark_problem} -->'

        # Replace only the body part (group 2), keeping the header (group 1)
        new_block = header_line + '\n' + new_body + '\n'
        content = content[:match.start()] + new_block + content[match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def enhance_block(
    client: 'anthropic.Anthropic',
    block: Block,
    model: str,
    dry_run: bool = False,
) -> EnhanceResult:
    """Enhance a single block."""
    prompt = build_prompt(block)

    if dry_run:
        log.info(f'[DRY-RUN] {block.ecag_id}: would send {len(prompt)} chars')
        return EnhanceResult(
            ecag_id=block.ecag_id,
            enhanced_body=block.body,
            benchmark_problem=None,
            success=True,
        )

    try:
        response_text = call_api(client, prompt, model)
        enhanced_body, benchmark_problem = parse_response(response_text)

        return EnhanceResult(
            ecag_id=block.ecag_id,
            enhanced_body=enhanced_body,
            benchmark_problem=benchmark_problem,
            success=True,
        )
    except Exception as e:
        log.error(f'{block.ecag_id}: API error: {e}')
        return EnhanceResult(
            ecag_id=block.ecag_id,
            enhanced_body=block.body,
            benchmark_problem=None,
            success=False,
            error=str(e),
        )


def process_file(
    filepath: str,
    client: Optional['anthropic.Anthropic'],
    model: str,
    state: ProcessingState,
    state_path: str,
    dry_run: bool = False,
    delay: float = 1.0,
) -> int:
    """Process all blocks in a single file.

    Returns the number of blocks enhanced.
    """
    blocks = parse_blocks(filepath)
    if not blocks:
        return 0

    log.info(f'Processing {filepath}: {len(blocks)} blocks')
    replacements: Dict[str, Tuple[str, Optional[str]]] = {}
    enhanced_count = 0

    for block in blocks:
        state.stats['total'] = state.stats.get('total', 0) + 1

        # Skip if already processed (resume support)
        chash = content_hash(block)
        if block.ecag_id in state.processed and state.processed[block.ecag_id] == chash:
            log.debug(f'  {block.ecag_id}: already processed, skipping')
            state.stats['skipped'] = state.stats.get('skipped', 0) + 1
            continue

        log.info(f'  Enhancing {block.ecag_id}: {block.env_type}'
                 f'{" — " + block.title[:60] if block.title else ""}'
                 f'{" [STUB]" if block.is_stub else ""}')

        result = enhance_block(client, block, model, dry_run=dry_run)

        if result.success and not dry_run:
            replacements[block.ecag_id] = (result.enhanced_body, result.benchmark_problem)
            state.processed[block.ecag_id] = chash
            enhanced_count += 1

            if block.is_stub:
                state.stats['stubs_filled'] = state.stats.get('stubs_filled', 0) + 1
            else:
                state.stats['enhanced'] = state.stats.get('enhanced', 0) + 1

            # Save state after each successful enhancement
            save_state(state, state_path)

            # Rate limiting delay between API calls
            if delay > 0:
                time.sleep(delay)
        elif not result.success:
            state.errors[block.ecag_id] = result.error or 'unknown error'
            state.stats['errors'] = state.stats.get('errors', 0) + 1
            save_state(state, state_path)

    # Write all replacements to file at once
    if replacements:
        rewrite_file(filepath, replacements)
        log.info(f'  Wrote {len(replacements)} enhanced blocks to {filepath}')

    return enhanced_count


def collect_files(content_dir: str, single_file: Optional[str] = None) -> List[str]:
    """Collect Markdown files to process."""
    if single_file:
        if not os.path.isfile(single_file):
            log.error(f'File not found: {single_file}')
            return []
        return [single_file]

    files = sorted(glob.glob(os.path.join(content_dir, '**', '*.md'), recursive=True))
    # Exclude index.md and other non-content files
    files = [f for f in files if not f.endswith('index.md')]
    return files


def main():
    parser = argparse.ArgumentParser(
        description='Enhance content/ examples via Anthropic API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/enhance_examples.py --content-dir content --dry-run
  python scripts/enhance_examples.py --content-dir content --file content/basic_concepts/curves.md
  python scripts/enhance_examples.py --content-dir content --resume
  python scripts/enhance_examples.py --content-dir content --model claude-opus-4-6
        """,
    )
    parser.add_argument('--content-dir', default='content',
                        help='Path to content/ directory (default: content)')
    parser.add_argument('--file', '-f', default=None,
                        help='Process a single file instead of all files')
    parser.add_argument('--model', '-m', default=DEFAULT_MODEL,
                        help=f'Anthropic model to use (default: {DEFAULT_MODEL})')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print prompts without calling the API')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from previous state (skip already-processed blocks)')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay in seconds between API calls (default: 1.0)')
    parser.add_argument('--state-file', default=STATE_FILE,
                        help=f'Path to state file (default: {STATE_FILE})')
    parser.add_argument('--show-prompt', action='store_true',
                        help='Print the prompt for the first block and exit')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable debug logging')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Collect files
    files = collect_files(args.content_dir, args.file)
    if not files:
        log.error('No files to process')
        return

    log.info(f'Found {len(files)} files to process')

    # If --show-prompt, just print the first block's prompt and exit
    if args.show_prompt:
        for f in files:
            blocks = parse_blocks(f)
            if blocks:
                prompt = build_prompt(blocks[0])
                print(f'=== Prompt for {blocks[0].ecag_id} ({f}) ===')
                print(prompt)
                return
        log.error('No blocks found in any file')
        return

    # Initialize API client
    client = None
    if not args.dry_run:
        if anthropic is None:
            log.error('anthropic package not installed. Run: pip install anthropic')
            return
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            log.error('ANTHROPIC_API_KEY environment variable not set')
            return
        client = anthropic.Anthropic(api_key=api_key)

    # Load or create state
    state_path = args.state_file
    if args.resume:
        state = load_state(state_path)
        log.info(f'Resumed state: {len(state.processed)} previously processed')
    else:
        state = ProcessingState()

    # Process files
    total_enhanced = 0
    for filepath in files:
        try:
            count = process_file(
                filepath=filepath,
                client=client,
                model=args.model,
                state=state,
                state_path=state_path,
                dry_run=args.dry_run,
                delay=args.delay,
            )
            total_enhanced += count
        except KeyboardInterrupt:
            log.warning('Interrupted — saving state...')
            save_state(state, state_path)
            break
        except Exception as e:
            log.error(f'Error processing {filepath}: {e}')
            continue

    # Final state save
    save_state(state, state_path)

    # Print summary
    print('\n' + '=' * 60)
    print('Enhancement Summary')
    print('=' * 60)
    print(f'  Files processed:    {len(files)}')
    print(f'  Blocks total:       {state.stats.get("total", 0)}')
    print(f'  Enhanced:           {state.stats.get("enhanced", 0)}')
    print(f'  Stubs filled:       {state.stats.get("stubs_filled", 0)}')
    print(f'  Skipped (resumed):  {state.stats.get("skipped", 0)}')
    print(f'  Errors:             {state.stats.get("errors", 0)}')
    print(f'  State saved to:     {state_path}')
    if state.errors:
        print(f'\nErrors:')
        for eid, err in state.errors.items():
            print(f'  {eid}: {err}')
    print()


if __name__ == '__main__':
    main()
