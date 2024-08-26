import numpy as np

a = np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])

w = a[0,1]
x = a[0:1,1]
y = a[0,1:2]
z = a[0:1,1:2]

print(w, w.ndim, w.shape)
print(x, x.ndim, x.shape)
print(y, y.ndim, y.shape)
print(z, z.ndim, z.shape)
