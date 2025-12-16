from typing import List, Tuple


machines = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

with open("input.txt") as f:
    machines = f.read()

machines = machines.splitlines()


def parse_machine(machine: str) -> List[List[bool], List[Tuple[int]], List[int]]:
    """Returns [diagram, buttons, joltages]"""
    start = machine.index("]")
    diagram = [x != "." for x in machine[1:start]]

    stop = machine.index("{")
    buttons = [
        tuple(map(int, button[1:-1].split(",")))
        for button in machine[start + 1 : stop].strip().split(" ")
    ]

    joltages = list(map(int, machine[stop + 1 : -1].split(",")))

    return diagram, buttons, joltages


def part1():
    total = 0
    for machine in machines:
        target_diagram, buttons, joltages = parse_machine(machine)

        pushes = 9999999999999

        for i in range(1, 2 ** len(buttons)):
            diagram = [False] * len(target_diagram)
            curr_pushes = 0

            bits_ = bin(i)[2:].rjust(len(buttons), "0")

            for idx, bit in enumerate(bits_):
                if bit == "1":
                    for b in buttons[idx]:
                        diagram[b] = not diagram[b]
                    curr_pushes += 1

                if diagram == target_diagram:
                    pushes = min(curr_pushes, pushes)
        total += pushes

    print("part 1:", total)


def part2_bruteforce():
    total = 0
    for machine in machines:
        target_diagram, buttons, target_joltages = parse_machine(machine)
        n_joltages = len(target_joltages)

        joltage_dict = {i: target_joltages[i] for i in range(n_joltages)}

        button_pool = []
        for button in buttons:
            _ = min([joltage_dict[b] for b in button])
            for i in range(_):
                button_pool.append(button)

        n_button_pool = len(button_pool)

        pushes = 9999999999999
        for i in range(1, 2**n_button_pool):
            joltages = [0] * n_joltages
            curr_pushes = 0

            bits_ = bin(i)[2:].rjust(n_button_pool, "0")

            for idx, bit in enumerate(bits_):
                if bit == "1":
                    for b in button_pool[idx]:
                        joltages[b] += 1

                    curr_pushes += 1

                if joltages == target_joltages:
                    pushes = min(pushes, curr_pushes)
        total += pushes

    print("part 2:", total)


def part2_bruteforce_dfs():
    total = 0
    for m_i, machine in enumerate(machines):
        print(f"processing machine {m_i+1} of {len(machines)}...")
        _, buttons, target_joltages = parse_machine(machine)

        joltage_dict = {i: target_joltages[i] for i in range(len(target_joltages))}

        button_pool = []
        for button in buttons:
            _ = min([joltage_dict[b] for b in button])
            for i in range(_):
                button_pool.append(button)

        cache = {}
        best_solution = [float('inf')]

        def dfs(pos: int, current_joltages, pushes: int):
            
            # caching
            key = (pos, tuple(current_joltages), pushes)
            if key in cache:
                return cache[key]
            
            # base case
            if current_joltages == target_joltages:
                # print("reached target")
                best_solution[0] = min(best_solution[0], pushes)
                return pushes
            
            # Prune
            for i, (curr, target) in enumerate(zip(current_joltages, target_joltages)):
                if curr > target:
                    return float('inf')
            if pushes >= best_solution[0]:
                return float('inf')

            min_pushes = float("inf")

            # go over all combinations of buttons
            for i in range(pos, len(button_pool)):
                skip = dfs(i + 1, current_joltages, pushes)
                min_pushes = min(min_pushes, skip)

                # now take the button
                new_joltages = current_joltages.copy()
                for b in button_pool[i]:
                    new_joltages[b] += 1

                use = dfs(i + 1, new_joltages, pushes + 1)
                min_pushes = min(min_pushes, use)

            cache[key] = min_pushes
            return min_pushes

        current_joltages = [0] * len(target_joltages)
        total += dfs(0, current_joltages, 0)

    print("part 2:", total)

# part2_bruteforce()
part2_bruteforce_dfs()
