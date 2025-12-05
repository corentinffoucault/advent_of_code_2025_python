from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day1.Dial import Dial


class Day1(ADay):

    _CIRCLE_SIZE = 100
    _INIT_POS = 50

    def run(self):
        data = self._get_data()
        dial = Dial(self._INIT_POS, self._CIRCLE_SIZE)
        nb_zero = 0
        for move in data:
            dial.apply_move_with_zero_tracking(move)
            if dial.pos == 0:
                nb_zero += 1
        return f"password: {nb_zero}"

    def run2(self):
        data = self._get_data()
        dial = Dial(self._INIT_POS, self._CIRCLE_SIZE)
        nb_zero = 0
        for move in data:
            dial.apply_move_with_zero_tracking(move)
            if dial.pos == 0:
                nb_zero += 1
        return f"password: {nb_zero + dial.zero_crossings}"

    def _get_data(self) -> list[tuple[str, int]]:
        with open(self.resource_path) as f:
            return [self._string_to_data(line.strip()) for line in f]

    @staticmethod
    def _string_to_data(data: str) -> tuple[str, int]:
        return data[0], int(data[1:])
