from typing import List

with open("input.txt") as f:
    database = f.read()

# database = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """


database = database.splitlines()
split_ = database.index('')


def is_fresh(x:int, ranges:List[int]) -> bool:
    for r in ranges:
        if x in r:
            return True
    return False

def part1():
    ranges = []

    for x in database[:split_]:
        start, stop = map(int, x.split("-"))
        ranges.append(range(start, stop+1))

    fresh = 0
    for x in database[split_+1:]:
        fresh += is_fresh(int(x))

    print(fresh)

def part2():
    ranges = []

    for x in database[:split_]:
        start, stop = map(int, x.split("-"))
        ranges.append((start, stop))

    ranges.sort(key=lambda x:x[0])

    fresh = 0

    start_, stop_ = ranges[0][0], -1
    for i in range(len(ranges)):
        start, stop = ranges[i]

        if start in range(start_, stop_+1) and stop in range(start_, stop_+1):
            continue

        if start in range(start_, stop_+1) and stop not in range(start_, stop_+1):
            # we're getting a farther stop
            _ = stop_ + 1
            stop_ = stop
            fresh += stop_ - _ + 1
            continue

        stop_ = stop
        fresh += stop_ - start + 1
        
    print(fresh)

part2()