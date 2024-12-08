from collections import defaultdict

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
                p3 = (2*p1[0]-p2[0], 2*p1[1]-p2[1])
                if 0 <= p3[0] <= max_y and 0 <= p3[1] <= max_x:
                    antinodes.add(p3)

print("Part 1:", len(antinodes))