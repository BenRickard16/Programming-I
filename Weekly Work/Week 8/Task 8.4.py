import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0.0, 8*np.pi, 100)
plt.plot(x, np.sin(x))
plt.gca().set_xlim(0,8*np.pi)
plt.show()


x = np.linspace(0.0, 8*np.pi, 100)
plt.plot(x, np.sin(x))
plt.show()