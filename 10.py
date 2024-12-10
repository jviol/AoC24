from itertools import chain

with open('input/10.txt') as f:
    topomap = [[int(c) for c in line.strip()] for line in f]

def within_bounds(p):
    y,x = p
    return 0 <= y < len(topomap) and 0 <= x < len(topomap[0])

def adjacent(y,x) -> list[tuple[int,int]]:
    return [p for p in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)] if within_bounds(p)]

def score(p, h):
    if h == 9:
        return 1
    return sum(score((y,x), h+1) for (y,x) in adjacent(*p) if topomap[y][x] == h+1)

def paths_from(y,x) -> list[list[tuple[int,int]]]:
    h = topomap[y][x]
    if h == 9:
        return [[(y,x)]]
    res = []
    for (y1, x1) in adjacent(y, x):
        if topomap[y1][x1] == h + 1:
            paths = paths_from(y1, x1)
            print("paths from", (y1, x1), "h =", topomap[y1][x1])
            for path in paths:
                print("\tpath:", path)
                res.append([(y,x)] + path)
    return res

def reachable_summits(y,x) -> set[tuple[int, int]]:
    h = topomap[y][x]
    if h == 9:
        return {(y, x),}
    res = set()
    for (y1, x1) in adjacent(y, x):
        if topomap[y1][x1] == h + 1:
            res |= reachable_summits(y1, x1)
    return res

print(sum(score((y,x), 0) for y,row in enumerate(topomap) for x, h in enumerate(row) if h == 0))

# for summits in reachable_summits(0, 2):
#     print(summits)

# total = 0
# for y, row in enumerate(topomap):
#     for x, h in enumerate(row):
#         if h == 0:
#             sc = score((y,x), h)
#             print("Trailhead at", (y,x), "has a score of", sc)
#             total += sc
#
# print(total)


