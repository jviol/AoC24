import re


w = 101
h = 103
ps = []
vs = []
with open('input/14.txt') as f:
    for line in f:
        m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        x0,y0,dx,dy = [int(g) for g in m.groups()]
        ps.append((x0,y0))
        vs.append((dx,dy))

def step(n):
    for t in range(n):
        for j, ((x,y), (dx, dy)) in enumerate(zip(ps,vs)):
            ps[j] = ((x+dx)%w, (y+dy)%h)


def print_picture():
    picture = [[' ']*w for _ in range(h)]
    for (x,y) in ps:
        picture[y][x] = '#'
    print('\n'.join(''.join(line) for line in picture))


def has_vertical_clumping():
    # Count particles in each column
    col_counts = [0] * w
    for (x, y) in ps:
        col_counts[x] += 1

    # Calculate variation in density
    avg_col = sum(col_counts) / w
    col_var = sum((c - avg_col) ** 2 for c in col_counts) / w

    # High variance indicates uneven distribution (possible clumping)
    return col_var > avg_col ** 2

def has_horizontal_clumping():
    # Count particles in each row
    row_counts = [0] * h
    for (x, y) in ps:
        row_counts[y] += 1

    # Calculate variation in density
    avg_row = sum(row_counts) / h
    row_var = sum((c - avg_row) ** 2 for c in row_counts) / h

    # High variance indicates uneven distribution (possible clumping)
    return row_var > avg_row ** 2


i = 0
horizontal_clumps = []
vertical_clumps = []

while True:
    i += 1
    step(1)
    if has_horizontal_clumping() and has_vertical_clumping():
        print("Iteration", i)
        print_picture()
        break



