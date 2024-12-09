def parse_diskmap(line: str) -> list[str]:
    diskmap = []
    id = 0
    is_file = True
    for char in line:
        digit = int(char)
        if is_file:
            diskmap.extend([str(id) for _ in range(digit)])
            id += 1
        else:
            diskmap.extend(["." for _ in range(digit)])
        is_file = not is_file

    return diskmap


def find_last_file_block(disk: list[str]) -> int:
    i = len(disk) -1
    while i > 0 and disk[i] == '.':
        i -= 1
    return i


def reorder_disk(disk: list[str]) -> None: 
    disk_size = len(disk)
    for i in range(disk_size):
        if disk[i].isnumeric():
            continue
        j = find_last_file_block(disk)
        if j > i:
            disk[i], disk[j] = disk[j], disk[i]


def calculate_checksum(diskmap: list[str]) -> int:
    stop = find_last_file_block(diskmap)
    return sum(i * int(diskmap[i]) for i in range(stop))


def solution(filename: str) -> int:
    with open(filename, "r") as f:
        diskmap = parse_diskmap(f.readline().strip())
    reorder_disk(diskmap)
    return calculate_checksum(diskmap)


print(solution("input_test"))
print(solution("input"))
