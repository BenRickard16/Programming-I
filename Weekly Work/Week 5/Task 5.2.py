def quadeval(a,x):
    terms =  [ a[i]*x**i for i in range(3) ]
    return sum(terms)

def grid(a, b, npts):
    lst = []
    step = (b-a)/(npts-1)
    for i in range (0, npts):
        lst = lst + [a + i*step]
    return lst

lst1 = grid(-2,2,50)
y = [quadeval([-1,-2,3],i) for i in lst1]

print(y)

