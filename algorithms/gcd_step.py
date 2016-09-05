import random


def gcd(a, b):
    count = 0
    while b:
        a, b = b, a%b
        count += 1
        average = float((a+b)/2)
    return a, count, average

n = input()
results = []
for i in range(n):
    i =  gcd(random.randint(1,10000), random.randint(1,10000))
    results.append(i)
