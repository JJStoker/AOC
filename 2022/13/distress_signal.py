import json
from functools import cmp_to_key

with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda p: p.split('\n'), i.read().split('\n\n')))

def in_order(left, right):
    max_width = max(len(left), len(right))
    for index in range(max_width):
        if index == len(left) and index < len(right):
            return True
        if index < len(left) and index == len(right):
            return False      

        l, r = left[index], right[index]
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            if l > r:
                return False
        else:
            result = in_order(
                l if isinstance(l, list) else [l],
                r if isinstance(r, list) else [r]
            )
            if result is not None:
                return result

def get_packets():
    for packet in [p for p in inputs if p != ""]:
        yield json.loads(packet[0]), json.loads(packet[1])
        
def part_01():
    index = 0
    for pix, (left, right) in enumerate(get_packets()):
        if in_order(left, right):
            index += (pix + 1)
    print(f"Part 1: {index}")

def part_02():
    packets = [packet for packets in get_packets() for packet in packets]
    packets.extend([[[2]], [[6]]])
    sorted_packets = sorted(packets, key = cmp_to_key(lambda a, b: -1 if in_order(a,b) else 1))
    index2 = sorted_packets.index([[2]]) + 1
    index6 = sorted_packets.index([[6]]) + 1
    print(f'part 2: {index2 * index6}')

part_01()
part_02()
