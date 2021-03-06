from unittest import TestCase

from sprint_2.a_schedule import max_disjoint_segments


class MaxDisjointSegmentsTest(TestCase):
    def test_empty(self):
        self.assertEqual([], max_disjoint_segments([]))

    def test_single(self):
        segment = [1, 2]
        self.assertEqual([segment], max_disjoint_segments([segment]))

    def test_two_intersected_first_ends_earlier(self):
        first = [1, 1.5]
        second = [1.3, 2]

        self.assertEqual([first], max_disjoint_segments([first, second]))

    def test_two_intersected_second_ends_earlier(self):
        first = [1, 2.1]
        second = [1.3, 2]

        self.assertEqual([second], max_disjoint_segments([first, second]))

    def test_two_disjoint_sorted_initially(self):
        first = [1, 2]
        second = [2, 4]

        self.assertEqual([first, second], max_disjoint_segments([first, second]))

    def test_two_disjoint_unsorted_initially(self):
        first = [2, 4]
        second = [1, 2]

        self.assertEqual([second, first], max_disjoint_segments([first, second]))

    def test_two_one_contains_another(self):
        first = [1, 10]
        second = [2, 8]

        self.assertEqual([second], max_disjoint_segments([first, second]))

    def test_two_zero_lengths(self):
        first = [1, 1]
        second = [1, 1]

        self.assertEqual([first, second], max_disjoint_segments([first, second]))

    def test_same_end_different_start(self):
        first = [5, 10]
        second = [1, 10]

        self.assertEqual([second], max_disjoint_segments([first, second]))
