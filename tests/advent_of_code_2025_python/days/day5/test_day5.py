import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day5.Day5 import Day5

class TestDay5:

    @pytest.fixture()
    def day5_instance(self):
        return Day5("")

    def test_run_1(self, day5_instance):
        mock_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day5_instance.run()
        assert result == "3"

    def test_run_2(self, day5_instance):
        mock_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day5_instance.run2()
        assert result == "14"

if __name__ == "__main__":
    unittest.main()
