#!/usr/bin/env python3
"""Deterministic contracts for the opt-in Pearson stakeholder brief profile.

This module validates source-level identity and accessibility invariants. It
does not judge wording, architecture depth, palette fidelity, number of tabs or
number of sections; those remain source-driven and independently reviewed.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'data-client-identity-profile="pearson"'
LOGO_PATH = "../../.harness/assets/brand/pearson-logo-white.png"
GUIDE_PATH = ".harness/references/pearson-design.md"
EXCEPTION_META = "harness-pearson-layout-exception"
LEGACY_META = "harness-pearson-exception"
REQUIRED_EXCEPTION_FIELDS = (
    "decision",
    "owner",
    "reason",
    "retained",
    "review",
    "re-review",
)


class LogoParser(HTMLParser):
    """Collect only logo-link semantics; never include source body in errors."""

    def __init__(self) -> None:
        super().__init__()
        self._logo_anchor: dict[str, str] | None = None
        self.logo_anchors: list[dict[str, str]] = []
        self.logo_images: list[dict[str, str]] = []
        self.styles: list[dict[str, str]] = []
        self.bodies: list[dict[str, str]] = []
        self.headers: list[dict[str, str]] = []
        self.metas: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        if tag == "meta" and values.get("name"):
            self.metas[values["name"]] = values.get("content", "")
        if tag == "style":
            self.styles.append(values)
        if tag == "body":
            self.bodies.append(values)
        if tag == "header" and "brief-header" in values.get("class", "").split():
            self.headers.append(values)
        if tag == "a" and "brief-client-logo" in values.get("class", "").split():
            self._logo_anchor = values
            self.logo_anchors.append(values)
        if tag == "img" and self._logo_anchor is not None:
            self.logo_images.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a":
            self._logo_anchor = None


def metadata_fields(content: str) -> dict[str, str]:
    return {
        key.strip(): value.strip()
        for part in content.split(";")
        if "=" in part
        for key, value in [part.split("=", 1)]
        if key.strip() and value.strip()
    }


def has_complete_exception(content: str) -> bool:
    fields = metadata_fields(content)
    if not all(fields.get(field) for field in REQUIRED_EXCEPTION_FIELDS):
        return False
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields["re-review"]))


def has_dated_legacy_exception(content: str) -> bool:
    fields = metadata_fields(content)
    return (
        fields.get("classification") == "historical/legacy"
        and bool(fields.get("decision"))
        and bool(fields.get("owner"))
        and bool(fields.get("reason"))
        and bool(fields.get("retained"))
        and bool(fields.get("review"))
        and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields.get("re-review", "")))
    )


def policy_errors(html: str, *, root: Path = ROOT, post_cutover: bool = True) -> list[str]:
    """Return stable repair-oriented errors without leaking document body text."""

    parser = LogoParser()
    parser.feed(html)
    errors: list[str] = []
    legacy_exception = parser.metas.get(LEGACY_META, "")
    legacy_allowed = has_dated_legacy_exception(legacy_exception)

    profile_match = re.search(
        r'\bdata-client-identity-profile\s*=\s*["\']([^"\']*)["\']',
        html,
    )
    profile = profile_match.group(1) if profile_match else ""
    if legacy_exception and not legacy_allowed:
        errors.append(
            "historical/legacy Pearson exception must record classification, decision, owner, "
            "reason, retained surfaces, review outcome and ISO re-review date"
        )

    if legacy_allowed:
        return errors

    if profile in {"", "vendor-neutral"}:
        # A neutral brief is the default.  It must not become a disguised
        # Pearson delivery through a copied logo, profile shell or exception
        # metadata; its visual and narrative adequacy still receive human
        # review, not a deterministic prose score.
        pearson_references = (
            "pearson-logo-white.png",
            "brief-client-logo",
            "data-harness-pearson-shell",
            EXCEPTION_META,
            LEGACY_META,
        )
        for reference in pearson_references:
            if reference in html:
                errors.append(
                    "vendor-neutral brief must not load, copy or reference Pearson identity assets or shell hooks"
                )
                break
        return errors

    if profile != "pearson":
        errors.append(
            'data-client-identity-profile must be "vendor-neutral" (or absent) or "pearson"'
        )
        return errors

    if not (root / GUIDE_PATH).is_file():
        errors.append(f"missing local Pearson design authority: {GUIDE_PATH}")

    shell_styles = [
        attrs for attrs in parser.styles
        if "data-harness-pearson-shell" in attrs
    ]
    override_styles = [
        attrs for attrs in parser.styles
        if "data-harness-visual-override" in attrs
    ]
    unmarked_styles = [
        attrs for attrs in parser.styles
        if "data-harness-pearson-shell" not in attrs
        and "data-harness-visual-override" not in attrs
    ]
    if len(shell_styles) != 1:
        errors.append(
            "canonical Pearson shell must declare exactly one data-harness-pearson-shell style; "
            "do not inject or reconstruct a second base"
        )
    if unmarked_styles:
        errors.append(
            "material style injection must declare data-harness-visual-override and documented exception metadata"
        )
    if len(parser.bodies) != 1 or "brief-shell" not in parser.bodies[0].get("class", "").split():
        errors.append("canonical Pearson shell must retain the body brief-shell semantic hook")
    if len(parser.headers) != 1:
        errors.append("canonical Pearson shell must retain exactly one brief-header semantic hook")

    if re.search(r'<(?:img|source)\b[^>]*\bsrc\s*=\s*["\']https?://', html, re.I):
        errors.append("Pearson logo/brand asset must use the approved local path; remote asset URLs are prohibited")
    if re.search(r'@import\s+url\(\s*["\']?https?://|url\(\s*["\']?https?://', html, re.I):
        errors.append("Pearson shell must not fetch remote font or stylesheet assets")
    if re.search(r"filter\s*:", html, re.I):
        errors.append("Pearson logo treatment must not use a CSS filter")

    if len(parser.logo_anchors) != 1:
        errors.append("Pearson shell must contain exactly one named native logo anchor")
    else:
        anchor = parser.logo_anchors[0]
        if not anchor.get("aria-label", "").strip():
            errors.append("Pearson logo anchor needs an accessible name")
        if anchor.get("role") == "img":
            errors.append('Pearson logo anchor must not use role="img"')

    if len(parser.logo_images) != 1:
        errors.append("Pearson logo anchor must contain exactly one local logo image")
    else:
        image = parser.logo_images[0]
        if image.get("src") != LOGO_PATH:
            errors.append(f"Pearson logo image must use {LOGO_PATH}")
        if image.get("width") != "175" or image.get("height") != "53":
            errors.append("Pearson logo image must retain 175x53 intrinsic dimensions")
        if image.get("alt") != "":
            errors.append("Pearson logo image must use empty alt inside its named anchor")

    selector_overlay = re.search(
        r'html\s*(?:\[data-client-identity-profile\s*=\s*["\']pearson["\']\]|:not\s*\()',
        html,
        re.I,
    )
    shell_tokens = (
        ":root",
        "--navy",
        "--lavender",
        ".brief-client-logo",
        "prefers-reduced-motion",
    )
    if selector_overlay:
        errors.append("selected Pearson shell must be a base, not a profile selector overlay")
    if not all(token in html for token in shell_tokens):
        errors.append(
            "canonical Pearson shell lacks required base identity/accessibility hooks; "
            "start from the canonical template instead of reconstructing generic CSS"
        )

    if override_styles:
        if not has_complete_exception(parser.metas.get(EXCEPTION_META, "")):
            errors.append(
                "material visual override requires documented Pearson exception metadata: "
                "decision, owner, reason, retained surfaces, review outcome and ISO re-review date"
            )
    return errors


def canonical_template_errors(root: Path = ROOT) -> list[str]:
    """Check that the canonical scaffold stays vendor-neutral.

    Pearson is validated only when an authored candidate explicitly selects it.
    """
    template = root / ".harness" / "templates" / "stakeholder-brief.html"
    return policy_errors(template.read_text(encoding="utf-8"), root=root)


if __name__ == "__main__":
    errors = canonical_template_errors()
    if errors:
        print("Pearson brief policy: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        raise SystemExit(1)
    print("Pearson brief policy: PASS")
