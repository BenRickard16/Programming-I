lst1 = [1, -1/5]
x0 = 1
x1 = -1/5
i = 2
while len(lst1) < 50:
    x = 14/5 * lst1[i-1] + 3/5 * lst1[i-2]
    i = i +1
    lst1.append(x)



lst2 = []
for n in range(51):
    x = (-1/5)**n
    lst2.append(x)
    

lst3 = []
for i in range(len(lst1)):
    d = lst1[i] - lst2[i]
    lst3.append(d)


lst4 = []
for i in range(len(lst1)):
    re = lst1[i]/lst2[i]
    lst4.append(re)


for i in range(50):
    print(lst1[i], lst2[i], lst3[i], lst4[i])
    

    