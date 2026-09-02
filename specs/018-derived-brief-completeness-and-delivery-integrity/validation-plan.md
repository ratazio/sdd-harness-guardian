# Validation Plan: 018-derived-brief-completeness-and-delivery-integrity

**Status:** validation_ready  
**Owner:** Harness maintainer  
**Last updated:** 2026-08-27

## 1. Strategy

Use deterministic checks for lifecycle truth, provenance, unsafe generic
content, source freshness, local assets and gate state. Use an independent
rendered review for whether a director, architect or operator can understand
the decision. No check requires a technology, fixed field count, tabs, cards,
diagram or prose style.

| Profile/task | Risk or claim | Technique | Oracle/evidence | Executor | Evaluator | Failure behavior |
|---|---|---|---|---|---|---|
| T-001 | bypass is understood | reproduction fixture + CLI | code trace and failing diagnostic | builder | distinct evaluator | revise inventory |
| T-002 | flexible contract | positive/negative fixtures | category/provenance assertions | builder | distinct evaluator | revise contract |
| T-003 | unsafe delivery blocked | unit/CLI + scaffold smoke + release suite | expected exit codes; no source-body leak | builder | distinct evaluator | fail closed/revise |
| T-004 | broad usefulness | fresh eight-domain run + local rendered review | per-package matrix and review | builder | distinct evaluator | no full-pass claim |

## 2. Acceptance traceability

| Validation ID | AC ID | Method/level | Command or steps | Expected result | Evidence destination | Owner |
|---|---|---|---|---|---|---|
| V-001 | AC-001 | CLI/scaffold regression | T-001 reproduces current `python scripts/smoke_test_scaffolder.py` misclassification; T-003 reruns it with the new negative gate fixture. | T-001 proves the old bypass; only T-003 proves the scaffold is visibly labelled and cannot cross delivery/baseline gate. | evidence/T-001.md, T-003.md | builder |
| V-002 | AC-002 | disposable integration | mock-lab full suite in fresh roots | varied domains produce source-backed HTML without shape rule | evidence/T-004.md | builder |
| V-003 | AC-003 | validator negatives | focused test module + human-visibility checks | generic, stale or incomplete v2 brief fails with sanitised diagnostic | evidence/T-001.md, T-003.md | builder |
| V-004 | AC-004 | independent eval | local-server HTML review using executive/architect/operator rubric | reviewer records pass/revise and limits of deterministic checks | evidence/T-004.md | evaluator |

## 3. Regression and non-functional checks

| Validation ID | Risk/constraint | Check | Expected result | Evidence |
|---|---|---|---|---|
| V-REG-001 | phase is misrepresented | scaffold smoke test checks explicit `scaffolded` phase/label | no scaffold is described as a complete/rendered delivery | T-003 |
| V-REG-002 | legacy regression | v1/pinned and materially regenerated v2 fixtures | v1 remains compatible; v2 applies lifecycle gate | T-002,T-003 |
| V-REG-003 | usability/privacy | local-server browser inspect, keyboard/no-script/print as applicable; inspect requests | accessible HTML, local Pearson asset only when opted in, no source-body diagnostic leak | T-003,T-004 |
| V-REG-004 | disconnected release checks | bundle/release runner invokes composition/lifecycle tests or records their execution | passing release cannot be merely structural-template validation | T-003 |

## 4. Required commands

| Command | Environment | Expected result | Applies |
|---|---|---|---|
| `python scripts/smoke_test_scaffolder.py` | repository root | scaffold semantics and provisioning checks pass | T-001,T-003 |
| `python scripts/validate_human_visibility.py <initiative> --write-baseline` | disposable/fresh fixture root | only reviewed authored/rendered v2 package can baseline | T-003,T-004 |
| `python scripts/validate_human_visibility.py <initiative>` | same root | baseline recheck passes | T-003,T-004 |
| `python scripts/validate_bundle.py` | repository root | release suite including lifecycle contract passes | T-003,T-004 |
| focused relevant `python -m unittest ...` command | repository root | negatives/positives pass | T-001–T-003 |

Exact test-module names are discovered in T-001; no fictitious command is a
pass criterion.

## 5. Manual checks and artifacts

| ID | Steps | Expected result | Artifact |
|---|---|---|---|
| M-001 | Serve generated package locally; inspect HTML at desktop and narrow viewport. | Content is populated, readable and navigation remains operable. | screenshot/reviewer notes in T-004 evidence |
| M-002 | Review as executive, architect and delivery owner. | Change/delta, operating model, risks, proof, tasks/authority and next decision are recoverable. | independent review matrix |
| M-003 | Compare a non-software/operational mock with a software mock. | Different representations are accepted; neither is forced into an irrelevant schema. | T-004 evidence |

## 6. Evals and limitations

| ID | Rubric | Input | Passing judgment | Reviewer |
|---|---|---|---|---|
| E-018-01 | source↔HTML honesty; actionable gap; no rigidity | T-001–T-003 diff and fixtures | approve/revise with concrete evidence | independent evaluator |
| E-018-02 | stakeholder decision usefulness | eight fresh rendered briefs | no empty/generic delivery; each domain is understandable, limitations disclosed | independent evaluator |

Deterministic success never certifies architectural correctness or prose
quality. A failed independent review blocks delivery until the finding is
fixed or explicitly resolved with an accountable authority.

## 7. Validation decision

**Validation Ready:** approved  
**All ACs mapped:** yes  
**Blocking gaps:** none for T-001; independent rendered review remains
separate and was recorded in D-018-04.
