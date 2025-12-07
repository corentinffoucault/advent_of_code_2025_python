from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day4.RollCleaner import RollCleaner


class Day4(ADay):

    def run(self):
        map_of_roll = self._get_data()
        nb_roll_removed = RollCleaner().count_deletable_roll(map_of_roll)
        return f"{nb_roll_removed}"

    def run2(self):
        map_of_roll = self._get_data()
        nb_roll_removed = 0
        roll_cleaner = RollCleaner()
        while True:
            nb_current_roll_removed, map_of_roll = roll_cleaner.count_deletable_roll_with_replace(map_of_roll)
            if nb_current_roll_removed == 0:
                break
            nb_roll_removed += nb_current_roll_removed
        return f"{nb_roll_removed}"

    def _get_data(self) -> list[list[str]]:
        with open(self.resource_path) as f:
            return [list(line.strip()) for line in f]
