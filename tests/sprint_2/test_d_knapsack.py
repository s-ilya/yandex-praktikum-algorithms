from unittest import TestCase

from sprint_2.d_knapsack import get_knapsack_contents


def item(index, value, weight):
    return index, value, weight


class KnapsackTest(TestCase):
    def test_empty(self):
        self.assertEqual(
            [],
            get_knapsack_contents(0, [])
        )

    def test_take_single(self):
        self.assertEqual(
            [0],
            get_knapsack_contents(1, [
                item(0, 1, 1)
            ])
        )

    def test_take_none(self):
        self.assertEqual(
            [],
            get_knapsack_contents(0, [
                item(0, 1, 1)
            ])
        )

    def test_take_two(self):
        self.assertEqual(
            [0, 1],
            get_knapsack_contents(2, [
                item(0, 1, 1),
                item(1, 1, 1)
            ])
        )

    def test_drop_last(self):
        self.assertEqual(
            [0, 1],
            get_knapsack_contents(2, [
                item(0, 1, 1),
                item(1, 1, 1),
                item(2, 1, 1)
            ])
        )

    def test_drop_first(self):
        self.assertEqual(
            [1, 2],
            get_knapsack_contents(2, [
                item(0, weight=1, value=1),
                item(1, weight=1, value=2),
                item(2, weight=1, value=3)
            ])
        )

    def test_same_value_different_weight(self):
        self.assertEqual(
            [1],
            get_knapsack_contents(3, [
                item(0, weight=3, value=3),
                item(1, weight=2, value=3)
            ])
        )

    def test_same_value_weight(self):
        self.assertEqual(
            [0],
            get_knapsack_contents(1, [
                item(0, weight=1, value=1),
                item(1, weight=1, value=1)
            ])
        )

    def test_drop_middle(self):
        self.assertEqual(
            [0, 2],
            get_knapsack_contents(2, [
                item(0, weight=1, value=2),
                item(1, weight=1, value=1),
                item(2, weight=1, value=3)
            ])
        )

    def test_sample(self):
        self.assertEqual(
            [1, 2, 3],
            get_knapsack_contents(123, [
                item(0, value=25, weight=50),
                item(1, value=30, weight=40),
                item(2, value=30, weight=80),
                item(3, value=2, weight=3)
            ])
        )
