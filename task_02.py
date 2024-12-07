from typing import List

from get_input_data import get_input_data


def is_safe(report: list[int]) -> bool:
    is_increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))

    valid_differences = all(1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))

    if (is_decreasing or is_increasing) and valid_differences:
        return True
    else:
        return False


def is_safe_with_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True
    return False


def part_one(reports: List[List[int]]) -> int:
    safe_reports = 0
    for report in reports:
        safe_reports += 1 if is_safe(report) else 0

    return safe_reports


def part_two(reports: List[List[int]]) -> int:
    safe_reports = 0
    for report in reports:
        safe_reports += 1 if is_safe(report) or is_safe_with_dampener(report) else 0

    return safe_reports


input_data = get_input_data(year=2024, task_number=2)
input_text_lines = input_data.split('\n')
input_reports = [[int(val) for val in report.split()] for report in input_text_lines]

print(f'Part One: {part_one(reports=input_reports)}')
print(f'Part Two: {part_two(reports=input_reports)}')
