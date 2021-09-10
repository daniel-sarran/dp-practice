"""
So this is a different problem because we don't need to know IF we can make
a sum, we need to know HOW.

WHICH coins do you use to reach a specified change?

how_sum(7, [5, 3, 4]) -> [4, 3]

So again, we make our table.
1) How to size?
    At worst 7 is the changing/shrinking problem.
    So we size at length 8, so that our index 7 matches up to target 7,
    while also allowing trivial case 0.

2) How to fill?
    Well, what do we return if we can't make change?

how_sum(1, [5, 3, 4]) -> null

    Okay, so we fill our table with null values.

3) How to seed?
    What is the trivial case? Probably 0.
    If we have a quantity of 0, we can simply take no coins.

how_sum(0, [5, 3, 4]) -> []

    Okay, so 0th index will have an empty array.

        0   1    2    3    4    5    6    7
Array   []  none none none none none none none


Okay so we start at 0. We don't need any coins.
If we go through each coin, what change can we make?
From options 5, 3, 4 -- we can make 5, 3, 4
        0   1    2    3    4    5    6    7
Array   []  none none [3]  [4]  [5] none none
        ^

Index 1. We cannot make change for 1. So we skip.
        0   1    2    3    4    5    6    7
Array   []  none none [3]  [4]  [5] none none
            ^

Index 2. We cannot make change for 1. So we skip.
        0   1    2    3    4    5    6    7
Array   []  none none [3]  [4]  [5] none none
                 ^

Index 3. We CAN make change here. So we update 5, 3, and 4 moves ahead.
        0   1    2    3    4    5    6    7
Array   []  none none [3]  [4]  [5] [3,3] [3,4]
                       ^
                       Now technically here we've completed, but we're okay
                       to simply complete until the end. That will update
                       index 7 when we get to index 4, because 4 + 3 will
                       create change for 7.
                       This will change [3,4] to [4,3]. That's fine.

Time complexity - we need to go through M table values
    At each table value, I need to do N operations
    So, that is O(m * n).
    In addition, in worst case our coins have a "1" option. That means we will
    need a final array of all "1s" which will be m values which will require m 
    time complexity.
    >>> O(m^2 * n)

Space complexity - initial size of table is m. However each quantity will have
    its own table. So in the end we could have up to m elements in an m sized
    table.
    >>> O(m^2)
    We're actually happy with this. It's in polynomial time not exponential.
"""


def how_sum(target, numbers):
    # Size and fill table
    table = [None for _ in range(target + 1)]

    # Seed table
    table[0] = []

    for i in range(target + 1):
        if table[i] is None:
            continue

        for choice in numbers:
            if i + choice > target:
                continue

            way = []
            way.extend(table[i])
            way.append(choice)
            table[i + choice] = way

    return table[target]


if __name__ == '__main__':
    print(how_sum(7, [5, 3, 4]))
