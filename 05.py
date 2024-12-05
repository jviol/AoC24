from collections import defaultdict

antecedents = defaultdict(set)
n = 0
m = 0

def reorder(update):
    for i, page in enumerate(update):
        for j, page2 in enumerate(update[i + 1:]):
            if page2 in antecedents[page]:
                update[i] = page2
                update[i+1+j] = page
                return reorder(update)
    return update[len(update) // 2]


with open('input/05.txt') as f:
    for line in f:
        stripped_line = line.strip()
        split_line = stripped_line.split("|")
        if len(split_line) == 2:
            antecedents[int(split_line[1])].add(int(split_line[0]))
        elif stripped_line:
            update = list(map(int, stripped_line.split(",")))
            if all(not any(page2 in antecedents[page]
                           for page2 in update[i + 1:])
                   for i, page in enumerate(update)):
                n += update[len(update) // 2]
            else:
                m += reorder(update)

print("Part 1:", n)
print("Part 2:", m)





