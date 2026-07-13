# Ratchet Log

Permanent corrections for this bundle.

## Format

Use `.harness/templates/ratchet-entry.md`.

## Entries

### RG-001 — Source build began before initiative state was scaffolded

**Date:** 2026-07-13  
**Failure type:** state_loss  
**Severity:** medium  
**Status:** implemented  
**Owner:** bundle maintainers

The build prompt supplied a usable spec, but the initial bundle did not provide
a direct, safe way to scaffold all mandatory state before edits. The source
build therefore began with state recorded only in the interactive session.

Prevention:

- `.harness/templates/README.md` defines the complete copy contract;
- `scripts/new_initiative.py` scaffolds project-local state without overwrite;
- `.harness/AGENTS.md` makes initiative bootstrap and resumability explicit.

Regression check: `python scripts/validate_bundle.py` plus a temporary
scaffolder smoke test must pass before release.

### RG-002 — Release state and evidence diverged during bootstrap

**Date:** 2026-07-13  
**Failure type:** task_too_large / state_loss / false_done risk  
**Severity:** high  
**Status:** implemented  
**Owner:** bundle maintainers

The first independent evaluation found dependency sequencing without a waiver,
stale progress/handoff, non-reproducible smoke summaries and premature
`status: ready`.

Prevention:

- `prompts/build-the-guardian.md` requires lifecycle bootstrap before edits;
- release uses `release_candidate` until checklist and evaluation pass;
- validator correlates `ready` with a closed checklist;
- `scripts/smoke_test_scaffolder.py` produces reproducible commands, environment,
  exits and hashes;
- state is synchronized before every evaluation cycle.

Regression check: validator + smoke command + fresh independent evaluation.
