---
id: W2_PERMISSION_DISCRIMINATION_RECEIPT
act: ACT-SELFCOMM-V0.1-WAKE-RECONTACT-PERMISSION-DISCRIMINATION-001
standing: LIVE_CANDIDATE_V0.1_PERMISSION_DISCRIMINATION
recorded_at_utc: 2026-09-07T15:02:35Z
terminus: STOP_BEFORE_ACTUATION
provider_invocation: NOT_PERFORMED
self_occurrence_formation: NOT_PERFORMED
autonomous_loop_established: false
latest_json_updated: false
---

# W2 Permission Discrimination Receipt

## Recontact Basis

A fresh temporary Git workspace at
`/private/tmp/selfcomm-v01-permission-discrimination-001` fetched
`origin main` from GitHub before the fixture was evaluated.

```text
FETCH_HEAD: 3410592f885f6a782da66fe18ecf2df7a34f5641
latest.json sha256: 909d87672697d559d5e82ba4b23e2faa2cba24217a426551e204500453dbbb14
M2 sha256: 325a03db2abe8b4b7d2efe88a2723930da04a11450ec171eb8728ba01f9df4b8
W1 receipt sha256: 2c04c87a3b0c61ac52fea0a76a25cd0645869c040b9a0a66636a4472e55e9910
```

`latest.json` still resolved to:

```json
{
  "id": "M2",
  "path": "interactions/M2.md"
}
```

The permission fixture used `M2` as the subject Matter and fixture-local grant
entries as the independent authority source. Message assertions were tested as
inputs to discrimination, not as permission sources.

## Decision Graph

```text
ExternalEvent
-> MachineWake
-> IndependentRecontact
-> D_PARTICIPATION
-> RequirementRef R, iff required
-> D_PERMISSION, iff R exists
-> PermissionStanding over exact R
-> D_ELIGIBILITY over exact TransitionRef T
-> NO_ACTION | HOLD | ELIGIBLE
-> STOP
```

## Fixture Results

| World | Requirement | Permission | Transition binding | Expected | Observed | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| A | absent | not asked | irrelevant | NO_ACTION | NO_ACTION | NO_PARTICIPATION_REQUIREMENT_ESTABLISHED |
| B | PR-B exact required participation | absent | exact | HOLD | HOLD | PERMISSION_ABSENT |
| C | PR-C exact required participation | mismatched operation | exact | HOLD | HOLD | GRANT_OPERATION_DOES_NOT_COVER_READ_ONLY_REVIEW_REQUIREMENT |
| D | PR-D exact required participation | exact current grant | exact | ELIGIBLE | ELIGIBLE | EXACT_CURRENT_PERMISSION_AND_TRANSITION_PREIMAGE_COVERED |
| E | PR-E exact required participation | absent, Matter asserts authorized | exact | HOLD | HOLD | MATTER_SELF_AUTHORIZATION_IGNORED_PERMISSION_ABSENT |
| F | PR-F exact required participation | exact current grant, Matter asserts unauthorized without valid revocation | exact | ELIGIBLE | ELIGIBLE | MESSAGE_SELF_DEAUTHORIZATION_IGNORED_NO_VALID_REVOCATION_AND_EXACT_PERMISSION_COVERS_REQUIREMENT |
| G | PR-G exact required participation | exact current grant | wrong TransitionRef | HOLD | HOLD | TRANSITION_BINDING_MISMATCH |

## Bound References

```text
matter_ref: FETCH_HEAD:interactions/M2.md#sha256:325a03db2abe8b4b7d2efe88a2723930da04a11450ec171eb8728ba01f9df4b8
wake_ref: FETCH_HEAD:interactions/W1-gh-wake-recontact-receipt.md#sha256:2c04c87a3b0c61ac52fea0a76a25cd0645869c040b9a0a66636a4472e55e9910
role_ref: ROLE:SELF_A_REVIEWER
operation_ref: READ_ONLY_REVIEW
consequence_scope: NO_MUTATION_NO_PROVIDER_INVOCATION
temporal_scope: CURRENT_AT:2026-09-07T15:02:35Z
```

Representative requirement reference:

```text
PR-D-RequiredParticipation(ROLE:SELF_A_REVIEWER,M2,READ_ONLY_REVIEW,NO_MUTATION_NO_PROVIDER_INVOCATION,CURRENT)
```

Representative exact grant reference:

```text
GRANT-D-READ_ONLY_REVIEW-CURRENT
```

Transition references remained world-bound. World G used
`T-G-DIFFERENT_TRANSITION` to prove that exact permission for a requirement does
not produce eligibility for the wrong transition.

## Classification

```text
SEVEN_WORLDS_EXECUTED = YES
EXPECTED_DECISION_MATCHED_OBSERVED_DECISION = 7/7
D_PARTICIPATION != D_PERMISSION != D_ELIGIBILITY
RequirementRef != PermissionRef != EligibilityRef != TransitionRef
PermissionExact != Eligibility
NoRequirement -> NoPermissionQuestion
MatterCanSelfAuthorize = 0
MatterCanSelfDeauthorize = 0 unless valid revocation is independently established
ELIGIBLE_ACTUATED = 0
PROVIDER_INVOCATION = NOT_PERFORMED
SELF_OCCURRENCE_FORMATION = NOT_PERFORMED
AUTONOMOUS_LOOP = NOT_ESTABLISHED
STOP_REACHED = YES
```
