from math import e
from matplotlib import pyplot as plt

def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-+')
    plt.semilogy()
    plt.xlabel('number of goalkeepers')
    plt.ylabel('goals')
    plt.show()
    


def my_fun(t):
    y = e**(-t)
    return y



plot_function(my_fun, 0, 5, 20)


def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-+')
    plt.loglog
    plt.show()
    


def my_fun2(u):
    y = u**10
    return y



plot_function(my_fun2, 0, 1, 20)