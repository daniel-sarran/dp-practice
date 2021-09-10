"""
grid_traveler(3, 3) -> 6
    ┏━┳━┳━┓
    ┣━╋━╋━┫
    ┣━╋━╋━┫
    ┗━┻━┻━┛

Number of ways to travel from top left to bottom right.
I know this is a counting problem, so I can preformat each cell to 0.

=== We create a 4x4 grid to cover the 0x0 case ===
1,1 is 1 -- there is ONE way to travel a 1x1 grid.
0,0 is 0 -- there are ZERO ways to travel a 0x0 grid

Take current position's element, and adding it to my right and down neighbor.

For m x n grid, this is just O(m * n) space.
"""


def grid_traveler(m, n):
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    M, N = m + 1, n + 1
    table[1][1] = 1

    for i in range(M):
        for j in range(N):
            current = table[i][j]

            if i + 1 < M:
                table[i + 1][j] += current
            if j + 1 < N:
                table[i][j + 1] += current

    return table


if __name__ == '__main__':
    print(grid_traveler(3, 3))
