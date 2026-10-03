#!/usr/bin/env python3
"""Mechanical helpers for direct-authored contract 3 briefs (standard library).

These checks do not judge coverage, execute repair skills, or grant authority.
The bounded YAML reader handles only the documented brief_repair mapping;
unrelated consumer YAML is preserved byte-for-byte by the writer.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime

ROUTES = ("scope", "architecture", "impact", "execution", "validation", "evolution", "decision", "coverage")
CORE_MD = ("spec.md", "impact-map.md", "plan.md", "tasks.md", "validation-plan.md", "decision-log.md", "progress.md")
COMPLETED = {"completed", "completed_with_source_limitations"}
STATUSES = COMPLETED | {"incomplete"}
EFFORTS = {"high", "xhigh", "max", "ultra"}
REPAIR_BLOCK = re.compile(r"(?m)^brief_repair:[ \t]*(?:#.*)?\r?\n(?:^(?:[ \t]+[^\r\n]*|[ \t]*)\r?\n?)*")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _scalar(value: str):
    value = value.strip()
    if not value or value == "{}":
        return {}
    if value in {"null", "~"}:
        return None
    if value.startswith('"'):
        try:
            result = json.loads(value)
        except json.JSONDecodeError as error:
            raise ValueError("brief_repair quoted scalar must be a single JSON-compatible YAML string") from error
        if not isinstance(result, str):
            raise ValueError("brief_repair scalar must be a string")
        return result
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    value = value.split(" #", 1)[0].strip()
    if value[:1] in {"[", "{", "|", ">", "&", "*", "!"}:
        raise ValueError("brief_repair supports only nested mappings and single-line scalar strings")
    return value


def repair_metadata(state: str) -> dict:
    """Read the documented mapping, without parsing unrelated consumer state."""
    matches = list(REPAIR_BLOCK.finditer(state))
    if len(matches) != 1:
        raise ValueError("run-state requires exactly one brief_repair mapping for contract 3")
    result: dict = {}
    stack: list[tuple[int, dict]] = [(0, result)]
    for line in matches[0].group().splitlines()[1:]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"( +)([^:]+):(?:[ \t]*(.*))?", line)
        if not match or len(match[1]) % 2:
            raise ValueError("brief_repair requires two-space mapping indentation")
        indent, key = len(match[1]), match[2].strip().strip('"\'')
        while stack[-1][0] >= indent:
            stack.pop()
        if stack[-1][0] != indent - 2:
            raise ValueError("brief_repair mapping indentation skips a level")
        parent = stack[-1][1]
        if key in parent:
            raise ValueError("brief_repair contains a duplicate field")
        value = _scalar(match[3] or "")
        parent[key] = value
        if isinstance(value, dict):
            stack.append((indent, value))
    return result


def write_repair_metadata(state: str, metadata: dict) -> str:
    def lines(mapping: dict, indent: int) -> list[str]:
        result = []
        for key, value in mapping.items():
            if not re.fullmatch(r"[A-Za-z0-9_./-]+", key):
                raise ValueError("brief_repair field/path is outside the portable mapping grammar")
            prefix = " " * indent + key + ":"
            if isinstance(value, dict) and value:
                result.extend([prefix, *lines(value, indent + 2)])
            else:
                rendered = "{}" if isinstance(value, dict) else json.dumps(value, ensure_ascii=False)
                result.append(prefix + " " + rendered)
        return result
    newline = "\r\n" if "\r\n" in state else "\n"
    block = newline.join(["brief_repair:", *lines(metadata, 2)]) + newline
    matches = list(REPAIR_BLOCK.finditer(state))
    if len(matches) > 1:
        raise ValueError("run-state contains duplicate brief_repair mappings")
    if matches:
        match = matches[0]
        return state[:match.start()] + block + state[match.end():]
    return state.rstrip("\r\n") + newline + block


def source_path(initiative: Path, name: str) -> Path:
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_./-]+\.md", name) or ".." in Path(name).parts:
        raise ValueError("source_snapshot requires safe initiative-relative Markdown paths")
    path = initiative / name
    try:
        path.resolve().relative_to(initiative.resolve())
    except ValueError as error:
        raise ValueError("source_snapshot path escapes the initiative") from error
    if any(part.is_symlink() for part in [path, *path.parents] if part != initiative.parent):
        raise ValueError("source_snapshot does not follow symlinks")
    if not path.is_file():
        raise ValueError("source_snapshot Markdown artifact is missing: " + name)
    return path


@dataclass
class Node:
    tag: str
    attrs: dict[str, str]
    parent: int | None
    index: int
    text: list[str] = field(default_factory=list)
    direct_text: list[str] = field(default_factory=list)


class Brief3Parser(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes: list[Node] = []
        self.stack: list[int] = []
        self.closed = False
        self.tail = False
        self.styles: list[str] = []

    def handle_starttag(self, tag, attrs):
        if self.closed:
            self.tail = True
        values = {key: value or "" for key, value in attrs}
        index = len(self.nodes)
        self.nodes.append(Node(tag, values, self.stack[-1] if self.stack else None, index))
        if tag not in self.VOID:
            self.stack.append(index)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        for position in range(len(self.stack) - 1, -1, -1):
            if self.nodes[self.stack[position]].tag == tag:
                if tag == "style":
                    self.styles.append("".join(self.nodes[self.stack[position]].text))
                del self.stack[position:]
                break
        if tag == "html":
            self.closed = True

    def handle_data(self, data):
        if self.closed and data.strip():
            self.tail = True
        for index in self.stack:
            self.nodes[index].text.append(data)
        if self.stack:
            self.nodes[self.stack[-1]].direct_text.append(data)

    def descendants(self, ancestor: Node):
        index = ancestor.index
        result = []
        for node in self.nodes:
            parent = node.parent
            while parent is not None:
                if parent == index:
                    result.append(node)
                    break
                parent = self.nodes[parent].parent
        return result

    def visible(self, node):
        parent = node.parent
        while parent is not None:
            if self.nodes[parent].tag in {"script", "style", "template", "code", "pre"}:
                return False
            parent = self.nodes[parent].parent
        return node.tag not in {"script", "style", "template", "code", "pre"}


def _text(node: Node) -> str:
    return " ".join("".join(node.text).split())


def structural_errors(html: str, *, rendered: bool) -> list[str]:
    """Check static structure only; browser/repair supplies visual and meaning proof."""
    parser = Brief3Parser()
    parser.feed(html)
    nodes = [node for node in parser.nodes if parser.visible(node)]
    errors = []
    ids = [node.attrs["id"] for node in nodes if node.attrs.get("id")]
    if len(ids) != len(set(ids)):
        errors.append("v3 rendered HTML ids must be unique")
    if parser.tail:
        errors.append("v3 content appears after terminal </html>")
    root = next((node for node in nodes if node.tag == "html"), None)
    if root is None or root.attrs.get("data-brief-contract") != "3":
        errors.append('v3 brief requires data-brief-contract="3" on html')
    if rendered and root and (root.attrs.get("data-harness-template-kind") == "scaffold" or root.attrs.get("data-brief-phase") == "scaffold"):
        errors.append("v3 scaffold must be authored before materialization")
    for hook in ("brief-shell", "brief-header"):
        if not any(hook in node.attrs.get("class", "").split() for node in nodes):
            errors.append("missing stakeholder brief canonical shell hook: " + hook)
    controls = [node for node in nodes if node.tag == "input" and node.attrs.get("name") == "brief-view"]
    if len(controls) != 8 or sum("checked" in node.attrs for node in controls) != 1:
        errors.append("v3 requires eight brief-view radios and exactly one initially checked control")
    css = re.sub(r"/\*.*?\*/", "", "\n".join(parser.styles), flags=re.S)
    css = re.sub(r"\s+", "", css)
    if ".route-panels>.tab-panel{display:none" not in css:
        errors.append("v3 screen CSS must hide inactive route panels")
    for route in ROUTES:
        control = [node for node in controls if node.attrs.get("id") == "view-" + route]
        labels = [node for node in nodes if node.tag == "label" and node.attrs.get("id") == "tab-" + route and node.attrs.get("for") == "view-" + route]
        panels = [node for node in nodes if node.attrs.get("id") == route and "tab-panel" in node.attrs.get("class", "").split()]
        if len(control) != 1 or control[0].attrs.get("type") != "radio" or control[0].attrs.get("aria-controls") != route:
            errors.append("v3 missing native radio/panel binding: " + route)
        if len(labels) != 1 or not _text(labels[0]):
            errors.append("v3 missing labeled native control: " + route)
        if len(panels) != 1 or panels[0].attrs.get("aria-labelledby") != "tab-" + route:
            errors.append("v3 missing route panel/label binding: " + route)
        if f"#view-{route}:checked~.route-panels>#{route}" not in css:
            errors.append("v3 missing native screen selection rule: " + route)
    if "@mediaprint" not in css:
        errors.append("v3 requires a print stylesheet")
    # Display dependencies differ from ordinary links to canonical source files.
    for node in parser.nodes:
        attrs = node.attrs
        for attr in ("src", "srcset", "poster", "data" if node.tag == "object" else ""):
            if attr and attrs.get(attr) and not attrs[attr].startswith("data:"):
                errors.append("v3 display resources must be embedded inline")
        if node.tag == "link" and attrs.get("rel") in {"stylesheet", "preload", "modulepreload"}:
            errors.append("v3 must not depend on linked display resources")
        if node.tag in {"iframe", "object", "embed", "base"}:
            errors.append("v3 must not embed active external documents")
        if node.tag in {"use", "image"}:
            value = attrs.get("href", attrs.get("xlink:href", ""))
            if value and not value.startswith(("#", "data:")):
                errors.append("v3 SVG resources must be inline")
        if node.tag == "script" and re.search(r"\b(?:import\s*\(|fetch\s*\(|XMLHttpRequest|WebSocket\s*\()", _text(node)):
            errors.append("v3 script must not require network resources")
        style = attrs.get("style", "")
        if node.tag == "style":
            style += "".join(node.text)
        if re.search(r"@import\b|url\(\s*['\"]?(?!data:|#)[^\s)'\"]", style, re.I):
            errors.append("v3 CSS display resources must be inline")
    if rendered:
        for node in nodes:
            # Instruction comments and legitimate literal syntax in code are not
            # unfilled editorial fields; inspect direct visible text only.
            direct = "".join(node.direct_text)
            direct += " ".join(node.attrs.get(attribute, "") for attribute in ("aria-label", "alt", "title"))
            if re.search(r"\{\{[A-Za-z_][A-Za-z0-9_-]*\}\}", direct):
                errors.append("v3 unresolved visible editorial placeholder")
                break
        coverage = next((node for node in nodes if node.attrs.get("id") == "coverage"), None)
        if coverage and not any(node.tag == "table" and "coverage" in node.attrs.get("class", "").split() for node in parser.descendants(coverage)):
            errors.append("v3 coverage requires its human source/fact/target table")
        for node in nodes:
            if node.attrs.get("data-source") and (not node.attrs.get("data-source-section") or node.attrs.get("data-coverage") not in {"represented", "synthesized", "not_applicable", "link_only"}):
                errors.append("v3 declared source block requires source-section and coverage disposition")
        architecture = next((node for node in nodes if node.attrs.get("id") == "architecture"), None)
        if architecture:
            descendants = parser.descendants(architecture)
            declaration = next((node for node in [architecture, *descendants] if node.attrs.get("data-architecture-visual")), architecture)
            mode = declaration.attrs.get("data-architecture-visual")
            if mode == "material":
                svgs = [node for node in descendants if node.tag == "svg" and "data-brief-architecture-diagram" in node.attrs]
                if not svgs or not any(node.attrs.get("role") == "img" and (node.attrs.get("aria-label") or node.attrs.get("aria-labelledby")) for node in svgs):
                    errors.append("v3 material architecture requires accessible inline SVG")
                if not any("diagram-equivalent" in node.attrs.get("class", "").split() and _text(node) for node in descendants):
                    errors.append("v3 material architecture requires a non-empty text equivalent")
                graph = [node for svg in svgs for node in parser.descendants(svg)]
                names = {node.attrs.get("data-architecture-node", "") for node in graph if node.attrs.get("data-architecture-node")}
                edges = [node for node in graph if node.attrs.get("data-architecture-relation")]
                if not edges or any(node.attrs.get("data-from") not in names or node.attrs.get("data-to") not in names or node.attrs.get("data-from") == node.attrs.get("data-to") for node in edges):
                    errors.append("v3 SVG connections must bind named architecture nodes")
                if any(not any(child.tag == "text" and _text(child) for child in parser.descendants(edge)) or not any(child.tag in {"path", "line", "polyline"} for child in parser.descendants(edge)) for edge in edges):
                    errors.append("v3 SVG connections require visible labels and rendered connectors")
            elif mode not in {"not-material", "not_applicable", "discovery"} or not declaration.attrs.get("data-architecture-visual-reason"):
                errors.append("v3 architecture requires material SVG or a grounded non-material reason")
    return list(dict.fromkeys(errors))


def snapshot_errors(initiative: Path, metadata: dict, html: str) -> list[str]:
    errors = []
    snapshot = metadata.get("source_snapshot")
    if not isinstance(snapshot, dict) or not snapshot:
        return ["v3 brief_repair.source_snapshot must record immutable Markdown SHA-256 values"]
    parser = Brief3Parser()
    parser.feed(html)
    declared = {node.attrs.get("data-source") for node in parser.nodes if node.attrs.get("data-source", "").endswith(".md")}
    required = set(CORE_MD) | declared
    for name in sorted(required - snapshot.keys()):
        errors.append("v3 source_snapshot lacks applicable Markdown: " + name)
    for name, recorded in snapshot.items():
        try:
            path = source_path(initiative, name)
            if not isinstance(recorded, str) or not re.fullmatch(r"(?:sha256:)?[0-9a-f]{64}", recorded):
                errors.append("v3 source_snapshot requires SHA-256: " + name)
            elif sha256(path.read_bytes()) != recorded.removeprefix("sha256:"):
                errors.append("v3 Markdown snapshot changed: " + name)
        except ValueError as error:
            errors.append(str(error))
    return errors


def completion_errors(metadata: dict, html: str, *, require_complete: bool = True) -> list[str]:
    errors = []
    if str(metadata.get("contract")) != "3":
        errors.append("v3 brief_repair.contract must be 3")
    author = metadata.get("author")
    if not isinstance(author, str) or not author.strip():
        errors.append("v3 brief_repair.author is required")
    status = metadata.get("status")
    if not isinstance(status, str) or status not in STATUSES:
        errors.append("v3 brief_repair.status is invalid")
    concluded = isinstance(status, str) and status in COMPLETED
    if require_complete and not concluded:
        errors.append("v3 repair remains incomplete; completion is not recorded")
    actors = []
    for name in ("content", "visual"):
        passage = metadata.get(name)
        if not isinstance(passage, dict):
            errors.append("v3 brief_repair lacks " + name + " passage")
            continue
        pass_status = passage.get("status")
        if not isinstance(pass_status, str) or pass_status not in STATUSES:
            errors.append("v3 " + name + " passage status is invalid")
        pass_concluded = isinstance(pass_status, str) and pass_status in COMPLETED
        if concluded and not pass_concluded:
            errors.append("v3 final completion requires completed " + name + " passage")
        if pass_concluded:
            for field in ("actor", "effective_effort", "execution_ref", "completed_at"):
                if not isinstance(passage.get(field), str) or not passage[field].strip():
                    errors.append("v3 completed " + name + " requires " + field)
            effort = passage.get("effective_effort")
            if not isinstance(effort, str) or effort not in EFFORTS:
                errors.append("v3 " + name + " effective_effort must be high/xhigh or explicitly supported superior effort")
            if passage.get("actor") == author:
                errors.append("v3 repair actor must be distinct from author")
            actors.append(passage.get("actor"))
            try:
                datetime.fromisoformat(str(passage.get("completed_at") or "").replace("Z", "+00:00"))
            except ValueError:
                errors.append("v3 " + name + " completed_at requires an ISO date/time")
    if len(actors) == 2 and actors[0] != actors[1]:
        errors.append("v3 content and visual require the same repair actor")
    if concluded and str(metadata.get("rendered_sha256") or "").removeprefix("sha256:") != sha256(html.encode("utf-8")):
        errors.append("v3 rendered_sha256 does not bind the completed HTML")
    return errors


def materialized_state(initiative: Path, state: str, html: str) -> str:
    metadata = repair_metadata(state)
    errors = completion_errors(metadata, html, require_complete=False)
    if not metadata.get("source_snapshot"):
        parser = Brief3Parser()
        parser.feed(html)
        names = set(CORE_MD) | {path.name for path in initiative.glob("*.md")}
        names |= {node.attrs["data-source"] for node in parser.nodes if node.attrs.get("data-source", "").endswith(".md")}
        metadata["source_snapshot"] = {name: sha256(source_path(initiative, name).read_bytes()) for name in sorted(names)}
    errors.extend(snapshot_errors(initiative, metadata, html))
    if errors:
        raise ValueError("; ".join(errors))
    result = write_repair_metadata(state, metadata)
    for field, value in (("brief_phase", "rendered"), ("brief_lineage", "v3")):
        pattern = re.compile(rf"(?m)^{field}:[^\r\n]*")
        if len(pattern.findall(result)) != 1:
            raise ValueError("run-state requires exactly one " + field + " scalar")
        result = pattern.sub(field + ": " + json.dumps(value), result, count=1)
    return result
