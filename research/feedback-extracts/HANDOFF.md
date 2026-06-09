# HANDOFF — Plan-review history mining

**Status:** investigation paused mid-stream 2026-06-09, to be continued in a fresh session.
**Goal:** produce real evidence — from Rex's actual Claude Code history — of how often his proposed **plans** get sent back for revision and **why**, so we can decide whether a "self-healing plan-review loop" is worth building and, if not, draft a planning prompt that pre-empts the recurring revisions.

This doc is written to be run **cold** — a session with zero memory of the originating conversation should be able to execute the extraction from this file alone.

---

## 1. Why we're here (origin + decision)

Rex sketched a "self-healing plan-review loop": capture the feedback he gives on Claude's plans → count it by theme → gate a human fix that folds the lesson back into context (CLAUDE.md / a planning prompt) so the same feedback stops recurring.

An LLM council pressure-tested it. Verdict (saved under [`docs/council/`](../../docs/council/)):
- [`council-report-2026-06-09-self-healing-loop.html`](../../docs/council/council-report-2026-06-09-self-healing-loop.html)
- [`council-transcript-2026-06-09-self-healing-loop.md`](../../docs/council/council-transcript-2026-06-09-self-healing-loop.md)

**Don't build the loop on instinct.** The repo's own principle is "earn a guardrail with evidence from the log, not instinct," and the proposal asserted "I fix the same things over and over" with *no count*. The council also flagged that a forward-looking 2-week tagging trial would (a) reproduce that same sin at smaller scale and (b) risk *manufacturing* the signal by training attention onto friction. **Mining history avoids both** — the corrections already happened, and we get real cross-project volume.

So the task is: **mine the existing transcripts for the count + the recurring categories of plan-revision feedback.** Then, and only then, decide.

---

## 2. The signal — what we are actually counting

The unit is **a plan-review round**, NOT a scattered "correction." A first attempt that keyword-grepped for any correction was **rejected as too broad** — it swept in build-time and design-iteration corrections that have nothing to do with reviewing a *plan*. Rex sharpened it: the thing to measure is the **plan → revise → plan → revise** loop — rounds of feedback against a *proposed plan*.

### Key findings from data validation (these are load-bearing — do not relearn them the hard way)

1. **Plans are fully captured.** Every `ExitPlanMode` tool call carries the complete plan text in its `input.plan` field (verified: seance plan v1 = 8,421 chars, revised = 10,690 chars). You can read the exact before/after of each revision.
2. **Rounds ≠ raw `ExitPlanMode` count.** Plan versions frequently appear back-to-back *within one assistant turn* (the model editing its own plan doc / re-exiting plan mode before showing it). Those are NOT separate review rounds. The TRUE round boundary is: **a plan is presented → Rex responds → was that response an approval or a revision?** Count rounds by the *human turn that sits between plan presentations*, then collapse consecutive plan presentations with no human turn between them into a single "presentation."
3. **Classify Rex's closing turn per round:**
   - **APPROVE** — "go" / "confirm" / "yes draft a plan" / "commit and push" / "looks good".
   - **REVISE** — substantive redirect of the plan. (Real example, epost: *"lets not do a token. we can build this at a link like /scoring-guide…"* — an approach change.)
   - **INTERRUPT** — "Request interrupted by user" followed by "stop, I have feedback for the plan." Often Rex pasting a Cowork review back in. Treat as a REVISE round.
4. **Honesty rule is load-bearing.** Both the keyword filter and the raw `ExitPlanMode` count overcount true revision rounds ~2–3×. Most human turns in PRD-interview and UI-iteration sessions are normal answers ("confirm", "yes", "v1"), not plan revisions. Agents MUST exclude non-revisions and may legitimately report **0 revisions** for a session. A small honest count is the goal; a padded one poisons the aggregate.
5. **Free themes beat the 8-tag taxonomy.** In the 6-transcript sample, the retro tags (bad-substitution / scope-creep / lost-context / goal-drift) and the four plan-review additions (weak-acceptance-criteria / missing-read-before-write / unstated-assumption / over-engineering) mostly landed as `other`. **Rank patterns by emergent free-form `theme`; keep `tag` only to confirm the taxonomy's poor fit.** (Rex had no categorization preference → use emergent-themes-with-taxonomy-as-a-check.)

---

## 3. Data landscape (from the deterministic scan, 2026-06-09)

Transcripts live on disk at `~/.claude/projects/<encoded-project-path>/*.jsonl`. Each line is a JSON event.

- **141** non-empty transcripts across real projects (tmp/probe dirs excluded).
- **82** sessions have a plan on the table (≥1 `ExitPlanMode`, or an interrupt-with-feedback).
- **≈48** of those show **2+ plan versions** — the multi-round back-and-forth Rex specifically cares about. (Live count; it ticks up as new sessions accrue — e.g. the documenting session itself crossed the threshold, 48→49. Re-run `planscan.py` for the current number.)
- Concentration: `seance`, `epost-assessment`, `epost-intelligence-feed`, `qventus-prototyper`, `prd-to-product`, `the-council`.

`scripts/planscan.py` reproduces the 82 / 48 numbers.

### jsonl schema (what the scripts rely on)
Each line: `type` (`user` | `assistant` | `system` | `custom-title` | …), `timestamp`, `cwd`, `gitBranch`, and `message` with `role` and `content`. `content` is either a string or a list of blocks: `{type:"text"}`, `{type:"tool_use", name, input}`, `{type:"tool_result"}`. A plan lives in a `tool_use` block where `name == "ExitPlanMode"`, under `input.plan`. A human turn = `type=="user"` AND `message.role=="user"` AND the content is not a `tool_result`.

---

## 4. Scripts (preserved in `scripts/`)

These were validated in this investigation and copied off ephemeral `/tmp`. All are **read-only** against `~/.claude/projects/`.

- **`prefilter.py`** — walks all real projects (skips tmp/probe), scores each transcript by human-turn count + a correction-signal regex + plan-mode signal, prints a ranked candidate list and per-project tallies. *(This is the OLD keyword approach — kept for reference, but the round-based method below supersedes it for the real run.)*
- **`planscan.py`** — the one that matters for scoping: counts `ExitPlanMode` / `EnterPlanMode` / interrupts per session; prints how many sessions have a plan and how many are multi-round. Also demonstrates that `input.plan` carries full plan text.
- **`rounds.py <file.jsonl>`** — reconstructs the plan↔feedback interleaving for a single session: prints each plan presented (char count + title) and the human turns between them. This is the core digest the extraction agents read.
- **`corrview.py <file.jsonl>`** — older correction-focused digest (assistant-tail + human turn). Useful but not round-aware; prefer `rounds.py` for the real run.

---

## 5. What's already done vs. not

**Done (this session):**
- The 6-transcript **sample extracts** in this folder (`feedback-extract-*.md`) — BUT they are **correction-based**, the rejected broad format. Treat them as a method-validation artifact, not the deliverable. The real run re-does these sessions **round-based**.
- All findings above, the data scan, and the scripts.

**Not done (the actual next-session job):**
- The round-based extraction run over the chosen population.
- The aggregate report `PATTERNS.md`.
- Drafting the planning-prompt "furnace" from the patterns.
- Any decision about building the loop itself.

---

## 6. The run to execute next session

### Per-session extract schema (round-based)
For each session, write `feedback-extract-<project>-<YYYY-MM-DD>-<topic>.md` with:

```
## Provenance
- source: Claude Code
- project / conversation / dates
- plans presented: <n distinct presentations, after collapsing back-to-back>
- revision rounds: <n REVISE/INTERRUPT closings>

## Rounds
### R<n> — <plan title / version>
- closing: approve | revise | interrupt
- (for revise/interrupt only:)
- verbatim: "<Rex's exact feedback, ≤200 chars>"
- normalized: <one neutral sentence — what was wrong with the plan>
- theme: <2–5 words, your own words — the real label>
- tag: <one of the 8 if it genuinely fits, else `other`>
- where_fix_lives: planning-prompt | claude-md | skill:<name> | context:<file> | code | decisions | unclear
- promotable: yes | no | maybe   (would a standing planning rule have pre-empted this?)

## Session summary
- rounds-to-acceptance for the session's plan(s)
- top revision themes here
- one honest sentence (real pattern, or mostly first-pass approvals?)
```

### Aggregate to produce (`PATTERNS.md`) — this is the answer
1. **Rounds-to-acceptance distribution** — how often do plans pass in 1 round vs need 2 / 3+? (The headline number Rex asked for.)
2. **Ranked recurring revision themes** across all rounds, with cross-project counts. **This ranked list is the first draft of the planning-prompt "furnace."**
3. **`where_fix_lives` distribution** — does the fix mostly belong in a planning prompt vs CLAUDE.md vs a specific skill?
4. **`promotable: yes` cluster**, ranked by frequency — each candidate rule citing the rounds that justify it (extends the repo's "every rule cites its failure mode" invariant backward).
5. **Taxonomy-fit note** — did the 8 tags hold, or confirm they don't?

### Suggested mechanics
This is real scale (≥48 sessions). Use a **`Workflow`** (Rex must opt in — it's multi-agent): `pipeline` over the chosen sessions; each agent reads that session's `rounds.py` digest, applies the schema above (honesty rule, collapse-back-to-back, approve/revise/interrupt classification), and Writes one extract file. Then a deterministic grep-tally over the fixed field keys (`theme:`, `tag:`, `where_fix_lives:`, `promotable:`, `closing:`) + one synthesis agent writes `PATTERNS.md`. No `isolation: worktree` needed (each agent writes a distinct file). Concurrency auto-caps ~16; ≥48 items run in ~3–4 waves.

---

## 7. Open scoping decision (Rex deferred — decide before the run)

**Which population?**
- **All 82 plan-bearing sessions (recommended)** — you need single-round sessions as the *denominator* to answer "how often do my plans pass first time vs. need revision." Multi-round sessions get the deep-dive; single-round ones still log their one approve/revise closing.
- **48 multi-round only** — tighter, cheaper, but loses the first-pass baseline.
- **48 + ~15 single-round sample** — middle path for a baseline ratio without all 82.

---

## 8. Guardrails / context

- This investigation is **not** the rejected `docs/plan-reviews/` subsystem. It's a one-time evidence-gathering pass. `research/feedback-extracts/` is staging; it can be deleted once `PATTERNS.md` is read and any furnace draft is folded in.
- Building the self-healing loop is **out of scope** until this run produces the evidence (council ruling).
- A `docs/DECISIONS.md` entry ("mine history before building the loop") is a candidate but is **Rex-gated** — flag it, don't auto-write.
- BACKLOG entry pointing here: see `BACKLOG.md` → "Plan-review history mining."
