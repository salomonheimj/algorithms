# Binary search according to grooking
from tracemalloc import take_snapshot


def binary_search(list, item):
    # low and high keep track of which part of the list we are searching
    low = 0
    high = len(list) - 1

    # while we haven't narrow down to one element
    while low <= high:
        # check the middle element
        # // is necessary and not only / since for python3, // indicates floor division, / indicates true division --> return s a float
        mid = (low + high) // 2
        guess = list[mid]

        # found the item
        if guess == item:
            return mid

        # guess too high
        if guess > item:
            high = mid - 1

        # guess too low
        else:
            low = mid + 1

    # the item doesn't exist
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1))
print(binary_search(my_list, -1))

# Exercises:
# 1. We have a sorted list of 128 names, with binary search, whats the maximum number of steps it would take_snapshot?
# A// 128 / 2 --> / 2 ..... 1 = 7

# 2. Suppose we double the size of the list, maximum number of steps now?
# A// 3