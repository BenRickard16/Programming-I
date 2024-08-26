def prime_factors(n):
    lst = []
    m = 2
    while m<=n:
        if n%m == 0:
            lst = lst + [m]
            n = n//m
        else:
            m = m+1
    return lst

print(prime_factors(32))