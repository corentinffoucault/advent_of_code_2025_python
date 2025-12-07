from advent_of_code_2025_python.days.day1.Day1 import Day1
from advent_of_code_2025_python.days.day2.Day2 import Day2
from advent_of_code_2025_python.days.day3.Day3 import Day3
from advent_of_code_2025_python.days.day4.Day4 import Day4
from advent_of_code_2025_python.days.day5.Day5 import Day5
from advent_of_code_2025_python.lib.path_utils import get_resources_path

days = [
    Day1(get_resources_path(1)),
    Day2(get_resources_path(2)),
    Day3(get_resources_path(3)),
    Day4(get_resources_path(4)),
    Day5(get_resources_path(5)),
]

def main():
    day_index = 0
    while day_index < 1 or day_index > 5:
        day_index = int(input("Merci d’indiquer un jour (1-25): "))

    day = days[day_index - 1]
    print("result day", day_index, day.run())
    print("result2 day", day_index, day.run2())

if __name__ == "__main__":
    main()
