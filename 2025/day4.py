from typing import List, Tuple

with open("input.txt") as f:
    rolls = f.read()


# rolls = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

rolls = rolls.splitlines()

rows, cols = len(rolls), len(rolls[0])


def get_accessible():
    accessible = 0
    non_rolls = []

    for r in range(rows):
        for c in range(cols):
            if rolls[r][c] != "@":
                non_rolls.append((r, c))
                continue

            adjacent = 0
            for dr, dc in [ (0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) ]:
                r_, c_ = r + dr, c + dc
                if r_ in range(rows) and c_ in range(cols) and rolls[r_][c_] == "@":
                    adjacent += 1
            if adjacent < 4:
                accessible += 1
                non_rolls.append((r, c))

    return (accessible, non_rolls)


def construct_rolls(non_rolls: List[Tuple[int, int]]):
    rolls = []
    for r in range(rows):
        _ = ""
        for c in range(cols):
            _ += "." if (r, c) in non_rolls else "@"
        rolls.append(_)

    return rolls


total_accessible = 0
while True:
    accessible, non_rolls = get_accessible()
    total_accessible += accessible
    if accessible == 0:
        break
    rolls = construct_rolls(non_rolls)

print(total_accessible)
