import unittest

from advent_of_code_2025_python.days.day4.RollCleaner import RollCleaner


class TestVoltageAnalyser:

    def test_count_deletable_roll(self):
        data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        grid = [list(line) for line in data.splitlines()]

        nb_roll_removed = RollCleaner().count_deletable_roll(grid)
        assert nb_roll_removed == 13

    def test_count_deletable_roll_with_replace(self):
        data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        grid = [list(line) for line in data.splitlines()]

        nb_roll_removed, new_map = RollCleaner().count_deletable_roll_with_replace(grid)
        assert nb_roll_removed == 30

        expected_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '@', '@', '.', '.', '.', '.', '.', '.', '.'], ['.', '@', '@', '@', '@', '.', '.', '.', '.', '.'], ['.', '.', '@', '@', '@', '@', '.', '.', '.', '.'], ['.', '.', '.', '@', '@', '@', '@', '.', '.', '.'], ['.', '.', '@', '@', '@', '@', '@', '@', '.', '.'], ['.', '.', '.', '@', '.', '@', '.', '@', '@', '.'], ['.', '.', '@', '@', '@', '.', '@', '@', '@', '.'], ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'], ['.', '.', '.', '.', '@', '@', '@', '.', '.', '.']]
        print(new_map)
        assert new_map == expected_grid

if __name__ == "__main__":
    unittest.main()
