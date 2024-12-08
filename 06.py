
obstructions = set()
with open('input/06.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '#':
                obstructions.add((y,x))
            elif c == '^':
                guard_pos = (y,x)
                guard_dir = (-1, 0) # up
        max_x = x
    max_y = y


def within_bounds(p):
    return 0 <= p[0] <= max_y and 0 <= p[1] <= max_x


positions_visited = set()

while within_bounds(guard_pos):
    positions_visited.add(guard_pos)
    dy, dx = guard_dir
    y, x = guard_pos
    new_pos = (y + dy, x + dx)
    if new_pos in obstructions:
        guard_dir = (dx, -dy)
    else:
        guard_pos = new_pos

print("Part 1:", len(positions_visited))


