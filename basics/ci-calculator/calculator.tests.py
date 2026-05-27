import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_adds_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_subtracts_two_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiplies_two_numbers(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divides_two_numbers(self):
        self.assertEqual(divide(12, 3), 4)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(divide(10, 0))


if __name__ == "__main__":
    unittest.main()