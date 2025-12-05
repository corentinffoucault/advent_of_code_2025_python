from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day2.RangeAnalyser import RangeAnalyser


class Day2(ADay):

    def run(self):
        data = self._get_data()
        sum_of_all_invalid = 0
        for key in data:
            start_end = key.split("-")
            sum_of_all_invalid += RangeAnalyser.sum_duplicated_sequence_fast(int(start_end[0]), int(start_end[1]))
        return f"password: {sum_of_all_invalid}"

    def run2(self):
        data = self._get_data()
        sum_of_all_invalid = 0
        for key in data:
            start_end = key.split("-")
            sum_of_all_invalid += RangeAnalyser.sum_repeated_sequence_fast(int(start_end[0]), int(start_end[1]))
        return f"password: {sum_of_all_invalid}"

    def _get_data(self) -> list[str]:
        with open(self.resource_path) as f:
            return self._string_to_data(f.readline())

    @staticmethod
    def _string_to_data(data: str) -> list[str]:
        return data.split(",")
