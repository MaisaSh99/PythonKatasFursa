import unittest
from katas.true_counter import count_true_values

class TestWordCount(unittest.TestCase):
    def test_true_counter(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)
        self.assertEqual(count_true_values([False, False, False, False, False]), 0)
        self.assertEqual(count_true_values([True, True]), 2)
        self.assertEqual(count_true_values([True, False, True, True]), 3)
        self.assertEqual(count_true_values([]), 0)