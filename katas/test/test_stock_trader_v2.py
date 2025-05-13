import unittest
from katas.stock_trader_v2 import max_profit


class TestMaxProfit(unittest.TestCase):
    def test_empty_prices(self):
        self.assertEqual(max_profit([]), 0)
        self.assertEqual(max_profit([5]), 0)
        self.assertEqual(max_profit([1, 2, 3, 2, 3, 2, 3]), 4)
        self.assertEqual(max_profit([2, 10]), 8)
        self.assertEqual(max_profit([5, 5, 5, 5]), 0)
        self.assertEqual(max_profit([1, 3, 1, 4, 1, 5]), 9)
