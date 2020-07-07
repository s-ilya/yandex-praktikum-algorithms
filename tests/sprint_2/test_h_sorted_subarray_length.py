from unittest import TestCase

from sprint_2.h_sorted_subarray_length import max_sorted_sub_length


class MaxSortedSubLengthTest(TestCase):
    def test_empty(self):
        self.assertEqual(0, max_sorted_sub_length([]))

    def test_single(self):
        self.assertEqual(1, max_sorted_sub_length([1]))

    def test_sorted(self):
        self.assertEqual(3, max_sorted_sub_length([1, 2, 3]))

    def test_reversed(self):
        self.assertEqual(1, max_sorted_sub_length([3, 2, 1]))

    def test_sorted_sub(self):
        self.assertEqual(2, max_sorted_sub_length([3, 2, 1, 2, 1]))

    def test_is_increasing(self):
        self.assertEqual(2, max_sorted_sub_length([1, 1, 2]))