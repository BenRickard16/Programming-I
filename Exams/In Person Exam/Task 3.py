def sumlst(lst):
    val = 0
    i = 0
    while i<len(lst):
        val = val+lst[i]
        i = i+1
    return val

def polyint(p):
    q = [0]
    for i in range(len(p)):
        q.append(p[i]/(i+1))
    return q

def polydefint(p,a,b):
    int1 = polyint(p)
    lst1 = [int1[i]*b**i for i in range(1,len(int1))]
    lst2 = [int1[i]*a**i for i in range(1,len(int1))]
    val1 = sumlst(lst1)
    val2 = sumlst(lst2)
    ans = val1 - val2
    return ans

print(polydefint([1,-0.5,3],-1,2))