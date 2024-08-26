def ninsects(gen,d):
    lst = [2.0]
    for i in range(gen):
         i = ((1+0.2*d[i])*lst[i])/((1+0.3*lst[i])**(3/2))
         lst.append(i)
    return lst


print(ninsects(4, [1,2,3,4,5]))