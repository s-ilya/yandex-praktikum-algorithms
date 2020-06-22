from unittest import TestCase

from b_transpose import transpose


class TransposeTest(TestCase):
    def test_transpose(self):
        self.assertEqual([], transpose([]))
        self.assertEqual([[1]], transpose([[1]]))
        self.assertEqual([[1], [2]], transpose([[1, 2]]))
        self.assertEqual([[1, 2]], transpose([[1], [2]]))
        self.assertEqual([[1, 3], [2, 4]], transpose([[1, 2], [3, 4]]))
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
