def lsqr(lst):
    val = 0
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        val = val + x**2
        i = i + 1
    return val

lst = [1,2,3]
print(lst)

lst2 = lsqr(lst)
print(lst, lst2)