from matplotlib import pyplot as plt

def is_mandelbrot(c):
    z = c
    for niter in range(1000): # 1000 is 'forever'
        z = z*z + c
        if abs(z) > 500:      # |z| > 500 goes to infinity
            return False
    return True


from random import random
x = [random()*2 - 1 for i in range(10000)]
y = [random()*3 - 1 for i in range (10000)]
i = 1
z = [x[i] + y[i]*1j for i in range(len(x))]
print(x,y)

xlst = []
ylst = []
for i in range(len(x)):
    if is_mandelbrot(z[i]) == True:
        xlst.append(x)
        ylst.append(y)

plt.plot(xlst, ylst, '-+')
plt.show()
