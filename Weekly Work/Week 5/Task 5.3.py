x = [i**2 for i in range(11)]

print(x)

def proot(n,p):
    lst = [i**(1/p) for i in range(n+1)]
    return lst

print(proot(27,3))