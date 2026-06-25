#!/usr/bin/env python3
"""Render BACKLOG.md as a visual kanban HTML view.

The markdown stays the source of truth; this is a read-only generated VIEW
(like the council report). Regenerate any time:

    python3 scripts/render-backlog-kanban.py

Writes BACKLOG.html next to BACKLOG.md. Parses the `## Board` table
(Item | Type | Lane | Seq | Tags | Gloss | Refs), groups rows into lane
columns, and renders each row as a card: the Gloss is the plain-English line,
Type + Tags show as chips, and a row that links a `tickets/<slug>.md` gets an
"open ticket" button. Tags are validated against the `<!-- TAGS -->` vocabulary
block above the board; unknown/over-budget tags are reported (stderr + a banner).
Self-contained, no dependencies.
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

MAX_TAGS = 2


def render_inline(text: str) -> str:
    """Light markdown-inline -> HTML: escape, then links, bold, code."""
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def plain(text: str) -> str:
    """Strip markdown links to their label, for clean warning messages."""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text).strip()


def parse_allowed_tags(md: str) -> dict:
    """Read the `<!-- TAGS ... -->` block into {axis: {allowed values}}."""
    allowed = {"gate": set(), "area": set()}
    m = re.search(r"<!--\s*TAGS.*?-->", md, re.S)
    if not m:
        return allowed
    block = m.group(0)
    for axis in allowed:
        am = re.search(rf"^\s*{axis}:.*?—(.*)$", block, re.M)
        if am:
            allowed[axis] = {v.strip() for v in am.group(1).split("·") if v.strip()}
    return allowed


def row_tags(row: dict) -> list:
    raw = row["tags"].strip()
    if not raw or raw == "—":
        return []
    return [t.strip() for t in raw.split(",") if t.strip()]


def validate_tags(rows: list, allowed: dict) -> list:
    """Return a list of human-readable warnings for off-vocabulary / over-budget tags."""
    warnings = []
    for r in rows:
        label = plain(r["item"])[:48]
        tags = row_tags(r)
        if len(tags) > MAX_TAGS:
            warnings.append(f'"{label}" — {len(tags)} tags (max {MAX_TAGS})')
        for t in tags:
            if ":" not in t:
                warnings.append(f'"{label}" — tag "{t}" missing an axis (gate:/area:)')
                continue
            axis, _, val = t.partition(":")
            if axis not in allowed:
                warnings.append(f'"{label}" — unknown axis in "{t}" (use gate:/area:)')
            elif val.startswith("blocked-on-"):
                continue  # wildcard: gate:blocked-on-<x>
            elif val not in allowed[axis]:
                warnings.append(f'"{label}" — "{t}" not in the {axis}: vocabulary')
    return warnings


def ticket_link(row: dict):
    """First `tickets/<slug>.md` link found in Item or Refs, if any."""
    for field in (row["item"], row["refs"]):
        m = re.search(r"\(([^)]*tickets/[^)]+\.md)\)", field)
        if m:
            return m.group(1)
    return None


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
        if len(cells) < 7:
            continue
        if cells[0] in ("Item", "") or set(cells[0]) <= {"-", ":"}:
            continue  # header or separator
        rows.append({
            "item": cells[0], "type": cells[1], "lane": cells[2].lower(),
            "seq": cells[3], "tags": cells[4], "gloss": cells[5],
            "refs": cells[6],
        })
    return rows


def card_html(row: dict) -> str:
    seq = row["seq"].strip()
    seq_badge = f'<span class="seq">{html.escape(seq)}</span>' if seq and seq != "—" else ""

    typ = row["type"].strip()
    type_chip = f'<span class="type">{html.escape(typ)}</span>' if typ and typ != "—" else ""
    chips = []
    for t in row_tags(row):
        axis = "gate" if t.startswith("gate:") else "area" if t.startswith("area:") else "other"
        chips.append(f'<span class="tag {axis}">{html.escape(t)}</span>')
    meta = f'<div class="meta">{type_chip}{"".join(chips)}</div>' if (type_chip or chips) else ""

    gloss = row["gloss"].strip()
    gloss_html = f'<div class="gloss">{render_inline(gloss)}</div>' if gloss and gloss != "—" else ""

    tkt = ticket_link(row)
    tkt_html = f'<a class="ticket" href="{html.escape(tkt)}">\U0001F4CB open ticket</a>' if tkt else ""
    refs = row["refs"].strip()
    refs_html = f'<div class="refs">{render_inline(refs)}</div>' if refs and refs != "—" else ""

    return (
        '<div class="card">'
        f'<div class="card-head">{seq_badge}<span class="title">{render_inline(row["item"])}</span></div>'
        f"{meta}{gloss_html}{tkt_html}{refs_html}"
        "</div>"
    )


def build(md: str) -> str:
    rows = parse_rows(md)
    warnings = validate_tags(rows, parse_allowed_tags(md))
    title_match = re.search(r"^#\s+(.+)$", md, re.M)
    title = title_match.group(1).strip() if title_match else "Backlog"

    banner = ""
    if warnings:
        items = "".join(f"<li>{render_inline(w)}</li>" for w in warnings)
        banner = f'<div class="warn"><strong>{len(warnings)} tag issue(s):</strong><ul>{items}</ul></div>'

    columns = []
    for key, label, color in LANES:
        lane_rows = [r for r in rows if r["lane"] == key]

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

    return TEMPLATE.format(
        title=html.escape(title), columns="".join(columns), n=len(rows), banner=banner
    )


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
.warn{{background:#fbeae4;border:1px solid #e0a99e;color:#8a3128;border-radius:10px;padding:12px 16px;margin-bottom:18px;font-size:13px}}
.warn ul{{margin:6px 0 0 18px}}
.warn li{{margin:2px 0}}
.board{{display:flex;gap:16px;align-items:flex-start;overflow-x:auto;padding-bottom:16px}}
.col{{flex:0 0 320px;background:#f5f4ef;border:1px solid var(--border);border-radius:12px;padding:12px}}
.col h2{{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--ink2);
  display:flex;align-items:center;gap:8px;padding:2px 4px 12px;border-bottom:2px solid var(--lane);margin-bottom:12px}}
.count{{margin-left:auto;background:var(--lane);color:#fff;font-size:11px;font-weight:600;
  border-radius:10px;padding:1px 8px;letter-spacing:0}}
.cards{{display:flex;flex-direction:column;gap:10px}}
.card{{background:var(--card);border:1px solid var(--border);border-left:3px solid var(--lane);
  border-radius:9px;padding:11px 12px;box-shadow:0 1px 2px var(--shadow)}}
.card-head{{display:flex;align-items:baseline;gap:8px;margin-bottom:6px}}
.seq{{flex:0 0 auto;background:var(--lane);color:#fff;font-size:11px;font-weight:700;
  border-radius:6px;padding:1px 7px;line-height:1.5}}
.title{{font-size:13.5px;font-weight:600;letter-spacing:-.005em}}
.meta{{display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin-bottom:6px}}
.type{{font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--ink2);
  background:#efeee9;border-radius:4px;padding:1.5px 6px}}
.tag{{font-size:10.5px;font-weight:500;border-radius:4px;padding:1.5px 6px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}
.tag.gate{{background:#fbeae4;color:#a8493f}}
.tag.area{{background:#e7eef2;color:#37657d}}
.tag.other{{background:#efeee9;color:var(--ink2)}}
.gloss{{font-size:12.5px;color:var(--ink);margin-bottom:6px}}
.ticket{{display:inline-block;font-size:11px;font-weight:600;margin-top:6px;color:var(--lane)!important;
  border:1px solid var(--lane);border-radius:6px;padding:2px 9px;text-decoration:none}}
.ticket:hover{{background:var(--lane);color:#fff!important}}
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
{banner}
<div class="board">{columns}</div>
</body></html>
"""


def main():
    if not SRC.exists():
        sys.exit(f"not found: {SRC}")
    md = SRC.read_text()
    warnings = validate_tags(parse_rows(md), parse_allowed_tags(md))
    OUT.write_text(build(md))
    for w in warnings:
        print(f"  tag warning: {w}", file=sys.stderr)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(warnings)} tag warning(s))")


if __name__ == "__main__":
    main()
