from math import factorial, pi
from matplotlib import pyplot as plt

def sintn(x,n):
    lst = []
    sm = 0
    for i in range(1,n+1):
        c = ((x**(2*i-1))*(-1)**(i-1))/factorial(2*i-1)
        lst.append(c)
    for i in range(len(lst)):
        sm = sm + lst[i]
    return sm

print(sintn(2,3))


startx = -pi
endx = pi
nx = 20

deltax = (endx-startx)/(nx-1)
xlst = [startx + i*deltax for i in range(nx)]
ylst1 = [sintn(x,1) for x in xlst]
ylst2 = [sintn(x,2) for x in xlst]
ylst3 = [sintn(x,3) for x in xlst]
ylst4 = [sintn(x,4) for x in xlst]
ylst5 = [sintn(x,5) for x in xlst]

plt.plot(xlst, ylst1, '-o')
plt.plot(xlst, ylst2, '-o')
plt.plot(xlst, ylst3, '-o')
plt.plot(xlst, ylst4, '-o')
plt.plot(xlst, ylst5, '-o')

plt.show()
