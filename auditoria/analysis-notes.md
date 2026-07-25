# Audit Analysis Notes

## Scope

This audit reviewed the current source bundle, not a downstream consumer. The
repository is explicitly a reusable bundle that consumers install under
`vendor/sdd-harness-guardian`.

## Key Reasoning

The bundle is structurally strong because its operational graph has a clear root:

```txt
AGENTS.md -> .harness/AGENTS.md -> manifest/rules/workflows/agents/skills/templates
```

The new audit capability is also reachable:

```txt
.harness/AGENTS.md -> .harness/workflows/sdd-harness-audit.md
.harness/AGENTS.md -> .harness/skills/sdd-harness-audit/SKILL.md
manifest.yaml -> sdd-harness-audit / harness-auditor / harness-graph-mapper / audit-policy / audit-report
```

The main maturity gap is not missing files. It is the difference between a
governed markdown harness and a hardened harness with deterministic enforcement
for every protected invariant.

## Skill Section Coverage Notes

The audit compared existing skills against the stronger production-ready
anatomy now documented for audit:

```txt
Purpose
When to Use
When Not to Use
Inputs Expected
Core Workflow
External Knowledge Policy
MCP Access Contract
Tool Policy
Output Contract
Validation Checklist
Gotchas
```

Observed gaps:

- `spec-review`, `impact-analysis`, `validation-planning`, `task-breakdown`,
  `evidence-pack-generation` and `ratchet-learning` are useful but compact.
- `interruption-recovery` is especially important and should gain explicit
  validation and gotchas.
- `sdd-harness-audit` is the closest to the new desired anatomy and now includes
  an explicit `External Knowledge Policy` heading.

## Agent Contract Notes

New audit agents have clearer contracts than older role files. Older agents
should be normalized over time, especially:

- `delivery-orchestrator.md`
- `harness-planner.md`
- `state-keeper.md`

These are high-leverage roles and should have explicit output contracts.

## SDD State Notes

Spec 001 is closed. Spec 002 is active and properly blocked on independent
evaluation, but `run-state.yaml` says `status: "draft"` while other fields say
the initiative is in `needs_evaluation`. This is an important concrete finding
because the harness itself says divergent state should block unsafe resumption.

## Release Notes

`manifest.yaml` still says `status: ready` and `version: 0.1.2`, while the
working tree contains significant new uncommitted capability additions. The
audit therefore cannot call the repository release-ready even though structural
validation passes.

## Graph Color Notes

The audit report now treats visual color semantics as part of the output
contract. White means present and neutral: it is a normal node with no special
risk signal. It does not mean missing. Missing or blocking surfaces must be red;
weak, pending or partially enforced surfaces must be amber; reachable and
validated surfaces must be green/teal; generated or contextual artifacts should
use blue.

Every graph or color-coded chart must include a visible legend close to the
graphic. This applies to the harness graph, maturity chart, harness layer view,
enforcement ladder, hooks view and any future diagrams.

## Hooks Notes

The audit found no implemented Git hooks and no CI workflow files. This is not
the same as having no enforcement scripts: `scripts\validate_bundle.py` and
`scripts\smoke_test_scaffolder.py` are strong manual/CI candidates. The gap is
that they are not wired to an automatic lifecycle interception point.

Future reports must include a Hooks tab even when no hooks exist. In the
hookless case, the tab should state that plainly, explain the impact and list
recommended hooks or CI wiring.
