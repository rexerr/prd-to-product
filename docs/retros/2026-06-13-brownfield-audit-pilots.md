# Retro — 2026-06-13 08:43 CDT — brownfield context-drift audit, pilots #1–#3   (2nd session of the day)

Picks up the brownfield-audit backlog item the furnace-plan session (1st session, 07:37) handed off. Rex redirected the pilot targets by hand (chose `epost-intelligence-feed`, then `field-society-demo`, then `tex`) rather than the scan-and-pick the backlog proposed — his gate, exercised. He also pushed for a third pilot after I'd written up two, which turned out to be the most valuable one.

## What was completed

- Ran the brownfield context-drift audit **by hand on two real projects** (the parked pilot), read-only, fanned the two-sided extraction (current-standard vs actual-state) out to parallel subagents, classified the diff by KIND myself.
- **Pilot #1 — `epost-intelligence-feed`:** report [`docs/audits/2026-06-13-epost-context-drift.md`](../audits/2026-06-13-epost-context-drift.md). Well-built earlier-generation structure; raw diff ~11 gaps → 4 worth backporting after classification. Headline false-positive: epost *deliberately* lets Codex write (`workspace-write`), the opposite of this repo's non-Claude-read-only rule — a naive diff flags it as a defect.
- **Pilot #2 — `field-society-demo`:** report [`docs/audits/2026-06-13-field-society-demo-context-drift.md`](../audits/2026-06-13-field-society-demo-context-drift.md). Deliberately different kind (not-git, scaffold-only, single-agent) to stress the rubric.
- **Pilot #3 — `tex`:** report [`docs/audits/2026-06-13-tex-context-drift.md`](../audits/2026-06-13-tex-context-drift.md). The decisive one: `tex` was **never scaffolded by context-engineering** — a hand-rolled "light ritual harness" for skill curation. **Out of scope.** A checklist diff would produce a ~12-item false-positive cascade (all intentional omissions) and tempt bloating a deliberately-minimal repo — actively harmful, not just noisy.
- **Cross-pilot finding (the actual deliverable):** the safe-backport tier is **rubric-stable** (6 items identical across the two in-scope projects); the judgment tier **flips on project facts, not the checklist**, reducing to a **5-field project profile** `{under-git, multi-agent, has-product-code, has-secrets/.env, has-deploy-target}`. **Pilot #3 added the missing GATE:** a **field 0 — `opted-into-the-standard?`** — must run before the profile; if a project never opted in, the audit reports "not a drift target" and stops. Final design: **(0) gate → (1) profile → (2) diff → (3) classify.** Step 0 is the difference between a useful tool and a harmful one — and only a never-scaffolded target could surface it, which is why the 3rd pilot mattered.
- Updated [`BACKLOG.md`](../../BACKLOG.md) to fold in all three pilots, the cross-pilot design, Rex's decisions, and a sharpened promotion trigger. Committed + pushed the audit bundle (`5e2c970`).
- **Second half — skill-location decision (spun out of pilot #3).** Auditing `tex` surfaced that the `frontend-er` skill it develops lives at `~/.claude/skills/frontend-er/` as an **unversioned, un-backed-up real directory**, while the three `prd-to-product` skills are symlinks into the versioned repo. Decided the pattern: skills under development live in a versioned `Sites/` repo and are symlinked into `~/.claude/skills/` (never a bare real dir); licensed skills (frontend-er's `motion.md` is purchaser-licensed) go in **private** repos. Rex will rename `Sites/tex` → `Sites/frontend-er`, vendor the skill in as `skill/`, symlink it back, and push to a private remote. Delivered a cold-start-sufficient migration brief (in chat) for him to paste into the `tex`/`frontend-er` project session — sequenced so nothing destructive precedes the backup, with the private-repo + licensing checks as hard gates.

## Failure this session

- **None of the four classic tags — but one honest process miss.** After pilot #2 I asserted "two data points were enough; a third would mostly confirm" and recommended stopping. Rex pushed for the third anyway, and `tex` falsified that prediction outright — it surfaced the field-0 gate (opted-into-standard?) that neither in-scope pilot could, because both *were* scaffolds. This is a mild instance of the **same T2 failure the furnace audit indicts**: asserting sufficiency ("enough data") I hadn't verified. The human gate caught it. Lesson logged: "N samples is enough" is itself an unverified claim when every sample so far shares a hidden property (here: both were CE scaffolds). Otherwise the method worked as designed — by-hand classification caught all the false-positives (epost Codex-writes, field-society no-Codex, the entire tex cascade) a mechanical diff would have shipped as defects.

## Key decisions made (Rex-gated)

- **Fix nothing in any of the three yet.** Tier-A backports captured in each report's "Open decisions" for later promotion. All three projects untouched (read-only).
- **Don't build `/audit-context` yet — hold for a real drift-fix need (Rule of Three / wait for the pain).** The shape is now fully *designable* (gated 4-step: gate → profile → diff → classify) but demand isn't proven. Same furnace lesson: earn the build. Promotion trigger: "a real project's drift causes actual friction."
- **Three pilots, not two.** #1/#2 surfaced the 5-field profile; **#3 surfaced the field-0 gate** that makes the difference between a useful and a harmful tool. Stopping at two would have shipped a design that mis-fires on every hand-rolled repo.
- **Post-close-out: build DECLINED, not held ([D-013](../DECISIONS.md)).** After the formal close-out, Rex called it: the skill automates a *one-time* catch-up across a few old projects, so it never pays back — fix them by hand from the audit docs instead. Sharpening logged in D-013: the recurring "sweep as AI evolves" need he anticipates is *targeted propagation of a known delta*, a different problem than diffuse drift-auditing, so even that bridge wouldn't resurrect this design reflexively. Narrowed the BACKLOG's prior "build held" trigger so a future session can't rebuild it on a weak signal.

## Files changed

- `docs/audits/2026-06-13-epost-context-drift.md` — pilot #1 report (new)
- `docs/audits/2026-06-13-field-society-demo-context-drift.md` — pilot #2 report + cross-pilot synthesis (new)
- `docs/audits/2026-06-13-tex-context-drift.md` — pilot #3 report + field-0 gate finding + 3-pilot synthesis (new)
- `BACKLOG.md` — brownfield item updated to 3-pilots-done / build-held (modified)
- `docs/retros/2026-06-13-brownfield-audit-pilots.md` — this retro (new)
- (epost-intelligence-feed, field-society-demo, tex: **read-only, untouched**)

## Next session

- **Rex-side (different repo, not prd-to-product):** run the `frontend-er` migration brief in the `tex` project session — rename → vendor skill → symlink → private remote. The brief's step 6 (add the skill-location convention to `~/.claude/CLAUDE.md`) comes back here as a gated proposal once he's ready.
- Brownfield audit is **parked, not active** — no next-session pickup in this repo. It surfaces again only when real drift bites a project; then build `/audit-context` per the gated 4-step shape in the reports/BACKLOG.
- Background, passive: the **furnace-plan trial** keeps running (Cowork-graded) — use `/furnace-plan that` on real planning work and watch the signal accumulate. Don't promote to a hook until the catch-rate drop is real.
- Top of Backlog after this item: the validation-finding cluster (skill chain auto-compose / input auto-detect / `design-system-bootstrap` from-nothing test) — all awaiting a real project to exercise them.
