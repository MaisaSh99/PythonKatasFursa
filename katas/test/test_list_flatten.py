import unittest
from katas.list_flatten import flatten_list

class TestListFlatten(unittest.TestCase):
    def test_list_flatten(self):
        self.assertEqual(flatten_list([
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]), [1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(flatten_list([
        1,
        [],
        [2, []],
        3
    ]), [1, 2, 3])

        self.assertEqual(flatten_list([
        1,
        2, 3,
        4, 5, 6,
        7
    ]), [1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(flatten_list([
        "hi",
        [2, 3],
        [4, [5, 6]],
        7
    ]), [2, 3, 4, 5, 6, 7])

        self.assertEqual(flatten_list([]), [])