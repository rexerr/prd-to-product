#!/usr/bin/env bash
# Hook: Block deploy CLI usage.
# Reason: this project auto-deploys on push to `main` via Vercel's GitHub
# integration. Running the Vercel CLI creates parallel deployment paths and
# obscures which version is "current."
# Enforcement note: prose in CLAUDE.md is a request; this hook is a guarantee.

echo "BLOCKED: Do not use the Vercel CLI. This project deploys via GitHub integration on push to main. Push to main and wait for the deploy." >&2
exit 2
