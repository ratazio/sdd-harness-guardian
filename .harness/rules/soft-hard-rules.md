# Rule: Soft Rules and Hard Mirrors

## Soft rule

Every critical Markdown instruction must name a deterministic or human gate
that can mirror it. Soft text defines intent; the mirror detects or prevents
violations.

## Mirror selection

| Failure class | Preferred mirror |
|---|---|
| missing structure | schema/custom linter |
| invalid transition | state-machine guard |
| contract drift | contract/regression test |
| missing evidence | artifact validator/CI gate |
| self-approval | identity check |
| destructive action | human approval + tool gate |
| secret exposure | secret scanner |
| unsafe repository action | branch protection/permissions |

Each critical rule declares what is checked, where enforcement runs, failure
behavior and a recommended check name. A recommendation remains
runtime-neutral; the consumer chooses implementation.

## Blocking conditions

Release is blocked if a critical rule lacks a `Soft rule` or
`Hard mirror recommendation` section. Safety-, security-, data- and
evidence-critical controls must not rely on soft text alone in production.

## Hard mirror recommendation

Lint all critical rule files for the two required sections and reconcile them
with the manifest registry. Consumers should track mirror implementation status
in local policy or validation artifacts.

Recommended check: `validate-soft-hard-rule-pairs`.
