from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day3.VoltageAnalyser import VoltageAnalyser


class Day3(ADay):

    def run(self):
        banks = self._get_data()
        sum_voltage = 0
        voltage_analyser = VoltageAnalyser(2)
        for bank in banks:
            sum_voltage += voltage_analyser.top_n_in_order(bank)
        return f"{sum_voltage}"

    def run2(self):
        banks = self._get_data()
        sum_voltage = 0
        voltage_analyser = VoltageAnalyser(12)
        for bank in banks:
            sum_voltage += voltage_analyser.top_n_in_order(bank)
        return f"{sum_voltage}"

    def _get_data(self) -> list[str]:
        with open(self.resource_path) as f:
            return [line.strip() for line in f]
