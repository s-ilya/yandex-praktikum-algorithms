from unittest import TestCase

from sprint_1.three_days_stats import three_days_stats


class ThreeDaysStatsTest(TestCase):
    def test_three_days_stats(self):
        self.assertEqual(
            -1,
            three_days_stats([1])
        )
        self.assertEqual(
            -1,
            three_days_stats([1, 2])
        )
        self.assertEqual(
            -1,
            three_days_stats([1, 2, 0])
        )
        self.assertEqual(
            -1,
            three_days_stats([1, 2, -3])
        )
        self.assertEqual(
            12,
            three_days_stats([-1, 4, -3])
        )
        self.assertEqual(
            6,
            three_days_stats([-2, -1, 3, -1, -2])
        )
        self.assertEqual(
            -1,
            three_days_stats([-2, 1, 1, -1, -2])
        )
