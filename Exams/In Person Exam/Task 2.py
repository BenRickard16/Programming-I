def polyint(p):
    q = [0]
    for i in range(len(p)):
        q.append(p[i]/(i+1))
    return q

print(polyint([4,6,-9,2,-1,6]))
        