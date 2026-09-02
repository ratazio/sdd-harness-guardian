# Decision Log — SPEC 021

| ID | Date | Status | Decision | Rationale/evidence | Owner | Supersedes |
|---|---|---|---|---|---|---|
| D-021-001 | 2026-08-28 | accepted | Create corrective SPEC rather than cosmetically approve/rerender r5. | Eight mocks have material REVISE from seven-lens review. | Guardian maintainer | none |
| D-021-002 | 2026-08-28 | accepted | Treat ratchet as conditionally material and relations as source-driven. | evidence/T-000-mock-lab-reproduction.md | Future T-001/T-002 evaluator | none |
| D-021-003 | 2026-08-28 | accepted | Add a corpus-driven natural-language semantic review hook to D-021-002; deterministic code verifies only a reviewer-declared input manifest (paths/identities and digests), reviewer identity and record scope. | User direction after SPEC 020: domains are unbounded, so no mock-specific detector, visual quota or prose score can be the semantic oracle. Materiality and sufficiency remain exclusively with the reviewer. | Guardian maintainer / future independent evaluator | none |
| D-021-004 | 2026-08-28 | accepted | Source package approved for gated execution. | `/root/spec021_source_review` cleared the decision chain and deterministic-boundary review; `validate_bundle.py` PASS (272 checks). | /root/spec021_source_review | none |
| D-021-107 | 2026-08-30 | accepted | Close T-001 after independent evaluation. | `/root/reevaluate_spec021_t001` returned APPROVE: the conditional source record binds effective corpus paths/scopes/digests, material ratchet recovery includes trigger/check/owner/consequence/provenance, the empty state is reasoned, and the hook keeps materiality and sufficiency human rather than automatic. | /root/reevaluate_spec021_t001 | none |
| D-021-108 | 2026-08-30 | accepted | Close T-002 after independent evaluation. | `/root/evaluate_spec021_t002` returned APPROVE: clearing recovers a source-backed trust-boundary handoff, reservoir operations recovers a source-backed recovery progression, and their negative candidates remain material REVISE with recovery actions. The corpus selects the representation; static checks only bind declared evidence. | /root/evaluate_spec021_t002 | none |

No task in this SPEC is authorized yet.

## D-021-100 — candidate brief composition and pre-render review history

- Status: approved pre-render composition review; promotion remains a separate mechanical step
- Author: spec021_brief_composer
- Reviewer: spec021_pre_render_reviewer
- Review outcome: APPROVE
- Composition provenance: verified
- Candidate: `evidence/T-000-stakeholder-brief.candidate.html`
- Candidate SHA-256: e4cf56b8fca251b0b888ffdfaacf707d30dd06fe3becef65377940e55bed85b0
- Reviewed source digests: `spec.md@sha256:fa87200f4dbb682ef57e0a6ece834268032ce312ecb3932d2b36dfb2b817c1d8`; `impact-map.md@sha256:7145d3a9733ba9a6e7dd98c1b8b75de96a379a1c12f495256b7905e8e05f0db9`; `plan.md@sha256:697e155339be1ca6d434df59a1d988c69f11004b819a505ccc84623d076bfa06`; `tasks.md@sha256:50ce42ac6be7651d32d7d3bceec8fdca397ac0427de61c8d23a3de7799d9a2eb`; `validation-plan.md@sha256:b745ef38e11b7b51bfdfeb4a0b90d58fa012331b4ff19eb813e7be833d09aee0`.
- Scope: source coverage, local provenance, structured governance/architecture relations, vendor-neutral no-JavaScript-required visibility and current gate truthfulness.
- Required review output: material decision still impossible from HTML (if any); source and locator; candidate locator; impact; concrete repair and re-review; and a source-backed N/A reason for each omitted relevant source or relation.
- Deterministic boundary: a later deterministic contract may validate only the reviewer-declared input manifest, distinct identity, digests and record scope. It cannot infer materiality, score prose, count visual elements, recognize a domain or declare this review sufficient.

### Review R-021-PR-001 — independent pre-render review

- Reviewer: spec021_pre_render_reviewer
- Reviewed candidate SHA-256: ed7e9953288d3c43b550bc66c2b610294ebcb2e0765184e3139347fa1b494886
- Scope: HTML-first, then comparison with `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, `validation-plan.md`, `decision-log.md`, `run-state.yaml`, `progress.md` and `ratchet.md`.
- Verdict: REVISE — three blocking material findings.
- F-021-PR-01: `impact-map.md#IR-021-04` lost its distinct signal (same result for materially different corpora) and controls (corpus-driven prompt, cited record, distinct evaluator) in candidate `#impact`/`#architecture`. Repair a connected representation with V-021-02/V-021-04 linkage.
- F-021-PR-02: `spec.md#FR-021-05` and `validation-plan.md#V-021-05` require a new root, eight new consumers, digests and re-review after material REVISE; candidate `#execution`/`#validation` weakened that proof. Repair it explicitly.
- F-021-PR-03: `tasks.md#T-004` and `plan.md#Approach` require approved `evidence/T-001.md`–`evidence/T-003.md` before the cross-domain run; candidate did not recover that authority. Repair it explicitly.
- Next safe step: correct canonical sources/candidate, replace the candidate digest in this record, set review back to pending re-review and obtain a new independent pre-render verdict. No promotion, baseline, Tasks Ready or T-001 execution is authorized now.

### Repair R-021-PR-002 — builder correction awaiting re-review

- Builder: spec021_brief_composer
- Repair scope: represent IR-021-04 separately with its signal, corpus-driven prompt, cited record, distinct evaluator and V-021-02/V-021-04 linkage; make the root-new/eight-consumer/digest/two-pass repair cycle explicit; and state the independently approved T-001–T-003 evidence prerequisite for T-004.
- Canonical sources repaired: `impact-map.md`, `spec.md`, `tasks.md`, `plan.md` and `validation-plan.md`; candidate provenance is refreshed against those exact bytes.
- Current outcome: PENDING independent re-review. This repair does not resolve R-021-PR-001, authorize promotion/baseline, set a gate, or change any task status.

### Review R-021-PR-003 — independent pre-render re-review

- Reviewer: spec021_pre_render_reviewer
- Reviewed candidate SHA-256: 5deffffc01e1e8e35256ea04de406c44d788a38ac935ed74bb042dde4e89ab57
- Scope: HTML-first, then comparison with `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`, `validation-plan.md`, `decision-log.md`, `run-state.yaml`, `progress.md` and `ratchet.md`.
- Verdict: APPROVE — no material decision remains impossible from the HTML.
- Severity: informational; no blocking finding.
- Repair verification: candidate `#impact`/`#architecture` now represents IR-021-04 with its corpus-difference signal, cited-record/distinct-reviewer controls and V-021-02/V-021-04 linkage; `#execution`/`#validation` recover the root-new, eight-consumer, request/source/HTML-digest and seven-lens/two-pass repair cycle; and `#execution` requires independently approved `evidence/T-001.md` through `evidence/T-003.md` before T-004.
- Deterministic checks: not assessed by this qualitative review. This APPROVE is not a deterministic PASS, promotion, baseline or task authorization.
- Next safe step: perform deterministic provenance/promotion checks, then obtain the distinct rendered-decision review required for Human Visibility and Tasks Ready.

## D-021-101 — Final candidate digest-integrity check

**Status:** pending independent confirmation · **Date:** 2026-08-28 ·
**Owner:** spec021_pre_render_reviewer

The independent checker inspected candidate SHA-256
`2eb99b00eb338b7dd1adf761bbf33ed00f169767f3f7fc70a699b6eef9da2741`
and found no regression in the three repaired material decision surfaces. It
correctly refused approval because D-021-100 then bound the previous SHA.

The binding is repaired by changing only D-021-100’s `Candidate SHA-256`
field to this candidate’s exact SHA. `decision_record_digest()` deliberately
normalizes that single candidate-SHA field, so the D-021-100 provenance digest
in the candidate remains stable; no candidate content is regenerated. A final
independent confirmation of the same immutable candidate is still required
before promotion.

### Final independent confirmation

- Reviewer: spec021_pre_render_reviewer
- Candidate SHA-256 verified: 2eb99b00eb338b7dd1adf761bbf33ed00f169767f3f7fc70a699b6eef9da2741
- Verdict: APPROVE — exact immutable candidate is now bound by D-021-100.
- Integrity result: D-021-100’s normalized decision-record digest remains stable while its Candidate SHA-256 field equals the reviewed candidate’s exact bytes; the candidate was not regenerated.
- Semantic result: no regression in IR-021-04 controls, the T-004 fresh-root/eight-consumer/request-source-HTML-digest/two-pass repair cycle, or the independently approved T-001–T-003 evidence prerequisite.
- Scope limit: this confirms pre-render binding only; deterministic promotion and the distinct rendered-decision review remain required before Human Visibility or Tasks Ready.

## D-021-102 — source-first recomposition after refused historical binding

**Status:** pending independent pre-render review · **Date:** 2026-08-30 ·
**Author:** spec021_brief_composer

- Author: spec021_brief_composer
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: 2876db8e4d51c44ee61021ab41c5c721fa636ac58d1f5c3add778154fabf97e0
- Candidate SHA-256: b22830c32a4a9d2d14afcd90766f3d021354a0ef8436569e833bf3e102e402e2

### Historical disposition

The prior D-021-100/D-021-101 bindings and rendered HTML are refused
historical evidence: the rendered review found candidate lifecycle text,
pre-promotion state provenance and a pre-render reviewer at a post-render
decision boundary. They do not authorize refresh, Human Visibility, Tasks
Ready or T-001. SPEC 022 repaired the reusable lifecycle contract; this record
starts a new composition rather than editing the historical HTML in place.

### Current composition

- Author: spec021_brief_composer
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: 2876db8e4d51c44ee61021ab41c5c721fa636ac58d1f5c3add778154fabf97e0
- Candidate SHA-256: b22830c32a4a9d2d14afcd90766f3d021354a0ef8436569e833bf3e102e402e2
- Core composition inputs: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
  `validation-plan.md`.
- Additional material inputs for human review: `ratchet.md` (conditional
  preventive rule), `decision-log.md` (historical refusal and current D-021-102
  authority), `run-state.yaml` (actual gates/lifecycle), `progress.md`
  (checkpoint/next action), `handoffs/latest-handoff.md` (resumption scope),
  `evidence/T-000-mock-lab-reproduction.md` (eight-consumer origin) and
  `evidence/T-000-source-package-review.md` (prior source-package evidence).
- Source treatment: the five core files bind the canonical composition
  manifest. The additional inputs are explicitly presented for human judgment;
  they do not expand the renderer's HTML + run-state recovery transaction.

### Required review scope

Review the exact candidate HTML first, then compare it to the five core source
files and all additional material inputs above. Record any decision still
impossible from the HTML with source/locator, impact and concrete repair; each
omitted material source/relationship needs a source-backed N/A reason. An
approval must bind the exact candidate SHA and current canonical manifest.

## D-021-103 — independent exact pre-render approval

- Author: spec021_brief_composer
- Reviewer: /root/review_d021102_candidate
- Reviewed at: 2026-08-30
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Reviewed input SHA-256: b22830c32a4a9d2d14afcd90766f3d021354a0ef8436569e833bf3e102e402e2
- Composition manifest SHA-256: 2876db8e4d51c44ee61021ab41c5c721fa636ac58d1f5c3add778154fabf97e0
- Candidate SHA-256: fa1526e056284718b1cb8955a9ac4e8e2b7bd74572446c452bb9d2fb722382ba
- Review scope: HTML-first review of D-021-102, followed by comparison with
  the five canonical composition inputs and the explicitly inventoried
  additional material sources.
- Review conclusion: approve only this immutable candidate for guarded
  refresh. This does not render, deliver, set Human Visibility/Tasks Ready or
  authorize T-001.

## D-021-104 — source-first composition repair

- Status: superseded before review by D-021-105 label repair
- Author: spec021_composition_repair
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: 2876db8e4d51c44ee61021ab41c5c721fa636ac58d1f5c3add778154fabf97e0
- Candidate SHA-256: 98430562e03fe1370f633b58b5be9cc50488d714268132cd1163f2b0aa8c628f
- Core composition inputs: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
  `validation-plan.md`.
- Additional material inputs for human review: `ratchet.md`, `decision-log.md`,
  `run-state.yaml`, `progress.md`, `handoffs/latest-handoff.md`,
  `evidence/T-000-mock-lab-reproduction.md` and
  `evidence/T-000-source-package-review.md`.
- Repair scope: the candidate now uses the valid `synthesized` disposition for
  `spec.md`, has separate coverage rows for `run-state.yaml` and `progress.md`
  that resolve to their corresponding provenance blocks, and projects
  IR-021-02, IR-021-03 and IR-021-04 in `#impact`.
- Boundary: this record only resets composition and review. It does not render,
  set Human Visibility/Tasks Ready, create a baseline or authorize any task.

## D-021-105 — source-first composition after pending-label repair

- Status: pending independent pre-render review
- Author: spec021_composition_repair
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: 2876db8e4d51c44ee61021ab41c5c721fa636ac58d1f5c3add778154fabf97e0
- Candidate SHA-256: 0aa8258d66c6614c381393669fd8711d441905d56b09da5b54aca2fc194dc524
- Core composition inputs: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
  `validation-plan.md`.
- Additional material inputs for human review: `ratchet.md`, `decision-log.md`,
  `run-state.yaml`, `progress.md`, `handoffs/latest-handoff.md`,
  `evidence/T-000-mock-lab-reproduction.md` and
  `evidence/T-000-source-package-review.md`.
- Repair scope: D-021-104 was never approved. This candidate corrects only the
  coverage-register label so it says that the current composition and review
  are pending, while D-021-100/D-021-101 and the rendered HTML remain refused
  historical evidence.
- Boundary: this record only resets composition and review. It does not render,
  set Human Visibility/Tasks Ready, create a baseline or authorize any task.

## D-021-106 — independent exact pre-render approval

- Author: spec021_composition_repair
- Reviewer: /root/review_d021105_candidate
- Reviewed at: 2026-08-30
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Reviewed input SHA-256: 0aa8258d66c6614c381393669fd8711d441905d56b09da5b54aca2fc194dc524
- Composition manifest SHA-256: 2876db8e4d51c44ee61021ab41c5c721fa636ac58d1f5c3add778154fabf97e0
- Candidate SHA-256: 3639843b26184f8d29f6baadd2f3ea3a3cb7f0b44245897bbfe46092adc1d45f
- Review scope: independent HTML-first review of D-021-105, followed by the
  current canonical five-source manifest and its explicitly inventoried
  additional material inputs.
- Review conclusion: approve only the mechanically bound, exact candidate for
  guarded refresh. This does not render, deliver, set Human Visibility/Tasks
  Ready, create a baseline or authorize T-001.

## D-021-107 — T-003 independent evidence approval and T-004 checkpoint

- Builder: spec021_t003_builder
- Evaluator: /root/evaluate_spec021_t003
- Evaluated at: 2026-08-30
- Outcome: approve
- Evidence: `evidence/T-003.md`
- Scope: the evaluator approved only AC-021-04 / V-021-04: distinct reviewer
  identity, exact candidate/rendered and corpus bindings, path/locator/digest
  integrity, explicit record scope, and negative refusal of violations.
- Boundary confirmed: valid structural `APPROVE` and `REVISE` records remain
  human semantic verdicts; no score, classifier, counter, materiality inference
  or automatic approval is introduced.
- Next checkpoint: T-004 remains pending. If it is started later, it must use a
  fresh M-001–M-008 root and both passes of seven human lenses; any material
  `REVISE` blocks baseline.
- Non-effects: no T-004 work, rendering, Human Visibility, Tasks Ready,
  baseline, delivery or lifecycle-gate release is authorized by this decision.

## D-021-109 — T-004 independent evidence approval

- Builder/registrar: `/root/execute_spec021_t004`
- Evaluator: `/root/review_t004_arch_system`
- Evaluated at: 2026-08-30
- Outcome: approve
- Evidence: `evidence/T-004.md` and `evidence/T-004-review-records.json`
- Scope: the final r15 evidence envelope: 112 individually auditable reviews,
  exact request/source/HTML bindings, the r14 coverage REVISE, and the
  M-005/M-006 A2-to-A3 repair with exactly 28 final restart records.
- Boundary: this approves T-004 only. It does not set Human Visibility, Tasks
  Ready, baseline, delivery, promotion approval or another lifecycle gate.

## D-021-110 — SPEC 022 T-004 source-first recomposition

- Status: pending independent pre-render review
- Author: spec022_t004_builder
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: 41256f31343531ed4c0c0b265527dda015a71d90b03edac5fffd774806b3fbcf
- Core composition inputs: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
  `validation-plan.md`.
- Additional material inputs for human review: `ratchet.md`, `decision-log.md`,
  `run-state.yaml`, `progress.md`, `handoffs/latest-handoff.md`,
  `evidence/T-000-mock-lab-reproduction.md`, `evidence/T-000-source-package-review.md`,
  and independently approved `evidence/T-001.md` through `evidence/T-004.md`.
- Scope: recompose the SPEC 021 brief after all four implementation tasks are
  complete. The earlier D-021-106 reviewed/finalized pair is retained as
  historical lifecycle evidence, not reused as this new candidate.
- Boundary: this reset does not grant Human Visibility, Tasks Ready, a
  baseline, delivery, or any task authorization. A distinct reviewer must
  inspect the exact candidate and the current five-source manifest before a
  guarded refresh.

## D-021-111 — independent pre-render REVISE of D-021-110

- Author: spec022_t004_builder
- Reviewer: /root/execute_spec022_t004/review_d021110_prerender
- Reviewed at: 2026-08-30
- Human attestation: confirmed
- Review outcome: revise
- Composition provenance: pending
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: 41256f31343531ed4c0c0b265527dda015a71d90b03edac5fffd774806b3fbcf
- Review scope: HTML-first, then current canonical manifest and material inputs.
- Finding F-021-PR-110-01 (material): `tasks.md` and the four approved packs
  show T-001–T-004 done, but candidate `#execution` said no task was done,
  ready or executing. This makes the task state impossible to determine from
  the page. Repair the sentence to state the four tasks are done while Human
  Visibility and Tasks Ready remain false, then regenerate/bind a new exact
  candidate and obtain a distinct re-review.
- Boundary: REVISE blocks refresh, Human Visibility, Tasks Ready, baseline and
  delivery. No lifecycle gate changes.

## D-021-112 — source-first repair after D-021-111

- Status: pending independent pre-render review
- Author: spec022_t004_builder
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: f4219ced6afa7b39878ab7ad1368efaad170d64cd28aaa0bb32997f320135910
- Core composition inputs: `spec.md`, `impact-map.md`, `plan.md`, `tasks.md`,
  `validation-plan.md`.
- Repair scope: only F-021-PR-110-01: make the execution summary agree with
  the visible four `done` rows and preserve the separate false lifecycle gates.
- Boundary: no refresh, Human Visibility, Tasks Ready, baseline or delivery
  follows until a distinct review approves the exact repaired candidate.

## D-021-113 — independent exact pre-render approval

- Author: spec022_t004_builder
- Reviewer: /root/execute_spec022_t004/review_d021112_prerender
- Reviewed at: 2026-08-30
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Reviewed input SHA-256: f4219ced6afa7b39878ab7ad1368efaad170d64cd28aaa0bb32997f320135910
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: 1e53324ecaba2c1d89e15c677dc374dfa53bf662c7dc5e29feef788086b02428
- Review scope: HTML-first, then current canonical five-source manifest and explicitly inventoried material inputs.
- Review conclusion: approve only the exact candidate for guarded refresh; this does not render, deliver, set Human Visibility or Tasks Ready, create a baseline, or release any gate.

## D-021-114 — source-first operational-authority repair pending review

- Status: pending independent pre-render review
- Author: spec022_t004_builder
- Reviewer: pending independent assignment
- Review outcome: pending
- Composition provenance: pending
- Human attestation: pending
- Composition manifest SHA-256: pending recomposition
- Candidate SHA-256: pending recomposition
- Scope: D-021-113 remains factual approval of candidate
  `1e53324ecaba2c1d89e15c677dc374dfa53bf662c7dc5e29feef788086b02428`.
  This repair corrects only the canonical run-state, progress and handoff
  projections that had still described D-021-110 as awaiting review. A fresh
  candidate and manifest must bind those changed sources.
- Boundary: no guarded refresh follows until a distinct reviewer approves the
  exact D-021-114 candidate and current canonical five-source manifest. Human
  Visibility, Tasks Ready, baseline and delivery remain false.

## D-021-115 — source-first candidate pending review

- Author: spec022_t004_builder
- Reviewer: /root/review_t004_arch_system
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: b8dfabaa7f203332459520d4a507601f2e733b81c1808b6cb56b60eafd605fe8
- Scope: mechanically binds the independently approved D-021-114 repair to
  the exact D-021-115 candidate. Candidate hashing is excluded from this
  decision digest to avoid a self-binding cycle.
- Boundary: no guarded refresh follows until a distinct reviewer approves this
  exact candidate. Human Visibility, Tasks Ready, baseline, delivery and
  post-render review remain unapproved.

## D-021-116 — source-first post-render-recovery candidate pending review

- Author: spec022_t004_builder
- Reviewer: /root/review_t004_arch_system
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: 046bdeb2968b0e908bcf2330a8dd3da260d3ba2f2e647a0039103c067b9ce776
- Scope: D-021-115 remains historical signed pre-render authority. This fresh
  immutable candidate repairs F-021-POST-115-DM-01 by declaring the correct
  future sequence: independent pre-render signature, guarded refresh, then
  independent post-render review before any delivery decision.
- Boundary: no refresh, Human Visibility, Tasks Ready, baseline or delivery is
  authorized while D-021-116 is unsigned.

## D-021-117 — rendered-review-status candidate pending review

- Author: spec022_t004_builder
- Reviewer: /root/review_t004_arch_system
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: 404b1ce9ef9540ff47da51d5af23c3a8dd96aaa317fcc426bb6055d9177a3f9b
- Scope: D-021-116 is historical signed pre-render authority. The explicit
  closed `rendered-review-status` hooks keep rendered decision/status snippets
  source-first and renderer-owned without rewriting unrelated prose.
- Boundary: no refresh, Human Visibility, Tasks Ready, baseline or delivery is
  authorized while D-021-117 is unsigned.

## D-021-118 — replacement-hook candidate pending review

- Author: spec022_t004_builder
- Reviewer: /root/review_t004_arch_system
- Human attestation: confirmed
- Review outcome: approve
- Composition provenance: verified
- Composition manifest SHA-256: 8c4a2f1f1ab950d4b790c8c4fcff9463bac85e4f8107744f173dce4329a75bc9
- Candidate SHA-256: 2bb742fc0551880226e48bcb3684fe7409a5934d629fdafe29af4111f58b3a4c
- Scope: replaces the three stale visible lifecycle instructions with closed
  rendered-review-status hooks; no other prose is lifecycle-owned.
- Boundary: no refresh, delivery, Human Visibility, Tasks Ready or baseline is
  authorized while unsigned.
