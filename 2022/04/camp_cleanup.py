with open('input_01.txt', 'r') as i:
    pairs = list(map(lambda l: l.replace("\n", ""), i.readlines()))

def part_01():
    total = 0
    for pair_a, pair_b in [pair.split(",") for pair in pairs]:
        start_a, end_a = map(int, pair_a.split("-"))
        start_b, end_b = map(int, pair_b.split("-"))
        if start_b >= start_a and end_b <= end_a or start_a >= start_b and end_a <= end_b:
            total += 1
    print (total)

def part_02():
    total = 0
    for pair_a, pair_b in [pair.split(",") for pair in pairs]:
        start_a, end_a = map(int, pair_a.split("-"))
        start_b, end_b = map(int, pair_b.split("-"))
        if end_a >= start_b and start_a <= end_b and end_a:
            total += 1
    print (total)   

part_01()
part_02()
