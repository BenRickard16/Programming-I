def is_perfect(n):
    lst = []
    val = 0
    for i in range (1, n+1):
        if n%i == 0:
            lst = lst +[i]
    m = len(lst)
    for j in range (0, m-1):
        val = val + lst[j]
    if val == lst[m-1]:
        return True
    else:
        return False
    
print(is_perfect(28))
n = 1
while True:
    if is_perfect(n) == True:
        print(n, 'is a perfect number')
    n = n+1
    
