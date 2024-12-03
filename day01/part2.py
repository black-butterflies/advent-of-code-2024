from collections import Counter

from day01_part1 import create_lists


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        left, right = create_lists(f)
    right_counter = Counter(right)
    return sum(x * right_counter[x] for x in left)


if __name__ == "__main__":
    print(solution("day01_input_test"))
    print(solution("day01_input"))
