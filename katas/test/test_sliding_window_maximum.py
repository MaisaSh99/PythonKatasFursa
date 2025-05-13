import unittest
from katas.sliding_window_maximum import max_sliding_window

class TestMaxSlidingWindow(unittest.TestCase):

    def test_window_equals_list(self):
        self.assertEqual(
            max_sliding_window([2, 1, 3], 3),
            [3]
        )
        self.assertEqual(
            max_sliding_window([], 3),
            []
        )
        self.assertEqual(
            max_sliding_window([1, 2, 3], 0),
            []
        )
        self.assertEqual(
            max_sliding_window([4, 4, 4, 4, 4], 3),
            [4, 4, 4]
        )
        self.assertEqual(
            max_sliding_window([10, 9, 8, 7, 6], 2),
            [10, 9, 8, 7]
        )
        self.assertEqual(
            max_sliding_window([1, 2, 3, 4, 5], 3),
            [3, 4, 5]
        )

        self.assertEqual(
            max_sliding_window([1, 2], 5),
            []
        )