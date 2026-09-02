# Progress: 013-brief-dom-integrity-a11y-hardening

**Current phase:** complete.  
**Last safe checkpoint:** 2026-08-27 — D-016 independently approved T-004; SPEC 013 is complete.  
**Authority:** T-001–T-004 are `done` under distinct approvals D-009, D-011, D-013 and D-016.

## Current facts

- `reproduction.md` records the M-006–M-008 false-pass trigger.
- T-002 now rejects rendered duplicate IDs and post-document material while allowing inert literals, comments and whitespace controls.
- T-003 applies only to declared v2 tablists. Its static grammar requires a per-tablist initializer and scoped listener evidence, but permits any number of tabs, panels, content blocks and views.
- Brief source coverage remains independently accepted in D-006; T-004 reconciled the execution projection with D-009, D-011, D-013, D-015 and D-016.
- D-015 records builder evidence: the focused suite and 267-check bundle passed; the SPEC 013 baseline write/recheck is clean. D-016 records the required distinct evaluator approval.

## Next safe step

SPEC 013 is complete. SPEC 014 may rely on the completed T-004 DOM/tab contract; no additional SPEC 013 task is authorized by this checkpoint.
