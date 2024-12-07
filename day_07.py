from itertools import product
from typing import List, Tuple

from get_input_data import get_input_data


def evaluate_expression(numbers: List[int],
                        operators: Tuple[str, ...]) -> int:
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
    return result


def evaluate_expression_with_concatenation(numbers: List[int], operators: Tuple[str, ...]) -> int:
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result


def part_one(equations: List[str]) -> int:
    total = 0

    for equation in equations:
        target, numbers = equation.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))

        number_of_operations = len(numbers) - 1
        for operators in product(['+', '*'], repeat=number_of_operations):
            if evaluate_expression(numbers, operators) == target:
                total += target
                break

    return total


def part_two(equations: List[str]) -> int:
    total = 0

    for equation in equations:
        target, numbers = equation.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))

        number_of_operations = len(numbers) - 1
        for operators in product(['+', '*', '||'], repeat=number_of_operations):
            if evaluate_expression_with_concatenation(numbers, operators) == target:
                total += target
                break

    return total


input_data = get_input_data(year=2024, task_number=7)
input_equations = input_data.split('\n')

print(f'Part One: {part_one(equations=input_equations)}')
print(f'Part Two: {part_two(equations=input_equations)}')
