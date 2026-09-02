# T-002 revision finding: fresh consumer logo distribution

**Status:** required before T-004 can resume.  
**Origin:** SPEC 014 T-004 builder reproduction, 2026-08-27.  
**Evidence:** `../evidence/T-004.md`.

## Finding

Fresh `new_initiative.py` output references the required local logo but does
not create its consumer-relative destination. The generated PNG path resolves
to a missing file, so source-template render tests are insufficient proof of a
fresh consumer’s brand contract.

## Narrow revision scope

Provision the exact official asset at
`.harness/assets/brand/pearson-logo-white.png` in a fresh consumer without
overwriting a user-owned existing file. An existing file must match SHA-256
`8EEE1FA799766BF385A307191D38C361677D442457D7CC0F92E5F3FCCC2282F7`; otherwise
fail clearly. Keep the current local relative HTML URL; do not use a hotlink,
data URI or vendor-install-path coupling.

## Required proof before T-004 resumes

1. Scaffold a new temporary consumer and resolve the image path from the
   generated brief.
2. Verify file existence, exact hash and 175 × 53 dimensions.
3. Serve that consumer locally and observe a successful same-origin PNG
   request from the generated brief.
4. Re-run T-002’s focused/scaffold/render/bundle checks with a distinct
   evaluator approval.

Only then may T-004 produce viewport screenshots, print evidence, final
inventory review and a Human Visibility baseline.
