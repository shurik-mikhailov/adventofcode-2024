from collections import defaultdict
from typing import List

from get_input_data import get_input_data


def part_one(city_map: List[str]) -> int:
    antennas_map = []

    for y, line in enumerate(city_map):
        for x, char in enumerate(line):
            if char != ".":
                antennas_map.append((x, y, char))

    height, width = len(city_map), len(city_map[0])

    antinodes_positions = set()

    frequency_map = defaultdict(list)
    for x, y, char in antennas_map:
        frequency_map[char].append((x, y))

    for char, positions in frequency_map.items():
        n = len(positions)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx, dy = x2 - x1, y2 - y1
                antinode_1 = (x1 - dx, y1 - dy)
                antinode_2 = (x2 + dx, y2 + dy)

                if (x1 + dx, y1 + dy) == (x2, y2):
                    antinodes_positions.add(antinode_1)
                    antinodes_positions.add(antinode_2)

    valid_antinodes = {
        (x, y) for x, y in list(antinodes_positions) if 0 <= x < width and 0 <= y < height
    }

    return len(valid_antinodes)


def part_two(city_map: List[str]) -> int:
    antennas = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(city_map):
        for x, char in enumerate(line):
            if char != ".":
                antennas[char].append((x, y))

    height, width = len(city_map), len(city_map[0])

    for char, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = positions[i]
                x2, y2 = positions[j]
                antinodes.add((x2, y2))

                new_x = x2 + (x2 - x1)
                new_y = y2 + (y2 - y1)

                while 0 <= new_x < width and 0 <= new_y < height:
                    antinodes.add((new_x, new_y))
                    new_x += (x2 - x1)
                    new_y += (y2 - y1)

    return len(antinodes)


input_data = get_input_data(year=2024, task_number=8)
input_map = input_data.split('\n')

print(f'Part One: {part_one(city_map=input_map)}')
print(f'Part Two: {part_two(city_map=input_map)}')
