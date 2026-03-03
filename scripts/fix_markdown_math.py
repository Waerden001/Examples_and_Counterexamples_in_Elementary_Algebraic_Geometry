#!/usr/bin/env python3
"""
fix_markdown_math.py — Post-process Markdown files to fix MathJax/arithmatex
rendering issues.

Fixes:
  1. Ensure blank lines before and after $$...$$ display math
  2. Split inline $$...$$ (text before/after $$ on same line)
  3. Fix tikzcd blocks: remove $$ wrapping around code blocks
  4. Fix \text{[} and \text{]} in headings that break {#ecag-XXXX} anchors
  5. Replace $$ in headings with $ (inline math)
  6. Fix %% pseudo-comments
  7. Clean up $$ only lines that are orphaned

Usage:
    python fix_markdown_math.py content/   # fix all .md files in-place
    python fix_markdown_math.py file.md    # fix a single file
"""

import re
import os
import sys
import glob


def fix_display_math_spacing(text: str) -> str:
    """Ensure blank lines surround $$...$$ display math blocks.

    Handles both single-line ($$formula$$) and multi-line blocks.
    """
    lines = text.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip lines inside code blocks
        if stripped.startswith('```'):
            result.append(line)
            i += 1
            # Skip until closing ```
            while i < len(lines):
                result.append(lines[i])
                if lines[i].strip().startswith('```') and i > 0:
                    i += 1
                    break
                i += 1
            continue

        # Case 1: Single-line display math $$...$$
        # Match lines that are ONLY a display math block (possibly with whitespace)
        if re.match(r'^\s*\$\$.*\$\$\s*$', stripped) and stripped != '$$':
            # Ensure blank line before (if previous line is not blank and not start)
            if result and result[-1].strip() != '' and not result[-1].strip().startswith('---'):
                result.append('')
            result.append(line)
            # Ensure blank line after
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
            i += 1
            continue

        # Case 2: Opening $$ on its own line (multi-line block start)
        if stripped == '$$':
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            i += 1
            continue

        # Case 3: Text BEFORE $$formula$$ on same line
        # e.g. "Then $$x^2 + y^2 = 1$$"
        m = re.match(r'^(.+?)\s*(\$\$.+\$\$)\s*$', stripped)
        if m and not stripped.startswith('#') and not stripped.startswith('```'):
            text_before = m.group(1)
            math_part = m.group(2)
            # Don't split if it's inside a list item and the math is short
            result.append(text_before)
            result.append('')
            result.append(math_part)
            result.append('')
            i += 1
            continue

        # Case 4: $$formula$$ followed by text on same line
        # e.g. "$$x^2$$ is the formula"
        m = re.match(r'^(\$\$.+?\$\$)\s+(.+)$', stripped)
        if m and not stripped.startswith('#'):
            math_part = m.group(1)
            text_after = m.group(2)
            if result and result[-1].strip() != '':
                result.append('')
            result.append(math_part)
            result.append('')
            result.append(text_after)
            i += 1
            continue

        # Case 5: text $$formula$$ more text (both sides)
        m = re.match(r'^(.+?)\s*(\$\$.+?\$\$)\s+(.+)$', stripped)
        if m and not stripped.startswith('#'):
            text_before = m.group(1)
            math_part = m.group(2)
            text_after = m.group(3)
            result.append(text_before)
            result.append('')
            result.append(math_part)
            result.append('')
            result.append(text_after)
            i += 1
            continue

        result.append(line)
        i += 1

    return '\n'.join(result)


def fix_tikzcd_blocks(text: str) -> str:
    """Remove $$ wrapping around tikzcd/xymatrix code blocks."""
    # Pattern: $$<!-- tikzcd ... --> followed by ```latex block and then $$
    # Replace with just the comment + code block (no $$)
    text = re.sub(
        r'\$\$\s*(<!-- (?:tikzcd|xymatrix) diagram: manual conversion needed -->)\s*\n'
        r'(```latex\n.*?```)\s*\n\$\$',
        r'\1\n\2',
        text,
        flags=re.DOTALL,
    )
    # Also handle case where $$ is on same line as comment
    text = re.sub(
        r'\$\$(<!-- (?:tikzcd|xymatrix) diagram: manual conversion needed -->)',
        r'\1',
        text,
    )
    return text


def fix_heading_math(text: str) -> str:
    """Fix math issues in ### headings."""
    lines = text.split('\n')
    result = []

    for line in lines:
        if not line.startswith('###'):
            result.append(line)
            continue

        # Fix $$ display math in headings → $ inline math
        line = re.sub(r'\$\$([^$]+)\$\$', r'$\1$', line)

        # Fix \text{[} and \text{]} that eat the {#ecag-XXXX} anchor
        # Pattern: $\mathrm{Spec}(k\text{[}\epsilon\text{ {#ecag-XXXX}
        # The problem is \text{[} swallows everything until }
        # Fix: replace \text{[} with [ and \text{]} with ]
        line = re.sub(r'\\text\{\[\}', '[', line)
        line = re.sub(r'\\text\{\]\}', ']', line)

        # Fix case where \text{ ate the anchor:
        # $...\text{ {#ecag-XXXX}\n}$] on next line
        # Detect: heading ends with \text{ {#ecag-XXXX} without closing $
        m = re.match(r'^(###\s+\w+:\s+.+)\$([^$]*\\text\{)\s*(\{#ecag-\d{4}\})\s*$', line)
        if m:
            prefix = m.group(1)
            math_fragment = m.group(2)
            anchor = m.group(3)
            # Reconstruct: close the math before the anchor
            # Remove the broken \text{ at the end
            math_fragment = re.sub(r'\\text\{$', '', math_fragment)
            line = f'{prefix}${math_fragment}$ {anchor}'

        # Fix Quotient stack heading: $[\mathbb{A}^{n}/GL_{n}\text{ {#ecag-
        # General fix: if heading has unclosed \text{ before anchor, close it
        m = re.match(r'^(###\s+\w+:\s+.*\$[^$]*)\\text\{\s*(\{#ecag-\d{4}\})\s*$', line)
        if m:
            before_text = m.group(1)
            anchor = m.group(2)
            line = f'{before_text}$ {anchor}'

        result.append(line)

    return '\n'.join(result)


def fix_percent_comments(text: str) -> str:
    """Comment out lines starting with %% (LaTeX comments that are visible in MD)."""
    lines = text.split('\n')
    result = []
    for line in lines:
        if line.strip().startswith('%%'):
            result.append(f'<!-- {line.strip()} -->')
        else:
            result.append(line)
    return '\n'.join(result)


def fix_href_math_interaction(text: str) -> str:
    """Fix cases where \\href conversion broke math expressions.

    Pattern: [$math](url) where $ is part of math, not link text.
    Convert to: $math$ ([link](url))
    """
    # Fix: [$\mathscr{E](url)xt^{i}...$ → $\mathscr{E}xt^{i}...$ [link](url)
    # This is hard to fix generically. Handle the most common pattern:
    # [text with $math](url) → text with $math$ ([source](url))
    # For now, just fix the clearly broken [$\cmd{ pattern
    # where [ opens a link but $ starts math
    text = re.sub(
        r'\[\$([^]]*)\]\(([^)]+)\)([^$]*)\$',
        lambda m: f'${m.group(1)}{m.group(3)}$ ([source]({m.group(2)}))',
        text,
    )
    return text


def normalize_blank_lines(text: str) -> str:
    """Collapse 3+ consecutive blank lines to 2."""
    return re.sub(r'\n{4,}', '\n\n\n', text)


def fix_file(filepath: str) -> int:
    """Fix a single markdown file. Returns number of changes made."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    text = original

    # Apply fixes in order
    text = fix_tikzcd_blocks(text)
    text = fix_heading_math(text)
    text = fix_percent_comments(text)
    text = fix_display_math_spacing(text)
    text = normalize_blank_lines(text)

    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        # Count approximate changes
        orig_lines = set(original.split('\n'))
        new_lines = set(text.split('\n'))
        changes = len(orig_lines.symmetric_difference(new_lines))
        return changes
    return 0


def main():
    if len(sys.argv) < 2:
        print('Usage: python fix_markdown_math.py <path>', file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isfile(path):
        changes = fix_file(path)
        print(f'{path}: {changes} line changes')
    elif os.path.isdir(path):
        total_changes = 0
        files = sorted(glob.glob(os.path.join(path, '**', '*.md'), recursive=True))
        for f in files:
            changes = fix_file(f)
            if changes > 0:
                print(f'  {f}: {changes} line changes')
                total_changes += changes
        print(f'\nFixed {len(files)} files, ~{total_changes} line changes total')
    else:
        print(f'Not found: {path}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
