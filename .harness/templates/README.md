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
duplicate slugs. New output is the v2 brief lineage; it is a draft package,
not a declaration that any readiness gate has passed.

## Manual copy

Create or update `specs/INDEX.md` from `specs-index.md`. Create the numbered
target tree, copy each canonical file with its target name, copy
`handoff.md` as `handoffs/latest-handoff.md` and create an empty `evidence/`.
Replace `<initiative-id>`, `<initiative-slug>`, `<initiative-sequence>`, dates
and ownership placeholders before review. The scaffolder renders the v2 brief
identity/date/risk/size fields; replace its neutral risk/size defaults from the
canonical sources before review.
Keep `stakeholder-brief.html` concise, human-readable and synchronized with the
source artifacts. For v2, draft tasks before the final brief, record the
applicable-source/heading composition in the existing plan, obtain a distinct
coverage review, then render, meet, propagate decisions and only then declare
Tasks Ready. `tasks_drafted` is not implementation authority. Use the checklist in
`.harness/rules/human-visibility.md`: size the initiative S/M/L, consider a
smaller option, record the architecture-readiness profile, and include the
proportional architecture/impact/flow views only when they make a concrete
relationship easier to decide.
Populate the canonical visual shell rather than reconstructing a page. Read
`stakeholder-brief-design.md` before authoring: it defines the current design
lineage marker, required meeting surfaces, conditional views and the reviewed
`decision-log.md` exception path for a material custom layout.

## Post-meeting refresh (v2)

After the meeting, extract each decision, append it to `decision-log.md`, and
update every affected canonical artifact (for example spec, impact, plan,
tasks or validation plan). Re-run the applicable coverage/readiness checks and
regenerate `stakeholder-brief.html` from those sources. Only then may the
Orchestrator set `tasks_ready`; never use an HTML-only decision as the record.
Historical/pinned v1 briefs remain on their legacy contract until a material
refresh follows the migration diagnostic or a reviewed legacy exception.

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
