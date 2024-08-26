def zeta(s,n):
    val = 0
    for i in range(1,n+1):
        val += i**(-s)
    return val

print(zeta(1,10))