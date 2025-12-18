import re


problems = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

with open("input.txt") as f:
    problems = f.read()


problems = problems.splitlines()

operations = list(re.findall(r'\*|\+', problems[-1]))

def part1():
    numbers = [list(map(int, re.findall(r'\d+', r))) for r in problems[:-1]]
    total = 0
    for idx, operation in enumerate(operations):

        if operation == "*":
            prod = 1
            for row in numbers:
                prod *= row[idx]
            total += prod

        else:
            prod = 0
            for row in numbers:
                prod += row[idx]
            total += prod

    print(total)


def part2():
    op_index = 0
    total = 0

    numbers = []
    for idx in range(len(problems[0])):

        number = ""
        for row in problems[:-1]:
            if row[idx].isdigit():
                number += row[idx]
        
        if number:
            numbers.append(int(number))

        if not number or idx == len(problems[0])-1:
            # got the blank
            # print(numbers, operations[op_index])
            if operations[op_index] == "*":
                prod = 1
                for n in numbers:
                    prod *= n
                # print(prod)
                total += prod
            else:
                prod = 0
                for n in numbers:
                    prod += n
                # print(prod)
                total += prod
            
            op_index += 1
            numbers = []
    
    print(total)

part1()
part2()
