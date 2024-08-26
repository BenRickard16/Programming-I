def listcalc(mylist):
    i = 0
    val = 0
    n = len(mylist)
    for i in range(n):
        if mylist[i]%2 == 1:
            val = val + mylist[i]
    return val

print(listcalc([12,2,6,50,4]))