# Initiative templates

These are canonical templates. New v2 stakeholder briefs are vendor-neutral by default;
never write consumer state inside `vendor/sdd-harness-guardian`.

## Target layout

```txt
specs/
  INDEX.md
specs/NNN-slug/
  spec.md
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

### Evidence destinations during planning

Preliminary v2 tasks may name their future `evidence/T-XXX.md` destination
before that pack exists. Record every such destination in `run-state.yaml`'s
`task_ledger` using the block-item form documented in `run-state.yaml.md`.
Human Visibility validation defers a missing destination only while that task
is `pending`, `ready`, `in_progress`, or `blocked`. Once it reaches
`needs_evaluation`, `approved`, or `done`, a cited pack must exist inside the
initiative; deterministic PASS is not an evidence or evaluator approval.

## Safe scaffolding

From the consumer root:

```bash
python vendor/sdd-harness-guardian/scripts/new_initiative.py <initiative>
```

Use `--kind bugfix` to add reproduction. Pass either a slug (`auth-login`) or an
explicit `NNN-slug`. The script creates the next numbered directory by default,
updates `specs/INDEX.md`, and refuses existing targets, reused numbers and
duplicate slugs. New output is explicitly `brief_phase: not_rendered`: it is a
source-only draft package, not a rendered brief, baseline, readiness gate or
declaration that any delivery step has passed. The scaffolder must never create
`stakeholder-brief.html`, a preview shell or a brand asset. Only the approved
composition workflow may materialize HTML after canonical sources and coverage
review are ready.

## Manual copy

Create or update `specs/INDEX.md` from `specs-index.md`. Create the numbered
target tree, copy each canonical file with its target name, copy
`handoff.md` as `handoffs/latest-handoff.md` and create an empty `evidence/`.
Replace `<initiative-id>`, `<initiative-slug>`, `<initiative-sequence>`, dates
and ownership placeholders before review. The scaffolder does not render a
brief. A renderer resolves identity/date/risk/size from reviewed canonical
sources before the HTML exists.

Only a candidate that explicitly selects Pearson provisions the official local
logo at `.harness/assets/brand/pearson-logo-white.png` in the consumer. The
vendor-neutral path does not copy or reference the Pearson asset. When selected,
the renderer verifies an existing file has the release hash and refuses to
overwrite a divergent consumer-owned file. Do not substitute a hotlink, data
URI or `vendor/` path.

### Guarded rendering

Do not copy the canonical shell into an initiative. After the author and the
distinct coverage reviewer have made the canonical sources ready, set
`brief_phase: "ready_to_render"` and `brief_coverage_ready: true`, then promote
the reviewed candidate through. The recorded `decision-log.md` review must name
the distinct author/reviewer, resolve from `brief_review.review_record` to an
explicit `## D-NNN` section, record an approved composition outcome and
`Composition provenance: verified`, bind `Candidate SHA-256: <digest>` for that
exact file and `Composition manifest SHA-256: <digest>` inside that section,
and list current digests for the reviewed
canonical sources. The candidate root must bind the same decision through
`data-composition-review-record`, declare `data-composition-provenance="pending"`
or the legacy `"reviewed"` value, and change its template identity from
`scaffold` to `composed`. Prefer `pending`: the candidate and its run-state may
remain immutable while an independent reviewer signs the exact hash in the
decision record. The renderer validates that signature directly; it does not
require copying reviewer-owned fields back into the signed input. A digest
elsewhere in the log or cosmetic relabelling of the scaffold is not a review. Every
declared source block in the candidate also carries its local `data-source-digest`,
locator and a visible `data-source-fragment` with its
`data-source-fragment-sha256`. The fragment must occur verbatim in the declared
local source and in that rendered block, so a foreign fact cannot be relabelled
with a local file name and digest. This is a factual binding, not a prose score:
authors still use human review to judge a faithful synthesis. A single global
source list is insufficient provenance. The composed mapping must replace the
canonical scaffold's source/locator/coverage topology; relabeling that topology
is not composition.

When source-composed body prose states the review lifecycle, add the optional
direct-text hook `data-lifecycle-marker="rendered-review-status"` with
`data-lifecycle-source="run-state.yaml"`,
`data-lifecycle-projection="lifecycle-review-status"` and a non-empty
`data-lifecycle-fragment`. It lets promotion replace that one declared status
with “pre-render recorded / post-render pending” without rewriting arbitrary
decision prose or any canonical source. Existing briefs remain compatible; add
the hook only to a newly reviewed candidate when that body-level status would
otherwise become stale after render.
Set `quality_review_required: true` so the independent post-render review is
also mandatory before Human Visibility can pass.

An editorial finding may be promoted only with the reviewed editorial exception
record in the same append-only `decision-log.md` section and a visible matching
projection in the rendered HTML. It includes the exception ID, finding, source
→ rendered target, decision impact, residual risk, accountable owner, explicit
decision to proceed, expiry, next action, and the exact candidate and
composition-manifest SHA-256 bindings. This narrow exception cannot waive
integrity, provenance, lifecycle or security controls, and it leaves Human
Visibility and Tasks Ready false until correction, rerender and re-review.

```bash
python vendor/sdd-harness-guardian/scripts/render_stakeholder_brief.py \
  specs/NNN-slug --candidate /absolute/path/to/reviewed-candidate.html
```

The command rejects the scaffold shell, cosmetic reclassification even with an
unrelated or copied digest, unresolved template fields, an invalid rendered
contract, a wrong lifecycle state and a divergent local Pearson logo when that
profile is selected. It writes
the HTML and changes the state to `rendered`; it does not declare Human
Visibility, task readiness or delivery approval.

Keep `stakeholder-brief.html` concise, human-readable and synchronized with the
source artifacts. For v2, draft tasks before the final brief, record the
applicable-source/heading composition in the existing plan, obtain a distinct
coverage review, then render, meet, propagate decisions and only then declare
Tasks Ready. `tasks_drafted` is not implementation authority. Use the checklist in
`.harness/rules/human-visibility.md`: size the initiative S/M/L, consider a
smaller option, record the architecture-readiness profile, and include the
proportional architecture/impact/flow views only when they make a concrete
relationship easier to decide.
Start from the canonical vendor-neutral shell. Select Pearson only when its
brand authority applies by declaring the v2 root
`data-client-identity-profile="pearson"`; then read
`stakeholder-brief-design.md` and `.harness/references/pearson-design.md`, retain
the local real logo image/link, semantic/provenance hooks, native fallback,
print and reduced-motion rules. Without that explicit profile, the brief does
not copy or reference the Pearson asset. A reviewed `decision-log.md` exception
is required for a material custom layout.
For v2, compose each tab from source sufficiency, not a fixed content quota:
recover a supported fact, state a concise source-backed N/A, or record an owned
material question. Ask only when the absent fact blocks a decision, AC, risk
control, authority or next safe step; state the exact fact needed, accountable
owner, decision impact and resolution path in plan/decision/progress before
rendering. This applies equally to software, operations and localized work.

## Opt-in Pearson visual profile and exceptions

The canonical v2 shell is vendor-neutral. Pearson is an explicit opt-in profile,
not a selector overlay: when selected, it uses only the local guide and
`.harness/assets/brand/pearson-logo-white.png`; do not add a CDN, hotlink,
remote font or CSS filter. Existing historical briefs remain unchanged until a
material refresh is explicitly classified in the migration inventory. A new
custom layout needs a reviewed, dated decision-log exception with owner,
rationale, retained decision/accessibility surfaces and review outcome.

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
