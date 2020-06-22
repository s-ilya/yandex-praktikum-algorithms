from unittest import TestCase

from sprint_1.not_double_number import not_double_number


class NotDoubleNumberTest(TestCase):
    def test_not_double_number(self):
        self.assertEqual(not_double_number([]), -1)
        self.assertEqual(not_double_number([1, 1]), -1)
        self.assertEqual(not_double_number([1, 2, 2]), 1)
        self.assertEqual(not_double_number([1, 3, 1, 3, 2, 3, 2]), 3)
        self.assertEqual(not_double_number([1, 1, 2, 2, 2, 2]), 2)
