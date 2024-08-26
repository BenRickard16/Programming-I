import numpy as np

a = np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
print(a)

print(a.ndim)
print(a.shape)

b = np.ones((2,3))
print(a+b)