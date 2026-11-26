import json
import unittest

from runtime.protocolself_registry import boot_protocolself_registry


class ProtocolSelfRegistryBootTests(unittest.TestCase):
    def test_boot_loads_all_18_without_transport(self):
        receipt = boot_protocolself_registry()
        self.assertEqual(receipt["protocol_count"], 18)
        self.assertEqual(receipt["status"], "REGISTRY_BOOTED_LISTENERS_DISABLED")
        self.assertEqual(receipt["network_listeners_started"], 0)
        self.assertEqual(receipt["external_bindings_created"], 0)
        self.assertEqual(receipt["network_transport_authority"], "NOT_GRANTED")


if __name__ == "__main__":
    unittest.main()
