############################
# Interpolation search
############################

from __future__ import print_function

def InterpolationSearch(values, target):
    min = 0
    max = len(values) - 1
    while (min <= max):
        scale = (target - values[min])//(values[max] - values[min])
        mid = min + (max - min) * scale 
        if (values[mid]<target):
            min = mid + 1
        elif (values[mid]>target):
            max = mid - 1
        else:
            return mid
    return -1


values = [1,2,3,4,5]
print (InterpolationSearch(values, 3))
