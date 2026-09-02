---
name: executive-brief-composition
description: Compose a source-grounded executive brief map and candidate projection when a stakeholder brief needs decision-ready narrative or architecture explanation without making the HTML a source of truth.
version: "0.1.0"
owner: platform-engineering
maturity: stable
risk_level: medium
---

# Executive Brief Composition

## Purpose

Create an additional editorial layer over reviewed canonical Markdown. It is
not a replacement for the source artifacts or an automatic architecture
extractor. The visual skeleton supplies component shapes and route boundaries;
it does not decide the final narrative, diagram, density or domain structure.

## Inputs

Read the requester intent, applicable canonical sources, the current task and
its validation plan. Establish a source locator before stating any material
fact. Keep the map next to the candidate/evidence for the initiative; do not
put consumer facts in this reusable skill.

## Construction record before skeleton

Use the existing `plan.md` as the only composition record. Coverage mapping
answers where a source is represented; the construction record answers how a
route helps its audience make a decision. Before copying a skeleton, record:

- the decision and audience, brief thesis and global relationships that need a
  transversal treatment;
- all eight routes (`scope`, `architecture.global`, `impact`, `execution`,
  `validation`, `evolution`, `decision`, `coverage`), with a source-backed
  treatment or a justified N/A/discovery;
- the decision question, narrative arc and closing action for each route;
- source path and precise locator;
- the allowed synthesis and the fact actually recoverable there;
- the relationship that needs to be made visible, selected form and the reason
  that form serves the decision;
- one entry for every material repeated source-defined component (for example
  a task, proof, impact surface or architecture domain), including the fields
  that must recur;
- a limit, or a discovery when the missing fact changes a decision: record
  owner and resolution path only if that source supports them; otherwise state
  their absence together with the missing fact and its decision impact;
- the projected route/block locator.

Choose the representation from the relationship in the sources. A handoff,
state progression, responsibility boundary, table or concise prose can each be
right. Do not require a diagram, pillar count, frontend zoom or architecture
section merely because a brief has one elsewhere.

## Architecture and scale

When architecture is material, distinguish changed, preserved/context,
out-of-scope and unknown surfaces in words as well as visual treatment. A
quantity must state its unit, denominator and source basis. `0`, out of scope,
and unknown are different statements. A zoom may name internal frontend or
other subsystem areas only when the source names them. Otherwise record the
exact missing fact and decision impact. If the source supports a discovery
owner/path, record both; if it does not, explicitly say that owner/path are not
established rather than attributing them to an adjacent actor.

## Composition boundaries

- Keep canonical Markdown authoritative; recover a source correction there
  rather than patching a derived HTML claim.
- Author the candidate HTML/CSS/JS directly as an agent after reviewing the
  route construction record and source locators. The final blocks are not
  emitted by Python or another deterministic Markdown-to-brief generator.
- A script may instantiate/copy the blank shell, validate identity/slots/IDs,
  promote exact reviewed bytes or capture evidence. It must not infer a
relationship, choose a visual form, write a task/proof dossier or compose
executive wording from Markdown.

## Independent plan review

Before skeleton instantiation, hand the completed `plan.md`, requester intent
and applicable canonical sources to a distinct reviewer. The reviewer returns
`APPROVE` or `REVISE`, never a numeric score. A `REVISE` finding uses this
recovery chain: **source → loss or ambiguity → decision prejudiced → canonical
correction**. Do not copy or compose a skeleton while a blocking `REVISE`
remains. A `REVISE` is a recovery instruction, not a reason to leave a
source-backed brief half-built or to wait for the requester. When the canonical
sources contain the missing material, the composer updates the existing
construction record, requests the same distinct review again, then continues
through the physical skeleton, candidate and guarded final render in the same
run. Ask the requester only when the correction needs new authority, a changed
scope, or a material fact that the sources genuinely cannot establish. Review
the plan rather than producing a sidecar map or a deterministic visual recipe.

## Autonomous completion rule

Once the request and canonical sources are sufficient, own the entire
composition path without asking the user to authorize each handoff:

1. repair the construction record after an internal `REVISE`;
2. obtain the distinct re-review;
3. copy the initiative-local skeleton and author the candidate in place;
4. run the inheritance/structural checks, repair the candidate when they fail;
5. promote through the guarded renderer, serve the final HTML locally, and
   route the independent rendered review back to the compositor when needed.

For the desktop review, use the smallest loopback-only preview that is already
available in the environment, for example from the consumer root:

```text
python -m http.server 4173 --bind 127.0.0.1
```

Open the exact `http://127.0.0.1:4173/.../stakeholder-brief.html?view=<route>`
route. Record that URL and the preview environment in the rendered-review
evidence. This server only exposes local files; it does not create a deploy or
substitute for the independent qualitative review.

The user may receive the complete final brief with a truthful residual
limitation when a source fact is unavailable; an agent must never turn an
ordinary composition finding, missing diagram choice, pending local preview or
review handoff into a passive request for approval. Only `approved`/Human
Visibility claims wait for their required evidence. The renderer remains a
byte/lifecycle promotion step; it does not author a missing route, diagram or
task dossier.
- Start with an initiative-local skeleton newly created by
  `scripts/instantiate_brief_skeleton.py` from the canonical v3 template;
  do not reuse a historical skeleton merely because it has matching tabs. The
  candidate starts as that physical file, not as a fresh HTML file. Before
  asking for qualitative review, run
  `python vendor/sdd-harness-guardian/scripts/validate_brief_candidate_inheritance.py
  <candidate> --initiative <initiative> --skeleton <initiative>/brief-candidates/stakeholder-brief.skeleton.html`.
  A metadata-only claim of `data-composition-base` is insufficient: the check
  requires the retained v3 route/component surface and the exact base hash.
- Do not infer technical topology from file names, CSS selectors, task IDs,
  labels or a preferred diagram grammar.
- Do not use lexical scores, card counts or static visual quotas as a quality
  decision.
- Preserve provenance and lifecycle contracts required by the renderer; this
  skill does not authorize rendering, Human Visibility or Tasks Ready.

## Whole-brief authorship check

The skeleton is a layout commitment, not partially reusable editorial copy.
Before handing a candidate to the rendered reviewer, open every one of the
eight desktop routes. Ask whether each **editorial** sentence, label, card or
diagram could have appeared unchanged in an unrelated initiative. If it could,
replace it with a source-backed treatment, a concise justified absence, or an
explicit discovery; do not leave a generic shell proposition beside otherwise
good task or proof dossiers. Apply the same judgment to the global header,
impact, evolution, decision and coverage routes, which are easy to overlook
after architecture and execution are complete.

Do not manufacture variation in stable interaction/lifecycle chrome just to
make a phrase unique: tab names, accessibility affordances, fixed provenance
marks, and the honest common status that Human Visibility/Tasks Ready are
false may remain shared when they are not asserting initiative-specific
substance. The accompanying explanatory editorial copy must still say what
that state means for this initiative.

This is an agentic reading pass, not a word blacklist or a fixed-card rule.
Preserve only the immutable layout, interaction, accessibility fallback and
structural affordances of the skeleton. The author remains responsible for
making every stakeholder-visible editorial block belong to the actual source
package.

## Handoff

Provide the `plan.md` construction record, source locators, known unknowns and
the exact independent-plan-review question. Request a reviewer with a distinct
identity; never issue the review verdict yourself.
