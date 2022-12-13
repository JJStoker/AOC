import json

with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda p: p.split('\n'), i.read().split('\n\n')))

def part_01():
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
    index = 0
    for pix, packet in enumerate([p for p in inputs if p != ""]):
        left, right = json.loads(packet[0]), json.loads(packet[1])
        if in_order(left, right):
            index += (pix + 1)
    print(f"Part 1: {index}")
    
part_01()
