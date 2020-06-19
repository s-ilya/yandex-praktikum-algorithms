from unittest import TestCase

from binary_sum import binary_sum


class BinarySumTest(TestCase):
    def test_simple_cases(self):
        self.assertEqual(binary_sum("1", "0"), "1")
        self.assertEqual(binary_sum("0", "1"), "1")
        self.assertEqual(binary_sum("0", "0"), "0")
        self.assertEqual(binary_sum("1", "1"), "10")
        self.assertEqual(binary_sum("100", "1"), "101")
        self.assertEqual(binary_sum("1010", "1011"), "10101")
        self.assertEqual(binary_sum(format(9223372036854775807, 'b'), format(9223372036854775807, 'b')),
                         format(9223372036854775807 + 9223372036854775807, 'b'))
