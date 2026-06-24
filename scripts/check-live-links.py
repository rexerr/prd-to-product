#!/usr/bin/env python3
"""Report broken internal markdown links in live, always-loaded docs.

On-demand hygiene check (not a gate, not a cron). Run it before any commit
that renames or moves files — that is the only moment live-doc link rot is
created, and catching it then means fixing in-context instead of cold.

Rationale for on-demand over a scheduled watcher: link rot is event-driven
(a rename), not time-driven, so a clock fires too late and trains
notification-blindness. See the 2026-06-24 devil's-advocate verdict in the
session retro. Promote to a pre-commit hook only if rot recurs after this.

Scope: only LIVE docs — the always-loaded set plus current skill/template
sources. Dated retros, council transcripts, archives, audits, brainstorms
and mined docs are point-in-time records: a link that was valid when written
is history, not a bug, so "fixing" it would rewrite the record.

Usage:
    python3 scripts/check-live-links.py        # live docs only (default)
    python3 scripts/check-live-links.py --all   # include historical zones (debug)

Exit code: 0 if clean, 1 if any broken link found (so it drops into a
pre-commit hook unchanged).
"""
import os
import re
import sys
import glob

# Point-in-time zones: excluded from the live scan because their links record
# the repo as it was, not as it is. Edit this list if a new historical zone
# is added (e.g. a future docs/<dated-record>/).
HISTORICAL = (
    "docs/retros/",
    "docs/council/",
    "/archive/",
    "docs/mined/",
    "docs/audits/",
    "docs/brainstorms/",
)
# Always skipped — gitignored third-party clones, never ours to fix.
ALWAYS_SKIP = ("docs/mined/repos/",)

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_live(path):
    return not any(zone in path for zone in HISTORICAL)


def scan(include_historical):
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    files = [
        f
        for f in glob.glob("**/*.md", recursive=True)
        if not any(s in f for s in ALWAYS_SKIP)
        and (include_historical or is_live(f))
    ]
    broken = []
    for f in files:
        d = os.path.dirname(f)
        try:
            text = open(f, encoding="utf-8").read()
        except OSError:
            continue
        for m in LINK.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            # strip anchor / title suffixes, keep the path
            path = target.split("#")[0].split(" ")[0].split("?")[0].strip()
            if not path:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(d, path))):
                broken.append((f, target))
    return files, broken


def main():
    include_historical = "--all" in sys.argv
    files, broken = scan(include_historical)
    scope = "all docs" if include_historical else "live docs"
    print(f"Scanned {len(files)} markdown files ({scope}).")
    if not broken:
        print("No broken internal links.")
        return 0
    print(f"Broken internal links: {len(broken)}\n")
    for f, t in broken:
        print(f"  {f}  ->  {t}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
