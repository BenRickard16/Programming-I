def is_perfect(n):
    lst = []
    val = 0
    for i in range (1, n+1):
        if n%i == 0:
            lst.append(i)
    m = len(lst)
    for j in range (0, m-1):
        val = val + lst[j]
    if val == lst[m-1]:
        return True
    else:
        return False

y = [x for x in range(1,10000) if is_perfect(x)]
print(y)
