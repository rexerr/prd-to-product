# scripts — plan-review history mining

Read-only utilities over `~/.claude/projects/<encoded-project>/*.jsonl` (Claude Code session transcripts). Preserved from ephemeral `/tmp` so the investigation survives. See [`../HANDOFF.md`](../HANDOFF.md) for the full method.

**jsonl schema:** each line is a JSON event with `type` (`user` | `assistant` | `system` | `custom-title` | …), `timestamp`, `cwd`, `gitBranch`, and `message` (`role` + `content`). `content` is a string or a list of blocks: `{type:"text"}`, `{type:"tool_use", name, input}`, `{type:"tool_result"}`. A **plan** lives in a `tool_use` block named `ExitPlanMode`, under `input.plan`. A **human turn** = `type=="user"` + `message.role=="user"` + content is not a `tool_result`.

| script | what it does |
|---|---|
| `planscan.py` | **Scoping.** Counts `ExitPlanMode` / `EnterPlanMode` / interrupts per session; reports how many sessions have a plan (82) and how many are multi-round (48). Confirms `input.plan` carries full plan text. |
| `rounds.py <file.jsonl>` | **Core digest for extraction.** Reconstructs the plan↔feedback interleaving for one session — each plan presented (chars + title) and the human turns between them. |
| `prefilter.py` | *(Legacy — keyword approach, superseded.)* Ranks transcripts by a correction-signal regex. Kept for reference; the round-based method in HANDOFF.md replaces it for the real run. |
| `corrview.py <file.jsonl>` | *(Legacy.)* Correction-focused digest (assistant-tail + human turn), not round-aware. Prefer `rounds.py`. |

Run examples:
```
python3 scripts/planscan.py                 # reproduce 82 plan-bearing / 48 multi-round
python3 scripts/rounds.py ~/.claude/projects/<proj>/<id>.jsonl
```
