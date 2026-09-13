#!/usr/bin/env python3
"""Platform length gate for distribution-ready social posts. Deterministic, no model.

Usage: platform-check.py FILE [FILE...]        exit 0 = no FAILs, exit 1 = a FAIL
       platform-check.py --selftest

Why: the roster models cannot count characters. Measured 2026-09-12 (hermes-model-eval,
social_repurpose): Qwen3-Coder-Next lands 289-351 chars on a 280 cap even when told to
write to 240, and prints a "[Character count: 27x/280]" line that is simply wrong. So the
number that gates publishing must come from len(), not from the model.

Checks:
  x-length    FAIL  any tweet/post body > 280 chars
  x-hashtag   FAIL  a #hashtag in an X post (house rule: none)
  li-length   FAIL  LinkedIn post body > 1300 chars
  count-claim WARN  the file's own "[Character count: N/limit]" is off by > 5 from len()

Platform comes from the filename (x-, twitter-, tweet, linkedin-) or, failing that, from a
heading in the file ("Twitter", "X/Twitter", "LinkedIn"). Unknown platform = skipped, noted.

Source of truth: this file in agent-marketing-team (scripts/). Under Claude Code the
distribution-specialist runs it from the plugin root; on agora the homelab-infrastructure sync
script copies it to ~/marketing/scripts/ and the profile's SOUL.md names that path. Stdlib only,
runs on Python 3.9+. Regression check: python3 scripts/platform-check.py --selftest
"""
import pathlib
import re
import sys

LIMITS = {"x": 280, "linkedin": 1300}
HEAD = re.compile(r"^\s*#{1,6}\s")
TWEET_HEAD = re.compile(r"^\s*#{2,4}\s*(Tweet|Draft|Post|Final Tweet)\b", re.I)
META = re.compile(r"^\s*(\*\*[^*]+\*\*:?\s*.*|\[Character count[^\]]*\]|---+|\s*)$", re.I)
CLAIM = re.compile(r"\[?Character count:?\s*(\d+)\s*/\s*(\d+)", re.I)
HASHTAG = re.compile(r"(?<![\w&])#[A-Za-z]\w*")
QUOTE = re.compile(r"^\s*>\s?")


def platform_of(path, text):
    name = pathlib.Path(path).name.lower()
    if re.search(r"(^|[-_])(x|twitter|tweet)s?([-_.]|$)", name):
        return "x"
    if "linkedin" in name:
        return "linkedin"
    head = "\n".join(text.splitlines()[:5]).lower()
    if "linkedin" in head:
        return "linkedin"
    if "twitter" in head or re.search(r"\bx/|\bx post|\bx thread", head):
        return "x"
    return None


def blocks(lines):
    """Yield (start_line, [body lines], [raw lines]) per post. Tweet/Draft headings split; else blockquote
    groups; else the whole body after the header. ponytail: heuristics for the two template
    shapes in references/platform-formats.md — extend if a third shape appears."""
    heads = [i for i, l in enumerate(lines) if TWEET_HEAD.match(l)]
    if heads:
        for i in heads:
            # a post ends at the NEXT HEADING OF ANY LEVEL (## Publishing Checklist, ## Next
            # steps ...), not only at the next tweet heading — bug found live 2026-09-12:
            # the last tweet swallowed the checklist and read 502/280.
            j = next((k for k in range(i + 1, len(lines)) if HEAD.match(lines[k])), len(lines))
            raw = lines[i + 1:j]
            body = [l for l in raw if not HEAD.match(l) and not META.match(l)]
            yield i + 1, body, raw
        return
    if any(QUOTE.match(l) for l in lines):
        cur, start = [], None
        for i, l in enumerate(lines):
            if QUOTE.match(l):
                if start is None:
                    start = i + 1
                cur.append(QUOTE.sub("", l, 1))
            elif cur and l.strip() == "":
                cur.append("")
            elif cur:
                yield start, cur, cur
                cur, start = [], None
        if cur:
            yield start, cur, cur
        return
    body = [l for l in lines if not HEAD.match(l) and not META.match(l)]
    yield 1, body, lines


def post_text(body):
    return "\n".join(body).strip()


def check_file(path):
    findings = []
    try:
        text = pathlib.Path(path).read_text(errors="replace")
    except OSError as e:
        return [("FAIL", path, 0, "io", str(e))]
    plat = platform_of(path, text)
    if plat is None:
        return [("NOTE", path, 0, "platform", "unknown platform (name it x-/twitter-/linkedin-), skipped")]
    limit = LIMITS[plat]
    lines = text.splitlines()
    for start, body, raw in blocks(lines):
        t = post_text(body)
        if not t:
            continue
        n = len(t)
        if n > limit:
            findings.append(("FAIL", path, start, plat + "-length", "%d/%d chars — cut %d" % (n, limit, n - limit)))
        if plat == "x":
            tags = HASHTAG.findall(t)
            if tags:
                findings.append(("FAIL", path, start, "x-hashtag", " ".join(tags)))
        for l in raw:
            m = CLAIM.search(l)
            if m and abs(int(m.group(1)) - n) > 5:
                findings.append(("WARN", path, start, "count-claim", "file says %s, actual %d — the model cannot count; trust this script" % (m.group(1), n)))
    return findings


def selftest():
    import tempfile
    long_tweet = "x" * 285
    samples = {
        "x-thread.md": "## Twitter Thread: T\n\n### Tweet 1/2 (Hook)\nshort one\n\n[Character count: 9/280]\n\n### Tweet 2/2\n" + long_tweet + " #tag\n\n[Character count: 250/280]\n",
        "x-clean-thread.md": "## X Thread: T\n\n### Tweet 1/2 (Hook)\nfine\n\n[Character count: 4/280]\n\n---\n\n### Tweet 2/2 (CTA)\nalso fine\n\n[Character count: 9/280]\n\n---\n\n## Publishing Checklist\n\n- [ ] " + "c" * 300 + "\n- [ ] more\n\n**Next steps for Chris:**\n1. " + "n" * 200 + "\n",
        "x-draft.md": "# X Post Draft\n\n## Draft 1 (278 chars)\n\n> " + "y" * 270 + "\n",
        "linkedin-post.md": "## LinkedIn Post: T\n\n**Character count:** 1400/1300\n\n---\n\n" + "z" * 1400 + "\n",
        "notes.md": "just notes\n",
    }
    with tempfile.TemporaryDirectory() as d:
        out = {}
        for name, body in samples.items():
            p = pathlib.Path(d) / name
            p.write_text(body)
            out[name] = [(f[0], f[3]) for f in check_file(str(p))]
    assert ("FAIL", "x-length") in out["x-thread.md"], out
    assert ("FAIL", "x-hashtag") in out["x-thread.md"], out
    assert ("WARN", "count-claim") in out["x-thread.md"], out
    assert out["x-draft.md"] == [], out
    assert out["x-clean-thread.md"] == [], out   # trailing checklist must not count toward the last tweet
    assert out["linkedin-post.md"] == [("FAIL", "linkedin-length")], out
    assert out["notes.md"][0][1] == "platform", out
    print("selftest OK")


def main(argv):
    if argv[1:] == ["--selftest"]:
        selftest()
        return 0
    if not argv[1:]:
        print(__doc__)
        return 2
    fails = 0
    for path in argv[1:]:
        for level, p, line, kind, msg in check_file(path):
            print("%s %s:%d [%s] %s" % (level, p, line, kind, msg))
            fails += level == "FAIL"
    print("platform-check: %s" % ("FAIL" if fails else "OK"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
