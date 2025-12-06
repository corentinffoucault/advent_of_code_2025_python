import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day3.Day3 import Day3

class TestDay2:

    @pytest.fixture()
    def day2_instance(self):
        return Day3("")

    def test_run_1(self, day2_instance):
        mock_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day2_instance.run()
        assert result == "357"

    def test_run_2(self, day2_instance):
        mock_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day2_instance.run2()
        assert result == "3121910778619"

if __name__ == "__main__":
    unittest.main()
