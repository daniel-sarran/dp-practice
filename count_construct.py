"""
count_construct(target, word_bank)
    accepts a target string
    accepts an array of strings

    returns `the number of ways` that the `target` can be constructed by
    concatenating elements of the `word bank` array

    You may reuse elements of `word bank` as many times as needed

example:
    count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) => 1

                        Start with your target
                                'abcdef'
                            /           |             \
                    -'ab'            -'abc'             -'abcd'
                    'cdef'          'def'               'ef'
                        |               |               stop
                    -'cd'           -'def'
                    'ef'            ''
                    stop            target reached


    each time the empty string is reached, 1 is bubbled up to base stack frame
    and if a dead end, 0 is bubbled up
"""


def count_construct(target: str, word_bank: list, memo=None) -> int:
    # BRUTE FORCE
    # if target == '':
    #     return 1
    #
    # total_count = 0
    #
    # for prefix in word_bank:
    #
    #     if len(prefix) > len(target):
    #         continue
    #
    #     match = True
    #     for i, char in enumerate(prefix):
    #         if char != target[i]:
    #             match = False
    #
    #     if match:
    #         num_ways_for_rest = count_construct(target[len(prefix)], word_bank)
    #         total_count += num_ways_for_rest
    #
    # return total_count

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == '':
        return 1

    total_count = 0

    for prefix in word_bank:

        if len(prefix) > len(target):
            continue

        match = True
        for i, char in enumerate(prefix):
            if char != target[i]:
                match = False

        if match:
            num_ways_for_rest = count_construct(target[len(prefix):],
                                                word_bank,
                                                memo)
            total_count += num_ways_for_rest

    memo[target] = total_count
    return memo[target]


if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                          ['e', 'ee', 'eee', 'eeee', 'eeeee']))
