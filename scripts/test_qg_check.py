#!/usr/bin/env python3
"""Regression tests for scripts/qg-check.py, derived from the 2026-08-08 fabricated-
testimonial incident (issue #16): invented quotes with invented attributions shipped
into drafts for a product whose proof library held no testimonials.

Run: python3 scripts/test_qg_check.py
"""

import importlib.util
import io
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

spec = importlib.util.spec_from_file_location("qg_check", Path(__file__).parent / "qg-check.py")
qg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qg)

LIBRARY = """# Proof Library: Acme

### [PROOF-001] Deploy incident reduction
**Proof:** "We cut our deploy incidents by 60% in 6 weeks."
**Attribution:** Jane Doe, VP Eng, MidCo
"""

# Case 1 (2026-08-08 regression): invented quote + invented attribution, no ID -> FAIL
FABRICATED = '''Our customers love it:

"This tool completely transformed how our team ships software every single week" — Alex Rivera, CTO, CloudCorp
'''

# Case 2 (2026-08-08 regression): social-proof @handle without an ID -> FAIL
FABRICATED_HANDLE = "As @devops_dana said, the rollback drills changed everything.\n"

# Case 3: paraphrased claim citing an ID that is NOT in the library -> FAIL
UNRESOLVABLE = "Teams report dramatically faster recovery after adopting drills. [PROOF-002]\n"

# Case 4: real claim citing the real entry -> PASS
CITED_OK = '''"We cut our deploy incidents by 60% in 6 weeks" — Jane Doe, VP Eng, MidCo [PROOF-001]
'''

# Case 5: unsourced outcome stat -> WARN only, no FAIL
STAT_ONLY = "Most teams see incidents reduced by 40% within a quarter.\n"


def run(draft_text):
    with tempfile.TemporaryDirectory() as d:
        lib = Path(d) / "proof-library-acme-2026-08-08.md"
        lib.write_text(LIBRARY)
        draft = Path(d) / "draft.md"
        draft.write_text(draft_text)
        out = io.StringIO()
        with redirect_stdout(out):
            code = qg.main([str(draft), "--library", str(lib), "--config", str(Path(d) / "none.json")])
        return code, out.getvalue()


code, out = run(FABRICATED)
assert code == 1 and "quoted testimonial with attribution" in out, out

code, out = run(FABRICATED_HANDLE)
assert code == 1 and "@handle" in out, out

code, out = run(UNRESOLVABLE)
assert code == 1 and "PROOF-002 does not resolve" in out, out

code, out = run(CITED_OK)
assert code == 0, out

code, out = run(STAT_ONLY)
assert code == 0 and "WARN" in out, out

# ── cases unified from the Hermes deployment's checker (2026-09-12) ──────────────
# Case 6: an explicit [PROOF NEEDED] marker is the honest unsourced state -> no FAIL
MARKED = '"This tool completely transformed how our team ships software every week" — Alex Rivera, CTO [PROOF NEEDED: no testimonial in library]\n'
code, out = run(MARKED)
assert code == 0, out

# Case 7: "— *Name, role*" attribution shape (the agora fabricated-testimonial signature) -> FAIL
NAMED = 'Best purchase this year.\n— *Sarah K., woodturning hobbyist*\n'
code, out = run(NAMED)
assert code == 1 and "named-person attribution" in out, out

# Case 8: built-in AI-tell phrase -> FAIL [banned], no config needed
TELL = "This is a game-changer for small shops.\n"
code, out = run(TELL)
assert code == 1 and "[banned]" in out, out

# Case 9: weekday that disagrees with the calendar -> FAIL [dates] (Aug 27 2026 is a Thursday)
BADDATE = "Day 5 — Wed, Aug 27: post the speed run.\n"
code, out = run(BADDATE)
assert code == 1 and "[dates]" in out and "Thu" in out, out
code, out = run("Day 5 — Thu, Aug 27: post the speed run.\n")
assert code == 0, out

# Case 10: hardware pattern from config -> WARN only
def run_cfg(draft_text, cfg):
    import json
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "lib.md").write_text(LIBRARY)
        (Path(d) / "cfg.json").write_text(json.dumps(dict(cfg, library_glob=str(Path(d) / "lib.md"))))
        draft = Path(d) / "draft.md"; draft.write_text(draft_text)
        out = io.StringIO()
        with redirect_stdout(out):
            code = qg.main([str(draft), "--config", str(Path(d) / "cfg.json")])
        return code, out.getvalue()
code, out = run_cfg("Engrave the clear acrylic tumbler.\n", {"hardware_extra": ["clear acrylic"], "campaign_year": 2026})
assert code == 0 and "[hardware]" in out, out

# Case 11: wrapper API contract (qg-langfuse.py): load_overrides() no-arg, check_file(path) one-arg, 5-tuples
with tempfile.TemporaryDirectory() as d:
    draft = Path(d) / "draft.md"; draft.write_text(FABRICATED)
    qg.load_overrides()
    f = qg.check_file(str(draft))
    assert f and len(f[0]) == 5 and f[0][0] == "FAIL", f

print("all qg-check regression tests passed")
