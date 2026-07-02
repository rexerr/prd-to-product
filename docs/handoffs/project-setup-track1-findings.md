# Track-1 findings — Project-setup system (premise verified)

**Written:** 2026-07-01 · **Feeds:** [`project-setup-system-handoff.md`](project-setup-system-handoff.md) §6 Track 1 · **Status:** research finding, not a decision.

Track 1 of the project-setup investigation asked whether the setup gap (stack / security / audits / tests / instrumentation, plus agent-environment parity) is a **recurring structural step** — which earns a connective layer per Rule-of-Two — or a one-off. Answered by reading two of Rex's real projects across two stacks and two lifecycle stages.

## Method

- **`seance`** (`~/Sites/seance`) — a native Swift/SwiftUI iOS app, **shipped to TestFlight** (builds 1–3). Setup pain visible in retrospect, encoded in its `CLAUDE.md` and ~19 retros.
- **`cat-tracker` / "Strays"** (`~/Sites/cat-tracker`) — a React Native / Expo app, **frozen at the trio→build seam**: PRD + context scaffold + design system all landed 2026-06-22, then stops. No `package.json`, no Expo, no `node_modules`, no `ios`/`android`. The gap shown *live*, not in retrospect.

## The recurrence test — the categories recur, the specifics share nothing

| Category | seance (native iOS, shipped) | Strays (RN/Expo, pre-build) |
|---|---|---|
| **Stack standup** | Manual Xcode project + gotchas: Info.plist ↔ Xcode-16 synchronized-groups collision, manual `.xcscheme` TestAction, ASCII scheme name, signing/provisioning | Entire Expo app un-stood-up; `global.css` / `tailwind.config.js` / 3 `.tsx` components emitted but **inert** (no runtime to host them) |
| **Deploy** | $99 Apple Developer Program blocked TestFlight; compliance flag + privacy reason codes discoverable-only | **No GitHub remote even exists** (`github_repo_url` is a placeholder); EAS / store path unset |
| **Tests** | `SeanceTests` target + manual `.xcscheme` TestAction; **agent cannot run tests headless** (Pseudo-Terminal / no PTY) — a standing tax | No harness at all |
| **Secrets** | `block-secrets-commit` hook + `.xcconfig` gitignore; certs/profiles never committed | `block-env-commit` hook (scaffold-emitted) |
| **Backend / instrumentation** | Hostless by design — **N/A** | Supabase planned, **unset**; instrumentation unaddressed |
| **Agent parity (verification)** | simctl build→screenshot→read-PNG wins layout; render fidelity (WKWebView WebGL) needs Rex's on-device eye; `devicectl --console` for logs; XcodeBuildMCP banned | "visual confirmation = the running Expo app" — **inert until the stack exists** |

**Verdict: premise verified.** The gap is structural, not a `seance` one-off. The *shape* recurs across two completely different stacks while every *specific* differs — the exact signature that earns a **thin, stack-aware connective layer**, and rules out both "do nothing" and "one hardcoded checklist."

## Three findings that shape the design

1. **The layer's job is sequencing + standup, not just checking.** Strays proves the trio produces stack *decisions* (D-010 NativeWind, D-011 fonts, D-012 palette) and design *artifacts* out of order relative to the stack that must host them — the design-system skill emitted RN components that can't compile because the RN project doesn't exist. The connective layer must own the sequence: **stand up the stack → wire the already-emitted design system into it → add backend → gate tests/deploy.** Today that's a hand-written BACKLOG note the developer improvises.

2. **Instrumentation and backend are project-type-conditional** (seance: neither; Strays: both). The layer must *ask per project type*, never assume — confirms the coverage-map nuance added 2026-07-01.

3. **"Verify it ran" must route to the capable actor.** seance's PTY wall + fidelity gate and Strays' "verification = the app that doesn't run yet" say the same thing: the agent often *can't* run or judge the check itself, so verification routes to Rex, a GUI, or CI. A real design constraint, not a detail.

## Corrections to the handoff's coverage map

- **Security was overstated as "thin."** seance stood up a secrets hook, `PrivacyInfo.xcprivacy` (reason code `CA92.1`, discovered from Apple's spec with no error hint), export-compliance, and a *trust*-based feature rejection (killed a mic waveform as creepy). Security setup **happens** — it's manual, stack-specific, and gotcha-laden, not absent.
- **Audits were used but never guaranteed** — Apple-skill audits (concurrency/webkit/navigation/animation) + a SwiftLint auto-fix hook + staged strict-concurrency ran ad-hoc, confirming "partial, not project-aware or guaranteed to run."

## What's next

- **"Compose what" (per stack) and "delivered how"** remain open — the latter is the blocked [Skill injection by project type](../../BACKLOG.md) row (plugin-vs-vendored), the costly + hard-to-reverse fork where [D-009](../DECISIONS_ACTIVE.md) says recommend a council.
- **Track 3 (scoped deep-research)** runs next, framed by what these two projects exposed: what already exists, per stack, for Expo/RN standup + EAS deploy, iOS standup + TestFlight, test-harness bootstrap, and secret/dep scanning — so the council chooses among real, named, maintained options rather than theory.
</content>
</invoke>
