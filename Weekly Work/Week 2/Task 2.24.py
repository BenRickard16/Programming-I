def gcd(p,q):
    while p != q:
        if p>q:
            p = p-q
        if q>p:
            q = q-p
    return p
print(gcd(456,123))
    