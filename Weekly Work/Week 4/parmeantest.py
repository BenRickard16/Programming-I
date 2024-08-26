# Functions we need later
from time import time
from random import random
from sys import exit

# Generates a list of n random numbers
def rndlist(n):
    i = 0
    lst = []
    while i<n:
        lst.append(random())
        i = i+1
    return lst


# Put your parmean function here
def parmean(alst):
    n = len(alst)
    s = 0
    lst = []
    for i in range(n):
        s = s + alst[i]
        lst.append(s/(i+1))
    return lst

# Checks that it works
def parmeanOK():
    x = parmean([1, 2, 3, 1, 2, 3])
    y = [1, 1.5, 2, 1.75, 1.8, 2]
    if len(x)!=len(y):
        return False
    i=0
    diff = 0
    while i<len(y):
        diff = diff + abs(x[i]-y[i])
        i = i+1
    if diff>1e-6:
        return False
    return True

if not parmeanOK():
    print('Your parmean function does not work')
    exit()

# Tests the parmean function's efficiency by measuring the time taken
# to compute the partial means for a list with 100000 elements
x = rndlist(100000)
seconds_start = time()
y = parmean(x)
seconds_end = time()
print("duration : ", seconds_end-seconds_start)
