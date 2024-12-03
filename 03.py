import re

def sum_results(S):
    matches = re.findall(r'mul\((\d+),(\d+)\)', S)
    return sum(int(x)*int(y) for x,y in matches)

with open('input/03.txt') as f:
    rest = f.read()

# print('Part 1:', sum_results(rest))
n = 0
try:
    while True:
        enabled, rest = rest.split(r"don't()", 1)
        n += sum_results(enabled)
        disabled, rest = rest.split(r"do()", 1)
except ValueError:
    print('Part 2:', n)