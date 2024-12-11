import time
from functools import cache

start_time = time.time()
with open('input/11.txt') as f:
    stones = f.read().strip().split()


@cache
def expand(s, n) -> int:
    if n == 0:
        return 1
    if s == '0':
        return expand('1', n - 1)
    if (l := len(s)) % 2 == 0:
        return expand(s[:l // 2].lstrip('0') or '0', n - 1) \
            + expand(s[l // 2:].lstrip('0') or '0', n - 1)
    else:
        return expand(str(int(s) * 2024), n - 1)


print("Part 1:", sum(expand(s, 25) for s in stones))
print("Part 2:", sum(expand(s, 75) for s in stones))
print(f"Time: {time.time() - start_time:.2f} sec.")
