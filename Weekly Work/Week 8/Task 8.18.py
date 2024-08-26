import numpy as np

M = np.array([[1.0, 2.0, 3.0], [1.0, 4.0, 5.0], [1.0, 6.0, 8.0]])
b = np.array([[1.0], [4.0], [9.0]])

ans = np.linalg.inv(M) @ b

print(ans)