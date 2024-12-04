from re import match

from part1 import MUL_REGEX


DO_REGEX = "do()"
DONT_REGEX = "don't()"


def parse_mul(mul: str) -> int:
    numbers = list(map(int, mul[4:-1].split(",")))
    return numbers[0] * numbers[1]


def multiply_line(line: str, default_multiply: bool) -> tuple[int, bool]:
    i = 0
    total = 0
    multiply = default_multiply
    while i < len(line):
        if line[i : i + len(DO_REGEX)] == DO_REGEX:
            multiply = True
            i += len(DO_REGEX)
        elif line[i : i + len(DONT_REGEX)] == DONT_REGEX:
            multiply = False
            i += len(DONT_REGEX)
        elif mul := match(MUL_REGEX, line[i:]):
            if multiply:
                total += parse_mul(mul.group(0))
            i += mul.end()
        else:
            i += 1
    return total, multiply


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        last_multiply = True
        total = 0
        for line in f:
            result, last_multiply = multiply_line(line, last_multiply)
            total += result
        return total


print(solution("input_test2"))
print(solution("input"))
