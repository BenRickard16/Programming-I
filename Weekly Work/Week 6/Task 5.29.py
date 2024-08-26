def is_in(x, lst):
    for i in range(len(lst)):
        if lst[i] != x:
            i = i + 1
            val = False
        else:
            return True
    return val
            

t1 = is_in(1,[1,4,3])
t2 = is_in(2,[1,4,3])
t3 = is_in(1.0,[1,4,3])

print(t1,t2,t3)

t1 = 1 in [1,4,3]
t2 = 2 in [1,4,3]
t3 = 1.0 in [1,4,3]
print(t1,t2,t3)
            