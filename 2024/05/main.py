import os
from collections import defaultdict, deque

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input(sample_filename=None):
    rules: list[list[int]] = []
    updates: list[list[int]] = []

    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        for line in i.readlines():
            if line == "\n":
                continue
            if "|" in line:
                rules.append(list(map(int, line.replace("\n", "").split("|"))))
            else:
                updates.append(list(map(int, line.replace("\n", "").split(","))))
    return rules, updates    

def get_relevant_rules(update, rules):
    return [rule for rule in rules if rule[0] in update and rule[1] in update]

def is_valid_update(update, rules):
    for rule in rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def sort_update(update: list[int], rules: list[list[int]]) -> list[int]:
    # Directed Acyclic Graph (had to get the hint for this one)
    graph = defaultdict(list)
    in_degree = {item: 0 for item in update}
    for a, b in rules:
        graph[a].append(b)
        in_degree[b] += 1
    queue = deque([item for item in update if in_degree[item] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_list

def part_01():
    rules, updates = get_input()
    total = 0
    for update in updates:
        relevant_rules = get_relevant_rules(update, rules)
        if is_valid_update(update, relevant_rules):
            total += update[len(update) // 2]
    print(f"Day 05, part 1: {total}")

def part_02():
    rules, updates = get_input()
    total = 0
    for update in updates:
        relevant_rules = get_relevant_rules(update, rules)
        if not is_valid_update(update, relevant_rules):
            sorted_update = sort_update(update, relevant_rules)
            total += sorted_update[len(sorted_update) // 2]
    print(f"Day 05, part 2: {total}")

part_01()
part_02()
