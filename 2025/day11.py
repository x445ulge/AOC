devices = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

with open("input.txt") as f:
    devices = f.read()

devices = devices.splitlines()

adj = {}
for device in devices:
    key, nodes = device.split(":")
    adj[key.strip()] = nodes.strip().split()


def part1():
    total_paths = 0
    for node in adj["you"]:
        path_len = [0]
        visited = set()
        stop = "out"

        def dfs(node):
            if node == stop:
                # print(visited)
                path_len[0] += 1
                return
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

                    visited.remove(neighbor)

        dfs(node)
        total_paths += path_len[0]

    print("part 1:", total_paths)


def part2():
    total_paths = 0
    N = len(adj["svr"])
    for n_i, node in enumerate(adj["svr"]):
        print(f"processing {n_i+1}/{N}")

        path_len = [0]

        dac_hits = [0]
        fft_hits = [0]

        visited = set()
        stop = "out"

        def dfs(node):
            if node == stop:
                if dac_hits[0] and fft_hits[0]:
                    path_len[0] += 1
                return

            # visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if neighbor == "dac":
                        dac_hits[0] += 1
                    if neighbor == "fft":
                        fft_hits[0] += 1
                    dfs(neighbor)

                    # backtrack
                    visited.remove(neighbor)

        dfs(node)
        total_paths += path_len[0]

        # print(node, path_len, visited)

    print("part 2:", total_paths)

part2()
