# Product requirements: simple-form

## Product summary

A one-paragraph contact form on a portfolio site. Posts to an API route that emails Jordan via Resend.

## Target users

- Visitors to the portfolio site who want to contact the designer. Mostly potential clients.

## Core problem

The portfolio's old form was a third-party iframe that broke styling and had spam problems. This replaces it with an in-house form that matches the site design and uses Resend for delivery.

## Main workflow

1. Visitor lands on `/contact`.
2. Fills name, email, message.
3. Submits.
4. Client posts to `/api/contact`.
5. API validates, calls Resend, returns 200.
6. Client shows success message.

## Out of scope

- No CRM integration.
- No saved drafts.
- No file uploads.
- No spam captcha (relying on Resend's filtering plus honeypot field).

## Deferred capabilities

Capabilities considered and deferred for V2 or later. Recorded here so they don't get re-proposed in future sessions.

(none)

## Cross-references

- Architecture: `docs/ARCHITECTURE.md`.
- Roadmap: `ROADMAP.md`.
