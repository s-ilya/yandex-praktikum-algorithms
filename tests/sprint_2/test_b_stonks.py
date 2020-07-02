from unittest import TestCase

from sprint_2.b_stonks import max_income


class MaxIncomeTest(TestCase):
    def test_empty(self):
        self.assertEqual(0, max_income([]))

    def test_single(self):
        self.assertEqual(0, max_income([1]))

    def test_two(self):
        self.assertEqual(1, max_income([0, 1]))

    def test_skip_middle(self):
        self.assertEqual(2, max_income([1, 2, 3]))

    def test_skip_first(self):
        self.assertEqual(1, max_income([3, 1, 2]))

    def test_skip_last(self):
        self.assertEqual(2, max_income([1, 2, 3, 2]))

    def test_skip_all(self):
        self.assertEqual(0, max_income([3, 2, 1]))