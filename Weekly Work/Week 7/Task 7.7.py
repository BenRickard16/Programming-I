y = 1
x = 3/2

while abs(x-y) > 1e-15:
    y = x
    x = y/2 + 1/y


print(x)
