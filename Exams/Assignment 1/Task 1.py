def fermat(a,b,n):
    val = (a**n +b**n)**(1/n)
    return val

print(fermat(3,4,3))
