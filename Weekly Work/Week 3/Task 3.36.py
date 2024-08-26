def grid(a, b, npoints):
    nlist = []
    step = (b-a)/(npoints-1)
    for i in range (0, npoints):
        nlist = nlist + [a + (i*step)]
    return nlist
    
print(grid(-1,1,4))