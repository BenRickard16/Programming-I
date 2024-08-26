def tayarctan(m):
    lst = []
    for i in range(m):
        if i%2 == 0:
            i = 0.0
            lst.append(i)
        else:
            i = (-1)**((i-1)/2)*(1/i)
            lst.append(i)
    return lst


        
def parsumarctan(n,x):
    lst = tayarctan(n)
    for j in range(n+1):
        lst[j] = x**j*lst[j]
    lst2 = []
    sum = 0
    for i in range(n+1):
        sum = sum + lst[i]
        lst2.append(sum)
    return lst2

print(parsumarctan(7,2))
        
            
        