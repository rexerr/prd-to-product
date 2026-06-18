# Morning Intent

## Product summary

Morning Intent is a personal daily tool that captures three intents each morning and sends an SMS check-in at 6pm asking which intents got done. It exists for a single user, the developer building it, who wants written intents that follow them into the afternoon instead of staying behind in a notebook.

## Target users

The developer building it. V1 ships single-user. No second user type planned for V1.

## Core problem

The user writes morning intents on paper or in Notes, then forgets the notebook by 11am and never re-opens the Note. The intent dissolves before lunch. A check-in pushed to the user's phone in the evening would force a yes-or-no reckoning and create a streak signal, both of which the current paper or Notes workaround cannot.

## Main workflow

1. User opens the app URL on their phone in the morning.
2. User types three intents into three text inputs and the inputs save automatically.
3. User closes the tab.
4. At 6pm the user receives an SMS containing the three intents, each with a yes-or-no prompt.
5. User taps yes or no on each, and the streak counter updates.

## Version 1 scope

- Single-page authless app at a URL only the user knows.
- Three text inputs for the day's intents, saved on change to the database.
- Scheduled job at 6pm sends an SMS via Twilio with the day's three intents.
- SMS reply or tap-through saves yes-or-no per intent.
- Streak counter that resets when a day is missed.

## Out of scope

- Multi-user accounts or auth flows.
- AI-suggested intents.
- Calendar integration.
- Anything beyond yes-or-no on the check-in (notes, partial credit, scoring).
- Configurable check-in time.

## Deferred capabilities

- AI nudges based on intent patterns over time.
- Weekly review surface summarizing the week's intents and completions.

## Architecture and stack

Next.js App Router on Vercel. Postgres on Neon for storage. Twilio for SMS send and reply handling. No additional services. The 6pm scheduled job runs as a Vercel cron route.

- Framework: Next.js App Router.
- Deploy target: Vercel.
- Database: Postgres on Neon.
- SMS: Twilio.
- AI surface: none in V1.

## Decisions already made

- **D-001** Check-in time is 6pm fixed in V1. Rationale: simplifies V1, configuration adds a settings UI not worth building yet.
- **D-002** Stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS. Rationale: matches existing tooling.
- **D-003** No AI surface in V1. Rationale: the value of V1 is friction-free capture, not AI features.
- **D-004** No auth in V1, access via obscure URL only. Rationale: single-user product, auth is overhead with no benefit.

## Open questions

- How to schedule the 6pm job. Vercel cron is the lean candidate but has not been verified for reliability against this use case.

## Success criteria

- User completes daily intent capture and 6pm check-in for two consecutive weeks without missing a day.
- The 6pm SMS arrives within five minutes of the scheduled time on every day during the validation window.
- Streak counter matches a hand-counted ledger across the two-week window.

## Testing decisions

No automated test suite in V1. Verification is the two-week live validation window named in success criteria, confirmed by hand that the 6pm SMS fires on time and the streak counter matches a hand-counted ledger. The parts that matter most are the 6pm scheduled job and the Twilio send path, since a missed or late send is the only failure the user would feel. No prior art to model tests on. Probe the Vercel cron reliability open question before relying on the scheduler.
