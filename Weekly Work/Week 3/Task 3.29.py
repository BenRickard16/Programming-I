def hailstones_seq(n):
    lst = []
    while n > 1:
        if n%2 == 0:
            n = n//2
            lst = lst + [n]
        else:
            n = 3*n+1
            lst = lst + [n]
    return lst
            
print(hailstones_seq(3))
