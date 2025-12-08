import unittest

from advent_of_code_2025_python.days.day6.Calculator import Calculator


class TestFreshPart:

    def test_calculator_add(self):
        calculator = Calculator(["123", " 45", "  6"], "+")
        assert calculator.solve() == 174
        assert calculator.solve_right_left() == 381

    def test_calculator_mul(self):
        calculator = Calculator(["123", " 45", "  6"], "*")
        assert calculator.solve() == 33210
        assert calculator.solve_right_left() == 8544

if __name__ == "__main__":
    unittest.main()
