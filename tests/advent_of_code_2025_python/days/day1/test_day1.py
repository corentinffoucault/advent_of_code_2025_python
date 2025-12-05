import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day1.Day1 import Day1

class TestDay1:

    @pytest.fixture()
    def day1_instance(self):
        return Day1("")

    def test_run_1(self, day1_instance):
        mock_data = "R10\nL60\nR120\nL250\nR75\nL30\nR300\nL0"

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day1_instance.run()
        assert result == "password: 1"

    def test_run_2(self, day1_instance):
        mock_data = "R10\nL60\nR120\nL250\nR75\nL30\nR300\nL0"

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day1_instance.run2()
        assert result == "password: 9"

if __name__ == "__main__":
    unittest.main()
