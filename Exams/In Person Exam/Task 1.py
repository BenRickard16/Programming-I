def sumlst(lst):
    val = 0
    i = 0
    while i<len(lst):
        val = val+lst[i]**-1
        i = i+1
    return val

def hmean(x):
    sumr = sumlst(x)
    ans = (1/(len(x))*sumr)**-1
    return ans

print(hmean([2,4,-1]))