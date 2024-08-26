from math import e
from matplotlib import pyplot as plt

def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-')
    plt.axhline(0)
    plt.show()
    


def my_fun(x):
    y = e**(-x) - 1/2
    return y



plot_function(my_fun, 0.69314, 0.69315, 2000)