"""
Я ненавижу регулярные выражения, и этот раз не стал исключением. Оправдаю себя тем, что я
обратился к LLM исключительно за регуляркой, остальное решение я продумал и написал сам :)
"""

import re

from get_input_data import get_input_data


def part_one(text: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)

    return sum(int(match[0]) * int(match[1]) for match in matches)


def part_two(text: str) -> int:
    multiplication_enabled = False
    total = 0

    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    for match in re.finditer(pattern, text):
        if match.group(0) == "do()":
            multiplication_enabled = True
        elif match.group(0) == "don't()":
            multiplication_enabled = False
        elif match.group(0).startswith('mul'):
            number_1 = int(match.group(1))
            number_2 = int(match.group(2))

            if multiplication_enabled:
                total += number_1 * number_2

    return total


input_data = get_input_data(year=2024, task_number=3)

print(f'Part One: {part_one(text=input_data)}')
print(f'Part Two: {part_two(text=input_data)}')
