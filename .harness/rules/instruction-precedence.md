# Rule: Instruction Precedence and Local Overrides

## Soft rule

Project-local instructions may specialize bundle defaults but may not weaken
protected safety, evidence, validation, evaluation, destructive-operation or
resumability invariants.

## Resolution order

```txt
1. safety, privacy, permissions and destructive approval
2. protected SDD/evidence/validation invariants
3. project-local rules
4. approved project-local spec
5. bundle defaults
6. generic agent preferences
```

When two applicable instructions conflict, follow the higher protected rule.
Record the conflict, chosen resolution and rationale in `decision-log.md`.
Escalate unresolved product, security or destructive conflicts.

## Blocking conditions

Block when an override removes a required gate, consumer root/bundle root is
ambiguous, or the chosen resolution would alter scope without authorization.

## Hard mirror recommendation

Maintain a machine-readable list of protected invariants and require override
records to identify the rule, local replacement, owner and approval. CI or an
orchestrator should reject disabled protected gates.

Recommended check: `validate-protected-invariants`.
