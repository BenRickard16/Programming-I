from matplotlib import pyplot as plt
from math import sin, pi

def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-o')
    plt.show()
    

def my_fun(x):
    y = sin(x) + sin(6**(1/2)*x)
    return y



plot_function(my_fun, 0, 4*pi, 200)

#Hence the 5th positive solution is between 6 and 7

def f(x):
    val = sin(x) + sin(6**(1/2)*x)
    return val

def equationroot():
    a = 6
    b = 7
    m = 1
    while abs(a-b) > 1e-11:
        m = (a + b)/2
        if f(m) > 0:
            a = m
        else:
            b = m
    return m


def strequationroot():
    a = 6
    b = 7
    m = 1
    while abs(a-b) > 1e-11:
        m = (a + b)/2
        if f(m) > 0:
            a = m
        else:
            b = m
    mstr = '{:.8f}'
    return mstr.format(m)

print(strequationroot())
