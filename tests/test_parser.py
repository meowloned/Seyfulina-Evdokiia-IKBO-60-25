
import sys
import unittest
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from parser import parse_command


class TestParser(unittest.TestCase):

    def test_simple_command(self):
        self.assertEqual(parse_command("ls"), ["ls"])

    def test_arguments(self):
        self.assertEqual(
            parse_command("cd documents"),
            ["cd", "documents"]
        )

    def test_quotes(self):
        self.assertEqual(
            parse_command('cd "My Documents"'),
            ["cd", "My Documents"]
        )

    def test_unclosed_quotes(self):
        with self.assertRaises(ValueError):
            parse_command('cd "Documents')
