import re
import operator
from typing import List
from collections import deque, defaultdict, OrderedDict

with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))


class Monkey:
    items: List[int] = []
    operation, test_conditio, outcome_true, outcome_false = None, None, None, None
    def __init__(self, items: List[int], operation: str, test_condition, outcome_true, outcome_false) -> None:
        self.items = items
        self.operation = operation
        self.test_condition = int(test_condition)
        self.outcome_true = int(outcome_true)
        self.outcome_false = int(outcome_false)

    def test(self, div: str):
        pass
    
    

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
def get_monkeys():
    items = OrderedDict()
    operations = OrderedDict()
    testcase = OrderedDict()
    target_true = OrderedDict()
    target_false = OrderedDict()
    monkey = 0
    for l in map(str.strip, inputs):
        if l == "":
            monkey += 1
        if l.startswith("Monkey"): continue
        starting_items = re.search(r'Starting items: (.+)', l)
        if starting_items:
            items[monkey] = list(map(int, starting_items.group(1).split(', ')))
        
        operation = re.search(r'Operation: (\w+)', l)
        if operation:
            _, op, right = l.split(' ')[3:]
            operations[monkey] = [op, right]
        test = re.search(r'Test: divisible by (\d+)', l)
        if test:
            testcase[monkey] = int(test.group(1))
        
        target_01 = re.search(r'If true: throw to monkey (\d+)', l)
        if target_01:
            target_true[monkey] = int(target_01.group(1))
            
        target_02 = re.search(r'If false: throw to monkey (\d+)', l)
        if target_02:
            target_false[monkey] = int(target_02.group(1))
    return [items, operations, testcase, target_true, target_false]
            
def part_01():
    inspections = defaultdict(int)
    monkey_items, operations, testcase, target_true, target_false = get_monkeys()
    for _ in range(20):
        for monkey in range(len(monkey_items.keys())):
            items = monkey_items[monkey]
            for item in items:
                inspections[monkey] += 1
                right = operations[monkey][1]
                if right == "old":
                    right = item
                new_value = operators[operations[monkey][0]](item, int(right)) // 3
                if new_value % testcase[monkey] == 0:
                    monkey_items[target_true[monkey]].append(new_value)
                else:
                    monkey_items[target_false[monkey]].append(new_value)
            monkey_items[monkey] = []
    print (inspections)
    print(f"Part 1: {operator.mul(*sorted(inspections.values(), reverse=True)[:2])}")

part_01()
