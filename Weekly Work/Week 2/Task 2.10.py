for n in range (1, 1001):
    s = 0
    while n > 1:
        s = s+1
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
    return s
