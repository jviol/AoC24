import time
from bitarray import bitarray
from multiprocessing import Pool

start_time = time.time()
obstructions = bitarray()
with open('input/06.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            obstructions.append(c == '#')
            if c == '^':
                starting_guard_pos = (y, x)
        dim_x = x+1
    dim_y = y + 1
    starting_guard_dir = (-1, 0)  # up


def within_bounds(p):
    return 0 <= p[0] < dim_y and 0 <= p[1] <= dim_x


def part1(guard_pos, guard_dir):
    positions_visited = set()
    while within_bounds(guard_pos):
        positions_visited.add(guard_pos)
        dy, dx = guard_dir
        y, x = guard_pos
        new_pos = (y + dy, x + dx)
        try:
            if obstructions[flatten_pos(*new_pos)]:
                guard_dir = (dx, -dy)
            else:
                guard_pos = new_pos
        except IndexError:
            return positions_visited

    return positions_visited

def flatten_pos(y,x):
    return y*dim_x+x

def new_empty_bitarray():
    b = bitarray(dim_y*dim_x)
    b.setall(0)
    return b

def is_loop(obstruction):
    obstructions[obstruction[0]*dim_x+obstruction[1]] = True
    # obsts = obstructions[:]
    # obsts[obstruction[0]*dim_x+obstruction[1]] = True
    guard_pos = starting_guard_pos
    guard_dir = starting_guard_dir
    pos_dirs_visited = {
        (-1,0):new_empty_bitarray(),
        (1,0):new_empty_bitarray(),
        (0,-1):new_empty_bitarray(),
        (0,1):new_empty_bitarray(),
    }
    try:
        while within_bounds(guard_pos):
            pos = flatten_pos(*guard_pos)
            if pos_dirs_visited[guard_dir][pos]:
                return True
            y, x = guard_pos
            pos_dirs_visited[guard_dir][pos] = True
            dy, dx = guard_dir
            new_pos = y_new, x_new = (y + dy, x + dx)

            if obstructions[y_new*dim_x+x_new]:
                guard_dir = (dx, -dy)
            else:
                guard_pos = new_pos
        return False
    except IndexError:
        return False
    finally:
        obstructions[obstruction[0] * dim_x + obstruction[1]] = False



if __name__ == '__main__':
    positions_visited = part1(starting_guard_pos, starting_guard_dir)
    print("Part 1:", len(positions_visited))

    positions_to_try = [p for p in positions_visited if p != starting_guard_pos]
    # with Pool() as pool:
    print("\nPart 2:", sum(map(is_loop, positions_to_try)))
    print(f"Time: {time.time() - start_time:.2f} sec.")

