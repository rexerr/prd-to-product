# Example transcript: small project

A hypothetical small project taken through the generator end to end. Demonstrates the flat-shape output, the always-on patterns, and minimal conditional patterns.

**Project shape (per phase-1-prd.md validation):** single-page Next.js app, one API route, no AI, no UI beyond `globals.css`, single developer, Vercel deploy, no Codex.

The full output tree this transcript produces lives in `output-small/`.

---

## Cluster 1: project basics

> **Skill:** What's the project name?

**User:** `simple-form`

> **Skill:** One-paragraph description of what this project is, who it's for, what it does.

**User:** A single-page contact form for a freelance designer's portfolio site. Visitors fill a name, email, and message; the form posts to an API route that emails the designer via Resend. No database, no auth, no logged-in state.

> **Skill:** Local repo path on disk?

**User:** `/Users/jordan/Sites/simple-form`

> **Skill:** GitHub repo URL? Format: `https://github.com/<org>/<repo>`.

**User:** `https://github.com/jordan-d/simple-form`

> **Skill:** Visual confirmer name. The human who confirms UI changes in a running dev server. Default: Jordan.

**User:** Jordan

## Cluster 2: AI surfaces

> **Skill:** How many AI surfaces? Pick: 0 / 1 / 2-3 / 4+.

**User:** 0

(Cluster 2 ends; AI templates skipped.)

## Cluster 3: design system and UX

> **Skill:** Design system shape. Pick: tokens with linter / basic styling / none.

**User:** none

(Design heuristics question skipped.)

## Cluster 4: voice and tone

> **Skill:** Voice and tone rule needed?

**User:** no

## Cluster 5: conditional patterns

> **Skill:** Two at once: include `DECISIONS_ACTIVE.md`? Add a `Later / V2` section to `BACKLOG.md`? (Mid-session deferrals always have a home in `BACKLOG.md` — no separate file.)

**User:** DECISIONS_ACTIVE no, no V2 section.

> **Skill:** Three more: Codex used in workflow (regular / occasional / no)? Tiebreaker doc name (or none)? `product-rules.md` always-on rule needed?

**User:** Codex no. No tiebreaker doc. No product rules.

## Cluster 6: content fills

(The skill walks through the PRD, ARCHITECTURE, BACKLOG build plan, and stack content fills. Captured answers below.)

- `product_summary_paragraph`: A one-paragraph contact form on a portfolio site. Posts to an API route that emails Jordan via Resend.
- `target_users_list`: Visitors to the portfolio site who want to contact the designer. Mostly potential clients.
- `core_problem_paragraph`: The portfolio's old form was a third-party iframe that broke styling and had spam problems. This replaces it with an in-house form that matches the site design and uses Resend for delivery.
- `main_workflow_steps`: 1. Visitor lands on `/contact`. 2. Fills name, email, message. 3. Submits. 4. Client posts to `/api/contact`. 5. API validates, calls Resend, returns 200. 6. Client shows success message.
- `out_of_scope_list`: No CRM integration. No saved drafts. No file uploads. No spam captcha (relying on Resend's filtering plus honeypot field).
- `deferred_capabilities_list_or_none`: none
- `additional_stack_summary`: Resend for email delivery.
- `primary_data_flow_name`: Contact submission flow.
- `primary_data_flow_steps`: 1. Visitor submits form on `/contact`. 2. Client posts JSON to `POST /api/contact`. 3. API route validates name, email, message. 4. API calls Resend `emails.send`. 5. API returns success or error. 6. Client renders confirmation or error state.
- `data_persistence_paragraph`: No persistence. The app does not own a database. Submissions are forwarded to Resend and forgotten.
- `external_integrations_list_or_none`: Resend (email delivery).
- `folder_structure_summary`: Standard App Router. `app/contact/page.jsx`, `app/api/contact/route.js`, `lib/email.js` for the Resend client wrapper.
- `phase_1_name`: MVP launch.
- `phase_1_goal`: Replace the third-party iframe form with the in-house form on the live portfolio site.
- `phase_1_task_placeholder`: Wire `/api/contact` to Resend, deploy, swap iframe out of portfolio site.
- `phase_1_done_when`: Form is live on portfolio site, Jordan has received a successful test submission, iframe is removed.
- `architecture_rules_numbered_list` (flat shape):
  1. **Validate before sending.** The API route validates name, email format, and message length before calling Resend. Never forward an unvalidated payload.
  2. **No client-side Resend.** The Resend SDK only runs in `app/api/contact/route.js`. Never import it from a client component.
  3. **Honeypot field stays.** The hidden `website` field is the spam filter. Never remove it without a replacement.

## Confirmation

> **Skill:** Here's what I'll generate. Confirm before I write files.
>
> **Rule shape:** flat (no AI surfaces, no design system, single workflow, no voice rule).
>
> **Files to write:**
> - `AGENTS.md` (canonical, all rules inline + Codex section)
> - `CLAUDE.md` (thin pointer: @AGENTS.md)
> - `BACKLOG.md`
> - `.claude/commands/session-start.md`
> - `docs/PRD.md`
> - `docs/ARCHITECTURE.md`
> - `docs/DECISIONS.md`
> - `docs/retros/README.md`
>
> Proceed?

**User:** yes

## Output

See `output-small/` for the full file tree.
