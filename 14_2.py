import math
import re
import matplotlib.pyplot as plt
import numpy as np
from bitarray import bitarray, frozenbitarray

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
    # Clear any existing plots
    plt.clf()

    # Create canvas and plot points
    canvas = np.ones((h, w))
    for (x, y) in ps:
        canvas[y, x] = 0

    # Display
    plt.imshow(canvas, cmap='binary')
    plt.axis('off')
    plt.draw()
    plt.pause(0.1)  # Give time to render

def is_symmetrical():
    in_left_side = sum(x < w // 2 for x,y in ps)
    in_right_side = sum(x > w // 2 for x,y in ps)
    return in_left_side == in_right_side

def ps_as_bitarray():
    a = bitarray(w*h)
    for x,y in ps:
        a[y*w+x] = True
    return frozenbitarray(a)


def detect_cycle():
    i = 0
    patterns = set()
    a = ps_as_bitarray()
    while not a in patterns:
        patterns.add(a)
        i += 1
        step(1)
        a = ps_as_bitarray()
    print("Iteration", i)
    print_picture()
    input("continue..?")

def safety_factor():
    qs = [0, 0, 0, 0]
    for x,y in ps:
        quadrant = get_quadrant(x, y)
        if quadrant:
            qs[quadrant]+=1
    return math.prod(qs)

i = 0
step(1)
min_sf = safety_factor()
while True:
    print(min_sf)
    i += 1
    step(1)
    sf = safety_factor()
    if sf < min_sf:
        print("Iteration", i)
        print_picture()
        input("continue..?")
        min_sf = sf








