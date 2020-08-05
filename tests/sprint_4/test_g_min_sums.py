from unittest import TestCase

from sprint_4.g_min_sums import min_sums, min_sums_arrays


class MinSumsTest(TestCase):
    def test_min_sums(self):
        arrays = min_sums_arrays([1, 2, 3, 4], [1, 2, 3, 4], 16)
        heap = min_sums([1, 2, 3, 4], [1, 2, 3, 4], 16)

        self.assertEqual(
            arrays,
            heap
        )
