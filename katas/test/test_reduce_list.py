import unittest
from katas.reduce_list import reduce_array

class TestReduceList(unittest.TestCase):
    def test_reduce_list(self):

        numbers = [10, 15, 7, 20, 25]
        reduce_array(numbers)
        self.assertEqual(numbers, [10, 5, -8, 13, 5])
        numbers = [3, 3, 3, 3]
        reduce_array(numbers)
        self.assertEqual(numbers, [3, 0, 0, 0])
        numbers = [2, 9]
        reduce_array(numbers)
        self.assertEqual(numbers, [2, 7])
        numbers = [2]
        reduce_array(numbers)
        self.assertEqual(numbers, [2])
        numbers = []
        reduce_array(numbers)
        self.assertEqual(numbers, [])