#!/usr/bin/env bash
# Hook: Block staging or committing of env files.
# Reason: env files contain secrets. Staging them risks committing secrets to
# version control, which is irreversible once pushed. This is a guarantee, not
# a guideline.

echo "BLOCKED: Do not stage or commit env files. Credentials follow this project's env pattern: .env.local locally; Vercel project env vars in production. Never commit .env.local. If you need to update production env vars, do so in the deploy provider's UI, not via git." >&2
exit 2
