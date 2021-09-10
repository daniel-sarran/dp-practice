"""
SAMPLE INPUT
3
odd 2
even 3
odd 5
"""


def some_func():
    return True


# first, grab the number of queries
queries = int(input())

# Then iterate that many times running `input`
# With the format x, y, z = input().split()
# All are strings so convert to integer where needed
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        some_func()
    else:
        some_func()
