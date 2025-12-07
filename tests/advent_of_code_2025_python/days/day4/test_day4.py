import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day4.Day4 import Day4

class TestDay4:

    @pytest.fixture()
    def day4_instance(self):
        return Day4("")

    def test_run_1(self, day4_instance):
        mock_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day4_instance.run()
        assert result == "13"

    def test_run_2(self, day4_instance):
        mock_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day4_instance.run2()
        assert result == "43"

if __name__ == "__main__":
    unittest.main()
