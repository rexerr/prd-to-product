# Output sketch: medium project (abbreviated)

Companion to `transcript-medium.md`. The medium case lands in flat shape so the output mirrors `output-small/` plus the deltas listed below. No full file tree.

## File tree

```
/Users/sam/Sites/prompt-coach/
├── AGENTS.md                    # @CLAUDE.md plus Codex override (Sam)
├── CLAUDE.md                    # canonical, all rules inline
├── ROADMAP.md
├── .codex/
│   └── config.toml              # write_paths = repo_local_path; approval = always_ask; network off
├── .claude/
│   └── commands/
│       └── session-start.md     # reads CLAUDE.md, ROADMAP.md, latest retro, PARKING_LOT.md
└── docs/
    ├── PRD.md
    ├── ARCHITECTURE.md
    ├── DECISIONS.md
    ├── DECISIONS_ACTIVE.md      # empty, awaiting first promotion
    ├── PARKING_LOT.md
    └── retros/
        └── README.md
```

No `.claude/rules/`. No `.agents/skills/`. The flat CLAUDE.md is doing the rule work.

## CLAUDE.md deltas vs the small case

The medium project has one AI surface, so the flat CLAUDE.md adds:

**Architecture rules (non-negotiable):**

1. **Validate before generating critique.** The API route validates the draft prompt length and content before calling Sonnet. Reject empty or single-character payloads with a 400.
2. **Critique runs server-side only.** `lib/ai/critique.js` is imported only from `app/api/critique/route.js`. Never from a client component.
3. **No critique caching.** Every request hits the model. Quality matters more than cost for this surface.
4. **Saved prompts are user-scoped via session cookie.** No cross-user reads.

**Where to look** table includes a row pointing at `docs/ARCHITECTURE.md` "AI layer" for AI-routing questions.

**Before you respond** block has six items (item 6 is the AI client-component constraint, included because `ai_surface_count >= 1`).

## .codex/config.toml content

Substituted from the template:

```toml
[sandbox]
write_paths = ["/Users/sam/Sites/prompt-coach"]

[network]
enabled = false

[approval]
policy = "always_ask"
```

`.agents/skills/` is **not** emitted because `codex_usage == "occasional"`, not `"regular"`.

## DECISIONS_ACTIVE.md content

Header and promotion criteria from the template. No decisions promoted yet.

## What's not present

- `.claude/rules/` directory
- `.agents/skills/`
- `FUTURE.md`
- Voice-and-tone rule
- Design system rule
- Design heuristics rule
- Surface-specific AI rule files
- `ai-shared.md`
- `product-rules.md`
- A canonical workflow doc

The medium-case test passes if the file list above matches what the generator emits. If `.claude/rules/` shows up, the flat-vs-modular criterion is wrong. If `.agents/skills/` shows up, the codex_usage gate is wrong. If item 6 is missing from the recency block, the renumbering rule is wrong.
