def hailstones(n):
    s = 0
    n=1
    while n in range (2,101):
        s = s+1
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        return s
    print(n,s)
    n = n+1
    
print(hailstones(2))
