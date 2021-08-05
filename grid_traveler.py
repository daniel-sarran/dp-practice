def grid_traveler(m, n, memo=None):
    key = str(m) + ',' + str(n)
    if memo is None:
        memo = {}

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0

    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
 
    return memo[key]


if __name__ == '__main__':
    print(grid_traveler(2, 3))  # 1
    print(grid_traveler(3, 2))  # 1
    print(grid_traveler(3, 3))  # 1
    print(grid_traveler(18, 18))  # 1
