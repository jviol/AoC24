import re
from math import prod

q = [0, 0, 0, 0]
w = 101
h = 103
with open('input/14.txt') as f:
    for line in f:
        m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        x0,y0,dx,dy = [int(g) for g in m.groups()]
        x100 = (x0+100*dx)%w
        y100 = (y0+100*dy)%h
        if x100 < w//2:
            qx = 0
        elif x100 > w//2:
            qx = 1
        else:
            continue
        if y100 < h//2:
            qy = 0
        elif y100 > h//2:
            qy = 2
        else:
            continue
        q[qy+qx] += 1
print(prod(q))
