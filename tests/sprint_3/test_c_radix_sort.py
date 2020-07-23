from unittest import TestCase
from random import randrange

from sprint_3.c_radix_sort import radix_sort


class RadixSortTest(TestCase):
    def test_empty(self):
        self.assertEqual([], radix_sort([]))

    def test_single(self):
        self.assertEqual([1], radix_sort([1]))

    def test_sorted(self):
        self.assertEqual([3, 8], radix_sort([3, 8]))

    def test_unsorted(self):
        self.assertEqual([3, 8], radix_sort([8, 3]))

    def test_ranks(self):
        self.assertEqual([12, 21], radix_sort([21, 12]))

    def test_random(self):
        for _ in range(randrange(1000)):
            max_item = 100000
            max_items = 1000

            unsorted = [
                randrange(max_item) for _ in range(randrange(max_items))
            ]

            self.assertEqual(
                sorted(unsorted),
                radix_sort(unsorted)
            )
