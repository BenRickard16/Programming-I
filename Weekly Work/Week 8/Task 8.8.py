import numpy as np
from matplotlib import pyplot as plt
from math import factorial

def sintn(x,n):
    lst = []
    sm = 0
    for i in range(1,n+1):
        c = ((x**(2*i-1))*(-1)**(i-1))/factorial(2*i-1)
        lst.append(c)
    for i in range(len(lst)):
        sm = sm + lst[i]
    return sm

x = np.linspace(-1*np.pi, np.pi, 100)
plt.plot(x, sintn(x,1))
plt.plot(x, sintn(x,2))
plt.plot(x, sintn(x,3))
plt.plot(x, sintn(x,4))
plt.plot(x, sintn(x,5))
plt.plot(x, sintn(x,6))
plt.gca().set_ylim(-2,2)
plt.gca().set_xlim(-2*np.pi, 2*np.pi)
plt.show()

