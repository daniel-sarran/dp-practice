"""
can_construct()
    receives a target string
    and an array of strings
    returns a boolean indicating whether or not the `target` can be
        constructed by concatenating elements of the `word_bank` array.
        We can reuse word bank elements as we see fit.

example:
>>> can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])
True
    (abc + def)

>>> can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])
False
    (we can get close but can never quite create 'skateboard'

>>> can_construct('', ['cat', 'dog', 'mouse'])
True
    (we can create empty string from zero words)

Visualize as a tree:

                    start with target
                        'abcdef'
                'ab'  / 'abc' |  'cd' \ DONT TAKE FROM MIDDLE!
                    /         |        \
                'cdef'      'def'       'abef' no because creating new adjacencies


                    start with target
                        'abcdef'
                'ab'  / 'abc' |  'abcd' \
                    /         |          \
                'cdef'      'def'       'ef' can't proceed from here
              'cd' |    'def' |
                   |          |
                 'ef'        '' job done TRUE

            Empty string should return true, we have achieved the target.
            A substring with no match should return false.
            True/False will bubble up the call stack, and if there is any
            true value, we should return true.

            COMPLEXITY

            single letters in word bank are almost worst case scenario
            they'll make a very tall tree because target does not reduce
            in size by very much.

            m = target length
            n = word bank length

            1. determine height of tree
            m, or target length should be the height

            2. determine branching factor
            this is some relation on n
            in worst case every prefix matches the target prefix

            that means you would branch by n prefixes each time
            at a height of m

            time: O(n ^ m) Wait -- what about any built-ins or 'hidden' costs?
                           slicing would contribute to complexity, at most m
                           times
                  O(n ^ m * m) the slicing doesn't matter as much because the
                    bottleneck is O(n^m)

            space: should be height of this tree, because when we get to the
            bottom of the tree, we would remove frames from the call stack
                  O(m) Wait -- what about those slices?
                        Each of m stack frames will need to store a string of
                        length m
                  O(m) call stack * O(m) slice
                  O(m ^ 2)

            Now, what about optimization. Are there any duplicate subtrees?
            Yes - so we can use memoization.

            MEMOIZED COMPLEXITY

            Time: O(n * m * m)
                    n is target - branching factor
                    m is height of tree
                    m is slice

"""


# def can_construct(target: str, word_bank: list) -> bool:
#     if target == '':
#         return True
#
#     # now make a choice based on words in word bank
#     for prefix in word_bank:
#
#         # when is it okay to make recursive call using that word
#         # word should be a PREFIX of the target
#         if len(prefix) > len(target):
#             continue
#
#         match = True
#         for i, char in enumerate(prefix):
#             if char != target[i]:
#                 match = False
#         if match:
#             suffix = target[len(prefix):]
#             if can_construct(suffix, word_bank):
#                 return True
#
#     return False

def can_construct(target: str, word_bank: list, memo=None) -> bool:
    if memo is None:  # establish our memo
        memo = {}

    if target in memo:  # we add our memo base case check
        return memo[target]  #

    if target == '':
        return True

        # now make a choice based on words in word bank
    for prefix in word_bank:

        # when is it okay to make recursive call using that word
        # word should be a PREFIX of the target
        if len(prefix) > len(target):
            continue

        match = True
        for i, char in enumerate(prefix):
            if char != target[i]:
                match = False
        if match:
            suffix = target[len(prefix):]
            if can_construct(suffix, word_bank, memo):  # we pass in our memo

                # Remember the rule is anywhere you would have a return
                # That you store the return in your memo
                memo[target] = True
                return memo[target]

    memo[target] = False
    return False


if __name__ == '__main__':
    print(can_construct('abcdef',
                        ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard',
                        ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('enterapotentpot',
                        ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                        ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
