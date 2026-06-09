# Brief — adopting Claude Design handoffs into the design-system flow

> **⚠️ SUPERSEDED by the 2026-06-09 audit — see [D-008](DECISIONS.md) and the [audit council report](council/council-report-2026-06-09-audit.html).**
> This brief proposed a new sibling skill (`design-handoff-adopt`). That proposal was **rejected** — twice — by the LLM Council. The settled stance: build no adopt-automation (no skill, no DSB mode, no command); Claude Design bundles stay authoritative; tokens reach a real product via a one-time product-side `cp`; revisit only on a 2nd bundle (Rule of Two). The kept knowledge lives in [`design-handoff-adoption.md`](design-handoff-adoption.md). Kept below as the record of the original proposal and the evidence that informed the decision.

**Status:** proposal, pre-decision. Written 2026-06-09 as input to an LLM Council evaluation.
**Question for the council:** Is a **new sibling skill** the best path for ingesting Claude Design bundles, or is there a better one? If a new skill is right, what are the greatest opportunities and risks?

---

## 1. What changed (why this exists)

Rex's design workflow has shifted. He increasingly mocks up products in **Claude Design** (`claude.ai/design`) — an AI design tool that produces HTML/CSS/JS prototypes — and exports a **handoff bundle** for a coding agent to implement. He wants to feed these bundles into the `prd-to-product` skill kit (`prd-creator` → `context-engineering` → `design-system-bootstrap`) and have them be first-class input, not something the flow fights.

The trigger was a real bundle: `the-council/spikes/claude-design/` (a Chrome-extension + web-app product called The Council). It was analyzed in full before this brief.

## 2. What a Claude Design bundle actually contains (evidence)

From the analyzed bundle:

- **A `README.md` aimed at coding agents** — declares "handoff bundle from Claude Design," names the primary file the user had open, and instructs: *recreate pixel-perfect in whatever tech fits the target codebase; don't copy the prototype's internal structure.*
- **HTML/CSS/JS prototypes** — React via Babel-standalone in the browser (unpkg React + `type="text/babel"`), not a build.
- **Zero Tailwind.** Styling is **plain CSS driven by a rich `:root` custom-property token system** — ~40 tokens across three CSS files: semantic palette, `oklch()` accents, font stacks, motion easings, a CRT-intensity scalar. Components style via ~442 semantic `className`s + ~82 inline styles.
- **It already *is* a design system** — more distinctive and opinionated than our `tokens.css` template generates, and it already does **class-based theming** (`body.twilight` re-binds the same token names; a runtime colorway tweak exists).
- **Multiple aesthetics in one bundle** — a light "Session" palette and an amber/cyan "Terminal" CRT palette are *different* token systems, not one theme with variants.
- **A full PRD** (`uploads/PRD.md`) and ~27 screenshots as ground truth. Target stack per the PRD: Next.js 14 / Vercel.

## 3. Why the current flow is the wrong tool

`design-system-bootstrap` (DSB) is a **generate-from-scratch / extract-from-brand-assets** flow. It emits a `tokens.css`, three generic seed components (Button/Card/Input), and a `DESIGN_SYSTEM.md`. Its own description says *"do not use for migrating an existing token system."* A Claude Design bundle **is** an existing token system. Pointing DSB at it is the **qventus class** all over again — the 2026-06-08 qventus post-mortem flagged "the skill does not migrate an existing system" and "needs a bootstrap-from-nothing project." The workflow shift turns that documented gap from an edge case into the **main road**.

Concretely, the current flow would:
- regenerate a palette when a richer one already exists (strictly worse — loses the `oklch` accents, the theming, the motion tokens);
- emit generic Button/Card/Input when the real components are the council cards / terminal stage / side panel;
- ignore the bundled PRD and screenshots entirely.

## 4. Proposed solution

A **new sibling skill** — working name `design-handoff-adopt` — that is the **inverse of bootstrap: an adopt/codify (import) flow.** Single-purpose, sibling to `prd-creator` / `context-engineering` / `design-system-bootstrap`, reusing DSB's `tokens.css` shape, `DESIGN_SYSTEM.md`, and write-guard machinery.

**Detection (cheap):** a Claude Design bundle ships its tell-tale `README.md` ("handoff bundle from Claude Design") + token-CSS + component prototypes. Presence → branch to extract/codify instead of generate.

**Flow contract:**
1. **Ingest & detect** — recognize the bundle; locate the primary design file (the README names it), CSS token sources, component prototypes, screenshots, and any bundled PRD.
2. **Extract, don't generate** — transcribe the `:root` token block(s) into our two-tier `tokens.css` shape (primitive → semantic), **preserving values exactly** (`oklch` and all). A structuring job, not a generation job.
3. **Reconcile multiple aesthetics** — when a bundle carries more than one token system, ask: theme variants over shared semantic tokens (like `body.twilight`), or competing directions to choose between? New decision point the current flow lacks.
4. **Recreate components from prototypes, not templates** — map the bundle's real components to the target framework, wired to the extracted tokens. Closer to a design-handoff/implementation task than a bootstrap. Honors the README's "recreate, don't copy structure."
5. **Emit under the write guard** — when this lands in an existing/target repo it must not clobber; the D-007 "agent performs the merge itself with diff-confirm" behavior is exactly right here.

**Tailwind decision (proposed, to be logged):** Claude Design emits token-CSS → default to the **vanilla CSS-vars** path. Keep the Tailwind path available only for *target repos that already use Tailwind*; **never let Claude Design input drive a Tailwind translation** (reverse-engineering `oklch` tokens + bespoke CSS into utilities is lossy and destroys the distinctiveness).

**Chain implication:** a Claude Design bundle can satisfy *both* the PRD input (it bundles a PRD) and the design input. That changes where the `prd-creator → context-engineering → design-system-bootstrap` chain starts — a direct input to the open `/idea-to-product` orchestration question.

## 5. Alternatives considered (for the council to weigh)

- **A. New sibling skill** (proposed). Pro: single-purpose, matches the kit's architecture; avoids fighting DSB's "don't migrate" guardrail. Con: a fourth skill; the chain-composition problem (skills don't auto-compose) gets one more node; some machinery duplicated with DSB.
- **B. A second *mode* inside DSB** (detect-and-branch: generate vs adopt). Pro: one skill, shared machinery, no new node. Con: doubles DSB's surface and directly contradicts its stated "do not migrate an existing token system" purpose; violates the single-purpose principle the kit holds elsewhere.
- **C. No new capability — handle it as a one-off implementation task each time** (treat the bundle as a normal design handoff, no skill). Pro: zero kit change; Claude Design's own README already instructs the agent well. Con: no token-normalization discipline, no reuse of `tokens.css`/`DESIGN_SYSTEM.md` conventions, no write-guard arming, reinvented every time.
- **D. Defer** — wait for a second real bundle before building (the kit's own "fix on the second instance" discipline). Pro: avoids building for a sample size of one. Con: the workflow shift is already real and recurring; the qventus gap is documented.

## 6. Open questions the council should pressure-test

1. Is a **new skill** actually the best path, or is mode-in-DSB (B) or no-skill (C) stronger given the kit's chain-composition weakness?
2. Is the **detection** robust, or will it misfire (e.g., a bundle without the README, or a non-Claude-Design token-CSS input)?
3. Is **"extract/transcribe, don't generate"** a real, repeatable procedure, or does it collapse into bespoke judgment every time (in which case a skill adds little over the README)?
4. The **multiple-aesthetics reconciliation** — is that a tractable skill step or a human-only decision?
5. **Component recreation** is genuinely hard (pixel-perfect from prototypes). Does a skill meaningfully help there, or is that just implementation work no skill improves?
6. Does this deepen the **chain-composition problem** (now four manually-composed skills), and does it strengthen or weaken the case for the `/idea-to-product` orchestrator?
7. What's the **honest ceiling** — what will this skill reliably do well vs. what will still need human judgment every run?

## 7. Constraints / context for the council

- Single developer (Rex). Skills are markdown-only generators that scaffold *shape, not product content*.
- The kit has a documented weakness: the three skills don't auto-compose; the user manually chains them. A fourth skill adds a node.
- Recent load-bearing work: D-005/D-006 write-guard (non-destructive, hook-enforced) and D-007 (agent-performed merges with diff-confirm). The adopt flow would lean on all three.
- Cross-references: [`docs/retros/2026-06-08-qventus-post-mortem.md`](retros/2026-06-08-qventus-post-mortem.md), [`BACKLOG.md`](../BACKLOG.md) (chain-composition + `/idea-to-product` items), [`skills/design-system-bootstrap/`](../skills/design-system-bootstrap/).
