from unittest import TestCase

from sprint_1.combinations import combinations


class CombinationsTest(TestCase):
    def test_combinations(self):
        self.assertEqual(combinations(""), [])
        self.assertEqual(combinations("2"), ["a", "b", "c"])
        self.assertEqual(
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            combinations("23")
        )
