from unittest import TestCase

from sprint_4.a_count_search_trees import count_search_trees


class CountSearchTreesTest(TestCase):
    def test_empty(self):
        self.assertEqual(0, count_search_trees(0))

    def test_single(self):
        self.assertEqual(1, count_search_trees(1))

    def test_two(self):
        self.assertEqual(2, count_search_trees(2))

    def test_three(self):
        self.assertEqual(5, count_search_trees(3))

    def test_four(self):
        self.assertEqual(14, count_search_trees(4))

    def test_max(self):
        self.assertEqual(6564120420, count_search_trees(20))
