# Medium example: Standup Digest

Abbreviated transcript. A SaaS-style tool with a real AI surface and a small but real brand-voice section. Brand content lands inline (three items). Decisions list is medium length.

---

**User:** Build me a PRD for "Standup Digest." It reads my Slack channels overnight and writes my morning standup update for me.

**Skill:** Running the PRD interview. First, let me check whether you have anything for me to read.

> Source-material question.

**User:** I have a notes doc. [Pastes 200-word note covering: target user is engineering managers, bored writing standups, want a draft they can ship in 30 seconds, monetization is later.]

**Skill:** Read it. The note covers the user, the problem, and a monetization stance. It does not cover the workflow, the stack, or success criteria. For the parts it covers I'll show you a draft to correct rather than ask from scratch; for the rest I'll ask.

Here's the pitch drawn from your note: Standup Digest reads engineering managers' Slack channels overnight and drafts a morning standup they can ship in about 30 seconds. The user is engineering managers, the problem is the daily writing tax, and monetization is deferred. Edit anything that's off, especially the user and the problem.

**User:** Close. Widen the user to engineering managers and senior engineers on teams that run async standup. Today they either skip days or paste yesterday's update with the date changed. Monetization stance is right.

**Skill:** Updated. The workflow, the stack, and success criteria aren't in the note, so I'll ask those.

> Workflow questions.

**User:** [Five-step workflow: nightly Slack scrape → AI summarizes activity per user → user opens app at 9am → reviews and edits the draft → posts back to standup channel with one click.]

**Skill:** Captured. Open question swept: "What's the cutoff time for 'overnight' if a user is in a different timezone." Captured.

> Scope.

**User:** V1: one Slack workspace per user, AI draft generation, edit-and-post flow, basic auth. Cuts: multi-workspace, team analytics, custom prompt tuning, integrations beyond Slack. Deferred: GitHub PR activity in the digest, Linear issue activity, weekly retrospective rollup.

**Skill:** Captured, noted as a decision to confirm later: V1 supports one Slack workspace per user.

> Architecture.

**User:** Next.js on Vercel. Supabase for auth and Postgres. Slack OAuth. Anthropic API for the summarization. Inngest for the overnight job.

**Skill:** Captured, noted as a decision to confirm later. Open question: "Whether Inngest scales to per-user nightly jobs at the cost we want." Asked about AI surface specifics.

**User:** One AI call per user per night. Server-side. Claude Haiku for cost. Prompt is templated.

**Skill:** Captured, noted as two more decisions to confirm later. Open question: "Whether Haiku's quality on summarization-of-Slack is sufficient." Captured.

> Decisions read-back.

[Six decisions confirmed: workspace-per-user, full stack, AI server-only, Haiku for cost, no custom prompts in V1, free tier with usage cap.]

> Brand and voice.

**User:** Audience is engineering managers, terse and time-pressed. Three tone attributes: terse, useful, never cute. Vocabulary lock: it's a "digest," not a "summary," not a "report." That's it for brand.

**Skill:** Three items captured (audience plus three tone attributes counts as one tone-attributes block plus one audience plus one vocabulary item, total three). Inline appendix per the placement rule.

> Success criteria and testing decisions.

**User:** Hundred users post a digest within their first three days. Drafts are accepted (posted with no edits) at least 30% of the time. Mean edit time under 60 seconds. No support tickets about "the AI hallucinated activity that didn't happen." On testing: no dedicated suite for V1, I'll verify the digest-generation path and the no-hallucination guard against real Slack activity during the first-week rollout.

**Skill:** Captured. Last criterion is a watch-not, kept as success criterion (checkable: count tickets matching that complaint). Testing decisions captured: digest-generation path is the part that matters most, verified by manual review during rollout plus the no-hallucination criterion above, no automated suite named for V1.

> Outline confirmed. Writing PRD.

[PRD emits 12 sections plus inline brand-and-voice appendix. Six decisions, four open questions, four success criteria.]

> Output summary.

PRD generated at docs/PRD.md.

Sections that emitted: 13 (including inline Brand and voice appendix).

Sections that were skipped:
- Supporting documents. Reason: no sibling file, no external sources named.

Decisions captured: 6. Top three by criticality:
- D-002 Stack is Next.js on Vercel, Supabase for auth and Postgres, Slack OAuth, Anthropic for AI, Inngest for jobs.
- D-003 AI calls are server-only via API route.
- D-001 V1 supports one Slack workspace per user.

Open questions: 4. Top blockers for V1:
- Whether Haiku's quality on Slack-summarization is sufficient.
- Whether Inngest scales to per-user nightly jobs at target cost.
- Cutoff time for "overnight" across timezones.

Brand and voice placement: inline appendix.

Files written:
- docs/PRD.md

Next step:
Run the context-engineering skill against this PRD.
