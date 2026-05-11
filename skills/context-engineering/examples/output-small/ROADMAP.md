# Roadmap — simple-form

What's left, in priority order. Read this at the start of every session alongside the most recent retro.

Check off tasks as they are completed. Mark phases done only when all tasks are checked and the done-when criteria is met.

---

## Phase 1: Ship deployable shell to Vercel

**Goal:** Confirm production is reachable and the build pipeline works before any feature work begins. Catches deploy-environment surprises (env loading, build step, framework adapter, CDN config) on day one rather than month six.

- [ ] Push the repo to GitHub.
- [ ] Connect the repo in the Vercel dashboard; confirm the framework preset is detected.
- [ ] Push a trivial commit; confirm the auto-deploy fires on push to `main`.
- [ ] Open the Vercel-assigned URL; confirm the page loads with no build errors.
- [ ] Add `<h1>simple-form</h1>` to the landing page; push; confirm production shows the change.
- [ ] Tag the commit `v0.0.1-deployed`.

**Done when:** Production URL serves a page containing the project name in an `<h1>`.

---

## Phase 2: MVP launch

**Goal:** Replace the third-party iframe form with the in-house form on the live portfolio site.

- [ ] Wire `/api/contact` to Resend, deploy, swap iframe out of portfolio site.

**Done when:** Form is live on portfolio site, Jordan has received a successful test submission, iframe is removed.

---

## Open decisions

Decisions deferred until more information is available. Move into `docs/DECISIONS.md` when resolved.

(none)

## Cross-references

- Product requirements: `docs/PRD.md`.
- Architecture and data model: `docs/ARCHITECTURE.md`.
- Mid-session deferred items: `docs/PARKING_LOT.md`.
- Decisions log: `docs/DECISIONS.md`.
- Session retros: `docs/retros/`.
