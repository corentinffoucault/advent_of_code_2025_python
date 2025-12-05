import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day2.Day2 import Day2

class TestDay2:

    @pytest.fixture()
    def day2_instance(self):
        return Day2("")

    def test_run_1(self, day2_instance):
        mock_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day2_instance.run()
        assert result == "password: 1227775554"

    def test_run_2(self, day2_instance):
        mock_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day2_instance.run2()
        assert result == "password: 4174379265"

if __name__ == "__main__":
    unittest.main()
