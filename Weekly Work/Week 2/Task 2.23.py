def nroots(a,b,c):
    n = (b**2-4*a*c)
    if n > 0:
        return 2
    if n == 0:
        return 1
    else:
        return 0
    
print(nroots(1,5,6))