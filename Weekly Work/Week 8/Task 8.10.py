import numpy as np
from matplotlib import pyplot as plt
from math import e, cos, sin

def deriv(f, x, h):
    return ( f(x + h) - f(x) ) / h 


def h(n):
    return np.e**((np.sin(n))/(n**3+1))


x = np.linspace(-5, 15, 10000)
plt.plot(x, h(x))
plt.plot(x, deriv(h, x, 0.01))
plt.gca().set_ylim(-2,20)
plt.show()
