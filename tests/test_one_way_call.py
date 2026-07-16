import importlib.util
from pathlib import Path
import unittest

import requests


SCRIPT = Path(__file__).parents[1] / "scripts" / "one_way_call.py"
spec = importlib.util.spec_from_file_location("one_way_call", SCRIPT)
one_way_call = importlib.util.module_from_spec(spec)
spec.loader.exec_module(one_way_call)


class CallTwiMLTest(unittest.TestCase):
    def test_message_uses_inline_speech_without_external_media(self):
        twiml = one_way_call.build_twiml("Hello Nate & Omer")

        self.assertIn("<Say", twiml)
        self.assertIn("Hello Nate &amp; Omer", twiml)
        self.assertNotIn("<Play", twiml)


if __name__ == "__main__":
    unittest.main()
