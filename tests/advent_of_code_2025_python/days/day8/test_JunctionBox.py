import unittest

import pytest

from advent_of_code_2025_python.days.day8.JunctionBox import JunctionBox

class TestJunctionBox:

    @pytest.mark.parametrize(
        "x, y, z, result",
        [
            (162, 817, 812, 0),
            (57 , 618, 57 , 787.814),
            (906, 360, 560, 908.784),
        ]
    )
    def test_get_straight_line_distance(self, x: int, y: int, z: int, result: float):
        junction_box_1 = JunctionBox(162,817,812)
        junction_box_2 = JunctionBox(x,y,z)

        assert junction_box_1.get_straight_line_distance(junction_box_2) == pytest.approx(result, 0.001)
        assert junction_box_2.get_straight_line_distance(junction_box_1) == pytest.approx(result, 0.001)

    @pytest.mark.parametrize(
        "last_join",
        [
            [2, 0],
            [2, 1],
            [0, 2],
            [1, 2],
        ]
    )
    def test_join_other_junction_box_diff_size_always_same_parent(self, last_join: list[int]):
        junction_box_1 = JunctionBox(162,817,812)
        junction_box_2 = JunctionBox(163,817,812)
        junction_box_3 = JunctionBox(164,817,812)

        boxes = [junction_box_1, junction_box_2, junction_box_3]
        TestJunctionBox.assert_roots_and_sizes(boxes, [junction_box_1, junction_box_2, junction_box_3], [1, 1, 1], [1, 1, 1])

        junction_box_1.join_other_junction_box(junction_box_2)
        TestJunctionBox.assert_roots_and_sizes(boxes, [junction_box_1, junction_box_1, junction_box_3], [2, 1, 1], [2, 2, 1])

        boxes[last_join[0]].join_other_junction_box(boxes[last_join[1]])
        TestJunctionBox.assert_roots_and_sizes(boxes, [junction_box_1, junction_box_1, junction_box_1], [3, 1, 1], [3, 3, 3])

    @staticmethod
    def assert_roots_and_sizes(boxes, expected_roots, expected_sizes, expected_root_sizes):
        for box, expected_root in zip(boxes, expected_roots):
            assert box.get_root() == expected_root
        for box, expected_size in zip(boxes, expected_sizes):
            assert box.size == expected_size
        for box, expected_root_size in zip(boxes, expected_root_sizes):
            assert box.get_root().size == expected_root_size

if __name__ == "__main__":
    unittest.main()
