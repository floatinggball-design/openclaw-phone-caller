import importlib.util
import os
from pathlib import Path
import unittest


class ServerConfigTest(unittest.TestCase):
    def test_conversation_model_can_be_configured(self):
        os.environ["CALLER_MODEL"] = "gemini-2.0-flash"
        script = Path(__file__).parents[1] / "scripts" / "server.py"
        spec = importlib.util.spec_from_file_location("caller_server", script)
        server = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(server)

        self.assertEqual(server.CONVERSATION_MODEL, "gemini-2.0-flash")


if __name__ == "__main__":
    unittest.main()
