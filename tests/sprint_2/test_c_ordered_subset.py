from unittest import TestCase

from sprint_2.c_ordered_subset import is_ordered_subset


class OrderedSubsetTest(TestCase):
    def test_both_empty(self):
        self.assertTrue(is_ordered_subset('', ''))

    def test_small_empty(self):
        self.assertTrue(is_ordered_subset('', 'abc'))

    def test_big_empty(self):
        self.assertFalse(is_ordered_subset('abc', ''))

    def test_obvious_subset(self):
        self.assertTrue(is_ordered_subset('abc', 'abcd'))

    def test_mixed_subset(self):
        self.assertTrue(is_ordered_subset('abc', 'ahbjck'))

    def test_unordered_subset(self):
        self.assertFalse(is_ordered_subset('abc', 'acb'))
