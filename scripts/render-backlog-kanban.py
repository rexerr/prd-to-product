#!/usr/bin/env python3
"""Render BACKLOG.md as a visual kanban HTML view.

The markdown stays the source of truth; this is a read-only generated VIEW
(like the council report). Regenerate any time:

    python3 scripts/render-backlog-kanban.py

Writes BACKLOG.html next to BACKLOG.md. Parses the `## Board` table
(Item | Lane | Seq | Next | Refs), groups rows into lane columns, and
renders each row as a card whose links point at the same tickets/briefs/
decisions the markdown does. Self-contained, no dependencies.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "BACKLOG.md"
OUT = ROOT / "BACKLOG.html"

# Lane order (kanban columns, left to right) + accent color.
LANES = [
    ("active", "Active", "#D97757"),
    ("next", "Next", "#3b82a0"),
    ("watching", "Watching", "#b08948"),
    ("backlog", "Backlog", "#6b6b8a"),
    ("blocked", "Blocked", "#b0524a"),
    ("icebox", "Icebox", "#8c8c8a"),
]


def render_inline(text: str) -> str:
    """Light markdown-inline -> HTML: escape, then links, bold, code."""
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def parse_rows(md: str):
    """Pull the board table rows out of the `## Board` section."""
    rows = []
    in_board = False
    for line in md.splitlines():
        if line.startswith("## Board"):
            in_board = True
            continue
        if in_board and line.startswith("## "):
            break
        if not (in_board and line.strip().startswith("|")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        if cells[0] in ("Item", "") or set(cells[0]) <= {"-", ":"}:
            continue  # header or separator
        item, lane, seq, nxt, refs = cells[0], cells[1].lower(), cells[2], cells[3], cells[4]
        rows.append({"item": item, "lane": lane, "seq": seq, "next": nxt, "refs": refs})
    return rows


def card_html(row: dict) -> str:
    seq = row["seq"].strip()
    seq_badge = f'<span class="seq">{html.escape(seq)}</span>' if seq and seq != "—" else ""
    refs = row["refs"].strip()
    refs_html = f'<div class="refs">{render_inline(refs)}</div>' if refs and refs != "—" else ""
    return (
        '<div class="card">'
        f'<div class="card-head">{seq_badge}<span class="title">{render_inline(row["item"])}</span></div>'
        f'<div class="next">{render_inline(row["next"])}</div>'
        f"{refs_html}"
        "</div>"
    )


def build(md: str) -> str:
    rows = parse_rows(md)
    title_match = re.search(r"^#\s+(.+)$", md, re.M)
    title = title_match.group(1).strip() if title_match else "Backlog"

    columns = []
    for key, label, color in LANES:
        lane_rows = [r for r in rows if r["lane"] == key]
        # Sort actionable lanes by Seq (numeric first, then the rest).
        def seq_key(r):
            s = r["seq"].strip()
            return (0, int(s)) if s.isdigit() else (1, 0)
        lane_rows.sort(key=seq_key)
        cards = "".join(card_html(r) for r in lane_rows) or '<div class="empty">—</div>'
        columns.append(
            f'<section class="col" style="--lane:{color}">'
            f'<h2>{label}<span class="count">{len(lane_rows)}</span></h2>'
            f'<div class="cards">{cards}</div>'
            "</section>"
        )

    return TEMPLATE.format(title=html.escape(title), columns="".join(columns), n=len(rows))


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#faf9f5;--card:#fff;--ink:#141413;--ink2:#5c5c5a;--muted:#8c8c8a;--border:#e5e4df;--shadow:rgba(20,20,19,.05)}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--ink);line-height:1.5;padding:28px 32px}}
header{{margin-bottom:22px}}
h1{{font-size:22px;font-weight:700;letter-spacing:-.01em}}
.sub{{color:var(--muted);font-size:13px;margin-top:3px}}
.board{{display:flex;gap:16px;align-items:flex-start;overflow-x:auto;padding-bottom:16px}}
.col{{flex:0 0 300px;background:#f5f4ef;border:1px solid var(--border);border-radius:12px;padding:12px}}
.col h2{{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--ink2);
  display:flex;align-items:center;gap:8px;padding:2px 4px 12px;border-bottom:2px solid var(--lane);margin-bottom:12px}}
.count{{margin-left:auto;background:var(--lane);color:#fff;font-size:11px;font-weight:600;
  border-radius:10px;padding:1px 8px;letter-spacing:0}}
.cards{{display:flex;flex-direction:column;gap:10px}}
.card{{background:var(--card);border:1px solid var(--border);border-left:3px solid var(--lane);
  border-radius:9px;padding:11px 12px;box-shadow:0 1px 2px var(--shadow)}}
.card-head{{display:flex;align-items:baseline;gap:8px;margin-bottom:5px}}
.seq{{flex:0 0 auto;background:var(--lane);color:#fff;font-size:11px;font-weight:700;
  border-radius:6px;padding:1px 7px;line-height:1.5}}
.title{{font-size:13.5px;font-weight:600;letter-spacing:-.005em}}
.next{{font-size:12px;color:var(--ink2)}}
.refs{{font-size:11px;color:var(--muted);margin-top:7px}}
.empty{{color:var(--muted);font-size:13px;text-align:center;padding:14px 0}}
a{{color:var(--lane,#D97757);text-decoration:none;border-bottom:1px solid transparent}}
a:hover{{border-bottom-color:currentColor}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.88em;
  background:#efeee9;border-radius:4px;padding:.5px 4px}}
strong{{font-weight:600;color:var(--ink)}}
</style></head><body>
<header><h1>{title}</h1>
<div class="sub">{n} live items · rendered view of BACKLOG.md (source of truth) · regenerate with scripts/render-backlog-kanban.py</div></header>
<div class="board">{columns}</div>
</body></html>
"""


def main():
    if not SRC.exists():
        sys.exit(f"not found: {SRC}")
    OUT.write_text(build(SRC.read_text()))
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
