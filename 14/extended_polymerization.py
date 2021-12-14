import os
from functools import reduce
from collections import defaultdict
from typing import DefaultDict

INPUT_FILE = "./sample.txt" if False else "./input.txt"

polymer_template: str or None = None
pair_insertion_rules: DefaultDict = defaultdict(str)
with open(INPUT_FILE, "r") as input_file:
    for i, line in enumerate(map(str.strip, input_file.readlines())):
        if i == 0: polymer_template = line; continue
        if i == 1 or not line: continue
        combination, insertion = list(map(str.strip, line.split('->')))
        pair_insertion_rules[combination] = insertion


def get_new_polymer_template(template: str):
    new_template = list(template)
    inserted = []
    for x in range(len(template) - 1):
        insert = pair_insertion_rules[f'{template[x]}{template[x + 1]}']
        if insert:
            new_template.insert(x + len(inserted) + 1, insert)
            inserted.append(insert)
    return ''.join(new_template)

def part_1(steps=4):
    new_template = polymer_template
    for i in range(steps):
        new_template = get_new_polymer_template(new_template)
        
    counter = defaultdict(int)
    most_common = new_template[0]
    least_common = new_template[0]
    for x in list(new_template):
        counter[x] += 1
        if counter[x] > counter[most_common]:
            most_common = x
        elif counter[x] < counter[least_common]:
            least_common = x
    print(f'Part 1: {counter[most_common] - counter[least_common]}')
part_1(10)
