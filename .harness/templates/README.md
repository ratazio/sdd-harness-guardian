# Initiative templates

These are canonical, vendor-neutral templates. Copy them into the consumer
repository; never write consumer state inside `vendor/sdd-harness-guardian`.

## Target layout

```txt
specs/
  INDEX.md
specs/NNN-slug/
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

Initiative directories use the canonical `NNN-slug` shape, for example
`specs/001-auth-login/`. The sequence is stable identity and chronology, not
business priority. New numbers are not reused after deletion, supersession or
abandonment.

Bugfixes also copy `reproduction.md`. Each implemented task copies
`evidence-pack.md` to `evidence/<task-id>.md`. New ratchet entries use
`ratchet-entry.md` inside the initiative `ratchet.md`.

## Safe scaffolding

From the consumer root:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py <initiative>
```

Use `--kind bugfix` to add reproduction. Pass either a slug (`auth-login`) or an
explicit `NNN-slug`. The script creates the next numbered directory by default,
updates `specs/INDEX.md`, and refuses existing targets, reused numbers and
duplicate slugs.

## Manual copy

Create or update `specs/INDEX.md` from `specs-index.md`. Create the numbered
target tree, copy each canonical file with its target name, copy
`handoff.md` as `handoffs/latest-handoff.md` and create an empty `evidence/`.
Replace `<initiative-id>`, `<initiative-slug>`, `<initiative-sequence>`, dates
and ownership placeholders before review.
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
