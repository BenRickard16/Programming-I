def isprime(n):
    m = 2
    prime = True
    while prime and m*m<=n:
        if n%m == 0:
            prime = False
        m = m+1
    return prime
    

def primes_up_to(n):
    lst = []  
    i =  1
    while i<=n:
        if isprime(i) == True:
            lst = lst + [i] 
        i = i+1
    return lst

print(primes_up_to(20))
