import re

with open('input/03.txt') as f:
    matches = re.findall(r'mul\((\d+),(\d+)\)', f.read())
    print('Part 1:', sum(int(x)*int(y) for x,y in matches))