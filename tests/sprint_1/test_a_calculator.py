from unittest import TestCase

from sprint_1.a_calculator import calculator


class CalculatorTest(TestCase):
    def test_empty_expression_returns_zero(self):
        self.assertEqual(0, calculator(""))

    def test_single_operand(self):
        self.assertEqual(1, calculator("1"))

    def test_simple_operation(self):
        self.assertEqual(2, calculator("5 2 /"))

    def test_multiple_operations_after_operands(self):
        self.assertEqual(-4, calculator("1 2 3 + -"))

    def test_multiple_operations_and_operands_mixed(self):
        self.assertEqual(9, calculator("1 2 + 3 *"))
