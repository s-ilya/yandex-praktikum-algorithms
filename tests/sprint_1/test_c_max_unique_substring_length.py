from array import array
from unittest import TestCase
from string import ascii_letters
from random import randrange, choice

from sprint_1.c_max_unique_substring_length import max_unique_substring_length


class MaxUniqueSubstringLengthTest(TestCase):
    def test_max_unique_substring_length(self):
        self.assertEqual(0, max_unique_substring_length(""))
        self.assertEqual(1, max_unique_substring_length("a"))
        self.assertEqual(1, max_unique_substring_length("aa"))
        self.assertEqual(2, max_unique_substring_length("ab"))
        self.assertEqual(2, max_unique_substring_length("aab"))
        self.assertEqual(2, max_unique_substring_length("aabb"))
        self.assertEqual(2, max_unique_substring_length("abb"))
        self.assertEqual(3, max_unique_substring_length("abcabcbb"))
        self.assertEqual(1, max_unique_substring_length("bbbbb"))
        self.assertEqual(3, max_unique_substring_length("abac"))
        self.assertEqual(4, max_unique_substring_length("wmomdu"))
        self.assertEqual(7, max_unique_substring_length("NNuSUOEAO"))

    def test_random(self):
        for _ in range(10000):
            input_length = randrange(10)
            input_list = list()

            for _ in range(input_length):
                input_list.append(choice(ascii_letters))

            input_string = "".join(input_list)
            print(input_string)
            self.assertEqual(self.__max_unique_too_long(input_string), max_unique_substring_length(input_string))

    def __max_unique_too_long(self, input_string: str) -> int:
        if len(input_string) <= 1:
            return len(input_string)

        max_length = 0

        for start_letter_index in range(len(input_string)):
            current_length = 0
            letter_frequencies = array('B', [0 for _ in range(123)])

            for current_letter_index in range(start_letter_index, len(input_string)):
                letter = input_string[current_letter_index]

                if letter_frequencies[ord(letter)] == 0:
                    letter_frequencies[ord(letter)] = 1
                    current_length += 1
                else:
                    break

            max_length = max(max_length, current_length)

        return max_length
