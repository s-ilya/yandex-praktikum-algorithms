from unittest import TestCase

from sprint_3.b_median import median


class MedianTest(TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            median([], [])

    def test_single_left(self):
        self.assertEqual(1, median([1], []))

    def test_single_right(self):
        self.assertEqual(1, median([], [1]))

    def test_odd_not_overlapped(self):
        self.assertEqual(23, median([7, 23], [49]))

    def test_odd_overlapped(self):
        self.assertEqual(23, median([23], [7, 49]))

    def test_even_not_overlapped(self):
        self.assertEqual(36, median([23, 35], [37, 79]))

    def test_even_overlapped(self):
        self.assertEqual(36, median([23, 79], [35, 37]))

    def test_sample(self):
        self.assertEqual(2, median([1, 3], [2]))
        self.assertEqual(2.5, median([1, 2], [3, 4]))
        self.assertEqual(5, median(
            [0, 0, 0, 1, 3, 3, 5, 10],
            [4, 4, 5, 7, 7, 7, 8, 9, 9, 10]
        ))
