import re, operator, math
from functools import reduce
from collections import defaultdict, OrderedDict

with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))

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
            case = int(test.group(1))
            testcase[monkey] = int(case)
        
        target_01 = re.search(r'If true: throw to monkey (\d+)', l)
        if target_01:
            target_true[monkey] = int(target_01.group(1))
            
        target_02 = re.search(r'If false: throw to monkey (\d+)', l)
        if target_02:
            target_false[monkey] = int(target_02.group(1))
    return [items, operations, testcase, target_true, target_false]
            
def simulate(rounds=20, reduce_func=None):
    inspections = defaultdict(int)
    monkey_items, operations, testcase, target_true, target_false = get_monkeys()
    
    if not reduce_func:
        # had to look this up
        def lcm(arr):
            l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
            return l
        print(f'LCM: {lcm(testcase.values())}')
        reduce_func = lambda x: x % lcm(testcase.values())
    
    for _ in range(rounds):
        for monkey in range(len(monkey_items.keys())):
            items = monkey_items[monkey]
            for item in items:
                inspections[monkey] += 1
                right = operations[monkey][1]
                if right == "old":
                    right = item
                new_value = reduce_func(operators[operations[monkey][0]](item, int(right)))
                if new_value % testcase[monkey] == 0:
                    monkey_items[target_true[monkey]].append(new_value)
                else:
                    monkey_items[target_false[monkey]].append(new_value)
            monkey_items[monkey] = []
    return operator.mul(*sorted(inspections.values(), reverse=True)[:2])

def part_01():
    print(f'Part 1: {simulate(20, lambda x: x // 3)}')

def part_02():
    print(f'Part 2: {simulate(10000)}')


part_01()
part_02()
