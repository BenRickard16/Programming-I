def f(x):
    return (10 + 2*x**2 + x**3)**-1

def lsum(lst):
    val = 0
    n = len(lst)
    i = 0
    while i<n:
        val = val + lst[i]
        i = i+1
    return val

def simpsonex(a,b,n):
    delx = (b - a)/n
    lst = [f(a + delx*i) for i in range(n+1)]
    for i in range(1,n):
        if i%2 == 0:
            lst[i] = 2*lst[i]
        else:
            lst[i] = 4*lst[i]
    integral = delx * lsum(lst)/3
    return integral
    


print(simpsonex(-3,2,6))

