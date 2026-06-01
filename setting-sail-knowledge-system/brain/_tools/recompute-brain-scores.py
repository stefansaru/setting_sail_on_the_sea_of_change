#!/usr/bin/env python3
"""Recompute Brain concept scores from each page's `supported_by:` list and
regenerate the leaderboard table in brain/maps/brain-index.md.

Source of truth = the `supported_by:` YAML list in every brain/concepts/*.md.
    score = number of distinct sources in supported_by.

Usage:  python recompute-brain-scores.py [--write]
        (without --write: dry-run, prints the table; with --write: updates files)
"""
import re, glob, os, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../brain
CONCEPTS = os.path.join(ROOT, "concepts")
INDEX = os.path.join(ROOT, "maps", "brain-index.md")
WRITE = "--write" in sys.argv

def parse_list(block, key):
    # supports `key: [a, b]` and YAML block lists under `key:`
    m = re.search(rf"^{key}:\s*\[(.*?)\]", block, re.M)
    if m:
        return [x.strip().strip('"\'') for x in m.group(1).split(",") if x.strip()]
    items, capture = [], False
    for line in block.splitlines():
        if re.match(rf"^{key}:\s*$", line):
            capture = True; continue
        if capture:
            mm = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if mm: items.append(mm.group(1).strip().strip('"\''))
            elif line and not line.startswith(" "): break
    return items

rows, books = [], set()
for f in sorted(glob.glob(os.path.join(CONCEPTS, "*.md"))):
    txt = open(f, encoding="utf-8").read()
    fm = txt.split("---", 2)
    if len(fm) < 3:  # no frontmatter
        continue
    block = fm[1]
    cid = (re.search(r"^id:\s*(\S+)", block, re.M) or [None, os.path.basename(f)[:-3]])[1]
    supported = parse_list(block, "supported_by")
    score = len(set(supported))
    books.update(supported)
    rows.append((score, cid, supported, f, txt, block))

rows.sort(key=lambda r: (-r[0], r[1]))

# --- rewrite each page's `score:` to match (if --write) ---
updated = 0
for score, cid, supported, f, txt, block in rows:
    new_block = re.sub(r"^score:\s*\d+\s*$", f"score: {score}", block, flags=re.M)
    if new_block != block:
        if WRITE:
            open(f, "w", encoding="utf-8").write(txt.replace(block, new_block, 1))
        updated += 1

# --- regenerate leaderboard table ---
lines = ["| Score | Concept | Supported by |", "|------:|---------|--------------|"]
for score, cid, supported, *_ in rows:
    lines.append(f"| {score} | [[{cid}]] | {', '.join(supported) or '—'} |")
table = "\n".join(lines)
books_line = f"**Books ingested:** {len(books)} — " + ", ".join(f"`{b}`" for b in sorted(books)) + "."

print(f"{len(rows)} concepts | {len(books)} sources | {updated} score field(s) "
      f"{'updated' if WRITE else 'would change (dry-run)'}\n")
print(table); print(); print(books_line)

if WRITE and os.path.exists(INDEX):
    doc = open(INDEX, encoding="utf-8").read()
    doc = re.sub(r"## Leaderboard\n\|.*?\n(?:\|.*\n)+",
                 "## Leaderboard\n" + table + "\n", doc, flags=re.S)
    doc = re.sub(r"\*\*Books ingested:\*\*.*", books_line, doc)
    open(INDEX, "w", encoding="utf-8").write(doc)
    print(f"\nregenerated {INDEX}")
