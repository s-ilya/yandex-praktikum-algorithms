from unittest import TestCase

from sprint_2.f_sorted_strings import min_indices_removed


class SortedStringsTest(TestCase):
    def test_example_one(self):
        self.assertEqual(
            1,
            min_indices_removed([
                'cba',
                'daf',
                'ghi'
            ])
        )

    def test_example_two(self):
        self.assertEqual(
            0,
            min_indices_removed(['a', 'b'])
        )
