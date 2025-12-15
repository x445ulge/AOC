red_tiles = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("input.txt") as f:
    red_tiles = f.read()

red_tiles = red_tiles.splitlines()
red_tiles = [tuple(map(int, tile.split(",")[::-1])) for tile in red_tiles]

area = -1
for i in range(len(red_tiles)):
    r1, c1 = red_tiles[i]
    for j in range(i + 1, len(red_tiles)):
        r2, c2 = red_tiles[j]
        curr_area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
        # print(curr_area)
        area = max(area, curr_area)

print("part 1:", area)


valid_rows = {x[1]: set() for x in red_tiles}


last_row = last_col = -1
for r, c in red_tiles:
    valid_rows[c].add(r)
    last_row = max(last_row, r)
    last_col = max(last_col, c)

rows = last_row + 1
cols = last_col + 1


# fixing the vertical bounds
valid_verticals = []
for c in valid_rows:
    rows_in_c = list(valid_rows[c])
    rows_in_c.sort()
    for _ in range(rows_in_c[0], rows_in_c[-1] + 1):
        valid_verticals.append((_, c))

valid_verticals.sort(key=lambda x: x[0])


valid_ranges = {}

prev_r = valid_verticals[0]
start = 99999999
stop = -999

for r, c in valid_verticals:
    if prev_r != r:
        start = 99999999
        stop = -999

    start = min(start, c)
    stop = max(stop, c)

    valid_ranges[r] = range(start, stop + 1)
    prev_r = r

# print(valid_ranges)
# print(len(valid_ranges))


def is_valid_area(r1, c1, r2, c2) -> bool:
    a = min(r1, r2), min(c1, c2)
    b = min(r1, r2), max(c1, c2)
    c = max(r1, r2), max(c1, c2)
    d = max(r1, r2), min(c1, c2)

    for x in [a, b, c, d]:
        r_, c_ = x
        if r_ not in valid_ranges:
            return False
        if c_ not in valid_ranges[r_]:
            return False
    return True


area = -1
for i in range(len(red_tiles)):
    r1, c1 = red_tiles[i]
    for j in range(i + 1, len(red_tiles)):
        r2, c2 = red_tiles[j]

        if not is_valid_area(r1, c1, r2, c2):
            continue

        curr_area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
        # print(curr_area, f"{valid_count = }")
        area = max(area, curr_area)

print("part 2:", area)
