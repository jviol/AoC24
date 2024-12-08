from collections import defaultdict
from itertools import count, takewhile

freq_map = defaultdict(set)
with open('input/08.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c != '.':
                freq_map[c].add((y, x))
        max_x = x
    max_y = y


def within_bounds(p):
    return 0 <= p[0] <= max_y and 0 <= p[1] <= max_x


antinodes1 = set()
antinodes2 = set()
for positions in freq_map.values():
    for y1, x1 in positions:
        for y2, x2 in positions:
            if (y1, x1) != (y2, x2):
                dy = y1 - y2
                dx = x1 - x2
                project = lambda n: (y1 + n * dy, x1 + n * dx)
                project_multiple = lambda ns : set(takewhile(within_bounds, map(project, ns)))
                antinodes1 |= project_multiple([1])
                antinodes2 |= project_multiple(count())

print("Part 1:", len(antinodes1))
print("Part 2:", len(antinodes2))
