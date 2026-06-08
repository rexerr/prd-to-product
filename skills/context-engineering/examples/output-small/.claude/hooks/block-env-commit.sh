#!/usr/bin/env bash
# Hook: Block staging of env files.
# Reason: env files contain secrets. Staging them risks committing secrets to
# version control, which is irreversible once pushed. This is a guarantee, not
# a guideline.
#
# PreToolUse hooks receive the tool-call payload as JSON on stdin. This script
# inspects the actual command and exits 2 ONLY when it stages a .env file, so it
# never false-positives and blocks unrelated Bash commands. The real scoping
# lives HERE, in the script — not in a settings.json matcher. (A bare matcher
# fires on every Bash call; an unconditional script would then block everything.)
#
# Known limitation: this catches an explicit `git add .env*`, not a bulk
# `git add .` / `git add -A` that sweeps in an untracked .env.

payload=$(cat)
if printf '%s' "$payload" | grep -Eq 'git[[:space:]]+(add|stage)[^|;&]*\.env'; then
  echo "BLOCKED: Do not stage env files. Credentials follow this project's env pattern: .env.local locally; Vercel project env vars in production. Never commit .env.local. Update production env vars in the deploy provider's UI, not via git." >&2
  exit 2
fi
exit 0
