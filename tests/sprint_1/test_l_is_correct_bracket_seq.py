from unittest import TestCase, skip
from random import choice, randrange

from sprint_1.l_is_correct_bracket_seq import is_correct_bracket_seq


class IsCorrectBracketSeqTest(TestCase):
    def test_empty(self):
        self.assertTrue(is_correct_bracket_seq(""))

    def test_single(self):
        self.assertFalse(is_correct_bracket_seq("("))

    def test_simple_pair(self):
        self.assertTrue(is_correct_bracket_seq("()"))

    def test_nested_pair(self):
        self.assertTrue(is_correct_bracket_seq("{()}"))

    def test_sibling_pair(self):
        self.assertTrue(is_correct_bracket_seq("(){}"))

    def test_unmatched_in_middle(self):
        self.assertFalse(is_correct_bracket_seq("{(}"))

    def test_first_closing_bracket(self):
        self.assertFalse(is_correct_bracket_seq("]"))

    @skip('Random testing')
    def test_random(self):
        brackets = ['(', ')', '{', '}', '[', ']']
        sequence_length = randrange(0, 100)
        sequence_list = list()

        for _ in range(0, 1000):
            for _ in range(sequence_length):
                sequence_list.append(choice(brackets))

            sequence = "".join(sequence_list)

            try:
                is_correct_bracket_seq(sequence)
            except:
                print(sequence)
                self.fail()

        self.assertTrue(True)
