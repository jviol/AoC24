from collections import defaultdict

antecedents = defaultdict(set)
n = 0
with open('input/05.txt') as f:
    for line in f:
        stripped_line = line.strip()
        split_line = stripped_line.split("|")
        if len(split_line) == 2:
            antecedents[int(split_line[1])].add(int(split_line[0]))
        elif stripped_line:
            updates = list(map(int, stripped_line.split(",")))
            if all(not any(page2 in antecedents[page]
                           for page2 in updates[i+1:])
                   for i, page in enumerate(updates)):
                n += updates[len(updates)//2]

print("Part 1:", n)





