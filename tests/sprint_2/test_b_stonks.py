from unittest import TestCase

from sprint_2.b_stonks import max_income


class MaxIncomeTest(TestCase):
    def test_empty(self):
        self.assertEqual(0, max_income([]))

    def test_single(self):
        self.assertEqual(0, max_income([1]))

    def test_two(self):
        self.assertEqual(1, max_income([0, 1]))
