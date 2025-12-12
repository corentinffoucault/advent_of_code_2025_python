import unittest

import pytest
from hypothesis import given
import hypothesis.strategies as st

from advent_of_code_2025_python.days.day7.BeamLevel import BeamLevel

class TestBeamLevel:

    @pytest.mark.parametrize(
        "level, previous, expected_positions, expected_split",
        [
            ("..^.............", set(), set(),  0),
            ("..^.............", {2},   {1, 3}, 1),
            (".......^........", {0},   {0},    0),
            (".......^........", {7},   {6, 8},   1),
            ("^...............", {0},   {1},    1),
            ("...............^", {15},  {14},   1),
        ]
    )
    def test_split_get_new_beam_position(self, level, previous, expected_positions, expected_split):
        beam_level = BeamLevel(level)
        next_pos, nb_split = beam_level.get_new_beam_position(previous)
        assert next_pos == expected_positions
        assert nb_split == expected_split

    @pytest.mark.parametrize(
        "level, previous, expected_positions, expected_split",
        [
            ("..S.............", set(),   {2},    0),
            ("..S.............", {1},     {1, 2}, 0),
            (".......S........", set(),   {7},    0),
            (".......S........", {1},     {1, 7}, 0),
        ]
    )
    def test_start_level_new_beam_position(self, level, previous, expected_positions, expected_split):
        beam_level = BeamLevel(level)
        next_pos, nb_split = beam_level.get_new_beam_position(previous)
        assert next_pos == expected_positions
        assert nb_split == expected_split

    @given(st.sets(
        st.integers(min_value=0, max_value=14),
        max_size=10
    ))
    def test_empty_level_get_new_beam_position(self, previous):
        beam_level = BeamLevel("."*15)
        next_pos, nb_split = beam_level.get_new_beam_position(previous)
        assert next_pos == previous
        assert nb_split == 0



    @given(st.dictionaries(
        keys=st.integers(min_value=0, max_value=14),
        values=st.integers(min_value=1, max_value=100),
        max_size=10
    ))
    def test_empty_level_get_all_beam_path(self, previous):
        beam_level = BeamLevel("."*15)
        next_pos = beam_level.get_all_beam_path(previous)
        assert next_pos == previous

    @pytest.mark.parametrize(
        "level, previous, expected_path",
        [
            (".S..............", {},              {1: 1}),
            (".S..............", {1: 3},          {1: 4}),
            (".......S........", {},              {7: 1}),
            (".......S........", {1: 3},          {1: 3, 7: 1}),
        ]
    )
    def test_start_level_get_all_beam_path(self, level, previous, expected_path):
        beam_level = BeamLevel(level)
        next_pos = beam_level.get_all_beam_path(previous)
        assert next_pos == expected_path

    @pytest.mark.parametrize(
        "level, previous, expected_path",
        [
            ("..^.............", {},              {}),
            ("..^.............", {2: 3},          {1: 3, 3: 3}),
            (".......^........", {},              {}),
            (".......^........", {7: 3},          {6: 3, 8: 3}),
            ("^...............", {0: 3},          {1: 3}),
            ("...............^", {15: 3},         {14: 3}),
            ("......^.^.......", {6:3, 7:2, 8:4}, {5:3, 7:9, 9:4}),
        ]
    )
    def test_split_level_get_all_beam_path(self, level, previous, expected_path):
        beam_level = BeamLevel(level)
        next_pos = beam_level.get_all_beam_path(previous)
        assert next_pos == expected_path


if __name__ == "__main__":
    unittest.main()
