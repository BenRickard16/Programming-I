def parmean(alst):
    n = len(alst)
    s = 0
    lst = []
    for i in range(n):
        s = s + alst[i]
        lst.append(s/(i+1))
    return lst


print(parmean([1,2,3,4]))

       
        
    
    