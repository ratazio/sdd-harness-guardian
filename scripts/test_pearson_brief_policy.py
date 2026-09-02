#!/usr/bin/env python3
"""Focused fixtures for opt-in Pearson and vendor-neutral brief policy."""

from __future__ import annotations

import tempfile
from pathlib import Path

from validate_pearson_brief_policy import ROOT, canonical_template_errors, policy_errors


FIXTURES = ROOT / "scripts" / "fixtures" / "pearson-brief-policy"


def read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_error(name: str, expected: str) -> None:
    errors = policy_errors(read(name))
    require(
        expected in errors,
        f"{name}: expected {expected!r}, got {errors!r}",
    )


def main() -> int:
    require(not canonical_template_errors(), canonical_template_errors())
    neutral_template = (ROOT / ".harness" / "templates" / "stakeholder-brief.html").read_text(encoding="utf-8")
    require(not policy_errors(neutral_template), "vendor-neutral canonical template failed")
    require(not policy_errors(read("valid-post-cutover.html")), "valid post-cutover fixture failed")
    require(
        not policy_errors(read("documented-override.html")),
        "documented material visual override should be permitted",
    )
    require(
        not policy_errors(read("legacy-exception.html")),
        "dated historical/legacy exception should be permitted",
    )

    require_error(
        "missing-profile.html",
        "vendor-neutral brief must not load, copy or reference Pearson identity assets or shell hooks",
    )
    require_error(
        "non-pearson-profile.html",
        'data-client-identity-profile must be "vendor-neutral" (or absent) or "pearson"',
    )
    require_error(
        "remote-logo.html",
        "Pearson logo/brand asset must use the approved local path; remote asset URLs are prohibited",
    )
    require_error(
        "remote-logo.html",
        "Pearson logo image must use ../../.harness/assets/brand/pearson-logo-white.png",
    )
    require_error("filtered-logo.html", "Pearson logo treatment must not use a CSS filter")
    require_error(
        "wrong-logo.html",
        "Pearson logo image must use ../../.harness/assets/brand/pearson-logo-white.png",
    )
    require_error("unsafe-anchor.html", 'Pearson logo anchor must not use role="img"')
    require_error("unsafe-anchor.html", "Pearson logo anchor needs an accessible name")
    require_error(
        "selector-overlay.html",
        "selected Pearson shell must be a base, not a profile selector overlay",
    )
    require_error(
        "undocumented-override.html",
        "material visual override requires documented Pearson exception metadata: "
        "decision, owner, reason, retained surfaces, review outcome and ISO re-review date",
    )
    require_error(
        "unmarked-material-style-injection.html",
        "material style injection must declare data-harness-visual-override and documented exception metadata",
    )
    require_error(
        "generic-base-reconstruction.html",
        "canonical Pearson shell must declare exactly one data-harness-pearson-shell style; "
        "do not inject or reconstruct a second base",
    )
    require_error(
        "missing-semantic-shell-hooks.html",
        "canonical Pearson shell must retain the body brief-shell semantic hook",
    )
    require_error(
        "missing-semantic-shell-hooks.html",
        "canonical Pearson shell must retain exactly one brief-header semantic hook",
    )
    require_error(
        "invalid-legacy-exception.html",
        "historical/legacy Pearson exception must record classification, decision, owner, "
        "reason, retained surfaces, review outcome and ISO re-review date",
    )

    with tempfile.TemporaryDirectory(prefix="pearson-policy-missing-guide-") as temporary:
        errors = policy_errors(read("valid-post-cutover.html"), root=Path(temporary))
    require(
        f"missing local Pearson design authority: .harness/references/pearson-design.md" in errors,
        errors,
    )

    sentinel = "PRIVATE_SOURCE_BODY_MUST_NOT_LEAK"
    errors = policy_errors(read("missing-profile.html").replace("</body>", sentinel + "</body>"))
    require(sentinel not in "\n".join(errors), errors)

    # This policy deliberately has no section/tab-count condition. A brief can
    # vary content and compose any number of tablists under the v2 DOM contract.
    flexible = read("valid-post-cutover.html")
    require(not policy_errors(flexible), policy_errors(flexible))

    neutral_leak = neutral_template.replace(
        "</body>",
        '<img src="../../.harness/assets/brand/pearson-logo-white.png" alt=""> </body>',
        1,
    )
    require(
        "vendor-neutral brief must not load, copy or reference Pearson identity assets or shell hooks"
        in policy_errors(neutral_leak),
        policy_errors(neutral_leak),
    )

    print("Pearson brief policy fixtures: PASS (vendor-neutral default and explicit Pearson enforcement)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
