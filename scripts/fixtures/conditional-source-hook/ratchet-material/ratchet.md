# Ratchet Log

## R-42 — preserve release hold evidence

- Trigger: a release probe loses its attached tenant evidence.
- Check: `python scripts/check_release_evidence.py --tenant <id>` before enable.
- Owner: release manager.
- Consequence: hold the flag, notify incident response, and rerun the probe.
