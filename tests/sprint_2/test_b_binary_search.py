from unittest import TestCase

from sprint_2.b_binary_search import binary_search


class BinarySearchTest(TestCase):
    def test_empty(self):
        self.assertEqual(-1, binary_search([], 1))

    def test_single_not_contains(self):
        self.assertEqual(-1, binary_search([9], 10))

    def test_single_contains(self):
        self.assertEqual(0, binary_search([9], 9))

    def test_double_contains_first(self):
        self.assertEqual(0, binary_search([8, 9], 8))

    def test_double_contains_second(self):
        self.assertEqual(1, binary_search([8, 9], 9))

    def test_sample(self):
        self.assertEqual(2, binary_search([5, 6, 7, 8, 9], 7))
        self.assertEqual(2, binary_search([5, 6, 7, 8, 9, 10], 7))

    def test_cycled(self):
        self.assertEqual(1, binary_search([9, 5, 6, 7, 8], 5))
        self.assertEqual(2, binary_search([8, 9, 5, 6, 7], 5))
        self.assertEqual(3, binary_search([7, 8, 9, 5, 6], 5))
        self.assertEqual(4, binary_search([6, 7, 8, 9, 5], 5))
