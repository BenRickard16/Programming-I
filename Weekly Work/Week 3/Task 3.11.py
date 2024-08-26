def lmax(lst):
    val = 0
    n = len(lst)
    i = 0
    while i<n:
        x = lst[i]
        if x>val:
           val = x
        i = i+1
    return val
        
print(lmax([3,1,5,2,8,3]))
    