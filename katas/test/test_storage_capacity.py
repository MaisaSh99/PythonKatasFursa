import unittest
from katas.max_storage_capacity import max_storage_area


class TestMaxStorageArea(unittest.TestCase):
    def test_all_equal_heights(self):
        self.assertEqual(max_storage_area([4, 4, 4, 4]), 16)
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)
        self.assertEqual(max_storage_area([7]), 7)
        self.assertEqual(max_storage_area([]), 0)
        self.assertEqual(max_storage_area([2, 1, 2]), 3)