from unittest import TestCase

from sprint_3.a_largest_number import largest_number


class LargestNumberTest(TestCase):
    def test_empty(self):
        self.assertEqual(0, largest_number([]))

    def test_single(self):
        self.assertEqual(42, largest_number([42]))

    def test_array(self):
        self.assertEqual(910, largest_number([10, 9]))

    def test_same_first_digit(self):
        self.assertEqual(110, largest_number([1, 10]))
        self.assertEqual(12121, largest_number([121, 12]))

    def test_sample(self):
        self.assertEqual(
            56215, largest_number([15, 56, 2])
        )
        self.assertEqual(
            78321, largest_number([1, 783, 2])
        )
        self.assertEqual(
            542210, largest_number([2, 4, 5, 2, 10])
        )
