"""Pinned registry-only boot for the OURSELFCOMM ProtocolSELF-18 projection.

This module does not alter SELFCOMM envelope validation or start transport.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

REGISTRY_SHA256 = "76a2a14c9bab0d0ded7ff05c80991141df53e9f1f15ec948443e0b950017508c"
REGISTRY_PATH = Path(__file__).resolve().parents[1] / "protocols" / "protocolself-18.v0.1.json"


def boot_protocolself_registry(path: Path = REGISTRY_PATH) -> dict[str, Any]:
    raw = path.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != REGISTRY_SHA256:
        raise ValueError("PROTOCOLSELF_SOURCE_DIGEST_MISMATCH")
    registry = json.loads(raw)
    if registry.get("registry_id") != "OURSELFCOMM-PROTOCOLSELF-18":
        raise ValueError("PROTOCOLSELF_REGISTRY_ID_INVALID")
    protocols = registry.get("protocols")
    if not isinstance(protocols, list) or len(protocols) != 18:
        raise ValueError("PROTOCOLSELF_REGISTRY_COUNT_INVALID")
    if any(
        item.get("listener_enabled") is not False
        or item.get("external_exposure") is not False
        or item.get("admission_required") is not True
        for item in protocols
    ):
        raise ValueError("PROTOCOLSELF_LISTENER_POLICY_VIOLATION")
    if registry.get("boot_policy", {}).get("network_transport_authority") != "NOT_GRANTED_BY_REGISTRY_BOOT":
        raise ValueError("PROTOCOLSELF_AUTHORITY_BOUNDARY_INVALID")
    return {
        "registry_id": registry["registry_id"],
        "source_sha256": actual,
        "status": "REGISTRY_BOOTED_LISTENERS_DISABLED",
        "protocol_count": len(protocols),
        "network_listeners_started": 0,
        "external_bindings_created": 0,
        "network_transport_authority": "NOT_GRANTED",
    }


if __name__ == "__main__":
    print(json.dumps(boot_protocolself_registry(), indent=2))
