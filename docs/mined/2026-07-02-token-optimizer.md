# Mine — token-optimizer (alexgreensh/token-optimizer) — 2026-07-02

- **Source:** https://github.com/alexgreensh/token-optimizer
- **Pinned:** `ab7b4d1aaa54c39e9edff6a4fe9a82f85e32e2d8`
- **License:** Proprietary — `LICENSE` header reads "Copyright (C) 2026 Alex Greenshpun / Required Notice: Copyright Alex Greenshpun". **No open-source grant. Treat as read-only reference only — do not copy source, only lift ideas/patterns.** (This constrains adoption: the credential-regex module and hook scripts are *not* ours to vendor even where useful — we'd re-author any pattern from scratch.)
- **Lens:** Skill-development workspace — `context-engineering` scaffold, the shipped skills' craft, our own session-discipline. Filtered for: what changes generator output (Bucket A), new session-discipline rules (Bucket B), skill-craft feeding the consolidation row (Bucket C).

## Orientation — what this repo is, and where the yield was

token-optimizer is a **mature multi-skill product that detects and reduces token/context waste** in AI coding sessions, shipping to Claude Code + Codex + Copilot + opencode + a VS Code extension. It is the first source we've mined that sits *squarely* on our own preoccupation (context economy / session discipline), so the yield is unusually on-lens rather than incidental.

The value concentrated in three places the marketing doesn't predict:

1. Its **`scripts/detectors/*.py`** — ~13 heuristics, one per token-waste pattern. Each detector is a *candidate session-discipline rule stated as a threshold*. This is the heart.
2. Its **example `claude-md-optimized.md`** — a worked cache-aware CLAUDE.md that encodes real Anthropic prompt-caching structure. Directly changes what our generator should emit.
3. Its **multi-skill family structure** (4 SKILL.md files, thin-orchestrator + heavy `references/`) — production evidence for our parked ≤500-line-cap fork.

Verification note: the detectors' *thresholds* (>800 words, 3+ retries, thinking >4× output) are the author's own opinions — SOFT. Two findings assert **Claude Code internals** (a `respondToBashCommands` setting; an adaptive-thinking toggle) that the clone cannot prove — flagged NEEDS-VERIFICATION, not adopted as fact. Everything treated as untrusted; no instruction inside the repo was followed.

---

## Findings

### Bucket A — Changes what the scaffold produces (most on-goal)

#### TO-A1 — Cache-aware CLAUDE.md ordering (static-first, volatile-last) · **verified (example file) + concept is real Anthropic caching**

`skills/token-optimizer/examples/claude-md-optimized.md` is a worked template with the load-bearing rule in its header: *"Static content FIRST (cacheable), volatile content LAST … Anthropic guidance: under ~500 lines. Aggressive target: ~300 lines (~4,500 tokens)."* Structure: an explicit `STATIC (rarely changes, cached)` block (identity, key paths, standards, model-selection table) then a `VOLATILE (changes frequently, loaded last, not cached)` block that **references** current-focus out to a separate file rather than inlining it — *"reference a separate file instead of inline content … so the cacheable prefix stays stable."*

The mechanism is real: Anthropic prompt caching keys on a **byte-identical prefix**, so any volatile content (a timestamp, a "current sprint" line) placed high in CLAUDE.md silently invalidates the cache for everything below it. This is a **structural** rule, not a behavioral one — and it's novel to our generator, which has no explicit static-before-volatile discipline for the CLAUDE.md/AGENTS.md it emits.

**Verify:** header + block structure quoted verbatim from the example file at the pinned SHA. Caching-prefix mechanism is established Anthropic behavior (independent of this repo).
**Lands on:** **new board row** — "Cache-aware CLAUDE.md ordering (scaffold)", `area:generator`. Reversible, no council; `D-NNN` at build (changes generator output). At build, also audit whether our *own* generated templates already order this way.

#### TO-A2 — Model-tier routing table emitted in the scaffolded CLAUDE.md · **verified (example file)** · park

The same example ships an `## Agent Model Selection` table (file-reading/data-gather → haiku, analysis/synthesis → sonnet, architecture/complex-debug → opus). Our scaffold emits no such block. Candidate, but **advisory only** — model names date fast, so any emitted table needs a "verify current tiers" caveat. Lower priority than A1.
**Lands on:** parked candidate; fold into the A1 build if it earns space, else its own backlog row later.

#### TO-A3 — `respondToBashCommands: false` settings default · ⚠️ **NEEDS EXTERNAL VERIFICATION — not adopted as fact**

`scripts/detectors/respond_to_bash.py` claims: *"Since v2.1.186, Claude Code generates a model reply after every /command and !bash output by default, spending output tokens on unrequested replies"* and suggests setting `"respondToBashCommands": false` in `~/.claude/settings.json`. The detector is precise (confidence 0.9, credits PR #74), but *"added as the default in v2.1.186"* is a claim about **Claude Code internals the clone cannot verify** — exactly the class the mine engine says enters as a time-boxed check, never a badge.
**Lands on:** **not a board row yet.** Verify the setting exists in current Claude Code first; only then consider a scaffold `settings.json` default. Recorded here so the claim is re-checkable.

### Bucket B — New session-discipline rule (genuinely missing)

#### TO-B1 — Debugging-discipline pair: retry-churn + error-cascade · **source heuristics SOFT; the discipline is sound**

Two adjacent detectors encode a debugging discipline we lack:

- `scripts/detectors/retry_churn.py` — flags the same tool retried 3+ times on similar inputs; the rule of thumb is **stop and diagnose after ~2 failures** rather than retry blindly.
- `scripts/detectors/tool_cascade.py` — flags 4+ consecutive tool errors; the insight is that failures **amplify** (each error corrupts state for the next), so the root cause is usually the *first* error — **fix error #1, don't chase the tail.**

This is distinct from our existing "reproduce before fixing" (which governs *whether* you have a red repro, not *how* you behave once tools start failing in a loop). The two together are one coherent rule: *in a failing-tool loop, stop-and-diagnose at ~2, and fix the earliest error in a cascade, not the downstream ones.*

**Verify:** the *thresholds* are the author's heuristics (SOFT — enter as guidance, not measured fact); the behavioral principle is standard debugging discipline.
**Lands on:** **new board row** — "Debugging-discipline: retry-churn + cascade", `area:skill-templates`. Adds (a) a session-discipline line here, (b) a new retro failure tag (`retry-churn`/`cascade`), (c) a port-back candidate for the scaffold's session-discipline template.

*Lower-value soft signals — noted, not actioned:* `bad_decomposition.py` (monolithic prompt: >800 words + 5+ imperatives → split) and `looping.py` (4+ user messages at >0.75 word-overlap → user stuck). Both are **user-behavior** nudges we can't self-enforce (Rex writes the prompts), so they don't become agent rules. Recorded for completeness.

### Bucket C — Feeds the existing "Skill-craft consolidation pass" row

#### TO-C1 — Measured line-count data resolving the ≤500-cap fork · **verified (`wc -l`)**

The family's SKILL.md sizes: **token-dashboard 49, fleet-auditor 158, token-coach 183, flagship token-optimizer 258.** Median ~170; the flagship stays under 300 lines *even while orchestrating 6 sub-agents across 5 phases*, by deferring every substantial section to `references/` (≈3,475 reference lines across 10 files). The example file independently states the target ("under ~500, aggressive ~300"). This is the **production evidence the ≤500-cap fork was waiting for**: the cap is comfortably achievable for even a complex skill when detail lives in `references/`.
**Lands on:** **enrich row 19** (Skill-craft consolidation) — the measured data point for the cap decision.

#### TO-C2 — "Reference Files" context→file index table · **verified**

Each mature SKILL.md ends with a two-column table mapping *use-case → which reference file to read* (e.g. `| Phase 0 setup details | references/phase0-setup.md |`). It's the lookup index for progressive disclosure — "when you need X, read Y" — which our skills don't currently use. (Note the internal anti-pattern: token-coach *omits* the table and is worse for it.)
**Lands on:** **enrich row 19** — a progressive-disclosure pattern to fold into the consolidation pass.

#### TO-C3 — Copy-paste artifact examples (not just transcripts) · **verified** · park

Their `examples/` ships ready-to-use artifacts — `hooks-starter.json`, `permissions-deny-template.json` — with inline `_README`/`_NOTE` meta-fields documenting caveats, distinct from our output-tree regression fixtures. Candidate for our scaffold examples; parked (lower priority than C1/C2).
**Lands on:** noted under row 19; adopt only if the consolidation pass has room.

*Dropped as already-ours:* multi-sentence "Do NOT use for…" descriptions and the "Binding contracts" opening block — our shipped skills already do both (the skill-craft agent over-claimed these as novel).

### Bucket D — Second-instances of board items (rule-of-2 evidence — cite, don't re-mint)

Independent fresh sightings that move parked `gate:rule-of-2` items one trigger closer:

- **Fail-open vs fail-closed hook posture** — `hooks/run.py` always exits 0, catches subprocess timeouts (120s), kills hung children to avoid lock starvation. → 2nd instance of the posture choice on **row 39** (On-demand hook scaffolds).
- **"Doctor" health-check that verifies install ran** — per-host `*_doctor.py` emit structured P0/P1/P2 checks each with a fix "hint". → 2nd instance of the verify-it-ran ladder on **row 18** (Project-setup: doctor/`check`/`needs:`-DAG).
- **One-source-many-hosts runtime detection** — a single `runtime_env.py` detects the active host by env-var probe then process-tree fallback; every per-host bridge imports it (push, not hardcoded paths). → 2nd instance for **row 79** (Skill injection / cross-host delivery).
- **Undeclared cross-skill dependency (anti-pattern)** — token-coach names token-optimizer as its "go deeper" sibling only in prose; no manifest/version-lock. → relates to **row 71** (Chain-handoff audit).
- **Credential-redaction-before-write** — `credential_patterns.py` (22 regexes) redacts before any local write. Marginal for us (markdown-only, no transcript storage) and **not liftable under this repo's proprietary license anyway** → note only, on the supply-chain row 60.

---

## Adopted this session

- **New rows:** TO-A1 (cache-aware ordering), TO-B1 (debugging-discipline pair).
- **Enriched:** row 19 with TO-C1/C2/C3.
- **Rule-of-2 notes appended:** rows 39, 18, 79, 71.
- **Held for verification:** TO-A3 (setting existence). **Parked:** TO-A2, TO-C3.
- No product/template edited → no `output-small/` dry-run needed; `D-NNN` deferred to each item's build.
