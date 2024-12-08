from operator import add, mul

to_str_dict = {add: "+", mul: "*"}
def to_str(op):
    return to_str_dict[op]

def ops_to_str(ops):
    return ' '.join(map(to_str, ops))

def step1(n, remaining, test_value):
    if len(remaining) == 0:
        if n == test_value:
            return n
        else:
            return 0
    return (step1(n + remaining[0], remaining[1:], test_value)
            or step1(n * remaining[0], remaining[1:], test_value))

def step2(n, remaining, test_value):
    if len(remaining) == 0:
        if n == test_value:
            return n
        else:
            return 0
    return (step2(n + remaining[0], remaining[1:], test_value)
            or step2(n * remaining[0], remaining[1:], test_value)
            or step2(int(f"{n}{remaining[0]}"), remaining[1:], test_value))


total1 = 0
total2 = 0
with open('input/07.txt') as f:
    for line in f:
        test_value, rest = line.strip().split(': ')
        test_value = int(test_value)
        numbers = list(map(int, rest.split(" ")))
        total1 += step1(numbers[0], numbers[1:], test_value)
        total2 += step2(numbers[0], numbers[1:], test_value)

print("Part 1:", total1)
print("Part 2:", total2)

