def isprime(n):
    m = 2
    prime = True
    if n == 1:
        prime = False
    while prime and m*m<=n:
        if n%m == 0:
            prime = False
        m = m+1
    return prime

def primes_in(lst):
    plst = []
    i = 0
    n = len(lst)
    while i < n:
        if isprime(lst[i]) == True:
            plst.append(lst[i])
        i = i+1
    return plst

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

def fracmers(lst):
    n = len(primes_in(lst))
    m = len(mprimes_in(lst))
    val = m/n
    return val


print(fracmers([3,4,7,11]))
        
        
    