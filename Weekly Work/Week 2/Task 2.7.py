def factorial(n):
    val = 1
    i = 2
    while i<=n:
        val = val * i
        i = i+1
    return val
print(factorial(3))