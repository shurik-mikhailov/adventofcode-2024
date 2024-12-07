from collections import Counter

from get_input_data import get_input_data

def part_one(left: list, right: list) -> int:
    left = sorted(left)
    right = sorted(right)

    return sum(abs(l - r) for l, r in zip(left, right))


def part_two(left: list, right: list) -> int:
    right_counts = Counter(right)
    return sum(num * right_counts.get(num, 0) for num in left)


input_data = get_input_data(year=2024, task_number=1)
input_text_lines = input_data.split('\n')
left_col, right_col = zip(*[map(int, line.split('   ')) for line in input_text_lines])
print(f'Part One: {part_one(left=left_col, right=right_col)}')
print(f'Part Two: {part_two(left=left_col, right=right_col)}')
