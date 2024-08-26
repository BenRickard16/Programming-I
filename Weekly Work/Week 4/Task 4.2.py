def divisors(n):
    lst = []
    for i in range (1, n+1):
        if n%i == 0:
            lst = lst +[i]
    return lst

print(divisors(8))