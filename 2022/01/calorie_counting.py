

def part_01():
    with open('input_01.txt', 'r') as i:
        items = map(lambda l: l.replace("\n", ""), i.readlines())
        print (items)
    total = 0
    elves = []
    for calories in items:
        if calories == "":
            elves.append(total)
            total = 0
            continue
        total += int(calories)
    print (sorted(elves)[-3:], sum(sorted(elves)[-3:]))

part_01()