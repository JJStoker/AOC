import os

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input(sample_filename=None):
    inputs = []

    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        inputs = map(
            lambda l: l.replace("\n", "").split("|") if "|" in l else l.replace("\n", "").split(","),
            i.readlines()
        )
    return list(inputs)

def part_01():
    rules: list[list[int]] = []
    updates: list[list[int]] = []
    for input in get_input():
        if input == [""]:
            continue
        if len(input) == 2:
            rules.append(list(map(int, input)))
        else:
            updates.append(list(map(int, input)))
    
    
    def is_valid_update(update):
        relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
        for rule in relevant_rules:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
        return True
    
    total = 0
    for update in updates:
        if is_valid_update(update):
            total += update[len(update) // 2]
    
    print(f"Day 05, part 1: {total}")

def part_02():
    grid = get_input()
    print(f"Day 05, part 2: {0}")

part_01()
# part_02()
