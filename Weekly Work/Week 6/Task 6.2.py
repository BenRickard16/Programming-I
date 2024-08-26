from math import pi, sin
from matplotlib import pyplot as plt

nx = 20
deltax = 4*pi/(nx-1)
xlst = [ i*deltax for i in range(nx) ]
ylst = [ sin(x) for x in xlst ]
plt.plot(xlst, ylst, '-+')
plt.show()
