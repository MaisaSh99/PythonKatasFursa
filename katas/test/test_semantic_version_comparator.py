import unittest
from katas.semantic_version_comparator import compare_versions


class TestCompareVersions(unittest.TestCase):
    def test_equal_versions(self):
        self.assertEqual(compare_versions("0.0.0", "0.0"), 0)
        self.assertEqual(compare_versions("1.9.9", "2.0.0"), -1)
        self.assertEqual(compare_versions("1.2", "1.2.1"), -1)
        self.assertEqual(compare_versions("1.2.1", "1.2"), 1)
        self.assertEqual(compare_versions("1.0.1", "1.0.0"), 1)
