from re import finditer

from part1 import MUL_REGEX


DO_REGEX = "do()"
DONT_REGEX = "don't()"


def parse_mul(mul: str) -> int:
    numbers = list(map(int, mul[4:-1].split(",")))
    return numbers[0] * numbers[1]


def multiply_line(line: str) -> int:
    muls = finditer(MUL_REGEX, line)
    dos = [(m.end(), True) for m in finditer(DO_REGEX, line)]
    donts = [(m.end(), False) for m in finditer(DONT_REGEX, line)]
    instructions = sorted(dos + donts, key=lambda tup: tup[0])

    total = 0
    for match in muls:
        i = 0
        while i < len(instructions) and instructions[i][0] < match.start():
            i += 1
        print(f"INSTRUCTION: {line[instructions[i-1][0] -5 : instructions[i-1][0]]}")
        print(f"VALUE: {instructions[i-1][1]}")
        if instructions[i - 1][1]:
            total += parse_mul(line[match.start() : match.end()])
    return total


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        return sum(multiply_line(line) for line in f)


print(solution("input_test2"))
print(solution("input"))
