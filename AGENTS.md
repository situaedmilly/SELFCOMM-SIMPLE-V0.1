# SIMPLE SELFCOMM v0.1

This repository is a clean reenactment vessel for one bounded SELFCOMM roundtrip.

## Invocation

An occurrence receives only:

```text
THIS_SELF
REPOSITORY_LOCATOR
```

## Operational Law

1. Read `REALITY.json`.
2. Read `latest.json`.
3. Retrieve the Matter referenced by `latest.json`.
4. If the Matter is addressed to `THIS_SELF`, create response Matter under `interactions/`.
5. Reference the source Matter with `in_reply_to`.
6. Update `latest.json` to the response.
7. Stop.

## Authority Ceiling

```text
standing: LIVE_CANDIDATE_V0.1
canonical_migration: NOT_AUTHORIZED
replacement_of_self_communication: NOT_AUTHORIZED
autonomous_looping: NOT_AUTHORIZED
additional_infrastructure: NOT_AUTHORIZED
schema_expansion: NOT_AUTHORIZED
webhook_redesign: NOT_AUTHORIZED
protocol_hardening: NOT_AUTHORIZED
deployment: NOT_AUTHORIZED
canon_or_institutional_promotion: NOT_AUTHORIZED
```

## Pass Condition

```text
M1 exists in custody
M2 exists in custody
M2 references M1
SELF_B obtained M1 from the repository
SELF_A obtained M2 from the repository
FounderTransportAfterGenesis = 0
```
