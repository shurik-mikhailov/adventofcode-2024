from collections import deque
from typing import List

from get_input_data import get_input_data


def allocate_files(files_queue: deque[int], space_queue: deque[int],
                   result: List[int]) -> List[int]:
    for file_pos, file_size, file_id in reversed(files_queue):
        for space_i, (space_pos, space_size) in enumerate(space_queue):
            if space_pos < file_pos and file_size <= space_size:
                for i in range(file_size):
                    assert result[file_pos + i] == file_id, f'{result[file_pos + i]=}'
                    result[file_pos + i] = None
                    result[space_pos + i] = file_id
                space_queue[space_i] = (space_pos + file_size, space_size - file_size)
                break
    return result


def calculate_result(result_array: List[int]) -> int:
    result = 0
    for i, val in enumerate(result_array):
        result += i * val if val else 0

    return result


def part_one(disk_map: str) -> int:
    files_queue = deque()
    space_queue = deque()
    result = []
    file_id = 0
    position = 0

    for i, val in enumerate(disk_map):
        if i % 2 == 0:
            size = int(val)
            for s in range(size):
                result.append(file_id)
                files_queue.append((position, 1, file_id))
                position += 1
            file_id += 1
        else:
            size = int(val)
            space_queue.append((position, size))
            for s in range(size):
                result.append(None)
                position += 1

    result_array = allocate_files(files_queue, space_queue, result)

    return calculate_result(result_array)


def part_two(disk_map: str) -> int:
    files_queue = deque()
    space_queue = deque()
    result = []
    file_id = 0
    position = 0

    for i, val in enumerate(disk_map):
        if i % 2 == 0:
            size = int(val)
            files_queue.append((position, size, file_id))
            for s in range(size):
                result.append(file_id)
                position += 1
            file_id += 1
        else:
            size = int(val)
            space_queue.append((position, size))
            for s in range(size):
                result.append(None)
                position += 1

    result_array = allocate_files(files_queue, space_queue, result)
    return calculate_result(result_array)


input_data = get_input_data(year=2024, task_number=9)

print(f'Part One: {part_one(disk_map=input_data)}')
print(f'Part Two: {part_two(disk_map=input_data)}')
