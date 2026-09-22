#!/usr/bin/env python3
"""Bounded SELFCOMM envelope validation for the local SELFGRAPH substrate."""

from __future__ import annotations

import json
from typing import Any

REQUIRED_FIELDS = frozenset({"event_id", "event_type", "source", "target", "status"})


class EnvelopeError(ValueError):
    """Raised when an event envelope cannot be admitted to SELFGRAPH."""


def validate_envelope(event: Any) -> dict[str, Any]:
    if not isinstance(event, dict):
        raise EnvelopeError("envelope must be an object")
    missing = sorted(REQUIRED_FIELDS - event.keys())
    if missing:
        raise EnvelopeError(f"missing fields: {', '.join(missing)}")
    for field in REQUIRED_FIELDS:
        if not isinstance(event[field], str) or not event[field].strip():
            raise EnvelopeError(f"{field} must be a non-empty string")
    return event


def parse_envelope(raw: str) -> dict[str, Any]:
    try:
        event = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise EnvelopeError(f"invalid JSON: {exc.msg}") from exc
    return validate_envelope(event)
