from Fraction import Fraction


def H(n):
    val = Fraction(1,1)
    k = 2
    while k <= n:
        val = val + Fraction(1, k)
        k += 1
    return val


def T(n):
    val = Fraction(1, 2)**0
    k = 1
    while k <= n:
        val = val + (Fraction(1, 2))**k
        k += 1
    return val


def Z(n):
    val = Fraction(1, 2)**0
    k = 1
    while k <= n:
        val = val + ((Fraction(1, 2))**k)
        k += 1
    return Fraction(2,1) - val


def R(n, b):
    val = Fraction(1,1)**b
    k = 2
    while k <= n:
        val = val + (Fraction(1, k))**b
        k += 1
    return val

def checkInt():
    n = input("Enter Number of iterations (integer>0):\n")
    try:
        val = int(n)
        return val
    except ValueError:
        return checkInt()



print("Welcome to Fun with Fractions!")
n = checkInt()
    
print("H(" + str(n) + ")=" + str(H(n)))
print("H({})~={:.8f}".format(n, H(n).approximate()))

print("T(" + str(n) + ")=" + str(T(n)))
print("T({})~={:.8f}".format(n, T(n).approximate()))

print("Z(" + str(n) + ")=" + str(Z(n)))
print("Z({})~={:.8f}".format(n, Z(n).approximate()))

for i in range(2,9):
    print("R(" + str(n) + "," + str(i) + ")=" + str(R(n,i)))
    print("R({},{})~={:.8f}".format(n, i, R(n,i).approximate()))