def lprod(lst):
    val = 1
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        val = val * x
        i = i+1
    return val


print(lprod([1,-2,3]))