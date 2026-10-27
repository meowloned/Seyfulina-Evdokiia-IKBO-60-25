
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from vfs import load_vfs, calculate_vfs_hash

EXAMPLES = ROOT / "vfs_examples"


class TestVFS(unittest.TestCase):

    def test_minimal(self):
        vfs = load_vfs(EXAMPLES / "minimal")
        self.assertIn("empty.txt", vfs)

    def test_multiple(self):
        vfs = load_vfs(EXAMPLES / "multiple")
        self.assertEqual(len(vfs), 4)

    def test_nested(self):
        vfs = load_vfs(EXAMPLES / "demo")
        self.assertIn("documents/vuz/referat.txt", vfs)
        self.assertEqual(len(vfs), 4)

    def test_missing_directory(self):
        with self.assertRaises(FileNotFoundError):
            load_vfs(EXAMPLES / "missing")

    def test_not_directory(self):
        with self.assertRaises(NotADirectoryError):
            load_vfs(EXAMPLES / "demo" / "notes.txt")

    def test_hash(self):
        vfs = load_vfs(EXAMPLES / "demo")
        original_hash = calculate_vfs_hash(vfs)

        self.assertEqual(len(original_hash), 64)
        self.assertEqual(original_hash, calculate_vfs_hash(vfs))

        vfs["notes.txt"]["content"] = b"Changed"
        self.assertNotEqual(original_hash, calculate_vfs_hash(vfs))
