def grid_traveler(m, n, memo=None):
    """
    Pattern: start at top left of grid, and can only move right or down.
    So for final square, it is the sum of the ways to get to square above, and
    to the left.

    This can cause a lot of overlap, which can be improved by caching previous
    calculated values using memoization.

    1) Create brute solution
    2) Analyze for overlapping subproblems
    3) Use a table/memo - check if the computed value is in the memo
    4) If not, assign the computed value to memo at that parameter
    Note: tuples are kind of hashable, but strings are always hashable -- this
    solution makes a hashable string out of m and n parameters -- a good tip
    for future issues with coordinates?
    """
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
