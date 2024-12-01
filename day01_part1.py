from typing import TextIO
from bisect import insort


def process_line(line: str) -> tuple[int]:
    return tuple(map(int, line.strip().split()))


def create_lists(fp: TextIO) -> tuple[list]:
    list1, list2 = [], []
    for line in fp:
        n1, n2 = process_line(line)
        insort(list1, n1)
        insort(list2, n2)
    return list1, list2


def solution(filename: str) -> int:
    with open(filename, 'r') as f:
        list1, list2 = create_lists(f)
    return sum(abs(n1 - n2) for n1, n2 in zip(list1, list2))


if __name__ == '__main__':
    print(solution('day01_input_test'))
    print(solution('day01_input'))
