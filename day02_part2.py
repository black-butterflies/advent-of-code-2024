def is_report_safe(levels: list[int]) -> bool:
    i, j = 0, 1
    is_asc = False
    is_desc = False
    while j < len(levels):
        if not (0 < abs(levels[i] - levels[j]) < 4):
            return False
        if levels[i] < levels[j]:
            is_asc = True
        elif levels[i] > levels[j]:
            is_desc = True
        else:
            return False
        i += 1
        j += 1
    return is_asc != is_desc


def is_line_safe(line: str) -> bool:
    levels = list(map(int, line.strip().split()))
    if is_report_safe(levels):
        return True
    for i in range(len(levels)):
        if is_report_safe([levels[j] for j in range(len(levels)) if j != i]):
            return True
    return False


def solution(filename: str) -> int:
    with open(filename, 'r') as f:
        return sum(int(is_line_safe(line)) for line in f)


print(solution('day02_input_test'))
print(solution('day02_input'))