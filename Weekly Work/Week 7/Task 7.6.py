from math import exp
def f(x):
    val = exp(-x) - (x)
    return val
        
def bisect(f,a,b,eps):
    m = 1
    if f(a) > 0 and f(b) < 0:
        while abs(a-b) > eps:
            m = (a + b)/2
            if f(m) > 0:
                a = m
            else:
                b = m
    else:
        while abs(a-b) > eps:
            m = (a + b)/2
            if f(m) > 0:
                b = m
            else:
                a = m
    return m

x = bisect(f, 0, 1, 1e-15)
print(x)
