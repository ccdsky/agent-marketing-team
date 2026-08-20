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

print("all qg-check regression tests passed")
