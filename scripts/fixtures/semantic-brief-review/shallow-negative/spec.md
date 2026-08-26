# Billing-export release — fictional shallow-negative source

## Outcome

Do not expose a cross-tenant invoice during the billing-export release.

## Risk and decision

If the isolation probe fails, the release operator must keep the feature flag
off and notify incident response; the owner is the release operator.
