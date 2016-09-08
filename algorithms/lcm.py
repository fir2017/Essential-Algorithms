def gcd(a, b):
    while b !=0:
        a, b = b, a%b
    return a

def lcd(a, b):
    product = a*b
    return (a*b)/gcd(a,b)

# test
print "Enter integer 1: "
a = input())
print "Enter integer 2: "
b = input()

print lcd (a,b)
