############################
# Binary search
############################

from __future__ import print_function

def BinarySearch(values,target):
    min = 0
    max = len(values) - 1

    while (min <= max):
        mid = (min + max) / 2
        if (target < values[mid]):
            max = mid - 1
        elif (target > values[mid]):
            min = mid + 1
        else:
            return mid
    return -1


values = [1,2,3,4,5]
print (BinarySearch(values, 3))
