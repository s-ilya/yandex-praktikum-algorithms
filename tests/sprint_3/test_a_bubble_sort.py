from unittest import TestCase

from sprint_3.a_bubble_sort import bubble_sort


class BubbleSortTest(TestCase):
    def test_empty(self):
        self.assertEqual([], bubble_sort([]))

    def test_single(self):
        self.assertEqual([42], bubble_sort([42]))

    def test_sorted(self):
        self.assertEqual([42, 56], bubble_sort([42, 56]))
        self.assertEqual([42, 56, 89], bubble_sort([42, 56, 89]))

    def test_unsorted(self):
        self.assertEqual([42, 56], bubble_sort([56, 42]))
        self.assertEqual([42, 56, 89], bubble_sort([56, 89, 42]))
