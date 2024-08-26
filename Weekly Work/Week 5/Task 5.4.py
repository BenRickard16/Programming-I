def grid(a, b, npts):
    step = (b-a)/(npts-1)
    lst =[(a + i*step) for i in range (0, npts)]
    return lst

print(grid(2,24,6))