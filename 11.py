import time
from functools import cache

start_time = time.time()
with open('input/11.txt') as f:
    stones = f.read().strip().split()


@cache
def expand(s, n) -> int:
    if n == 0:
        return 1
    s = s.lstrip('0') # remove leading zeroes
    if not s:
        return expand('1', n - 1)
    q, r = divmod(len(s), 2)
    if r == 0:
        return expand(s[:q], n - 1) + expand(s[q:], n - 1)
    else:
        return expand(str(int(s) * 2024), n - 1)


print("Part 1:", sum(expand(s, 25) for s in stones))
print("Part 2:", sum(expand(s, 75) for s in stones))
print(f"Time: {time.time() - start_time:.2f} sec.")
