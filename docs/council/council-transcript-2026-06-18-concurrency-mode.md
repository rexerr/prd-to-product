# Council transcript — 2026-06-18 — Concurrency-aware mode for UI projects

**Question put to the council:** Is it worth building a "concurrency-aware mode" into `context-engineering` (so parallel agent sessions can run on UI projects, where the worktree block currently prevents the clean path), or is that too much machinery for the operator's solo-designer workflow? Brief: [`docs/concurrency-mode-brief.md`](../concurrency-mode-brief.md).

**Outcome (chairman):** Build nothing now (Option B). Adopt the documented "shared tree, disjoint files, commit often" pattern; at most add a provisional pre-edit collision-warning hook. Do **not** ship preview-deploy (D) as a planned path — peer review showed it has its own staleness lie. Decide nothing until the throughput desire is converted into logged data. Verdict was effectively unanimous on B.

---

## Anonymization mapping (for audit)

```
A = The Long View
B = The Veteran
C = The Skeptic
D = The Architect
E = The Stranger
```

Note: the options in the question are *also* lettered A–E (A=per-port, B=build-nothing, C=non-visual-only, D=preview-deploy, E=devcontainer). In the reviews, "option D" = preview-deploy; response-letters were de-anonymized to advisor names below.

---

## Advisor responses (de-anonymized)

### The Skeptic
The block exists because visual confirmation silently lying is catastrophic — every option except B reintroduces that failure through a side door. Wrong-port confirmation (A) isn't an edge case, it's the default failure with N servers and a hurried human. Preview-deploy (D) is worse than it looks: build-and-deploy latency means confirming a *stale artifact* — the same lie plus network delay plus build minutes per check. C is just B with extra steps. The trigger is one near-miss that was *caught*, on a workflow that worked — nothing failed. The Rule of Two exists to kill decisions on exactly this evidence: one data point, and it's a success. The bottleneck is the solo reviewer, not session count. **Verdict: Build nothing (B); revisit only on real lost work, twice.**

### The Architect
Worktrees solve a problem he doesn't have. The real problem is "one near-miss + a throughput desire." Fix A weakens the invariant — a wrong-port confirmer is the exact silent-lie the block prevents. Reframe: solo UI parallelism isn't bottlenecked by isolation, it's bottlenecked by the designer's eyes — one screen at a time, serial. Worktrees buy the illusion of throughput while fragmenting attention. Rule of Two: one is not two. **Verdict: B plus one cheap instrument — a pre-edit collision check (warns if a second session touches an uncommitted file another opened); near-zero cost, touches no invariant, generates data. Recurrence = failure two; then D, never A.**

### The Stranger
Two robots editing one set of blueprints; today they share a desk (fast, occasionally grab the same page); the "clean" fix gives each its own desk but the inspector only checks the original — so a robot can swear it fixed something the inspector never sees. Three unspoken assumptions: (1) that parallelism is wanted at all — "works fast, alone, values simplicity" describes serialized work, and there's no blocked-work queue in the brief; (2) that a "nearly" collision is a signal — it resolved, so by Rule of Two it's one and it didn't land; (3) that the guard is under pressure — it isn't, it worked; the operator just wants it not to apply to him. **Verdict: B, the correct answer, not a compromise.**

### The Long View
A per-port worktree mode is a software asset, and software depreciates — three years out it's either obsolete or a load-bearing dependency maintained across every scaffolded project. What compounds rightly is the Rule-of-Two discipline itself; that track record is the real asset. The friction is "I want throughput," not "I can't parallelize." Preview-deploys (D) beat worktrees because Vercel is already paid for. **Verdict: B now, D when a real failure appears; the hour hardening A is an hour not shipping UI.**

### The Veteran
A dozen solo operators built "parallel mode"; the throughput fantasy is real, the gain is not — two sessions doubles the context-switching tax on one bottleneck (you). Don't build concurrency infrastructure for a single-threaded operator. Exception-check: Rule of Two says no — one near-miss, zero failures. A's trap: wrong-port confirmation is silent breakage wearing a green checkmark, worse than honest collision risk. **Verdict: B with teeth — document the pattern AND add a cheap pre-edit same-file warning. Revisit only after a real collision twice; then D, never A.**

---

## Peer review (de-anonymized)

**Votes — strongest:** The Skeptic ×3, The Veteran ×1, The Architect ×1.
**Votes — biggest blind spot:** The Long View ×3, The Architect ×2 (all for endorsing preview-deploy/D without catching its own staleness lie).

**What the council collectively missed (the high-value field):**
- **The near-miss was mis-modeled** — all framed collision as file-level git contention; the real risk is two agents corrupting each other's *uncommitted mid-edit state* (interleaved writes between commits) that a pre-edit file-touch check would not catch. *(flagged by The Skeptic reviewer)*
- **Nobody costed the throughput claim** — no blocked-work queue, no count of how often two sessions were genuinely wanted; every verdict rests on an unmeasured premise. *(The Long View / The Veteran reviewers)*
- **The two failure modes were never separated** — file collision (shared tree) vs silent-lying confirmation (isolated tree) are independent risks conflated by one near-miss. *(The Long View reviewer)*
- **The cheapest win went unnamed: staggered/queued sessions** — one confirms while the next scaffolds — raises throughput without touching isolation or the guard. *(The Architect reviewer)*
- **The proposed collision guard may itself be machinery** — a cross-session check may need shared lock state the single-tree setup doesn't expose. *(The Architect reviewer)*
- **Cheapest diagnostic skipped** — instrument-and-measure before deciding, rather than reasoning from one anecdote. *(The Stranger reviewer)*

---

## Chairman synthesis

**Headline:** Build nothing now (Option B), add at most one cheap collision guard, and instrument the throughput desire — escalate only after two real in-project failures, and never to per-port worktrees.

**Recommendation:** Keep the worktree block as-is; it's the one component protecting against a catastrophic silent failure, and every isolation option (A, D, E) reintroduces that failure through a different door. Adopt "shared tree, disjoint files, commit often." Optionally add a *provisional* pre-edit collision-warning hook, dropping it if it turns out to need real lock infrastructure. Do NOT ship preview-deploy (D) as a planned upgrade — peer review showed it confirms a build-lagged stale artifact (the same lie as A). The question rests on an observed desire with zero in-project failures; the Rule of Two exists to refuse exactly this.

**The one thing to do first:** For the next 2–4 weeks, log every moment you genuinely wanted a second parallel session and every actual file collision — convert "desire" into a counted queue — and decide nothing until that data exists.

---

*Council session — 2026-06-18. Report: [`council-report-2026-06-18-concurrency-mode.html`](council-report-2026-06-18-concurrency-mode.html).*
