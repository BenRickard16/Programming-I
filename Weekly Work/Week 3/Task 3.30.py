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

hs3 = hailstones_seq(3)
for x in hs3:
    print(x)