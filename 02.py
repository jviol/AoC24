reports = []
with open('input/02.txt') as f:
    for line in f:
        reports.append(list(map(int,line.strip().split())))

def is_safe(levels):
    increasing = levels == sorted(levels)
    decreasing = levels == sorted(levels, reverse=True)
    return ((increasing or decreasing)
        and all(1 <= abs(levels[i]-levels[i+1]) <= 3
            for i in range(len(levels)-1)))

# print('Part 1:', sum(is_safe(levels) for levels in reports))

def is_almost_safe(levels):
    return is_safe(levels) or any(
        is_safe(levels[:i] + levels[i+1:])
        for i in range(len(levels))
    )

print('Part 2:', sum(is_almost_safe(levels) for levels in reports))
