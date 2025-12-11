coordinates = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

with open("input.txt") as f:
    coordinates = f.read()

coordinates = coordinates.splitlines()
num_coordinates = len(coordinates)


def distance(a1, b1, c1, a2, b2, c2):
    return ((a1 - a2) ** 2 + (b1 - b2) ** 2 + (c1 - c2) ** 2) ** 0.5

distances = []
for i in range(num_coordinates):
    if not coordinates[i]:
        continue

    a1, b1, c1 = map(int, coordinates[i].split(","))

    for j in range(i + 1, num_coordinates):
        a2, b2, c2 = map(int, coordinates[j].split(","))
        # print(round(distance(a1, b1, c1, a2, b2, c2), 2))
        distances.append((
            distance(a1, b1, c1, a2, b2, c2),
            (a1, b1, c1),
            (a2, b2, c2)
        ))

distances.sort(key=lambda x: x[0])


def solve(N=None):
    seen = []

    for dist, pt1, pt2 in distances[:N]:
        pt1_hit_indices = []
        pt2_hit_indices = []

        for idx, s in enumerate(seen):
            if pt1 in s:
                pt1_hit_indices.append(idx)

            elif pt2 in s:
                pt2_hit_indices.append(idx)
        
        # 4 cases are possible here:

        # saw the first one only
        if pt1_hit_indices and not pt2_hit_indices:
            seen[ pt1_hit_indices[0] ].add(pt2)

        # saw the second one only
        elif pt2_hit_indices and not pt1_hit_indices:
            seen[ pt2_hit_indices[0] ].add(pt1)
        
        # didn't see any
        elif not pt2_hit_indices and not pt1_hit_indices:
            _ = set()
            _.add(pt1)
            _.add(pt2)
            seen.append(_)

        # saw both
        else:
            # put 2 to 1 and nuke 2
            for e in seen[ pt2_hit_indices[0] ]:
                seen[ pt1_hit_indices[0] ].add(e)
            
            seen.pop(pt2_hit_indices[0])
        
        len_arr = [len(s) for s in seen]
        if num_coordinates in len_arr:
            print("all connected!")
            print(f"{pt1_hit_indices}, {pt2_hit_indices}, {pt1, pt2 = }")
            print(f"{pt1[0] * pt2[0] = } [Answer]")
            break

    circuit_lengths = [len(s) for s in seen]
    circuit_lengths.sort(reverse=True)

    print(f"{circuit_lengths[:3] = }")
    prod = 1
    for l in circuit_lengths[:3]:
        prod *= l

    print(prod)

print("part 1:")
solve(1000)

print("\npart 2:")
solve()
