from typing import List, Tuple


machines = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

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


# def generate_possibilities(buttons, depth=3):
#     button = buttons[0]

#     for x in buttons:
#         any([ _ in button for _ in x ])
        

for machine in machines:
    target_diagram, buttons, joltages = parse_machine(machine)
    print(buttons)
    # valid_indices = [ i for i in range(len(target_diagram)) if target_diagram[i] ]
    # diagram = [False] * len(target_diagram)

    