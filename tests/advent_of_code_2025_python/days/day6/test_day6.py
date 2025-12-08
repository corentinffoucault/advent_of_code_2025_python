import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day6.Day6 import Day6

class TestDay6:

    @pytest.fixture()
    def day6_instance(self):
        return Day6("")

    def test_run_1(self, day6_instance):
        mock_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day6_instance.run()
        assert result == "4277556"

    def test_run_2(self, day6_instance):
        mock_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day6_instance.run2()
        assert result == "3263827"

if __name__ == "__main__":
    unittest.main()
