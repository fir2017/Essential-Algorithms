import random

def RaiseToPower(A,P):

    C = 0
    if P == 0:
        return 1
    elif P%2 == 0:
        C = RaiseToPower(A, P/2)
        return C*C
    else:
        return A*RaiseToPower(A, P-1)

# test
A = float(input("Base: "))
P = int(input("Exponent: "))
print RaiseToPower(A,P)
