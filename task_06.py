from copy import deepcopy
from typing import List, Tuple, Dict

from get_input_data import get_input_data

DIRECTIONS = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}

ROTATOR = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


def find_starting_position(lab_map: List[str],
                           directions: Dict[str, Tuple[int, ...]]):
    for y in range(len(lab_map)):
        for x in range(len(lab_map[0])):
            if lab_map[y][x] in directions.keys():
                return x, y


def is_infinite_position(lab_map: List[str],
                         target_position: Tuple[int, int],
                         starting_position: Tuple[int, int]) -> bool:
    lab_map_copy = [row[:] for row in lab_map]
    lab_height = len(lab_map_copy)
    lab_width = len(lab_map_copy[0])

    target_row = lab_map_copy[target_position[1]]
    lab_map_copy[target_position[1]] = target_row[:target_position[0]] + '#' + target_row[target_position[0] + 1:]

    current_position = starting_position
    current_direction = lab_map_copy[current_position[1]][current_position[0]]

    seen_positions = set()
    seen_positions.add((current_position, current_direction))

    while True:
        dx, dy = DIRECTIONS[current_direction]
        next_position = (current_position[0] + dx, current_position[1] + dy)

        if not (0 <= next_position[0] < lab_width and 0 <= next_position[1] < lab_height):
            return False

        elif lab_map_copy[next_position[1]][next_position[0]] == '#':
            current_direction = ROTATOR[current_direction]

        else:
            current_position = next_position

        state = (current_position, current_direction)
        if state in seen_positions:
            return True
        seen_positions.add(state)

def part_one(lab_map: List[str]) -> List[Tuple[int, int]]:
    height = len(lab_map)
    width = len(lab_map[0])

    position = find_starting_position(lab_map, DIRECTIONS)
    direction = lab_map[position[1]][position[0]]
    path = [position]

    while True:
        dx, dy = DIRECTIONS[direction]
        next_pos = (position[0] + dx, position[1] + dy)

        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
            break
        elif lab_map[next_pos[1]][next_pos[0]] == '#':
            direction = ROTATOR[direction]
        else:
            position = next_pos
            path.append(position)

    return path


def part_two(lab_map: List[str], visited_positions: List[Tuple[int, int]]) -> int:
    infinite_count = 0
    starting_position = find_starting_position(lab_map, DIRECTIONS)
    visited_positions = set(visited_positions[1:])

    for position in visited_positions:
        if is_infinite_position(
                lab_map=lab_map,
                target_position=position,
                starting_position=starting_position):
            infinite_count += 1

    return infinite_count

input_data = get_input_data(year=2024, task_number=6)
input_lab_map = input_data.split('\n')

guard_path = part_one(lab_map=input_lab_map)

print(f'Part One: {len(set(guard_path))}')
print(f'Part Two: {part_two(lab_map=input_lab_map, visited_positions=guard_path)}')
