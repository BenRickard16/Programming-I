from math import sin
from matplotlib import pyplot as plt

def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, 'r-o')
    plt.show()
    

def my_fun(x):
    y = sin(x)/x
    return y




plot_function(my_fun, 0.1, 8, 20)