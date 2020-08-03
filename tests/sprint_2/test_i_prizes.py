from unittest import TestCase

from sprint_2.i_prizes import can_split


class TestPrizes(TestCase):
    def test_empty(self):
        self.assertFalse(can_split([], 3))

    def test_not_divisible(self):
        self.assertFalse(can_split([1, 9], 3))

    def test_single(self):
        self.assertTrue(can_split([10], 1))

    def test_two(self):
        self.assertTrue(can_split([2, 2], 2))

    def test_sample(self):
        self.assertTrue(can_split([4, 3, 2, 3, 5, 2, 1], 4))
        self.assertFalse(can_split([2, 3, 1, 3, 5, 2, 1], 2))
