from re import search


def is_update_correct(update: str, rules: list[list[str]]) -> bool:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not search(f"{rule[0]}.+{rule[1]}", update):
                return False
    return True


def solution(filename: str) -> int:
    rule_delimiter = "|"
    with open(filename, "r") as f:
        rules: list[list[str]] = []
        updates = []
        for line in f:
            if rule_delimiter in line:
                rules.append(line.strip().split(rule_delimiter))
            elif line.strip():
                updates.append(line.strip())

    total = 0
    for u in updates:
        if is_update_correct(u, rules):
            m = (len(u) - 1) // 2
            total += int(u[m : m + 2])

    return total


print(solution("input_test"))
print(solution("input"))
