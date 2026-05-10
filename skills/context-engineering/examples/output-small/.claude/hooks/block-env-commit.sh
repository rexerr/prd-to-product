#!/usr/bin/env bash
# Hook: Block staging or committing of env files.
# Reason: env files contain secrets. Staging them risks committing secrets to
# version control, which is irreversible once pushed.

echo "BLOCKED: Do not stage or commit env files. Credentials live in .env.local locally and Vercel project env vars in production. If you need to update production env vars, do so in Vercel's UI, not via git." >&2
exit 2
