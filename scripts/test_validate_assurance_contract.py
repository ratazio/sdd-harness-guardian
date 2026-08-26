from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "scripts/fixtures/assurance-contracts/fictional-006"

def run(name: str) -> int:
    return subprocess.run([sys.executable, "scripts/validate_assurance_contract.py", str(FIXTURE / name)], cwd=ROOT).returncode

assert run("positive-plan.md") == 0
assert run("negative-missing-rationale.md") == 1
assert run("negative-invalid-profile.md") == 1
assert run("negative-empty-a2-link.md") == 1
assert run("a1-local.md") == 0
waiver = (FIXTURE / "negative-incomplete-waiver.md").read_text(encoding="utf-8")
for field in ("human=missing", "reason=missing", "residual_risk=missing", "compensating_control=missing", "scope=missing", "expiry=missing"):
    assert field in waiver
print("Assurance contract fixture tests passed.")
