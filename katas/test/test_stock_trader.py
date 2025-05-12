import unittest
from katas.stock_trader import max_profit


class TestMaxProfit(unittest.TestCase):
    def test_profit_possible(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit([5]), 0)
        self.assertEqual(max_profit([]), 0)
        self.assertEqual(max_profit([9, 8, 7, 6, 5, 10]), 5)
