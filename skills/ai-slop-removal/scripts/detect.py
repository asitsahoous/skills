#!/usr/bin/env python3
"""
Flag candidate AI-slop patterns in a text file.

This finds what greps find reliably. It does not make judgment calls, and it
cannot see the patterns that matter most -- fake depth, generated lists, and
missing concrete detail. Treat every hit as a candidate to inspect, not a
verdict. Read references/patterns.md and do the judgment pass by hand.

Usage:
    python detect.py draft.md
    python detect.py draft.md --category rhetorical
    python detect.py draft.md --quiet          # counts only
"""

import argparse
import pathlib
import re
import sys
from collections import defaultdict

# (label, regex, category, note)
CHECKS = [
    ("em dash", r"—", "lexical",
     "One per document reads as style; ten is a signature."),

    ("empty superlative", r"\b(groundbreaking|transformative|revolutionar(y|ise|ize)|"
     r"game[- ]chang(ing|er)|cutting[- ]edge|next[- ]generation|seamless|"
     r"unparalleled|unprecedented)\b", "lexical",
     "Replace the adjective with the fact behind it."),

    ("corporate buzzword", r"\b(leverag(e|ing|ed)|empower(s|ing|ed)?|unlock(s|ing|ed)?|"
     r"harness(es|ing|ed)?|streamlin(e|es|ing|ed)|robust|holistic|"
     r"best[- ]in[- ]class|mission[- ]critical|synerg(y|ies|istic))\b", "lexical",
     "Most have a plain equivalent."),

    ("weightless intensifier", r"\b(genuinely|actually|truly|really|simply|essentially|"
     r"fundamentally|importantly|notably)\b", "lexical",
     "Delete. If the sentence weakens, it was weak."),

    ("hedge stack", r"\b(arguably|somewhat|potentially|relatively|fairly)\b", "lexical",
     "One hedge, or state the uncertainty concretely."),

    ("agentless assertion", r"\b(it is (widely |often |generally )?(regarded|believed|said|"
     r"considered|acknowledged)|many experts|studies show|research suggests)\b", "lexical",
     "Name who, or drop the claim."),

    ("transition opener", r"(?mi)^\s*(furthermore|moreover|additionally|however|"
     r"ultimately|in conclusion|that said|nevertheless)\b", "lexical",
     "Human writing jumps. 'but' and 'so' usually suffice."),

    ("symmetric construction", r"(?i)(it'?s not (about|just) .{1,60}?[,.]?\s*it'?s (about|that)|"
     r"(this|that|it) is not .{1,50}?\.\s+(it|this|that) is )", "rhetorical",
     "State the positive claim directly."),

    ("negation pivot", r"(?i)\b(not|isn'?t|aren'?t|doesn'?t|won'?t) (a |an |the )?"
     r"\w+[,.]? (it|they|that|this) (is|are|was|were) ", "rhetorical",
     "The 'not X, it is Y' shape. Check whether the negation earns its place."),

    ("we don't need / we need", r"(?i)we (don'?t|do not) need .{1,60}\.\s*we need", "rhetorical",
     "Classic symmetric pair."),

    ("signposting", r"(?i)(here'?s the thing|that'?s the whole point|that'?s what makes|"
     r"and that'?s (exactly )?why|the (real|actual) (question|point|issue) is)", "rhetorical",
     "Delete. If the point lands, it lands unannounced."),

    ("fake novelty", r"(?i)(nobody (talks about|tells you)|here'?s the secret|"
     r"most people don'?t (know|realis|realiz)|what (nobody|no one) tells)", "rhetorical",
     "Usually followed by something everyone knows."),

    ("rule of three", r"\b\w+, \w+,? and \w+\.", "rhetorical",
     "Count these. More than one or two per page is a tell."),

    ("generic opener", r"(?mi)^\s*(in today'?s|in an era|in a world|as (we|the world) "
     r"(move|continue)|artificial intelligence is transform)", "structural",
     "Start at the actual observation."),

    ("universal conclusion", r"(?i)(the future is (bright|exciting)|this is only the beginning|"
     r"we'?re just getting started|only time will tell|the possibilities are endless)",
     "structural", "End on the last real point."),

    ("closing question", r"(?mi)^\s*(thoughts\?|what do you think\?|"
     r"would love (to hear |your )|let me know (what you think|if you)|"
     r"(want|would you like) me to )", "conversational",
     "Ask a real question or end."),

    ("sycophantic opener", r"(?mi)^\s*(great|excellent|fantastic|good) (question|point|catch)\b",
     "conversational", "Just answer."),

    ("narrating", r"(?i)(let me (break|walk|dive|unpack|explain)|"
     r"i'?ll (walk|break|guide) you through|let'?s dive (in|into))", "conversational",
     "Do the thing instead of announcing it."),

    ("fake personal story", r"(?i)(i recently realis|i recently realiz|i couldn'?t stop thinking|"
     r"i had an interesting conversation|it got me thinking)", "conversational",
     "Include the specifics, or cut the frame."),
]

CATEGORIES = ("structural", "lexical", "rhetorical", "conversational")


def find_fragments(lines):
    """Standalone very short paragraphs -- fragment-for-drama candidates."""
    hits = []
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if not s or s.startswith(("#", "-", "*", ">", "|", "```")):
            continue
        prev = lines[i - 2].strip() if i >= 2 else ""
        nxt = lines[i].strip() if i < len(lines) else ""
        words = len(s.split())
        if words <= 5 and s.endswith(".") and not prev and not nxt:
            hits.append((i, s))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--category", choices=CATEGORIES)
    ap.add_argument("--quiet", action="store_true", help="counts only")
    args = ap.parse_args()

    p = pathlib.Path(args.path)
    if not p.exists():
        sys.exit(f"no such file: {p}")

    text = p.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    words = len(text.split())

    by_cat = defaultdict(list)

    seen = set()
    for label, pattern, cat, note in CHECKS:
        if args.category and cat != args.category:
            continue
        flags = 0 if pattern.startswith("(?") else re.IGNORECASE
        for m in re.finditer(pattern, text, flags):
            # A match may open with leading whitespace or a newline (the ^\s*
            # patterns). Anchor the line number to the first real character.
            start = m.start()
            while start < m.end() and text[start].isspace():
                start += 1
            line_no = text[:start].count("\n") + 1
            key = (label, line_no, m.group(0).strip().lower())
            if key in seen:
                continue
            seen.add(key)
            snippet = lines[line_no - 1].strip() if line_no <= len(lines) else ""
            if len(snippet) > 110:
                snippet = snippet[:107] + "..."
            by_cat[cat].append((label, line_no, snippet, note))

    if not args.category or args.category == "rhetorical":
        for line_no, snippet in find_fragments(lines):
            by_cat["rhetorical"].append(
                ("fragment for drama", line_no, snippet,
                 "Fold into the paragraph unless it is the pivot of the argument."))

    total = sum(len(v) for v in by_cat.values())

    print(f"{p.name}: {words} words, {total} candidate flags")
    if words:
        print(f"density: {total / words * 1000:.1f} per 1,000 words")
    print()

    if not total:
        print("No mechanical hits. The patterns that matter most are not greppable:")
        print("fake depth, generated lists, missing concrete detail, aphoristic")
        print("closers. Read references/patterns.md and do the judgment pass.")
        return

    if args.quiet:
        counts = defaultdict(int)
        for cat, hits in by_cat.items():
            for label, *_ in hits:
                counts[label] += 1
        for label, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"{n:>4}  {label}")
        return

    for cat in CATEGORIES:
        hits = by_cat.get(cat)
        if not hits:
            continue
        print(f"--- {cat} ({len(hits)}) ---")
        seen_notes = set()
        for label, line_no, snippet, note in sorted(hits, key=lambda h: h[1]):
            print(f"  L{line_no:<5} [{label}]  {snippet}")
            if label not in seen_notes:
                print(f"         -> {note}")
                seen_notes.add(label)
        print()

    print("These are candidates, not verdicts. Judge each one, then read")
    print("references/patterns.md for the patterns no grep can find.")


if __name__ == "__main__":
    main()
