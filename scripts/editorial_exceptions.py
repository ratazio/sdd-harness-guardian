#!/usr/bin/env python3
"""Bounded, review-bound handling of open editorial brief findings.

This module deliberately does not rate prose or decide whether a report is
executive-ready.  It identifies only mechanically recoverable projection
gaps, then verifies that an explicit human decision makes any temporary
exception visible in the exact candidate that was reviewed.
"""

from __future__ import annotations

import re
from datetime import date
from html.parser import HTMLParser
from pathlib import Path


TASK_ID = re.compile(r"\bT-\d{3}\b")
VALIDATION_ID = re.compile(r"\b(?:AC-\d{3}|V-\d{3}(?:-\d{2})?)\b")
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
EXCEPTION_FIELDS = (
    "Finding", "Source", "Target", "Decision impact", "Residual risk",
    "Owner", "Decision", "Expires", "Next action",
)


class _PanelText(HTMLParser):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.identifier = identifier
        self.depth: int | None = None
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if self.depth is None and tag == "section" and values.get("id") == self.identifier:
            self.depth = 1
            return
        if self.depth is not None and tag not in VOID_TAGS:
            self.depth += 1

    def handle_endtag(self, tag: str) -> None:
        if self.depth is not None and tag not in VOID_TAGS:
            self.depth -= 1
            if self.depth == 0:
                self.depth = None

    def handle_data(self, data: str) -> None:
        if self.depth is not None:
            self.parts.append(data)


class _ExceptionMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[tuple[str, dict[str, str], bool]] = []
        self.entries: dict[str, list[str]] = {}
        self.hidden_entries: set[str] = set()
        self._active_ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        inherited_hidden = self.stack[-1][2] if self.stack else False
        style = values.get("style", "").replace(" ", "").lower()
        hidden = inherited_hidden or tag in {"template", "script", "style"} or "hidden" in values or values.get("aria-hidden") == "true" or "display:none" in style or "visibility:hidden" in style
        if tag not in VOID_TAGS:
            self.stack.append((tag, values, hidden))
        identifier = values.get("data-composition-exception-id")
        if identifier:
            in_visible_section = any(item[1].get("id") == "composition-exceptions" and not item[2] for item in self.stack)
            if in_visible_section and not hidden:
                self.entries.setdefault(identifier, [])
                self._active_ids.append(identifier)
            else:
                self.hidden_entries.add(identifier)

    def handle_endtag(self, tag: str) -> None:
        if self.stack and tag not in VOID_TAGS:
            _, values, _ = self.stack.pop()
            identifier = values.get("data-composition-exception-id")
            if identifier and self._active_ids and self._active_ids[-1] == identifier:
                self._active_ids.pop()

    def handle_data(self, data: str) -> None:
        for identifier in self._active_ids:
            self.entries[identifier].append(data)


def _panel_ids(html: str, identifier: str, pattern: re.Pattern[str]) -> set[str]:
    # The v3 contract projects IDs only into the named top-level decision
    # routes.  Limiting the scan to that route prevents a visible exception
    # elsewhere in the document from satisfying its own missing projection.
    match = re.search(rf'''(?is)<section\b[^>]*\bid\s*=\s*["']{re.escape(identifier)}["'][^>]*>(.*?)</section>''', html)
    return set(pattern.findall(match.group(1))) if match else set()


def composition_editorial_findings(initiative: Path, candidate_html: str) -> list[str]:
    """Return only exact source-to-panel omissions and declared empty slots."""
    # This is an additive contract.  Existing v1/v2 candidates retain their
    # established validator surface until a new composition explicitly opts
    # into the handoff/exception protocol.
    root = re.search(r"(?is)<html\b([^>]*)>", candidate_html)
    if not root or not re.search(r'''\bdata-composition-contract\s*=\s*["']v3["']''', root.group(1)):
        return []
    findings: list[str] = []
    tasks_path = initiative / "tasks.md"
    validation_path = initiative / "validation-plan.md"
    if tasks_path.is_file():
        expected = set(TASK_ID.findall(tasks_path.read_text(encoding="utf-8")))
        missing = sorted(expected - _panel_ids(candidate_html, "execution", TASK_ID))
        if missing:
            findings.append("missing task projection: " + ", ".join(missing))
    if validation_path.is_file():
        expected = set(VALIDATION_ID.findall(validation_path.read_text(encoding="utf-8")))
        missing = sorted(expected - _panel_ids(candidate_html, "validation", VALIDATION_ID))
        if missing:
            findings.append("missing validation projection: " + ", ".join(missing))
    for value in re.findall(r'''(?is)data-composition-slot-state\s*=\s*["']([^"']+)["']''', candidate_html):
        if value == "a_preencher":
            findings.append("unresolved composition slot: a_preencher")
            break
    return findings


def _record_field(record: str, name: str) -> str | None:
    match = re.search(rf"(?im)^\s*(?:[-*]\s*)?{re.escape(name)}\s*:\s*(.+?)\s*$", record)
    return match.group(1).strip() if match else None


def _exception_records(decision: str) -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    headings = list(re.finditer(r"(?im)^###\s+Editorial exception\s+([A-Za-z][A-Za-z0-9_-]*)\s*$", decision))
    for index, heading in enumerate(headings):
        content = decision[heading.end() : headings[index + 1].start() if index + 1 < len(headings) else len(decision)]
        records[heading.group(1)] = {
            field: value for field in EXCEPTION_FIELDS
            if (value := _record_field(content, field)) is not None
        }
    return records


def reviewed_editorial_exception_error(
    candidate_html: str, decision: str, findings: list[str], allow: bool,
) -> str | None:
    """Require every bypass to be reviewed, visible, owned and still current."""
    parser = _ExceptionMarkup()
    parser.feed(candidate_html)
    markup = {identifier: " ".join(parts).strip() for identifier, parts in parser.entries.items()}
    records = _exception_records(decision)
    if (findings or markup) and not allow:
        return "editorial findings require a normal correction or --allow-reviewed-editorial-exceptions"
    if not findings and not markup:
        return None
    if not markup:
        return "reviewed editorial exception requires a visible #composition-exceptions entry in the candidate"
    if parser.hidden_entries:
        return "reviewed editorial exception must be rendered visibly, not hidden or inert: " + ", ".join(sorted(parser.hidden_entries))
    if set(markup) != set(records):
        return "visible editorial exception IDs must exactly match the reviewed decision record"
    matched: set[str] = set()
    for identifier, record in records.items():
        missing_fields = [field for field in EXCEPTION_FIELDS if not record.get(field)]
        if missing_fields:
            return f"editorial exception {identifier} is missing reviewed field(s): " + ", ".join(missing_fields)
        if record["Decision"] != "proceed":
            return f"editorial exception {identifier} must declare Decision: proceed exactly"
        try:
            if date.fromisoformat(record["Expires"]) < date.today():
                return f"editorial exception {identifier} is expired"
        except ValueError:
            return f"editorial exception {identifier} must declare Expires as YYYY-MM-DD"
        visible = markup[identifier]
        for field in ("Finding", "Source", "Target", "Decision impact", "Residual risk", "Owner", "Next action"):
            if record[field] not in visible:
                return f"editorial exception {identifier} does not visibly expose reviewed {field.lower()}"
        if record["Finding"] in findings:
            matched.add(record["Finding"])
        else:
            return f"editorial exception {identifier} does not correspond to a current deterministic editorial finding"
    unreviewed = sorted(set(findings) - matched)
    if unreviewed:
        return "deterministic editorial finding(s) lack a reviewed visible exception: " + "; ".join(unreviewed)
    return None
