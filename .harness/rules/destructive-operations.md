# Rule: Destructive Operations

## Soft rule

Any destructive, irreversible, production-facing, permission-changing or
security-sensitive action requires explicit human approval immediately before
execution.

Examples include deleting data, irreversible migration, secret rotation,
permission/billing changes, force push, history rewrite and write-enabled
external tools with material impact.

## Approval record

Record operation, exact target, reason, preview/diff, expected effect, blast
radius, backup/checkpoint, rollback feasibility, requested by, approved by and
timestamp. Approval for one target does not authorize another.

The agent may perform read-only discovery and prepare a preview before
approval. It must re-request approval if scope or effect changes.

## Blocking conditions

Block when approval is missing/stale/ambiguous, rollback claims are unverified,
target identity is uncertain, or the operation conflicts with safety,
privacy, permissions or local policy.

## Hard mirror recommendation

Route destructive tools through a confirmation gate with target allowlisting,
least privilege, audit logging and time-bounded approval tokens. Prefer dry-run
or preview enforcement.

Recommended check: `require-human-approval-for-destructive-action`.
