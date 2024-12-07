from functools import partial, cmp_to_key
from typing import List, Tuple, Dict, Set

from get_input_data import get_input_data


def is_update_correct(update: List[int],
                      rules: List[Tuple[int, ...]]) -> bool:
    page_positions = {page: pos for pos, page in enumerate(update)}

    for x, y in rules:
        if x in page_positions.keys() and y in page_positions.keys():
            if page_positions[x] > page_positions[y]:
                return False
    return True


def find_update_middle(update: List[int]) -> int:
    mid_index = len(update) // 2
    return update[mid_index]


def get_priority(rules: List[Tuple[int, ...]]) -> Dict[int, Set[int]]:
    priority = {x: set() for rule in rules for x in rule}
    for x, y in rules:
        priority[y].add(x)

    return priority


def compare(x: int, y: int, priority: Dict[int, Set[int]]) -> int:
    if x in priority[y]:
        return -1
    elif y in priority[x]:
        return 1
    else:
        return 0


def part_one(rules: List[Tuple[int, ...]], updates: List[List[int]]) -> int:
    total = 0
    for update in updates:
        if is_update_correct(update, rules):
            total += find_update_middle(update)

    return total


def part_two(rules: List[Tuple[int, ...]], updates: List[List[int]]) -> int:
    total = 0
    priority = get_priority(rules=rules)
    compare_with_priority = partial(compare, priority=priority)

    for update in updates:
        if any(compare_with_priority(update[i], update[i + 1]) > 0 for i in range(len(update) - 1)):
            sorted_update = sorted(update, key=cmp_to_key(compare_with_priority))
            total += find_update_middle(sorted_update)

    return total


input_data = get_input_data(year=2024, task_number=5)
rules_text, updates_text = input_data.split('\n\n')
input_rules = [tuple(map(int, rule.split('|'))) for rule in rules_text.strip().split('\n')]
input_updates = [list(map(int, update.split(','))) for update in updates_text.strip().split('\n')]

print(f'Part One: {part_one(rules=input_rules, updates=input_updates)}')
print(f'Part Two: {part_two(rules=input_rules, updates=input_updates)}')
