import random


# string array can be initialized as a list in python,
# so input for RandomizeArray will be arr[]
def RandomizeArray(arr):
    max_i = arr[len(arr) - 1]
    for i in range(len(arr)):
        j = random.randint(i,(len(arr) - 1))
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr

# test
# arr = [2,3,4,5,6,7]
# print RandomizeArray(arr)
