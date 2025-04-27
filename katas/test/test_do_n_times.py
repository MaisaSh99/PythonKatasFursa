import unittest
from unittest.mock import patch
from katas.do_n_times import do_n_times, say_hello, print_message


class TestDoNTimes(unittest.TestCase):
    @patch('builtins.print')
    def test_do_n_times(self, mock_print):

        do_n_times(say_hello, 4)
        self.assertEqual(mock_print.call_count, 4)
        do_n_times(print_message, 6)
        self.assertEqual(mock_print.call_count, 10)


