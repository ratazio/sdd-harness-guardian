#!/usr/bin/env python3
"""Promote a reviewed, source-backed candidate into a stakeholder brief.

This command intentionally does not invent content from Markdown. Rich decision
communication remains authored from canonical sources and reviewed by people.
Its job is narrower and safety-critical: a source-only scaffold cannot acquire
an HTML brief by copying the empty canonical shell or by bypassing lifecycle,
structural and local-brand checks.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import uuid
from html.parser import HTMLParser
from pathlib import Path

from new_initiative import provision_pearson_logo
from validate_bundle import stakeholder_brief_errors
from validate_brief_candidate_inheritance import errors as candidate_inheritance_errors
from validate_pearson_brief_policy import policy_errors
from brief_v2_sources import V2_REQUIRED_SOURCES
from brief_review import REVIEW_FINDING_OUTCOMES, review_finding_outcome, yaml_review_finding_outcome
from editorial_exceptions import composition_editorial_findings, reviewed_editorial_exception_error


CANONICAL_COMPOSITION_SOURCES = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "tasks.md",
    "validation-plan.md",
)
ALLOWED_BLOCK_SOURCES = V2_REQUIRED_SOURCES

# This is deliberately a data-only contract.  It describes the *only* bytes a
# promotion is allowed to change; it is not a vocabulary for decision prose.
LIFECYCLE_SCHEMA_VERSION = 1
RENDERED_AUTHORITY_TEXT = (
    "Rendered artifact; rendered-decision review pending; "
    "not approved/deliverable; Tasks Ready false."
)
UNAPPROVED_RENDERED_AUTHORITY_TEXT = (
    "Rendered artifact; autonomous decision review or recovery pending; "
    "not approved/deliverable; Tasks Ready false."
)
PRE_RENDER_PENDING_AUTHORITY_TEXT = (
    "Authored candidate; pre-render review pending; not rendered/deliverable; "
    "Human Visibility and Tasks Ready false."
)
PRE_RENDER_READY_AUTHORITY_TEXT = (
    "Authored candidate; exact pre-render review has passed; ready only for "
    "guarded refresh; not rendered/deliverable; Human Visibility and Tasks Ready false."
)
PRE_RENDER_PENDING_NEXT_STEP_TEXT = (
    "Obtain a distinct exact pre-render review for the current candidate and "
    "source manifest before guarded refresh; Human Visibility and Tasks Ready "
    "remain false."
)
PRE_RENDER_READY_NEXT_STEP_TEXT = (
    "Guarded refresh may be considered only for this exact reviewed candidate; "
    "Human Visibility and Tasks Ready remain false."
)
PRE_RENDER_PENDING_REVIEW_STATUS_TEXT = (
    "Exact distinct pre-render review is pending; no refresh, delivery, Human "
    "Visibility or Tasks Ready decision is authorized."
)
PRE_RENDER_SIGNED_REVIEW_STATUS_TEXT = (
    "Exact distinct pre-render review is recorded; guarded refresh may be "
    "considered, while Human Visibility and Tasks Ready remain false."
)
RENDERED_REVIEW_STATUS_TEXT = (
    "Exact distinct pre-render review is recorded; independent post-render "
    "review is pending; Human Visibility and Tasks Ready remain false."
)
UNAPPROVED_RENDERED_REVIEW_STATUS_TEXT = (
    "The complete source-backed brief is available while independent review or "
    "automatic recovery remains pending; Human Visibility and Tasks Ready false."
)
POST_REVIEW_RECORDED_STATUS_TEXT = (
    "Exact pre-render and independent post-render reviews are recorded; "
    "Human Visibility and Tasks Ready remain separate false decisions."
)
RENDERED_NEXT_STEP_TEXT = (
    "Record the initiative's independent post-render review before any delivery "
    "decision; Human Visibility and Tasks Ready remain false."
)
UNAPPROVED_RENDERED_NEXT_STEP_TEXT = (
    "Run or complete the independent rendered review; recover source-backed "
    "findings automatically before any Human Visibility decision."
)
RENDERED_STATE_SUMMARY_TEXT = (
    "Stakeholder brief rendered; independent post-render review pending; "
    "not approved or deliverable."
)
UNAPPROVED_RENDERED_STATE_SUMMARY_TEXT = (
    "Stakeholder brief rendered from available canonical sources; autonomous "
    "decision review or recovery pending; not approved or deliverable."
)
RENDERED_STATE_CHECKPOINT_TEXT = (
    "Rendered lifecycle transition committed; independent post-render review "
    "is pending."
)
UNAPPROVED_RENDERED_STATE_CHECKPOINT_TEXT = (
    "Unapproved rendered brief committed from available canonical sources; "
    "independent review or automatic recovery is pending."
)
POST_REVIEW_RECORDED_AUTHORITY_TEXT = (
    "Rendered artifact; independent post-render review recorded; "
    "not approved/deliverable; Tasks Ready false."
)
POST_REVIEW_RECORDED_NEXT_STEP_TEXT = (
    "Retain the recorded post-render review; any Human Visibility or delivery "
    "decision remains separate, and Tasks Ready remains false."
)
POST_REVIEW_RECORDED_STATE_SUMMARY_TEXT = (
    "Stakeholder brief rendered; independent post-render review recorded; "
    "not approved or deliverable."
)
POST_REVIEW_RECORDED_STATE_CHECKPOINT_TEXT = (
    "Post-render review recorded against the immutable rendered HTML snapshot; "
    "no delivery decision was made."
)
RECOVERY_BLOCKED_NEXT_STEP_TEXT = (
    "Resolve the blocked lifecycle checkpoint before any refresh or delivery; "
    "Human Visibility and Tasks Ready remain false."
)
RECOVERY_BLOCKED_AUTHORITY_TEXT = (
    "Lifecycle recovery blocked; no refresh or delivery is authorized; "
    "Human Visibility and Tasks Ready false."
)
AUTHORITY_PROJECTION = "lifecycle-authority"
LIFECYCLE_MARKERS = {
    "brief-phase": {
        "tag": "html", "attribute": "data-brief-phase",
        "source": "run-state.yaml", "fragment": "brief_phase",
        "value": lambda rendered_state: "rendered",
    },
    "rendered-state-digest": {
        "tag": "meta", "attribute": "content",
        "source": "run-state.yaml", "fragment": "rendered run-state bytes",
        "value": lambda rendered_state: hashlib.sha256(rendered_state.encode("utf-8")).hexdigest(),
    },
    "rendered-authority": {
        # Repeated, opt-in authority statements. Their tag, location, and
        # authored pre-render wording belong to the candidate; promotion may
        # replace only their direct text.
        "attribute": "text", "source": "run-state.yaml",
        "value": lambda rendered_state: lifecycle_authority_projection(rendered_state),
    },
    "rendered-next-safe-step": {
        # Like authority, an exact next action is author-declared direct text.
        # Promotion may change it only when the candidate has explicitly bound
        # the element to the closed lifecycle next-step projection.
        "attribute": "text", "source": "run-state.yaml",
        "value": lambda rendered_state: lifecycle_projection(
            "lifecycle-next-safe-step", rendered_state
        ),
    },
    "rendered-review-status": {
        # An optional, explicit body hook for source-composed lifecycle prose.
        # It is not a search-and-replace facility: only this direct text is
        # renderer-owned, and an unmarked sentence is never rewritten.
        "attribute": "text", "source": "run-state.yaml",
        "value": lambda rendered_state: lifecycle_projection(
            "lifecycle-review-status", rendered_state
        ),
    },
    "rendered-state-source-digest": {
        # A source-backed block may opt in to refreshing its run-state digest.
        # It deliberately has no tag, layout, or identifier contract: the
        # author owns those. Promotion changes only this direct attribute on
        # an explicitly declared run-state block.
        "attribute": "data-source-digest",
        "source": "run-state.yaml",
        "value": lambda rendered_state: "sha256:" + hashlib.sha256(rendered_state.encode("utf-8")).hexdigest(),
    },
}

# Canonical source files may opt in to the same transition.  This deliberately
# is a tiny, closed syntax rather than a search for phrases such as "refresh"
# or "candidate".  It works in any textual source format which can carry an
# HTML comment (Markdown is the usual case) and never changes unmarked bytes.
SOURCE_AUTHORITY_OPEN = "sdd-lifecycle-authority"
SOURCE_AUTHORITY_CLOSE = "/sdd-lifecycle-authority"
SOURCE_AUTHORITY_RE = re.compile(
    r'<!--\s*sdd-lifecycle-authority\s+'
    r'source="(?P<source>[^"]+)"\s+projection="(?P<projection>[^"]+)"\s+fragment="(?P<fragment>[^"]+)"\s*-->'
    r'(?P<text>.*?)<!--\s*/sdd-lifecycle-authority\s*-->', re.DOTALL,
)
# YAML has no native inline span syntax.  An opted-in field is therefore
# delimited by comments and declares the one scalar it permits promotion to
# replace.  The field name is data, not a hard-coded operational vocabulary.
SOURCE_AUTHORITY_YAML_RE = re.compile(
    r'(?m)^(?P<open>[ \t]*#\s*sdd-lifecycle-authority\s+'
    r'source="(?P<source>[^"]+)"\s+projection="(?P<projection>[^"]+)"\s+'
    r'fragment="(?P<fragment>[^"]+)"\s+field="(?P<field>[A-Za-z_][A-Za-z0-9_]*)"\s*\r?\n)'
    r'(?P<indent>[ \t]*)(?P=field):\s*(?P<quote>["\'])(?P<text>[^\r\n"\']*)(?P=quote)\s*\r?\n'
    r'(?P<close>[ \t]*#\s*/sdd-lifecycle-authority\s*)$',
)
COMMIT_POINTS = (
    "temp_html", "temp_state", "journal", "backup_target", "backup_state",
    "rename_state", "rename_target", "cleanup", "recovery_restore_target",
    "recovery_restore_state", "recovery_cleanup",
)


class ProvenanceParser(HTMLParser):
    """Collect declared source blocks without deriving quality from their text."""

    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[dict[str, str]] = []
        self._open_elements: list[tuple[str, dict[str, str] | None]] = []
        self.nesting_error: str | None = None

    _VOID_TAGS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr",
    }

    def _provenance_block(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> dict[str, str] | None:
        values = {name: value or "" for name, value in attrs}
        provenance = ("data-source", "data-source-section", "data-coverage", "data-source-digest")
        if any(name in values for name in provenance):
            values["__tag"] = tag
            values["__text"] = ""
            self.blocks.append(values)
            return values
        return None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        active = self._provenance_block(tag, attrs)
        # HTMLParser does not emit an end tag for void elements. Keeping them
        # out of this stack prevents an <img> or <meta> from breaking the
        # visible-text association of a surrounding provenance block.
        if tag not in self._VOID_TAGS:
            self._open_elements.append((tag, active))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # A self-closing provenance element is recorded but has no visible text,
        # so provenance_error() will reject it through the fragment check.
        self._provenance_block(tag, attrs)

    def handle_data(self, data: str) -> None:
        for _, block in self._open_elements:
            if block is not None:
                block["__text"] += data

    def handle_endtag(self, tag: str) -> None:
        if tag in self._VOID_TAGS:
            self.nesting_error = self.nesting_error or f"void element </{tag}> must not have an end tag"
            return
        if not self._open_elements:
            self.nesting_error = self.nesting_error or f"unexpected closing element </{tag}>"
            return
        opened, _ = self._open_elements[-1]
        if opened != tag:
            self.nesting_error = self.nesting_error or (
                f"closing element </{tag}> does not match open <{opened}>"
            )
            return
        self._open_elements.pop()

    def final_nesting_error(self) -> str | None:
        if self.nesting_error:
            return self.nesting_error
        if self._open_elements:
            return f"unclosed element <{self._open_elements[-1][0]}>"
        return None


class LifecycleParser(HTMLParser):
    """Parse lifecycle declarations without accepting duplicate HTML attributes."""

    _VOID_TAGS = ProvenanceParser._VOID_TAGS

    def __init__(self) -> None:
        super().__init__()
        self.markers: list[tuple[str, list[tuple[str, str | None]], tuple[str, ...]]] = []
        self.marker_in_coverage_register: list[bool] = []
        self.marker_depths: list[int] = []
        self.marker_text: list[str] = []
        self.marker_has_nested_content: list[bool] = []
        self.marker_open: list[bool] = []
        self.error: str | None = None
        self.stack: list[tuple[str, dict[str, str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for index, depth in enumerate(self.marker_depths):
            if self.marker_open[index] and len(self.stack) >= depth:
                self.marker_has_nested_content[index] = True
        names = [name.lower() for name, _ in attrs]
        lifecycle_names = [name for name in names if name.startswith("data-lifecycle-")]
        if lifecycle_names and len(names) != len(set(names)):
            self.error = self.error or "lifecycle marker has duplicate HTML attributes"
        values = dict((name.lower(), value or "") for name, value in attrs)
        if lifecycle_names and "data-lifecycle-marker" not in values:
            self.error = self.error or "undeclared data-lifecycle attribute"
        if "data-lifecycle-marker" in values:
            self.markers.append((tag.lower(), attrs, tuple(open_tag for open_tag, _ in self.stack)))
            self.marker_in_coverage_register.append(any(
                open_tag == "table" and open_attrs.get("id") == "coverage-register"
                for open_tag, open_attrs in self.stack
            ))
            self.marker_depths.append(len(self.stack) + 1)
            self.marker_text.append("")
            self.marker_has_nested_content.append(False)
            self.marker_open.append(True)
        if tag.lower() not in self._VOID_TAGS:
            self.stack.append((tag.lower(), values))

    def handle_endtag(self, tag: str) -> None:
        if self.stack and self.stack[-1][0] == tag.lower():
            for index, depth in enumerate(self.marker_depths):
                if self.marker_open[index] and len(self.stack) == depth:
                    self.marker_open[index] = False
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        for index, depth in enumerate(self.marker_depths):
            if self.marker_open[index] and len(self.stack) == depth:
                self.marker_text[index] += data
            elif self.marker_open[index] and len(self.stack) > depth:
                self.marker_has_nested_content[index] = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("initiative", type=Path, help="initiative directory under specs/NNN-slug")
    parser.add_argument("--candidate", type=Path, help="reviewed candidate HTML outside the initiative delivery path")
    parser.add_argument(
        "--render-unapproved",
        action="store_true",
        help=("render a complete, source-bound candidate for autonomous review/recovery without "
              "granting Human Visibility, delivery approval, or Tasks Ready"),
    )
    parser.add_argument("--refresh", action="store_true", help="replace an existing historical brief only with an explicit refresh")
    parser.add_argument(
        "--allow-reviewed-editorial-exceptions", action="store_true",
        help=("permit only current deterministic editorial findings that are visibly disclosed and "
              "fully bound to this exact candidate's independent pre-render review; integrity, "
              "provenance, lifecycle and safety failures still refuse promotion"),
    )
    parser.add_argument(
        "--finalize-post-review", action="store_true",
        help="atomically record an already-approved independent rendered review; no delivery decision is made",
    )
    parser.add_argument("--fault-at", choices=COMMIT_POINTS, help=argparse.SUPPRESS)
    return parser.parse_args()


def scalar(content: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*[\"']?([^\n\"']+)", content)
    value = match.group(1).strip() if match else None
    return None if value in {None, "null", "None", ""} else value


def brief_review_field(state: str, key: str) -> str | None:
    """Read one field from the structured brief_review mapping only."""
    match = re.search(r"(?ms)^brief_review:\s*\n(?P<body>(?:^[ \t]+.*\n?)*)", state)
    if not match:
        return None
    value = re.search(rf"(?m)^\s+{re.escape(key)}:\s*[\"']?([^\n\"']+)", match.group("body"))
    result = value.group(1).strip() if value else None
    return None if result in {None, "null", "None", ""} else result


def brief_review_finding_outcome(state: str) -> str | None:
    """Read the status without trimming semantic whitespace or nested quotes."""
    match = re.search(r"(?ms)^brief_review:\s*\n(?P<body>(?:^[ \t]+.*\n?)*)", state)
    if not match:
        return None
    value = re.search(r"(?m)^\s+findings_status:\s?(.*)$", match.group("body"))
    return yaml_review_finding_outcome(value.group(1) if value else None)


def lifecycle_authority_projection(
    state: str, initiative: Path | None = None, candidate_html: str | None = None
) -> str:
    """Derive the only permitted lifecycle authority projection from state.

    This is intentionally a closed state machine.  Authority markers can opt
    in to this projection, but neither markers nor a free-text state scalar can
    select its result.
    """
    # A blocked checkpoint is an explicit lifecycle fact, not an invitation to
    # infer authority from retained candidate prose or historical review
    # records.  It therefore takes precedence over the otherwise valid phase.
    if scalar(state, "status") == "blocked":
        return RECOVERY_BLOCKED_AUTHORITY_TEXT
    brief_phase = scalar(state, "brief_phase")
    current_phase = scalar(state, "current_phase")
    if brief_phase == "rendered" and current_phase == "rendered_autonomous_review_pending":
        return UNAPPROVED_RENDERED_AUTHORITY_TEXT
    if brief_phase == "rendered" and current_phase == "rendered_decision_review_pending":
        return RENDERED_AUTHORITY_TEXT
    if brief_phase == "rendered" and current_phase == "rendered_decision_review_recorded":
        return POST_REVIEW_RECORDED_AUTHORITY_TEXT
    if brief_phase != "ready_to_render" or current_phase != "render_pending":
        raise ValueError("run-state has an unknown or incompatible lifecycle phase for authority projection")
    review = {key: brief_review_field(state, key) for key in (
        "author", "coverage_reviewer", "reviewed_at", "review_record", "findings_status",
    )}
    if all(value is None for value in review.values()):
        return PRE_RENDER_PENDING_AUTHORITY_TEXT
    # A candidate is an immutable review input.  Its author can declare the
    # record that will contain a later signature while all reviewer-owned
    # state remains pending.  Do not require copying that signature back into
    # the candidate's state: doing so changes the input after it was signed.
    if not review["author"] or not review["review_record"]:
        return PRE_RENDER_PENDING_AUTHORITY_TEXT
    if initiative is None or candidate_html is None:
        raise ValueError("exact pre-render review linkage is required for ready authority projection")
    review_error = pre_render_review_error(
        initiative, state, candidate_html,
        hashlib.sha256(candidate_html.encode("utf-8")).hexdigest(),
    )
    if review_error:
        # A fully asserted legacy review remains an authority claim and must
        # fail loudly when its binding is invalid.  A pending signing state is
        # merely a candidate waiting for its independent reviewer.
        if review["coverage_reviewer"] and review["reviewed_at"] and brief_review_finding_outcome(state) == "pass":
            raise ValueError(f"pre-render authority projection requires validated review linkage: {review_error}")
        return PRE_RENDER_PENDING_AUTHORITY_TEXT
    return PRE_RENDER_READY_AUTHORITY_TEXT


def lifecycle_projection(
    projection: str, state: str, initiative: Path | None = None, candidate_html: str | None = None,
) -> str:
    """Return one closed operational lifecycle projection from structured state.

    Declarations choose a projection name, never their own rendered wording.
    This keeps operational source claims declarative while allowing an author
    to opt in a summary, checkpoint, or next-step slot without a filename or
    phrase catalogue.
    """
    authority = lifecycle_authority_projection(state, initiative, candidate_html)
    if projection == "lifecycle-review-status":
        if authority == RECOVERY_BLOCKED_AUTHORITY_TEXT:
            return RECOVERY_BLOCKED_AUTHORITY_TEXT
        if authority == UNAPPROVED_RENDERED_AUTHORITY_TEXT:
            return UNAPPROVED_RENDERED_REVIEW_STATUS_TEXT
        if authority == RENDERED_AUTHORITY_TEXT:
            return RENDERED_REVIEW_STATUS_TEXT
        if authority == POST_REVIEW_RECORDED_AUTHORITY_TEXT:
            return POST_REVIEW_RECORDED_STATUS_TEXT
        if authority == PRE_RENDER_READY_AUTHORITY_TEXT:
            return PRE_RENDER_SIGNED_REVIEW_STATUS_TEXT
        return PRE_RENDER_PENDING_REVIEW_STATUS_TEXT
    if projection == AUTHORITY_PROJECTION:
        return authority
    if projection != "lifecycle-next-safe-step":
        raise ValueError("source lifecycle declaration has an unknown projection")
    if authority == RECOVERY_BLOCKED_AUTHORITY_TEXT:
        return RECOVERY_BLOCKED_NEXT_STEP_TEXT
    if authority == UNAPPROVED_RENDERED_AUTHORITY_TEXT:
        return UNAPPROVED_RENDERED_NEXT_STEP_TEXT
    if authority == RENDERED_AUTHORITY_TEXT:
        return RENDERED_NEXT_STEP_TEXT
    if authority == POST_REVIEW_RECORDED_AUTHORITY_TEXT:
        return POST_REVIEW_RECORDED_NEXT_STEP_TEXT
    if authority == PRE_RENDER_READY_AUTHORITY_TEXT:
        return PRE_RENDER_READY_NEXT_STEP_TEXT
    return PRE_RENDER_PENDING_NEXT_STEP_TEXT


def immutable_candidate_pending_projection(
    actual: str, expected: str, state: str | None,
) -> bool:
    """Allow an authored review input to retain its conservative pending text.

    Once a reviewer signs the exact candidate, replacing its lifecycle text
    with the newly-ready projection would invalidate that signature.  Pending
    is a strictly lower-authority statement, so it is safe to retain only on
    an authored ``ready_to_render`` input.  Rendered output is still rewritten
    from the computed state and never receives this exception.
    """
    if state is None or scalar(state, "brief_phase") != "ready_to_render":
        return False
    return (expected, actual) in {
        (PRE_RENDER_READY_AUTHORITY_TEXT, PRE_RENDER_PENDING_AUTHORITY_TEXT),
        (PRE_RENDER_READY_NEXT_STEP_TEXT, PRE_RENDER_PENDING_NEXT_STEP_TEXT),
        (PRE_RENDER_SIGNED_REVIEW_STATUS_TEXT, PRE_RENDER_PENDING_REVIEW_STATUS_TEXT),
    }


def rendered_lifecycle_state(
    state: str, initiative: Path | None = None, candidate_html: str | None = None,
) -> str:
    """Prepare the exact lifecycle-only state transition for promotion.

    The state is staged with the rendered HTML and committed as the same
    recoverable pair.  Apart from phase, only the three canonical operational
    scalars are normalized, so a rendered checkpoint cannot retain a
    pre-render refresh instruction.  Narrative artifacts remain authored
    evidence and are not rewritten here.
    """
    if scalar(state, "status") not in {None, "executing"}:
        raise ValueError('run-state status must be "executing" before rendering')
    if scalar(state, "brief_phase") != "ready_to_render":
        raise ValueError('run-state brief_phase must be "ready_to_render"')
    if scalar(state, "current_phase") != "render_pending":
        raise ValueError('run-state current_phase must be "render_pending" before rendering')
    rendered = state.replace('brief_phase: "ready_to_render"', 'brief_phase: "rendered"', 1)
    rendered = rendered.replace(
        'current_phase: "render_pending"',
        'current_phase: "rendered_decision_review_pending"',
        1,
    )
    for field, value in (
        ("summary", RENDERED_STATE_SUMMARY_TEXT),
        ("last_safe_checkpoint", RENDERED_STATE_CHECKPOINT_TEXT),
        ("next_safe_step", RENDERED_NEXT_STEP_TEXT),
    ):
        pattern = re.compile(rf'(?m)^(?P<prefix>{re.escape(field)}: )(?:null|"[^"\r\n]*")$')
        rendered, replacements = pattern.subn(rf'\g<prefix>"{value}"', rendered, count=1)
        if replacements != 1:
            raise ValueError(f'run-state must declare one quoted {field} scalar before rendering')
    if rendered == state or scalar(rendered, "brief_phase") != "rendered" or scalar(rendered, "current_phase") != "rendered_decision_review_pending":
        raise ValueError("could not prepare declared render lifecycle transition")
    return rendered


def _set_quoted_scalar(state: str, key: str, value: str) -> str:
    """Replace one top-level YAML scalar without interpreting source prose."""
    pattern = re.compile(rf'(?m)^(?P<prefix>{re.escape(key)}: )(?:null|"[^"\r\n]*")$')
    updated, replacements = pattern.subn(rf'\g<prefix>"{value}"', state, count=1)
    if replacements != 1:
        raise ValueError(f'run-state must declare one quoted {key} scalar before rendering')
    return updated


def rendered_unapproved_lifecycle_state(state: str) -> str:
    """Stage a source-bound final brief without asserting review approval.

    This is intentionally a lifecycle-only escape from a passive composition
    stop. It never grants Human Visibility, Tasks Ready, delivery, or content
    authority; it merely permits a composed candidate with real source bindings
    to become the reviewable final HTML while a reviewer or recovery loop works.
    """
    if scalar(state, "status") not in {None, "draft", "spec_ready", "executing"}:
        raise ValueError('run-state status must be draft/spec_ready/executing before unapproved rendering')
    if scalar(state, "brief_lineage") not in {None, "v2"}:
        raise ValueError('unapproved rendering requires v2 lineage or an unset brief_lineage')
    if scalar(state, "brief_phase") not in {None, "not_rendered", "ready_to_render", "rendered"}:
        raise ValueError('run-state brief_phase must be not_rendered/ready_to_render/rendered before unapproved rendering')
    if scalar(state, "human_visibility_ready") == "true" or scalar(state, "tasks_ready") == "true":
        raise ValueError('unapproved rendering refuses a state that already claims Human Visibility or Tasks Ready')

    rendered = _set_quoted_scalar(state, "status", "executing")
    rendered = _set_quoted_scalar(rendered, "brief_lineage", "v2")
    rendered = _set_quoted_scalar(rendered, "brief_phase", "rendered")
    rendered = _set_quoted_scalar(rendered, "current_phase", "rendered_autonomous_review_pending")
    for field, value in (
        ("summary", UNAPPROVED_RENDERED_STATE_SUMMARY_TEXT),
        ("last_safe_checkpoint", UNAPPROVED_RENDERED_STATE_CHECKPOINT_TEXT),
        ("next_safe_step", UNAPPROVED_RENDERED_NEXT_STEP_TEXT),
    ):
        rendered = _set_quoted_scalar(rendered, field, value)
    return rendered


def post_review_recorded_lifecycle_state(state: str) -> str:
    """Prepare the non-delivery state after a verified rendered review.

    This is deliberately a narrow lifecycle transition.  It records only that
    an independent review exists for an immutable already-rendered HTML
    snapshot.  It does not set Human Visibility, Tasks Ready, task status or
    any delivery/approval field.
    """
    if scalar(state, "status") not in {None, "executing"}:
        raise ValueError('run-state status must be "executing" before recording post-render review')
    if scalar(state, "brief_phase") != "rendered":
        raise ValueError('run-state brief_phase must be "rendered" before recording post-render review')
    if scalar(state, "current_phase") not in {
        "rendered_decision_review_pending", "rendered_autonomous_review_pending",
    }:
        raise ValueError('run-state current_phase must be a rendered review-pending phase before recording post-render review')
    pending_phase = scalar(state, "current_phase")
    reviewed = state.replace(
        f'current_phase: "{pending_phase}"',
        'current_phase: "rendered_decision_review_recorded"',
        1,
    )
    for field, value in (
        ("summary", POST_REVIEW_RECORDED_STATE_SUMMARY_TEXT),
        ("last_safe_checkpoint", POST_REVIEW_RECORDED_STATE_CHECKPOINT_TEXT),
        ("next_safe_step", POST_REVIEW_RECORDED_NEXT_STEP_TEXT),
    ):
        pattern = re.compile(rf'(?m)^(?P<prefix>{re.escape(field)}: )(?:null|"[^"\r\n]*")$')
        reviewed, replacements = pattern.subn(rf'\g<prefix>"{value}"', reviewed, count=1)
        if replacements != 1:
            raise ValueError(f'run-state must declare one quoted {field} scalar before recording post-render review')
    if reviewed == state or scalar(reviewed, "current_phase") != "rendered_decision_review_recorded":
        raise ValueError("could not prepare declared post-render review lifecycle transition")
    return reviewed


def fail(message: str) -> int:
    print(f"Render refused: {message}", file=sys.stderr)
    return 1


def review_record_content(log: str, record_id: str) -> str | None:
    """Resolve one explicit decision section without searching the whole log.

    A single table cell can identify a decision, but cannot carry a complete
    composition review.  Promotion therefore accepts only an explicit Markdown
    decision section headed by the same ID named by run-state.
    """
    heading = re.compile(rf"(?m)^(?P<level>#+)\s+{re.escape(record_id)}\b.*$")
    match = heading.search(log)
    if not match:
        return None
    next_heading = re.compile(r"(?m)^(?P<level>#+)\s+")
    following = next(
        (item for item in next_heading.finditer(log, match.end()) if len(item.group("level")) <= len(match.group("level"))),
        None,
    )
    return log[match.start() : following.start() if following else len(log)]


def record_field(record: str, *names: str) -> str | None:
    """Read a labelled review field from its resolved decision section only."""
    for name in names:
        match = re.search(
            rf"(?im)^\s*(?:[-*]\s*)?{re.escape(name)}\s*:\s*(.+?)\s*$",
            record,
        )
        if match:
            return match.group(1).strip()
    return None


def record_exact_literal(record: str, literal: str, *names: str) -> bool:
    """Require an authored record field to contain one unnormalized literal.

    The one space after ``:`` is Markdown field syntax.  Any further
    whitespace, quoting, casing or prose is field content and is not approval.
    """
    for name in names:
        pattern = rf"(?m)^\s*(?:[-*]\s*)?{re.escape(name)}: (?P<value>.*)$"
        match = re.search(pattern, record)
        if match:
            return match.group("value") == literal
    return False


def decision_record_digest(record: str) -> str:
    """Digest stable decision context while excluding the signing envelope.

    A candidate can cite the decision section before an independent reviewer
    signs it.  The signature necessarily adds the candidate hash and reviewer
    attestation, so those fields cannot participate in a digest embedded in
    that same immutable input.  They are instead validated directly from the
    resolved current record by ``pre_render_review_error``.  Scope, authored
    rationale, source manifest and every other field remain context-bound.
    """
    normalized = re.sub(
        r"(?im)^\s*(?:[-*]\s*)?(?:Candidate SHA-256|candidate_sha256|Reviewer|Coverage reviewer|Review outcome|Coverage review outcome|Composition provenance|Human attestation)\s*:\s*.*(?:\r?\n|$)",
        "",
        record,
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def provenance_error(
    initiative: Path, candidate_html: str, decision: str,
    source_manifest: dict[str, bytes] | None = None,
) -> str | None:
    """Validate local source bindings; never judge the prose they support."""
    parser = ProvenanceParser()
    parser.feed(candidate_html)
    parser.close()
    nesting_error = parser.final_nesting_error()
    if nesting_error:
        return f"candidate HTML has malformed element nesting: {nesting_error}"
    if not parser.blocks:
        return "candidate must declare source provenance for material blocks"
    for block in parser.blocks:
        source = block.get("data-source", "")
        section = block.get("data-source-section", "")
        coverage = block.get("data-coverage", "")
        declared_digest = block.get("data-source-digest", "")
        fragment = block.get("data-source-fragment", "")
        fragment_digest = block.get("data-source-fragment-sha256", "")
        if not source or not section or not coverage or not declared_digest or not fragment or not fragment_digest:
            return "every declared provenance block requires data-source, data-source-section, data-coverage, data-source-digest, data-source-fragment and data-source-fragment-sha256"
        if source not in ALLOWED_BLOCK_SOURCES:
            return f"provenance source is not allowed for this initiative: {source}"
        if source == "decision-log.md":
            expected = f"decision-record-sha256:{decision_record_digest(decision)}"
        else:
            source_path = initiative / source
            if not source_path.is_file():
                return f"provenance source does not exist in this initiative: {source}"
            source_bytes = (source_manifest or {}).get(source, source_path.read_bytes())
            expected = f"sha256:{hashlib.sha256(source_bytes).hexdigest()}"
        if declared_digest != expected:
            return f"provenance digest does not bind the current local source: {source}"
        if source == "decision-log.md":
            source_text = decision
        else:
            source_text = (source_manifest or {}).get(source, source_path.read_bytes()).decode("utf-8")
        if fragment not in source_text:
            return f"provenance fragment is not present in the current local source: {source}"
        expected_fragment_digest = hashlib.sha256(fragment.encode("utf-8")).hexdigest()
        if fragment_digest != f"sha256:{expected_fragment_digest}":
            return f"provenance fragment digest does not bind the declared source fragment: {source}"
        if fragment not in block.get("__text", ""):
            return f"provenance fragment is not visible in its rendered source block: {source}"
    return None


def final_source_manifest(
    initiative: Path, rendered_state: str, source_updates: dict[Path, str],
) -> dict[str, bytes]:
    """Return the canonical source bytes that will exist after promotion.

    This is intentionally source-first: rendered provenance is derived from
    staged state/source records, never repaired after those records become
    visible.  The mapping is layout-agnostic and contains every readable
    canonical source which a provenance block may name.
    """
    manifest: dict[str, bytes] = {"run-state.yaml": rendered_state.encode("utf-8")}
    for path in initiative.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        try:
            relative = path.relative_to(initiative).as_posix()
            manifest.setdefault(relative, path.read_bytes())
        except ValueError:
            continue
    for path, content in source_updates.items():
        manifest[path.relative_to(initiative).as_posix()] = content.encode("utf-8")
    return manifest


def render_provenance_digests(
    candidate_html: str, source_manifest: dict[str, bytes], *, preserve_rendered_state_snapshot: bool = False,
) -> str:
    """Bind each declared local source digest to the final source manifest.

    Only an existing ``data-source-digest`` attribute is rewritten.  This
    preserves the candidate's authored source topology and cannot infer a
    source or a claim from prose.
    """
    def attribute(attributes: str, name: str) -> str | None:
        match = re.search(rf'\b{re.escape(name)}\s*=\s*["\']([^"\']*)["\']', attributes)
        return match.group(1) if match else None

    def rewrite(match: re.Match[str]) -> str:
        tag, attributes = match.groups()
        source = attribute(attributes, "data-source")
        # Decision records use a deliberately scoped, self-cycle-safe digest
        # rather than the digest of the entire mutable decision log.
        if source == "decision-log.md" or source not in source_manifest or attribute(attributes, "data-source-digest") is None:
            return match.group(0)
        if (preserve_rendered_state_snapshot and source == "run-state.yaml"
                and attribute(attributes, "data-lifecycle-marker") == "rendered-state-source-digest"):
            return match.group(0)
        digest = hashlib.sha256(source_manifest[source]).hexdigest()
        attributes = re.sub(
            r'(\bdata-source-digest\s*=\s*["\'])[^"\']*(["\'])',
            rf"\g<1>sha256:{digest}\g<2>", attributes, count=1,
        )
        return f"<{tag}{attributes}>"

    rendered = re.sub(r"(?is)<([a-z][a-z0-9:-]*)\b([^>]*)>", rewrite, candidate_html)

    return rendered


def _declared_lifecycle_texts(content: str) -> dict[tuple[str, str, str, str], list[str]]:
    """Return text owned by explicit source-lifecycle declarations only.

    This is deliberately not a general-purpose source diff.  A promotion may
    carry a provenance fragment forward only when that fragment contains text
    from a declared lifecycle span which the same promotion is allowed to
    replace.
    """
    declared: dict[tuple[str, str, str, str], list[str]] = {}
    for expression in (SOURCE_AUTHORITY_RE, SOURCE_AUTHORITY_YAML_RE):
        for match in expression.finditer(content):
            key = (
                match.group("source"), match.group("projection"),
                match.group("fragment"), match.groupdict().get("field", ""),
            )
            declared.setdefault(key, []).append(match.group("text"))
    return declared


def lifecycle_source_fragment_replacements(
    initiative: Path, source_manifest: dict[str, bytes],
) -> dict[str, list[tuple[str, str]]]:
    """Derive allowed provenance-fragment replacements from staged sources.

    Both sides must have an identical declaration topology.  This makes the
    final HTML bind the source bundle being promoted, including a lifecycle
    field embedded in an otherwise factual fragment, without granting the
    renderer authority to rewrite arbitrary source citations.
    """
    replacements: dict[str, list[tuple[str, str]]] = {}
    for relative, after_bytes in source_manifest.items():
        path = initiative / relative
        if not path.is_file():
            continue
        try:
            before = path.read_text(encoding="utf-8")
            after = after_bytes.decode("utf-8")
        except UnicodeDecodeError:
            continue
        before_declared = _declared_lifecycle_texts(before)
        if not before_declared:
            continue
        after_declared = _declared_lifecycle_texts(after)
        if set(before_declared) != set(after_declared):
            raise ValueError(f"staged lifecycle declaration topology changed: {relative}")
        pairs: list[tuple[str, str]] = []
        for key, old_texts in before_declared.items():
            new_texts = after_declared[key]
            if len(old_texts) != len(new_texts):
                raise ValueError(f"staged lifecycle declaration count changed: {relative}")
            pairs.extend((old, new) for old, new in zip(old_texts, new_texts) if old != new)
        if pairs:
            replacements[relative] = pairs

    # ``run-state.yaml`` is the other deliberately staged member of the
    # promotion pair.  Rendering changes exactly these three root scalars to
    # close an active pre-render checkpoint.  A provenance fragment which
    # cites one of their *complete YAML scalars* must therefore move to the
    # staged state too; otherwise the final HTML correctly has a final digest
    # but incorrectly cites a pre-render value.  Do not treat this as a
    # general run-state rewrite: partial values, nested fields and every field
    # outside this small declared transition stay ineligible.
    state_after = source_manifest.get("run-state.yaml")
    state_path = initiative / "run-state.yaml"
    if state_after is not None and state_path.is_file():
        try:
            state_before_text = state_path.read_text(encoding="utf-8")
            state_after_text = state_after.decode("utf-8")
        except UnicodeDecodeError:
            state_before_text = state_after_text = ""
        state_pairs: list[tuple[str, str]] = []
        for field in ("summary", "last_safe_checkpoint", "next_safe_step"):
            pattern = re.compile(rf'(?m)^{re.escape(field)}: "(?P<value>[^"\r\n]*)"$')
            before_match = pattern.search(state_before_text)
            after_match = pattern.search(state_after_text)
            if before_match and after_match and before_match.group(0) != after_match.group(0):
                state_pairs.append((before_match.group(0), after_match.group(0)))
        if state_pairs:
            replacements["run-state.yaml"] = [
                *replacements.get("run-state.yaml", []), *state_pairs,
            ]
    return replacements


def render_provenance_fragments(
    candidate_html: str, initiative: Path, source_manifest: dict[str, bytes],
    *, preserve_rendered_state_snapshot: bool = False,
) -> str:
    """Refresh only provenance fragments changed by declared lifecycle spans.

    Digests alone are insufficient: a fragment citation has to occur in the
    final local source as well.  Transforming the declared fragment and its
    digest in the same in-memory render transaction keeps that binding atomic.
    """
    replacements = lifecycle_source_fragment_replacements(initiative, source_manifest)

    def attribute(attributes: str, name: str) -> str | None:
        match = re.search(rf'\b{re.escape(name)}\s*=\s*["\']([^"\']*)["\']', attributes)
        return html.unescape(match.group(1)) if match else None

    def rewrite(match: re.Match[str]) -> str:
        tag, attributes = match.groups()
        source = attribute(attributes, "data-source")
        fragment = attribute(attributes, "data-source-fragment")
        if (preserve_rendered_state_snapshot and source == "run-state.yaml"
                and attribute(attributes, "data-lifecycle-marker") == "rendered-state-source-digest"):
            return match.group(0)
        if not source or fragment is None or source not in replacements:
            return match.group(0)
        rewritten_fragment = fragment
        for old, new in replacements[source]:
            if old in rewritten_fragment:
                rewritten_fragment = rewritten_fragment.replace(old, new)
        if rewritten_fragment == fragment:
            return match.group(0)
        escaped_fragment = html.escape(rewritten_fragment, quote=True)
        attributes = re.sub(
            r'(\bdata-source-fragment\s*=\s*["\'])[^"\']*(["\'])',
            rf"\g<1>{escaped_fragment}\g<2>", attributes, count=1,
        )
        fragment_digest = hashlib.sha256(rewritten_fragment.encode("utf-8")).hexdigest()
        attributes = re.sub(
            r'(\bdata-source-fragment-sha256\s*=\s*["\'])[^"\']*(["\'])',
            rf"\g<1>sha256:{fragment_digest}\g<2>", attributes, count=1,
        )
        return f"<{tag}{attributes}>"

    rendered = re.sub(r"(?is)<([a-z][a-z0-9:-]*)\b([^>]*)>", rewrite, candidate_html)
    # Attribute rewriting above intentionally works on opening tags so nested
    # provenance blocks retain their authored layout. Find matching close tags
    # with a small stack before synchronizing visible source text; a
    # whole-element regex would let an outer <html> consume nested blocks.
    token = re.compile(r"(?is)<(?P<closing>/)?(?P<tag>[a-z][a-z0-9:-]*)\b(?P<attributes>[^>]*)>")
    stack: list[tuple[str, int, str | None, str | None]] = []
    body_ranges: list[tuple[int, int, list[tuple[str, str]]]] = []
    for match in token.finditer(rendered):
        tag = match.group("tag").lower()
        if not match.group("closing"):
            if tag in ProvenanceParser._VOID_TAGS or match.group("attributes").rstrip().endswith("/"):
                continue
            attrs = match.group("attributes")
            stack.append((tag, match.end(), attribute(attrs, "data-source"), attribute(attrs, "data-source-fragment")))
            continue
        for index in range(len(stack) - 1, -1, -1):
            if stack[index][0] != tag:
                continue
            _tag, body_start, source, fragment = stack.pop(index)
            if source in replacements and fragment is not None:
                pairs = [(old, new) for old, new in replacements[source] if new in fragment]
                if pairs:
                    body_ranges.append((body_start, match.start(), pairs))
            break
    for start, end, pairs in reversed(body_ranges):
        body = rendered[start:end]
        for old, new in pairs:
            body = body.replace(old, new)
        rendered = rendered[:start] + body + rendered[end:]
    return rendered


def provenance_topology_digest(html: str) -> str:
    """Digest source topology, never narrative text or visual quantity."""
    parser = ProvenanceParser()
    parser.feed(html)
    parser.close()
    topology = [
        (
            block.get("__tag", ""),
            block.get("data-source", ""),
            block.get("data-source-section", ""),
            block.get("data-coverage", ""),
        )
        for block in parser.blocks
    ]
    return hashlib.sha256(
        json.dumps(topology, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    ).hexdigest()


def scaffold_topology_error(candidate_html: str) -> str | None:
    """Reject a relabelled scaffold by its canonical provenance topology.

    A real composition may preserve useful layout conventions, but must replace
    the scaffold's generic source/locator/disposition topology with a reviewed
    mapping for its own initiative. This deliberately does not inspect prose,
    word count, tabs, cards, diagrams or CSS quality.
    """
    template = Path(__file__).resolve().parent.parent / ".harness" / "templates" / "stakeholder-brief.html"
    if not template.is_file():
        return "canonical stakeholder brief template is required to verify composition identity"
    if provenance_topology_digest(candidate_html) == provenance_topology_digest(
        template.read_text(encoding="utf-8")
    ):
        return "candidate retains the canonical scaffold provenance topology; a composed review mapping is required"
    return None


def root_attribute(html: str, name: str) -> str | None:
    root = re.search(r"(?is)<html\b([^>]*)>", html)
    if not root:
        return None
    value = re.search(
        rf"\b{re.escape(name)}\s*=\s*[\"']([^\"']*)[\"']",
        root.group(1),
    )
    return value.group(1) if value else None


def candidate_skeleton_inheritance_error(initiative: Path, candidate: Path, candidate_html: str) -> str | None:
    """Require v3 promotion inputs to retain their initiative-local skeleton.

    Legacy/v2 material remains on its documented lifecycle path.  A v3
    candidate, however, explicitly promises the immutable shell contract; the
    renderer is its delivery boundary and must verify that promise for normal
    and autonomous-recovery promotion alike.
    """
    if root_attribute(candidate_html, "data-brief-shell-contract") != "v1":
        return None
    skeleton = initiative / "brief-candidates" / "stakeholder-brief.skeleton.html"
    if not skeleton.is_file():
        return "v3 candidate requires initiative-local brief-candidates/stakeholder-brief.skeleton.html"
    findings = candidate_inheritance_errors(candidate, skeleton, initiative)
    if findings:
        return "candidate does not retain the initiative-local skeleton: " + "; ".join(findings)
    return None


def pre_render_review_error(
    initiative: Path, state: str, candidate_html: str, candidate_digest: str
) -> str | None:
    """Require a distinct, source-backed review of this exact candidate.

    This validates review provenance and lifecycle identity, not narrative
    quality.  A distinct human remains responsible for deciding whether the
    composed prose and representations are sufficient for the initiative.
    """
    if scalar(state, "brief_lineage") != "v2":
        return 'run-state brief_lineage must be "v2"'
    author = brief_review_field(state, "author")
    state_reviewer = brief_review_field(state, "coverage_reviewer")
    record = brief_review_field(state, "review_record")
    findings = brief_review_field(state, "findings_status")
    reviewed_at = brief_review_field(state, "reviewed_at")
    if not author:
        return "brief_review.author is required for an exact pre-render review"
    if not record or not record.startswith("decision-log.md#"):
        return "brief_review.review_record must locate a decision-log.md record"
    try:
        outcome = brief_review_finding_outcome(state)
    except ValueError as error:
        return str(error)
    if outcome not in {None, "not_started", "pending", "pass"}:
        return "brief_review.findings_status must be pending/not_started or exactly pass for a pre-render review"
    decision_log = initiative / "decision-log.md"
    if not decision_log.is_file():
        return "decision-log.md is required for pre-render review"
    record_id = record.partition("#")[2]
    log = decision_log.read_text(encoding="utf-8")
    decision = review_record_content(log, record_id)
    if not decision:
        return "pre-render review record must resolve to an explicit decision-log.md heading"
    bound_digest = record_field(decision, "Candidate SHA-256", "candidate_sha256")
    if bound_digest != candidate_digest:
        return "resolved pre-render review record does not bind the exact candidate SHA-256"
    if record_field(decision, "Author") != author:
        return "resolved pre-render review record must name the state brief_review.author"
    reviewer = record_field(decision, "Reviewer", "Coverage reviewer")
    if not reviewer or reviewer == author:
        return "resolved pre-render review record requires a reviewer distinct from its author"
    if state_reviewer and state_reviewer != reviewer:
        return "resolved pre-render review record reviewer does not match state brief_review.coverage_reviewer"
    if state_reviewer and author == state_reviewer:
        return "brief_review author and coverage_reviewer must be distinct"
    # Legacy states may mirror a completed review.  The mirror is optional in
    # the signed-pending contract, but cannot contradict the signed record.
    if reviewed_at and outcome != "pass":
        return "brief_review.reviewed_at requires findings_status: pass"
    # This is an authoring contract for the composition decision record, not
    # the lifecycle enum used by brief_review.findings_status.  A record can
    # authorize promotion only with its one canonical literal.
    if not record_exact_literal(decision, "approve", "Review outcome", "Coverage review outcome"):
        return "resolved pre-render review record must record Review outcome: approve exactly"
    if record_field(decision, "Composition provenance") != "verified":
        return "resolved pre-render review record must attest Composition provenance: verified"
    if record_field(decision, "Human attestation") != "confirmed":
        return "resolved pre-render review record must contain Human attestation: confirmed"
    manifest = canonical_composition_manifest(initiative)
    if record_field(decision, "Composition manifest SHA-256") != manifest:
        return "resolved pre-render review record does not bind the current canonical composition manifest"
    if root_attribute(candidate_html, "data-harness-template-kind") != "composed":
        return "candidate must declare data-harness-template-kind=\"composed\"; scaffold identity cannot be promoted"
    if root_attribute(candidate_html, "data-composition-review-record") != record_id:
        return "candidate must bind data-composition-review-record to the resolved decision record"
    provenance = root_attribute(candidate_html, "data-composition-provenance")
    if provenance not in {"pending", "reviewed"}:
        return "candidate must declare data-composition-provenance=\"pending\" or \"reviewed\""
    block_error = provenance_error(initiative, candidate_html, decision)
    if block_error:
        return block_error
    topology_error = scaffold_topology_error(candidate_html)
    if topology_error:
        return topology_error
    return None


def unapproved_render_error(initiative: Path, candidate_html: str, state: str) -> tuple[str | None, str]:
    """Validate the non-approval facts needed to make a final review surface.

    This path is deliberately narrower than ``pre_render_review_error``: it
    does not accept a review *outcome* as a substitute for evidence, but it
    allows a pending or revise record to yield an explicitly unapproved final
    page. It never synthesizes or repairs editorial content.
    """
    if root_attribute(candidate_html, "data-harness-template-kind") != "composed":
        return 'candidate must declare data-harness-template-kind="composed"', ""
    if root_attribute(candidate_html, "data-composition-provenance") not in {"pending", "reviewed"}:
        return 'candidate must declare data-composition-provenance="pending" or "reviewed"', ""
    record_id = root_attribute(candidate_html, "data-composition-review-record")
    if not record_id:
        return "candidate must bind data-composition-review-record for unapproved rendering", ""
    state_record = brief_review_field(state, "review_record")
    if state_record != f"decision-log.md#{record_id}":
        return "unapproved rendering requires brief_review.review_record to match the candidate composition record", ""
    try:
        outcome = brief_review_finding_outcome(state)
    except ValueError as error:
        return str(error), ""
    if outcome not in {"pending", "revise"}:
        return "unapproved rendering requires brief_review.findings_status: pending or revise", ""
    decision_log = initiative / "decision-log.md"
    if not decision_log.is_file():
        return "decision-log.md is required for unapproved rendering", ""
    decision = review_record_content(decision_log.read_text(encoding="utf-8"), record_id)
    if not decision:
        return "candidate data-composition-review-record must resolve to a decision-log.md heading", ""
    if outcome == "revise":
        if not record_exact_literal(decision, "revise", "Review outcome", "Coverage review outcome"):
            return "a revise state requires its bound composition record to state Review outcome: revise exactly", ""
        if not record_field(decision, "Recovery action", "Canonical recovery"):
            return "a revise composition record requires a Recovery action", ""
    try:
        canonical_composition_manifest(initiative)
    except ValueError as error:
        return str(error), ""
    topology_error = scaffold_topology_error(candidate_html)
    if topology_error:
        return topology_error, ""
    provenance = provenance_error(initiative, candidate_html, decision)
    if provenance:
        return provenance, ""
    return None, decision


def with_unapproved_lifecycle_surface(candidate_html: str) -> str:
    """Attach only closed lifecycle markers to a composed candidate if absent.

    The markers are operational state, not source-derived narrative. A
    candidate that declares *some* lifecycle surface must own the complete
    surface itself; silently extending a partial declaration would hide an
    authoring mistake.
    """
    if "data-lifecycle-marker" in candidate_html:
        return candidate_html
    root = re.search(r"(?is)<html\b([^>]*)>", candidate_html)
    if not root or not re.search(r"\bdata-brief-phase\s*=", root.group(1)):
        raise ValueError("candidate must have an <html> root with data-brief-phase before unapproved rendering")
    if not re.search(r"(?is)<head\b[^>]*>", candidate_html) or not re.search(r"(?is)</body\s*>", candidate_html):
        raise ValueError("candidate must contain <head> and </body> before unapproved rendering")
    root_open = root.group(0)
    marked_root = root_open[:-1] + (
        ' data-lifecycle-marker="brief-phase" data-lifecycle-source="run-state.yaml"'
        ' data-lifecycle-fragment="brief_phase">'
    )
    marked = candidate_html[:root.start()] + marked_root + candidate_html[root.end():]
    marked = re.sub(
        r"(?is)(<head\b[^>]*>)",
        r'\1<meta data-lifecycle-marker="rendered-state-digest" '
        r'data-lifecycle-source="run-state.yaml" data-lifecycle-fragment="rendered run-state bytes" '
        r'content="candidate">',
        marked,
        count=1,
    )
    lifecycle_note = (
        '<p class="brief-lifecycle-state" role="status" '
        'data-lifecycle-marker="rendered-authority" '
        'data-lifecycle-source="run-state.yaml" '
        'data-lifecycle-projection="lifecycle-authority" '
        'data-lifecycle-fragment="brief lifecycle authority">candidate</p>'
        '<p class="brief-lifecycle-state" role="status" '
        'data-lifecycle-marker="rendered-next-safe-step" '
        'data-lifecycle-source="run-state.yaml" '
        'data-lifecycle-projection="lifecycle-next-safe-step" '
        'data-lifecycle-fragment="brief lifecycle next safe step">candidate</p>'
        '<p class="brief-lifecycle-state" role="status" '
        'data-lifecycle-marker="rendered-review-status" '
        'data-lifecycle-source="run-state.yaml" '
        'data-lifecycle-projection="lifecycle-review-status" '
        'data-lifecycle-fragment="brief lifecycle review status">candidate</p>'
    )
    return re.sub(r"(?is)</body\s*>", lifecycle_note + "</body>", marked, count=1)


def _unquote_markdown_code(value: str | None) -> str | None:
    """Compare an identity written in a Markdown field without normalizing it."""
    if value is None:
        return None
    return value[1:-1] if len(value) >= 2 and value.startswith("`") and value.endswith("`") else value


def _exact_brief_review_literal(state: str, key: str, literal: str) -> bool:
    """Require one YAML scalar whose content is exactly the closed literal."""
    match = re.search(r"(?ms)^brief_review:\s*\n(?P<body>(?:^[ \t]+.*\n?)*)", state)
    if not match:
        return False
    field = re.search(rf"(?m)^\s+{re.escape(key)}: (?P<value>.*)$", match.group("body"))
    if not field:
        return False
    value = field.group("value")
    # Ordinary YAML quote delimiters do not change scalar content. Nested
    # quoting, whitespace and aliases do: they are not an authorization.
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value == literal


def _reviewed_rendered_digest(inputs: str | None) -> str | None:
    if not inputs:
        return None
    match = re.search(
        r"(?:^|;\s*)rendered=stakeholder-brief\.html@sha256:([0-9a-fA-F]{64})(?=;|$)",
        inputs,
    )
    return match.group(1).lower() if match else None


def post_render_review_error(
    initiative: Path, state: str, rendered_html: str, *, require_current_html: bool = True,
) -> str | None:
    """Validate the minimum, exact linkage needed to record post-render review.

    The evidence remains a human judgment.  This only verifies that the state,
    evidence record and immutable HTML which was reviewed identify the same
    concrete artifact.  It deliberately does not prescribe a persona, count,
    transport, score or delivery decision.
    """
    if scalar(state, "brief_phase") != "rendered":
        return 'run-state brief_phase must be "rendered" for post-render review finalization'
    allowed_phases = (
        {"rendered_decision_review_pending", "rendered_autonomous_review_pending"}
        if require_current_html else {"rendered_decision_review_recorded"}
    )
    if scalar(state, "current_phase") not in allowed_phases:
        expected = " or ".join(f'"{phase}"' for phase in sorted(allowed_phases))
        return f"run-state current_phase must be {expected} for post-render review finalization"
    if not _exact_brief_review_literal(state, "quality_review_required", "true"):
        return "brief_review.quality_review_required must be exactly true for post-render review finalization"
    if not _exact_brief_review_literal(state, "quality_review_status", "approve"):
        return "brief_review.quality_review_status must be exactly approve for post-render review finalization"
    author = brief_review_field(state, "author")
    reviewer = brief_review_field(state, "quality_review_reviewer")
    record = brief_review_field(state, "quality_review_record")
    reviewed_digest = _reviewed_rendered_digest(brief_review_field(state, "quality_review_inputs"))
    if not reviewer:
        return "brief_review.quality_review_reviewer is required for post-render review finalization"
    if author and reviewer == author:
        return "brief_review.quality_review_reviewer must be distinct from brief_review.author"
    if not record:
        return "brief_review.quality_review_record is required for post-render review finalization"
    evidence_root = (initiative / "evidence").resolve()
    evidence_path = (initiative / record).resolve()
    try:
        contained = evidence_path.is_relative_to(evidence_root)
    except AttributeError:
        contained = str(evidence_path).startswith(str(evidence_root))
    if not contained or not evidence_path.is_file():
        return "brief_review.quality_review_record must resolve to an existing file inside evidence/"
    if not reviewed_digest:
        return "brief_review.quality_review_inputs must bind stakeholder-brief.html to a SHA-256 digest"
    actual_digest = hashlib.sha256(rendered_html.encode("utf-8")).hexdigest()
    if require_current_html and reviewed_digest != actual_digest:
        return "brief_review.quality_review_inputs does not bind the exact pre-finalization stakeholder-brief.html"
    evidence = evidence_path.read_text(encoding="utf-8")
    if _unquote_markdown_code(record_field(evidence, "Reviewer")) != reviewer:
        return "post-render review evidence reviewer does not match brief_review.quality_review_reviewer"
    if _unquote_markdown_code(record_field(evidence, "Outcome", "Review outcome")) != "approve":
        return "post-render review evidence must contain Outcome: approve exactly"
    if _unquote_markdown_code(record_field(evidence, "Reviewed rendered artifact")) != "stakeholder-brief.html":
        return "post-render review evidence must identify stakeholder-brief.html exactly"
    if _unquote_markdown_code(record_field(evidence, "Rendered HTML SHA-256")) != reviewed_digest:
        return "post-render review evidence does not bind the stakeholder-brief.html recorded in brief_review.quality_review_inputs"
    preview_url = _unquote_markdown_code(record_field(evidence, "Preview URL")) or ""
    if not re.fullmatch(r"http://127\.0\.0\.1(?::\d{1,5})?(?:/[^\s]*)?", preview_url):
        return "post-render review evidence must contain Preview URL: http://127.0.0.1[:port]/... exactly"
    if not (_unquote_markdown_code(record_field(evidence, "Preview environment")) or ""):
        return "post-render review evidence must contain a non-empty Preview environment"
    return None


def canonical_composition_manifest(initiative: Path) -> str:
    """Return the stable digest of the canonical composition input set.

    The review record binds this one manifest, rather than turning every
    narrative artifact in an initiative into a promotion participant.  The
    manifest is a pre-render check only; promotion still commits exactly the
    rendered HTML and run-state pair.
    """
    entries = []
    for source in CANONICAL_COMPOSITION_SOURCES:
        path = initiative / source
        if not path.is_file():
            raise ValueError(f"canonical composition source is missing: {source}")
        entries.append({"path": source, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    return hashlib.sha256(
        json.dumps(entries, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def lifecycle_error(
    candidate_html: str, state: str | None = None, initiative: Path | None = None,
    *, allow_rendered_state_snapshot: bool = False,
) -> str | None:
    """Validate opt-in markers against the computed lifecycle projection."""
    seen: dict[str, int] = {}
    parser = LifecycleParser()
    parser.feed(candidate_html)
    parser.close()
    if parser.error:
        return parser.error
    for index, (tag, attrs, ancestors) in enumerate(parser.markers):
        values = {name.lower(): value or "" for name, value in attrs}
        marker_id = values["data-lifecycle-marker"]
        spec = LIFECYCLE_MARKERS.get(marker_id)
        if not spec:
            return f"unknown lifecycle marker: {marker_id}"
        seen[marker_id] = seen.get(marker_id, 0) + 1
        if "tag" in spec and tag.lower() != spec["tag"]:
            return f"lifecycle marker {marker_id} is misplaced: expected <{spec['tag']}>"
        if marker_id == "brief-phase" and ancestors:
            return "lifecycle marker brief-phase is misplaced: expected document root"
        if marker_id == "rendered-state-digest" and ancestors[-1:] != ("head",):
            return "lifecycle marker rendered-state-digest is misplaced: expected <head>"
        if marker_id in {"rendered-authority", "rendered-next-safe-step", "rendered-review-status"}:
            if "body" not in ancestors:
                return f"lifecycle marker {marker_id} is misplaced: expected <body>"
            if parser.marker_in_coverage_register[index]:
                return f"lifecycle marker {marker_id} is forbidden inside #coverage-register"
            if parser.marker_has_nested_content[index] or not parser.marker_text[index].strip():
                if marker_id == "rendered-authority":
                    return "lifecycle marker rendered-authority must contain non-empty raw direct authority text only"
                return f"lifecycle marker {marker_id} must contain non-empty raw direct lifecycle text only"
            if state is not None:
                try:
                    projection = {
                        "rendered-authority": AUTHORITY_PROJECTION,
                        "rendered-next-safe-step": "lifecycle-next-safe-step",
                        "rendered-review-status": "lifecycle-review-status",
                    }[marker_id]
                    expected_text = lifecycle_projection(
                        projection, state, initiative, candidate_html
                    )
                except ValueError as error:
                    return str(error)
                if (parser.marker_text[index].strip() != expected_text
                        and not immutable_candidate_pending_projection(
                            parser.marker_text[index].strip(), expected_text, state,
                        )):
                    if marker_id == "rendered-authority":
                        return "lifecycle marker rendered-authority text does not bind the computed lifecycle authority projection"
                    return f"lifecycle marker {marker_id} text does not bind its computed lifecycle projection"
        allowed = {"data-lifecycle-marker", "data-lifecycle-source", "data-lifecycle-fragment"}
        if marker_id in {"rendered-authority", "rendered-next-safe-step", "rendered-review-status"}:
            allowed.add("data-lifecycle-projection")
        if spec["attribute"] != "text":
            allowed.add(spec["attribute"])
        if any(name.startswith("data-lifecycle-") and name not in allowed for name in values):
            return f"lifecycle marker {marker_id} has undeclared lifecycle attribute"
        for name, expected in (("data-lifecycle-source", spec["source"]),):
            if values.get(name) != expected:
                return f"lifecycle marker {marker_id} has undeclared {name} binding"
        if marker_id == "rendered-state-source-digest" and values.get("data-source") != "run-state.yaml":
            return "lifecycle marker rendered-state-source-digest must bind data-source=run-state.yaml"
        if marker_id in {"rendered-authority", "rendered-next-safe-step", "rendered-review-status"}:
            if not values.get("data-lifecycle-fragment", "").strip():
                return f"lifecycle marker {marker_id} requires a non-empty provenance fragment"
            expected_projection = {
                "rendered-authority": AUTHORITY_PROJECTION,
                "rendered-next-safe-step": "lifecycle-next-safe-step",
                "rendered-review-status": "lifecycle-review-status",
            }[marker_id]
            if values.get("data-lifecycle-projection") != expected_projection:
                return f"lifecycle marker {marker_id} must bind its computed lifecycle projection"
        elif marker_id != "rendered-state-source-digest" and values.get("data-lifecycle-fragment") != spec["fragment"]:
            return f"lifecycle marker {marker_id} has undeclared data-lifecycle-fragment binding"
        elif marker_id == "rendered-state-source-digest" and not values.get("data-lifecycle-fragment", "").strip():
            return "lifecycle marker rendered-state-source-digest requires a non-empty provenance fragment"
        if spec["attribute"] != "text":
            if spec["attribute"] not in values:
                return f"lifecycle marker {marker_id} lacks {spec['attribute']}"
        if state is not None and marker_id == "brief-phase":
            expected_phase = scalar(state, "brief_phase")
            # ``ready_to_render`` is an authored source checkpoint, not a
            # rendered HTML phase.  The candidate remains explicitly authored
            # until the pair promotion commits ``rendered``.
            if expected_phase == "ready_to_render":
                expected_phase = "authored"
            if values.get("data-brief-phase") != expected_phase:
                return "lifecycle marker brief-phase does not bind the current run-state brief_phase"
        if (state is not None and marker_id == "rendered-state-digest"
                and scalar(state, "brief_phase") in {"rendered", "reviewed", "approved"}
                and not allow_rendered_state_snapshot):
            expected_digest = hashlib.sha256(state.encode("utf-8")).hexdigest()
            if values.get("content") != expected_digest:
                return "lifecycle marker rendered-state-digest does not bind the current run-state bytes"
    for marker_id in LIFECYCLE_MARKERS:
        count = seen.get(marker_id, 0)
        if marker_id == "rendered-authority":
            if count < 1:
                return f"lifecycle marker {marker_id} must appear at least once"
            continue
        if marker_id in {"rendered-state-source-digest", "rendered-next-safe-step", "rendered-review-status"}:
            continue
        if count != 1:
            return f"lifecycle marker {marker_id} must appear exactly once (found {count})"
    return None


def render_lifecycle(
    candidate_html: str, rendered_state: str, *, preserve_rendered_state_digest: bool = False,
) -> str:
    """Replace only declared attribute values or the declared marker's text."""
    error = lifecycle_error(candidate_html)
    if error:
        raise ValueError(error)

    def replace_opening_tag(match: re.Match[str]) -> str:
        tag, attributes = match.groups()
        marker_match = re.search(r'\bdata-lifecycle-marker\s*=\s*["\']([^"\']+)["\']', attributes)
        if not marker_match:
            return match.group(0)
        if preserve_rendered_state_digest and marker_match.group(1) == "rendered-state-digest":
            return match.group(0)
        spec = LIFECYCLE_MARKERS[marker_match.group(1)]
        if spec["attribute"] == "text":
            return match.group(0)
        value = spec["value"](rendered_state)
        rewritten = re.sub(
            rf'(\b{re.escape(spec["attribute"])}\s*=\s*["\'])[^"\']*(["\'])',
            rf"\g<1>{value}\g<2>", attributes, count=1,
        )
        return f"<{tag}{rewritten}>"

    # Lifecycle tags are intentionally constrained to non-nested, explicit
    # tags.  This makes the byte-diff surface auditable and keeps arbitrary
    # authored content outside the transformer.
    rendered = re.sub(r"(?is)<([a-z0-9]+)\b([^>]*)>", replace_opening_tag, candidate_html)

    def replace_projection_text(match: re.Match[str]) -> str:
        tag, attributes, _body, closing = match.groups()
        marker = re.search(r'\bdata-lifecycle-marker\s*=\s*["\']([^"\']+)["\']', attributes)
        if not marker or marker.group(1) not in {"rendered-authority", "rendered-next-safe-step", "rendered-review-status"}:
            return match.group(0)
        projection = {
            "rendered-authority": AUTHORITY_PROJECTION,
            "rendered-next-safe-step": "lifecycle-next-safe-step",
            "rendered-review-status": "lifecycle-review-status",
        }[marker.group(1)]
        return f"<{tag}{attributes}>{lifecycle_projection(projection, rendered_state)}{closing}"

    # Authority declarations are validated as non-nested, direct-text
    # elements before this byte-limited replacement.
    rendered = re.sub(r"(?is)<([a-z0-9]+)\b([^>]*)>([^<]*)(</\1\s*>)", replace_projection_text, rendered)
    return rendered


def source_lifecycle_error(
    source_path: Path, content: str, state: str | None = None, authority: str | None = None,
    initiative: Path | None = None, candidate_html: str | None = None,
) -> str | None:
    """Validate explicit source authority spans without interpreting prose.

    A source marker has no identifier or layout convention: its path, its
    declared run-state binding, and a non-empty provenance fragment are the
    complete contract.  Repetition is intentional (several independent
    lifecycle claims may exist in one document); malformed, unknown, nested,
    or non-direct declarations are refused before any transaction begins.
    """
    token = "sdd-lifecycle-"
    if token not in content:
        return None
    spans = list(SOURCE_AUTHORITY_RE.finditer(content))
    yaml_spans = list(SOURCE_AUTHORITY_YAML_RE.finditer(content))
    # A token not consumed by the closed grammar includes unknown/open-only,
    # close-only, malformed attributes and nested declarations.
    residue = SOURCE_AUTHORITY_YAML_RE.sub("", SOURCE_AUTHORITY_RE.sub("", content))
    if token in residue or SOURCE_AUTHORITY_CLOSE in residue:
        return f"source lifecycle declaration is malformed or unknown: {source_path.name}"
    for span in [*spans, *yaml_spans]:
        if span.group("source") != "run-state.yaml":
            return f"source lifecycle declaration must bind source=run-state.yaml: {source_path.name}"
        if span.group("projection") not in {AUTHORITY_PROJECTION, "lifecycle-next-safe-step"}:
            return f"source lifecycle declaration has an unknown projection: {source_path.name}"
        if not span.group("fragment").strip():
            return f"source lifecycle declaration requires a non-empty provenance fragment: {source_path.name}"
        text = span.group("text")
        if not text.strip() or "<" in text or ">" in text:
            return f"source lifecycle declaration must contain non-empty raw direct text only: {source_path.name}"
        if authority is not None:
            # ``authority`` is retained for the original single-projection
            # caller; mixed declarations derive their own closed projection.
            expected = authority if span.group("projection") == AUTHORITY_PROJECTION else lifecycle_projection(
                span.group("projection"), state or "", initiative, candidate_html,
            )
            if (text.strip() != expected
                    and not immutable_candidate_pending_projection(text.strip(), expected, state)):
                return f"source lifecycle declaration text does not bind the computed lifecycle authority projection: {source_path.name}"
        elif state is not None:
            try:
                authority = lifecycle_projection(
                    span.group("projection"), state, initiative, candidate_html,
                )
            except ValueError as error:
                return str(error)
            if (text.strip() != authority
                    and not immutable_candidate_pending_projection(text.strip(), authority, state)):
                return f"source lifecycle declaration text does not bind the computed lifecycle authority projection: {source_path.name}"
    return None


def rendered_source_lifecycle_content(
    source_path: Path, content: str, rendered_state: str,
    initiative: Path | None = None, candidate_html: str | None = None,
) -> str:
    """Stage only declared lifecycle authority text in one canonical source."""
    error = source_lifecycle_error(
        source_path, content, initiative=initiative, candidate_html=candidate_html,
    )
    if error:
        raise ValueError(error)
    def replacement(match: re.Match[str]) -> str:
        return match.group(0).replace(
            match.group("text"), lifecycle_projection(
                match.group("projection"), rendered_state, initiative, candidate_html,
            ), 1,
        )
    return SOURCE_AUTHORITY_YAML_RE.sub(replacement, SOURCE_AUTHORITY_RE.sub(replacement, content))


def declared_source_lifecycle_updates(
    initiative: Path, state: str, rendered_state: str, candidate_html: str | None = None
) -> dict[Path, str]:
    """Discover opt-in source spans under the initiative, excluding evidence.

    Evidence is immutable testimony, not active canonical state.  All other
    text sources are discovered structurally, so this makes no assumptions
    about a SPEC's file names or Markdown heading layout.
    """
    updates: dict[Path, str] = {}
    pre_render_authority = lifecycle_authority_projection(state, initiative, candidate_html)
    for path in initiative.rglob("*"):
        if (
            not path.is_file()
            or path.is_symlink()
            # run-state is the separately staged lifecycle authority; letting
            # it re-enter through opt-in source discovery would create two
            # competing transaction representations for the same file.
            or path.resolve() == (initiative / "run-state.yaml").resolve()
            or _recovery_path_error(path, initiative, "source artifact")
            or "evidence" in path.relative_to(initiative).parts
            or path.name.endswith(".tmp")
            or path.name.endswith(".promotion-backup")
            or path.name.endswith(".promotion-journal.json")
        ):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "sdd-lifecycle-" not in content:
            continue
        if error := source_lifecycle_error(
            path, content, state, pre_render_authority, initiative, candidate_html,
        ):
            raise ValueError(error)
        updated = rendered_source_lifecycle_content(
            path, content, rendered_state, initiative, candidate_html,
        )
        if updated != content:
            updates[path] = updated
    return updates


def _write_durable(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())


def _digest_path(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def _fault(point: str, requested: str | None) -> None:
    if requested == point:
        raise RuntimeError(f"injected failure at {point}")


def _promotion_paths(target: Path, state_path: Path) -> dict[str, Path]:
    return {
        "journal": target.with_name(f".{target.name}.promotion-journal.json"),
        "target_backup": target.with_name(f".{target.name}.promotion-backup"),
        "state_backup": state_path.with_name(f".{state_path.name}.promotion-backup"),
    }


def _relative_artifact_path(path: Path, root: Path) -> str:
    """Return the one normalized, root-contained spelling used in journals."""
    return path.resolve().relative_to(root.resolve()).as_posix()


def _recovery_path_error(path: Path, root: Path, kind: str) -> str | None:
    """Refuse links and resolved paths outside the initiative before mutation.

    Journals are crash-recovery input, not authority to follow filesystem
    indirections.  This check deliberately applies to generated staging files
    too: an attacker can pre-create one as a symlink before recovery runs.
    """
    if path.is_symlink():
        return f"source promotion {kind} is a symlink; manual recovery required"
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return f"source promotion {kind} escapes initiative root; manual recovery required"
    return None


def _is_sha256(value: object, *, allow_none: bool = False) -> bool:
    return (allow_none and value is None) or (
        isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None
    )


def _declared_source_paths(root: Path) -> set[Path]:
    """Discover canonical lifecycle sources without naming a SPEC layout."""
    paths: set[Path] = set()
    for path in root.rglob("*"):
        if (not path.is_file() or path.is_symlink()
                # run-state is the separately staged transaction member, not
                # a discovered auxiliary source update. Keeping this mirror
                # of declared_source_lifecycle_updates prevents the final
                # bundle-set check from treating it as a duplicate member.
                or path.resolve() == (root / "run-state.yaml").resolve()
                or _recovery_path_error(path, root, "source artifact")
                or "evidence" in path.relative_to(root).parts
                or path.name.endswith(".tmp")
                or path.name.endswith(".promotion-backup")
                or path.name.endswith(".promotion-journal.json")):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "sdd-lifecycle-" in content:
            # A malformed declaration is never a valid transaction member.
            if source_lifecycle_error(path, content) is None:
                paths.add(path.resolve())
    return paths


def _validated_bundle_journal(target: Path, state_path: Path, journal: object) -> tuple[list[tuple[Path, dict[str, object]]], str | None]:
    """Validate every recovery input before touching a single artifact.

    The journal is deliberately capability-limited: it can name the delivered
    HTML, run-state, and source files that *currently* carry an opt-in
    lifecycle declaration.  It cannot turn recovery into a generic file mover.
    """
    root = target.parent.resolve()
    for path, kind in ((target, "target artifact"), (state_path, "state artifact")):
        if error := _recovery_path_error(path, root, kind):
            return [], error
    if not isinstance(journal, dict) or journal.get("schema_version") != 2:
        return [], "unrecognized source promotion journal; manual recovery required"
    nonce = journal.get("nonce")
    artifacts = journal.get("artifacts")
    if not isinstance(nonce, str) or not re.fullmatch(r"[0-9a-f]{32}", nonce):
        return [], "source promotion journal has unsafe nonce; manual recovery required"
    if not isinstance(artifacts, list) or len(artifacts) < 2:
        return [], "unrecognized source promotion journal; manual recovery required"
    try:
        target_rel = _relative_artifact_path(target, root)
        state_rel = _relative_artifact_path(state_path, root)
    except ValueError:
        return [], "source promotion paths escape initiative root; manual recovery required"
    allowed_fixed = {target.resolve(), state_path.resolve()}
    resolved: list[tuple[Path, dict[str, object]]] = []
    seen: set[str] = set()
    for index, entry in enumerate(artifacts):
        if not isinstance(entry, dict) or set(entry) != {"path", "temp", "backup", "intended_sha256", "previous_existed", "previous_sha256"}:
            return [], "unrecognized source promotion journal; manual recovery required"
        relative = entry["path"]
        if not isinstance(relative, str) or not relative or "\\" in relative:
            return [], "unsafe source promotion path; manual recovery required"
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts or candidate.as_posix() != relative:
            return [], "unsafe source promotion path; manual recovery required"
        path = (root / candidate).resolve()
        if path == root:
            return [], "unsafe source promotion path; manual recovery required"
        if error := _recovery_path_error(root / candidate, root, "source artifact"):
            return [], error
        if relative in seen:
            return [], "source promotion journal contains duplicate artifact paths; manual recovery required"
        seen.add(relative)
        if not isinstance(entry["previous_existed"], bool) or not _is_sha256(entry["intended_sha256"]) or not _is_sha256(entry["previous_sha256"], allow_none=True):
            return [], "source promotion journal has invalid digest record; manual recovery required"
        if entry["previous_existed"] != (entry["previous_sha256"] is not None):
            return [], "source promotion journal has invalid predecessor record; manual recovery required"
        expected_temp = f".{path.name}.{nonce}.{index}.tmp"
        expected_backup = f".{path.name}.{nonce}.{index}.promotion-backup"
        if entry["temp"] != expected_temp or entry["backup"] != expected_backup:
            return [], "source promotion journal has unsafe temporary or backup path; manual recovery required"
        temp = path.with_name(expected_temp)
        backup = path.with_name(expected_backup)
        for representation, kind in ((temp, "temporary artifact"), (backup, "backup artifact")):
            if error := _recovery_path_error(representation, root, kind):
                return [], error
        # If a durable staging/backup artifact exists, its bytes must match the
        # record before recovery is allowed to make any change.
        if temp.exists() and _digest_path(temp) != entry["intended_sha256"]:
            return [], "source promotion journal temporary digest mismatch; manual recovery required"
        if backup.exists() and _digest_path(backup) != entry["previous_sha256"]:
            return [], "source promotion journal backup digest mismatch; manual recovery required"
        if path not in allowed_fixed:
            # A source remains canonical through every transaction phase: one
            # of its live, staged, or backed-up representations must carry the
            # same explicit declaration.  This avoids a filename allow-list
            # while refusing arbitrary journal-selected files.
            declared_here = False
            for representation in (path, temp, backup):
                if representation.is_file():
                    try:
                        body = representation.read_text(encoding="utf-8")
                    except UnicodeDecodeError:
                        continue
                    if "sdd-lifecycle-" in body and source_lifecycle_error(path, body) is None:
                        declared_here = True
                        break
            if not declared_here:
                return [], "source promotion journal names an undeclared source artifact; manual recovery required"
        resolved.append((path, entry))
    if {target_rel, state_rel} - seen:
        return [], "source promotion journal omits required lifecycle artifacts; manual recovery required"
    # Promotion closed this exact set before durable journaling. During
    # recovery members may be backups or staged representations, so live
    # discovery cannot safely redefine the set from mutable files.
    journal_sources = {path for path, _ in resolved} - allowed_fixed
    if not journal_sources:
        return [], "source promotion journal omits declared lifecycle source artifacts; manual recovery required"
    return resolved, None


def recover_promotion(target: Path, state_path: Path, fault_at: str | None = None) -> str | None:
    """Restore an interrupted pair, or finalize a pair whose intended bytes exist."""
    paths = _promotion_paths(target, state_path)
    journal_path = paths["journal"]
    root = target.parent.resolve()
    for path, kind in ((target, "target artifact"), (state_path, "state artifact"), (journal_path, "journal artifact")):
        if error := _recovery_path_error(path, root, kind):
            return error
    for key in ("target_backup", "state_backup"):
        if error := _recovery_path_error(paths[key], root, "backup artifact"):
            return error
    if not journal_path.exists():
        prefixes = (f".{target.name}.", f".{state_path.name}.")
        stale = [path for path in target.parent.iterdir() if path.is_file() and path.name.startswith(prefixes) and path.name.endswith(".tmp")]
        for temp in stale:
            if error := _recovery_path_error(temp, root, "temporary artifact"):
                return error
            nonce = temp.name.rsplit(".", 2)[-2]
            if not re.fullmatch(r"[0-9a-f]{32}", nonce):
                return f"unsafe pre-journal temporary artifact: {temp.name}; manual recovery required"
        for temp in stale:
            temp.unlink()
        return None
    try:
        journal = json.loads(journal_path.read_text(encoding="utf-8"))
        # Schema v2 journalled arbitrary source edits alongside the delivered
        # pair.  That recovery scope was deliberately removed: narrative
        # sources are not promotion members and a legacy journal is never
        # authority to move or delete them.
        if journal.get("schema_version") == 2:
            return "legacy multi-source promotion journal is not recoverable; manual recovery required"
        if journal.get("schema_version") != LIFECYCLE_SCHEMA_VERSION:
            return "unrecognized promotion journal schema; manual recovery required"
        intended = journal["intended"]
        temp_names = journal.get("temps", [])
        target_pattern = re.compile(rf"^\.{re.escape(target.name)}\.([0-9a-f]{{32}})\.tmp$")
        state_pattern = re.compile(rf"^\.{re.escape(state_path.name)}\.([0-9a-f]{{32}})\.tmp$")
        if not isinstance(temp_names, list) or len(temp_names) != 2 or len(set(temp_names)) != 2:
            return "promotion journal has unsafe temporary path; manual recovery required"
        target_temp = next((name for name in temp_names if isinstance(name, str) and target_pattern.fullmatch(name)), None)
        state_temp = next((name for name in temp_names if isinstance(name, str) and state_pattern.fullmatch(name)), None)
        if not target_temp or not state_temp or target_pattern.fullmatch(target_temp).group(1) != state_pattern.fullmatch(state_temp).group(1):
            return "promotion journal has unsafe temporary path; manual recovery required"
        for name in temp_names:
            if error := _recovery_path_error(target.parent / name, root, "temporary artifact"):
                return error
        complete = _digest_path(target) == intended["target_sha256"] and _digest_path(state_path) == intended["state_sha256"]
        if not complete:
            for key, live in (("target", target), ("state", state_path)):
                backup = paths[f"{key}_backup"]
                existed = journal["previous"][f"{key}_existed"]
                if existed:
                    if not backup.is_file():
                        if _digest_path(live) == journal["previous"].get(f"{key}_sha256"):
                            continue
                        return f"incomplete promotion lacks {key} backup; manual recovery required"
                    _fault(f"recovery_restore_{key}", fault_at)
                    os.replace(backup, live)
                elif live.exists():
                    _fault(f"recovery_restore_{key}", fault_at)
                    live.unlink()
        _fault("recovery_cleanup", fault_at)
        for path in paths.values():
            if path.exists():
                path.unlink()
        for name in temp_names:
            temp = target.parent / name
            if temp.exists():
                temp.unlink()
        return None
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, json.JSONDecodeError) as error:
        return f"cannot recover interrupted promotion: {error}"


def promote_pair(target: Path, state_path: Path, html: str, rendered_state: str, fault_at: str | None) -> None:
    """Commit the state first, then the HTML, while a durable journal guards both."""
    paths = _promotion_paths(target, state_path)
    nonce = uuid.uuid4().hex
    html_temp = target.with_name(f".{target.name}.{nonce}.tmp")
    state_temp = state_path.with_name(f".{state_path.name}.{nonce}.tmp")
    journal_created = False
    try:
        _write_durable(html_temp, html); _fault("temp_html", fault_at)
        _write_durable(state_temp, rendered_state); _fault("temp_state", fault_at)
        journal = {
            "schema_version": LIFECYCLE_SCHEMA_VERSION,
            "intended": {"target_sha256": _digest_path(html_temp), "state_sha256": _digest_path(state_temp)},
            "previous": {
                "target_existed": target.exists(), "state_existed": state_path.exists(),
                "target_sha256": _digest_path(target), "state_sha256": _digest_path(state_path),
            },
            "temps": [html_temp.name, state_temp.name],
        }
        _write_durable(paths["journal"], json.dumps(journal, sort_keys=True)); journal_created = True; _fault("journal", fault_at)
        if target.exists():
            os.replace(target, paths["target_backup"])
        _fault("backup_target", fault_at)
        if state_path.exists():
            os.replace(state_path, paths["state_backup"])
        _fault("backup_state", fault_at)
        os.replace(state_temp, state_path); _fault("rename_state", fault_at)
        os.replace(html_temp, target); _fault("rename_target", fault_at)
        _fault("cleanup", fault_at)
        for path in paths.values():
            if path.exists(): path.unlink()
    except Exception:
        # Keep journal/backups/temps for startup recovery; never paper over a
        # crash by presenting a target whose companion state is uncertain.
        if not journal_created:
            for temp in (html_temp, state_temp):
                if temp.exists():
                    temp.unlink()
        raise


def promote_bundle(target: Path, state_path: Path, html: str, rendered_state: str,
                   source_updates: dict[Path, str], fault_at: str | None = None) -> None:
    """Reject the retired multi-source promotion API.

    Kept only as an explicit failure for callers that still import the old
    helper.  The recoverable unit is exactly the rendered HTML plus
    ``run-state.yaml``; canonical sources are authored outside promotion.
    """
    if source_updates:
        raise ValueError("promotion only supports stakeholder-brief.html and run-state.yaml; source updates are not transaction members")
    promote_pair(target, state_path, html, rendered_state, fault_at)
    return

    """Unreachable legacy implementation retained below temporarily."""
    paths_and_content = [(target, html), (state_path, rendered_state), *source_updates.items()]
    if len({path.resolve() for path, _ in paths_and_content}) != len(paths_and_content):
        raise ValueError("source lifecycle transaction contains duplicate artifact paths")
    root = target.parent.resolve()
    if state_path.resolve().parent != root:
        raise ValueError("source lifecycle transaction artifacts must share the initiative root")
    for path, kind in ((target, "target artifact"), (state_path, "state artifact")):
        if error := _recovery_path_error(path, root, kind):
            raise ValueError(error)
    declared = _declared_source_paths(root)
    requested_sources = {path.resolve() for path in source_updates}
    for path in source_updates:
        if error := _recovery_path_error(path, root, "source artifact"):
            raise ValueError(error)
    if not requested_sources <= declared:
        raise ValueError("source lifecycle transaction contains undeclared or non-canonical source artifacts")
    if requested_sources != _declared_source_paths(root):
        raise ValueError("source lifecycle transaction must include every declared lifecycle source update")
    if any("evidence" in path.relative_to(root).parts for path in requested_sources):
        raise ValueError("source lifecycle transaction cannot modify evidence")
    journal_path = _promotion_paths(target, state_path)["journal"]
    if error := _recovery_path_error(journal_path, root, "journal artifact"):
        raise ValueError(error)
    nonce = uuid.uuid4().hex
    artifacts: list[dict[str, object]] = []
    journal_created = False
    try:
        for index, (path, content) in enumerate(paths_and_content):
            temp = path.with_name(f".{path.name}.{nonce}.{index}.tmp")
            backup = path.with_name(f".{path.name}.{nonce}.{index}.promotion-backup")
            for representation, kind in ((temp, "temporary artifact"), (backup, "backup artifact")):
                if error := _recovery_path_error(representation, root, kind):
                    raise ValueError(error)
            _write_durable(temp, content)
            artifacts.append({
                "path": _relative_artifact_path(path, root),
                "temp": temp.name,
                "backup": backup.name,
                "intended_sha256": _digest_path(temp),
                "previous_existed": path.exists(),
                "previous_sha256": _digest_path(path),
            })
            if index == 0:
                _fault("temp_html", fault_at)
        _fault("temp_state", fault_at)
        _write_durable(journal_path, json.dumps({"schema_version": 2, "nonce": nonce, "artifacts": artifacts}, sort_keys=True))
        journal_created = True; _fault("journal", fault_at)
        for index, (path, _) in enumerate(paths_and_content):
            if path.exists(): os.replace(path, path.with_name(f".{path.name}.{nonce}.{index}.promotion-backup"))
            if path == target:
                _fault("backup_target", fault_at)
        _fault("backup_state", fault_at)
        # State first retains the historical pair ordering; source records and
        # target become visible only while the journal makes recovery mandatory.
        ordered = [(state_path, rendered_state), *source_updates.items(), (target, html)]
        for path, _ in ordered:
            entry = next(item for item in artifacts if item["path"] == _relative_artifact_path(path, root))
            os.replace(path.with_name(str(entry["temp"])), path)
            if path == state_path:
                _fault("rename_state", fault_at)
        _fault("rename_target", fault_at)
        _fault("cleanup", fault_at)
        for entry, (path, _) in zip(artifacts, paths_and_content):
            path.with_name(str(entry["backup"])).unlink(missing_ok=True)
        journal_path.unlink(missing_ok=True)
    except Exception:
        if not journal_created:
            for artifact, (path, _) in zip(artifacts, paths_and_content):
                path.with_name(str(artifact["temp"])).unlink(missing_ok=True)
        raise


def finalize_post_render_review(
    initiative: Path, target: Path, state_path: Path, *, fault_at: str | None = None,
) -> tuple[str, str]:
    """Atomically record a valid rendered review without making a delivery decision.

    The already-rendered page is the review input, retained by its SHA-256 in
    evidence/state. Its lifecycle metadata and run-state provenance then move
    together to the final state in the same recoverable pair.
    """
    state = state_path.read_text(encoding="utf-8")
    rendered_html = target.read_text(encoding="utf-8")
    recorded = scalar(state, "current_phase") == "rendered_decision_review_recorded"
    marker_error = lifecycle_error(
        # The rendered review metadata is written after the original render,
        # so the input page's state digest may legitimately predate it. The
        # exact reviewed page is bound independently below; the final pair is
        # always checked strictly against the final state before promotion.
        rendered_html, state, initiative, allow_rendered_state_snapshot=True,
    )
    if marker_error:
        raise ValueError(marker_error)
    review_error = post_render_review_error(
        initiative, state, rendered_html, require_current_html=not recorded,
    )
    if review_error:
        raise ValueError(review_error)
    final_state = state if recorded else post_review_recorded_lifecycle_state(state)
    manifest = final_source_manifest(initiative, final_state, {})
    final_html = render_provenance_digests(
        render_provenance_fragments(
            render_lifecycle(rendered_html, final_state),
            initiative,
            manifest,
        ),
        manifest,
    )
    record_id = (brief_review_field(state, "review_record") or "").partition("#")[2]
    decision = review_record_content(
        (initiative / "decision-log.md").read_text(encoding="utf-8"), record_id,
    ) or ""
    provenance = provenance_error(initiative, final_html, decision, manifest)
    if provenance:
        raise ValueError(f"finalized rendered provenance does not bind final source manifest: {provenance}")
    marker_error = lifecycle_error(final_html, final_state, initiative)
    if marker_error:
        raise ValueError(marker_error)
    promote_pair(target, state_path, final_html, final_state, fault_at)
    return final_html, final_state


def main() -> int:
    args = parse_args()
    initiative = args.initiative.resolve()
    target = initiative / "stakeholder-brief.html"
    state_path = initiative / "run-state.yaml"
    if not initiative.is_dir() or not state_path.is_file():
        return fail("initiative directory with run-state.yaml is required")
    recovery_error = recover_promotion(target, state_path, args.fault_at)
    if recovery_error:
        return fail(recovery_error)
    if args.finalize_post_review:
        if args.candidate is not None or args.render_unapproved:
            return fail("--finalize-post-review does not accept --candidate or --render-unapproved")
        if not target.is_file():
            return fail("stakeholder-brief.html must exist before recording post-render review")
        try:
            finalize_post_render_review(initiative, target, state_path, fault_at=args.fault_at)
        except (OSError, ValueError, RuntimeError) as error:
            return fail(f"post-render review finalization interrupted; rerun to recover before another finalization: {error}")
        print(f"Recorded independent post-render review: {target}")
        print("Human Visibility, Tasks Ready and delivery remain separate decisions.")
        return 0
    if args.candidate is None:
        return fail("--candidate is required unless --finalize-post-review is used")
    candidate = args.candidate.resolve()
    if not candidate.is_file():
        return fail(f"candidate does not exist: {candidate}")
    if candidate == target.resolve():
        return fail("candidate must not be the delivered stakeholder-brief.html path")
    if target.exists() and not args.refresh:
        return fail("stakeholder-brief.html already exists; historical artifacts require --refresh and a newly reviewed replacement")
    state = state_path.read_text(encoding="utf-8")
    candidate_html = candidate.read_text(encoding="utf-8")
    inheritance_error = candidate_skeleton_inheritance_error(initiative, candidate, candidate_html)
    if inheritance_error:
        return fail(inheritance_error)
    if args.render_unapproved:
        try:
            candidate_html = with_unapproved_lifecycle_surface(candidate_html)
            rendered_state = rendered_unapproved_lifecycle_state(state)
        except ValueError as error:
            return fail(str(error))
        marker_error = lifecycle_error(candidate_html)
        if marker_error:
            return fail(marker_error)
        unapproved_error, decision_record = unapproved_render_error(initiative, candidate_html, state)
        if unapproved_error:
            return fail(unapproved_error)
    else:
        try:
            # A ready pre-render lifecycle projection is candidate-bound. Pass
            # that same context into the source-first state transition so declared
            # source next-step fields cannot lose their exact review linkage.
            rendered_state = rendered_lifecycle_state(state, initiative, candidate_html)
        except ValueError as error:
            return fail(str(error))
        if scalar(state, "brief_coverage_ready") != "true":
            return fail("coverage review must be ready before rendering")
        marker_error = lifecycle_error(candidate_html, state, initiative)
        if marker_error:
            return fail(marker_error)
        review_error = pre_render_review_error(
            initiative,
            state,
            candidate_html,
            hashlib.sha256(candidate_html.encode("utf-8")).hexdigest(),
        )
        if review_error:
            return fail(review_error)
        decision_record = review_record_content(
            (initiative / "decision-log.md").read_text(encoding="utf-8"),
            brief_review_field(state, "review_record").partition("#")[2],
        ) or ""
        editorial_findings = composition_editorial_findings(initiative, candidate_html)
        exception_error = reviewed_editorial_exception_error(
            candidate_html, decision_record, editorial_findings, args.allow_reviewed_editorial_exceptions,
        )
        if exception_error:
            return fail(exception_error)
    errors = stakeholder_brief_errors(candidate_html, rendered=True)
    if errors:
        return fail("candidate fails rendered structural contract: " + "; ".join(errors))
    bundle_root = Path(__file__).resolve().parent.parent
    pearson_errors = policy_errors(candidate_html, root=bundle_root)
    if pearson_errors:
        return fail("candidate fails Pearson identity policy: " + "; ".join(pearson_errors))
    consumer_root = initiative.parent.parent
    if root_attribute(candidate_html, "data-client-identity-profile") == "pearson":
        try:
            provision_pearson_logo(bundle_root, consumer_root)
        except Exception as error:
            return fail(f"could not provision official local logo: {error}")

    try:
        # Promotion owns only the derived HTML and its lifecycle state.  Notes,
        # handoffs and decision records are evidence/narrative, not transaction
        # members: changing them here made a generic renderer rewrite process
        # prose and expanded recovery scope without improving pair integrity.
        manifest = final_source_manifest(initiative, rendered_state, {})
        rendered_html = render_provenance_digests(
            render_provenance_fragments(
                render_lifecycle(candidate_html, rendered_state), initiative, manifest,
            ),
            manifest,
        )
        final_provenance_error = provenance_error(
            initiative, rendered_html,
            decision_record,
            manifest,
        )
        if final_provenance_error:
            raise ValueError(f"rendered provenance does not bind final source manifest: {final_provenance_error}")
        final_marker_error = lifecycle_error(rendered_html, rendered_state, initiative)
        if final_marker_error:
            raise ValueError(final_marker_error)
        promote_pair(target, state_path, rendered_html, rendered_state, args.fault_at)
    except (OSError, ValueError, RuntimeError) as error:
        return fail(f"promotion interrupted; rerun to recover before another promotion: {error}")
    print(f"Rendered stakeholder brief: {target}")
    if args.render_unapproved:
        print("Final HTML is available for autonomous review/recovery; Human Visibility, Tasks Ready and delivery remain false.")
    else:
        print("Next step: record the initiative's independent post-render review; rendering is not delivery approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
