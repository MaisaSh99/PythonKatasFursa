import unittest
from katas.is_valid_git_tree import is_valid_git_tree


class TestIsValidGitTree(unittest.TestCase):
    def test_is_valid_git_tree(self):
        self.assertEqual(is_valid_git_tree({
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }), True)

        self.assertEqual(is_valid_git_tree({
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }), False)

        self.assertEqual(is_valid_git_tree({
            "A": ["B"],
            "C": ["D"],
            "B": [],
            "D": []
        }), False)

        self.assertEqual(is_valid_git_tree({
            "A": ["B"],
            "B": [],
            "C": []
        }), False)

        self.assertEqual(is_valid_git_tree({}), False)