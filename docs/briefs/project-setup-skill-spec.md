# Spec — the `project-setup` skill (draft for approval)

**Written:** 2026-07-01 · **Status:** draft spec, not yet built · **Feeds:** [`../handoffs/project-setup-system-handoff.md`](../handoffs/project-setup-system-handoff.md) · **Grounded in:** [Track-1 findings](../handoffs/project-setup-track1-findings.md), [Track-3 research](../handoffs/project-setup-track3-research.md), [council](../council/council-report-2026-07-01-project-setup.html).

---

## First principle (Rex's correction, 2026-07-01 — supersedes the council's "hand-notes" baseline)

**Rex is not the developer. Claude is.** The entire reason this skill exists is so Rex invokes *one thing* and Claude does the engineering. Any design that requires Rex to hand-author setup, or to judge an *engineering* pass/fail signal, is **wrong by definition** — it defeats the purpose. The council floated "just hand-write setup notes twice" as a cheap baseline; that baseline is **struck**. Rex judges only what a designer can judge: *does it look right, does it work when I tap it, ship y/n.* Everything else routes to Claude or to an automated check.

**Failure this prevents:** re-inventing the exact burden the skill is meant to remove — pushing engineering work or engineering judgment back onto a non-engineer.

---

## What it is (one line)

A **fourth skill**, sibling to the trio, invoked **after** `context-engineering`. Rex runs `/project-setup`; Claude stands up the stack, wires in tests/security/deploy by composing externally-maintained tools, verifies each step routed to whoever can actually judge it, and reports status in plain language.

## Rex's operating manual (the whole thing, for Rex)

1. Run your skills in order: `prd-creator` → `context-engineering` → `design-system-bootstrap` → **`/project-setup`** (new).
2. Answer at most one plain question ("is this iOS, a cross-platform app, or web?") if it can't be inferred.
3. Read the status report Claude gives back (✅ done / ❌ missing, plain language).
4. When asked, do the *only* things that need your eye: look at a screen, tap through the app, say "ship it."

That's it. No terminal, no config, no engineering calls.

## What Claude does when it runs (the flow)

1. **Detect project type** from the repo + PRD (iOS / React Native-Expo / web). Ask Rex once only if genuinely ambiguous.
2. **Stand up the stack** — run the setup tools (Claude executes; see per-stack recipes).
3. **Wire in the essentials** — test harness, the free security defaults, a deploy path.
4. **Verify each step, routed to the capable actor** — engineering checks run in Claude's shell or in CI; anything Claude's shell can't run (e.g. iOS headless tests) routes to CI or is flagged, *never* dumped on Rex; visual/product checks route to Rex.
5. **Report** — a plain ✅/❌ status table, in Rex's language, plus what (if anything) needs his eye.

## Design principles (why it's shaped this way)

- **Compose, don't author.** The skill calls externally-maintained tools; it holds only the durable *questions* ("is a test harness present? did it run green?") and the *composition order* — **never version pins**. *Failure it prevents:* a non-engineer maintaining perishable engineering config that silently rots (the prior-council guardrail).
- **Verification routes to the capable actor.** Engineering → Claude/CI. Product/visual → Rex. *Failure it prevents:* a verification step that terminates at someone who can't read the signal = theater (the council's sharpest catch).
- **Vendored delivery.** Installs as a skill exactly like the trio — no plugin/marketplace plumbing yet (revisit at more projects/consumers). *Failure it prevents:* paying a packaging tax before it's earned.
- **Markdown-only.** The skill is instructions Claude follows, not a program it ships. *Failure it prevents:* breaching the markdown-only invariant ([D-001]).
- **Every rule cites its failure mode** (as above), per the repo idiom.

## Per-stack recipes (what Claude composes)

Each row: capability → the maintained tool composed → **who verifies** → what red/green looks like. This table is the durable core — tools may be swapped as they change; the *questions* don't.

### React Native / Expo  (pilot stack — Strays lives here)
| Capability | Composes | Who verifies | Red / Green |
|---|---|---|---|
| Stack standup | `create-expo-app` (Expo Router + TS); NativeWind via `rn-new` | Claude (runs `expo` build) | Red = build error · Green = app boots |
| Tests | `jest-expo` + Testing Library; Maestro (E2E) | Claude (runs `jest`) | Red = fail · Green = suite passes |
| Security | GitHub push-protection + Dependabot (defaults) · Gitleaks · Renovate (minor-automerge, majors gated) | CI (automated) | Red = alert/leak · Green = clean |
| Deploy | EAS Build / Submit / Update | Claude (build) + **Rex** (installs, taps) | Red = build fails · Green = installs & runs |

### Native iOS (Swift/SwiftUI)
| Capability | Composes | Who verifies | Red / Green |
|---|---|---|---|
| Stack standup | XcodeGen *or* Tuist (project-as-code) + xcodes/mise (pin Xcode) | Claude (`xcodebuild build` — works headless) | Red = build error · Green = builds |
| Tests | Swift Testing / XCTest | **CI or Xcode GUI** (headless broken on Xcode 26 — PTY wall) — *never Rex* | Red = fail · Green = passes |
| Security | privacy manifest · secrets commit-hook · export-compliance flag | Claude (presence) + CI | Red = missing/leak · Green = present |
| Deploy | Xcode Cloud (default) *or* Fastlane | Claude (archive) + **Rex** (installs on iPhone, taps) | Red = archive fails · Green = installs & runs |

### Web
Not yet researched to the same depth — **stub**. Fill from a real web project before claiming coverage (the enumerate-before-claiming discipline).

## What the skill never does (scope guardrails)

- Never authors product code (app screens, business logic) — that stays the developer-session job, same line as `context-engineering`.
- Never freezes a version pin into the skill body (pins live in the *project*, chosen at run time from current best practice).
- Never asks Rex an engineering judgment, and never hands him a check his eye can't read.
- Never re-imports this-repo-internal machinery into the shipped skill ([D-013]/[D-019] line).

## Forks — resolved / deferred

- **Build vs compose** → COMPOSE (settled by council).
- **Delivery** → VENDORED now; plugin/marketplace revisited at more projects (deferred).
- **Starter lane** (RN official-minimal vs Obytes; iOS XcodeGen vs Tuist) → **deferred, decision rule:** pick the company-backed maintained option when Rex can't judge staleness; default to the simplest readable one otherwise. Settle per-stack at build time.
- **iOS submission** (Fastlane vs Xcode Cloud) → **deferred, decision rule:** Xcode Cloud until the free tier is outgrown (Fastlane is under-resourced).

## Open questions to resolve before/at build

1. **cruft-style drift-binding — in or out for v1?** The council flagged it may propagate *pins* not *questions* (contradicting the compose principle). **Recommendation: OUT of v1** — ship the question-set + recipes first; add drift-binding only if brownfield-drift actually bites. (Keeps v1 honest to the compose principle.)
2. **v1 scope = one stack, end to end.** Recommendation: build the **RN/Expo** recipe first and prove it by standing up **Strays** for real; generalize to iOS/web after. *Failure it prevents:* a theoretical 3-stack skill that's never exercised.
3. **Where the status report lives** — chat-only, or a written `SETUP-STATUS.md` in the project? (Lean: written, so it survives the session — matches the repo's durable-artifact instinct.)

## Recommended build path

**v1:** RN/Expo recipe only → dogfify by running it (or its steps) against Strays → capture what broke → then generalize. Nothing ships to the other stacks until the RN recipe has stood up one real app.
</content>
