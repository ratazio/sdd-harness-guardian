#!/usr/bin/env python3
"""Check that a composed brief retains its approved visual skeleton.

This deliberately narrow guard verifies an authored file is a physical copy of
the local skeleton with changes confined to declared composition slots.  It
does not read Markdown, judge wording, select visuals, or generate HTML.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROUTES = ("scope", "architecture", "impact", "execution", "validation", "evolution", "decision", "coverage")
RAW_SCAFFOLD_TEXT = re.compile(
    r"\ba preencher\b|\bcomposi[çc][ãa]o m-\d{3}\b|\bsource[- ]backed detail\b",
    re.IGNORECASE,
)
# The candidate may assert the record that signed its composition and whether
# that composition is pending/reviewed.  These are candidate lifecycle facts,
# not a structural rewrite of the inherited shell.  The renderer validates them
# against decision-log/run-state before either normal or recovery promotion.
ROOT_MUTABLE_ATTRIBUTES = {
    "data-harness-template-kind",
    "data-brief-phase",
    "data-composition-base",
    "data-composition-base-sha256",
    "data-composition-review-record",
    "data-composition-provenance",
}


def attrs_token(tag: str, attrs: list[tuple[str, str | None]], *, root: bool = False) -> tuple[str, tuple[tuple[str, str], ...]]:
    filtered = ((name, value or "") for name, value in attrs if not (root and name in ROOT_MUTABLE_ATTRIBUTES))
    return tag, tuple(sorted(filtered))


class Surface(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root: dict[str, str] = {}
        self.tabs: list[dict[str, str]] = []
        self.panels: list[dict[str, str]] = []
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.text: list[str] = []
        self.raw_scaffold_outside_slots: list[str] = []
        self.base_styles: list[str] = []
        self.base_scripts: list[str] = []
        self.contract: list[tuple[str, tuple[tuple[str, str], ...]] | tuple[str]] = []
        self.slot_count = 0
        self.contract_version = ""
        self._stack: list[tuple[str, bool, bool]] = []
        self._capture: list[tuple[str, list[str]]] = []

    @staticmethod
    def _is_slot(values: dict[str, str]) -> bool:
        return bool(values.get("data-composition-slot")) or "slot" in values.get("class", "").split()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        if tag == "html":
            self.root = values
            self.contract_version = values.get("data-brief-shell-contract", "")
        if values.get("role") == "tab":
            self.tabs.append(values)
        if values.get("role") == "tabpanel":
            self.panels.append(values)
        if values.get("id"):
            if values["id"] in self.ids:
                self.duplicate_ids.add(values["id"])
            self.ids.add(values["id"])

        parent_opaque = any(item[1] for item in self._stack)
        is_slot = self._is_slot(values)
        if is_slot:
            self.slot_count += 1
        opaque = parent_opaque or is_slot
        if not parent_opaque:
            self.contract.append(attrs_token(tag, attrs, root=tag == "html"))
        self._stack.append((tag, opaque, parent_opaque))
        if values.get("data-brief-base-stylesheet") == "v1":
            self._capture.append(("style", []))
        if values.get("data-brief-base-behavior") == "v1":
            self._capture.append(("script", []))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if not self._stack:
            return
        opened, opaque, parent_opaque = self._stack.pop()
        if opened != tag:
            return
        if not parent_opaque:
            self.contract.append((f"/{tag}",))
        if self._capture and self._capture[-1][0] == tag:
            kind, content = self._capture.pop()
            (self.base_styles if kind == "style" else self.base_scripts).append("".join(content))

    def handle_data(self, data: str) -> None:
        # Slots are structurally opaque, but their rendered text is still
        # candidate-visible and must not retain a raw scaffold marker.
        in_base_code = any(item[0] in {"style", "script"} for item in self._stack)
        if (not in_base_code and not any(item[1] for item in self._stack)
                and RAW_SCAFFOLD_TEXT.search(data)):
            self.raw_scaffold_outside_slots.append(data.strip())
        if not self._capture:
            self.text.append(data)
        if self._capture:
            self._capture[-1][1].append(data)


def read_surface(path: Path) -> Surface:
    surface = Surface()
    surface.feed(path.read_text(encoding="utf-8"))
    surface.close()
    return surface


def digest_blocks(blocks: list[str]) -> str:
    return hashlib.sha256("\0".join(blocks).encode("utf-8")).hexdigest()


def errors(candidate: Path, skeleton: Path, initiative: Path | None = None) -> list[str]:
    candidate_surface = read_surface(candidate)
    skeleton_surface = read_surface(skeleton)
    root = candidate_surface.root
    result: list[str] = []
    expected_hash = hashlib.sha256(skeleton.read_bytes()).hexdigest()
    if root.get("data-harness-template-kind") != "composed":
        result.append('candidate must declare data-harness-template-kind="composed"')
    if root.get("data-brief-phase") != "authored":
        result.append('candidate must declare data-brief-phase="authored"')
    if root.get("data-harness-brief-structure") != "executive-brief-v3":
        result.append("candidate must declare executive-brief-v3")
    if root.get("data-composition-base-sha256") != expected_hash:
        result.append("candidate does not bind the exact approved skeleton SHA-256")
    if initiative is not None:
        declared_base = root.get("data-composition-base", "")
        if not declared_base or (initiative / declared_base).resolve() != skeleton.resolve():
            result.append("candidate must declare its initiative-local skeleton as data-composition-base")

    if not skeleton_surface.contract_version and root.get("data-harness-brief-structure") == "executive-brief-v3":
        result.append(
            "specified v3 skeleton lacks the immutable shell contract; instantiate a new initiative-local skeleton"
        )
    if skeleton_surface.contract_version:
        if root.get("data-brief-shell-contract") != skeleton_surface.contract_version:
            result.append("candidate must retain the skeleton shell contract marker")
        if not skeleton_surface.base_styles or not skeleton_surface.base_scripts:
            result.append("specified skeleton lacks the marked base stylesheet or behavior")
        if digest_blocks(candidate_surface.base_styles) != digest_blocks(skeleton_surface.base_styles):
            result.append("candidate does not retain the exact base stylesheet")
        if digest_blocks(candidate_surface.base_scripts) != digest_blocks(skeleton_surface.base_scripts):
            result.append("candidate does not retain the exact base navigation behavior")
        if candidate_surface.contract != skeleton_surface.contract:
            # A composition slot is intentionally opaque *after* its opening
            # tag.  Its own attributes still identify an immutable anchor in
            # the inherited shell.  The usual accidental violation is putting
            # a source tuple on that anchor instead of on an authored child.
            # Name that recovery path so this guard guides composition rather
            # than looking like a generic bureaucratic refusal.
            mismatch = next(
                (
                    (expected, actual)
                    for expected, actual in zip(
                        skeleton_surface.contract, candidate_surface.contract
                    )
                    if expected != actual
                ),
                None,
            )
            if mismatch:
                expected, actual = mismatch
                expected_attrs = dict(expected[1]) if len(expected) > 1 else {}
                actual_attrs = dict(actual[1]) if len(actual) > 1 else {}
                source_attrs = {
                    "data-source",
                    "data-source-section",
                    "data-coverage",
                    "data-source-digest",
                    "data-source-fragment",
                    "data-source-fragment-sha256",
                }
                if (
                    expected_attrs.get("data-composition-slot")
                    and source_attrs.intersection(actual_attrs).difference(expected_attrs)
                ):
                    result.append(
                        "candidate adds provenance directly to an immutable composition slot; "
                        "retain the slot attributes and place the source-backed block in a child"
                    )
                else:
                    result.append("candidate changed immutable skeleton shell outside declared composition slots")
            else:
                result.append("candidate changed immutable skeleton shell outside declared composition slots")
        if not skeleton_surface.slot_count:
            result.append("specified skeleton exposes no composable slots")
        if skeleton_surface.raw_scaffold_outside_slots:
            marker = RAW_SCAFFOLD_TEXT.search(" ".join(skeleton_surface.raw_scaffold_outside_slots))
            result.append(
                "specified skeleton exposes raw scaffold placeholder outside a composition slot: "
                + repr(marker.group(0) if marker else "placeholder")
            )
    else:
        if len(candidate_surface.tabs) != len(ROUTES) or tuple(tab.get("aria-controls", "") for tab in candidate_surface.tabs) != ROUTES:
            result.append("candidate must retain the eight ordered route tabs")
        if len(candidate_surface.panels) != len(ROUTES) or tuple(panel.get("id", "") for panel in candidate_surface.panels) != ROUTES:
            result.append("candidate must retain the eight ordered route panels")
    if candidate_surface.duplicate_ids:
        result.append("candidate contains duplicate IDs: " + ", ".join(sorted(candidate_surface.duplicate_ids)))
    scaffold_marker = RAW_SCAFFOLD_TEXT.search(" ".join(candidate_surface.text))
    if scaffold_marker:
        result.append(f"candidate still exposes raw scaffold placeholder: {scaffold_marker.group(0)!r}")
    if not set(ROUTES).issubset(skeleton_surface.ids):
        result.append("specified skeleton itself has an invalid route surface")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--skeleton", type=Path, required=True)
    parser.add_argument("--initiative", type=Path, help="initiative root used to verify the declared local base")
    args = parser.parse_args()
    findings = errors(args.candidate.resolve(), args.skeleton.resolve(), args.initiative.resolve() if args.initiative else None)
    if findings:
        print("Candidate inheritance FAILED:", *findings, sep="\n- ", file=sys.stderr)
        return 1
    print("Candidate inheritance passed: v3 skeleton shell retained; semantic quality remains a human review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
