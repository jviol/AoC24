from itertools import combinations_with_replacement, accumulate, permutations, chain
from operator import add, mul

to_str_dict = {add: "+", mul: "*"}
def to_str(op):
    return to_str_dict[op]

def ops_to_str(ops):
    return ' '.join(map(to_str, ops))

total = 0
with open('input/07.txt') as f:
    for line in f:
        test_value, rest = line.strip().split(': ')
        test_value = int(test_value)
        numbers = list(map(int, rest.split(" ")))
        print(test_value, ":")
        for ops in set(chain.from_iterable(map(permutations, combinations_with_replacement([add, mul], len(numbers) - 1)))):
            n = numbers[0]
            for i, op in enumerate(ops):
                n = op(n, numbers[i + 1])
            print("\t", n, ops_to_str(ops))
            if n == test_value:
                total += n
                break

print("Part 1:", total)
