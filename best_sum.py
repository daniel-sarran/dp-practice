"""
This time, we need an optimization. 
We need the smallest number of values which reaches the target.

best_sum(8, [2, 3, 5]) => [3, 5] *Not [2, 2, 2, 2]

1. Visualize recurrence relations as a tree

                8
         /      |      \
        6       5        3
       /|\     /|\      /|
      4 3 1   3 2 8    1 0 
    // /\    // |
   2 1 1 0  1 0 0
  /
 0

    Complexity PRE MEMOIZATION
    
    m is target sum
    n is array length

    time: exponential - branching factor to the height power
          O(n ^ m)

    space: O(m)? Wait, think about this - it will be at least m size
                 But what about shortest? Shortest is a new array on each
                 stack frame.
                 There are at most m stack frames, each with a size m array

            O(m ^ 2)

    MEMOIZED complexity
    Time - no longer exponential
            no longer looking at full duplicate subtrees
            but still have to branch for each number in array

            O(m * n * m)
                m is target
                n is branching (array length)
                m is copying list over for memo

"""


def best_sum(target, arr, memo=None):
    if memo is None:  # Optimization
        memo = {}  #

    if target in memo:  #
        return memo[target]  #

    if target == 0:
        return []

    if target < 0:
        return None

    shortest = None

    for val in arr:
        remainder = target - val
        remainder_sum = best_sum(remainder, arr, memo)

        if remainder_sum is not None:
            new_rem = list(remainder_sum)
            new_rem.append(val)

            if shortest is None or len(new_rem) < len(shortest):
                shortest = new_rem

    memo[target] = shortest
    return memo[target]


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
