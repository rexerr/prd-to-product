# Furnace draft — plan-time verification preflight

**Status:** SHIPPED as a trial, 2026-06-12. The four checks below now live in the global skill `~/.claude/skills/furnace-plan/` (explicit-invoke, outside this repo). This file is kept as the design record + the evidence-to-rule mapping. Trial is active and Cowork-graded — see BACKLOG.
**Source:** [`PATTERNS.md`](PATTERNS.md) (83-session audit) → [`council-report-2026-06-12-furnace.html`](../../docs/council/council-report-2026-06-12-furnace.html) (build-narrow verdict) → this draft.
**Scope:** the contamination-proof verification-citation core only (audit themes T1/T2/T6). Deliberately omits R5–R7 and the preventable/healthy-friction split — those rested on data the council judged too soft to promote.

---

## Why this is safe to build despite soft data

Every revision in the audit was caught by Claude Cowork (pasted in), never by Rex unaided. That would normally poison a guardrail — except these four checks don't depend on *who* caught the error. **A plan that asserts a file's contents without reading the file is wrong regardless of who flagged it.** The defect is mechanical and verifiable, so the furnace clears the repo's "earn a guardrail with evidence" bar on the defect's own merits, not on the contested counts.

## How to validate it (the oracle is Cowork, never Rex)

Rex cannot grade this — he doesn't catch these errors. The only honest test:

1. Run the next ~10 real planning sessions with the furnace preflight applied.
2. **Still route every furnace-on plan through Cowork**, exactly as today.
3. Count T1/T2/T6 defects Cowork flags in furnace-on plans vs. the audit baseline.
4. Fewer Cowork catches → the furnace pre-empted them at authoring time. It works. More/equal → it doesn't reach the failure (the defect may be an execution-stage gap a planning prompt can't fix — a live council caveat).

**Guard against the trust trap:** until that test clears, the furnace is a *complement* that shrinks Cowork's mechanical load — NOT a reason to skip the Cowork round-trip. Cowork stays authoritative and in-the-loop. A furnace that catches 70% and quietly retires Cowork lets the other 30% ship unseen, and Rex has no independent way to catch the leak.

---

## THE FURNACE — paste-ready preflight

> Apply this to your own draft plan **before** presenting it (before `ExitPlanMode`). It is a self-review, not advice to the user. For each check: if it fails, fix the plan or do the read/probe now — do not present a plan that fails any check. It is legitimate and expected for this preflight to send you back to read a file or run a probe before you are allowed to present.

**1. Cite every codebase claim to a read you actually ran this session.**
Every "X is missing," "no files modified," "these mirror each other," every count or filename or content claim must trace to a grep/read you performed in *this* session — not memory, not inference from names. If you haven't read it, you don't know it; go read it before the plan asserts it.
*Failure it prevents (audit T2, ~14 rounds):* "Step 7 — replacing AGENTS.md with @CLAUDE.md loses content. AGENTS.md isn't a pure pointer today." A plan built on imagined repo state.

**2. Make every verification step able to fail, and able to reach what it claims to test.**
For each verify item, state the observation that would make it RED. Include the unchanged/default path and the failure path, not just the happy path. Measure claimed wins; do not assert them. If a check would pass even when the thing it tests is broken, it is theater — replace it.
*Failure it prevents (audit T1, ~20 rounds):* "The live 'abort path' test doesn't test the abort path — a bad key is an auth failure that rejects instantly; it never arms the timeout." / "The test script may run zero tests and report green."

**3. Probe unverified platform/tool mechanics as step 0, before the plan depends on them.**
If the design rests on a tool/SDK/platform/MCP behavior you have not empirically confirmed this session, the probe is the FIRST step and its result is allowed to fork the plan. Do not schedule the probe at step 8 of a plan that collapses if step 0 fails.
*Failure it prevents (audit T6, ~6 rounds):* "Headline: `ask` hangs in headless mode — so it deadlocks the very orchestrator it's meant to unblock." / "verify `paths:` empirically before step 1, not at step 8. The entire plan rests on it."

**4. (Boundary check) Diff the plan against recorded decisions and this session's agreements before presenting.**
Name every recorded decision (D-NNN or equivalent) the plan touches; flag any reversal as an explicit sign-off item, never a silent change; confirm nothing agreed earlier this session was dropped. *This one is more project-specific than 1–3 — it needs a decisions log to check against — so treat it as the optional fourth check, droppable when there's no such log.*
*Failure it prevents (audit T4, ~10 rounds):* "that is not the full plan. where is the bit about housekeeping?" / a plan that "re-commits the exact import-crash the last two splits exist to avoid."

---

*If you adopt this: the natural home is a planning-prompt fragment the agent self-applies, or a check folded into the existing plan-review skill. Keep checks 1–3 portable (no project facts); keep check 4 wherever the decisions log lives.*
