#!/usr/bin/env python3
"""Observable, append-only SELFGRAPH JSONL event tailer."""

from __future__ import annotations

import argparse
import os
import time
from pathlib import Path

from selfcomm import EnvelopeError, parse_envelope

DEFAULT_EVENT_LOG = Path(__file__).resolve().parents[1] / "graph" / "events.jsonl"


def render_event(event: dict[str, object]) -> str:
    return (
        f"[SELFGRAPH][EVENT] {event['event_id']} "
        f"{event['source']} -> {event['target']} "
        f"{event['event_type']} [{event['status']}]"
    )


def process_line(raw: str) -> str:
    try:
        return render_event(parse_envelope(raw))
    except EnvelopeError as exc:
        return f"[SELFGRAPH][REJECT] {exc}"


def follow(path: Path, *, once: bool = False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    with path.open("r", encoding="utf-8") as stream:
        if not once:
            stream.seek(0, os.SEEK_END)
        while True:
            line = stream.readline()
            if line:
                yield line.rstrip("\n")
                continue
            if once:
                return
            time.sleep(0.25)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events", type=Path, default=DEFAULT_EVENT_LOG)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    print("[SELFGRAPH] boot")
    print(f"[SELFGRAPH] event stream: {args.events}")
    for line in follow(args.events, once=args.once):
        print(process_line(line), flush=True)


if __name__ == "__main__":
    main()
