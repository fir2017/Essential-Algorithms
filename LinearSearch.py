############################
# Linear search
############################

from __future__ import print_function

def LinearSearch(values, target):
    for i in range(len(values)):
        if (values[i] == target):
            return i
        if (values[i] > target):
            return -1
    return -1

values = [1,2,3,4,5]
print (LinearSearch(values, 3))
