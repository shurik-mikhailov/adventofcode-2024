"""
Смог решить это задание самостоятельно за час. Понаписал комментариев, как будто
кто-то будет их читать, но все-таки решил их потом удалить. Вторая часть доставила
какое-то особое наслаждение, почувствовал себя на минуту программистом :)
"""

from typing import List

from get_input_data import get_input_data


def xmas_exists_in_direction(target_word: str, matrix: List[str],
                             row: int, col: int,
                             row_direction: int, col_direction: int) -> bool:
    for i in range(len(target_word)):
        new_row = row + i * row_direction
        new_col = col + i * col_direction

        if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
            return False

        if matrix[new_row][new_col] != target_word[i]:
            return False

    return True


def mas_diagonal_exists(matrix: List[str],
                        row: int, col: int,
                        row_direction: int, col_direction: int) -> bool:
    try:
        return (
                matrix[row][col] == 'M' and
                matrix[row + row_direction][col + col_direction] == 'A' and
                matrix[row + 2 * row_direction][col + 2 * col_direction] == 'S'
        ) or (
                matrix[row][col] == 'S' and
                matrix[row + row_direction][col + col_direction] == 'A' and
                matrix[row + 2 * row_direction][col + 2 * col_direction] == 'M'
        )
    except IndexError:
        return False


def part_one(matrix: List[str]) -> int:
    words_counter = 0

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            for dir_row, dir_col in directions:
                if xmas_exists_in_direction('XMAS', matrix, r, c, dir_row, dir_col):
                    words_counter += 1

    return words_counter


def part_two(matrix: List[str]) -> int:
    words_counter = 0

    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[0]) - 1):
            if mas_diagonal_exists(matrix, r - 1, c - 1, 1, 1) and mas_diagonal_exists(matrix, r - 1, c + 1, 1, -1):
                words_counter += 1

    return words_counter


input_data = get_input_data(year=2024, task_number=4)
input_matrix = input_data.split('\n')

print(f'Part One: {part_one(matrix=input_matrix)}')
print(f'Part Two: {part_two(matrix=input_matrix)}')
