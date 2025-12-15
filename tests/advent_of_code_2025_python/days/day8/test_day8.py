import unittest
import pytest

from unittest.mock import patch, mock_open
from advent_of_code_2025_python.days.day8.Day8 import Day8

class TestDay6:

    @pytest.fixture()
    def day8_instance(self):
        return Day8("")

    def test_run_1(self, day8_instance):
        mock_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day8_instance.run(10)
        assert result == "40"

    def test_run_2(self, day8_instance):
        mock_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = day8_instance.run2()
        assert result == "25272"

if __name__ == "__main__":
    unittest.main()
