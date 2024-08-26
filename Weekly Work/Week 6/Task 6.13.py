from matplotlib import pyplot as plt

def fib(n):
    lst = [1,1]
    for i in range (2,n):
        i = lst[i-1] + lst[i-2]
        lst.append(i)
    return lst

print(fib(20))





