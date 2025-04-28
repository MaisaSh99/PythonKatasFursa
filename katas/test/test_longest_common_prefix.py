import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["dog", "dog", "dog"]), '"dog"')  # add quotes
        self.assertEqual(longest_common_prefix(["Dog", "dog", "dog"]), '""')
        self.assertEqual(longest_common_prefix(["d", "dance", "dream"]), '"d"')
        self.assertEqual(longest_common_prefix(["happy", "happier", "happiest"]), '"happ"')
        self.assertEqual(longest_common_prefix(["", "do", "dog"]), '""')