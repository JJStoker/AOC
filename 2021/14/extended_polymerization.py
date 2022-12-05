from collections import defaultdict
from typing import DefaultDict

INPUT_FILE = "./sample.txt" if False else "./input.txt"

polymer_template: str or None = None
pair_insertion_rules: DefaultDict = defaultdict(str)
with open(INPUT_FILE, "r") as input_file:
    for i, line in enumerate(map(str.strip, input_file.readlines())):
        if i == 0:
            polymer_template = line
            continue
        if i == 1 or not line:
            continue
        combination, insertion = list(map(str.strip, line.split("->")))
        pair_insertion_rules[combination] = insertion


def part_1(steps=10):
    def get_new_polymer_template(template: str):
        new_template = list(template)
        inserted = []
        for x in range(len(template) - 1):
            insert = pair_insertion_rules[f"{template[x]}{template[x + 1]}"]
            if insert:
                new_template.insert(x + len(inserted) + 1, insert)
                inserted.append(insert)
        return "".join(new_template)

    new_template = str(polymer_template)
    for _ in range(steps):
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
    print(f"Part 1: {counter[most_common] - counter[least_common]}")


def part_2():
    single_count = defaultdict(int)
    for x in list(polymer_template):
        single_count[x] += 1

    pairs = defaultdict(int)
    for x in range(len(polymer_template) - 1):
        pairs[polymer_template[x] + polymer_template[x + 1]] += 1

    for _ in range(40):
        inserted = []
        for pair in pair_insertion_rules.keys():
            if pair in pairs:
                inserted.append((pair, pair_insertion_rules[pair], pairs[pair]))
                del pairs[pair]

        for pair, insert, cnt in inserted:
            single_count[insert] += cnt
            pairs[pair[0] + insert] += cnt
            pairs[insert + pair[1]] += cnt

    print(f"Part 2: {max(single_count.values()) - min(single_count.values())}")


part_1()
part_2()
