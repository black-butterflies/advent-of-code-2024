from re import findall

WORD = "XMAS"
WORD_LENGTH = len(WORD)


def flatten_vertically(soup: list[str]) -> list[str]:
    vertical_soup = []

    for col in range(len(soup[0])):
        new_row = ""
        for row in range(len(soup)):
            new_row += soup[row][col]
        vertical_soup.append(new_row)

    return vertical_soup


def flatten_diagonally_left(soup: list[str]) -> list[str]:
    diagonal_soup = []

    # diagonals starting from the first row
    for col in range(WORD_LENGTH - 1, len(soup[0])):
        new_row = ""
        i, j = col, 0
        while i >= 0 and j < len(soup):
            new_row += soup[j][i]
            j += 1
            i -= 1
        diagonal_soup.append(new_row)

    # diagonals starting from the next rows
    for row in range(1, len(soup) - WORD_LENGTH + 1):
        new_row = ""
        i, j = len(soup[0]) - 1, row
        while i >= 0 and j < len(soup):
            new_row += soup[j][i]
            j += 1
            i -= 1
        diagonal_soup.append(new_row)

    return diagonal_soup


def flatten_diagonally_right(soup: list[str]) -> list[str]:
    diagonal_soup = []

    # diagonals starting from the first row
    for col in range(len(soup[0]) - WORD_LENGTH + 1):
        new_row = ""
        i, j = col, 0
        while i < len(soup[0]) and j < len(soup):
            new_row += soup[j][i]
            i += 1
            j += 1
        diagonal_soup.append(new_row)

    # diagonals starting form the next rows
    for row in range(1, len(soup) - WORD_LENGTH + 1):
        new_row = ""
        i, j = 0, row
        while i < len(soup[0]) and j < len(soup):
            new_row += soup[j][i]
            i += 1
            j += 1
        diagonal_soup.append(new_row)

    return diagonal_soup


def find_word(soup: list[str]) -> int:
    return sum(len(findall(WORD, row)) + len(findall(WORD[::-1], row)) for row in soup)


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        soup = [line.strip() for line in f]
    return (
        find_word(soup)
        + find_word(flatten_vertically(soup))
        + find_word(flatten_diagonally_left(soup))
        + find_word(flatten_diagonally_right(soup))
    )


print(solution("input_test"))
print(solution("input"))
