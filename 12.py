from __future__ import annotations
from itertools import groupby
from typing import Callable


class Region:
    def __init__(self, p:tuple[int,int], c:str):
        self.plant = c
        self.plots = {p}

    def merge(self, other:Region):
        if self is not other and other.plant == self.plant:
            # print("merging", self, "and", other)
            self.plots |= other.plots
            for y, x in other.plots:
                region_map[y][x] = self
            regions.remove(other)
            return self
        else:
            return other


    def side_count(self):
        # print(self.plant, ":")
        res = 0
        for dy, dx in directions:
            d_perim = self.perim_plots(dy,dx)
            # merge adjacent plots in d_perim
            key, value = get_grouping_key_and_value(dy)
            d_perim.sort(key=key)
            # print("\t", (dy,dx), d_perim)
            groups = groupby(d_perim, key)
            for k, group in groups:
                # group = list(group)
                distinct_sides = count_consecutive_groups(list(map(value, group)))
                # print("\t\t", k, list(group), distinct_sides)
                res += distinct_sides
        return res

    # get all the perimeter plots for one direction
    def perim_plots(self, dy, dx):
        return [(y,x) for y,x in self.plots
                if not lookup(y+dy, x+dx) is self]

    def total_perimeter_length(self):
        return sum(len(self.perim_plots(*d)) for d in directions)

    def price(self):
        return len(self.plots) * self.total_perimeter_length()

    def discounted_price(self):
        return len(self.plots)*self.side_count()

    def __repr__(self):
        # return f"{self.plant}:{self.plots}"
        return f"{self.plant}:{len(self.plots)}x{self.total_perimeter_length()}"

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def get_grouping_key_and_value(dy:int) -> tuple[Callable[[tuple[int,int]],int],Callable[[tuple[int,int]],int]]:
    if abs(dy) == 1:  # up or down -> horizontal side
        return get_y, get_x
    else:
        return get_x, get_y

def lookup(y, x) -> bool | Region:
    try:
        return 0 <= y and 0 <= x and region_map[y][x]
    except IndexError:
        return False

def get_x(p):
    y,x = p
    return x

def get_y(p):
    y,x = p
    return y

def count_consecutive_groups(lst:list[int]) -> int:
    lst.sort()
    group_count = 1
    cur = lst[0]
    for nxt in lst[1:]:
        if nxt != cur+1:
            group_count += 1
        cur = nxt
    return group_count

regions = set()
region_map: list[list[Region]] = []
with open('input/12.txt') as f:
    for y, row in enumerate(f):
        region_map.append([])
        for x, c in enumerate(row.strip()):
            r = Region((y, x), c)
            region_map[y].append(r)
            regions.add(r)
            for y1, x1 in [(y - 1, x), (y, x - 1)]:
                if 0 <= y1 and 0 <= x1:
                    r1 = region_map[y1][x1]
                    r = r1.merge(r)

# print(regions)
# print(region_map)
print("Part 1:", sum(r.price() for r in regions))
print("Part 2:", sum(r.discounted_price() for r in regions))
