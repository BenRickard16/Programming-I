def lsum(lst):
    val = 0
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        val = val + x
        i = i+1
    return val


print(lsum([8,10,12]))
