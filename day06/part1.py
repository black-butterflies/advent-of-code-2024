DIRECTIONS = {"^": ">", ">": "v", "v": "<", "<": "^"}


def find_initial_position(map_: list[str]) -> tuple[int]:
    for i in range(len(map_[0])):
        for j in range(len(map_)):
            if map_[j][i] in DIRECTIONS.keys():
                return (i, j)
    raise KeyError("guard not found")


def guard_path(map_: list[str]) -> set[tuple[int]]:
    positions = set()
    i, j = find_initial_position(map_)
    direction = map_[j][i]
    while 0 <= i < len(map_[0]) and 0 <= j < len(map_):
        if map_[j][i] == "#":
            i = i + (-1 if direction == ">" else 0) + (1 if direction == "<" else 0)
            j = j + (-1 if direction == "v" else 0) + (1 if direction == "^" else 0)
            direction = DIRECTIONS[direction]
        else:
            positions.add((i, j))
        i = i + (1 if direction == ">" else 0) + (-1 if direction == "<" else 0)
        j = j + (1 if direction == "v" else 0) + (-1 if direction == "^" else 0)

    return positions


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        return len(guard_path([line.strip() for line in f]))


print(solution("input_test"))
print(solution("input"))
