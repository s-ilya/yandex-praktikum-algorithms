from unittest import TestCase

from sprint_3.z_insort_index import leftmost_insort_index


class LeftInsortIndexTest(TestCase):
    def test_empty(self):
        self.assertEqual(
            0, leftmost_insort_index([], 42)
        )

    def test_single_less_than(self):
        self.assertEqual(
            1, leftmost_insort_index([40], 42)
        )

    def test_single_more_than(self):
        self.assertEqual(
            0, leftmost_insort_index([40], 39)
        )

    def test_two_insert_first(self):
        self.assertEqual(
            0, leftmost_insort_index([35, 40], 30)
        )

    def test_two_insert_middle(self):
        self.assertEqual(
            1, leftmost_insort_index([35, 40], 37)
        )

    def test_two_insert_last(self):
        self.assertEqual(
            2, leftmost_insort_index([35, 40], 45)
        )

    def test_insert_before_same(self):
        self.assertEqual(
            0, leftmost_insort_index([35], 35)
        )
