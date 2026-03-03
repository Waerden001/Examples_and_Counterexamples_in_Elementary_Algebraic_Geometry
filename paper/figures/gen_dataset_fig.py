#!/usr/bin/env python3
"""Generate 4-panel dataset distribution figure for ECAG-Bench paper (Figure 1)."""

import json
import os
from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

BENCHMARK_PATH = os.path.join(os.path.dirname(__file__), '../../benchmark/data/ecag_bench.jsonl')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'dataset_distribution.pdf')

CHAPTER_LABELS = {
    'basic_concepts': 'Basic\nConcepts',
    'cohomology': 'Cohomology',
    'computations': 'Computations',
    'moduli': 'Moduli &\nDeformation',
}
CHAPTER_ORDER = ['basic_concepts', 'computations', 'moduli', 'cohomology']

QTYPE_LABELS = {
    'example': 'Example',
    'counterexample': 'Counterexample',
    'computation': 'Computation',
    'proof': 'Proof',
}
QTYPE_ORDER = ['example', 'counterexample', 'computation', 'proof']
QTYPE_COLORS = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

DIFF_LABELS = {1: 'Level 1\n(Routine)', 2: 'Level 2\n(Non-trivial)', 3: 'Level 3\n(Deep)'}
DIFF_ORDER = [1, 2, 3]
DIFF_COLORS = ['#7fbf7f', '#ffbf7f', '#ff7f7f']

VERIF_LABELS = {'cas': 'CAS', 'exact': 'Exact', 'rubric': 'Rubric'}
VERIF_ORDER = ['cas', 'exact', 'rubric']


def load_data():
    with open(BENCHMARK_PATH) as f:
        return [json.loads(line) for line in f]


def main():
    data = load_data()
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('ECAG-Bench Dataset Distribution (N = 332)', fontsize=14, fontweight='bold', y=0.98)

    # (a) By chapter
    ax = axes[0, 0]
    chap_counts = Counter(d['chapter'] for d in data)
    chapters = CHAPTER_ORDER
    counts = [chap_counts[c] for c in chapters]
    labels = [CHAPTER_LABELS[c] for c in chapters]
    bars = ax.bar(labels, counts, color='#4C72B0', edgecolor='white', width=0.6)
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, str(count),
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_ylabel('Number of Problems')
    ax.set_title('(a) By Chapter', fontweight='bold')
    ax.set_ylim(0, max(counts) * 1.15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # (b) By difficulty
    ax = axes[0, 1]
    diff_counts = Counter(d['difficulty'] for d in data)
    diffs = DIFF_ORDER
    counts = [diff_counts[d] for d in diffs]
    labels = [DIFF_LABELS[d] for d in diffs]
    bars = ax.bar(labels, counts, color=DIFF_COLORS, edgecolor='white', width=0.5)
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, str(count),
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_ylabel('Number of Problems')
    ax.set_title('(b) By Difficulty Level', fontweight='bold')
    ax.set_ylim(0, max(counts) * 1.15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # (c) Question type by chapter (stacked bar)
    ax = axes[1, 0]
    x = np.arange(len(CHAPTER_ORDER))
    width = 0.6
    bottoms = np.zeros(len(CHAPTER_ORDER))
    for qi, qtype in enumerate(QTYPE_ORDER):
        counts = []
        for chap in CHAPTER_ORDER:
            counts.append(sum(1 for d in data if d['chapter'] == chap and d['question_type'] == qtype))
        counts = np.array(counts)
        ax.bar(x, counts, width, bottom=bottoms, label=QTYPE_LABELS[qtype],
               color=QTYPE_COLORS[qi], edgecolor='white')
        bottoms += counts
    ax.set_xticks(x)
    ax.set_xticklabels([CHAPTER_LABELS[c] for c in CHAPTER_ORDER])
    ax.set_ylabel('Number of Problems')
    ax.set_title('(c) Question Type by Chapter', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # (d) Verification strategy (pie chart)
    ax = axes[1, 1]
    verif_counts = Counter(d['verification_strategy'] for d in data)
    sizes = [verif_counts[v] for v in VERIF_ORDER]
    labels = [f"{VERIF_LABELS[v]}\n({verif_counts[v]})" for v in VERIF_ORDER]
    colors = ['#4C72B0', '#55A868', '#DD8452']
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                       colors=colors, startangle=90,
                                       textprops={'fontsize': 10})
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    ax.set_title('(d) Verification Strategy', fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight')
    print(f"Saved to {OUTPUT_PATH}")

    # Also save PNG for preview
    png_path = OUTPUT_PATH.replace('.pdf', '.png')
    plt.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"Saved to {png_path}")


if __name__ == '__main__':
    main()
