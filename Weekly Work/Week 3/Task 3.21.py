def isprime(n):
    m = 2
    prime = True
    while prime and m*m<=n:
        if n%m == 0:
            prime = False
        m = m+1
    return prime

def primes_in(lst):
    plst = []
    i = 1
    n = len(lst)
    x = lst[i]
    while i < n:
        if isprime(i) == True:
            plst = plst + [i]
        i = i+1
    return plst

print(primes_in([1,2,3,4,5,6,7,8,9]))
            