import re
from functools import reduce

from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day6.Calculator import Calculator

class Day6(ADay):

    def run(self):
        calculator = self._get_data()
        result = reduce(lambda acc, c: acc + c.solve(), calculator, 0)
        return f"{result}"

    def run2(self):
        calculator = self._get_data()
        result = reduce(lambda acc, c: acc + c.solve_right_left(), calculator, 0)
        return f"{result}"

    def _get_data(self) -> list[Calculator]:
        with open(self.resource_path) as f:
            lines = f.readlines()

        operators = re.findall(r'\S\s+',  lines[-1].rstrip("\n"))
        data_lines = [line.rstrip("\n") for line in lines[:-1]]

        calculators = []
        position = 0

        for index, operator_in_string in enumerate(operators[:-1]):
            size = len(operator_in_string)-1
            values = [line[position:position+size] for line in data_lines]
            calculators.append(Calculator(values, operator_in_string.strip()))
            position+=size+1

        values = [line[position:] for line in data_lines]
        calculators.append(Calculator(values, operators[-1].strip()))
        return calculators