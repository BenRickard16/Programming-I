import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.plot(x, np.sin(x)**2)
plt.plot(x, np.cos(x))
plt.gca().set_ylim(-3,2)
plt.show()