import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("hello world"), 0)
        self.assertEqual(sum_of_digits("2m2a2i2s2a"), 10)
        self.assertEqual(sum_of_digits("100 205"), 8)
        self.assertEqual(sum_of_digits("16422"), 15)
        self.assertEqual(sum_of_digits(""), 0)