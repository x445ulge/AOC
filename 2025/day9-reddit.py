# https://github.com/mnvr/aoc-25/blob/main/09.py

import sys
from itertools import combinations, pairwise
from collections import defaultdict

red = [list(map(int, line.split(","))) for line in sys.stdin]


def dist(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


ds = ((dist(a, b), (a, b)) for (a, b) in combinations(red, 2))
ds = list(sorted(ds, reverse=True))

vertical_lines = defaultdict(list)
horizontal_lines = defaultdict(list)
for (x, y), (u, v) in pairwise(red + [red[0]]):
    if x == u:
        vertical_lines[x].append((min(y, v), max(y, v)))
    else:
        horizontal_lines[y].append((min(x, u), max(x, u)))

hx = defaultdict(set)
for y in horizontal_lines:
    s = set()
    for a, b in horizontal_lines[y]:
        for x in range(a, b + 1):
            s.add(x)
    hx[y] = s

vy = defaultdict(set)
for x in vertical_lines:
    s = set()
    for a, b in vertical_lines[x]:
        for y in range(a, b + 1):
            s.add(y)
    vy[x] = s


def is_point_on_boundary(x, y):
    return x in hx[y] or y in vy[x]


def has_intersection(x, y, u, v):
    xr = range(min(x, u) + 1, max(x, u))
    yr = range(min(y, v) + 1, max(y, v))
    for iy in horizontal_lines:
        if iy in yr:
            for ix1, ix2 in horizontal_lines[iy]:
                if any(jx in xr for jx in range(ix1 + 1, ix2)):
                    return False
    for ix in vertical_lines:
        if ix in xr:
            for iy1, iy2 in vertical_lines[ix]:
                if any(jy in yr for jy in range(iy1 + 1, iy2)):
                    return False
    return True


p1 = ds[0][0]
p2 = None
for d, ((x, y), (u, v)) in ds:
    if is_point_on_boundary(x, v) or is_point_on_boundary(u, y):
        if has_intersection(x, y, u, v):
            p2 = d
            break

print(p1, p2)
