from advent_of_code_2025_python.days.ADay import ADay

class Day1(ADay):

    _CIRCLE_SIZE = 100
    _INIT_POS = 50

    def run(self):
        pos = self._INIT_POS
        nb_zero = 0
        data = self._get_data()
        for move in data:
            pos = self._apply_move_1(pos, move)
            if pos == 0:
                nb_zero += 1
        return f"password: {nb_zero}"

    def run2(self):
        pos = self._INIT_POS
        nb_zero = 0
        data = self._get_data()
        for move in data:
            pos, tmp_nb_zero = self._apply_move_2(pos, move)
            nb_zero += tmp_nb_zero
            if pos == 0:
                nb_zero += 1
        return f"password: {nb_zero}"

    def _apply_move_1(self, pos: int, move: tuple[str, int]) -> int:
        delta = move[1] if move[0] == 'R' else -move[1]
        return (pos + delta) % self._CIRCLE_SIZE

    def _apply_move_2(self, pos: int, move: tuple[str, int]) -> tuple[int, int]:
        direction, steps = move
        nb_full_cycles = steps // self._CIRCLE_SIZE
        remaining_steps = steps % self._CIRCLE_SIZE

        zero_crossings = nb_full_cycles

        if direction == 'L':
            new_pos = pos - remaining_steps
            if pos - remaining_steps < 0:
                zero_crossings += 1
            if pos == 0:
                zero_crossings -= 1
        else:
            new_pos = pos + remaining_steps
            if pos + remaining_steps > self._CIRCLE_SIZE:
                zero_crossings += 1

        return new_pos % self._CIRCLE_SIZE, zero_crossings

    def _get_data(self) -> list[tuple[str, int]]:
        with open(self.resource_path) as f:
            return [self._string_to_data(line.strip()) for line in f]

    @staticmethod
    def _string_to_data(data: str) -> tuple[str, int]:
        return data[0], int(data[1:])
