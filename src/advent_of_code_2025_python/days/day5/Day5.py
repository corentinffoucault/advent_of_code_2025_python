from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day5.FreshPart import FreshPart


class Day5(ADay):

    def run(self):
        fresh_parts, ids_to_check = self._get_data()
        result = len(ids_to_check)
        for id_to_check in ids_to_check:
            for fresh_part in fresh_parts:
                if fresh_part.contains(id_to_check):
                    break
            else:
                result -= 1
        return f"{result}"

    def run2(self):
        fresh_parts, ids_to_check = self._get_data()
        result = 0
        for fresh_part in fresh_parts:
            result += fresh_part.nb_elements()
        return f"{result}"

    def _get_data(self) -> tuple[list[FreshPart], list[int]]:
        fresh_parts = []
        ids_to_check = []
        with open(self.resource_path) as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line == "":
                    break
                fresh_part = Day5._build_fresh_part(stripped_line)
                fresh_parts = Day5.merge_fresh_part(fresh_parts, fresh_part)

            for line in f:
                ids_to_check.append(int(line.strip()))
        return fresh_parts, ids_to_check

    @staticmethod
    def _build_fresh_part(line: str) -> FreshPart:
        limits = line.split("-")
        return FreshPart(int(limits[0]), int(limits[1]))

    @staticmethod
    def merge_fresh_part(fresh_parts: list[FreshPart], fresh_part: FreshPart) -> list[FreshPart]:
        fresh_parts_merged = []

        for tmp_fresh_part in fresh_parts:
            if fresh_part.mergeable(tmp_fresh_part):
                fresh_part.merge(tmp_fresh_part)
            else:
                fresh_parts_merged.append(tmp_fresh_part)

        fresh_parts_merged.append(fresh_part)
        return fresh_parts_merged
