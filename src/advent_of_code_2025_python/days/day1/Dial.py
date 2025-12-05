
class Dial:

    def __init__(self, init_pos: int, nb_value: int):
        self._pos = init_pos
        self._nb_value = nb_value
        self._zero_crossings = 0

    @property
    def pos(self):
        """Actual position"""
        return self._pos

    @property
    def zero_crossings(self):
        """Number of times zero was crossed"""
        return self._zero_crossings

    def apply_move_with_zero_tracking(self, move: tuple[str, int]):
        """Move the dial and count how many times zero was crossed"""
        direction, steps = move
        nb_full_cycles = steps // self._nb_value
        remaining_steps = steps % self._nb_value

        self._zero_crossings += nb_full_cycles

        if direction == 'L':
            new_pos = self._pos - remaining_steps
            if self._pos != 0 and self._pos - remaining_steps < 0:
                self._zero_crossings += 1
        else:
            new_pos = self._pos + remaining_steps
            if self._pos + remaining_steps > self._nb_value:
                self._zero_crossings += 1

        self._pos = new_pos % self._nb_value
