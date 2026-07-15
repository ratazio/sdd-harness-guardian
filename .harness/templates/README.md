# Initiative templates

These are canonical, vendor-neutral templates. Copy them into the consumer
repository; never write consumer state inside `vendor/sdd-harness-guardian`.

## Target layout

```txt
specs/<initiative>/
  spec.md
  stakeholder-brief.html
  impact-map.md
  plan.md
  validation-plan.md
  tasks.md
  run-state.yaml
  progress.md
  decision-log.md
  ratchet.md
  evidence/
  handoffs/latest-handoff.md
```

Bugfixes also copy `reproduction.md`. Each implemented task copies
`evidence-pack.md` to `evidence/<task-id>.md`. New ratchet entries use
`ratchet-entry.md` inside the initiative `ratchet.md`.

## Safe scaffolding

From the consumer root:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py <initiative>
```

Use `--kind bugfix` to add reproduction. The script creates a new directory
atomically enough for scaffolding and refuses any existing target.

## Manual copy

Create the target tree, copy each canonical file with its target name, copy
`handoff.md` as `handoffs/latest-handoff.md` and create an empty `evidence/`.
Replace `<initiative>`, dates and ownership placeholders before review.
Keep `stakeholder-brief.html` concise, human-readable and synchronized with the
source artifacts.

Do not copy `run-state.yaml.md` as state; it documents the contract.
Copy `run-state.yaml` itself.

## Template change policy

Update templates, rules and workflows together when a required field changes.
Outcome-readiness fields are part of the execution contract, not optional
metadata.
The stakeholder brief is a derived visibility artifact and must not become a
parallel source of truth.
Run `python scripts/validate_bundle.py` before release. Consumers pin a bundle
tag, so template evolution must be versioned.
