from itertools import count


def compact(layout):
    tail = len(layout)-1
    for i in count():
        while layout[i] is None:
            if tail <= i:
                return
            layout[i] = layout[tail]
            layout[tail] = None
            tail -= 1


with open('input/09.txt') as f:
    s = f.read().strip()
    files = map(int, s[0::2])
    empty_spaces = list(map(int, s[1::2]))
    layout = []
    for id, file_length in enumerate(files):
        layout += [id]*file_length
        if id < len(empty_spaces):
            layout += [None]*empty_spaces[id]

compact(layout)
print("Part 1:", sum(i*x for i,x in enumerate(layout) if x))


