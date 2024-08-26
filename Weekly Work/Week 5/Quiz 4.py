def lcvec3(x,y):
    z = []
    for i in range (0, len(x)):
        j = x[i]**2 - 2*y[i]
        z.append(j)
    return z

print(lcvec3([3,-2,3,0],[4,-5,6,-2]))