s = [1]
t = [2,s]
u = t[:]

print(t,u)

from copy import deepcopy
s = [1]
t = [2,s]
u = deepcopy(t)
s.append(3)

print(t,u)