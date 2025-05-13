import unittest
from katas.requirements_coverage import select_minimal_test_cases


class TestRequirementsCoverage(unittest.TestCase):
    def test_single_test_case_covers_all(self):
        test_cases = [[1, 2, 3, 4, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

        test_cases = [[1], [2], [3], [4], [5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set(result), {0, 1, 2, 3, 4})

        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3],
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue(set(result) in [{0, 1}, {1, 2}, {0, 2}])

        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set().union(*(test_cases[i] for i in result)), {1, 2, 3, 4, 5})

        test_cases = []
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [])