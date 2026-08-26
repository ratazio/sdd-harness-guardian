# Validation — fictional software fixture

Run `npm run test:integration -- invoice-export-tenant-isolation` with fixtures
for two tenants. The oracle is that the second tenant's invoice ID cannot occur
in the response. Store the output in `evidence/T-003.md` before the release
decision.
