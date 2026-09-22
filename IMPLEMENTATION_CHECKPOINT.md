# OURLLAMASELF implementation checkpoint

- Jurisdiction: this repository only.
- Preimage: `main` at `b3a4259ac6ed0494d4cd22fa43cc3c6991a6c770`, clean before amendment.
- Scope: local SELFGRAPH JSONL observation and SELFCOMM envelope validation.
- Explicit ceiling: no deployment, daemon installation, autonomous looping, remote mutation, or canon promotion.
- Rollback: revert the amendment and delete the added `runtime/`, `protocol/`, `graph/events.jsonl`, and `tests/` files.
- Verification: Python unit tests, schema parse, one-shot runtime probe, and post-change Git diff/status.
