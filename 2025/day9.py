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


tiles_of_interest = set()


def get_tiles_of_interest(idx):
    start, stop = red_tiles[0], red_tiles[-1]

    for tile in red_tiles:
        if tile[idx] == start[idx]:
            tiles_of_interest.add(tile)
        else:
            break

    for tile in red_tiles[::-1]:
        if tile[idx] == stop[idx]:
            tiles_of_interest.add(tile)
        else:
            break


# # sort by x: width
# red_tiles.sort(key=lambda x: x[0])
# get_tiles_of_interest(0)

# # sort by y: height
# red_tiles.sort(key=lambda x: x[1])
# get_tiles_of_interest(1)

# tiles_of_interest = list(tiles_of_interest)
# N = len(tiles_of_interest)

# area = -1
# for i in range(N):
#     x1, y1 = tiles_of_interest[i]
#     for j in range(i + 1, N):
#         x2, y2 = tiles_of_interest[j]
#         area = max(area, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) )

area = -1
for i in range(len(red_tiles)):
    x1, y1 = red_tiles[i]
    for j in range(i + 1, len(red_tiles)):
        x2, y2 = red_tiles[j]
        curr_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        # print(curr_area)
        area = max(area, curr_area)

print("part 1:", area)


valid_cols = {x[0]: set() for x in red_tiles}
valid_rows = {x[1]: set() for x in red_tiles}


last_row = last_col = -1
for r, c in red_tiles:
    valid_cols[r].add(c)
    valid_rows[c].add(r)
    last_row = max(last_row, r)
    last_col = max(last_col, c)

rows = last_row + 1
cols = last_col + 1

matrix = matrix = [[0] * cols for _ in range(rows)]

boundaries = []

# fixing the vertical bounds
for c in valid_rows:
    rows_in_c = list(valid_rows[c])
    rows_in_c.sort()
    for _ in range(rows_in_c[0], rows_in_c[-1] + 1):
        boundaries.append((_, c))
        matrix[_][c] = 1

# fixing the horizontal bounds
for r in valid_cols:
    cols_in_r = list(valid_cols[r])
    cols_in_r.sort()
    for _ in range(cols_in_r[0], cols_in_r[-1] + 1):
        boundaries.append((r, _))
        matrix[r][_] = 1

# print(rows, cols, len(boundaries))

# matrix = []

# for r in range(rows):
#     for c in range(cols):
#         print("#" if matrix[r][c] else ".", end=" ")
#     print()


for r in range(rows):
    # print(sum(matrix[r]))
    
    # if not sum(matrix[r]) >= 2:
    #     continue

    if not matrix[r].count(1) >= 2:
        continue

    start = matrix[r].index(1)
    # stop = matrix[r][::-1].index(1)

    # stop = cols - stop - 1

    # for i in range(start, stop + 1):
    for i in range(start, cols):
        matrix[r][i] = 1

# print("-"*10)

# for r in range(rows):
#     for c in range(cols):
#         print("#" if matrix[r][c] else ".", end=" ")
#     print()


print(len(matrix))
