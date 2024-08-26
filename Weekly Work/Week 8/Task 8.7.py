import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0.0, 2*np.pi, 100)
plt.gca().set_aspect('equal')
plt.plot(np.cos(t) + np.cos(5*t), np.sin(t) + np.sin(5*t))
plt.show()