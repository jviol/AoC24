import re
import matplotlib.pyplot as plt
import numpy as np



q = [0, 0, 0, 0]
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

def get_quadrant(x,y):
    if x < w // 2:
        qx = 0
    elif x > w // 2:
        qx = 1
    else:
        return None
    if y < h // 2:
        qy = 0
    elif y > h // 2:
        qy = 2
    else:
        return None
    return qx+qy


def step(n):
    for t in range(n):
        for j, ((x,y), (dx, dy)) in enumerate(zip(ps,vs)):
            ps[j] = ((x+dx)%w, (y+dy)%h)


def print_picture():
    picture = [[' ']*w for _ in range(h)]
    for (x,y) in ps:
        picture[y][x] = '#'
    print('\n'.join(''.join(line) for line in picture))


def is_symmetrical():
    in_left_side = sum(x < w // 2 for x,y in ps)
    in_right_side = sum(x > w // 2 for x,y in ps)
    return in_left_side == in_right_side

i = 0
while True:
    while not is_symmetrical():
        i += 1
        step(1)
    print("Iteration", i)
    print_picture()
    input("continue..?")
    i += 1
    step(1)




