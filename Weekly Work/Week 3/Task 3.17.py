def firstnats(n):
    lst = []  
    i =  1
    while i<=n:
        # The next line of code adds i as a
        # new element at the end of lst
        lst = lst + [i] 
        i = i+1
    return lst

print(firstnats(4/2))