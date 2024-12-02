import os

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input():
    reports = []

    with open("sample.txt" if DEBUG else "input.txt", "r") as i:
        reports = map(
            lambda l: list(map(int, l.replace("\n", "").split(" "))), i.readlines()
        )
    return list(reports)


def part_01():
    reports = get_input()

    def check_report(report):
        # set flag to determine if the levels are increasing or decreasing
        dir = 0 if report[0] > report[1] else 1
        for i, level in enumerate(report):
            if i == 0:
                continue
            diff = abs(level - report[i - 1])
            if diff > 3:
                return False
            if diff == 0:
                return False
            if dir and level < report[i - 1]:
                return False
            if not dir and level > report[i - 1]:
                return False
        return True

    print(f"Day 02, part 1: {len([report for report in reports if check_report(report)])}")

part_01()
