import unittest

from advent_of_code_2025_python.days.day3.VoltageAnalyser import VoltageAnalyser

class TestVoltageAnalyser:

    def test_top_n_in_order_small_size(self):
        voltage_analyser = VoltageAnalyser(2)
        result = voltage_analyser.top_n_in_order("987654321111111")
        assert result == 98
        result = voltage_analyser.top_n_in_order("811111111111119")
        assert result == 89
        result = voltage_analyser.top_n_in_order("234234234234278")
        assert result == 78
        result = voltage_analyser.top_n_in_order("818181911112111")
        assert result == 92

    def test_top_n_in_order_big_size(self):
        voltage_analyser = VoltageAnalyser(12)
        result = voltage_analyser.top_n_in_order("987654321111111")
        assert result == 987654321111
        result = voltage_analyser.top_n_in_order("811111111111119")
        assert result == 811111111119
        result = voltage_analyser.top_n_in_order("234234234234278")
        assert result == 434234234278
        result = voltage_analyser.top_n_in_order("818181911112111")
        assert result == 888911112111

if __name__ == "__main__":
    unittest.main()
