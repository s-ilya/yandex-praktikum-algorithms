from unittest import TestCase

from sprint_2.a_photocopies import get_max_photos_to_backup


class PhotocopiesTest(TestCase):
    def test_empty(self):
        self.assertEqual(0, get_max_photos_to_backup([]))

    def test_single(self):
        self.assertEqual(0, get_max_photos_to_backup([100]))

    def test_two(self):
        self.assertEqual(1, get_max_photos_to_backup([1, 2]))

    def test_three(self):
        self.assertEqual(3, get_max_photos_to_backup([3, 2, 1]))

    def test_zeroes(self):
        self.assertEqual(3, get_max_photos_to_backup([3, 0, 2, 0, 1]))

    def test_sample(self):
        self.assertEqual(11, get_max_photos_to_backup([8, 7, 4, 3]))

    def test_sample2(self):
        self.assertEqual(16, get_max_photos_to_backup([8, 7, 7, 6, 5]))

    def test_sample3(self):
        self.assertEqual(12, get_max_photos_to_backup([1, 6, 9, 8]))
