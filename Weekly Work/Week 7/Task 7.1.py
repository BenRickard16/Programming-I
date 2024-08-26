x, y, z = 0.1, 0.2, 0.3
print(x)
print(y)
print(z)
print(x+y-z)
print((x+y)-z,x+(y-z))
print((x+y)*z == x*z + y*z)


eps = 1e-15
closeto0 = abs(x+y-z) < eps
print(closeto0)

y = z-y
print(abs(x-y) < eps)