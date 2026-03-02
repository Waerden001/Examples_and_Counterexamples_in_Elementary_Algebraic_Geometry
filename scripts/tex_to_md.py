#!/usr/bin/env python3
"""
tex_to_md.py — Convert LaTeX subfiles to Markdown for the ECAG project.

Converts \begin{example/remark/...}[title]...\end{...} environments into
Markdown sections with metadata, expands custom macros, and handles basic
LaTeX structures (itemize, href, section headers, etc.).

Usage:
    python tex_to_md.py latex/Basic_concepts/commutative_algebra.tex \
           -o content/basic_concepts/commutative_algebra.md \
           --chapter basic_concepts
    python tex_to_md.py --all   # convert all .tex subfiles
"""

import re
import os
import sys
import argparse
import glob
from typing import List, Tuple

# Import sibling module
sys.path.insert(0, os.path.dirname(__file__))
from expand_macros import expand_macros


# Map source directories to chapter slugs
CHAPTER_MAP = {
    'Basic_concepts': 'basic_concepts',
    'Cohomology_and_homological_algebra': 'cohomology',
    'Computations': 'computations',
    'Moduli_problems_and_deformation_theory': 'moduli',
    'Relative': 'relative',
    'Title': 'title',
}

# Environments to extract as Markdown sections
ENVIRONMENTS = [
    'example', 'remark', 'theorem', 'lemma', 'proposition',
    'corollary', 'conjecture', 'definition', 'exercise', 'warning',
]

# Global counter for ECAG IDs
_id_counter = 0


def next_ecag_id() -> str:
    global _id_counter
    _id_counter += 1
    return f'ecag-{_id_counter:04d}'


def reset_id_counter(start: int = 0):
    global _id_counter
    _id_counter = start


def strip_preamble(text: str) -> str:
    """Remove \\documentclass, \\begin{document}, \\end{document}."""
    text = re.sub(r'\\documentclass\[.*?\]\{.*?\}\s*', '', text)
    text = re.sub(r'\\begin\{document\}\s*', '', text)
    text = re.sub(r'\\end\{document\}\s*', '', text)
    return text.strip()


def convert_sections(text: str) -> str:
    """Convert \\section, \\subsection, \\subsubsection to Markdown headings."""
    text = re.sub(r'\\section\{([^}]*)\}', r'# \1', text)
    text = re.sub(r'\\subsection\{([^}]*)\}', r'## \1', text)
    text = re.sub(r'\\subsubsection\{([^}]*)\}', r'### \1', text)
    return text


def convert_hrefs(text: str) -> str:
    """Convert \\href{url}{text} to [text](url)."""
    return re.sub(r'\\href\{([^}]*)\}\{([^}]*)\}', r'[\2](\1)', text)


def convert_textit_textbf(text: str) -> str:
    """Convert \\textit{} and \\textbf{} to Markdown."""
    text = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', text)
    text = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', text)
    text = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', text)
    return text


def convert_itemize(text: str) -> str:
    """Convert \\begin{itemize}...\\end{itemize} to Markdown lists.

    Handles nested itemize by increasing indent level.
    """
    # Simple iterative approach: process innermost itemize first
    max_iterations = 10
    for _ in range(max_iterations):
        # Find innermost itemize (one that contains no nested itemize)
        pattern = r'\\begin\{itemize\}((?:(?!\\begin\{itemize\})(?!\\end\{itemize\}).)*?)\\end\{itemize\}'
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            break
        content = match.group(1)
        # Convert \item to - with proper formatting
        lines = content.split(r'\item')
        md_lines = []
        for line in lines:
            line = line.strip()
            if line:
                md_lines.append(f'- {line}')
        replacement = '\n' + '\n'.join(md_lines) + '\n'
        text = text[:match.start()] + replacement + text[match.end():]

    # Also handle enumerate
    for _ in range(max_iterations):
        pattern = r'\\begin\{enumerate\}(?:\[.*?\])?((?:(?!\\begin\{enumerate\})(?!\\end\{enumerate\}).)*?)\\end\{enumerate\}'
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            break
        content = match.group(1)
        lines = content.split(r'\item')
        md_lines = []
        for i, line in enumerate(lines):
            line = line.strip()
            if line:
                md_lines.append(f'{i}. {line}')
        replacement = '\n' + '\n'.join(md_lines) + '\n'
        text = text[:match.start()] + replacement + text[match.end():]

    return text


def convert_labels_and_refs(text: str) -> str:
    """Remove \\label{} and convert \\ref{} to plain text."""
    text = re.sub(r'\\label\{[^}]*\}', '', text)
    text = re.sub(r'\\ref\{([^}]*)\}', r'\1', text)
    return text


def convert_includegraphics(text: str) -> str:
    """Convert \\includegraphics to Markdown image."""
    text = re.sub(
        r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}',
        r'![](\1)',
        text
    )
    return text


def flag_tikzcd(text: str) -> str:
    """Flag tikzcd environments for manual conversion."""
    text = re.sub(
        r'(\\begin\{tikzcd\}.*?\\end\{tikzcd\})',
        r'<!-- tikzcd diagram: manual conversion needed -->\n```latex\n\1\n```',
        text,
        flags=re.DOTALL,
    )
    # Also flag xy-pic diagrams
    text = re.sub(
        r'(\$\$\s*\\xymatrix.*?\$\$)',
        r'<!-- xymatrix diagram: manual conversion needed -->\n```latex\n\1\n```',
        text,
        flags=re.DOTALL,
    )
    return text


def clean_whitespace(text: str) -> str:
    """Normalize whitespace: collapse multiple blank lines to two."""
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'


def extract_environments(text: str) -> List[Tuple[str, str, str, bool]]:
    """Extract theorem-like environments from text.

    Returns list of (env_type, title, body, is_stub).
    Also returns the inter-environment text as ('text', '', content, False).
    """
    # Build regex for all environments
    env_names = '|'.join(ENVIRONMENTS)
    # Match: \begin{env}[optional title] ... \end{env}
    pattern = re.compile(
        r'\\begin\{(' + env_names + r')\}'
        r'(?:\[([^\]]*)\])?\s*'  # optional [title]
        r'(.*?)'  # body (lazy)
        r'\\end\{\1\}',
        re.DOTALL,
    )

    parts = []
    last_end = 0

    for match in pattern.finditer(text):
        # Inter-environment text
        if match.start() > last_end:
            between = text[last_end:match.start()].strip()
            if between:
                parts.append(('text', '', between, False))

        env_type = match.group(1)
        title = match.group(2) or ''
        body = match.group(3).strip()
        is_stub = len(body) == 0

        parts.append((env_type, title, body, is_stub))
        last_end = match.end()

    # Trailing text
    if last_end < len(text):
        trailing = text[last_end:].strip()
        if trailing:
            parts.append(('text', '', trailing, False))

    return parts


def env_type_label(env_type: str) -> str:
    """Human-readable label for environment type."""
    return env_type.capitalize()


def format_environment_md(env_type: str, title: str, body: str,
                          is_stub: bool, ecag_id: str) -> str:
    """Format a single environment as Markdown."""
    label = env_type_label(env_type)
    lines = []

    if title:
        lines.append(f'### {label}: {title} {{#{ecag_id}}}')
    else:
        lines.append(f'### {label} {{#{ecag_id}}}')

    lines.append('')

    if is_stub:
        lines.append('> **Status:** Stub — content needed.')
        lines.append('')
    else:
        lines.append(body)
        lines.append('')

    return '\n'.join(lines)


def convert_tex_to_md(tex_content: str, chapter: str = '',
                      source_file: str = '') -> str:
    """Full conversion pipeline: LaTeX subfile → Markdown."""
    text = tex_content

    # 1. Expand custom macros
    text = expand_macros(text)

    # 2. Strip LaTeX preamble
    text = strip_preamble(text)

    # 3. Convert sections (before environment extraction)
    text = convert_sections(text)

    # 4. Flag tikzcd/xymatrix (before general conversions)
    text = flag_tikzcd(text)

    # 5. Convert basic LaTeX structures
    text = convert_hrefs(text)
    text = convert_textit_textbf(text)
    text = convert_itemize(text)
    text = convert_labels_and_refs(text)
    text = convert_includegraphics(text)

    # 6. Remove \cite{} → [citation needed] or just the key
    text = re.sub(r'\\cite\{([^}]*)\}', r'[\\cite{\1}]', text)

    # 7. Remove stray LaTeX commands that don't translate
    text = re.sub(r'\\noindent\s*', '', text)
    text = re.sub(r'\\bigskip\s*', '\n', text)
    text = re.sub(r'\\medskip\s*', '\n', text)
    text = re.sub(r'\\smallskip\s*', '\n', text)
    text = re.sub(r'\\newpage\s*', '', text)
    text = re.sub(r'\\clearpage\s*', '', text)
    text = re.sub(r'\\vspace\{[^}]*\}\s*', '\n', text)
    text = re.sub(r'\\hspace\{[^}]*\}', ' ', text)

    # 8. Extract environments and format
    parts = extract_environments(text)

    output_lines = []
    # File header with metadata
    basename = os.path.basename(source_file).replace('.tex', '') if source_file else 'unknown'
    output_lines.append(f'---')
    output_lines.append(f'chapter: {chapter}')
    output_lines.append(f'source: {source_file}')
    output_lines.append(f'---')
    output_lines.append('')

    for env_type, title, body, is_stub in parts:
        if env_type == 'text':
            # Section headers and inter-environment text
            output_lines.append(body)
            output_lines.append('')
        else:
            ecag_id = next_ecag_id()
            md = format_environment_md(env_type, title, body, is_stub, ecag_id)
            output_lines.append(md)

    result = '\n'.join(output_lines)
    result = clean_whitespace(result)
    return result


def get_all_subfiles(latex_dir: str) -> List[Tuple[str, str, str]]:
    """Find all convertible .tex subfiles.

    Returns list of (tex_path, chapter_slug, output_path).
    Skips chapter header files (001_*) and title files.
    """
    results = []
    base = os.path.abspath(latex_dir)

    for subdir, slug in CHAPTER_MAP.items():
        if slug == 'title':
            continue  # skip title/introduction
        full_subdir = os.path.join(base, subdir)
        if not os.path.isdir(full_subdir):
            continue
        for tex_file in sorted(glob.glob(os.path.join(full_subdir, '*.tex'))):
            fname = os.path.basename(tex_file)
            if fname.startswith('001_'):
                continue  # chapter headers
            md_name = fname.replace('.tex', '.md')
            out_path = os.path.join('content', slug, md_name)
            results.append((tex_file, slug, out_path))

    return results


def main():
    parser = argparse.ArgumentParser(description='Convert LaTeX subfiles to Markdown')
    parser.add_argument('input', nargs='?', help='Input .tex file')
    parser.add_argument('-o', '--output', help='Output .md file (stdout if omitted)')
    parser.add_argument('--chapter', default='', help='Chapter slug for metadata')
    parser.add_argument('--all', action='store_true',
                        help='Convert all subfiles from latex/ to content/')
    parser.add_argument('--latex-dir', default='latex',
                        help='Path to latex/ directory (default: latex)')
    parser.add_argument('--start-id', type=int, default=0,
                        help='Starting ECAG ID counter (default: 0)')
    args = parser.parse_args()

    reset_id_counter(args.start_id)

    if args.all:
        files = get_all_subfiles(args.latex_dir)
        if not files:
            print('No subfiles found. Check --latex-dir path.', file=sys.stderr)
            sys.exit(1)

        total_examples = 0
        for tex_path, chapter, out_path in files:
            with open(tex_path, 'r', encoding='utf-8') as f:
                tex_content = f.read()

            md_content = convert_tex_to_md(tex_content, chapter, tex_path)

            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            # Count examples/remarks in output
            n = md_content.count('### Example:') + md_content.count('### Remark:')
            total_examples += n
            print(f'  {out_path} ({n} items)')

        print(f'\nConverted {len(files)} files, {total_examples} items total.')
        print(f'Last ECAG ID: ecag-{_id_counter:04d}')
        return

    if not args.input:
        parser.error('Either provide an input file or use --all')

    with open(args.input, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    chapter = args.chapter
    if not chapter:
        # Try to infer from path
        parts = args.input.replace('\\', '/').split('/')
        for p in parts:
            if p in CHAPTER_MAP:
                chapter = CHAPTER_MAP[p]
                break

    md_content = convert_tex_to_md(tex_content, chapter, args.input)

    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f'Written to {args.output}')
    else:
        sys.stdout.write(md_content)


if __name__ == '__main__':
    main()
