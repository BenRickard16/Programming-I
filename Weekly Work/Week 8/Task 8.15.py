import numpy as np

a = np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
b = a.sum(0)
c = a.sum(1)

print(b,c)