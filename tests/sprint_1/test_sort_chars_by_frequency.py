from unittest import TestCase

from sprint_1.sort_chars_by_frequency import sort_chars_by_frequency


class SortCharsByFrequencyTest(TestCase):
    def test_sort_chars_by_frequency(self):
        self.assertEqual(sort_chars_by_frequency(""), "")
        self.assertEqual(sort_chars_by_frequency("a"), "a")
        self.assertEqual(sort_chars_by_frequency("ab"), "ab")
        self.assertEqual(sort_chars_by_frequency("aab"), "aab")
        self.assertEqual(sort_chars_by_frequency("ba"), "ab")
        self.assertEqual(sort_chars_by_frequency("ba"), "ab")
        self.assertEqual(sort_chars_by_frequency("baa"), "aab")
        self.assertEqual(sort_chars_by_frequency("abb"), "bba")
        self.assertEqual(sort_chars_by_frequency("bbaa"), "aabb")
        self.assertEqual(sort_chars_by_frequency("abbccc"), "cccbba")
