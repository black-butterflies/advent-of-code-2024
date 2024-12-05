from re import search


def is_update_correct(
    update: str, rules: list[list[str]]
) -> tuple[bool, list[list[str]]]:
    broken_rules = []
    correct = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not search(f"{rule[0]}.+{rule[1]}", update):
                broken_rules.append(rule)
                correct = False
    return correct


def reorder(update: str, broken_rules: list[list[str]]) -> str: ...


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
        correct, broken_rules = is_update_correct(u, rules)
        if not correct:
            new = reorder(u, broken_rules)
            m = (len(new) - 1) // 2
            total += int(new[m : m + 2])

    return total


print(solution("input_test"))
# print(solution("input"))
