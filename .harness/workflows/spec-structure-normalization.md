# Workflow: Spec Structure Normalization

## Purpose

Bring a consumer repository with legacy `specs/<slug>/` initiatives into the
canonical `specs/NNN-slug/` structure without losing traceability.

## Entry condition

The consumer has at least one initiative directory that is missing the numeric
prefix, has no `specs/INDEX.md`, or has index/state disagreement.

## Roles

| Step | Lead role | Output |
|---|---|---|
| Inventory | State Keeper | list of initiatives, current paths, dates and statuses |
| Impact | Impact Mapper | references that would break after rename |
| Plan | Delivery Orchestrator | deterministic sequence and rename map |
| Approval | Human/Orchestrator | approval or blocker for risky renames |
| Apply | Builder or State Keeper | directory moves and reference updates |
| Evaluate | Evaluator | index/state/path consistency decision |

## Flow

1. Read project-local rules, bundle entrypoint and current `specs/` tree.
2. Build an inventory with current path, inferred chronology, status and owner.
3. Infer sequence from existing numeric prefixes, Git history, creation dates,
   decision logs or human notes.
4. If chronology is uncertain, use lexical order and record the uncertainty in
   the affected `decision-log.md`.
5. Produce a rename map from `specs/<slug>/` to `specs/NNN-slug/`.
6. Search for references to old paths in docs, prompts, state, handoffs,
   evidence and automation.
7. Request human approval before risky or broad renames.
8. Apply the rename map and update `run-state.yaml`, `specs/INDEX.md`,
   handoffs and references.
9. Evaluate that each non-archived initiative has exactly one index row and
   matching `initiative_id`, `initiative_sequence` and `initiative_slug`.
10. Record evidence and the normalization decision.

## Blocking conditions

- two initiatives want the same sequence or slug;
- references cannot be updated confidently;
- active work is interrupted without a safe checkpoint;
- human approval is required but missing.

## Output

```md
## Spec Structure Normalization

Inventory:
Rename map:
References updated:
Human approvals:
Validation:
Residual risk:
Next safe step:
```
