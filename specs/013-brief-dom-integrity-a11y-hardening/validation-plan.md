# Validation Plan: 013-brief-dom-integrity-a11y-hardening

**Status:** draft · **Owner:** platform-engineering

| Validation | AC | Oracle / command | Evidence |
|---|---|---|---|
| V-001 | AC-001 | known/arbitrary rendered duplicate IDs fail, inert-subtree literals pass; `python scripts/test_validate_human_visibility.py` | evidence/T-002.md |
| V-002 | AC-002 | rendered tag/text/declaration/processing-instruction tails fail; whitespace/comment/inert controls pass; same command | evidence/T-002.md |
| V-003 | AC-003 | click-only (including prose-token), multiple-selected, broken-reference, multiple-tablist and missing-script-handler fixtures fail; canonical static shell passes; same command | evidence/T-003.md |
| V-004 | AC-004 | canonical tabbed v2, non-tab v2, and v1 controls pass; same command | evidence/T-003.md |
| V-005 | AC-005 | diagnostic identifies rule/ID without body content; same command | evidence/T-004.md |

After implementation, also run `python scripts/validate_bundle.py` and baseline/recheck this initiative. Independent review checks fixture realism and confirms deterministic pass is not semantic approval.
