with open("input.txt") as f:
    joltages = f.read()

# joltages = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """


def max_joltage1(joltage: str) -> int:
    max_joltage = -1
    for i in range(len(joltage)):
        for j in range(i + 1, len(joltage)):
            max_joltage = max(max_joltage, int(f"{joltage[i]}{joltage[j]}"))
    return max_joltage

def max_joltage2(joltage: str) -> int:
    n = len(joltage)

    # max_joltage = -1
    # for i in range(int("0" * (n - 12) + "1" * 12, 2), int("1" * 12 + "0" * (n - 12), 2)):
    #     x = bin(i)[2:].rjust(n, "0")
    #     temp = ""
    #     if x.count("1") == 12:
    #         for idx, c in enumerate(x):
    #             if c == "1":
    #                 temp += joltage[idx]
    #         # print("considering", temp)
    #         max_joltage = max(max_joltage, int(temp))

    # return max_joltage

    pos = 0
    temp = ""
    for rem in range(12, 0, -1):
        end = n - rem + 1
        best = max(joltage[pos:end])
        pos = joltage.index(best, pos, end) + 1
        temp += best
    
    return int(temp)


total_joltage = 0

for joltage in joltages.splitlines():
    total_joltage += max_joltage2(joltage)

print(total_joltage)

# print(max_joltage2("811111111111119"))
