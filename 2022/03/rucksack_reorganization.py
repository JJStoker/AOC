from string import ascii_lowercase as alc, ascii_uppercase as upc

with open('input_01.txt', 'r') as i:
    rucksacks = list(map(lambda l: l.replace("\n", ""), i.readlines()))

priorities_low = {x: c + 1 for c, x in enumerate(alc)}
priorities_high = {x: len(upc) + c + 1 for c, x in enumerate(upc)}
    
def part_01():
    total = 0
    for items in rucksacks:
        halfway = len(items) // 2
        a = items[0:halfway]
        b = items[halfway:len(items)]
        common = []
        for x in a:
            if x in b and x not in common:
                if x in priorities_low:
                    total += priorities_low[x]
                else:
                    total += priorities_high[x]
                common.append(x)
    print(total)
    
def part_02():
    total = 0
    common = []
    for index in range(0, len(rucksacks), 3):
        one, two, three = rucksacks[index:index+3]
        common = []
        for x in one:
            if x in two and x in three and x not in common:
                common.append(x)
        for x in two:
            if x in one and x in three and x not in common:
                common.append(x)
        for x in three:
            if x in one and x in two and x not in common:
                common.append(x)
                
        for x in common:
            if x in priorities_low:
                total += priorities_low[x]
            else:
                total += priorities_high[x]
    print(total)

part_01()
part_02()