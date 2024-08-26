def vadd(v1,v2):
    v = [v1[i] + v2[i] for i in range(len(v1))]
    return v

def vdot(v1,v2):
    l = [v1[i] * v2[i] for i in range(len(v1))]
    val = 0
    for j in range(len(v1)):
        val = val + l[j]
    return val

def vsmul(v,x):
    b = [v[k] * x for k in range(len(v))]
    return b

