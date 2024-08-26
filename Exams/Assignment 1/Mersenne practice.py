def mprimes_in(lst):
    mlist = []
    plst = [2,3,5,7]
    n = 1
    i = 0
    while i < len(plst):
        while n < 3:
            if 2**n == (plst[i]+1):
                mlist.append(plst[i])
            n = n+1
            i = i+1
    return mlist

print(mprimes_in([2,3,5,7]))