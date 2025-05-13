import unittest

from katas.test_case_grouping import group_test_cases  # adjust if the path is different


def normalize(groups):
    return sorted([sorted(group) for group in groups])


class TestGroupTestCases(unittest.TestCase):
    def test_case_1(self):
        input_data = [1, 2, 3, 3, 3, 2]
        expected = [[0], [1, 5], [2, 3, 4]]
        self.assertEqual(normalize(group_test_cases(input_data)), normalize(expected))

        input_data = [2, 2, 1, 1]
        expected = [[0, 1], [2], [3]]
        self.assertEqual(normalize(group_test_cases(input_data)), normalize(expected))

        input_data = [1, 1, 1]
        expected = [[0], [1], [2]]
        self.assertEqual(normalize(group_test_cases(input_data)), normalize(expected))

        input_data = []
        expected = []
        self.assertEqual(group_test_cases(input_data), expected)
