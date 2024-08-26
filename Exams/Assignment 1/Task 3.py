def containsmultipleofn(lst,n):
    for i in range(len(lst)):
        if lst[i]%n != 0:
            i = i + 1
            val = False
        else:
            return True
    return val

print(containsmultipleofn([4,9,12,-2,6],7))
        