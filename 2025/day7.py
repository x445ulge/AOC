tachyon_manifold = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
...............
"""

with open("input.txt") as f:
    tachyon_manifold = f.read()

tachyon_manifold = tachyon_manifold.splitlines()
start_index = tachyon_manifold[0].index("S")

valid_split_indices = set()
valid_split_indices.add(start_index)

splits = 0


N = len(tachyon_manifold[0])
splitters = []
matrix = []

encountered_splitter = False
for row_idx, row in enumerate(tachyon_manifold[1:]):

    if encountered_splitter:
        encountered_splitter = False
        continue

    line = ["."] * N
    for _ in valid_split_indices:
        line[_] = "|"

    if splitters:
        for _ in splitters:
            line[_] = "^"

    splitters = []

    for idx, c in enumerate(row):
        if c == "^" and idx in valid_split_indices:
            encountered_splitter = True
            splitters.append(idx)

            valid_split_indices.remove(idx)
            valid_split_indices.add(idx - 1)
            valid_split_indices.add(idx + 1)
            splits += 1

    matrix.append(line)


print("part 1:", splits)


# for r in matrix:
#     print(''.join(r))

# part 2

rows, cols = len(matrix), len(matrix[0])
print(f"{rows, cols = }")

start = (0, matrix[0].index("|"))

adj = {}
leaves = []

print("calculating adjacancy matrix...", end=" ")

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "|":
            adj[(r, c)] = []

            # check neighbors
            if r + 1 in range(rows):
                if matrix[r + 1][c] == "^":
                    for dr, dc in [(1, -1), (1, 1)]:
                        r_, c_ = r + dr, c + dc
                        if (
                            r_ in range(rows)
                            and c_ in range(cols)
                            and matrix[r_][c_] == "|"
                        ):
                            adj[(r, c)].append((r_, c_))

                elif matrix[r + 1][c] == "|":
                    adj[(r, c)].append((r + 1, c))

            if not adj[(r, c)]:
                leaves.append((r, c))

# # print(start, leaves)
# # stop = (7, 2)

print("Done!")

# print(adj)

def dfs(node, stop, visited, paths):
    if node == stop:
        paths[0] += 1
        return

    visited.add(node)

    for neighbor in adj[node]:
        if neighbor not in visited:
            dfs(neighbor, stop, visited, paths)

    visited.remove(node)


timelines = 0
n_leaves = len(leaves)
for i, stop in enumerate(leaves):
    print(f"computing leaf {i+1}/{n_leaves}")
    paths = [0]
    visited = set()

    dfs(start, stop, visited, paths)

    timelines += paths[0]

print("\npart 2, timelines: ", timelines)
