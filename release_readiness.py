#!/usr/bin/env python3
"""Validate release-readiness evidence for a staged product change."""
import json
import sys

REQUIRED_TEXT = ("feature", "owner", "staging_environment", "documentation", "audit_note")
REQUIRED_FLAGS = ("code_reviewed", "tests_passing", "accessibility_checked", "security_checked")


def load_release(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def missing_items(release):
    missing = []
    for key in REQUIRED_TEXT:
        if not str(release.get(key, "")).strip():
            missing.append(key)
    for key in REQUIRED_FLAGS:
        if release.get(key) is not True:
            missing.append(key)
    return missing


def readiness_report(release):
    missing = missing_items(release)
    status = "READY_FOR_STAGING_REVIEW" if not missing else "NOT_READY"
    lines = [
        f"Feature: {release.get('feature', 'Unknown')}",
        f"Status: {status}",
    ]
    if missing:
        lines.append("Missing: " + ", ".join(missing))
    else:
        lines.append("Evidence: review, tests, docs, accessibility, security and audit note are present.")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 2:
        print("Usage: python3 release_readiness.py <release.json>")
        return 2
    report = readiness_report(load_release(argv[1]))
    print(report)
    return 0 if "READY_FOR_STAGING_REVIEW" in report else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
