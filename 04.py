
def transposed_and_reversed(M):
    return [''.join(M[j][i] for j in range(len(M)))
            for i in reversed(range(len(M[0])))]

def count_xmases_in_rows(M):
    return sum(row[i:i + 4] in ["XMAS", "SAMX"]
               for row in M
               for i in range(len(row) - 3))

def count_diagonal_xmases(M):
    return sum(''.join(M[i+k][j+k] for k in range(4)) in ["XMAS", "SAMX"]
               for i in range(len(M)-3)
               for j in range(len(M[i])-3))

grid = []
with open('input/04.txt') as f:
    for line in f:
        grid.append(line.strip())

tr_grid = transposed_and_reversed(grid)

print('Part 1:',
    count_xmases_in_rows(grid)
      + count_xmases_in_rows(tr_grid)
      + count_diagonal_xmases(grid)
      + count_diagonal_xmases(tr_grid))


def Xs(M):
    return sum(
        M[i][j] + M[i][j + 2]
            + M[i + 1][j + 1]
        + M[i + 2][j] + M[i + 2][j + 2]
        in ['MSAMS', 'MMASS', 'SSAMM', 'SMASM']
        for i in range(len(M) - 2)
        for j in range(len(M[0]) - 2)
    )

print('Part 2:', Xs(grid))
