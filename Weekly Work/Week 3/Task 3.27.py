def lmedian(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 1:
        m = lst[(n+1)/2]
    else:
        m = (lst[n//2-1]+lst[n//2])/2
    return m
    
    
print(lmedian([10,6,4,6,8,1]))