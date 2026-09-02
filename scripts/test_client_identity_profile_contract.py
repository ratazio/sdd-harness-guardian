#!/usr/bin/env python3
"""Deterministic checks for vendor-neutral default and opt-in Pearson identity."""

import hashlib
import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'data-client-identity-profile="pearson"'
NEUTRAL_PROFILE = 'data-client-identity-profile="vendor-neutral"'
LOGO_PATH = "../../.harness/assets/brand/pearson-logo-white.png"


def required_text(path: Path, snippets: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [snippet for snippet in snippets if snippet not in text]


def main() -> int:
    failures: list[str] = []
    plan_template = ROOT / ".harness" / "templates" / "plan.md"
    readme = ROOT / ".harness" / "templates" / "README.md"
    design = ROOT / ".harness" / "templates" / "stakeholder-brief-design.md"
    brief_template = ROOT / ".harness" / "templates" / "stakeholder-brief.html"
    logo = ROOT / ".harness" / "assets" / "brand" / "pearson-logo-white.png"

    for path, snippets in (
        (
            plan_template,
            [
                "Client visual profile selection (conditional)",
                PROFILE,
                "vendor-neutral",
                "Only when the rendered HTML explicitly selects `pearson`",
            ],
        ),
        (
            readme,
            [
                "vendor-neutral by default",
                PROFILE,
                "Opt-in Pearson visual profile",
                "does not copy or reference the Pearson asset",
            ],
        ),
        (
            design,
            [
                PROFILE,
                "explicit opt-in",
                "official local white logo is an actual image inside a named native link",
                "320px/768px/1024px/1440px",
            ],
        ),
        (
            brief_template,
            [
                NEUTRAL_PROFILE,
                "data-harness-brief-shell",
                "prefers-reduced-motion:reduce",
                ".brief-architecture-cut",
                ".brief-impact-footprint",
                ".brief-risk-chain",
                ".brief-proof-card",
                ".brief-decision-call",
                ".brief-coverage-group",
            ],
        ),
    ):
        for missing in required_text(path, snippets):
            failures.append(f"{path.relative_to(ROOT)} missing: {missing}")

    if not logo.exists():
        failures.append("official local Pearson logo is missing")
    else:
        data = logo.read_bytes()
        if hashlib.sha256(data).hexdigest().upper() != "8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7":
            failures.append("official local Pearson logo checksum changed")
        if data[:8] != b"\x89PNG\r\n\x1a\n":
            failures.append("official local Pearson logo is not a PNG")
        elif struct.unpack(">II", data[16:24]) != (175, 53):
            failures.append("official local Pearson logo dimensions are not 175x53")

    template_text = brief_template.read_text(encoding="utf-8")
    if "http://" in template_text or "https://" in template_text:
        failures.append("canonical vendor-neutral template must not hotlink assets or fonts")
    for pearson_reference in (
        PROFILE,
        LOGO_PATH,
        "brief-client-logo",
        "data-harness-pearson-shell",
    ):
        if pearson_reference in template_text:
            failures.append(f"canonical vendor-neutral template retained Pearson reference: {pearson_reference}")
    if template_text.count(NEUTRAL_PROFILE) != 1:
        failures.append("canonical root must contain exactly one vendor-neutral identity marker")

    if failures:
        print("Client identity profile contract: FAIL")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("Client identity profile contract: PASS (vendor-neutral default; Pearson remains explicit and local)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
