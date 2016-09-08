from math import sqrt
import random

def FindFactors(n):

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n/2

    i = 3
    max_factor = sqrt(n)
    while i <= max_factor:
        while n % i == 0:
            factors.append(i)
            n = n/i
            max_factor = sqrt(n)
        i = i + 2
    if n > 1:
        factors.append(n)
    return factors



print FindFactors(random.randint(1, 100000))
