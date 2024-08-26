from math import pi, sin, cos
from matplotlib import pyplot as plt

nx = 200
deltax = 4*pi/(nx-1)
xlst = [ i*deltax for i in range(nx) ]
ylst = [ sin(x) for x in xlst ]
ylst2 = [ cos(x) for x in xlst ]
ylst3 = [ sin(x)**2 for x in xlst ]
plt.plot(xlst, ylst, '-+')
plt.plot(xlst, ylst2, 'r-+')
plt.plot(xlst, ylst3, 'g-+')
plt.show()



