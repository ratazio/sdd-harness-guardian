# Decision Log — SPEC 022

| ID | Date | Status | Decision | Rationale/evidence | Owner | Supersedes |
|---|---|---|---|---|---|---|
| D-022-001 | 2026-08-28 | accepted | Create a separate corrective SPEC rather than patch the blocked SPEC 021 HTML. | Five-lens rendered review found reusable lifecycle/provenance contradiction. | Guardian maintainer | none |
| D-022-002 | 2026-08-28 | accepted | Synchronize only declared lifecycle markers and their source bindings before target write. | Independent source review approved the lifecycle-only constraint. | `spec022_source_review` | none |
| D-022-003 | 2026-08-28 | accepted | Make T-001 the complete minimal renderer repair. | The independent review found that modeling-only T-001 would leave the self-hosting block in T-002. User authorization and review delimit the exception to T-001. | `spec022_source_review` | none |
| D-022-004 | 2026-08-28 | accepted | Start the limited T-001 bootstrap before the v2 brief gates. | The renderer defect prevents this SPEC's normal promotion. Only the lifecycle-only repair is authorized; the evaluator prohibits T-002–T-004, domain mutation and baseline until normal gates resume. | `spec022_source_review` | none |
| D-022-005 | 2026-08-28 | accepted | T-001 lifecycle repair is complete and independently approved. | r4 accepted the closed marker schema, final-state provenance, exact pending authority and fault-injected recovery; the orchestrator reran all required regressions (bundle: 272 checks). | `spec022_t001_evaluator_r4` | none |

## D-022-006 — SPEC 022 composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_semantic_review
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: e35a1c80ec570a121b5f3b45857aab200b6fbf25ff777d3556ee171d3b0b9dcb
Reviewed at: 2026-08-28
Review method: HTML-alone decision review followed by comparison against all canonical SPEC 022 sources; no semantic score or visual-count proxy.
Review outcome detail: APPROVE after r4 verified durable post-promotion wording, vendor-neutral identity, all allowed source bindings and factual N/A dispositions. The candidate explains the lifecycle fault, closed rewrite surface, recovery, task/evidence authority and human-versus-deterministic boundary without claiming rendered-decision approval.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:4560ecf987d8f15e670ca9f78000f1581a498abbeca5b8573f7b0bfa0bd15a10
- tasks.md@sha256:651fab17d07d2555612bb819792bdb3317adcc798e2fbd2f4f1574101ca7e484
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-046 — Next-safe-step candidate recomposition pending

Status: proposed
Decision: the candidate now declares its visible exact next safe action through
the same closed `lifecycle-next-safe-step` projection already used by canonical
state, progress and handoff sources. The binding is source-first: the displayed
action binds `run-state.yaml` / `next_safe_step`, while the review card retains
`progress.md` / `Exact next safe step` as the canonical operational context.
This is a recomposition only, not a review outcome. The prior D-022-045
candidate binding is historical because the candidate/source package changed.

Required next action: obtain a distinct exact pre-render review for this new
candidate and its source manifest. Until that review is recorded against the
exact candidate digest, no guarded refresh, rendered review, Human Visibility,
Tasks Ready, baseline, delivery, T-004 or SPEC 021 transition is authorized.

## D-022-047 — Exact pre-render review binding for D-022-046 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022046_candidate
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 18c960d68c5703cd735bdaa1c42f0a829fcd6d3b77fb9458d1c85a9ba8e884c6
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical SPEC 022 source manifest, lifecycle declarations,
provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE for D-022-046's exact recomposed candidate and
the source-backed recomposition that binds this record. The canonical
decision-record digest excludes only the `Candidate SHA-256` binding, avoiding
the one hash cycle while retaining an exact locator. The candidate is
authored/pre-render and eligible only for guarded refresh; it is not rendered
or deliverable. This does not approve rendered-decision review, Human
Visibility, Tasks Ready, T-004, delivery, baseline or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f44e4e4bbdefc2147fe4288ba2083623d0d5b9ff8c83adc6472860e066127d06
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-035 — D-022-034 source-first recovery independently approved

Status: accepted
Builder: `spec022_postrender_authority_builder`
Evaluator: `/root/evaluate_d022034_repair` (independent from the builder)

Decision: APPROVE the D-022-034 recovery boundary. An explicit blocked
checkpoint has precedence over phase-derived authority; declared lifecycle
spans opt in to that generic projection; unmarked historical records stay
factual and byte-preserved; and guarded refresh refuses unless the initiative
is explicitly `executing`. This closes the T-003 recovery evaluation. The
finding is classified as **2 — lack of proof**: the former evidence did not
prove checkpoint precedence over retained historical review context.

Evidence: `evidence/T-003-postrender-authority-revise.md` and
`evidence/T-003.md`. The independent evaluator reran the five required suites
and manually confirmed guarded refresh rejects the blocked checkpoint without
mutating the refused target.

Boundary: this is not a candidate pre-render approval. The target
`stakeholder-brief.html` remains refused historical evidence. The new
source-first candidate has `brief_review` pending and must receive a distinct
exact SHA-256/source-manifest review before guarded refresh. Human Visibility
and Tasks Ready remain false; T-004 remains pending; no baseline, delivery or
SPEC 021 transition is authorized.

## D-022-036 — Exact pre-render review binding for the recovered candidate

Author: spec022_brief_composer
Reviewer: /root/review_fresh_prerender_d022035
Review outcome: approve
Composition provenance: verified
Reviewed input Candidate SHA-256: d8b16c05c757fb67ccccbd19d79951a0cdab4d275216fa577ab440b09859a5e4
Candidate SHA-256: 6e52801248c11f7080fed92203f440f31fc5c5e6f42244578cbeb3ca027b38a9
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical SPEC 022 source manifest, lifecycle declarations
and source provenance. The reviewer is distinct from the author.
Review outcome detail: APPROVE for the reviewed input candidate and its
source-backed recomposition only. The canonical decision-record digest excludes
only the `Candidate SHA-256` binding, preventing a hash cycle while retaining
an exact decision locator. The candidate remains authored/pre-render and is
ready only for guarded refresh; it is not rendered or deliverable. This does
not approve rendered-decision review, Human Visibility, Tasks Ready, T-004,
delivery or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:c4bcf5d2fbe8d8c7982d3d9740925bc1e461e5442e2700e62b724057215c86ad
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-037 — Operational-authority REVISE and source-first restoration

Status: needs_evaluation  
Classification: **1 — problema de olhar agêntico.**

Finding: after a prior promotion, `run-state.yaml` retained the rendered
lifecycle while the target HTML was explicitly refused historical evidence.
The active `summary`, checkpoint/work-summary/next-step and declared
operational projections could therefore describe a guarded refresh alongside a
rendered-decision state. This is a canonical-state contradiction, not an HTML
wording repair or an approval.

Decision: restore `brief_phase: ready_to_render` and
`current_phase: render_pending`; retain all human/delivery gates as false and
T-004 as pending; keep `stakeholder-brief.html` untouched as refused history.
The reusable repair adds a generic regression: any opted-in source lifecycle
span whose direct text projects a post-render state is refused while the
canonical source state is pre-render. The contract uses only the declared
`run-state.yaml` projection and preserves unmarked bytes; it introduces no
phrase matching, IDs, layouts, semantic score, arbitrary rewrite or SPEC 021
change.

Evidence: `scripts/test_render_stakeholder_brief.py` source-state/post-render
conflict regression and the five required suites. Independent evaluation is
still required before guarded refresh. This record neither approves a candidate
nor a rendered artifact, Human Visibility, Tasks Ready, T-004, delivery or
SPEC 021.

## D-022-038 — Stale candidate binding REVISE and pre-render reset

Status: needs_evaluation  
Classification: **1 — problema de olhar agêntico.**

Finding: D-022-037 changed canonical sources after D-022-036 bound candidate
SHA-256 `6e52801248c11f7080fed92203f440f31fc5c5e6f42244578cbeb3ca027b38a9`.
Consequently its provenance no longer binds the current local `run-state.yaml`;
the pre-render review check and guarded refresh correctly refuse it. The active
state/progress/handoff nevertheless still described an exact passed review and
guarded-refresh readiness. T-003 was also recorded `done` despite the pending
authority REVISE. These are state/evidence contradictions, not an approval.

Decision: preserve `stakeholder-brief.html` unchanged as refused historical
evidence (SHA-256
`50ea9542934bc8da3e6c637ddd636ac0132a30e69914be2e5d25cd88acf00363`);
reopen T-003 as `needs_evaluation`; reset `brief_review` to pending; and
recompose the candidate source-first with current provenance and the closed
pending pre-render lifecycle projection. All Human Visibility, Tasks Ready and
delivery gates remain false, T-004 remains pending, and SPEC 021/baselines are
not changed.

Candidate SHA-256: ba94a291f33ee4307a6ded79ef7de82157295339627b2595b588c84e32852146

Evidence: the prior D-022-036 candidate fails current-manifest linkage with
`provenance digest does not bind the current local source: run-state.yaml`.
The recomposed candidate is authored/pre-render only and must receive a new,
distinct exact SHA-256/source-manifest review before guarded refresh. This
record does not approve the candidate, a rendered artifact, Human Visibility,
Tasks Ready, T-004, delivery or SPEC 021.

## D-022-039 — Exact pre-render review binding for recomposed candidate

Author: spec022_brief_composer
Reviewer: /root/review_recomposed_ledger_candidate
Review outcome: approve
Composition provenance: verified
Reviewed input Candidate SHA-256: ba94a291f33ee4307a6ded79ef7de82157295339627b2595b588c84e32852146
Candidate SHA-256: 952b10bd0d492dfe6801b33838320f6e190a676be952277826a402118ec48ecd
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical SPEC 022 source manifest, lifecycle declarations,
task ledger and provenance. The reviewer is distinct from the author.
Review outcome detail: APPROVE for D-022-038's reviewed input and the
source-backed recomposition that binds this record. The canonical
decision-record digest excludes only the `Candidate SHA-256` binding, avoiding
the one hash cycle while retaining the reviewer, outcome and source evidence.
The candidate is authored/pre-render and eligible only for guarded refresh; it
is not rendered or deliverable. This does not approve rendered-decision review,
Human Visibility, Tasks Ready, T-004, delivery, baseline or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f44e4e4bbdefc2147fe4288ba2083623d0d5b9ff8c83adc6472860e066127d06
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-040 — Visible authority correction resets stale exact binding

Status: needs_revision
Finding: the candidate's visible D-022-039 decision block still said that
D-022-039 recorded a stale-binding REVISE and that the candidate awaited
pre-render review. That contradicted D-022-039's actual independent APPROVE
and guarded-refresh authority.

Decision: correct that visible claim source-first and reset D-022-039's exact
candidate binding. D-022-039 remains valid historical approval evidence for
its own SHA-256, but no approval transfers to recomposed bytes. The active
candidate is authored/pre-render with review pending; a distinct reviewer must
bind its exact SHA-256 and current source manifest before guarded refresh.
Candidate SHA-256: 9f31afdae7fb7549d2522a4ef2ac90790ebebfb37bc5487d59ea1459dcf06fec

Boundary: this correction does not render, deliver, create a baseline, advance
Human Visibility or Tasks Ready, start T-004, or alter SPEC 021.

## D-022-041 — Source-span correction resets D-022-040 candidate binding

Status: needs_evaluation
Finding: D-022-040's candidate binding predated the source-first corrections
to the stale lifecycle-authority spans in `progress.md` and
`handoffs/latest-handoff.md`. Its candidate SHA-256 `9f31afdae7fb7549d2522a4ef2ac90790ebebfb37bc5487d59ea1459dcf06fec`
therefore no longer binds the current canonical source manifest.

Decision: retain D-022-040 as historical reset evidence and recompose the
candidate from the current sources with `brief_review` pending. This record is
not a review approval and its candidate binding does not transfer authority.
A distinct reviewer must bind the recomposed candidate's exact SHA-256 and
current source manifest before guarded refresh. The rendered target remains
refused historical evidence; Human Visibility and Tasks Ready remain false,
T-003 remains `needs_evaluation`, T-004 remains pending, and no baseline,
delivery or SPEC 021 transition is authorized.

Candidate SHA-256: 72c2ac96d655694ddd7573eaf3a81e79319d088b7f803ab99a1f0c10a44b175d

## D-022-042 — Exact pre-render review binding for D-022-041 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022041_candidate_retry
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: b8f4669b304fa6eb3b0a65d06db6ae5cddc0a5f15b890424e9f0d5fc69c2d9cb
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical SPEC 022 source manifest, lifecycle declarations,
task ledger and source provenance. The reviewer is distinct from the author.
Review outcome detail: APPROVE for the D-022-041 recomposed candidate and its
source-backed recomposition only. The canonical decision-record digest excludes
only the `Candidate SHA-256` binding, preventing a hash cycle while preserving
an exact decision locator. The candidate remains authored/pre-render and is
ready only for guarded refresh; it is not rendered or deliverable. This does
not approve rendered-decision review, Human Visibility, Tasks Ready, T-004,
delivery, baseline or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f44e4e4bbdefc2147fe4288ba2083623d0d5b9ff8c83adc6472860e066127d06
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-043 — Systemic operational-source projection REVISE

Status: needs_evaluation

Finding: the generic source-span repair updated authority labels but did not
make the active `run-state.yaml` summary, checkpoint, working-tree summary or
next safe step participate in the lifecycle transaction. The relevant
progress/handoff next-step prose likewise remained outside that declared
transition. A future guarded refresh could again publish rendered scalar state
alongside pre-render operational instructions.

Decision: declare each active operational field/span explicitly and project it
from the closed structured lifecycle state. `lifecycle-authority` carries the
current authority; `lifecycle-next-safe-step` carries the corresponding next
action. The YAML declaration names only an authored scalar field; Markdown
uses the existing direct-text span. Promotion stages run-state, every declared
source and HTML in one journalled/recoverable transaction and preserves all
unmarked bytes. D-022-042 remains historical review evidence only because
this repair changes the source manifest.

Boundary: restore the active source-first state to `ready_to_render` /
`render_pending` with review pending. Keep all delivery/human gates false,
T-003 `needs_evaluation`, T-004 pending, no baseline and no SPEC 021 change.
`stakeholder-brief.html` remains untouched refused historical evidence.

Evidence: `evidence/T-003-systemic-operational-projection-revise.md` and the
renderer regression that models arbitrary YAML operational fields plus
progress/handoff source spans, source/HTML coherence and fault recovery.

## D-022-044 — Historical-target chain reconciliation and pending recomposition

Status: needs_evaluation

Finding: records produced during earlier recovery rounds state that the refused
historical target was SHA-256
`50ea9542934bc8da3e6c637ddd636ac0132a30e69914be2e5d25cd88acf00363`, but
no current evidence links that claim to the retained target file. A direct
observation of the untouched current refused `stakeholder-brief.html` instead
returns SHA-256
`c4646d6723c145db2908b1f896168f2ce6f5979ebb69887bf204f5c97e2ef516`.
Both the recorded 50ea claim and the observed c464 file's promotion lineage
are unverified. Calling either one intact, rendered-current, or a valid
promotion chain would fabricate evidence.

Decision: preserve the target byte-for-byte as refused historical evidence;
record 50ea as an unverified historical claim and c464 as an independently
observed current artifact with an unverified chain. D-022-042's APPROVE and
candidate binding are stale historical evidence after D-022-043 changed the
canonical source manifest. Reset all active review authority to pending and
recompose a new candidate source-first from the current D-022-043 state and
this decision. The new candidate must bind D-022-044 provenance but does not
receive a pre-render approval from this record.

Boundary: T-003 remains `needs_evaluation`; T-004 remains pending;
`brief_phase: ready_to_render` / `current_phase: render_pending` remain
canonical; Human Visibility, Tasks Ready, delivery, baseline and SPEC 021
remain false or blocked. This decision does not mutate the historical target
or assert that its bytes are intact.

Evidence: direct SHA-256 observation recorded by the State Keeper; updated
state/progress/handoff; pending candidate recomposed from canonical sources;
focused renderer and relevant validation suites. Independent evaluation and a
distinct exact pre-render review remain required before guarded refresh.

## D-022-045 — Closed pending next-safe-step projection repair

Status: needs_evaluation

Finding: D-022-044 correctly reset the lifecycle to the closed pending
projection but its three declared `lifecycle-next-safe-step` source spans used
custom composition wording. Those direct-text declarations must equal the
projection selected by structured state, rather than narrate a SPEC-specific
composition sequence.

Decision: reset the active candidate and bind its recomposition to this
record. `run-state.yaml`, `progress.md` and `handoffs/latest-handoff.md` now
declare the identical closed pending next-safe-step: obtain a distinct exact
pre-render review for the current candidate and source manifest before guarded
refresh; Human Visibility and Tasks Ready remain false. The historical target
and its unverified chain remain preserved verbatim; no approval transfers.

Boundary: T-003 remains `needs_evaluation`, T-004 remains pending, and
`brief_phase: ready_to_render` / `current_phase: render_pending` remain
canonical. Human Visibility, Tasks Ready, delivery, baseline and SPEC 021
remain false or blocked. This decision neither renders nor approves a
candidate.

Evidence: source-lifecycle/provenance checks and focused renderer validation
must verify the recomposed pending candidate. A distinct reviewer must bind
its exact SHA-256 and current source manifest before guarded refresh.

## D-022-028 — P1 reopen: declared pre-render authority was stale

Status: needs_revision
Finding: D-022-027 binds candidate SHA-256
`571a4d11e4f69d8c221428b8f5bd7970fb0cfef9aad6946c89089e4d8644b175`
and records a PASS, while declared direct-text lifecycle authority still said
that the exact review was pending. The binding is historical and cannot
authorize promotion of the repaired candidate.
Repair in progress: the reusable renderer derives each opted-in authority
surface from closed structured lifecycle state. `ready_to_render` /
`render_pending` projects either pending review or, only after a complete
structured review and exact record binding, guarded-refresh readiness;
`rendered` / `rendered_decision_review_pending` projects pending rendered
decision review. No free-text scalar selects authority. Source spans use the
same declarative projection. This is not prose inference, scoring, layout
discovery or rendered approval.
Recomputed repaired candidate SHA-256:
`7af7adf757a28621f5417ac6ae1adcce75cf7bfe22e1b129131ec93bd8747353`
Next decision: a distinct independent pre-render review must bind this exact
candidate and current canonical source digests before guarded refresh. Human
Visibility, Tasks Ready, T-004, delivery and SPEC 021 remain blocked.

## D-022-029 — Structured authority derivation repair awaiting evaluation

Status: needs_revision
Builder result: authority declarations now opt in with
`projection="lifecycle-authority"`; they cannot read or select manual
authority text. The closed derivation rejects incompatible phases, projects an
authored/pending candidate for the current pending `brief_review`, and reserves
the guarded-refresh projection for a complete, exact pre-render record
binding. The exact P1 regression (pending review metadata + mismatched record
SHA + passed-looking marker) refuses before render.

Candidate SHA-256: `7af7adf757a28621f5417ac6ae1adcce75cf7bfe22e1b129131ec93bd8747353`.
This builder record is not an approval. T-003 remains `needs_revision`; a
distinct evaluator must review the repair and a new independent pre-render
review must bind any candidate before guarded refresh.

## D-022-030 — Closed-gate repair independently approved

Status: accepted
Builder: `spec022_t003_authority_builder` (Terra, medium)
Evaluator: `/root/evaluate_closed_gate_contract` (independent from the
builder)

Decision: approve the systemic repair for lifecycle authority and the closed
gate-outcome policy after the P1 findings. Authority is derived only from the
structured lifecycle/review model; malformed, incompatible or stale
declarations refuse before render. The repair remains non-semantic and does
not introduce a role, stage, score, taxonomy or arbitrary prose rewrite.

Evidence: `evidence/T-003.md`. The independent evaluator confirmed the five
required suites passed, including source-render isolation and
`validate_bundle.py` (272 checks).

Boundary: this approves T-003 only. Candidate SHA-256
`7af7adf757a28621f5417ac6ae1adcce75cf7bfe22e1b129131ec93bd8747353`
remains authored and pending pre-render review; no review record PASS binds
it. The historical rendered target remains refused. Rendered-decision review,
Human Visibility, Tasks Ready, T-004, delivery and SPEC 021 remain blocked.

## D-022-031 — Current candidate independent pre-render review

Author: spec022_brief_composer
Reviewer: /root/review_current_prerender_candidate
Review outcome: approve
Composition provenance: verified
Reviewed input candidate SHA-256: 7dda9e3e18b8b768bdb5c18c58f6fe92ea07327326df127aa451183deb559c88
Candidate SHA-256: 4124948f4b2fadbf0d636e6e97f40d72823f9c4cd31bed634abfeeddcb77a0de
Reviewed at: 2026-08-29
Review method: independent pre-render composition and provenance review of the
exact authored candidate, followed by comparison with the current canonical
SPEC 022 source set.
Review outcome detail: PASS. The reviewer is distinct from the author and
approved the reviewed input above. Updating the candidate's root review record
and provenance to this decision necessarily recomposes its bytes. The
decision-record digest excludes only the `Candidate SHA-256` field; after
exact confirmation, that field is therefore updated to bind the resulting
candidate SHA without falsely claiming the reviewer inspected pre-update bytes.
The result is ready only for guarded refresh. It is not rendered or
deliverable, and does not approve rendered-decision review, Human Visibility,
Tasks Ready, T-004, delivery or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:5f1b71cba2b2b6610725981e0a9b6462233e83d30583332b798ab17be1968353
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-032 — Source-manifest repair independently approved

Status: accepted
Builder: `spec022_t003_authority_builder`
Evaluator: `/root/evaluate_source_manifest_repair` (independent from the
builder)

Decision: approve the source-manifest repair only. The evaluator confirmed
that lifecycle-bearing canonical sources can return to the authored,
pre-render-pending state without treating the historical rendered target or a
prior candidate review as current authority.

Evidence: `evidence/T-003.md`. The approval is limited to the repair and its
targeted regressions; it does not bind a candidate SHA-256 or replace the
required distinct pre-render composition review.

Boundary: the historical rendered target remains refused. Human Visibility and
Tasks Ready remain false; T-004, delivery and SPEC 021 remain blocked. The
current candidate is authored only, with `brief_review.findings_status:
pending`, and must receive an exact source-bound pre-render review before any
guarded refresh.

## D-022-033 — Current candidate independent pre-render review binding

Author: spec022_brief_composer
Reviewer: spec022_prerender_r33
Review outcome: approve
Composition provenance: verified
Reviewed input candidate SHA-256: b1e19bf4de9eb2b30dbad009686eb553a45387b7640e5cc37cbb7488f0dbc66c
Candidate SHA-256: a130e1219e51bc226f9d12ab05fc89512d657b7de483abb346e09134525fac66
Reviewed at: 2026-08-30
Review method: independent pre-render composition and provenance review of the
exact authored input candidate, followed by comparison with the current
canonical SPEC 022 source set.
Review outcome detail: APPROVE for the pre-render candidate only. The reviewer
is distinct from the author. Updating the state, source projections and
candidate review binding necessarily recomposes the candidate. The canonical
decision-record digest excludes only the `Candidate SHA-256` field, preventing
the one self-reference without excluding any decision, reviewer, outcome,
source-digest or provenance content. After exact SHA confirmation, that field
binds the recomposed bytes; it does not assert the reviewer inspected those
post-binding bytes.

Boundary: ready only for guarded refresh. The candidate is not rendered or
deliverable; rendered-decision review, Human Visibility, Tasks Ready, T-004,
delivery and SPEC 021 remain blocked.

Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:5f1b71cba2b2b6610725981e0a9b6462233e83d30583332b798ab17be1968353
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-034 — Post-render source-authority contradiction

Status: needs_evaluation
Finding: REVISE P1. The retained HTML correctly projected rendered lifecycle
authority, but the active canonical source state still made D-022-033's
pre-render guarded-refresh result read as an operational next instruction.
That is a source-first contradiction: a refused historical target cannot be
the current lifecycle authority, and a historical review record cannot
override an explicit recovery block.

Repair: restore the canonical source state to the retained pre-render candidate
and mark the recovery `blocked`. The generic opt-in lifecycle projection gives
an explicit blocked checkpoint precedence over phase-derived authority, and
the renderer refuses to start from a blocked state. Declared source spans use
that projection; unmarked historical decision records remain byte-preserved
and factual without becoming current instructions.

Boundary: this is not a rendered-decision approval, Human Visibility, Tasks
Ready, T-004, delivery, baseline or SPEC 021 transition. The current
`stakeholder-brief.html` remains refused historical evidence. T-003 requires
independent evaluation before the exact candidate digest/source manifest may
be reconfirmed for any guarded refresh.

## D-022-008 — Ratchet-covered composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_semantic_review
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: c266da05c77aa520664b05947795815ee38d44b238515733cebc4d46d6c60ea3
Reviewed at: 2026-08-28
Review method: HTML-alone review followed by all-source comparison, including
the static ratchet support-source contract and human-readable coverage register;
no semantic score or visual-count proxy.
Review outcome detail: APPROVE. The candidate directly attributes
`RATCHET-022-001` as proposed with its trigger/prevention and four-task proof
condition, has nine factual coverage rows, retains all three impact risks and
does not claim ratchet implementation, rendered-decision approval, Human
Visibility, Tasks Ready or later tasks.
Supersession context: D-022-007 rendered but revealed the source-set
contradiction. T-002 resolved that contradiction without policy expansion; this
record binds the refreshed candidate under the resulting unified contract.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:4560ecf987d8f15e670ca9f78000f1581a498abbeca5b8573f7b0bfa0bd15a10
- tasks.md@sha256:0cfc086578b3770923ee22386be49a01c354ccbb9bbe71579a624d7c06b9de11
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-009 — User authorization for minimal ratchet integration

Status: accepted
Authority: user, 2026-08-28
Decision: execute only the bounded T-002 integration required to make the
renderer and v2 Human Visibility contract agree on `ratchet.md`: one static
support-source enumeration, coverage register/baseline consistency and
adversarial regression tests with independent evaluation.
Anti-scope: no semantic scoring, content taxonomy, prose threshold, ratchet
severity inference, new reviewer role, new approval stage, evidence/handoff
path expansion, SPEC 021 edit or T-003/T-004 execution.
Success measure: fewer conflicting source rules—the same local ratchet source
is admitted and validated everywhere it is already materially projected.

## D-022-010 — T-002 completed without policy expansion

Status: accepted
Decision: T-002 is independently approved. It centralizes the existing v2
source contract, treats `ratchet.md` as one static support source for
provenance/coverage/baseline and leaves the pre-existing evidence-reference
scanner on its original eight sources.
Evidence: r4 reviewed the focused negatives and five required commands; the
orchestrator reran them (bundle: 272 checks). No semantic/content rule, role,
stage, arbitrary path policy, SPEC 021 change or later task was added.

## D-022-011 — Rendered-decision review requires source repair

Status: needs_revision
Reviewers: `spec022_render_architect` and `spec022_render_system` (both
distinct from the composer and T-002 builder)
Artifact: `stakeholder-brief.html` SHA-256
`cbf53371bcff9b33c35646b6ec3931362a4d5a385ffae456fb01684dfdb427d2`
Outcome: REVISE P1; no Human Visibility or Tasks Ready approval.

Findings:

- Canonical `run-state.yaml`, `progress.md` and handoff still instructed a
  refresh although the bound artifact was already rendered. The HTML accurately
  bound those bytes, but therefore repeated a contradictory operational truth.
- The HTML showed the commit sequence but not the decision model for an
  interrupted pair: old pair, journal intent digests, complete-new versus
  incomplete recovery, refusal condition and sole exposure point were not
  assessable without Markdown.
- A wording improvement is required in the replacement: say “Rendered
  artifact; not yet approved or deliverable,” rather than implying no HTML
  artifact exists.

Repair is intentionally source-first and narrow: reconcile the actual state,
make the existing transaction behavior decision-readable in `plan.md`, project
it into a new candidate, then obtain a new composition and rendered-decision
review. This adds no scoring, roles, stages, content taxonomy or generic gate.

## D-022-012 — Replacement composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r5
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: ac5bca1cf9d602985cb3a68c5e7db864d25584b5208309e012f580c0fb3b4a5d
Reviewed at: 2026-08-28
Review method: HTML-alone decision review followed by comparison against the
canonical SPEC 022 sources. The r5 P1 correctly rejected the misleading reuse
of D-022-008; r6 approved after D-022-008 became historical-only and this
candidate stated that no approval yet bound it. No semantic score, prose
threshold, reviewer stage or visual-count proxy was used.
Review outcome detail: APPROVE. The exact candidate makes the pair/journal
transaction decision-readable—old pair, intent digests, complete-new outcome,
restore/refusal and sole exposure point—while remaining lifecycle-only. It
truthfully remains authored, not rendered, approved or deliverable, and does
not claim Human Visibility, Tasks Ready, T-003/T-004 or SPEC 021 approval.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:0cfc086578b3770923ee22386be49a01c354ccbb9bbe71579a624d7c06b9de11
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-013 — Minimal T-003 repair authorized to prevent a reproduced P1

Status: accepted
Authority: user, 2026-08-28 (explicit authorization to continue SPEC 022
after critical assessment of bureaucracy/loop risk)
Problem demonstrated before promotion: the renderer changes only
`brief_phase`. A successful D-022-012 refresh would therefore leave
`current_phase: render_pending` and source instructions that tell the reader to
refresh again, exactly reproducing D-022-011's P1 contradiction.
Decision: execute T-003 now, limited to the declared lifecycle scalar
`current_phase` moving atomically with the state/HTML pair to
`rendered_decision_review_pending`, plus adversarial tests for stale phase,
digest and authority. Recompose after the task because its task/state sources
will legitimately change.
Anti-scope: no generated rewrite of progress/handoff or arbitrary prose, no
semantic score/materiality inference, no new reviewer stage, no baseline or
SPEC 021 mutation. This is a defect correction in an existing acceptance
criterion, not an added process gate.

## D-022-014 — T-003 independently approved

Status: accepted
Builder: `spec022_t003_builder` (Terra, medium)
Evaluator: `spec022_t003_evaluator` (Terra, medium; distinct from builder)
Decision: T-003 is done. The promotor requires `current_phase: render_pending`
and stages `current_phase: rendered_decision_review_pending` atomically with
`brief_phase: rendered`. It refuses inappropriate lifecycle states; recovery
still exposes only the complete old or complete new pair.
Evidence: `evidence/T-003.md`. Builder, evaluator and orchestrator each ran
the five required regressions; all passed, including `validate_bundle.py`
(`272 checks`). No progress/handoff/prose rewrite, semantic scoring,
materiality inference, reviewer stage or baseline was added.

## D-022-015 — Post-T-003 replacement composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r8
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: a0ac1ec9b658ed45ab3db3394f6919c6e6250a57edd35c197d8778fab05e71b0
Reviewed at: 2026-08-28
Review method: HTML-alone decision review followed by comparison against all
canonical SPEC 022 sources. It confirmed D-022-012 is historical, T-003 is
accurately complete, the pair/journal recovery decision is readable, and the
future scalar transition remains lifecycle-only. No semantic score, prose
threshold, visual-count proxy or new reviewer stage was used.
Review outcome detail: APPROVE. The exact candidate is authored and not
rendered/deliverable. Its composition approval does not approve rendered review,
Human Visibility, Tasks Ready, T-004 or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:753193ac26aa281325cc5f8b921b2d15cb8164595fc33932feff45ee4b3d6d15
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-016 — Rendered authority projection reopens T-003

Status: needs_revision
Reviewers: `spec022_post_architect`, `spec022_post_system` (independent from
builder)
Artifact: `stakeholder-brief.html` SHA-256
`c589f536a699cde02f20e1ddfee97ccabcb2923833baff4db9259a0c7392054d`
Outcome: REVISE P1; no Human Visibility or Tasks Ready approval.

Both reviewers found the same contradiction: the rendered marker/state say
`rendered` and `rendered_decision_review_pending`, while the hero, review
requirement, coverage/progress copy and footer still call the target an
unrendered candidate awaiting guarded refresh. The renderer correctly updated
scalar state but faithfully carried stale authored authority text.

Repair scope: extend the existing closed lifecycle allowlist only with explicit
authority-text markers for the affected, source-bound locations; on promotion
they derive the fixed post-render message “Rendered artifact; rendered-decision
review pending; not approved/deliverable; Tasks Ready false.” Do not generate
or rewrite arbitrary prose, progress/handoff, semantic judgments, scores,
roles or stages. Recompose after repair and repeat review.

## D-022-017 — T-003 authority-projection revision independently approved

Status: accepted
Builder: `spec022_t003_authority_builder` (Terra, medium)
Evaluator: `spec022_t003_authority_evaluator` (Terra, medium; distinct from
builder)
Decision: T-003 is done. Six explicit, location-bound lifecycle authority
markers turn only their direct candidate text into the truthful rendered
authority statement. Unknown, duplicate, misplaced, nested or stale markers
refuse. No arbitrary prose/progress/handoff rewrite, semantic score,
materiality inference, role, stage or baseline was added.
Evidence: `evidence/T-003.md`. Evaluator and orchestrator each ran the five
required commands; all passed (`validate_bundle.py`: 272 checks).

## D-022-018 — Fresh candidate composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r13
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 447a2630023e5c0a2c5102403428a7ed8d336aa49d6f33967f997782b3259c0b
Reviewed at: 2026-08-28
Review method: independent HTML-alone review followed by comparison with the
canonical source set, source-binding verification and lifecycle-marker review.
Review outcome detail: APPROVE. The exact candidate explains the lifecycle
defect, narrow architecture, recovery, risks, execution, validation and
authority boundaries. It accurately remains pre-render, names the refused
historical target and contains six valid direct candidate authority markers.
It does not approve rendered-decision review, Human Visibility, Tasks Ready,
T-004 or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:15563a71752744add8fcc797deac76f51f4849a8755ce80b6326ac975e4cf085
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-019 — Coverage-authority projection correction independently approved

Status: accepted
Builder: `spec022_t003_coverage_fix` (Terra, medium)
Evaluator: `spec022_t003_coverage_evaluator` (Terra, medium; distinct from
builder)
Decision: T-003 remains done after correcting the demonstrated structural
conflict. `rendered-authority-coverage` is a direct-text, location-bound
paragraph immediately after the coverage table; it no longer replaces the
table cell that declares a factual coverage disposition. No arbitrary prose
rewrite, semantic score, domain/materiality inference, role, stage or gate was
added.
Evidence: `evidence/T-003.md`. Builder and evaluator ran renderer, Human
Visibility contract, source isolation, decision-quality contract and bundle
validation; all passed (`validate_bundle.py`: 272 checks).

## D-022-020 — Corrected candidate composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r15
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: e4611f5deb21161b1b9f4a70b6c36afef2fc64b37371e3b26550731c0706c7d4
Reviewed at: 2026-08-28
Review method: independent HTML-alone review followed by comparison with the
canonical source set, source-binding verification and lifecycle-marker review.
Review outcome detail: APPROVE. The candidate accurately remains pre-render;
the coverage register retains its factual progress disposition and the separate
post-table authority marker is direct candidate text. It explains the defect,
architecture, recovery, risks, execution, validation and authority boundary,
but does not approve rendered-decision review, Human Visibility, Tasks Ready,
T-004 or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f057b768d5e2661885003c673601b7e556255993b060d5cb3772b39ed0d339e8
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-021 — Stable candidate composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r20
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 75d2d1ecd4940c609082544cf7279cd5958e14fb3a1312ac7f6e8dcb430c7fbc
Reviewed at: 2026-08-28
Review method: independent HTML-alone review followed by comparison with the
canonical source set, source-binding verification and lifecycle-marker review.
Review outcome detail: APPROVE. The candidate is honestly authored/pending;
the historical target is refused. The handoff N/A card binds current
`progress.md` and identifies the handoff as complementary operational context.
The coverage table and post-table authority marker are coherent. This does not
approve rendered-decision review, Human Visibility, Tasks Ready, T-004 or SPEC
021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f057b768d5e2661885003c673601b7e556255993b060d5cb3772b39ed0d339e8
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-022 — Rendered authority P1 reopens T-003

Status: needs_revision
Reviewers: `spec022_post_architect` and `spec022_post_system` (independent
from the builder)
Artifact: `stakeholder-brief.html` SHA-256
`77027bd5d517bd309f5766afedc6bf43a99ed86ff16e0dbd1bdb30cf73c19386`

Decision: REVISE P1. The rendered root/state markers correctly declared that
rendering occurred and rendered-decision review remained pending, but visible
operational projections still described an authored candidate whose next step
was guarded refresh. This includes the decision boundary, progress and review
path. A stakeholder therefore could not tell whether rendering had happened.

Scope: reopen T-003 only for a source-first reusable authority-projection
repair. The refused target is historical evidence, not a patch target; no
Human Visibility, Tasks Ready, baseline, delivery or SPEC 021 transition may
advance.

## D-022-023 — Generic authority contract independently approved

Status: accepted
Builder: `spec022_t003_authority_builder` (Terra, medium)
Evaluator: `spec022_t003_authority_evaluator` (Terra, medium; distinct from
builder)

Decision: replace SPEC-specific authority marker names, text seeds and layout
assumptions with one repeated, author-declared `rendered-authority` marker.
Each declaration is a direct-text lifecycle authority claim with
`run-state.yaml` provenance and a nonempty fragment; the renderer replaces
only that declared text during the atomic state/HTML transition. It accepts
different body layouts and authored pre-render wording, requires at least one
authority declaration, and refuses undeclared, duplicate, nested or
outside-body lifecycle declarations. The standardized v2 coverage register is
protected from authority markers so factual dispositions remain intact.

Evidence: `evidence/T-003.md`. The evaluator verified generic fixtures with
different tags/layouts/text, non-marker byte preservation, the SPEC 022 P1
reproduction and the coverage-register regression. The five required suites
passed with `validate_bundle.py` reporting 272 checks. No semantic scoring,
domain taxonomy, content heuristic, reviewer role, gate or arbitrary prose
rewrite was introduced.

## D-022-024 — Fresh candidate composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r20
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: c1472b3e4c097c45cee99bcf8cd518747ac7da9716ee31b7d275e180dd1be103
Reviewed at: 2026-08-28
Review method: HTML-alone composition review followed by comparison with all
canonical SPEC 022 sources, lifecycle declarations and source bindings. The
reviewer separately confirmed that the generic authority contract is not a
catalog of layout, identifier or prose assumptions.
Review outcome detail: APPROVE for the fresh pre-render composition. It is
authored, not rendered or deliverable; D-022-021 is historical, the current
candidate awaits the independently confirmed exact binding required before
promotion, and Human Visibility, Tasks Ready, T-004 and SPEC 021 do not
advance.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:9996480c6d544d8f6729930cc61d739908695e1c2282e5becaff8d6e756a7993
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-025 — Recomputed candidate composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r25
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 8404868176dd1654cd7f854ca92bf404f17ac3f6b8fab1a007e89073aa765c06
Reviewed at: 2026-08-28
Review method: HTML-alone review followed by all-source comparison, explicit
lifecycle/provenance validation and generic-contract boundary inspection.
Review outcome detail: APPROVE for this authored pre-render candidate only. It
truthfully awaits exact confirmation before promotion, is not rendered or
deliverable, and leaves Human Visibility, Tasks Ready, T-004 and SPEC 021
blocked.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:9996480c6d544d8f6729930cc61d739908695e1c2282e5becaff8d6e756a7993
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-026 — Source-lifecycle repair independently approved

Status: accepted
Builder: `spec022_t003_authority_builder` (Terra, medium)
Evaluator: `spec022_t003_authority_evaluator` (Terra, medium; distinct from
builder)

Decision: retain the generic, author-declared `rendered-authority` mechanism
and extend its source-first use to the canonical lifecycle claims that form an
operational projection. The repair is an opt-in direct-text transition bound to
`run-state.yaml`, applied with the state/HTML promotion pair. It does not
interpret candidate words, invent a universal brief structure, or rewrite
unmarked prose.

Evidence: `evidence/T-003.md`. The independent evaluation exercised varied
source layouts and wording, malformed/foreign/nested declaration refusal,
byte preservation outside declared spans and the exact P1 reproduction. The
historical rendered target remains refused. The active source state is returned
to `ready_to_render` / `render_pending` for a new authored candidate and fresh
independent pre-render review; no rendered-decision, Human Visibility, Tasks
Ready, baseline, delivery or SPEC 021 gate advances.

## D-022-027 — Fresh candidate independent pre-render review

Author: spec022_brief_composer
Reviewer: spec022_prerender_r27
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 571a4d11e4f69d8c221428b8f5bd7970fb0cfef9aad6946c89089e4d8644b175
Reviewed at: 2026-08-29
Review method: independent HTML-alone pre-render review followed by comparison
with the canonical SPEC 022 sources, lifecycle declarations and source
provenance. The review input was authored candidate SHA-256
`3506efaf2f523020680c6613629d195464898868c2cb7158e2bc0373b92147e4`;
the record/provenance binding updates required a source-backed recomposition,
whose resulting candidate SHA is the binding above.
Review outcome detail: PASS for the fresh pre-render composition only. The
reviewer is distinct from the author. It confirms the candidate remains
authored/pre-render and not deliverable, the historical rendered target remains
refused, and D-022-026 is a reusable repair rather than an approval of this
candidate. This is not a rendered-decision approval and does not approve Human
Visibility, Tasks Ready, T-004 or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:9996480c6d544d8f6729930cc61d739908695e1c2282e5becaff8d6e756a7993
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-007 — Structural recomposition and composition review

Author: spec022_brief_composer
Reviewer: spec022_prerender_semantic_review
Review outcome: approve
Composition provenance: verified
Candidate SHA-256: 9a638035e93b2f28e0283d1ae61945e092cb4baa5c6bc15e2681a4c3c37d517f
Reviewed at: 2026-08-28
Review method: HTML-alone decision review followed by comparison with all
canonical SPEC 022 sources, plus verification that every mandatory v2 hook
maps to nonempty real decision content; no semantic score or visual-count
proxy.
Review outcome detail: APPROVE. The recomposition maps existing content to all
required hooks, retains current source bindings and factual N/A dispositions,
and keeps durable post-promotion wording. It does not claim rendered-decision
approval, Human Visibility, Tasks Ready, T-002–T-004 or SPEC 021 approval.
Supersession context: D-022-006 records a candidate refused before target
creation for missing hooks. This record binds the recomposed candidate; no
empty scaffold wrapper was added.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:4560ecf987d8f15e670ca9f78000f1581a498abbeca5b8573f7b0bfa0bd15a10
- tasks.md@sha256:651fab17d07d2555612bb819792bdb3317adcc798e2fbd2f4f1574101ca7e484
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6
## D-022-048 — Source-first reset after generic transition-context repair

Status: pending pre-render review
Builder: `/root/repair_nextstep_context_transition` (Terra, medium)

Decision: declared source lifecycle spans receive the same initiative and
candidate context as the HTML lifecycle projection. This preserves the exact
pre-render review linkage when a ready-state `lifecycle-next-safe-step` span is
validated, staged and promoted. The contract remains declarative: source
authors opt in with a projection, source binding and direct text; the renderer
does not infer prose or alter unmarked bytes.

Reset: the renderer and canonical source package changed after D-022-047.
That approval is historical evidence only and cannot bind the recomposed
candidate. `brief_review` is reset to `not_started`; all lifecycle authority
and next-safe-step declarations return to the closed pending projection. No
HTML promotion, rendered-decision review, Human Visibility, Tasks Ready,
baseline, delivery, T-004 or SPEC 021 transition is authorized.

Validation: `test_render_stakeholder_brief.py` adds a ready next-safe-step
source projection to the generic guarded-promotion integration fixture, which
exercises source update and atomic promotion. The five required suites pass.
The candidate must receive a fresh distinct review bound to its final hash and
source manifest before guarded refresh.

## D-022-049 — Exact pre-render review binding for D-022-048 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022048_candidate
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: d2a6af15b9062345f5f90ae3d9cb71fc34843209726edc7a1688541e36c49a89
Candidate SHA-256: 8e0239b436dcced4aed2b04ca29543699a50d8327814a3d2005c0275d2bf3873
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical SPEC 022 source manifest, lifecycle declarations,
provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE for D-022-048's exact recomposed candidate and
the source-backed review binding recorded here. The decision-record digest
excludes only the Candidate SHA-256 field, avoiding that one hash cycle while
retaining an exact locator. The candidate is authored/pre-render and eligible
only for guarded refresh; it is not rendered or deliverable. This does not
approve rendered-decision review, Human Visibility, Tasks Ready, T-004,
delivery, baseline or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f44e4e4bbdefc2147fe4288ba2083623d0d5b9ff8c83adc6472860e066127d06
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-050 — Full operational-prose authority REVISE and source-first reset

Status: revise
Builder: `/root/repair_full_operational_prose_authority` (Terra, medium)

Finding: the D-022-049 promotion made the state and the declared summary/
next-step spans rendered, but two active current-context narratives in
`progress.md` and `handoffs/latest-handoff.md` still described the candidate
as eligible for guarded refresh. Those unmarked claims were operational, not
immutable decision history, and contradicted the rendered checkpoint.

Decision: each current-context lifecycle claim now opts in explicitly to the
closed `lifecycle-authority` or `lifecycle-next-safe-step` projection. The
renderer transitions only those direct declared values. It does not search for
terms, encode SPEC-specific prose/IDs, or rewrite historical records. The
regression simulates a full source-first-to-rendered transition for every
active operational source and proves all declared current claims transition.

Reset: D-022-049 and its candidate are historical review evidence after this
source change. The visible rendered target is refused historical evidence and
must not be presented as a deliverable. `run-state.yaml` is reset to
`ready_to_render` / `render_pending` with `brief_review` pending; a freshly
composed candidate, distinct exact pre-render review, guarded refresh and
five post-render reviews are required. Human Visibility, Tasks Ready, T-004,
baseline, delivery and SPEC 021 remain blocked.

Evidence: `evidence/T-003-full-operational-prose-authority-revise.md` and
`scripts/test_render_stakeholder_brief.py`.

Candidate composition: pending independent pre-render review
Candidate SHA-256: 68d9b7f18920c57608cd774f97e100a4f14d46dd5e4c5b3a853e5bd1d60627aa
Composition provenance: source-first; current manifest and task ledger bound
Required next action: obtain a distinct exact pre-render review for the
recomposed candidate and its source manifest. It is not eligible for guarded
refresh, rendering or delivery.

## D-022-051 — Exact pre-render review binding for D-022-050 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022050_candidate
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: 68d9b7f18920c57608cd774f97e100a4f14d46dd5e4c5b3a853e5bd1d60627aa
Candidate SHA-256: f6f62abe15b3ce4c64aa050e615f0bec884097edb9b034ab99cae49408ec9542
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical SPEC 022 source manifest, lifecycle declarations,
provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE for D-022-050's exact reviewed candidate and
the source-backed review binding recorded here. The decision-record digest
excludes only the Candidate SHA-256 field, avoiding that one hash cycle while
retaining an exact locator. The recomposed candidate is authored/pre-render
and eligible only for guarded refresh; it is not rendered or deliverable. This
does not approve rendered-decision review, Human Visibility, Tasks Ready,
T-004, delivery, baseline or SPEC 021.
Source digests:
- spec.md@sha256:db8882d34e44b62abad3958099b5a75802209d00923ff81dc6179b562d1e93ef
- impact-map.md@sha256:d0f151df1cec31ba99281e4def6c8bbf981079fb4ad2e46296d37a84d3bc42bf
- plan.md@sha256:c349ff4d24a8285cb0c0e4e637cbcf88f976fff328d9b5f72756320032d07299
- tasks.md@sha256:f44e4e4bbdefc2147fe4288ba2083623d0d5b9ff8c83adc6472860e066127d06
- validation-plan.md@sha256:1c8c2c149a44b0bfe02c11bb53e79b29c0996a185abfafbc59468d1c813f74e6

## D-022-052 — Minimal promotion boundary

Status: accepted corrective scope; fresh candidate review required.

Decision: the generic renderer commits and recovers only
`stakeholder-brief.html` plus `run-state.yaml`. Progress notes, handoffs and
decision records remain authored evidence and are never rewritten or included
in the transaction. Pre-render authorization binds an exact candidate SHA-256,
a canonical composition-manifest SHA-256 and a distinct human attestation.

Consequence: D-022-051 is historical because its candidate/review did not bind
this simplified contract. No visibility, readiness, baseline, delivery, T-004
or SPEC 021 gate advances from this decision. Initiative-specific post-render
review remains planned evidence rather than a fixed renderer runtime gate.

Candidate composition (authored; review pending):
- Candidate file: `evidence/T-000-stakeholder-brief.candidate.html`
- Candidate SHA-256: a9e18eef18a87bb2588ddf52d7f20a704206c5576bd652114bb71e2dcb89f2ae
- Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f
- Canonical sources: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, and
  `validation-plan.md`.

This records composition provenance only. It is not a review, human
attestation, rendering authorization or delivery approval.

## D-022-053 — Exact pre-render review binding for D-022-052 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022052_minimal_candidate
Human attestation: confirmed
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: a9e18eef18a87bb2588ddf52d7f20a704206c5576bd652114bb71e2dcb89f2ae
Candidate SHA-256: 61e00ab121e6106b736bb0df6bebbb24cb2a488565fd2cc772d76eb134ddc661
Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison with the current canonical SPEC 022 source manifest, lifecycle declarations, provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE for D-022-052's exact composed candidate and the source-backed review binding recorded here. The decision-record digest excludes only the Candidate SHA-256 field, avoiding that one hash cycle while retaining an exact locator. The candidate is authored/pre-render and eligible only for guarded refresh; it is not rendered or deliverable. This does not approve rendered-decision review, Human Visibility, Tasks Ready, T-004, delivery, baseline or SPEC 021.

## D-022-054 — Source-first reset after rendered authority review

Status: composition-only; pre-render review pending.

Finding: the retained rendered HTML correctly reached the rendered lifecycle,
but its decision-register projection still presented D-022-053 as current
pre-render authority. The operational source checkpoint must not claim a
refresh remains next once it is rendered; D-022-053 remains a historical
pre-render record, not a rewritten fact.

Decision: restore the canonical source state to `ready_to_render` /
`render_pending`, clear the exact review linkage, and compose a new candidate
which cites this record as pending composition. The only composition inputs are
`spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, and `validation-plan.md`.
Progress and handoff remain operational context, not promotion transaction
members or composition inputs.

Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f

Consequence: no guarded refresh, rendered review, Human Visibility, Tasks
Ready, baseline, delivery, T-004 or SPEC 021 transition is authorized. A
distinct reviewer must bind the newly composed candidate and five-source
manifest before rendering may be considered.

## D-022-055 — Exact pre-render review binding for D-022-054 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022054_candidate
Human attestation: confirmed
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: 8c471b309d8b4fd728ae150b0b07b37ee982325e285fd99e0765f629f9329101
Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f
Candidate SHA-256: 15dc66ff384b43286a68c73898003b716f6a72dec68c1ef46c789e65a7e0d9c3
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison with the current canonical five-source manifest, lifecycle declarations, provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE for D-022-054's exact composed candidate and the source-backed review binding recorded here. D-022-053 remains historical pre-render evidence; D-022-054 is the current composition-only record. The candidate is authored/pre-render and eligible only for guarded refresh after its final binding. This does not approve rendered review, Human Visibility, Tasks Ready, baseline, delivery, T-004 or SPEC 021.

## D-022-056 — Source-first reset after rendered operational-state repair

Status: composition-only; pre-render review pending.

Decision: rendering now updates the canonical rendered state scalars
(`summary`, `last_safe_checkpoint`, and `next_safe_step`) together with the
lifecycle phase. This prevents a rendered state from retaining guarded refresh
as its current action, without rewriting progress, handoff, or decision
narratives and without expanding the promotion transaction beyond HTML plus
run-state.

Reset: D-022-055 and its candidate are historical pre-render evidence because
the renderer and active source state changed. The current candidate is authored
from the source-first state with review pending. No rendering, post-render
approval, Human Visibility, Tasks Ready, baseline, delivery, T-004, or SPEC
021 transition is authorized.

Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f

Required next action: obtain a distinct exact pre-render review for the newly
composed candidate and the canonical five-source manifest.

## D-022-057 — Exact pre-render review binding for D-022-056 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022056_candidate
Human attestation: confirmed
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: 00c41f160e0dd4f244fa12ba6115b8f682262cdb028c0e03717d6521a12a4ebb
Candidate SHA-256: 184f60d27e2e4bde3f93d51f3394ba6e7d00fb50fa8094dbff22cc9bfe11c3d8
Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison with the current canonical five-source manifest, lifecycle declarations, provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE only the exact D-022-056 candidate plus the mechanical source-backed recomposition that binds D-022-057. This does not approve rendered review, post-render review, Human Visibility, Tasks Ready, T-004, baseline, delivery, or SPEC 021.

## D-022-058 — Source-first recomposition after post-render integrity finding

Status: composition-only; independent pre-render review pending.

Finding: a post-render review altered `run-state.yaml`, while the delivered
page retained its promotion-time state digest. A special rendered-state snapshot
may identify that immutable promotion point, but it cannot make a normal
represented run-state block stale. The `#progress-path` block incorrectly
claimed to represent `progress.md` while binding `run-state.yaml`.

Decision: recovery is restricted to the rendered HTML plus `run-state.yaml`;
schema-v2 multi-source journals are refused for manual recovery. Restore SPEC
022 to source-first state, remove the former rendered target, and compose this
candidate with `#progress-path` represented from `progress.md`. Lifecycle text
remains explicitly bound to current run-state separately. No review, render,
Human Visibility, Tasks Ready, baseline, T-004, delivery, or SPEC 021 advance
is authorized by this composition record.

## D-022-059 — Exact pre-render review binding for D-022-058 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022058_candidate
Human attestation: confirmed
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: 76f38bf890935a562f955bfd452b791f21e0eef9d2f2e93f73ba777bde30b203
Composition manifest SHA-256: f904e2f24dcea68a7b620b3a717ce7ce52e98b3ae8435f6df3babef613d64a1f
Reviewed at: 2026-08-30
Candidate SHA-256: b9da684572ffd8f010f7ca5a4a7aabe20501fff8e5f0f03f3e1bd79a0f58f504
Review method: independent HTML-alone review followed by comparison with the
current canonical five-source manifest, lifecycle declarations, provenance and
task ledger. The review uses the minimal promotion boundary: only the rendered
HTML and run-state can be committed or recovered.
Review outcome detail: APPROVE only the exact D-022-058 candidate and the
mechanical source-backed binding recorded here. This does not authorize
rendering, post-render review, Human Visibility, Tasks Ready, T-004, baseline,
delivery, or SPEC 021.

## D-022-060 — T-003 final independent evaluation

Status: accepted
Evaluator: `/root/final_reevaluate_spec022_t003` (independent from the T-003
builders)

Decision: APPROVE T-003. The evaluator found `lifecycle_error`,
`provenance_error` and `post_render_review_error` all `None` for the finalized
pair. The final `run-state.yaml` SHA-256 is
`4496e5f9c7e1a81fa9790e94ea7d74684c38c99028a7489e056bf5e455ce37ca`; the HTML
metadata and two rendered-state provenance blocks bind that state. The
pre-finalization review input remains
`stakeholder-brief.html@sha256:f3ddd7984af0e4bc6abdab069b3ac07fd9ee526a486449793c2bd1b5eddb9239`.

Evidence: `evidence/T-003-final-evaluation-d022060.md`. The evaluator
confirmed recovery is only the HTML/run-state pair and refuses the old
schema-v2 multi-source journal. Renderer finalization, render, source
isolation, Human Visibility, decision-quality and bundle suites passed; the
bundle reported 272 checks.

Boundary: this closes T-003 only. It does not mark Human Visibility, Tasks
Ready, baseline, delivery, T-004 or any SPEC 021 task/gate. The rendered page
remains the finalized historical post-render-review snapshot, and this
append-only decision must not cause a rewrite of it.

## D-022-061 — Source-first recomposition after T-003 closure

Status: composition-only; independent pre-render review pending.

Finding: D-022-060 correctly closes T-003, which changes factual task and
operational source records. The retained rendered-review HTML is intentionally
an immutable historical snapshot and must not be retroactively rewritten to
claim it was reviewed against the later records.

Decision: restore the active source state to `ready_to_render` /
`render_pending`, clear active pre/post-render review linkage, and recompose a
new candidate from the current canonical five-source manifest. The retained
rendered page remains historical evidence only. This is not a source exception,
render, review, Human Visibility, Tasks Ready, delivery, T-004 or SPEC 021
transition.

Required next action: obtain a distinct exact pre-render review for the D-022-061
candidate and its current canonical composition manifest before any guarded
refresh may be considered.

## D-022-062 — Exact pre-render review binding for D-022-061 candidate

Author: spec022_brief_composer
Reviewer: /root/review_d022061_candidate
Human attestation: confirmed
Review outcome: approve
Composition provenance: verified
Reviewed input SHA-256: db9d44aac20857304d6bb47e2cc47e3afc97d99b6a40acf73740279ce3942c02
Candidate SHA-256: ec7d92ca6ce89620de711efe53b8317ad63bf1b0345f51bcb08ca8ef5c4b1dac
Composition manifest SHA-256: dfcfcf57d32872fac3206954a3cd7d0500f59821e2ac294772a150cfb3bf909b
Reviewed at: 2026-08-30
Review method: independent HTML-alone pre-render review followed by comparison
with the current canonical five-source manifest, lifecycle declarations,
provenance and task ledger. The reviewer is distinct from the author.
Review outcome detail: APPROVE only the D-022-061 candidate and its mechanical
source-backed binding. This is an authored/pre-render authorization for guarded
refresh only; it does not approve rendered review, Human Visibility, Tasks
Ready, T-004, baseline, delivery or SPEC 021.
