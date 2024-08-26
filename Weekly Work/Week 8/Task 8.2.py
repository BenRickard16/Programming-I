import numpy as np

x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0])
print(x, type(x), x[1], x[2:4])

print(np.zeros(3))
print(np.ones(5))

print(np.linspace(0.0,2.0*np.pi,10))