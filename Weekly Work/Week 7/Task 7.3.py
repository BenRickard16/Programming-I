from math import exp

def f(x):
    val = exp(-x) - (1/2)
    return val
    

a = 0
b = 1
m = 1
n = 0
while abs(a-b) > 1e-15:
    m = (a + b)/2
    if f(m) > 0:
        a = m
        n = n + 1
    else:
        b = m
        n = n + 1


print("a equals", a,
      "b equals", b,
      "the solution equals", m,
      "and the output of the solution is", f(m),
      n)