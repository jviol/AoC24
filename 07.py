from operator import add, mul

to_str_dict = {add: "+", mul: "*"}
def to_str(op):
    return to_str_dict[op]

def ops_to_str(ops):
    return ' '.join(map(to_str, ops))

def step(n,remaining, test_value):
    if len(remaining) == 0:
        if n == test_value:
            return n
        else:
            return 0
    return (step(n + remaining[0], remaining[1:], test_value)
            or step(n * remaining[0], remaining[1:], test_value))


total = 0
with open('input/07.txt') as f:
    for line in f:
        test_value, rest = line.strip().split(': ')
        test_value = int(test_value)
        numbers = list(map(int, rest.split(" ")))
        total += step(numbers[0], numbers[1:], test_value)

print("Part 1:", total)

