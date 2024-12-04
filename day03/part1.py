from re import findall


MUL_REGEX = "mul\(\d{1,3},\d{1,3}\)"


def multiply_line(line: str) -> int:
    matches = findall(MUL_REGEX, line)
    total = 0
    for m in matches:
        numbers = list(map(int, m[4:-1].split(",")))
        total += numbers[0] * numbers[1]
    return total


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        return sum(multiply_line(line) for line in f)


if __name__ == "__main__":
    print(solution("input_test"))
    print(solution("input"))
