import unittest
from pathlib import Path
from advent_of_code_2025_python.days.day1.Day1 import Day1

class TestDay1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_file = Path("test_input.txt")
        test_data = ["R10", "L60", "R120", "L250", "R75", "L30", "R300", "L0"]
        cls.test_file.write_text("\n".join(test_data))

    @classmethod
    def tearDownClass(cls):
        cls.test_file.unlink()

    def setUp(self):
        self.day = Day1(str(self.test_file))

    def test_run_1(self):
        self.assertEqual(self.day.run(), "password: 1")

    def test_run_2(self):
        self.assertEqual(self.day.run2(), "password: 9")

if __name__ == "__main__":
    unittest.main()
