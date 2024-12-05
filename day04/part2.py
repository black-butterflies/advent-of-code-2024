def check_position_is_x_mas(i: int, j: int, soup: list[str]) -> bool:
    curr = soup[j][i]
    left = soup[j - 1][i - 1] + curr + soup[j + 1][i + 1]
    right = soup[j - 1][i + 1] + curr + soup[j + 1][i - 1]

    x_mas = ("MAS", "SAM")
    return left in x_mas and right in x_mas


def find_x_mas(soup: list[str]) -> int:
    counter = 0
    for i in range(1, len(soup[0]) - 1):
        for j in range(1, len(soup) - 1):
            if soup[j][i] == "A":
                counter += int(check_position_is_x_mas(i, j, soup))
    return counter


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        return find_x_mas([line.strip() for line in f])


print(solution("input_test"))
print(solution("input"))
