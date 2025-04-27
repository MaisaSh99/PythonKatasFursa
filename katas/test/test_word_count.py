import unittest
from katas.word_count import count_words

class TestWordCount(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("  hello world  "), 2)
        self.assertEqual(count_words("my name is maisa"), 4)
        self.assertEqual(count_words("my    name  is maisa"), 4)
        self.assertEqual(count_words(""), 0)