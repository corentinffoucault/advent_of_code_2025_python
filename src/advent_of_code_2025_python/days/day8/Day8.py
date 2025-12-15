from functools import reduce
from itertools import combinations
from operator import mul

from advent_of_code_2025_python.days.ADay import ADay
from advent_of_code_2025_python.days.day8.JunctionBox import JunctionBox

class Day8(ADay):

    def run(self, nb_loop = 1000):
        junction_box = self._get_data()

        all_distance = {
            (first_box, second_box): first_box.get_straight_line_distance(second_box)
            for first_box, second_box in combinations(junction_box, 2)
        }

        for (box_1, box_2), _ in sorted(all_distance.items(), key=lambda x: x[1])[:nb_loop]:
            box_1.join_other_junction_box(box_2)

        circuits = {}
        for box in junction_box:
            root = box.get_root()
            circuits[root] = root.size

        circuits_by_size = sorted(circuits.values(), reverse=True)
        return f"{reduce(mul, circuits_by_size[:3], 1)}"

    def run2(self):
        junction_box = self._get_data()

        all_distance = {
            (first_box, second_box): first_box.get_straight_line_distance(second_box)
            for first_box, second_box in combinations(junction_box, 2)
        }

        result = 0

        for (box_1, box_2), _ in sorted(all_distance.items(), key=lambda x: x[1]):
            box_1.join_other_junction_box(box_2)
            if box_1.get_root().size == len(junction_box):
                result = box_1.x*box_2.x
                break

        return f"{result}"

    def _get_data(self) -> list[JunctionBox]:
        junction_box = []
        with open(self.resource_path) as f:
            for line in f:
                junction_box.append(JunctionBox(*(int(x) for x in line.split(","))))
        return junction_box