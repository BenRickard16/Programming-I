from math import factorial

def nchoosek(n,k):
    val = factorial(n)//(factorial(n-k)*factorial(k))
    return val

def R(n):
    lst = [nchoosek(n,k) for k in range(0,n+1)]
    sum = 0
    for i in range (0, len(lst)):
        sum = sum + lst[i]
    return sum

def S(n):
    lst = [(k*nchoosek(n,k)) for k in range(0,n+1)]
    sum = 0
    for i in range (0, len(lst)):
        sum = sum + lst[i]
    return sum

y = [R(n) for n in range(1,11)]

z = [S(n) for n in range (1,11)]

