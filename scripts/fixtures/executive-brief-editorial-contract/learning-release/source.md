# Learning-release authority

## Decision boundary

The learner shell will show the revised assessment result after the publishing
contract confirms the release. The entitlement guard remains the refusal point
for learners without a valid entitlement.

## Change surfaces

Three source-supported surfaces participate in this release: learner shell,
publishing contract and entitlement guard. The reporting warehouse is context
only and is not changed by this release.

## Learner-shell zoom

Within the learner shell, the result panel consumes the confirmed release
event. Its route transition and entitlement message remain unchanged.
