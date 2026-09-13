#!/usr/bin/env python3
"""Quality Gate mechanical checker — one program for every deployment (unified 2026-09-12).

Runs BEFORE editorial review (TEAM.md > Quality Gate: mechanical checklist first). Model-based
holistic quality judging measured coin-flip-unreliable on the local stack; these checks are not.

Checks (tag in output):
  [proof]    FAIL  a cited [PROOF-NNN] ID that does not resolve to a proof-library entry
             FAIL  a proof-shaped claim — @handle, "Quote:"/"Testimonial:" line, quoted text with
                   a dash attribution, or a "— *Name, role*" attribution — with neither a
                   resolvable [PROOF-NNN] ID (same or adjacent line) nor an explicit
                   `[PROOF NEEDED: ...]` marker. The marker is the honest unsourced state;
                   inventing plausible proof is the one unrecoverable failure in this team.
             WARN  an outcome statistic with no ID and no marker — "verify before ship"
  [banned]   FAIL  a banned phrase: built-in AI tells + config banned_phrases / banned_extra
  [hardware] WARN  a physical effect that needs a bench check (config hardware_patterns /
                   hardware_extra; empty by default)
  [dates]    FAIL  a weekday name that disagrees with the calendar, an impossible date, or a
                   dated line outside its "Week N (Mon D - Mon D)" header range

Usage:
  python3 scripts/qg-check.py <draft.md> [<draft2.md> ...] [--library GLOB] [--config PATH]

Config (JSON, all keys optional). Searched in order when --config is not given:
  context/qg-checklist.json, then ~/marketing/context/qg-checklist.json (Hermes deployments).
  {"library_glob": "knowledge/research/proof-library-*.md",
   "banned_phrases": ["..."],            # plain substrings, case-insensitive
   "banned_extra": ["regex", ...],        # regexes appended to the built-in AI-tell list
   "hardware_patterns": ["regex", ...],  # or "hardware_extra" — same thing
   "campaign_year": 2026}                # calendar year for [dates]; default: this year

Exit code: 1 if any FAIL, else 0. Module API kept stable for wrappers (qg-langfuse.py):
  load_overrides(config_path=None) then check_file(path) -> [(level, path, line, tag, msg)].
"""

import argparse
import datetime
import glob
import json
import pathlib
import re
import sys

# ── proof ──────────────────────────────────────────────────────────────────────
CITED = re.compile(r"\[PROOF-\d{3}\]")
ANY_ID = re.compile(r"PROOF-\d{3}")
MARKER = re.compile(r"\[PROOF NEEDED", re.I)
HANDLE = re.compile(r"(?<![\w.])@[A-Za-z]\w{2,}")
QUOTE_LINE = re.compile(r"^\s*>?\s*[-*]?\s*\*{0,2}(\w+\s+){0,3}(quote|testimonial|review)s?\*{0,2}\s*:", re.I)
QUOTED_ATTRIB = re.compile(r"[\"“][^\"”]{25,}[\"”]\s*(?:—|--|-)\s*\S+")
NAMED_ATTRIB = re.compile(r"[—–-]\s*\*[A-Z][\w.]*(\s[A-Z][\w.]*)?,\s[a-z][^*\n]{3,40}\*")  # — *Sarah K., hobbyist*
STAT = re.compile(r"\b\d+(?:\.\d+)?(?:%|x(?!\w))")
OUTCOME_VERB = re.compile(
    r"\b(cut|reduc\w*|increas\w*|grew|grow\w*|sav\w*|boost\w*|improv\w*|doubl\w*|tripl\w*)\b", re.I)
OUTCOME_NOUN = re.compile(
    r"\d[\d,.]*\s*%?\s*(custom\s+)?(orders?|customers?|sales|revenue|followers|retention|conversions?|clients?)\b", re.I)

# ── banned (AI tells; config adds project phrases) ─────────────────────────────
DEFAULT_BANNED = [
    r"\bdelve\b", r"\btapestry\b", r"\btestament to\b", r"\bcrucial\b", r"\bparamount\b",
    r"\bleverag(e|ing)\b", r"\bin conclusion\b", r"\bgame.changer\b", r"\bseamless(ly)?\b",
    r"\bunleash", r"(is|it'?s)\s+not just\b.*\b(it'?s|but)\b",
    r"\bthe\s+\w+\s+landscape\b",  # the metaphor, not the art subject
]

# ── dates ──────────────────────────────────────────────────────────────────────
DATE_RE = re.compile(r"\b(Mon|Tue|Tues|Wed|Thu|Thur|Thurs|Fri|Sat|Sun)[a-z]*,?\s+"
                     r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(\d{1,2})", re.I)
WEEK_HEADER = re.compile(
    r"Week\s+\d+\s*\(\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(\d{1,2})\s*"
    r"[-–]\s*(?:(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+)?(\d{1,2})", re.I)
WEEKDAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}

CONFIG_SEARCH = ["context/qg-checklist.json", str(pathlib.Path.home() / "marketing/context/qg-checklist.json")]
CFG = {"library_glob": "knowledge/research/proof-library-*.md", "banned_phrases": [], "banned_regex": [],
       "hardware": [], "year": datetime.date.today().year}
_LIBRARY = None  # lazily loaded set of PROOF-NNN ids


def load_overrides(config_path=None):
    """Load config (explicit path, else the first existing CONFIG_SEARCH entry). Missing = defaults."""
    global _LIBRARY
    candidates = [config_path] if config_path else CONFIG_SEARCH
    for c in candidates:
        if c and pathlib.Path(c).exists():
            try:
                d = json.loads(pathlib.Path(c).read_text(encoding="utf-8"))
            except Exception as e:
                print(f"WARN {c}: unreadable config ({e}); using defaults")
                break
            CFG["library_glob"] = d.get("library_glob", CFG["library_glob"])
            CFG["banned_phrases"] = list(d.get("banned_phrases", []))
            CFG["banned_regex"] = list(d.get("banned_extra", []))
            CFG["hardware"] = list(d.get("hardware_patterns", [])) + list(d.get("hardware_extra", []))
            CFG["year"] = int(d.get("campaign_year", CFG["year"]))
            break
    _LIBRARY = None
    return CFG


def library_ids():
    global _LIBRARY
    if _LIBRARY is None:
        ids = set()
        for path in glob.glob(str(pathlib.Path(CFG["library_glob"]).expanduser())):
            ids.update(ANY_ID.findall(pathlib.Path(path).read_text(encoding="utf-8", errors="replace")))
        _LIBRARY = ids
    return _LIBRARY


def check_file(path, ids=None):
    """Return findings as (level, path, line_no, tag, message). `ids` overrides the library set."""
    findings = []
    try:
        lines = pathlib.Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as e:
        return [("FAIL", path, 0, "io", str(e))]
    ids = library_ids() if ids is None else ids
    banned_rx = [re.compile(b, re.I) for b in DEFAULT_BANNED + CFG["banned_regex"]]
    hardware_rx = [re.compile(h, re.I) for h in CFG["hardware"]]
    year = CFG["year"]
    week_range = None

    def sourced(i):
        # ponytail: same-line or +/-1-line adjacency for IDs; block-level scopes if too strict
        lo, hi = max(0, i - 1), min(len(lines), i + 2)
        return MARKER.search(lines[i]) or any(CITED.search(lines[j]) for j in range(lo, hi))

    for i, line in enumerate(lines):
        n = i + 1
        # [proof]
        for m in CITED.finditer(line):
            pid = m.group(0).strip("[]")
            if pid not in ids:
                findings.append(("FAIL", path, n, "proof", f"cited {pid} does not resolve to any proof-library entry"))
        shaped = []
        if HANDLE.search(line):
            shaped.append("@handle")
        if QUOTE_LINE.search(line):
            shaped.append("Quote: line")
        if QUOTED_ATTRIB.search(line):
            shaped.append("quoted testimonial with attribution")
        if NAMED_ATTRIB.search(line):
            shaped.append("named-person attribution")
        if shaped and not sourced(i):
            findings.append(("FAIL", path, n, "proof",
                             f"proof-shaped claim ({', '.join(shaped)}) without a resolvable [PROOF-NNN] ID or a [PROOF NEEDED] marker"))
        elif not shaped and not sourced(i) and (
                (STAT.search(line) and OUTCOME_VERB.search(line)) or OUTCOME_NOUN.search(line)):
            findings.append(("WARN", path, n, "proof", "outcome statistic without a proof ID — verify before ship"))
        # [banned]
        for phrase in CFG["banned_phrases"]:
            if phrase.lower() in line.lower():
                findings.append(("FAIL", path, n, "banned", f"banned phrase: {phrase!r}"))
        for rx in banned_rx:
            m = rx.search(line)
            if m:
                findings.append(("FAIL", path, n, "banned", f"banned phrase: {m.group(0)!r}"))
        # [hardware]
        for rx in hardware_rx:
            m = rx.search(line)
            if m:
                findings.append(("WARN", path, n, "hardware", f"verify on the bench before committing: {m.group(0)!r}"))
        # [dates]
        hm = WEEK_HEADER.search(line)
        if hm:
            m1, d1, m2, d2 = hm.group(1), int(hm.group(2)), hm.group(3), int(hm.group(4))
            try:
                week_range = (datetime.date(year, MONTHS[m1.lower()[:3]], d1),
                              datetime.date(year, MONTHS[(m2 or m1).lower()[:3]], d2))
            except ValueError:
                findings.append(("FAIL", path, n, "dates", f"impossible week range: {hm.group(0)}"))
                week_range = None
        for m in DATE_RE.finditer(line):
            wd, mon, day = m.group(1).lower()[:3], m.group(2).lower()[:3], int(m.group(3))
            try:
                d = datetime.date(year, MONTHS[mon], day)
            except ValueError:
                findings.append(("FAIL", path, n, "dates", f"impossible date: {m.group(0)}"))
                continue
            if WEEKDAYS[d.weekday()] != wd:
                findings.append(("FAIL", path, n, "dates",
                                 f"{m.group(0)} is wrong — {mon.title()} {day} {year} is a {WEEKDAYS[d.weekday()].title()}"))
            if week_range and not (week_range[0] <= d <= week_range[1]):
                findings.append(("FAIL", path, n, "dates",
                                 f"{m.group(0)} falls outside its week header range {week_range[0]:%b %d}–{week_range[1]:%b %d}"))
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description="Quality Gate mechanical checker")
    ap.add_argument("drafts", nargs="+", help="draft file(s) to check")
    ap.add_argument("--library", default=None, help="glob for proof library files (overrides config)")
    ap.add_argument("--config", default=None, help="JSON config path (default: first of %s)" % ", ".join(CONFIG_SEARCH))
    args = ap.parse_args(argv)
    load_overrides(args.config)
    if args.library:
        CFG["library_glob"] = args.library
    ids = library_ids()
    if not ids:
        print(f"NOTE: no proof-library entries found via {CFG['library_glob']!r} — every proof-shaped claim "
              "needs a [PROOF NEEDED] marker or it FAILs (correct when nothing was harvested)")
    fails = warns = 0
    for path in args.drafts:
        try:
            text_lines = pathlib.Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            text_lines = []
        for level, p, n, tag, msg in check_file(path, ids):
            print(f"{level} {p}:{n} [{tag}] {msg}")
            if 0 < n <= len(text_lines):
                print(f"     > {text_lines[n - 1].strip()[:160]}")
            fails += level == "FAIL"
            warns += level == "WARN"
    print(f"\n{'FAIL' if fails else 'PASS'}: {fails} FAIL, {warns} WARN across {len(args.drafts)} file(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
