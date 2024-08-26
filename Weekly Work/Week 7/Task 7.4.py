def f(x):
    val = x**2 - 2
    return val
    

a = 1
b = 2
m = 1
while abs(a-b) > 1e-15:
    m = (a + b)/2
    if f(m) > 0:
        b = m
    else:
        a = m

fstr = '{:.15g}'
print(fstr.format(m))   

def g(x):
    val = x**3 - 2
    return val
    
c = 1
d = 1.5
n = 1
while abs(c-d) > 1e-10:
    m = (c + d)/2
    if g(n) > 0:
        d = n
    else:
        c = n

fstr = '{:.15g}'
print(fstr.format(n))   
