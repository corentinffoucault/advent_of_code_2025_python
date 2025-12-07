import unittest

from advent_of_code_2025_python.days.day5.FreshPart import FreshPart


class TestFreshPart:

    def test_contains(self):
        fresh_part = FreshPart(2, 10)
        assert fresh_part.contains(2)
        assert fresh_part.contains(10)
        assert fresh_part.contains(5)
        assert not fresh_part.contains(11)
        assert not fresh_part.contains(1)

    def test_nb_elements(self):
        fresh_part = FreshPart(2, 10)
        assert fresh_part.nb_elements() == 9

    def test_mergeable(self):
        fresh_part = FreshPart(2, 10)
        assert fresh_part.mergeable(FreshPart(0, 2))
        assert fresh_part.mergeable(FreshPart(10, 12))
        assert fresh_part.mergeable(FreshPart(3, 4))
        assert fresh_part.mergeable(FreshPart(1, 11))
        assert not fresh_part.mergeable(FreshPart(0, 1))
        assert not fresh_part.mergeable(FreshPart(11, 12))

    def test_merge_include(self):
        fresh_part = FreshPart(2, 10)
        fresh_part_1 = FreshPart(3, 9)
        fresh_part_2 = FreshPart(1, 11)

        fresh_part.merge(fresh_part_1)
        assert fresh_part.start == 2
        assert fresh_part.end == 10

        fresh_part.merge(fresh_part_2)
        assert fresh_part.start == 1
        assert fresh_part.end == 11

    def test_merge_just_border(self):
        fresh_part = FreshPart(2, 10)
        fresh_part_1 = FreshPart(0, 2)
        fresh_part_2 = FreshPart(10, 11)

        fresh_part.merge(fresh_part_1)
        assert fresh_part.start == 0
        assert fresh_part.end == 10

        fresh_part.merge(fresh_part_2)
        assert fresh_part.start == 0
        assert fresh_part.end == 11

    def test_merge_border(self):
        fresh_part = FreshPart(2, 10)
        fresh_part_1 = FreshPart(0, 3)
        fresh_part_2 = FreshPart(9, 11)

        fresh_part.merge(fresh_part_1)
        assert fresh_part.start == 0
        assert fresh_part.end == 10

        fresh_part.merge(fresh_part_2)
        assert fresh_part.start == 0
        assert fresh_part.end == 11

if __name__ == "__main__":
    unittest.main()
