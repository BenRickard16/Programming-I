lst1 = [0,1,2,3,4,5,6]
lst2 = [i**3 for i in lst1]
print(lst2)

lst3 = [x**(1/3) for x in lst2]
print(lst3)

lst4 = [lst2[j] for j in range (1, len(lst2)-1)]
print(lst4)

lst5 = [lst1[j] for j in range (3, len(lst1)-2)]
print(lst5)
    