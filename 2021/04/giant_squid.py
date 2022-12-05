from collections import defaultdict, deque
from functools import reduce
from typing import DefaultDict, List

INPUT_FILE = './sample.txt' if False else './input.txt'


bingo_numbers: List[int] = []
bingo_cards: List[List[List[int]]] = []
with open(INPUT_FILE, 'r') as input_file:
    bingo_lines = input_file.readlines()
    bingo_numbers = list(map(int, list(bingo_lines[0].strip().split(','))))
    bingo_card = []
    for (i, bingo_line) in enumerate(bingo_lines[2:]):
        if bingo_line == '\n': continue
        bingo_card.append(
            list(map(int, filter(lambda x: x, map(str.strip, bingo_line.strip().split(' ')))))
        )
        if (len(bingo_card) == 5):
            bingo_cards.append(bingo_card)
            bingo_card = []
        
def part_1():
    hits = [
        [[False for _ in range(len(card[0]))] for _ in range(len(card))]
        for card in bingo_cards
    ]
    won = False
    for number in bingo_numbers:
        if won: continue
        for (cI, card) in enumerate(bingo_cards):
            if won: continue
            range_x = range(len(card[0]))
            range_y = range(len(card))
            for x in range_x:
                for y in range_y:
                    if card[x][y] == number:
                        hits[cI][x][y] = True
            for x in range_x:
                won_row = True
                for y in range_y:
                    if not hits[cI][x][y]:
                        won_row = False
                if won_row:
                    won = True
            for y in range_y:
                won_col = True
                for x in range_x:
                    if not hits[cI][x][y]:
                        won_col = False
                if won_col:
                    won = True
            if won:
                unmarked = 0
                for x in range_x:
                    for y in range_y:
                        if not hits[cI][x][y]:
                            unmarked += card[x][y]
                print(f'Part 1: {unmarked * number}')

def part_2():
    hits = [
        [[False for _ in range(len(card[0]))] for _ in range(len(card))]
        for card in bingo_cards
    ]
    finished_cards = [False for _ in range(len(bingo_cards))]
    for number in bingo_numbers:
        for (cI, card) in enumerate(bingo_cards):
            won = False
            range_x = range(len(card[0]))
            range_y = range(len(card))
            for x in range_x:
                for y in range_y:
                    if card[x][y] == number:
                        hits[cI][x][y] = True
            for x in range_x:
                won_row = True
                for y in range_y:
                    if not hits[cI][x][y]:
                        won_row = False
                if won_row:
                    won = True
            for y in range_y:
                won_col = True
                for x in range_x:
                    if not hits[cI][x][y]:
                        won_col = False
                if won_col:
                    won = True
            if won and not finished_cards[cI]:
                finished_cards[cI] = True
                if all([finished_cards[x] for x in range(len(bingo_cards))]):
                    unmarked = 0
                    for x in range_x:
                        for y in range_y:
                            if not hits[cI][x][y]:
                                unmarked += card[x][y]
                    print(f'Part 2: {unmarked * number}')

part_1()
part_2()
