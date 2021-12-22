import operator
from functools import reduce


INPUT_FILE = "./sample.txt" if False else "./input.txt"

bits = ''
with open(INPUT_FILE, "r") as input_file:
    bits = bin(int('1'+input_file.read(),16))[3:]

def part_1(startbit):
    current_pos = startbit
    total_version = int(bits[current_pos:current_pos+3],2)
    type_id = int(bits[current_pos+3:current_pos+6],2)
    current_pos += 6
    if type_id == 4:
        while True:
            current_pos += 5
            if bits[current_pos-5] == '0':
                break
    else:
        if bits[current_pos] == '0':
            endi = current_pos + 16 + int(bits[current_pos+1:current_pos+16],2)
            current_pos += 16
            while current_pos < endi:
                current_pos, version = part_1(current_pos)
                total_version += version
        else:
            np = int(bits[current_pos+1:current_pos+12],2)
            current_pos += 12
            for _ in range(np):
                current_pos, version = part_1(current_pos)
                total_version += version

    return current_pos, total_version

print(f'Part 1: {part_1(0)[1]}')


ops = [
    sum,                                    # sum
    lambda x: reduce(operator.mul, x, 1),   # product
    min,                                    # min
    max,                                    # max
    lambda ls: ls[0],                       # literal
    lambda ls: 1 if ls[0] > ls[1] else 0,   # gt
    lambda ls: 1 if ls[0] < ls[1] else 0,   # lt
    lambda ls: 1 if ls[0] == ls[1] else 0,  # eq
]

def part_2(startbit):
    current_pos = startbit
    type_id = int(bits[current_pos+3:current_pos+6],2)
    current_pos += 6
    if type_id == 4: #literal value
        values = [0]
        while True:
            values[0] = 16* values[0] + int(bits[current_pos + 1:current_pos + 5],2)
            current_pos += 5
            if bits[current_pos-5] == '0':
                break
    else:
        values = []
        if bits[current_pos] == '0':
            length = current_pos + 16 + int(bits[current_pos + 1:current_pos + 16],2)
            current_pos += 16
            while current_pos < length:
                current_pos, value = part_2(current_pos)
                values.append(value)
        else:
            np = int(bits[current_pos+1:current_pos+12],2)
            current_pos += 12
            for _ in range(np):
                current_pos, value = part_2(current_pos)
                values.append(value)

    return current_pos, ops[type_id](values) # position, result

print(f'Part 2: {part_2(0)[1]}')
