def sumints(n):
    val = 0
    i = 1
    for i in range (1, n+1):
        val = val+i
        i = i+1
    return val
print(sumints(25))