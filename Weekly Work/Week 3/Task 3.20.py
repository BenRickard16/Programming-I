def lsum(lst):
    val = 0
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        val = val + x
        i = i+1
    return val

def lsumsq(lst):
    val = 0
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        val = val + x**2
        i = i+1
    return val

def lmean(lst):
    val = lsum(lst)/len(lst)
    return val

def lstdev(lst):
    val = ((lsumsq(lst)/ len(lst))-lmean(lst)**2)**(1/2)
    return val