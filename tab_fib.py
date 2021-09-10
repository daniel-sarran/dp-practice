"""
fib(6) -> 8

With tabulation, instead of recursion + memoization, we use a table.

      0 1 2 3 4 5 6
array

(length of 7)

Each subproblem represents a position of the array.
Initialize with 0. Fibonacci requires a sum, and 0 is a great value to add 
on. 

We should also "seed" the initial values.

e.g. fib of 0 is 0. fib of 1 is 1

      0 1 2 3 4 5 6
array 0 1 0 0 0 0 0

Now need to go back to definition of Fibonacci. Take a value and add it to
the next two positions.

so at Index 0, we add arr[0] to arr[1] and arr[2]

      0 1 2 3 4 5 6
array*0 1 0 0 0 0 0
        +0+0

Index 1:
      0 1 2 3 4 5 6
array 0*1 1 1 0 0 0
          +1+1

Index 2:

      0 1 2 3 4 5 6
array 0 1*1 2 1 0 0
            +1+1

Index 3:

      0 1 2 3 4 5 6
array 0 1 1 2*3 5 3
                +3+3

Index 3:

      0 1 2 3 4 5 6
array 0 1 1 2 3*5 8   (note on the last iteration, we only add to 1 index)
                  +5

We only iterate through array of size n, so this is a linear O(n) solution.
Note that although different from recursive solution, logic carries over.
Still using overlapping subproblems.
Each index in the array represents a call on fib(n) for index n.

So our array is basically

array fib(0) fib(1) fib(2) fib(3) fib(4) fib(5) fib(6)
"""


def fib(n):
    table = [0 for _ in range(n + 1)]
    table[1] = 1

    for i in range(n):
        table[i + 1] += table[i]
        if i + 2 < len(table):
            table[i + 2] += table[i]

    return table[n]


if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
