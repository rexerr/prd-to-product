# Concurrency for UI projects — design brief (rev 2)

> **Status:** rev 2, 2026-06-18. Rev 1 was run through an LLM Council
> ([`council-report-2026-06-18-concurrency-mode.html`](council/council-report-2026-06-18-concurrency-mode.html)),
> which returned **"build nothing (B)"** — but on a premise the operator then corrected. The council assumed the
> bottleneck is *serial review attention* ("you can only look at one screen at a time"). The operator's actual
> bottleneck is **latency** (sitting idle waiting for each task to finish) **and safe option-exploration**
> (can't try approach A vs B without them clobbering each other). This rev re-frames around the real bottleneck
> and proposes a design. **Councilled + devils-advocate'd 2026-06-18 — outcome pinned below. Nothing built.**

---

## Outcome — pinned 2026-06-18 (do not re-litigate without the trigger)

Run through a full LLM Council, then a devils-advocate pass on the rev-2 design. Net result, **don't build a
concurrency / exploration mode now.**

- **Latency (the "I wait" pain) — adopt now, free.** Background agents, a second project, or disjoint-file
  same-tree work (§4). No build, no guard change. This is most of the win.
- **Safe option-exploration — use a second `git clone` or a throwaway branch, confirmed sequentially. No new
  mode, no hook relaxation.** A separate clone is its own checkout with its own dev server, so visual
  confirmation is honest by construction. The DA (verdict, *reconsider*) showed the proposed "exploration mode"
  (§5) is premature, its manual-prototype gate is self-defeating, single-server-sequential *relocates* rather
  than removes the silent-lie footgun, and the mode is itself a blessed bypass of a safety guard.
- **Preview-deploy (option D) is out** — it confirms a build-lagged stale page, the same silent-lie.
- **Revisit trigger (Rule of Two),** clone-or-branch exploration is *actually tried on a real project and found
  wanting twice.* Not one near-miss, not a hunch. Then — and only then — reconsider a worktree-specific mode,
  never per-port-with-a-human-picking, never preview-deploy.

Everything below is the preserved rev-2 analysis the outcome rests on.

---

## 1. The real bottleneck (corrected)

Not review attention — **throughput and safe experimentation**:

- **Latency.** The operator works one agent at a time and waits, idle, for each task to complete before starting
  the next. Serialized work, forced by the tooling, not chosen.
- **Safe option-exploration.** He cannot try two approaches to the same task in parallel and compare, because
  the clean isolation tool (git worktrees) is blocked on UI projects, and the fallback (two sessions on one
  working tree) risks them clobbering each other (the near-collision that surfaced this).

This is the data the rev-1 council explicitly said was missing ("nobody costed the throughput claim — there's no
blocked-work queue"). The operator supplied it: the desire is real, named, and recurring.

## 2. What the rev-1 council got right (keep) vs wrong (discard)

**Keep (survives the premise correction):**
- **Preview-deploy (option D) is out.** A Vercel preview lags local edits by build time, so "confirm on preview"
  confirms a *stale* artifact — the same silent-lie the worktree block exists to prevent, just network-delayed.
- **A naive per-port setup where a human or agent *picks* a port is genuinely dangerous** — wrong-port
  confirmation is "silent breakage wearing a green checkmark."
- **Don't weaken the guard by default for every scaffolded project** (the stickiness objection).

**Discard:**
- **"Parallelism won't help a solo operator."** This rested on the review-attention premise, now corrected.
  The operator isn't bottlenecked on his eyes; he's bottlenecked on *wall-clock wait* and *isolation*.

## 3. The need splits in two — different best answers

| Need | What it is | Best answer |
|---|---|---|
| **Latency** | Idle while one agent grinds | Solvable **today, no build, no guard change** (§4) |
| **Safe option-exploration** | Try A vs B on one project without collision | A **scoped, opt-in worktree mode** that preserves visual confirmation (§5) |

Conflating these two is what muddied rev 1.

## 4. Part 1 — latency (available now, zero build)

The worktree block is **per-project**; nothing stops parallel work *across* surfaces:

- **Background agents** — dispatch a long task to a background agent and keep working in the foreground (the
  harness already supports `run_in_background` and the `Agent`/`Workflow` tools).
- **A second project** — while one project's agent grinds, work in another repo. Different repos, different dev
  servers, zero collision risk.
- **Same-project, disjoint files** — two sessions on one tree is safe *as long as they own different files* and
  commit small/often (the rev-1 fallback).

None of this touches the visual-confirmation guard. Grab it immediately; it likely removes most of the "I wait"
pain. Capture it as documented practice (a session-management note), not new machinery.

## 5. Part 2 — safe option-exploration (the design)

The genuine worktree-shaped need. The design preserves the guard's protection by making relaxation **deliberate,
session-scoped, and disciplined** — never a default weakening.

- **Opt-in "exploration mode," default-off.** Reuse the existing [D-006](DECISIONS.md) write-guard sentinel
  pattern: a session arms exploration mode explicitly (e.g. an `/explore` command writing a session-scoped
  sentinel); the `block-worktree` hook checks for it and *only then* permits worktree creation. Every normal
  session keeps the hard block. The guard is never weakened across projects — it's consciously, temporarily
  relaxed by the one human who accepts the discipline.
- **Visual confirmation stays honest, two tiers:**
  - **Default — single-server-sequential.** Only one dev server runs at a time. Build options A and B in
    isolated worktrees (no visual confirmation needed *during* the build), then confirm them one at a time:
    point the dev server at A, look, stop it, point at B. One server, one truth, **no multi-port and no lie at
    all.** For "explore options," deliberate sequential comparison is what you want anyway.
  - **Opt-in — deterministic per-worktree port.** For genuine side-by-side live viewing: each worktree's port is
    a pure function of its path, and the confirmer **always derives the port from the current working
    directory** — so nothing "picks," and the rev-1 wrong-port failure is engineered out. **Fail-closed:** if the
    derived port has no server running, confirmation errors loudly rather than confirming the wrong app.
- **Cleanup** — exploration mode disarms at session end; stale worktrees are pruned.

Why this answers the council's deepest objection: the guard is **not** permanently mutated in every scaffolded
project. It stays hard-blocking by default; exploration mode is an explicit, per-session, discipline-bound opt-in.

## 6. Sequencing (Rule of Two) — prototype before scaffolding

Do **not** bake this into `context-engineering` first. Order:

1. **Now:** adopt the §4 latency practices (free).
2. **Next, manually:** on one real project, prototype the §5 worktree + single-server-sequential workflow by hand
   (temporarily bypass the hook for that session). Feel whether deliberate sequential exploration actually works.
3. **Only after it earns its keep across ~2 real explorations:** bake "exploration mode" (the opt-in sentinel
   disarm + the discipline + an intake question) into the scaffolder. Until then it's a documented manual
   workflow, not generated machinery.

This keeps the operator's anti-accretion discipline intact: prove the workflow twice before generalizing it into
every future project.

## 7. Open questions for the devils-advocate pass

- Is the §4 latency fix actually most of the win — making §5 a small marginal gain not worth even the manual
  prototype? (i.e. is exploration-on-one-project rare vs. just-run-a-second-thing?)
- Does "exploration mode" reintroduce the silent-lie through operator error — forgetting which worktree the one
  dev server points at? Is single-server-sequential genuinely safe, or just relocating the footgun?
- Is the D-006-sentinel reuse real, or hand-waving — does the block-worktree hook even have access to read such a
  sentinel cleanly?
- Does manual prototyping (step 2) require bypassing a hook in a way that's itself risky or annoying enough to
  never actually happen — making this die in the gap between "documented" and "done"?
- Is there a simpler answer than all of this — e.g., the operator just runs explorations as separate short-lived
  *branches* (not worktrees) with stash/checkout, accepting serial dev-server use, no new mode at all?

## 8. Cross-references

- Rev-1 council: [`council-report-2026-06-18-concurrency-mode.html`](council/council-report-2026-06-18-concurrency-mode.html),
  [`council-transcript-2026-06-18-concurrency-mode.md`](council/council-transcript-2026-06-18-concurrency-mode.md).
- Block mechanism: [`block-worktree.sh.template`](../skills/context-engineering/templates/claude-hooks/block-worktree.sh.template).
- Sentinel-disarm precedent: [D-006](DECISIONS.md) (write-guard run-armed sentinel).
- Visual-gate flag: [D-003](DECISIONS.md). Council threshold: [D-009](DECISIONS.md). Anti-accretion precedents: [D-008](DECISIONS.md), [D-013](DECISIONS.md).
