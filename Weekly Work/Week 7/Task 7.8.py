y = 5/4
x = 63/50

while abs(x-y) > 1e-5:
    y = x
    x = y - ((y**3-2)/3*y**2)


print(x)