from collections import Counter

ls = []
rs = []
with open('input/01.txt') as f:
    for line in f:
        l, r = map(int, line.strip().split())
        ls.append(l)
        rs.append(r)

ls.sort()
rs.sort()
#print('Part 1:', sum(abs(l-r) for l,r in zip(ls, rs)))

r_counts = Counter(rs)
print('Part 2:', sum(l*r_counts[l] for l in ls))