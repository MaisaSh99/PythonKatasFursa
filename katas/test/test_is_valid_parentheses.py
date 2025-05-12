import unittest
from katas.is_valid_parentheses import is_valid_parentheses

class TestIsValidParentheses(unittest.TestCase):
    def test_is_valid_parentheses(self):
        self.assertEqual(is_valid_parentheses("()[]{}"), True)
        self.assertEqual(is_valid_parentheses("(]"), False)
        self.assertEqual(is_valid_parentheses("([)]"), False)
        self.assertEqual(is_valid_parentheses("{[]()}"), True)
        self.assertEqual(is_valid_parentheses(""), True)
        self.assertEqual(is_valid_parentheses("("), False)
        self.assertEqual(is_valid_parentheses("["), False)
        self.assertEqual(is_valid_parentheses("((()))"), True)
