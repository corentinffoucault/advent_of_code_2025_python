from functools import reduce

from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day7.BeamLevel import BeamLevel

class Day7(ADay):

    def run(self):
        beam_levels = self._get_data()

        beam_position = set()
        nb_split = 0
        for beam_level in beam_levels:
            beam_position, split_time = beam_level.get_new_beam_position(beam_position)
            nb_split += split_time
        return f"{nb_split}"

    def run2(self):
        beam_levels = self._get_data()

        beam_position = dict()
        for beam_level in beam_levels:
            beam_position = beam_level.get_all_beam_path(beam_position)
            print(beam_position)

        result = 0
        for nb_path in beam_position.values():
            result+=nb_path
        return f"{result}"

    def _get_data(self) -> list[BeamLevel]:
        beam_levels = []
        with open(self.resource_path) as f:
            for line in f:
                beam_levels.append(BeamLevel(line))
        return beam_levels