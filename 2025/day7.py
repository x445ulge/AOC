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
                        if r_ in range(rows) and c_ in range(cols) and matrix[r_][c_] == "|":
                            adj[(r, c)].append((r_, c_))

                elif matrix[r + 1][c] == "|":
                    adj[(r, c)].append((r + 1, c))

            if not adj[(r, c)]:
                leaves.append((r, c))

# # print(start, leaves)
# # stop = (7, 2)

print("Done!")

# print(adj)


n_leaves = len(leaves)

from functools import cache

def dfs_helper(stop) -> int:
    visited = set()

    @cache
    def dfs(node, paths)->int:
        if node == stop:
            paths += 1
            return paths

        visited.add(node)

        for neighbor in adj[node]:
            if neighbor not in visited:
                paths = dfs(neighbor, paths)

        visited.remove(node)
        return paths


    return dfs(start, 0)


timelines = 0

from concurrent.futures import ThreadPoolExecutor

results = []
with ThreadPoolExecutor(max_workers=60) as executor:
    # Submit two tasks to run in parallel
    for i, stop in enumerate(leaves):
        print(f"computing leaf {i+1}/{n_leaves}")
        # timelines += dfs_helper(stop)
        _ = executor.submit(dfs_helper, stop)
        results.append(_)
    
    print("Exitting executor block...")
    # executor.submit(worker, 1)
    # executor.submit(worker, 2)

print(sum([r.result() for r in results]))

# print("\npart 2, timelines: ", timelines)
