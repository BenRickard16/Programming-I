from math import cos, pi
        
def bisect(f,a,b,eps):
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

x = bisect(cos, 1, 2, 1e-15)
print(x-pi/2)
        
