"""
This is coin change!

can_sum(7, [5, 3, 4]) -> True

We need to create a table. But what size? Which value contributes to our table?
If we can use the numbers any amount of time, we're not shrinking the table.
But our target, does shrink.

So we'll build a table based off of the target.
An array of size targetSum+1 (off by one).

How should we fill our table?
We return a boolean, so we should use a boolean. 
We should assume we cannot sum a target unless proven otherwise (use False).

Seed values?
Think of the base case. What about a target of 0? We can take no elements
to create that sum.

So array[0] is True.

        0 1 2 3 4 5 6 7
Array   F F F F F F F F

Take [5, 3, 4] and apply them to current case 0.
If we can do 0, we can certainly do 0 + 5, 0 + 3, 0 + 4.
So we look ahead to index 5, 3, 4, and change those to True. We can make those
sums.

        0 1 2 3 4 5 6 7
Array   F F F T T T F F
              ^ ^ ^

Then we iterate to index 1. This is False, we can't create 1 from 5, 3, 4.
So we skip this index.

Same for 2.

Then at 3, we can achieve 3, so we can add 5, 3, 4. This will take us out of
bounds so we only add indices within the array.

So our table is size m.
And for each index, how much work are we doing?
We have an outer loop to iterate through each index.
And we have an inner loop to iterate through our options.

So time complexity is O(m * n)
"""


def can_sum(target, numbers):
    # Choose table size, and fill
    table = [False for _ in range(target + 1)]

    # Seed
    table[0] = True

    for i in range(target + 1):
        # Look ahead but only if current position is True
        if not table[i]:
            continue

        # For each "coin", if the next sum (which is based on index) can be
        # made (and is in array bounds) then change those to True
        for choice in numbers:
            if i + choice > target:
                continue

            table[i + choice] = True

    return table[target]


if __name__ == '__main__':
    print(can_sum(7, [5, 3, 4]))
