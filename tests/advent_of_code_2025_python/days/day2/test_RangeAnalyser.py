import unittest

from advent_of_code_2025_python.days.day2.RangeAnalyser import RangeAnalyser

class TestRangeAnalyser:

    def test_sum_duplicated_sequence_fast(self):
        result = RangeAnalyser.sum_duplicated_sequence_fast(11, 22)
        assert result == 33
        result = RangeAnalyser.sum_duplicated_sequence_fast(95, 115)
        assert result == 99
        result = RangeAnalyser.sum_duplicated_sequence_fast(998, 1012)
        assert result == 1010
        result = RangeAnalyser.sum_duplicated_sequence_fast(1188511880, 1188511890)
        assert result == 1188511885
        result = RangeAnalyser.sum_duplicated_sequence_fast(222220, 222224)
        assert result == 222222

        result = RangeAnalyser.sum_duplicated_sequence_fast(1698522, 1698528)
        assert result == 0
        result = RangeAnalyser.sum_duplicated_sequence_fast(446443, 446449)
        assert result == 446446
        result = RangeAnalyser.sum_duplicated_sequence_fast(38593856, 38593862)
        assert result == 38593859
        result = RangeAnalyser.sum_duplicated_sequence_fast(565653, 565659)
        assert result == 0
        result = RangeAnalyser.sum_duplicated_sequence_fast(824824821, 824824827)
        assert result == 0
        result = RangeAnalyser.sum_duplicated_sequence_fast(2121212118, 2121212124)
        assert result == 0

    def test_sum_repeated_sequence_fast(self):
        result = RangeAnalyser.sum_repeated_sequence_fast(11, 22)
        assert result == 33
        result = RangeAnalyser.sum_repeated_sequence_fast(95, 115)
        assert result == 210
        result = RangeAnalyser.sum_repeated_sequence_fast(998, 1012)
        assert result == 2009
        result = RangeAnalyser.sum_repeated_sequence_fast(1188511880, 1188511890)
        assert result == 1188511885
        result = RangeAnalyser.sum_repeated_sequence_fast(222220, 222224)
        assert result == 222222

        result = RangeAnalyser.sum_repeated_sequence_fast(1698522, 1698528)
        assert result == 0
        result = RangeAnalyser.sum_repeated_sequence_fast(446443, 446449)
        assert result == 446446
        result = RangeAnalyser.sum_repeated_sequence_fast(38593856, 38593862)
        assert result == 38593859
        result = RangeAnalyser.sum_repeated_sequence_fast(565653, 565659)
        assert result == 565656
        result = RangeAnalyser.sum_repeated_sequence_fast(824824821, 824824827)
        assert result == 824824824
        result = RangeAnalyser.sum_repeated_sequence_fast(2121212118, 2121212124)
        assert result == 2121212121

if __name__ == "__main__":
    unittest.main()
