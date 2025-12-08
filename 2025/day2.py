with open("input.txt") as f:
    ranges = f.read()

# ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def is_invalid1(id_: str) -> bool:
    n = len(id_)
    if n % 2 != 0:
        return False
    return id_[: n // 2] == id_[n // 2 :]


def is_invalid2(id_: str) -> bool:
    n = len(id_)
    limit = 1
    while limit < n:
        if id_[:limit] * (n // limit) == id_:
            # print(id_[:limit])
            return True
        limit += 1
    return False


invalid_sum = 0
for range_ in ranges.split(","):
    start, stop = map(int, range_.split("-"))
    for i in range(start, stop + 1):
        if is_invalid2(str(i)):
            invalid_sum += i

print(invalid_sum)

# print(is_invalid2("2121212121"))
