rotations = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

with open("input.txt") as f:
    rotations = f.read()


pt = 50
count = 0
for rotation in rotations.splitlines():
    rot = int(rotation[1:]) if rotation[0] == "R" else -int(rotation[1:])

    # part 1
    # pt = (pt + rot) % 100
    # if pt == 0: count += 1

    # part 2
    # print(f"{pt} -- [{rot}] --> ", end="")
    rot_amount = abs(rot)
    while rot_amount != 0:

        if rot < 0:
            pt -= 1
        elif rot > 0:
            pt += 1
        
        if pt == -1:
            pt = 99
        if pt == 100:
            pt = 0
        
        if pt == 0:
            count += 1

        rot_amount -= 1
    # print(pt)



print(count)
