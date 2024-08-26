import numpy as np
from matplotlib import pyplot as plt

def deriv(f, x, h):
    return( f(x + h) - f(x) ) / h



x = np.linspace(0, np.pi, 100)
plt.plot(x, np.sin(x))
plt.plot(x, deriv(np.sin, x, 0.1))
plt.plot(x, np.cos(x))
plt.show()


