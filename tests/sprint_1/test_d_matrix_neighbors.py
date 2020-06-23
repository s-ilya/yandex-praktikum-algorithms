from unittest import TestCase

from sprint_1.d_matrix_neighbors import matrix_neighbors


class MatrixNeighborsTest(TestCase):
    def test_empty(self):
        self.assertEqual([], matrix_neighbors([], 0, 0))

    def test_single(self):
        self.assertEqual([], matrix_neighbors([[1]], 0, 0))

    def test_only_right(self):
        self.assertEqual([2], matrix_neighbors([[1, 2]], 0, 0))

    def test_only_left(self):
        self.assertEqual([1], matrix_neighbors([[1, 2]], 0, 1))

    def test_only_top(self):
        self.assertEqual([1], matrix_neighbors([[1], [2]], 1, 0))

    def test_only_bottom(self):
        self.assertEqual([2], matrix_neighbors([[1], [2]], 0, 0))

    def test_sorted(self):
        self.assertEqual([1, 2], matrix_neighbors([[0, 2], [1, 3]], 0, 0))

    def test_full(self):
        self.assertEqual([2, 4, 6, 8], matrix_neighbors([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
