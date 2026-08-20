#!/usr/bin/env python3
"""Quality Gate mechanical checker.

Runs BEFORE editorial review (see TEAM.md > Quality Gate: mechanical checklist first).
Converts the proof gate from "does it look fabricated?" to "does the evidence exist?":

FAIL (automatic revision request):
  - a cited [PROOF-NNN] ID that does not resolve to an entry in the proof library
  - a proof-shaped claim (@handle, "Quote:" line, quoted text with attribution)
    with no [PROOF-NNN] ID on the same or an adjacent line
  - a banned phrase from the optional config

WARN (itemized "verify before ship", never silently approved):
  - an outcome statistic (percent/multiplier + outcome verb) with no proof ID

Usage:
  python3 scripts/qg-check.py <draft.md> [<draft2.md> ...]
      [--library "knowledge/research/proof-library-*.md"]
      [--config context/qg-checklist.json]

Exit code: 1 if any FAIL, else 0.

Config (all keys optional): {"banned_phrases": ["..."], "library_glob": "..."}
"""

import argparse
import glob
import json
import re
import sys

CITED = re.compile(r"\[PROOF-\d{3}\]")
ANY_ID = re.compile(r"PROOF-\d{3}")
HANDLE = re.compile(r"(?<![\w.])@[A-Za-z]\w{2,}")
QUOTE_LINE = re.compile(r"^\s*>?\s*Quote:", re.IGNORECASE)
# quoted text of some substance followed by a dash attribution: "..." — Name
QUOTED_ATTRIB = re.compile(r"[\"“][^\"”]{25,}[\"”]\s*(?:—|--|-)\s*\S+")
STAT = re.compile(r"\b\d+(?:\.\d+)?(?:%|x(?!\w))")
OUTCOME = re.compile(
    r"\b(cut|reduc\w*|increas\w*|grew|grow\w*|sav\w*|boost\w*|improv\w*|doubl\w*|tripl\w*)\b",
    re.IGNORECASE,
)


def load_library_ids(pattern):
    ids = set()
    for path in glob.glob(pattern):
        with open(path, encoding="utf-8") as f:
            ids.update(ANY_ID.findall(f.read()))
    return ids


def check_file(path, library_ids, banned):
    findings = []  # (level, line_no, message, line_text)
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    def has_id_nearby(i):
        # ponytail: same-line or +/-1-line adjacency; block-level citation scopes if this proves too strict
        lo, hi = max(0, i - 1), min(len(lines), i + 2)
        return any(CITED.search(lines[j]) for j in range(lo, hi))

    for i, line in enumerate(lines):
        n = i + 1
        for m in CITED.finditer(line):
            pid = m.group(0).strip("[]")
            if pid not in library_ids:
                findings.append(("FAIL", n, f"cited {pid} does not resolve to any proof-library entry", line))
        shaped = []
        if HANDLE.search(line):
            shaped.append("@handle")
        if QUOTE_LINE.search(line):
            shaped.append("Quote: line")
        if QUOTED_ATTRIB.search(line):
            shaped.append("quoted testimonial with attribution")
        if shaped and not has_id_nearby(i):
            findings.append(("FAIL", n, f"proof-shaped claim ({', '.join(shaped)}) without a resolvable [PROOF-NNN] ID", line))
        if not shaped and STAT.search(line) and OUTCOME.search(line) and not has_id_nearby(i):
            findings.append(("WARN", n, "outcome statistic without a proof ID — verify before ship", line))
        for phrase in banned:
            if phrase.lower() in line.lower():
                findings.append(("FAIL", n, f"banned phrase: {phrase!r}", line))
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description="Quality Gate mechanical checker")
    ap.add_argument("drafts", nargs="+", help="draft file(s) to check")
    ap.add_argument("--library", default="knowledge/research/proof-library-*.md", help="glob for proof library files")
    ap.add_argument("--config", default="context/qg-checklist.json", help="optional JSON config (banned_phrases, library_glob)")
    args = ap.parse_args(argv)

    banned = []
    library_glob = args.library
    try:
        with open(args.config, encoding="utf-8") as f:
            cfg = json.load(f)
        banned = cfg.get("banned_phrases", [])
        library_glob = cfg.get("library_glob", library_glob)
    except FileNotFoundError:
        pass

    library_ids = load_library_ids(library_glob)
    if not library_ids:
        print(f"NOTE: no proof-library entries found via {library_glob!r} — every proof-shaped claim will FAIL (correct when nothing was harvested)")

    failed = False
    for path in args.drafts:
        for level, n, msg, text in check_file(path, library_ids, banned):
            print(f"{level} {path}:{n} {msg}")
            print(f"     > {text.strip()}")
            if level == "FAIL":
                failed = True
    if not failed:
        print("PASS: no FAIL findings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
