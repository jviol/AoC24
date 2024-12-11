from itertools import chain

with open('input/11.txt') as f:
    stones = f.read().strip().split()

for i in range(25):
    stones = list(chain.from_iterable(
        ['1'] if s == '0' else
        [str(int(s[:len(s)//2])), str(int(s[len(s)//2:]))] if len(s) % 2 == 0 else
        [str(int(s)*2024)]
        for s in stones
    ))
    # print(stones)

print(len(stones))
