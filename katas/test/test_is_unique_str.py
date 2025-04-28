import unittest
from katas.is_unique_str import is_unique

class TestIsUniqueStr(unittest.TestCase):
    def test_is_unique_str(self):
        self.assertEqual(is_unique("maisa"), False)
        self.assertEqual(is_unique(" hi world  "), True)
        self.assertEqual(is_unique("Aa"), True)
        self.assertEqual(is_unique("My    Love"), True)
        self.assertEqual(is_unique(""), True)