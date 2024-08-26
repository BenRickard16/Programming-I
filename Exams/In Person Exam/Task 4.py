from math import sqrt

def lmin(lst):
    val = lst[0]
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        if x<val:
           val = x
        i = i+1
    return val

def dynlist(y0, a, M):
    lst = [y0]
    n = 0
    s = 0
    while lmin(lst) >= a and len(lst) < M:
        for i in range(len(lst)):
            n = sqrt(lst[s]-a)
            lst.append(n)
            s = s + 1
    return lst


print(dynlist(1.5,0.5,10))


