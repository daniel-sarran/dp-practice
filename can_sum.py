    """
    We can't reuse values in nums to come up with the target sum.

    can_sum(7, [5, 3, 4, 7]) -> True

    can_sum(7, [2, 4]) -> False

    How can we frame this problem recursively?
    How can we `shrink` the size of the problem?

    can_sum(7, [5, 3, 4, 7]) -> True

                7
         -5  -3  -4  -7
          2   4   3   7
          ^
          2 has no valid options

                7
         -5  -3  -4  -7
          2   4   3   7
              ^
          -3    -4
          -1     0

          0 is a base case that should return TRUE - it has created a sum
          The boolean values will bubble up
          The parent will just ensure at LEAST ONE of the values is true.
                

    can_sum(7, [5, 3, 4, 7]) -> True

                7
            -2      -4
            5       3

        -2  -4      -2
        3   1       1
        
        -2
        1

        Here none of the values can result in zero, so will return false.

        TIME COMPLEXITY is O(n ^ m), pre-memoization
        where m is target sum, and n is array length
        SPACE COMPLEXITY is O(m)

        Bear in mind, the SPACE COMPLEXITY on recursive stack here is only the
        HEIGHT of the tree, which is M.
    """
def can_sum(target, nums, memo=None):
    if memo is None:
        memo = {}
    
    # Base case - sum found!
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    # Recurrence relation
    for num in nums:
        remainder = target - num
        if can_sum(remainder, nums):
            memo[target] = True  # Notice we just save the return values
            return True  # This is a common pattern in memoization!

    memo[target] = False
    return False
