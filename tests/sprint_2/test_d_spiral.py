from unittest import TestCase

from sprint_2.d_spiral import spiral


class SpiralTest(TestCase):
    def test_empty(self):
        self.assertEqual([], spiral([]))

    def test_single(self):
        self.assertEqual([1], spiral([[1]]))

    def test_one_row(self):
        self.assertEqual([1, 2, 3], spiral([[1, 2, 3]]))

    def test_one_column(self):
        self.assertEqual([1, 2, 3], spiral([[1], [2], [3]]))

    def test_simple_square(self):
        self.assertEqual([1, 2, 4, 3], spiral([
            [1, 2],
            [3, 4]
        ]))

    def test_odd_square(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], spiral([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))

    def test_even_rectangle(self):
        self.assertEqual([1, 2, 4, 6, 8, 7, 5, 3], spiral([
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]))

    def test_odd_rectangle(self):
        self.assertEqual([1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11], spiral([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15]
        ]))
