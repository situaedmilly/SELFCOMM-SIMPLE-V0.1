import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from selfcomm import EnvelopeError, parse_envelope
from selfgraph import process_line, render_event


class SelfGraphTests(unittest.TestCase):
    def test_valid_envelope_is_rendered(self):
        event = {
            "event_id": "evt_test_001",
            "event_type": "PING",
            "source": "RAWMAC-PIMAC",
            "target": "SELFPI",
            "status": "PROPOSED",
        }
        self.assertEqual(
            render_event(event),
            "[SELFGRAPH][EVENT] evt_test_001 RAWMAC-PIMAC -> SELFPI PING [PROPOSED]",
        )
        self.assertIn("[SELFGRAPH][EVENT]", process_line(json.dumps(event)))

    def test_invalid_json_is_rejected(self):
        self.assertTrue(process_line("{not-json}").startswith("[SELFGRAPH][REJECT]"))

    def test_missing_required_field_is_rejected(self):
        with self.assertRaises(EnvelopeError):
            parse_envelope(json.dumps({"event_id": "evt_only"}))

    def test_event_schema_is_valid_json(self):
        schema = json.loads((ROOT / "protocol" / "event.schema.json").read_text())
        self.assertEqual(schema["$id"], "ourself.selfgraph.event.v0.1")


if __name__ == "__main__":
    unittest.main()
