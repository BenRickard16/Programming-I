def grid(a, b, npts):
    lst = []
    step = (b-a)/(npts-1)
    for i in range (0, npts):
        lst = lst + [a + i*step]
    return lst

print(grid(-1.1, 2.5, 5))