from unittest import TestCase

from sprint_1.excess_letter import excess_letter


class ExcessLetterTest(TestCase):
    def test_excess_letter(self):
        self.assertEqual(excess_letter("a", "ab"), "b")
        self.assertEqual(excess_letter("a", "ba"), "b")
        self.assertEqual(excess_letter("og", "goo"), "o")
        self.assertEqual(excess_letter("xtkpx", "xkctpx"), "c")

