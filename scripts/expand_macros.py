#!/usr/bin/env python3
"""
expand_macros.py — Expand custom LaTeX macros from mystyle.sty to standard LaTeX.

Usage:
    python expand_macros.py < input.tex > output.tex
    python expand_macros.py input.tex [-o output.tex]
    python expand_macros.py --test   # run self-tests
"""

import re
import sys
import argparse
from typing import Optional, Tuple, List


def find_brace_group(text: str, start: int) -> Optional[Tuple[int, int]]:
    """Find a matched {…} group starting at position `start`.

    Returns (content_start, end) where text[start] == '{' and text[end-1] == '}'.
    Returns None if no brace group starts at `start`.
    """
    if start >= len(text) or text[start] != '{':
        return None
    depth = 0
    for i in range(start, len(text)):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return (start + 1, i + 1)
    return None


def build_macro_table() -> List[Tuple[str, str, int]]:
    """Return a list of (pattern_name, replacement, num_args).

    Sorted by descending pattern length to avoid partial matches
    (e.g. \cA before \c, \RR before \R, \Spec before \Sp).
    """
    macros = []

    # --- 0-arg macros: \name → replacement ---

    # Boldface number fields/spaces
    zero_arg = {
        r'\A': r'\mathbf{A}',
        r'\P': r'\mathbf{P}',
        r'\RR': r'\mathbf{R}',
        r'\C': r'\mathbf{C}',
        r'\Q': r'\mathbf{Q}',
        r'\Z': r'\mathbf{Z}',
        r'\H': r'\mathrm{H}',
        r'\HH': r'\mathbf{H}',
        r'\R': r'\mathbf{R}',
        r'\PS': r'\mathbf{P}',
        r'\dR': r'\mathbf{R}',
        # Calligraphic sheaves
        r'\E': r'\mathcal{E}',
        r'\F': r'\mathcal{F}',
        r'\G': r'\mathcal{G}',
        r'\I': r'\mathcal{I}',
        r'\L': r'\mathcal{L}',
        r'\M': r'\mathcal{M}',
        r'\O': r'\mathcal{O}',
        r'\S': r'\mathcal{S}',
        # Mathscr alphabet
        **{f'\\c{c}': f'\\mathscr{{{c}}}' for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'},
        # Names
        r'\Poincare': r"Poincar\'{e} ",
        r'\Etale': r"\'{E}tale ",
        r'\etale': r"\'{e}tale ",
        r'\Cech': r'\v{C}ech ',
        # Misc 0-arg
        r'\ext': r'\mathrm{Ext}',
        r'\bu': r'\bullet',
        r'\co': r'\colon',
        r'\card': r'\#',
        r'\ft': r'{}^{\sigma}',
        r'\sgn': r'\operatorname{sgn}',
        r'\frob': r'\operatorname{Frob}',
    }
    for name, repl in zero_arg.items():
        macros.append((name, repl, 0))

    # \nm has an embedded \Q that itself needs expansion; expand inline
    macros.append((r'\nm', r'\operatorname{N}_{K/\mathbf{Q}}', 0))
    macros.append((r'\proSS', r'\mathrm{pro}-\mathcal{S}', 0))

    # --- 1-arg macros: \name{arg} → replacement with #1 ---
    one_arg = {
        r'\ol': r'\overline{#1}',
        r'\cl': r'\overline{#1}',
        r'\ul': r'\underline{#1}',
        r'\wh': r'\widehat{#1}',
        r'\wt': r'\widetilde{#1}',
        r'\mf': r'\mathfrak{#1}',
        r'\mrm': r'\mathrm{#1}',
        r'\mbb': r'\mathbf{#1}',
        r'\mbf': r'\mathbf{#1}',
        r'\Cal': r'\mathcal{#1}',
        r'\cal': r'\mathcal{#1}',
        r'\newpar': r'\noindent\textbf{#1}',
    }
    for name, repl in one_arg.items():
        macros.append((name, repl, 1))

    # --- 2-arg macros ---
    two_arg = {
        r'\leg': r'\left(\frac{#1}{#2}\right)',
        r'\pderiv': r'\frac{\partial #1}{\partial #2}',
        r'\rmono': r'\underset{#2}{\stackrel{#1}{\hookrightarrow}}',
        r'\lmono': r'\underset{#2}{\stackrel{#1}{\hookleftarrow}}',
        r'\rrat': r'\underset{#2}{\stackrel{#1}{\dashrightarrow}}',
        r'\lrat': r'\underset{#2}{\stackrel{#1}{\dashleftarrow}}',
    }
    for name, repl in two_arg.items():
        macros.append((name, repl, 2))

    # --- 4-arg macro ---
    macros.append((r'\pmat', r'\begin{pmatrix}#1 & #2 \\ #3 & #4\end{pmatrix}', 4))

    # --- DeclareMathOperator: \Name → \operatorname{Text} ---
    # These are 0-arg. Keep the operator text exactly as defined.
    operators = {
        r'\Hilb': 'Hilb', r'\Ad': 'Ad', r'\Art': 'Art', r'\Aut': 'Aut',
        r'\Br': 'Br', r'\Bun': 'Bun', r'\Dec': 'Dec', r'\Div': 'Div',
        r'\Enc': 'Enc', r'\End': 'End',
        r'\Et': r"\acute{E}t",
        r'\Ext': 'Ext', r'\Fib': 'Fib', r'\Fix': 'Fix',
        r'\Frac': 'Frac', r'\Frob': 'Frob', r'\GL': 'GL', r'\Gr': 'Gr',
        r'\Hck': 'Hck', r'\Hom': 'Hom', r'\Id': 'Id',
        r'\Ima': r'Im\,',
        r'\Ind': 'Ind', r'\Inn': 'Inn', r'\Isom': 'Isom',
        r'\Jac': 'Jac', r'\Jet': 'Jet', r'\Lat': 'Lat', r'\Lie': 'Lie',
        r'\MaxSpec': 'MaxSpec', r'\Nm': 'Nm',
        r'\N': r'\mathbf{N}',
        r'\Or': 'O', r'\Out': 'Out', r'\PGL': 'PGL', r'\Pic': 'Pic',
        r'\Proj': r'Proj\,',
        r'\Quot': 'Quot', r'\Rep': 'Rep', r'\Res': 'Res',
        r'\SL': 'SL', r'\SO': 'SO', r'\Shtuka': 'Shtuka', r'\Sht': 'Sht',
        r'\Span': 'Span',
        r'\Spec': r'Spec\,',
        r'\Sp': 'Sp', r'\Sq': 'Sq', r'\Stab': 'Stab', r'\Sym': 'Sym',
        r'\TO': 'TO', r'\Tr': 'Tr', r'\Ver': 'Ver',
        r'\ab': 'ab', r'\ad': 'ad',
        r'\bfet': r"\textbf{f\'{e}t}",
        r'\ch': r'ch\,',
        r'\cla': 'cl', r'\codim': 'codim', r'\coker': 'coker',
        r'\cusp': 'cusp', r'\cyc': 'cyc', r'\dom': 'dom',
        r'\et': r"\acute{e}t",
        r'\even': 'even',
        r'\hEt': r'\hat{Et}',
        r'\inv': 'inv', r'\length': 'length', r'\nd': 'nd',
        r'\odd': 'odd', r'\ord': 'ord', r'\pr': 'pr', r'\pt': 'pt',
        r'\rad': 'rad', r'\rank': 'rank', r'\red': 'red',
        r'\tors': 'tors', r'\unr': 'unr',
        r'\Cl': 'Cl', r'\Gal': 'Gal', r'\Mat': 'Mat',
        r'\tr': r'tr',
        r'\vac': r'|vac\rangle',
    }
    for name, text in operators.items():
        # \N and a few others have special replacement (not \operatorname)
        if name == r'\N':
            macros.append((name, r'\mathbf{N}', 0))
        else:
            macros.append((name, f'\\operatorname{{{text}}}', 0))

    # Sort by descending name length to avoid partial matches
    macros.sort(key=lambda x: -len(x[0]))

    return macros


# Build once at module level
MACRO_TABLE = build_macro_table()


def strip_editorial_comments(text: str) -> str:
    """Remove \\shuai{...} and \\reword{...} blocks entirely."""
    result = text
    for cmd in (r'\shuai', r'\reword'):
        while True:
            idx = result.find(cmd)
            if idx == -1:
                break
            # Find the brace group after the command name
            brace_start = idx + len(cmd)
            # Skip optional whitespace between command and {
            while brace_start < len(result) and result[brace_start] in ' \t\n':
                brace_start += 1
            group = find_brace_group(result, brace_start)
            if group:
                _, end = group
                result = result[:idx] + result[end:]
            else:
                # Malformed, just remove the command name
                result = result[:idx] + result[idx + len(cmd):]
    return result


def expand_single_macro(text: str, name: str, replacement: str, num_args: int) -> str:
    """Expand all occurrences of a single macro in text."""
    result = []
    i = 0
    name_len = len(name)

    while i < len(text):
        # Check if we're at an occurrence of this macro
        if text[i:i + name_len] == name:
            # Verify word boundary: the character after the macro name
            # must not be a letter (to avoid \Spec matching inside \Special)
            after = i + name_len
            if after < len(text) and text[after].isalpha():
                result.append(text[i])
                i += 1
                continue

            if num_args == 0:
                result.append(replacement)
                i += name_len
            else:
                # Collect arguments
                pos = after
                args = []
                success = True
                for _ in range(num_args):
                    # Skip whitespace
                    while pos < len(text) and text[pos] in ' \t\n':
                        pos += 1
                    group = find_brace_group(text, pos)
                    if group is None:
                        success = False
                        break
                    content_start, end = group
                    args.append(text[content_start:end - 1])
                    pos = end

                if success:
                    expanded = replacement
                    for j, arg in enumerate(args, 1):
                        expanded = expanded.replace(f'#{j}', arg)
                    result.append(expanded)
                    i = pos
                else:
                    # Could not find all args, leave as-is
                    result.append(text[i])
                    i += 1
        else:
            result.append(text[i])
            i += 1

    return ''.join(result)


def expand_macros(text: str) -> str:
    """Expand all custom macros in text to standard LaTeX."""
    # First strip editorial comments
    text = strip_editorial_comments(text)

    # Apply each macro expansion (sorted by descending name length)
    for name, replacement, num_args in MACRO_TABLE:
        if name in text:  # fast pre-check
            text = expand_single_macro(text, name, replacement, num_args)

    return text


def run_tests():
    """Self-test suite for macro expansion."""
    tests = [
        # 0-arg: boldface
        (r'$\A^n_k$', r'$\mathbf{A}^n_k$'),
        (r'$\P^1$', r'$\mathbf{P}^1$'),
        (r'$\C$', r'$\mathbf{C}$'),
        (r'$\Q$', r'$\mathbf{Q}$'),
        (r'$\Z$', r'$\mathbf{Z}$'),
        (r'$\RR$', r'$\mathbf{R}$'),
        # 0-arg: calligraphic
        (r'$\O_X$', r'$\mathcal{O}_X$'),
        (r'$\F$', r'$\mathcal{F}$'),
        (r'$\L$', r'$\mathcal{L}$'),
        # 0-arg: mathscr
        (r'$\cA$', r'$\mathscr{A}$'),
        (r'$\cM$', r'$\mathscr{M}$'),
        (r'$\cZ$', r'$\mathscr{Z}$'),
        # 0-arg: operators
        (r'$\Spec(R)$', r'$\operatorname{Spec\,}(R)$'),
        (r'$\Proj(S)$', r'$\operatorname{Proj\,}(S)$'),
        (r'$\Pic(X)$', r'$\operatorname{Pic}(X)$'),
        (r'$\Hom(A,B)$', r'$\operatorname{Hom}(A,B)$'),
        (r'$\Ext^1$', r'$\operatorname{Ext}^1$'),
        (r'$\GL_n$', r'$\operatorname{GL}_n$'),
        # Word boundary: \Spec should not match \Special
        (r'$\Special$', r'$\Special$'),
        # 1-arg
        (r'$\ol{X}$', r'$\overline{X}$'),
        (r'$\wt{X}$', r'$\widetilde{X}$'),
        (r'$\wh{X}$', r'$\widehat{X}$'),
        (r'$\mf{p}$', r'$\mathfrak{p}$'),
        (r'$\mrm{H}$', r'$\mathrm{H}$'),
        # 2-arg
        (r'$\pderiv{f}{x}$', r'$\frac{\partial f}{\partial x}$'),
        (r'$\leg{a}{p}$', r'$\left(\frac{a}{p}\right)$'),
        # 4-arg
        (r'$\pmat{a}{b}{c}{d}$', r'$\begin{pmatrix}a & b \\ c & d\end{pmatrix}$'),
        # Editorial comment stripping
        (r'text \shuai{some note} more', r'text  more'),
        (r'text \reword{fix this} more', r'text  more'),
        # Names
        (r'\Poincare duality', r"Poincar\'{e}  duality"),
        # Nested: \ol with content containing other macros
        (r'$\ol{\A^1}$', r'$\overline{\mathbf{A}^1}$'),
        # Don't expand inside longer names: \codim should not be eaten by \co
        (r'$\codim(X)$', r'$\operatorname{codim}(X)$'),
        # \Sht vs \Shtuka ordering
        (r'$\Shtuka$', r'$\operatorname{Shtuka}$'),
        (r'$\Sht$', r'$\operatorname{Sht}$'),
    ]

    passed = 0
    failed = 0
    for input_text, expected in tests:
        result = expand_macros(input_text)
        if result == expected:
            passed += 1
        else:
            failed += 1
            print(f'FAIL: {input_text!r}')
            print(f'  expected: {expected!r}')
            print(f'  got:      {result!r}')

    print(f'\n{passed} passed, {failed} failed out of {passed + failed} tests')
    return failed == 0


def main():
    parser = argparse.ArgumentParser(description='Expand custom LaTeX macros to standard LaTeX')
    parser.add_argument('input', nargs='?', help='Input .tex file (stdin if omitted)')
    parser.add_argument('-o', '--output', help='Output file (stdout if omitted)')
    parser.add_argument('--test', action='store_true', help='Run self-tests')
    args = parser.parse_args()

    if args.test:
        success = run_tests()
        sys.exit(0 if success else 1)

    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    result = expand_macros(text)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
