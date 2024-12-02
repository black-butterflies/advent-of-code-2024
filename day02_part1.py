def is_line_safe(line: str) -> bool:
    numbers = list(map(int, line.split()))
    i, j = 0, 1
    is_asc = numbers[i] < numbers[j]
    while j < len(numbers):
        if not (0 < abs(numbers[i] - numbers[j]) < 4):
            return False
        elif is_asc and numbers[i] > numbers[j]:
            return False
        elif not is_asc and numbers[i] < numbers[j]:
            return False
        j += 1
        i += 1
    return True


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        out = [int(is_line_safe(line.strip())) for line in f]
    return sum(out)


print(solution("day02_input_test"))
print(solution("day02_input"))
