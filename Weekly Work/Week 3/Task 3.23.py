def distn(p1,p2):
    n = len(p1)
    i = 0
    val = 0
    while i < n:
        l = p1[i] - p2[i]
        val = val + l**2
        i = i+1
    return val**0.5

print(distn([1,0,3,-1],[-2,4,5,1]))
