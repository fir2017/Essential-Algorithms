import random


def gcd(a, b):
    count = 0
    average = float((a+b)/2)

    while b:
        a, b = b, a%b
        count += 1
    return a, count, average

print "Enter number of sets:"
n = input()
results = []
for i in range(n):
    i =  gcd(random.randint(1,10000), random.randint(1,10000))
    results.append(i)
print "(GCD, steps, average)"
print results
