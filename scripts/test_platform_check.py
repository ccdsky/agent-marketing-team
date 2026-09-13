#!/usr/bin/env python3
"""Regression tests for scripts/platform-check.py — the built-in --selftest, runnable the
same way as test_qg_check.py. Cases: over-limit tweet, hashtag, wrong self-reported count,
clean blockquote draft, trailing Publishing Checklist NOT counted toward the last tweet
(the 2026-09-12 live bug: a 134-char tweet read 502/280), over-limit LinkedIn, unknown platform.

Run: python3 scripts/test_platform_check.py
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("platform_check", Path(__file__).parent / "platform-check.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)

if __name__ == "__main__":
    pc.selftest()
