# L7 Pilot Trigger

This file exists to gate the `l7-self-hosted-smoke.yml` workflow on
its presence (path filter). Touching this file in subsequent PRs
re-triggers the smoke. Delete after pilot is validated.
