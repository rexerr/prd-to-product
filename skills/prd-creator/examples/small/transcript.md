# Small example: Morning Intent

Full transcript of a prd-creator run for a single-purpose daily tool. The user is the developer building it for themselves. No brand work, no AI surface, tight V1.

---

**User:** I want to build a morning intent tracker. Just for me. Use the prd-creator skill.

**Skill:** Running the PRD interview. Cluster 0 first.

Before we start, do you have a working brief, research dump, transcript, message thread, or notes you want me to read first. Paste, link, or tell me there's none.

**User:** None. It's just an idea.

**Skill:** Acknowledged. Moving to cluster 1, the elevator pitch.

In one paragraph, what is this product. Lead with what it does, then who it is for, then why it exists.

**User:** A tiny tool I open every morning. I type three intents for the day. At 6pm it texts me a check-in: did I do them. That's it. It's for me, because I keep telling myself I'll do focused work and then drift, and writing intents on paper doesn't follow me into the afternoon.

**Skill:** Got it. Two more cluster 1 questions.

Who specifically is the V1 user. You said "for me," confirming that V1 ships single-user and the only user is you.

**User:** Yes. Single-user. Me.

**Skill:** What are you currently doing instead.

**User:** Writing intents in a notebook every morning. Forgetting the notebook by 11am. Sometimes I open Notes on my phone but I never look at it again.

**Skill:** Captured. Cluster 1 summary: Morning Intent is a personal daily tool that captures three intents each morning and texts a check-in at 6pm. V1 is single-user (you). The current workaround is paper notebooks and the Notes app, both of which you abandon mid-day.

Anything you do not yet know about the product, user, or problem that would change the build.

**User:** No. It's clear.

**Skill:** Confirmed. Moving to cluster 2, the main workflow.

Walk me through the V1 happy path. What does the user do, step by step, the first time the product works for them.

**User:** I open the URL on my phone in the morning. I type three intents. I close the tab. At 6pm I get an SMS with my three intents and a yes/no for each. I tap yes or no and that's it. Maybe it shows me a streak.

**Skill:** Five steps, clean. Captured.

Anything you do not yet know about the workflow.

**User:** Whether the SMS check-in should be 6pm fixed or configurable. Probably fixed for V1.

**Skill:** Capturing as a decision: D-001 candidate, "Check-in time is 6pm fixed in V1." I'll review this in cluster 5. Cluster 2 summary: five-step happy path from morning capture through evening SMS check-in plus optional streak display.

Moving to cluster 3, scope.

What is V1. Bullet list of capabilities, each one checkable.

**User:** Authless single-page app at a URL only I know. Three text inputs that save to a database. A scheduled job at 6pm that sends an SMS with my intents and yes/no buttons. Tap yes or no, it saves. Streak counter that resets if I miss a day.

**Skill:** Captured.

What did you consider for V1 and explicitly cut.

**User:** Multi-user accounts. AI suggestions for intents. Calendar integration. Anything beyond yes/no on the check-in. Configurable check-in time.

**Skill:** Captured.

What is V2 or later.

**User:** Maybe AI nudges based on patterns. Maybe a weekly review. Honestly I don't know if there's a V2.

**Skill:** Capturing "AI nudges based on patterns" and "weekly review" as deferred. Noted that V2 is uncertain.

Anything you do not yet know about scope.

**User:** No.

**Skill:** Cluster 3 summary: V1 is single-page authless app with three intent inputs, scheduled SMS at 6pm, yes/no response, streak counter. Cuts include multi-user, AI suggestions, calendar integration, anything beyond yes/no. Deferred items noted.

Moving to cluster 4, architecture and stack.

What is the stack.

**User:** Next.js on Vercel. Postgres on Neon. Twilio for SMS. That's it.

**Skill:** Captured. D-002 candidate, "Stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS."

What integrations does V1 require.

**User:** Twilio for the SMS. That's the only external thing.

**Skill:** Captured.

What is the AI surface, if any.

**User:** None in V1.

**Skill:** Captured. D-003 candidate, "No AI surface in V1."

Anything you do not yet know about architecture.

**User:** How to schedule the 6pm job. Vercel cron probably but I haven't checked.

**Skill:** Capturing "How to schedule the 6pm job. Vercel cron is the lean candidate" as an open question. Cluster 4 summary: Next.js on Vercel, Postgres on Neon, Twilio SMS, no AI in V1. One open question on the scheduler.

Moving to cluster 5, decisions consolidation.

I captured these decisions during clusters 1-4. Confirm, edit, or drop each.

- D-001: Check-in time is 6pm fixed in V1. Rationale: simplifies V1, configuration adds settings UI you do not want yet.
- D-002: Stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS. Rationale: matches your existing tooling.
- D-003: No AI surface in V1. Rationale: the value of V1 is friction-free capture, not AI features.

**User:** All three confirmed. Add: D-004, no auth in V1. Just an obscure URL.

**Skill:** Added.

- D-004: No auth in V1, access via obscure URL only. Rationale: single-user product, auth is overhead with no benefit.

Cluster 5 summary: four decisions locked. Moving to cluster 6, brand and voice.

**User:** Skip. It's just for me, no copy to write.

**Skill:** Skipping cluster 6. Moving to cluster 7, success criteria.

What does V1 success look like.

**User:** I use it every morning for two weeks straight without dropping a day. The 6pm SMS arrives reliably and I tap yes or no without thinking about it. Streak counter is accurate.

**Skill:** Captured three criteria. Anything you do not yet know about success.

**User:** No.

**Skill:** Cluster 7 summary: success is two weeks of daily use, reliable SMS, accurate streak.

All clusters complete. Proposed PRD outline:

Sections that will emit:
- Product summary (cluster 1)
- Target users (cluster 1)
- Core problem (cluster 1)
- Main workflow (cluster 2)
- Version 1 scope (cluster 3)
- Out of scope (cluster 3)
- Deferred capabilities (cluster 3)
- Architecture and stack (cluster 4)
- Decisions already made (cluster 5, four entries)
- Open questions (sweep, one entry)
- Success criteria (cluster 7)

Sections that will be skipped:
- Brand and voice. Reason: cluster 6 not run, no user-facing copy.
- Supporting documents. Reason: no sibling file emitted, no external sources named.

Path: `docs/PRD.md`. Confirm to write.

**User:** Confirm.

**Skill:** Writing. [PRD.md is shown at `examples/small/PRD.md`.]

PRD generated at docs/PRD.md.

Sections that emitted:
- Product summary (from cluster 1)
- Target users (from cluster 1)
- Core problem (from cluster 1)
- Main workflow (from cluster 2)
- Version 1 scope (from cluster 3)
- Out of scope (from cluster 3)
- Deferred capabilities (from cluster 3)
- Architecture and stack (from cluster 4)
- Decisions already made (from cluster 5)
- Open questions (from sweep)
- Success criteria (from cluster 7)

Sections that were skipped:
- Brand and voice. Reason: cluster 6 not run, no user-facing copy.
- Supporting documents. Reason: no sibling file, no external sources.

Decisions captured: 4. All:
- D-001 Check-in time is 6pm fixed in V1.
- D-002 Stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS.
- D-003 No AI surface in V1.
- D-004 No auth in V1, access via obscure URL only.

Open questions: 1.
- How to schedule the 6pm job. Vercel cron is the lean candidate.

Brand and voice placement: not run.

Files written:
- docs/PRD.md

Next step:
Run the context-engineering skill against this PRD to scaffold AGENTS.md, CLAUDE.md, .claude/rules/, and docs/. The PRD's decisions and architecture sections become cluster 0 input; you will not be asked to restate them.
