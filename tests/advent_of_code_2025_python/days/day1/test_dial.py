import unittest

from hypothesis import given
from hypothesis import strategies as st

from advent_of_code_2025_python.days.day1.Dial import Dial

class TestDial:

    def test_init(self):
        dial = Dial(init_pos=34, nb_value=100)
        assert dial.pos == 34
        assert dial.zero_crossings == 0

    @given(st.tuples(st.sampled_from(["L", "R"]), st.integers(min_value=0, max_value=10_000)))
    def test_zero_start_not_count(self, move):
        dial = Dial(init_pos=0, nb_value=100)
        dial.apply_move_with_zero_tracking(move)
        assert 0<=dial.pos<=99
        assert dial.zero_crossings == (move[1] // 100)

    @given(st.integers(min_value=0, max_value=10_000))
    def test_zero_end_not_count_from_right(self, incr):
        dial = Dial(init_pos=(100-incr) % 100, nb_value=100)
        dial.apply_move_with_zero_tracking(("R", incr))
        assert dial.pos == 0
        assert dial.zero_crossings == incr // 100

    @given(st.integers(min_value=0, max_value=10_000))
    def test_zero_end_not_count_from_right(self, incr):
        dial = Dial(init_pos=(0+incr) % 100, nb_value=100)
        dial.apply_move_with_zero_tracking(("L", incr))
        assert dial.pos == 0
        assert dial.zero_crossings == incr // 100

    @given(st.integers(2, 98))
    def test_incr_over_hundred(self, incr):
        dial = Dial(init_pos=99, nb_value=100)
        dial.apply_move_with_zero_tracking(("R", incr))
        assert dial.pos == (99 + incr) % 100
        assert dial.zero_crossings == 1

    @given(st.integers(2, 99))
    def test_decr_under_zero(self, decr):
        dial = Dial(init_pos=1, nb_value=100)
        dial.apply_move_with_zero_tracking(("L", decr))
        assert dial.pos == (1-decr) % 100
        assert dial.zero_crossings == 1

    @given(st.integers(0, 98))
    def test_incr(self, pos):
        dial = Dial(init_pos=pos, nb_value=100)
        dial.apply_move_with_zero_tracking(("R", 1))
        assert dial.pos == pos + 1
        assert dial.zero_crossings == 0

    @given(st.integers(1, 99))
    def test_decr(self, pos):
        dial = Dial(init_pos=pos, nb_value=100)
        dial.apply_move_with_zero_tracking(("L", 1))
        assert dial.pos == pos - 1
        assert dial.zero_crossings == 0

    @given(st.integers(1, 99))
    def test_full_circle_identity(self, pos):
        dial = Dial(init_pos=pos, nb_value=100)

        dial.apply_move_with_zero_tracking(("R", 100))
        assert dial.pos == pos
        assert dial.zero_crossings == 1

        dial.apply_move_with_zero_tracking(("L", 100))
        assert dial.pos == pos
        assert dial.zero_crossings == 2

    @given(st.integers(0, 99), st.integers(0, 1000))
    def test_reverse_moves(self, pos, steps):
        dial = Dial(init_pos=pos, nb_value=100)
        dial.apply_move_with_zero_tracking(("R", steps))
        dial.apply_move_with_zero_tracking(("L", steps))
        assert pos == dial.pos

if __name__ == "__main__":
    unittest.main()
