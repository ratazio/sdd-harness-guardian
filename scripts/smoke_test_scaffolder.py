#!/usr/bin/env python3
"""Reproducible, isolated smoke tests for the initiative scaffolder."""

from __future__ import annotations

import hashlib
import platform
import struct
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

from validate_bundle import stakeholder_brief_errors


ROOT = Path(__file__).resolve().parent.parent
SCAFFOLDER = ROOT / "scripts" / "new_initiative.py"
PEARSON_LOGO = ROOT / ".harness" / "assets" / "brand" / "pearson-logo-white.png"
PEARSON_LOGO_RELATIVE_PATH = Path(".harness/assets/brand/pearson-logo-white.png")
PEARSON_LOGO_SHA256 = "8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7"
FEATURE_FILES = (
    "spec.md",
    "impact-map.md",
    "plan.md",
    "validation-plan.md",
    "tasks.md",
    "run-state.yaml",
    "progress.md",
    "decision-log.md",
    "ratchet.md",
    "handoffs/latest-handoff.md",
)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(SCAFFOLDER), *args]
    print("COMMAND:", " ".join(command))
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    print("EXIT:", result.returncode)
    if result.stdout:
        print("STDOUT:", result.stdout.strip())
    if result.stderr:
        print("STDERR:", result.stderr.strip())
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    require(data[:8] == b"\x89PNG\r\n\x1a\n", f"{path} is not a PNG")
    return struct.unpack(">II", data[16:24])


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_exact_errors(actual: list[str], expected: list[str], case: str) -> None:
    require(actual == expected, f"{case}: expected {expected!r}, got {actual!r}")


def main() -> int:
    print("PYTHON:", sys.version.split()[0])
    print("PLATFORM:", platform.platform())
    with tempfile.TemporaryDirectory(prefix="sdd-guardian-smoke-") as temporary:
        consumer_root = Path(temporary)
        print("TEMP_ROOT:", consumer_root)

        feature = run("sample-feature", "--consumer-root", str(consumer_root))
        require(feature.returncode == 0, "feature scaffold failed")

        bugfix = run(
            "sample-bug",
            "--kind",
            "bugfix",
            "--consumer-root",
            str(consumer_root),
        )
        require(bugfix.returncode == 0, "bugfix scaffold failed")

        feature_root = consumer_root / "specs" / "001-sample-feature"
        bugfix_root = consumer_root / "specs" / "002-sample-bug"
        for relative in FEATURE_FILES:
            require((feature_root / relative).is_file(), f"missing {relative}")
        require(
            (bugfix_root / "reproduction.md").is_file(),
            "bugfix lacks reproduction.md",
        )
        index = (consumer_root / "specs" / "INDEX.md").read_text(encoding="utf-8")
        require("`001-sample-feature`" in index, "index lacks feature row")
        require("`002-sample-bug`" in index, "index lacks bugfix row")

        feature_spec = feature_root / "spec.md"
        hash_before = sha256(feature_spec)
        duplicate = run("sample-feature", "--consumer-root", str(consumer_root))
        hash_after = sha256(feature_spec)
        print("HASH_BEFORE:", hash_before)
        print("HASH_AFTER:", hash_after)
        require(duplicate.returncode != 0, "duplicate scaffold unexpectedly succeeded")
        require(hash_before == hash_after, "duplicate scaffold changed existing spec")

        bugfix_state = (
            bugfix_root / "run-state.yaml"
        ).read_text(encoding="utf-8")
        require(
            'initiative_kind: "bugfix"' in bugfix_state,
            "bugfix kind was not rendered",
        )
        require(
            'initiative_id: "002-sample-bug"' in bugfix_state,
            "bugfix initiative_id was not rendered",
        )
        require(
            'initiative_sequence: "002"' in bugfix_state,
            "bugfix sequence was not rendered",
        )

        require(
            not (feature_root / "stakeholder-brief.html").exists(),
            "a new scaffold must not materialize a stakeholder brief before canonical composition",
        )
        consumer_logo = consumer_root / PEARSON_LOGO_RELATIVE_PATH
        require(not consumer_logo.exists(), "a new scaffold must not provision a brand asset without a rendered brief")
        require(sha256(PEARSON_LOGO) == PEARSON_LOGO_SHA256, "bundle Pearson logo hash changed")

        divergent_root = consumer_root / "divergent-asset-consumer"
        divergent_logo = divergent_root / PEARSON_LOGO_RELATIVE_PATH
        divergent_logo.parent.mkdir(parents=True)
        divergent_logo.write_bytes(b"not the official Pearson logo")
        divergent = run("asset-mismatch", "--consumer-root", str(divergent_root))
        require(divergent.returncode == 0, "source-only scaffold must not depend on a consumer brand asset")
        require(
            divergent_logo.read_bytes() == b"not the official Pearson logo",
            "source-only scaffold touched a consumer-owned brand asset",
        )
        require(
            (divergent_root / "specs" / "001-asset-mismatch").is_dir(),
            "source-only scaffold did not create its initiative",
        )
        require(
            not (divergent_root / "specs" / "001-asset-mismatch" / "stakeholder-brief.html").exists(),
            "source-only scaffold created a brief in the divergent-asset fixture",
        )

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
