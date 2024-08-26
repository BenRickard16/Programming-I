def divisors(n):
    lst = []
    for i in range(1, n+1):
        if n%i == 0:
            lst.append(i)
    val = len(lst)
    return val

from matplotlib import pyplot as plt

nx = 251
xlst = [ i for i in range(nx) ]
ylst = [ divisors(x) for x in xlst ]
plt.plot(xlst, ylst, '-+')
plt.show()





            
    