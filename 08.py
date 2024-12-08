import itertools
from collections import defaultdict
from itertools import count, takewhile

freq_map = defaultdict(set)
with open('input/08.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c != '.':
                freq_map[c].add((y,x))
        max_x = x
    max_y = y

antinodes = set()
for positions in freq_map.values():
    for p1 in positions:
        for p2 in positions:
            if p1 != p2:
                p = (2 * p1[0] - p2[0], 2 * p1[1] - p2[1])
                if 0 <= p[0] <= max_y and 0 <= p[1] <= max_x:
                    antinodes.add(p)

print("Part 1:", len(antinodes))

antinodes = set()
for positions in freq_map.values():
    for y1, x1 in positions:
        for y2, x2 in positions:
            if (y1, x1) != (y2, x2):
                n = 0
                while True:
                    y = y1 + n * (y1 - y2)
                    x = x1 + n * (x1 - x2)
                    if 0 <= y <= max_y and 0 <= x <= max_x:
                        antinodes.add((y,x))
                        n += 1
                    else:
                        break

print("Part 2:", len(antinodes))