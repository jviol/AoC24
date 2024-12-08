obstructions = set()
with open('input/06.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '#':
                obstructions.add((y, x))
            elif c == '^':
                starting_guard_pos = (y, x)
                starting_guard_dir = (-1, 0)  # up
        max_x = x
    max_y = y


def within_bounds(p):
    return 0 <= p[0] <= max_y and 0 <= p[1] <= max_x


def part1():
    guard_pos = starting_guard_pos
    guard_dir = starting_guard_dir
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
    return positions_visited


positions_visited = part1()
print("Part 1:", len(positions_visited))


iterations = 0
positions_to_try = [p for p in positions_visited if p != starting_guard_pos]


def is_loop(obstruction):
    global iterations, positions_to_try
    iterations += 1
    print('\r', iterations, "/", len(positions_to_try), end='', flush=True)
    obsts = obstructions | {obstruction}
    guard_pos = starting_guard_pos
    guard_dir = starting_guard_dir
    pos_dirs_visited = set()
    while within_bounds(guard_pos):
        if (guard_pos, guard_dir) in pos_dirs_visited:
            return True
        pos_dirs_visited.add((guard_pos, guard_dir))
        dy, dx = guard_dir
        y, x = guard_pos
        new_pos = (y + dy, x + dx)
        if new_pos in obsts:
            guard_dir = (dx, -dy)
        else:
            guard_pos = new_pos
    return False


print("\nPart 2:", sum(is_loop(p) for p in positions_to_try))
