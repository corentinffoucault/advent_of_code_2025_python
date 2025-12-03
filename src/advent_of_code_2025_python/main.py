from advent_of_code_2025_python.days.day1.Day1 import Day1
from advent_of_code_2025_python.lib.path_utils import get_resources_path

days = [
    Day1(get_resources_path(1)),
]

def main():
    day_index = 0
    while day_index < 1 or day_index > 25:
        day_index = int(input("Merci d’indiquer un jour (1-25): "))

    day = days[day_index - 1]
    print("result day", day_index, day.run())
    print("result2 day", day_index, day.run2())

if __name__ == "__main__":
    main()
