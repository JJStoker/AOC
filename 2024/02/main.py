import os

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input():
    reports = []

    with open("sample.txt" if DEBUG else "input.txt", "r") as i:
        reports = map(
            lambda l: list(map(int, l.replace("\n", "").split(" "))), i.readlines()
        )
    return list(reports)

def check_level(level, prev_level, descending):
    diff = abs(level - prev_level)
    if diff > 3:
        return False
    if diff == 0:
        return False
    if descending and level < prev_level:
        return False
    if not descending and level > prev_level:
        return False
    return True

def check_report(report):
    # set flag to determine if the levels are increasing or decreasing
    descending = 0 if report[0] > report[1] else 1
    for i, level in enumerate(report):
        if i == 0:
            continue
        if not check_level(level, report[i - 1], descending):
            return False
    return True

def check_report_dampened(report):
    if check_report(report):
        return True
    
    for i in range(len(report)):
        replaced_report = report[:i] + report[i+1:]
        print (replaced_report  )
        if check_report(replaced_report):
            return True
    return False

def part_01():
    reports = get_input()
    print(f"Day 02, part 1: {len([report for report in reports if check_report(report)])}")

def part_02():
    reports = get_input()
    print(f"Day 02, part 2: {len([report for report in reports if check_report_dampened(report)])}")

part_01()
part_02()
