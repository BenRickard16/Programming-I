def cmult(w,z):
    x = w[0] * z[0] - w[1] * z[1]
    y = w[0] * z[1] + w[1] * z[0]
    return [x,y]


def csetmut(lst):
    w = lst[0]
    z = lst[1]
    val = cmult(w,z)
    i = 2
    while i < len(lst):
        val = cmult(val,lst[i])
        i = i +1
    return val

print(csetmut([[1,2],[-1,3],[4,-3],[5,-2],[-12,30]]))