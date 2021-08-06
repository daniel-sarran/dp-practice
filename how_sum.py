"""
how_sum(8, [2, 3, 5]) => [3, 5]

how_sum(7, [2, 4]) => None

how_sum(0, [1, 2, 3]) => how is target sum of zero trivially solved?
                      => []

example:
    how_sum(7, [5, 3, 4, 7])

                   7
            -5  -3  -4  -7
            2   4   3   0

            2 can't go further - should return null
            4 will lead to a valid sum
            3 will also lead to a valid sum
            7 already has reached target

            so these return values should return to parent, where the parent
            should also append itself to the value

            4 could subtract 3, so now the target is 1, which leads to null
            but 4 will lead to target reached

            so the parent will need to accept null and arrays
            and the array needs to override the null

            so combinations are encoded as a path of edges

    say m is target sum
    and n is array length

    Time: O(n^m)
    Space: O(m) - stack space, also the array returned which is also m-size

    MEMOIZED version:
    Time: O(n*m)
    Space: O(m)? Wait, consider the MEMO object.
            Maximal length of any array is length m
            There are m keys
            So m keys * m length array
"""
#def how_sum(target, arr):
#    if target == 0:
#        return []
#    
#    if target < 0:
#        return None
#
#    # branching logic for recursive calls
#    for val in arr:
#        remainder = target - val
#        result = how_sum(remainder, arr)
#        if result != None:
#            result.append(val)
#            return result
#
#    return None
#

def how_sum(target, arr, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []
    
    if target < 0:
        return None

    # branching logic for recursive calls
    for val in arr:
        remainder = target - val
        result = how_sum(remainder, arr, memo)
        if result != None:
            result.append(val)
            memo[target] = result
            return memo[target]

    memo[target] = None
    return None

if __name__ == '__main__':
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))


