#!/usr/bin/env python3
"""Validate the deterministic part of a consumer stakeholder-brief contract.

This script deliberately does not score prose, render screenshots, or decide
whether a stakeholder brief is useful.  Those remain independent human review
responsibilities at the Human Visibility gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

from brief_v2_sources import V2_EVIDENCE_REFERENCE_SOURCES, V2_REQUIRED_SOURCES, V2_SUPPORT_SOURCES
from brief_review import yaml_review_finding_outcome
from render_stakeholder_brief import lifecycle_error
from architecture_visual_contract import architecture_visual_errors
from editorial_exceptions import composition_editorial_findings, reviewed_editorial_exception_error

V1_REQUIRED_SOURCES = ("spec.md", "impact-map.md", "plan.md", "validation-plan.md")
V1_REQUIRED_SECTION_IDS = ("decision-snapshot", "scope", "validation", "decision")
V2_REQUIRED_SECTION_IDS = (
    "decision-snapshot", "scope", "architecture", "impact", "execution", "validation",
    "evolution", "decision", "coverage",
)
CORE_V2_SOURCES = frozenset(V2_REQUIRED_SOURCES[:6])
ALLOWED_COVERAGE = frozenset({"represented", "synthesized", "not_applicable", "link_only"})
REQUIRED_SHELL_HOOKS = ("brief-shell", "brief-header", "decision-register", "impact-evidence", "decision-actions")
PLACEHOLDERS = ("<initiative>", "<YYYY-MM-DD>")
BASELINE_FILE = "human-visibility-baseline.json"
EXCEPTION_FILE = "human-visibility-exception.yaml"

# Evidence packs are always initiative-relative. The bare form is the normal
# Markdown/link target form; the second expression deliberately catches paths
# that reach an evidence directory by traversal or absolute path so they are
# rejected instead of silently ignored.
EVIDENCE_REFERENCE = re.compile(
    r"(?<![A-Za-z0-9_/\\-])(?P<reference>(?:\.[\\/])?evidence[\\/][^\s`<>\"'()\[\]#?]*?\.md)(?:#[^\s`<>\"'()\[\]]*)?"
)
UNSAFE_EVIDENCE_REFERENCE = re.compile(
    r"(?<![A-Za-z0-9_.-])(?P<reference>(?:(?:[A-Za-z]:)?[\\/]|(?:\.\.[\\/])+)[^\s`<>\"'()\[\]#?]*?evidence[\\/][^\s`<>\"'()\[\]#?]*?\.md)(?:#[^\s`<>\"'()\[\]]*)?"
)

# T-003 deliberately mirrors the bounded grammar approved in
# specs/012-.../evidence/T-001.md. Product specs may use arbitrary prose;
# only these explicit source forms create a projection obligation.
RISK_TABLE_ROW = re.compile(r"^\|\s*(IR-[A-Za-z0-9][A-Za-z0-9_-]*)\s*\|.+\|\s*$")
HTTP_ROUTE = re.compile(
    r"\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(/api/[A-Za-z0-9._~!$&'()*+,;=:@%{}\-/]+)(?:\?[^`|\s]*)?"
)


@dataclass
class Report:
    structural: list[str] = field(default_factory=list)
    gate: list[str] = field(default_factory=list)
    freshness: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    editorial_exceptions: list[str] = field(default_factory=list)
    human_review: list[str] = field(default_factory=lambda: [
        "Independent reviewer must confirm the brief is accurate, decision-useful, "
        "proportional, and visually legible in its rendered form.",
        "A structural pass is not Human Visibility approval and does not replace "
        "the required independent semantic/rendered review.",
    ])

    @property
    def failures(self) -> list[str]:
        return self.structural + self.gate + self.freshness


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, report: Report, label: str) -> dict[str, object] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        report.structural.append(f"invalid {label}: {path.name} ({error})")
        return None
    if not isinstance(value, dict):
        report.structural.append(f"invalid {label}: {path.name} must contain an object")
        return None
    return value


class BriefParser(HTMLParser):
    """Keep just enough DOM shape for deterministic, non-semantic checks."""

    def __init__(self) -> None:
        super().__init__()
        self.nodes: list[tuple[str, dict[str, str]]] = []
        self.rendered_ids: list[str] = []
        self.tail_tokens: list[str] = []
        self.coverage_rows: list[list[tuple[str, list[str]]]] = []
        self._in_coverage_table = False
        self._row: list[tuple[str, list[str]]] | None = None
        self._cell_parts: list[str] | None = None
        self.panel_text: dict[str, list[str]] = {panel: [] for panel in ("impact", "architecture", "validation")}
        self._open_panels: list[tuple[str, str | None]] = []
        self._inert_depth = 0
        self._seen_rendered_html_close = False
        # Tab groups retain node indexes instead of source text.  The
        # validator must prove only rendered structure; prose that happens to
        # mention a keyboard key cannot create a tab contract.
        self.tablist_groups: list[list[int]] = []
        self._tablist_stack: list[tuple[str, list[int]]] = []
        self.script_bodies: list[str] = []
        self._script_body_stack: list[int] = []
        self.provenance_blocks: list[dict[str, str]] = []
        self._provenance_stack: list[tuple[str, dict[str, str]]] = []

    def _tail(self, token: str) -> None:
        if self._seen_rendered_html_close and not self._inert_depth:
            self.tail_tokens.append(token)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if self._inert_depth:
            if tag in {"script", "style", "template"}:
                self._inert_depth += 1
            return
        self._tail("element")
        self.nodes.append((tag, values))
        if "data-source" in values:
            block = {**values, "__tag": tag, "__text": ""}
            self.provenance_blocks.append(block)
            self._provenance_stack.append((tag, block))
        node_index = len(self.nodes) - 1
        if values.get("role") == "tablist":
            group: list[int] = []
            self.tablist_groups.append(group)
            self._tablist_stack.append((tag, group))
        elif values.get("role") == "tab" and self._tablist_stack:
            # A nested tablist owns its tabs; a surrounding tablist cannot
            # borrow them to satisfy its own selected/roving state.
            self._tablist_stack[-1][1].append(node_index)
        if values.get("id"):
            self.rendered_ids.append(values["id"])
        self._open_panels.append((tag, values.get("id") if values.get("id") in self.panel_text else None))
        if tag == "table" and values.get("id") == "coverage-register":
            self._in_coverage_table = True
        elif self._in_coverage_table and tag == "tr":
            self._row = []
        elif self._in_coverage_table and tag in {"td", "th"} and self._row is not None:
            self._cell_parts = []
        elif self._in_coverage_table and tag == "a" and self._cell_parts is not None:
            href = values.get("href", "")
            if href.startswith("#"):
                self._cell_parts.append(href)
        if tag in {"script", "style", "template"}:
            if tag == "script":
                self.script_bodies.append("")
                self._script_body_stack.append(len(self.script_bodies) - 1)
            self._inert_depth += 1

    def handle_data(self, data: str) -> None:
        # Script/style/template contents are source code or inert markup, not
        # text a stakeholder can see in the rendered panel. They must never
        # satisfy a source-to-brief projection obligation.
        if self._inert_depth:
            if self._script_body_stack:
                self.script_bodies[self._script_body_stack[-1]] += data
        else:
            if data.strip():
                self._tail("text")
            for _, block in self._provenance_stack:
                block["__text"] += data
            for _, panel in self._open_panels:
                if panel is not None:
                    self.panel_text[panel].append(data)
        if self._cell_parts is not None:
            self._cell_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._inert_depth:
            if tag in {"script", "style", "template"}:
                if tag == "script" and self._script_body_stack:
                    self._script_body_stack.pop()
                self._inert_depth -= 1
            return
        if tag == "html":
            self._seen_rendered_html_close = True
        else:
            self._tail("end-tag")
        if self._in_coverage_table and tag in {"td", "th"} and self._row is not None and self._cell_parts is not None:
            self._row.append((" ".join(self._cell_parts).strip(), [part for part in self._cell_parts if part.startswith("#")]))
            self._cell_parts = None
        elif self._in_coverage_table and tag == "tr" and self._row is not None:
            self.coverage_rows.append(self._row)
            self._row = None
        elif self._in_coverage_table and tag == "table":
            self._in_coverage_table = False
        for index in range(len(self._provenance_stack) - 1, -1, -1):
            if self._provenance_stack[index][0] == tag:
                del self._provenance_stack[index:]
                break
        for index in range(len(self._open_panels) - 1, -1, -1):
            if self._open_panels[index][0] == tag:
                del self._open_panels[index:]
                break
        for index in range(len(self._tablist_stack) - 1, -1, -1):
            if self._tablist_stack[index][0] == tag:
                del self._tablist_stack[index:]
                break

    def handle_decl(self, decl: str) -> None:
        self._tail("declaration")

    def unknown_decl(self, data: str) -> None:
        self._tail("declaration")

    def handle_pi(self, data: str) -> None:
        self._tail("processing-instruction")


def brief_lineage(html: str) -> str | None:
    marker = re.search(r'\bdata-harness-brief-design\s*=\s*["\'](v1|v2)["\']', html)
    return marker.group(1) if marker else None


def required_sources(lineage: str) -> tuple[str, ...]:
    return V2_REQUIRED_SOURCES if lineage == "v2" else V1_REQUIRED_SOURCES


def yaml_scalar(content: str, key: str, *, indent: int | None = None) -> str | None:
    prefix = rf"^\s{{{indent}}}" if indent is not None else r"^\s*"
    match = re.search(rf"(?m){prefix}{re.escape(key)}:\s*(.*?)\s*$", content)
    if not match:
        return None
    return match.group(1).split(" #", 1)[0].strip().strip('"\'')


def yaml_raw_scalar(content: str, key: str, *, indent: int | None = None) -> str | None:
    """Read a scalar without converting whitespace or nested quotes to syntax."""
    prefix = rf"^\s{{{indent}}}" if indent is not None else r"^\s*"
    match = re.search(rf"(?m){prefix}{re.escape(key)}:\s?(.*)$", content)
    return match.group(1) if match else None


def yaml_exact_literal(raw_value: str | None, literal: str) -> bool:
    """Accept one canonical YAML scalar without normalizing its contents.

    YAML quote delimiters are syntax and may surround the literal.  Case,
    whitespace, embedded quotes and descriptive alternatives are content and
    must not grant a gate outcome.
    """
    if raw_value is None:
        return False
    value = raw_value
    if value[:1] in {"\"", "'"} and value[-1:] == value[:1]:
        value = value[1:-1]
    return value == literal


def yaml_bool(content: str, key: str) -> bool | None:
    value = yaml_scalar(content, key, indent=2)
    if value is None:
        return None
    return value.lower() == "true"


def baseline_metadata(state: str) -> dict[str, str | None]:
    """Keep review and prior-change identity explicit in the one v2 baseline."""
    reviewer = yaml_scalar(state, "coverage_reviewer", indent=2)
    review_record = yaml_scalar(state, "review_record", indent=2)
    return {
        "review_record": review_record,
        "reviewed_by": reviewer,
        "coverage_reviewer": reviewer,
        "reviewed_at": yaml_scalar(state, "reviewed_at", indent=2),
        "prior_change_anchor": review_record,
    }


def load_exception_yaml(path: Path, report: Report) -> dict[str, str] | None:
    """Read the deliberately tiny, portable exception contract without PyYAML."""
    values: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        report.structural.append(f"invalid Human Visibility exception: {path.name} ({error})")
        return None
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.fullmatch(r"([a-z_]+):\s*(.+)", stripped)
        if not match:
            report.structural.append(f"invalid Human Visibility exception: unsupported line {stripped!r}")
            return None
        value = re.split(r"\s+#", match.group(2).strip(), maxsplit=1)[0].strip()
        values[match.group(1)] = value.strip('"\'')
    return values


def approved_exception(initiative: Path, report: Report) -> str | None:
    path = initiative / EXCEPTION_FILE
    if not path.is_file():
        return None
    exception = load_exception_yaml(path, report)
    if exception is None:
        return None
    scope = exception.get("scope")
    required = ("reason", "owner", "human_visibility_status")
    missing = [key for key in required if not isinstance(exception.get(key), str) or not exception[key].strip()]
    if missing or exception.get("human_visibility_status") != "reviewed":
        report.gate.append(
            "unapproved Human Visibility exception: requires non-empty reason, owner, "
            "and human_visibility_status: reviewed"
        )
        return None
    if scope not in {"not_applicable", "freshness", "legacy"}:
        report.gate.append("unapproved Human Visibility exception: scope must be not_applicable, freshness or legacy")
        return None
    return str(scope)


def approved_design_exception(initiative: Path, report: Report) -> bool:
    """A material custom layout is reviewed in the canonical decision log."""
    path = initiative / "decision-log.md"
    if not path.is_file():
        report.structural.append("missing decision-log.md required for design exception review")
        return False
    for row in (line.lower() for line in path.read_text(encoding="utf-8").splitlines() if "|" in line):
        if (("design exception" in row or "layout exception" in row)
                and ("reviewed" in row or "accepted" in row)
                and ("rationale" in row or "reason" in row)
                and "decision surface" in row):
            return True
    return False


def check_gate_state(initiative: Path, report: Report) -> None:
    state = initiative / "run-state.yaml"
    if not state.is_file():
        report.gate.append("missing required source artifact: run-state.yaml")
        return
    content = state.read_text(encoding="utf-8")
    human_visibility = yaml_bool(content, "human_visibility_ready")
    if human_visibility is None:
        report.gate.append("run-state.yaml lacks quality_gates.human_visibility_ready")
    elif not human_visibility:
        report.gate.append("Human Visibility gate is not declared ready in run-state.yaml")


def check_v2_gate_state(initiative: Path, report: Report) -> None:
    """Enforce v2-only readiness and distinct review metadata.

    This intentionally reads a small, fixed YAML shape instead of introducing a
    YAML dependency or a parallel review-state file.
    """
    state_path = initiative / "run-state.yaml"
    content = state_path.read_text(encoding="utf-8")
    state_lineage = yaml_scalar(content, "brief_lineage")
    if state_lineage != "v2":
        report.gate.append("v2 brief requires run-state.yaml brief_lineage: v2")
    gates = {key: yaml_bool(content, key) for key in (
        "tasks_drafted", "brief_coverage_ready", "human_visibility_ready", "tasks_ready",
    )}
    for key, value in gates.items():
        if value is None:
            report.gate.append(f"run-state.yaml lacks quality_gates.{key} required by v2")
        elif not value:
            report.gate.append(f"v2 gate is not declared ready: {key}")
    author = yaml_scalar(content, "author", indent=2)
    reviewer = yaml_scalar(content, "coverage_reviewer", indent=2)
    reviewed_at = yaml_scalar(content, "reviewed_at", indent=2)
    review_record = yaml_scalar(content, "review_record", indent=2)
    findings = yaml_raw_scalar(content, "findings_status", indent=2)
    if not author:
        report.gate.append("v2 brief_review.author is required")
    if not reviewer:
        report.gate.append("v2 brief_review.coverage_reviewer is required")
    if author and reviewer and author == reviewer:
        report.gate.append("v2 brief_review author and coverage_reviewer must be distinct identities")
    if not reviewed_at:
        report.gate.append("v2 brief_review.reviewed_at is required")
    if not review_record or not review_record.startswith("decision-log.md#"):
        report.gate.append("v2 brief_review.review_record must locate a decision-log.md record")
    try:
        findings_outcome = yaml_review_finding_outcome(findings)
    except ValueError as error:
        report.gate.append(str(error))
    else:
        if findings_outcome != "pass":
            report.gate.append("v2 brief_review.findings_status must be exactly pass for Human Visibility readiness")
    decision_log = initiative / "decision-log.md"
    if review_record and review_record.startswith("decision-log.md#"):
        record_id = review_record.partition("#")[2]
        record = decision_record(decision_log, record_id) if decision_log.is_file() else None
        if record is None:
            report.gate.append("v2 brief_review.review_record does not resolve in decision-log.md")
        elif gates.get("tasks_ready") is True:
            if "propagat" not in record.lower():
                report.gate.append("v2 Tasks Ready review record does not confirm decision propagation")
    check_decision_quality_review(initiative, content, report)


def check_decision_quality_review(initiative: Path, state: str, report: Report) -> None:
    """Verify minimal independent rendered-review evidence, never its judgment.

    Initiatives may add review lenses that fit their own risk and domain, but
    the reusable validator must not prescribe personas or a review count.  The
    deterministic boundary is intentionally small: a real record, an exact
    approval, an independent reviewer, a digest of the rendered artifact, and
    the loopback preview evidence that makes the rendered claim inspectable.
    """
    required = yaml_scalar(state, "quality_review_required", indent=2)
    if required not in {"true", "True"}:
        return
    fields = {key: yaml_scalar(state, key, indent=2) for key in (
        "quality_review_record", "quality_review_status", "quality_review_reviewer",
        "quality_review_inputs",
    )}
    raw_outcomes = {
        "quality_review_status": yaml_raw_scalar(state, "quality_review_status", indent=2),
    }
    for key, value in fields.items():
        if not value:
            report.gate.append(f"v2 decision-quality review lacks brief_review.{key}")
    # These are closed outcome fields.  Do not turn aliases or prose into
    # authorization through case folding or whitespace/quote normalization.
    if fields["quality_review_status"] and not yaml_exact_literal(raw_outcomes["quality_review_status"], "approve"):
        report.gate.append("v2 decision-quality review status must be exactly approve")
    reviewer = fields["quality_review_reviewer"] or ""
    author = yaml_scalar(state, "author", indent=2)
    if reviewer and author and reviewer == author:
        report.gate.append("v2 decision-quality reviewer must be distinct from brief_review.author")
    inputs = fields["quality_review_inputs"] or ""
    rendered_pattern = r"(?:^|;\s*)rendered=[^;@]+@sha256:[0-9a-fA-F]{64}(?=;|$)"
    if not re.search(rendered_pattern, inputs):
        report.gate.append("v2 decision-quality review inputs must locate and digest the rendered artifact")
    record = fields["quality_review_record"] or ""
    if record:
        candidate = (initiative / record).resolve()
        evidence_root = (initiative / "evidence").resolve()
        try:
            contained = candidate.is_relative_to(evidence_root)
        except AttributeError:
            contained = str(candidate).startswith(str(evidence_root))
        if not contained or not candidate.is_file():
            report.gate.append("v2 decision-quality review record must resolve inside evidence/")
        elif not candidate.read_text(encoding="utf-8").strip():
            report.gate.append("v2 decision-quality review record must be nonempty")
        else:
            evidence = candidate.read_text(encoding="utf-8")
            preview = re.search(r"(?m)^\s*Preview URL: `?(?P<url>\S+?)`?\s*$", evidence)
            if not preview or not re.fullmatch(r"http://127\.0\.0\.1(?::\d{1,5})?(?:/[^\s]*)?", preview.group("url")):
                report.gate.append("v2 decision-quality review record must contain Preview URL: http://127.0.0.1[:port]/...")
            environment = re.search(r"(?m)^\s*Preview environment:\s*`?(?P<value>.*?)`?\s*$", evidence)
            if not environment or not environment.group("value").strip():
                report.gate.append("v2 decision-quality review record must contain a non-empty Preview environment")


def decision_record(path: Path, record_id: str) -> str | None:
    """Resolve one exact table record or explicit Markdown decision section.

    Table rows preserve the legacy concise decision register.  Composition
    reviews use a headed record so their identity and fields cannot be inferred
    from an arbitrary substring elsewhere in the log.
    """
    log = path.read_text(encoding="utf-8")
    # A word boundary would treat the hyphen in a longer identifier (for
    # example, D-001-extra) as a valid terminator.  Headed records must use
    # the exact ID, followed only by a title boundary.
    heading = re.compile(rf"(?m)^(?P<level>#+)\s+{re.escape(record_id)}(?=$|\s|—).*$")
    match = heading.search(log)
    if match:
        next_heading = re.compile(r"(?m)^(?P<level>#+)\s+")
        following = next(
            (item for item in next_heading.finditer(log, match.end()) if len(item.group("level")) <= len(match.group("level"))),
            None,
        )
        return log[match.start() : following.start() if following else len(log)]
    for line in log.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] == record_id:
            return line
    return None


def coverage_source(cell: str) -> tuple[str | None, str]:
    for source in V2_REQUIRED_SOURCES:
        if cell.startswith(source):
            return source, cell[len(source):].strip(" \t§:-")
    return None, ""


def evidence_references(content: str) -> set[str]:
    """Return every declared evidence path, removing optional heading anchors.

    We intentionally inspect only the canonical v2 source set. Brief
    provenance is checked separately and must not introduce an untracked file
    dependency.
    """
    return {
        re.sub(r"^\.[\\/]", "", match.group("reference").split("#", 1)[0])
        for pattern in (EVIDENCE_REFERENCE, UNSAFE_EVIDENCE_REFERENCE)
        for match in pattern.finditer(content)
        # `evidence/*.md` is a documentation glob, not a cited artifact.
        if "*" not in match.group("reference")
    }


def inventory_risk_ids(impact_map: str) -> set[str]:
    """Return material IDs only from the first column of Markdown tables."""
    return {match.group(1) for line in impact_map.splitlines() if (match := RISK_TABLE_ROW.match(line))}


def inventory_http_routes(plan: str) -> set[str]:
    """Return normalized API routes from the T-001 explicit contract grammar."""
    routes: set[str] = set()
    in_contract_heading = False
    table_contract = False
    for line in plan.splitlines():
        if not line.strip():
            table_contract = False
            continue
        heading = re.match(r"^#{1,6}\s+(.+)$", line)
        if heading:
            in_contract_heading = bool(re.search(r"\b(api|contract)s?\b", heading.group(1), re.IGNORECASE))
            table_contract = False
            continue
        is_table = line.lstrip().startswith("|")
        if is_table:
            cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
            is_separator = all(not cell or set(cell) <= {"-", ":", " "} for cell in cells)
            has_contract_column = any(re.fullmatch(r"(?:api )?(?:route|method)", cell) for cell in cells)
            if (in_contract_heading or has_contract_column) and not table_contract:
                table_contract = True
                continue
            if is_separator:
                continue
        is_table_contract = is_table and table_contract
        is_list_contract = in_contract_heading and re.match(r"^\s*[-*]\s+`", line) is not None
        if is_table_contract or is_list_contract:
            routes.update(f"{match.group(1)} {match.group(2)}" for match in HTTP_ROUTE.finditer(line))
    return routes


def panel_contains_token(panel_text: str, token: str) -> bool:
    """Avoid accepting an ID/route merely because it is a longer token's prefix."""
    return re.search(rf"(?<![A-Za-z0-9_./:{{}}-]){re.escape(token)}(?![A-Za-z0-9_./:{{}}-])", panel_text) is not None


def check_v2_projection(initiative: Path, report: Report) -> None:
    """Prove material source tokens are visible in their prescribed v2 view."""
    impact_map = initiative / "impact-map.md"
    plan = initiative / "plan.md"
    brief = initiative / "stakeholder-brief.html"
    if not (impact_map.is_file() and plan.is_file() and brief.is_file()):
        return
    parser = BriefParser()
    try:
        parser.feed(brief.read_text(encoding="utf-8"))
    except Exception:
        report.structural.append("invalid v2 stakeholder brief HTML")
        return
    impact_text = " ".join(parser.panel_text["impact"])
    architecture_text = " ".join(parser.panel_text["architecture"])
    validation_text = " ".join(parser.panel_text["validation"])
    for risk_id in sorted(inventory_risk_ids(impact_map.read_text(encoding="utf-8"))):
        if not panel_contains_token(impact_text, risk_id):
            report.structural.append(f"missing v2 risk projection: {risk_id} from impact-map.md must appear in #impact")
    for route in sorted(inventory_http_routes(plan.read_text(encoding="utf-8"))):
        if not (panel_contains_token(architecture_text, route) or panel_contains_token(validation_text, route)):
            report.structural.append(f"missing v2 API projection: {route} from plan.md must appear in #architecture or #validation")


def deferred_task_evidence(initiative: Path) -> set[str]:
    """Return evidence destinations for tasks not yet ready for evaluation.

    A v2 planning package must declare evidence for every preliminary task, so
    treating those future destinations as current citations would make a valid
    `tasks_ready` initiative impossible to baseline.  Once a task reaches
    needs_evaluation/approved/done, its declared evidence is no longer
    deferred and missing proof fails normally.
    """
    state_path = initiative / "run-state.yaml"
    if not state_path.is_file():
        return set()
    deferred: set[str] = set()
    content = state_path.read_text(encoding="utf-8")
    entries = re.split(r"(?m)^\s{2}-\s+id:\s*", content)[1:]
    for entry in entries:
        status = yaml_scalar(entry, "status", indent=4)
        evidence = yaml_scalar(entry, "evidence", indent=4)
        if status in {"pending", "ready", "in_progress", "blocked"} and evidence:
            candidate = Path(evidence)
            if (
                not candidate.is_absolute()
                and ".." not in candidate.parts
                and candidate.parts
                and candidate.parts[0] == "evidence"
                and candidate.suffix.lower() == ".md"
            ):
                deferred.add(candidate.as_posix())
    return deferred


def check_v2_evidence_references(initiative: Path, report: Report) -> None:
    """Require cited v2 evidence packs to exist inside this initiative."""
    initiative_root = initiative.resolve()
    deferred = deferred_task_evidence(initiative)
    for source in V2_EVIDENCE_REFERENCE_SOURCES:
        source_path = initiative / source
        if not source_path.is_file():
            continue
        for reference in sorted(evidence_references(source_path.read_text(encoding="utf-8"))):
            if reference.replace("\\", "/") in deferred:
                continue
            candidate = Path(reference)
            invalid = (
                candidate.is_absolute()
                or ".." in candidate.parts
                or not candidate.parts
                or candidate.parts[0] != "evidence"
                or candidate.suffix.lower() != ".md"
            )
            if invalid:
                report.structural.append(
                    "invalid v2 evidence reference in " + source
                    + ": must be an initiative-relative evidence/*.md path without traversal or absolute path"
                )
                continue
            resolved = (initiative_root / candidate).resolve()
            try:
                relative = resolved.relative_to(initiative_root)
            except ValueError:
                report.structural.append(
                    "invalid v2 evidence reference in " + source
                    + ": must resolve inside the initiative evidence directory"
                )
                continue
            if not relative.parts or relative.parts[0] != "evidence":
                report.structural.append(
                    "invalid v2 evidence reference in " + source
                    + ": must resolve inside the initiative evidence directory"
                )
                continue
            if not resolved.is_file():
                report.structural.append(
                    f"missing referenced v2 evidence artifact: {relative.as_posix()} (cited by {source})"
                )


def check_v2_coverage_rows(parser: BriefParser, report: Report) -> None:
    provenance_by_id = {
        attrs.get("id"): attrs.get("data-source")
        for _, attrs in parser.nodes
        if attrs.get("id") and attrs.get("data-source")
    }
    rows_by_source: dict[str, list[tuple[str, list[str], str, str]]] = {}
    for row in parser.coverage_rows:
        if len(row) < 3 or row[0][0].lower() == "source / heading":
            continue
        source, heading = coverage_source(row[0][0])
        if source is None:
            continue
        target_text, targets = row[1]
        disposition_cell = row[2][0].strip()
        disposition, separator, reason = disposition_cell.partition(":")
        disposition = disposition.strip()
        rows_by_source.setdefault(source, []).append((heading, targets, disposition, reason.strip()))
        if not heading:
            report.structural.append(f"v2 coverage row missing heading locator for source {source}")
        if not targets:
            report.structural.append(f"v2 coverage row missing #target for source {source}")
        for target in targets:
            target_id = target[1:]
            if target_id not in provenance_by_id:
                report.structural.append(f"v2 coverage row target does not resolve for source {source}")
            elif disposition in {"represented", "synthesized"} and provenance_by_id[target_id] != source:
                report.structural.append(f"v2 coverage row target/provenance mismatch for source {source}")
        if disposition not in ALLOWED_COVERAGE:
            report.structural.append(f"v2 coverage row has invalid disposition for source {source}")
        elif disposition in {"not_applicable", "link_only"} and (not separator or not reason):
            report.structural.append(f"v2 coverage row missing reason for source {source}")
    for source in V2_REQUIRED_SOURCES:
        if source not in rows_by_source:
            report.structural.append(f"missing v2 coverage register entry: {source}")


def check_v2_support_provenance(initiative: Path, parser: BriefParser, report: Report) -> None:
    """Bind the fixed v2 support source to local bytes without judging its meaning."""
    for source in V2_SUPPORT_SOURCES:
        blocks = [block for block in parser.provenance_blocks if block.get("data-source") == source]
        if not blocks:
            report.structural.append(f"missing v2 provenance block for required support source: {source}")
            continue
        source_path = initiative / source
        if not source_path.is_file():
            continue
        source_text = source_path.read_text(encoding="utf-8")
        expected_digest = f"sha256:{digest(source_path)}"
        for block in blocks:
            section = block.get("data-source-section", "")
            fragment = block.get("data-source-fragment", "")
            fragment_digest = block.get("data-source-fragment-sha256", "")
            coverage = block.get("data-coverage", "")
            if coverage not in {"represented", "synthesized"}:
                report.structural.append(f"v2 support source must be represented or synthesized: {source}")
            if not section or section not in source_text:
                report.structural.append(f"v2 support provenance section is not present in the local source: {source}")
            if block.get("data-source-digest") != expected_digest:
                report.structural.append(f"v2 support provenance digest does not bind the current local source: {source}")
            if not fragment or fragment not in source_text:
                report.structural.append(f"v2 support provenance fragment is not present in the current local source: {source}")
            elif fragment not in block.get("__text", ""):
                report.structural.append(f"v2 support provenance fragment is not visible in its rendered source block: {source}")
            expected_fragment_digest = f"sha256:{hashlib.sha256(fragment.encode('utf-8')).hexdigest()}"
            if fragment_digest != expected_fragment_digest:
                report.structural.append(f"v2 support provenance fragment digest does not bind the declared source fragment: {source}")


def check_v2_represented_source_digests(initiative: Path, parser: BriefParser, report: Report) -> None:
    """Bind every declared represented local source to its current bytes.

    This is deliberately attribute-driven: a visible phrase never creates a
    validation obligation.  Decision records retain their separately scoped
    digest contract; every filesystem-backed represented source is compared
    directly to the source bytes it declares.
    """
    root = initiative.resolve()
    snapshot_digest = None
    snapshots = [
        attrs for tag, attrs in parser.nodes
        if attrs.get("data-lifecycle-marker") == "rendered-state-digest"
    ]
    snapshot_blocks = [
        block for block in parser.provenance_blocks
        if (block.get("data-source") == "run-state.yaml"
            and block.get("data-lifecycle-marker") == "rendered-state-source-digest")
    ]
    if snapshot_blocks and len(snapshots) != 1:
        report.structural.append(
            "rendered state snapshot requires exactly one data-lifecycle-marker=rendered-state-digest meta"
        )
        snapshot_digest = None
    elif snapshots:
        snapshot = snapshots[0]
        if (snapshot.get("data-lifecycle-source") != "run-state.yaml"
                or snapshot.get("data-lifecycle-fragment") != "rendered run-state bytes"
                or not re.fullmatch(r"[0-9a-f]{64}", snapshot.get("content", ""))):
            report.structural.append("rendered state snapshot meta has invalid source, fragment, or digest content")
            snapshot_digest = None
        else:
            snapshot_digest = "sha256:" + snapshot["content"]
    for block in parser.provenance_blocks:
        if block.get("data-coverage") != "represented":
            continue
        source = block.get("data-source", "")
        if source == "decision-log.md":
            continue
        candidate = initiative / source
        try:
            candidate.resolve().relative_to(root)
        except ValueError:
            continue
        if not candidate.is_file():
            continue
        snapshot_bound = (
            source == "run-state.yaml"
            and block.get("data-lifecycle-marker") == "rendered-state-source-digest"
        )
        if snapshot_bound:
            if not block.get("data-source-fragment") or block["data-source-fragment"] not in block.get("__text", ""):
                report.structural.append("rendered-state-source-digest block requires a non-empty visible provenance fragment")
            expected = snapshot_digest
        else:
            expected = f"sha256:{digest(candidate)}"
        if expected is None:
            continue
        if block.get("data-source-digest") != expected:
            report.structural.append(
                ("v2 represented run-state provenance digest does not bind the rendered snapshot"
                 if snapshot_bound else
                 f"v2 represented provenance digest does not bind the current local source: {source}")
            )


def strip_javascript_comments(source: str) -> str:
    """Return source with comments blanked while retaining executable tokens.

    This is intentionally a small lexical pass, not a JavaScript evaluator.
    It prevents a comment containing a copied handler from satisfying the
    static contract while preserving quoted values used by real event calls.
    """
    output: list[str] = []
    index = 0
    quote: str | None = None
    while index < len(source):
        character = source[index]
        following = source[index + 1] if index + 1 < len(source) else ""
        if quote:
            output.append(character)
            if character == "\\" and index + 1 < len(source):
                output.append(source[index + 1])
                index += 2
                continue
            if character == quote:
                quote = None
            index += 1
            continue
        if character in {"'", '"', "`"}:
            quote = character
            output.append(character)
            index += 1
            continue
        if character == "/" and following == "/":
            while index < len(source) and source[index] not in "\r\n":
                output.append(" ")
                index += 1
            continue
        if character == "/" and following == "*":
            output.extend((" ", " "))
            index += 2
            while index < len(source) - 1 and not (source[index] == "*" and source[index + 1] == "/"):
                output.append("\n" if source[index] == "\n" else " ")
                index += 1
            if index < len(source):
                output.extend((" ", " "))
                index += 2
            continue
        output.append(character)
        index += 1
    return "".join(output)


def _matching_javascript_brace(source: str, opening: int) -> int | None:
    """Find a matching brace outside quoted literals in a bounded source body."""
    depth = 0
    index = opening
    quote: str | None = None
    while index < len(source):
        character = source[index]
        if quote:
            if character == "\\":
                index += 2
                continue
            if character == quote:
                quote = None
            index += 1
            continue
        if character in {"'", '"', "`"}:
            quote = character
        elif character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def _matching_javascript_parenthesis(source: str, opening: int) -> int | None:
    """Find a matching parenthesis outside quoted literals in a bounded body."""
    depth = 0
    index = opening
    quote: str | None = None
    while index < len(source):
        character = source[index]
        if quote:
            if character == "\\" and index + 1 < len(source):
                index += 2
                continue
            if character == quote:
                quote = None
            index += 1
            continue
        if character in {"'", '"', "`"}:
            quote = character
        elif character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def remove_unreachable_javascript_blocks(source: str) -> str:
    """Blank simple literal-false blocks so copied dead handlers are not proof.

    We do not attempt to prove all JavaScript reachability.  This narrow guard
    rejects the common `if (false) { ... }` or `if (0) { ... }` token dump and
    keeps the contract candidly static rather than pretending to execute code.
    """
    output = source
    pattern = re.compile(r"\bif\s*\(\s*(?:false|0)\s*\)\s*\{")
    search_from = 0
    while match := pattern.search(output, search_from):
        opening = output.find("{", match.start(), match.end())
        closing = _matching_javascript_brace(output, opening)
        if closing is None:
            break
        output = output[:match.start()] + (" " * (closing + 1 - match.start())) + output[closing + 1:]
        search_from = closing + 1
    return output


def mask_javascript_strings(source: str) -> str:
    """Blank literals while retaining offsets for code-only method detection."""
    output: list[str] = []
    index = 0
    quote: str | None = None
    while index < len(source):
        character = source[index]
        if quote:
            output.append("\n" if character == "\n" else " ")
            if character == "\\" and index + 1 < len(source):
                output.append(" ")
                index += 2
                continue
            if character == quote:
                quote = None
            index += 1
            continue
        if character in {"'", '"', "`"}:
            quote = character
            output.append(" ")
        else:
            output.append(character)
        index += 1
    return "".join(output)


def _javascript_string_at(source: str, index: int) -> tuple[str, int] | None:
    while index < len(source) and source[index].isspace():
        index += 1
    if index >= len(source) or source[index] not in {"'", '"'}:
        return None
    quote = source[index]
    start = index + 1
    index += 1
    value: list[str] = []
    while index < len(source):
        character = source[index]
        if character == "\\" and index + 1 < len(source):
            value.append(source[index + 1])
            index += 2
            continue
        if character == quote:
            return "".join(value), index + 1
        value.append(character)
        index += 1
    return None


def has_javascript_method_call(source: str, masked: str, method: str, first_argument: str) -> bool:
    """Find a real method call with its expected first literal argument."""
    for match in re.finditer(rf"\.{re.escape(method)}\s*\(", masked):
        value = _javascript_string_at(source, match.end())
        if value and value[0] == first_argument:
            return True
    return False


def javascript_key_values(source: str, masked: str) -> set[str]:
    """Return literal values compared to event.key/event.code in live code."""
    values: set[str] = set()
    for match in re.finditer(r"\.(?:key|code)\s*={2,3}", masked):
        value = _javascript_string_at(source, match.end())
        if value:
            values.add(value[0])
    return values


def javascript_tab_initializers(script_bodies: list[str]) -> list[tuple[str, str, str]]:
    """Discover live, tablist-scoped initializers invoked for every tablist.

    The grammar intentionally permits arbitrary function names and arbitrary
    tab counts/layout.  It proves the important association: the initializer
    receives one tablist and bootstrap iterates every declared tablist, rather
    than relying on document-wide tabs or a canonical count.
    """
    source = remove_unreachable_javascript_blocks(strip_javascript_comments("\n".join(script_bodies)))
    candidates: list[tuple[str, str, str]] = []
    patterns = (
        re.compile(r"\bfunction\s+([A-Za-z_$][\w$]*)\s*\(\s*([A-Za-z_$][\w$]*)\s*\)\s*\{"),
        re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\(\s*([A-Za-z_$][\w$]*)\s*\)\s*=>\s*\{"),
    )
    for pattern in patterns:
        for match in pattern.finditer(source):
            closing = _matching_javascript_brace(source, match.end() - 1)
            if closing is not None:
                candidates.append((match.group(1), match.group(2), source[match.end():closing]))

    live: list[tuple[str, str, str]] = []
    for name, parameter, body in candidates:
        bootstrap = re.compile(
            rf"document\s*\.\s*querySelectorAll\s*\(\s*['\"]\[role\s*=\s*['\"]tablist['\"]\]\s*['\"]\s*\)\s*\.\s*forEach\s*\(\s*{re.escape(name)}\s*\)"
        )
        if bootstrap.search(source):
            live.append((name, parameter, body))
    return live


def javascript_named_function_bodies(source: str) -> dict[str, tuple[tuple[str, ...], str]]:
    """Return bounded named function bodies for a local static call path.

    This deliberately recognizes only ordinary declarations and block-bodied
    arrow assignments.  The tab contract needs a reviewable proof that a
    listener is attached for each scoped tab, not a JavaScript interpreter.
    """
    functions: dict[str, tuple[tuple[str, ...], str]] = {}
    patterns = (
        re.compile(r"\bfunction\s+([A-Za-z_$][\w$]*)\s*\(([^)]*)\)\s*\{"),
        re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\(([^)]*)\)\s*=>\s*\{"),
        re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?([A-Za-z_$][\w$]*)\s*=>\s*\{"),
    )
    for pattern in patterns:
        for match in pattern.finditer(source):
            opening = source.find("{", match.start(), match.end())
            closing = _matching_javascript_brace(source, opening)
            if closing is None:
                continue
            raw_parameters = match.group(2)
            parameters = tuple(
                parameter.strip()
                for parameter in raw_parameters.split(",")
                if re.fullmatch(r"[A-Za-z_$][\w$]*", parameter.strip())
            )
            functions[match.group(1)] = (parameters, source[opening + 1:closing])
    return functions


def javascript_scoped_tab_collections(body: str, parameter: str) -> set[str]:
    """Return collection variables sourced directly from this tablist only."""
    source_pattern = (
        rf"(?:\[\s*\.\.\.\s*)?\b{re.escape(parameter)}"
        r"\.querySelectorAll\s*\(\s*['\"]\[role\s*=\s*['\"]tab['\"]\]\s*['\"]\s*\)"
    )
    array_source_pattern = (
        rf"Array\.from\s*\(\s*\b{re.escape(parameter)}"
        r"\.querySelectorAll\s*\(\s*['\"]\[role\s*=\s*['\"]tab['\"]\]\s*['\"]\s*\)\s*\)"
    )
    return {
        match.group(1)
        for match in re.finditer(
            rf"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:{source_pattern}|{array_source_pattern})",
            body,
        )
    }


def _javascript_callback_body(callback: str, functions: dict[str, tuple[tuple[str, ...], str]]) -> tuple[tuple[str, ...], str] | None:
    """Parse the bounded callback grammar accepted for scoped `forEach`."""
    callback = callback.strip()
    named = re.fullmatch(r"([A-Za-z_$][\w$]*)", callback)
    if named:
        return functions.get(named.group(1))
    arrow = re.match(r"(?:\(([^)]*)\)|([A-Za-z_$][\w$]*))\s*=>\s*", callback)
    function = re.match(r"function\s*\(([^)]*)\)\s*", callback)
    match = arrow or function
    if not match:
        return None
    raw_parameters = match.group(1) if match.group(1) is not None else match.group(2)
    parameters = tuple(
        parameter.strip()
        for parameter in raw_parameters.split(",")
        if re.fullmatch(r"[A-Za-z_$][\w$]*", parameter.strip())
    )
    remainder = callback[match.end():].strip()
    if remainder.startswith("{"):
        closing = _matching_javascript_brace(remainder, 0)
        if closing is None:
            return None
        return parameters, remainder[1:closing]
    # An expression-bodied callback can only be the activation call itself.
    return parameters, remainder


def _javascript_listener_events(source: str, receivers: tuple[str, ...]) -> set[str]:
    """Return click/keydown listeners attached to one of the supplied values."""
    masked = mask_javascript_strings(source)
    events: set[str] = set()
    for receiver in receivers:
        for match in re.finditer(rf"\b{re.escape(receiver)}\.addEventListener\s*\(", masked):
            value = _javascript_string_at(source, match.end())
            if value and value[0] in {"click", "keydown"}:
                events.add(value[0])
    return events


def _javascript_callback_listener_events(
    callback: tuple[tuple[str, ...], str],
    functions: dict[str, tuple[tuple[str, ...], str]],
    visited: set[str],
) -> set[str]:
    """Follow a callback's explicit per-tab helper calls, without globals.

    A helper is considered only when the callback passes one of its tab
    parameters to it.  This rejects a no-op `tabs.forEach` paired with
    listeners wired solely to a particular DOM element elsewhere.
    """
    parameters, body = callback
    events = _javascript_listener_events(body, parameters)
    for match in re.finditer(r"\b([A-Za-z_$][\w$]*)\s*\(([^()]*)\)", mask_javascript_strings(body)):
        name, raw_arguments = match.group(1), match.group(2)
        helper = functions.get(name)
        if not helper or name in visited:
            continue
        arguments = {argument.strip() for argument in raw_arguments.split(",")}
        if not arguments.intersection(parameters):
            continue
        visited.add(name)
        events.update(_javascript_callback_listener_events(helper, functions, visited))
    return events


def javascript_scoped_tab_listener_events(body: str, parameter: str) -> set[str]:
    """Find listeners attached in a callback of a tablist-scoped collection.

    This static grammar permits arbitrary tab counts and arbitrary numbers of
    tablists.  It only requires that the listener proof belongs to a callback
    of a collection queried from the initializer's own tablist (or a local
    helper explicitly invoked with that callback's tab).
    """
    functions = javascript_named_function_bodies(body)
    events: set[str] = set()
    for collection in javascript_scoped_tab_collections(body, parameter):
        for match in re.finditer(rf"\b{re.escape(collection)}\.forEach\s*\(", body):
            closing = _matching_javascript_parenthesis(body, body.find("(", match.start(), match.end()))
            if closing is None:
                continue
            callback = _javascript_callback_body(body[body.find("(", match.start(), match.end()) + 1:closing], functions)
            if callback is not None:
                events.update(_javascript_callback_listener_events(callback, functions, set()))
    return events


def check_v2_tab_contract(parser: BriefParser, report: Report) -> None:
    """Validate the bounded static contract for each declared rendered tablist.

    This deliberately does not execute JavaScript or certify browser/AT
    behaviour.  It proves that the canonical, progressive-enhancement surface
    has locally inspectable structural wiring and handler evidence.  The
    script body is the only accepted location for handler/key tokens, so
    visible prose cannot mask click-only controls.
    """
    if not parser.tablist_groups:
        return

    nodes_by_id: dict[str, tuple[str, dict[str, str]]] = {
        attrs["id"]: (tag, attrs)
        for tag, attrs in parser.nodes
        if attrs.get("id")
    }
    for position, group in enumerate(parser.tablist_groups, start=1):
        tabs = [parser.nodes[index][1] for index in group]
        label = f"v2 tablist {position}"
        if not tabs:
            report.structural.append(f"{label} has no contained role=tab controls; add a tab or remove the tablist role")
            continue
        selected = [tab for tab in tabs if tab.get("aria-selected") == "true"]
        if len(selected) != 1:
            report.structural.append(f'{label} must have exactly one aria-selected="true" tab')
        for tab in tabs:
            tab_id = tab.get("id", "")
            if not tab_id:
                report.structural.append(f"{label} tab requires a non-empty id for aria-labelledby reciprocity")
                continue
            panel_id = tab.get("aria-controls", "")
            panel = nodes_by_id.get(panel_id)
            if not panel:
                report.structural.append(f"{label} tab aria-controls must reference a rendered role=tabpanel")
                continue
            panel_tag, panel_attrs = panel
            if panel_attrs.get("role") != "tabpanel" or panel_attrs.get("aria-labelledby") != tab_id:
                report.structural.append(f"{label} tab/panel aria-controls and aria-labelledby must be reciprocal")
            if tab.get("aria-selected") == "true":
                if tab.get("tabindex") != "0":
                    report.structural.append(f'{label} selected tab must use tabindex="0"')
            elif tab.get("tabindex") != "-1":
                report.structural.append(f'{label} unselected tabs must use tabindex="-1"')

    initializers = javascript_tab_initializers(parser.script_bodies)
    if not initializers:
        report.structural.append(
            "v2 tab handler missing a live per-tablist initializer; initialize each rendered tablist without a fixed tab count"
        )
        return

    # A single reusable initializer is enough because bootstrap applies it to
    # every declared tablist.  Conversely, all candidate initializers must be
    # complete: an alternate live initializer cannot become a weak bypass.
    for name, parameter, body in initializers:
        masked = mask_javascript_strings(body)
        if not re.search(
            rf"\b{re.escape(parameter)}\.querySelectorAll\s*\(\s*['\"]\[role\s*=\s*['\"]tab['\"]\]\s*['\"]\s*\)",
            body,
        ):
            report.structural.append(f"v2 tab handler initializer {name} must query tabs within its tablist parameter")
        listener_events = javascript_scoped_tab_listener_events(body, parameter)
        if not listener_events:
            report.structural.append(f"v2 tab handler initializer {name} must attach controls for its tab collection")
        for requirement, event in (("click listener", "click"), ("keydown listener", "keydown")):
            if event not in listener_events:
                report.structural.append(f"v2 tab handler initializer {name} missing static {requirement} evidence")
        if not has_javascript_method_call(body, masked, "setAttribute", "aria-selected"):
            report.structural.append(f"v2 tab handler initializer {name} missing static selection mutation evidence")
        if not (re.search(r"\.hidden\s*=", masked) or has_javascript_method_call(body, masked, "setAttribute", "hidden") or has_javascript_method_call(body, masked, "toggleAttribute", "hidden")):
            report.structural.append(f"v2 tab handler initializer {name} missing static active-panel mutation evidence")
        if not re.search(r"\.focus\s*\(", masked):
            report.structural.append(f"v2 tab handler initializer {name} missing static focus mutation evidence")
        if not (re.search(r"\bhistory\.(?:replaceState|pushState)\s*\(", masked) or re.search(r"(?:\blocation|\bwindow\.location)\.hash\s*=", masked)):
            report.structural.append(f"v2 tab handler initializer {name} missing static hash/history mutation evidence")
        key_values = javascript_key_values(body, masked)
        missing_keys = [key for key in ("ArrowLeft", "ArrowRight", "Home", "End", "Enter") if key not in key_values]
        if not ({" ", "Space", "Spacebar"} & key_values):
            missing_keys.append("Space")
        if missing_keys:
            report.structural.append(
                f"v2 tab handler initializer {name} missing static keyboard evidence for: " + ", ".join(missing_keys)
            )


def check_v2_provenance(html: str, report: Report, initiative: Path | None = None) -> None:
    parser = BriefParser()
    try:
        parser.feed(html)
        parser.close()
    except Exception:
        report.structural.append("invalid v2 stakeholder brief HTML")
        return
    ids = {attrs.get("id") for _, attrs in parser.nodes}
    duplicate_ids = sorted({identifier for identifier in parser.rendered_ids if parser.rendered_ids.count(identifier) > 1})
    for identifier in duplicate_ids:
        report.structural.append(f"duplicate rendered HTML id: {identifier}; make every rendered id unique")
    if parser.tail_tokens:
        report.structural.append("rendered content appears after terminal </html>; remove trailing document content")
    check_v2_tab_contract(parser, report)
    report.structural.extend(architecture_visual_errors(html))
    if "coverage-register" not in ids:
        report.structural.append("missing v2 human-readable coverage register: coverage-register")
    check_v2_coverage_rows(parser, report)
    if initiative is not None:
        check_v2_support_provenance(initiative, parser, report)
        check_v2_represented_source_digests(initiative, parser, report)
    for tag, attrs in parser.nodes:
        if "data-source" not in attrs:
            continue
        identifier = attrs.get("id", "")
        location = f"#{identifier}" if re.fullmatch(r"[A-Za-z0-9_-]+", identifier) else f"<{tag}>"
        source = attrs["data-source"]
        if source not in V2_REQUIRED_SOURCES and not source.startswith(("evidence/", "handoffs/")):
            report.structural.append(f"unknown v2 provenance source at {location}")
        if not attrs.get("data-source-section"):
            report.structural.append(f"v2 provenance missing data-source-section for source {source if source in V2_REQUIRED_SOURCES else 'declared source'} at {location}")
        coverage = attrs.get("data-coverage")
        if coverage not in ALLOWED_COVERAGE:
            report.structural.append(f"v2 provenance has invalid data-coverage for source {source if source in V2_REQUIRED_SOURCES else 'declared source'} at {location}")
            continue
        if source in CORE_V2_SOURCES and coverage == "link_only":
            report.structural.append(f"v2 core source cannot be link_only: {source}")
        if coverage in {"not_applicable", "link_only"} and not attrs.get("data-coverage-reason"):
            report.structural.append(f"v2 coverage reason missing for source {source if source in V2_REQUIRED_SOURCES else 'declared source'} at {location}")


def check_brief(initiative: Path, report: Report, not_applicable: bool) -> str | None:
    brief = initiative / "stakeholder-brief.html"
    state_path = initiative / "run-state.yaml"
    state = state_path.read_text(encoding="utf-8") if state_path.is_file() else ""
    phase = yaml_scalar(state, "brief_phase") if state else None
    if not brief.is_file():
        if phase in {"authored", "rendered", "reviewed", "approved"}:
            report.structural.append(
                f"run-state brief_phase '{phase}' requires stakeholder-brief.html"
            )
        if not not_applicable:
            report.structural.append("missing stakeholder brief: stakeholder-brief.html")
        return None
    if phase is not None and phase not in {"rendered", "reviewed", "approved"}:
        report.structural.append(
            "stakeholder-brief.html exists before run-state brief_phase is rendered"
        )
    html = brief.read_text(encoding="utf-8")
    lineage = brief_lineage(html)
    if lineage is None:
        report.structural.append("missing stakeholder brief design-lineage marker: data-harness-brief-design=\"v1\" or \"v2\"")
        return None
    for section_id in (V2_REQUIRED_SECTION_IDS if lineage == "v2" else V1_REQUIRED_SECTION_IDS):
        if not re.search(rf'\bid\s*=\s*["\']{re.escape(section_id)}["\']', html):
            report.structural.append(f"missing stakeholder brief section id: {section_id}")
    if lineage == "v1":
        for source in V1_REQUIRED_SOURCES:
            if not re.search(rf'href\s*=\s*["\']{re.escape(source)}["\']', html):
                report.structural.append(f"missing stakeholder brief source link: {source}")
    for placeholder in PLACEHOLDERS:
        if placeholder in html:
            report.structural.append(f"unresolved stakeholder brief placeholder: {placeholder}")
    design_errors: list[str] = []
    for hook in REQUIRED_SHELL_HOOKS:
        if not re.search(rf'\bclass\s*=\s*["\'][^"\']*\b{re.escape(hook)}\b', html):
            design_errors.append(f"missing stakeholder brief canonical shell hook: {hook}")
    if design_errors:
        if approved_design_exception(initiative, report):
            report.limitations.append("custom stakeholder brief layout accepted by reviewed design exception in decision-log.md; independent rendered review must confirm retained decision surfaces")
        else:
            report.structural.extend(design_errors)
    if lineage == "v2":
        if phase is None:
            report.structural.append("v2 stakeholder brief requires run-state brief_phase")
        if re.search(r'\bdata-brief-phase\s*=\s*["\']scaffold["\']', html):
            report.gate.append("scaffolded v2 stakeholder brief cannot cross Human Visibility; author and render the source-backed brief first")
        if "data-lifecycle-marker" in html:
            lifecycle_failure = lifecycle_error(
                html, state, initiative, allow_rendered_state_snapshot=True,
            )
            if lifecycle_failure:
                report.structural.append("rendered lifecycle does not bind current run-state: " + lifecycle_failure)
        check_v2_provenance(html, report, initiative)
    return lineage


def check_reviewed_editorial_exceptions(initiative: Path, report: Report) -> None:
    """Keep a rendered exception visible without mistaking it for a gate pass."""
    brief = initiative / "stakeholder-brief.html"
    state_path = initiative / "run-state.yaml"
    if not brief.is_file() or not state_path.is_file():
        return
    html = brief.read_text(encoding="utf-8")
    if not re.search(r'''(?is)<html\b[^>]*\bdata-composition-contract\s*=\s*["']v3["']''', html):
        return
    state = state_path.read_text(encoding="utf-8")
    record_ref = yaml_scalar(state, "review_record", indent=2)
    record = None
    if record_ref and record_ref.startswith("decision-log.md#"):
        record = decision_record(initiative / "decision-log.md", record_ref.partition("#")[2])
    findings = composition_editorial_findings(initiative, html)
    error = reviewed_editorial_exception_error(html, record or "", findings, True)
    if error:
        report.structural.append("invalid reviewed editorial exception: " + error)
        return
    identifiers = sorted(set(re.findall(r'''\bdata-composition-exception-id\s*=\s*["']([^"']+)["']''', html)))
    if not identifiers:
        return
    report.editorial_exceptions.append(
        "Open reviewed editorial exception(s) in rendered brief: " + ", ".join(identifiers)
        + ". They are visible decision debt, not Human Visibility or Tasks Ready approval."
    )
    if yaml_bool(state, "human_visibility_ready") or yaml_bool(state, "tasks_ready"):
        report.gate.append("open reviewed editorial exceptions require Human Visibility and Tasks Ready to remain false")


def changed_paths_from_git(root: Path, base_ref: str, initiative: Path) -> tuple[set[str] | None, str | None]:
    relative = initiative.relative_to(root).as_posix()
    result = subprocess.run(
        ["git", "-C", str(root), "diff", "--name-only", base_ref, "--", relative],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        return None, result.stderr.strip() or "git diff failed"
    prefix = relative + "/"
    return {path[len(prefix):] for path in result.stdout.splitlines() if path.startswith(prefix)}, None


def check_baseline_freshness(sources: dict[str, Path], initiative: Path, report: Report, exception_scope: str | None, lineage: str) -> None:
    baseline_path = initiative / BASELINE_FILE
    if not baseline_path.is_file():
        if exception_scope == "freshness":
            report.limitations.append("freshness baseline absent; explicit reviewed freshness exception accepted")
        else:
            report.freshness.append(
                f"missing freshness baseline: {BASELINE_FILE}; run with --write-baseline after independent review or record a reviewed freshness exception"
            )
        return
    baseline = load_json(baseline_path, report, "freshness baseline")
    if baseline is None:
        return
    expected_schema = 2 if lineage == "v2" else 1
    if baseline.get("schema_version") != expected_schema:
        if lineage == "v2":
            report.freshness.append(
                "v2 migration required: freshness baseline must use schema_version 2; run --write-baseline after independent review"
            )
        else:
            report.freshness.append("invalid v1 freshness baseline: human-visibility-baseline.json must use schema_version 1")
        return
    if lineage == "v2":
        if baseline.get("brief_lineage") != "v2":
            report.freshness.append("v2 migration required: freshness baseline lacks brief_lineage v2 metadata")
            return
        if baseline.get("source_set") != list(V2_REQUIRED_SOURCES):
            report.freshness.append("v2 migration required: freshness baseline lacks the expanded v2 source_set metadata")
            return
        state = (initiative / "run-state.yaml").read_text(encoding="utf-8")
        expected_metadata = baseline_metadata(state)
        for key, value in expected_metadata.items():
            if not value or baseline.get(key) != value:
                report.freshness.append(f"v2 freshness baseline metadata changed or missing: {key}; rerun --write-baseline after review")
                return
        prior_anchor = str(baseline["prior_change_anchor"])
        if not prior_anchor.startswith("decision-log.md#") or decision_record(
            initiative / "decision-log.md", prior_anchor.partition("#")[2]
        ) is None:
            report.freshness.append("v2 freshness baseline has an invalid prior_change_anchor")
            return
        if baseline.get("brief_sha256") != digest(initiative / "stakeholder-brief.html"):
            report.freshness.append("v2 stakeholder brief changed since the reviewed baseline; rerun independent review and --write-baseline")
            return
    recorded = baseline.get("source_sha256")
    if not isinstance(recorded, dict):
        report.freshness.append(f"invalid freshness baseline: {BASELINE_FILE} lacks source_sha256")
        return
    changed = [name for name, path in sources.items() if recorded.get(name) != digest(path)]
    if changed:
        if exception_scope == "freshness" or (lineage == "v1" and exception_scope == "legacy"):
            report.limitations.append("changed source artifact(s) accepted by explicit reviewed freshness exception: " + ", ".join(changed))
        else:
            if lineage == "v1":
                report.freshness.append(
                    "historical/pinned v1 stakeholder brief is stale for changed source artifact(s): "
                    + ", ".join(changed)
                    + "; migrate to v2 or record a reviewed legacy exception"
                )
            else:
                report.freshness.append("v2 stakeholder brief is stale for changed source artifact(s): " + ", ".join(changed))


def check_freshness(initiative: Path, root: Path, base_ref: str | None, report: Report, exception_scope: str | None, lineage: str) -> None:
    sources = {name: initiative / name for name in required_sources(lineage)}
    for name, path in sources.items():
        if not path.is_file():
            report.structural.append(f"missing required source artifact: {name}")
    if report.structural:
        return
    if base_ref:
        changed, error = changed_paths_from_git(root, base_ref, initiative)
        if changed is None:
            report.limitations.append(
                f"cannot compare freshness against Git base ref {base_ref!r}; falling back to {BASELINE_FILE}: {error}"
            )
            check_baseline_freshness(sources, initiative, report, exception_scope, lineage)
            return
        changed_sources = sorted(set(sources) & changed)
        if changed_sources and "stakeholder-brief.html" not in changed:
            if exception_scope == "freshness" or (lineage == "v1" and exception_scope == "legacy"):
                report.limitations.append("Git freshness failure accepted by explicit reviewed freshness exception: " + ", ".join(changed_sources))
            else:
                if lineage == "v1":
                    report.freshness.append(
                        "historical/pinned v1 stakeholder brief was not refreshed in Git diff after changed source artifact(s): "
                        + ", ".join(changed_sources)
                        + "; migrate to v2 or record a reviewed legacy exception"
                    )
                else:
                    report.freshness.append("v2 stakeholder brief was not refreshed in Git diff after changed source artifact(s): " + ", ".join(changed_sources))
        return
    check_baseline_freshness(sources, initiative, report, exception_scope, lineage)


def write_baseline(initiative: Path, root: Path) -> None:
    brief = initiative / "stakeholder-brief.html"
    if not brief.is_file():
        raise ValueError("cannot write freshness baseline; missing stakeholder brief: stakeholder-brief.html")
    lineage = brief_lineage(brief.read_text(encoding="utf-8"))
    if lineage is None:
        raise ValueError("cannot write freshness baseline; missing stakeholder brief design-lineage marker")
    sources = required_sources(lineage)
    missing = [name for name in sources if not (initiative / name).is_file()]
    if missing:
        raise ValueError("cannot write freshness baseline; missing source artifact(s): " + ", ".join(missing))
    report = validate(initiative, root, None, skip_freshness=True)
    if report.structural or report.gate:
        failures = report.structural + report.gate
        raise ValueError("deterministic structure/gate must pass before writing baseline: " + "; ".join(failures))
    payload: dict[str, object] = {
        "schema_version": 1 if lineage == "v1" else 2,
        "source_sha256": {name: digest(initiative / name) for name in sources},
    }
    if lineage == "v2":
        state = (initiative / "run-state.yaml").read_text(encoding="utf-8")
        payload.update({
            "brief_lineage": "v2",
            "source_set": list(V2_REQUIRED_SOURCES),
            "brief_sha256": digest(brief),
            **baseline_metadata(state),
        })
    (initiative / BASELINE_FILE).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def validate(initiative: Path, root: Path, base_ref: str | None, *, skip_freshness: bool = False) -> Report:
    report = Report()
    if not initiative.is_dir():
        report.structural.append(f"initiative path does not exist: {initiative}")
        return report
    exception_scope = approved_exception(initiative, report)
    check_gate_state(initiative, report)
    lineage = check_brief(initiative, report, exception_scope == "not_applicable")
    if lineage == "v2":
        check_v2_gate_state(initiative, report)
        check_v2_evidence_references(initiative, report)
        check_v2_projection(initiative, report)
    check_reviewed_editorial_exceptions(initiative, report)
    if not skip_freshness and exception_scope != "not_applicable":
        if lineage is not None:
            check_freshness(initiative, root, base_ref, report, exception_scope, lineage)
    elif exception_scope == "not_applicable":
        report.limitations.append("stakeholder brief structural/freshness checks are not applicable under the explicit reviewed exception")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--consumer-root", type=Path, required=True)
    parser.add_argument("--initiative", required=True, help="Path relative to consumer root, e.g. specs/004-example")
    parser.add_argument("--base-ref", help="Compare source/brief changes against this Git ref; use the local baseline if Git/ref comparison is unavailable")
    parser.add_argument("--write-baseline", action="store_true", help="Write local source hashes after the required independent review")
    args = parser.parse_args()
    root = args.consumer_root.resolve()
    initiative = (root / args.initiative).resolve()
    try:
        initiative.relative_to(root)
    except ValueError:
        parser.error("--initiative must resolve inside --consumer-root")
    if args.write_baseline:
        try:
            write_baseline(initiative, root)
        except ValueError as error:
            print(f"Human Visibility validation FAILED: {error}")
            return 1
        print(f"Wrote freshness baseline: {initiative / BASELINE_FILE}")
        return 0
    report = validate(initiative, root, args.base_ref)
    print("Human Visibility deterministic design-contract validation")
    for label, entries in (("STRUCTURAL FAILURES", report.structural), ("GATE/STATE INCONSISTENCIES", report.gate), ("FRESHNESS FAILURES", report.freshness), ("EDITORIAL EXCEPTIONS (VISIBLE, NOT A GATE PASS)", report.editorial_exceptions), ("LIMITATIONS", report.limitations), ("HUMAN REVIEW REQUIRED", report.human_review)):
        print(f"\n{label}:")
        for entry in entries or ("none",):
            print(f"- {entry}")
    if report.failures:
        print(f"\nRESULT: FAIL ({len(report.failures)} deterministic failure(s))")
        return 1
    print("\nRESULT: PASS (deterministic design/structure contract only; independent review still required)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
